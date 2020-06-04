# File: G (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import GraphicsOutput

class GraphicsWindow(GraphicsOutput.GraphicsOutput, FFIExternalObject.FFIExternalObject):
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
        if libpanda and libpanda._inPO9cY6u1B:
            libpanda._inPO9cY6u1B(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPO9cYjGVA()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getProperties(self):
        returnValue = libpanda._inPO9cYhbmW(self.this)
        import WindowProperties
        returnObject = WindowProperties.WindowProperties(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getRequestedProperties(self):
        returnValue = libpanda._inPO9cY0Htu(self.this)
        import WindowProperties
        returnObject = WindowProperties.WindowProperties(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def clearRejectedProperties(self):
        returnValue = libpanda._inPO9cYYZ4X(self.this)
        return returnValue

    
    def getRejectedProperties(self):
        returnValue = libpanda._inPO9cYcXSI(self.this)
        import WindowProperties
        returnObject = WindowProperties.WindowProperties(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def requestProperties(self, requestedProperties):
        returnValue = libpanda._inPO9cYGdcu(self.this, requestedProperties.this)
        return returnValue

    
    def isClosed(self):
        returnValue = libpanda._inPO9cYu9q8(self.this)
        return returnValue

    
    def isFullscreen(self):
        returnValue = libpanda._inPO9cYJaEs(self.this)
        return returnValue

    
    def setWindowEvent(self, windowEvent):
        returnValue = libpanda._inPO9cYGNv6(self.this, windowEvent)
        return returnValue

    
    def getWindowEvent(self):
        returnValue = libpanda._inPO9cY_R55(self.this)
        return returnValue

    
    def getNumInputDevices(self):
        returnValue = libpanda._inPO9cYWc_C(self.this)
        return returnValue

    
    def getInputDeviceName(self, device):
        returnValue = libpanda._inPO9cYqhfW(self.this, device)
        return returnValue

    
    def hasPointer(self, device):
        returnValue = libpanda._inPO9cYYErM(self.this, device)
        return returnValue

    
    def hasKeyboard(self, device):
        returnValue = libpanda._inPO9cYeEpH(self.this, device)
        return returnValue

    
    def getPointer(self, device):
        returnValue = libpanda._inPO9cYxqr_(self.this, device)
        import MouseData
        returnObject = MouseData.MouseData(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def movePointer(self, device, x, y):
        returnValue = libpanda._inPO9cYPl6f(self.this, device, x, y)
        return returnValue

    
    def closeIme(self):
        returnValue = libpanda._inPO9cY_nZW(self.this)
        return returnValue


