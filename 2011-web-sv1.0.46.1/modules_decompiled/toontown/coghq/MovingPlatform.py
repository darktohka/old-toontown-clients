# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\MovingPlatform.py
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.showbase import DirectObject
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
import types

class MovingPlatform(DirectObject.DirectObject, NodePath):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('MovingPlatform')

    def __init__(self):
        self.hasLt = 0
        DirectObject.DirectObject.__init__(self)
        NodePath.__init__(self)

    def setupCopyModel(self, parentToken, model, floorNodeName=None, parentingNode=None):
        if floorNodeName is None:
            floorNodeName = 'floor'
        if type(parentToken) == types.IntType:
            parentToken = ToontownGlobals.SPDynamic + parentToken
        self.parentToken = parentToken
        self.name = 'MovingPlatform-%s' % parentToken
        self.assign(hidden.attachNewNode(self.name))
        self.model = model.copyTo(self)
        self.ownsModel = 1
        floorList = self.model.findAllMatches('**/%s' % floorNodeName)
        if len(floorList) == 0:
            MovingPlatform.notify.warning('no floors in model')
            return
        for floor in floorList:
            floor.setName(self.name)

        if parentingNode == None:
            parentingNode = self
        base.cr.parentMgr.registerParent(self.parentToken, parentingNode)
        self.parentingNode = parentingNode
        self.accept('enter%s' % self.name, self.__handleEnter)
        self.accept('exit%s' % self.name, self.__handleExit)
        return

    def destroy(self):
        base.cr.parentMgr.unregisterParent(self.parentToken)
        self.ignoreAll()
        if self.hasLt:
            self.__releaseLt()
        if self.ownsModel:
            self.model.removeNode()
            del self.model
        if hasattr(self, 'parentingNode') and self.parentingNode is self:
            del self.parentingNode

    def getEnterEvent(self):
        return '%s-enter' % self.name

    def getExitEvent(self):
        return '%s-exit' % self.name

    def releaseLocalToon(self):
        if self.hasLt:
            self.__releaseLt()

    def __handleEnter(self, collEntry):
        self.notify.debug('on movingPlatform %s' % self.name)
        self.__grabLt()
        messenger.send(self.getEnterEvent())

    def __handleExit(self, collEntry):
        self.notify.debug('off movingPlatform %s' % self.name)
        self.__releaseLt()
        messenger.send(self.getExitEvent())

    def __handleOnFloor(self, collEntry):
        if collEntry.getIntoNode().getName() == self.name:
            self.__handleEnter(collEntry)

    def __handleOffFloor(self, collEntry):
        if collEntry.getIntoNode().getName() == self.name:
            self.__handleExit(collEntry)

    def __grabLt(self):
        base.localAvatar.b_setParent(self.parentToken)
        self.hasLt = 1

    def __releaseLt(self):
        if base.localAvatar.getParent().compareTo(self.parentingNode) == 0:
            base.localAvatar.b_setParent(ToontownGlobals.SPRender)
            base.localAvatar.controlManager.currentControls.doDeltaPos()
        self.hasLt = 0