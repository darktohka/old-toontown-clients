# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\MintManagerAI.py
from direct.directnotify import DirectNotifyGlobal
import DistributedMintAI
from toontown.toonbase import ToontownGlobals
from toontown.coghq import MintLayout
from direct.showbase import DirectObject
import random

class MintManagerAI(DirectObject.DirectObject):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('MintManagerAI')
    mintId = None

    def __init__(self, air):
        DirectObject.DirectObject.__init__(self)
        self.air = air

    def getDoId(self):
        return 0

    def createMint(self, mintId, players):
        for avId in players:
            if bboard.has('mintId-%s' % avId):
                mintId = bboard.get('mintId-%s' % avId)
                break

        numFloors = ToontownGlobals.MintNumFloors[mintId]
        floor = random.randrange(numFloors)
        for avId in players:
            if bboard.has('mintFloor-%s' % avId):
                floor = bboard.get('mintFloor-%s' % avId)
                floor = max(0, floor)
                floor = min(floor, numFloors - 1)
                break

        for avId in players:
            if bboard.has('mintRoom-%s' % avId):
                roomId = bboard.get('mintRoom-%s' % avId)
                for i in xrange(numFloors):
                    layout = MintLayout.MintLayout(mintId, i)
                    if roomId in layout.getRoomIds():
                        floor = i
                else:
                    from toontown.coghq import MintRoomSpecs
                    roomName = MintRoomSpecs.CashbotMintRoomId2RoomName[roomId]
                    MintManagerAI.notify.warning('room %s (%s) not found in any floor of mint %s' % (roomId, roomName, mintId))

        mintZone = self.air.allocateZone()
        mint = DistributedMintAI.DistributedMintAI(self.air, mintId, mintZone, floor, players)
        mint.generateWithRequired(mintZone)
        return mintZone