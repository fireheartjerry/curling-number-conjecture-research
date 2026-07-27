// Search exact all-square segments of a canonical value-2 copy-parent ray.
//
// A state consists of a finite word W whose curling number is exactly two
// and whose least maximizing root is A.  If 0 < r < |A|, the only possible
// larger square root of length |A|+r on the next ray edge is
//
//     B = suffix_r(A) A.
//
// We append B, recompute the curling number from the full word (not merely
// from B^2), and retain the child only when its curling number is exactly two
// and B is again the least maximizing root.

#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>

using Word = std::vector<int>;

struct Curl {
    int exponent;
    int least_root;
};

static bool equal_blocks(const Word& w, int a, int b, int len) {
    for (int j = 0; j < len; ++j) {
        if (w[a + j] != w[b + j]) return false;
    }
    return true;
}

static Curl curl(const Word& w) {
    const int n = static_cast<int>(w.size());
    int best = 1;
    int least = n;
    for (int p = 1; p <= n; ++p) {
        int copies = 1;
        for (int start = n - 2 * p; start >= 0; start -= p) {
            if (!equal_blocks(w, start, n - p, p)) break;
            ++copies;
        }
        if (copies > best) {
            best = copies;
            least = p;
        } else if (copies == best && p < least) {
            least = p;
        }
    }
    return {best, least};
}

static std::string encode(const Word& w) {
    std::string s;
    s.reserve(w.size());
    for (int x : w) s.push_back(static_cast<char>('0' + x));
    return s;
}

struct State {
    Word word;
    Word root;
    std::vector<int> roots;
    std::vector<int> extensions;
};

static void enumerate_binary_roots(
    int pos, Word& a, int max_len, std::vector<State>& states) {
    const int n = static_cast<int>(a.size());
    if (pos == n - 1) {
        a[pos] = 2;
        Word w = {9};
        w.insert(w.end(), a.begin(), a.end());
        w.insert(w.end(), a.begin(), a.end());
        Curl c = curl(w);
        if (c.exponent == 2 && c.least_root == n) {
            states.push_back({w, a, {n}, {}});
        }
        return;
    }
    for (int x : {2, 3}) {
        a[pos] = x;
        enumerate_binary_roots(pos + 1, a, max_len, states);
    }
}

int main(int argc, char** argv) {
    int max_initial = argc > 1 ? std::stoi(argv[1]) : 10;
    int depth = argc > 2 ? std::stoi(argv[2]) : 30;
    int beam = argc > 3 ? std::stoi(argv[3]) : 2000;

    std::vector<State> states;
    for (int n = 2; n <= max_initial; ++n) {
        Word a(n, 2);
        a.front() = 2;
        enumerate_binary_roots(1, a, max_initial, states);
    }
    std::cout << "initial=" << states.size() << "\n";

    for (int level = 0; level < depth && !states.empty(); ++level) {
        std::vector<State> next;
        for (const State& st : states) {
            const int d = static_cast<int>(st.root.size());
            for (int r = 1; r < d; ++r) {
                if (st.root[d - r] != 2) continue;
                Word b(st.root.end() - r, st.root.end());
                b.insert(b.end(), st.root.begin(), st.root.end());
                Word q = st.word;
                q.insert(q.end(), b.begin(), b.end());
                Curl c = curl(q);
                if (c.exponent != 2 ||
                    c.least_root != static_cast<int>(b.size())) {
                    continue;
                }
                State child{std::move(q), std::move(b), st.roots,
                            st.extensions};
                child.roots.push_back(static_cast<int>(child.root.size()));
                child.extensions.push_back(r);
                next.push_back(std::move(child));
            }
        }

        std::sort(next.begin(), next.end(), [](const State& x, const State& y) {
            if (x.root.size() != y.root.size())
                return x.root.size() < y.root.size();
            return x.word.size() < y.word.size();
        });
        std::unordered_set<std::string> seen;
        states.clear();
        for (State& st : next) {
            std::string key = encode(st.root);
            if (!seen.insert(key).second) continue;
            states.push_back(std::move(st));
            if (static_cast<int>(states.size()) == beam) break;
        }
        if (states.empty()) {
            std::cout << "dead_after=" << level << "\n";
            break;
        }
        const State& best = states.front();
        std::cout << "level=" << (level + 1)
                  << " states=" << states.size()
                  << " root=" << best.root.size()
                  << " word=" << best.word.size()
                  << " roots=";
        for (int x : best.roots) std::cout << x << ",";
        std::cout << " ext=";
        for (int x : best.extensions) std::cout << x << ",";
        std::cout << "\n";
    }

    if (!states.empty()) {
        const State& best = states.front();
        std::cout << "best_root_word=" << encode(best.root) << "\n";
        std::cout << "best_full_word=" << encode(best.word) << "\n";
    }
}
