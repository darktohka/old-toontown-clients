# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\built\lib\pandac\libpandaModules.py
from extension_native_helpers import *
Dtool_PreloadDLL('libpanda')
from libpanda import *
from extension_native_helpers import *
Dtool_PreloadDLL('libpanda')
from libpanda import *

def pPrintValues(self):
    return '\n%s\n%s\n%s' % (self.getRow(0).pPrintValues(), self.getRow(1).pPrintValues(), self.getRow(2).pPrintValues())


Dtool_funcToMethod(pPrintValues, Mat3)
del pPrintValues
from extension_native_helpers import *
Dtool_PreloadDLL('libpanda')
from libpanda import *

def asList(self):
    print 'Warning: NodePathCollection.asList() is no longer needed and deprecated.  Iterate on the collection directly instead.'
    return list(self)


Dtool_funcToMethod(asList, NodePathCollection)
del asList

def getTightBounds(self):
    from pandac.PandaModules import Point3
    if self.getNumPaths() == 0:
        return (
         Point3.Point3(0), Point3.Point3(0))
    (v1, v2) = self.getPath(0).getTightBounds()
    for i in range(1, self.getNumPaths()):
        (v1x, v2x) = self.getPath(i).getTightBounds()
        v1 = Point3.Point3(min(v1[0], v1x[0]), min(v1[1], v1x[1]), min(v1[2], v1x[2]))
        v2 = Point3.Point3(max(v2[0], v2x[0]), max(v2[1], v2x[1]), max(v2[2], v2x[2]))

    return (
     v1, v2)


Dtool_funcToMethod(getTightBounds, NodePathCollection)
del getTightBounds
from extension_native_helpers import *
Dtool_PreloadDLL('libpanda')
from libpanda import *

def pPrintValues(self):
    return '% 10.4f, % 10.4f, % 10.4f' % (self[0], self[1], self[2])


Dtool_funcToMethod(pPrintValues, VBase3)
del pPrintValues

def asTuple(self):
    print 'Warning: VBase3.asTuple() is no longer needed and deprecated.  Use the vector directly instead.'
    return tuple(self)


Dtool_funcToMethod(asTuple, VBase3)
del asTuple
from extension_native_helpers import *
Dtool_PreloadDLL('libpanda')
from libpanda import *

def pPrintValues(self):
    return '% 10.4f, % 10.4f, % 10.4f, % 10.4f' % (self[0], self[1], self[2], self[3])


Dtool_funcToMethod(pPrintValues, VBase4)
del pPrintValues

def asTuple(self):
    print 'Warning: VBase4.asTuple() is no longer needed and deprecated.  Use the vector directly instead.'
    return tuple(self)


Dtool_funcToMethod(asTuple, VBase4)
del asTuple
from extension_native_helpers import *
Dtool_PreloadDLL('libpanda')
from libpanda import *

def id(self):
    return self.getKey()


Dtool_funcToMethod(id, NodePath)
del id

def getChildrenAsList(self):
    print 'Warning: NodePath.getChildrenAsList() is deprecated.  Use getChildren() instead.'
    return list(self.getChildren())


Dtool_funcToMethod(getChildrenAsList, NodePath)
del getChildrenAsList

def printChildren(self):
    for child in self.getChildren():
        print child.getName()


Dtool_funcToMethod(printChildren, NodePath)
del printChildren

def removeChildren(self):
    self.getChildren().detach()


Dtool_funcToMethod(removeChildren, NodePath)
del removeChildren

def toggleVis(self):
    if self.isHidden():
        self.show()
        return 1
    else:
        self.hide()
        return 0


Dtool_funcToMethod(toggleVis, NodePath)
del toggleVis

def showSiblings(self):
    for sib in self.getParent().getChildren():
        if sib.node() != self.node():
            sib.show()


Dtool_funcToMethod(showSiblings, NodePath)
del showSiblings

def hideSiblings(self):
    for sib in self.getParent().getChildren():
        if sib.node() != self.node():
            sib.hide()


Dtool_funcToMethod(hideSiblings, NodePath)
del hideSiblings

def showAllDescendants(self):
    self.show()
    for child in self.getChildren():
        child.showAllDescendants()


Dtool_funcToMethod(showAllDescendants, NodePath)
del showAllDescendants

def isolate(self):
    self.showAllDescendants()
    self.hideSiblings()


Dtool_funcToMethod(isolate, NodePath)
del isolate

def remove(self):
    messenger.send('preRemoveNodePath', [self])
    self.removeNode()


Dtool_funcToMethod(remove, NodePath)
del remove

def lsNames(self):
    if self.isEmpty():
        print '(empty)'
    else:
        type = self.node().getType().getName()
        name = self.getName()
        print type + '  ' + name
        self.lsNamesRecurse()


Dtool_funcToMethod(lsNames, NodePath)
del lsNames

def lsNamesRecurse(self, indentString=' '):
    for nodePath in self.getChildren():
        type = nodePath.node().getType().getName()
        name = nodePath.getName()
        print indentString + type + '  ' + name
        nodePath.lsNamesRecurse(indentString + ' ')


Dtool_funcToMethod(lsNamesRecurse, NodePath)
del lsNamesRecurse

def reverseLsNames(self):
    ancestors = list(self.getAncestors())
    ancestry = ancestors.reverse()
    indentString = ''
    for nodePath in ancestry:
        type = nodePath.node().getType().getName()
        name = nodePath.getName()
        print indentString + type + '  ' + name
        indentString = indentString + ' '


Dtool_funcToMethod(reverseLsNames, NodePath)
del reverseLsNames

