# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggPrimitive

class EggPolygon(EggPrimitive.EggPrimitive, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EggPolygon__overloaded_constructor_ptrConstEggPolygon(self, copy):
        self.this = libpandaegg._inPkAOMXJZS(copy.this)
        self.userManagesMemory = 1

    
    def _EggPolygon__overloaded_constructor_atomicstring(self, name):
        self.this = libpandaegg._inPkAOMUWBj(name)
        self.userManagesMemory = 1

    
    def _EggPolygon__overloaded_constructor(self):
        self.this = libpandaegg._inPkAOMO3JE()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOMxjGA:
            libpandaegg._inPkAOMxjGA(self.this)
        

    
    def getClassType():
        returnValue = libpandaegg._inPkAOMuGjd()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOMG5ro(self.this, copy.this)
        returnObject = EggPolygon(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _EggPolygon__overloaded_calculateNormal_ptrConstEggPolygon_ptrLVector3d___enum__CoordinateSystem(self, result, cs):
        returnValue = libpandaegg._inPkAOM1KP0(self.this, result.this, cs)
        return returnValue

    
    def _EggPolygon__overloaded_calculateNormal_ptrConstEggPolygon_ptrLVector3d(self, result):
        returnValue = libpandaegg._inPkAOM7k0F(self.this, result.this)
        return returnValue

    
    def isPlanar(self):
        returnValue = libpandaegg._inPkAOMMiG7(self.this)
        return returnValue

    
    def _EggPolygon__overloaded_recomputePolygonNormal_ptrEggPolygon___enum__CoordinateSystem(self, cs):
        returnValue = libpandaegg._inPkAOMPIIR(self.this, cs)
        return returnValue

    
    def _EggPolygon__overloaded_recomputePolygonNormal_ptrEggPolygon(self):
        returnValue = libpandaegg._inPkAOM5vES(self.this)
        return returnValue

    
    def triangulateInto(self, container, convexAlso):
        returnValue = libpandaegg._inPkAOMMg0u(self.this, container.this, convexAlso)
        return returnValue

    
    def triangulateInPlace(self, convexAlso):
        returnValue = libpandaegg._inPkAOMdd1f(self.this, convexAlso)
        returnObject = EggPolygon(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggPolygon__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._EggPolygon__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], EggPolygon):
                return self._EggPolygon__overloaded_constructor_ptrConstEggPolygon(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <EggPolygon> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def calculateNormal(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._EggPolygon__overloaded_calculateNormal_ptrConstEggPolygon_ptrLVector3d(*_args)
        elif numArgs == 2:
            return self._EggPolygon__overloaded_calculateNormal_ptrConstEggPolygon_ptrLVector3d___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def recomputePolygonNormal(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggPolygon__overloaded_recomputePolygonNormal_ptrEggPolygon(*_args)
        elif numArgs == 1:
            return self._EggPolygon__overloaded_recomputePolygonNormal_ptrEggPolygon___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


