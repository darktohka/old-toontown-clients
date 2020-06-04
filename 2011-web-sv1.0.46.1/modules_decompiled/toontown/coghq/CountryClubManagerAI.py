# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\CountryClubManagerAI.py
from direct.directnotify import DirectNotifyGlobal
import DistributedCountryClubAI
from toontown.toonbase import ToontownGlobals
from toontown.coghq import CountryClubLayout
from direct.showbase import DirectObject
import random
CountryClubId2Layouts = {ToontownGlobals.BossbotCountryClubIntA: (0, 1, 2), ToontownGlobals.BossbotCountryClubIntB: (3, 4, 5), ToontownGlobals.BossbotCountryClubIntC: (6, 7, 8)}

class CountryClubManagerAI(DirectObject.DirectObject):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('CountryClubManagerAI')
    countryClubId = None

    def __init__(self, air):
        DirectObject.DirectObject.__init__(self)
        self.air = air

    def getDoId(self):
        return 0

    def createCountryClub(self, countryClubId, players):
        for avId in players:
            if bboard.has('countryClubId-%s' % avId):
                countryClubId = bboard.get('countryClubId-%s' % avId)
                break

        numFloors = 1
        layoutIndex = None
        floor = 0
        for avId in players:
            if bboard.has('countryClubFloor-%s' % avId):
                floor = bboard.get('countryClubFloor-%s' % avId)
                floor = max(0, floor)
                floor = min(floor, numFloors - 1)
                break

        for avId in players:
            if bboard.has('countryClubRoom-%s' % avId):
                roomId = bboard.get('countryClubRoom-%s' % avId)
                for i in xrange(numFloors):
                    layout = CountryClubLayout.CountryClubLayout(countryClubId, i)
                    if roomId in layout.getRoomIds():
                        floor = i
                else:
                    from toontown.coghq import CountryClubRoomSpecs
                    roomName = CountryClubRoomSpecs.BossbotCountryClubRoomId2RoomName[roomId]
                    CountryClubManagerAI.notify.warning('room %s (%s) not found in any floor of countryClub %s' % (roomId, roomName, countryClubId))

        countryClubZone = self.air.allocateZone()
        if layoutIndex is None:
            layoutIndex = random.choice(CountryClubId2Layouts[countryClubId])
        countryClub = DistributedCountryClubAI.DistributedCountryClubAI(self.air, countryClubId, countryClubZone, floor, players, layoutIndex)
        countryClub.generateWithRequired(countryClubZone)
        return countryClubZone