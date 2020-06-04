# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\distributed\ToontownDistrictStats.py
from direct.showbase import DirectObject
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from direct.task import Task
from direct.distributed import DoInterestManager
from otp.distributed.OtpDoGlobals import *
_ToonTownDistrictStatInterest = None
_ToonTownDistrictStatInterestComplete = 0
_trashObject = DirectObject.DirectObject()

def EventName():
    return 'ShardPopulationSet'


def isOpen():
    global _ToonTownDistrictStatInterest
    return _ToonTownDistrictStatInterest is not None


def isComplete():
    global _ToonTownDistrictStatInterestComplete
    return _ToonTownDistrictStatInterestComplete


def open(event=None):
    global _ToonTownDistrictStatInterest
    global _trashObject
    if not isOpen():

        def _CompleteProc(event):
            global _ToonTownDistrictStatInterestComplete
            _ToonTownDistrictStatInterestComplete = 1
            if event is not None:
                messenger.send(event)
            return

        _trashObject.acceptOnce(EventName(), _CompleteProc)
        _ToonTownDistrictStatInterest = base.cr.addInterest(OTP_DO_ID_TOONTOWN, OTP_ZONE_ID_DISTRICTS_STATS, EventName(), EventName())
    elif isComplete():
        messenger.send(EventName())


def refresh(event=None):
    global _ToonTownDistrictStatInterest
    if isOpen():
        if isComplete():
            messenger.send(EventName())
            if event is not none:
                messenger.send(event)
    else:

        def _CompleteProc(event):
            global _ToonTownDistrictStatInterestComplete
            _ToonTownDistrictStatInterestComplete = 1
            if event is not None:
                messenger.send(event)
            close()
            return

        _trashObject.acceptOnce(EventName(), _CompleteProc, [event])
        _ToonTownDistrictStatInterest = base.cr.addInterest(OTP_DO_ID_TOONTOWN, OTP_ZONE_ID_DISTRICTS_STATS, EventName(), EventName())


def close():
    global _ToonTownDistrictStatInterest
    global _ToonTownDistrictStatInterestComplete
    if isOpen():
        _ToonTownDistrictStatInterestComplete = 0
        base.cr.removeInterest(_ToonTownDistrictStatInterest, None)
        _ToonTownDistrictStatInterest = None
    return


class ToontownDistrictStats(DistributedObject.DistributedObject):
    __module__ = __name__
    neverDisable = 1

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.toontownDistrictId = 0

    def settoontownDistrictId(self, value):
        self.toontownDistrictId = value

    def setAvatarCount(self, avatarCount):
        if self.cr.activeDistrictMap.has_key(self.toontownDistrictId):
            self.cr.activeDistrictMap[self.toontownDistrictId].avatarCount = avatarCount

    def setNewAvatarCount(self, newAvatarCount):
        if self.cr.activeDistrictMap.has_key(self.toontownDistrictId):
            self.cr.activeDistrictMap[self.toontownDistrictId].newAvatarCount = newAvatarCount

    def setStats(self, avatarCount, newAvatarCount):
        self.setAvatarCount(avatarCount)
        self.setNewAvatarCount(newAvatarCount)