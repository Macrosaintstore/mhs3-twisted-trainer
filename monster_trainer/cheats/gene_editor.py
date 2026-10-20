from monster_trainer.cheats.base import BaseCheat
from monster_trainer.offsets import genes as gene_offsets


class GeneEditor(BaseCheat):
    name = "gene_editor"
    description = "Unlocks the gene slots on the currently selected monstie."

    def on_enable(self) -> None:
        if not self.process:
            return
        for slot, off in enumerate(gene_offsets.SLOT_TABLE):
            addr = self.process.base + off
            self._orig[addr] = self.process.read_int(addr)
            self.process.write_int(addr, gene_offsets.UNLOCKED_FLAG)

    def on_disable(self) -> None:
        if not self.process:
            return
        for addr, val in self._orig.items():
            self.process.write_int(addr, val)
        self._orig.clear()