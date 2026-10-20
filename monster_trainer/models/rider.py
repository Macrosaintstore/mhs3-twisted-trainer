from dataclasses import dataclass


@dataclass
class RiderState:
    name: str
    level: int
    hp: int
    max_hp: int
    stamina: int
    max_stamina: int
    stat_points: int = 0

    @property
    def hp_ratio(self) -> float:
        return self.hp / self.max_hp if self.max_hp else 0.0