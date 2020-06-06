# File: L (Python 2.2)

from pandac.PandaModules import *
from direct.directnotify.DirectNotifyGlobal import *
import Interval
from direct.showbase import LerpBlendHelpers

class LerpNodePathInterval(CLerpNodePathInterval):
    lerpNodePathNum = 1
    
    def __init__(self, name, duration, blendType, bakeInStart, fluid, nodePath, other):
        if name == None:
            name = '%s-%d' % (self.__class__.__name__, self.lerpNodePathNum)
            LerpNodePathInterval.lerpNodePathNum += 1
        
        blendType = self.stringBlendType(blendType)
        if other == None:
            other = NodePath()
        
        CLerpNodePathInterval.__init__(self, name, duration, blendType, bakeInStart, fluid, nodePath, other)

    
    def anyCallable(self, *params):
        for param in params:
            if callable(param):
                return 1
            
        
        return 0

    
    def setupParam(self, func, param):
        if param != None:
            if callable(param):
                func(param())
            else:
                func(param)
        



class LerpPosInterval(LerpNodePathInterval):
    
    def __init__(self, nodePath, duration, pos, startPos = None, other = None, blendType = 'noBlend', bakeInStart = 1, fluid = 0, name = None):
        LerpNodePathInterval.__init__(self, name, duration, blendType, bakeInStart, fluid, nodePath, other)
        self.paramSetup = self.anyCallable(pos, startPos)
        if self.paramSetup:
            self.endPos = pos
            self.startPos = startPos
            self.inPython = 1
        else:
            self.setEndPos(pos)
            if startPos != None:
                self.setStartPos(startPos)
            

    
    def privDoEvent(self, t, event):
        if self.paramSetup and event == CInterval.ETInitialize:
            self.setupParam(self.setEndPos, self.endPos)
            self.setupParam(self.setStartPos, self.startPos)
        
        LerpNodePathInterval.privDoEvent(self, t, event)



class LerpHprInterval(LerpNodePathInterval):
    
    def __init__(self, nodePath, duration, hpr, startHpr = None, startQuat = None, other = None, blendType = 'noBlend', bakeInStart = 1, fluid = 0, name = None):
        LerpNodePathInterval.__init__(self, name, duration, blendType, bakeInStart, fluid, nodePath, other)
        self.paramSetup = self.anyCallable(hpr, startHpr, startQuat)
        if self.paramSetup:
            self.endHpr = hpr
            self.startHpr = startHpr
            self.startQuat = startQuat
            self.inPython = 1
        else:
            self.setEndHpr(hpr)
            if startHpr != None:
                self.setStartHpr(startHpr)
            
            if startQuat != None:
                self.setStartQuat(startQuat)
            

    
    def privDoEvent(self, t, event):
        if self.paramSetup and event == CInterval.ETInitialize:
            self.setupParam(self.setEndHpr, self.endHpr)
            self.setupParam(self.setStartHpr, self.startHpr)
            self.setupParam(self.setStartQuat, self.startQuat)
        
        LerpNodePathInterval.privDoEvent(self, t, event)



class LerpQuatInterval(LerpNodePathInterval):
    
    def __init__(self, nodePath, duration, quat, startHpr = None, startQuat = None, other = None, blendType = 'noBlend', bakeInStart = 1, fluid = 0, name = None):
        LerpNodePathInterval.__init__(self, name, duration, blendType, bakeInStart, fluid, nodePath, other)
        self.paramSetup = self.anyCallable(quat, startHpr, startQuat)
        if self.paramSetup:
            self.endQuat = quat
            self.startHpr = startHpr
            self.startQuat = startQuat
            self.inPython = 1
        else:
            self.setEndQuat(quat)
            if startHpr != None:
                self.setStartHpr(startHpr)
            
            if startQuat != None:
                self.setStartQuat(startQuat)
            

    
    def privDoEvent(self, t, event):
        if self.paramSetup and event == CInterval.ETInitialize:
            self.setupParam(self.setEndQuat, self.endQuat)
            self.setupParam(self.setStartHpr, self.startHpr)
            self.setupParam(self.setStartQuat, self.startQuat)
        
        LerpNodePathInterval.privDoEvent(self, t, event)



class LerpScaleInterval(LerpNodePathInterval):
    
    def __init__(self, nodePath, duration, scale, startScale = None, other = None, blendType = 'noBlend', bakeInStart = 1, fluid = 0, name = None):
        LerpNodePathInterval.__init__(self, name, duration, blendType, bakeInStart, fluid, nodePath, other)
        self.paramSetup = self.anyCallable(scale, startScale)
        if self.paramSetup:
            self.endScale = scale
            self.startScale = startScale
            self.inPython = 1
        else:
            self.setEndScale(scale)
            if startScale != None:
                self.setStartScale(startScale)
            

    
    def privDoEvent(self, t, event):
        if self.paramSetup and event == CInterval.ETInitialize:
            self.setupParam(self.setEndScale, self.endScale)
            self.setupParam(self.setStartScale, self.startScale)
        
        LerpNodePathInterval.privDoEvent(self, t, event)



class LerpShearInterval(LerpNodePathInterval):
    
    def __init__(self, nodePath, duration, shear, startShear = None, other = None, blendType = 'noBlend', bakeInStart = 1, fluid = 0, name = None):
        LerpNodePathInterval.__init__(self, name, duration, blendType, bakeInStart, fluid, nodePath, other)
        self.paramSetup = self.anyCallable(shear, startShear)
        if self.paramSetup:
            self.endShear = shear
            self.startShear = startShear
            self.inPython = 1
        else:
            self.setEndShear(shear)
            if startShear != None:
                self.setStartShear(startShear)
            

    
    def privDoEvent(self, t, event):
        if self.paramSetup and event == CInterval.ETInitialize:
            self.setupParam(self.setEndShear, self.endShear)
            self.setupParam(self.setStartShear, self.startShear)
        
        LerpNodePathInterval.privDoEvent(self, t, event)



class LerpPosHprInterval(LerpNodePathInterval):
    
    def __init__(self, nodePath, duration, pos, hpr, startPos = None, startHpr = None, startQuat = None, other = None, blendType = 'noBlend', bakeInStart = 1, fluid = 0, name = None):
        LerpNodePathInterval.__init__(self, name, duration, blendType, bakeInStart, fluid, nodePath, other)
        self.paramSetup = self.anyCallable(pos, startPos, hpr, startHpr, startQuat)
        if self.paramSetup:
            self.endPos = pos
            self.startPos = startPos
            self.endHpr = hpr
            self.startHpr = startHpr
            self.startQuat = startQuat
            self.inPython = 1
        else:
            self.setEndPos(pos)
            if startPos != None:
                self.setStartPos(startPos)
            
            self.setEndHpr(hpr)
            if startHpr != None:
                self.setStartHpr(startHpr)
            
            if startQuat != None:
                self.setStartQuat(startQuat)
            

    
    def privDoEvent(self, t, event):
        if self.paramSetup and event == CInterval.ETInitialize:
            self.setupParam(self.setEndPos, self.endPos)
            self.setupParam(self.setStartPos, self.startPos)
            self.setupParam(self.setEndHpr, self.endHpr)
            self.setupParam(self.setStartHpr, self.startHpr)
            self.setupParam(self.setStartQuat, self.startQuat)
        
        LerpNodePathInterval.privDoEvent(self, t, event)



class LerpPosQuatInterval(LerpNodePathInterval):
    
    def __init__(self, nodePath, duration, pos, quat, startPos = None, startHpr = None, startQuat = None, other = None, blendType = 'noBlend', bakeInStart = 1, fluid = 0, name = None):
        LerpNodePathInterval.__init__(self, name, duration, blendType, bakeInStart, fluid, nodePath, other)
        self.paramSetup = self.anyCallable(pos, startPos, quat, startHpr, startQuat)
        if self.paramSetup:
            self.endPos = pos
            self.startPos = startPos
            self.endQuat = quat
            self.startHpr = startHpr
            self.startQuat = startQuat
            self.inPython = 1
        else:
            self.setEndPos(pos)
            if startPos != None:
                self.setStartPos(startPos)
            
            self.setEndQuat(quat)
            if startHpr != None:
                self.setStartHpr(startHpr)
            
            if startQuat != None:
                self.setStartQuat(startQuat)
            

    
    def privDoEvent(self, t, event):
        if self.paramSetup and event == CInterval.ETInitialize:
            self.setupParam(self.setEndPos, self.endPos)
            self.setupParam(self.setStartPos, self.startPos)
            self.setupParam(self.setEndQuat, self.endQuat)
            self.setupParam(self.setStartHpr, self.startHpr)
            self.setupParam(self.setStartQuat, self.startQuat)
        
        LerpNodePathInterval.privDoEvent(self, t, event)



