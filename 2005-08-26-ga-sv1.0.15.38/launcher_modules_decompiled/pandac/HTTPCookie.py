# File: H (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class HTTPCookie(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _HTTPCookie__overloaded_constructor(self):
        self.this = libpandaexpress._inP2KOd2hG5()
        self.userManagesMemory = 1

    
    def _HTTPCookie__overloaded_constructor_atomicstring_ptrConstURLSpec(self, format, url):
        self.this = libpandaexpress._inP2KOdWucY(format, url.this)
        self.userManagesMemory = 1

    
    def _HTTPCookie__overloaded_constructor_atomicstring_atomicstring_atomicstring(self, name, path, domain):
        self.this = libpandaexpress._inP2KOdAtcu(name, path, domain)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inP2KOdypo8:
            libpandaexpress._inP2KOdypo8(self.this)
        

    
    def setName(self, name):
        returnValue = libpandaexpress._inP2KOdOck5(self.this, name)
        return returnValue

    
    def getName(self):
        returnValue = libpandaexpress._inP2KOdyFhg(self.this)
        return returnValue

    
    def setValue(self, value):
        returnValue = libpandaexpress._inP2KOdi2Qd(self.this, value)
        return returnValue

    
    def getValue(self):
        returnValue = libpandaexpress._inP2KOdFSc5(self.this)
        return returnValue

    
    def setDomain(self, domain):
        returnValue = libpandaexpress._inP2KOdVNff(self.this, domain)
        return returnValue

    
    def getDomain(self):
        returnValue = libpandaexpress._inP2KOdBGrk(self.this)
        return returnValue

    
    def setPath(self, path):
        returnValue = libpandaexpress._inP2KOdgXYU(self.this, path)
        return returnValue

    
    def getPath(self):
        returnValue = libpandaexpress._inP2KOdP4T7(self.this)
        return returnValue

    
    def setExpires(self, expires):
        returnValue = libpandaexpress._inP2KOdpqyy(self.this, expires.this)
        return returnValue

    
    def clearExpires(self):
        returnValue = libpandaexpress._inP2KOdAto1(self.this)
        return returnValue

    
    def hasExpires(self):
        returnValue = libpandaexpress._inP2KOdNpuR(self.this)
        return returnValue

    
    def getExpires(self):
        returnValue = libpandaexpress._inP2KOdRhpB(self.this)
        import HTTPDate
        returnObject = HTTPDate.HTTPDate(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setSecure(self, flag):
        returnValue = libpandaexpress._inP2KOd8wcJ(self.this, flag)
        return returnValue

    
    def getSecure(self):
        returnValue = libpandaexpress._inP2KOdlxx4(self.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpandaexpress._inP2KOdFRXJ(self.this, other.this)
        return returnValue

    
    def updateFrom(self, other):
        returnValue = libpandaexpress._inP2KOdf06y(self.this, other.this)
        return returnValue

    
    def parseSetCookie(self, format, url):
        returnValue = libpandaexpress._inP2KOdu1Zp(self.this, format, url.this)
        return returnValue

    
    def _HTTPCookie__overloaded_isExpired_ptrConstHTTPCookie_ptrConstHTTPDate(self, now):
        returnValue = libpandaexpress._inP2KOddC4P(self.this, now.this)
        return returnValue

    
    def _HTTPCookie__overloaded_isExpired_ptrConstHTTPCookie(self):
        returnValue = libpandaexpress._inP2KOdv13h(self.this)
        return returnValue

    
    def matchesUrl(self, url):
        returnValue = libpandaexpress._inP2KOd6_jU(self.this, url.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inP2KOdDQSj(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._HTTPCookie__overloaded_constructor(*_args)
        elif numArgs == 2:
            return self._HTTPCookie__overloaded_constructor_atomicstring_ptrConstURLSpec(*_args)
        elif numArgs == 3:
            return self._HTTPCookie__overloaded_constructor_atomicstring_atomicstring_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 2 3 '

    
    def isExpired(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._HTTPCookie__overloaded_isExpired_ptrConstHTTPCookie(*_args)
        elif numArgs == 1:
            return self._HTTPCookie__overloaded_isExpired_ptrConstHTTPCookie_ptrConstHTTPDate(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


