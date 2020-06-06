# File: L (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import PandaNode

class LensNode(PandaNode.PandaNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self, name):
        self.this = libpanda._inPkJyoZGLe(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPkJyo10eB:
            libpanda._inPkJyo10eB(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPkJyoF6_K()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def copyLens(self, lens):
        returnValue = libpanda._inPkJyo1vNW(self.this, lens.this)
        return returnValue

    
    def setLens(self, lens):
        returnValue = libpanda._inPkJyo_2fA(self.this, lens.this)
        return returnValue

    
    def getLens(self):
        returnValue = libpanda._inPkJyoC5Ow(self.this)
        import Lens
        returnObject = Lens.Lens(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def isInView(self, pos):
        returnValue = libpanda._inPkJyoVo66(self.this, pos.this)
        return returnValue


