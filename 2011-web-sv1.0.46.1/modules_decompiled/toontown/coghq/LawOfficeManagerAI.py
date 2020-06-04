# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\LawOfficeManagerAI.py
from direct.directnotify import DirectNotifyGlobal
import DistributedLawOfficeAI, DistributedStageAI
from toontown.coghq import StageLayout
from toontown.toonbase import ToontownGlobals
from direct.showbase import DirectObject
import random
StageId2Layouts = {ToontownGlobals.LawbotStageIntA: (0, 1, 2), ToontownGlobals.LawbotStageIntB: (3, 4, 5), ToontownGlobals.LawbotStageIntC: (6, 7, 8), ToontownGlobals.LawbotStageIntD: (9, 10, 11)}

class LawOfficeManagerAI(DirectObject.DirectObject):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('LawOfficeManagerAI')
    lawOfficeId = None

    def __init__(self, air):
        DirectObject.DirectObject.__init__(self)
        self.air = air

    def getDoId(self):
        return 0

    def createLawOffice(self, StageId, entranceId, players):
        for avId in players:
            if bboard.has('StageId-%s' % avId):
                StageId = bboard.get('StageId-%s' % avId)
                break

        floor = 0
        layoutIndex = None
        for avId in players:
            if bboard.has('stageRoom-%s' % avId):
                roomId = bboard.get('stageRoom-%s' % avId)
                for lt in StageId2Layouts[StageId]:
                    for i in xrange(StageLayout.getNumFloors(lt)):
                        layout = StageLayout.StageLayout(StageId, i, stageLayout=lt)
                        if roomId in layout.getRoomIds():
                            layoutIndex = lt
                            floor = i

                else:
                    from toontown.coghq import StageRoomSpecs
                    roomName = StageRoomSpecs.CashbotStageRoomId2RoomName[roomId]
                    LawOfficeManagerAI.notify.warning('room %s (%s) not found in any floor of Stage %s' % (roomId, roomName, StageId))

        StageZone = self.air.allocateZone()
        if layoutIndex is None:
            layoutIndex = random.choice(StageId2Layouts[StageId])
        Stage = DistributedStageAI.DistributedStageAI(self.air, StageId, StageZone, floor, players, layoutIndex)
        Stage.generateWithRequired(StageZone)
        return StageZone