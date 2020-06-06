# File: A (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase import ToontownGlobals
from direct.showbase import PandaObject
from toontown.toon import ToonDNA
from toontown.toon import ToonHead
from toontown.toontowngui import TTDialog
from direct.gui.DirectGui import *
from toontown.toonbase import TTLocalizer
from direct.directnotify import DirectNotifyGlobal
from toontown.toontowngui import TeaserPanel

class AvatarChoice(DirectButton):
    notify = DirectNotifyGlobal.directNotify.newCategory('AvatarChoice')
    TRIALER_OPEN_POS = 1
    MODE_CREATE = 0
    MODE_CHOOSE = 1
    MODE_LOCKED = 2
    
    def __init__(self, av = None, position = 0, paid = 0, okToLockout = 1):
        DirectButton.__init__(self, relief = None, text = '', text_font = ToontownGlobals.getSignFont())
        self.initialiseoptions(AvatarChoice)
        self.hasPaid = paid
        self.mode = None
        if base.restrictTrialers and okToLockout:
            if position != AvatarChoice.TRIALER_OPEN_POS:
                if not (self.hasPaid):
                    self.mode = AvatarChoice.MODE_LOCKED
                    self.name = ''
                    self.dna = None
                
            
        
        if self.mode is not AvatarChoice.MODE_LOCKED:
            if not av:
                print 'MODE_CREATE'
                self.mode = AvatarChoice.MODE_CREATE
                self.name = ''
                self.dna = None
            else:
                self.mode = AvatarChoice.MODE_CHOOSE
                self.name = av.name
                self.dna = ToonDNA.ToonDNA(av.dna)
                self.wantName = av.wantName
                self.approvedName = av.approvedName
                self.rejectedName = av.rejectedName
                self.allowedName = av.allowedName
        
        self.position = position
        self.doneEvent = 'avChoicePanel-' + str(self.position)
        self.deleteWithPasswordFrame = None
        self.pickAToonGui = loader.loadModelOnce('phase_3/models/gui/pick_a_toon_gui')
        self['image'] = self.pickAToonGui.find('**/av-chooser_Square_UP')
        self.setScale(1.01)
        if self.mode is AvatarChoice.MODE_LOCKED:
            self['command'] = self._AvatarChoice__handleTrialer
            self['text'] = TTLocalizer.AvatarChoiceSubscribersOnly
            self['text0_scale'] = 0.10000000000000001
            self['text1_scale'] = 0.115
            self['text2_scale'] = 0.115
            self['text0_fg'] = (0, 1, 0.80000000000000004, 0.0)
            self['text1_fg'] = (0, 1, 0.80000000000000004, 1)
            self['text2_fg'] = (0.29999999999999999, 1, 0.90000000000000002, 1)
            self['text_pos'] = (0, 0.19)
            logoModel = loader.loadModelOnce('phase_3/models/gui/members_only_gui')
            logo = DirectFrame(parent = self, relief = None, image = logoModel.find('**/MembersOnly'), image_scale = (0.4375, 0, 0.375), image_pos = (0, 0, 0))
            logo.reparentTo(self.stateNodePath[0], 20)
            logo.instanceTo(self.stateNodePath[1], 20)
            logo.instanceTo(self.stateNodePath[2], 20)
            logoModel.removeNode()
        elif self.mode is AvatarChoice.MODE_CREATE:
            print 'MODE_CREATE 2'
            self['command'] = self._AvatarChoice__handleCreate
            self['text'] = (TTLocalizer.AvatarChoiceMakeAToon,)
            self['text_pos'] = (0, 0)
            self['text0_scale'] = 0.10000000000000001
            self['text1_scale'] = 0.12
            self['text2_scale'] = 0.12
            self['text0_fg'] = (0, 1, 0.80000000000000004, 0.5)
            self['text1_fg'] = (0, 1, 0.80000000000000004, 1)
            self['text2_fg'] = (0.29999999999999999, 1, 0.90000000000000002, 1)
        else:
            self['command'] = self._AvatarChoice__handleChoice
            self['text'] = ('', TTLocalizer.AvatarChoicePlayThisToon, TTLocalizer.AvatarChoicePlayThisToon)
            self['text_scale'] = 0.12
            self['text_fg'] = (1, 0.90000000000000002, 0.10000000000000001, 1)
            self.nameText = DirectLabel(parent = self, relief = None, scale = 0.089999999999999997, pos = (0, 0, 0.27000000000000002), text = self.name, text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), text_wordwrap = 7.5, text_font = ToontownGlobals.getToonFont(), state = DISABLED)
            if self.approvedName != '':
                self.nameText['text'] = self.approvedName
            
            guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
            self.nameYourToonButton = DirectButton(parent = self, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), text = (TTLocalizer.AvatarChoiceNameYourToon, TTLocalizer.AvatarChoiceNameYourToon, TTLocalizer.AvatarChoiceNameYourToon), text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), text_scale = 0.14999999999999999, text_pos = (0, 0.029999999999999999), text_font = ToontownGlobals.getInterfaceFont(), pos = (-0.20000000000000001, 0, -0.29999999999999999), scale = 0.45000000000000001, image_scale = (2, 1, 3), command = self._AvatarChoice__handleNameYourToon)
            guiButton.removeNode()
            self.statusText = DirectLabel(parent = self, relief = None, scale = 0.089999999999999997, pos = (0, 0, -0.23999999999999999), text = '', text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), text_wordwrap = 7.5, text_font = ToontownGlobals.getToonFont(), state = DISABLED)
            if self.wantName != '':
                self.nameYourToonButton.hide()
                self.statusText['text'] = TTLocalizer.AvatarChoiceNameReview
            elif self.approvedName != '':
                self.nameYourToonButton.hide()
                self.statusText['text'] = TTLocalizer.AvatarChoiceNameApproved
            elif self.rejectedName != '':
                self.nameYourToonButton.hide()
                self.statusText['text'] = TTLocalizer.AvatarChoiceNameRejected
            elif self.allowedName == 1 and base.cr.allowFreeNames() or self.hasPaid:
                self.nameYourToonButton.show()
                self.statusText['text'] = ''
            else:
                self.nameYourToonButton.hide()
                self.statusText['text'] = ''
            self.head = hidden.attachNewNode('head')
            self.head.setPosHprScale(0, 5, -0.10000000000000001, 180, 0, 0, 0.23999999999999999, 0.23999999999999999, 0.23999999999999999)
            self.head.reparentTo(self.stateNodePath[0], 20)
            self.head.instanceTo(self.stateNodePath[1], 20)
            self.head.instanceTo(self.stateNodePath[2], 20)
            self.headModel = ToonHead.ToonHead()
            self.headModel.setupHead(self.dna, forGui = 1)
            self.headModel.reparentTo(self.head)
            animalStyle = self.dna.getAnimal()
            bodyScale = ToontownGlobals.toonBodyScales[animalStyle]
            self.headModel.setScale(bodyScale / 0.75)
            self.headModel.startBlink()
            self.headModel.startLookAround()
            trashcanGui = loader.loadModelOnce('phase_3/models/gui/trashcan_gui')
            self.deleteButton = DirectButton(parent = self, image = (trashcanGui.find('**/TrashCan_CLSD'), trashcanGui.find('**/TrashCan_OPEN'), trashcanGui.find('**/TrashCan_RLVR')), text = ('', TTLocalizer.AvatarChoiceDelete, TTLocalizer.AvatarChoiceDelete), text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), text_scale = 0.14999999999999999, text_pos = (0, -0.10000000000000001), text_font = ToontownGlobals.getInterfaceFont(), relief = None, pos = (0.27000000000000002, 0, -0.25), scale = 0.45000000000000001, command = self._AvatarChoice__handleDelete)
            trashcanGui.removeNode()
        self.resetFrameSize()

    
    def destroy(self):
        loader.unloadModel('phase_3/models/gui/pick_a_toon_gui')
        self.pickAToonGui.removeNode()
        del self.pickAToonGui
        del self.dna
        if self.mode in (AvatarChoice.MODE_CREATE, AvatarChoice.MODE_LOCKED):
            pass
        1
        self.headModel.stopBlink()
        self.headModel.stopLookAroundNow()
        self.headModel.delete()
        self.head.removeNode()
        del self.head
        del self.headModel
        del self.nameText
        del self.statusText
        del self.deleteButton
        del self.nameYourToonButton
        loader.unloadModel('phase_3/models/gui/trashcan_gui')
        loader.unloadModel('phase_3/models/gui/quit_button')
        DirectFrame.destroy(self)
        if self.deleteWithPasswordFrame:
            self.deleteWithPasswordFrame.destroy()
        

    
    def _AvatarChoice__handleChoice(self):
        cleanupDialog('globalDialog')
        messenger.send(self.doneEvent, [
            'chose',
            self.position])

    
    def _AvatarChoice__handleCreate(self):
        cleanupDialog('globalDialog')
        messenger.send(self.doneEvent, [
            'create',
            self.position])

    
    def _AvatarChoice__handleDelete(self):
        cleanupDialog('globalDialog')
        self.verify = TTDialog.TTGlobalDialog(doneEvent = 'verifyDone', message = TTLocalizer.AvatarChoiceDeleteConfirm % self.name, style = TTDialog.TwoChoice)
        self.verify.show()
        self.accept('verifyDone', self._AvatarChoice__handleVerifyDelete)

    
    def _AvatarChoice__handleNameYourToon(self):
        messenger.send(self.doneEvent, [
            'nameIt',
            self.position])

    
    def _AvatarChoice__handleVerifyDelete(self):
        status = self.verify.doneStatus
        self.ignore('verifyDone')
        self.verify.cleanup()
        del self.verify
        if status == 'ok':
            self.verifyDeleteWithPassword()
        

    
    def verifyDeleteWithPassword(self):
        tt = base.cr.loginInterface
        if tt.supportsAuthenticateDelete() and base.cr.productName != 'DisneyOnline-UK':
            self.deleteWithPassword = 1
            deleteText = TTLocalizer.AvatarChoiceDeletePasswordText % self.name
        else:
            self.deleteWithPassword = 0
            deleteText = TTLocalizer.AvatarChoiceDeleteConfirmText % {
                'name': self.name,
                'confirm': TTLocalizer.AvatarChoiceDeleteConfirmUserTypes }
        if self.deleteWithPasswordFrame == None:
            buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
            nameBalloon = loader.loadModel('phase_3/models/props/chatbox_input')
            okButtonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
            cancelButtonImage = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr'))
            self.deleteWithPasswordFrame = DirectFrame(pos = (0.0, 0.10000000000000001, 0.20000000000000001), relief = None, image = getDefaultDialogGeom(), image_color = ToontownGlobals.GlobalDialogColor, image_scale = (1.3999999999999999, 1.0, 1.0), text = deleteText, text_wordwrap = 19, text_scale = 0.059999999999999998, text_pos = (0, 0.25), textMayChange = 1, sortOrder = NO_FADE_SORT_INDEX)
            if self.deleteWithPassword:
                self.passwordLabel = DirectLabel(parent = self.deleteWithPasswordFrame, relief = None, pos = (-0.070000000000000007, 0.0, -0.20000000000000001), text = TTLocalizer.AvatarChoicePassword, text_scale = 0.080000000000000002, text_align = TextNode.ARight, textMayChange = 0)
                self.passwordEntry = DirectEntry(parent = self.deleteWithPasswordFrame, relief = None, image = nameBalloon, image1_color = (0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1.0), scale = 0.064000000000000001, pos = (0.0, 0.0, -0.20000000000000001), width = ToontownGlobals.maxLoginWidth, numLines = 1, focus = 1, cursorKeys = 1, obscured = 1, command = self._AvatarChoice__handleDeleteWithPasswordOK)
                DirectButton(parent = self.deleteWithPasswordFrame, image = okButtonImage, relief = None, text = TTLocalizer.AvatarChoiceDeletePasswordOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (-0.22, 0.0, -0.34999999999999998), command = self._AvatarChoice__handleDeleteWithPasswordOK)
            else:
                self.passwordEntry = DirectEntry(parent = self.deleteWithPasswordFrame, relief = None, image = nameBalloon, image1_color = (0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1.0), scale = 0.064000000000000001, pos = (-0.29999999999999999, 0.0, -0.20000000000000001), width = 10, numLines = 1, focus = 1, cursorKeys = 1, command = self._AvatarChoice__handleDeleteWithConfirmOK)
                DirectButton(parent = self.deleteWithPasswordFrame, image = okButtonImage, relief = None, text = TTLocalizer.AvatarChoiceDeletePasswordOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (-0.22, 0.0, -0.34999999999999998), command = self._AvatarChoice__handleDeleteWithConfirmOK)
            DirectLabel(parent = self.deleteWithPasswordFrame, relief = None, pos = (0, 0, 0.34999999999999998), text = TTLocalizer.AvatarChoiceDeletePasswordTitle, textMayChange = 0, text_scale = 0.080000000000000002)
            DirectButton(parent = self.deleteWithPasswordFrame, image = cancelButtonImage, relief = None, text = TTLocalizer.AvatarChoiceDeletePasswordCancel, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 1, pos = (0.20000000000000001, 0.0, -0.34999999999999998), command = self._AvatarChoice__handleDeleteWithPasswordCancel)
            buttons.removeNode()
            nameBalloon.removeNode()
        else:
            self.deleteWithPasswordFrame['text'] = deleteText
            self.passwordEntry['focus'] = 1
            self.passwordEntry.enterText('')
        base.transitions.fadeScreen(0.5)
        self.deleteWithPasswordFrame.show()

    
    def _AvatarChoice__handleDeleteWithPasswordOK(self, *args):
        password = self.passwordEntry.get()
        tt = base.cr.loginInterface
        (okFlag, errorMsg) = tt.authenticateDelete(base.cr.userName, password)
        if okFlag:
            self.deleteWithPasswordFrame.hide()
            base.transitions.noTransitions()
            messenger.send(self.doneEvent, [
                'delete',
                self.position])
        elif errorMsg is not None:
            self.notify.warning('authenticateDelete returned unexpected error: %s' % errorMsg)
        
        self.deleteWithPasswordFrame['text'] = TTLocalizer.AvatarChoiceDeleteWrongPassword
        self.passwordEntry['focus'] = 1
        self.passwordEntry.enterText('')

    
    def _AvatarChoice__handleDeleteWithConfirmOK(self, *args):
        password = self.passwordEntry.get()
        passwordMatch = TTLocalizer.AvatarChoiceDeleteConfirmUserTypes
        password = TextEncoder.lower(password)
        passwordMatch = TextEncoder.lower(passwordMatch)
        if password == passwordMatch:
            self.deleteWithPasswordFrame.hide()
            base.transitions.noTransitions()
            messenger.send(self.doneEvent, [
                'delete',
                self.position])
        else:
            self.deleteWithPasswordFrame['text'] = TTLocalizer.AvatarChoiceDeleteWrongConfirm % {
                'name': self.name,
                'confirm': TTLocalizer.AvatarChoiceDeleteConfirmUserTypes }
            self.passwordEntry['focus'] = 1
            self.passwordEntry.enterText('')

    
    def _AvatarChoice__handleDeleteWithPasswordCancel(self):
        self.deleteWithPasswordFrame.hide()
        base.transitions.noTransitions()

    
    def _AvatarChoice__handleTrialer(self):
        TeaserPanel.TeaserPanel(pageName = 'sixToons')


