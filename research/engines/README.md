# Verification engines

Drafting-aid scripts used to machine-verify the letter arithmetic in the
2026-07-28/29 p>q campaign (see docs/DECISION_LOG.md). Preserved here at
user request for continuation on another machine; they are evidence
tools, not proof dependencies. The proofs stand in the research notes.

- forced_replay.py       tame forced-replay table (r=4 seed 223222323)
- horn2_geography.py     phase-2 horn-2 pin/correlation survey (r=4)
- zoo_targeted.py        r=4 shallow zoo: union-find consistency plus
                         branch-on-demand replay of all 52,880 cases
- zoo_total2.py          exhaustive per-q token DFS over all Q (r=4)
- p21_tree.py            post-exit continuation tree explorer (draft;
                         superseded by the phase-51 wall)
- r5_filters.py          r>=5 catalogue cut filters S7/S8/S11/S12; the
                         committed run also used S16 (no fourth powers)
                         and S20/S21 (B^2 3, B^3 3 suffix-cube-free),
                         reported in research/pgtq_r5_cut_filters.md
- r13_zoo.py             B-generic small-q zoo DFS, parametrized by the
                         bridge word (B, t); prepared for the two r=13
                         survivors, NOT YET RUN
- fix_stars.py           repair tool for the local formatter corruption
                         documented in the 2026-07-28 decision entry

Python 3, no dependencies beyond the repository curling.py.
