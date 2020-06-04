# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedReferenceCount

class DNASuitPoint(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    FRONTDOORPOINT = 1
    SIDEDOORPOINT = 2
    COGHQINPOINT = 3
    STREETPOINT = 0
    COGHQOUTPOINT = 4
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _DNASuitPoint__overloaded_constructor_int___enum__DNASuitPointType_ptrLPoint3f_int(self, index, type, pos, lbIndex):
        self.this = libtoontown._inPdt4yqaal(index, type, pos.this, lbIndex)
        self.userManagesMemory = 1

    
    def _DNASuitPoint__overloaded_constructor_int___enum__DNASuitPointType_ptrLPoint3f(self, index, type, pos):
        self.this = libtoontown._inPdt4yaogd(index, type, pos.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPdt4yqwXD:
            libtoontown._inPdt4yqwXD(self.this)
        

    
    def getClassType():
        returnValue = libtoontown._inPdt4y88If()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setIndex(self, index):
        returnValue = libtoontown._inPdt4y1KrK(self.this, index)
        return returnValue

    
    def getIndex(self):
        returnValue = libtoontown._inPdt4yTHKF(self.this)
        return returnValue

    
    def setPointType(self, type):
        returnValue = libtoontown._inPdt4yPzDT(self.this, type)
        return returnValue

    
    def getPointType(self):
        returnValue = libtoontown._inPdt4y9WF8(self.this)
        return returnValue

    
    def setPos(self, pos):
        returnValue = libtoontown._inPdt4ywt9s(self.this, pos.this)
        return returnValue

    
    def getPos(self):
        returnValue = libtoontown._inPdt4yoSRO(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setGraphId(self, graphId):
        returnValue = libtoontown._inPdt4yv3nG(self.this, graphId)
        return returnValue

    
    def getGraphId(self):
        returnValue = libtoontown._inPdt4yUczs(self.this)
        return returnValue

    
    def setLandmarkBuildingIndex(self, lbIndex):
        returnValue = libtoontown._inPdt4ygoF_(self.this, lbIndex)
        return returnValue

    
    def getLandmarkBuildingIndex(self):
        returnValue = libtoontown._inPdt4yTC6v(self.this)
        return returnValue

    
    def isTerminal(self):
        returnValue = libtoontown._inPdt4y_bKo(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libtoontown._inPdt4yRrxR(self.this, out.this)
        return returnValue

    
    def _DNASuitPoint__overloaded_write_ptrConstDNASuitPoint_ptrOstream_int(self, out, indentLevel):
        returnValue = libtoontown._inPdt4ys_3h(self.this, out.this, indentLevel)
        return returnValue

    
    def _DNASuitPoint__overloaded_write_ptrConstDNASuitPoint_ptrOstream(self, out):
        returnValue = libtoontown._inPdt4ynXK6(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 3:
            return self._DNASuitPoint__overloaded_constructor_int___enum__DNASuitPointType_ptrLPoint3f(*_args)
        elif numArgs == 4:
            return self._DNASuitPoint__overloaded_constructor_int___enum__DNASuitPointType_ptrLPoint3f_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._DNASuitPoint__overloaded_write_ptrConstDNASuitPoint_ptrOstream(*_args)
        elif numArgs == 2:
            return self._DNASuitPoint__overloaded_write_ptrConstDNASuitPoint_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


