#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <numeric>
#include <vector>

static bool primitive(const std::vector<int>& q) {
    const int n = static_cast<int>(q.size());
    for (int p = 1; p < n; ++p) {
        if (n % p != 0) continue;
        bool period = true;
        for (int i = p; i < n; ++i) {
            if (q[i] != q[i % p]) { period = false; break; }
        }
        if (period) return false;
    }
    return true;
}

// Maximum integer exponent at the cut immediately before q[cut], allowing
// only roots shorter than the primitive circular word q.
static int proper_cyclic_curl(const std::vector<int>& q, int cut) {
    const int n = static_cast<int>(q.size());
    int best = 1;
    for (int p = 1; p < n; ++p) {
        int copies = 1;
        while (copies * p < p + n - std::gcd(p, n)) {
            bool equal = true;
            for (int j = 0; j < p; ++j) {
                const int a = (cut - (copies + 1) * p + j) % n;
                const int b = (cut - p + j) % n;
                if (q[(a + n) % n] != q[(b + n) % n]) {
                    equal = false;
                    break;
                }
            }
            if (!equal) break;
            ++copies;
        }
        if (copies > best) best = copies;
    }
    return best;
}

int main(int argc, char** argv) {
    if (argc < 2 || argc > 3) {
        std::cerr << "usage: search_cyclic_fixed LENGTH [MAX_SYMBOL]\n";
        return 2;
    }
    const int n = std::atoi(argv[1]);
    const int max_symbol = argc == 3 ? std::atoi(argv[2]) : 3;
    if (n <= 0 || max_symbol < 2) return 2;
    const std::uint64_t radix = static_cast<std::uint64_t>(max_symbol - 1);
    std::uint64_t count = 1;
    for (int i = 0; i < n; ++i) {
        if (count > std::numeric_limits<std::uint64_t>::max() / radix) return 2;
        count *= radix;
    }
    std::uint64_t found_words = 0;
    for (std::uint64_t code = 0; code < count; ++code) {
        std::uint64_t x = code;
        std::vector<int> q(n);
        for (int i = 0; i < n; ++i) {
            q[i] = 2 + static_cast<int>(x % radix);
            x /= radix;
        }
        if (!primitive(q)) continue;
        bool fixed = true;
        for (int cut = 0; cut < n; ++cut) {
            if (proper_cyclic_curl(q, cut) != q[cut]) {
                fixed = false;
                break;
            }
        }
        if (!fixed) continue;
        ++found_words;
        std::cout << "word=";
        for (int x : q) std::cout << x;
        std::cout << "\n";
    }
    std::cout << "length=" << n << " found_words=" << found_words << "\n";
}
