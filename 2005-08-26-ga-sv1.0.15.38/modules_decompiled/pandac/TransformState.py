# File: T (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import CachedTypedWritableReferenceCount

class TransformState(CachedTypedWritableReferenceCount.CachedTypedWritableReferenceCount, FFIExternalObject.FFIExternalObject):
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
        

    
    def makeIdentity():
        returnValue = libpanda._inPnJyooK5A()
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makeIdentity = staticmethod(makeIdentity)
    
    def makeInvalid():
        returnValue = libpanda._inPnJyo0MDC()
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makeInvalid = staticmethod(makeInvalid)
    
    def makePos(pos):
        returnValue = libpanda._inPnJyoe_gZ(pos.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makePos = staticmethod(makePos)
    
    def makeHpr(hpr):
        returnValue = libpanda._inPnJyonj11(hpr.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makeHpr = staticmethod(makeHpr)
    
    def makeQuat(quat):
        returnValue = libpanda._inPnJyo_1bt(quat.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makeQuat = staticmethod(makeQuat)
    
    def makePosHpr(pos, hpr):
        returnValue = libpanda._inPnJyom6_l(pos.this, hpr.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makePosHpr = staticmethod(makePosHpr)
    
    def _TransformState__overloaded_makeScale_ptrConstLVecBase3f(scale):
        returnValue = libpanda._inPnJyoeCL8(scale.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _TransformState__overloaded_makeScale_ptrConstLVecBase3f = staticmethod(_TransformState__overloaded_makeScale_ptrConstLVecBase3f)
    
    def _TransformState__overloaded_makeScale_float(scale):
        returnValue = libpanda._inPnJyoUwg8(scale)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _TransformState__overloaded_makeScale_float = staticmethod(_TransformState__overloaded_makeScale_float)
    
    def makeShear(scale):
        returnValue = libpanda._inPnJyo7OFW(scale.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makeShear = staticmethod(makeShear)
    
    def makePosHprScale(pos, hpr, scale):
        returnValue = libpanda._inPnJyorG32(pos.this, hpr.this, scale.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makePosHprScale = staticmethod(makePosHprScale)
    
    def makePosQuatScale(pos, quat, scale):
        returnValue = libpanda._inPnJyoR_EG(pos.this, quat.this, scale.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makePosQuatScale = staticmethod(makePosQuatScale)
    
    def makePosHprScaleShear(pos, hpr, scale, shear):
        returnValue = libpanda._inPnJyoFwpz(pos.this, hpr.this, scale.this, shear.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makePosHprScaleShear = staticmethod(makePosHprScaleShear)
    
    def makePosQuatScaleShear(pos, quat, scale, shear):
        returnValue = libpanda._inPnJyoDFJS(pos.this, quat.this, scale.this, shear.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makePosQuatScaleShear = staticmethod(makePosQuatScaleShear)
    
    def makeMat(mat):
        returnValue = libpanda._inPnJyoyOW1(mat.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makeMat = staticmethod(makeMat)
    
    def getNumStates():
        returnValue = libpanda._inPnJyoft1r()
        return returnValue

    getNumStates = staticmethod(getNumStates)
    
    def getNumUnusedStates():
        returnValue = libpanda._inPnJyofD2f()
        return returnValue

    getNumUnusedStates = staticmethod(getNumUnusedStates)
    
    def clearCache():
        returnValue = libpanda._inPnJyo8dXE()
        return returnValue

    clearCache = staticmethod(clearCache)
    
    def listCycles(out):
        returnValue = libpanda._inPnJyoCbxp(out.this)
        return returnValue

    listCycles = staticmethod(listCycles)
    
    def listStates(out):
        returnValue = libpanda._inPnJyoIP9P(out.this)
        return returnValue

    listStates = staticmethod(listStates)
    
    def validateStates():
        returnValue = libpanda._inPnJyoidJ2()
        return returnValue

    validateStates = staticmethod(validateStates)
    
    def getClassType():
        returnValue = libpanda._inPnJyoOzaR()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def lessThan(self, other):
        returnValue = libpanda._inPnJyoQ1lR(self.this, other.this)
        return returnValue

    
    def getHash(self):
        returnValue = libpanda._inPnJyoNPd4(self.this)
        return returnValue

    
    def isIdentity(self):
        returnValue = libpanda._inPnJyo70HT(self.this)
        return returnValue

    
    def isInvalid(self):
        returnValue = libpanda._inPnJyo5m5t(self.this)
        return returnValue

    
    def isSingular(self):
        returnValue = libpanda._inPnJyo83Ub(self.this)
        return returnValue

    
    def hasComponents(self):
        returnValue = libpanda._inPnJyo3N1T(self.this)
        return returnValue

    
    def componentsGiven(self):
        returnValue = libpanda._inPnJyooeA_(self.this)
        return returnValue

    
    def hprGiven(self):
        returnValue = libpanda._inPnJyoePnm(self.this)
        return returnValue

    
    def quatGiven(self):
        returnValue = libpanda._inPnJyofBB6(self.this)
        return returnValue

    
    def hasPos(self):
        returnValue = libpanda._inPnJyod7_k(self.this)
        return returnValue

    
    def hasHpr(self):
        returnValue = libpanda._inPnJyoaR4z(self.this)
        return returnValue

    
    def hasQuat(self):
        returnValue = libpanda._inPnJyobgn7(self.this)
        return returnValue

    
    def hasScale(self):
        returnValue = libpanda._inPnJyoeXCQ(self.this)
        return returnValue

    
    def hasUniformScale(self):
        returnValue = libpanda._inPnJyoCj8m(self.this)
        return returnValue

    
    def hasShear(self):
        returnValue = libpanda._inPnJyoQZ2I(self.this)
        return returnValue

    
    def hasNonzeroShear(self):
        returnValue = libpanda._inPnJyoUk2V(self.this)
        return returnValue

    
    def hasMat(self):
        returnValue = libpanda._inPnJyoSx0T(self.this)
        return returnValue

    
    def getPos(self):
        returnValue = libpanda._inPnJyo1Y_X(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getHpr(self):
        returnValue = libpanda._inPnJyoyy3m(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getQuat(self):
        returnValue = libpanda._inPnJyozDmu(self.this)
        import Quat
        returnObject = Quat.Quat(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getScale(self):
        returnValue = libpanda._inPnJyomyBD(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getUniformScale(self):
        returnValue = libpanda._inPnJyo6_8Z(self.this)
        return returnValue

    
    def getShear(self):
        returnValue = libpanda._inPnJyon_27(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getMat(self):
        returnValue = libpanda._inPnJyoKS0G(self.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setPos(self, pos):
        returnValue = libpanda._inPnJyow_sj(self.this, pos.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setHpr(self, hpr):
        returnValue = libpanda._inPnJyotUny(self.this, hpr.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setQuat(self, quat):
        returnValue = libpanda._inPnJyoAH3z(self.this, quat.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setScale(self, scale):
        returnValue = libpanda._inPnJyo9kl0(self.this, scale.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setShear(self, shear):
        returnValue = libpanda._inPnJyoIVYt(self.this, shear.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def compose(self, other):
        returnValue = libpanda._inPnJyoNCSV(self.this, other.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def invertCompose(self, other):
        returnValue = libpanda._inPnJyo4b4F(self.this, other.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def unref(self):
        returnValue = libpanda._inPnJyo93Y1(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPnJyopd25(self.this, out.this)
        return returnValue

    
    def write(self, out, indentLevel):
        returnValue = libpanda._inPnJyoREBo(self.this, out.this, indentLevel)
        return returnValue

    
    def makeScale(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return TransformState._TransformState__overloaded_makeScale_float(*_args)
            
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                return TransformState._TransformState__overloaded_makeScale_ptrConstLVecBase3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3.VBase3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    makeScale = staticmethod(makeScale)

