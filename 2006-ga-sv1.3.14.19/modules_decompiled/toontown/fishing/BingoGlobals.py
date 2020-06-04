# File: B (Python 2.2)

from toontown.toonbase import TTLocalizer
NORMAL_CARD = 0
FOURCORNER_CARD = 1
DIAGONAL_CARD = 2
THREEWAY_CARD = 3
BLOCKOUT_CARD = 4
Style1 = ((249, 193, 41, 255), (106, 241, 233, 255), (64, 215, 206, 255))
Style2 = ((138, 241, 106, 255), (246, 129, 220, 255), (221, 113, 197, 255))
Style3 = ((128, 108, 250, 255), (248, 129, 56, 255), (250, 95, 26, 255))
Style4 = ((10, 118, 251, 255), (252, 225, 97, 255), (245, 207, 29, 255))
Style5 = ((243, 84, 253, 255), (97, 163, 253, 255), (48, 129, 240, 255))
CardTypeDict = {
    NORMAL_CARD: (Style1, 10, 140, TTLocalizer.FishBingoTypeNormal, TTLocalizer.FishBingoHelpNormal),
    FOURCORNER_CARD: (Style2, 20, 120, TTLocalizer.FishBingoTypeCorners, TTLocalizer.FishBingoHelpCorners),
    DIAGONAL_CARD: (Style3, 40, 180, TTLocalizer.FishBingoTypeDiagonal, TTLocalizer.FishBingoHelpDiagonals),
    THREEWAY_CARD: (Style4, 80, 180, TTLocalizer.FishBingoTypeThreeway, TTLocalizer.FishBingoHelpThreeway),
    BLOCKOUT_CARD: (Style5, 1000, 90, TTLocalizer.FishBingoTypeBlockout, TTLocalizer.FishBingoHelpBlockout) }

def getGameTime(typeId):
    return CardTypeDict[typeId][2]


def getGameName(typeId):
    return CardTypeDict[typeId][3]


def getJackpot(typeId):
    return CardTypeDict[typeId][1]


def getColor(typeId):
    float_color = map(lambda x: x / 255.0, CardTypeDict[typeId][0][0])
    return float_color


def getButtonColor(typeId):
    float_color = map(lambda x: x / 255.0, CardTypeDict[typeId][0][1])
    return float_color


def getButtonRolloverColor(typeId):
    float_color = map(lambda x: x / 255.0, CardTypeDict[typeId][0][2])
    return float_color


def getHelpString(typeId):
    return CardTypeDict[typeId][4]

CellColorActive = (1.0, 1.0, 1.0, 1.0)
CellColorInactive = (0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1.0)
ROLLOVER_AMOUNT = 100
MIN_SUPER_JACKPOT = 1000
MAX_SUPER_JACKPOT = 10000
NO_UPDATE = 0
UPDATE = 1
WIN = 2
CARD_ROWS = 5
CARD_COLS = 5
CARD_SIZE = 25
INTRO_SESSION = 5.0
TIMEOUT_SESSION = 15.0
REWARD_TIMEOUT = 5.0
CLOSE_EVENT_TIMEOUT = 5.0
HOUR_BREAK_SESSION = 300
HOUR_BREAK_MIN = 55
NORMAL_GAME = 0
INTERMISSION = 1
CLOSE_EVENT = 2
CardImageScale = (0.035000000000000003, 0.035000000000000003, 0.035000000000000003)
CardPosition = (0.75, 1.0, -0.65000000000000002)
TutorialPosition = (0.20000000000000001, 1.0, -0.76000000000000001)
TutorialScale = 0.59999999999999998
TutorialTextScale = (0.070000000000000007, 0.23300000000000001)
CellImageScale = 0.087999999999999995
GridXOffset = -0.051999999999999998
FishButtonDict = {
    -1: ('mickeyButton',),
    0: ('BaloonFishButton',),
    2: ('CatfishButton',),
    4: ('ClownfishButton',),
    6: ('FrozenfishButton',),
    8: ('starfishButton',),
    10: ('holyMackrelButton',),
    12: ('DogfishButton',),
    14: ('amoreEelButton',),
    16: ('nursesharkButton',),
    18: ('kingcrabButton',),
    20: ('moonfishButton',),
    22: ('pPlane21',),
    24: ('poolsharkButton',),
    26: ('BearacudaButton',),
    28: ('troutButton',),
    30: ('pianotunaButton',),
    32: ('PBJfishButton',),
    34: ('DevilrayButton',) }
TutorialIntro = 1
TutorialMark = 2
TutorialCard = 3
TutorialBingo = 4
