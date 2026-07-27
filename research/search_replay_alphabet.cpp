#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

static int cn(const std::vector<int>& w) {
    const int n = static_cast<int>(w.size());
    int best = 1;
    for (int p = 1; p <= n / (best + 1); ++p) {
        int copies = 1;
        while ((copies + 1) * p <= n) {
            bool same = true;
            int a = n - (copies + 1) * p, b = n - p;
            for (int j = 0; j < p; ++j) {
                if (w[a + j] != w[b + j]) {
                    same = false;
                    break;
                }
            }
            if (!same) break;
            ++copies;
        }
        best = std::max(best, copies);
    }
    return best;
}

static bool primitive(const std::vector<int>& w) {
    int n = static_cast<int>(w.size());
    for (int p = 1; p <= n / 2; ++p) {
        if (n % p) continue;
        bool ok = true;
        for (int i = p; i < n; ++i) {
            if (w[i] != w[i % p]) {
                ok = false;
                break;
            }
        }
        if (ok) return false;
    }
    return true;
}

static bool replay(const std::vector<int>& q) {
    if (!primitive(q)) return false;
    int n = static_cast<int>(q.size());
    std::vector<int> s = q;
    s.reserve(3 * n);
    for (int d = 0; d < 2 * n; ++d) {
        int want = q[d % n];
        if (cn(s) != want) return false;
        s.push_back(want);
    }
    return true;
}

int main(int argc, char** argv) {
    if (argc != 3) return 2;
    int n = std::stoi(argv[1]), alphabet = std::stoi(argv[2]);
    std::uint64_t total = 1;
    for (int i = 0; i < n; ++i) total *= alphabet;
    std::uint64_t found = 0;
    for (std::uint64_t code = 0; code < total; ++code) {
        std::uint64_t x = code;
        std::vector<int> q(n);
        for (int i = 0; i < n; ++i) {
            q[i] = 2 + static_cast<int>(x % alphabet);
            x /= alphabet;
        }
        if (q[0] != 2 || !replay(q)) continue;
        ++found;
        if (found <= 30) {
            for (int a : q) std::cout << a;
            std::cout << "\n";
        }
    }
    std::cerr << "n=" << n << " alphabet=" << alphabet
              << " total=" << total << " found=" << found << "\n";
}
