# File: B (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TypedReferenceCount

class BoundingVolume(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    IFAll = 4
    IFNoIntersection = 0
    IFDontUnderstand = 8
    IFPossible = 1
    IFSome = 2
    
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
        

    
    def destructor(self):
        if libpanda and libpanda._inPSkjP0loB:
            libpanda._inPSkjP0loB(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPSkjP0fVo()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def makeCopy(self):
        returnValue = libpanda._inPSkjPi4zP(self.this)
        returnObject = BoundingVolume(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def isEmpty(self):
        returnValue = libpanda._inPSkjPVfqL(self.this)
        return returnValue

    
    def isInfinite(self):
        returnValue = libpanda._inPSkjPFsFC(self.this)
        return returnValue

    
    def setInfinite(self):
        returnValue = libpanda._inPSkjPA2hm(self.this)
        return returnValue

    
    def extendBy(self, vol):
        returnValue = libpanda._inPSkjPBRix(self.this, vol.this)
        return returnValue

    
    def contains(self, vol):
        returnValue = libpanda._inPSkjPdpPR(self.this, vol.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPSkjPQbvQ(self.this, out.this)
        return returnValue

    
    def _BoundingVolume__overloaded_write_ptrConstBoundingVolume_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPSkjPIz6_(self.this, out.this, indentLevel)
        return returnValue

    
    def _BoundingVolume__overloaded_write_ptrConstBoundingVolume_ptrOstream(self, out):
        returnValue = libpanda._inPSkjPZ2qR(self.this, out.this)
        return returnValue

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._BoundingVolume__overloaded_write_ptrConstBoundingVolume_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._BoundingVolume__overloaded_write_ptrConstBoundingVolume_ptrOstream_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


