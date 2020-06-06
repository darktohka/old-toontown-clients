# File: L (Python 2.2)

from ShowBaseGlobal import *
from ToontownMsgTypes import *
import DirectNotifyGlobal
import LoginBase

class LoginGSAccount(LoginBase.LoginBase):
    
    def __init__(self, tcr):
        LoginBase.LoginBase.__init__(self, tcr)
        tcr.freeTimeExpiresAt = -1
        tcr.setIsPaid(1)

    
    def createAccount(self, loginName, password, data):
        self.loginName = loginName
        self.password = password
        self.createFlag = 1
        return None

    
    def authorize(self, loginName, password):
        self.loginName = loginName
        self.password = password
        self.createFlag = 0
        return None

    
    def supportsRelogin(self):
        return 1

    
    def sendLoginMsg(self):
        tcr = self.tcr
        datagram = Datagram()
        datagram.addUint16(CLIENT_LOGIN)
        datagram.addString(self.loginName)
        if not (tcr.connectHttp):
            datagram.addUint32(tcr.tcpConn.getAddress().getIp())
        else:
            datagram.addUint32(0)
        datagram.addUint16(5150)
        datagram.addString(tcr.serverVersion)
        datagram.addUint32(tcr.hashVal)
        datagram.addString(self.password)
        datagram.addBool(self.createFlag)
        tcr.send(datagram)

    
    def resendPlayToken(self):
        return None

    
    def requestPwdReminder(self, email = None, acctName = None):
        return 0

    
    def getAccountData(self, loginName, password):
        return 'Unsupported'

    
    def supportsParentPassword(self):
        return 1

    
    def authenticateParentPassword(self, loginName, password, parentPassword):
        return (password == parentPassword, None)

    
    def supportsAuthenticateDelete(self):
        return 1

    
    def authenticateDelete(self, loginName, password):
        return (password == toonbase.tcr.password, None)

    
    def enableSecretFriends(self, loginName, password, parentPassword, enable = 1):
        return (password == parentPassword, None)


