# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class PStatCollector(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _PStatCollector__overloaded_constructor_ptrConstPStatCollector_atomicstring(self, parent, name):
        self.this = libpanda._inPhqKxzIR6(parent.this, name)
        self.userManagesMemory = 1

    
    def _PStatCollector__overloaded_constructor_atomicstring_ptrPStatClient(self, name, client):
        self.this = libpanda._inPhqKx3W_r(name, client.this)
        self.userManagesMemory = 1

    
    def _PStatCollector__overloaded_constructor_atomicstring(self, name):
        self.this = libpanda._inPhqKxAnSO(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPhqKxddCV:
            libpanda._inPhqKxddCV(self.this)
        

    
    def isActive(self):
        returnValue = libpanda._inPhqKxIh5b(self.this)
        return returnValue

    
    def isStarted(self):
        returnValue = libpanda._inPhqKx_sps(self.this)
        return returnValue

    
    def start(self):
        returnValue = libpanda._inPhqKxq9Pr(self.this)
        return returnValue

    
    def stop(self):
        returnValue = libpanda._inPhqKx6E21(self.this)
        return returnValue

    
    def clearLevel(self):
        returnValue = libpanda._inPhqKxrN32(self.this)
        return returnValue

    
    def setLevel(self, parameter1):
        returnValue = libpanda._inPhqKxSICx(self.this, parameter1)
        return returnValue

    
    def addLevel(self, parameter1):
        returnValue = libpanda._inPhqKxJc8M(self.this, parameter1)
        return returnValue

    
    def subLevel(self, parameter1):
        returnValue = libpanda._inPhqKx7Ti2(self.this, parameter1)
        return returnValue

    
    def getLevel(self):
        returnValue = libpanda._inPhqKxxyK6(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._PStatCollector__overloaded_constructor_atomicstring(*_args)
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                return self._PStatCollector__overloaded_constructor_atomicstring_ptrPStatClient(*_args)
            
            if isinstance(_args[0], PStatCollector):
                return self._PStatCollector__overloaded_constructor_ptrConstPStatCollector_atomicstring(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <PStatCollector> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


