from monster_trainer.cheats.base import BaseCheat
from monster_trainer.offsets import bond as bond_offsets


class InstantKinshipSkill(BaseCheat):
    name = "instant_kinship_skill"
    description = "Forces the kinship skill to be considered ready."

    def on_enable(self) -> None:
        if not self.process:
            return
        addr = self.process.base + bond_offsets.KINSHIP_GAUGE
        self._orig[addr] = self.process.read_int(addr)
        self.process.write_int(addr, bond_offsets.KINSHIP_MAX)

    def on_disable(self) -> None:
        if not self.process:
            return
        for addr, val in self._orig.items():
            self.process.write_int(addr, val)
        self._orig.clear()