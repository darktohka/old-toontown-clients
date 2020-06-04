# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\level\CollisionSolidEntity.py
from pandac.PandaModules import *
from otp.otpbase import OTPGlobals
from direct.directnotify import DirectNotifyGlobal
import BasicEntities

class CollisionSolidEntity(BasicEntities.NodePathEntity):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('CollisionSolidEntity')

    def __init__(self, level, entId):
        self.collNodePath = None
        BasicEntities.NodePathEntity.__init__(self, level, entId)
        self.initSolid()
        return

    def destroy(self):
        self.destroySolid()
        BasicEntities.NodePathEntity.destroy(self)

    def initSolid(self):
        self.destroySolid()
        if self.solidType == 'sphere':
            solid = CollisionSphere(0, 0, 0, self.radius)
        else:
            solid = CollisionTube(0, 0, 0, 0, 0, self.length, self.radius)
        node = CollisionNode(self.getUniqueName(self.__class__.__name__))
        node.addSolid(solid)
        node.setCollideMask(OTPGlobals.WallBitmask)
        self.collNodePath = self.attachNewNode(node)
        if __dev__:
            if self.showSolid:
                self.showCS()
            else:
                self.hideCS()

    def destroySolid(self):
        if self.collNodePath is not None:
            self.collNodePath.removeNode()
            self.collNodePath = None
        return

    if __dev__:

        def attribChanged(self, attrib, value):
            print 'attribChanged'
            self.initSolid()