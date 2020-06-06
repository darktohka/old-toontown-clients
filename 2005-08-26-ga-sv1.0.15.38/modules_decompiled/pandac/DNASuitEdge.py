# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedReferenceCount

class DNASuitEdge(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, startPoint, endPoint, zoneId):
        self.this = libtoontown._inPdt4yL1XC(startPoint.this, endPoint.this, zoneId)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPdt4yazsM:
            libtoontown._inPdt4yazsM(self.this)
        

    
    def getClassType():
        returnValue = libtoontown._inPdt4yOVpE()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def eq(self, other):
        returnValue = libtoontown._inPdt4yiUCU(self.this, other.this)
        return returnValue

    
    def getStartPoint(self):
        returnValue = libtoontown._inPdt4yh728(self.this)
        import DNASuitPoint
        returnObject = DNASuitPoint.DNASuitPoint(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getEndPoint(self):
        returnValue = libtoontown._inPdt4y7Cdh(self.this)
        import DNASuitPoint
        returnObject = DNASuitPoint.DNASuitPoint(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getZoneId(self):
        returnValue = libtoontown._inPdt4yex_N(self.this)
        return returnValue

    
    def setZoneId(self, zoneId):
        returnValue = libtoontown._inPdt4ywx8C(self.this, zoneId)
        return returnValue

    
    def output(self, out):
        returnValue = libtoontown._inPdt4ysQOc(self.this, out.this)
        return returnValue

    
    def _DNASuitEdge__overloaded_write_ptrConstDNASuitEdge_ptrOstream_ptrDNAStorage_int(self, out, store, indentLevel):
        returnValue = libtoontown._inPdt4ykMts(self.this, out.this, store.this, indentLevel)
        return returnValue

    
    def _DNASuitEdge__overloaded_write_ptrConstDNASuitEdge_ptrOstream_ptrDNAStorage(self, out, store):
        returnValue = libtoontown._inPdt4ygV5N(self.this, out.this, store.this)
        return returnValue

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._DNASuitEdge__overloaded_write_ptrConstDNASuitEdge_ptrOstream_ptrDNAStorage(*_args)
        elif numArgs == 3:
            return self._DNASuitEdge__overloaded_write_ptrConstDNASuitEdge_ptrOstream_ptrDNAStorage_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


