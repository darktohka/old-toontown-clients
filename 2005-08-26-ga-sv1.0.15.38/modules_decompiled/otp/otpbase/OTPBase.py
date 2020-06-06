# File: O (Python 2.2)

from direct.showbase import ShowBase

class OTPBase(ShowBase.ShowBase):
    
    def __init__(self):
        ShowBase.ShowBase.__init__(self)
        __builtins__['wantOtpServer'] = self.config.GetBool('want-otp-server', 0)


