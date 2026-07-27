#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>

static bool primitive(const std::vector<int>& word) {
    const int n = static_cast<int>(word.size());
    for (int p = 1; p < n; ++p) {
        if (n % p != 0) continue;
        bool power = true;
        for (int i = p; i < n; ++i) {
            if (word[i] != word[i % p]) {
                power = false;
                break;
            }
        }
        if (power) return false;
    }
    return true;
}

static int proper_cyclic_curl(
    const std::vector<int>& word,
    const int cut,
    const int root_cap
) {
    const int q = static_cast<int>(word.size());
    std::vector<int> state;
    state.reserve(2 * q + cut);
    state.insert(state.end(), word.begin(), word.end());
    state.insert(state.end(), word.begin(), word.end());
    state.insert(state.end(), word.begin(), word.begin() + cut);

    const int n = static_cast<int>(state.size());
    int best = 1;
    for (int p = 1; p < q && p <= root_cap; ++p) {
        int copies = 1;
        int cursor = n - 2 * p;
        while (cursor >= 0) {
            bool equal = true;
            for (int j = 0; j < p; ++j) {
                if (state[cursor + j] != state[n - p + j]) {
                    equal = false;
                    break;
                }
            }
            if (!equal) break;
            ++copies;
            cursor -= p;
        }
        if (copies > best) best = copies;
    }
    return best;
}

int main(int argc, char** argv) {
    if (argc < 2 || argc > 3) {
        std::cerr << "usage: search_proper_cyclic_fixed LENGTH [ROOT_CAP]\n";
        return 2;
    }
    const int q = std::atoi(argv[1]);
    const int root_cap = argc == 3 ? std::atoi(argv[2]) : q - 1;
    if (q <= 0 || q >= 63) {
        std::cerr << "LENGTH must lie in [1,62]\n";
        return 2;
    }

    const std::uint64_t count = std::uint64_t{1} << q;
    std::uint64_t found = 0;
    std::uint64_t squareful_fourth_free = 0;
    for (std::uint64_t bits = 0; bits < count; ++bits) {
        std::vector<int> word;
        word.reserve(q);
        for (int i = 0; i < q; ++i) {
            word.push_back(2 + static_cast<int>((bits >> i) & 1));
        }
        if (!primitive(word)) continue;

        bool fixed = true;
        bool squareful = true;
        for (int cut = 0; cut < q; ++cut) {
            const int value = proper_cyclic_curl(word, cut, root_cap);
            if (value < 2 || value > 3) {
                squareful = false;
            }
            if (value != word[cut]) {
                fixed = false;
            }
        }
        if (squareful) ++squareful_fourth_free;
        if (!fixed) continue;

        ++found;
        std::cout << "word=";
        for (int value : word) std::cout << value;
        std::cout << "\n";
    }
    std::cout << "length=" << q
              << " root_cap=" << root_cap
              << " squareful_fourth_free=" << squareful_fourth_free
              << " found=" << found << "\n";
    return 0;
}
