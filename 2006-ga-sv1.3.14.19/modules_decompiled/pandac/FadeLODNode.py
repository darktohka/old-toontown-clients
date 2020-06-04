# File: F (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import PandaNode

class FadeLODNode(PandaNode.PandaNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpanda._inPnJyowaxw(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPnJyow0Id:
            libpanda._inPnJyow0Id(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPnJyorHme()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def addSwitch(self, _in, out):
        returnValue = libpanda._inPnJyo0CwY(self.this, _in, out)
        return returnValue

    
    def setSwitch(self, index, _in, out):
        returnValue = libpanda._inPnJyo9uCi(self.this, index, _in, out)
        return returnValue

    
    def clearSwitches(self):
        returnValue = libpanda._inPnJyoFssR(self.this)
        return returnValue

    
    def getNumSwitches(self):
        returnValue = libpanda._inPnJyoVqJf(self.this)
        return returnValue

    
    def getIn(self, index):
        returnValue = libpanda._inPnJyoeeE8(self.this, index)
        return returnValue

    
    def getOut(self, index):
        returnValue = libpanda._inPnJyo3gO5(self.this, index)
        return returnValue

    
    def setCenter(self, center):
        returnValue = libpanda._inPnJyoVHdV(self.this, center.this)
        return returnValue

    
    def getCenter(self):
        returnValue = libpanda._inPnJyoUwYg(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setFadeTime(self, t):
        returnValue = libpanda._inPnJyobh3A(self.this, t)
        return returnValue

    
    def getFadeTime(self):
        returnValue = libpanda._inPnJyoXLep(self.this)
        return returnValue


