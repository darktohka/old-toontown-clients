# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\parties\InviteInfo.py
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.parties.PartyGlobals import InviteStatus
from toontown.toonbase import TTLocalizer

class InviteInfoBase:
    __module__ = __name__

    def __init__(self, inviteKey, partyId, status):
        self.inviteKey = inviteKey
        self.partyId = partyId
        self.status = status

    def __str__(self):
        string = 'inviteKey=%d ' % self.inviteKey
        string += 'partyId=%d ' % self.partyId
        string += 'status=%s' % InviteStatus.getString(self.status)
        return string

    def __repr__(self):
        return self.__str__()


class InviteInfo(InviteInfoBase):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('InviteInfo')

    def __init__(self, inviteKey, partyId, status):
        InviteInfoBase.__init__(self, inviteKey, partyId, status)

    def acceptItem(self, mailbox, acceptingIndex, callback):
        InviteInfo.notify.debug('acceptItem')
        mailbox.acceptInvite(self, acceptingIndex, callback)

    def discardItem(self, mailbox, acceptingIndex, callback):
        InviteInfo.notify.debug('discardItem')
        mailbox.rejectInvite(self, acceptingIndex, callback)

    def getAcceptItemErrorText(self, retcode):
        InviteInfo.notify.debug('getAcceptItemErrorText')
        if retcode == ToontownGlobals.P_InvalidIndex:
            return TTLocalizer.InviteAcceptInvalidError
        elif retcode == ToontownGlobals.P_ItemAvailable:
            return TTLocalizer.InviteAcceptAllOk
        else:
            return TTLocalizer.CatalogAcceptGeneralError % retcode

    def getDiscardItemErrorText(self, retcode):
        InviteInfo.notify.debug('getDiscardItemErrorText')
        if retcode == ToontownGlobals.P_InvalidIndex:
            return TTLocalizer.InviteAcceptInvalidError
        elif retcode == ToontownGlobals.P_ItemAvailable:
            return TTLocalizer.InviteRejectAllOk
        else:
            return TTLocalizer.CatalogAcceptGeneralError % retcode

    def output(self, store=-1):
        return 'InviteInfo %s' % str(self)