#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

static int mod(int x, int n) {
    x %= n;
    return x < 0 ? x + n : x;
}

static bool primitive(const std::vector<int>& w) {
    const int n = static_cast<int>(w.size());
    for (int p = 1; p < n; ++p) {
        if (n % p) continue;
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

static bool power_at(const std::vector<int>& w, int cut, int p, int k) {
    const int n = static_cast<int>(w.size());
    for (int block = 2; block <= k; ++block) {
        for (int j = 0; j < p; ++j) {
            if (w[mod(cut - block * p + j, n)] !=
                w[mod(cut - p + j, n)])
                return false;
        }
    }
    return true;
}

static int proper_curl(const std::vector<int>& w, int cut) {
    const int n = static_cast<int>(w.size());
    int best = 1;
    for (int p = 1; p < n; ++p) {
        if (power_at(w, cut, p, 4)) return 4;
        if (power_at(w, cut, p, 3))
            best = std::max(best, 3);
        else if (power_at(w, cut, p, 2))
            best = std::max(best, 2);
    }
    return best;
}

static bool primitive_factor(const std::vector<int>& w, int start, int p) {
    const int n = static_cast<int>(w.size());
    for (int q = 1; q < p; ++q) {
        if (p % q) continue;
        bool same = true;
        for (int j = q; j < p; ++j) {
            if (w[mod(start + j, n)] != w[mod(start + j % q, n)]) {
                same = false;
                break;
            }
        }
        if (same) return false;
    }
    return true;
}

struct Violation {
    int left = -1;
    int period = 0;
    int mass = 0;
    std::vector<std::pair<int, int>> children;
    std::vector<int> holes;
};

static bool mass_violation(const std::vector<int>& w,
                           const std::vector<int>& profile,
                           Violation& out) {
    const int n = static_cast<int>(w.size());
    int maximum_cube_period = 0;
    for (int cut = 0; cut < n; ++cut) {
        if (profile[cut] != 3) continue;
        for (int p = 1; p < n; ++p) {
            if (power_at(w, cut, p, 3))
                maximum_cube_period = std::max(maximum_cube_period, p);
        }
    }
    if (maximum_cube_period == 0) return false;

    const int p = maximum_cube_period;
    for (int left = 0; left < n; ++left) {
        if (w[mod(left - 1, n)] == w[mod(left - 1 + p, n)])
            continue;
        if (!primitive_factor(w, left, p)) continue;

        int length = p;
        while (length < 2 * n &&
               w[mod(left + length, n)] ==
                   w[mod(left + length - p, n)])
            ++length;
        if (length < 3 * p) continue;

        Violation here;
        here.left = left;
        here.period = p;

        for (int offset = 0; offset < p; ++offset) {
            const int cut = left + 2 * p + offset;
            if (profile[mod(cut, n)] != 3) continue;
            int child = p;
            for (int q = 1; q < p; ++q) {
                if (power_at(w, cut, q, 3)) {
                    child = q;
                    break;
                }
            }
            // A globally maximal run should force an internal child.
            if (child == p) {
                std::cerr << "missing internal child\n";
                std::exit(3);
            }
            here.children.push_back({offset, child});
            here.mass += child;
        }

        for (int offset = 0; offset < p; ++offset) {
            const int cut = left + offset;
            if (profile[mod(cut, n)] != 2) continue;
            // In a fixed profile the labels at aligned copies agree.
            // Outside fixedness, do not charge a first-copy hole at an
            // offset already charged as a third-copy child.
            if (profile[mod(left + 2 * p + offset, n)] == 3) continue;
            bool contained_square = false;
            for (int q = 1; 2 * q <= offset; ++q) {
                bool square = true;
                for (int j = 0; j < q; ++j) {
                    if (w[mod(cut - 2 * q + j, n)] !=
                        w[mod(cut - q + j, n)]) {
                        square = false;
                        break;
                    }
                }
                if (square) {
                    contained_square = true;
                    break;
                }
            }
            if (!contained_square) {
                here.holes.push_back(offset);
                ++here.mass;
            }
        }

        if (here.mass > p) {
            out = here;
            return true;
        }
    }
    return false;
}

static void print_word(const std::vector<int>& w) {
    for (int x : w) std::cout << x;
}

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "usage: search_maximal_root_mass LENGTH\n";
        return 2;
    }
    const int n = std::atoi(argv[1]);
    if (n <= 0 || n >= 63) return 2;

    const std::uint64_t cases = std::uint64_t{1} << n;
    std::uint64_t admissible = 0;
    std::uint64_t with_cube = 0;
    for (std::uint64_t bits = 0; bits < cases; ++bits) {
        std::vector<int> w(n), profile(n);
        for (int i = 0; i < n; ++i)
            w[i] = 2 + ((bits >> i) & 1);
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
        with_cube +=
            std::find(profile.begin(), profile.end(), 3) != profile.end();

        Violation violation;
        if (mass_violation(w, profile, violation)) {
            std::cout << "violation Q=";
            print_word(w);
            std::cout << " F=";
            print_word(profile);
            std::cout << " l=" << violation.left
                      << " p=" << violation.period
                      << " mass=" << violation.mass << " children=";
            for (auto [offset, child] : violation.children)
                std::cout << "(" << offset << "," << child << ")";
            std::cout << " holes=";
            for (int hole : violation.holes) std::cout << hole << ",";
            std::cout << "\n";
            return 1;
        }
    }
    std::cout << "n=" << n << " admissible=" << admissible
              << " with_cube=" << with_cube << " no_violation\n";
    return 0;
}
