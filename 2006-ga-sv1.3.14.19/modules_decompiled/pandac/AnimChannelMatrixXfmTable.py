# File: A (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import AnimChannelACMatrixSwitchType

class AnimChannelMatrixXfmTable(AnimChannelACMatrixSwitchType.AnimChannelACMatrixSwitchType, FFIExternalObject.FFIExternalObject):
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
        if libpanda and libpanda._inPn9gMg0QL:
            libpanda._inPn9gMg0QL(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPn9gMBX4a()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def clearAllTables(self):
        returnValue = libpanda._inPn9gMvh4K(self.this)
        return returnValue

    
    def setTable(self, tableId, table):
        returnValue = libpanda._inPn9gMF4Yg(self.this, tableId, table.this)
        return returnValue

    
    def hasTable(self, tableId):
        returnValue = libpanda._inPn9gMZcqj(self.this, tableId)
        return returnValue

    
    def getTable(self, tableId):
        returnValue = libpanda._inPn9gM091i(self.this, tableId)
        import CPTAFloat
        returnObject = CPTAFloat.CPTAFloat(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def clearTable(self, tableId):
        returnValue = libpanda._inPn9gMO_k0(self.this, tableId)
        return returnValue


