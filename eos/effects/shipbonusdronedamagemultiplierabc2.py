# Used by:
# Ship: Prophecy
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Battlecruiser").level
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"),
                                 "damageMultiplier", ship.getModifiedItemAttr("shipBonusABC2") * level)
