# File: P (Python 2.2)

from ShowBaseGlobal import *
from ToontownGlobals import *
from DirectObject import *
from DirectGui import *
from MultiPageTextFrame import *
import Localizer
import ToontownDialog

class PrivacyPolicyPanel(ToontownDialog.GlobalDialog):
    
    def __init__(self, doneEvent, hidePageNum = 0, pageChangeCallback = None):
        ToontownDialog.GlobalDialog.__init__(self, parent = aspect2d, dialogName = 'privacyPolicyDialog', doneEvent = doneEvent, okButtonText = Localizer.BillingScreenPrivacyPolicyClose, style = ToontownDialog.Acknowledge, text = '', topPad = 1.5, sidePad = 1.2, pos = (0, 0, -0.55000000000000004), scale = 0.90000000000000002)
        self.privacyPolicyText = MultiPageTextFrame(parent = self, textList = Localizer.BillingScreenPrivacyPolicyText, hidePageNum = hidePageNum, pageChangeCallback = pageChangeCallback, pos = (0, 0, 0.69999999999999996), width = 2.3999999999999999, height = 1.5)
        self['image'] = self['image']
        self['image_pos'] = (0, 0, 0.65000000000000002)
        self['image_scale'] = (2.7000000000000002, 1, 1.8999999999999999)
        closeButton = self.getChild(0)
        closeButton.setZ(-0.13)


