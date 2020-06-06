# File: T (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.directnotify import DirectNotifyGlobal
from direct.showbase import PythonUtil
from toontown.toonbase import TTLocalizer
import HTTPUtil
import RemoteValueSet
import copy
accountServer = ''
if launcher:
    accountServer = launcher.getAccountServer()
    print 'TTAccount: accountServer from launcher: ', accountServer

configAccountServer = base.config.GetString('account-server', '')
if configAccountServer:
    accountServer = configAccountServer
    print 'TTAccount: overriding accountServer from config: ', accountServer

if not accountServer:
    accountServer = 'https://account.toontown.com'
    print 'TTAccount: default accountServer: ', accountServer

accountServer = URLSpec(accountServer, 1)

def getAccountServer():
    return accountServer

TTAccountException = HTTPUtil.HTTPUtilException

class TTAccount:
    notify = DirectNotifyGlobal.directNotify.newCategory('TTAccount')
    notify.setDebug(1)
    
    def __init__(self, cr):
        self.cr = cr
        self.response = None

    
    def createAccount(self, loginName, password, data):
        return self.talk('create', data = self._TTAccount__makeLoginDict(loginName, password, data))

    
    def authorize(self, loginName, password):
        return self.talk('play', data = self._TTAccount__makeLoginDict(loginName, password))

    
    def createBilling(self, loginName, password, data):
        return self.talk('purchase', data = self._TTAccount__makeLoginDict(loginName, password, data))

    
    def setParentPassword(self, loginName, password, parentPassword):
        return self.talk('setParentPassword', data = self._TTAccount__makeLoginDict(loginName, password, {
            'parentPassword': parentPassword }))

    
    def supportsParentPassword(self):
        return 1

    
    def authenticateParentPassword(self, loginName, password, parentPassword):
        
        try:
            errorMsg = self.talk('authenticateParentPassword', data = self._TTAccount__makeLoginDict(loginName, parentPassword))
            if not errorMsg:
                return (1, None)
            
            if self.response.getInt('errorCode') in (5, 72):
                return (0, None)
            
            return (0, errorMsg)
        except TTAccountException:
            e = None
            return (0, str(e))


    
    def supportsAuthenticateDelete(self):
        return 1

    
    def authenticateDelete(self, loginName, password):
        
        try:
            errorMsg = self.talk('authenticateDelete', data = self._TTAccount__makeLoginDict(loginName, password))
            if not errorMsg:
                return (1, None)
            
            if self.response.getInt('errorCode') in (5, 72):
                return (0, None)
            
            return (0, errorMsg)
        except TTAccountException:
            e = None
            return (0, str(e))


    
    def enableSecretFriends(self, loginName, password, parentPassword, enable = 1):
        
        try:
            errorMsg = self.talk('setSecretChat', data = self._TTAccount__makeLoginDict(loginName, parentPassword, {
                'chat': base.cr.secretChatAllowed,
                'secretsNeedParentPassword': base.cr.secretChatNeedsParentPassword }))
            if not errorMsg:
                return (1, None)
            
            if self.response.getInt('errorCode') in (5, 72):
                return (0, None)
            
            return (0, errorMsg)
        except TTAccountException:
            e = None
            return (0, str(e))


    
    def changePassword(self, loginName, password, newPassword):
        return self.talk('purchase', data = self._TTAccount__makeLoginDict(loginName, password, {
            'newPassword': newPassword }))

    
    def requestPwdReminder(self, email = None, acctName = None):
        data = { }
        if email is not None:
            data['email'] = email
        else:
            data['accountName'] = acctName
        return self.talk('forgotPassword', data)

    
    def cancelAccount(self, loginName, password):
        return self.talk('cancel', data = self._TTAccount__makeLoginDict(loginName, password))

    
    def getAccountData(self, loginName, password):
        errorMsg = self.talk('get', data = self._TTAccount__makeLoginDict(loginName, password))
        if errorMsg:
            self.notify.warning('getAccountData error: %s' % errorMsg)
            return errorMsg
        
        if self.response.hasKey('errorMsg'):
            self.notify.warning("error field is: '%s'" % self.response.getString('errorMsg'))
        
        self.accountData = copy.deepcopy(self.response)
        fieldNameMap = {
            'em': 'email',
            'l1': 'addr1',
            'l2': 'addr2',
            'l3': 'addr3' }
        dict = self.accountData.dict
        for fieldName in dict.keys():
            if fieldNameMap.has_key(fieldName):
                dict[fieldNameMap[fieldName]] = dict[fieldName]
                del dict[fieldName]
            
        
        return None

    
    def getLastErrorMsg(self, forceCustServNum = 0):
        errCode = self.response.getInt('errorCode')
        if errCode < 100:
            msg = self.response.getString('errorMsg')
            if forceCustServNum:
                msg += ' ' + TTLocalizer.TTAccountCustomerServiceHelp % self.cr.accountServerConstants.getString('customerServicePhoneNumber')
            
        elif errCode < 200:
            msg = self.response.getString('errorMsg')
            msg += ' ' + TTLocalizer.TTAccountCustomerServiceHelp % self.cr.accountServerConstants.getString('customerServicePhoneNumber')
        elif errCode >= 500:
            msg = TTLocalizer.TTAccountIntractibleError
            msg += ' ' + TTLocalizer.TTAccountCallCustomerService % self.cr.accountServerConstants.getString('customerServicePhoneNumber')
        else:
            self.notify.warning('unknown error code class: %s: %s' % (self.response.getInt('errorCode'), self.response.getString('errorMsg')))
            msg = self.response.getString('errorMsg')
            msg += ' ' + TTLocalizer.TTAccountCallCustomerService % self.cr.accountServerConstants.getString('customerServicePhoneNumber')
        return msg

    
    def _TTAccount__makeLoginDict(self, loginName, password, data = None):
        dict = {
            'accountName': loginName,
            'password': password }
        if data:
            dict.update(data)
        
        return dict

    
    def talk(self, operation, data = { }):
        self.notify.debug('TTAccount.talk()')
        for key in data.keys():
            data[key] = str(data[key])
        
        if operation in ('play', 'get', 'cancel', 'authenticateParentPassword', 'authenticateDelete'):
            pass
        1
        if operation == 'forgotPassword':
            pass
        1
        if operation == 'setParentPassword':
            pass
        1
        if operation == 'setSecretChat':
            pass
        1
        if operation == 'create':
            pass
        1
        if operation == 'purchase':
            if data.has_key('newPassword'):
                pass
            1
        else:
            self.notify.error("Internal TTAccount error: need to add 'required data' checking for %s operation" % operation)
        op2Php = {
            'play': 'play',
            'get': 'get',
            'cancel': 'cancel',
            'create': 'create',
            'purchase': 'purchase',
            'setParentPassword': 'setSecrets',
            'authenticateParentPassword': 'authenticateChat',
            'authenticateDelete': 'authDelete',
            'setSecretChat': 'setChat',
            'forgotPassword': 'forgotPw' }
        url = URLSpec(getAccountServer())
        url.setPath('/%s.php' % op2Php[operation])
        body = ''
        if data.has_key('accountName'):
            url.setQuery('n=%s' % URLSpec.quote(data['accountName']))
        
        serverFields = {
            'accountName': 'n',
            'password': 'p',
            'parentPassword': 'sp',
            'newPassword': 'np',
            'chat': 'chat',
            'email': 'em',
            'dobYear': 'doby',
            'dobMonth': 'dobm',
            'dobDay': 'dobd',
            'ccNumber': 'ccn',
            'ccMonth': 'ccm',
            'ccYear': 'ccy',
            'nameOnCard': 'noc',
            'addr1': 'l1',
            'addr2': 'l2',
            'addr3': 'l3',
            'city': 'city',
            'state': 'state',
            'country': 'country',
            'zip': 'zip',
            'referrer': 'ref',
            'secretsNeedParentPassword': 'secretsNeedsParentPassword' }
        ignoredFields = ('ccType',)
        outBoundFields = { }
        for fieldName in data.keys():
            if not serverFields.has_key(fieldName):
                if not (fieldName in ignoredFields):
                    self.notify.error('unknown data field: %s' % fieldName)
                
            else:
                outBoundFields[serverFields[fieldName]] = data[fieldName]
        
        orderedFields = outBoundFields.keys()
        orderedFields.sort()
        for fieldName in orderedFields:
            if len(body):
                body += '&'
            
            body += '%s=%s' % (fieldName, URLSpec.quotePlus(outBoundFields[fieldName]))
        
        self.notify.debug('url=' + url.cStr())
        self.notify.debug('body=' + body)
        if operation in ('get',):
            expectedHeader = 'ACCOUNT INFO'
        elif operation in ('play', 'cancel', 'create', 'purchase', 'setParentPassword', 'setSecretChat', 'authenticateParentPassword', 'authenticateDelete', 'forgotPassword'):
            expectedHeader = 'ACCOUNT SERVER RESPONSE'
        else:
            self.notify.error("Internal TTAccount error: need to set expected response header for '%s' operation" % operation)
        self.response = RemoteValueSet.RemoteValueSet(url, self.cr.http, body = body, expectedHeader = expectedHeader)
        self.notify.debug('    self.response=' + str(self.response))
        if self.response.hasKey('errorCode'):
            errorCode = self.response.getInt('errorCode')
            self.notify.info('account server error code: %s' % errorCode)
            if errorCode == 10:
                self.cr.freeTimeExpiresAt = 0
            
        
        if self.response.hasKey('errorMsg'):
            return self.getLastErrorMsg()
        
        if operation in ('get', 'forgotPassword', 'authenticateDelete', 'play', 'cancel', 'create', 'purchase', 'setParentPassword', 'authenticateParentPassword'):
            pass
        1
        if operation == 'setSecretChat':
            self.playToken = self.response.getString('playToken')
            self.playTokenIsEncrypted = 1
        else:
            self.notify.error('Internal TTAccount error: need to extract useful data for %s operation' % operation)
        return None


