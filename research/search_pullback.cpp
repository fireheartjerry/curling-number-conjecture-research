#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

static int curl_and_roots(
    const std::vector<int>& word,
    std::vector<int>* roots
) {
    const int n = static_cast<int>(word.size());
    int best = 1;
    roots->clear();
    for (int p = 1; p <= n; ++p) {
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
        if (copies > best) {
            best = copies;
            roots->clear();
            roots->push_back(p);
        } else if (copies == best) {
            roots->push_back(p);
        }
    }
    return best;
}

static std::vector<int> digits(const std::string& text) {
    std::vector<int> result;
    for (char value : text) result.push_back(value - '0');
    return result;
}

static std::string render(const std::vector<int>& word) {
    std::string result;
    for (int value : word) result.push_back(static_cast<char>('0' + value));
    return result;
}

int main() {
    const std::vector<int> target = digits("223222322232322232223");
    const int p = static_cast<int>(target.size());
    std::uint64_t count = 0;
    int minimum_crossing_root = p + 1;
    std::vector<int> minimizing_word;
    std::vector<int> roots;
    std::uint64_t internal_relocations = 0;
    int minimum_internal_crossing_root = p + 1;
    std::vector<int> minimizing_internal_word;
    int minimizing_internal_offset = -1;
    int minimizing_internal_root = -1;
    for (std::uint64_t bits = 0; bits < (1ULL << p); ++bits) {
        std::vector<int> state(p);
        for (int i = 0; i < p; ++i) {
            state[i] = 2 + static_cast<int>((bits >> i) & 1ULL);
        }
        int maximum_crossing_root = 0;
        bool matches = true;
        for (int j = 0; j < p; ++j) {
            const int value = curl_and_roots(state, &roots);
            if (value != target[j]) {
                matches = false;
                break;
            }
            for (int root : roots) {
                if (value * root > j) {
                    maximum_crossing_root =
                        std::max(maximum_crossing_root, root);
                }
            }
            state.push_back(value);
        }
        if (!matches) continue;
        ++count;
        if (maximum_crossing_root < minimum_crossing_root) {
            minimum_crossing_root = maximum_crossing_root;
            minimizing_word.assign(state.begin(), state.begin() + p);
        }

        // The state now ends in P.  Check that it emits a second P, so
        // those two generated copies form the square under study.
        for (int j = 0; j < p; ++j) {
            const int value = curl_and_roots(state, &roots);
            if (value != target[j]) {
                matches = false;
                break;
            }
            state.push_back(value);
        }
        if (!matches) continue;

        // Compare the attempted third copy.  Record only a first mismatch
        // whose maximizing cube lies wholly to the right of the generated
        // square origin.
        for (int j = 0; j < p; ++j) {
            const int value = curl_and_roots(state, &roots);
            if (value == target[j]) {
                state.push_back(value);
                continue;
            }
            if (target[j] == 2 && value == 3) {
                for (int root : roots) {
                    const int relative_origin = 2 * p + j - 3 * root;
                    if (relative_origin >= 0) {
                        ++internal_relocations;
                        if (maximum_crossing_root <
                            minimum_internal_crossing_root) {
                            minimum_internal_crossing_root =
                                maximum_crossing_root;
                            minimizing_internal_word.assign(
                                state.begin(), state.begin() + p
                            );
                            minimizing_internal_offset = j;
                            minimizing_internal_root = root;
                        }
                        break;
                    }
                }
            }
            break;
        }
    }
    std::cout << "preimages " << count << "\n";
    std::cout << "minimum_maximum_crossing_root "
              << minimum_crossing_root << "\n";
    std::cout << "witness " << render(minimizing_word) << "\n";
    std::cout << "internal_relocations " << internal_relocations << "\n";
    std::cout << "minimum_internal_prior_crossing_root "
              << minimum_internal_crossing_root << "\n";
    std::cout << "internal_witness " << render(minimizing_internal_word)
              << " offset " << minimizing_internal_offset
              << " root " << minimizing_internal_root << "\n";
}
