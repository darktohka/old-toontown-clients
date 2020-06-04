# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\racing\FlyingGag.py
from pandac.PandaModules import *
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from otp.avatar.ShadowCaster import ShadowCaster

class FlyingGag(NodePath, ShadowCaster):
    __module__ = __name__

    def __init__(self, name, geom=None):
        an = ActorNode('flyingGagAN')
        NodePath.__init__(self, an)
        self.actorNode = an
        self.gag = None
        self.gagNode = None
        ShadowCaster.__init__(self, False)
        if geom:
            self.gagNode = self.attachNewNode('PieNode')
            self.gag = geom.copyTo(self.gagNode)
            self.gag.setScale(3)
            self.gagNode.setHpr(0, -45, 0)
            self.gagNode.setPos(0, 0, 2)
            self.initializeDropShadow()
            self.setActiveShadow()
            self.dropShadow.setPos(0, 0, 2)
            self.dropShadow.setScale(3)
        return

    def delete(self):
        ShadowCaster.delete(self)
        NodePath.remove(self)
        self.gag = None
        return

    def getGeomNode(self):
        return self.gag