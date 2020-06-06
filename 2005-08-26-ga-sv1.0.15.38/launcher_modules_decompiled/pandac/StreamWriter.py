# File: S (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class StreamWriter(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _StreamWriter__overloaded_constructor_ptrConstStreamWriter(self, copy):
        self.this = libpandaexpress._inPKoxt9OZ1(copy.this)
        self.userManagesMemory = 1

    
    def _StreamWriter__overloaded_constructor_ptrOstream(self, out):
        self.this = libpandaexpress._inPKoxtKElO(out.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxtRX7A:
            libpandaexpress._inPKoxtRX7A(self.this)
        

    
    def assign(self, copy):
        returnValue = libpandaexpress._inPKoxtDFlt(self.this, copy.this)
        returnObject = StreamWriter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getOstream(self):
        returnValue = libpandaexpress._inPKoxtUDoY(self.this)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def addBool(self, value):
        returnValue = libpandaexpress._inPKoxt3JN5(self.this, value)
        return returnValue

    
    def addInt8(self, value):
        returnValue = libpandaexpress._inPKoxtTGkZ(self.this, value)
        return returnValue

    
    def addUint8(self, value):
        returnValue = libpandaexpress._inPKoxtEVDZ(self.this, value)
        return returnValue

    
    def addInt16(self, value):
        returnValue = libpandaexpress._inPKoxtmnpY(self.this, value)
        return returnValue

    
    def addInt32(self, value):
        returnValue = libpandaexpress._inPKoxt1WLJ(self.this, value)
        return returnValue

    
    def addInt64(self, value):
        returnValue = libpandaexpress._inPKoxtWgUQ(self.this, value)
        return returnValue

    
    def addUint16(self, value):
        returnValue = libpandaexpress._inPKoxtq_Hu(self.this, value)
        return returnValue

    
    def addUint32(self, value):
        returnValue = libpandaexpress._inPKoxtar_h(self.this, value)
        return returnValue

    
    def addUint64(self, value):
        returnValue = libpandaexpress._inPKoxt31RL(self.this, value)
        return returnValue

    
    def addFloat32(self, value):
        returnValue = libpandaexpress._inPKoxtyymY(self.this, value)
        return returnValue

    
    def addFloat64(self, value):
        returnValue = libpandaexpress._inPKoxtREib(self.this, value)
        return returnValue

    
    def addBeInt16(self, value):
        returnValue = libpandaexpress._inPKoxtoxlG(self.this, value)
        return returnValue

    
    def addBeInt32(self, value):
        returnValue = libpandaexpress._inPKoxtKkpS(self.this, value)
        return returnValue

    
    def addBeInt64(self, value):
        returnValue = libpandaexpress._inPKoxtboTe(self.this, value)
        return returnValue

    
    def addBeUint16(self, value):
        returnValue = libpandaexpress._inPKoxtt7kL(self.this, value)
        return returnValue

    
    def addBeUint32(self, value):
        returnValue = libpandaexpress._inPKoxtEcr4(self.this, value)
        return returnValue

    
    def addBeUint64(self, value):
        returnValue = libpandaexpress._inPKoxtGgAL(self.this, value)
        return returnValue

    
    def addBeFloat32(self, value):
        returnValue = libpandaexpress._inPKoxtgr8S(self.this, value)
        return returnValue

    
    def addBeFloat64(self, value):
        returnValue = libpandaexpress._inPKoxtgAln(self.this, value)
        return returnValue

    
    def addString(self, str):
        returnValue = libpandaexpress._inPKoxtV9F1(self.this, str)
        return returnValue

    
    def addString32(self, str):
        returnValue = libpandaexpress._inPKoxtMtIk(self.this, str)
        return returnValue

    
    def addZString(self, str):
        returnValue = libpandaexpress._inPKoxtYv3_(self.this, str)
        return returnValue

    
    def addFixedString(self, str, size):
        returnValue = libpandaexpress._inPKoxtXQSq(self.this, str, size)
        return returnValue

    
    def padBytes(self, size):
        returnValue = libpandaexpress._inPKoxtMjY_(self.this, size)
        return returnValue

    
    def appendData(self, data):
        returnValue = libpandaexpress._inPKoxtbBfh(self.this, data)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], StreamWriter):
                return self._StreamWriter__overloaded_constructor_ptrConstStreamWriter(*_args)
            
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._StreamWriter__overloaded_constructor_ptrOstream(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <StreamWriter> <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


