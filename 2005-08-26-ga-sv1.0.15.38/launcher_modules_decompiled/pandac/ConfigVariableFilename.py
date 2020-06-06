# File: C (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import ConfigVariable

class ConfigVariableFilename(ConfigVariable.ConfigVariable, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _ConfigVariableFilename__overloaded_constructor_atomicstring(self, name):
        self.this = libpandaexpress._inPKoxtuiRq(name)
        self.userManagesMemory = 1

    
    def _ConfigVariableFilename__overloaded_constructor_atomicstring_ptrConstFilename_atomicstring_int(self, name, defaultValue, description, flags):
        self.this = libpandaexpress._inPKoxt5vRW(name, defaultValue.this, description, flags)
        self.userManagesMemory = 1

    
    def _ConfigVariableFilename__overloaded_constructor_atomicstring_ptrConstFilename_atomicstring(self, name, defaultValue, description):
        self.this = libpandaexpress._inPKoxtyAQf(name, defaultValue.this, description)
        self.userManagesMemory = 1

    
    def _ConfigVariableFilename__overloaded_constructor_atomicstring_ptrConstFilename(self, name, defaultValue):
        self.this = libpandaexpress._inPKoxt0kwV(name, defaultValue.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxtCSB2:
            libpandaexpress._inPKoxtCSB2(self.this)
        

    
    def assign(self, value):
        returnValue = libpandaexpress._inPKoxttq7m(self.this, value.this)
        returnObject = ConfigVariableFilename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def cStr(self):
        returnValue = libpandaexpress._inPKoxtFSXo(self.this)
        return returnValue

    
    def empty(self):
        returnValue = libpandaexpress._inPKoxtJ1W6(self.this)
        return returnValue

    
    def length(self):
        returnValue = libpandaexpress._inPKoxtwSZu(self.this)
        return returnValue

    
    def __getitem__(self, n):
        returnValue = libpandaexpress._inPKoxtJYNd(self.this, n)
        return returnValue

    
    def getFullpath(self):
        returnValue = libpandaexpress._inPKoxtdX94(self.this)
        return returnValue

    
    def getDirname(self):
        returnValue = libpandaexpress._inPKoxtdZMt(self.this)
        return returnValue

    
    def getBasename(self):
        returnValue = libpandaexpress._inPKoxt_BB0(self.this)
        return returnValue

    
    def getFullpathWoExtension(self):
        returnValue = libpandaexpress._inPKoxtA2V6(self.this)
        return returnValue

    
    def getBasenameWoExtension(self):
        returnValue = libpandaexpress._inPKoxtxTY1(self.this)
        return returnValue

    
    def getExtension(self):
        returnValue = libpandaexpress._inPKoxtiXPS(self.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpandaexpress._inPKoxtql0m(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpandaexpress._inPKoxt4gwG(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpandaexpress._inPKoxtKw5E(self.this, other.this)
        return returnValue

    
    def setValue(self, value):
        returnValue = libpandaexpress._inPKoxt6HHO(self.this, value.this)
        return returnValue

    
    def getValue(self):
        returnValue = libpandaexpress._inPKoxtqvVh(self.this)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getDefaultValue(self):
        returnValue = libpandaexpress._inPKoxtjUSR(self.this)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getWord(self, n):
        returnValue = libpandaexpress._inPKoxtBeVR(self.this, n)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setWord(self, n, value):
        returnValue = libpandaexpress._inPKoxteMQy(self.this, n, value.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._ConfigVariableFilename__overloaded_constructor_atomicstring(*_args)
        elif numArgs == 2:
            return self._ConfigVariableFilename__overloaded_constructor_atomicstring_ptrConstFilename(*_args)
        elif numArgs == 3:
            return self._ConfigVariableFilename__overloaded_constructor_atomicstring_ptrConstFilename_atomicstring(*_args)
        elif numArgs == 4:
            return self._ConfigVariableFilename__overloaded_constructor_atomicstring_ptrConstFilename_atomicstring_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    
    def __str__(self):
        return self.cStr()

    
    def __len__(self):
        return self.length()

    
    def __getitem__(self, n):
        return self.cStr().__getitem__(n)


