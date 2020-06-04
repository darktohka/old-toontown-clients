# File: B (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import DataNode

class ButtonNode(DataNode.DataNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, client, deviceName):
        self.this = libpanda._inPOfOPN3Xg(client.this, deviceName)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPOfOPO7Jc()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def isValid(self):
        returnValue = libpanda._inPOfOPWoo7(self.this)
        return returnValue

    
    def getNumButtons(self):
        returnValue = libpanda._inPOfOP0MKT(self.this)
        return returnValue

    
    def setButtonMap(self, index, button):
        returnValue = libpanda._inPOfOPgucs(self.this, index, button.this)
        return returnValue

    
    def getButtonMap(self, index):
        returnValue = libpanda._inPOfOPQ5W8(self.this, index)
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getButtonState(self, index):
        returnValue = libpanda._inPOfOPGekS(self.this, index)
        return returnValue

    
    def isButtonKnown(self, index):
        returnValue = libpanda._inPOfOPIiuC(self.this, index)
        return returnValue


