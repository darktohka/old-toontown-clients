# File: L (Python 2.2)

from ShowBaseGlobal import *
from ToontownMsgTypes import *
import DirectNotifyGlobal
import LoginBase
import TTAccount

class LoginTTAccount(LoginBase.LoginBase, TTAccount.TTAccount):
    notify = DirectNotifyGlobal.directNotify.newCategory('LoginTTAcct')
    
    def supportsRelogin(self):
        return 1

    
    def sendLoginMsg(self):
        tcr = self.tcr
        datagram = Datagram()
        datagram.addUint16(CLIENT_LOGIN_2)
        self._LoginTTAccount__addPlayToken(datagram)
        datagram.addString(tcr.serverVersion)
        datagram.addUint32(tcr.hashVal)
        self._LoginTTAccount__addTokenType(datagram)
        tcr.send(datagram)

    
    def resendPlayToken(self):
        tcr = self.tcr
        datagram = Datagram()
        datagram.addUint16(CLIENT_SET_SECURITY)
        self._LoginTTAccount__addPlayToken(datagram)
        self._LoginTTAccount__addTokenType(datagram)
        tcr.send(datagram)

    
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


