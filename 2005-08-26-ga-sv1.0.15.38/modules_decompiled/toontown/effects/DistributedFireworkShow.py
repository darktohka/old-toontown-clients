# File: D (Python 2.2)

from toontown.toonbase.ToontownGlobals import *
from direct.interval.IntervalGlobal import *
from direct.distributed.ClockDelta import *
from toontown.toonbase import ToontownGlobals
from direct.distributed import DistributedObject
from toontown.toonbase import TTLocalizer
from direct.task import Task
import Fireworks
import FireworkShows
from toontown.hood import DDHood

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

    
    def localShootFirework(self):
        pos = base.localAvatar.getPos(render)
        style = 1
        color = 0
        self.d_requestFirework(pos[0], pos[1], pos[2], style, color, color)

    
    def d_requestFirework(self, x, y, z, style, color1, color2):
        self.sendUpdate('requestFirework', (x, y, z, style, color1, color2))

    
    def shootFirework(self, x, y, z, style, color1, color2):
        amp = 5
        Fireworks.shootFirework(style, x, y, z, color1, color2, amp)
        return None

    
    def startShow(self, holidayId, style, timestamp):
        t = globalClockDelta.localElapsedTime(timestamp)
        self.currentShow = self.getFireworkShowIval(holidayId, style, t)
        if self.currentShow:
            self.currentShow.start(t)
        
        return None

    
    def getFireworkShowIval(self, holidayId, index, startT):
        
        def checkDDFog():
            if isinstance(self.getHood(), DDHood.DDHood):
                self.getHood().whiteFogColor = Vec4(0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 1)
                if not (base.cr.playGame.getPlace().cameraSubmerged):
                    self.getHood().setWhiteFog()
                
            

        
        def restoreDDFog():
            if isinstance(self.getHood(), DDHood.DDHood):
                self.getHood().whiteFogColor = Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1)
                if not (base.cr.playGame.getPlace().cameraSubmerged):
                    self.getHood().setWhiteFog()
                
            

        if holidayId == JULY4_FIREWORKS:
            startMessage = TTLocalizer.FireworksJuly4Beginning
            endMessage = TTLocalizer.FireworksJuly4Ending
            musicFile = 'phase_4/audio/bgm/firework_music.mid'
        elif holidayId == NEWYEARS_FIREWORKS:
            startMessage = TTLocalizer.FireworksNewYearsEveBeginning
            endMessage = TTLocalizer.FireworksNewYearsEveEnding
            musicFile = 'phase_4/audio/bgm/new_years_fireworks_music.mid'
        else:
            self.notify.warning('Invalid fireworks holiday ID: %d' % holidayId)
            return None
        showMusic = loader.loadMusic(musicFile)
        showMusic.setVolume(1)
        show = FireworkShows.getShow(holidayId, index)
        if show is None:
            self.notify.warning('could not find firework show: index: %s' % index)
            return None
        
        dark = 0.5
        skyDark = 0.0
        preShow = Sequence(Func(base.localAvatar.setSystemMessage, 0, startMessage), Func(checkDDFog), Parallel(LerpColorScaleInterval(self.getGeom(), 2, Vec4(dark, dark, dark, 1)), LerpColorScaleInterval(self.getSky(), 2, Vec4(skyDark, skyDark, skyDark, 1))), Func(base.localAvatar.setSystemMessage, 0, TTLocalizer.FireworksInstructions), Wait(2), Func(self.getLoader().music.stop), Func(base.playMusic, showMusic, 0, 1, 0.80000000000000004, max(0, startT - 4)))
        mainShow = Sequence()
        currentT = 4.0
        for effect in show:
            (waitTime, style, colorIndex1, colorIndex2, amp, x, y, z) = effect
            if waitTime > 0:
                currentT += waitTime
                mainShow.append(Wait(waitTime))
            
            if currentT >= startT:
                mainShow.append(Func(Fireworks.shootFirework, style, x, y, z, colorIndex1, colorIndex2, amp))
            
        
        postShow = Sequence(Wait(4), Func(restoreDDFog), Parallel(LerpColorScaleInterval(self.getGeom(), 2, Vec4(1, 1, 1, 1)), LerpColorScaleInterval(self.getSky(), 2, Vec4(1, 1, 1, 1))), Func(self.getGeom().clearColorScale), Func(self.getSky().clearColorScale), Func(showMusic.stop), Func(base.localAvatar.setSystemMessage, 0, endMessage), Wait(0.5), Func(base.playMusic, self.getLoader().music, 1, 1, 0.80000000000000004))
        return Sequence(preShow, mainShow, postShow)

    
    def getLoader(self):
        if base.cr.playGame.hood != None:
            return base.cr.playGame.hood.loader
        

    
    def getHood(self):
        if base.cr.playGame.hood != None:
            return base.cr.playGame.hood
        

    
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


