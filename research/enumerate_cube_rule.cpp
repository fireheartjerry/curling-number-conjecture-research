#include <cstdint>
#include <iostream>
#include <string>

static bool primitive(std::uint64_t w, int n) {
    for (int d = 1; d < n; ++d) {
        if (n % d) continue;
        bool same = true;
        for (int i = d; i < n; ++i) {
            if (((w >> i) & 1ULL) != ((w >> (i % d)) & 1ULL)) {
                same = false;
                break;
            }
        }
        if (same) return false;
    }
    return true;
}

static bool eq(std::uint64_t w, int n, int a, int b) {
    a %= n; if (a < 0) a += n;
    b %= n; if (b < 0) b += n;
    return ((w >> a) & 1ULL) == ((w >> b) & 1ULL);
}

static bool power(std::uint64_t w, int n, int cut, int q, int e) {
    for (int k = 1; k < e; ++k) {
        for (int j = 0; j < q; ++j) {
            if (!eq(w, n, cut - q + j, cut - (k + 1) * q + j)) return false;
        }
    }
    return true;
}

int main(int argc, char** argv) {
    int max_n = argc > 1 ? std::stoi(argv[1]) : 25;
    for (int n = 1; n <= max_n; ++n) {
        std::uint64_t count = 0, example = 0;
        const std::uint64_t lim = 1ULL << n;
        for (std::uint64_t w = 0; w < lim; ++w) {
            if (!primitive(w, n)) continue;
            bool ok = true;
            for (int c = 0; c < n && ok; ++c) {
                bool cube = false, fourth = false;
                for (int q = 1; q < n; ++q) {
                    if (power(w, n, c, q, 3)) cube = true;
                    if (power(w, n, c, q, 4)) fourth = true;
                }
                const bool bit = (w >> c) & 1ULL;
                if (bit != (cube && !fourth) || fourth) ok = false;
            }
            if (ok) {
                ++count;
                if (!example) example = w;
            }
        }
        std::string s;
        if (count) for (int i = 0; i < n; ++i) s += ((example >> i) & 1ULL) ? '3' : '2';
        std::cout << n << " " << count << " " << s << "\n";
    }
}
