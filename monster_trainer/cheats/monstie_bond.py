from monster_trainer.cheats.base import BaseCheat
from monster_trainer.offsets import bond as bond_offsets


class MaxMonstieBond(BaseCheat):
    name = "max_monstie_bond"
    description = "Fills the kinship gauge for the active monstie."

    def on_enable(self) -> None:
        if not self.process:
            return
        addr = self.process.base + bond_offsets.KINSHIP_GAUGE
        self._orig[addr] = self.process.read_int(addr)
        self.process.write_int(addr, 1000)

    def on_disable(self) -> None:
        if not self.process:
            return
        for addr, val in self._orig.items():
            self.process.write_int(addr, val)
        self._orig.clear()