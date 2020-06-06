# File: R (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class ReferenceCount(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
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
        returnValue = libpandaexpress._inPJoxtn3ZO()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getRefCount(self):
        returnValue = libpandaexpress._inPJoxtM11_(self.this)
        return returnValue

    
    def ref(self):
        returnValue = libpandaexpress._inPJoxtVS5_(self.this)
        return returnValue

    
    def unref(self):
        returnValue = libpandaexpress._inPJoxtzyVy(self.this)
        return returnValue

    
    def testRefCountIntegrity(self):
        returnValue = libpandaexpress._inPJoxtupj2(self.this)
        return returnValue


