# File: S (Python 2.2)

from ShowBaseGlobal import *
from ToontownGlobals import *
from DirectObject import *
from DirectGui import *
from MultiPageTextFrame import *
import Localizer
import ToontownDialog

class SecretFriendsInfoPanel(ToontownDialog.GlobalDialog):
    
    def __init__(self, doneEvent, hidePageNum = 0, pageChangeCallback = None):
        ToontownDialog.GlobalDialog.__init__(self, parent = aspect2d, dialogName = 'secretFriendsInfoDialog', doneEvent = doneEvent, okButtonText = Localizer.BillingScreenPrivacyPolicyClose, style = ToontownDialog.Acknowledge, text = '', topPad = 1.5, sidePad = 1.2, pos = (0, 0, 0.10000000000000001), scale = 0.90000000000000002)
        self.textPanel = MultiPageTextFrame(parent = self, textList = Localizer.SecretFriendsInfoPanelText, hidePageNum = hidePageNum, pageChangeCallback = pageChangeCallback)
        self['image'] = self['image']
        self['image_pos'] = (0, 0, -0.10000000000000001)
        self['image_scale'] = (2, 1, 1.3)
        closeButton = self.getChild(0)
        closeButton.setZ(-0.56000000000000005)


