# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class ConnectionReader(FFIExternalObject.FFIExternalObject):
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
        

    
    def destructor(self):
        if libpanda and libpanda._inP9ImMGUzi:
            libpanda._inP9ImMGUzi(self.this)
        

    
    def addConnection(self, connection):
        returnValue = libpanda._inP9ImMqLA4(self.this, connection.this)
        return returnValue

    
    def removeConnection(self, connection):
        returnValue = libpanda._inP9ImMBUJ8(self.this, connection.this)
        return returnValue

    
    def isConnectionOk(self, connection):
        returnValue = libpanda._inP9ImMNKeX(self.this, connection.this)
        return returnValue

    
    def poll(self):
        returnValue = libpanda._inP9ImMXxFz(self.this)
        return returnValue

    
    def getManager(self):
        returnValue = libpanda._inP9ImMivcH(self.this)
        import ConnectionManager
        returnObject = ConnectionManager.ConnectionManager(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def isPolling(self):
        returnValue = libpanda._inP9ImMLEEA(self.this)
        return returnValue

    
    def getNumThreads(self):
        returnValue = libpanda._inP9ImM2jeO(self.this)
        return returnValue

    
    def setRawMode(self, mode):
        returnValue = libpanda._inP9ImM7duY(self.this, mode)
        return returnValue

    
    def getRawMode(self):
        returnValue = libpanda._inP9ImMCWld(self.this)
        return returnValue


