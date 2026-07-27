#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

static int cn(const std::vector<int>& w) {
    int n = static_cast<int>(w.size()), best = 1;
    for (int p = 1; p <= n / (best + 1); ++p) {
        int copies = 1;
        while ((copies + 1) * p <= n) {
            bool ok = true;
            int a = n - (copies + 1) * p, b = n - p;
            for (int j = 0; j < p; ++j) {
                if (w[a + j] != w[b + j]) {
                    ok = false;
                    break;
                }
            }
            if (!ok) break;
            ++copies;
        }
        best = std::max(best, copies);
    }
    return best;
}

int main(int argc, char** argv) {
    if (argc != 2) return 2;
    int m = std::stoi(argv[1]);
    const std::string q = "223222322232322232223";
    const std::string t = q + q + q + "3";
    if (m >= 63) return 2;
    std::uint64_t found = 0, total = std::uint64_t{1} << m;
    int best = -1;
    std::string best_seed;
    for (std::uint64_t mask = 0; mask < total; ++mask) {
        std::vector<int> seed;
        seed.reserve(m + static_cast<int>(t.size()) + m);
        for (int j = 0; j < m; ++j) seed.push_back(2 + ((mask >> j) & 1));
        std::vector<int> state = seed;
        int score = 0;
        bool ok = true;
        for (char c : t) {
            int want = c - '0';
            if (cn(state) != want) {
                ok = false;
                break;
            }
            state.push_back(want);
            ++score;
        }
        if (ok) {
            for (int j = 0; j < m; ++j) {
                int want = seed[j];
                if (cn(state) != want) {
                    ok = false;
                    break;
                }
                state.push_back(want);
                ++score;
            }
        }
        if (score > best) {
            best = score;
            best_seed.clear();
            for (int x : seed) best_seed.push_back(static_cast<char>('0' + x));
        }
        if (!ok) continue;
        ++found;
        for (int x : seed) std::cout << x;
        std::cout << "\n";
    }
    std::cerr << "m=" << m << " total=" << total << " found=" << found
              << " best=" << best << " seed=" << best_seed << "\n";
}
