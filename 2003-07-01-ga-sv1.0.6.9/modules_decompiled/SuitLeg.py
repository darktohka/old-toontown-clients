# File: S (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import FFIExternalObject

class SuitLeg(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts]
    TBellicose = 2
    TToToonBuilding = 7
    TToSky = 4
    TToSuitBuilding = 6
    TWalkToStreet = 1
    TFromSky = 3
    TWalkFromStreet = 0
    TFromSuitBuilding = 5
    TOff = 8
    
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
        if libtoontown and libtoontown._inPdPJOYNMj:
            libtoontown._inPdPJOYNMj(self.this)
        

    
    def getTypeName(type):
        returnValue = libtoontown._inPdPJOoT06(type)
        return returnValue

    getTypeName = staticmethod(getTypeName)
    
    def getType(self):
        returnValue = libtoontown._inPdPJOAZxb(self.this)
        return returnValue

    
    def getStartTime(self):
        returnValue = libtoontown._inPdPJO5StD(self.this)
        return returnValue

    
    def getLegTime(self):
        returnValue = libtoontown._inPdPJOuXv5(self.this)
        return returnValue

    
    def getZoneId(self):
        returnValue = libtoontown._inPdPJOD_t_(self.this)
        return returnValue

    
    def getPointA(self):
        returnValue = libtoontown._inPdPJOAiby(self.this)
        return returnValue

    
    def getPointB(self):
        returnValue = libtoontown._inPdPJOMFcS(self.this)
        return returnValue

    
    def getPosA(self):
        returnValue = libtoontown._inPdPJOAQBi(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getPosB(self):
        returnValue = libtoontown._inPdPJOGQP_(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getPosAtTime(self, time):
        returnValue = libtoontown._inPdPJOCQI5(self.this, time)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def output(self, out):
        returnValue = libtoontown._inPdPJO0B4j(self.this, out.this)
        return returnValue


