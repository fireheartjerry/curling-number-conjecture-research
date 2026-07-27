"""Executed audit for the deleted-cube profile inheritance note."""

from __future__ import annotations

from itertools import product


def power_roots(word: tuple[int, ...], cut: int, exponent: int) -> tuple[int, ...]:
    n = len(word)
    roots = []
    for root in range(1, n):
        reference = tuple(word[(cut - root + offset) % n] for offset in range(root))
        if all(
            tuple(
                word[(cut - block * root + offset) % n]
                for offset in range(root)
            )
            == reference
            for block in range(2, exponent + 1)
        ):
            roots.append(root)
    return tuple(roots)


def exact_profile_at(
    word: tuple[int, ...], cut: int
) -> tuple[int, tuple[int, ...]]:
    n = len(word)
    best = 1
    maximizing: list[int] = []
    for root in range(1, n):
        exponent = 1
        reference = tuple(word[(cut - root + offset) % n] for offset in range(root))
        while exponent <= n:
            next_block = tuple(
                word[(cut - (exponent + 1) * root + offset) % n]
                for offset in range(root)
            )
            if next_block != reference:
                break
            exponent += 1
        if exponent > best:
            best = exponent
            maximizing = [root]
        elif exponent == best:
            maximizing.append(root)
    return best, tuple(maximizing)


def primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return all(
        any(word[index] != word[index % period] for index in range(period, n))
        for period in range(1, n)
        if n % period == 0
    )


def deleted_cube(root: tuple[int, ...]) -> tuple[int, ...]:
    return root[1:] + root + root


def aligned_cuts(root_length: int, phase: int) -> tuple[int, int, int]:
    circumference = 3 * root_length - 1
    return tuple(
        (phase - 1 + copy * root_length) % circumference for copy in range(3)
    )


def audit_examples() -> None:
    root = tuple(map(int, "232"))
    macro = deleted_cube(root)
    assert macro == tuple(map(int, "32232232"))
    assert exact_profile_at(macro, 0) == (3, (3,))
    assert exact_profile_at(root, 0)[0] == 1
    cuts = aligned_cuts(len(root), 0)
    assert cuts == (7, 2, 5)
    assert tuple(exact_profile_at(macro, cut) for cut in cuts) == (
        (2, (3,)),
        (2, (2,)),
        (2, (3, 5)),
    )

    terminal_root = tuple(map(int, "2322232"))
    terminal_macro = deleted_cube(terminal_root)
    assert terminal_macro == tuple(map(int, "32223223222322322232"))
    assert terminal_root[-5:] == tuple(map(int, "22232"))
    terminal_phase = len(terminal_root) - 1
    assert exact_profile_at(terminal_root, terminal_phase)[0] == 1
    terminal_cuts = aligned_cuts(len(terminal_root), terminal_phase)
    assert terminal_cuts == (5, 12, 19)
    assert tuple(exact_profile_at(terminal_macro, cut) for cut in terminal_cuts) == (
        (2, (6,)),
        (2, (13,)),
        (2, (7,)),
    )
    assert tuple(exact_profile_at(terminal_macro, cut)[0] for cut in range(20)) == (
        3,
        2,
        2,
        2,
        3,
        2,
        2,
        2,
        2,
        2,
        2,
        3,
        2,
        2,
        2,
        2,
        2,
        2,
        3,
        2,
    )


def audit_structural_identities() -> None:
    # Exhaust all binary primitive roots through length ten.  This checks
    # the concrete embedding behind Lemma 1 and the structural late
    # root-r square at every phase.
    for root_length in range(2, 11):
        for root in product((2, 3), repeat=root_length):
            if not primitive(root) or root[0] != root[-1]:
                continue
            macro = deleted_cube(root)
            for phase in range(root_length):
                late_cut = aligned_cuts(root_length, phase)[2]
                assert root_length in power_roots(macro, late_cut, 2)
                assert exact_profile_at(root, phase)[0] <= exact_profile_at(
                    macro, late_cut
                )[0]

    # The canonical seam mask is a formal identity for every A in
    # B=2A2 (equivalently C=rot_left(B)=A22).  Exhaustive
    # symbolic-letter surrogates are unnecessary:
    # testing every binary A through total root length ten exercises all
    # equality patterns, including repeated A.
    for root_length in range(3, 11):
        for middle in product((2, 3), repeat=root_length - 2):
            root = (2,) + middle + (2,)
            macro = deleted_cube(root)
            phase = root_length - 1
            cuts = aligned_cuts(root_length, phase)
            expected = (root_length - 1, 2 * root_length - 1, root_length)
            for cut, period in zip(cuts, expected):
                assert period in power_roots(macro, cut, 2)


def audit_smallest_local_failure() -> None:
    failures = []
    for root_length in range(2, 4):
        for middle in product((2, 3), repeat=max(0, root_length - 2)):
            root = (2,) + middle + (2,)
            if len(root) != root_length or root[1] != 3 or not primitive(root):
                continue
            macro = deleted_cube(root)
            if exact_profile_at(macro, 0)[0] != 3:
                continue
            for phase in range(root_length):
                cuts = aligned_cuts(root_length, phase)
                if (
                    all(
                        exact_profile_at(macro, cut)[0] == root[phase]
                        for cut in cuts
                    )
                    and exact_profile_at(root, phase)[0] != root[phase]
                ):
                    failures.append((root_length, root, phase, cuts))
    assert failures == [
        (3, (2, 3, 2), 0, (7, 2, 5)),
        (3, (2, 3, 2), 2, (1, 4, 7)),
    ]


