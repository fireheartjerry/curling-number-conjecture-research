#include <bits/stdc++.h>
using namespace std;

struct Event {
    int length;
    int exponent;
    int period;
    bool fully_generated_square;
    int bridge_period;
};

pair<int,int> curling_number_and_shortest_period(const vector<unsigned char>& s) {
    const int n = (int)s.size();
    if (n == 0) throw runtime_error("curling number requires a nonempty word");

    // Z-function of the reversed word. For a suffix period p,
    // 1 + Z[p]/p is the suffix exponent at period p.
    vector<int> z(n, 0);
    int left = 0, right = 0;
    auto rev_at = [&](int i) -> unsigned char { return s[n - 1 - i]; };
    for (int i = 1; i < n; ++i) {
        if (i < right) z[i] = min(right - i, z[i - left]);
        while (i + z[i] < n && rev_at(z[i]) == rev_at(i + z[i])) ++z[i];
        if (i + z[i] > right) {
            left = i;
            right = i + z[i];
        }
    }

    int best_k = 1;
    int best_p = n;
    for (int p = 1; p < n; ++p) {
        const int k = 1 + z[p] / p;
        if (k > best_k || (k == best_k && p < best_p)) {
            best_k = k;
            best_p = p;
        }
    }
    return {best_k, best_p};
}

vector<unsigned char> digits(const string& x) {
    vector<unsigned char> s;
    s.reserve(x.size());
    for (char c : x) {
        if (c != '2' && c != '3') throw runtime_error("binary word must use only 2 and 3");
        s.push_back((unsigned char)(c - '0'));
    }
    return s;
}

int total_length_before_first_one(vector<unsigned char> s, int max_steps = 100000) {
    for (int step = 0; step <= max_steps; ++step) {
        auto [k, p] = curling_number_and_shortest_period(s);
        if (k == 1) return (int)s.size();
        if (k != 2 && k != 3) throw runtime_error("calibration orbit hit a value other than 1,2,3");
        s.push_back((unsigned char)k);
    }
    throw runtime_error("calibration max_steps exceeded");
}

void calibrate() {
    const vector<pair<string,int>> cases = {
        {"322", 5},
        {"23222323", 66},
        {"2322322323222323223223", 142},
    };
    for (const auto& [seed, expected] : cases) {
        int actual = total_length_before_first_one(digits(seed));
        if (actual != expected) {
            throw runtime_error("calibration failed for " + seed + ": expected " +
                                to_string(expected) + ", got " + to_string(actual));
        }
    }
    cerr << "Calibration passed: total pre-1 lengths 5, 66, 142.\n";
}

string mask_word(uint64_t mask, int n) {
    string s;
    s.reserve(n);
    for (int i = 0; i < n; ++i) s.push_back(((mask >> i) & 1ULL) ? '3' : '2');
    return s;
}

bool primitive_mask(uint64_t mask, int n) {
    for (int d = 1; d < n; ++d) if (n % d == 0) {
        bool periodic = true;
        for (int i = d; i < n; ++i) {
            if (((mask >> i) & 1ULL) != ((mask >> (i % d)) & 1ULL)) {
                periodic = false;
                break;
            }
        }
        if (periodic) return false;
    }
    return true;
}

using PairKey = tuple<int,int,int,int>; // (P1,q1,P2,q2)

void audit_all_binary_seeds(int max_n, int max_steps, int min_n) {
    map<PairKey,long long> counts;
    map<PairKey,string> example;
    long long seeds = 0, pairs = 0;

    for (int seed_length = min_n; seed_length <= max_n; ++seed_length) {
        if (seed_length >= 63) throw runtime_error("mask enumeration supports lengths below 63");
        const uint64_t total = 1ULL << seed_length;
        for (uint64_t mask = 0; mask < total; ++mask) {
            ++seeds;
            vector<unsigned char> s;
            s.reserve(seed_length + max_steps + 2);
            for (int i = 0; i < seed_length; ++i)
                s.push_back(((mask >> i) & 1ULL) ? 3 : 2);

            int global_record = 0;
            vector<int> periods;
            periods.reserve(max_steps + 2);
            Event previous_record{-1,-1,-1,false,-1};

            for (int step = 0; step <= max_steps; ++step) {
                auto [k,p] = curling_number_and_shortest_period(s);
                const int n = (int)s.size();
                periods.push_back(p); // index = n-seed_length

                if (p > global_record) {
                    global_record = p;
                    const bool fully = (k == 2 && n - p >= seed_length);
                    const int bridge = fully ? periods[(n - p) - seed_length] : -1;
                    Event current{n,k,p,fully,bridge};

                    if (previous_record.length >= 0 && previous_record.exponent == 2 &&
                        current.exponent == 2 && previous_record.fully_generated_square &&
                        current.fully_generated_square) {
                        ++pairs;
                        PairKey key{previous_record.period, previous_record.bridge_period,
                                    current.period, current.bridge_period};
                        ++counts[key];
                        example.emplace(key, mask_word(mask, seed_length));
                        if (current.bridge_period > previous_record.bridge_period) {
                            cout << "COUNTEREXAMPLE seed_length=" << seed_length
                                 << " seed=" << mask_word(mask, seed_length)
                                 << " first=" << previous_record.period << "/"
                                 << previous_record.bridge_period
                                 << " second=" << current.period << "/"
                                 << current.bridge_period << "\n";
                            return;
                        }
                    }
                    previous_record = current;
                }

                if (k != 2 && k != 3) break;
                s.push_back((unsigned char)k);
            }
        }
        cerr << "all-seeds n=" << seed_length << " cumulative_seeds=" << seeds
             << " cumulative_pairs=" << pairs << " kinds=" << counts.size() << "\n";
    }

    cout << "NO_COUNTEREXAMPLE all-seeds min_n=" << min_n << " max_n=" << max_n
         << " seeds=" << seeds << " pairs=" << pairs << " kinds=" << counts.size() << "\n";
    for (const auto& [key,count] : counts) {
        auto [P1,q1,P2,q2] = key;
        cout << P1 << "/" << q1 << " -> " << P2 << "/" << q2
             << " count=" << count << " example=" << example[key] << "\n";
    }
}

