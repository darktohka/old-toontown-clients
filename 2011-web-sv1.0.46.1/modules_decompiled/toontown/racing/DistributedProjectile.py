# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\racing\DistributedProjectile.py
from pandac.PandaModules import *
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.fsm import FSM
from direct.distributed.DistributedSmoothNode import DistributedSmoothNode
from otp.avatar.ShadowCaster import ShadowCaster

class DistributedProjectile(DistributedSmoothNode, ShadowCaster, NodePath):
    __module__ = __name__

    def __init__(self, cr):
        ShadowCaster.__init__(self)
        DistributedSmoothNode.__init__(self, cr)
        NodePath.__init__(self, 'Projectile')

    def announceGenerate(self):
        DistributedSmoothNode.announceGenerate(self)
        self.name = self.uniqueName('projectile')
        self.posHprBroadcastName = self.uniqueName('projectileBroadcast')
        geom = loader.loadModel('models/smiley')
        self.geom = geom
        self.geom.reparentTo(self)
        self.startSmooth()
        self.reparentTo(render)

    def generate(self):
        DistributedSmoothNode.generate(self)
        self.name = self.uniqueName('projectile')
        self.posHprBroadcastName = self.uniqueName('projectileBroadcast')
        geom = loader.loadModel('models/smiley')
        self.geom = geom
        self.geom.reparentTo(self)
        self.startSmooth()
        self.reparentTo(render)

    def setAvId(self, avId):
        self.avId = avId

    def delete(self):
        DistributedSmoothNode.delete(self)