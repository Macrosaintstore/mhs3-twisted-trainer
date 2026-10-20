import importlib
import pkgutil
import threading
import time
from typing import Dict, List

from monster_trainer.cheats.base import BaseCheat
from monster_trainer.config import TrainerConfig
from monster_trainer.core.process_attach import GameProcess


class Trainer:
    def __init__(self, cfg: TrainerConfig, process: GameProcess | None):
        self.cfg = cfg
        self.process = process
        self.cheats: Dict[str, BaseCheat] = {}
        self._watchdog = None
        self._stop = threading.Event()

    def load_cheats(self) -> None:
        import monster_trainer.cheats as cheats_pkg
        for _, mod_name, _ in pkgutil.iter_modules(cheats_pkg.__path__):
            if mod_name in ("base",):
                continue
            module = importlib.import_module(f"monster_trainer.cheats.{mod_name}")
            for attr in dir(module):
                obj = getattr(module, attr)
                if isinstance(obj, type) and issubclass(obj, BaseCheat) and obj is not BaseCheat:
                    instance = obj(self.process)
                    self.cheats[instance.name] = instance

    def toggle(self, name: str, on: bool) -> bool:
        cheat = self.cheats.get(name)
        if cheat is None:
            return False
        cheat.set_enabled(on)
        return True

    def start_watchdog(self) -> None:
        def _loop():
            while not self._stop.wait(self.cfg.process_watchdog_interval):
                if self.process and self.process.pm is None:
                    return
        self._watchdog = threading.Thread(target=_loop, daemon=True, name="mhs3-watchdog")
        self._watchdog.start()

    def idle_loop(self) -> None:
        while True:
            time.sleep(0.25)

    def shutdown(self) -> None:
        self._stop.set()
        for cheat in self.cheats.values():
            cheat.set_enabled(False)