# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class CurveFitter(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpanda._inPHc9WMvxy()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHc9WTI_c:
            libpanda._inPHc9WTI_c(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPHc9WS9rR()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def reset(self):
        returnValue = libpanda._inPHc9WLEBv(self.this)
        return returnValue

    
    def addXyz(self, t, xyz):
        returnValue = libpanda._inPHc9WU_r2(self.this, t, xyz.this)
        return returnValue

    
    def addHpr(self, t, hpr):
        returnValue = libpanda._inPHc9WWyG0(self.this, t, hpr.this)
        return returnValue

    
    def addXyzHpr(self, t, xyz, hpr):
        returnValue = libpanda._inPHc9W8TgF(self.this, t, xyz.this, hpr.this)
        return returnValue

    
    def getNumSamples(self):
        returnValue = libpanda._inPHc9WxRbc(self.this)
        return returnValue

    
    def getSampleT(self, n):
        returnValue = libpanda._inPHc9WbZg8(self.this, n)
        return returnValue

    
    def getSampleXyz(self, n):
        returnValue = libpanda._inPHc9WeDCE(self.this, n)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getSampleHpr(self, n):
        returnValue = libpanda._inPHc9WpADi(self.this, n)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getSampleTangent(self, n):
        returnValue = libpanda._inPHc9W6bTo(self.this, n)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def removeSamples(self, begin, end):
        returnValue = libpanda._inPHc9WaErD(self.this, begin, end)
        return returnValue

    
    def sample(self, curves, count):
        returnValue = libpanda._inPHc9Wt_E2(self.this, curves.this, count)
        return returnValue

    
    def wrapHpr(self):
        returnValue = libpanda._inPHc9WN25m(self.this)
        return returnValue

    
    def sortPoints(self):
        returnValue = libpanda._inPHc9WUxVM(self.this)
        return returnValue

    
    def desample(self, factor):
        returnValue = libpanda._inPHc9We3Ay(self.this, factor)
        return returnValue

    
    def computeTangents(self, scale):
        returnValue = libpanda._inPHc9WsxwM(self.this, scale)
        return returnValue

    
    def makeHermite(self):
        returnValue = libpanda._inPHc9WTvHh(self.this)
        import ParametricCurveCollection
        returnObject = ParametricCurveCollection.ParametricCurveCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def makeNurbs(self):
        returnValue = libpanda._inPHc9WppFN(self.this)
        import ParametricCurveCollection
        returnObject = ParametricCurveCollection.ParametricCurveCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def output(self, out):
        returnValue = libpanda._inPHc9WfDRp(self.this, out.this)
        return returnValue

    
    def write(self, out):
        returnValue = libpanda._inPHc9WX7hW(self.this, out.this)
        return returnValue


