from monster_trainer.core.trainer import Trainer
from monster_trainer.utils.hotkeys import bind_hotkeys, unbind_all


class HotkeyService:
    def __init__(self, trainer: Trainer, hotkey_map: dict[str, str]):
        self.trainer = trainer
        self.hotkey_map = hotkey_map  # cheat_name -> combo

    def install(self) -> None:
        mapping = {}
        for name, combo in self.hotkey_map.items():
            mapping[combo] = self._make_toggle(name)
        bind_hotkeys(mapping)

    def _make_toggle(self, name: str):
        def _cb():
            cheat = self.trainer.cheats.get(name)
            if cheat is not None:
                self.trainer.toggle(name, not cheat.enabled)
        return _cb

    def uninstall(self) -> None:
        unbind_all()