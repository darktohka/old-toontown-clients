# File: M (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class MaterialPool(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
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
        if libpanda and libpanda._inPMAKPG26j:
            libpanda._inPMAKPG26j(self.this)
        

    
    def getMaterial(temp):
        returnValue = libpanda._inPMAKPNuX5(temp.this)
        import Material
        returnObject = Material.Material(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    getMaterial = staticmethod(getMaterial)
    
    def garbageCollect():
        returnValue = libpanda._inPMAKPXM0z()
        return returnValue

    garbageCollect = staticmethod(garbageCollect)
    
    def listContents(out):
        returnValue = libpanda._inPMAKP5ZKx(out.this)
        return returnValue

    listContents = staticmethod(listContents)