class LerpHprScaleInterval(LerpNodePathInterval):
    
    def __init__(self, nodePath, duration, hpr, scale, startHpr = None, startQuat = None, startScale = None, other = None, blendType = 'noBlend', bakeInStart = 1, fluid = 0, name = None):
        LerpNodePathInterval.__init__(self, name, duration, blendType, bakeInStart, fluid, nodePath, other)
        self.paramSetup = self.anyCallable(hpr, startHpr, startQuat, scale, startScale)
        if self.paramSetup:
            self.endHpr = hpr
            self.startHpr = startHpr
            self.startQuat = startQuat
            self.endScale = scale
            self.startScale = startScale
            self.inPython = 1
        else:
            self.setEndHpr(hpr)
            if startHpr != None:
                self.setStartHpr(startHpr)
            
            if startQuat != None:
                self.setStartQuat(startQuat)
            
            self.setEndScale(scale)
            if startScale != None:
                self.setStartScale(startScale)
            

    
    def privDoEvent(self, t, event):
        if self.paramSetup and event == CInterval.ETInitialize:
            self.setupParam(self.setEndHpr, self.endHpr)
            self.setupParam(self.setStartHpr, self.startHpr)
            self.setupParam(self.setStartQuat, self.startQuat)
            self.setupParam(self.setEndScale, self.endScale)
            self.setupParam(self.setStartScale, self.startScale)
        
        LerpNodePathInterval.privDoEvent(self, t, event)



class LerpQuatScaleInterval(LerpNodePathInterval):
    
    def __init__(self, nodePath, duration, quat, scale, startHpr = None, startQuat = None, startScale = None, other = None, blendType = 'noBlend', bakeInStart = 1, fluid = 0, name = None):
        LerpNodePathInterval.__init__(self, name, duration, blendType, bakeInStart, fluid, nodePath, other)
        self.paramSetup = self.anyCallable(quat, startHpr, startQuat, scale, startScale)
        if self.paramSetup:
            self.endQuat = quat
            self.startHpr = startHpr
            self.startQuat = startQuat
            self.endScale = scale
            self.startScale = startScale
            self.inPython = 1
        else:
            self.setEndQuat(quat)
            if startHpr != None:
                self.setStartHpr(startHpr)
            
            if startQuat != None:
                self.setStartQuat(startQuat)
            
            self.setEndScale(scale)
            if startScale != None:
                self.setStartScale(startScale)
            

    
    def privDoEvent(self, t, event):
        if self.paramSetup and event == CInterval.ETInitialize:
            self.setupParam(self.setEndQuat, self.endQuat)
            self.setupParam(self.setStartHpr, self.startHpr)
            self.setupParam(self.setStartQuat, self.startQuat)
            self.setupParam(self.setEndScale, self.endScale)
            self.setupParam(self.setStartScale, self.startScale)
        
        LerpNodePathInterval.privDoEvent(self, t, event)



class LerpPosHprScaleInterval(LerpNodePathInterval):
    
    def __init__(self, nodePath, duration, pos, hpr, scale, startPos = None, startHpr = None, startQuat = None, startScale = None, other = None, blendType = 'noBlend', bakeInStart = 1, fluid = 0, name = None):
        LerpNodePathInterval.__init__(self, name, duration, blendType, bakeInStart, fluid, nodePath, other)
        self.paramSetup = self.anyCallable(pos, startPos, hpr, startHpr, startQuat, scale, startScale)
        if self.paramSetup:
            self.endPos = pos
            self.startPos = startPos
            self.endHpr = hpr
            self.startHpr = startHpr
            self.startQuat = startQuat
            self.endScale = scale
            self.startScale = startScale
            self.inPython = 1
        else:
            self.setEndPos(pos)
            if startPos != None:
                self.setStartPos(startPos)
            
            self.setEndHpr(hpr)
            if startHpr != None:
                self.setStartHpr(startHpr)
            
            if startQuat != None:
                self.setStartQuat(startQuat)
            
            self.setEndScale(scale)
            if startScale != None:
                self.setStartScale(startScale)
            

    
    def privDoEvent(self, t, event):
        if self.paramSetup and event == CInterval.ETInitialize:
            self.setupParam(self.setEndPos, self.endPos)
            self.setupParam(self.setStartPos, self.startPos)
            self.setupParam(self.setEndHpr, self.endHpr)
            self.setupParam(self.setStartHpr, self.startHpr)
            self.setupParam(self.setStartQuat, self.startQuat)
            self.setupParam(self.setEndScale, self.endScale)
            self.setupParam(self.setStartScale, self.startScale)
        
        LerpNodePathInterval.privDoEvent(self, t, event)



class LerpPosQuatScaleInterval(LerpNodePathInterval):
    
    def __init__(self, nodePath, duration, pos, quat, scale, startPos = None, startHpr = None, startQuat = None, startScale = None, other = None, blendType = 'noBlend', bakeInStart = 1, fluid = 0, name = None):
        LerpNodePathInterval.__init__(self, name, duration, blendType, bakeInStart, fluid, nodePath, other)
        self.paramSetup = self.anyCallable(pos, startPos, quat, startHpr, startQuat, scale, startScale)
        if self.paramSetup:
            self.endPos = pos
            self.startPos = startPos
            self.endQuat = quat
            self.startHpr = startHpr
            self.startQuat = startQuat
            self.endScale = scale
            self.startScale = startScale
            self.inPython = 1
        else:
            self.setEndPos(pos)
            if startPos != None:
                self.setStartPos(startPos)
            
            self.setEndQuat(quat)
            if startHpr != None:
                self.setStartHpr(startHpr)
            
            if startQuat != None:
                self.setStartQuat(startQuat)
            
            self.setEndScale(scale)
            if startScale != None:
                self.setStartScale(startScale)
            

    
    def privDoEvent(self, t, event):
        if self.paramSetup and event == CInterval.ETInitialize:
            self.setupParam(self.setEndPos, self.endPos)
            self.setupParam(self.setStartPos, self.startPos)
            self.setupParam(self.setEndQuat, self.endQuat)
            self.setupParam(self.setStartHpr, self.startHpr)
            self.setupParam(self.setStartQuat, self.startQuat)
            self.setupParam(self.setEndScale, self.endScale)
            self.setupParam(self.setStartScale, self.startScale)
        
        LerpNodePathInterval.privDoEvent(self, t, event)



class LerpPosHprScaleShearInterval(LerpNodePathInterval):
    
    def __init__(self, nodePath, duration, pos, hpr, scale, shear, startPos = None, startHpr = None, startQuat = None, startScale = None, startShear = None, other = None, blendType = 'noBlend', bakeInStart = 1, fluid = 0, name = None):
        LerpNodePathInterval.__init__(self, name, duration, blendType, bakeInStart, fluid, nodePath, other)
        self.paramSetup = self.anyCallable(pos, startPos, hpr, startHpr, startQuat, scale, startScale, shear, startShear)
        if self.paramSetup:
            self.endPos = pos
            self.startPos = startPos
            self.endHpr = hpr
            self.startHpr = startHpr
            self.startQuat = startQuat
            self.endScale = scale
            self.startScale = startScale
            self.endShear = shear
            self.startShear = startShear
            self.inPython = 1
        else:
            self.setEndPos(pos)
            if startPos != None:
                self.setStartPos(startPos)
            
            self.setEndHpr(hpr)
            if startHpr != None:
                self.setStartHpr(startHpr)
            
            if startQuat != None:
                self.setStartQuat(startQuat)
            
            self.setEndScale(scale)
            if startScale != None:
                self.setStartScale(startScale)
            
            self.setEndShear(shear)
            if startShear != None:
                self.setStartShear(startShear)
            

    
    def privDoEvent(self, t, event):
        if self.paramSetup and event == CInterval.ETInitialize:
            self.setupParam(self.setEndPos, self.endPos)
            self.setupParam(self.setStartPos, self.startPos)
            self.setupParam(self.setEndHpr, self.endHpr)
            self.setupParam(self.setStartHpr, self.startHpr)
            self.setupParam(self.setStartQuat, self.startQuat)
            self.setupParam(self.setEndScale, self.endScale)
            self.setupParam(self.setStartScale, self.startScale)
            self.setupParam(self.setEndShear, self.endShear)
            self.setupParam(self.setStartShear, self.startShear)
        
        LerpNodePathInterval.privDoEvent(self, t, event)



