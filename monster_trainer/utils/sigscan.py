from typing import List, Optional


def parse_pattern(pattern: str) -> List[Optional[int]]:
    out: List[Optional[int]] = []
    for tok in pattern.split():
        out.append(None if tok in ("?", "??") else int(tok, 16))
    return out


def find_pattern(buffer: bytes, pattern: str) -> int:
    """Naive scan — returns offset into buffer or -1."""
    pat = parse_pattern(pattern)
    plen = len(pat)
    for i in range(0, len(buffer) - plen):
        ok = True
        for j, b in enumerate(pat):
            if b is not None and buffer[i + j] != b:
                ok = False
                break
        if ok:
            return i
    return -1