# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\TempMinigameAI.py
from toontown.toonbase import ToontownGlobals
ALLOW_TEMP_MINIGAMES = simbase.config.GetBool('allow-temp-minigames', False)
TEMP_MG_ID_COUNTER = ToontownGlobals.TravelGameId - 1
TempMgCtors = {}

def _printMessage(message):
    print '\n\n!!!', message, '\n\n'


def _registerTempMinigame(name, Class, id, minPlayers=1, maxPlayers=4):
    if not ALLOW_TEMP_MINIGAMES:
        _printMessage('registerTempMinigame WARNING: allow-temp-minigames config is set to false, but we are trying to register temp minigame ' + name)
        import traceback
        traceback.print_stack()
        return
    ToontownGlobals.MinigameIDs += (id,)
    ToontownGlobals.MinigameNames[name] = id
    TempMgCtors[id] = Class
    for i in range(minPlayers, maxPlayers):
        ToontownGlobals.MinigamePlayerMatrix[i] += (id,)

    _printMessage('registerTempMinigame: ' + name)


if ALLOW_TEMP_MINIGAMES:
    pass