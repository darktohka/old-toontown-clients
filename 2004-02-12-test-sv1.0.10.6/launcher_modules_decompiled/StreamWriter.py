# File: S (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class StreamWriter(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _StreamWriter__overloaded_constructor_ptrConstStreamWriter(self, copy):
        self.this = libpandaexpress._inPJoxt8OZ1(copy.this)
        self.userManagesMemory = 1

    
    def _StreamWriter__overloaded_constructor_ptrOstream(self, out):
        self.this = libpandaexpress._inPJoxtKElO(out.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPJoxtRX7A:
            libpandaexpress._inPJoxtRX7A(self.this)
        

    
    def assign(self, copy):
        returnValue = libpandaexpress._inPJoxtCFlt(self.this, copy.this)
        returnObject = StreamWriter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getOstream(self):
        returnValue = libpandaexpress._inPJoxtUDoY(self.this)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def addBool(self, value):
        returnValue = libpandaexpress._inPJoxt2JN5(self.this, value)
        return returnValue

    
    def addInt8(self, value):
        returnValue = libpandaexpress._inPJoxtTGkZ(self.this, value)
        return returnValue

    
    def addUint8(self, value):
        returnValue = libpandaexpress._inPJoxtEVDZ(self.this, value)
        return returnValue

    
    def addInt16(self, value):
        returnValue = libpandaexpress._inPJoxtmnpY(self.this, value)
        return returnValue

    
    def addInt32(self, value):
        returnValue = libpandaexpress._inPJoxt1WLJ(self.this, value)
        return returnValue

    
    def addInt64(self, value):
        returnValue = libpandaexpress._inPJoxtWgUQ(self.this, value)
        return returnValue

    
    def addUint16(self, value):
        returnValue = libpandaexpress._inPJoxtp_Hu(self.this, value)
        return returnValue

    
    def addUint32(self, value):
        returnValue = libpandaexpress._inPJoxtFr_h(self.this, value)
        return returnValue

    
    def addUint64(self, value):
        returnValue = libpandaexpress._inPJoxt31RL(self.this, value)
        return returnValue

    
    def addFloat32(self, value):
        returnValue = libpandaexpress._inPJoxtyymY(self.this, value)
        return returnValue

    
    def addFloat64(self, value):
        returnValue = libpandaexpress._inPJoxtREib(self.this, value)
        return returnValue

    
    def addBeInt16(self, value):
        returnValue = libpandaexpress._inPJoxtoxlG(self.this, value)
        return returnValue

    
    def addBeInt32(self, value):
        returnValue = libpandaexpress._inPJoxtKkpS(self.this, value)
        return returnValue

    
    def addBeInt64(self, value):
        returnValue = libpandaexpress._inPJoxtboTe(self.this, value)
        return returnValue

    
    def addBeUint16(self, value):
        returnValue = libpandaexpress._inPJoxtt7kL(self.this, value)
        return returnValue

    
    def addBeUint32(self, value):
        returnValue = libpandaexpress._inPJoxtFcr4(self.this, value)
        return returnValue

    
    def addBeUint64(self, value):
        returnValue = libpandaexpress._inPJoxtGgAL(self.this, value)
        return returnValue

    
    def addBeFloat32(self, value):
        returnValue = libpandaexpress._inPJoxtgr8S(self.this, value)
        return returnValue

    
    def addBeFloat64(self, value):
        returnValue = libpandaexpress._inPJoxtjAln(self.this, value)
        return returnValue

    
    def addString(self, str):
        returnValue = libpandaexpress._inPJoxtS9F1(self.this, str)
        return returnValue

    
    def addString32(self, str):
        returnValue = libpandaexpress._inPJoxtPtIk(self.this, str)
        return returnValue

    
    def addZString(self, str):
        returnValue = libpandaexpress._inPJoxtbv3_(self.this, str)
        return returnValue

    
    def addFixedString(self, str, size):
        returnValue = libpandaexpress._inPJoxtoQSq(self.this, str, size)
        return returnValue

    
    def padBytes(self, size):
        returnValue = libpandaexpress._inPJoxtPjY_(self.this, size)
        return returnValue

    
    def appendData(self, data):
        returnValue = libpandaexpress._inPJoxtEBfh(self.this, data)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], StreamWriter):
                return self._StreamWriter__overloaded_constructor_ptrConstStreamWriter(_args[0])
            elif isinstance(_args[0], Ostream.Ostream):
                return self._StreamWriter__overloaded_constructor_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <StreamWriter> <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