def quotient_component_count(root_length: int, short_root: int) -> int:
    circumference = 3 * root_length - 1
    parent = list(range(circumference))

    def find(index: int) -> int:
        index %= circumference
        if parent[index] != index:
            parent[index] = find(parent[index])
        return parent[index]

    def union(left: int, right: int) -> None:
        left_root = find(left)
        right_root = find(right)
        if left_root != right_root:
            parent[right_root] = left_root

    representatives: dict[int, int] = {}
    for position in range(circumference):
        root_phase = (position + 1) % root_length
        if root_phase in representatives:
            union(position, representatives[root_phase])
        else:
            representatives[root_phase] = position
    union(representatives[0], representatives[root_length - 1])

    cut = root_length - 2
    for offset in range(short_root):
        union(cut - 2 * short_root + offset, cut - short_root + offset)
    return len({find(position) for position in range(circumference)})


def audit_short_terminal_repairs() -> None:
    # Exact equality-component formula (15).
    for root_length in range(4, 51):
        for short_root in range(1, root_length - 1):
            assert quotient_component_count(root_length, short_root) == (
                root_length - 1 - short_root
            )
        assert quotient_component_count(root_length, root_length - 1) == (
            root_length - 1
        )

    terminal = tuple(map(int, "23222332322232"))
    terminal_macro = deleted_cube(terminal)
    terminal_phase = len(terminal) - 1
    terminal_cuts = aligned_cuts(len(terminal), terminal_phase)
    assert terminal[-5:] == tuple(map(int, "22232"))
    assert exact_profile_at(terminal, terminal_phase)[0] == 1
    assert tuple(power_roots(terminal_macro, cut, 2) for cut in terminal_cuts) == (
        (7, 13),
        (27,),
        (14,),
    )
    assert all(
        exact_profile_at(terminal_macro, cut)[0] <= terminal_macro[cut]
        for cut in range(len(terminal_macro))
    )

    deep_root = tuple(map(int, "232332233232332"))
    deep_macro = deleted_cube(deep_root)
    deep_phase = 2
    deep_cuts = aligned_cuts(len(deep_root), deep_phase)
    assert exact_profile_at(deep_root, deep_phase)[0] == 1
    assert deep_root[deep_phase] == 2
    assert deep_cuts == (1, 16, 31)
    assert tuple(exact_profile_at(deep_macro, cut) for cut in deep_cuts) == (
        (2, (3, 5)),
        (2, (9,)),
        (2, (15,)),
    )
    assert all(
        exact_profile_at(deep_macro, cut)[0] <= deep_macro[cut]
        for cut in range(len(deep_macro))
    )


def no_merge_power(
    root_length: int, cut: int, exponent: int, power_root: int
) -> bool:
    circumference = 3 * root_length - 1

    def component(position: int) -> int:
        root_phase = ((position % circumference) + 1) % root_length
        return 0 if root_phase == root_length - 1 else root_phase

    return all(
        component(cut - block * power_root + offset)
        == component(cut - power_root + offset)
        for block in range(2, exponent + 1)
        for offset in range(power_root)
    )


def audit_no_merge_classification() -> None:
    for root_length in range(3, 51):
        circumference = 3 * root_length - 1
        cubes = {
            (cut, power_root)
            for cut in range(circumference)
            for power_root in range(1, circumference)
            if no_merge_power(root_length, cut, 3, power_root)
        }
        assert cubes == {(0, root_length)}

        squares = {
            (cut, power_root)
            for cut in range(circumference)
            for power_root in range(1, circumference)
            if no_merge_power(root_length, cut, 2, power_root)
        }
        expected_squares = {
            (0, root_length),
            (root_length - 2, root_length - 1),
            (root_length - 1, root_length - 1),
            (root_length, 1),
            (2 * root_length, 1),
            (2 * root_length - 2, 2 * root_length - 1),
            (2 * root_length - 1, 2 * root_length - 1),
        }
        expected_squares.update(
            (cut, root_length)
            for cut in range(2 * root_length - 1, 3 * root_length - 1)
        )
        assert squares == expected_squares

    quotient = tuple(map(int, "232223"))
    assert tuple(
        exact_profile_at(quotient, cut)[0] for cut in range(len(quotient))
    ) == (1, 1, 2, 2, 2, 3)


def main() -> None:
    audit_examples()
    audit_structural_identities()
    audit_smallest_local_failure()
    audit_short_terminal_repairs()
    audit_no_merge_classification()
    print(
        {
            "smallest_local_failure": {
                "root": "232",
                "macro": "32232232",
                "phase": 0,
                "aligned_cuts": (7, 2, 5),
            },
            "terminal_mask": {
                "root": "2322232",
                "macro": "32223223222322322232",
                "phase": 6,
                "roots": (6, 13, 7),
            },
            "structural_audit": "all primitive binary roots through length 10",
            "short_repair_component_formula": "all r through 50",
            "no_merge_power_classification": "all r through 50",
            "deep_repair_adversary": {
                "root": "232332233232332",
                "phase": 2,
                "aligned_roots": ((3, 5), (9,), (15,)),
            },
        }
    )


if __name__ == "__main__":
    main()
