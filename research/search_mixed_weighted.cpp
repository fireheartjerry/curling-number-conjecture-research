#include <algorithm>
#include <array>
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
    int cut
) {
    const int n = static_cast<int>(word.size());
    int best = 1;
    for (int root = 1; root < n; ++root) {
        for (int exponent = 2; exponent <= 4; ++exponent) {
            if (!ends_power(word, cut, root, exponent)) break;
            best = std::max(best, exponent);
        }
    }
    return best;
}

static int score(
    const std::vector<unsigned char>& word,
    const std::array<int, 3>& weights
) {
    int result = 0;
    std::array<int, 3> counts = {0, 0, 0};
    for (unsigned char value : word) ++counts[value];
    for (int count : counts) {
        if (count == 0) result += 2 * static_cast<int>(word.size());
    }
    for (int cut = 0; cut < static_cast<int>(word.size()); ++cut) {
        const int value = proper_curl(word, cut);
        const int wanted = weights[word[cut]];
        if (value != wanted) result += 1 + std::abs(value - wanted);
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
        result += static_cast<char>('0' + value);
    }
    return result;
}

int main(int argc, char** argv) {
    if (argc < 3 || argc > 5) {
        std::cerr << "usage: search_mixed_weighted LENGTH WEIGHTS "
                  << "[RESTARTS] [ITERATIONS]\n";
        return 2;
    }
    const int n = std::stoi(argv[1]);
    const std::string weight_encoding = argv[2];
    if (n < 1 || weight_encoding.size() != 3) return 2;
    std::array<int, 3> weights;
    for (int a = 0; a < 3; ++a) {
        weights[a] = weight_encoding[a] - '0';
        if (weights[a] < 2 || weights[a] > 3) return 2;
    }
    if (
        std::all_of(weights.begin(), weights.end(),
                    [](int x) { return x == 2; }) ||
        std::all_of(weights.begin(), weights.end(),
                    [](int x) { return x == 3; })
    ) return 2;
    const int restarts = argc >= 4 ? std::stoi(argv[3]) : 200;
    const int iterations = argc >= 5 ? std::stoi(argv[4]) : 100000;

    std::mt19937_64 rng(
        0x4d495845445750ULL ^ static_cast<std::uint64_t>(n)
    );
    std::uniform_real_distribution<double> unit(0.0, 1.0);
    int global_best = 10 * n;
    std::string best_word;
    for (int restart = 0; restart < restarts; ++restart) {
        std::vector<unsigned char> word(n);
        for (auto& value : word) {
            value = static_cast<unsigned char>(rng() % 3);
        }
        int current = score(word, weights);
        for (int iteration = 0; iteration < iterations; ++iteration) {
            if (current == 0) break;
            const int position = static_cast<int>(rng() % n);
            const unsigned char old_value = word[position];
            unsigned char new_value = old_value;
            while (new_value == old_value) {
                new_value = static_cast<unsigned char>(rng() % 3);
            }
            word[position] = new_value;
            const int candidate = score(word, weights);
            const double progress =
                static_cast<double>(iteration) / iterations;
            const double temperature = 3.0 * (1.0 - progress) + 0.02;
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
                std::cout << "length=" << n << " weights="
                          << weight_encoding << " best=" << global_best
                          << " word=" << best_word << "\n";
            }
        }
        if (current == 0 && primitive(word)) {
            std::cout << "MIXED COUNTERMODEL " << n << " "
                      << weight_encoding << " " << render(word) << "\n";
            return 0;
        }
    }
    std::cout << "done length=" << n << " weights=" << weight_encoding
              << " best=" << global_best << " word=" << best_word << "\n";
    return 0;
}
