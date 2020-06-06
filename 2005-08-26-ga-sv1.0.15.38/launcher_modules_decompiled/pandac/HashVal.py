# File: H (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class HashVal(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _HashVal__overloaded_constructor(self):
        self.this = libpandaexpress._inPKoxtI_Ud()
        self.userManagesMemory = 1

    
    def _HashVal__overloaded_constructor_ptrConstHashVal(self, copy):
        self.this = libpandaexpress._inPKoxtH_4C(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxtzpzW:
            libpandaexpress._inPKoxtzpzW(self.this)
        

    
    def assign(self, copy):
        returnValue = libpandaexpress._inPKoxt3FRA(self.this, copy.this)
        returnObject = HashVal(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def eq(self, other):
        returnValue = libpandaexpress._inPKoxtnq7I(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpandaexpress._inPKoxt7G7E(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpandaexpress._inPKoxtyVFW(self.this, other.this)
        return returnValue

    
    def compareTo(self, other):
        returnValue = libpandaexpress._inPKoxtpxYW(self.this, other.this)
        return returnValue

    
    def mergeWith(self, other):
        returnValue = libpandaexpress._inPKoxtvbg2(self.this, other.this)
        return returnValue

    
    def outputDec(self, out):
        returnValue = libpandaexpress._inPKoxtPh3K(self.this, out.this)
        return returnValue

    
    def inputDec(self, _in):
        returnValue = libpandaexpress._inPKoxtl92_(self.this, _in.this)
        return returnValue

    
    def outputHex(self, out):
        returnValue = libpandaexpress._inPKoxtn_Zx(self.this, out.this)
        return returnValue

    
    def inputHex(self, _in):
        returnValue = libpandaexpress._inPKoxtZ1DR(self.this, _in.this)
        return returnValue

    
    def outputBinary(self, out):
        returnValue = libpandaexpress._inPKoxt_T88(self.this, out.this)
        return returnValue

    
    def inputBinary(self, _in):
        returnValue = libpandaexpress._inPKoxt_JzH(self.this, _in.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inPKoxtL3Nu(self.this, out.this)
        return returnValue

    
    def asDec(self):
        returnValue = libpandaexpress._inPKoxtzYur(self.this)
        return returnValue

    
    def setFromDec(self, text):
        returnValue = libpandaexpress._inPKoxtOC7K(self.this, text)
        return returnValue

    
    def asHex(self):
        returnValue = libpandaexpress._inPKoxtyITU(self.this)
        return returnValue

    
    def setFromHex(self, text):
        returnValue = libpandaexpress._inPKoxtWCVt(self.this, text)
        return returnValue

    
    def writeDatagram(self, destination):
        returnValue = libpandaexpress._inPKoxticbw(self.this, destination.this)
        return returnValue

    
    def readDatagram(self, source):
        returnValue = libpandaexpress._inPKoxto9e6(self.this, source.this)
        return returnValue

    
    def writeStream(self, destination):
        returnValue = libpandaexpress._inPKoxtb0yS(self.this, destination.this)
        return returnValue

    
    def readStream(self, source):
        returnValue = libpandaexpress._inPKoxtUgPU(self.this, source.this)
        return returnValue

    
    def hashFile(self, filename):
        returnValue = libpandaexpress._inPKoxt1jdB(self.this, filename.this)
        return returnValue

    
    def hashRamfile(self, ramfile):
        returnValue = libpandaexpress._inPKoxtk7sL(self.this, ramfile.this)
        return returnValue

    
    def hashString(self, data):
        returnValue = libpandaexpress._inPKoxtIiKt(self.this, data)
        return returnValue

    
    def hashBuffer(self, buffer, length):
        returnValue = libpandaexpress._inPKoxtWiK7(self.this, buffer, length)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._HashVal__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._HashVal__overloaded_constructor_ptrConstHashVal(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


