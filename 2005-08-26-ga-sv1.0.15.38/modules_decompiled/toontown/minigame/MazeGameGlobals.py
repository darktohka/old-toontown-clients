# File: M (Python 2.2)

from direct.showbase import RandomNumGen
ENDLESS_GAME = config.GetBool('endless-maze-game', 0)
GAME_DURATION = 60.0
SHOWSCORES_DURATION = 2.0
SUIT_TIC_FREQ = int(256)

def getMazeName(gameDoId, numPlayers, mazeNames):
    
    try:
        return forcedMaze
    except:
        names = mazeNames[numPlayers - 1]
        return names[RandomNumGen.randHash(gameDoId) % len(names)]


