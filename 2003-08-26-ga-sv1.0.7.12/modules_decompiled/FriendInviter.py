# File: F (Python 2.2)

from ShowBaseGlobal import *
from ToontownGlobals import *
from DirectGui import *
import PandaObject
import FSM
import State
import DirectNotifyGlobal
import AvatarDetailPanel
import TeleportPanel
import Suit
import Localizer
globalFriendInviter = None

def showFriendInviter(avId, avName, avDisableName):
    global globalFriendInviter
    if globalFriendInviter != None:
        globalFriendInviter.cleanup()
        globalFriendInviter = None
    
    globalFriendInviter = FriendInviter(avId, avName, avDisableName)


def hideFriendInviter():
    global globalFriendInviter
    if globalFriendInviter != None:
        globalFriendInviter.cleanup()
        globalFriendInviter = None
    


def unloadFriendInviter():
    global globalFriendInviter
    if globalFriendInviter != None:
        globalFriendInviter.cleanup()
        globalFriendInviter = None
    


class FriendInviter(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('FriendInviter')
    
    def __init__(self, avId, avName, avDisableName):
        DirectFrame.__init__(self, pos = (0.29999999999999999, 0.10000000000000001, 0.65000000000000002), image_color = GlobalDialogColor, image_scale = (1.0, 1.0, 0.59999999999999998), text = '', text_wordwrap = 13.5, text_scale = 0.059999999999999998, text_pos = (0.0, 0.13))
        self['image'] = getDefaultDialogGeom()
        self.avId = avId
        self.avName = avName
        self.avDisableName = avDisableName
        self.fsm = FSM.FSM('FriendInviter', [
            State.State('off', self.enterOff, self.exitOff),
            State.State('getNewFriend', self.enterGetNewFriend, self.exitGetNewFriend),
            State.State('begin', self.enterBegin, self.exitBegin),
            State.State('tooMany', self.enterTooMany, self.exitTooMany),
            State.State('notYet', self.enterNotYet, self.exitNotYet),
            State.State('checkAvailability', self.enterCheckAvailability, self.exitCheckAvailability),
            State.State('notAvailable', self.enterNotAvailable, self.exitNotAvailable),
            State.State('notAcceptingFriends', self.enterNotAcceptingFriends, self.exitNotAcceptingFriends),
            State.State('wentAway', self.enterWentAway, self.exitWentAway),
            State.State('already', self.enterAlready, self.exitAlready),
            State.State('askingCog', self.enterAskingCog, self.exitAskingCog),
            State.State('endFriendship', self.enterEndFriendship, self.exitEndFriendship),
            State.State('friendsNoMore', self.enterFriendsNoMore, self.exitFriendsNoMore),
            State.State('self', self.enterSelf, self.exitSelf),
            State.State('ignored', self.enterIgnored, self.exitIgnored),
            State.State('asking', self.enterAsking, self.exitAsking),
            State.State('yes', self.enterYes, self.exitYes),
            State.State('no', self.enterNo, self.exitNo),
            State.State('otherTooMany', self.enterOtherTooMany, self.exitOtherTooMany),
            State.State('maybe', self.enterMaybe, self.exitMaybe),
            State.State('down', self.enterDown, self.exitDown),
            State.State('cancel', self.enterCancel, self.exitCancel)], 'off', 'off')
        self.context = None
        TeleportPanel.hideTeleportPanel()
        AvatarDetailPanel.hideAvatarDetail()
        buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
        gui = loader.loadModelOnce('phase_3.5/models/gui/avatar_panel_gui')
        self.bOk = DirectButton(self, image = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr')), relief = None, text = Localizer.FriendInviterOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), pos = (0.0, 0.0, -0.10000000000000001), command = self._FriendInviter__handleOk)
        self.bOk.hide()
        self.bCancel = DirectButton(self, image = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr')), relief = None, text = Localizer.FriendInviterCancel, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), pos = (0.0, 0.0, -0.10000000000000001), command = self._FriendInviter__handleCancel)
        self.bCancel.hide()
        self.bStop = DirectButton(self, image = (gui.find('**/Ignore_Btn_UP'), gui.find('**/Ignore_Btn_DN'), gui.find('**/Ignore_Btn_RLVR')), relief = None, text = Localizer.FriendInviterStopBeingFriends, text_scale = 0.050000000000000003, text_pos = (0.25, -0.014999999999999999), pos = (-0.20000000000000001, 0.0, 0.050000000000000003), command = self._FriendInviter__handleStop)
        self.bStop.hide()
        self.bYes = DirectButton(self, image = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr')), relief = None, text = Localizer.FriendInviterYes, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), pos = (-0.14999999999999999, 0.0, -0.10000000000000001), command = self._FriendInviter__handleYes)
        self.bYes.hide()
        self.bNo = DirectButton(self, image = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr')), relief = None, text = Localizer.FriendInviterNo, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), pos = (0.14999999999999999, 0.0, -0.10000000000000001), command = self._FriendInviter__handleNo)
        self.bNo.hide()
        buttons.removeNode()
        gui.removeNode()
        self.fsm.enterInitialState()
        if self.avId == None:
            self.fsm.request('getNewFriend')
        else:
            self.fsm.request('begin')

    
    def cleanup(self):
        self.fsm.request('cancel')
        del self.fsm
        self.destroy()

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterGetNewFriend(self):
        self['text'] = Localizer.FriendInviterClickToon
        self.bCancel.show()
        self.accept('clickedNametag', self._FriendInviter__handleClickedNametag)

    
    def exitGetNewFriend(self):
        self.bCancel.hide()
        self.ignore('clickedNametag')

    
    def _FriendInviter__handleClickedNametag(self, avatar):
        self.avId = avatar.doId
        self.avName = avatar.getName()
        self.avDisableName = avatar.uniqueName('disable')
        self.fsm.request('begin')

    
    def enterBegin(self):
        myId = toonbase.localToon.doId
        self.accept(self.avDisableName, self._FriendInviter__handleDisableAvatar)
        if self.avId == myId:
            self.fsm.request('self')
        elif toonbase.tcr.isFriend(self.avId):
            self.fsm.request('already')
        else:
            tooMany = len(toonbase.localToon.friendsList) >= MaxFriends
            if tooMany:
                self.fsm.request('tooMany')
            else:
                self.fsm.request('notYet')

    
    def exitBegin(self):
        self.ignore(self.avDisableName)

    
    def enterTooMany(self):
        self['text'] = Localizer.FriendInviterTooMany % self.avName
        self['text_pos'] = (0.0, 0.20000000000000001)
        self.bCancel.show()
        self.bCancel.setPos(0.0, 0.0, -0.16)

    
    def exitTooMany(self):
        self.bCancel.hide()

    
    def enterNotYet(self):
        self.accept(self.avDisableName, self._FriendInviter__handleDisableAvatar)
        self['text'] = Localizer.FriendInviterNotYet % self.avName
        self.bYes.show()
        self.bNo.show()

    
    def exitNotYet(self):
        self.ignore(self.avDisableName)
        self.bYes.hide()
        self.bNo.hide()

    
    def enterCheckAvailability(self):
        self.accept(self.avDisableName, self._FriendInviter__handleDisableAvatar)
        if not toonbase.tcr.doId2do.has_key(self.avId):
            self.fsm.request('wentAway')
            return None
        
        avatar = toonbase.tcr.doId2do[self.avId]
        if isinstance(avatar, Suit.Suit):
            self.fsm.request('askingCog')
            return None
        
        if not (toonbase.tcr.friendManager):
            self.notify.warning('No FriendManager available.')
            self.fsm.request('down')
            return None
        
        toonbase.tcr.friendManager.up_friendQuery(self.avId)
        self['text'] = Localizer.FriendInviterCheckAvailability % self.avName
        self.accept('friendConsidering', self._FriendInviter__friendConsidering)
        self.accept('friendResponse', self._FriendInviter__friendResponse)
        self.bCancel.show()

    
    def exitCheckAvailability(self):
        self.ignore(self.avDisableName)
        self.ignore('friendConsidering')
        self.ignore('friendResponse')
        self.bCancel.hide()

    
    def enterNotAvailable(self):
        self['text'] = Localizer.FriendInviterNotAvailable % self.avName
        self.context = None
        self.bOk.show()

    
    def exitNotAvailable(self):
        self.bOk.hide()

    
    def enterNotAcceptingFriends(self):
        self['text'] = Localizer.FriendInviterFriendSaidNoNewFriends % self.avName
        self.context = None
        self.bOk.show()

    
    def exitNotAcceptingFriends(self):
        self.bOk.hide()

    
    def enterWentAway(self):
        self['text'] = Localizer.FriendInviterWentAway % self.avName
        if self.context != None:
            toonbase.tcr.friendManager.up_cancelFriendQuery(self.context)
            self.context = None
        
        self.bOk.show()

    
    def exitWentAway(self):
        self.bOk.hide()

    
    def enterAlready(self):
        self['text'] = Localizer.FriendInviterAlready % self.avName
        self['text_pos'] = (0.0, 0.20000000000000001)
        self.context = None
        self.bStop.show()
        self.bCancel.show()

    
    def exitAlready(self):
        self['text'] = ''
        self['text_pos'] = (0.0, 0.13)
        self.bStop.hide()
        self.bCancel.hide()

    
    def enterAskingCog(self):
        self['text'] = Localizer.FriendInviterAskingCog % self.avName
        taskMgr.doMethodLater(2.0, self.cogReplies, 'cogFriendship')
        self.bCancel.show()

    
    def exitAskingCog(self):
        taskMgr.remove('cogFriendship')
        self.bCancel.hide()

    
    def cogReplies(self, task):
        self.fsm.request('no')
        return Task.done

    
    def enterEndFriendship(self):
        self['text'] = Localizer.FriendInviterEndFriendship % self.avName
        self.context = None
        self.bYes.show()
        self.bNo.show()

    
    def exitEndFriendship(self):
        self.bYes.hide()
        self.bNo.hide()

    
    def enterFriendsNoMore(self):
        toonbase.tcr.removeFriend(self.avId)
        self['text'] = Localizer.FriendInviterFriendsNoMore % self.avName
        self.bOk.show()
        if not toonbase.tcr.doId2do.has_key(self.avId):
            messenger.send(self.avDisableName)
        

    
    def exitFriendsNoMore(self):
        self.bOk.hide()

    
    def enterSelf(self):
        self['text'] = Localizer.FriendInviterSelf
        self.context = None
        self.bOk.show()

    
    def exitSelf(self):
        self.bOk.hide()

    
    def enterIgnored(self):
        self['text'] = Localizer.FriendInviterIgnored % self.avName
        self.context = None
        self.bOk.show()

    
    def exitIgnored(self):
        self.bOk.hide()

    
    def enterAsking(self):
        self.accept(self.avDisableName, self._FriendInviter__handleDisableAvatar)
        self['text'] = Localizer.FriendInviterAsking % self.avName
        self.accept('friendResponse', self._FriendInviter__friendResponse)
        self.bCancel.show()

    
    def exitAsking(self):
        self.ignore(self.avDisableName)
        self.ignore('friendResponse')
        self.bCancel.hide()

    
    def enterYes(self):
        self['text'] = Localizer.FriendInviterFriendSaidYes % self.avName
        self.context = None
        self.bOk.show()

    
    def exitYes(self):
        self.bOk.hide()

    
    def enterNo(self):
        self['text'] = Localizer.FriendInviterFriendSaidNo % self.avName
        self.context = None
        self.bOk.show()

    
    def exitNo(self):
        self.bOk.hide()

    
    def enterOtherTooMany(self):
        self['text'] = Localizer.FriendInviterTooMany % self.avName
        self.context = None
        self.bOk.show()

    
    def exitOtherTooMany(self):
        self.bOk.hide()

    
    def enterMaybe(self):
        self['text'] = Localizer.FriendInviterMaybe % self.avName
        self.context = None
        self.bOk.show()

    
    def exitMaybe(self):
        self.bOk.hide()

    
    def enterDown(self):
        self['text'] = Localizer.FriendInviterDown
        self.context = None
        self.bOk.show()

    
    def exitDown(self):
        self.bOk.hide()

    
    def enterCancel(self):
        if self.context != None:
            toonbase.tcr.friendManager.up_cancelFriendQuery(self.context)
            self.context = None
        
        self.fsm.request('off')

    
    def exitCancel(self):
        pass

    
    def _FriendInviter__handleOk(self):
        unloadFriendInviter()

    
    def _FriendInviter__handleCancel(self):
        unloadFriendInviter()

    
    def _FriendInviter__handleStop(self):
        self.fsm.request('endFriendship')

    
    def _FriendInviter__handleYes(self):
        if self.fsm.getCurrentState().getName() == 'notYet':
            self.fsm.request('checkAvailability')
        elif self.fsm.getCurrentState().getName() == 'endFriendship':
            self.fsm.request('friendsNoMore')
        else:
            unloadFriendInviter()

    
    def _FriendInviter__handleNo(self):
        unloadFriendInviter()

    
    def _FriendInviter__handleList(self):
        messenger.send('openFriendsList')

    
    def _FriendInviter__friendConsidering(self, yesNoAlready, context):
        if yesNoAlready == 1:
            self.context = context
            self.fsm.request('asking')
        elif yesNoAlready == 0:
            self.fsm.request('notAvailable')
        elif yesNoAlready == 2:
            self.fsm.request('already')
        elif yesNoAlready == 3:
            self.fsm.request('self')
        elif yesNoAlready == 4:
            self.fsm.request('ignored')
        elif yesNoAlready == 6:
            self.fsm.request('notAcceptingFriends')
        elif yesNoAlready == 10:
            self.fsm.request('no')
        elif yesNoAlready == 13:
            self.fsm.request('otherTooMany')
        else:
            self.notify.warning('Got unexpected response to friendConsidering: %s' % yesNoAlready)
            self.fsm.request('maybe')

    
    def _FriendInviter__friendResponse(self, yesNoMaybe, context):
        if self.context != context:
            self.notify.warning('Unexpected change of context from %s to %s.' % (self.context, context))
            self.context = context
        
        if yesNoMaybe == 1:
            self.fsm.request('yes')
        elif yesNoMaybe == 0:
            self.fsm.request('no')
        elif yesNoMaybe == 3:
            self.fsm.request('otherTooMany')
        else:
            self.notify.warning('Got unexpected response to friendResponse: %s' % yesNoMaybe)
            self.fsm.request('maybe')

    
    def _FriendInviter__handleDisableAvatar(self):
        self.fsm.request('wentAway')


