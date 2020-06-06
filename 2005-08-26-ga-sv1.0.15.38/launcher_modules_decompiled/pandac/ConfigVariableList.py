# File: C (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import ConfigVariableBase

class ConfigVariableList(ConfigVariableBase.ConfigVariableBase, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _ConfigVariableList__overloaded_constructor_atomicstring_atomicstring_int(self, name, description, flags):
        self.this = libpandaexpress._inPKoxt0y9H(name, description, flags)
        self.userManagesMemory = 1

    
    def _ConfigVariableList__overloaded_constructor_atomicstring_atomicstring(self, name, description):
        self.this = libpandaexpress._inPKoxtb__G(name, description)
        self.userManagesMemory = 1

    
    def _ConfigVariableList__overloaded_constructor_atomicstring(self, name):
        self.this = libpandaexpress._inPKoxtQEAl(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxtR_dj:
            libpandaexpress._inPKoxtR_dj(self.this)
        

    
    def getNumValues(self):
        returnValue = libpandaexpress._inPKoxtUmrj(self.this)
        return returnValue

    
    def getStringValue(self, n):
        returnValue = libpandaexpress._inPKoxtiLnG(self.this, n)
        return returnValue

    
    def getNumUniqueValues(self):
        returnValue = libpandaexpress._inPKoxt9_us(self.this)
        return returnValue

    
    def getUniqueValue(self, n):
        returnValue = libpandaexpress._inPKoxtclMe(self.this, n)
        return returnValue

    
    def size(self):
        returnValue = libpandaexpress._inPKoxttI9s(self.this)
        return returnValue

    
    def __getitem__(self, n):
        returnValue = libpandaexpress._inPKoxtowvO(self.this, n)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inPKoxt5Asq(self.this, out.this)
        return returnValue

    
    def write(self, out):
        returnValue = libpandaexpress._inPKoxthtwC(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._ConfigVariableList__overloaded_constructor_atomicstring(*_args)
        elif numArgs == 2:
            return self._ConfigVariableList__overloaded_constructor_atomicstring_atomicstring(*_args)
        elif numArgs == 3:
            return self._ConfigVariableList__overloaded_constructor_atomicstring_atomicstring_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

    
    def __hash__(self):
        raise AttributeError, 'ConfigVariables are not immutable.'

    
    def ls(self):
        Notify = Notify
        import pandac.Notify
        self.write(Notify.out())

    
    def __cmp__(self, other):
        return list(self).__cmp__(list(other))

    
    def __len__(self):
        return self.getNumValues()

    
    def __getitem__(self, n):
        if n < 0 or n >= self.getNumUniqueValues():
            raise IndexError
        
        return self.getUniqueValue(n)


