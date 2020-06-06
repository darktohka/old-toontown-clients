# File: D (Python 2.2)

import types
import libdirect
import libdirectDowncasts
from direct.ffi import FFIExternalObject
import DCPackerInterface

class DCField(DCPackerInterface.DCPackerInterface, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libdirectDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libdirect and libdirect._inP5HfQSs2p:
            libdirect._inP5HfQSs2p(self.this)
        

    
    def getNumber(self):
        returnValue = libdirect._inP5HfQYIQq(self.this)
        return returnValue

    
    def _DCField__overloaded_asAtomicField_ptrDCField(self):
        returnValue = libdirect._inP5HfQEiDu(self.this)
        import DCAtomicField
        returnObject = DCAtomicField.DCAtomicField(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _DCField__overloaded_asAtomicField_ptrConstDCField(self):
        returnValue = libdirect._inP5HfQzwks(self.this)
        import DCAtomicField
        returnObject = DCAtomicField.DCAtomicField(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _DCField__overloaded_asMolecularField_ptrDCField(self):
        returnValue = libdirect._inP5HfQuhmz(self.this)
        import DCMolecularField
        returnObject = DCMolecularField.DCMolecularField(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _DCField__overloaded_asMolecularField_ptrConstDCField(self):
        returnValue = libdirect._inP5HfQ5dUO(self.this)
        import DCMolecularField
        returnObject = DCMolecularField.DCMolecularField(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _DCField__overloaded_asParameter_ptrDCField(self):
        returnValue = libdirect._inP5HfQdmWk(self.this)
        import DCParameter
        returnObject = DCParameter.DCParameter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _DCField__overloaded_asParameter_ptrConstDCField(self):
        returnValue = libdirect._inP5HfQORwy(self.this)
        import DCParameter
        returnObject = DCParameter.DCParameter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def formatData(self, packedData):
        returnValue = libdirect._inP5HfQAzaE(self.this, packedData)
        return returnValue

    
    def parseString(self, formattedString):
        returnValue = libdirect._inP5HfQZxBu(self.this, formattedString)
        return returnValue

    
    def validateRanges(self, packedData):
        returnValue = libdirect._inP5HfQu_ys(self.this, packedData)
        return returnValue

    
    def hasDefaultValue(self):
        returnValue = libdirect._inP5HfQMANq(self.this)
        return returnValue

    
    def getDefaultValue(self):
        returnValue = libdirect._inP5HfQJt60(self.this)
        return returnValue

    
    def isRequired(self):
        returnValue = libdirect._inP5HfQsDoF(self.this)
        return returnValue

    
    def isBroadcast(self):
        returnValue = libdirect._inP5HfQ01Fw(self.this)
        return returnValue

    
    def isP2p(self):
        returnValue = libdirect._inP5HfQ3LEd(self.this)
        return returnValue

    
    def isRam(self):
        returnValue = libdirect._inP5HfQFnxN(self.this)
        return returnValue

    
    def isDb(self):
        returnValue = libdirect._inP5HfQnl1_(self.this)
        return returnValue

    
    def isClsend(self):
        returnValue = libdirect._inP5HfQ_j06(self.this)
        return returnValue

    
    def isClrecv(self):
        returnValue = libdirect._inP5HfQtyCR(self.this)
        return returnValue

    
    def isOwnsend(self):
        returnValue = libdirect._inP5HfQGJ0E(self.this)
        return returnValue

    
    def isAirecv(self):
        returnValue = libdirect._inP5HfQl0Uq(self.this)
        return returnValue

    
    def compareFlags(self, other):
        returnValue = libdirect._inP5HfQYr6o(self.this, other.this)
        return returnValue

    
    def output(self, out):
        returnValue = libdirect._inP5HfQLxp4(self.this, out.this)
        return returnValue

    
    def write(self, out, indentLevel):
        returnValue = libdirect._inP5HfQnirA(self.this, out.this, indentLevel)
        return returnValue

    
    def packArgs(self, packer, sequence):
        returnValue = libdirect._inP5HfQBNMR(self.this, packer.this, sequence)
        return returnValue

    
    def unpackArgs(self, packer):
        returnValue = libdirect._inP5HfQ7m86(self.this, packer.this)
        return returnValue

    
    def receiveUpdate(self, packer, distobj):
        returnValue = libdirect._inP5HfQc4tY(self.this, packer.this, distobj)
        return returnValue

    
    def clientFormatUpdate(self, doId, args):
        returnValue = libdirect._inP5HfQsnRB(self.this, doId, args)
        import Datagram
        returnObject = Datagram.Datagram(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def aiFormatUpdate(self, doId, toId, fromId, args):
        returnValue = libdirect._inP5HfQUeo2(self.this, doId, toId, fromId, args)
        import Datagram
        returnObject = Datagram.Datagram(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def asAtomicField(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DCField__overloaded_asAtomicField_ptrConstDCField(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 '

    
    def asParameter(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DCField__overloaded_asParameter_ptrConstDCField(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 '

    
    def asMolecularField(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DCField__overloaded_asMolecularField_ptrConstDCField(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 '


