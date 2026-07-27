#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
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

static bool power_at_cut(
    const std::vector<int>& w,
    const int cut,
    const int root,
    const int exponent
) {
    const int n = static_cast<int>(w.size());
    for (int block = 2; block <= exponent; ++block) {
        for (int j = 0; j < root; ++j) {
            const int earlier = (cut - block * root + j) % n;
            const int terminal = (cut - root + j) % n;
            if (
                w[(earlier + n) % n]
                != w[(terminal + n) % n]
            ) {
                return false;
            }
        }
    }
    return true;
}

static int proper_curl(const std::vector<int>& w, const int cut) {
    const int n = static_cast<int>(w.size());
    int best = 1;
    for (int root = 1; root < n; ++root) {
        int exponent = 1;
        while (
            exponent < 4
            && power_at_cut(w, cut, root, exponent + 1)
        ) {
            ++exponent;
        }
        best = std::max(best, exponent);
        if (best == 4) return best;
    }
    return best;
}

static std::vector<int> minimal_roots(const std::vector<int>& w) {
    const int n = static_cast<int>(w.size());
    std::vector<int> mu(n, 0);
    for (int cut = 0; cut < n; ++cut) {
        for (int root = 1; root < n; ++root) {
            if (power_at_cut(w, cut, root, 2)) {
                mu[cut] = root;
                break;
            }
        }
        if (mu[cut] == 0) return {};
    }
    return mu;
}

static std::vector<std::vector<int>> cycles(
    const std::vector<int>& mu
) {
    const int n = static_cast<int>(mu.size());
    std::vector<int> done(n, 0);
    std::vector<std::vector<int>> result;
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
            result.emplace_back(path.begin() + index[cut], path.end());
        }
        for (int phase : path) done[phase] = 1;
    }
    return result;
}

static void print_word(const std::vector<int>& w) {
    for (int token : w) std::cout << token;
}

int main(int argc, char** argv) {
    if (argc != 3) {
        std::cerr << "usage: search_compatible_cycles LENGTH ALPHABET\n";
        return 2;
    }
    const int n = std::atoi(argv[1]);
    const int alphabet = std::atoi(argv[2]);
    if (n < 1 || n > 40 || alphabet < 2 || alphabet > 9) return 2;

    std::uint64_t cases = 1;
    for (int i = 1; i < n; ++i) {
        if (cases > UINT64_MAX / static_cast<std::uint64_t>(alphabet)) {
            return 2;
        }
        cases *= static_cast<std::uint64_t>(alphabet);
    }

    std::uint64_t admissible = 0;
    std::uint64_t compatible_failures = 0;
    std::uint64_t compatible_token_failures = 0;
    std::uint64_t weighted = 0;
    std::uint64_t weighted_failures = 0;
    bool shown = false;
    for (std::uint64_t code = 0; code < cases; ++code) {
        std::uint64_t x = code;
        std::vector<int> w(n, 0), profile(n);
        for (int i = 1; i < n; ++i) {
            w[i] = static_cast<int>(x % alphabet);
            x /= alphabet;
        }
        if (!primitive(w)) continue;
        bool good = true;
        for (int cut = 0; cut < n; ++cut) {
            profile[cut] = proper_curl(w, cut);
            if (profile[cut] < 2 || profile[cut] > 3) {
                good = false;
                break;
            }
        }
        if (!good) continue;
        ++admissible;
        const std::vector<int> mu = minimal_roots(w);
        if (mu.empty()) std::abort();
        const auto graph_cycles = cycles(mu);

        std::map<int, int> compatible_by_weight;
        bool failure = false;
        for (const auto& cycle : graph_cycles) {
            const int first_weight =
                profile[(cycle[0] - 1 + n) % n];
            bool compatible = true;
            for (int cut : cycle) {
                if (profile[(cut - 1 + n) % n] != first_weight) {
                    compatible = false;
                    break;
                }
            }
            if (
                compatible
                && ++compatible_by_weight[first_weight] > 1
            ) {
                failure = true;
            }
        }
        compatible_failures += failure;

        std::map<int, int> token_weight;
        std::map<int, int> compatible_tokens_by_weight;
        bool is_weighted = true;
        for (int i = 0; i < n; ++i) {
            const auto [it, inserted] =
                token_weight.emplace(w[i], profile[i]);
            if (!inserted && it->second != profile[i]) {
                is_weighted = false;
                break;
            }
        }
        for (int token = 0; token < alphabet; ++token) {
            int token_profile = 0;
            bool occurs = false;
            bool compatible_token = true;
            for (int i = 0; i < n; ++i) {
                if (w[i] != token) continue;
                if (!occurs) {
                    occurs = true;
                    token_profile = profile[i];
                } else if (profile[i] != token_profile) {
                    compatible_token = false;
                    break;
                }
            }
            if (occurs && compatible_token) {
                ++compatible_tokens_by_weight[token_profile];
            }
        }
        bool token_failure = false;
        for (const auto& [weight, count] : compatible_tokens_by_weight) {
            if (count > 1) token_failure = true;
        }
        compatible_token_failures += token_failure;
        if (is_weighted) {
            ++weighted;
            weighted_failures += failure;
        }
        if (failure && !shown) {
            shown = true;
            std::cout << "compatible-cycle-counterexample word=";
            print_word(w);
            std::cout << " profile=";
            print_word(profile);
            std::cout << " weighted=" << is_weighted << " mu=";
            for (int root : mu) std::cout << root << ",";
            std::cout << " cycles=";
            for (const auto& cycle : graph_cycles) {
                std::cout << "(";
                for (int cut : cycle) std::cout << cut << ",";
                std::cout << ")";
            }
            std::cout << "\n";
        }
    }
    std::cout << "length=" << n << " alphabet=" << alphabet
              << " cases=" << cases
              << " admissible=" << admissible
              << " compatible_failures=" << compatible_failures
              << " compatible_token_failures="
              << compatible_token_failures
              << " weighted=" << weighted
              << " weighted_failures=" << weighted_failures << "\n";
}
