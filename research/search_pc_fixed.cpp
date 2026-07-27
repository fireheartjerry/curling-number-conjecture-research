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
    int cut
) {
    const int n = static_cast<int>(word.size());
    bool has_square = false;
    bool has_cube = false;
    for (int root = 1; root < n; ++root) {
        if (!ends_power(word, cut, root, 2)) continue;
        has_square = true;
        if (!ends_power(word, cut, root, 3)) continue;
        has_cube = true;
        if (ends_power(word, cut, root, 4)) return 4;
    }
    if (has_cube) return 3;
    if (has_square) return 2;
    return 1;
}

static int score(const std::vector<unsigned char>& word) {
    int result = 0;
    for (int cut = 0; cut < static_cast<int>(word.size()); ++cut) {
        if (proper_curl(word, cut) != word[cut]) ++result;
    }
    return result;
}

static std::string render(const std::vector<unsigned char>& word) {
    std::string result;
    for (unsigned char value : word) {
        result.push_back(static_cast<char>('0' + value));
    }
    return result;
}

static int least_period(const std::vector<unsigned char>& word) {
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
        if (periodic) return p;
    }
    return n;
}

int main(int argc, char** argv) {
    const int minimum_length = argc >= 2 ? std::stoi(argv[1]) : 25;
    const int maximum_length = argc >= 3 ? std::stoi(argv[2]) : 80;
    const int restarts = argc >= 4 ? std::stoi(argv[3]) : 200;
    const int iterations = argc >= 5 ? std::stoi(argv[4]) : 20000;
    std::mt19937_64 rng(0xC0FFEEULL);
    std::uniform_real_distribution<double> unit(0.0, 1.0);

    for (int n = minimum_length; n <= maximum_length; ++n) {
        int global_best = n + 1;
        std::string best_word;
        for (int restart = 0; restart < restarts; ++restart) {
            std::vector<unsigned char> word(n);
            for (auto& value : word) value = 2 + (rng() & 1ULL);
            int current = score(word);
            for (int iteration = 0; iteration < iterations; ++iteration) {
                if (current == 0) break;
                const int position = static_cast<int>(rng() % n);
                word[position] = 5 - word[position];
                const int candidate = score(word);
                const double temperature =
                    1.5 * (1.0 - static_cast<double>(iteration) / iterations)
                    + 0.02;
                if (candidate <= current ||
                    unit(rng) < std::exp((current - candidate) / temperature)) {
                    current = candidate;
                } else {
                    word[position] = 5 - word[position];
                }
                if (current < global_best) {
                    global_best = current;
                    best_word = render(word);
                }
            }
            if (current == 0 && least_period(word) == n) {
                std::cout << "fixed " << n << " " << render(word) << "\n";
                break;
            }
        }
        std::cout << "length " << n << " best " << global_best
                  << " " << best_word << "\n";
    }
}
