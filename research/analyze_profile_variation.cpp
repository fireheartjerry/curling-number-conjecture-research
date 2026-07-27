#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

static bool primitive(const std::vector<int>& w) {
    const int n = static_cast<int>(w.size());
    for (int p = 1; p < n; ++p) {
        if (n % p) continue;
        bool same = true;
        for (int i = p; i < n; ++i) {
            if (w[i] != w[i % p]) { same = false; break; }
        }
        if (same) return false;
    }
    return true;
}

static int proper_curl(const std::vector<int>& w, int cut) {
    const int n = static_cast<int>(w.size());
    int best = 1;
    for (int p = 1; p < n; ++p) {
        int copies = 1;
        while (copies < 4) {
            bool same = true;
            for (int j = 0; j < p; ++j) {
                const int a = (cut - (copies + 1) * p + j) % n;
                const int b = (cut - p + j) % n;
                if (w[(a + n) % n] != w[(b + n) % n]) {
                    same = false;
                    break;
                }
            }
            if (!same) break;
            ++copies;
        }
        best = std::max(best, copies);
        if (best >= 4) return best;
    }
    return best;
}

static int variation(const std::vector<int>& w) {
    int result = 0;
    for (int i = 0; i < static_cast<int>(w.size()); ++i) {
        result += w[i] != w[(i + 1) % w.size()];
    }
    return result;
}

// For each maximal cyclic component [a,b] of profile value three, count
// symbol changes on the closed edge-neighborhood a-1,...,b.  These edge
// neighborhoods are disjoint for distinct components.
static int weak_cube_components(const std::vector<int>& w,
                                const std::vector<int>& f) {
    const int n = static_cast<int>(w.size());
    int bad = 0;
    if (std::all_of(f.begin(), f.end(), [](int x) { return x == 3; })) {
        return variation(w) < 2;
    }
    for (int a = 0; a < n; ++a) {
        if (f[a] != 3 || f[(a - 1 + n) % n] == 3) continue;
        int b = a;
        while (f[(b + 1) % n] == 3) b = (b + 1) % n;
        int changes = 0;
        int edge = (a - 1 + n) % n;
        while (true) {
            changes += w[edge] != w[(edge + 1) % n];
            if (edge == b) break;
            edge = (edge + 1) % n;
        }
        if (changes < 2) ++bad;
    }
    return bad;
}

static bool primitive_factor(const std::vector<int>& w, int start, int p) {
    const int n = static_cast<int>(w.size());
    for (int q = 1; q < p; ++q) {
        if (p % q) continue;
        bool same = true;
        for (int j = q; j < p; ++j) {
            if (w[(start + j) % n] != w[(start + (j % q)) % n]) {
                same = false;
                break;
            }
        }
        if (same) return false;
    }
    return true;
}

static bool last_interval_hall = true;
static bool last_candidate_arc_convex = true;

static std::vector<int> rotation(const std::vector<int>& w, int start, int p,
                                 int shift) {
    const int n = static_cast<int>(w.size());
    std::vector<int> result(p);
    for (int j = 0; j < p; ++j)
        result[j] = w[(start + shift + j) % n];
    return result;
}

