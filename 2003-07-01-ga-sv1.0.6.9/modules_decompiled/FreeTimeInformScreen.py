# File: F (Python 2.2)

from ShowBaseGlobal import *
from ToontownGlobals import *
from ToontownMsgTypes import *
from DirectGui import *
from TaskManagerGlobal import *
import OnscreenText
import StateData
import ToontownDialog
import FSM
import State
import DirectNotifyGlobal
import Task
import Localizer
import TTAccount
import GuiScreen
import math

class FreeTimeInformScreen(StateData.StateData, GuiScreen.GuiScreen):
    notify = DirectNotifyGlobal.directNotify.newCategory('FreeTimeInformScreen')
    
    def __init__(self, tcr, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        GuiScreen.GuiScreen.__init__(self)
        self.tcr = tcr
        self.fsm = FSM.FSM('FreeTimeInformScreen', [
            State.State('off', self.enterOff, self.exitOff, [
                'inform']),
            State.State('inform', self.enterInform, self.exitInform, [])], 'off', 'off')
        self.fsm.enterInitialState()

    
    def load(self):
        masterScale = 0.80000000000000004
        textScale = 0.10000000000000001 * masterScale
        entryScale = 0.080000000000000002 * masterScale
        lineHeight = 0.20999999999999999 * masterScale
        buttonScale = 2.0 * masterScale
        buttonLineHeight = 0.31 * masterScale
        background = loader.loadModel('phase_3/models/gui/login-background')
        guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
        self.frame = DirectFrame(parent = aspect2d, relief = FLAT, image = background.find('**/free_time_expired'), image_scale = (1, 1, 1))
        self.frame.hide()
        freeTimeExpired = self.tcr.isFreeTimeExpired()
        if not freeTimeExpired:
            (daysLeft, hoursLeft) = self._FreeTimeInformScreen__getTimeLeft()
            daysLeftInt = int(math.ceil(daysLeft))
            if daysLeftInt >= 2:
                notice = Localizer.FreeTimeInformScreenNDaysLeft % daysLeftInt
            elif hoursLeft >= 12:
                notice = Localizer.FreeTimeInformScreenOneDayLeft
            elif hoursLeft >= 2:
                notice = Localizer.FreeTimeInformScreenNHoursLeft % hoursLeft
            elif hoursLeft == 1:
                notice = Localizer.FreeTimeInformScreenOneHourLeft
            else:
                notice = Localizer.FreeTimeInformScreenLessThanOneHourLeft
            freeTimeLabelPos = 0.62
            freeTimeLabelText = notice
            freeTimeLabelTextScale = 0.12
            linePos = 0.23000000000000001
            self.freeButton = DirectButton(parent = self.frame, relief = None, pos = (0, 0, linePos), scale = buttonScale, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR'), guiButton.find('**/QuitBtn_UP')), image_color = (1, 1, 1, 1), text = Localizer.FreeTimeInformScreenFreePlay, text_scale = 0.059999999999999998, text_pos = (0, -0.02), image_scale = (1.3, 1.1000000000000001, 1.1000000000000001), command = self._FreeTimeInformScreen__handlePlayFreeButton)
            linePos = -0.10000000000000001
            self.sentence2Label = DirectLabel(parent = self.frame, relief = None, pos = (0, 0, linePos), text = Localizer.FreeTimeInformScreenSecondSentence, text_scale = 0.11, text_fg = (1, 1, 0, 1), text_shadow = (0, 0, 0, 1), text_shadowOffset = (0.080000000000000002, 0.080000000000000002))
            joinButtonPos = -0.41999999999999998
            quitButtonPos = joinButtonPos - buttonLineHeight * 1.3999999999999999
        else:
            freeTimeLabelPos = 0.5
            if self.tcr.getCreditCardUpFront():
                freeTimeLabelText = Localizer.FreeTimeInformScreenExpiredCCUF
                joinButtonPos = 0.059999999999999998
            else:
                freeTimeLabelText = Localizer.FreeTimeInformScreenExpired
                joinButtonPos = 0.13500000000000001
            freeTimeLabelTextScale = 0.089999999999999997
            if self.tcr.getCreditCardUpFront():
                quitLabelPos = -0.28000000000000003
                quitLabelText = Localizer.FreeTimeInformScreenExpiredQuitCCUFText
                quitButtonPos = -0.64000000000000001
            else:
                quitLabelPos = -0.27000000000000002
                quitLabelText = Localizer.FreeTimeInformScreenExpiredQuitText
                quitButtonPos = -0.71999999999999997
            self.freeTimeQuitLabel = DirectLabel(parent = self.frame, relief = None, pos = (0, 0, quitLabelPos), text = quitLabelText, text_scale = 0.089999999999999997, text_fg = (1, 1, 0, 1), text_shadow = (0, 0, 0, 1), text_shadowOffset = (0.080000000000000002, 0.080000000000000002))
        linePos = freeTimeLabelPos
        self.freeTimeLabel = DirectLabel(parent = self.frame, relief = None, pos = (0, 0, linePos), text = freeTimeLabelText, text_scale = freeTimeLabelTextScale, text_fg = (1, 1, 0, 1), text_shadow = (0, 0, 0, 1), text_shadowOffset = (0.080000000000000002, 0.080000000000000002))
        if freeTimeExpired and not self.tcr.getCreditCardUpFront():
            self.oopsLabel = DirectLabel(parent = self.freeTimeLabel, relief = None, pos = (-0.53000000000000003, 0, 0), scale = 1.3600000000000001, text = Localizer.FreeTimeInformScreenOops, text_font = getMinnieFont(), text_scale = freeTimeLabelTextScale, text_fg = (1, 0.5, 0.10000000000000001, 1), text_shadow = (0, 0, 0, 1), text_shadowOffset = (0.080000000000000002, 0.080000000000000002))
        
        linePos = joinButtonPos
        self.joinButton = DirectButton(parent = self.frame, relief = None, pos = (0, 0, linePos), scale = buttonScale, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), text = Localizer.FreeTimeInformScreenPurchase, text_scale = 0.059999999999999998, text_pos = (0, -0.02), image_scale = (1.3, 1.1000000000000001, 1.1000000000000001), command = self._FreeTimeInformScreen__handleJoinButton)
        linePos = quitButtonPos
        self.quitButton = DirectButton(parent = self.frame, relief = None, pos = (0, 0, linePos), scale = buttonScale, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image0_color = Vec4(1, 0.10000000000000001, 0.10000000000000001, 1), image1_color = Vec4(1, 0.10000000000000001, 0.10000000000000001, 1), image2_color = Vec4(1, 1, 1, 1), text = Localizer.FreeTimeInformScreenQuit, text_scale = 0.059999999999999998, text_pos = (0, -0.02), image_scale = (1.3, 1.1000000000000001, 1.1000000000000001), command = self._FreeTimeInformScreen__handleQuitButton)
        background.removeNode()
        guiButton.removeNode()

    
    def unload(self):
        self.frame.destroy()
        del self.frame
        del self.fsm

    
    def enter(self):
        self.fsm.request('inform')

    
    def exit(self):
        self.fsm.requestFinalState()

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterInform(self):
        self.frame.show()

    
    def exitInform(self):
        self.frame.hide()

    
    def _FreeTimeInformScreen__getTimeLeft(self):
        secsLeft = self.tcr.freeTimeLeft()
        hourSecs = 60 * 60
        daySecs = 24 * hourSecs
        return (float(secsLeft) / daySecs, int(secsLeft / hourSecs))

    
    def _FreeTimeInformScreen__handleJoinButton(self):
        messenger.send(self.doneEvent, [
            {
                'mode': 'join' }])

    
    def _FreeTimeInformScreen__handlePlayFreeButton(self):
        messenger.send(self.doneEvent, [
            {
                'mode': 'free' }])

    
    def _FreeTimeInformScreen__handleQuitButton(self):
        messenger.send(self.doneEvent, [
            {
                'mode': 'quit' }])


