from pathlib import Path
from typing import List

import yaml
from pydantic import BaseModel, Field


class CheatToggle(BaseModel):
    name: str
    enabled: bool = False
    hotkey: str = ""


class TrainerConfig(BaseModel):
    version: str = "0.6.2"
    exe_name: str = "MHS3.exe"
    process_watchdog_interval: float = 2.5
    overlay_scale: float = 1.0
    cheats: List[CheatToggle] = Field(default_factory=list)


def load_config(path: Path) -> TrainerConfig:
    if not path.exists():
        return TrainerConfig()
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return TrainerConfig(**raw)