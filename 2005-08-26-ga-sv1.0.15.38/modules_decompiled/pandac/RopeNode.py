# File: R (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import PandaNode

class RopeNode(PandaNode.PandaNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    RMTube = 3
    RMBillboard = 2
    RMTape = 1
    RMThread = 0
    UVNone = 0
    UVDistance2 = 3
    UVDistance = 2
    UVParametric = 1
    NMVertex = 1
    NMNone = 0
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpanda._inPHc9WzBQj(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHc9WRiMF:
            libpanda._inPHc9WRiMF(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPHc9WXsAM()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setCurve(self, curve):
        returnValue = libpanda._inPHc9WFaXK(self.this, curve.this)
        return returnValue

    
    def getCurve(self):
        returnValue = libpanda._inPHc9Waios(self.this)
        import NurbsCurveEvaluator
        returnObject = NurbsCurveEvaluator.NurbsCurveEvaluator(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setRenderMode(self, renderMode):
        returnValue = libpanda._inPHc9WuWlh(self.this, renderMode)
        return returnValue

    
    def getRenderMode(self):
        returnValue = libpanda._inPHc9WYvch(self.this)
        return returnValue

    
    def setUvMode(self, uvMode):
        returnValue = libpanda._inPHc9W6nhf(self.this, uvMode)
        return returnValue

    
    def getUvMode(self):
        returnValue = libpanda._inPHc9Wigqq(self.this)
        return returnValue

    
    def setUvDirection(self, uDominant):
        returnValue = libpanda._inPHc9WgEwx(self.this, uDominant)
        return returnValue

    
    def getUvDirection(self):
        returnValue = libpanda._inPHc9W_9Z_(self.this)
        return returnValue

    
    def setUvScale(self, scale):
        returnValue = libpanda._inPHc9W2gSR(self.this, scale)
        return returnValue

    
    def getUvScale(self):
        returnValue = libpanda._inPHc9WUMN6(self.this)
        return returnValue

    
    def setNormalMode(self, normalMode):
        returnValue = libpanda._inPHc9WoMpH(self.this, normalMode)
        return returnValue

    
    def getNormalMode(self):
        returnValue = libpanda._inPHc9WGyYY(self.this)
        return returnValue

    
    def setTubeUp(self, tubeUp):
        returnValue = libpanda._inPHc9WjaO5(self.this, tubeUp.this)
        return returnValue

    
    def getTubeUp(self):
        returnValue = libpanda._inPHc9WHo6a(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setUseVertexColor(self, flag):
        returnValue = libpanda._inPHc9WnZ_r(self.this, flag)
        return returnValue

    
    def getUseVertexColor(self):
        returnValue = libpanda._inPHc9WB86D(self.this)
        return returnValue

    
    def setNumSubdiv(self, numSubdiv):
        returnValue = libpanda._inPHc9WjOxh(self.this, numSubdiv)
        return returnValue

    
    def getNumSubdiv(self):
        returnValue = libpanda._inPHc9W9Cxy(self.this)
        return returnValue

    
    def setNumSlices(self, numSlices):
        returnValue = libpanda._inPHc9WDjUu(self.this, numSlices)
        return returnValue

    
    def getNumSlices(self):
        returnValue = libpanda._inPHc9WMuU_(self.this)
        return returnValue

    
    def setThickness(self, thickness):
        returnValue = libpanda._inPHc9WF_Y0(self.this, thickness)
        return returnValue

    
    def getThickness(self):
        returnValue = libpanda._inPHc9WbcPu(self.this)
        return returnValue

    
    def setMatrix(self, matrix):
        returnValue = libpanda._inPHc9WMilH(self.this, matrix.this)
        return returnValue

    
    def clearMatrix(self):
        returnValue = libpanda._inPHc9WRoo1(self.this)
        return returnValue

    
    def hasMatrix(self):
        returnValue = libpanda._inPHc9W9ssg(self.this)
        return returnValue

    
    def getMatrix(self):
        returnValue = libpanda._inPHc9WYvf4(self.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def resetBound(self, relTo):
        returnValue = libpanda._inPHc9W4xWg(self.this, relTo.this)
        return returnValue


