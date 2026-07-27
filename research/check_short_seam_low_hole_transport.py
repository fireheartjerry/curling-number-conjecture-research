"""Bounded audit of the short symbol-two low-hole transport.

The proof is symbolic and is recorded in ``symbol_two_status_seam.md``.
This checker exhausts arbitrary binary words (not merely fixed profiles)
through the requested length and checks the only combinatorial implication
used by the proof:

* if ``s`` is a finite-word period of ``P`` and
  ``Y = P^2 P[:s]``, then every proper circular square root of ``P`` at
  phase ``s+t`` is also a proper circular square root of ``Y`` at phase
  ``t``, for ``0 <= t <= n-s``.

At ``t=n-s``, phase ``s+t`` is interpreted as phase zero of ``P``.
Run the A094004 calibration before this script.
"""

from __future__ import annotations

import argparse
from itertools import product

from check_run_length_grammar import word_power_root_lengths


Word = tuple[int, ...]


def has_finite_period(word: Word, period: int) -> bool:
    return 1 <= period < len(word) and all(
        word[index] == word[index - period]
        for index in range(period, len(word))
    )


def audit(max_n: int) -> dict[str, int]:
    words = 0
    period_pairs = 0
    phases = 0
    transported_roots = 0

    for n in range(2, max_n + 1):
        for tail in product((2, 3), repeat=n - 1):
            word = (2,) + tail
            words += 1
            for period in range(1, n):
                if not has_finite_period(word, period):
                    continue
                period_pairs += 1
                prefix = word[:period]
                extended = word + word + prefix

                for phase in range(0, n - period + 1):
                    phases += 1
                    lifted_phase = period + phase
                    assert prefix + word[:phase] == word[:lifted_phase]
                    assert extended + word[:phase] == (
                        word + word + word[:lifted_phase]
                    )

                    circular_phase = lifted_phase % n
                    source_roots = word_power_root_lengths(
                        word, circular_phase, 2
                    )
                    target_roots = word_power_root_lengths(
                        extended, phase, 2
                    )
                    for root in source_roots:
                        assert root < n < len(extended)
                        assert root in target_roots
                        transported_roots += 1

    return {
        "max_n": max_n,
        "binary_words_with_initial_2": words,
        "finite_period_pairs": period_pairs,
        "audited_phases": phases,
        "transported_square_roots": transported_roots,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=14)
    args = parser.parse_args()
    print(audit(args.max_n))


if __name__ == "__main__":
    main()
