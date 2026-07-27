import unittest

from research.search_episode_origins import (
    episode_record_events,
    first_episode_origin_failure,
)


class EpisodeOriginTests(unittest.TestCase):
    def test_hidden_seed_extension_is_included(self):
        seed = tuple(map(int, "2322232232223223"))
        records = episode_record_events(seed, 180)
        event = next(record for record in records if record.span == 7)
        self.assertEqual(event.displayed_origin, 2)
        self.assertEqual(event.periodic_origin, 0)
        self.assertEqual(event.visible_left, 0)

    def test_generated_four_to_twenty_one_record_moves_left(self):
        seed = tuple(map(int, "2323222322"))
        records = episode_record_events(seed, 180)
        event = next(
            record
            for record in records
            if record.previous_span == 4 and record.span == 21
        )
        self.assertEqual(event.previous_origin, 12)
        self.assertEqual(event.periodic_origin, 0)
        self.assertIsNone(first_episode_origin_failure(seed, 180))


if __name__ == "__main__":
    unittest.main()