def getAncestry(self):
    print 'NodePath.getAncestry() is deprecated.  Use getAncestors() instead.'
    ancestors = list(self.getAncestors())
    ancestors.reverse()
    return ancestors


Dtool_funcToMethod(getAncestry, NodePath)
del getAncestry

def getTightBounds(self):
    from pandac.PandaModules import Point3
    v1 = Point3.Point3(0)
    v2 = Point3.Point3(0)
    self.calcTightBounds(v1, v2)
    return (v1, v2)


Dtool_funcToMethod(getTightBounds, NodePath)
del getTightBounds

def pPrintString(self, other=None):
    pass


Dtool_funcToMethod(pPrintString, NodePath)
del pPrintString

def printPos(self, other=None, sd=2):
    formatString = '%0.' + '%d' % sd + 'f'
    if other:
        pos = self.getPos(other)
        otherString = other.getName() + ', '
    else:
        pos = self.getPos()
        otherString = ''
    print self.getName() + '.setPos(' + otherString + formatString % pos[0] + ', ' + formatString % pos[1] + ', ' + formatString % pos[2] + ')\n'


Dtool_funcToMethod(printPos, NodePath)
del printPos

def printHpr(self, other=None, sd=2):
    formatString = '%0.' + '%d' % sd + 'f'
    if other:
        hpr = self.getHpr(other)
        otherString = other.getName() + ', '
    else:
        hpr = self.getHpr()
        otherString = ''
    print self.getName() + '.setHpr(' + otherString + formatString % hpr[0] + ', ' + formatString % hpr[1] + ', ' + formatString % hpr[2] + ')\n'


Dtool_funcToMethod(printHpr, NodePath)
del printHpr

def printScale(self, other=None, sd=2):
    formatString = '%0.' + '%d' % sd + 'f'
    if other:
        scale = self.getScale(other)
        otherString = other.getName() + ', '
    else:
        scale = self.getScale()
        otherString = ''
    print self.getName() + '.setScale(' + otherString + formatString % scale[0] + ', ' + formatString % scale[1] + ', ' + formatString % scale[2] + ')\n'


Dtool_funcToMethod(printScale, NodePath)
del printScale

def printPosHpr(self, other=None, sd=2):
    formatString = '%0.' + '%d' % sd + 'f'
    if other:
        pos = self.getPos(other)
        hpr = self.getHpr(other)
        otherString = other.getName() + ', '
    else:
        pos = self.getPos()
        hpr = self.getHpr()
        otherString = ''
    print self.getName() + '.setPosHpr(' + otherString + formatString % pos[0] + ', ' + formatString % pos[1] + ', ' + formatString % pos[2] + ', ' + formatString % hpr[0] + ', ' + formatString % hpr[1] + ', ' + formatString % hpr[2] + ')\n'


Dtool_funcToMethod(printPosHpr, NodePath)
del printPosHpr

def printPosHprScale(self, other=None, sd=2):
    formatString = '%0.' + '%d' % sd + 'f'
    if other:
        pos = self.getPos(other)
        hpr = self.getHpr(other)
        scale = self.getScale(other)
        otherString = other.getName() + ', '
    else:
        pos = self.getPos()
        hpr = self.getHpr()
        scale = self.getScale()
        otherString = ''
    print self.getName() + '.setPosHprScale(' + otherString + formatString % pos[0] + ', ' + formatString % pos[1] + ', ' + formatString % pos[2] + ', ' + formatString % hpr[0] + ', ' + formatString % hpr[1] + ', ' + formatString % hpr[2] + ', ' + formatString % scale[0] + ', ' + formatString % scale[1] + ', ' + formatString % scale[2] + ')\n'


Dtool_funcToMethod(printPosHprScale, NodePath)
del printPosHprScale

def printTransform(self, other=None, sd=2, fRecursive=0):
    from pandac.PandaModules import Vec3
    fmtStr = '%%0.%df' % sd
    name = self.getName()
    if other == None:
        transform = self.getTransform()
    else:
        transform = self.getTransform(other)
    if transform.hasPos():
        pos = transform.getPos()
        if not pos.almostEqual(Vec3(0)):
            outputString = '%s.setPos(%s, %s, %s)' % (name, fmtStr, fmtStr, fmtStr)
            print outputString % (pos[0], pos[1], pos[2])
    if transform.hasHpr():
        hpr = transform.getHpr()
        if not hpr.almostEqual(Vec3(0)):
            outputString = '%s.setHpr(%s, %s, %s)' % (name, fmtStr, fmtStr, fmtStr)
            print outputString % (hpr[0], hpr[1], hpr[2])
    if transform.hasScale():
        if transform.hasUniformScale():
            scale = transform.getUniformScale()
            if scale != 1.0:
                outputString = '%s.setScale(%s)' % (name, fmtStr)
                print outputString % scale
        else:
            scale = transform.getScale()
            if not scale.almostEqual(Vec3(1)):
                outputString = '%s.setScale(%s, %s, %s)' % (name, fmtStr, fmtStr, fmtStr)
                print outputString % (scale[0], scale[1], scale[2])
    if fRecursive:
        for child in self.getChildren():
            child.printTransform(other, sd, fRecursive)

    return


Dtool_funcToMethod(printTransform, NodePath)
del printTransform

def iPos(self, other=None):
    if other:
        self.setPos(other, 0, 0, 0)
    else:
        self.setPos(0, 0, 0)


Dtool_funcToMethod(iPos, NodePath)
del iPos

def iHpr(self, other=None):
    if other:
        self.setHpr(other, 0, 0, 0)
    else:
        self.setHpr(0, 0, 0)


Dtool_funcToMethod(iHpr, NodePath)
del iHpr

