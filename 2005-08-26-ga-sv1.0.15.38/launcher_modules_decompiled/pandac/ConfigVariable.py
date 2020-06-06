# File: C (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import ConfigVariableBase

class ConfigVariable(ConfigVariableBase.ConfigVariableBase, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpandaexpress._inPKoxtfAWp(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxtL_tx:
            libpandaexpress._inPKoxtL_tx(self.this)
        

    
    def getDefaultValue(self):
        returnValue = libpandaexpress._inPKoxtRHwC(self.this)
        import ConfigDeclaration
        returnObject = ConfigDeclaration.ConfigDeclaration(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getStringValue(self):
        returnValue = libpandaexpress._inPKoxtvDN0(self.this)
        return returnValue

    
    def setStringValue(self, value):
        returnValue = libpandaexpress._inPKoxt3HD1(self.this, value)
        return returnValue

    
    def getNumWords(self):
        returnValue = libpandaexpress._inPKoxtp0MY(self.this)
        return returnValue

    
    def hasStringWord(self, n):
        returnValue = libpandaexpress._inPKoxt4Tsy(self.this, n)
        return returnValue

    
    def hasBoolWord(self, n):
        returnValue = libpandaexpress._inPKoxt94kx(self.this, n)
        return returnValue

    
    def hasIntWord(self, n):
        returnValue = libpandaexpress._inPKoxtd0tj(self.this, n)
        return returnValue

    
    def hasDoubleWord(self, n):
        returnValue = libpandaexpress._inPKoxtxdWD(self.this, n)
        return returnValue

    
    def getStringWord(self, n):
        returnValue = libpandaexpress._inPKoxtg2rl(self.this, n)
        return returnValue

    
    def getBoolWord(self, n):
        returnValue = libpandaexpress._inPKoxtFdkk(self.this, n)
        return returnValue

    
    def getIntWord(self, n):
        returnValue = libpandaexpress._inPKoxt1RtW(self.this, n)
        return returnValue

    
    def getDoubleWord(self, n):
        returnValue = libpandaexpress._inPKoxtGzV2(self.this, n)
        return returnValue

    
    def setStringWord(self, n, value):
        returnValue = libpandaexpress._inPKoxtz4LI(self.this, n, value)
        return returnValue

    
    def setBoolWord(self, n, value):
        returnValue = libpandaexpress._inPKoxtytus(self.this, n, value)
        return returnValue

    
    def setIntWord(self, n, value):
        returnValue = libpandaexpress._inPKoxtzKpF(self.this, n, value)
        return returnValue

    
    def setDoubleWord(self, n, value):
        returnValue = libpandaexpress._inPKoxt9Fer(self.this, n, value)
        return returnValue

    
    def __str__(self):
        return self.getStringValue()

    
    def __hash__(self):
        raise AttributeError, 'ConfigVariables are not immutable.'

    
    def ls(self):
        Notify = Notify
        import pandac.Notify
        self.write(Notify.out())

    
    def __int__(self):
        return int(self.getValue())

    
    def __long__(self):
        return long(self.getValue())

    
    def __float__(self):
        return float(self.getValue())

    
    def __nonzero__(self):
        return bool(self.getValue())

    
    def __oct__(self):
        return oct(self.getValue())

    
    def __hex__(self):
        return hex(self.getValue())

    
    def __cmp__(self, other):
        return self.getValue().__cmp__(other)

    
    def __neg__(self):
        return -self.getValue()

    
    def __coerce__(self, other):
        return (self.getValue(), other)

    
    def __len__(self):
        return self.getNumWords()

    
    def __getitem__(self, n):
        if n < 0 or n >= self.getNumWords():
            raise IndexError
        
        return self.getWord(n)

    
    def __setitem__(self, n, value):
        if n < 0 or n > self.getNumWords():
            raise IndexError
        
        self.setWord(n, value)


