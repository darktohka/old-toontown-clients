# File: A (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import DataNode

class AnalogNode(DataNode.DataNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self, client, deviceName):
        self.this = libpanda._inPOfOPq0Vk(client.this, deviceName)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPOfOPJCld()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def isValid(self):
        returnValue = libpanda._inPOfOPkjF9(self.this)
        return returnValue

    
    def getNumControls(self):
        returnValue = libpanda._inPOfOPPfB0(self.this)
        return returnValue

    
    def getControlState(self, index):
        returnValue = libpanda._inPOfOPVK5b(self.this, index)
        return returnValue

    
    def isControlKnown(self, index):
        returnValue = libpanda._inPOfOP4d_i(self.this, index)
        return returnValue

    
    def setOutput(self, channel, index, flip):
        returnValue = libpanda._inPOfOPAna3(self.this, channel, index, flip)
        return returnValue

    
    def clearOutput(self, channel):
        returnValue = libpanda._inPOfOP1Apo(self.this, channel)
        return returnValue

    
    def getOutput(self, channel):
        returnValue = libpanda._inPOfOP_dLB(self.this, channel)
        return returnValue

    
    def isOutputFlipped(self, channel):
        returnValue = libpanda._inPOfOPzrW_(self.this, channel)
        return returnValue


