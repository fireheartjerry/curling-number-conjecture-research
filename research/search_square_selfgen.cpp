#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>

static int cn(const std::vector<int>& w) {
    const int n = static_cast<int>(w.size());
    int best = 1;
    for (int root = 1; root <= n / (best + 1); ++root) {
        int copies = 1;
        while ((copies + 1) * root <= n) {
            bool same = true;
            const int left = n - (copies + 1) * root;
            const int right = n - root;
            for (int j = 0; j < root; ++j) {
                if (w[left + j] != w[right + j]) {
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
    for (int root = 1; root < n; ++root) {
        if (n % root != 0) continue;
        bool power = true;
        for (int i = root; i < n; ++i) {
            if (w[i] != w[i % root]) {
                power = false;
                break;
            }
        }
        if (power) return false;
    }
    return true;
}

static bool square_at_cut(
    const std::vector<int>& w, const int cut, const int root
) {
    const int n = static_cast<int>(w.size());
    for (int j = 0; j < root; ++j) {
        int left = (cut - 2 * root + j) % n;
        int right = (cut - root + j) % n;
        if (left < 0) left += n;
        if (right < 0) right += n;
        if (w[left] != w[right]) return false;
    }
    return true;
}

static std::vector<int> minimal_roots(const std::vector<int>& w) {
    const int n = static_cast<int>(w.size());
    std::vector<int> mu(n, 0);
    for (int cut = 0; cut < n; ++cut) {
        for (int root = 1; root < n; ++root) {
            if (square_at_cut(w, cut, root)) {
                mu[cut] = root;
                break;
            }
        }
        if (mu[cut] == 0) return {};
    }
    return mu;
}

static int max_cycles_for_one_letter(
    const std::vector<int>& w, const std::vector<int>& mu
) {
    const int n = static_cast<int>(w.size());
    std::vector<int> done(n, 0);
    std::map<int, int> counts;
    for (int start = 0; start < n; ++start) {
        if (done[start]) continue;
        std::vector<int> path;
        std::map<int, int> at;
        int x = start;
        while (!done[x] && !at.count(x)) {
            at[x] = static_cast<int>(path.size());
            path.push_back(x);
            x = (x - mu[x] + n) % n;
        }
        if (at.count(x)) {
            ++counts[w[(x - 1 + n) % n]];
        }
        for (int y : path) done[y] = 1;
    }
    int result = 0;
    for (const auto& [letter, count] : counts) {
        result = std::max(result, count);
    }
    return result;
}

int main(int argc, char** argv) {
    if (argc != 2) return 2;
    const int n = std::stoi(argv[1]);
    if (n < 1 || n > 62) return 2;
    const std::uint64_t total = std::uint64_t{1} << n;
    std::uint64_t source_generators = 0;
    std::uint64_t square_towers = 0;
    std::uint64_t early = 0;
    std::uint64_t multi_cycle = 0;
    int longest_target_prefix = -1;
    std::vector<int> best;

    for (std::uint64_t code = 0; code < total; ++code) {
        if ((code & 1) != 0) continue;  // P[0]=2.
        std::vector<int> p(n);
        for (int i = 0; i < n; ++i) {
            p[i] = 2 + static_cast<int>((code >> i) & 1);
        }
        if (!primitive(p)) continue;

        std::vector<int> state = p;
        bool source = true;
        for (int d = 0; d < n; ++d) {
            const int value = cn(state);
            if (value != p[d]) {
                source = false;
                break;
            }
            state.push_back(value);
        }
        if (!source) continue;
        ++source_generators;
        if (cn(state) != 2) continue;
        ++square_towers;

        const std::vector<int> mu = minimal_roots(p);
        if (
            !mu.empty() &&
            max_cycles_for_one_letter(p, mu) > 1
        ) {
            ++multi_cycle;
            if (multi_cycle <= 3) {
                std::cout << "multi-cycle ";
                for (int a : p) std::cout << a;
                std::cout << "\n";
            }
        }

        int matched = 0;
        while (matched < n && cn(state) == p[matched]) {
            state.push_back(p[matched]);
            ++matched;
        }
        if (matched > longest_target_prefix) {
            longest_target_prefix = matched;
            best = p;
        }
        if (matched < n && cn(state) > p[matched]) {
            ++early;
            if (early <= 20) {
                std::cout << "early h=" << matched << " want="
                          << p[matched] << " got=" << cn(state)
                          << " word=";
                for (int a : p) std::cout << a;
                std::cout << "\n";
            }
        }
    }
    std::cout << "n=" << n
              << " source_generators=" << source_generators
              << " square_towers=" << square_towers
              << " early=" << early
              << " multi_cycle=" << multi_cycle
              << " longest_target_prefix=" << longest_target_prefix
              << " best=";
    for (int a : best) std::cout << a;
    std::cout << "\n";
}
