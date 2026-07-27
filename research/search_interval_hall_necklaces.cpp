// Exhaustively search primitive binary circular words modulo rotation for
// failures of the interval-Hall condition implemented in
// analyze_profile_variation.cpp.
//
// The Fredricksen-Kessler-Maiorana recursion below emits exactly one
// lexicographically least representative of every binary necklace.  Its
// parameter p is the least rotational period, so p == n selects precisely
// the primitive circular words.  Proper profiles and Hall candidates are
// then recomputed by the independent exact routines in the included file.

#define main analyze_profile_variation_main
#include "analyze_profile_variation.cpp"
#undef main

#include <functional>

struct SearchCounts {
    std::uint64_t primitive_necklaces = 0;
    std::uint64_t admissible_necklaces = 0;
    std::uint64_t handle_matching_failures = 0;
    std::uint64_t pre_hall_failures = 0;
    std::uint64_t interval_hall_failures = 0;
};

static void print_word(const std::vector<int>& word) {
    for (int x : word) std::cout << x;
}

static int mobius(int value) {
    int prime_factors = 0;
    for (int prime = 2; prime * prime <= value; ++prime) {
        if (value % prime) continue;
        value /= prime;
        ++prime_factors;
        if (value % prime == 0) return 0;
        while (value % prime == 0) value /= prime;
    }
    if (value > 1) ++prime_factors;
    return prime_factors % 2 ? -1 : 1;
}

static std::uint64_t expected_primitive_necklaces(int n) {
    std::int64_t primitive_words = 0;
    for (int divisor = 1; divisor <= n; ++divisor) {
        if (n % divisor) continue;
        primitive_words +=
            static_cast<std::int64_t>(mobius(divisor))
            * static_cast<std::int64_t>(
                std::uint64_t{1} << (n / divisor));
    }
    return static_cast<std::uint64_t>(primitive_words / n);
}

static SearchCounts search_necklaces(int n, bool stop_first) {
    SearchCounts counts;
    std::vector<int> digits(n + 1, 0);
    bool stopped = false;

    auto process = [&](const std::vector<int>& word) {
        ++counts.primitive_necklaces;
        std::vector<int> profile(n);
        for (int cut = 0; cut < n; ++cut) {
            profile[cut] = proper_curl(word, cut);
            if (profile[cut] < 2 || profile[cut] > 3) return;
        }

        ++counts.admissible_necklaces;
        const bool matched = profile_handle_matching(word, profile);
        counts.handle_matching_failures += !matched;
        counts.pre_hall_failures += !matched && last_interval_hall;
        if (!last_interval_hall) {
            ++counts.interval_hall_failures;
            std::cout << "interval-hall-failure=";
            print_word(word);
            std::cout << " profile=";
            print_word(profile);
            std::cout << "\n";
            stopped = stop_first;
        }
    };

    // FKM fixed-content recursion specialized to the binary alphabet.
    // At a leaf, digits[1..n] is the lexicographically least rotation,
    // and p is its least rotational period.
    std::function<void(int, int)> generate = [&](int t, int p) {
        if (stopped) return;
        if (t > n) {
            if (p != n) return;
            std::vector<int> word(n);
            for (int i = 0; i < n; ++i) word[i] = 2 + digits[i + 1];
            process(word);
            return;
        }

        digits[t] = digits[t - p];
        generate(t + 1, p);
        for (int digit = digits[t - p] + 1; digit <= 1; ++digit) {
            digits[t] = digit;
            generate(t + 1, t);
        }
    };

    generate(1, 1);
    if (!stopped
        && counts.primitive_necklaces != expected_primitive_necklaces(n)) {
        std::cerr << "necklace-count calibration failed\n";
        std::exit(3);
    }
    std::cout << "length=" << n
              << " primitive_necklaces=" << counts.primitive_necklaces
              << " admissible_necklaces=" << counts.admissible_necklaces
              << " handle_matching_failures="
              << counts.handle_matching_failures
              << " pre_hall_failures=" << counts.pre_hall_failures
              << " interval_hall_failures="
              << counts.interval_hall_failures
              << " stopped_early=" << (stopped ? 1 : 0) << "\n";
    return counts;
}

int main(int argc, char** argv) {
    if (argc < 2 || argc > 3) {
        std::cerr
            << "usage: search_interval_hall_necklaces LENGTH [--stop-first]\n";
        return 2;
    }
    const int n = std::atoi(argv[1]);
    if (n <= 0 || n >= 63) return 2;
    const bool stop_first =
        argc == 3 && std::string(argv[2]) == "--stop-first";
    if (argc == 3 && !stop_first) return 2;
    search_necklaces(n, stop_first);
    return 0;
}
