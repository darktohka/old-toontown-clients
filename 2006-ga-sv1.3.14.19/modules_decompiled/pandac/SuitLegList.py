# File: S (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
from direct.ffi import FFIExternalObject

class SuitLegList(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, path, storage, suitWalkSpeed, fromSkyTime, toSkyTime, fromSuitBuildingTime, toSuitBuildingTime, toToonBuildingTime):
        self.this = libtoontown._inPdPJOzejz(path.this, storage.this, suitWalkSpeed, fromSkyTime, toSkyTime, fromSuitBuildingTime, toSuitBuildingTime, toToonBuildingTime)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPdPJO2LSu:
            libtoontown._inPdPJO2LSu(self.this)
        

    
    def getNumLegs(self):
        returnValue = libtoontown._inPdPJOiBz_(self.this)
        return returnValue

    
    def getLeg(self, n):
        returnValue = libtoontown._inPdPJOfTx7(self.this, n)
        import SuitLeg
        returnObject = SuitLeg.SuitLeg(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def __getitem__(self, n):
        returnValue = libtoontown._inPdPJOaX3E(self.this, n)
        import SuitLeg
        returnObject = SuitLeg.SuitLeg(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getLegIndexAtTime(self, time, start):
        returnValue = libtoontown._inPdPJODW6Z(self.this, time, start)
        return returnValue

    
    def getType(self, n):
        returnValue = libtoontown._inPdPJOOGbg(self.this, n)
        return returnValue

    
    def getStartTime(self, n):
        returnValue = libtoontown._inPdPJOdbo9(self.this, n)
        return returnValue

    
    def getLegTime(self, n):
        returnValue = libtoontown._inPdPJO6Pm1(self.this, n)
        return returnValue

    
    def getZoneId(self, n):
        returnValue = libtoontown._inPdPJOKCGY(self.this, n)
        return returnValue

    
    def getBlockNumber(self, n):
        returnValue = libtoontown._inPdPJO9bGq(self.this, n)
        return returnValue

    
    def getPointA(self, n):
        returnValue = libtoontown._inPdPJOYFQP(self.this, n)
        return returnValue

    
    def getPointB(self, n):
        returnValue = libtoontown._inPdPJOkGQd(self.this, n)
        return returnValue

    
    def isPointInRange(self, point, begin, end):
        returnValue = libtoontown._inPdPJOIgCC(self.this, point.this, begin, end)
        return returnValue

    
    def output(self, out):
        returnValue = libtoontown._inPdPJOmAhd(self.this, out.this)
        return returnValue

    
    def write(self, out):
        returnValue = libtoontown._inPdPJOe8xK(self.this, out.this)
        return returnValue


