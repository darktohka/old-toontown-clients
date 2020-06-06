# File: F (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TextNode

class FrameRateMeter(TextNode.TextNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpanda._inPXs2xYERg(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPXs2xKim9()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setupWindow(self, window):
        returnValue = libpanda._inPXs2xU30L(self.this, window.this)
        return returnValue

    
    def clearWindow(self):
        returnValue = libpanda._inPXs2xxnBF(self.this)
        return returnValue

    
    def getWindow(self):
        returnValue = libpanda._inPXs2xYSXV(self.this)
        import GraphicsOutput
        returnObject = GraphicsOutput.GraphicsOutput(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getDisplayRegion(self):
        returnValue = libpanda._inPXs2xtWk2(self.this)
        import DisplayRegion
        returnObject = DisplayRegion.DisplayRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setUpdateInterval(self, updateInterval):
        returnValue = libpanda._inPXs2xUvgr(self.this, updateInterval)
        return returnValue

    
    def getUpdateInterval(self):
        returnValue = libpanda._inPXs2x0Ouf(self.this)
        return returnValue

    
    def setTextPattern(self, textPattern):
        returnValue = libpanda._inPXs2xNbmG(self.this, textPattern)
        return returnValue

    
    def getTextPattern(self):
        returnValue = libpanda._inPXs2xJ3wF(self.this)
        return returnValue

    
    def setClockObject(self, clockObject):
        returnValue = libpanda._inPXs2xqr7U(self.this, clockObject.this)
        return returnValue

    
    def getClockObject(self):
        returnValue = libpanda._inPXs2xZmdy(self.this)
        import ClockObject
        returnObject = ClockObject.ClockObject(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject


