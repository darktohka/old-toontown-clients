# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggCurve

class EggNurbsCurve(EggCurve.EggCurve, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EggNurbsCurve__overloaded_constructor_ptrConstEggNurbsCurve(self, copy):
        self.this = libpandaegg._inPkAOMSb5s(copy.this)
        self.userManagesMemory = 1

    
    def _EggNurbsCurve__overloaded_constructor_atomicstring(self, name):
        self.this = libpandaegg._inPkAOMqKMX(name)
        self.userManagesMemory = 1

    
    def _EggNurbsCurve__overloaded_constructor(self):
        self.this = libpandaegg._inPkAOM8ypa()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOMUWcZ:
            libpandaegg._inPkAOMUWcZ(self.this)
        

    
    def getClassType():
        returnValue = libpandaegg._inPkAOMTsQD()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOMetUP(self.this, copy.this)
        returnObject = EggNurbsCurve(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setup(self, order, numKnots):
        returnValue = libpandaegg._inPkAOM1I_P(self.this, order, numKnots)
        return returnValue

    
    def setOrder(self, order):
        returnValue = libpandaegg._inPkAOM6zeh(self.this, order)
        return returnValue

    
    def setNumKnots(self, num):
        returnValue = libpandaegg._inPkAOM_mS3(self.this, num)
        return returnValue

    
    def setKnot(self, k, value):
        returnValue = libpandaegg._inPkAOMsz1o(self.this, k, value)
        return returnValue

    
    def isValid(self):
        returnValue = libpandaegg._inPkAOMXgbF(self.this)
        return returnValue

    
    def getOrder(self):
        returnValue = libpandaegg._inPkAOMU0kx(self.this)
        return returnValue

    
    def getDegree(self):
        returnValue = libpandaegg._inPkAOMa0DG(self.this)
        return returnValue

    
    def getNumKnots(self):
        returnValue = libpandaegg._inPkAOMBXkq(self.this)
        return returnValue

    
    def getNumCvs(self):
        returnValue = libpandaegg._inPkAOMyBqz(self.this)
        return returnValue

    
    def isClosed(self):
        returnValue = libpandaegg._inPkAOM07Jv(self.this)
        return returnValue

    
    def getKnot(self, k):
        returnValue = libpandaegg._inPkAOMYx8U(self.this, k)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggNurbsCurve__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._EggNurbsCurve__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], EggNurbsCurve):
                return self._EggNurbsCurve__overloaded_constructor_ptrConstEggNurbsCurve(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <EggNurbsCurve> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


