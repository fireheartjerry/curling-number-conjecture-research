#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>

static bool primitive(const std::vector<int>& w) {
    const int n = static_cast<int>(w.size());
    for (int p = 1; p < n; ++p) {
        if (n % p != 0) continue;
        bool period = true;
        for (int i = p; i < n; ++i) {
            if (w[i] != w[i % p]) {
                period = false;
                break;
            }
        }
        if (period) return false;
    }
    return true;
}

static bool square_at_cut(
    const std::vector<int>& w, const int cut, const int root
) {
    const int n = static_cast<int>(w.size());
    for (int j = 0; j < root; ++j) {
        const int left = (cut - 2 * root + j) % n;
        const int right = (cut - root + j) % n;
        if (w[(left + n) % n] != w[(right + n) % n]) return false;
    }
    return true;
}

static std::vector<int> minimal_roots(const std::vector<int>& w) {
    const int n = static_cast<int>(w.size());
    std::vector<int> result(n, 0);
    for (int cut = 0; cut < n; ++cut) {
        for (int root = 1; root < n; ++root) {
            if (square_at_cut(w, cut, root)) {
                result[cut] = root;
                break;
            }
        }
        if (result[cut] == 0) return {};
    }
    return result;
}

int main(int argc, char** argv) {
    if (argc != 2) return 2;
    const int n = std::stoi(argv[1]);
    if (n < 1 || n > 62) return 2;
    const std::uint64_t total = std::uint64_t{1} << n;
    std::uint64_t squareful = 0;
    int max_cycle = 0;
    int max_winding = 0;
    bool printed_multi_same_letter = false;
    bool printed_multi_winding = false;

    for (std::uint64_t code = 0; code < total; ++code) {
        std::vector<int> w(n);
        for (int i = 0; i < n; ++i) {
            w[i] = 2 + static_cast<int>((code >> i) & 1);
        }
        if (!primitive(w)) continue;
        const std::vector<int> mu = minimal_roots(w);
        if (mu.empty()) continue;
        ++squareful;

        std::vector<int> state(n, 0);
        std::map<int, int> cycles_by_letter;
        for (int start = 0; start < n; ++start) {
            if (state[start] != 0) continue;
            std::vector<int> path;
            std::map<int, int> index;
            int x = start;
            while (state[x] == 0 && !index.count(x)) {
                index[x] = static_cast<int>(path.size());
                path.push_back(x);
                x = (x - mu[x] + n) % n;
            }
            if (index.count(x)) {
                const int first = index[x];
                int sum = 0;
                for (int i = first; i < static_cast<int>(path.size()); ++i) {
                    sum += mu[path[i]];
                }
                const int cycle_length =
                    static_cast<int>(path.size()) - first;
                const int winding = sum / n;
                const int letter = w[(x - 1 + n) % n];
                ++cycles_by_letter[letter];
                max_cycle = std::max(max_cycle, cycle_length);
                max_winding = std::max(max_winding, winding);
                if (winding > 1 && !printed_multi_winding) {
                    printed_multi_winding = true;
                    std::cout << "winding>1 word=";
                    for (int a : w) std::cout << a;
                    std::cout << " winding=" << winding << "\n";
                }
            }
            for (int y : path) state[y] = 1;
        }
        for (const auto& [letter, count] : cycles_by_letter) {
            if (count > 1 && !printed_multi_same_letter) {
                printed_multi_same_letter = true;
                std::cout << "multiple-same-letter word=";
                for (int a : w) std::cout << a;
                std::cout << " letter=" << letter
                          << " cycles=" << count << "\n";
            }
        }
    }
    std::cout << "n=" << n << " squareful=" << squareful
              << " max_cycle=" << max_cycle
              << " max_winding=" << max_winding
              << " multi_same_letter=" << printed_multi_same_letter
              << " multi_winding=" << printed_multi_winding << "\n";
}
