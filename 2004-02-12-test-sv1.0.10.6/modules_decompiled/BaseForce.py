# File: B (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TypedReferenceCount

class BaseForce(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
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
        

    
    def getClassType():
        returnValue = libpandaphysics._inP9fJJ2Xv7()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getActive(self):
        returnValue = libpandaphysics._inP9fJJjE3t(self.this)
        return returnValue

    
    def setActive(self, active):
        returnValue = libpandaphysics._inP9fJJQQYE(self.this, active)
        return returnValue

    
    def isLinear(self):
        returnValue = libpandaphysics._inP9fJJx2t9(self.this)
        return returnValue

    
    def getForceNode(self):
        returnValue = libpandaphysics._inP9fJJ_1U0(self.this)
        import ForceNode
        returnObject = ForceNode.ForceNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def getVector(self, po):
        returnValue = libpandaphysics._inP9fJJ7Jvx(self.this, po.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def output(self, out):
        returnValue = libpandaphysics._inP9fJJbo8P(self.this, out.this)
        return returnValue

    
    def _BaseForce__overloaded_write_ptrConstBaseForce_ptrOstream_unsignedint(self, out, indent):
        returnValue = libpandaphysics._inP9fJJ_ya5(self.this, out.this, indent)
        return returnValue

    
    def _BaseForce__overloaded_write_ptrConstBaseForce_ptrOstream(self, out):
        returnValue = libpandaphysics._inP9fJJeSbQ(self.this, out.this)
        return returnValue

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._BaseForce__overloaded_write_ptrConstBaseForce_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._BaseForce__overloaded_write_ptrConstBaseForce_ptrOstream_unsignedint(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


