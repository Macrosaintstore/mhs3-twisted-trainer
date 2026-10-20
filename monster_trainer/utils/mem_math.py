def align_down(value: int, alignment: int = 4) -> int:
    return value - (value % alignment)


def align_up(value: int, alignment: int = 4) -> int:
    rem = value % alignment
    return value if rem == 0 else value + (alignment - rem)


def is_aligned(value: int, alignment: int = 4) -> bool:
    return value % alignment == 0