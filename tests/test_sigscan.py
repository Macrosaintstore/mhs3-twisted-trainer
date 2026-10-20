from monster_trainer.utils.sigscan import find_pattern, parse_pattern


def test_parse_pattern_wildcards():
    assert parse_pattern("48 8B ?? 05") == [0x48, 0x8B, None, 0x05]


def test_find_pattern_simple():
    buf = bytes([0x00, 0x48, 0x8B, 0x11, 0x05, 0x00])
    assert find_pattern(buf, "48 8B 11 05") == 1


def test_find_pattern_missing():
    buf = b"\x00" * 16
    assert find_pattern(buf, "DE AD BE EF") == -1