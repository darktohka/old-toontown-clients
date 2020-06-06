# File: T (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class TypeRegistry(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxtxkrK:
            libpandaexpress._inPKoxtxkrK(self.this)
        

    
    def reregisterTypes():
        returnValue = libpandaexpress._inPKoxt5_p8()
        return returnValue

    reregisterTypes = staticmethod(reregisterTypes)
    
    def ptr():
        returnValue = libpandaexpress._inPKoxtuwsa()
        returnObject = TypeRegistry(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    ptr = staticmethod(ptr)
    
    def findType(self, name):
        returnValue = libpandaexpress._inPKoxtx9n6(self.this, name)
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getName(self, type, object):
        returnValue = libpandaexpress._inPKoxt5DEU(self.this, type.this, object.this)
        return returnValue

    
    def isDerivedFrom(self, child, base, childObject):
        returnValue = libpandaexpress._inPKoxtMBOu(self.this, child.this, base.this, childObject.this)
        return returnValue

    
    def getNumRootClasses(self):
        returnValue = libpandaexpress._inPKoxtPxO1(self.this)
        return returnValue

    
    def getRootClass(self, n):
        returnValue = libpandaexpress._inPKoxtLFNI(self.this, n)
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getNumParentClasses(self, child, childObject):
        returnValue = libpandaexpress._inPKoxtlx7d(self.this, child.this, childObject.this)
        return returnValue

    
    def getParentClass(self, child, index):
        returnValue = libpandaexpress._inPKoxt4LWH(self.this, child.this, index)
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getNumChildClasses(self, child, childObject):
        returnValue = libpandaexpress._inPKoxtmVbL(self.this, child.this, childObject.this)
        return returnValue

    
    def getChildClass(self, child, index):
        returnValue = libpandaexpress._inPKoxtfTRM(self.this, child.this, index)
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getParentTowards(self, child, base, childObject):
        returnValue = libpandaexpress._inPKoxt3YQ7(self.this, child.this, base.this, childObject.this)
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def write(self, out):
        returnValue = libpandaexpress._inPKoxteZEC(self.this, out.this)
        return returnValue


