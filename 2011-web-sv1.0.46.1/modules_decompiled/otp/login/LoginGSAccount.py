# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\login\LoginGSAccount.py
from pandac.PandaModules import *
from direct.distributed.MsgTypes import *
from direct.directnotify import DirectNotifyGlobal
import LoginBase
from direct.distributed.PyDatagram import PyDatagram

class LoginGSAccount(LoginBase.LoginBase):
    __module__ = __name__

    def __init__(self, cr):
        LoginBase.LoginBase.__init__(self, cr)

    def createAccount(self, loginName, password, data):
        self.loginName = loginName
        self.password = password
        self.createFlag = 1
        self.cr.freeTimeExpiresAt = -1
        self.cr.setIsPaid(1)
        return

    def authorize(self, loginName, password):
        self.loginName = loginName
        self.password = password
        self.createFlag = 0
        self.cr.freeTimeExpiresAt = -1
        self.cr.setIsPaid(1)
        return

    def supportsRelogin(self):
        return 1

    def sendLoginMsg(self):
        DISLID = config.GetInt('fake-DISL-PlayerAccountId', 0)
        if not DISLID:
            NameStringId = 'DISLID_%s' % self.loginName
            DISLID = config.GetInt(NameStringId, 0)
        cr = self.cr
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_LOGIN)
        datagram.addString(self.loginName)
        if cr.connectMethod != cr.CM_HTTP:
            datagram.addUint32(cr.tcpConn.getAddress().getIp())
        else:
            datagram.addUint32(0)
        datagram.addUint16(5150)
        datagram.addString(cr.serverVersion)
        datagram.addUint32(cr.hashVal)
        datagram.addString(self.password)
        datagram.addBool(self.createFlag)
        datagram.addString(cr.validateDownload)
        datagram.addString(cr.wantMagicWords)
        datagram.addUint32(DISLID)
        datagram.addString(config.GetString('otp-whitelist', 'YES'))
        cr.send(datagram)

    def resendPlayToken(self):
        pass

    def requestPwdReminder(self, email=None, acctName=None):
        return 0

    def getAccountData(self, loginName, password):
        return 'Unsupported'

    def supportsParentPassword(self):
        return 1

    def authenticateParentPassword(self, loginName, password, parentPassword):
        return (
         password == parentPassword, None)

    def authenticateParentUsernameAndPassword(self, loginName, password, parentUsername, parentPassword):
        return (
         password == parentPassword, None)

    def supportsAuthenticateDelete(self):
        return 1

    def authenticateDelete(self, loginName, password):
        return (
         password == self.cr.password, None)

    def enableSecretFriends(self, loginName, password, parentPassword, enable=1):
        return (
         password == parentPassword, None)