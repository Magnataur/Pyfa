# gunneryFalloffBonusOnline
#
# Used by:
# Modules from group: Tracking Enhancer (17 of 17)
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                  "falloff", module.getModifiedItemAttr("falloffBonus"),
                                  stackingPenalties = True)