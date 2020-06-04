# File: A (Python 2.2)

from ShowBaseGlobal import *
from HTTPUtil import *
import DirectNotifyGlobal
import TTAccount
import DateObject
import TTDateObject
import time

class AccountServerDate:
    notify = DirectNotifyGlobal.directNotify.newCategory('AccountServerDate')
    
    def __init__(self):
        self._AccountServerDate__grabbed = 0

    
    def getServer(self):
        return TTAccount.getAccountServer().cStr()

    
    def grabDate(self, force = 0):
        if self._AccountServerDate__grabbed and not force:
            self.notify.debug('using cached account server date')
            return None
        
        if toonbase.tcr.accountOldAuth or base.config.GetBool('use-local-date', 0):
            self._AccountServerDate__useLocalClock()
            return None
        
        url = URLSpec(self.getServer())
        url.setPath('/getDate.php')
        self.notify.debug('grabbing account server date from %s' % url.cStr())
        response = getHTTPResponse(url)
        if response[0] != 'ACCOUNT SERVER DATE':
            self.notify.debug('invalid response header')
            raise UnexpectedResponse, 'unexpected response, response=%s' % response
        
        
        try:
            epoch = int(response[1])
        except ValueError:
            e = None
            self.notify.debug(str(e))
            raise UnexpectedResponse, 'unexpected response, response=%s' % response

        timeTuple = time.gmtime(epoch)
        self.year = timeTuple[0]
        self.month = timeTuple[1]
        self.day = timeTuple[2]
        toonbase.tcr.dateObject = TTDateObject.TTDateObject(self)
        self._AccountServerDate__grabbed = 1

    
    def _AccountServerDate__useLocalClock(self):
        self.month = toonbase.tcr.dateObject.getMonth()
        self.year = toonbase.tcr.dateObject.getYear()
        self.day = toonbase.tcr.dateObject.getDay()

    
    def getMonth(self):
        return self.month

    
    def getYear(self):
        return self.year

    
    def getDay(self):
        return self.day