def iScale(self, other=None):
    if other:
        self.setScale(other, 1, 1, 1)
    else:
        self.setScale(1, 1, 1)


Dtool_funcToMethod(iScale, NodePath)
del iScale

def iPosHpr(self, other=None):
    if other:
        self.setPosHpr(other, 0, 0, 0, 0, 0, 0)
    else:
        self.setPosHpr(0, 0, 0, 0, 0, 0)


Dtool_funcToMethod(iPosHpr, NodePath)
del iPosHpr

def iPosHprScale(self, other=None):
    if other:
        self.setPosHprScale(other, 0, 0, 0, 0, 0, 0, 1, 1, 1)
    else:
        self.setPosHprScale(0, 0, 0, 0, 0, 0, 1, 1, 1)


Dtool_funcToMethod(iPosHprScale, NodePath)
del iPosHprScale

def __lerp(self, functorFunc, duration, blendType, taskName=None):
    from direct.task import Task
    from direct.showbase import LerpBlendHelpers
    from direct.task.TaskManagerGlobal import taskMgr

    def lerpTaskFunc(task):
        from pandac.PandaModules import Lerp
        from pandac.PandaModules import ClockObject
        from direct.task.Task import Task, cont, done
        if task.init == 1:
            functor = task.functorFunc()
            task.lerp = Lerp(functor, task.duration, task.blendType)
            task.init = 0
        dt = globalClock.getDt()
        task.lerp.setStepSize(dt)
        task.lerp.step()
        if task.lerp.isDone():
            task.init = 1
            return done
        else:
            return cont

    lerpTask = Task.Task(lerpTaskFunc)
    lerpTask.init = 1
    lerpTask.functorFunc = functorFunc
    lerpTask.duration = duration
    lerpTask.blendType = LerpBlendHelpers.getBlend(blendType)
    if taskName == None:
        return lerpTask
    else:
        taskMgr.add(lerpTask, taskName)
        return lerpTask
    return


Dtool_funcToMethod(__lerp, NodePath)
del __lerp

def __autoLerp(self, functorFunc, time, blendType, taskName):
    from pandac.PandaModules import AutonomousLerp
    from direct.showbase import LerpBlendHelpers
    functor = functorFunc()
    lerp = AutonomousLerp.AutonomousLerp(functor, time, LerpBlendHelpers.getBlend(blendType), base.eventHandler)
    lerp.start()
    return lerp


Dtool_funcToMethod(__autoLerp, NodePath)
del __autoLerp

def lerpColor(self, *posArgs, **keyArgs):
    if len(posArgs) == 2:
        return apply(self.lerpColorVBase4, posArgs, keyArgs)
    elif len(posArgs) == 3:
        return apply(self.lerpColorVBase4VBase4, posArgs, keyArgs)
    elif len(posArgs) == 5:
        return apply(self.lerpColorRGBA, posArgs, keyArgs)
    elif len(posArgs) == 9:
        return apply(self.lerpColorRGBARGBA, posArgs, keyArgs)
    else:
        raise Exception('Error: NodePath.lerpColor: bad number of args')


Dtool_funcToMethod(lerpColor, NodePath)
del lerpColor

def lerpColorRGBA(self, r, g, b, a, time, blendType='noBlend', auto=None, task=None):

    def functorFunc(self=self, r=r, g=g, b=b, a=a):
        from pandac.PandaModules import ColorLerpFunctor
        startColor = self.getColor()
        functor = ColorLerpFunctor.ColorLerpFunctor(self, startColor[0], startColor[1], startColor[2], startColor[3], r, g, b, a)
        return functor

    if auto != None:
        return self.__autoLerp(functorFunc, time, blendType, auto)
    elif task != None:
        return self.__lerp(functorFunc, time, blendType, task)
    else:
        return self.__lerp(functorFunc, time, blendType)
    return


Dtool_funcToMethod(lerpColorRGBA, NodePath)
del lerpColorRGBA

def lerpColorRGBARGBA(self, sr, sg, sb, sa, er, eg, eb, ea, time, blendType='noBlend', auto=None, task=None):

    def functorFunc(self=self, sr=sr, sg=sg, sb=sb, sa=sa, er=er, eg=eg, eb=eb, ea=ea):
        from pandac.PandaModules import ColorLerpFunctor
        functor = ColorLerpFunctor.ColorLerpFunctor(self, sr, sg, sb, sa, er, eg, eb, ea)
        return functor

    if auto != None:
        return self.__autoLerp(functorFunc, time, blendType, auto)
    elif task != None:
        return self.__lerp(functorFunc, time, blendType, task)
    else:
        return self.__lerp(functorFunc, time, blendType)
    return


Dtool_funcToMethod(lerpColorRGBARGBA, NodePath)
del lerpColorRGBARGBA

def lerpColorVBase4(self, endColor, time, blendType='noBlend', auto=None, task=None):

    def functorFunc(self=self, endColor=endColor):
        from pandac.PandaModules import ColorLerpFunctor
        startColor = self.getColor()
        functor = ColorLerpFunctor.ColorLerpFunctor(self, startColor, endColor)
        return functor

    if auto != None:
        return self.__autoLerp(functorFunc, time, blendType, auto)
    elif task != None:
        return self.__lerp(functorFunc, time, blendType, task)
    else:
        return self.__lerp(functorFunc, time, blendType)
    return


Dtool_funcToMethod(lerpColorVBase4, NodePath)
del lerpColorVBase4

