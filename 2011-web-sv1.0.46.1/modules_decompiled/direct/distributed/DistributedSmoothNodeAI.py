# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\distributed\DistributedSmoothNodeAI.py
import DistributedNodeAI, DistributedSmoothNodeBase

class DistributedSmoothNodeAI(DistributedNodeAI.DistributedNodeAI, DistributedSmoothNodeBase.DistributedSmoothNodeBase):
    __module__ = __name__

    def __init__(self, air, name=None):
        DistributedNodeAI.DistributedNodeAI.__init__(self, air, name)
        DistributedSmoothNodeBase.DistributedSmoothNodeBase.__init__(self)

    def generate(self):
        DistributedNodeAI.DistributedNodeAI.generate(self)
        DistributedSmoothNodeBase.DistributedSmoothNodeBase.generate(self)
        self.cnode.setRepository(self.air, 1, self.air.ourChannel)

    def disable(self):
        DistributedSmoothNodeBase.DistributedSmoothNodeBase.disable(self)
        DistributedNodeAI.DistributedNodeAI.disable(self)

    def delete(self):
        DistributedSmoothNodeBase.DistributedSmoothNodeBase.delete(self)
        DistributedNodeAI.DistributedNodeAI.delete(self)

    def setSmStop(self, t=None):
        pass

    def setSmH(self, h, t=None):
        self.setH(h)

    def setSmZ(self, z, t=None):
        self.setZ(z)

    def setSmXY(self, x, y, t=None):
        self.setX(x)
        self.setY(y)

    def setSmXZ(self, x, z, t=None):
        self.setX(x)
        self.setZ(z)

    def setSmPos(self, x, y, z, t=None):
        self.setPos(x, y, z)

    def setSmHpr(self, h, p, r, t=None):
        self.setHpr(h, p, r)

    def setSmXYH(self, x, y, h, t=None):
        self.setX(x)
        self.setY(y)
        self.setH(h)

    def setSmXYZH(self, x, y, z, h, t=None):
        self.setPos(x, y, z)
        self.setH(h)

    def setSmPosHpr(self, x, y, z, h, p, r, t=None):
        self.setPosHpr(x, y, z, h, p, r)

    def setSmPosHprL(self, l, x, y, z, h, p, r, t=None):
        self.setPosHpr(x, y, z, h, p, r)

    def clearSmoothing(self, bogus=None):
        pass

    def setComponentX(self, x):
        self.setX(x)

    def setComponentY(self, y):
        self.setY(y)

    def setComponentZ(self, z):
        self.setZ(z)

    def setComponentH(self, h):
        self.setH(h)

    def setComponentP(self, p):
        self.setP(p)

    def setComponentR(self, r):
        self.setR(r)

    def setComponentL(self, l):
        pass

    def setComponentT(self, t):
        pass

    def getComponentX(self):
        return self.getX()

    def getComponentY(self):
        return self.getY()

    def getComponentZ(self):
        return self.getZ()

    def getComponentH(self):
        return self.getH()

    def getComponentP(self):
        return self.getP()

    def getComponentR(self):
        return self.getR()

    def getComponentL(self):
        if self.zoneId:
            return self.zoneId
        else:
            return 0

    def getComponentT(self):
        return 0