void audit_exact_power_seeds(int max_root, int max_steps, int exponent, int min_root) {
    map<PairKey,long long> counts;
    map<PairKey,string> example;
    long long masks = 0, valid = 0, pairs = 0;

    for (int root_length = min_root; root_length <= max_root; ++root_length) {
        if (root_length >= 63) throw runtime_error("mask enumeration supports lengths below 63");
        const uint64_t total = 1ULL << root_length;
        for (uint64_t mask = 0; mask < total; ++mask) {
            ++masks;
            if (!primitive_mask(mask, root_length)) continue;

            vector<unsigned char> s;
            s.reserve(exponent * root_length + max_steps + 2);
            for (int rep = 0; rep < exponent; ++rep)
                for (int i = 0; i < root_length; ++i)
                    s.push_back(((mask >> i) & 1ULL) ? 3 : 2);

            auto [initial_k, initial_p] = curling_number_and_shortest_period(s);
            if (initial_k != exponent || initial_p != root_length) continue;
            ++valid;

            const int seed_length = (int)s.size();
            int global_record = 0;
            vector<int> periods;
            Event previous_record{-1,-1,-1,false,-1};

            for (int step = 0; step <= max_steps; ++step) {
                auto [k,p] = curling_number_and_shortest_period(s);
                const int n = (int)s.size();
                periods.push_back(p);
                if (p > global_record) {
                    global_record = p;
                    const bool fully = (k == 2 && n - p >= seed_length);
                    const int bridge = fully ? periods[(n - p) - seed_length] : -1;
                    Event current{n,k,p,fully,bridge};
                    if (previous_record.length >= 0 && previous_record.exponent == 2 &&
                        current.exponent == 2 && previous_record.fully_generated_square &&
                        current.fully_generated_square) {
                        ++pairs;
                        PairKey key{previous_record.period, previous_record.bridge_period,
                                    current.period, current.bridge_period};
                        ++counts[key];
                        example.emplace(key, mask_word(mask, root_length));
                        if (current.bridge_period > previous_record.bridge_period) {
                            cout << "COUNTEREXAMPLE exact-power exponent=" << exponent
                                 << " root_length=" << root_length
                                 << " root=" << mask_word(mask, root_length)
                                 << " first=" << previous_record.period << "/"
                                 << previous_record.bridge_period
                                 << " second=" << current.period << "/"
                                 << current.bridge_period << "\n";
                            return;
                        }
                    }
                    previous_record = current;
                }
                if (k != 2 && k != 3) break;
                s.push_back((unsigned char)k);
            }
        }
        cerr << "power exponent=" << exponent << " root_length=" << root_length
             << " masks=" << masks << " valid=" << valid << " pairs=" << pairs << "\n";
    }

    cout << "NO_COUNTEREXAMPLE exact-power exponent=" << exponent
         << " min_root=" << min_root << " max_root=" << max_root
         << " masks=" << masks << " valid=" << valid << " pairs=" << pairs << "\n";
    for (const auto& [key,count] : counts) {
        auto [P1,q1,P2,q2] = key;
        cout << P1 << "/" << q1 << " -> " << P2 << "/" << q2
             << " count=" << count << " example_root=" << example[key] << "\n";
    }
}

int main(int argc, char** argv) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    try {
        calibrate();
        if (argc < 2) {
            cerr << "Usage:\n"
                 << "  " << argv[0] << " all-seeds MAX_N [MAX_STEPS=600] [MIN_N=1]\n"
                 << "  " << argv[0] << " power MAX_ROOT EXPONENT [MAX_STEPS=600] [MIN_ROOT=1]\n";
            return 2;
        }
        const string mode = argv[1];
        if (mode == "all-seeds") {
            if (argc < 3) throw runtime_error("all-seeds requires MAX_N");
            audit_all_binary_seeds(stoi(argv[2]), argc >= 4 ? stoi(argv[3]) : 600,
                                   argc >= 5 ? stoi(argv[4]) : 1);
        } else if (mode == "power") {
            if (argc < 4) throw runtime_error("power requires MAX_ROOT and EXPONENT");
            audit_exact_power_seeds(stoi(argv[2]), argc >= 5 ? stoi(argv[4]) : 600,
                                    stoi(argv[3]), argc >= 6 ? stoi(argv[5]) : 1);
        } else {
            throw runtime_error("unknown mode: " + mode);
        }
    } catch (const exception& e) {
        cerr << "ERROR: " << e.what() << "\n";
        return 1;
    }
    return 0;
}
