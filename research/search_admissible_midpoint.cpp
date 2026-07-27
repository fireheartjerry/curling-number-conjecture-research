#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
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

// Values at least four are capped at four, which is sufficient for testing
// membership in {2,3}.
static int proper_curl(const std::vector<int>& w, const int cut) {
    const int n = static_cast<int>(w.size());
    int best = 1;
    for (int root = 1; root < n; ++root) {
        int copies = 1;
        while (copies < 4) {
            bool equal = true;
            for (int j = 0; j < root; ++j) {
                const int earlier =
                    (cut - (copies + 1) * root + j) % n;
                const int terminal = (cut - root + j) % n;
                if (
                    w[(earlier + n) % n]
                    != w[(terminal + n) % n]
                ) {
                    equal = false;
                    break;
                }
            }
            if (!equal) break;
            ++copies;
        }
        best = std::max(best, copies);
        if (best == 4) return 4;
    }
    return best;
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
    for (int letter : w) std::cout << letter;
}

struct CycleAudit {
    int maximum_winding = 0;
    bool multiple_same_color = false;
    std::vector<std::vector<int>> cycles;
};

static CycleAudit audit_cycles(
    const std::vector<int>& w, const std::vector<int>& mu
) {
    const int n = static_cast<int>(w.size());
    std::vector<int> done(n, 0);
    std::map<int, int> cycles_by_color;
    CycleAudit result;
    for (int start = 0; start < n; ++start) {
        if (done[start]) continue;
        std::vector<int> path;
        std::map<int, int> index;
        int cut = start;
        while (!done[cut] && !index.count(cut)) {
            index[cut] = static_cast<int>(path.size());
            path.push_back(cut);
            cut = (cut - mu[cut] + n) % n;
        }
        if (index.count(cut)) {
            std::vector<int> cycle(
                path.begin() + index[cut], path.end()
            );
            int sum = 0;
            for (int phase : cycle) sum += mu[phase];
            if (sum % n != 0) std::abort();
            result.maximum_winding =
                std::max(result.maximum_winding, sum / n);
            const int color = w[(cycle[0] - 1 + n) % n];
            ++cycles_by_color[color];
            result.cycles.push_back(cycle);
        }
        for (int phase : path) done[phase] = 1;
    }
    for (const auto& [color, count] : cycles_by_color) {
        if (count > 1) result.multiple_same_color = true;
    }
    return result;
}

int main(int argc, char** argv) {
    if (argc != 3) {
        std::cerr
            << "usage: search_admissible_midpoint LENGTH admissible|fixed\n";
        return 2;
    }
    const int n = std::atoi(argv[1]);
    const std::string mode = argv[2];
    if (
        n < 1 || n >= 63
        || (mode != "admissible" && mode != "fixed")
    ) {
        return 2;
    }

    const std::uint64_t cases = std::uint64_t{1} << n;
    std::uint64_t accepted = 0;
    std::uint64_t multiple = 0;
    std::uint64_t multiple_compatible = 0;
    int maximum_winding = 0;
    bool printed_multiple = false;
    bool printed_winding = false;
    for (std::uint64_t bits = 0; bits < cases; ++bits) {
        std::vector<int> w(n);
        for (int i = 0; i < n; ++i) {
            w[i] = 2 + static_cast<int>((bits >> i) & 1);
        }
        if (!primitive(w)) continue;
        std::vector<int> profile(n);
        bool admissible = true;
        for (int cut = 0; cut < n; ++cut) {
            profile[cut] = proper_curl(w, cut);
            if (profile[cut] < 2 || profile[cut] > 3) {
                admissible = false;
                break;
            }
        }
        if (!admissible) continue;
        if (mode == "fixed" && profile != w) continue;
        const std::vector<int> mu = minimal_roots(w);
        if (mu.empty()) std::abort();
        ++accepted;
        const CycleAudit audit = audit_cycles(w, mu);
        maximum_winding =
            std::max(maximum_winding, audit.maximum_winding);
        if (audit.multiple_same_color) {
            ++multiple;
            if (!printed_multiple) {
                printed_multiple = true;
                std::cout << "same-color-counterexample word=";
                print_word(w);
                std::cout << " profile=";
                print_word(profile);
                std::cout << " mu=";
                for (int root : mu) std::cout << root << ",";
                std::cout << " cycles=";
                for (const auto& cycle : audit.cycles) {
                    std::cout << "(";
                    for (int phase : cycle) std::cout << phase << ",";
                    std::cout << ")";
                }
                std::cout << "\n";
            }
        }
        std::map<int, int> compatible_cycles_by_color;
        for (const auto& cycle : audit.cycles) {
            const int color = w[(cycle[0] - 1 + n) % n];
            bool compatible = true;
            for (int phase : cycle) {
                const int predecessor = (phase - 1 + n) % n;
                if (profile[predecessor] != color) {
                    compatible = false;
                    break;
                }
            }
            if (compatible) ++compatible_cycles_by_color[color];
        }
        bool has_multiple_compatible = false;
        for (const auto& [color, count] : compatible_cycles_by_color) {
            if (count > 1) has_multiple_compatible = true;
        }
        multiple_compatible += has_multiple_compatible;
        if (audit.maximum_winding > 1 && !printed_winding) {
            printed_winding = true;
            std::cout << "winding-counterexample word=";
            print_word(w);
            std::cout << " profile=";
            print_word(profile);
            std::cout << " winding=" << audit.maximum_winding << "\n";
        }
    }
    std::cout << "length=" << n << " mode=" << mode
              << " accepted=" << accepted
              << " multiple_same_color=" << multiple
              << " multiple_compatible_same_color="
              << multiple_compatible
              << " maximum_winding=" << maximum_winding << "\n";
}
