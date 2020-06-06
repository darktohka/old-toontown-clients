# File: L (Python 2.2)

from pandac.PandaModules import *
easeIn = EaseInBlendType()
easeOut = EaseOutBlendType()
easeInOut = EaseInOutBlendType()
noBlend = NoBlendType()

def getBlend(blendType):
    if blendType == 'easeIn':
        return easeIn
    elif blendType == 'easeOut':
        return easeOut
    elif blendType == 'easeInOut':
        return easeInOut
    elif blendType == 'noBlend':
        return noBlend
    else:
        raise Exception('Error: LerpInterval.__getBlend: Unknown blend type')

