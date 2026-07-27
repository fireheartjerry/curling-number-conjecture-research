#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <random>
#include <string>
#include <vector>

static bool ends_power(
    const std::vector<unsigned char>& word,
    int cut,
    int root,
    int exponent
) {
    const int n = static_cast<int>(word.size());
    for (int offset = 0; offset < (exponent - 1) * root; ++offset) {
        int a = (cut - 1 - offset) % n;
        int b = (cut - 1 - offset - root) % n;
        if (a < 0) a += n;
        if (b < 0) b += n;
        if (word[a] != word[b]) return false;
    }
    return true;
}

static int proper_curl(
    const std::vector<unsigned char>& word,
    int cut,
    int maximum_symbol
) {
    const int n = static_cast<int>(word.size());
    int best = 1;
    for (int root = 1; root < n; ++root) {
        for (int exponent = 2; exponent <= maximum_symbol + 1; ++exponent) {
            if (!ends_power(word, cut, root, exponent)) break;
            best = std::max(best, exponent);
        }
    }
    return best;
}

static int score(
    const std::vector<unsigned char>& word,
    int maximum_symbol
) {
    const int n = static_cast<int>(word.size());
    std::vector<int> profile(n, 1);
    // For a fixed shift p, the equality indicator
    // word[t]==word[t-p] is n-periodic.  Scanning two cycles gives the exact
    // backward match length at every cut when word is primitive.  If p is
    // a global period, the resulting exponent already exceeds the alphabet
    // bound and is therefore safely a mismatch.
    for (int root = 1; root < n; ++root) {
        int run = 0;
        for (int t = 0; t < 2 * n; ++t) {
            if (word[t % n] == word[(t - root + n) % n]) {
                ++run;
            } else {
                run = 0;
            }
            if (t >= n) {
                const int cut = (t + 1) % n;
                profile[cut] =
                    std::max(profile[cut], 1 + run / root);
            }
        }
    }
    int result = 0;
    for (int cut = 0; cut < n; ++cut) {
        const int value = profile[cut];
        if (value != word[cut]) result += 1 + std::abs(value - word[cut]);
    }
    return result;
}

static bool primitive(const std::vector<unsigned char>& word) {
    const int n = static_cast<int>(word.size());
    for (int p = 1; p < n; ++p) {
        if (n % p != 0) continue;
        bool periodic = true;
        for (int i = p; i < n; ++i) {
            if (word[i] != word[i % p]) {
                periodic = false;
                break;
            }
        }
        if (periodic) return false;
    }
    return true;
}

static std::string render(const std::vector<unsigned char>& word) {
    std::string result;
    for (unsigned char value : word) {
        result += std::to_string(static_cast<int>(value));
    }
    return result;
}

int main(int argc, char** argv) {
    if (argc < 3 || argc > 6) {
        std::cerr
            << "usage: search_pc_fixed_k LENGTH MAX_SYMBOL "
            << "[RESTARTS] [ITERATIONS] [FIX_ENTRANCE]\n";
        return 2;
    }
    const int n = std::stoi(argv[1]);
    const int maximum_symbol = std::stoi(argv[2]);
    const int restarts = argc >= 4 ? std::stoi(argv[3]) : 200;
    const int iterations = argc >= 5 ? std::stoi(argv[4]) : 100000;
    const bool fix_entrance = argc >= 6 ? std::stoi(argv[5]) != 0 : true;
    const int entrance_length = maximum_symbol + 2;
    if (n < entrance_length || maximum_symbol < 4) return 2;

    std::mt19937_64 rng(0x4d41584c4142454cULL);
    std::uniform_real_distribution<double> unit(0.0, 1.0);
    int global_best = 4 * n;
    std::string best_word;

    for (int restart = 0; restart < restarts; ++restart) {
        std::vector<unsigned char> word(n);
        for (auto& value : word) {
            value = static_cast<unsigned char>(
                2 + rng() % static_cast<std::uint64_t>(maximum_symbol - 1)
            );
        }
        if (fix_entrance) {
            word[0] = static_cast<unsigned char>(maximum_symbol - 2);
            for (int i = 1; i <= maximum_symbol; ++i) {
                word[i] = static_cast<unsigned char>(maximum_symbol - 1);
            }
            word[maximum_symbol + 1] =
                static_cast<unsigned char>(maximum_symbol);
        }
        int current = score(word, maximum_symbol);
        for (int iteration = 0; iteration < iterations; ++iteration) {
            if (current == 0) break;
            const int first_mutable = fix_entrance ? entrance_length : 0;
            const int position =
                first_mutable + static_cast<int>(rng() % (n - first_mutable));
            const unsigned char old_value = word[position];
            unsigned char new_value = old_value;
            while (new_value == old_value) {
                new_value = static_cast<unsigned char>(
                    2 + rng() %
                        static_cast<std::uint64_t>(maximum_symbol - 1)
                );
            }
            word[position] = new_value;
            const int candidate = score(word, maximum_symbol);
            const double progress =
                static_cast<double>(iteration) / iterations;
            const double temperature = 2.0 * (1.0 - progress) + 0.03;
            if (
                candidate <= current ||
                unit(rng) < std::exp((current - candidate) / temperature)
            ) {
                current = candidate;
            } else {
                word[position] = old_value;
            }
            if (current < global_best) {
                global_best = current;
                best_word = render(word);
            }
        }
        if (current == 0 && primitive(word)) {
            std::cout << "fixed " << n << " " << render(word) << "\n";
            return 0;
        }
    }
    std::cout << "length " << n << " best " << global_best << " "
              << best_word << "\n";
    return 0;
}
