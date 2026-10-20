from abc import ABC, abstractmethod

from monster_trainer.core.process_attach import GameProcess


class BaseCheat(ABC):
    name: str = "base"
    description: str = ""

    def __init__(self, process: GameProcess | None):
        self.process = process
        self._enabled = False
        self._orig: dict[int, int] = {}

    @abstractmethod
    def on_enable(self) -> None: ...

    @abstractmethod
    def on_disable(self) -> None: ...

    def set_enabled(self, on: bool) -> None:
        if on and not self._enabled:
            self.on_enable()
            self._enabled = True
        elif not on and self._enabled:
            self.on_disable()
            self._enabled = False

    @property
    def enabled(self) -> bool:
        return self._enabled