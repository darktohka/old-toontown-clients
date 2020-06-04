# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\racing\DroppedGag.py
from pandac.PandaModules import *
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from otp.avatar import ShadowCaster

class DroppedGag(NodePath, ShadowCaster.ShadowCaster):
    __module__ = __name__

    def __init__(self, name, geom):
        NodePath.__init__(self, name)
        ShadowCaster.ShadowCaster.__init__(self, False)
        self.gag = geom.copyTo(self)
        self.initializeDropShadow()
        self.setActiveShadow()
        self.dropShadow.setScale(1)

    def delete(self):
        ShadowCaster.ShadowCaster.delete(self)
        NodePath.removeNode(self)
        self.gag = None
        return

    def getGeomNode(self):
        return self.gag