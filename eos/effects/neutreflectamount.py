# neutReflectAmount
#
# Used by:
# Modules from group: Capacitor Battery (27 of 27)
type = "passive"
def handler(fit, module, context):
    fit.ship.boostItemAttr("neutReflectAmount", module.getModifiedItemAttr("neutReflectAmountBonus"))
