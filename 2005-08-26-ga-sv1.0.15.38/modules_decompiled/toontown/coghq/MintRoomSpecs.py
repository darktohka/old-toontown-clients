# File: M (Python 2.2)

from direct.showbase.PythonUtil import invertDict
from toontown.toonbase import ToontownGlobals
from toontown.coghq import NullCogs
from toontown.coghq import CashbotMintBoilerRoom_Battle00_Cogs
from toontown.coghq import CashbotMintBoilerRoom_Battle01_Cogs
from toontown.coghq import CashbotMintControlRoom_Battle00_Cogs
from toontown.coghq import CashbotMintDuctRoom_Battle00_Cogs
from toontown.coghq import CashbotMintDuctRoom_Battle01_Cogs
from toontown.coghq import CashbotMintGearRoom_Battle00_Cogs
from toontown.coghq import CashbotMintGearRoom_Battle01_Cogs
from toontown.coghq import CashbotMintLavaRoomFoyer_Battle00_Cogs
from toontown.coghq import CashbotMintLavaRoomFoyer_Battle01_Cogs
from toontown.coghq import CashbotMintLobby_Battle00_Cogs
from toontown.coghq import CashbotMintLobby_Battle01_Cogs
from toontown.coghq import CashbotMintOilRoom_Battle00_Cogs
from toontown.coghq import CashbotMintPaintMixerReward_Battle00_Cogs
from toontown.coghq import CashbotMintPipeRoom_Battle00_Cogs
from toontown.coghq import CashbotMintPipeRoom_Battle01_Cogs

def getMintRoomSpecModule(roomId):
    return CashbotMintSpecModules[roomId]


def getCogSpecModule(roomId):
    roomName = CashbotMintRoomId2RoomName[roomId]
    return CogSpecModules.get(roomName, NullCogs)


def getNumBattles(roomId):
    return roomId2numBattles[roomId]

CashbotMintEntrances = ('CashbotMintEntrance_Action00',)
CashbotMintMiddleRooms = ('CashbotMintBoilerRoom_Action00', 'CashbotMintBoilerRoom_Battle00', 'CashbotMintDuctRoom_Action00', 'CashbotMintDuctRoom_Battle00', 'CashbotMintGearRoom_Action00', 'CashbotMintGearRoom_Battle00', 'CashbotMintLavaRoomFoyer_Action00', 'CashbotMintLavaRoomFoyer_Action01', 'CashbotMintLavaRoomFoyer_Battle00', 'CashbotMintLavaRoom_Action00', 'CashbotMintLobby_Action00', 'CashbotMintLobby_Battle00', 'CashbotMintPaintMixer_Action00', 'CashbotMintPipeRoom_Action00', 'CashbotMintPipeRoom_Battle00', 'CashbotMintStomperAlley_Action00')
CashbotMintFinalRooms = ('CashbotMintBoilerRoom_Battle01', 'CashbotMintControlRoom_Battle00', 'CashbotMintDuctRoom_Battle01', 'CashbotMintGearRoom_Battle01', 'CashbotMintLavaRoomFoyer_Battle01', 'CashbotMintOilRoom_Battle00', 'CashbotMintLobby_Battle01', 'CashbotMintPaintMixerReward_Battle00', 'CashbotMintPipeRoom_Battle01')
CashbotMintConnectorRooms = ('phase_10/models/cashbotHQ/connector_7cubeL2', 'phase_10/models/cashbotHQ/connector_7cubeR2')
CashbotMintRoomName2RoomId = { }
i = 0
for roomName in CashbotMintEntrances + CashbotMintMiddleRooms + CashbotMintFinalRooms:
    CashbotMintRoomName2RoomId[roomName] = i
    i += 1

del i
CashbotMintRoomId2RoomName = invertDict(CashbotMintRoomName2RoomId)
CashbotMintSpecModules = { }
for (roomName, roomId) in CashbotMintRoomName2RoomId.items():
    exec 'from toontown.coghq import %s' % roomName
    CashbotMintSpecModules[roomId] = eval(roomName)

CogSpecModules = {
    'CashbotMintBoilerRoom_Battle00': CashbotMintBoilerRoom_Battle00_Cogs,
    'CashbotMintBoilerRoom_Battle01': CashbotMintBoilerRoom_Battle01_Cogs,
    'CashbotMintControlRoom_Battle00': CashbotMintControlRoom_Battle00_Cogs,
    'CashbotMintDuctRoom_Battle00': CashbotMintDuctRoom_Battle00_Cogs,
    'CashbotMintDuctRoom_Battle01': CashbotMintDuctRoom_Battle01_Cogs,
    'CashbotMintGearRoom_Battle00': CashbotMintGearRoom_Battle00_Cogs,
    'CashbotMintGearRoom_Battle01': CashbotMintGearRoom_Battle01_Cogs,
    'CashbotMintLavaRoomFoyer_Battle00': CashbotMintLavaRoomFoyer_Battle00_Cogs,
    'CashbotMintLavaRoomFoyer_Battle01': CashbotMintLavaRoomFoyer_Battle01_Cogs,
    'CashbotMintLobby_Battle00': CashbotMintLobby_Battle00_Cogs,
    'CashbotMintLobby_Battle01': CashbotMintLobby_Battle01_Cogs,
    'CashbotMintOilRoom_Battle00': CashbotMintOilRoom_Battle00_Cogs,
    'CashbotMintPaintMixerReward_Battle00': CashbotMintPaintMixerReward_Battle00_Cogs,
    'CashbotMintPipeRoom_Battle00': CashbotMintPipeRoom_Battle00_Cogs,
    'CashbotMintPipeRoom_Battle01': CashbotMintPipeRoom_Battle01_Cogs }
roomId2numBattles = { }
for (roomName, roomId) in CashbotMintRoomName2RoomId.items():
    if roomName not in CogSpecModules:
        roomId2numBattles[roomId] = 0
    else:
        cogSpecModule = CogSpecModules[roomName]
        roomId2numBattles[roomId] = len(cogSpecModule.BattleCells)

name2id = CashbotMintRoomName2RoomId
roomId2numBattles[name2id['CashbotMintBoilerRoom_Battle00']] = 3
roomId2numBattles[name2id['CashbotMintPipeRoom_Battle00']] = 2
del name2id
middleRoomId2numBattles = { }
for roomName in CashbotMintMiddleRooms:
    roomId = CashbotMintRoomName2RoomId[roomName]
    middleRoomId2numBattles[roomId] = roomId2numBattles[roomId]

