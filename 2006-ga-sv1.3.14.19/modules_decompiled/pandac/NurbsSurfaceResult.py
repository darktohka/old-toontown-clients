# File: N (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import ReferenceCount

class NurbsSurfaceResult(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
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
        if libpanda and libpanda._inPHc9WnrIg:
            libpanda._inPHc9WnrIg(self.this)
        

    
    def getStartU(self):
        returnValue = libpanda._inPHc9WlxRL(self.this)
        return returnValue

    
    def getEndU(self):
        returnValue = libpanda._inPHc9WxP5f(self.this)
        return returnValue

    
    def getStartV(self):
        returnValue = libpanda._inPHc9WlIgM(self.this)
        return returnValue

    
    def getEndV(self):
        returnValue = libpanda._inPHc9WJL57(self.this)
        return returnValue

    
    def evalPoint(self, u, v, point):
        returnValue = libpanda._inPHc9WtQQk(self.this, u, v, point.this)
        return returnValue

    
    def evalNormal(self, u, v, normal):
        returnValue = libpanda._inPHc9W_6lV(self.this, u, v, normal.this)
        return returnValue

    
    def evalExtendedPoint(self, u, v, d):
        returnValue = libpanda._inPHc9W9yzI(self.this, u, v, d)
        return returnValue

    
    def getNumUSegments(self):
        returnValue = libpanda._inPHc9WQs85(self.this)
        return returnValue

    
    def getNumVSegments(self):
        returnValue = libpanda._inPHc9WZT9V(self.this)
        return returnValue

    
    def evalSegmentPoint(self, ui, vi, u, v, point):
        returnValue = libpanda._inPHc9WqiBr(self.this, ui, vi, u, v, point.this)
        return returnValue

    
    def evalSegmentNormal(self, ui, vi, u, v, normal):
        returnValue = libpanda._inPHc9WmDzQ(self.this, ui, vi, u, v, normal.this)
        return returnValue

    
    def evalSegmentExtendedPoint(self, ui, vi, u, v, d):
        returnValue = libpanda._inPHc9WZ0qy(self.this, ui, vi, u, v, d)
        return returnValue

    
    def getSegmentU(self, ui, u):
        returnValue = libpanda._inPHc9WPEBw(self.this, ui, u)
        return returnValue

    
    def getSegmentV(self, vi, v):
        returnValue = libpanda._inPHc9WTExR(self.this, vi, v)
        return returnValue


