# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\hood\TrialerForceAcknowledge.py
from pandac.PandaModules import *
from toontown.toonbase import TTLocalizer
import ZoneUtil
from toontown.toonbase import ToontownGlobals
from toontown.toontowngui import TeaserPanel

class TrialerForceAcknowledge:
    __module__ = __name__

    def __init__(self, doneEvent):
        self.doneEvent = doneEvent
        self.dialog = None
        return

    def enter(self, destHood):
        doneStatus = {}

        def letThrough(self=self, doneStatus=doneStatus):
            doneStatus['mode'] = 'pass'
            messenger.send(self.doneEvent, [doneStatus])

        if not base.restrictTrialers:
            letThrough()
            return
        if base.roamingTrialers:
            letThrough()
            return
        if base.cr.isPaid():
            letThrough()
            return
        if ZoneUtil.getCanonicalHoodId(destHood) in (ToontownGlobals.ToontownCentral, ToontownGlobals.MyEstate, ToontownGlobals.GoofySpeedway):
            letThrough()
            return
        else:
            try:
                base.localAvatar.b_setAnimState('neutral', 1)
            except:
                pass

        doneStatus['mode'] = 'fail'
        self.doneStatus = doneStatus
        self.dialog = TeaserPanel.TeaserPanel(pageName='otherHoods', doneFunc=self.handleOk)

    def exit(self):
        if self.dialog:
            self.dialog.cleanup()
            self.dialog.unload()
            self.dialog = None
        return

    def handleOk(self):
        messenger.send(self.doneEvent, [self.doneStatus])