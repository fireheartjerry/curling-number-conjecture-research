import itertools
import unittest

from curling import curling_number
from research.search_refined_record import curl_and_shortest, first_failure


class RefinedRecordSearchTests(unittest.TestCase):
    def test_combined_oracle_agrees_with_calibrated_oracle(self):
        for length in range(1, 9):
            for sequence in itertools.product((2, 3), repeat=length):
                value, root = curl_and_shortest(sequence)
                self.assertEqual(value, curling_number(sequence))
                self.assertEqual(sequence[-value * root :], sequence[-root:] * value)
                for shorter in range(1, root):
                    self.assertNotEqual(
                        sequence[-value * shorter :],
                        sequence[-shorter:] * value,
                    )

    def test_seed_crossing_record_relocation_is_not_a_refined_failure(self):
        seed = tuple(map(int, "2322232232223223"))
        self.assertIsNone(first_failure(seed, 180))


if __name__ == "__main__":
    unittest.main()
