# File: O (Python 2.2)

from ShowBaseGlobal import *
import ShtikerPage
import ToontownDialog
from DirectGui import *
import ToontownDialog
import Localizer
import DisplaySettingsDialog
import LeaveToPayDialog
import Task

class OptionsPage(ShtikerPage.ShtikerPage):
    DisplaySettingsTaskName = 'save-display-settings'
    DisplaySettingsDelay = 60
    ChangeDisplaySettings = base.config.GetBool('change-display-settings', 1)
    DisplaySettingsApiMap = {
        'OpenGL': Settings.GL,
        'DirectX7': Settings.DX7,
        'DirectX8': Settings.DX8 }
    
    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.currentSizeIndex = None

    
    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        self.displaySettings = None
        self.displaySettingsChanged = 0
        self.displaySettingsSize = (None, None)
        self.displaySettingsFullscreen = None
        self.displaySettingsApi = None
        guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
        gui = loader.loadModelOnce('phase_3.5/models/gui/friendslist_gui')
        topMargin = 0.48999999999999999
        textRowHeight = 0.14430000000000001
        leftMargin = -0.71999999999999997
        buttonbase_ycoord = 0.504
        buttonbase_xcoord = 0.45000000000000001
        button_image_scale = (0.69999999999999996, 1, 1)
        button_textpos = (0, -0.02)
        options_text_scale = 0.051999999999999998
        disabled_arrow_color = Vec4(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 1.0)
        self.title = DirectLabel(parent = self, relief = None, text = Localizer.OptionsPageTitle, text_scale = 0.12, textMayChange = 0, pos = (0, 0, 0.59999999999999998))
        self.Music_Label = DirectLabel(parent = self, relief = None, text = '', text_align = TextNode.ALeft, text_scale = options_text_scale, pos = (leftMargin, 0, topMargin - textRowHeight))
        self.SoundFX_Label = DirectLabel(parent = self, relief = None, text = '', text_align = TextNode.ALeft, text_scale = options_text_scale, pos = (leftMargin, 0, topMargin - 2 * textRowHeight))
        self.Friends_Label = DirectLabel(parent = self, relief = None, text = '', text_align = TextNode.ALeft, text_scale = options_text_scale, text_wordwrap = 10, pos = (leftMargin, 0, (topMargin - 3 * textRowHeight) + 0.040000000000000001))
        self.DisplaySettings_Label = DirectLabel(parent = self, relief = None, text = '', text_align = TextNode.ALeft, text_scale = options_text_scale, text_wordwrap = 10, pos = (leftMargin, 0, (topMargin - 4 * textRowHeight) + 0.040000000000000001))
        self.Music_toggleButton = DirectButton(parent = self, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = button_image_scale, text = '', text_scale = options_text_scale, text_pos = button_textpos, pos = (buttonbase_xcoord, 0.0, buttonbase_ycoord - textRowHeight), command = self._OptionsPage__doToggleMusic)
        self.SoundFX_toggleButton = DirectButton(parent = self, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = button_image_scale, text = '', text_scale = options_text_scale, text_pos = button_textpos, pos = (buttonbase_xcoord, 0.0, buttonbase_ycoord - textRowHeight * 2), command = self._OptionsPage__doToggleSfx)
        self.Friends_toggleButton = DirectButton(parent = self, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = button_image_scale, text = '', text_scale = options_text_scale, text_pos = button_textpos, pos = (buttonbase_xcoord, 0.0, buttonbase_ycoord - textRowHeight * 3), command = self._OptionsPage__doToggleAcceptFriends)
        self.DisplaySettingsButton = DirectButton(parent = self, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = button_image_scale, text = Localizer.OptionsPageChange, text_scale = options_text_scale, text_pos = button_textpos, pos = (buttonbase_xcoord, 0.0, buttonbase_ycoord - textRowHeight * 4), command = self._OptionsPage__doDisplaySettings)
        if not toonbase.tcr.isPaid():
            self.purchaseButton = DirectButton(parent = self, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = 1.1499999999999999, text = Localizer.OptionsPagePurchase, text_scale = options_text_scale, text_pos = button_textpos, textMayChange = 0, pos = (0.45000000000000001, 0, -0.34999999999999998), command = self._OptionsPage__handlePurchase)
        
        self.exitButton = DirectButton(parent = self, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = 1.1499999999999999, text = Localizer.OptionsPageExitToontown, text_scale = options_text_scale, text_pos = button_textpos, textMayChange = 0, pos = (0.45000000000000001, 0, -0.59999999999999998), command = self._OptionsPage__handleExitShowWithConfirm)
        guiButton.removeNode()
        gui.removeNode()

    
    def _OptionsPage__doToggleMusic(self):
        messenger.send('wakeup')
        if base.musicActive:
            base.enableMusic(0)
            Settings.setMusic(0)
        else:
            base.enableMusic(1)
            Settings.setMusic(1)
        self.settingsChanged = 1
        self._OptionsPage__setMusicButton()

    
    def _OptionsPage__setMusicButton(self):
        if base.musicActive:
            self.Music_Label['text'] = Localizer.OptionsPageMusicOnLabel
            self.Music_toggleButton['text'] = Localizer.OptionsPageToggleOff
        else:
            self.Music_Label['text'] = Localizer.OptionsPageMusicOffLabel
            self.Music_toggleButton['text'] = Localizer.OptionsPageToggleOn

    
    def _OptionsPage__doToggleSfx(self):
        messenger.send('wakeup')
        if base.sfxActive:
            base.enableSoundEffects(0)
            Settings.setSfx(0)
        else:
            base.enableSoundEffects(1)
            Settings.setSfx(1)
        self.settingsChanged = 1
        self._OptionsPage__setSoundFXButton()

    
    def _OptionsPage__setSoundFXButton(self):
        if base.sfxActive:
            self.SoundFX_Label['text'] = Localizer.OptionsPageSFXOnLabel
            self.SoundFX_toggleButton['text'] = Localizer.OptionsPageToggleOff
        else:
            self.SoundFX_Label['text'] = Localizer.OptionsPageSFXOffLabel
            self.SoundFX_toggleButton['text'] = Localizer.OptionsPageToggleOn

    
    def _OptionsPage__doToggleAcceptFriends(self):
        messenger.send('wakeup')
        if toonbase.localToon.acceptingNewFriends:
            toonbase.localToon.acceptingNewFriends = 0
        else:
            toonbase.localToon.acceptingNewFriends = 1
        self._OptionsPage__setAcceptFriendsButton()

    
    def _OptionsPage__setAcceptFriendsButton(self):
        if toonbase.localToon.acceptingNewFriends:
            self.Friends_Label['text'] = Localizer.OptionsPageFriendsEnabledLabel
            self.Friends_toggleButton['text'] = Localizer.OptionsPageToggleOff
        else:
            self.Friends_Label['text'] = Localizer.OptionsPageFriendsDisabledLabel
            self.Friends_toggleButton['text'] = Localizer.OptionsPageToggleOn

    
    def _OptionsPage__doDisplaySettings(self):
        if self.displaySettings == None:
            self.displaySettings = DisplaySettingsDialog.DisplaySettingsDialog()
            self.displaySettings.load()
            self.accept(self.displaySettings.doneEvent, self._OptionsPage__doneDisplaySettings)
        
        self.displaySettings.enter(self.ChangeDisplaySettings)
        return None

    
    def _OptionsPage__doneDisplaySettings(self, anyChanged):
        if anyChanged:
            self._OptionsPage__setDisplaySettings()
            properties = base.win.getProperties()
            self.displaySettingsChanged = 1
            self.displaySettingsSize = (properties.getXSize(), properties.getYSize())
            self.displaySettingsFullscreen = properties.getFullscreen()
            self.displaySettingsApi = base.pipe.getInterfaceName()
        

    
    def _OptionsPage__setDisplaySettings(self):
        properties = base.win.getProperties()
        if properties.getFullscreen():
            screensize = '%s x %s' % (properties.getXSize(), properties.getYSize())
        else:
            screensize = Localizer.OptionsPageDisplayWindowed
        api = base.pipe.getInterfaceName()
        settings = {
            'screensize': screensize,
            'api': api }
        if self.ChangeDisplaySettings:
            text = Localizer.OptionsPageDisplaySettings % settings
        else:
            text = Localizer.OptionsPageDisplaySettingsNoApi % settings
        self.DisplaySettings_Label['text'] = text

    
    def enter(self):
        ShtikerPage.ShtikerPage.enter(self)
        taskMgr.remove(self.DisplaySettingsTaskName)
        self.settingsChanged = 0
        self._OptionsPage__setMusicButton()
        self._OptionsPage__setSoundFXButton()
        self._OptionsPage__setAcceptFriendsButton()
        self._OptionsPage__setDisplaySettings()
        if self.book.safeMode:
            self.exitButton.hide()
            if hasattr(self, 'purchaseButton'):
                self.purchaseButton.hide()
            
        else:
            self.exitButton.show()
            if hasattr(self, 'purchaseButton'):
                self.purchaseButton.show()
            

    
    def exit(self):
        if self.settingsChanged != 0:
            Settings.writeSettings()
        
        if self.displaySettingsChanged:
            taskMgr.doMethodLater(self.DisplaySettingsDelay, self.writeDisplaySettings, self.DisplaySettingsTaskName)
        
        ShtikerPage.ShtikerPage.exit(self)

    
    def writeDisplaySettings(self, task = None):
        if not (self.displaySettingsChanged):
            return None
        
        taskMgr.remove(self.DisplaySettingsTaskName)
        self.notify.info('writing new display settings %s, %s, %s to SettingsFile.' % (self.displaySettingsSize, self.displaySettingsFullscreen, self.displaySettingsApi))
        Settings.setResolutionDimensions(self.displaySettingsSize[0], self.displaySettingsSize[1])
        Settings.setWindowedMode(not (self.displaySettingsFullscreen))
        api = self.DisplaySettingsApiMap.get(self.displaySettingsApi)
        if api == None:
            self.notify.warning('Cannot save unknown display API: %s' % self.displaySettingsApi)
        else:
            Settings.setDisplayDriver(api)
        Settings.writeSettings()
        self.displaySettingsChanged = 0
        return Task.done

    
    def unload(self):
        self.writeDisplaySettings()
        taskMgr.remove(self.DisplaySettingsTaskName)
        if self.displaySettings != None:
            self.ignore(self.displaySettings.doneEvent)
            self.displaySettings.unload()
        
        self.displaySettings = None
        del self.title
        del self.exitButton
        del self.SoundFX_Label
        del self.Music_Label
        del self.Friends_Label
        del self.SoundFX_toggleButton
        del self.Music_toggleButton
        del self.Friends_toggleButton
        self.currentSizeIndex = None
        ShtikerPage.ShtikerPage.unload(self)

    
    def _OptionsPage__handlePurchase(self):
        if toonbase.tcr.isWebPlayToken():
            self.leaveToPayDialog = LeaveToPayDialog.LeaveToPayDialog()
            self.leaveToPayDialog.show()
        else:
            self.doneStatus = {
                'mode': 'exit',
                'exitTo': 'memberAgreement' }
            messenger.send(self.doneEvent)

    
    def _OptionsPage__handleExitShowWithConfirm(self):
        self.confirm = ToontownDialog.GlobalDialog(doneEvent = 'confirmDone', message = Localizer.OptionsPageExitConfirm, style = ToontownDialog.TwoChoice)
        self.confirm.show()
        self.doneStatus = {
            'mode': 'exit',
            'exitTo': 'waitForAvatarList' }
        self.accept('confirmDone', self._OptionsPage__handleConfirm)

    
    def _OptionsPage__handleConfirm(self):
        status = self.confirm.doneStatus
        self.ignore('confirmDone')
        self.confirm.cleanup()
        del self.confirm
        if status == 'ok':
            messenger.send(self.doneEvent)
        


