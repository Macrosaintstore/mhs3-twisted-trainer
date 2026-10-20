"""Developer helper: dump candidate offsets for a running MHS3.exe.

Not shipped with releases. Requires the game to be running.
"""
import sys

from monster_trainer.core.process_attach import GameProcess
from monster_trainer.utils.sigscan import find_pattern

SIGS = {
    "rider_hp_hint": "48 8B 05 ?? ?? ?? ?? 89 88 40 1C 2A 0F",
    "kinship_hint": "8B 0D ?? ?? ?? ?? 83 F9 64 7E 05",
}


def main() -> int:
    proc = GameProcess("MHS3.exe")
    if not proc.attach():
        print("MHS3.exe not running", file=sys.stderr)
        return 1
    print(f"base = 0x{proc.base:X}")
    for name, sig in SIGS.items():
        print(f"{name}: pattern length {len(sig.split())} bytes (scan stub)")
    return 0


if __name__ == "__main__":
    sys.exit(main())