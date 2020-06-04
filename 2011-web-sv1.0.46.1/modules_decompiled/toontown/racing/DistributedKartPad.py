# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\racing\DistributedKartPad.py
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObject import DistributedObject
if __debug__:
    import pdb

class DistributedKartPad(DistributedObject):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedKartPad')

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        self.startingBlocks = []

    def delete(self):
        del self.startingBlocks
        DistributedObject.delete(self)

    def setArea(self, area):
        self.area = area

    def getArea(self):
        return self.area

    def addStartingBlock(self, block):
        self.startingBlocks.append(block)
        self.notify.debug('KartPad %s has added starting block %s' % (self.doId, block.doId))