import re
import os

ROOT = r"C:\Users\fireh\OneDrive\Documents\Curling Problem"
FILES = [
    r"research\pgtq_boundary_small_r.md",
    r"research\pgtq_r4_phase_two.md",
    r"research\pgtq_r4_horn2_geography.md",
    r"research\pgtq_r4_forced_replay.md",
    r"research\pgtq_r4_exit_root_kill.md",
    "CURRENT_STATUS.md",
    "FULL_PROOF_CHECKLIST.md",
]
pat = re.compile("([A-Za-z0-9])[*]([A-Za-z0-9" + chr(92) * 2 + "])")
total = 0
for rel in FILES:
    f = os.path.join(ROOT, rel)
    src = open(f, encoding="utf-8").read()
    fixed, n = pat.subn(r"\1_\2", src)
    if n:
        open(f, "w", encoding="utf-8", newline="\n").write(fixed)
    total += n
    print(rel, "fixed", n)

# repair the garbled Case paragraph in exit_root_kill
f = os.path.join(ROOT, r"research\pgtq_r4_exit_root_kill.md")
src = open(f, encoding="utf-8").read()
b = chr(92)  # backslash
start = src.index("_Case " + b + "(1" + b + "le j" + b + "le4" + b + ")._")
sq = b + "(" + b + "square" + b + ")"
end = src.index(sq, start) + len(sq)
L = lambda s: s.replace("~", b)  # ~ stands for backslash below
clean = L(
    "_Case ~(1~le j~le4~)._ Here ~(r_{j+s}=t_{n+j-4+s}~). Apply (R.1)\n"
    "at ~(p=n+j-4~le n~); this is admissible because\n"
    "~(s~ge~ell^*+4=n-4~) gives ~(2s~ge2n-8~ge n~ge n+j-4~) (using\n"
    "~(n~ge9~) and ~(j~le4~)). Hence ~(r_{j+s}=t_{n+j-4}~). But\n"
    "~(t_{n-3},t_{n-2},t_{n-1},t_n~) are the four leftmost tail letters\n"
    "read right-to-left, and the tail begins with\n"
    "~(B^2=~texttt{2232}~ldots~), so\n"
    "~((t_{n-3},t_{n-2},t_{n-1},t_n)=(2,3,2,2)~) — exactly reversed\n"
    "~(B=(r_1,r_2,r_3,r_4)~). Hence ~(r_{j+s}=r_j~). ~(~square~)"
)
src = src[:start] + clean + src[end:]
open(f, "w", encoding="utf-8", newline="\n").write(src)
print("case paragraph rewritten")

for rel in FILES:
    f = os.path.join(ROOT, rel)
    src = open(f, encoding="utf-8").read()
    bad = pat.findall(src)
    assert not bad, (rel, bad[:5])
print("ALL CLEAN, total fixes:", total)
