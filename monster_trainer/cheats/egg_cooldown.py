from monster_trainer.cheats.base import BaseCheat

EGG_COOLDOWN_OFFSET = 0x0F2D0010


class NoEggCooldown(BaseCheat):
    name = "no_egg_cooldown"
    description = "Zeroes the egg hatching cooldown timer each tick."

    def on_enable(self) -> None:
        if not self.process:
            return
        addr = self.process.base + EGG_COOLDOWN_OFFSET
        self._orig[addr] = self.process.read_int(addr)
        self.process.write_int(addr, 0)

    def on_disable(self) -> None:
        if not self.process:
            return
        for addr, val in self._orig.items():
            self.process.write_int(addr, val)
        self._orig.clear()