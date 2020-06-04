# File: W (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class WindowsRegistry(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    TString = 2
    TInt = 1
    TNone = 0
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPJoxtuWsE:
            libpandaexpress._inPJoxtuWsE(self.this)
        

    
    def setStringValue(key, name, value):
        returnValue = libpandaexpress._inPJoxt02db(key, name, value)
        return returnValue

    setStringValue = staticmethod(setStringValue)
    
    def setIntValue(key, name, value):
        returnValue = libpandaexpress._inPJoxtB50d(key, name, value)
        return returnValue

    setIntValue = staticmethod(setIntValue)
    
    def getKeyType(key, name):
        returnValue = libpandaexpress._inPJoxtKoxx(key, name)
        return returnValue

    getKeyType = staticmethod(getKeyType)
    
    def getStringValue(key, name, defaultValue):
        returnValue = libpandaexpress._inPJoxtR21I(key, name, defaultValue)
        return returnValue

    getStringValue = staticmethod(getStringValue)
    
    def getIntValue(key, name, defaultValue):
        returnValue = libpandaexpress._inPJoxtk5ML(key, name, defaultValue)
        return returnValue

    getIntValue = staticmethod(getIntValue)

