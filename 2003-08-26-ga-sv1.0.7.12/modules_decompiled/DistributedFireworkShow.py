# File: D (Python 2.2)

from ToontownGlobals import *
from IntervalGlobal import *
from ClockDelta import *
import ToontownGlobals
import DistributedObject
import Localizer
import Task
import Fireworks
import FireworkShows
import DDHood

class DistributedFireworkShow(DistributedObject.DistributedObject):
    notify = directNotify.newCategory('DistributedFireworkShow')
    notify.setDebug(1)
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.currentShow = None

    
    def generate(self):
        DistributedObject.DistributedObject.generate(self)

    
    def disable(self):
        DistributedObject.DistributedObject.disable(self)
        if self.currentShow:
            self.currentShow.pause()
            self.currentShow = None
            ivalMgr.finishIntervalsMatching('shootFirework*')
        
        if isinstance(self.getHood(), DDHood.DDHood):
            self.getHood().whiteFogColor = Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1)
        
        if hasattr(self.getHood(), 'loader'):
            self.getGeom().clearColorScale()
        
        if hasattr(self.getHood(), 'sky'):
            self.getSky().clearColorScale()
        

    
    def delete(self):
        DistributedObject.DistributedObject.delete(self)

    
    def startShow(self, style, timestamp):
        t = globalClockDelta.localElapsedTime(timestamp)
        self.currentShow = self.getFireworkShow(style, t)
        if self.currentShow:
            self.currentShow.play(t)
        
        return None

    
    def localShootFirework(self):
        pos = toonbase.localToon.getPos(render)
        style = 1
        color = 0
        self.d_requestFirework(pos[0], pos[1], pos[2], style, color, color)

    
    def d_requestFirework(self, x, y, z, style, color1, color2):
        self.sendUpdate('requestFirework', (x, y, z, style, color1, color2))

    
    def shootFirework(self, x, y, z, style, color1, color2):
        amp = 5
        Fireworks.shootFirework(style, x, y, z, color1, color2, amp)
        return None

    
    def getFireworkShow(self, index, t):
        show = FireworkShows.getShow(index)
        if show is None:
            self.notify.warning('could not find firework show: index' % index)
            return None
        
        track = Sequence()
        dark = 0.5
        skyDark = 0.0
        currentT = 0.0
        
        def checkDDFog():
            if isinstance(self.getHood(), DDHood.DDHood):
                self.getHood().whiteFogColor = Vec4(0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 1)
                if not (toonbase.tcr.playGame.getPlace().cameraSubmerged):
                    self.getHood().setWhiteFog()
                
            

        
        def restoreDDFog():
            if isinstance(self.getHood(), DDHood.DDHood):
                self.getHood().whiteFogColor = Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1)
                if not (toonbase.tcr.playGame.getPlace().cameraSubmerged):
                    self.getHood().setWhiteFog()
                
            

        showMusic = loader.loadMusic('phase_4/audio/bgm/firework_music.mid')
        showMusic.setVolume(1)
        track.extend((Func(toonbase.localToon.setSystemMessage, 0, Localizer.FireworksBeginning), Func(checkDDFog), Parallel(LerpColorScaleInterval(self.getGeom(), 2, Vec4(dark, dark, dark, 1)), LerpColorScaleInterval(self.getSky(), 2, Vec4(skyDark, skyDark, skyDark, 1))), Func(toonbase.localToon.setSystemMessage, 0, Localizer.FireworksInstructions), Wait(2), Func(self.getLoader().music.stop), Func(base.playMusic, showMusic, 0, 1, 0.80000000000000004, t), Wait(1)))
        currentT = 7.0
        for effect in show:
            (waitTime, style, colorIndex1, colorIndex2, amp, x, y, z) = effect
            if waitTime > 0:
                currentT += waitTime
                track.append(Wait(waitTime))
            
            if currentT >= t:
                track.append(Func(Fireworks.shootFirework, style, x, y, z, colorIndex1, colorIndex2, amp))
            
        
        track.extend((Wait(4), Func(restoreDDFog), Parallel(LerpColorScaleInterval(self.getGeom(), 2, Vec4(1, 1, 1, 1)), LerpColorScaleInterval(self.getSky(), 2, Vec4(1, 1, 1, 1))), Func(self.getGeom().clearColorScale), Func(self.getSky().clearColorScale), Func(showMusic.stop), Func(toonbase.localToon.setSystemMessage, 0, Localizer.FireworksEnding), Wait(0.5), Func(base.playMusic, self.getLoader().music, 1, 1, 0.80000000000000004)))
        return track

    
    def getLoader(self):
        if toonbase.tcr.playGame.hood != None:
            return toonbase.tcr.playGame.hood.loader
        

    
    def getHood(self):
        if toonbase.tcr.playGame.hood != None:
            return toonbase.tcr.playGame.hood
        

    
    def getGeom(self):
        loader = self.getLoader()
        if loader:
            return loader.geom
        
        return None

    
    def getSky(self):
        hood = self.getHood()
        if hood:
            return hood.sky
        
        return None


