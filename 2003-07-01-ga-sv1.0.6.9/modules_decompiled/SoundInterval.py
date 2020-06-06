# File: S (Python 2.2)

from PandaModules import *
from DirectNotifyGlobal import *
import Interval

class SoundInterval(Interval.Interval):
    soundNum = 1
    notify = directNotify.newCategory('SoundInterval')
    
    def __init__(self, sound, loop = 0, duration = 0.0, name = None, volume = 1.0, startTime = 0.0, node = None):
        id = 'Sound-%d' % SoundInterval.soundNum
        SoundInterval.soundNum += 1
        self.sound = sound
        self.fLoop = loop
        self.volume = volume
        self.startTime = startTime
        self.node = node
        if duration == 0.0 and self.sound != None:
            duration = max(self.sound.length() - self.startTime, 0)
            if duration == 0:
                self.notify.warning('zero length duration!')
            
            duration += min(duration * 2.3999999999999999, 1.5)
        
        if name == None:
            name = id
        
        Interval.Interval.__init__(self, name, duration)

    
    def privInitialize(self, t):
        t1 = t + self.startTime
        if t1 < 0.10000000000000001:
            t1 = 0.0
        
        base.sfxPlayer.playSfx(self.sound, self.fLoop, 1, self.volume, t1, self.node)
        self.state = CInterval.SStarted
        self.currT = t1

    
    def privStep(self, t):
        if self.state == CInterval.SPaused:
            base.sfxPlayer.playSfx(self.sound, self.fLoop, 1, self.volume, t, self.node)
        
        self.state = CInterval.SStarted
        self.currT = t

    
    def privFinalize(self):
        if self.sound != None:
            self.sound.stop()
        
        self.currT = self.getDuration()
        self.state = CInterval.SFinal

    
    def privInterrupt(self):
        if self.sound != None:
            self.sound.stop()
        
        self.state = CInterval.SPaused


