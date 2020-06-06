# File: F (Python 2.2)

from toontown.toonbase import ToontownGlobals
OFF = 0
MOVING = 1
StepTime = 5.0
MinimumHunger = 1.0
NUM_TARGETS_INDEX = 0
POS_START_INDEX = 1
POS_END_INDEX = 4
RADIUS_INDEX = 4
WATER_LEVEL_INDEX = 5
__targetInfoDict = {
    ToontownGlobals.ToontownCentral: (2, -81, 31, -4.7999999999999998, 14, -1.3999999999999999),
    ToontownGlobals.SillyStreet: (2, 20, -664, -1.3999999999999999, 14, -1.3999999999999999 - 0.438),
    ToontownGlobals.LoopyLane: (2, -234, 175, -1.3999999999999999, 14, -1.3999999999999999 - 0.46200000000000002),
    ToontownGlobals.PunchlinePlace: (2, 529, -70, -1.3999999999999999, 13, -1.3999999999999999 - 0.48599999999999999),
    ToontownGlobals.DonaldsDock: (2, -17, 130, 1.73, 15, 1.73 - 3.6150000000000002),
    ToontownGlobals.BarnacleBoulevard: (2, 381, -350, -2, 14, -2 - 0.48199999999999998),
    ToontownGlobals.SeaweedStreet: (2, -395, -226, -2, 14, -2 - 0.48199999999999998),
    ToontownGlobals.LighthouseLane: (2, 350, 100, -2, 14, -2 - 0.48199999999999998),
    ToontownGlobals.DaisyGardens: (2, 50, 47, -1.48, 13, -1.48 - 0.34499999999999997),
    ToontownGlobals.ElmStreet: (2, 149, 44, -1.4299999999999999, 13, -1.4299999999999999 - 0.61799999999999999),
    ToontownGlobals.MapleStreet: (2, 176, 100, -1.4299999999999999, 13, -1.4299999999999999 - 0.61799999999999999),
    ToontownGlobals.OakStreet: (2, 134, -70.5, -1.5, 13, -1.5 - 0.377),
    ToontownGlobals.MinniesMelodyland: (2, -0.20000000000000001, -20.199999999999999, -14.65, 14, -14.65 - -12),
    ToontownGlobals.AltoAvenue: (2, -580, -90, -0.87, 14, -0.87 - 1.8440000000000001),
    ToontownGlobals.BaritoneBoulevard: (2, -214, 250, -0.87, 14, -0.87 - 1.8440000000000001),
    ToontownGlobals.TenorTerrace: (2, 715, -15, -0.87, 14, -0.87 - 1.8440000000000001),
    ToontownGlobals.TheBrrrgh: (2, -58, -26, 1.7, 10, -0.80000000000000004),
    ToontownGlobals.WalrusWay: (2, 460, 29, -2, 13, -2 - 0.40000000000000002),
    ToontownGlobals.SleetStreet: (2, 340, 480, -2, 13, -2 - 0.40000000000000002),
    ToontownGlobals.DonaldsDreamland: (2, 159, 0.20000000000000001, -17.100000000000001, 14, -17.100000000000001 - -14.6),
    ToontownGlobals.LullabyLane: (2, 118, -185, -2.1000000000000001, 14, -2.1000000000000001 - 0.378),
    ToontownGlobals.PajamaPlace: (2, 241, -348, -2.1000000000000001, 14, -2.1000000000000001 - 0.378),
    ToontownGlobals.MyEstate: (3, 30, -126, -0.29999999999999999, 16, -0.82999999999999996) }

def getNumTargets(zone):
    info = __targetInfoDict.get(zone)
    if info:
        return info[NUM_TARGETS_INDEX]
    else:
        return 2


def getTargetCenter(zone):
    info = __targetInfoDict.get(zone)
    if info:
        return info[POS_START_INDEX:POS_END_INDEX]
    else:
        return (0, 0, 0)


def getTargetRadius(zone):
    info = __targetInfoDict.get(zone)
    if info:
        return info[RADIUS_INDEX]
    else:
        return 10


def getWaterLevel(zone):
    info = __targetInfoDict.get(zone)
    if info:
        return info[WATER_LEVEL_INDEX]
    else:
        return 0

