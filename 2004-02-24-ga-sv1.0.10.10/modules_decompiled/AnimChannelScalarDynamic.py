# File: A (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import AnimChannelACScalarSwitchType

class AnimChannelScalarDynamic(AnimChannelACScalarSwitchType.AnimChannelACScalarSwitchType, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
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
        if libpanda and libpanda._inPn9gMWJX6:
            libpanda._inPn9gMWJX6(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPn9gMywy2()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setValue(self, value):
        returnValue = libpanda._inPn9gMUD_1(self.this, value)
        return returnValue

    
    def setValueNode(self, node):
        returnValue = libpanda._inPn9gM7Avw(self.this, node.this)
        return returnValue


