#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <vector>

static bool primitive(const std::vector<int>& w) {
    const int n = static_cast<int>(w.size());
    for (int p = 1; p < n; ++p) {
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

static void print_word(const std::vector<int>& w) {
    for (int x : w) std::cout << x;
}

int main(int argc, char** argv) {
    if (argc != 3) {
        std::cerr << "usage: search_midpoint_winding LENGTH ALPHABET_SIZE\n";
        return 2;
    }
    const int n = std::atoi(argv[1]);
    const int alphabet = std::atoi(argv[2]);
    if (n < 1 || n > 40 || alphabet < 2 || alphabet > 9) return 2;

    // Fix the first letter to zero.  Renaming the first letter preserves
    // primitivity, all square equalities, and the midpoint graph.
    std::uint64_t cases = 1;
    for (int i = 1; i < n; ++i) {
        if (cases > UINT64_MAX / static_cast<std::uint64_t>(alphabet)) {
            std::cerr << "case count overflow\n";
            return 2;
        }
        cases *= static_cast<std::uint64_t>(alphabet);
    }

    std::uint64_t primitive_count = 0;
    std::uint64_t squareful_count = 0;
    std::uint64_t multi_same_color = 0;
    int maximum_winding = 0;

    for (std::uint64_t code = 0; code < cases; ++code) {
        std::uint64_t x = code;
        std::vector<int> w(n, 0);
        for (int i = 1; i < n; ++i) {
            w[i] = static_cast<int>(x % alphabet);
            x /= alphabet;
        }
        if (!primitive(w)) continue;
        ++primitive_count;
        const std::vector<int> mu = minimal_roots(w);
        if (mu.empty()) continue;
        ++squareful_count;

        std::vector<int> globally_done(n, 0);
        std::map<int, int> cycles_by_color;
        for (int start = 0; start < n; ++start) {
            if (globally_done[start]) continue;
            std::vector<int> path;
            std::map<int, int> path_index;
            int cut = start;
            while (!globally_done[cut] && !path_index.count(cut)) {
                path_index[cut] = static_cast<int>(path.size());
                path.push_back(cut);
                cut = (cut - mu[cut] + n) % n;
            }
            if (path_index.count(cut)) {
                const int first = path_index[cut];
                int sum = 0;
                std::vector<int> cycle;
                for (int i = first; i < static_cast<int>(path.size()); ++i) {
                    cycle.push_back(path[i]);
                    sum += mu[path[i]];
                }
                if (sum % n != 0) {
                    std::cerr << "nonintegral winding\n";
                    return 1;
                }
                const int winding = sum / n;
                maximum_winding = std::max(maximum_winding, winding);
                const int color = w[(cut - 1 + n) % n];
                ++cycles_by_color[color];
                if (winding > 1) {
                    std::cout << "winding-counterexample word=";
                    print_word(w);
                    std::cout << " mu=";
                    for (int r : mu) std::cout << r << ",";
                    std::cout << " cycle=";
                    for (int c : cycle) std::cout << c << ",";
                    std::cout << " winding=" << winding << "\n";
                    return 0;
                }
            }
            for (int c : path) globally_done[c] = 1;
        }
        bool multiple = false;
        for (const auto& [color, count] : cycles_by_color) {
            if (count > 1) multiple = true;
        }
        multi_same_color += multiple;
    }

    std::cout << "length=" << n << " alphabet=" << alphabet
              << " cases=" << cases
              << " primitive=" << primitive_count
              << " squareful=" << squareful_count
              << " multi_same_color=" << multi_same_color
              << " maximum_winding=" << maximum_winding << "\n";
}
