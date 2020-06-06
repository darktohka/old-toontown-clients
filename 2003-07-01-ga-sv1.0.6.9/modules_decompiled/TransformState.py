# File: T (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TypedWritableReferenceCount

class TransformState(TypedWritableReferenceCount.TypedWritableReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def makeIdentity():
        returnValue = libpanda._inPkJyooK5A()
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makeIdentity = staticmethod(makeIdentity)
    
    def makeInvalid():
        returnValue = libpanda._inPkJyo0MDC()
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makeInvalid = staticmethod(makeInvalid)
    
    def makePos(pos):
        returnValue = libpanda._inPkJyoe_gZ(pos.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makePos = staticmethod(makePos)
    
    def makeHpr(hpr):
        returnValue = libpanda._inPkJyomj11(hpr.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makeHpr = staticmethod(makeHpr)
    
    def makeQuat(quat):
        returnValue = libpanda._inPkJyo_1bt(quat.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makeQuat = staticmethod(makeQuat)
    
    def makePosHpr(pos, hpr):
        returnValue = libpanda._inPkJyon6_l(pos.this, hpr.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makePosHpr = staticmethod(makePosHpr)
    
    def _TransformState__overloaded_makeScale_ptrConstLVecBase3f(scale):
        returnValue = libpanda._inPkJyofCL8(scale.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _TransformState__overloaded_makeScale_ptrConstLVecBase3f = staticmethod(_TransformState__overloaded_makeScale_ptrConstLVecBase3f)
    
    def _TransformState__overloaded_makeScale_float(scale):
        returnValue = libpanda._inPkJyobwg8(scale)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _TransformState__overloaded_makeScale_float = staticmethod(_TransformState__overloaded_makeScale_float)
    
    def makePosHprScale(pos, hpr, scale):
        returnValue = libpanda._inPkJyosG32(pos.this, hpr.this, scale.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makePosHprScale = staticmethod(makePosHprScale)
    
    def makePosQuatScale(pos, quat, scale):
        returnValue = libpanda._inPkJyoR_EG(pos.this, quat.this, scale.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makePosQuatScale = staticmethod(makePosQuatScale)
    
    def makeMat(mat):
        returnValue = libpanda._inPkJyozOW1(mat.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makeMat = staticmethod(makeMat)
    
    def getNumStates():
        returnValue = libpanda._inPkJyoAt1r()
        return returnValue

    getNumStates = staticmethod(getNumStates)
    
    def getNumUnusedStates():
        returnValue = libpanda._inPkJyofD2f()
        return returnValue

    getNumUnusedStates = staticmethod(getNumUnusedStates)
    
    def clearCache():
        returnValue = libpanda._inPkJyo8dXE()
        return returnValue

    clearCache = staticmethod(clearCache)
    
    def getClassType():
        returnValue = libpanda._inPkJyoOzaR()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def isIdentity(self):
        returnValue = libpanda._inPkJyo70HT(self.this)
        return returnValue

    
    def isInvalid(self):
        returnValue = libpanda._inPkJyo_m5t(self.this)
        return returnValue

    
    def isSingular(self):
        returnValue = libpanda._inPkJyo83Ub(self.this)
        return returnValue

    
    def hasComponents(self):
        returnValue = libpanda._inPkJyo3N1T(self.this)
        return returnValue

    
    def componentsGiven(self):
        returnValue = libpanda._inPkJyopeA_(self.this)
        return returnValue

    
    def hprGiven(self):
        returnValue = libpanda._inPkJyofPnm(self.this)
        return returnValue

    
    def quatGiven(self):
        returnValue = libpanda._inPkJyoQBB6(self.this)
        return returnValue

    
    def hasPos(self):
        returnValue = libpanda._inPkJyoc7_k(self.this)
        return returnValue

    
    def hasHpr(self):
        returnValue = libpanda._inPkJyoZR4z(self.this)
        return returnValue

    
    def hasQuat(self):
        returnValue = libpanda._inPkJyoEgn7(self.this)
        return returnValue

    
    def hasScale(self):
        returnValue = libpanda._inPkJyoeXCQ(self.this)
        return returnValue

    
    def hasUniformScale(self):
        returnValue = libpanda._inPkJyoDj8m(self.this)
        return returnValue

    
    def hasMat(self):
        returnValue = libpanda._inPkJyoSx0T(self.this)
        return returnValue

    
    def getPos(self):
        returnValue = libpanda._inPkJyo1Y_X(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getHpr(self):
        returnValue = libpanda._inPkJyoxy3m(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getQuat(self):
        returnValue = libpanda._inPkJyo8Dmu(self.this)
        import Quat
        returnObject = Quat.Quat(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getScale(self):
        returnValue = libpanda._inPkJyomyBD(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getUniformScale(self):
        returnValue = libpanda._inPkJyo6_8Z(self.this)
        return returnValue

    
    def getMat(self):
        returnValue = libpanda._inPkJyoKS0G(self.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setPos(self, pos):
        returnValue = libpanda._inPkJyo3_sj(self.this, pos.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setHpr(self, hpr):
        returnValue = libpanda._inPkJyosUny(self.this, hpr.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setQuat(self, quat):
        returnValue = libpanda._inPkJyoBH3z(self.this, quat.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setScale(self, scale):
        returnValue = libpanda._inPkJyo_kl0(self.this, scale.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def compose(self, other):
        returnValue = libpanda._inPkJyoNCSV(self.this, other.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def invertCompose(self, other):
        returnValue = libpanda._inPkJyo4b4F(self.this, other.this)
        returnObject = TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def output(self, out):
        returnValue = libpanda._inPkJyood25(self.this, out.this)
        return returnValue

    
    def write(self, out, indentLevel):
        returnValue = libpanda._inPkJyoQEBo(self.this, out.this, indentLevel)
        return returnValue

    
    def makeScale(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return TransformState._TransformState__overloaded_makeScale_float(_args[0])
            elif isinstance(_args[0], VBase3.VBase3):
                return TransformState._TransformState__overloaded_makeScale_ptrConstLVecBase3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3.VBase3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    makeScale = staticmethod(makeScale)