def lerpColorVBase4VBase4(self, startColor, endColor, time, blendType='noBlend', auto=None, task=None):

    def functorFunc(self=self, startColor=startColor, endColor=endColor):
        from pandac.PandaModules import ColorLerpFunctor
        functor = ColorLerpFunctor.ColorLerpFunctor(self, startColor, endColor)
        return functor

    if auto != None:
        return self.__autoLerp(functorFunc, time, blendType, auto)
    elif task != None:
        return self.__lerp(functorFunc, time, blendType, task)
    else:
        return self.__lerp(functorFunc, time, blendType)
    return


Dtool_funcToMethod(lerpColorVBase4VBase4, NodePath)
del lerpColorVBase4VBase4

def lerpColorScale(self, *posArgs, **keyArgs):
    if len(posArgs) == 2:
        return apply(self.lerpColorScaleVBase4, posArgs, keyArgs)
    elif len(posArgs) == 3:
        return apply(self.lerpColorScaleVBase4VBase4, posArgs, keyArgs)
    elif len(posArgs) == 5:
        return apply(self.lerpColorScaleRGBA, posArgs, keyArgs)
    elif len(posArgs) == 9:
        return apply(self.lerpColorScaleRGBARGBA, posArgs, keyArgs)
    else:
        raise Exception('Error: NodePath.lerpColorScale: bad number of args')


Dtool_funcToMethod(lerpColorScale, NodePath)
del lerpColorScale

def lerpColorScaleRGBA(self, r, g, b, a, time, blendType='noBlend', auto=None, task=None):

    def functorFunc(self=self, r=r, g=g, b=b, a=a):
        from pandac.PandaModules import ColorScaleLerpFunctor
        startColor = self.getColor()
        functor = ColorScaleLerpFunctor.ColorScaleLerpFunctor(self, startColor[0], startColor[1], startColor[2], startColor[3], r, g, b, a)
        return functor

    if auto != None:
        return self.__autoLerp(functorFunc, time, blendType, auto)
    elif task != None:
        return self.__lerp(functorFunc, time, blendType, task)
    else:
        return self.__lerp(functorFunc, time, blendType)
    return


Dtool_funcToMethod(lerpColorScaleRGBA, NodePath)
del lerpColorScaleRGBA

def lerpColorScaleRGBARGBA(self, sr, sg, sb, sa, er, eg, eb, ea, time, blendType='noBlend', auto=None, task=None):

    def functorFunc(self=self, sr=sr, sg=sg, sb=sb, sa=sa, er=er, eg=eg, eb=eb, ea=ea):
        from pandac.PandaModules import ColorScaleLerpFunctor
        functor = ColorScaleLerpFunctor.ColorScaleLerpFunctor(self, sr, sg, sb, sa, er, eg, eb, ea)
        return functor

    if auto != None:
        return self.__autoLerp(functorFunc, time, blendType, auto)
    elif task != None:
        return self.__lerp(functorFunc, time, blendType, task)
    else:
        return self.__lerp(functorFunc, time, blendType)
    return


Dtool_funcToMethod(lerpColorScaleRGBARGBA, NodePath)
del lerpColorScaleRGBARGBA

def lerpColorScaleVBase4(self, endColor, time, blendType='noBlend', auto=None, task=None):

    def functorFunc(self=self, endColor=endColor):
        from pandac.PandaModules import ColorScaleLerpFunctor
        startColor = self.getColor()
        functor = ColorScaleLerpFunctor.ColorScaleLerpFunctor(self, startColor, endColor)
        return functor

    if auto != None:
        return self.__autoLerp(functorFunc, time, blendType, auto)
    elif task != None:
        return self.__lerp(functorFunc, time, blendType, task)
    else:
        return self.__lerp(functorFunc, time, blendType)
    return


Dtool_funcToMethod(lerpColorScaleVBase4, NodePath)
del lerpColorScaleVBase4

def lerpColorScaleVBase4VBase4(self, startColor, endColor, time, blendType='noBlend', auto=None, task=None):

    def functorFunc(self=self, startColor=startColor, endColor=endColor):
        from pandac.PandaModules import ColorScaleLerpFunctor
        functor = ColorScaleLerpFunctor.ColorScaleLerpFunctor(self, startColor, endColor)
        return functor

    if auto != None:
        return self.__autoLerp(functorFunc, time, blendType, auto)
    elif task != None:
        return self.__lerp(functorFunc, time, blendType, task)
    else:
        return self.__lerp(functorFunc, time, blendType)
    return


Dtool_funcToMethod(lerpColorScaleVBase4VBase4, NodePath)
del lerpColorScaleVBase4VBase4

def lerpHpr(self, *posArgs, **keyArgs):
    if len(posArgs) == 4:
        return apply(self.lerpHprHPR, posArgs, keyArgs)
    elif len(posArgs) == 2:
        return apply(self.lerpHprVBase3, posArgs, keyArgs)
    else:
        raise Exception('Error: NodePath.lerpHpr: bad number of args')


Dtool_funcToMethod(lerpHpr, NodePath)
del lerpHpr

def lerpHprHPR(self, h, p, r, time, other=None, blendType='noBlend', auto=None, task=None, shortest=1):

    def functorFunc(self=self, h=h, p=p, r=r, other=other, shortest=shortest):
        from pandac.PandaModules import HprLerpFunctor
        if other != None:
            startHpr = self.getHpr(other)
            functor = HprLerpFunctor.HprLerpFunctor(self, startHpr[0], startHpr[1], startHpr[2], h, p, r, other)
            if shortest:
                functor.takeShortest()
        else:
            startHpr = self.getHpr()
            functor = HprLerpFunctor.HprLerpFunctor(self, startHpr[0], startHpr[1], startHpr[2], h, p, r)
            if shortest:
                functor.takeShortest()
        return functor

    if auto != None:
        return self.__autoLerp(functorFunc, time, blendType, auto)
    elif task != None:
        return self.__lerp(functorFunc, time, blendType, task)
    else:
        return self.__lerp(functorFunc, time, blendType)
    return


