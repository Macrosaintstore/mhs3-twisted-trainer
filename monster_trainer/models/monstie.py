from dataclasses import dataclass, field
from typing import List


@dataclass
class MonstieGene:
    slot: int
    gene_id: int
    unlocked: bool = False


@dataclass
class MonstieState:
    name: str
    species_id: int
    level: int
    genes: List[MonstieGene] = field(default_factory=list)

    def unlocked_genes(self) -> List[MonstieGene]:
        return [g for g in self.genes if g.unlocked]

    def unlock_all(self) -> None:
        for g in self.genes:
            g.unlocked = True