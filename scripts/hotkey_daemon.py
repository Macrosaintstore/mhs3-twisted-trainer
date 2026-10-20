"""Standalone hotkey daemon — useful when running the trainer headless."""
from monster_trainer.bootstrap import main

if __name__ == "__main__":
    raise SystemExit(main(["--no-hud"]))