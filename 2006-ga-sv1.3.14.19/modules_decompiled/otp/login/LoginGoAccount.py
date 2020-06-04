# File: L (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.distributed.MsgTypes import *
from direct.directnotify import DirectNotifyGlobal
import LoginBase
from direct.distributed.PyDatagram import PyDatagram

class LoginGoAccount(LoginBase.LoginBase):
    
    def __init__(self, cr):
        LoginBase.LoginBase.__init__(self, cr)

    
    def createAccount(self, loginName, password, data):
        return 'Unsupported'

    
    def authorize(self, loginName, password):
        self.loginName = loginName
        self.password = password
        return None

    
    def supportsRelogin(self):
        return 0

    
    def sendLoginMsg(self):
        cr = self.cr
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_LOGIN_2)
        datagram.addString(self.password)
        datagram.addString(cr.serverVersion)
        datagram.addUint32(cr.hashVal)
        self._LoginGoAccount__addTokenType(datagram)
        datagram.addString(cr.validateDownload)
        datagram.addString(cr.wantMagicWords)
        cr.send(datagram)

    
    def resendPlayToken(self):
        return None

    
    def requestPwdReminder(self, email = None, acctName = None):
        return 0

    
    def getAccountData(self, loginName, password):
        return 'Unsupported'

    
    def supportsParentPassword(self):
        return 0

    
    def authenticateParentPassword(self, loginName, password, parentPassword):
        return (0, None)

    
    def supportsAuthenticateDelete(self):
        return 0

    
    def enableSecretFriends(self, loginName, password, parentPassword, enable = 1):
        return (0, None)

    
    def _LoginGoAccount__addTokenType(self, datagram):
        datagram.addInt32(CLIENT_LOGIN_2_BLUE)


