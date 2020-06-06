# File: S (Python 2.2)

import math

class SfxPlayer:
    UseInverseSquare = 1
    
    def __init__(self):
        self.cutoffDistance = 120.0
        if SfxPlayer.UseInverseSquare:
            self.cutoffDistance = 300.0
        
        self.cutoffVolume = 0.02
        rawCutoffDistance = math.sqrt(1.0 / self.cutoffVolume)
        self.distanceScale = rawCutoffDistance / self.cutoffDistance

    
    def getLocalizedVolume(self, node):
        import math
        d = node.getDistance(base.cam)
        if d > self.cutoffDistance:
            volume = 0
        elif SfxPlayer.UseInverseSquare:
            sd = d * self.distanceScale
            volume = min(1, 1 / sd * sd)
        else:
            volume = 1 - d / self.cutoffDistance
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
            
        


