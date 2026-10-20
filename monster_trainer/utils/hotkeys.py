from typing import Callable, Dict

import keyboard


def bind_hotkeys(mapping: Dict[str, Callable[[], None]]) -> None:
    for combo, cb in mapping.items():
        keyboard.add_hotkey(combo, cb)


def unbind_all() -> None:
    keyboard.unhook_all_hotkeys()