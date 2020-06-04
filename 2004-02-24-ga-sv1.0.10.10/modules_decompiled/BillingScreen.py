# File: B (Python 2.2)

from ShowBaseGlobal import *
from ToontownGlobals import *
from ToontownMsgTypes import *
from DirectGui import *
from MultiPageTextFrame import *
from TaskManagerGlobal import *
from PrivacyPolicyPanel import *
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
import InputCheck
import copy
import PythonUtil

class BillingScreen(StateData.StateData, GuiScreen.GuiScreen):
    notify = DirectNotifyGlobal.directNotify.newCategory('BillingScreen')
    preferVisa = config.GetBool('prefer-visa', 1)
    ActiveEntryColor = (1, 0.90000000000000002, 0.10000000000000001, 1)
    InactiveEntryColor = (0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1)
    DisabledEntryColor = (0.5, 0.5, 0.5, 0.5)
    EntryFrameColor = (ActiveEntryColor, InactiveEntryColor, DisabledEntryColor)
    labelFg = (0, 0, 0, 1)
    labelFgActive = (1, 0, 0, 1)
    months = [
        '01',
        '02',
        '03',
        '04',
        '05',
        '06',
        '07',
        '08',
        '09',
        '10',
        '11',
        '12']
    yearRange = 10
    handleControlFocus = 1
    attemptThreshold = 6
    showLegalBlurb = 0
    countryCodes = [
        'US',
        'CA',
        'AU',
        'UK',
        'AF',
        'AL',
        'DZ',
        'AS',
        'AD',
        'AO',
        'AI',
        'AQ',
        'AG',
        'AR',
        'AM',
        'AW',
        'AT',
        'AZ',
        'BS',
        'BH',
        'BD',
        'BB',
        'BY',
        'BE',
        'BZ',
        'BJ',
        'BM',
        'BT',
        'BO',
        'BA',
        'BW',
        'BV',
        'BR',
        'IO',
        'BN',
        'BG',
        'BF',
        'BI',
        'KH',
        'CM',
        'CV',
        'KY',
        'CF',
        'TD',
        'CL',
        'CN',
        'CX',
        'CC',
        'CO',
        'KM',
        'CG',
        'CK',
        'CR',
        'CI',
        'HR',
        'CU',
        'CY',
        'CZ',
        'CS',
        'DK',
        'DJ',
        'DM',
        'DO',
        'TP',
        'EC',
        'EG',
        'SV',
        'GQ',
        'ER',
        'EE',
        'ET',
        'FK',
        'FO',
        'FJ',
        'FI',
        'FR',
        'FX',
        'GF',
        'PF',
        'TF',
        'GA',
        'GM',
        'GE',
        'DE',
        'GH',
        'GI',
        'GB',
        'GR',
        'GL',
        'GD',
        'GP',
        'GU',
        'GT',
        'GN',
        'GW',
        'GY',
        'HT',
        'HM',
        'HN',
        'HK',
        'HU',
        'IS',
        'IN',
        'ID',
        'IR',
        'IQ',
        'IE',
        'IL',
        'IT',
        'JM',
        'JP',
        'JO',
        'KZ',
        'KE',
        'KI',
        'KP',
        'KR',
        'KW',
        'KG',
        'LA',
        'LV',
        'LB',
        'LS',
        'LR',
        'LY',
        'LI',
        'LT',
        'LU',
        'MO',
        'MK',
        'MG',
        'MW',
        'MY',
        'MV',
        'ML',
        'MT',
        'MH',
        'MQ',
        'MR',
        'MU',
        'YT',
        'MX',
        'FM',
        'MD',
        'MC',
        'MN',
        'MS',
        'MA',
        'MZ',
        'MM',
        'NA',
        'NR',
        'NP',
        'NL',
        'AN',
        'NT',
        'NC',
        'NZ',
        'NI',
        'NE',
        'NG',
        'NU',
        'NF',
        'MP',
        'NO',
        'OM',
        'PK',
        'PW',
        'PA',
        'PG',
        'PY',
        'PE',
        'PH',
        'PN',
        'PL',
        'PT',
        'PR',
        'QA',
        'RE',
        'RO',
        'RU',
        'RW',
        'GS',
        'KN',
        'LC',
        'VC',
        'WS',
        'SM',
        'ST',
        'SA',
        'SN',
        'SC',
        'SL',
        'SG',
        'SK',
        'SI',
        'Sb',
        'SO',
        'ZA',
        'ES',
        'LK',
        'SH',
        'PM',
        'SD',
        'SR',
        'SJ',
        'SZ',
        'SE',
        'CH',
        'SY',
        'TW',
        'TJ',
        'TZ',
        'TH',
        'TG',
        'TK',
        'TO',
        'TT',
        'TN',
        'TR',
        'TM',
        'TC',
        'TV',
        'UG',
        'UA',
        'AE',
        'UY',
        'UM',
        'SU',
        'UZ',
        'VU',
        'VA',
        'VE',
        'VN',
        'VG',
        'VI',
        'WF',
        'EH',
        'YE',
        'YU',
        'ZR',
        'ZM',
        'ZW']
    state50Codes = [
        'AL',
        'AK',
        'AR',
        'AZ',
        'CA',
        'CO',
        'CT',
        'DE',
        'FL',
        'GA',
        'HI',
        'IA',
        'ID',
        'IL',
        'IN',
        'KS',
        'KY',
        'LA',
        'MA',
        'MD',
        'ME',
        'MI',
        'MN',
        'MO',
        'MS',
        'MT',
        'NE',
        'NC',
        'ND',
        'NH',
        'NJ',
        'NM',
        'NV',
        'NY',
        'OH',
        'OK',
        'OR',
        'PA',
        'RI',
        'SC',
        'SD',
        'TN',
        'TX',
        'UT',
        'VA',
        'VT',
        'WA',
        'WI',
        'WV',
        'WY',
        'DC']
    territoryStateCodes = [
        'AS',
        'GU',
        'MP',
        'PR',
        'VI',
        'FPO',
        'APO',
        'MH',
        'PW',
        'FM']
    canadianProvinceCodes = [
        'AB',
        'BC',
        'MB',
        'NB',
        'NF',
        'NT',
        'NS',
        'ON',
        'PE',
        'QC',
        'SK',
        'YT']
    
    def __init__(self, tcr, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        GuiScreen.GuiScreen.__init__(self)
        self.tcr = tcr
        self.ttAccount = self.tcr.loginInterface
        self.fsm = FSM.FSM('BillingScreen', [
            State.State('off', self.enterOff, self.exitOff, [
                'create']),
            State.State('create', self.enterCreate, self.exitCreate, [
                'waitForLoginResponse',
                'create']),
            State.State('waitForLoginResponse', self.enterWaitForLoginResponse, self.exitWaitForLoginResponse, [
                'create'])], 'off', 'off')
        self.fsm.enterInitialState()

    
    def load(self):
        masterScale = 0.90000000000000002
        textScale = 0.10000000000000001 * masterScale
        entryScale = 0.080000000000000002 * masterScale
        lineHeight = 0.14999999999999999 * masterScale * 0.90000000000000002
        if self.showLegalBlurb:
            lineHeight *= 0.84999999999999998 / 0.94999999999999996
        
        buttonScale = 1.1499999999999999 * masterScale
        buttonLineHeight = 0.14000000000000001 * masterScale
        entryWidth = 15 * 0.75
        entryFrameSize = (-0.20000000000000001, entryWidth + 0.20000000000000001, -0.59999999999999998, 1.3)
        labelX = -0.17000000000000001
        entryX = -0.12
        scrolledListZOffset = 0.0050000000000000001
        background = loader.loadModel('phase_3/models/gui/login-background')
        guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
        cogIcons = loader.loadModel('phase_3/models/gui/cog_icons')
        gui = loader.loadModelOnce('phase_3/models/gui/nameshop_gui')
        loginGui = loader.loadModel('phase_3/models/gui/login_gui')
        self.frame = DirectFrame(parent = aspect2d, relief = FLAT, image = background.find('**/billing'))
        self.frame.hide()
        self.frame.stateNodePath[0].find('**/visa_logo').removeNode()
        self.visaLogo = DirectFrame(parent = self.frame, relief = FLAT, image = background.find('**/visa_logo'))
        self.visaLogo.setPos(0.48999999999999999, 0, -0.29499999999999998)
        self.visaLogo.setScale(0.51000000000000001)
        if self.preferVisa:
            self.visaLogo.show()
        else:
            self.visaLogo.hide()
        self.cogIcon = DirectLabel(parent = self.frame, relief = None, pos = (-1.1200000000000001, 0, 0.80000000000000004), scale = 0.20000000000000001, image = cogIcons.find('**/MoneyIcon'))
        linePos = 0.84999999999999998
        self.titleLabel = DirectLabel(parent = self.frame, relief = None, pos = (0, 0, linePos), text = Localizer.BillingScreenTitle, text_scale = textScale, text_font = getSuitFont(), text_fg = (0.10000000000000001, 0.20000000000000001, 0.10000000000000001, 1))
        linePos -= lineHeight
        self.accountNameLabel = DirectLabel(parent = self.frame, relief = None, pos = (labelX, 0, linePos), text = Localizer.BillingScreenAccountName, text_scale = textScale, text_align = TextNode.ARight, text_fg = self.labelFg)
        self.accountNameEntry = DirectLabel(parent = self.frame, relief = None, pos = (entryX - 0.01, 0, linePos), text = Localizer.BillingScreenAccountName, text_scale = textScale, text_align = TextNode.ALeft, text_fg = self.labelFg)
        linePos -= lineHeight
        scaleDown = 0.75
        oldValues = [
            textScale,
            entryScale,
            lineHeight,
            buttonScale,
            buttonLineHeight,
            entryWidth,
            entryFrameSize]
        textScale *= scaleDown * 1.1000000000000001
        entryScale *= scaleDown
        lineHeight *= scaleDown * 1.1000000000000001
        buttonScale *= scaleDown
        buttonLineHeight *= scaleDown
        entryWidth = self.ENTRY_WIDTH
        entryFrameSize = (-0.20000000000000001, entryWidth + 0.20000000000000001, -0.59999999999999998, 1.3)
        optionMenuScale = textScale
        self.emailLabel = DirectLabel(parent = self.frame, relief = None, pos = (labelX, 0, linePos), text = Localizer.BillingScreenEmail, text_scale = textScale, text_align = TextNode.ARight, text_fg = self.labelFg)
        self.emailEntry = DirectEntry(parent = self.frame, relief = SUNKEN, borderWidth = (0.10000000000000001, 0.10000000000000001), frameColor = self.EntryFrameColor, frameSize = entryFrameSize, scale = entryScale, pos = (entryX, 0.0, linePos), width = entryWidth, numLines = 1, focus = 0, cursorKeys = 1)
        self.emailEntry.label = self.emailLabel
        linePos -= lineHeight
        self.emailConfirmLabel = DirectLabel(parent = self.frame, relief = None, pos = (labelX, 0, linePos), text = Localizer.BillingScreenEmailConfirm, text_scale = textScale, text_align = TextNode.ARight, text_fg = self.labelFg)
        self.emailConfirmEntry = DirectEntry(parent = self.frame, relief = SUNKEN, borderWidth = (0.10000000000000001, 0.10000000000000001), frameColor = self.EntryFrameColor, frameSize = entryFrameSize, scale = entryScale, pos = (entryX, 0.0, linePos), width = entryWidth, numLines = 1, focus = 0, cursorKeys = 1)
        self.emailConfirmEntry.label = self.emailConfirmLabel
        linePos -= lineHeight
        self.address1Label = DirectLabel(parent = self.frame, relief = None, pos = (labelX, 0, linePos), text = Localizer.BillingScreenBillingAddress, text_scale = textScale, text_align = TextNode.ARight, text_fg = self.labelFg)
        self.address1Entry = DirectEntry(parent = self.frame, relief = SUNKEN, borderWidth = (0.10000000000000001, 0.10000000000000001), frameColor = self.EntryFrameColor, frameSize = entryFrameSize, scale = entryScale, pos = (entryX, 0.0, linePos), width = entryWidth, numLines = 1, focus = 0, cursorKeys = 1)
        self.address1Entry.label = self.address1Label
        linePos -= lineHeight
        self.address2Label = DirectLabel(parent = self.frame, relief = None, pos = (labelX, 0, linePos), text = Localizer.BillingScreenBillingAddress2, text_scale = textScale, text_align = TextNode.ARight, text_fg = self.labelFg)
        self.address2Entry = DirectEntry(parent = self.frame, relief = SUNKEN, borderWidth = (0.10000000000000001, 0.10000000000000001), frameColor = self.EntryFrameColor, frameSize = entryFrameSize, scale = entryScale, pos = (entryX, 0.0, linePos), width = entryWidth, numLines = 1, focus = 0, cursorKeys = 1)
        self.address2Entry.label = self.address2Label
        linePos -= lineHeight
        self.cityLabel = DirectLabel(parent = self.frame, relief = None, pos = (labelX, 0, linePos), text = Localizer.BillingScreenCity, text_scale = textScale, text_align = TextNode.ARight, text_fg = self.labelFg)
        self.cityEntry = DirectEntry(parent = self.frame, relief = SUNKEN, borderWidth = (0.10000000000000001, 0.10000000000000001), frameColor = self.EntryFrameColor, frameSize = entryFrameSize, scale = entryScale, pos = (entryX, 0.0, linePos), width = entryWidth, numLines = 1, focus = 0, cursorKeys = 1)
        self.cityEntry.label = self.cityLabel
        linePos -= lineHeight
        countryEntryHeightRatio = 0.25
        linePos -= lineHeight * countryEntryHeightRatio
        self.countryLabel = DirectLabel(parent = self.frame, relief = None, pos = (labelX, 0, linePos), text = Localizer.BillingScreenCountry, text_scale = textScale, text_align = TextNode.ARight, text_fg = self.labelFg)
        countries = map(lambda cCode: Localizer.BillingScreenCountryNames[cCode], self.countryCodes)
        iS = 14.0
        self.defaultCountryScale = 0.80000000000000004
        self.countryControl = DirectScrolledList(parent = self.frame, relief = None, items = countries, image = loginGui.find('**/cogCountryPanel'), image_scale = (iS * 1.3, iS, iS), image_pos = (0.65000000000000002, 0, 0.14999999999999999), scale = optionMenuScale, incButton_image = (loginGui.find('**/cogPanelArrowUp'), loginGui.find('**/cogPanelArrowDwn'), loginGui.find('**/cogPanelArrowRllvr'), loginGui.find('**/cogPanelArrowUp')), incButton_relief = None, incButton_scale = (18.247800000000002, 1, -15.09), incButton_pos = (5.2677300000000002, 0, -0.080101900000000004), incButton_image3_color = Vec4(0.5, 0.5, 0.5, 1), decButton_image = (loginGui.find('**/cogPanelArrowUp'), loginGui.find('**/cogPanelArrowDwn'), loginGui.find('**/cogPanelArrowRllvr'), loginGui.find('**/cogPanelArrowUp')), decButton_relief = None, decButton_scale = (18.247800000000002, 1, 15.09), decButton_pos = (5.2677300000000002, 0, 0.60346100000000003), decButton_image3_color = Vec4(0.5, 0.5, 0.5, 1), pos = (0.231214, 0.0, linePos + scrolledListZOffset), itemFrame_pos = (0, 0, 0), itemFrame_scale = self.defaultCountryScale, itemFrame_relief = None, itemFrame_textMayChange = 1)
        self.countryControl.label = self.countryLabel
        linePos -= lineHeight * countryEntryHeightRatio
        linePos -= lineHeight
        self.stateLabel = DirectLabel(parent = self.frame, relief = None, pos = (labelX, 0, linePos), text = Localizer.BillingScreenState, text_scale = textScale, text_align = TextNode.ARight, text_fg = self.labelFg)
        states = []
        self.stateName2Code = { }
        for stateCode in self.state50Codes:
            name = Localizer.BillingScreenStateNames[stateCode]
            states.append(name)
            self.stateName2Code[name] = stateCode
        
        states.sort()
        territories = []
        for stateCode in self.territoryStateCodes:
            name = Localizer.BillingScreenStateNames[stateCode]
            if type(name) == type(''):
                territories.append(name)
                self.stateName2Code[name] = stateCode
            else:
                territories.extend(name)
                for n in name:
                    self.stateName2Code[n] = stateCode
                
        
        territories.sort()
        states += territories
        self.stateCodes = []
        for state in states:
            self.stateCodes.append(self.stateName2Code[state])
        
        bS = 12.550000000000001
        itemFrameScale = 0.80000000000000004
        imagePos = (0.5, 0, 0.13)
        iS = 12
        hS = 1.5
        bX = 5.0527199999999999
        self.stateControl = DirectScrolledList(parent = self.frame, relief = None, items = states, image = loginGui.find('**/cogCountryPanel'), image_scale = (iS * hS, iS, iS), image_pos = imagePos, incButton_image = (loginGui.find('**/cogPanelArrowUp'), loginGui.find('**/cogPanelArrowDwn'), loginGui.find('**/cogPanelArrowRllvr'), loginGui.find('**/cogPanelArrowUp')), incButton_relief = None, incButton_scale = (bS * hS, bS, -bS), incButton_pos = (bX, 0, -0.068218799999999996), incButton_image3_color = Vec4(0.5, 0.5, 0.5, 1), decButton_image = (loginGui.find('**/cogPanelArrowUp'), loginGui.find('**/cogPanelArrowDwn'), loginGui.find('**/cogPanelArrowRllvr'), loginGui.find('**/cogPanelArrowUp')), decButton_relief = None, decButton_scale = (bS * hS, bS, bS), decButton_pos = (bX, 0, 0.52127999999999997), decButton_image3_color = Vec4(0.5, 0.5, 0.5, 1), pos = (0.208342, 0.0, linePos + scrolledListZOffset), scale = 0.068000000000000005, itemFrame_pos = (-0.110268, 0, 0), itemFrame_scale = itemFrameScale, itemFrame_relief = None)
        self.stateControl.label = self.stateLabel
        self.stateLabel.wrtReparentTo(self.stateControl)
        self.caProvinceLabel = DirectLabel(parent = self.frame, relief = None, pos = (labelX, 0, linePos), text = Localizer.BillingScreenCAProvince, text_scale = textScale, text_align = TextNode.ARight, text_fg = self.labelFg)
        bS = 12.550000000000001
        iS = 12.0
        self.defaultCAProvinceScale = 0.80000000000000004
        CA_provinces = map(lambda pCode: Localizer.BillingScreenCanadianProvinces[pCode], self.canadianProvinceCodes)
        self.caProvinceControl = DirectScrolledList(parent = self.frame, relief = None, items = CA_provinces, image = loginGui.find('**/cogCountryPanel'), image_scale = (iS * 1.3, iS, iS), image_pos = (0.5, 0, 0.13), incButton_image = (loginGui.find('**/cogPanelArrowUp'), loginGui.find('**/cogPanelArrowDwn'), loginGui.find('**/cogPanelArrowRllvr'), loginGui.find('**/cogPanelArrowUp')), incButton_relief = None, incButton_scale = (bS * 1.27, bS, -bS), incButton_pos = (4.4588400000000004, 0, -0.068218799999999996), incButton_image3_color = Vec4(0.5, 0.5, 0.5, 1), decButton_image = (loginGui.find('**/cogPanelArrowUp'), loginGui.find('**/cogPanelArrowDwn'), loginGui.find('**/cogPanelArrowRllvr'), loginGui.find('**/cogPanelArrowUp')), decButton_relief = None, decButton_scale = (bS * 1.27, bS, bS), decButton_pos = (4.4588400000000004, 0, 0.52127999999999997), decButton_image3_color = Vec4(0.5, 0.5, 0.5, 1), pos = (0.156309, 0.0, linePos + scrolledListZOffset), scale = 0.068000000000000005, itemFrame_pos = (0, 0, 0), itemFrame_scale = itemFrameScale, itemFrame_relief = None)
        self.caProvinceControl.label = self.caProvinceLabel
        self.caProvinceLabel.wrtReparentTo(self.caProvinceControl)
        self.provinceLabel = DirectLabel(parent = self.frame, relief = None, pos = (labelX, 0, linePos), text = Localizer.BillingScreenProvince, text_scale = textScale, text_align = TextNode.ARight, text_fg = self.labelFg)
        self.provinceEntry = DirectEntry(parent = self.frame, relief = SUNKEN, borderWidth = (0.10000000000000001, 0.10000000000000001), frameColor = self.EntryFrameColor, frameSize = entryFrameSize, scale = entryScale, pos = (entryX, 0.0, linePos), width = entryWidth, numLines = 1, focus = 0, cursorKeys = 1)
        self.provinceEntry.label = self.provinceLabel
        self.provinceLabel.wrtReparentTo(self.provinceEntry)
        linePos -= lineHeight
        self.zipCodeLabel = DirectLabel(parent = self.frame, relief = None, pos = (labelX, 0, linePos), text = Localizer.BillingScreenZipCode, text_scale = textScale, text_align = TextNode.ARight, text_fg = self.labelFg)
        self.postalCodeLabel = DirectLabel(parent = self.frame, relief = None, pos = (labelX, 0, linePos), text = Localizer.BillingScreenPostalCode, text_scale = textScale, text_align = TextNode.ARight, text_fg = self.labelFg)
        self.postalCodeLabel.hide()
        self.zipCodeEntry = DirectEntry(parent = self.frame, relief = SUNKEN, borderWidth = (0.10000000000000001, 0.10000000000000001), frameColor = self.EntryFrameColor, frameSize = entryFrameSize, scale = entryScale, pos = (entryX, 0.0, linePos), width = entryWidth, numLines = 1, focus = 0, cursorKeys = 1)
        self.zipCodeEntry.label = self.zipCodeLabel
        linePos -= lineHeight
        if self.showLegalBlurb:
            ccTypeControlHeightRatio = 0.10000000000000001
        else:
            ccTypeControlHeightRatio = 0
        linePos -= lineHeight * ccTypeControlHeightRatio
        self.ccTypeLabel = DirectLabel(parent = self.frame, relief = None, pos = (labelX, 0, linePos), text = Localizer.BillingScreenCreditCardType, text_scale = textScale, text_align = TextNode.ARight, text_fg = self.labelFg)
        iS = 13
        bS = 14
        bX = 3.8190400000000002
        self.ccTypeControl = DirectScrolledList(parent = self.frame, relief = None, items = [
            Localizer.BillingScreenCCTypeInitialText] + Localizer.BillingScreenCreditCardTypes, image = loginGui.find('**/cogCountryPanel'), image_scale = (iS, iS, iS), image_pos = (0.5, 0, 0.14999999999999999), scale = optionMenuScale, incButton_image = (loginGui.find('**/cogPanelArrowUp'), loginGui.find('**/cogPanelArrowDwn'), loginGui.find('**/cogPanelArrowRllvr'), loginGui.find('**/cogPanelArrowUp')), incButton_relief = None, incButton_scale = (bS, bS, -bS), incButton_pos = (bX, 0, -0.037134899999999998), incButton_image3_color = Vec4(0.5, 0.5, 0.5, 1), decButton_image = (loginGui.find('**/cogPanelArrowUp'), loginGui.find('**/cogPanelArrowDwn'), loginGui.find('**/cogPanelArrowRllvr'), loginGui.find('**/cogPanelArrowUp')), decButton_relief = None, decButton_scale = (bS, bS, bS), decButton_pos = (bX, 0, 0.60346100000000003), decButton_image3_color = Vec4(0.5, 0.5, 0.5, 1), pos = (0.12529399999999999, 0.0, linePos + scrolledListZOffset), itemFrame_pos = (0, 0, 0), itemFrame_scale = self.defaultCountryScale, itemFrame_relief = None, itemFrame_textMayChange = 1)
        self.ccTypeControl.label = self.ccTypeLabel
        self.removedCCTypePleaseChoose = 0
        if self.preferVisa:
            self.removedCCTypePleaseChoose = 1
            pleaseChoose = self.ccTypeControl['items'][0]
            self.ccTypeControl.removeItem(pleaseChoose)
            pleaseChoose.destroy()
            self.ccTypeControl.scrollTo(0)
        
        linePos -= lineHeight * ccTypeControlHeightRatio
        linePos -= lineHeight
        self.ccNumberLabel = DirectLabel(parent = self.frame, relief = None, pos = (labelX, 0, linePos), text = Localizer.BillingScreenCreditCardNumber, text_scale = textScale, text_align = TextNode.ARight, text_fg = self.labelFg)
        if self.showLegalBlurb:
            self.ccNumberLabel['text'] += '*'
        
        self.ccNumberEntry = DirectEntry(parent = self.frame, relief = SUNKEN, borderWidth = (0.10000000000000001, 0.10000000000000001), frameColor = self.EntryFrameColor, frameSize = entryFrameSize, width = entryWidth, scale = entryScale, pos = (entryX, 0.0, linePos), numLines = 1, focus = 0, cursorKeys = 1)
        self.ccNumberEntry.label = self.ccNumberLabel
        linePos -= lineHeight
        self.ccExpiresLabel = DirectLabel(parent = self.frame, relief = None, pos = (labelX, 0, linePos), text = Localizer.BillingScreenCreditCardExpires, text_scale = textScale, text_align = TextNode.ARight, text_fg = self.labelFg)
        bS = 12.550000000000001
        itemFrameScale = 0.80000000000000004
        imagePos = (0.5, 0, 0.13)
        imageScale = 12
        self.ccMonthControl = DirectScrolledList(parent = self.frame, relief = None, items = self.months, image = loginGui.find('**/cogMonthPanel'), image_scale = imageScale, image_pos = imagePos, incButton_image = (loginGui.find('**/cogPanelArrowUp'), loginGui.find('**/cogPanelArrowDwn'), loginGui.find('**/cogPanelArrowRllvr'), loginGui.find('**/cogPanelArrowUp')), incButton_relief = None, incButton_scale = (bS, bS, bS), incButton_pos = (1.3825700000000001, 0, 0.52127999999999997), incButton_image3_color = Vec4(0.5, 0.5, 0.5, 1), decButton_image = (loginGui.find('**/cogPanelArrowUp'), loginGui.find('**/cogPanelArrowDwn'), loginGui.find('**/cogPanelArrowRllvr'), loginGui.find('**/cogPanelArrowUp')), decButton_relief = None, decButton_scale = (bS, bS, -bS), decButton_pos = (1.3825700000000001, 0, -0.068218799999999996), decButton_image3_color = Vec4(0.5, 0.5, 0.5, 1), pos = (-0.062, 0.0, linePos + scrolledListZOffset), scale = 0.068000000000000005, itemFrame_pos = (0, 0, 0), itemFrame_scale = itemFrameScale, itemFrame_relief = None)
        self.ccMonthControl.label = self.ccExpiresLabel
        curYear = self.tcr.dateObject.getYear()
        years = range(curYear, curYear + self.yearRange + 1)
        years = map(str, years)
        self.ccYearControl = DirectScrolledList(parent = self.frame, relief = None, items = years, image = loginGui.find('**/cogYearPanel'), image_scale = imageScale, image_pos = imagePos, incButton_image = (loginGui.find('**/cogPanelArrowUp'), loginGui.find('**/cogPanelArrowDwn'), loginGui.find('**/cogPanelArrowRllvr'), loginGui.find('**/cogPanelArrowUp')), incButton_relief = None, incButton_scale = (bS, bS, bS), incButton_pos = (2.12466, 0, 0.52127999999999997), incButton_image3_color = Vec4(0.5, 0.5, 0.5, 1), decButton_image = (loginGui.find('**/cogPanelArrowUp'), loginGui.find('**/cogPanelArrowDwn'), loginGui.find('**/cogPanelArrowRllvr'), loginGui.find('**/cogPanelArrowUp')), decButton_relief = None, decButton_scale = (bS, bS, -bS), decButton_pos = (2.12466, 0, -0.068218799999999996), decButton_image3_color = Vec4(0.5, 0.5, 0.5, 1), pos = (0.21356700000000001, 0.0, linePos + scrolledListZOffset), scale = 0.068000000000000005, itemFrame_pos = (0, 0, 0), itemFrame_scale = itemFrameScale, itemFrame_relief = None)
        linePos -= lineHeight
        self.nameOnCardLabel = DirectLabel(parent = self.frame, relief = None, pos = (labelX, 0, linePos), text = Localizer.BillingScreenCreditCardName, text_scale = textScale, text_align = TextNode.ARight, text_fg = self.labelFg)
        self.nameOnCardEntry = DirectEntry(parent = self.frame, relief = SUNKEN, borderWidth = (0.10000000000000001, 0.10000000000000001), frameColor = self.EntryFrameColor, frameSize = entryFrameSize, scale = entryScale, pos = (entryX, 0.0, linePos), width = entryWidth, numLines = 1, focus = 0, cursorKeys = 1, command = self._BillingScreen__handleNameOnCard)
        self.nameOnCardEntry.label = self.nameOnCardLabel
        linePos -= lineHeight
        priceTextScale = 0.089999999999999997
        priceShadowOffset = (0.040000000000000001, 0.040000000000000001)
        self.pricingLabel = DirectLabel(parent = self.frame, relief = None, pos = (-0.11, 0, -0.65700000000000003), text = Localizer.BillingScreenPricing, text_scale = priceTextScale, text_align = TextNode.ACenter, text_fg = (0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 1), text_wordwrap = 42)
        priceColor = (0, 0.90000000000000002, 0, 1)
        self.priceFirstMonth = DirectLabel(parent = self.pricingLabel, relief = None, pos = (-0.84999999999999998, 0, 0), text = '$%s' % self.tcr.accountServerConstants.getString('priceFirstMonth'), text_scale = priceTextScale, text_fg = priceColor, text_shadow = (0, 0, 0, 1), text_shadowOffset = priceShadowOffset)
        self.pricePerMonth = DirectLabel(parent = self.pricingLabel, relief = None, pos = (0.45500000000000002, 0, 0), text = '$%s' % self.tcr.accountServerConstants.getString('pricePerMonth'), text_scale = priceTextScale, text_fg = priceColor, text_shadow = (0, 0, 0, 1), text_shadowOffset = priceShadowOffset)
        linePos -= lineHeight
        if self.showLegalBlurb:
            self.agreementLabel = DirectLabel(parent = self.frame, relief = None, pos = (-1.2, 0, linePos + lineHeight * 0.10000000000000001), text = Localizer.BillingScreenAgreementText, text_scale = 0.051999999999999998, text_align = TextNode.ALeft, text_fg = (0.10000000000000001, 0.20000000000000001, 0.10000000000000001, 1), text_wordwrap = 42)
            linePos -= lineHeight
        
        (textScale, entryScale, lineHeight, buttonScale, buttonLineHeight, entryWidth, entryFrameSize) = oldValues
        linePos = -0.80000000000000004
        self.submitButton = DirectButton(parent = self.frame, relief = None, pos = (0, 0, linePos), scale = buttonScale, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), text = Localizer.BillingScreenSubmit, text_scale = 0.059999999999999998, text_pos = (0, -0.02), image_scale = (1.3, 1.1000000000000001, 1.1000000000000001), command = self._BillingScreen__handleSubmit)
        linePos -= buttonLineHeight
        self.cancelButton = DirectButton(parent = self.frame, relief = None, pos = (0, 0, linePos), scale = buttonScale, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (1.3, 1.1000000000000001, 1.1000000000000001), image0_color = Vec4(1, 0.10000000000000001, 0.10000000000000001, 1), image1_color = Vec4(1, 0.10000000000000001, 0.10000000000000001, 1), image2_color = Vec4(1, 1, 1, 1), text = Localizer.BillingScreenCancel, text_scale = 0.059999999999999998, text_pos = (0, -0.02), command = self._BillingScreen__handleCancel)
        linePos -= buttonLineHeight
        self.dialogDoneEvent = 'accountDialogAck'
        self.dialog = ToontownDialog.GlobalDialog(dialogName = 'billingScreenDialog', doneEvent = self.dialogDoneEvent, message = '', style = ToontownDialog.Acknowledge)
        self.dialog.hide()
        self.whySafeDoneEvent = 'whySafeDialogAck'
        self.whySafeDialog = ToontownDialog.GlobalDialog(dialogName = 'whySafeDialog', okButtonText = Localizer.BillingScreenWhySafeClose, doneEvent = self.whySafeDoneEvent, style = ToontownDialog.Acknowledge, text = Localizer.BillingScreenWhySafeText, text_scale = 0.050000000000000003, text_wordwrap = 48, pos = (0, 0, 0.12), scale = 0.90000000000000002)
        self.whySafeDialog.hide()
        self.whySafeTitle = DirectLabel(parent = self.whySafeDialog, relief = None, pos = (-0.78000000000000003, 0, 0.70999999999999996), scale = 0.074999999999999997, text = Localizer.BillingScreenWhySafeTitle, text_font = getMinnieFont(), text_fg = (0, 0, 1, 1))
        self.whySafeCCGuarantee = DirectLabel(parent = self.whySafeDialog, relief = None, pos = (-0.60999999999999999, 0, 0.02), scale = 0.074999999999999997, text = Localizer.BillingScreenWhySafeCreditCardGuarantee, text_font = getMinnieFont(), text_fg = (1, 0.5, 0.10000000000000001, 1))
        self.whySafeJoin = DirectLabel(parent = self.whySafeDialog, relief = None, pos = (-0.81000000000000005, 0, -0.78000000000000003), scale = 0.074999999999999997, text = Localizer.BillingScreenWhySafeJoin, text_font = getMinnieFont(), text_fg = (1, 0, 0, 1))
        self.whySafeToontown = DirectLabel(parent = self.whySafeDialog, relief = None, pos = (0, 0, -0.78000000000000003), scale = 0.074999999999999997, text = Localizer.BillingScreenWhySafeToontown, text_font = getMinnieFont(), text_fg = (1, 0.5, 0.10000000000000001, 1))
        self.whySafeToday = DirectLabel(parent = self.whySafeDialog, relief = None, pos = (0.85999999999999999, 0, -0.78000000000000003), scale = 0.074999999999999997, text = Localizer.BillingScreenWhySafeToday, text_font = getMinnieFont(), text_fg = (1, 0, 0, 1))
        self.whySafeButton = DirectButton(parent = self.frame, relief = None, pos = (-1.1000000000000001, 0, -0.93999999999999995), image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (1, 0.80000000000000004, 0.80000000000000004), text = Localizer.BillingScreenWhySafe, text_pos = (0, -0.01), text_scale = 0.042000000000000003, command = self.showWhySafe)
        self.privacyPolicyButton = DirectButton(parent = self.frame, relief = None, pos = (1.1000000000000001, 0, -0.93999999999999995), scale = 1.1000000000000001, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (1, 0.80000000000000004, 0.80000000000000004), text = Localizer.BillingScreenPrivacyPolicy, text_pos = (0, -0.012), text_scale = 0.053999999999999999, command = self.showPrivacyPolicy)
        self.pleaseWaitDialog = DirectFrame(relief = None, image = getDefaultDialogGeom(), image_color = GlobalDialogColor, image_scale = (1, 1, 0.5), text = Localizer.BillingScreenPleaseWait, text_scale = 0.10000000000000001, text_pos = (0, -0.029999999999999999), sortOrder = NO_FADE_SORT_INDEX)
        self.pleaseWaitDialog.hide()
        guiButton.removeNode()
        background.removeNode()
        cogIcons.removeNode()
        loginGui.removeNode()

    
    def unload(self):
        self.dialog.cleanup()
        del self.dialog
        self.whySafeDialog.cleanup()
        del self.whySafeDialog
        self.pleaseWaitDialog.destroy()
        del self.pleaseWaitDialog
        self.frame.destroy()
        del self.frame
        del self.visaLogo
        del self.fsm

    
    def enter(self):
        self.frame.show()
        self.firstTime = 1
        self.attempts = 0
        self.fsm.request('create')

    
    def exit(self):
        self.frame.hide()
        self.ignore(self.dialogDoneEvent)
        self.fsm.requestFinalState()

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterCreate(self):
        if self.firstTime:
            
            try:
                error = self.ttAccount.getAccountData(self.tcr.userName, self.tcr.password)
            except TTAccount.TTAccountException:
                error = 'exception raised'

            self.email = ''
            if error:
                self.dobMonth = None
                self.dobYear = None
                self.dobDay = None
            else:
                accountData = self.ttAccount.accountData
                self.dobMonth = accountData.getInt('dobMonth')
                self.dobYear = accountData.getInt('dobYear')
                self.dobDay = accountData.getInt('dobDay')
                age = toonbase.tcr.dateObject.getAge(self.dobMonth, self.dobYear, self.dobDay)
                if age >= 18:
                    self.email = accountData.getString('email', '')
                
            self.address1 = ''
            self.address2 = ''
            self.city = ''
            self.countryCode = self.countryCodes[0]
            self.stateIndex = 0
            self.stateCode = self.stateCodes[self.stateIndex]
            self.caProvince = self.canadianProvinceCodes[0]
            self.province = ''
            self.zipCode = ''
            self.ccType = ''
            self.ccNumber = ''
            self.ccMonth = ''
            self.ccYear = ''
            self.nameOnCard = ''
        
        if hasattr(self, 'origInputs'):
            for fieldName in self.origInputs.keys():
                origValue = self.origInputs[fieldName]
                self.__dict__[fieldName] = origValue
            
            del self.origInputs
        
        self.accountNameEntry['text'] = self.tcr.userName
        self.emailEntry.enterText(self.email)
        if self.firstTime:
            self.emailConfirmEntry.enterText(self.email)
        
        self.address1Entry.enterText(self.address1)
        self.address2Entry.enterText(self.address2)
        self.cityEntry.enterText(self.city)
        self.countryControl.scrollTo(self.countryCodes.index(self.countryCode))
        if self.countryCode == 'US':
            self.stateControl.scrollTo(self.stateIndex)
        elif self.countryCode == 'CA':
            self.caProvinceControl.scrollTo(self.canadianProvinceCodes.index(self.caProvince))
        else:
            self.provinceEntry.enterText(self.province)
        self.zipCodeEntry.enterText(self.zipCode)
        self.ccNumberEntry.enterText(self.ccNumber)
        self.nameOnCardEntry.enterText(self.nameOnCard)
        self._BillingScreen__showStateOrProvince()
        self.countryControl['command'] = self._BillingScreen__handleCountry
        self.ccTypeControl['command'] = self._BillingScreen__handleCCType
        self.ccYearControl['command'] = self._BillingScreen__handleCCYear
        self.restartFocusMgmt()
        if self.firstTime and self.email != '':
            self.setFocus(2)
        elif hasattr(self, 'lastFocusIndex'):
            self.setFocus(self.lastFocusIndex)
            del self.lastFocusIndex
        
        self.firstTime = 0

    
    def exitCreate(self):
        self.lastFocusIndex = self.getFocusIndex()
        self.stopFocusMgmt()
        self.countryControl['command'] = None
        self.ccTypeControl['command'] = None
        self.ccYearControl['command'] = None

    
    def restartFocusMgmt(self):
        if self.focusMgmtActive():
            curFocusIndex = self.getFocusIndex()
        else:
            curFocusIndex = 0
        self.stopFocusMgmt()
        self.focusList = [
            self.emailEntry,
            self.emailConfirmEntry,
            self.address1Entry,
            self.address2Entry,
            self.cityEntry,
            'country',
            'stateProvince',
            self.zipCodeEntry,
            'ccType',
            self.ccNumberEntry,
            'ccExpDate',
            self.nameOnCardEntry]
        if not (self.handleControlFocus):
            i = 0
            while i < len(self.focusList):
                if type(self.focusList[i]) == type(''):
                    self.focusList.pop(i)
                else:
                    i += 1
        else:
            controls = {
                'country': self.countryControl,
                'stateProvince': None,
                'ccType': self.ccTypeControl,
                'ccExpDate': self.ccMonthControl }
            countryIndex = self.countryControl.getSelectedIndex()
            if countryIndex == self.countryCodes.index('US'):
                controls['stateProvince'] = self.stateControl
            elif countryIndex == self.countryCodes.index('CA'):
                controls['stateProvince'] = self.caProvinceControl
            else:
                controls['stateProvince'] = self.provinceEntry
            for tag in controls.keys():
                PythonUtil.replace(self.focusList, tag, controls[tag])
            
        self.startFocusMgmt(startFocus = curFocusIndex, overrides = {
            self.address2Entry: GuiScreen.GuiScreen.ENTERPRESS_ADVANCE,
            self.provinceEntry: GuiScreen.GuiScreen.ENTERPRESS_ADVANCE,
            self.ccTypeControl: self._BillingScreen__handleCCTypeEnterPress,
            self.nameOnCardEntry: GuiScreen.GuiScreen.ENTERPRESS_DONT_ADVANCE }, globalFocusHandler = self._BillingScreen__handleFocusChange)

    
    def enterWaitForLoginResponse(self):
        self.tcr.handler = self.handleWaitForLoginResponse
        
        try:
            
            try:
                base.transitions.fadeScreen(0.5)
                self.pleaseWaitDialog.show()
                toonbase.tcr.renderFrame()
                argDict = {
                    'email': self.email,
                    'ccType': self.ccType,
                    'ccNumber': self.ccNumber,
                    'ccMonth': self.ccMonth,
                    'ccYear': self.ccYear,
                    'nameOnCard': self.nameOnCard,
                    'addr1': self.address1,
                    'addr2': self.address2,
                    'city': self.city,
                    'country': self.countryCode,
                    'zip': self.zipCode }
                if self.countryCode == 'US':
                    argDict['state'] = self.stateCode
                elif self.countryCode == 'CA':
                    argDict['state'] = self.caProvince
                else:
                    argDict['state'] = self.province
                if self.dobMonth is not None:
                    argDict['dobMonth'] = self.dobMonth
                
                if self.dobYear is not None:
                    argDict['dobYear'] = self.dobYear
                
                if self.dobDay is not None:
                    argDict['dobDay'] = self.dobDay
                
                error = self.ttAccount.createBilling(self.tcr.userName, self.tcr.password, argDict)
            finally:
                self.pleaseWaitDialog.hide()
                base.transitions.noTransitions()

        except TTAccount.TTAccountException:
            e = None
            error = str(e)
            self.notify.info(error)
            self.dialog.setMessage(error + Localizer.BillingScreenConnectionErrorSuffix)
            self.dialog.show()
            self.acceptOnce(self.dialogDoneEvent, self._BillingScreen__handleConnectionErrorAck)
            return None

        if error:
            error = self.ttAccount.getLastErrorMsg(self.attempts >= self.attemptThreshold)
            self.notify.info(error)
            self.dialog.setMessage(error)
            self.dialog.show()
            self.acceptOnce(self.dialogDoneEvent, self._BillingScreen__handleErrorAck)
        else:
            self.notify.info('Account billing successful.')
            if launcher:
                launcher.setPaidUserLoggedIn()
            
            self.ttAccount.sendLoginMsg()
            self.waitForDatabaseTimeout()

    
    def exitWaitForLoginResponse(self):
        self.cleanupWaitingForDatabase()
        self.tcr.handler = None

    
    def _BillingScreen__handleFocusChange(self, focusItem):
        for item in self.focusList:
            item.label.setColor(*self.labelFg)
        
        if focusItem is not None:
            focusItem.label.setColor(*self.labelFgActive)
        

    
    def _BillingScreen__handleCCYear(self):
        self.setFocus(self.ccMonthControl)

    
    def _BillingScreen__handleCCType(self):
        if not (self.removedCCTypePleaseChoose):
            self.removedCCTypePleaseChoose = 1
            pleaseChoose = self.ccTypeControl['items'][0]
            self.ccTypeControl.removeItem(pleaseChoose)
            pleaseChoose.destroy()
            self.ccTypeControl.scrollTo(0)
        

    
    def _BillingScreen__handleCCTypeEnterPress(self):
        self.advanceFocus(self.removedCCTypePleaseChoose)

    
    def _BillingScreen__handleCountry(self):
        defaultCountry = 'US'
        longestCountry = 'VC'
        currentCountry = self.countryControl.getSelectedText()
        defaultLen = len(Localizer.BillingScreenCountryNames[defaultCountry])
        longestLen = len(Localizer.BillingScreenCountryNames[longestCountry])
        currentLen = len(currentCountry)
        longestCountryScale = 0.61944200000000005
        if len(currentCountry) > len(defaultCountry):
            
            def lerp(x, y, t):
                return x + (y - x) * t

            maxLenDif = longestLen - defaultLen
            curLenDif = currentLen - defaultLen
            scale = lerp(self.defaultCountryScale, longestCountryScale, float(curLenDif) / maxLenDif)
            self.countryControl.itemFrame.setScale(scale)
        
        self._BillingScreen__showStateOrProvince()
        self.restartFocusMgmt()

    
    def _BillingScreen__showStateOrProvince(self):
        self.stateControl.hide()
        self.caProvinceControl.hide()
        self.provinceEntry.hide()
        self.zipCodeLabel.hide()
        self.postalCodeLabel.hide()
        if self.countryControl.getSelectedIndex() == self.countryCodes.index('US'):
            self.stateControl.show()
            self.zipCodeLabel.show()
            self.zipCodeEntry.label = self.zipCodeLabel
        elif self.countryControl.getSelectedIndex() == self.countryCodes.index('CA'):
            self.caProvinceControl.show()
            self.postalCodeLabel.show()
            self.zipCodeEntry.label = self.postalCodeLabel
        else:
            self.provinceEntry.show()
            self.postalCodeLabel.show()
            self.zipCodeEntry.label = self.postalCodeLabel

    
    def _BillingScreen__handleNameOnCard(self, name):
        if name != '':
            self._BillingScreen__handleSubmit()
        

    
    def _BillingScreen__handleSubmit(self):
        self.removeFocus()
        self.attempts += 1
        self.email = self.emailEntry.get()
        self.confirmEmail = self.emailConfirmEntry.get()
        self.address1 = self.address1Entry.get()
        self.address2 = self.address2Entry.get()
        self.city = self.cityEntry.get()
        self.countryCode = self.countryCodes[self.countryControl.getSelectedIndex()]
        self.stateCode = self.stateName2Code[self.stateControl.getSelectedText()]
        self.stateIndex = self.stateControl.getSelectedIndex()
        self.caProvince = self.canadianProvinceCodes[self.caProvinceControl.getSelectedIndex()]
        self.province = self.provinceEntry.get()
        self.zipCode = self.zipCodeEntry.get()
        self.ccType = self.ccTypeControl.getSelectedText()
        self.ccNumber = self.ccNumberEntry.get()
        self.ccMonth = self.ccMonthControl.getSelectedText()
        self.ccYear = self.ccYearControl.getSelectedText()
        self.nameOnCard = self.nameOnCardEntry.get()
        self.origInputs = {
            'ccNumber': self.ccNumber }
        self.ccNumber = InputCheck.stripCreditCardNumber(self.ccNumber)
        
        def displayError(msg, entryToReturnTo = None, postAckCallback = None):
            if self.attempts >= self.attemptThreshold:
                phoneNumber = self.tcr.accountServerConstants.getString('customerServicePhoneNumber')
                msg += Localizer.BillingScreenCustomerServiceHelp % phoneNumber
            
            self.dialog.setMessage(msg)
            self.dialog.show()
            
            def handleInvalidInputAck(self = self, entryToReturnTo = entryToReturnTo, postAckCallback = postAckCallback):
                self.dialog.hide()
                self.fsm.request('create')
                if postAckCallback:
                    postAckCallback()
                
                if entryToReturnTo:
                    self.setFocus(entryToReturnTo)
                

            self.acceptOnce(self.dialogDoneEvent, handleInvalidInputAck)

        
        def handleEmailMismatch():
            
            def clearEmailConfirmEntry():
                self.emailConfirmEntry.set('')

            displayError(Localizer.BillingScreenEmailMismatch, entryToReturnTo = self.emailEntry, postAckCallback = clearEmailConfirmEntry)

        
        def isValidCreditCardType(ccType):
            return ccType in Localizer.BillingScreenCreditCardTypes

        checks = ((self.email, [
            Localizer.BillingScreenEnterEmail,
            self.emailEntry]), ([
            InputCheck.isValidEmailAddr,
            [
                self.email]], [
            Localizer.BillingScreenEnterValidEmail,
            self.emailEntry]), (self.confirmEmail, [
            Localizer.BillingScreenEnterEmailConfirm,
            self.emailConfirmEntry]), ([
            InputCheck.emailAddrMatch,
            [
                self.email,
                self.confirmEmail]], [
            handleEmailMismatch,
            []]), (self.address1 + self.address2, [
            Localizer.BillingScreenEnterAddress,
            self.address1Entry]), (self.city, [
            Localizer.BillingScreenEnterAddress,
            self.cityEntry]), (self.zipCode, [
            Localizer.BillingScreenEnterAddress,
            self.zipCodeEntry]), ([
            isValidCreditCardType,
            [
                self.ccType]], [
            Localizer.BillingScreenChooseCreditCardType,
            self.ccTypeControl]), (self.ccNumber, [
            Localizer.BillingScreenEnterCreditCardNumber,
            self.ccNumberEntry]), ([
            InputCheck.isValidCreditCardNum,
            [
                self.ccNumber]], [
            Localizer.BillingScreenEnterValidCreditCardNumber,
            self.ccNumberEntry]), ([
            InputCheck.isValidCreditCardNum,
            [
                self.ccNumber,
                self.ccType]], [
            Localizer.BillingScreenEnterValidSpecificCreditCardNumber % self.ccType,
            self.ccNumberEntry]), ([
            InputCheck.isValidCreditCardExpDate,
            [
                self.ccMonth,
                self.ccYear,
                self.tcr.dateObject.getMonth(),
                self.tcr.dateObject.getYear()]], [
            Localizer.BillingScreenEnterValidCreditCardExpDate,
            self.ccMonthControl]), (self.nameOnCard, [
            Localizer.BillingScreenEnterNameOnCard,
            self.nameOnCardEntry]))
        for (check, failureAction) in checks:
            if type(check) == type(''):
                entryOk = check != ''
            else:
                (func, args) = check
                entryOk = func(*args)
            if not entryOk:
                if type(failureAction[1]) == type([]):
                    (func, args) = failureAction
                    func(*args)
                else:
                    (msg, entryToReturnTo) = failureAction
                    displayError(msg, entryToReturnTo = entryToReturnTo)
                return None
            
        
        self.fsm.request('waitForLoginResponse')

    
    def _BillingScreen__handleCancel(self):
        self.confirmCancel = ToontownDialog.GlobalDialog(doneEvent = 'confirmCancelDone', message = Localizer.BillingScreenConfirmCancel, okButtonText = Localizer.BillingScreenConfirmCancelYes, cancelButtonText = Localizer.BillingScreenConfirmCancelNo, style = ToontownDialog.TwoChoice)
        self.confirmCancel.show()
        self.acceptOnce('confirmCancelDone', self._BillingScreen__handleConfirmCancel)

    
    def _BillingScreen__handleConfirmCancel(self):
        status = self.confirmCancel.doneStatus
        self.ignore('confirmCancelDone')
        self.confirmCancel.cleanup()
        del self.confirmCancel
        if status == 'ok':
            messenger.send(self.doneEvent, [
                {
                    'mode': 'cancel' }])
        

    
    def _BillingScreen__handleErrorAck(self):
        self.dialog.hide()
        self.fsm.request('create')

    
    def _BillingScreen__handleConnectionErrorAck(self):
        self.dialog.hide()
        messenger.send(self.doneEvent, [
            {
                'mode': 'failure' }])

    
    def handleWaitForLoginResponse(self, msgType, di):
        if msgType == CLIENT_LOGIN_2_RESP:
            self.handleLoginResponseMsg2(di)
        elif msgType == CLIENT_SERVER_UP:
            self.tcr.handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self.tcr.handleServerDown(di)
        else:
            self.tcr.handleUnexpectedMsgType(msgType, di)

    
    def handleLoginResponseMsg2(self, di):
        returnCode = di.getUint8()
        self.notify.info('Login response return code: ' + str(returnCode))
        if returnCode == 0:
            self.notify.info('Logged in with username: %s' % self.tcr.userName)
            if launcher:
                launcher.setGoUserName(self.tcr.userName)
            
            self.tcr.justPaid = 1
            messenger.send(self.doneEvent, [
                {
                    'mode': 'success' }])
        else:
            errorString = di.getString()
            self.notify.warning(errorString)
            messenger.send(self.doneEvent, [
                {
                    'mode': 'reject' }])

    
    def showWhySafe(self):
        self.removeFocus()
        self.whySafeDialog.show()
        
        def hideWhySafe(self = self):
            self.whySafeDialog.hide()
            self.restoreFocus()

        self.acceptOnce(self.whySafeDoneEvent, hideWhySafe)

    
    def showPrivacyPolicy(self):
        self.removeFocus()
        ppDoneEvent = 'privacyPolicyDone'
        self.privacyPolicyDialog = PrivacyPolicyPanel(ppDoneEvent)
        self.privacyPolicyDialog.show()
        
        def hidePrivacyPolicy(self = self):
            self.privacyPolicyDialog.hide()
            self.privacyPolicyDialog.cleanup()
            del self.privacyPolicyDialog
            self.restoreFocus()

        self.acceptOnce(ppDoneEvent, hidePrivacyPolicy)


