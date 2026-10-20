from monster_trainer.config.loader import TrainerConfig
from monster_trainer.core.trainer import Trainer


def test_load_cheats_dry_run():
    t = Trainer(TrainerConfig(), process=None)
    t.load_cheats()
    assert "infinite_health" in t.cheats
    assert "gene_editor" in t.cheats
    assert "no_egg_cooldown" in t.cheats


def test_toggle_unknown_returns_false():
    t = Trainer(TrainerConfig(), process=None)
    t.load_cheats()
    assert t.toggle("does_not_exist", True) is False