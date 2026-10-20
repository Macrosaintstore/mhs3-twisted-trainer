import argparse
import sys
from pathlib import Path

from rich.console import Console

from monster_trainer.config.loader import load_config
from monster_trainer.core.process_attach import GameProcess
from monster_trainer.core.trainer import Trainer
from monster_trainer.overlay.hud import TrainerHud

console = Console()


def parse_args(argv=None):
    p = argparse.ArgumentParser(prog="mhs3-twisted-trainer")
    p.add_argument("--config", default="config/default.yaml")
    p.add_argument("--dry-run", action="store_true", help="Load modules without attaching")
    p.add_argument("--no-hud", action="store_true", help="Disable overlay HUD")
    return p.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    cfg = load_config(Path(args.config))
    console.print(f"[bold cyan]MHS3 Twisted Reflection Trainer[/] v{cfg.version}")

    if args.dry_run:
        console.print("[yellow]dry-run: skipping process attach[/]")
        Trainer(cfg, process=None).load_cheats()
        console.print("[green]all cheat modules imported OK[/]")
        return 0

    proc = GameProcess(cfg.exe_name)
    if not proc.attach():
        console.print("[red]Could not find Monster Hunter Stories 3 process. Is it running?[/]")
        return 2

    trainer = Trainer(cfg, process=proc)
    trainer.load_cheats()
    trainer.start_watchdog()

    if not args.no_hud:
        TrainerHud(trainer, cfg).run()
    else:
        try:
            trainer.idle_loop()
        except KeyboardInterrupt:
            pass
    return 0


if __name__ == "__main__":
    sys.exit(main())