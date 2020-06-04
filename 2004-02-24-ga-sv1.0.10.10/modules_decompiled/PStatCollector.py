# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class PStatCollector(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _PStatCollector__overloaded_constructor_ptrConstPStatCollector_atomicstring(self, parent, name):
        self.this = libpanda._inPiqKx0IR6(parent.this, name)
        self.userManagesMemory = 1

    
    def _PStatCollector__overloaded_constructor_atomicstring_ptrPStatClient(self, name, client):
        self.this = libpanda._inPiqKx2W_r(name, client.this)
        self.userManagesMemory = 1

    
    def _PStatCollector__overloaded_constructor_atomicstring(self, name):
        self.this = libpanda._inPiqKxAnSO(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPiqKxddCV:
            libpanda._inPiqKxddCV(self.this)
        

    
    def isActive(self):
        returnValue = libpanda._inPiqKxIh5b(self.this)
        return returnValue

    
    def start(self):
        returnValue = libpanda._inPiqKxp9Pr(self.this)
        return returnValue

    
    def stop(self):
        returnValue = libpanda._inPiqKx7E21(self.this)
        return returnValue

    
    def clearLevel(self):
        returnValue = libpanda._inPiqKxqN32(self.this)
        return returnValue

    
    def setLevel(self, parameter1):
        returnValue = libpanda._inPiqKxTICx(self.this, parameter1)
        return returnValue

    
    def addLevel(self, parameter1):
        returnValue = libpanda._inPiqKxJc8M(self.this, parameter1)
        return returnValue

    
    def subLevel(self, parameter1):
        returnValue = libpanda._inPiqKx4Ti2(self.this, parameter1)
        return returnValue

    
    def getLevel(self):
        returnValue = libpanda._inPiqKxuyK6(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._PStatCollector__overloaded_constructor_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                import PStatClient
                if isinstance(_args[1], PStatClient.PStatClient):
                    return self._PStatCollector__overloaded_constructor_atomicstring_ptrPStatClient(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <PStatClient.PStatClient> '
            elif isinstance(_args[0], PStatCollector):
                if isinstance(_args[1], types.StringType):
                    return self._PStatCollector__overloaded_constructor_ptrConstPStatCollector_atomicstring(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <PStatCollector> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