Dtool_funcToMethod(lerpHprHPR, NodePath)
del lerpHprHPR

def lerpHprVBase3(self, hpr, time, other=None, blendType='noBlend', auto=None, task=None, shortest=1):

    def functorFunc(self=self, hpr=hpr, other=other, shortest=shortest):
        from pandac.PandaModules import HprLerpFunctor
        if other != None:
            functor = HprLerpFunctor.HprLerpFunctor(self, self.getHpr(other), hpr, other)
            if shortest:
                functor.takeShortest()
        else:
            functor = HprLerpFunctor.HprLerpFunctor(self, self.getHpr(), hpr)
            if shortest:
                functor.takeShortest()
        return functor

    if auto != None:
        return self.__autoLerp(functorFunc, time, blendType, auto)
    elif task != None:
        return self.__lerp(functorFunc, time, blendType, task)
    else:
        return self.__lerp(functorFunc, time, blendType)
    return


Dtool_funcToMethod(lerpHprVBase3, NodePath)
del lerpHprVBase3

def lerpPos(self, *posArgs, **keyArgs):
    if len(posArgs) == 4:
        return apply(self.lerpPosXYZ, posArgs, keyArgs)
    elif len(posArgs) == 2:
        return apply(self.lerpPosPoint3, posArgs, keyArgs)
    else:
        raise Exception('Error: NodePath.lerpPos: bad number of args')


Dtool_funcToMethod(lerpPos, NodePath)
del lerpPos

def lerpPosXYZ(self, x, y, z, time, other=None, blendType='noBlend', auto=None, task=None):

    def functorFunc(self=self, x=x, y=y, z=z, other=other):
        from pandac.PandaModules import PosLerpFunctor
        if other != None:
            startPos = self.getPos(other)
            functor = PosLerpFunctor.PosLerpFunctor(self, startPos[0], startPos[1], startPos[2], x, y, z, other)
        else:
            startPos = self.getPos()
            functor = PosLerpFunctor.PosLerpFunctor(self, startPos[0], startPos[1], startPos[2], x, y, z)
        return functor

    if auto != None:
        return self.__autoLerp(functorFunc, time, blendType, auto)
    elif task != None:
        return self.__lerp(functorFunc, time, blendType, task)
    else:
        return self.__lerp(functorFunc, time, blendType)
    return


Dtool_funcToMethod(lerpPosXYZ, NodePath)
del lerpPosXYZ

def lerpPosPoint3(self, pos, time, other=None, blendType='noBlend', auto=None, task=None):

    def functorFunc(self=self, pos=pos, other=other):
        from pandac.PandaModules import PosLerpFunctor
        if other != None:
            functor = PosLerpFunctor.PosLerpFunctor(self, self.getPos(other), pos, other)
        else:
            functor = PosLerpFunctor.PosLerpFunctor(self, self.getPos(), pos)
        return functor

    if auto != None:
        return self.__autoLerp(functorFunc, time, blendType, auto)
    elif task != None:
        return self.__lerp(functorFunc, time, blendType, task)
    else:
        return self.__lerp(functorFunc, time, blendType)
    return


Dtool_funcToMethod(lerpPosPoint3, NodePath)
del lerpPosPoint3

def lerpPosHpr(self, *posArgs, **keyArgs):
    if len(posArgs) == 7:
        return apply(self.lerpPosHprXYZHPR, posArgs, keyArgs)
    elif len(posArgs) == 3:
        return apply(self.lerpPosHprPoint3VBase3, posArgs, keyArgs)
    else:
        raise Exception('Error: NodePath.lerpPosHpr: bad number of args')


Dtool_funcToMethod(lerpPosHpr, NodePath)
del lerpPosHpr

def lerpPosHprPoint3VBase3(self, pos, hpr, time, other=None, blendType='noBlend', auto=None, task=None, shortest=1):

    def functorFunc(self=self, pos=pos, hpr=hpr, other=other, shortest=shortest):
        from pandac.PandaModules import PosHprLerpFunctor
        if other != None:
            startPos = self.getPos(other)
            startHpr = self.getHpr(other)
            functor = PosHprLerpFunctor.PosHprLerpFunctor(self, startPos, pos, startHpr, hpr, other)
            if shortest:
                functor.takeShortest()
        else:
            startPos = self.getPos()
            startHpr = self.getHpr()
            functor = PosHprLerpFunctor.PosHprLerpFunctor(self, startPos, pos, startHpr, hpr)
            if shortest:
                functor.takeShortest()
        return functor

    if auto != None:
        return self.__autoLerp(functorFunc, time, blendType, auto)
    elif task != None:
        return self.__lerp(functorFunc, time, blendType, task)
    else:
        return self.__lerp(functorFunc, time, blendType)
    return


Dtool_funcToMethod(lerpPosHprPoint3VBase3, NodePath)
del lerpPosHprPoint3VBase3

def lerpPosHprXYZHPR(self, x, y, z, h, p, r, time, other=None, blendType='noBlend', auto=None, task=None, shortest=1):

    def functorFunc(self=self, x=x, y=y, z=z, h=h, p=p, r=r, other=other, shortest=shortest):
        from pandac.PandaModules import PosHprLerpFunctor
        if other != None:
            startPos = self.getPos(other)
            startHpr = self.getHpr(other)
            functor = PosHprLerpFunctor.PosHprLerpFunctor(self, startPos[0], startPos[1], startPos[2], x, y, z, startHpr[0], startHpr[1], startHpr[2], h, p, r, other)
            if shortest:
                functor.takeShortest()
        else:
            startPos = self.getPos()
            startHpr = self.getHpr()
            functor = PosHprLerpFunctor.PosHprLerpFunctor(self, startPos[0], startPos[1], startPos[2], x, y, z, startHpr[0], startHpr[1], startHpr[2], h, p, r)
            if shortest:
                functor.takeShortest()
        return functor

    if auto != None:
        return self.__autoLerp(functorFunc, time, blendType, auto)
    elif task != None:
        return self.__lerp(functorFunc, time, blendType, task)
    else:
        return self.__lerp(functorFunc, time, blendType)
    return


