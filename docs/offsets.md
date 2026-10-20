# Offset Reference — MHS3 build 1.3.0.4

All offsets are base-relative (module base of `MHS3.exe`).

| Cheat | Offset | Notes |
|-------|--------|-------|
| rider_hp | 0x0F2A1C40 | int32, clamped by game |
| rider_stamina | 0x0F2A1C48 | int32 |
| kinship_gauge | 0x0F2B4A10 | int32, max 1000 |
| gene_slot_0..3 | 0x0F3C1100 | int32 flags |

When the game patches, re-run `scripts/resolve_offsets.py` and update `monster_trainer/offsets/`.