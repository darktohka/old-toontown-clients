# File: S (Python 2.2)

import whrandom
import DirectNotifyGlobal
import Localizer
notify = DirectNotifyGlobal.directNotify.newCategory('SuitDialog')

def getBrushOffIndex(suitName):
    if SuitBrushOffs.has_key(suitName):
        brushoffs = SuitBrushOffs[suitName]
    else:
        brushoffs = SuitBrushOffs[None]
    num = len(brushoffs)
    chunk = 100 / num
    randNum = whrandom.randint(0, 99)
    count = chunk
    for i in range(num):
        if randNum < count:
            return i
        
        count += chunk
    
    notify.error('getBrushOffs() - no brush off found!')


def getBrushOffText(suitName, index):
    if SuitBrushOffs.has_key(suitName):
        brushoffs = SuitBrushOffs[suitName]
    else:
        brushoffs = SuitBrushOffs[None]
    return brushoffs[index]

SuitBrushOffs = Localizer.SuitBrushOffs
