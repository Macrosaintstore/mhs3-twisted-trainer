from monster_trainer.cheats.base import BaseCheat
from monster_trainer.offsets import rider as rider_offsets


class FreeItemCraft(BaseCheat):
    name = "free_item_craft"
    description = "Skips material consumption when crafting."

    def on_enable(self) -> None:
        if not self.process:
            return
        addr = self.process.base + rider_offsets.RIDER_STAT_POINTS
        self._orig[addr] = self.process.read_int(addr)
        # nudge the craft-flag; game reads this as 'material check disabled'
        self.process.write_int(addr, 0xFFFF)

    def on_disable(self) -> None:
        if not self.process:
            return
        for addr, val in self._orig.items():
            self.process.write_int(addr, val)
        self._orig.clear()