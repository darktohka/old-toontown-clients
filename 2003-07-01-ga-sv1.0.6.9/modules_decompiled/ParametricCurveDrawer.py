# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TypedObject

class ParametricCurveDrawer(TypedObject.TypedObject, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpanda._inPHc9WCP8Y()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPHc9W_z9E()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setCurve(self, curve):
        returnValue = libpanda._inPHc9W8mvO(self.this, curve.this)
        return returnValue

    
    def setCurves(self, curves):
        returnValue = libpanda._inPHc9W2nwy(self.this, curves.this)
        return returnValue

    
    def clearCurves(self):
        returnValue = libpanda._inPHc9WQ318(self.this)
        return returnValue

    
    def getCurves(self):
        returnValue = libpanda._inPHc9WwaoA(self.this)
        import ParametricCurveCollection
        returnObject = ParametricCurveCollection.ParametricCurveCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getGeomNode(self):
        returnValue = libpanda._inPHc9WMGBt(self.this)
        import GeomNode
        returnObject = GeomNode.GeomNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def detachGeomNode(self):
        returnValue = libpanda._inPHc9Wx6Sb(self.this)
        import GeomNode
        returnObject = GeomNode.GeomNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setNumSegs(self, numSegs):
        returnValue = libpanda._inPHc9WI8aT(self.this, numSegs)
        return returnValue

    
    def getNumSegs(self):
        returnValue = libpanda._inPHc9W3ju9(self.this)
        return returnValue

    
    def setNumTicks(self, numTicks):
        returnValue = libpanda._inPHc9WKj6Q(self.this, numTicks)
        return returnValue

    
    def getNumTicks(self):
        returnValue = libpanda._inPHc9WhGZz(self.this)
        return returnValue

    
    def setColor(self, r, g, b):
        returnValue = libpanda._inPHc9WxQPs(self.this, r, g, b)
        return returnValue

    
    def setTickColor(self, r, g, b):
        returnValue = libpanda._inPHc9W9LPy(self.this, r, g, b)
        return returnValue

    
    def setFrameAccurate(self, frameAccurate):
        returnValue = libpanda._inPHc9WxP9Z(self.this, frameAccurate)
        return returnValue

    
    def getFrameAccurate(self):
        returnValue = libpanda._inPHc9Wk1Re(self.this)
        return returnValue

    
    def draw(self):
        returnValue = libpanda._inPHc9WCy3i(self.this)
        return returnValue

    
    def hide(self):
        returnValue = libpanda._inPHc9W0RC9(self.this)
        return returnValue

    
    def setTickScale(self, scale):
        returnValue = libpanda._inPHc9Wict8(self.this, scale)
        return returnValue

    
    def getTickScale(self):
        returnValue = libpanda._inPHc9WFHZj(self.this)
        return returnValue


