# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggAnimData

class EggXfmAnimData(EggAnimData.EggAnimData, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EggXfmAnimData__overloaded_constructor_ptrConstEggXfmAnimData(self, copy):
        self.this = libpandaegg._inPkAOMb2RM(copy.this)
        self.userManagesMemory = 1

    
    def _EggXfmAnimData__overloaded_constructor_ptrConstEggXfmSAnim(self, convertFrom):
        self.this = libpandaegg._inPkAOMIOPW(convertFrom.this)
        self.userManagesMemory = 1

    
    def _EggXfmAnimData__overloaded_constructor_atomicstring___enum__CoordinateSystem(self, name, cs):
        self.this = libpandaegg._inPkAOM4g06(name, cs)
        self.userManagesMemory = 1

    
    def _EggXfmAnimData__overloaded_constructor_atomicstring(self, name):
        self.this = libpandaegg._inPkAOMwzqM(name)
        self.userManagesMemory = 1

    
    def _EggXfmAnimData__overloaded_constructor(self):
        self.this = libpandaegg._inPkAOM9omr()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOMGLCf:
            libpandaegg._inPkAOMGLCf(self.this)
        

    
    def getStandardOrder():
        returnValue = libpandaegg._inPkAOM4nKv()
        return returnValue

    getStandardOrder = staticmethod(getStandardOrder)
    
    def getClassType():
        returnValue = libpandaegg._inPkAOM0uoj()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOMuTJ7(self.this, copy.this)
        returnObject = EggXfmAnimData(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setOrder(self, order):
        returnValue = libpandaegg._inPkAOMQOOI(self.this, order)
        return returnValue

    
    def clearOrder(self):
        returnValue = libpandaegg._inPkAOMF43l(self.this)
        return returnValue

    
    def hasOrder(self):
        returnValue = libpandaegg._inPkAOMpqB7(self.this)
        return returnValue

    
    def getOrder(self):
        returnValue = libpandaegg._inPkAOMxPBu(self.this)
        return returnValue

    
    def setContents(self, contents):
        returnValue = libpandaegg._inPkAOMf_7y(self.this, contents)
        return returnValue

    
    def clearContents(self):
        returnValue = libpandaegg._inPkAOMCl5p(self.this)
        return returnValue

    
    def hasContents(self):
        returnValue = libpandaegg._inPkAOMjktg(self.this)
        return returnValue

    
    def getContents(self):
        returnValue = libpandaegg._inPkAOMbBtT(self.this)
        return returnValue

    
    def getCoordinateSystem(self):
        returnValue = libpandaegg._inPkAOMFVWG(self.this)
        return returnValue

    
    def getNumRows(self):
        returnValue = libpandaegg._inPkAOMjSnu(self.this)
        return returnValue

    
    def getNumCols(self):
        returnValue = libpandaegg._inPkAOMf3hX(self.this)
        return returnValue

    
    def _EggXfmAnimData__overloaded_getValue_ptrConstEggXfmAnimData_int_ptrLMatrix4d(self, row, mat):
        returnValue = libpandaegg._inPkAOMNC28(self.this, row, mat.this)
        return returnValue

    
    def _EggXfmAnimData__overloaded_getValue_ptrConstEggXfmAnimData_int_int(self, row, col):
        returnValue = libpandaegg._inPkAOM_V0v(self.this, row, col)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggXfmAnimData__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._EggXfmAnimData__overloaded_constructor_atomicstring(*_args)
            
            import EggXfmSAnim
            if isinstance(_args[0], EggXfmSAnim.EggXfmSAnim):
                return self._EggXfmAnimData__overloaded_constructor_ptrConstEggXfmSAnim(*_args)
            
            if isinstance(_args[0], EggXfmAnimData):
                return self._EggXfmAnimData__overloaded_constructor_ptrConstEggXfmAnimData(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <EggXfmSAnim.EggXfmSAnim> <EggXfmAnimData> '
        elif numArgs == 2:
            return self._EggXfmAnimData__overloaded_constructor_atomicstring___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def getValue(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                if isinstance(_args[1], types.IntType) or isinstance(_args[1], types.LongType):
                    return self._EggXfmAnimData__overloaded_getValue_ptrConstEggXfmAnimData_int_int(*_args)
                
                import Mat4D
                if isinstance(_args[1], Mat4D.Mat4D):
                    return self._EggXfmAnimData__overloaded_getValue_ptrConstEggXfmAnimData_int_ptrLMatrix4d(*_args)
                
                raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> <Mat4D.Mat4D> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '


