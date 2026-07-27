#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <string>
#include <vector>

static int curling_number(const std::vector<int>& word) {
    const int n = static_cast<int>(word.size());
    int best = 1;
    for (int root = 1; root <= n / (best + 1); ++root) {
        int copies = 1;
        while ((copies + 1) * root <= n) {
            const int left = n - (copies + 1) * root;
            const int right = n - copies * root;
            bool equal = true;
            for (int j = 0; j < root; ++j) {
                if (word[left + j] != word[right + j]) {
                    equal = false;
                    break;
                }
            }
            if (!equal) break;
            ++copies;
        }
        best = std::max(best, copies);
    }
    return best;
}

static bool primitive(const std::vector<int>& word) {
    const int n = static_cast<int>(word.size());
    for (int root = 1; root < n; ++root) {
        if (n % root != 0) continue;
        bool power = true;
        for (int i = root; i < n; ++i) {
            if (word[i] != word[i % root]) {
                power = false;
                break;
            }
        }
        if (power) return false;
    }
    return true;
}

static std::vector<int> rotate_left(const std::vector<int>& word, int shift) {
    const int n = static_cast<int>(word.size());
    std::vector<int> result;
    result.reserve(n);
    for (int i = 0; i < n; ++i) result.push_back(word[(i + shift) % n]);
    return result;
}

static std::string digits(const std::vector<int>& word) {
    std::string result;
    for (int x : word) {
        if (x < 0 || x > 9) return "-";
        result.push_back(static_cast<char>('0' + x));
    }
    return result;
}

int main(int argc, char** argv) {
    if (argc < 3 || argc > 4) {
        std::cerr << "usage: search_early_square MAX_S MAX_SYMBOL [list]\n";
        return 2;
    }
    const int max_s = std::atoi(argv[1]);
    const int max_symbol = std::atoi(argv[2]);
    const bool list = argc == 4;
    if (max_s < 1 || max_symbol < 2) return 2;
    const std::uint64_t radix = static_cast<std::uint64_t>(max_symbol - 1);

    for (int s = 1; s <= max_s; ++s) {
        std::uint64_t cases = 1;
        for (int i = 0; i < s; ++i) {
            if (cases > std::numeric_limits<std::uint64_t>::max() / radix) {
                std::cerr << "search space overflow at s=" << s << "\n";
                return 2;
            }
            cases *= radix;
        }
        std::uint64_t structural = 0;
        std::uint64_t self_generators = 0;
        std::uint64_t early = 0;
        for (std::uint64_t code = 0; code < cases; ++code) {
            std::uint64_t x = code;
            std::vector<int> D(s);
            for (int i = 0; i < s; ++i) {
                D[i] = 2 + static_cast<int>(x % radix);
                x /= radix;
            }
            for (int quotient = 1; quotient <= 2; ++quotient) {
                for (int u = 1; u < s; ++u) {
                    const int r = quotient * s + u;
                    const int h_min = quotient == 1 ? 1 : u + 1;
                    const int h_max = quotient == 1 ? u - 1 : s;
                    for (int h = h_min; h <= h_max; ++h) {
                        const int a = r - s - h;
                        if (D[a % s] != 2 || D[u] != 2) continue;

                        std::vector<int> Y;
                        Y.reserve(r);
                        for (int i = 0; i < r; ++i) Y.push_back(D[i % s]);
                        if (!primitive(Y)) continue;

                        std::vector<int> Z = Y;
                        Z.insert(Z.end(), Y.begin(), Y.end());
                        Z.insert(Z.end(), D.begin(), D.end());
                        std::vector<int> P = rotate_left(Z, a);
                        if (!primitive(P)) continue;
                        ++structural;

                        std::vector<int> state = P;
                        bool self_generates = true;
                        for (int d = 0; d < static_cast<int>(P.size()); ++d) {
                            const int value = curling_number(state);
                            if (value != P[d]) {
                                self_generates = false;
                                break;
                            }
                            state.push_back(value);
                        }
                        if (!self_generates || curling_number(state) != 2) {
                            continue;
                        }
                        ++self_generators;

                        std::vector<int> target = state;
                        int mismatch = -1;
                        for (int d = 0; d < static_cast<int>(P.size()); ++d) {
                            const int value = curling_number(target);
                            if (value != P[d]) {
                                mismatch = d;
                                break;
                            }
                            target.push_back(value);
                        }
                        if (mismatch != h || curling_number(target) != 3) {
                            continue;
                        }
                        ++early;
                        if (list) {
                            std::cout << "model s=" << s << " r=" << r
                                      << " h=" << h << " D=" << digits(D)
                                      << " Y=" << digits(Y)
                                      << " P=" << digits(P) << "\n";
                        }
                    }
                }
            }
        }
        std::cout << "s=" << s << " structural=" << structural
                  << " self_generators=" << self_generators
                  << " early=" << early << "\n";
    }
}
