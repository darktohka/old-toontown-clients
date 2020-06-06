# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggGroupNode

class EggXfmSAnim(EggGroupNode.EggGroupNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EggXfmSAnim__overloaded_constructor_ptrConstEggXfmAnimData(self, convertFrom):
        self.this = libpandaegg._inPkAOMRYEx(convertFrom.this)
        self.userManagesMemory = 1

    
    def _EggXfmSAnim__overloaded_constructor_ptrConstEggXfmSAnim(self, copy):
        self.this = libpandaegg._inPkAOMmYOa(copy.this)
        self.userManagesMemory = 1

    
    def _EggXfmSAnim__overloaded_constructor_atomicstring___enum__CoordinateSystem(self, name, cs):
        self.this = libpandaegg._inPkAOMcgvp(name, cs)
        self.userManagesMemory = 1

    
    def _EggXfmSAnim__overloaded_constructor_atomicstring(self, name):
        self.this = libpandaegg._inPkAOM7lEE(name)
        self.userManagesMemory = 1

    
    def _EggXfmSAnim__overloaded_constructor(self):
        self.this = libpandaegg._inPkAOMg0m6()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOMOgBB:
            libpandaegg._inPkAOMOgBB(self.this)
        

    
    def getStandardOrder():
        returnValue = libpandaegg._inPkAOMAIxi()
        return returnValue

    getStandardOrder = staticmethod(getStandardOrder)
    
    def composeWithOrder(mat, scale, shear, hpr, trans, order, cs):
        returnValue = libpandaegg._inPkAOM3FmY(mat.this, scale.this, shear.this, hpr.this, trans.this, order, cs)
        return returnValue

    composeWithOrder = staticmethod(composeWithOrder)
    
    def getClassType():
        returnValue = libpandaegg._inPkAOMm6HI()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOMBbhs(self.this, copy.this)
        returnObject = EggXfmSAnim(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setFps(self, fps):
        returnValue = libpandaegg._inPkAOMsNjA(self.this, fps)
        return returnValue

    
    def clearFps(self):
        returnValue = libpandaegg._inPkAOM6b_o(self.this)
        return returnValue

    
    def hasFps(self):
        returnValue = libpandaegg._inPkAOMfhuX(self.this)
        return returnValue

    
    def getFps(self):
        returnValue = libpandaegg._inPkAOMngbU(self.this)
        return returnValue

    
    def setOrder(self, order):
        returnValue = libpandaegg._inPkAOMW2jL(self.this, order)
        return returnValue

    
    def clearOrder(self):
        returnValue = libpandaegg._inPkAOMfUuB(self.this)
        return returnValue

    
    def hasOrder(self):
        returnValue = libpandaegg._inPkAOM2pYT(self.this)
        return returnValue

    
    def getOrder(self):
        returnValue = libpandaegg._inPkAOMcqDQ(self.this)
        return returnValue

    
    def getCoordinateSystem(self):
        returnValue = libpandaegg._inPkAOMnUlS(self.this)
        return returnValue

    
    def optimize(self):
        returnValue = libpandaegg._inPkAOMqvPQ(self.this)
        return returnValue

    
    def optimizeToStandardOrder(self):
        returnValue = libpandaegg._inPkAOMga25(self.this)
        return returnValue

    
    def normalize(self):
        returnValue = libpandaegg._inPkAOMsVux(self.this)
        return returnValue

    
    def getNumRows(self):
        returnValue = libpandaegg._inPkAOMXO7Q(self.this)
        return returnValue

    
    def getValue(self, row, mat):
        returnValue = libpandaegg._inPkAOM4L7T(self.this, row, mat.this)
        return returnValue

    
    def setValue(self, row, mat):
        returnValue = libpandaegg._inPkAOMIeZX(self.this, row, mat.this)
        return returnValue

    
    def clearData(self):
        returnValue = libpandaegg._inPkAOM4n4x(self.this)
        return returnValue

    
    def addData(self, mat):
        returnValue = libpandaegg._inPkAOMCJDG(self.this, mat.this)
        return returnValue

    
    def _EggXfmSAnim__overloaded_addComponentData_ptrEggXfmSAnim_atomicstring_double(self, componentName, value):
        returnValue = libpandaegg._inPkAOMAOJJ(self.this, componentName, value)
        return returnValue

    
    def _EggXfmSAnim__overloaded_addComponentData_ptrEggXfmSAnim_int_double(self, component, value):
        returnValue = libpandaegg._inPkAOMXAkq(self.this, component, value)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggXfmSAnim__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._EggXfmSAnim__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], EggXfmSAnim):
                return self._EggXfmSAnim__overloaded_constructor_ptrConstEggXfmSAnim(*_args)
            
            import EggXfmAnimData
            if isinstance(_args[0], EggXfmAnimData.EggXfmAnimData):
                return self._EggXfmSAnim__overloaded_constructor_ptrConstEggXfmAnimData(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <EggXfmSAnim> <EggXfmAnimData.EggXfmAnimData> '
        elif numArgs == 2:
            return self._EggXfmSAnim__overloaded_constructor_atomicstring___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def addComponentData(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._EggXfmSAnim__overloaded_addComponentData_ptrEggXfmSAnim_int_double(*_args)
            
            if isinstance(_args[0], types.StringType):
                return self._EggXfmSAnim__overloaded_addComponentData_ptrEggXfmSAnim_atomicstring_double(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '


