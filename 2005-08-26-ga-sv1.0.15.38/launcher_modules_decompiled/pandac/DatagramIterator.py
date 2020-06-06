# File: D (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class DatagramIterator(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _DatagramIterator__overloaded_constructor(self):
        self.this = libpandaexpress._inPKoxtlJZb()
        self.userManagesMemory = 1

    
    def _DatagramIterator__overloaded_constructor_ptrConstDatagram_unsignedint(self, datagram, offset):
        self.this = libpandaexpress._inPKoxtEwZZ(datagram.this, offset)
        self.userManagesMemory = 1

    
    def _DatagramIterator__overloaded_constructor_ptrConstDatagram(self, datagram):
        self.this = libpandaexpress._inPKoxtz_OF(datagram.this)
        self.userManagesMemory = 1

    
    def _DatagramIterator__overloaded_constructor_ptrConstDatagramIterator(self, copy):
        self.this = libpandaexpress._inPKoxtYg7_(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxtA6Oz:
            libpandaexpress._inPKoxtA6Oz(self.this)
        

    
    def assign(self, copy):
        returnValue = libpandaexpress._inPKoxtnHKF(self.this, copy.this)
        returnObject = DatagramIterator(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getBool(self):
        returnValue = libpandaexpress._inPKoxtgFgv(self.this)
        return returnValue

    
    def getInt8(self):
        returnValue = libpandaexpress._inPKoxtFX9M(self.this)
        return returnValue

    
    def getUint8(self):
        returnValue = libpandaexpress._inPKoxtD6SU(self.this)
        return returnValue

    
    def getInt16(self):
        returnValue = libpandaexpress._inPKoxtEVNl(self.this)
        return returnValue

    
    def getInt32(self):
        returnValue = libpandaexpress._inPKoxtFcUY(self.this)
        return returnValue

    
    def getInt64(self):
        returnValue = libpandaexpress._inPKoxtkKNB(self.this)
        return returnValue

    
    def getUint16(self):
        returnValue = libpandaexpress._inPKoxtX2ad(self.this)
        return returnValue

    
    def getUint32(self):
        returnValue = libpandaexpress._inPKoxtpR_A(self.this)
        return returnValue

    
    def getUint64(self):
        returnValue = libpandaexpress._inPKoxtFGTd(self.this)
        return returnValue

    
    def getFloat32(self):
        returnValue = libpandaexpress._inPKoxtvFBB(self.this)
        return returnValue

    
    def getFloat64(self):
        returnValue = libpandaexpress._inPKoxt0JoL(self.this)
        return returnValue

    
    def getBeInt16(self):
        returnValue = libpandaexpress._inPKoxtzzGa(self.this)
        return returnValue

    
    def getBeInt32(self):
        returnValue = libpandaexpress._inPKoxt6U9R(self.this)
        return returnValue

    
    def getBeInt64(self):
        returnValue = libpandaexpress._inPKoxtAdBm(self.this)
        return returnValue

    
    def getBeUint16(self):
        returnValue = libpandaexpress._inPKoxte_MA(self.this)
        return returnValue

    
    def getBeUint32(self):
        returnValue = libpandaexpress._inPKoxt7bZ7(self.this)
        return returnValue

    
    def getBeUint64(self):
        returnValue = libpandaexpress._inPKoxtF489(self.this)
        return returnValue

    
    def getBeFloat32(self):
        returnValue = libpandaexpress._inPKoxtgTRq(self.this)
        return returnValue

    
    def getBeFloat64(self):
        returnValue = libpandaexpress._inPKoxtjsC8(self.this)
        return returnValue

    
    def getString(self):
        returnValue = libpandaexpress._inPKoxtxS8B(self.this)
        return returnValue

    
    def getString32(self):
        returnValue = libpandaexpress._inPKoxtp2Xo(self.this)
        return returnValue

    
    def getZString(self):
        returnValue = libpandaexpress._inPKoxtjyF6(self.this)
        return returnValue

    
    def getFixedString(self, size):
        returnValue = libpandaexpress._inPKoxtmT0q(self.this, size)
        return returnValue

    
    def skipBytes(self, size):
        returnValue = libpandaexpress._inPKoxtTwSY(self.this, size)
        return returnValue

    
    def extractBytes(self, size):
        returnValue = libpandaexpress._inPKoxt3j8S(self.this, size)
        return returnValue

    
    def getRemainingBytes(self):
        returnValue = libpandaexpress._inPKoxtyKhi(self.this)
        return returnValue

    
    def getRemainingSize(self):
        returnValue = libpandaexpress._inPKoxtOxKa(self.this)
        return returnValue

    
    def getDatagram(self):
        returnValue = libpandaexpress._inPKoxtdg_H(self.this)
        import Datagram
        returnObject = Datagram.Datagram(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def getCurrentIndex(self):
        returnValue = libpandaexpress._inPKoxt_KNH(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inPKoxtG38c(self.this, out.this)
        return returnValue

    
    def _DatagramIterator__overloaded_write_ptrConstDatagramIterator_ptrOstream_unsignedint(self, out, indent):
        returnValue = libpandaexpress._inPKoxtcoYU(self.this, out.this, indent)
        return returnValue

    
    def _DatagramIterator__overloaded_write_ptrConstDatagramIterator_ptrOstream(self, out):
        returnValue = libpandaexpress._inPKoxtuJe3(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DatagramIterator__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], DatagramIterator):
                return self._DatagramIterator__overloaded_constructor_ptrConstDatagramIterator(*_args)
            
            import Datagram
            if isinstance(_args[0], Datagram.Datagram):
                return self._DatagramIterator__overloaded_constructor_ptrConstDatagram(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <DatagramIterator> <Datagram.Datagram> '
        elif numArgs == 2:
            return self._DatagramIterator__overloaded_constructor_ptrConstDatagram_unsignedint(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._DatagramIterator__overloaded_write_ptrConstDatagramIterator_ptrOstream(*_args)
        elif numArgs == 2:
            return self._DatagramIterator__overloaded_write_ptrConstDatagramIterator_ptrOstream_unsignedint(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


