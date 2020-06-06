# File: S (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class StreamReader(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _StreamReader__overloaded_constructor_ptrConstStreamReader(self, copy):
        self.this = libpandaexpress._inPKoxtFpUz(copy.this)
        self.userManagesMemory = 1

    
    def _StreamReader__overloaded_constructor_ptrIstream_bool(self, _in, ownsStream):
        self.this = libpandaexpress._inPKoxtRUwl(_in.this, ownsStream)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxtY3Qy:
            libpandaexpress._inPKoxtY3Qy(self.this)
        

    
    def assign(self, copy):
        returnValue = libpandaexpress._inPKoxt9fei(self.this, copy.this)
        returnObject = StreamReader(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getIstream(self):
        returnValue = libpandaexpress._inPKoxtBqye(self.this)
        import Istream
        returnObject = Istream.Istream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getBool(self):
        returnValue = libpandaexpress._inPKoxtRU6i(self.this)
        return returnValue

    
    def getInt8(self):
        returnValue = libpandaexpress._inPKoxtKvu5(self.this)
        return returnValue

    
    def getUint8(self):
        returnValue = libpandaexpress._inPKoxt3bcv(self.this)
        return returnValue

    
    def getInt16(self):
        returnValue = libpandaexpress._inPKoxtC3S_(self.this)
        return returnValue

    
    def getInt32(self):
        returnValue = libpandaexpress._inPKoxtfHEw(self.this)
        return returnValue

    
    def getInt64(self):
        returnValue = libpandaexpress._inPKoxtVfP_(self.this)
        return returnValue

    
    def getUint16(self):
        returnValue = libpandaexpress._inPKoxtCGYB(self.this)
        return returnValue

    
    def getUint32(self):
        returnValue = libpandaexpress._inPKoxtq8Q6(self.this)
        return returnValue

    
    def getUint64(self):
        returnValue = libpandaexpress._inPKoxtlBk_(self.this)
        return returnValue

    
    def getFloat32(self):
        returnValue = libpandaexpress._inPKoxtFJu6(self.this)
        return returnValue

    
    def getFloat64(self):
        returnValue = libpandaexpress._inPKoxtMMwk(self.this)
        return returnValue

    
    def getBeInt16(self):
        returnValue = libpandaexpress._inPKoxtx_KM(self.this)
        return returnValue

    
    def getBeInt32(self):
        returnValue = libpandaexpress._inPKoxtntwJ(self.this)
        return returnValue

    
    def getBeInt64(self):
        returnValue = libpandaexpress._inPKoxtM_CL(self.this)
        return returnValue

    
    def getBeUint16(self):
        returnValue = libpandaexpress._inPKoxtiU6t(self.this)
        return returnValue

    
    def getBeUint32(self):
        returnValue = libpandaexpress._inPKoxthfBh(self.this)
        return returnValue

    
    def getBeUint64(self):
        returnValue = libpandaexpress._inPKoxtCq6J(self.this)
        return returnValue

    
    def getBeFloat32(self):
        returnValue = libpandaexpress._inPKoxttDBP(self.this)
        return returnValue

    
    def getBeFloat64(self):
        returnValue = libpandaexpress._inPKoxtxzXr(self.this)
        return returnValue

    
    def getString(self):
        returnValue = libpandaexpress._inPKoxtSbCK(self.this)
        return returnValue

    
    def getString32(self):
        returnValue = libpandaexpress._inPKoxtjatw(self.this)
        return returnValue

    
    def getZString(self):
        returnValue = libpandaexpress._inPKoxttLbM(self.this)
        return returnValue

    
    def getFixedString(self, size):
        returnValue = libpandaexpress._inPKoxtdj5Y(self.this, size)
        return returnValue

    
    def skipBytes(self, size):
        returnValue = libpandaexpress._inPKoxtRyDw(self.this, size)
        return returnValue

    
    def extractBytes(self, size):
        returnValue = libpandaexpress._inPKoxtxpca(self.this, size)
        return returnValue

    
    def readline(self):
        returnValue = libpandaexpress._inPKoxtUfmk(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._StreamReader__overloaded_constructor_ptrConstStreamReader(*_args)
        elif numArgs == 2:
            return self._StreamReader__overloaded_constructor_ptrIstream_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def readlines(self):
        lines = []
        line = self.readline()
        while line:
            lines.append(line)
            line = self.readline()
        return lines


