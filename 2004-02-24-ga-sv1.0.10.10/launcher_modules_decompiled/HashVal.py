# File: H (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class HashVal(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _HashVal__overloaded_constructor(self):
        self.this = libpandaexpress._inPJoxtI_Ud()
        self.userManagesMemory = 1

    
    def _HashVal__overloaded_constructor_ptrConstHashVal(self, copy):
        self.this = libpandaexpress._inPJoxtH_4C(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPJoxtzpzW:
            libpandaexpress._inPJoxtzpzW(self.this)
        

    
    def assign(self, copy):
        returnValue = libpandaexpress._inPJoxt3FRA(self.this, copy.this)
        returnObject = HashVal(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def eq(self, other):
        returnValue = libpandaexpress._inPJoxtnq7I(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpandaexpress._inPJoxt7G7E(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpandaexpress._inPJoxtyVFW(self.this, other.this)
        return returnValue

    
    def compareTo(self, other):
        returnValue = libpandaexpress._inPJoxtpxYW(self.this, other.this)
        return returnValue

    
    def mergeWith(self, other):
        returnValue = libpandaexpress._inPJoxtubg2(self.this, other.this)
        return returnValue

    
    def outputDec(self, out):
        returnValue = libpandaexpress._inPJoxtPh3K(self.this, out.this)
        return returnValue

    
    def inputDec(self, _in):
        returnValue = libpandaexpress._inPJoxtk92_(self.this, _in.this)
        return returnValue

    
    def outputHex(self, out):
        returnValue = libpandaexpress._inPJoxtm_Zx(self.this, out.this)
        return returnValue

    
    def inputHex(self, _in):
        returnValue = libpandaexpress._inPJoxtZ1DR(self.this, _in.this)
        return returnValue

    
    def outputBinary(self, out):
        returnValue = libpandaexpress._inPJoxt_T88(self.this, out.this)
        return returnValue

    
    def inputBinary(self, _in):
        returnValue = libpandaexpress._inPJoxt_JzH(self.this, _in.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inPJoxtM3Nu(self.this, out.this)
        return returnValue

    
    def asDec(self):
        returnValue = libpandaexpress._inPJoxtyYur(self.this)
        return returnValue

    
    def setFromDec(self, text):
        returnValue = libpandaexpress._inPJoxtOC7K(self.this, text)
        return returnValue

    
    def asHex(self):
        returnValue = libpandaexpress._inPJoxtyITU(self.this)
        return returnValue

    
    def setFromHex(self, text):
        returnValue = libpandaexpress._inPJoxtVCVt(self.this, text)
        return returnValue

    
    def writeDatagram(self, destination):
        returnValue = libpandaexpress._inPJoxtjcbw(self.this, destination.this)
        return returnValue

    
    def readDatagram(self, source):
        returnValue = libpandaexpress._inPJoxtp9e6(self.this, source.this)
        return returnValue

    
    def writeStream(self, destination):
        returnValue = libpandaexpress._inPJoxtb0yS(self.this, destination.this)
        return returnValue

    
    def readStream(self, source):
        returnValue = libpandaexpress._inPJoxtUgPU(self.this, source.this)
        return returnValue

    
    def hashFile(self, filename):
        returnValue = libpandaexpress._inPJoxt1jdB(self.this, filename.this)
        return returnValue

    
    def hashRamfile(self, ramfile):
        returnValue = libpandaexpress._inPJoxtk7sL(self.this, ramfile.this)
        return returnValue

    
    def hashString(self, data):
        returnValue = libpandaexpress._inPJoxtJiKt(self.this, data)
        return returnValue

    
    def hashBuffer(self, buffer, length):
        returnValue = libpandaexpress._inPJoxtXiK7(self.this, buffer, length)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._HashVal__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], HashVal):
                return self._HashVal__overloaded_constructor_ptrConstHashVal(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <HashVal> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


