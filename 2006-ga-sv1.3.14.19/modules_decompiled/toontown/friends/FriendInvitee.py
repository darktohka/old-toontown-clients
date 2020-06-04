# File: F (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToontownGlobals import *
from direct.showbase import PandaObject
from direct.directnotify import DirectNotifyGlobal
from toontown.toontowngui import TTDialog
from otp.otpbase import OTPLocalizer
from toontown.toontowngui import ToonHeadDialog

class FriendInvitee(ToonHeadDialog.ToonHeadDialog):
    notify = DirectNotifyGlobal.directNotify.newCategory('FriendInvitee')
    
    def __init__(self, avId, avName, avDNA, context, **kw):
        self.avId = avId
        self.avName = avName
        self.avDNA = avDNA
        self.context = context
        if len(base.localAvatar.friendsList) >= MaxFriends:
            base.cr.friendManager.up_inviteeFriendResponse(3, self.context)
            self.context = None
            text = OTPLocalizer.FriendInviteeTooManyFriends % self.avName
            style = TTDialog.Acknowledge
            buttonTextList = [
                OTPLocalizer.FriendInviteeOK]
            command = self._FriendInvitee__handleOhWell
        else:
            text = OTPLocalizer.FriendInviteeInvitation % self.avName
            style = TTDialog.TwoChoice
            buttonTextList = [
                OTPLocalizer.FriendInviteeOK,
                OTPLocalizer.FriendInviteeNo]
            command = self._FriendInvitee__handleButton
        optiondefs = (('dialogName', 'FriendInvitee', None), ('text', text, None), ('style', style, None), ('buttonTextList', buttonTextList, None), ('command', command, None), ('image_color', (1.0, 0.89000000000000001, 0.77000000000000002, 1.0), None), ('geom_scale', 0.20000000000000001, None), ('geom_pos', (-0.10000000000000001, 0, -0.025000000000000001), None), ('pad', (0.074999999999999997, 0.074999999999999997), None), ('topPad', 0, None), ('midPad', 0, None), ('pos', (0.45000000000000001, 0, 0.75), None), ('scale', 0.75, None))
        self.defineoptions(kw, optiondefs)
        ToonHeadDialog.ToonHeadDialog.__init__(self, self.avDNA)
        self.accept('cancelFriendInvitation', self._FriendInvitee__handleCancelFromAbove)
        self.initialiseoptions(FriendInvitee)
        self.show()

    
    def cleanup(self):
        ToonHeadDialog.ToonHeadDialog.cleanup(self)
        self.ignore('cancelFriendInvitation')
        if self.context != None:
            base.cr.friendManager.up_inviteeFriendResponse(2, self.context)
            self.context = None
        

    
    def _FriendInvitee__handleButton(self, value):
        if value == TTDialog.DIALOG_OK:
            base.cr.friendManager.up_inviteeFriendResponse(1, self.context)
        else:
            base.cr.friendManager.up_inviteeFriendResponse(0, self.context)
        self.context = None
        self.cleanup()

    
    def _FriendInvitee__handleOhWell(self, value):
        self.cleanup()

    
    def _FriendInvitee__handleCancelFromAbove(self, context = None):
        if context == None or context == self.context:
            self.context = None
            self.cleanup()
        


