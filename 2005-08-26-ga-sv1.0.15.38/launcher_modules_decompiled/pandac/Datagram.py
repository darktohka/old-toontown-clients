# File: D (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedObject

class Datagram(TypedObject.TypedObject, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _Datagram__overloaded_constructor(self):
        self.this = libpandaexpress._inPKoxtCJxx()
        self.userManagesMemory = 1

    
    def _Datagram__overloaded_constructor_ptrConstDatagram(self, copy):
        self.this = libpandaexpress._inPKoxteUaC(copy.this)
        self.userManagesMemory = 1

    
    def _Datagram__overloaded_constructor_atomicstring(self, data):
        self.this = libpandaexpress._inPKoxtgu3g(data)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxtDv_2:
            libpandaexpress._inPKoxtDv_2(self.this)
        

    
    def getClassType():
        returnValue = libpandaexpress._inPKoxt4Vv_()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaexpress._inPKoxtfPb_(self.this, copy.this)
        returnObject = Datagram(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def clear(self):
        returnValue = libpandaexpress._inPKoxtSYfy(self.this)
        return returnValue

    
    def dumpHex(self, out):
        returnValue = libpandaexpress._inPKoxtPUpE(self.this, out.this)
        return returnValue

    
    def addBool(self, value):
        returnValue = libpandaexpress._inPKoxtO0pV(self.this, value)
        return returnValue

    
    def addInt8(self, value):
        returnValue = libpandaexpress._inPKoxtmQ0b(self.this, value)
        return returnValue

    
    def addUint8(self, value):
        returnValue = libpandaexpress._inPKoxttZzT(self.this, value)
        return returnValue

    
    def addInt16(self, value):
        returnValue = libpandaexpress._inPKoxtR6wM(self.this, value)
        return returnValue

    
    def addInt32(self, value):
        returnValue = libpandaexpress._inPKoxtdRJV(self.this, value)
        return returnValue

    
    def addInt64(self, value):
        returnValue = libpandaexpress._inPKoxt2_qH(self.this, value)
        return returnValue

    
    def addUint16(self, value):
        returnValue = libpandaexpress._inPKoxtPwfl(self.this, value)
        return returnValue

    
    def addUint32(self, value):
        returnValue = libpandaexpress._inPKoxtllNj(self.this, value)
        return returnValue

    
    def addUint64(self, value):
        returnValue = libpandaexpress._inPKoxtkyp3(self.this, value)
        return returnValue

    
    def addFloat32(self, value):
        returnValue = libpandaexpress._inPKoxt9aTM(self.this, value)
        return returnValue

    
    def addFloat64(self, value):
        returnValue = libpandaexpress._inPKoxth7H7(self.this, value)
        return returnValue

    
    def addBeInt16(self, value):
        returnValue = libpandaexpress._inPKoxtStGs(self.this, value)
        return returnValue

    
    def addBeInt32(self, value):
        returnValue = libpandaexpress._inPKoxtfvnt(self.this, value)
        return returnValue

    
    def addBeInt64(self, value):
        returnValue = libpandaexpress._inPKoxtia1n(self.this, value)
        return returnValue

    
    def addBeUint16(self, value):
        returnValue = libpandaexpress._inPKoxtvmv8(self.this, value)
        return returnValue

    
    def addBeUint32(self, value):
        returnValue = libpandaexpress._inPKoxtKwYO(self.this, value)
        return returnValue

    
    def addBeUint64(self, value):
        returnValue = libpandaexpress._inPKoxtfEpz(self.this, value)
        return returnValue

    
    def addBeFloat32(self, value):
        returnValue = libpandaexpress._inPKoxtvJGy(self.this, value)
        return returnValue

    
    def addBeFloat64(self, value):
        returnValue = libpandaexpress._inPKoxtk_M8(self.this, value)
        return returnValue

    
    def addString(self, str):
        returnValue = libpandaexpress._inPKoxtLkWU(self.this, str)
        return returnValue

    
    def addString32(self, str):
        returnValue = libpandaexpress._inPKoxtWlwF(self.this, str)
        return returnValue

    
    def addZString(self, str):
        returnValue = libpandaexpress._inPKoxtfOXB(self.this, str)
        return returnValue

    
    def addFixedString(self, str, size):
        returnValue = libpandaexpress._inPKoxt6J1o(self.this, str, size)
        return returnValue

    
    def padBytes(self, size):
        returnValue = libpandaexpress._inPKoxtqdvo(self.this, size)
        return returnValue

    
    def appendData(self, data):
        returnValue = libpandaexpress._inPKoxt1lCb(self.this, data)
        return returnValue

    
    def getMessage(self):
        returnValue = libpandaexpress._inPKoxtrWvj(self.this)
        return returnValue

    
    def getData(self):
        returnValue = libpandaexpress._inPKoxtT0sE(self.this)
        return returnValue

    
    def getLength(self):
        returnValue = libpandaexpress._inPKoxtkk_0(self.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpandaexpress._inPKoxtN2MM(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpandaexpress._inPKoxtrt7L(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpandaexpress._inPKoxthPT3(self.this, other.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inPKoxt9OXp(self.this, out.this)
        return returnValue

    
    def _Datagram__overloaded_write_ptrConstDatagram_ptrOstream_unsignedint(self, out, indent):
        returnValue = libpandaexpress._inPKoxtm1mc(self.this, out.this, indent)
        return returnValue

    
    def _Datagram__overloaded_write_ptrConstDatagram_ptrOstream(self, out):
        returnValue = libpandaexpress._inPKoxtXtYv(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Datagram__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._Datagram__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], Datagram):
                return self._Datagram__overloaded_constructor_ptrConstDatagram(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <Datagram> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Datagram__overloaded_write_ptrConstDatagram_ptrOstream(*_args)
        elif numArgs == 2:
            return self._Datagram__overloaded_write_ptrConstDatagram_ptrOstream_unsignedint(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


