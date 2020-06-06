# File: A (Python 2.2)

from ShowBaseGlobal import *
from RemoteValueSet import *
import DirectNotifyGlobal
import TTAccount
import HTTPUtil

class AccountServerConstants(RemoteValueSet):
    notify = DirectNotifyGlobal.directNotify.newCategory('AccountServerConstants')
    
    def __init__(self):
        self.expectedConstants = [
            'minNameLength',
            'minPwLength',
            'allowNewAccounts',
            'freeTrialPeriodInDays',
            'priceFirstMonth',
            'pricePerMonth',
            'customerServicePhoneNumber',
            'creditCardUpFront']
        self.defaults = {
            'minNameLength': '4',
            'minPwLength': '6',
            'allowNewAccounts': '1',
            'creditCardUpFront': '0',
            'priceFirstMonth': '9.95',
            'pricePerMonth': '7.95' }
        if toonbase.tcr.accountOldAuth or base.config.GetBool('default-server-constants', 0):
            self.notify.debug('there is no account server, setting defaults')
            self.dict = { }
            for constantName in self.expectedConstants:
                self.dict[constantName] = 'DEFAULT'
            
            self.dict.update(self.defaults)
            return None
        
        url = URLSpec(AccountServerConstants.getServer())
        url.setPath('/constants.php')
        self.notify.debug('grabbing account server constants from %s' % url.cStr())
        RemoteValueSet.__init__(self, url, expectedHeader = 'ACCOUNT SERVER CONSTANTS', expectedFields = self.expectedConstants)

    
    def getBool(self, name):
        return self._AccountServerConstants__getConstant(name, RemoteValueSet.getBool)

    
    def getInt(self, name):
        return self._AccountServerConstants__getConstant(name, RemoteValueSet.getInt)

    
    def getFloat(self, name):
        return self._AccountServerConstants__getConstant(name, RemoteValueSet.getFloat)

    
    def getString(self, name):
        return self._AccountServerConstants__getConstant(name, RemoteValueSet.getString)

    
    def _AccountServerConstants__getConstant(self, constantName, accessor):
        if not (constantName in self.expectedConstants):
            self.notify.warning("requested constant '%s' not in expected constant list; if it's a new constant, add it to the list" % constantName)
        
        return accessor(self, constantName)

    
    def getServer():
        return TTAccount.getAccountServer().cStr()

    getServer = staticmethod(getServer)
    
    def getServerURL():
        return TTAccount.getAccountServer()

    getServerURL = staticmethod(getServerURL)

