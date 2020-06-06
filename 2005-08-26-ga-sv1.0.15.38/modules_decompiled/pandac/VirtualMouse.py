# File: V (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import DataNode

class VirtualMouse(DataNode.DataNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpanda._inPOfOPZip_(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPOfOPFWPT:
            libpanda._inPOfOPFWPT(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPOfOP2nN2()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setMousePos(self, x, y):
        returnValue = libpanda._inPOfOPOTQU(self.this, x, y)
        return returnValue

    
    def setWindowSize(self, width, height):
        returnValue = libpanda._inPOfOPaz5v(self.this, width, height)
        return returnValue

    
    def setMouseOn(self, flag):
        returnValue = libpanda._inPOfOPi_qA(self.this, flag)
        return returnValue

    
    def pressButton(self, button):
        returnValue = libpanda._inPOfOPe3_V(self.this, button.this)
        return returnValue

    
    def releaseButton(self, button):
        returnValue = libpanda._inPOfOPgbfY(self.this, button.this)
        return returnValue


