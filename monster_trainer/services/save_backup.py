import shutil
import time
from pathlib import Path


class SaveBackupService:
    """Copies the MHS3 save directory before enabling risky cheats."""

    def __init__(self, save_dir: Path, backup_dir: Path):
        self.save_dir = save_dir
        self.backup_dir = backup_dir

    def snapshot(self, tag: str = "pre_cheat") -> Path | None:
        if not self.save_dir.exists():
            return None
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        stamp = time.strftime("%Y%m%d_%H%M%S")
        dest = self.backup_dir / f"{tag}_{stamp}"
        shutil.copytree(self.save_dir, dest)
        return dest