Dtool_funcToMethod(lerpPosHprXYZHPR, NodePath)
del lerpPosHprXYZHPR

def lerpPosHprScale(self, pos, hpr, scale, time, other=None, blendType='noBlend', auto=None, task=None, shortest=1):

    def functorFunc(self=self, pos=pos, hpr=hpr, scale=scale, other=other, shortest=shortest):
        from pandac.PandaModules import PosHprScaleLerpFunctor
        if other != None:
            startPos = self.getPos(other)
            startHpr = self.getHpr(other)
            startScale = self.getScale(other)
            functor = PosHprScaleLerpFunctor.PosHprScaleLerpFunctor(self, startPos, pos, startHpr, hpr, startScale, scale, other)
            if shortest:
                functor.takeShortest()
        else:
            startPos = self.getPos()
            startHpr = self.getHpr()
            startScale = self.getScale()
            functor = PosHprScaleLerpFunctor.PosHprScaleLerpFunctor(self, startPos, pos, startHpr, hpr, startScale, scale)
            if shortest:
                functor.takeShortest()
        return functor

    if auto != None:
        return self.__autoLerp(functorFunc, time, blendType, auto)
    elif task != None:
        return self.__lerp(functorFunc, time, blendType, task)
    else:
        return self.__lerp(functorFunc, time, blendType)
    return


Dtool_funcToMethod(lerpPosHprScale, NodePath)
del lerpPosHprScale

def lerpScale(self, *posArgs, **keyArgs):
    if len(posArgs) == 4:
        return apply(self.lerpScaleXYZ, posArgs, keyArgs)
    elif len(posArgs) == 2:
        return apply(self.lerpScaleVBase3, posArgs, keyArgs)
    else:
        raise Exception('Error: NodePath.lerpScale: bad number of args')


Dtool_funcToMethod(lerpScale, NodePath)
del lerpScale

def lerpScaleVBase3(self, scale, time, other=None, blendType='noBlend', auto=None, task=None):

    def functorFunc(self=self, scale=scale, other=other):
        from pandac.PandaModules import ScaleLerpFunctor
        if other != None:
            functor = ScaleLerpFunctor.ScaleLerpFunctor(self, self.getScale(other), scale, other)
        else:
            functor = ScaleLerpFunctor.ScaleLerpFunctor(self, self.getScale(), scale)
        return functor

    if auto != None:
        return self.__autoLerp(functorFunc, time, blendType, auto)
    elif task != None:
        return self.__lerp(functorFunc, time, blendType, task)
    else:
        return self.__lerp(functorFunc, time, blendType)
    return


Dtool_funcToMethod(lerpScaleVBase3, NodePath)
del lerpScaleVBase3

def lerpScaleXYZ(self, sx, sy, sz, time, other=None, blendType='noBlend', auto=None, task=None):

    def functorFunc(self=self, sx=sx, sy=sy, sz=sz, other=other):
        from pandac.PandaModules import ScaleLerpFunctor
        if other != None:
            startScale = self.getScale(other)
            functor = ScaleLerpFunctor.ScaleLerpFunctor(self, startScale[0], startScale[1], startScale[2], sx, sy, sz, other)
        else:
            startScale = self.getScale()
            functor = ScaleLerpFunctor.ScaleLerpFunctor(self, startScale[0], startScale[1], startScale[2], sx, sy, sz)
        return functor

    if auto != None:
        return self.__autoLerp(functorFunc, time, blendType, auto)
    elif task != None:
        return self.__lerp(functorFunc, time, blendType, task)
    else:
        return self.__lerp(functorFunc, time, blendType)
    return


Dtool_funcToMethod(lerpScaleXYZ, NodePath)
del lerpScaleXYZ

def place(self):
    base.startDirect(fWantTk=1)
    from direct.tkpanels import Placer
    return Placer.place(self)


Dtool_funcToMethod(place, NodePath)
del place

def explore(self):
    base.startDirect(fWantTk=1)
    from direct.tkwidgets import SceneGraphExplorer
    return SceneGraphExplorer.explore(self)


Dtool_funcToMethod(explore, NodePath)
del explore

def rgbPanel(self, cb=None):
    base.startTk()
    from direct.tkwidgets import Slider
    return Slider.rgbPanel(self, cb)


Dtool_funcToMethod(rgbPanel, NodePath)
del rgbPanel

def select(self):
    base.startDirect(fWantTk=0)
    base.direct.select(self)


Dtool_funcToMethod(select, NodePath)
del select

def deselect(self):
    base.startDirect(fWantTk=0)
    base.direct.deselect(self)


Dtool_funcToMethod(deselect, NodePath)
del deselect

def showCS(self, mask=None):
    npc = self.findAllMatches('**/+CollisionNode')
    for p in range(0, npc.getNumPaths()):
        np = npc[p]
        if mask == None or (np.node().getIntoCollideMask() & mask).getWord():
            np.show()

    return


Dtool_funcToMethod(showCS, NodePath)
del showCS

