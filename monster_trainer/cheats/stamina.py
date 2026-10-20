from monster_trainer.cheats.base import BaseCheat
from monster_trainer.offsets import health as hp_offsets


class InfiniteStamina(BaseCheat):
    name = "infinite_stamina"
    description = "Pins rider stamina to its max value."

    def on_enable(self) -> None:
        if not self.process:
            return
        addr = self.process.base + hp_offsets.RIDER_STAMINA
        self._orig[addr] = self.process.read_int(addr)
        self.process.write_int(addr, hp_offsets.MAX_HP_SENTINEL)

    def on_disable(self) -> None:
        if not self.process:
            return
        for addr, val in self._orig.items():
            self.process.write_int(addr, val)
        self._orig.clear()