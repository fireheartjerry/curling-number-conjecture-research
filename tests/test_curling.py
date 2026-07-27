import itertools
import multiprocessing
import unittest

from curling import curling_number, curling_number_reference, tail_length


def _maximum_binary_tail_interval(interval):
    start_length, lower, upper = interval
    best = 0
    for bits in range(lower, upper):
        sequence = tuple(2 + ((bits >> shift) & 1) for shift in range(start_length))
        best = max(best, tail_length(sequence))
    return best


class CurlingNumberTests(unittest.TestCase):
    def test_length_21_cube_root_self_replicates_twice(self):
        root = tuple(map(int, "223222322232322232223"))
        current = root
        produced = []
        for _ in range(2 * len(root)):
            value = curling_number(current)
            produced.append(value)
            current += (value,)

        self.assertEqual(tuple(produced), root * 2)
        self.assertEqual(current, root * 3)
        self.assertEqual(curling_number(current), 3)

    def test_generated_length_21_square_has_no_midpoint_parent(self):
        seed = tuple(map(int, "2332232223322233223222332223322322233"))
        root = tuple(map(int, "223222322232322232223"))
        current = seed
        produced = []
        spectra = {}
        for time in range(66):
            value = curling_number(current)
            produced.append(value)
            if time in (1, 2, 21, 42):
                spectra[time] = tuple(
                    root_length
                    for root_length in range(
                        1, len(current) // value + 1
                    )
                    if current[-value * root_length :]
                    == current[-root_length:] * value
                )
            if value == 1:
                break
            current += (value,)

        self.assertEqual(tuple(produced), root * 3 + (3, 2, 1))
        self.assertEqual(spectra[1], (13,))
        self.assertEqual(spectra[2], (13,))
        self.assertEqual(spectra[21], (4, 10))
        self.assertEqual(spectra[42], (4, 10, 21))

    def test_calibration_example_uses_all_block_lengths(self):
        self.assertEqual(curling_number((2, 3, 2, 3, 2)), 2)

    def test_two_implementations_agree_on_small_ternary_sequences(self):
        for length in range(1, 9):
            for sequence in itertools.product((-1, 0, 1), repeat=length):
                self.assertEqual(
                    curling_number(sequence),
                    curling_number_reference(sequence),
                    sequence,
                )

    def test_a094004_total_length_calibration(self):
        expected_total_lengths = {3: 5, 8: 66, 22: 142}
        for start_length, expected_total_length in expected_total_lengths.items():
            case_count = 1 << start_length
            worker_count = min(8, multiprocessing.cpu_count(), case_count)
            chunk_size = (case_count + worker_count - 1) // worker_count
            intervals = [
                (start_length, lower, min(case_count, lower + chunk_size))
                for lower in range(0, case_count, chunk_size)
            ]
            with multiprocessing.Pool(worker_count) as pool:
                maximum_tail = max(pool.map(_maximum_binary_tail_interval, intervals))
            self.assertEqual(start_length + maximum_tail, expected_total_length)


if __name__ == "__main__":
    unittest.main()
