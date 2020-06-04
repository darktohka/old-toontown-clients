# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\DistributedCrushableEntity.py
from otp.level import DistributedEntity
from direct.directnotify import DirectNotifyGlobal
from pandac.PandaModules import NodePath
from otp.level import BasicEntities

class DistributedCrushableEntity(DistributedEntity.DistributedEntity, NodePath, BasicEntities.NodePathAttribs):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCrushableEntity')

    def __init__(self, cr):
        DistributedEntity.DistributedEntity.__init__(self, cr)
        node = hidden.attachNewNode('DistributedNodePathEntity')

    def initNodePath(self):
        node = hidden.attachNewNode('DistributedNodePathEntity')
        NodePath.__init__(self, node)

    def announceGenerate(self):
        DistributedEntity.DistributedEntity.announceGenerate(self)
        BasicEntities.NodePathAttribs.initNodePathAttribs(self)

    def disable(self):
        self.reparentTo(hidden)
        BasicEntities.NodePathAttribs.destroy(self)
        DistributedEntity.DistributedEntity.disable(self)

    def delete(self):
        self.removeNode()
        DistributedEntity.DistributedEntity.delete(self)

    def setPosition(self, x, y, z):
        self.setPos(x, y, z)

    def setCrushed(self, crusherId, axis):
        self.playCrushMovie(crusherId, axis)

    def playCrushMovie(self, crusherId, axis):
        pass