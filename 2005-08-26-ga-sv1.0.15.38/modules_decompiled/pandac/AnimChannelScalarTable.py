# File: A (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import AnimChannelACScalarSwitchType

class AnimChannelScalarTable(AnimChannelACScalarSwitchType.AnimChannelACScalarSwitchType, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
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
        

    
    def destructor(self):
        if libpanda and libpanda._inPn9gMavTi:
            libpanda._inPn9gMavTi(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPn9gMptvC()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setTable(self, table):
        returnValue = libpanda._inPn9gM8JvW(self.this, table.this)
        return returnValue

    
    def hasTable(self):
        returnValue = libpanda._inPn9gM1YIG(self.this)
        return returnValue

    
    def clearTable(self):
        returnValue = libpanda._inPn9gMPoPB(self.this)
        return returnValue


