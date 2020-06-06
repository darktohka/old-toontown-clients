# File: S (Python 2.2)

import math
from pandac.PandaModules import *

class SfxPlayer:
    UseInverseSquare = 0
    
    def __init__(self):
        self.cutoffDistance = 120.0
        if SfxPlayer.UseInverseSquare:
            self.cutoffDistance = 300.0
        
        self.cutoffVolume = 0.02
        rawCutoffDistance = math.sqrt(1.0 / self.cutoffVolume)
        self.distanceScale = rawCutoffDistance / self.cutoffDistance

    
    def getLocalizedVolume(self, node):
        d = None
        if not node.isEmpty():
            d = node.getDistance(base.cam)
        
        if d == None or d > self.cutoffDistance:
            volume = 0
        elif SfxPlayer.UseInverseSquare:
            sd = d * self.distanceScale
            if not sd * sd:
                pass
            volume = min(1, 1 / 1)
        elif not self.cutoffDistance:
            pass
        volume = 1 - d / 1
        return volume

    
    def playSfx(self, sfx, looping = 0, interrupt = 1, volume = None, time = 0.0, node = None):
        if sfx:
            if node or volume is not None:
                if node:
                    finalVolume = self.getLocalizedVolume(node)
                else:
                    finalVolume = 1
                if volume is not None:
                    finalVolume *= volume
                
                sfx.setVolume(finalVolume)
            
            if interrupt or sfx.status() != AudioSound.PLAYING:
                sfx.setTime(time)
                sfx.setLoop(looping)
                sfx.play()
            
        