// Candidate matching suggested by the cubic-run handle theorem:
// * a non-unary cubic run offers every CKRRW min/max-conjugate handle;
// * a unary cubic run offers the two transitions immediately outside it.
// A component may use candidates from any cubic run whose cube-end interval
// lies in that component.  Return false when two distinct candidates per
// component cannot be chosen globally.
static bool profile_handle_matching(const std::vector<int>& w,
                                    const std::vector<int>& f) {
    const int n = static_cast<int>(w.size());
    last_interval_hall = true;
    last_candidate_arc_convex = true;
    if (std::all_of(f.begin(), f.end(), [](int x) { return x == 3; }))
        return true;

    std::vector<int> component(n, -1);
    int components = 0;
    for (int a = 0; a < n; ++a) {
        if (f[a] != 3 || f[(a - 1 + n) % n] == 3) continue;
        int x = a;
        do {
            component[x] = components;
            x = (x + 1) % n;
        } while (f[x] == 3);
        ++components;
    }
    std::vector<std::vector<int>> candidates(components);

    for (int p = 1; p < n; ++p) {
        for (int l = 0; l < n; ++l) {
            if (w[(l - 1 + n) % n] == w[(l - 1 + p) % n]) continue;
            if (!primitive_factor(w, l, p)) continue;

            int length = p;
            while (length < 2 * n &&
                   w[(l + length) % n] ==
                       w[(l + length - p) % n]) {
                ++length;
            }
            if (length < 3 * p) continue;

            int id = component[(l + 3 * p) % n];
            if (id < 0) continue;
            bool one_component = true;
            for (int t = 0; t <= length - 3 * p; ++t) {
                if (component[(l + 3 * p + t) % n] != id) {
                    one_component = false;
                    break;
                }
            }
            if (!one_component) return false;

            if (p == 1) {
                candidates[id].push_back((l - 1 + n) % n);
                candidates[id].push_back((l + length - 1) % n);
                continue;
            }

            std::vector<int> smallest = rotation(w, l, p, 0);
            std::vector<int> largest = smallest;
            for (int shift = 1; shift < p; ++shift) {
                auto r = rotation(w, l, p, shift);
                smallest = std::min(smallest, r);
                largest = std::max(largest, r);
            }
            for (int s = 0; s + 2 * p <= length; ++s) {
                auto r = rotation(w, l + s, p, 0);
                if (r == smallest || r == largest)
                    candidates[id].push_back((l + s + p - 1) % n);
            }
            // Experimental augmenting pool: every unequal inter-position
            // internal to the maximal cubic run.  CKRRW handles are the
            // initially disjoint matching; these extra edges are possible
            // destinations when a unary run claims an external boundary.
            for (int s = 0; s + 1 < length; ++s) {
                const int edge = (l + s) % n;
                if (w[edge] != w[(edge + 1) % n])
                    candidates[id].push_back(edge);
            }
        }
    }

    for (auto& c : candidates) {
        std::sort(c.begin(), c.end());
        c.erase(std::unique(c.begin(), c.end()), c.end());
        for (int edge : c) {
            if (w[edge] == w[(edge + 1) % n]) return false;
        }
    }

    for (int left_symbol : {2, 3}) {
        std::vector<int> oriented_edges;
        for (int edge = 0; edge < n; ++edge) {
            if (w[edge] == left_symbol &&
                w[edge] != w[(edge + 1) % n]) {
                oriented_edges.push_back(edge);
            }
        }
        for (int id = 0; id < components; ++id) {
            std::vector<char> has(n, false);
            for (int edge : candidates[id]) {
                if (w[edge] == left_symbol) has[edge] = true;
            }
            int transitions = 0;
            for (int j = 0; j < static_cast<int>(oriented_edges.size()); ++j) {
                const bool here = has[oriented_edges[j]];
                const bool before =
                    has[oriented_edges[(j - 1 + oriented_edges.size()) %
                                       oriented_edges.size()]];
                transitions += here != before;
            }
            if (transitions > 2) last_candidate_arc_convex = false;
        }
        for (int first = 0; first < components; ++first) {
            std::vector<char> united(n, false);
            for (int count = 1; count <= components; ++count) {
                const int id = (first + count - 1) % components;
                for (int edge : candidates[id]) {
                    if (w[edge] == left_symbol) united[edge] = true;
                }
                int size = 0;
                for (int edge : oriented_edges) size += united[edge];
                if (size < count) last_interval_hall = false;
            }
        }

        std::vector<int> owner(n, -1);
        auto augment = [&](auto&& self, int id,
                           std::vector<char>& seen) -> bool {
            for (int edge : candidates[id]) {
                if (w[edge] != left_symbol) continue;
                if (seen[edge]) continue;
                seen[edge] = true;
                if (owner[edge] < 0 || self(self, owner[edge], seen)) {
                    owner[edge] = id;
                    return true;
                }
            }
            return false;
        };
        for (int id = 0; id < components; ++id) {
            std::vector<char> seen(n, false);
            if (!augment(augment, id, seen)) return false;
        }
    }
    return true;
}

