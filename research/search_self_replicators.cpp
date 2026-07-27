#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>

static int curling_number(const std::vector<int>& word) {
    const int n = static_cast<int>(word.size());
    int best = 1;
    for (int p = 1; p <= n / 2; ++p) {
        int copies = 1;
        int cursor = n - 2 * p;
        while (cursor >= 0) {
            bool equal = true;
            for (int j = 0; j < p; ++j) {
                if (word[cursor + j] != word[n - p + j]) {
                    equal = false;
                    break;
                }
            }
            if (!equal) break;
            ++copies;
            cursor -= p;
        }
        if (copies > best) best = copies;
    }
    return best;
}

static bool primitive(const std::vector<int>& word) {
    const int n = static_cast<int>(word.size());
    for (int p = 1; p < n; ++p) {
        if (n % p != 0) continue;
        bool power = true;
        for (int i = p; i < n; ++i) {
            if (word[i] != word[i % p]) {
                power = false;
                break;
            }
        }
        if (power) return false;
    }
    return true;
}

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "usage: search_self_replicators LENGTH\n";
        return 2;
    }
    const int n = std::atoi(argv[1]);
    if (n <= 0 || n >= 63) {
        std::cerr << "LENGTH must lie in [1,62]\n";
        return 2;
    }

    const std::uint64_t count = std::uint64_t{1} << n;
    std::uint64_t found = 0;
    for (std::uint64_t bits = 0; bits < count; ++bits) {
        std::vector<int> root;
        root.reserve(3 * n);
        for (int i = 0; i < n; ++i) root.push_back(2 + ((bits >> i) & 1));
        if (root[0] != 2 || !primitive(root)) continue;

        bool matches = true;
        for (int step = 0; step < 2 * n; ++step) {
            const int value = curling_number(root);
            if (value != root[step % n]) {
                matches = false;
                break;
            }
            root.push_back(value);
        }
        if (!matches || curling_number(root) != 3) continue;

        ++found;
        std::cout << "root=";
        for (int i = 0; i < n; ++i) std::cout << root[i];
        std::cout << "\n";
    }
    std::cout << "length=" << n << " found=" << found << "\n";
    return 0;
}
