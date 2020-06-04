# File: P (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TypedReferenceCount

class Physical(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _Physical__overloaded_constructor_ptrConstPhysical(self, copy):
        self.this = libpandaphysics._inP9fJJqW30(copy.this)
        self.userManagesMemory = 1

    
    def _Physical__overloaded_constructor_int_bool(self, totalObjects, preAlloc):
        self.this = libpandaphysics._inP9fJJvRxK(totalObjects, preAlloc)
        self.userManagesMemory = 1

    
    def _Physical__overloaded_constructor_int(self, totalObjects):
        self.this = libpandaphysics._inP9fJJ36xJ(totalObjects)
        self.userManagesMemory = 1

    
    def _Physical__overloaded_constructor(self):
        self.this = libpandaphysics._inP9fJJRZEx()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpandaphysics._inP9fJJ5K_k()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getPhysicsManager(self):
        returnValue = libpandaphysics._inP9fJJGnHU(self.this)
        import PhysicsManager
        returnObject = PhysicsManager.PhysicsManager(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getPhysicalNode(self):
        returnValue = libpandaphysics._inP9fJJ_v4Q(self.this)
        import PhysicalNode
        returnObject = PhysicalNode.PhysicalNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def getPhysBody(self):
        returnValue = libpandaphysics._inP9fJJQp7H(self.this)
        import PhysicsObject
        returnObject = PhysicsObject.PhysicsObject(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def clearLinearForces(self):
        returnValue = libpandaphysics._inP9fJJnJZ_(self.this)
        return returnValue

    
    def clearAngularForces(self):
        returnValue = libpandaphysics._inP9fJJY7oN(self.this)
        return returnValue

    
    def clearPhysicsObjects(self):
        returnValue = libpandaphysics._inP9fJJJunY(self.this)
        return returnValue

    
    def addLinearForce(self, f):
        returnValue = libpandaphysics._inP9fJJYy0c(self.this, f.this)
        return returnValue

    
    def addAngularForce(self, f):
        returnValue = libpandaphysics._inP9fJJnNNk(self.this, f.this)
        return returnValue

    
    def addPhysicsObject(self, po):
        returnValue = libpandaphysics._inP9fJJHrhr(self.this, po.this)
        return returnValue

    
    def removeLinearForce(self, f):
        returnValue = libpandaphysics._inP9fJJqkU3(self.this, f.this)
        return returnValue

    
    def removeAngularForce(self, f):
        returnValue = libpandaphysics._inP9fJJ3L9H(self.this, f.this)
        return returnValue

    
    def getNumLinearForces(self):
        returnValue = libpandaphysics._inP9fJJ_ygv(self.this)
        return returnValue

    
    def getLinearForce(self, index):
        returnValue = libpandaphysics._inP9fJJOUJj(self.this, index)
        import LinearForce
        returnObject = LinearForce.LinearForce(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNumAngularForces(self):
        returnValue = libpandaphysics._inP9fJJItUr(self.this)
        return returnValue

    
    def getAngularForce(self, index):
        returnValue = libpandaphysics._inP9fJJAVLw(self.this, index)
        import AngularForce
        returnObject = AngularForce.AngularForce(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setViscosity(self, viscosity):
        returnValue = libpandaphysics._inP9fJJMcA4(self.this, viscosity)
        return returnValue

    
    def getViscosity(self):
        returnValue = libpandaphysics._inP9fJJOx2x(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaphysics._inP9fJJ9XnP(self.this, out.this)
        return returnValue

    
    def _Physical__overloaded_writePhysicsObjects_ptrConstPhysical_ptrOstream_unsignedint(self, out, indent):
        returnValue = libpandaphysics._inP9fJJPTed(self.this, out.this, indent)
        return returnValue

    
    def _Physical__overloaded_writePhysicsObjects_ptrConstPhysical_ptrOstream(self, out):
        returnValue = libpandaphysics._inP9fJJ0ZIV(self.this, out.this)
        return returnValue

    
    def _Physical__overloaded_writeLinearForces_ptrConstPhysical_ptrOstream_unsignedint(self, out, indent):
        returnValue = libpandaphysics._inP9fJJclJe(self.this, out.this, indent)
        return returnValue

    
    def _Physical__overloaded_writeLinearForces_ptrConstPhysical_ptrOstream(self, out):
        returnValue = libpandaphysics._inP9fJJZ_4i(self.this, out.this)
        return returnValue

    
    def _Physical__overloaded_writeAngularForces_ptrConstPhysical_ptrOstream_unsignedint(self, out, indent):
        returnValue = libpandaphysics._inP9fJJIy5h(self.this, out.this, indent)
        return returnValue

    
    def _Physical__overloaded_writeAngularForces_ptrConstPhysical_ptrOstream(self, out):
        returnValue = libpandaphysics._inP9fJJWdr3(self.this, out.this)
        return returnValue

    
    def _Physical__overloaded_write_ptrConstPhysical_ptrOstream_unsignedint(self, out, indent):
        returnValue = libpandaphysics._inP9fJJq83C(self.this, out.this, indent)
        return returnValue

    
    def _Physical__overloaded_write_ptrConstPhysical_ptrOstream(self, out):
        returnValue = libpandaphysics._inP9fJJTZoV(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Physical__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._Physical__overloaded_constructor_int(_args[0])
            elif isinstance(_args[0], Physical):
                return self._Physical__overloaded_constructor_ptrConstPhysical(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <Physical> '
        elif numArgs == 2:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.IntType):
                    return self._Physical__overloaded_constructor_int_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._Physical__overloaded_write_ptrConstPhysical_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._Physical__overloaded_write_ptrConstPhysical_ptrOstream_unsignedint(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def writePhysicsObjects(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._Physical__overloaded_writePhysicsObjects_ptrConstPhysical_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._Physical__overloaded_writePhysicsObjects_ptrConstPhysical_ptrOstream_unsignedint(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def writeLinearForces(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._Physical__overloaded_writeLinearForces_ptrConstPhysical_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._Physical__overloaded_writeLinearForces_ptrConstPhysical_ptrOstream_unsignedint(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def writeAngularForces(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._Physical__overloaded_writeAngularForces_ptrConstPhysical_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._Physical__overloaded_writeAngularForces_ptrConstPhysical_ptrOstream_unsignedint(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


