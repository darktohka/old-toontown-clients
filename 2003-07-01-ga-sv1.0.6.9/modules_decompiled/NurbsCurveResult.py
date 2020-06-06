# File: N (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ReferenceCount

class NurbsCurveResult(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
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
        

    
    def destructor(self):
        if libpanda and libpanda._inPHc9W0sXG:
            libpanda._inPHc9W0sXG(self.this)
        

    
    def getStartT(self):
        returnValue = libpanda._inPHc9WMf1r(self.this)
        return returnValue

    
    def getEndT(self):
        returnValue = libpanda._inPHc9WIEFs(self.this)
        return returnValue

    
    def evalPoint(self, t, point):
        returnValue = libpanda._inPHc9Wlne8(self.this, t, point.this)
        return returnValue

    
    def evalTangent(self, t, tangent):
        returnValue = libpanda._inPHc9WIZT_(self.this, t, tangent.this)
        return returnValue

    
    def getNumSegments(self):
        returnValue = libpanda._inPHc9Wx2Tl(self.this)
        return returnValue

    
    def evalSegmentPoint(self, segment, t, point):
        returnValue = libpanda._inPHc9WlDoh(self.this, segment, t, point.this)
        return returnValue

    
    def evalSegmentTangent(self, segment, t, tangent):
        returnValue = libpanda._inPHc9WOjKk(self.this, segment, t, tangent.this)
        return returnValue

    
    def getSegmentT(self, segment, t):
        returnValue = libpanda._inPHc9W6YrI(self.this, segment, t)
        return returnValue


