# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\login\LoginTTSpecificDevAccount.py
from pandac.PandaModules import *
from direct.distributed.MsgTypes import *
from direct.directnotify import DirectNotifyGlobal
import LoginTTAccount
from direct.distributed.PyDatagram import PyDatagram
from TTAccount import TTAccountException

class LoginTTSpecificDevAccount(LoginTTAccount.LoginTTAccount):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('LoginTTSpecificDevAccount')

    def __init__(self, cr):
        LoginTTAccount.LoginTTAccount.__init__(self, cr)

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
        cr = self.cr
        tokenString = ''
        access = base.config.GetString('force-paid-status', '')
        if access == '':
            access = 'FULL'
        elif access == 'paid':
            access = 'FULL'
        elif access == 'unpaid':
            access = 'VELVET_ROPE'
        elif access == 'VELVET':
            access = 'VELVET_ROPE'
        else:
            self.notify.error("don't know what to do with force-paid-status %s" % access)
        tokenString += 'TOONTOWN_ACCESS=%s&' % access
        tokenString += 'TOONTOWN_GAME_KEY=%s&' % self.loginName
        wlChatEnabled = 'YES'
        if base.config.GetString('otp-whitelist', 'YES') == 'NO':
            wlChatEnabled = 'NO'
        tokenString += 'WL_CHAT_ENABLED=%s &' % wlChatEnabled
        openChatEnabled = 'NO'
        if cr.openChatAllowed:
            openChatEnabled = 'YES'
        tokenString += 'OPEN_CHAT_ENABLED=%s&' % openChatEnabled
        createFriendsWithChat = 'NO'
        if cr.allowSecretChat:
            createFriendsWithChat = 'CODE'
        tokenString += 'CREATE_FRIENDS_WITH_CHAT=%s&' % createFriendsWithChat
        chatCodeCreationRule = 'No'
        if cr.allowSecretChat:
            if base.config.GetBool('secret-chat-needs-parent-password', 0):
                chatCodeCreationRule = 'PARENT'
            else:
                chatCodeCreationRule = 'YES'
        tokenString += 'CHAT_CODE_CREATION_RULE=%s&' % chatCodeCreationRule
        DISLID = config.GetInt('fake-DISL-PlayerAccountId', 0)
        if not DISLID:
            NameStringId = 'DISLID_%s' % self.loginName
            DISLID = config.GetInt(NameStringId, 0)
        tokenString += 'ACCOUNT_NUMBER=%d&' % DISLID
        tokenString += 'ACCOUNT_NAME=%s&' % self.loginName
        tokenString += 'GAME_USERNAME=%s&' % self.loginName
        tokenString += 'ACCOUNT_NAME_APPROVED=TRUE&'
        tokenString += 'FAMILY_NUMBER=&'
        tokenString += 'Deployment=US&'
        withParentAccount = base.config.GetBool('dev-with-parent-account', 0)
        if withParentAccount:
            tokenString += 'TOON_ACCOUNT_TYPE=WITH_PARENT_ACCOUNT&'
        else:
            tokenString += 'TOON_ACCOUNT_TYPE=NO_PARENT_ACCOUNT&'
        tokenString += 'valid=true'
        self.notify.info('tokenString=\n%s' % tokenString)
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_LOGIN_TOONTOWN)
        playToken = tokenString
        datagram.addString(playToken)
        datagram.addString('dev')
        datagram.addUint32(cr.hashVal)
        datagram.addUint32(4)
        magicWords = base.config.GetString('want-magic-words', '')
        datagram.addString(magicWords)
        cr.send(datagram)

    def resendPlayToken(self):
        pass

    def requestPwdReminder(self, email=None, acctName=None):
        return 0

    def getAccountData(self, loginName, password):
        return 'Unsupported'

    def supportsParentPassword(self):
        return 1

    def supportsAuthenticateDelete(self):
        return 1

    def enableSecretFriends(self, loginName, password, parentPassword, enable=1):
        return (
         password == parentPassword, None)

    def needToSetParentPassword(self):
        return False