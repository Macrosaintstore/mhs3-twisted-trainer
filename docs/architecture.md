# Architecture

```
monster_trainer/
  bootstrap.py        entry — arg parsing, attach, HUD
  config/             pydantic config + default.yaml
  core/               pymem wrapper, trainer orchestrator
  cheats/             one module per cheat, discovered via pkgutil
  offsets/            static offsets per game build
  overlay/            terminal HUD
  services/           save backup, hotkey binding
  models/             rider + monstie dataclasses
  utils/              sigscan, mem math, logging
```

Cheat modules subclass `BaseCheat` and are auto-registered on startup.
Offsets live in `monster_trainer/offsets/` and must be updated when the game patches.