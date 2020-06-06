# File: C (Python 2.2)

TowerYRange = 200
GameTime = 90
MAX_SCORE = 15
MIN_SCORE = 5
FUSE_TIME = 0.0

def calcScore(t):
    range = MAX_SCORE - MIN_SCORE
    score = MAX_SCORE - range * (float(t) / GameTime)
    return int(score + 0.5)

