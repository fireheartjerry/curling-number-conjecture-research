#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

static const std::string TOKEN_WORD =
    "0020010010100100020010010100100020010";
static const std::vector<unsigned char> E = {2,3,3,3,3,4};

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

static std::vector<unsigned char> expand(
    const std::vector<unsigned char>& r0,
    const std::vector<unsigned char>& r1,
    const std::vector<unsigned char>& r2
) {
    std::vector<unsigned char> q;
    for (char token : TOKEN_WORD) {
        const auto& block = token == '0' ? r0 : token == '1' ? r1 : r2;
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

static std::string render(const std::vector<unsigned char>& word) {
    std::string result;
    for (unsigned char x : word) result.push_back(static_cast<char>('0' + x));
    return result;
}

int main(int argc, char** argv) {
    if (argc != 4) {
        std::cerr << "usage: enumerate_u37_lifts LEN_R0 LEN_R1 LEN_R2\n";
        return 2;
    }
    const int a = std::stoi(argv[1]);
    const int b = std::stoi(argv[2]);
    const int c = std::stoi(argv[3]);
    if (a < 6 || b < 6 || c < 7 || a > 25 || b > 25 || c > 25) return 2;
    const auto ca = assignments(a);
    const auto cb = assignments(b);
    const auto cc = assignments(c);
    std::uint64_t tested = 0;
    int best = 1000000000;
    std::string best0, best1, best2;
    for (std::uint64_t xa = 0; xa < ca; ++xa) {
        const auto r0 = block_from_code(a, 2, xa);
        for (std::uint64_t xb = 0; xb < cb; ++xb) {
            const auto r1 = block_from_code(b, 2, xb);
            if (r0 == r1) continue;
            for (std::uint64_t xc = 0; xc < cc; ++xc) {
                const auto r2 = block_from_code(c, 3, xc);
                const auto q = expand(r0, r1, r2);
                const int current = score(q);
                ++tested;
                if (current < best) {
                    best = current;
                    best0 = render(r0);
                    best1 = render(r1);
                    best2 = render(r2);
                }
                if (current == 0) {
                    std::cout << "fixed q=" << q.size()
                              << " R0=" << best0 << " R1=" << best1
                              << " R2=" << best2 << "\n";
                    return 0;
                }
            }
        }
    }
    std::cout << "a=" << a << " b=" << b << " c=" << c
              << " q=" << 25*a+9*b+3*c << " tested=" << tested
              << " best=" << best << " R0=" << best0
              << " R1=" << best1 << " R2=" << best2 << "\n";
    return 0;
}
