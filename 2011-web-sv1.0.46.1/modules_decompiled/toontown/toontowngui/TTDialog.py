# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\toontowngui\TTDialog.py
from otp.otpgui.OTPDialog import *

class TTDialog(OTPDialog):
    __module__ = __name__

    def __init__(self, parent=None, style=NoButtons, **kw):
        self.path = 'phase_3/models/gui/dialog_box_buttons_gui'
        OTPDialog.__init__(self, parent, style, **kw)
        self.initialiseoptions(TTDialog)


class TTGlobalDialog(GlobalDialog):
    __module__ = __name__

    def __init__(self, message='', doneEvent=None, style=NoButtons, okButtonText=OTPLocalizer.DialogOK, cancelButtonText=OTPLocalizer.DialogCancel, **kw):
        self.path = 'phase_3/models/gui/dialog_box_buttons_gui'
        GlobalDialog.__init__(self, message, doneEvent, style, okButtonText, cancelButtonText, **kw)
        self.initialiseoptions(TTGlobalDialog)