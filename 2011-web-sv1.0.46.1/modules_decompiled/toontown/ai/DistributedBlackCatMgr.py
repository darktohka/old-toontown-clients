# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\ai\DistributedBlackCatMgr.py
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from direct.interval.IntervalGlobal import *
from toontown.effects import DustCloud

def getDustCloudIval(toon):
    dustCloud = DustCloud.DustCloud(fBillboard=0)
    dustCloud.setBillboardAxis(2.0)
    dustCloud.setZ(3)
    dustCloud.setScale(0.4)
    dustCloud.createTrack()
    toon.laffMeter.color = toon.style.getBlackColor()
    return Sequence(Wait(0.5), Func(dustCloud.reparentTo, toon), dustCloud.track, Func(dustCloud.detachNode), Func(toon.laffMeter.adjustFace, toon.hp, toon.maxHp))


class DistributedBlackCatMgr(DistributedObject.DistributedObject):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBlackCatMgr')
    ActivateEvent = 'DistributedBlackCatMgr-activate'

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    def setAvId(self, avId):
        self.avId = avId

    def announceGenerate(self):
        DistributedBlackCatMgr.notify.debug('announceGenerate')
        DistributedObject.DistributedObject.announceGenerate(self)
        self.acceptOnce(DistributedBlackCatMgr.ActivateEvent, self.doBlackCatTransformation)
        self.dustCloudIval = None
        return

    def delete(self):
        if self.dustCloudIval:
            self.dustCloudIval.finish()
        del self.dustCloudIval
        self.ignore(DistributedBlackCatMgr.ActivateEvent)
        DistributedObject.DistributedObject.delete(self)

    def doBlackCatTransformation(self):
        DistributedBlackCatMgr.notify.debug('doBlackCatTransformation')
        toon = base.cr.doId2do[self.avId]
        if not toon:
            DistributedBlackCatMgr.notify.warning("couldn't find Toon %s" % self.avId)
            return
        if toon.style.getAnimal() != 'cat':
            DistributedBlackCatMgr.notify.warning('not a cat: %s' % self.avId)
            return
        self.sendUpdate('doBlackCatTransformation', [])
        self.dustCloudIval = getDustCloudIval(toon)
        self.dustCloudIval.start()