#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

static const std::vector<int> E = {2, 3, 3, 3, 3, 4};

static int proper_curl(const std::vector<int>& w, const int cut) {
    const int n = static_cast<int>(w.size());
    int best = 1;
    for (int root = 1; root < n; ++root) {
        int exponent = 1;
        while (exponent < 5) {
            bool equal = true;
            for (int j = 0; j < root; ++j) {
                const int earlier =
                    (cut - (exponent + 1) * root + j) % n;
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
            ++exponent;
        }
        best = std::max(best, exponent);
        if (best >= 5) return best;
    }
    return best;
}

static bool equals_e_at(
    const std::vector<int>& word, const int start
) {
    const int n = static_cast<int>(word.size());
    for (int j = 0; j < static_cast<int>(E.size()); ++j) {
        const int index = ((start + j) % n + n) % n;
        if (word[index] != E[j]) return false;
    }
    return true;
}

static std::vector<std::vector<int>> candidates(const int maximum_length) {
    std::vector<std::vector<int>> result;
    for (int length = 6; length <= maximum_length; ++length) {
        const int free_length = length - 6;
        int cases = 1;
        for (int i = 0; i < free_length; ++i) cases *= 3;
        for (int code = 0; code < cases; ++code) {
            int x = code;
            std::vector<int> word(length);
            for (int i = 0; i < free_length; ++i) {
                word[i] = 2 + x % 3;
                x /= 3;
            }
            for (int i = 0; i < 6; ++i) {
                word[free_length + i] = E[i];
            }
            if (word[0] != 2) continue;
            bool internal_e = false;
            for (int start = 0; start + 6 < length; ++start) {
                bool equal = true;
                for (int j = 0; j < 6; ++j) {
                    if (word[start + j] != E[j]) {
                        equal = false;
                        break;
                    }
                }
                if (equal) internal_e = true;
            }
            if (!internal_e) result.push_back(word);
        }
    }
    return result;
}

static std::string render(const std::vector<int>& word) {
    std::string result;
    for (int symbol : word) {
        result.push_back(static_cast<char>('0' + symbol));
    }
    return result;
}

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "usage: search_return_lifts MAX_RETURN_LENGTH\n";
        return 2;
    }
    const int maximum_length = std::atoi(argv[1]);
    if (maximum_length < 6 || maximum_length > 14) return 2;

    // One representative of the unique length-31 model up to rotation
    // and token permutation.
    const std::string encoded = "0010200100101001020010200100101";
    std::vector<int> u;
    for (char symbol : encoded) u.push_back(symbol - '0');

    const auto words = candidates(maximum_length);
    std::uint64_t assignments = 0;
    std::uint64_t synchronized = 0;
    int best_agreement = -1;
    for (int i = 0; i < static_cast<int>(words.size()); ++i) {
        for (int j = 0; j < static_cast<int>(words.size()); ++j) {
            if (j == i) continue;
            for (int k = 0; k < static_cast<int>(words.size()); ++k) {
                if (k == i || k == j) continue;
                ++assignments;
                const std::vector<std::vector<int>> image = {
                    words[i], words[j], words[k]
                };
                std::vector<int> q;
                std::vector<int> expected_ends;
                for (int token : u) {
                    q.insert(
                        q.end(), image[token].begin(), image[token].end()
                    );
                    expected_ends.push_back(static_cast<int>(q.size()));
                }

                std::vector<int> actual_ends;
                for (int cut = 0; cut < static_cast<int>(q.size()); ++cut) {
                    if (equals_e_at(q, cut - 6)) actual_ends.push_back(cut);
                }
                std::sort(expected_ends.begin(), expected_ends.end());
                for (int& cut : expected_ends) cut %= q.size();
                std::sort(expected_ends.begin(), expected_ends.end());
                if (actual_ends != expected_ends) continue;
                ++synchronized;

                int agreement = 0;
                int first_failure = -1;
                int actual_value = -1;
                for (int cut = 0; cut < static_cast<int>(q.size()); ++cut) {
                    const int value = proper_curl(q, cut);
                    if (value != q[cut]) {
                        first_failure = cut;
                        actual_value = value;
                        break;
                    }
                    ++agreement;
                }
                if (agreement > best_agreement) {
                    best_agreement = agreement;
                    std::cout << "best=" << agreement << "/" << q.size()
                              << " first_failure=" << first_failure
                              << " actual=" << actual_value
                              << " wanted="
                              << (first_failure >= 0
                                  ? q[first_failure] : -1)
                              << " images=(" << render(words[i]) << ","
                              << render(words[j]) << ","
                              << render(words[k]) << ")\n";
                }
                if (first_failure < 0) {
                    std::cout << "LIFT FOUND\n";
                    return 0;
                }
            }
        }
    }
    std::cout << "candidates=" << words.size()
              << " assignments=" << assignments
              << " synchronized=" << synchronized
              << " best_agreement=" << best_agreement << "\n";
}