class LerpPosQuatScaleShearInterval(LerpNodePathInterval):
    
    def __init__(self, nodePath, duration, pos, quat, scale, shear, startPos = None, startHpr = None, startQuat = None, startScale = None, startShear = None, other = None, blendType = 'noBlend', bakeInStart = 1, fluid = 0, name = None):
        LerpNodePathInterval.__init__(self, name, duration, blendType, bakeInStart, fluid, nodePath, other)
        self.paramSetup = self.anyCallable(pos, startPos, quat, startHpr, startQuat, scale, startScale, shear, startShear)
        if self.paramSetup:
            self.endPos = pos
            self.startPos = startPos
            self.endQuat = quat
            self.startHpr = startHpr
            self.startQuat = startQuat
            self.endScale = scale
            self.startScale = startScale
            self.endShear = shear
            self.startShear = startShear
            self.inPython = 1
        else:
            self.setEndPos(pos)
            if startPos != None:
                self.setStartPos(startPos)
            
            self.setEndQuat(quat)
            if startHpr != None:
                self.setStartHpr(startHpr)
            
            if startQuat != None:
                self.setStartQuat(startQuat)
            
            self.setEndScale(scale)
            if startScale != None:
                self.setStartScale(startScale)
            
            self.setEndShear(shear)
            if startShear != None:
                self.setStartShear(startShear)
            

    
    def privDoEvent(self, t, event):
        if self.paramSetup and event == CInterval.ETInitialize:
            self.setupParam(self.setEndPos, self.endPos)
            self.setupParam(self.setStartPos, self.startPos)
            self.setupParam(self.setEndQuat, self.endQuat)
            self.setupParam(self.setStartHpr, self.startHpr)
            self.setupParam(self.setStartQuat, self.startQuat)
            self.setupParam(self.setEndScale, self.endScale)
            self.setupParam(self.setStartScale, self.startScale)
            self.setupParam(self.setEndShear, self.endShear)
            self.setupParam(self.setStartShear, self.startShear)
        
        LerpNodePathInterval.privDoEvent(self, t, event)



class LerpColorScaleInterval(LerpNodePathInterval):
    
    def __init__(self, nodePath, duration, colorScale, startColorScale = None, other = None, blendType = 'noBlend', bakeInStart = 1, fluid = 0, name = None):
        LerpNodePathInterval.__init__(self, name, duration, blendType, bakeInStart, fluid, nodePath, other)
        self.setEndColorScale(colorScale)
        if startColorScale != None:
            self.setStartColorScale(startColorScale)
        



class LerpColorInterval(LerpNodePathInterval):
    
    def __init__(self, nodePath, duration, color, startColor = None, other = None, blendType = 'noBlend', bakeInStart = 1, fluid = 0, name = None):
        LerpNodePathInterval.__init__(self, name, duration, blendType, bakeInStart, fluid, nodePath, other)
        self.setEndColor(color)
        if startColor != None:
            self.setStartColor(startColor)
        



class LerpFunctionInterval(Interval.Interval):
    lerpFunctionIntervalNum = 1
    notify = directNotify.newCategory('LerpFunctionInterval')
    
    def __init__(self, function, fromData = 0, toData = 1, duration = 0.0, blendType = 'noBlend', extraArgs = [], name = None):
        self.function = function
        self.fromData = fromData
        self.toData = toData
        self.blendType = LerpBlendHelpers.getBlend(blendType)
        self.extraArgs = extraArgs
        if name == None:
            name = 'LerpFunctionInterval-%d' % LerpFunctionInterval.lerpFunctionIntervalNum
            LerpFunctionInterval.lerpFunctionIntervalNum += 1
        
        Interval.Interval.__init__(self, name, duration)

    
    def privStep(self, t):
        if t >= self.duration:
            apply(self.function, [
                self.toData] + self.extraArgs)
        elif self.duration == 0.0:
            apply(self.function, [
                self.toData] + self.extraArgs)
        else:
            bt = self.blendType(t / self.duration)
            data = self.fromData * (1 - bt) + self.toData * bt
            apply(self.function, [
                data] + self.extraArgs)
        self.notify.debug('updateFunc() - %s: t = %f' % (self.name, t))
        self.state = CInterval.SStarted
        self.currT = t



class LerpFunc(LerpFunctionInterval):
    
    def __init__(self, *args, **kw):
        LerpFunctionInterval.__init__(self, *args, **args)


