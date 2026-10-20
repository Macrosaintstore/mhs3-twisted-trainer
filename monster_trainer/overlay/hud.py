import threading
import time

from rich.console import Console
from rich.table import Table

from monster_trainer.config import TrainerConfig
from monster_trainer.core.trainer import Trainer


class TrainerHud:
    def __init__(self, trainer: Trainer, cfg: TrainerConfig):
        self.trainer = trainer
        self.cfg = cfg
        self.console = Console()
        self._stop = threading.Event()

    def _render(self) -> Table:
        t = Table(title="MHS3 Twisted Reflection — Trainer")
        t.add_column("Cheat")
        t.add_column("Hotkey")
        t.add_column("State")
        hotkeys = {c.name: c.hotkey for c in self.cfg.cheats}
        for name, cheat in sorted(self.trainer.cheats.items()):
            state = "[green]ON[/]" if cheat.enabled else "[dim]off[/]"
            t.add_row(name, hotkeys.get(name, "-"), state)
        return t

    def run(self) -> None:
        self.console.clear()
        while not self._stop.is_set():
            self.console.clear()
            self.console.print(self._render())
            time.sleep(0.5)