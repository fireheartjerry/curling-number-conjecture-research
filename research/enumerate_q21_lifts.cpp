#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

static const std::string TOKEN_WORD = "223222322232322232223";
static const std::vector<unsigned char> E = {2,3,3,3,3,4};

static std::vector<unsigned char> expand(
    const std::vector<unsigned char>& r2,
    const std::vector<unsigned char>& r3
) {
    std::vector<unsigned char> q;
    for (char token : TOKEN_WORD) {
        const auto& block = token == '2' ? r2 : r3;
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

static int proper_curl(const std::vector<unsigned char>& q, int cut) {
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

static int score(const std::vector<unsigned char>& q) {
    int result = 0;
    for (int cut = 0; cut < static_cast<int>(q.size()); ++cut) {
        if (proper_curl(q, cut) != q[cut]) ++result;
    }
    return result;
}

static std::vector<unsigned char> block_from_code(
    int length,
    int first,
    std::uint64_t code
) {
    std::vector<unsigned char> block(length, 2);
    block[0] = static_cast<unsigned char>(first);
    std::copy(E.begin(), E.end(), block.end() - 6);
    for (int i = 1; i < length - 6; ++i) {
        block[i] = static_cast<unsigned char>(2 + code % 3);
        code /= 3;
    }
    return block;
}

static std::uint64_t assignments(int length) {
    std::uint64_t result = 1;
    for (int i = 1; i < length - 6; ++i) result *= 3;
    return result;
}

int main(int argc, char** argv) {
    if (argc != 3) {
        std::cerr << "usage: enumerate_q21_lifts LEN_R2 LEN_R3\n";
        return 2;
    }
    const int a = std::stoi(argv[1]);
    const int b = std::stoi(argv[2]);
    if (a < 6 || b < 7 || a > 25 || b > 25) return 2;
    const std::uint64_t count2 = assignments(a);
    const std::uint64_t count3 = assignments(b);
    std::uint64_t tested = 0;
    int best = 1000000000;
    std::string best2, best3;
    for (std::uint64_t code2 = 0; code2 < count2; ++code2) {
        const auto r2 = block_from_code(a, 2, code2);
        for (std::uint64_t code3 = 0; code3 < count3; ++code3) {
            const auto r3 = block_from_code(b, 3, code3);
            const auto q = expand(r2, r3);
            const int current = score(q);
            ++tested;
            if (current < best) {
                best = current;
                best2.assign(r2.begin(), r2.end());
                best3.assign(r3.begin(), r3.end());
                for (char& x : best2) x = static_cast<char>('0' + x);
                for (char& x : best3) x = static_cast<char>('0' + x);
            }
            if (current == 0) {
                std::cout << "fixed a=" << a << " b=" << b
                          << " R2=" << best2 << " R3=" << best3 << "\n";
                return 0;
            }
        }
    }
    std::cout << "a=" << a << " b=" << b
              << " raw_length=" << 15*a+6*b
              << " tested=" << tested << " best_mismatches=" << best
              << " R2=" << best2 << " R3=" << best3 << "\n";
    return 0;
}
