"""Executable reference definitions for curling-number experiments."""


def curling_number(sequence):
    """Return the greatest repeated-suffix exponent of a nonempty sequence."""
    sequence = tuple(sequence)
    if not sequence:
        raise ValueError("curling_number requires a nonempty sequence")

    length = len(sequence)
    best = 1
    for block_length in range(1, length + 1):
        block = sequence[length - block_length :]
        copies = 1
        cursor = length - 2 * block_length
        while cursor >= 0 and sequence[cursor : cursor + block_length] == block:
            copies += 1
            cursor -= block_length
        if copies > best:
            best = copies
    return best


def curling_number_reference(sequence):
    """Slow specification implementation, structured independently."""
    sequence = tuple(sequence)
    if not sequence:
        raise ValueError("curling_number_reference requires a nonempty sequence")

    length = len(sequence)
    feasible_exponents = {1}
    for exponent in range(2, length + 1):
        for block_length in range(1, length // exponent + 1):
            suffix_length = exponent * block_length
            suffix = sequence[length - suffix_length :]
            block = suffix[:block_length]
            if suffix == block * exponent:
                feasible_exponents.add(exponent)
    return max(feasible_exponents)


def tail_length(sequence, step_limit=None):
    """Steps before the first current sequence whose curling number is one."""
    current = tuple(sequence)
    if not current:
        raise ValueError("tail_length requires a nonempty sequence")

    steps = 0
    while True:
        value = curling_number(current)
        if value == 1:
            return steps
        if step_limit is not None and steps >= step_limit:
            raise RuntimeError("step limit reached before curling number one")
        current += (value,)
        steps += 1
