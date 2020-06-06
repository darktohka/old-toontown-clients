# File: Q (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class QueuedReturnPointerToConnection(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
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
        

    
    def setMaxQueueSize(self, maxSize):
        returnValue = libpanda._inP9ImMBHvr(self.this, maxSize)
        return returnValue

    
    def getMaxQueueSize(self):
        returnValue = libpanda._inP9ImMCaPK(self.this)
        return returnValue

    
    def getCurrentQueueSize(self):
        returnValue = libpanda._inP9ImMswOz(self.this)
        return returnValue


