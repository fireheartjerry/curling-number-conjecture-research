#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

static int curling_number(const std::vector<int>& word) {
    const int n = static_cast<int>(word.size());
    int best = 1;
    for (int p = 1; p <= n / (best + 1); ++p) {
        int copies = 1;
        while ((copies + 1) * p <= n) {
            bool equal = true;
            const int left = n - (copies + 1) * p;
            const int right = n - copies * p;
            for (int j = 0; j < p; ++j) {
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

static std::vector<int> decode(std::uint64_t bits, int p) {
    std::vector<int> word(p);
    for (int i = 0; i < p; ++i) {
        word[i] = 2 + static_cast<int>((bits >> i) & 1ULL);
    }
    return word;
}

static std::string digits(const std::vector<int>& word) {
    std::string result;
    result.reserve(word.size());
    for (int value : word) result.push_back(static_cast<char>('0' + value));
    return result;
}

int main(int argc, char** argv) {
    const int max_p = argc >= 2 ? std::stoi(argv[1]) : 24;
    const bool list_words = argc >= 3;
    for (int p = 1; p <= max_p; ++p) {
        if (p >= 63) return 2;
        std::uint64_t count = 0;
        std::uint64_t fixed = 0;
        std::uint64_t internal = 0;
        std::string first_fixed;
        std::string first_internal;
        int first_internal_j = -1;
        int first_internal_root = -1;
        const std::uint64_t cases = 1ULL << p;
        for (std::uint64_t bits = 0; bits < cases; ++bits) {
            if ((bits & 1ULL) != 0) continue;  // P[0] must be 2.
            std::vector<int> P = decode(bits, p);
            std::vector<int> state = P;
            bool generates = true;
            for (int j = 0; j < p; ++j) {
                if (curling_number(state) != P[j]) {
                    generates = false;
                    break;
                }
                state.push_back(P[j]);
            }
            if (!generates || curling_number(state) != 2) continue;
            ++count;
            if (list_words) {
                std::cout << "word " << p << " " << digits(P) << "\n";
            }

            int mismatch = p;
            int mismatch_root = p;
            for (int j = 0; j < p; ++j) {
                const int value = curling_number(state);
                if (value != P[j]) {
                    mismatch = j;
                    const int n = static_cast<int>(state.size());
                    for (int q = 1; q * value <= n; ++q) {
                        bool power = true;
                        for (int copy = 1; copy < value && power; ++copy) {
                            for (int x = 0; x < q; ++x) {
                                if (state[n - q + x] !=
                                    state[n - (copy + 1) * q + x]) {
                                    power = false;
                                    break;
                                }
                            }
                        }
                        if (power) {
                            mismatch_root = q;
                            break;
                        }
                    }
                    break;
                }
                state.push_back(P[j]);
            }
            if (mismatch == p) {
                ++fixed;
                if (first_fixed.empty()) first_fixed = digits(P);
            } else {
                ++internal;
                if (first_internal.empty()) {
                    first_internal = digits(P);
                    first_internal_j = mismatch;
                    first_internal_root = mismatch_root;
                }
            }
        }
        std::cout << p << " " << count << " " << fixed << " " << internal
                  << " " << (first_fixed.empty() ? "-" : first_fixed)
                  << " " << (first_internal.empty() ? "-" : first_internal)
                  << " " << first_internal_j << " " << first_internal_root
                  << "\n";
    }
}
