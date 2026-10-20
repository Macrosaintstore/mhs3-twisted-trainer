# Contributing to mhs3-twisted-trainer

Thanks for wanting to help with the Monster Hunter Stories 3: Twisted Reflection trainer.

## Ground rules
- Test against the current Steam build before opening a PR. Offsets shift between patches.
- Keep new features behind a toggle in `config/default.yaml`.
- Do not commit memory dumps, saved files, or extracted game assets.
- Follow the existing module layout: put new cheats in `monster_trainer/cheats/`, new overlays in `monster_trainer/overlay/`.

## Dev setup
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m monster_trainer --dry-run
```

## Pull requests
- One feature per PR.
- Include a short note in the PR body describing the offset or signature you resolved and how you verified it.
- Add a test in `tests/` when the logic is pure (parsers, math, offset math).