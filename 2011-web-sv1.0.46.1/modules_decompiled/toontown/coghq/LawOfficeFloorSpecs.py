# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\LawOfficeFloorSpecs.py
from direct.showbase.PythonUtil import invertDict
from toontown.toonbase import ToontownGlobals
from toontown.coghq import NullCogs
from toontown.coghq import LabotOfficeFloor_01a_Cogs
from toontown.coghq import LabotOfficeFloor_01b_Cogs

def getLawOfficeFloorSpecModule(floorId):
    return LawbotOfficeSpecModules[floorId]


def getCogSpecModule(floorId):
    floor = LawbotOfficeFloorId2FloorName[roomId]
    return CogSpecModules.get(floorId, NullCogs)


def getNumBattles(floorId):
    return floorId2numBattles[floorId]


LawbotOfficeFloorId2FloorName = {0: 'LabotOfficeFloor_01_a', 1: 'LabotOfficeFloor_01_b'}
LawbotOfficeFloorName2FloorId = invertDict(LawbotOfficeFloorId2FloorName)
LawbotOfficeEntranceIDs = (0, 1)
LawbotOfficeFloorIDs = (0, 1)
LawbotOfficeSpecModules = {}
for (roomName, roomId) in LawbotOfficeFloorName2FloorId.items():
    exec 'from toontown.coghq import %s' % roomName
    LawbotOfficeSpecModules[roomId] = eval(roomName)

CogSpecModules = {'CashbotMintBoilerRoom_Battle00': LabotOfficeFloor_01a_Cogs, 'CashbotMintBoilerRoom_Battle01': LabotOfficeFloor_01b_Cogs}
floorId2numBattles = {}
for (roomName, roomId) in LawbotOfficeFloorName2FloorId.items():
    if roomName not in CogSpecModules:
        floorId2numBattles[roomId] = 0
    else:
        cogSpecModule = CogSpecModules[roomName]
        floorId2numBattles[roomId] = len(cogSpecModule.BattleCells)