# File: L (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.distributed.MsgTypes import *
from direct.directnotify import DirectNotifyGlobal
import LoginBase
import TTAccount
from direct.distributed.PyDatagram import PyDatagram

class LoginTTAccount(LoginBase.LoginBase, TTAccount.TTAccount):
    notify = DirectNotifyGlobal.directNotify.newCategory('LoginTTAcct')
    
    def __init__(self, cr):
        LoginBase.LoginBase.__init__(self, cr)
        TTAccount.TTAccount.__init__(self, cr)

    
    def supportsRelogin(self):
        return 1

    
    def sendLoginMsg(self):
        cr = self.cr
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_LOGIN_2)
        self._LoginTTAccount__addPlayToken(datagram)
        datagram.addString(cr.serverVersion)
        datagram.addUint32(cr.hashVal)
        self._LoginTTAccount__addTokenType(datagram)
        datagram.addString(cr.validateDownload)
        datagram.addString(cr.wantMagicWords)
        cr.send(datagram)

    
    def resendPlayToken(self):
        cr = self.cr
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_SET_SECURITY)
        self._LoginTTAccount__addPlayToken(datagram)
        self._LoginTTAccount__addTokenType(datagram)
        cr.send(datagram)

    
    def _LoginTTAccount__addPlayToken(self, datagram):
        self.playToken = self.playToken.strip()
        datagram.addString(self.playToken)

    
    def _LoginTTAccount__addTokenType(self, datagram):
        if self.playTokenIsEncrypted:
            datagram.addInt32(CLIENT_LOGIN_2_PLAY_TOKEN)
        else:
            datagram.addInt32(CLIENT_LOGIN_2_PLAY_TOKEN)

    
    def getErrorCode(self):
        return self.response.getInt('errorCode', 0)

    
    def needToSetParentPassword(self):
        return self.response.getBool('secretsPasswordNotSet', 0)


