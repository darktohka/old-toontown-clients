# File: M (Python 2.2)

from DirectGui import *
from DateOfBirthEntry import *
from MultiPageTextFrame import *
from ToontownGlobals import *
import Localizer
import ToontownDialog
import FSM
import State
import TTAccount

class MemberAgreementScreen(DirectObject):
    
    def __init__(self, tcr, doneEvent):
        self.doneEvent = doneEvent
        self.tcr = tcr
        self.loginInterface = self.tcr.loginInterface
        self.legalText = Localizer.MemberAgreementScreenLegalText
        self.numPages = len(self.legalText)
        self.checkAge = config.GetBool('check-member-agreement-age', 0)
        self.fsm = FSM.FSM('MemberAgreementScreen', [
            State.State('off', self.enterOff, self.exitOff, [
                'getParents']),
            State.State('getParents', self.enterGetParents, self.exitGetParents, [
                'viewAgreement']),
            State.State('viewAgreement', self.enterViewAgreement, self.exitViewAgreement, [
                'youMustAgree']),
            State.State('youMustAgree', self.enterYouMustAgree, self.exitYouMustAgree, [
                'viewAgreement'])], 'off', 'off')
        self.fsm.enterInitialState()

    
    def load(self):
        guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
        background = loader.loadModel('phase_3/models/gui/login-background')
        cogIcons = loader.loadModel('phase_3/models/gui/cog_icons')
        self.frame = DirectFrame(parent = aspect2d, relief = FLAT, image = background.find('**/member_agreement'))
        self.welcomeLabel = DirectLabel(parent = self.frame, relief = None, pos = (0, 0, 0.88), text = Localizer.MemberAgreementScreenWelcome, text_font = getMinnieFont(), text_scale = 0.0935, text_fg = (1, 0.5, 0.10000000000000001, 1), text_shadow = (0, 0, 0, 1), text_shadowOffset = (0.080000000000000002, 0.080000000000000002))
        self.onYourWayLabel = DirectLabel(parent = self.frame, relief = None, pos = (0, 0, 0.79000000000000004), text = Localizer.MemberAgreementScreenOnYourWay, text_scale = 0.072499999999999995, text_fg = (1, 1, 0, 1), text_shadow = (0, 0, 0, 1), text_shadowOffset = (0.080000000000000002, 0.080000000000000002))
        self.toontownLabel = DirectLabel(parent = self.frame, relief = None, pos = (0, 0, 0.67000000000000004), text = Localizer.MemberAgreementScreenToontown, text_font = getMinnieFont(), text_scale = 0.086999999999999994, text_fg = (1, 0.5, 0.10000000000000001, 1), text_shadow = (0, 0, 0, 1), text_shadowOffset = (0.080000000000000002, 0.080000000000000002))
        priceColor = (0, 0.90000000000000002, 0, 1)
        if self.tcr.getCreditCardUpFront():
            priceTextScale = 0.089999999999999997
            self.pricingLabel = DirectLabel(parent = self.frame, relief = None, pos = (0, 0, 0.55800000000000005), text = Localizer.MemberAgreementScreenCCUpFrontPricing, text_scale = priceTextScale, text_fg = (1, 1, 0, 1), text_shadow = (0, 0, 0, 1), text_shadowOffset = (0.080000000000000002, 0.080000000000000002))
            self.freeTrialDuration = DirectLabel(parent = self.pricingLabel, relief = None, pos = (-0.35999999999999999, 0, 0), text = self.tcr.accountServerConstants.getString('freeTrialPeriodInDays'), text_scale = priceTextScale, text_fg = priceColor, text_shadow = (0, 0, 0, 1), text_shadowOffset = (0.080000000000000002, 0.080000000000000002))
            priceFirstMonthPos = (0.92000000000000004, 0, -0.17999999999999999)
            pricePerMonthPos = (-0.11, 0, -0.27000000000000002)
        else:
            priceTextScale = 0.10000000000000001
            self.pricingLabel = DirectLabel(parent = self.frame, relief = None, pos = (0, 0, 0.55800000000000005), text = Localizer.MemberAgreementScreenPricing, text_scale = priceTextScale, text_fg = (1, 1, 0, 1), text_shadow = (0, 0, 0, 1), text_shadowOffset = (0.080000000000000002, 0.080000000000000002))
            priceFirstMonthPos = (0.52000000000000002, 0, 0)
            pricePerMonthPos = (0.84999999999999998, 0, -0.10000000000000001)
        self.priceFirstMonth = DirectLabel(parent = self.pricingLabel, relief = None, pos = priceFirstMonthPos, text = '$%s' % self.tcr.accountServerConstants.getString('priceFirstMonth'), text_scale = priceTextScale, text_fg = priceColor, text_shadow = (0, 0, 0, 1), text_shadowOffset = (0.080000000000000002, 0.080000000000000002))
        self.pricePerMonth = DirectLabel(parent = self.pricingLabel, relief = None, pos = pricePerMonthPos, text = '$%s' % self.tcr.accountServerConstants.getString('pricePerMonth'), text_scale = priceTextScale, text_fg = priceColor, text_shadow = (0, 0, 0, 1), text_shadowOffset = (0.080000000000000002, 0.080000000000000002))
        self.dobEntry = DateOfBirthEntry(parent = self.frame, pos = (0, 0, 0.26000000000000001), scale = 0.095000000000000001, defaultAge = 0, curYear = self.tcr.dateObject.getYear())
        if not (self.checkAge):
            self.dobEntry.hide()
        
        self.memAgreement = MultiPageTextFrame(parent = self.frame, relief = None, textList = self.legalText, hidePageNum = 1, width = 1.8, height = 0.90000000000000002, wordWrap = 34, pos = (0, 0, -0.29999999999999999))
        self.cogIcon = DirectLabel(parent = self.memAgreement, relief = None, pos = (-0.75, 0, 0.29999999999999999), scale = 0.25, image = cogIcons.find('**/LegalIcon'))
        self.agreementTitle = DirectLabel(parent = self.memAgreement, relief = None, pos = (0.042651300000000003, 0, 0.26879399999999998), scale = 0.089999999999999997, text = Localizer.MemberAgreementScreenAgreementTitle, text_font = getSuitFont(), text_wordwrap = 10)
        self.clickNextLabel = DirectLabel(parent = self.memAgreement, relief = None, pos = (-0.32528299999999999, 0, -0.38825700000000002), scale = 0.050000000000000003, text = Localizer.MemberAgreementScreenClickNext)
        self.memAgreement.setPageChangeCallback(self._MemberAgreementScreen__handlePageChange)
        bottomButtonZ = -0.56999999999999995
        self.cancelButton = DirectButton(parent = self.memAgreement, relief = None, scale = 1.1000000000000001, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (1, 1, 1), pos = (-0.5, 0, bottomButtonZ), text = Localizer.MemberAgreementScreenCancel, text_scale = 0.059999999999999998, text_pos = (0, -0.017999999999999999), command = self._MemberAgreementScreen__handleCancel)
        self.declineButton = DirectButton(parent = self.memAgreement, relief = None, scale = 1.1000000000000001, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (1, 1, 1), pos = (0, 0, bottomButtonZ), text = Localizer.MemberAgreementScreenDisagree, text_scale = 0.059999999999999998, text_pos = (0, -0.017999999999999999), command = self._MemberAgreementScreen__handleDisagree)
        self.acceptButton = DirectButton(parent = self.memAgreement, relief = None, scale = 1.1000000000000001, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (1, 1, 1), pos = (0.5, 0, bottomButtonZ), text = Localizer.MemberAgreementScreenAgree, text_scale = 0.059999999999999998, text_pos = (0, -0.017999999999999999), command = self._MemberAgreementScreen__handleAgree)
        self.dialogDoneEvent = 'memberAgreementDialogAck'
        self.dialog = ToontownDialog.GlobalDialog(doneEvent = self.dialogDoneEvent, message = '', style = ToontownDialog.Acknowledge)
        self.dialog.hide()
        self.mustAgreeDialog = DirectFrame(relief = None, pos = (0, 0.10000000000000001, 0), image = getDefaultDialogGeom(), image_color = GlobalDialogColor, image_scale = (1.3, 1.0, 0.80000000000000004), text = Localizer.MemberAgreementScreenYouMustAgree, text_scale = 0.080000000000000002, text_pos = (0.0, 0.20000000000000001), text_wordwrap = 15, sortOrder = NO_FADE_SORT_INDEX)
        self.mustAgreeDialog.hide()
        linePos = -0.13
        buttonImageScale = 1.1000000000000001
        buttonLineHeight = 0.112
        self.mustAgreeOkButton = DirectButton(parent = self.mustAgreeDialog, relief = None, pos = (0, 0, linePos), scale = 0.90000000000000002, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = buttonImageScale, text = Localizer.MemberAgreementScreenYouMustAgreeOk, text_scale = 0.059999999999999998, text_pos = (0, -0.02), command = self._MemberAgreementScreen__handleMustAgreeOk)
        linePos -= buttonLineHeight
        self.mustAgreeQuitButton = DirectButton(parent = self.mustAgreeDialog, relief = None, pos = (0, 0, linePos), scale = 0.90000000000000002, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = buttonImageScale, image0_color = Vec4(1, 0.10000000000000001, 0.10000000000000001, 1), image1_color = Vec4(1, 0.10000000000000001, 0.10000000000000001, 1), image2_color = Vec4(1, 1, 1, 1), text = Localizer.MemberAgreementScreenYouMustAgreeQuit, text_scale = 0.059999999999999998, text_pos = (0, -0.02), command = self._MemberAgreementScreen__handleMustAgreeQuit)
        linePos -= buttonLineHeight
        self.frame.hide()
        background.removeNode()
        guiButton.removeNode()
        cogIcons.removeNode()

    
    def unload(self):
        self.mustAgreeDialog.destroy()
        self.frame.destroy()
        self.dialog.cleanup()
        del self.frame
        del self.dialog
        del self.fsm

    
    def enter(self):
        self.frame.show()
        
        def getDOBfromEntry(self = self):
            self.dobMonth = self.dobEntry.getMonth()
            self.dobYear = self.dobEntry.getYear()
            self.dobDay = self.dobEntry.getDay()

        if self.tcr.getCreditCardUpFront():
            getDOBfromEntry()
        else:
            
            try:
                error = self.loginInterface.getAccountData(self.tcr.userName, self.tcr.password)
            except TTAccount.TTAccountException:
                error = 'exception raised'

            if not error:
                accountData = self.loginInterface.accountData
                if accountData.hasKey('dobMonth') and accountData.hasKey('dobYear'):
                    pass
                if not accountData.hasKey('dobDay'):
                    error = 1
                
            
            if error:
                getDOBfromEntry()
            else:
                
                try:
                    self.dobMonth = accountData.getInt('dobMonth')
                    self.dobYear = accountData.getInt('dobYear')
                    self.dobDay = accountData.getInt('dobDay')
                except ValueError:
                    getDOBfromEntry()

                if self.checkAge:
                    self.dobEntry.setMonth(self.dobMonth)
                    self.dobEntry.setYear(self.dobYear)
                    self.dobEntry.setDay(self.dobDay)
                
        self.age = toonbase.tcr.dateObject.getAge(self.dobMonth, self.dobYear, self.dobDay)
        self.fsm.request('getParents')

    
    def exit(self):
        self.fsm.requestFinalState()
        self.frame.hide()

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterGetParents(self):
        if self.tcr.getCreditCardUpFront() or self.age < 18:
            if self.tcr.getCreditCardUpFront():
                msg = Localizer.MemberAgreementScreenGetParentsUnconditional
            else:
                msg = Localizer.MemberAgreementScreenGetParents
            self.dialog.setMessage(msg)
            self.dialog.show()
            
            def handleGetParentsAck(self = self):
                self.dialog.hide()
                self.fsm.request('viewAgreement')

            self.acceptOnce(self.dialogDoneEvent, handleGetParentsAck)
        else:
            self.fsm.request('viewAgreement')

    
    def exitGetParents(self):
        pass

    
    def enterViewAgreement(self):
        self.memAgreement.acceptAgreementKeypresses()

    
    def exitViewAgreement(self):
        self.memAgreement.ignoreAgreementKeypresses()

    
    def enterYouMustAgree(self):
        base.transitions.fadeScreen(0.5)
        self.mustAgreeDialog.show()

    
    def _MemberAgreementScreen__handleMustAgreeOk(self):
        self.fsm.request('viewAgreement')

    
    def _MemberAgreementScreen__handleMustAgreeQuit(self):
        messenger.send(self.doneEvent, [
            {
                'mode': 'quit' }])

    
    def exitYouMustAgree(self):
        base.transitions.noTransitions()
        self.mustAgreeDialog.hide()

    
    def _MemberAgreementScreen__handleAgree(self):
        if self.checkAge:
            age = self.dobEntry.getAge()
            if age < 18:
                self.dialog.setMessage(Localizer.MemberAgreementScreenMustBeOlder)
                self.dialog.show()
                
                def handleOlderAck(self = self):
                    self.dialog.hide()
                    self.fsm.request('viewAgreement')

                self.acceptOnce(self.dialogDoneEvent, handleOlderAck)
                self.memAgreement.ignoreAgreementKeypresses()
            else:
                messenger.send(self.doneEvent, [
                    {
                        'mode': 'agree' }])
        else:
            messenger.send(self.doneEvent, [
                {
                    'mode': 'agree' }])

    
    def _MemberAgreementScreen__handleDisagree(self):
        self.fsm.request('youMustAgree')

    
    def _MemberAgreementScreen__handleCancel(self):
        messenger.send(self.doneEvent, [
            {
                'mode': 'cancel' }])

    
    def _MemberAgreementScreen__handlePageChange(self, pageNum):
        if pageNum == 0:
            self.cogIcon.show()
            self.agreementTitle.show()
            self.clickNextLabel.show()
        else:
            self.cogIcon.hide()
            self.agreementTitle.hide()
            self.clickNextLabel.hide()