int main(int argc, char** argv) {
    if (argc < 2 || argc > 3) {
        std::cerr << "usage: analyze_profile_variation LENGTH [--show-equal]\n";
        return 2;
    }
    const bool show_equal = argc == 3 && std::string(argv[2]) == "--show-equal";
    const int n = std::atoi(argv[1]);
    if (n <= 0 || n >= 63) return 2;
    const std::uint64_t cases = std::uint64_t{1} << n;
    std::uint64_t admissible = 0, violations = 0, equal = 0, fixed = 0;
    std::uint64_t weak_components = 0;
    std::uint64_t handle_match_failures = 0;
    std::uint64_t interval_hall_failures = 0;
    std::uint64_t nonconvex_candidate_words = 0;
    int max_delta = -n;
    for (std::uint64_t bits = 0; bits < cases; ++bits) {
        std::vector<int> w(n), f(n);
        for (int i = 0; i < n; ++i) w[i] = 2 + ((bits >> i) & 1);
        if (!primitive(w)) continue;
        bool good = true;
        for (int i = 0; i < n; ++i) {
            f[i] = proper_curl(w, i);
            if (f[i] < 2 || f[i] > 3) { good = false; break; }
        }
        if (!good) continue;
        ++admissible;
        const int weak = weak_cube_components(w, f);
        if (weak) {
            ++weak_components;
            if (weak_components <= 3) {
                std::cout << "weak-component=";
                for (int x : w) std::cout << x;
                std::cout << " profile=";
                for (int x : f) std::cout << x;
                std::cout << " count=" << weak << "\n";
            }
        }
        if (!profile_handle_matching(w, f)) {
            ++handle_match_failures;
            if (handle_match_failures <= 3) {
                std::cout << "handle-match-failure=";
                for (int x : w) std::cout << x;
                std::cout << " profile=";
                for (int x : f) std::cout << x;
                std::cout << "\n";
            }
        }
        if (!last_interval_hall) {
            ++interval_hall_failures;
            if (interval_hall_failures <= 3) {
                std::cout << "interval-hall-failure=";
                for (int x : w) std::cout << x;
                std::cout << " profile=";
                for (int x : f) std::cout << x;
                std::cout << "\n";
            }
        }
        nonconvex_candidate_words += !last_candidate_arc_convex;
        const int delta = variation(f) - variation(w);
        max_delta = std::max(max_delta, delta);
        if (delta > 0) {
            ++violations;
            if (violations <= 3) {
                std::cout << "violation=";
                for (int x : w) std::cout << x;
                std::cout << " profile=";
                for (int x : f) std::cout << x;
                std::cout << " delta=" << delta << "\n";
            }
        }
        if (delta == 0) {
            ++equal;
            if (show_equal) {
                std::cout << "equal=";
                for (int x : w) std::cout << x;
                std::cout << " profile=";
                for (int x : f) std::cout << x;
                std::cout << "\n";
            }
        }
        if (w == f) ++fixed;
    }
    std::cout << "length=" << n << " admissible=" << admissible
              << " violations=" << violations << " equal=" << equal
              << " fixed=" << fixed << " max_delta=" << max_delta << "\n";
    std::cout << "weak_component_words=" << weak_components << "\n";
    std::cout << "handle_match_failures=" << handle_match_failures << "\n";
    std::cout << "interval_hall_failures=" << interval_hall_failures << "\n";
    std::cout << "nonconvex_candidate_words=" << nonconvex_candidate_words
              << "\n";
}
