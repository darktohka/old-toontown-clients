# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\MazeGameGlobals.py
from direct.showbase import RandomNumGen

def getMazeName(gameDoId, numPlayers, mazeNames):
    try:
        return forcedMaze
    except:
        names = mazeNames[(numPlayers - 1)]
        return names[(RandomNumGen.randHash(gameDoId) % len(names))]


ENDLESS_GAME = config.GetBool('endless-maze-game', 0)
GAME_DURATION = 60.0
SHOWSCORES_DURATION = 2.0
SUIT_TIC_FREQ = int(256)
WALK_SAME_DIRECTION_PROB = 4
WALK_TURN_AROUND_PROB = 30
SUIT_START_POSITIONS = (
 (0.25, 0.25), (0.75, 0.75), (0.25, 0.75), (0.75, 0.25), (0.2, 0.5), (0.8, 0.5), (0.5, 0.2), (0.5, 0.8), (0.33, 0.0), (0.66, 0.0), (0.33, 1.0), (0.66, 1.0), (0.0, 0.33), (0.0, 0.66), (1.0, 0.33), (1.0, 0.66))