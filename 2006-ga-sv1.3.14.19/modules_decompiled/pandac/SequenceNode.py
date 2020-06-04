# File: S (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import SelectiveChildNode

class SequenceNode(SelectiveChildNode.SelectiveChildNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, cycleRate, name):
        self.this = libpanda._inPnJyoxgAs(cycleRate, name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPnJyo_77X:
            libpanda._inPnJyo_77X(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPnJyoNJ9E()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setCycleRate(self, cycleRate):
        returnValue = libpanda._inPnJyoZDCt(self.this, cycleRate)
        return returnValue

    
    def getCycleRate(self):
        returnValue = libpanda._inPnJyonfhi(self.this)
        return returnValue

    
    def setVisibleChild(self, index):
        returnValue = libpanda._inPnJyowb0Q(self.this, index)
        return returnValue


