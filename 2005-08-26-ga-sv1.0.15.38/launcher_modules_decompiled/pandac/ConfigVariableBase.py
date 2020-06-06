# File: C (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import ConfigFlags

class ConfigVariableBase(ConfigFlags.ConfigFlags, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getName(self):
        returnValue = libpandaexpress._inPKoxtLAYK(self.this)
        return returnValue

    
    def getValueType(self):
        returnValue = libpandaexpress._inPKoxtSB4b(self.this)
        return returnValue

    
    def getDescription(self):
        returnValue = libpandaexpress._inPKoxtZc0t(self.this)
        return returnValue

    
    def getFlags(self):
        returnValue = libpandaexpress._inPKoxtZZnT(self.this)
        return returnValue

    
    def isClosed(self):
        returnValue = libpandaexpress._inPKoxtE1aP(self.this)
        return returnValue

    
    def getTrustLevel(self):
        returnValue = libpandaexpress._inPKoxtrrma(self.this)
        return returnValue

    
    def isDynamic(self):
        returnValue = libpandaexpress._inPKoxtYuk3(self.this)
        return returnValue

    
    def clearLocalValue(self):
        returnValue = libpandaexpress._inPKoxtfhKJ(self.this)
        return returnValue

    
    def hasLocalValue(self):
        returnValue = libpandaexpress._inPKoxtV4Ko(self.this)
        return returnValue

    
    def hasValue(self):
        returnValue = libpandaexpress._inPKoxtVuDp(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inPKoxt35Ii(self.this, out.this)
        return returnValue

    
    def write(self, out):
        returnValue = libpandaexpress._inPKoxt08N6(self.this, out.this)
        return returnValue


