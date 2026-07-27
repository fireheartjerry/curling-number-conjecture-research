"""Search record cubes using transported-square episode origins.

All positions are zero based.  ``C_t`` is the curling number of ``S_t`` and
the value appended at time ``t``.  At a time with ``C_t == 2``, every
maximizing root is a square root.  Equal root lengths at consecutive
``2``-times belong to the same transported episode when the time gap is
strictly smaller than the root length.

When such an episode matures to a canonical cube on a value-2 copy-parent
ray, its *periodic-union origin* is the left end of the maximal contiguous
periodic interval obtained from the episode union, including a hidden
leftward extension already present in the seed.
"""

from __future__ import annotations

from dataclasses import dataclass

from research.search_low_reset_second_root import curl_and_roots


@dataclass(frozen=True)
class EpisodeRecord:
    vertex: int
    span: int
    visible_left: int
    episode_birth: int
    displayed_origin: int
    periodic_origin: int
    previous_vertex: int | None
    previous_span: int
    previous_origin: int | None


def episode_record_events(seed, step_limit):
    """Return new canonical-ray cube records with exact episode origins."""
    seed = tuple(seed)
    seed_length = len(seed)
    state = seed
    word = list(seed)

    previous_two_time = None
    # root length -> birth time, for the most recent 2-event
    previous_episodes = {}
    # value-2 vertex -> (record span, periodic origin, record vertex)
    ray_records = {}
    events = []

    for time in range(step_limit + 1):
        value, roots = curl_and_roots(state)
        shortest = roots[0]

        if value == 2:
            current_episodes = {}
            for root in roots:
                transported = (
                    previous_two_time is not None
                    and root in previous_episodes
                    and time - previous_two_time < root
                )
                current_episodes[root] = (
                    previous_episodes[root] if transported else time
                )
            previous_two_time = time
            previous_episodes = current_episodes

        # The final symbol of S_time is the value-2 vertex appended at
        # time-1.  Its canonical parent is determined by S_time.
        if time >= 1 and word[-1] == 2 and value >= 2:
            vertex = seed_length + time - 1
            parent = vertex - shortest
            old_span, old_origin, old_vertex = ray_records.get(
                parent, (-1, None, None)
            )
            new_span, new_origin, new_vertex = (
                old_span,
                old_origin,
                old_vertex,
            )

            if value == 3 and shortest > old_span:
                if previous_two_time != time - 1:
                    raise AssertionError("a value-2 vertex must come from C_(t-1)=2")
                birth = previous_episodes.get(shortest)
                if birth is None:
                    raise AssertionError(
                        "a canonical cube must mature from its conjugate square"
                    )

                displayed_origin = seed_length + birth - 2 * shortest
                visible_left = seed_length + time - 3 * shortest
                periodic_origin = displayed_origin
                while (
                    periodic_origin > 0
                    and word[periodic_origin - 1]
                    == word[periodic_origin - 1 + shortest]
                ):
                    periodic_origin -= 1

                if periodic_origin != visible_left:
                    raise AssertionError(
                        "the matured cube must start at the maximal episode origin"
                    )

                events.append(
                    EpisodeRecord(
                        vertex=vertex,
                        span=shortest,
                        visible_left=visible_left,
                        episode_birth=birth,
                        displayed_origin=displayed_origin,
                        periodic_origin=periodic_origin,
                        previous_vertex=old_vertex,
                        previous_span=old_span,
                        previous_origin=old_origin,
                    )
                )
                new_span, new_origin, new_vertex = (
                    shortest,
                    periodic_origin,
                    vertex,
                )

            ray_records[vertex] = (new_span, new_origin, new_vertex)

        if value == 1:
            break
        word.append(value)
        state += (value,)

    return tuple(events)


def first_episode_origin_failure(seed, step_limit):
    """Find a record whose origin fails to move left of a generated record."""
    seed_length = len(seed)
    for event in episode_record_events(seed, step_limit):
        if (
            event.previous_origin is not None
            and event.previous_origin >= seed_length
            and event.periodic_origin >= event.previous_origin
        ):
            return event
    return None
