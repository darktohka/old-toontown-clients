# File: C (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import ConfigVariable

class ConfigVariableString(ConfigVariable.ConfigVariable, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _ConfigVariableString__overloaded_constructor_atomicstring(self, name):
        self.this = libpandaexpress._inPKoxtxoFd(name)
        self.userManagesMemory = 1

    
    def _ConfigVariableString__overloaded_constructor_atomicstring_atomicstring_atomicstring_int(self, name, defaultValue, description, flags):
        self.this = libpandaexpress._inPKoxtlDF7(name, defaultValue, description, flags)
        self.userManagesMemory = 1

    
    def _ConfigVariableString__overloaded_constructor_atomicstring_atomicstring_atomicstring(self, name, defaultValue, description):
        self.this = libpandaexpress._inPKoxtZRZG(name, defaultValue, description)
        self.userManagesMemory = 1

    
    def _ConfigVariableString__overloaded_constructor_atomicstring_atomicstring(self, name, defaultValue):
        self.this = libpandaexpress._inPKoxtpyKD(name, defaultValue)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxtcPA_:
            libpandaexpress._inPKoxtcPA_(self.this)
        

    
    def assign(self, value):
        returnValue = libpandaexpress._inPKoxtlnPz(self.this, value)
        returnObject = ConfigVariableString(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def cStr(self):
        returnValue = libpandaexpress._inPKoxtehBq(self.this)
        return returnValue

    
    def empty(self):
        returnValue = libpandaexpress._inPKoxtYAjn(self.this)
        return returnValue

    
    def length(self):
        returnValue = libpandaexpress._inPKoxtkRuz(self.this)
        return returnValue

    
    def __getitem__(self, n):
        returnValue = libpandaexpress._inPKoxtjG7L(self.this, n)
        return returnValue

    
    def eq(self, other):
        returnValue = libpandaexpress._inPKoxtvnj9(self.this, other)
        return returnValue

    
    def ne(self, other):
        returnValue = libpandaexpress._inPKoxt8nB4(self.this, other)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpandaexpress._inPKoxtfdFk(self.this, other)
        return returnValue

    
    def setValue(self, value):
        returnValue = libpandaexpress._inPKoxteOBH(self.this, value)
        return returnValue

    
    def getValue(self):
        returnValue = libpandaexpress._inPKoxtiqp3(self.this)
        return returnValue

    
    def getDefaultValue(self):
        returnValue = libpandaexpress._inPKoxtlm9N(self.this)
        return returnValue

    
    def getWord(self, n):
        returnValue = libpandaexpress._inPKoxtkWLx(self.this, n)
        return returnValue

    
    def setWord(self, n, value):
        returnValue = libpandaexpress._inPKoxtBIo5(self.this, n, value)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._ConfigVariableString__overloaded_constructor_atomicstring(*_args)
        elif numArgs == 2:
            return self._ConfigVariableString__overloaded_constructor_atomicstring_atomicstring(*_args)
        elif numArgs == 3:
            return self._ConfigVariableString__overloaded_constructor_atomicstring_atomicstring_atomicstring(*_args)
        elif numArgs == 4:
            return self._ConfigVariableString__overloaded_constructor_atomicstring_atomicstring_atomicstring_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    
    def __len__(self):
        return self.getValue().__len__()

    
    def __getitem__(self, n):
        return self.getValue().__getitem__(n)


