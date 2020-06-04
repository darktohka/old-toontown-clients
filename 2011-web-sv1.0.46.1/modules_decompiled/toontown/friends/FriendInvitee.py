# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\friends\FriendInvitee.py
from pandac.PandaModules import *
from toontown.toonbase.ToontownGlobals import *
from direct.showbase import DirectObject
from direct.directnotify import DirectNotifyGlobal
from toontown.toontowngui import TTDialog
from otp.otpbase import OTPLocalizer
from toontown.toontowngui import ToonHeadDialog
from direct.gui.DirectGui import DGG
from otp.otpbase import OTPGlobals
from toontown.toon import GMUtils

class FriendInvitee(ToonHeadDialog.ToonHeadDialog):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('FriendInvitee')

    def __init__(self, avId, avName, avDNA, context, **kw):
        self.avId = avId
        self.avDNA = avDNA
        self.context = context
        if GMUtils.testGMIdentity(avName):
            self.avName = GMUtils.handleGMName(avName)
        else:
            self.avName = avName
        if len(base.localAvatar.friendsList) >= MaxFriends:
            base.cr.friendManager.up_inviteeFriendResponse(3, self.context)
            self.context = None
            text = OTPLocalizer.FriendInviteeTooManyFriends % self.avName
            style = TTDialog.Acknowledge
            buttonTextList = [OTPLocalizer.FriendInviteeOK]
            command = self.__handleOhWell
        else:
            text = OTPLocalizer.FriendInviteeInvitation % self.avName
            style = TTDialog.TwoChoice
            buttonTextList = [OTPLocalizer.FriendInviteeOK, OTPLocalizer.FriendInviteeNo]
            command = self.__handleButton
        optiondefs = (('dialogName', 'FriendInvitee', None), ('text', text, None), ('style', style, None), ('buttonTextList', buttonTextList, None), ('command', command, None), ('image_color', (1.0, 0.89, 0.77, 1.0), None), ('geom_scale', 0.2, None), ('geom_pos', (-0.1, 0, -0.025), None), ('pad', (0.075, 0.075), None), ('topPad', 0, None), ('midPad', 0, None), ('pos', (0.45, 0, 0.75), None), ('scale', 0.75, None))
        self.defineoptions(kw, optiondefs)
        ToonHeadDialog.ToonHeadDialog.__init__(self, self.avDNA)
        self.accept('cancelFriendInvitation', self.__handleCancelFromAbove)
        self.initialiseoptions(FriendInvitee)
        self.show()
        return

    def cleanup(self):
        ToonHeadDialog.ToonHeadDialog.cleanup(self)
        self.ignore('cancelFriendInvitation')
        if self.context != None:
            base.cr.friendManager.up_inviteeFriendResponse(2, self.context)
            self.context = None
        if base.friendMode == 1:
            base.cr.friendManager.executeGameSpecificFunction()
        return

    def __handleButton(self, value):
        print 'handleButton'
        if value == DGG.DIALOG_OK:
            if base.friendMode == 0:
                base.cr.friendManager.up_inviteeFriendResponse(1, self.context)
            elif base.friendMode == 1:
                print 'sending Request Invite'
                base.cr.avatarFriendsManager.sendRequestInvite(self.avId)
        elif base.friendMode == 0:
            base.cr.friendManager.up_inviteeFriendResponse(0, self.context)
        elif base.friendMode == 1:
            base.cr.avatarFriendsManager.sendRequestRemove(self.avId)
        self.context = None
        self.cleanup()
        return

    def __handleOhWell(self, value):
        self.cleanup()

    def __handleCancelFromAbove(self, context=None):
        if context == None or context == self.context:
            self.context = None
            self.cleanup()
        return