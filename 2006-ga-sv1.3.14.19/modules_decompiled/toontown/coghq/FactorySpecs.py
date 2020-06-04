# File: F (Python 2.2)

from toontown.toonbase import ToontownGlobals
import SellbotLegFactorySpec
import SellbotLegFactoryCogs

def getFactorySpecModule(factoryId):
    return FactorySpecModules[factoryId]


def getCogSpecModule(factoryId):
    return CogSpecModules[factoryId]

FactorySpecModules = {
    ToontownGlobals.SellbotFactoryInt: SellbotLegFactorySpec }
CogSpecModules = {
    ToontownGlobals.SellbotFactoryInt: SellbotLegFactoryCogs }
if __dev__:
    import FactoryMockupSpec
    FactorySpecModules[ToontownGlobals.MockupFactoryId] = FactoryMockupSpec
    import FactoryMockupCogs
    CogSpecModules[ToontownGlobals.MockupFactoryId] = FactoryMockupCogs

