# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\GoonClipPlane.py
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from otp.level import BasicEntities

class GoonClipPlane(BasicEntities.NodePathEntity):
    __module__ = __name__

    def __init__(self, level, entId):
        BasicEntities.NodePathEntity.__init__(self, level, entId)
        self.zoneNum = self.getZoneEntity().getZoneNum()
        self.initPlane()
        self.registerWithFactory()

    def destroy(self):
        self.unregisterWithFactory()
        BasicEntities.NodePathEntity.destroy(self)
        self.removeNode()

    def registerWithFactory(self):
        clipList = self.level.goonClipPlanes.get(self.zoneNum)
        if clipList:
            if self.entId not in clipList:
                clipList.append(self.entId)
        else:
            self.level.goonClipPlanes[self.zoneNum] = [
             self.entId]

    def unregisterWithFactory(self):
        clipList = self.level.goonClipPlanes.get(self.zoneNum)
        if clipList:
            if self.entId in clipList:
                clipList.remove(self.entId)

    def initPlane(self):
        self.coneClip = PlaneNode('coneClip')
        self.coneClip.setPlane(Plane(Vec3(1, 0, 0), Point3(0, 0, 0)))
        self.coneClipPath = self.attachNewNode(self.coneClip)

    def getPlane(self):
        return self.coneClipPath