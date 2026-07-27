#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <random>
#include <string>
#include <vector>

static const std::string TOKEN_ENCODING =
    "0010200100101001020010200100101";
static const std::vector<unsigned char> ENTRANCE = {2,3,3,3,3,4};

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

static std::vector<unsigned char> expand(
    const std::array<std::vector<unsigned char>, 3>& images
) {
    std::vector<unsigned char> q;
    for (char token : TOKEN_ENCODING) {
        const auto& image = images[token - '0'];
        q.insert(q.end(), image.begin(), image.end());
    }
    return q;
}

static int score(
    const std::array<std::vector<unsigned char>, 3>& images,
    std::vector<int>* failures = nullptr
) {
    const auto q = expand(images);
    int result = 0;
    if (failures != nullptr) failures->clear();
    for (int cut = 0; cut < static_cast<int>(q.size()); ++cut) {
        const int actual = proper_curl(q, cut);
        if (actual != q[cut]) {
            result += 1 + std::abs(actual - q[cut]);
            if (failures != nullptr) failures->push_back(cut);
        }
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
    std::mt19937_64& rng
) {
    for (auto& x : block) x = static_cast<unsigned char>(2 + rng() % 3);
    block[0] = 2;
    std::copy(ENTRANCE.begin(), ENTRANCE.end(), block.end() - 6);
}

static std::vector<int> mutable_positions(int length) {
    std::vector<int> result;
    for (int i = 1; i < length - 6; ++i) result.push_back(i);
    return result;
}

int main(int argc, char** argv) {
    if (argc < 4 || argc > 6) {
        std::cerr << "usage: search_u31_lift L0 L1 L2 "
                  << "[RESTARTS] [ITERATIONS]\n";
        return 2;
    }
    const std::array<int, 3> lengths = {
        std::stoi(argv[1]), std::stoi(argv[2]), std::stoi(argv[3])
    };
    const int restarts = argc >= 5 ? std::stoi(argv[4]) : 100;
    const int iterations = argc >= 6 ? std::stoi(argv[5]) : 50000;
    for (int length : lengths) {
        if (length < 8) return 2;
    }

    std::mt19937_64 rng(0x5533314c494654ULL);
    std::uniform_real_distribution<double> unit(0.0, 1.0);
    std::array<std::vector<int>, 3> mutable_positions_by_image;
    for (int a = 0; a < 3; ++a) {
        mutable_positions_by_image[a] = mutable_positions(lengths[a]);
    }

    int global_best = 1000000000;
    std::array<std::string, 3> best_images;
    std::vector<int> best_failures;
    for (int restart = 0; restart < restarts; ++restart) {
        std::array<std::vector<unsigned char>, 3> images;
        for (int a = 0; a < 3; ++a) {
            images[a].resize(lengths[a]);
            initialize(images[a], rng);
        }
        int current = score(images);
        for (int iteration = 0; iteration < iterations; ++iteration) {
            if (current == 0) break;
            const int image_index = static_cast<int>(rng() % 3);
            const auto& positions =
                mutable_positions_by_image[image_index];
            if (positions.empty()) continue;
            auto& image = images[image_index];
            const int position = positions[rng() % positions.size()];
            const unsigned char old_value = image[position];
            unsigned char new_value = old_value;
            while (new_value == old_value) {
                new_value = static_cast<unsigned char>(2 + rng() % 3);
            }
            image[position] = new_value;
            const int candidate = score(images);
            const double progress =
                static_cast<double>(iteration) / iterations;
            const double temperature = 3.0 * (1.0 - progress) + 0.03;
            if (
                candidate <= current ||
                unit(rng) < std::exp((current - candidate) / temperature)
            ) {
                current = candidate;
            } else {
                image[position] = old_value;
            }
            if (current < global_best) {
                global_best = current;
                for (int a = 0; a < 3; ++a) {
                    best_images[a] = render(images[a]);
                }
                score(images, &best_failures);
                std::cout << "best=" << global_best
                          << " raw_length=" << expand(images).size()
                          << " failures=" << best_failures.size()
                          << " first="
                          << (best_failures.empty() ? -1 : best_failures[0])
                          << " images=(" << best_images[0] << ","
                          << best_images[1] << "," << best_images[2]
                          << ")\n";
            }
        }
        if (current == 0) {
            std::cout << "FIXED LIFT FOUND\n";
            return 0;
        }
    }
    std::cout << "lengths=" << lengths[0] << "," << lengths[1]
              << "," << lengths[2] << " best=" << global_best
              << " failures=" << best_failures.size()
              << " images=(" << best_images[0] << ","
              << best_images[1] << "," << best_images[2] << ")\n";
    return 0;
}
