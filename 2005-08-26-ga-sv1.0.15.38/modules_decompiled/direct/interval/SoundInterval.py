# File: S (Python 2.2)

from pandac.PandaModules import *
from direct.directnotify.DirectNotifyGlobal import *
import Interval

class SoundInterval(Interval.Interval):
    soundNum = 1
    notify = directNotify.newCategory('SoundInterval')
    
    def __init__(self, sound, loop = 0, duration = 0.0, name = None, volume = 1.0, startTime = 0.0, node = None):
        id = 'Sound-%d' % SoundInterval.soundNum
        SoundInterval.soundNum += 1
        self.sound = sound
        if sound:
            self.soundDuration = sound.length()
        else:
            self.soundDuration = 0
        self.fLoop = loop
        self.volume = volume
        self.startTime = startTime
        self.node = node
        if float(duration) == 0.0 and self.sound != None:
            duration = max(self.soundDuration - self.startTime, 0)
        
        if name == None:
            name = id
        
        Interval.Interval.__init__(self, name, duration)

    
    def privInitialize(self, t):
        t1 = t + self.startTime
        if t1 < 0.10000000000000001:
            t1 = 0.0
        
        if t1 < self.soundDuration:
            base.sfxPlayer.playSfx(self.sound, self.fLoop, 1, self.volume, t1, self.node)
        
        self.state = CInterval.SStarted
        self.currT = t

    
    def privStep(self, t):
        if self.state == CInterval.SPaused:
            t1 = t + self.startTime
            if t1 < self.soundDuration:
                base.sfxPlayer.playSfx(self.sound, self.fLoop, 1, self.volume, t1, self.node)
            
        
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


