"""Exact component quotient for an all-long gap-four pair cycle.

The selected high pair ends at cut zero.  Its incoming cube has root
length ``r``.  A loss square of root ``q`` copies it to the first low
pair, and the incoming cube supplies the second low pair, so

    N = q + 2*r.

Unlike the singleton-marker quotient, every selected endpoint carries
the complete pair word ``222322232`` and every cut from the left unary
cube through the right marker is required to have its exact 2/3 profile.

This is a research enumerator.  A SAT result is independently checked
with the exhaustive proper-circular-profile implementation.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE / ".vendor"))
sys.path.insert(0, str(ROOT))

from z3 import And, Bool, BoolVal, Not, Or, Solver, is_true, sat  # type: ignore

from check_terminal_marker_ancestry import checked_cn, primitive, proper_cut


PAIR = tuple(map(int, "222322232"))


class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))

    def find(self, item: int) -> int:
        item %= len(self.parent)
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, left: int, right: int) -> None:
        left = self.find(left)
        right = self.find(right)
        if left != right:
            self.parent[right] = left


@dataclass(frozen=True)
class Geometry:
    incoming: int
    outgoing: int
    length: int
    component_count: int
    forced_component_count: int
    difference: int


def add_power_equalities(
    quotient: UnionFind,
    cut: int,
    exponent: int,
    root: int,
) -> None:
    for block in range(2, exponent + 1):
        for offset in range(root):
            quotient.union(
                cut - block * root + offset,
                cut - root + offset,
            )


def quotient_forces_power(
    quotient: UnionFind,
    cut: int,
    exponent: int,
    root: int,
) -> bool:
    return all(
        quotient.find(cut - block * root + offset)
        == quotient.find(cut - root + offset)
        for block in range(2, exponent + 1)
        for offset in range(root)
    )


def base_geometry(
    incoming: int,
    outgoing: int,
) -> tuple[Geometry, UnionFind, dict[int, int]] | None:
    """Return the equality quotient and forced colors, or inconsistency."""

    if not (9 <= outgoing < 3 * incoming and incoming >= 9):
        return None
    length = outgoing + 2 * incoming
    quotient = UnionFind(length)
    add_power_equalities(quotient, 0, 3, incoming)
    add_power_equalities(quotient, outgoing, 2, outgoing)
    add_power_equalities(
        quotient,
        outgoing + incoming,
        2,
        incoming,
    )

    endpoints = (0, outgoing, outgoing + incoming)
    forced_positions: list[tuple[int, int]] = []
    for endpoint in endpoints:
        forced_positions.extend(
            (endpoint - len(PAIR) + offset, value)
            for offset, value in enumerate(PAIR)
        )
    forced_positions.extend(
        (
            (0, 3),
            (outgoing, 2),
            (outgoing + incoming, 2),
            (-3 * incoming - 1, 3),
        )
    )

    forced: dict[int, int] = {}
    for position, value in forced_positions:
        component = quotient.find(position)
        previous = forced.get(component)
        if previous is not None and previous != value:
            return None
        forced[component] = value

    components = {quotient.find(index) for index in range(length)}
    geometry = Geometry(
        incoming=incoming,
        outgoing=outgoing,
        length=length,
        component_count=len(components),
        forced_component_count=len(forced),
        difference=incoming - outgoing,
    )
    return geometry, quotient, forced


def solve_geometry(
    incoming: int,
    outgoing: int,
    extra_cuts: tuple[int, ...] = (),
    singleton_three: bool = False,
) -> tuple[Geometry, tuple[int, ...]] | None:
    base = base_geometry(incoming, outgoing)
    if base is None:
        return None
    geometry, quotient, forced = base
    length = geometry.length
    component_ids = sorted(
        {quotient.find(index) for index in range(length)}
    )
    variables = {
        component: Bool(
            f"x_{incoming}_{outgoing}_{component}"
        )
        for component in component_ids
    }
    solver = Solver()
    for component, value in forced.items():
        solver.add(variables[component] if value == 3 else Not(variables[component]))

    power_cache = {}

    def letter(position: int):
        return variables[quotient.find(position)]

    if singleton_three:
        for position in range(length):
            solver.add(
                Not(And(letter(position), letter(position + 1)))
            )

    def power(cut: int, exponent: int, root: int):
        key = (cut % length, exponent, root)
        if key in power_cache:
            return power_cache[key]
        comparisons = {
            (
                quotient.find(cut - block * root + offset),
                quotient.find(cut - root + offset),
            )
            for block in range(2, exponent + 1)
            for offset in range(root)
        }
        clauses = [
            variables[left] == variables[right]
            for left, right in comparisons
            if left != right
        ]
        result = And(*clauses) if clauses else BoolVal(True)
        power_cache[key] = result
        return result

    def some_power(cut: int, exponent: int):
        return Or(
            *(power(cut, exponent, root) for root in range(1, length))
        )

    def exact_profile(cut: int):
        return And(
            some_power(cut, 2),
            letter(cut) == some_power(cut, 3),
            Not(some_power(cut, 4)),
        )

    # The pair ending at e contains unary leaves at e-6 and e-2,
    # marker endpoints at e-4 and e, and all intervening generated cuts.
    # Requiring every offset -6,...,0 is stronger than merely requiring
    # the four landmark cuts and is exactly what contraction needs.
    endpoints = (0, outgoing, outgoing + incoming)
    pair_profile_cuts = {
        (endpoint + offset) % length
        for endpoint in endpoints
        for offset in range(-6, 1)
    }
    for cut in pair_profile_cuts:
        solver.add(exact_profile(cut))
    for cut in extra_cuts:
        solver.add(exact_profile(cut))

    # Circular primitivity.
    for period in range(1, length):
        if length % period == 0:
            solver.add(
                Or(
                    *(
                        letter(index) != letter(index % period)
                        for index in range(period, length)
                    )
                )
            )

    if solver.check() != sat:
        return None
    model = solver.model()
    word = tuple(
        3 if is_true(model.eval(letter(index), model_completion=True)) else 2
        for index in range(length)
    )

    # Independent exhaustive audit of every cut imposed above and every
    # selected long witness.
    assert primitive(word)
    for endpoint in endpoints:
        factor = (
            word[endpoint - len(PAIR) : endpoint]
            if endpoint
            else word[-len(PAIR) :]
        )
        assert factor == PAIR
    assert incoming in proper_cut(word, 0)[1]
    assert outgoing in proper_cut(word, outgoing)[1]
    assert incoming in proper_cut(word, outgoing + incoming)[1]
    for cut in pair_profile_cuts:
        assert proper_cut(word, cut)[0] == word[cut]
    for cut in extra_cuts:
        assert proper_cut(word, cut % length)[0] == word[cut % length]

    # Independent normal-form and border-object audit.
    difference = incoming - outgoing
    incoming_root = word[-incoming:]
    assert incoming_root[:difference] == incoming_root[outgoing:]
    assert incoming_root[-len(PAIR) :] == PAIR
    assert incoming_root[difference] == 3
    assert incoming_root[outgoing - 1] == 3
    if difference < len(PAIR):
        assert difference in (1, 5)
    else:
        border_object = incoming_root[:difference]
        assert border_object[-len(PAIR) :] == PAIR
        assert checked_cn(border_object) == 2
    return geometry, word


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-r", type=int, default=24)
    parser.add_argument("--models", action="store_true")
    parser.add_argument("--cut-one", action="store_true")
    parser.add_argument("--prefix", type=int, default=0)
    parser.add_argument(
        "--singleton-three",
        action="store_true",
        help="exclude every circular adjacent pair 33",
    )
    args = parser.parse_args()

    equality_survivors: list[Geometry] = []
    exact_survivors: list[tuple[Geometry, tuple[int, ...]]] = []
    for incoming in range(9, args.max_r + 1):
        for outgoing in range(9, 3 * incoming):
            base = base_geometry(incoming, outgoing)
            if base is None:
                continue
            equality_survivors.append(base[0])
            extra_cuts = tuple(range(1, args.prefix + 1))
            if args.cut_one and 1 not in extra_cuts:
                extra_cuts = (1,) + extra_cuts
            solved = solve_geometry(
                incoming,
                outgoing,
                extra_cuts,
                args.singleton_three,
            )
            if solved is not None:
                exact_survivors.append(solved)

    assert all(
        geometry.outgoing < geometry.incoming
        for geometry in equality_survivors
    )
    assert all(
        geometry.component_count == geometry.outgoing
        for geometry in equality_survivors
    )
    assert all(
        geometry.difference >= len(PAIR)
        or geometry.difference in (1, 5)
        for geometry in equality_survivors
    )
    # At the high endpoint of the prefix-border occurrence, cut 2r,
    # a whole-border cube delta<=s<r/2 is never already implied by the
    # base quotient.  It therefore spends at least one equality-component
    # merge.
    for geometry in equality_survivors:
        base = base_geometry(geometry.incoming, geometry.outgoing)
        assert base is not None
        _, quotient, _ = base
        for root in range(
            geometry.difference,
            (geometry.incoming - 1) // 2 + 1,
        ):
            assert not quotient_forces_power(
                quotient,
                2 * geometry.incoming,
                3,
                root,
            )
    print(
        "equality_survivors",
        tuple(
            (
                item.incoming,
                item.outgoing,
                item.difference,
                item.component_count,
                item.forced_component_count,
            )
            for item in equality_survivors
        ),
    )
    print(
        "exact_survivor_geometries",
        tuple(
            (
                geometry.incoming,
                geometry.outgoing,
                geometry.difference,
                geometry.length,
            )
            for geometry, _ in exact_survivors
        ),
    )
    if args.models:
        for geometry, word in exact_survivors:
            print(
                "model",
                geometry,
                "".join(map(str, word)),
            )


if __name__ == "__main__":
    main()
