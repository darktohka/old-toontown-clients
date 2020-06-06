# File: N (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import ReferenceCount

class NurbsCurveResult(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
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
        if libpanda and libpanda._inPHc9W0sXG:
            libpanda._inPHc9W0sXG(self.this)
        

    
    def getStartT(self):
        returnValue = libpanda._inPHc9WNf1r(self.this)
        return returnValue

    
    def getEndT(self):
        returnValue = libpanda._inPHc9WPEFs(self.this)
        return returnValue

    
    def evalPoint(self, t, point):
        returnValue = libpanda._inPHc9Wkne8(self.this, t, point.this)
        return returnValue

    
    def evalTangent(self, t, tangent):
        returnValue = libpanda._inPHc9WHZT_(self.this, t, tangent.this)
        return returnValue

    
    def evalExtendedPoint(self, t, d):
        returnValue = libpanda._inPHc9WYSlj(self.this, t, d)
        return returnValue

    
    def getNumSegments(self):
        returnValue = libpanda._inPHc9Ww2Tl(self.this)
        return returnValue

    
    def evalSegmentPoint(self, segment, t, point):
        returnValue = libpanda._inPHc9WiDoh(self.this, segment, t, point.this)
        return returnValue

    
    def evalSegmentTangent(self, segment, t, tangent):
        returnValue = libpanda._inPHc9WNjKk(self.this, segment, t, tangent.this)
        return returnValue

    
    def evalSegmentExtendedPoint(self, segment, t, d):
        returnValue = libpanda._inPHc9Wtc44(self.this, segment, t, d)
        return returnValue

    
    def getSegmentT(self, segment, t):
        returnValue = libpanda._inPHc9W6YrI(self.this, segment, t)
        return returnValue


