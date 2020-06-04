# File: S (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class StreamReader(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _StreamReader__overloaded_constructor_ptrConstStreamReader(self, copy):
        self.this = libpandaexpress._inPJoxtEpUz(copy.this)
        self.userManagesMemory = 1

    
    def _StreamReader__overloaded_constructor_ptrIstream_bool(self, _in, ownsStream):
        self.this = libpandaexpress._inPJoxtOUwl(_in.this, ownsStream)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPJoxtZ3Qy:
            libpandaexpress._inPJoxtZ3Qy(self.this)
        

    
    def assign(self, copy):
        returnValue = libpandaexpress._inPJoxtyfei(self.this, copy.this)
        returnObject = StreamReader(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getIstream(self):
        returnValue = libpandaexpress._inPJoxtBqye(self.this)
        import Istream
        returnObject = Istream.Istream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getBool(self):
        returnValue = libpandaexpress._inPJoxtQU6i(self.this)
        return returnValue

    
    def getInt8(self):
        returnValue = libpandaexpress._inPJoxtJvu5(self.this)
        return returnValue

    
    def getUint8(self):
        returnValue = libpandaexpress._inPJoxt2bcv(self.this)
        return returnValue

    
    def getInt16(self):
        returnValue = libpandaexpress._inPJoxtD3S_(self.this)
        return returnValue

    
    def getInt32(self):
        returnValue = libpandaexpress._inPJoxtcHEw(self.this)
        return returnValue

    
    def getInt64(self):
        returnValue = libpandaexpress._inPJoxtKfP_(self.this)
        return returnValue

    
    def getUint16(self):
        returnValue = libpandaexpress._inPJoxtCGYB(self.this)
        return returnValue

    
    def getUint32(self):
        returnValue = libpandaexpress._inPJoxtr8Q6(self.this)
        return returnValue

    
    def getUint64(self):
        returnValue = libpandaexpress._inPJoxtiBk_(self.this)
        return returnValue

    
    def getFloat32(self):
        returnValue = libpandaexpress._inPJoxtKJu6(self.this)
        return returnValue

    
    def getFloat64(self):
        returnValue = libpandaexpress._inPJoxtNMwk(self.this)
        return returnValue

    
    def getBeInt16(self):
        returnValue = libpandaexpress._inPJoxtx_KM(self.this)
        return returnValue

    
    def getBeInt32(self):
        returnValue = libpandaexpress._inPJoxtntwJ(self.this)
        return returnValue

    
    def getBeInt64(self):
        returnValue = libpandaexpress._inPJoxtM_CL(self.this)
        return returnValue

    
    def getBeUint16(self):
        returnValue = libpandaexpress._inPJoxtjU6t(self.this)
        return returnValue

    
    def getBeUint32(self):
        returnValue = libpandaexpress._inPJoxtifBh(self.this)
        return returnValue

    
    def getBeUint64(self):
        returnValue = libpandaexpress._inPJoxtCq6J(self.this)
        return returnValue

    
    def getBeFloat32(self):
        returnValue = libpandaexpress._inPJoxttDBP(self.this)
        return returnValue

    
    def getBeFloat64(self):
        returnValue = libpandaexpress._inPJoxtwzXr(self.this)
        return returnValue

    
    def getString(self):
        returnValue = libpandaexpress._inPJoxtSbCK(self.this)
        return returnValue

    
    def getZString(self):
        returnValue = libpandaexpress._inPJoxttLbM(self.this)
        return returnValue

    
    def getFixedString(self, size):
        returnValue = libpandaexpress._inPJoxtdj5Y(self.this, size)
        return returnValue

    
    def skipBytes(self, size):
        returnValue = libpandaexpress._inPJoxtSyDw(self.this, size)
        return returnValue

    
    def extractBytes(self, size):
        returnValue = libpandaexpress._inPJoxtxpca(self.this, size)
        return returnValue

    
    def readline(self):
        returnValue = libpandaexpress._inPJoxtLfmk(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], StreamReader):
                return self._StreamReader__overloaded_constructor_ptrConstStreamReader(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <StreamReader> '
        elif numArgs == 2:
            import Istream
            if isinstance(_args[0], Istream.Istream):
                if isinstance(_args[1], types.IntType):
                    return self._StreamReader__overloaded_constructor_ptrIstream_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Istream.Istream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def readlines(self):
        lines = []
        line = self.readline()
        while line:
            lines.append(line)
            line = self.readline()
        return lines


