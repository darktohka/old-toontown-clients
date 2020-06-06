# File: C (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import ConfigVariable

class ConfigVariableInt(ConfigVariable.ConfigVariable, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _ConfigVariableInt__overloaded_constructor_atomicstring(self, name):
        self.this = libpandaexpress._inPKoxtZ5NO(name)
        self.userManagesMemory = 1

    
    def _ConfigVariableInt__overloaded_constructor_atomicstring_atomicstring_atomicstring_int(self, name, defaultValue, description, flags):
        self.this = libpandaexpress._inPKoxtCIhz(name, defaultValue, description, flags)
        self.userManagesMemory = 1

    
    def _ConfigVariableInt__overloaded_constructor_atomicstring_atomicstring_atomicstring(self, name, defaultValue, description):
        self.this = libpandaexpress._inPKoxttwuj(name, defaultValue, description)
        self.userManagesMemory = 1

    
    def _ConfigVariableInt__overloaded_constructor_atomicstring_atomicstring(self, name, defaultValue):
        self.this = libpandaexpress._inPKoxtVauC(name, defaultValue)
        self.userManagesMemory = 1

    
    def _ConfigVariableInt__overloaded_constructor_atomicstring_int_atomicstring_int(self, name, defaultValue, description, flags):
        self.this = libpandaexpress._inPKoxtJdKP(name, defaultValue, description, flags)
        self.userManagesMemory = 1

    
    def _ConfigVariableInt__overloaded_constructor_atomicstring_int_atomicstring(self, name, defaultValue, description):
        self.this = libpandaexpress._inPKoxtIVT4(name, defaultValue, description)
        self.userManagesMemory = 1

    
    def _ConfigVariableInt__overloaded_constructor_atomicstring_int(self, name, defaultValue):
        self.this = libpandaexpress._inPKoxt15LP(name, defaultValue)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxtBUF_:
            libpandaexpress._inPKoxtBUF_(self.this)
        

    
    def assign(self, value):
        returnValue = libpandaexpress._inPKoxtvXiv(self.this, value)
        returnObject = ConfigVariableInt(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def size(self):
        returnValue = libpandaexpress._inPKoxttake(self.this)
        return returnValue

    
    def __getitem__(self, n):
        returnValue = libpandaexpress._inPKoxtrtl3(self.this, n)
        return returnValue

    
    def setValue(self, value):
        returnValue = libpandaexpress._inPKoxtV_rk(self.this, value)
        return returnValue

    
    def getValue(self):
        returnValue = libpandaexpress._inPKoxtUxqZ(self.this)
        return returnValue

    
    def getDefaultValue(self):
        returnValue = libpandaexpress._inPKoxtyloR(self.this)
        return returnValue

    
    def getWord(self, n):
        returnValue = libpandaexpress._inPKoxtaaqx(self.this, n)
        return returnValue

    
    def setWord(self, n, value):
        returnValue = libpandaexpress._inPKoxtUSbb(self.this, n, value)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._ConfigVariableInt__overloaded_constructor_atomicstring(*_args)
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType) or isinstance(_args[1], types.LongType):
                    return self._ConfigVariableInt__overloaded_constructor_atomicstring_int(*_args)
                
                if isinstance(_args[1], types.StringType):
                    return self._ConfigVariableInt__overloaded_constructor_atomicstring_atomicstring(*_args)
                
                raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> <types.StringType> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType) or isinstance(_args[1], types.LongType):
                    return self._ConfigVariableInt__overloaded_constructor_atomicstring_int_atomicstring(*_args)
                
                if isinstance(_args[1], types.StringType):
                    return self._ConfigVariableInt__overloaded_constructor_atomicstring_atomicstring_atomicstring(*_args)
                
                raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> <types.StringType> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 4:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType) or isinstance(_args[1], types.LongType):
                    return self._ConfigVariableInt__overloaded_constructor_atomicstring_int_atomicstring_int(*_args)
                
                if isinstance(_args[1], types.StringType):
                    return self._ConfigVariableInt__overloaded_constructor_atomicstring_atomicstring_atomicstring_int(*_args)
                
                raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> <types.StringType> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    
    def __getitem__(self, n):
        if n < 0 or n >= self.getNumWords():
            raise IndexError
        
        return self.getWord(n)


