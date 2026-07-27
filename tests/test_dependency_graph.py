import itertools
import math
import unittest

from curling import curling_number
from research.dependency_graph import (
    canonical_vertices,
    finite_orbit_prefix,
    maximizing_root_lengths,
)


class DependencyGraphTests(unittest.TestCase):
    def test_maximizing_root_lengths_are_complete(self):
        for length in range(1, 9):
            for sequence in itertools.product((2, 3), repeat=length):
                exponent = curling_number(sequence)
                expected = tuple(
                    root_length
                    for root_length in range(
                        1,
                        len(sequence) // exponent + 1,
                    )
                    if sequence[-exponent * root_length :]
                    == sequence[-root_length:] * exponent
                )
                self.assertEqual(
                    maximizing_root_lengths(sequence),
                    expected,
                )

    def test_canonical_parent_is_an_equal_earlier_position(self):
        for length in range(1, 9):
            for seed in itertools.product((2, 3), repeat=length):
                states, values = finite_orbit_prefix(seed, 80)
                word = seed + values
                for vertex in canonical_vertices(seed, 80):
                    self.assertLess(vertex.parent, vertex.position)
                    self.assertEqual(word[vertex.parent], word[vertex.position])
                    self.assertLessEqual(vertex.position, 2 * vertex.parent + 1)

                    following = states[vertex.time + 1]
                    root = following[-vertex.span :]
                    repeated_suffix = root * vertex.next_exponent
                    self.assertEqual(
                        following[-len(repeated_suffix) :],
                        repeated_suffix,
                    )
                    self.assertEqual(
                        vertex.next_exponent,
                        curling_number(following),
                    )

    def test_consecutive_copy_intervals_satisfy_overlap_dichotomy(self):
        for length in range(1, 9):
            for seed in itertools.product((2, 3), repeat=length):
                vertices = canonical_vertices(seed, 80)
                by_position = {vertex.position: vertex for vertex in vertices}
                for child in vertices:
                    parent = by_position.get(child.parent)
                    if parent is None:
                        continue

                    old_span = parent.span
                    new_span = child.span
                    old_exponent = parent.next_exponent
                    new_exponent = child.next_exponent
                    common_divisor = math.gcd(old_span, new_span)

                    if old_span != new_span:
                        upward = (
                            new_span
                            > (old_exponent - 1) * old_span + common_divisor
                        )
                        downward = (
                            old_span
                            > (new_exponent - 2) * new_span + common_divisor
                        )
                        self.assertTrue(upward or downward)

                    old_left = (
                        parent.position
                        - old_exponent * old_span
                        + 1
                    )
                    new_left = (
                        child.position
                        - new_exponent * new_span
                        + 1
                    )
                    if new_exponent == 2:
                        self.assertGreater(new_left, old_left)

    def test_record_cube_left_endpoints_need_not_decrease(self):
        seed = tuple(map(int, "2322232232223223"))
        vertices = canonical_vertices(seed, 200)
        by_position = {
            vertex.position: vertex
            for vertex in vertices
            if vertex.value == 2
        }

        ray = []
        vertex = by_position[75]
        while vertex is not None:
            ray.append(vertex)
            vertex = by_position.get(vertex.parent)
        ray.reverse()

        record_cubes = []
        record_span = 0
        for vertex in ray:
            if (
                vertex.next_exponent == 3
                and vertex.span > record_span
            ):
                left = vertex.position - 3 * vertex.span + 1
                record_cubes.append((vertex.position, vertex.span, left))
                record_span = vertex.span

        self.assertEqual(record_cubes, [(20, 7, 0), (75, 21, 13)])


if __name__ == "__main__":
    unittest.main()
