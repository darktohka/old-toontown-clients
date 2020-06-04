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
import SpeedChat
import SCColorScheme
import SCStaticTextTerminal
speedChatStyles = ((2000, (200 / 255.0, 60 / 255.0, 229 / 255.0), (200 / 255.0, 135 / 255.0, 255 / 255.0), (220 / 255.0, 195 / 255.0, 229 / 255.0)), (2001, (0 / 255.0, 0 / 255.0, 255 / 255.0), (140 / 255.0, 150 / 255.0, 235 / 255.0), (201 / 255.0, 215 / 255.0, 255 / 255.0)), (2002, (90 / 255.0, 175 / 255.0, 225 / 255.0), (120 / 255.0, 215 / 255.0, 255 / 255.0), (208 / 255.0, 230 / 255.0, 250 / 255.0)), (2003, (130 / 255.0, 235 / 255.0, 235 / 255.0), (120 / 255.0, 225 / 255.0, 225 / 255.0), (234 / 255.0, 255 / 255.0, 255 / 255.0)), (2004, (0 / 255.0, 200 / 255.0, 70 / 255.0), (0 / 255.0, 200 / 255.0, 80 / 255.0), (204 / 255.0, 255 / 255.0, 204 / 255.0)), (2005, (235 / 255.0, 230 / 255.0, 0 / 255.0), (255 / 255.0, 250 / 255.0, 100 / 255.0), (255 / 255.0, 250 / 255.0, 204 / 255.0)), (2006, (255 / 255.0, 153 / 255.0, 0 / 255.0), (229 / 255.0, 147 / 255.0, 0 / 255.0), (255 / 255.0, 234 / 255.0, 204 / 255.0)), (2007, (255 / 255.0, 0 / 255.0, 50 / 255.0), (229 / 255.0, 0 / 255.0, 50 / 255.0), (255 / 255.0, 204 / 255.0, 204 / 255.0)), (2008, (255 / 255.0, 153 / 255.0, 193 / 255.0), (240 / 255.0, 157 / 255.0, 192 / 255.0), (255 / 255.0, 215 / 255.0, 238 / 255.0)), (2009, (170 / 255.0, 120 / 255.0, 20 / 255.0), (165 / 255.0, 120 / 255.0, 50 / 255.0), (210 / 255.0, 200 / 255.0, 180 / 255.0)))

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
        self.displaySettingsApiChanged = 0
        guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
        gui = loader.loadModelOnce('phase_3.5/models/gui/friendslist_gui')
        titleHeight = 0.60999999999999999
        textStartHeight = 0.45000000000000001
        textRowHeight = 0.14999999999999999
        leftMargin = -0.71999999999999997
        buttonbase_ycoord = 0.45000000000000001
        buttonbase_xcoord = 0.34999999999999998
        button_image_scale = (0.69999999999999996, 1, 1)
        button_textpos = (0, -0.02)
        options_text_scale = 0.051999999999999998
        disabled_arrow_color = Vec4(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 1.0)
        self.speed_chat_scale = 0.055
        self.title = DirectLabel(parent = self, relief = None, text = Localizer.OptionsPageTitle, text_scale = 0.12, textMayChange = 0, pos = (0, 0, titleHeight))
        self.Music_Label = DirectLabel(parent = self, relief = None, text = '', text_align = TextNode.ALeft, text_scale = options_text_scale, pos = (leftMargin, 0, textStartHeight))
        self.SoundFX_Label = DirectLabel(parent = self, relief = None, text = '', text_align = TextNode.ALeft, text_scale = options_text_scale, text_wordwrap = 16, pos = (leftMargin, 0, textStartHeight - textRowHeight))
        self.Friends_Label = DirectLabel(parent = self, relief = None, text = '', text_align = TextNode.ALeft, text_scale = options_text_scale, text_wordwrap = 16, pos = (leftMargin, 0, textStartHeight - 2 * textRowHeight))
        self.DisplaySettings_Label = DirectLabel(parent = self, relief = None, text = '', text_align = TextNode.ALeft, text_scale = options_text_scale, text_wordwrap = 10, pos = (leftMargin, 0, textStartHeight - 3 * textRowHeight))
        self.SpeedChatStyle_Label = DirectLabel(parent = self, relief = None, text = Localizer.OptionsPageSpeedChatStyleLabel, text_align = TextNode.ALeft, text_scale = options_text_scale, text_wordwrap = 10, pos = (leftMargin, 0, textStartHeight - 4 * textRowHeight))
        self.Music_toggleButton = DirectButton(parent = self, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = button_image_scale, text = '', text_scale = options_text_scale, text_pos = button_textpos, pos = (buttonbase_xcoord, 0.0, buttonbase_ycoord), command = self._OptionsPage__doToggleMusic)
        self.SoundFX_toggleButton = DirectButton(parent = self, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = button_image_scale, text = '', text_scale = options_text_scale, text_pos = button_textpos, pos = (buttonbase_xcoord, 0.0, buttonbase_ycoord - textRowHeight), command = self._OptionsPage__doToggleSfx)
        self.Friends_toggleButton = DirectButton(parent = self, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = button_image_scale, text = '', text_scale = options_text_scale, text_pos = button_textpos, pos = (buttonbase_xcoord, 0.0, buttonbase_ycoord - textRowHeight * 2), command = self._OptionsPage__doToggleAcceptFriends)
        self.DisplaySettingsButton = DirectButton(parent = self, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = button_image_scale, text = Localizer.OptionsPageChange, text_scale = options_text_scale, text_pos = button_textpos, pos = (buttonbase_xcoord, 0.0, buttonbase_ycoord - textRowHeight * 3), command = self._OptionsPage__doDisplaySettings)
        self.speedChatStyleLeftArrow = DirectButton(parent = self, relief = None, image = (gui.find('**/Horiz_Arrow_UP'), gui.find('**/Horiz_Arrow_DN'), gui.find('**/Horiz_Arrow_Rllvr'), gui.find('**/Horiz_Arrow_UP')), image3_color = Vec4(1, 1, 1, 0.5), scale = (-1.0, 1.0, 1.0), pos = (0.25, 0, buttonbase_ycoord - textRowHeight * 4), command = self._OptionsPage__doSpeedChatStyleLeft)
        self.speedChatStyleRightArrow = DirectButton(parent = self, relief = None, image = (gui.find('**/Horiz_Arrow_UP'), gui.find('**/Horiz_Arrow_DN'), gui.find('**/Horiz_Arrow_Rllvr'), gui.find('**/Horiz_Arrow_UP')), image3_color = Vec4(1, 1, 1, 0.5), pos = (0.65000000000000002, 0, buttonbase_ycoord - textRowHeight * 4), command = self._OptionsPage__doSpeedChatStyleRight)
        self.speedChatStyleText = SpeedChat.SpeedChat(name = 'OptionsPageStyleText', structure = [
            2000])
        self.speedChatStyleText.setScale(self.speed_chat_scale)
        self.speedChatStyleText.setPos(0.37, 0, -0.12)
        self.speedChatStyleText.reparentTo(self, FOREGROUND_SORT_INDEX)
        if not toonbase.tcr.isPaid() and toonbase.tcr.productName == 'DisneyOnline-US':
            self.purchaseButton = DirectButton(parent = self, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = 1.1499999999999999, text = Localizer.OptionsPagePurchase, text_scale = options_text_scale, text_pos = button_textpos, textMayChange = 0, pos = (0.45000000000000001, 0, -0.37), command = self._OptionsPage__handlePurchase)
        
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

    
    def _OptionsPage__doneDisplaySettings(self, anyChanged, apiChanged):
        if anyChanged:
            self._OptionsPage__setDisplaySettings()
            properties = base.win.getProperties()
            self.displaySettingsChanged = 1
            self.displaySettingsSize = (properties.getXSize(), properties.getYSize())
            self.displaySettingsFullscreen = properties.getFullscreen()
            self.displaySettingsApi = base.pipe.getInterfaceName()
            self.displaySettingsApiChanged = apiChanged
        

    
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

    
    def _OptionsPage__doSpeedChatStyleLeft(self):
        if self.speedChatStyleIndex > 0:
            self.speedChatStyleIndex = self.speedChatStyleIndex - 1
            self.updateSpeedChatStyle()
        

    
    def _OptionsPage__doSpeedChatStyleRight(self):
        if self.speedChatStyleIndex < len(speedChatStyles) - 1:
            self.speedChatStyleIndex = self.speedChatStyleIndex + 1
            self.updateSpeedChatStyle()
        

    
    def updateSpeedChatStyle(self):
        (nameKey, arrowColor, rolloverColor, frameColor) = speedChatStyles[self.speedChatStyleIndex]
        newSCColorScheme = SCColorScheme.SCColorScheme(arrowColor = arrowColor, rolloverColor = rolloverColor, frameColor = frameColor)
        self.speedChatStyleText.setColorScheme(newSCColorScheme)
        self.speedChatStyleText.clearMenu()
        colorName = SCStaticTextTerminal.SCStaticTextTerminal(nameKey)
        self.speedChatStyleText.append(colorName)
        self.speedChatStyleText.finalize()
        self.speedChatStyleText.setPos(0.44500000000000001 - self.speedChatStyleText.getWidth() * self.speed_chat_scale / 2, 0, -0.12)
        if self.speedChatStyleIndex > 0:
            self.speedChatStyleLeftArrow['state'] = NORMAL
        else:
            self.speedChatStyleLeftArrow['state'] = DISABLED
        if self.speedChatStyleIndex < len(speedChatStyles) - 1:
            self.speedChatStyleRightArrow['state'] = NORMAL
        else:
            self.speedChatStyleRightArrow['state'] = DISABLED
        toonbase.localToon.b_setSpeedChatStyleIndex(self.speedChatStyleIndex)

    
    def enter(self):
        ShtikerPage.ShtikerPage.enter(self)
        taskMgr.remove(self.DisplaySettingsTaskName)
        self.settingsChanged = 0
        self._OptionsPage__setMusicButton()
        self._OptionsPage__setSoundFXButton()
        self._OptionsPage__setAcceptFriendsButton()
        self._OptionsPage__setDisplaySettings()
        self.speedChatStyleText.enter()
        self.speedChatStyleIndex = toonbase.localToon.getSpeedChatStyleIndex()
        self.updateSpeedChatStyle()
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
        
        self.speedChatStyleText.exit()
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
        if self.displaySettingsApiChanged:
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
        del self.SpeedChatStyle_Label
        del self.SoundFX_toggleButton
        del self.Music_toggleButton
        del self.Friends_toggleButton
        del self.speedChatStyleLeftArrow
        del self.speedChatStyleRightArrow
        self.speedChatStyleText.exit()
        self.speedChatStyleText.destroy()
        del self.speedChatStyleText
        self.currentSizeIndex = None
        ShtikerPage.ShtikerPage.unload(self)

    
    def _OptionsPage__handlePurchase(self):
        if toonbase.tcr.isWebPlayToken():
            if toonbase.tcr.isPaid() and launcher and not launcher.getParentPasswordSet():
                self.paidNoParentPassword = 1
            else:
                self.paidNoParentPassword = 0
            self.leaveToPayDialog = LeaveToPayDialog.LeaveToPayDialog(self.paidNoParentPassword)
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
        


