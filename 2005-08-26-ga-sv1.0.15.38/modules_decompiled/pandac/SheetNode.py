# File: S (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import PandaNode

class SheetNode(PandaNode.PandaNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpanda._inPHc9WHNcz(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHc9Wt9L6:
            libpanda._inPHc9Wt9L6(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPHc9Wv2IZ()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setSurface(self, surface):
        returnValue = libpanda._inPHc9W0cvy(self.this, surface.this)
        return returnValue

    
    def getSurface(self):
        returnValue = libpanda._inPHc9W18wP(self.this)
        import NurbsSurfaceEvaluator
        returnObject = NurbsSurfaceEvaluator.NurbsSurfaceEvaluator(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setUseVertexColor(self, flag):
        returnValue = libpanda._inPHc9WYR_Z(self.this, flag)
        return returnValue

    
    def getUseVertexColor(self):
        returnValue = libpanda._inPHc9WE_yX(self.this)
        return returnValue

    
    def setNumUSubdiv(self, numUSubdiv):
        returnValue = libpanda._inPHc9WATi0(self.this, numUSubdiv)
        return returnValue

    
    def getNumUSubdiv(self):
        returnValue = libpanda._inPHc9Wor5e(self.this)
        return returnValue

    
    def setNumVSubdiv(self, numVSubdiv):
        returnValue = libpanda._inPHc9W65jU(self.this, numVSubdiv)
        return returnValue

    
    def getNumVSubdiv(self):
        returnValue = libpanda._inPHc9WkQ7_(self.this)
        return returnValue

    
    def resetBound(self, relTo):
        returnValue = libpanda._inPHc9WZQ8j(self.this, relTo.this)
        return returnValue


