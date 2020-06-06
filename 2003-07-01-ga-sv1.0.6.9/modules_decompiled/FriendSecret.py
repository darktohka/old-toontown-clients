# File: F (Python 2.2)

from ShowBaseGlobal import *
from ToontownGlobals import *
from DirectGui import *
import StateData
import string
import Localizer
globalFriendSecret = None

def showFriendSecret():
    global globalFriendSecret
    if not toonbase.tcr.isPaid():
        chatMgr = toonbase.localToon.chatMgr
        chatMgr.fsm.request('unpaidChatWarning')
    elif not toonbase.tcr.allowSecretChat():
        chatMgr = toonbase.localToon.chatMgr
        chatMgr.fsm.request('noSecretChatWarning')
    elif globalFriendSecret == None:
        globalFriendSecret = FriendSecret()
    
    globalFriendSecret.enter()


def hideFriendSecret():
    if globalFriendSecret != None:
        globalFriendSecret.exit()
    


def unloadFriendSecret():
    global globalFriendSecret
    if globalFriendSecret != None:
        globalFriendSecret.unload()
        globalFriendSecret = None
    


class FriendSecret(DirectFrame, StateData.StateData):
    
    def __init__(self):
        DirectFrame.__init__(self, pos = (0, 0, 0.29999999999999999), relief = None, image = getDefaultDialogGeom(), image_scale = (1.6000000000000001, 1, 1.2), image_pos = (0, 0, -0.050000000000000003), image_color = GlobalDialogColor, borderWidth = (0.01, 0.01))
        StateData.StateData.__init__(self, 'friend-secret-done')
        self.initialiseoptions(FriendSecret)

    
    def unload(self):
        if self.isLoaded == 0:
            return None
        
        self.isLoaded = 0
        self.exit()
        del self.introText
        del self.getSecret
        del self.enterSecretText
        del self.enterSecret
        del self.ok1
        del self.ok2
        del self.cancel
        del self.secretText
        DirectFrame.destroy(self)

    
    def load(self):
        if self.isLoaded == 1:
            return None
        
        self.isLoaded = 1
        self.introText = DirectLabel(parent = self, relief = None, pos = (0, 0, 0.40000000000000002), scale = 0.050000000000000003, text = Localizer.FriendSecretIntro, text_fg = (0, 0, 0, 1), text_wordwrap = 30)
        self.introText.hide()
        guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
        self.getSecret = DirectButton(parent = self, relief = None, pos = (0, 0, -0.11), image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (1, 1, 1), text = Localizer.FriendSecretGetSecret, text_scale = 0.059999999999999998, text_pos = (0, -0.02), command = self._FriendSecret__getSecret)
        self.getSecret.hide()
        self.enterSecretText = DirectLabel(parent = self, relief = None, pos = (0, 0, -0.27000000000000002), scale = 0.050000000000000003, text = Localizer.FriendSecretEnterSecret, text_fg = (0, 0, 0, 1), text_wordwrap = 30)
        self.enterSecretText.hide()
        self.enterSecret = DirectEntry(parent = self, relief = SUNKEN, scale = 0.059999999999999998, pos = (-0.59999999999999998, 0, -0.38), frameColor = (0.80000000000000004, 0.80000000000000004, 0.5, 1), borderWidth = (0.10000000000000001, 0.10000000000000001), numLines = 1, width = 20, frameSize = (-0.40000000000000002, 20.399999999999999, -0.40000000000000002, 1.1000000000000001), command = self._FriendSecret__enterSecret)
        self.enterSecret.resetFrameSize()
        self.enterSecret.hide()
        self.ok1 = DirectButton(parent = self, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (0.59999999999999998, 1, 1), text = Localizer.FriendSecretOK, text_scale = 0.059999999999999998, text_pos = (0, -0.02), pos = (0, 0, -0.5), command = self._FriendSecret__ok1)
        self.ok1.hide()
        self.ok2 = DirectButton(parent = self, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (0.59999999999999998, 1, 1), text = Localizer.FriendSecretOK, text_scale = 0.059999999999999998, text_pos = (0, -0.02), pos = (0, 0, -0.56999999999999995), command = self._FriendSecret__ok2)
        self.ok2.hide()
        self.cancel = DirectButton(parent = self, relief = None, text = Localizer.FriendSecretCancel, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (0.59999999999999998, 1, 1), text_scale = 0.059999999999999998, text_pos = (0, -0.02), pos = (0, 0, -0.56999999999999995), command = self._FriendSecret__cancel)
        self.cancel.hide()
        self.nextText = DirectLabel(parent = self, relief = None, pos = (0, 0, 0.29999999999999999), scale = 0.059999999999999998, text = '', text_fg = (0, 0, 0, 1), text_wordwrap = 22)
        self.nextText.hide()
        self.secretText = DirectLabel(parent = self, relief = None, pos = (0, 0, -0.41999999999999998), scale = 0.10000000000000001, text = '', text_fg = (0, 0, 0, 1), text_wordwrap = 30)
        self.secretText.hide()
        guiButton.removeNode()

    
    def enter(self):
        if self.isEntered == 1:
            return None
        
        self.isEntered = 1
        if self.isLoaded == 0:
            self.load()
        
        self.show()
        self.introText.show()
        self.getSecret.show()
        self.enterSecretText.show()
        self.enterSecret.show()
        self.ok1.show()
        self.ok2.hide()
        self.cancel.hide()
        self.nextText.hide()
        self.secretText.hide()
        chatEntry = toonbase.localToon.chatMgr.chatInputNormal.chatEntry
        self.oldFocus = chatEntry['backgroundFocus']
        chatEntry['backgroundFocus'] = 0
        self.enterSecret['focus'] = 1
        NametagGlobals.setOnscreenChatForced(1)
        return None

    
    def exit(self):
        if self.isEntered == 0:
            return None
        
        self.isEntered = 0
        NametagGlobals.setOnscreenChatForced(0)
        self._FriendSecret__cleanupFirstPage()
        self.ignoreAll()
        self.hide()
        return None

    
    def _FriendSecret__getSecret(self):
        if not (toonbase.tcr.friendManager):
            self.notify.warning('No FriendManager available.')
            self.exit()
            return None
        
        self._FriendSecret__cleanupFirstPage()
        self.nextText['text'] = Localizer.FriendSecretGettingSecret
        self.nextText.setPos(0, 0, 0.29999999999999999)
        self.nextText.show()
        self.ok1.hide()
        self.cancel.show()
        self.accept('requestSecretResponse', self._FriendSecret__gotSecret)
        toonbase.tcr.friendManager.up_requestSecret()

    
    def _FriendSecret__gotSecret(self, result, secret):
        self.ignore('requestSecretResponse')
        if result == 1:
            self.nextText['text'] = Localizer.FriendSecretGotSecret
            self.nextText.setPos(0, 0, 0.37)
            self.secretText['text'] = secret
        else:
            self.nextText['text'] = Localizer.FriendSecretTooMany
        self.nextText.show()
        self.secretText.show()
        self.cancel.hide()
        self.ok1.hide()
        self.ok2.show()

    
    def _FriendSecret__enterSecret(self, secret):
        self.enterSecret.set('')
        secret = string.strip(secret)
        if not secret:
            self.exit()
            return None
        
        if not (toonbase.tcr.friendManager):
            self.notify.warning('No FriendManager available.')
            self.exit()
            return None
        
        self._FriendSecret__cleanupFirstPage()
        self.nextText['text'] = Localizer.FriendSecretTryingSecret
        self.nextText.setPos(0, 0, 0.29999999999999999)
        self.nextText.show()
        self.ok1.hide()
        self.cancel.show()
        self.accept('submitSecretResponse', self._FriendSecret__enteredSecret)
        toonbase.tcr.friendManager.up_submitSecret(secret)

    
    def _FriendSecret__enteredSecret(self, result, avId):
        self.ignore('submitSecretResponse')
        if result == 1:
            handle = toonbase.tcr.identifyAvatar(avId)
            if handle != None:
                self.nextText['text'] = Localizer.FriendSecretEnteredSecretSuccess % handle.getName()
            else:
                self.accept('friendsMapComplete', self._FriendSecret__nowFriends, [
                    avId])
                ready = toonbase.tcr.fillUpFriendsMap()
                if ready:
                    self._FriendSecret__nowFriends(avId)
                
                return None
        elif result == 0:
            self.nextText['text'] = Localizer.FriendSecretEnteredSecretUnknown
        elif result == 2:
            handle = toonbase.tcr.identifyAvatar(avId)
            if handle != None:
                self.nextText['text'] = Localizer.FriendSecretEnteredSecretFull % handle.getName()
            else:
                self.nextText['text'] = Localizer.FriendSecretEnteredSecretFullNoName
        elif result == 3:
            self.nextText['text'] = Localizer.FriendSecretEnteredSecretSelf
        
        self.nextText.show()
        self.cancel.hide()
        self.ok1.hide()
        self.ok2.show()

    
    def _FriendSecret__nowFriends(self, avId):
        self.ignore('friendsMapComplete')
        handle = toonbase.tcr.identifyAvatar(avId)
        if handle != None:
            self.nextText['text'] = Localizer.FriendSecretNowFriends % handle.getName()
        else:
            self.nextText['text'] = Localizer.FriendSecretNowFriendsNoName
        self.nextText.show()
        self.cancel.hide()
        self.ok1.hide()
        self.ok2.show()

    
    def _FriendSecret__ok1(self):
        secret = self.enterSecret.get()
        self._FriendSecret__enterSecret(secret)

    
    def _FriendSecret__ok2(self):
        self.exit()

    
    def _FriendSecret__cancel(self):
        self.exit()

    
    def _FriendSecret__cleanupFirstPage(self):
        self.introText.hide()
        self.getSecret.hide()
        self.enterSecretText.hide()
        self.enterSecret.hide()
        chatEntry = toonbase.localToon.chatMgr.chatInputNormal.chatEntry
        chatEntry['backgroundFocus'] = self.oldFocus