def hideCS(self, mask=None):
    npc = self.findAllMatches('**/+CollisionNode')
    for p in range(0, npc.getNumPaths()):
        np = npc[p]
        if mask == None or (np.node().getIntoCollideMask() & mask).getWord():
            np.hide()

    return


Dtool_funcToMethod(hideCS, NodePath)
del hideCS

def posInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpPosInterval(self, *args, **kw)


Dtool_funcToMethod(posInterval, NodePath)
del posInterval

def hprInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpHprInterval(self, *args, **kw)


Dtool_funcToMethod(hprInterval, NodePath)
del hprInterval

def quatInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpQuatInterval(self, *args, **kw)


Dtool_funcToMethod(quatInterval, NodePath)
del quatInterval

def scaleInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpScaleInterval(self, *args, **kw)


Dtool_funcToMethod(scaleInterval, NodePath)
del scaleInterval

def shearInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpShearInterval(self, *args, **kw)


Dtool_funcToMethod(shearInterval, NodePath)
del shearInterval

def posHprInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpPosHprInterval(self, *args, **kw)


Dtool_funcToMethod(posHprInterval, NodePath)
del posHprInterval

def posQuatInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpPosQuatInterval(self, *args, **kw)


Dtool_funcToMethod(posQuatInterval, NodePath)
del posQuatInterval

def hprScaleInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpHprScaleInterval(self, *args, **kw)


Dtool_funcToMethod(hprScaleInterval, NodePath)
del hprScaleInterval

def quatScaleInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpQuatScaleInterval(self, *args, **kw)


Dtool_funcToMethod(quatScaleInterval, NodePath)
del quatScaleInterval

def posHprScaleInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpPosHprScaleInterval(self, *args, **kw)


Dtool_funcToMethod(posHprScaleInterval, NodePath)
del posHprScaleInterval

def posQuatScaleInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpPosQuatScaleInterval(self, *args, **kw)


Dtool_funcToMethod(posQuatScaleInterval, NodePath)
del posQuatScaleInterval

def posHprScaleShearInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpPosHprScaleShearInterval(self, *args, **kw)


Dtool_funcToMethod(posHprScaleShearInterval, NodePath)
del posHprScaleShearInterval

def posQuatScaleShearInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpPosQuatScaleShearInterval(self, *args, **kw)


Dtool_funcToMethod(posQuatScaleShearInterval, NodePath)
del posQuatScaleShearInterval

def colorInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpColorInterval(self, *args, **kw)


Dtool_funcToMethod(colorInterval, NodePath)
del colorInterval

def colorScaleInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpColorScaleInterval(self, *args, **kw)


Dtool_funcToMethod(colorScaleInterval, NodePath)
del colorScaleInterval

def attachCollisionSphere(self, name, cx, cy, cz, r, fromCollide, intoCollide):
    from pandac.PandaModules import CollisionSphere
    from pandac.PandaModules import CollisionNode
    coll = CollisionSphere.CollisionSphere(cx, cy, cz, r)
    collNode = CollisionNode.CollisionNode(name)
    collNode.addSolid(coll)
    collNode.setFromCollideMask(fromCollide)
    collNode.setIntoCollideMask(intoCollide)
    collNodePath = self.attachNewNode(collNode)
    return collNodePath


Dtool_funcToMethod(attachCollisionSphere, NodePath)
del attachCollisionSphere

def attachCollisionSegment(self, name, ax, ay, az, bx, by, bz, fromCollide, intoCollide):
    from pandac.PandaModules import CollisionSegment
    from pandac.PandaModules import CollisionNode
    coll = CollisionSegment.CollisionSegment(ax, ay, az, bx, by, bz)
    collNode = CollisionNode.CollisionNode(name)
    collNode.addSolid(coll)
    collNode.setFromCollideMask(fromCollide)
    collNode.setIntoCollideMask(intoCollide)
    collNodePath = self.attachNewNode(collNode)
    return collNodePath


Dtool_funcToMethod(attachCollisionSegment, NodePath)
del attachCollisionSegment

def attachCollisionRay(self, name, ox, oy, oz, dx, dy, dz, fromCollide, intoCollide):
    from pandac.PandaModules import CollisionRay
    from pandac.PandaModules import CollisionNode
    coll = CollisionRay.CollisionRay(ox, oy, oz, dx, dy, dz)
    collNode = CollisionNode.CollisionNode(name)
    collNode.addSolid(coll)
    collNode.setFromCollideMask(fromCollide)
    collNode.setIntoCollideMask(intoCollide)
    collNodePath = self.attachNewNode(collNode)
    return collNodePath


Dtool_funcToMethod(attachCollisionRay, NodePath)
del attachCollisionRay

def flattenMultitex(self, stateFrom=None, target=None, useGeom=0, allowTexMat=0, win=None):
    from pandac.PandaModules import MultitexReducer
    mr = MultitexReducer.MultitexReducer()
    if target != None:
        mr.setTarget(target)
    mr.setUseGeom(useGeom)
    mr.setAllowTexMat(allowTexMat)
    if win == None:
        win = base.win
    if stateFrom == None:
        mr.scan(self)
    else:
        mr.scan(self, stateFrom)
    mr.flatten(win)
    return


Dtool_funcToMethod(flattenMultitex, NodePath)
del flattenMultitex

def getNumDescendants(self):
    return len(self.findAllMatches('**')) - 1


Dtool_funcToMethod(getNumDescendants, NodePath)
del getNumDescendants

def removeNonCollisions(self):
    stack = [
     self]
    while len(stack):
        np = stack.pop()
        if np.find('**/+CollisionNode').isEmpty():
            np.detachNode()
        else:
            stack.extend(np.getChildren())


