# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\StageManagerAI.py
from direct.directnotify import DirectNotifyGlobal
import DistributedStageAI
from toontown.toonbase import ToontownGlobals
from toontown.coghq import StageLayout
from direct.showbase import DirectObject
import random

class StageManagerAI(DirectObject.DirectObject):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('StageManagerAI')
    stageId = None

    def __init__(self, air):
        DirectObject.DirectObject.__init__(self)
        self.air = air

    def getDoId(self):
        return 0

    def createStage(self, stageId, players):
        for avId in players:
            if bboard.has('stageId-%s' % avId):
                stageId = bboard.get('stageId-%s' % avId)
                break

        numFloors = StageLayout.getNumFloors(stageId)
        floor = random.randrange(numFloors)
        for avId in players:
            if bboard.has('stageFloor-%s' % avId):
                floor = bboard.get('stageFloor-%s' % avId)
                floor = max(0, floor)
                floor = min(floor, numFloors - 1)
                break

        for avId in players:
            if bboard.has('stageRoom-%s' % avId):
                roomId = bboard.get('stageRoom-%s' % avId)
                for i in xrange(numFloors):
                    layout = StageLayout.StageLayout(stageId, i)
                    if roomId in layout.getRoomIds():
                        floor = i
                else:
                    from toontown.coghq import StageRoomSpecs
                    roomName = StageRoomSpecs.CashbotStageRoomId2RoomName[roomId]
                    StageManagerAI.notify.warning('room %s (%s) not found in any floor of stage %s' % (roomId, roomName, stageId))

        stageZone = self.air.allocateZone()
        stage = DistributedStageAI.DistributedStageAI(self.air, stageId, stageZone, floor, players)
        stage.generateWithRequired(stageZone)
        return stageZone