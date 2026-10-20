from monster_trainer.offsets import genes, health


def test_health_offsets_aligned():
    assert health.RIDER_HP % 4 == 0
    assert health.RIDER_STAMINA - health.RIDER_HP == 8


def test_gene_slots_contiguous():
    slots = genes.SLOT_TABLE
    for a, b in zip(slots, slots[1:]):
        assert b - a == 4