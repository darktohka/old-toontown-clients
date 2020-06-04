# File: F (Python 2.2)

from ShowBaseGlobal import *
from ToontownGlobals import *
import PandaObject
import DirectNotifyGlobal
import ToontownDialog
import Localizer
import ToonHeadDialog

class FriendInvitee(ToonHeadDialog.ToonHeadDialog):
    notify = DirectNotifyGlobal.directNotify.newCategory('FriendInvitee')
    
    def __init__(self, avId, avName, avDNA, context, **kw):
        self.avId = avId
        self.avName = avName
        self.avDNA = avDNA
        self.context = context
        if len(toonbase.localToon.friendsList) >= MaxFriends:
            toonbase.tcr.friendManager.up_inviteeFriendResponse(3, self.context)
            self.context = None
            text = Localizer.FriendInviteeTooManyFriends % self.avName
            style = ToontownDialog.Acknowledge
            buttonTextList = [
                Localizer.FriendInviteeOK]
            command = self._FriendInvitee__handleOhWell
        else:
            text = Localizer.FriendInviteeInvitation % self.avName
            style = ToontownDialog.TwoChoice
            buttonTextList = [
                Localizer.FriendInviteeOK,
                Localizer.FriendInviteeNo]
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
            toonbase.tcr.friendManager.up_inviteeFriendResponse(2, self.context)
            self.context = None
        

    
    def _FriendInvitee__handleButton(self, value):
        if value == ToontownDialog.DIALOG_OK:
            toonbase.tcr.friendManager.up_inviteeFriendResponse(1, self.context)
        else:
            toonbase.tcr.friendManager.up_inviteeFriendResponse(0, self.context)
        self.context = None
        self.cleanup()

    
    def _FriendInvitee__handleOhWell(self, value):
        self.cleanup()

    
    def _FriendInvitee__handleCancelFromAbove(self, context = None):
        if context == None or context == self.context:
            self.context = None
            self.cleanup()
        


