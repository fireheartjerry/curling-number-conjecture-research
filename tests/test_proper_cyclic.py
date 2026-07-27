import unittest

from curling import curling_number, curling_number_reference


P21 = tuple(map(int, "223222322232322232223"))


def proper_cyclic_profile(word):
    word = tuple(word)
    q = len(word)
    values = []
    least_maximizing_roots = []
    for cut in range(q):
        state = word * 2 + word[:cut]
        best = 1
        roots = []
        for root_length in range(1, q):
            copies = 1
            cursor = len(state) - 2 * root_length
            block = state[-root_length:]
            while (
                cursor >= 0
                and state[cursor : cursor + root_length] == block
            ):
                copies += 1
                cursor -= root_length
            if copies > best:
                best = copies
                roots = [root_length]
            elif copies == best:
                roots.append(root_length)
        values.append(best)
        least_maximizing_roots.append(min(roots))
    return tuple(values), tuple(least_maximizing_roots)


class ProperCyclicProfileTests(unittest.TestCase):
    def test_p21_is_fixed_at_every_rotation(self):
        for shift in range(len(P21)):
            rotation = P21[shift:] + P21[:shift]
            profile, _ = proper_cyclic_profile(rotation)
            self.assertEqual(profile, rotation)

    def test_p21_parent_cycles(self):
        _, roots = proper_cyclic_profile(P21)
        self.assertEqual(
            roots,
            (4, 4, 4, 3, 3, 1, 1, 7, 4, 1, 1, 4, 4, 2, 2, 1, 1, 6, 6, 1, 1),
        )

        q = len(P21)
        parent = tuple((cut - roots[cut]) % q for cut in range(q))
        self.assertEqual(
            tuple(parent[cut] for cut in (0, 17, 11, 7)),
            (17, 11, 7, 0),
        )
        self.assertEqual(
            tuple(parent[cut] for cut in (1, 18, 12, 8, 4)),
            (18, 12, 8, 4, 1),
        )

    def test_length_eight_prefix_generates_p21_cube_then_three(self):
        current = P21[:8]
        expected = P21[8:] + P21 * 2 + (3,)
        produced = []
        for wanted in expected:
            first = curling_number(current)
            second = curling_number_reference(current)
            self.assertEqual(first, second)
            self.assertEqual(first, wanted)
            produced.append(first)
            current += (first,)

        self.assertEqual(tuple(produced), expected)
        self.assertEqual(current, P21 * 3 + (3,))
        self.assertEqual(curling_number(current), 2)
        self.assertEqual(curling_number_reference(current), 2)
        current += (2,)
        self.assertEqual(curling_number(current), 1)
        self.assertEqual(curling_number_reference(current), 1)


if __name__ == "__main__":
    unittest.main()
