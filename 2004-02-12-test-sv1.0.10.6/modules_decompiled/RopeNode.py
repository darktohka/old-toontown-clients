# File: R (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import PandaNode

class RopeNode(PandaNode.PandaNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    RMBillboard = 1
    RMThread = 0
    UVNone = 0
    UVDistance2 = 3
    UVDistance = 2
    UVParametric = 1
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self, name):
        self.this = libpanda._inPHc9WwBQj(name)
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
        returnValue = libpanda._inPHc9WZios(self.this)
        import NurbsCurveEvaluator
        returnObject = NurbsCurveEvaluator.NurbsCurveEvaluator(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setRenderMode(self, renderMode):
        returnValue = libpanda._inPHc9WtWlh(self.this, renderMode)
        return returnValue

    
    def getRenderMode(self):
        returnValue = libpanda._inPHc9WHvch(self.this)
        return returnValue

    
    def setUvMode(self, uvMode):
        returnValue = libpanda._inPHc9W6nhf(self.this, uvMode)
        return returnValue

    
    def getUvMode(self):
        returnValue = libpanda._inPHc9Wjgqq(self.this)
        return returnValue

    
    def setUvDirection(self, uDominant):
        returnValue = libpanda._inPHc9WhEwx(self.this, uDominant)
        return returnValue

    
    def getUvDirection(self):
        returnValue = libpanda._inPHc9W_9Z_(self.this)
        return returnValue

    
    def _RopeNode__overloaded_setUvScale_ptrRopeNode_ptrConstLVecBase2f(self, uvScale):
        returnValue = libpanda._inPHc9WGBGl(self.this, uvScale.this)
        return returnValue

    
    def _RopeNode__overloaded_setUvScale_ptrRopeNode_float(self, scale):
        returnValue = libpanda._inPHc9W2gSR(self.this, scale)
        return returnValue

    
    def getUvScale(self):
        returnValue = libpanda._inPHc9WbMN6(self.this)
        return returnValue

    
    def setUseVertexColor(self, flag):
        returnValue = libpanda._inPHc9W4Z_r(self.this, flag)
        return returnValue

    
    def getUseVertexColor(self):
        returnValue = libpanda._inPHc9WB86D(self.this)
        return returnValue

    
    def setNumSubdiv(self, numSubdiv):
        returnValue = libpanda._inPHc9WgOxh(self.this, numSubdiv)
        return returnValue

    
    def getNumSubdiv(self):
        returnValue = libpanda._inPHc9W6Cxy(self.this)
        return returnValue

    
    def setThickness(self, thickness):
        returnValue = libpanda._inPHc9WG_Y0(self.this, thickness)
        return returnValue

    
    def getThickness(self):
        returnValue = libpanda._inPHc9WYcPu(self.this)
        return returnValue

    
    def resetBound(self, relTo):
        returnValue = libpanda._inPHc9W5xWg(self.this, relTo.this)
        return returnValue

    
    def setUvScale(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase2
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._RopeNode__overloaded_setUvScale_ptrRopeNode_float(_args[0])
            elif isinstance(_args[0], VBase2.VBase2):
                return self._RopeNode__overloaded_setUvScale_ptrRopeNode_ptrConstLVecBase2f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2.VBase2> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


