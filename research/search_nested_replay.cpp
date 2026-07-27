#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

static int cn(const std::vector<int>& w) {
    const int n = static_cast<int>(w.size());
    int best = 1;
    for (int p = 1; p <= n / (best + 1); ++p) {
        int copies = 1;
        while ((copies + 1) * p <= n) {
            bool same = true;
            const int a = n - (copies + 1) * p;
            const int b = n - p;
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
    const int n = static_cast<int>(w.size());
    for (int p = 1; p <= n / 2; ++p) {
        if (n % p != 0) continue;
        bool same = true;
        for (int i = p; i < n; ++i) {
            if (w[i] != w[i % p]) {
                same = false;
                break;
            }
        }
        if (same) return false;
    }
    return true;
}

static bool replay_fixed(const std::vector<int>& root) {
    if (!primitive(root)) return false;
    const int n = static_cast<int>(root.size());
    std::vector<int> state = root;
    state.reserve(3 * n);
    for (int d = 0; d < 2 * n; ++d) {
        const int want = root[d % n];
        if (cn(state) != want) return false;
        state.push_back(want);
    }
    return true;
}

static int replay_score(const std::vector<int>& root) {
    if (!primitive(root)) return -1;
    const int n = static_cast<int>(root.size());
    std::vector<int> state = root;
    state.reserve(3 * n);
    for (int d = 0; d < 2 * n; ++d) {
        const int want = root[d % n];
        if (cn(state) != want) return d;
        state.push_back(want);
    }
    return 2 * n;
}

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "usage: search_nested_replay LENGTH\n";
        return 2;
    }
    const int n = std::stoi(argv[1]);
    const std::string q = "223222322232322232223";
    const std::string prefix = q + q + q + "3";
    if (n < static_cast<int>(prefix.size())) return 0;
    const int free = n - static_cast<int>(prefix.size());
    if (free >= 63) {
        std::cerr << "too many free binary positions\n";
        return 2;
    }
    const std::uint64_t total = std::uint64_t{1} << free;
    std::uint64_t found = 0;
    int best_score = -1;
    std::string best_root;
    for (std::uint64_t mask = 0; mask < total; ++mask) {
        std::vector<int> root;
        root.reserve(n);
        for (char c : prefix) root.push_back(c - '0');
        for (int j = 0; j < free; ++j) {
            root.push_back(2 + static_cast<int>((mask >> j) & 1));
        }
        const int score = replay_score(root);
        if (score > best_score) {
            best_score = score;
            best_root.clear();
            for (int x : root) best_root.push_back(static_cast<char>('0' + x));
        }
        if (score != 2 * n) continue;
        ++found;
        for (int x : root) std::cout << x;
        std::cout << "\n";
    }
    std::cerr << "length=" << n << " candidates=" << total
              << " found=" << found << " best_score=" << best_score
              << " best_root=" << best_root << "\n";
}