Dtool_funcToMethod(removeNonCollisions, NodePath)
del removeNonCollisions

def subdivideCollisions(self, numSolidsInLeaves):
    colNps = self.findAllMatches('**/+CollisionNode')
    for colNp in colNps:
        node = colNp.node()
        numSolids = node.getNumSolids()
        if numSolids <= numSolidsInLeaves:
            continue
        solids = []
        for i in xrange(numSolids):
            solids.append(node.getSolid(i))

        solidTree = self.r_subdivideCollisions(solids, numSolidsInLeaves)
        root = colNp.getParent().attachNewNode('%s-subDivRoot' % colNp.getName())
        self.r_constructCollisionTree(solidTree, root, colNp.getName())
        colNp.stash()


def r_subdivideCollisions(self, solids, numSolidsInLeaves):
    if len(solids) <= numSolidsInLeaves:
        return solids
    origins = []
    avgX = 0
    avgY = 0
    avgZ = 0
    minX = None
    minY = None
    minZ = None
    maxX = None
    maxY = None
    maxZ = None
    for solid in solids:
        origin = solid.getCollisionOrigin()
        origins.append(origin)
        x = origin.getX()
        y = origin.getY()
        z = origin.getZ()
        avgX += x
        avgY += y
        avgZ += z
        if minX is None:
            minX = x
            minY = y
            minZ = z
            maxX = x
            maxY = y
            maxZ = z
        else:
            minX = min(x, minX)
            minY = min(y, minY)
            minZ = min(z, minZ)
            maxX = max(x, maxX)
            maxY = max(y, maxY)
            maxZ = max(z, maxZ)

    avgX /= len(solids)
    avgY /= len(solids)
    avgZ /= len(solids)
    extentX = maxX - minX
    extentY = maxY - minY
    extentZ = maxZ - minZ
    maxExtent = max(max(extentX, extentY), extentZ)
    xyzSolids = []
    XyzSolids = []
    xYzSolids = []
    XYzSolids = []
    xyZSolids = []
    XyZSolids = []
    xYZSolids = []
    XYZSolids = []
    midX = avgX
    midY = avgY
    midZ = avgZ
    if extentX < maxExtent * 0.75 or extentX > maxExtent * 1.25:
        midX += maxExtent
    if extentY < maxExtent * 0.75 or extentY > maxExtent * 1.25:
        midY += maxExtent
    if extentZ < maxExtent * 0.75 or extentZ > maxExtent * 1.25:
        midZ += maxExtent
    for i in xrange(len(solids)):
        origin = origins[i]
        x = origin.getX()
        y = origin.getY()
        z = origin.getZ()
        if x < midX:
            if y < midY:
                if z < midZ:
                    xyzSolids.append(solids[i])
                else:
                    xyZSolids.append(solids[i])
            elif z < midZ:
                xYzSolids.append(solids[i])
            else:
                xYZSolids.append(solids[i])
        elif y < midY:
            if z < midZ:
                XyzSolids.append(solids[i])
            else:
                XyZSolids.append(solids[i])
        elif z < midZ:
            XYzSolids.append(solids[i])
        else:
            XYZSolids.append(solids[i])

    newSolids = []
    if len(xyzSolids):
        newSolids.append(self.r_subdivideCollisions(xyzSolids, numSolidsInLeaves))
    if len(XyzSolids):
        newSolids.append(self.r_subdivideCollisions(XyzSolids, numSolidsInLeaves))
    if len(xYzSolids):
        newSolids.append(self.r_subdivideCollisions(xYzSolids, numSolidsInLeaves))
    if len(XYzSolids):
        newSolids.append(self.r_subdivideCollisions(XYzSolids, numSolidsInLeaves))
    if len(xyZSolids):
        newSolids.append(self.r_subdivideCollisions(xyZSolids, numSolidsInLeaves))
    if len(XyZSolids):
        newSolids.append(self.r_subdivideCollisions(XyZSolids, numSolidsInLeaves))
    if len(xYZSolids):
        newSolids.append(self.r_subdivideCollisions(xYZSolids, numSolidsInLeaves))
    if len(XYZSolids):
        newSolids.append(self.r_subdivideCollisions(XYZSolids, numSolidsInLeaves))
    return newSolids


def r_constructCollisionTree(self, solidTree, parentNode, colName):
    for item in solidTree:
        if type(item[0]) == type([]):
            newNode = parentNode.attachNewNode('%s-branch' % colName)
            self.r_constructCollisionTree(item, newNode, colName)
        else:
            cn = CollisionNode('%s-leaf' % colName)
            for solid in item:
                cn.addSolid(solid)

            parentNode.attachNewNode(cn)


Dtool_funcToMethod(subdivideCollisions, NodePath)
Dtool_funcToMethod(r_subdivideCollisions, NodePath)
Dtool_funcToMethod(r_constructCollisionTree, NodePath)
del subdivideCollisions
del r_subdivideCollisions
del r_constructCollisionTree

def analyze(self):
    from pandac.PandaModules import SceneGraphAnalyzer
    sga = SceneGraphAnalyzer()
    sga.addNode(self.node())
    if sga.getNumLodNodes() == 0:
        print sga
    else:
        print 'At highest LOD:'
        sga2 = SceneGraphAnalyzer()
        sga2.setLodMode(sga2.LMHighest)
        sga2.addNode(self.node())
        print sga2
        print '\nAt lowest LOD:'
        sga2.clear()
        sga2.setLodMode(sga2.LMLowest)
        sga2.addNode(self.node())
        print sga2
        print '\nAll nodes:'
        print sga


Dtool_funcToMethod(analyze, NodePath)
del analyze