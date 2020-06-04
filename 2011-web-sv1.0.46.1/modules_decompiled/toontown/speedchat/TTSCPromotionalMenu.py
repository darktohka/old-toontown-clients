# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\speedchat\TTSCPromotionalMenu.py
from direct.directnotify import DirectNotifyGlobal
from otp.speedchat.SCMenu import SCMenu
from otp.speedchat import SCMenuHolder
from otp.speedchat.SCStaticTextTerminal import SCStaticTextTerminal
from otp.otpbase import OTPLocalizer
from toontown.toonbase import ToontownGlobals
holidayId2menuInfo = {ToontownGlobals.ELECTION_PROMOTION: (OTPLocalizer.SCMenuElection, [10000, 10001, 10006, 10007])}

class TTSCPromotionalMenu(SCMenu):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('TTSCPromotionalMenu')

    def __init__(self):
        SCMenu.__init__(self)
        base.TTSCPromotionalMenu = self
        self.curHolidayId = None
        self.clearMenu()
        return

    def destroy(self):
        del base.TTSCPromotionalMenu
        SCMenu.destroy(self)

    def startHoliday(self, holidayId):
        if self.curHolidayId is not None:
            TTSCPromotionalMenu.notify.warning('overriding existing holidayId %s with %s' % (self.curHolidayId, holidayId))
        self.curHolidayId = holidayId
        (title, structure) = holidayId2menuInfo[holidayId]
        self.rebuildFromStructure(structure, title=title)
        return

    def endHoliday(self, holidayId):
        if holidayId != self.curHolidayId:
            TTSCPromotionalMenu.notify.warning('unexpected holidayId: %s' % holidayId)
            return
        self.curHolidayId = None
        self.clearMenu()
        return