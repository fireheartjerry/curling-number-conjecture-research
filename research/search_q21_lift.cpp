#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <vector>

static const std::vector<int> TOKENS = {
    2,2,3,2,2,2,3,2,2,2,3,2,3,2,2,2,3,2,2,2,3
};
static const std::vector<unsigned char> ENTRANCE = {2,3,3,3,3,4};

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

static std::vector<unsigned char> expand(
    const std::vector<unsigned char>& r2,
    const std::vector<unsigned char>& r3
) {
    std::vector<unsigned char> q;
    for (int token : TOKENS) {
        const auto& block = token == 2 ? r2 : r3;
        q.insert(q.end(), block.begin(), block.end());
    }
    return q;
}

static bool power(
    const std::vector<unsigned char>& q,
    int cut,
    int root,
    int exponent
) {
    const int n = static_cast<int>(q.size());
    for (int block = 2; block <= exponent; ++block) {
        for (int j = 0; j < root; ++j) {
            int a = (cut - block * root + j) % n;
            int b = (cut - root + j) % n;
            if (a < 0) a += n;
            if (b < 0) b += n;
            if (q[a] != q[b]) return false;
        }
    }
    return true;
}

static int proper_curl(
    const std::vector<unsigned char>& q,
    int cut
) {
    const int n = static_cast<int>(q.size());
    int best = 1;
    for (int root = 1; root < n; ++root) {
        for (int exponent = 2; exponent <= 5; ++exponent) {
            if (!power(q, cut, root, exponent)) break;
            best = std::max(best, exponent);
        }
    }
    return best;
}

static int score(
    const std::vector<unsigned char>& r2,
    const std::vector<unsigned char>& r3
) {
    const auto q = expand(r2, r3);
    const int n = static_cast<int>(q.size());
    std::vector<int> profile(n, 1);
    for (int root = 1; root < n; ++root) {
        int run = 0;
        for (int t = 0; t < 2 * n; ++t) {
            if (q[t % n] == q[(t - root + n) % n]) {
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
        const int actual = profile[cut];
        result += actual == q[cut] ? 0 : 1 + std::abs(actual - q[cut]);
    }
    return result;
}

static std::string render(const std::vector<unsigned char>& word) {
    std::string result;
    for (unsigned char value : word) result += std::to_string(value);
    return result;
}

static void initialize(
    std::vector<unsigned char>& block,
    int first,
    std::mt19937_64& rng
) {
    for (auto& x : block) x = static_cast<unsigned char>(2 + rng() % 3);
    block[0] = static_cast<unsigned char>(first);
    std::copy(ENTRANCE.begin(), ENTRANCE.end(), block.end() - 6);
}

static std::vector<int> mutable_positions(int length) {
    std::vector<int> result;
    for (int i = 1; i < length - 6; ++i) result.push_back(i);
    return result;
}

int main(int argc, char** argv) {
    if (argc < 3 || argc > 5) {
        std::cerr << "usage: search_q21_lift LEN_R2 LEN_R3 "
                  << "[RESTARTS] [ITERATIONS]\n";
        return 2;
    }
    const int a = std::stoi(argv[1]);
    const int b = std::stoi(argv[2]);
    const int restarts = argc >= 4 ? std::stoi(argv[3]) : 100;
    const int iterations = argc >= 5 ? std::stoi(argv[4]) : 50000;
    if (a < 7 || b < 7) return 2;

    std::mt19937_64 rng(0x5132314c494654ULL);
    std::uniform_real_distribution<double> unit(0.0, 1.0);
    const auto mutable2 = mutable_positions(a);
    const auto mutable3 = mutable_positions(b);
    if (mutable2.empty() && mutable3.empty()) return 2;

    int global_best = 1000000000;
    std::string best2, best3;
    for (int restart = 0; restart < restarts; ++restart) {
        std::vector<unsigned char> r2(a), r3(b);
        initialize(r2, 2, rng);
        initialize(r3, 3, rng);
        int current = score(r2, r3);
        for (int iteration = 0; iteration < iterations; ++iteration) {
            if (current == 0) break;
            const bool choose2 =
                !mutable2.empty() &&
                (mutable3.empty() || (rng() & 1ULL) == 0);
            auto& block = choose2 ? r2 : r3;
            const auto& positions = choose2 ? mutable2 : mutable3;
            const int position = positions[rng() % positions.size()];
            const unsigned char old_value = block[position];
            unsigned char new_value = old_value;
            while (new_value == old_value) {
                new_value = static_cast<unsigned char>(2 + rng() % 3);
            }
            block[position] = new_value;
            const int candidate = score(r2, r3);
            const double progress =
                static_cast<double>(iteration) / iterations;
            const double temperature = 3.0 * (1.0 - progress) + 0.03;
            if (
                candidate <= current ||
                unit(rng) < std::exp((current - candidate) / temperature)
            ) {
                current = candidate;
            } else {
                block[position] = old_value;
            }
            if (current < global_best) {
                global_best = current;
                best2 = render(r2);
                best3 = render(r3);
            }
        }
        if (current == 0) {
            const auto q = expand(r2, r3);
            std::cout << "fixed raw_length=" << q.size()
                      << " primitive=" << primitive(q)
                      << " R2=" << render(r2)
                      << " R3=" << render(r3) << "\n";
            return 0;
        }
    }
    std::cout << "a=" << a << " b=" << b
              << " raw_length=" << (15 * a + 6 * b)
              << " best=" << global_best
              << " R2=" << best2 << " R3=" << best3 << "\n";
    return 0;
}
