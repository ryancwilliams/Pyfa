# Used by:
# Subsystem: Tengu Defensive - Adaptive Shielding
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Defensive Systems").level
    for type in ("Em", "Explosive", "Kinetic", "Thermal"):
        fit.ship.boostItemAttr("shield{0}DamageResonance".format(type), module.getModifiedItemAttr("subsystemBonusCaldariDefensive") * level)
