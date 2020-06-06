# File: L (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import LinearForce

class LinearCylinderVortexForce(LinearForce.LinearForce, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _LinearCylinderVortexForce__overloaded_constructor_ptrConstLinearCylinderVortexForce(self, copy):
        self.this = libpandaphysics._inP9fJJ255x(copy.this)
        self.userManagesMemory = 1

    
    def _LinearCylinderVortexForce__overloaded_constructor_float_float_float_float_bool(self, radius, length, coef, a, md):
        self.this = libpandaphysics._inP9fJJYCN4(radius, length, coef, a, md)
        self.userManagesMemory = 1

    
    def _LinearCylinderVortexForce__overloaded_constructor_float_float_float_float(self, radius, length, coef, a):
        self.this = libpandaphysics._inP9fJJCnEA(radius, length, coef, a)
        self.userManagesMemory = 1

    
    def _LinearCylinderVortexForce__overloaded_constructor_float_float_float(self, radius, length, coef):
        self.this = libpandaphysics._inP9fJJStkP(radius, length, coef)
        self.userManagesMemory = 1

    
    def _LinearCylinderVortexForce__overloaded_constructor_float_float(self, radius, length):
        self.this = libpandaphysics._inP9fJJfl9B(radius, length)
        self.userManagesMemory = 1

    
    def _LinearCylinderVortexForce__overloaded_constructor_float(self, radius):
        self.this = libpandaphysics._inP9fJJTc4_(radius)
        self.userManagesMemory = 1

    
    def _LinearCylinderVortexForce__overloaded_constructor(self):
        self.this = libpandaphysics._inP9fJJE3hd()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpandaphysics._inP9fJJcafq()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setCoef(self, coef):
        returnValue = libpandaphysics._inP9fJJelCt(self.this, coef)
        return returnValue

    
    def getCoef(self):
        returnValue = libpandaphysics._inP9fJJaM30(self.this)
        return returnValue

    
    def setRadius(self, radius):
        returnValue = libpandaphysics._inP9fJJeg2d(self.this, radius)
        return returnValue

    
    def getRadius(self):
        returnValue = libpandaphysics._inP9fJJBbDi(self.this)
        return returnValue

    
    def setLength(self, length):
        returnValue = libpandaphysics._inP9fJJuquM(self.this, length)
        return returnValue

    
    def getLength(self):
        returnValue = libpandaphysics._inP9fJJ_n8Q(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._LinearCylinderVortexForce__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._LinearCylinderVortexForce__overloaded_constructor_float(_args[0])
            elif isinstance(_args[0], LinearCylinderVortexForce):
                return self._LinearCylinderVortexForce__overloaded_constructor_ptrConstLinearCylinderVortexForce(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <LinearCylinderVortexForce> '
        elif numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._LinearCylinderVortexForce__overloaded_constructor_float_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._LinearCylinderVortexForce__overloaded_constructor_float_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 4:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._LinearCylinderVortexForce__overloaded_constructor_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 5:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            if isinstance(_args[4], types.IntType):
                                return self._LinearCylinderVortexForce__overloaded_constructor_float_float_float_float_bool(_args[0], _args[1], _args[2], _args[3], _args[4])
                            else:
                                raise TypeError, 'Invalid argument 4, expected one of: <types.IntType> '
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 3 4 5 '


