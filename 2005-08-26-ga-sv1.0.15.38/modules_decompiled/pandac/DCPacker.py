# File: D (Python 2.2)

import types
import libdirect
import libdirectDowncasts
from direct.ffi import FFIExternalObject

class DCPacker(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libdirectDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libdirect._inP5HfQfQtS()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libdirect and libdirect._inP5HfQkCam:
            libdirect._inP5HfQkCam(self.this)
        

    
    def getNumStackElementsEverAllocated():
        returnValue = libdirect._inP5HfQMJrY()
        return returnValue

    getNumStackElementsEverAllocated = staticmethod(getNumStackElementsEverAllocated)
    
    def clearData(self):
        returnValue = libdirect._inP5HfQJSK8(self.this)
        return returnValue

    
    def beginPack(self, root):
        returnValue = libdirect._inP5HfQ45bk(self.this, root.this)
        return returnValue

    
    def endPack(self):
        returnValue = libdirect._inP5HfQ7Jow(self.this)
        return returnValue

    
    def setUnpackData(self, data):
        returnValue = libdirect._inP5HfQvBpF(self.this, data)
        return returnValue

    
    def beginUnpack(self, root):
        returnValue = libdirect._inP5HfQbOoZ(self.this, root.this)
        return returnValue

    
    def endUnpack(self):
        returnValue = libdirect._inP5HfQbEEC(self.this)
        return returnValue

    
    def beginRepack(self, root):
        returnValue = libdirect._inP5HfQthAN(self.this, root.this)
        return returnValue

    
    def endRepack(self):
        returnValue = libdirect._inP5HfQwRsw(self.this)
        return returnValue

    
    def _DCPacker__overloaded_seek_ptrDCPacker_atomicstring(self, fieldName):
        returnValue = libdirect._inP5HfQ_NNW(self.this, fieldName)
        return returnValue

    
    def _DCPacker__overloaded_seek_ptrDCPacker_int(self, seekIndex):
        returnValue = libdirect._inP5HfQ2QAv(self.this, seekIndex)
        return returnValue

    
    def hasNestedFields(self):
        returnValue = libdirect._inP5HfQ0gaI(self.this)
        return returnValue

    
    def getNumNestedFields(self):
        returnValue = libdirect._inP5HfQQA_a(self.this)
        return returnValue

    
    def moreNestedFields(self):
        returnValue = libdirect._inP5HfQloor(self.this)
        return returnValue

    
    def getCurrentParent(self):
        returnValue = libdirect._inP5HfQO8yu(self.this)
        import DCPackerInterface
        returnObject = DCPackerInterface.DCPackerInterface(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getCurrentField(self):
        returnValue = libdirect._inP5HfQe_9F(self.this)
        import DCPackerInterface
        returnObject = DCPackerInterface.DCPackerInterface(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getLastSwitch(self):
        returnValue = libdirect._inP5HfQ3fj4(self.this)
        import DCSwitchParameter
        returnObject = DCSwitchParameter.DCSwitchParameter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getPackType(self):
        returnValue = libdirect._inP5HfQDwsp(self.this)
        return returnValue

    
    def push(self):
        returnValue = libdirect._inP5HfQcQuF(self.this)
        return returnValue

    
    def pop(self):
        returnValue = libdirect._inP5HfQ6bfW(self.this)
        return returnValue

    
    def packDouble(self, value):
        returnValue = libdirect._inP5HfQBIAM(self.this, value)
        return returnValue

    
    def packInt(self, value):
        returnValue = libdirect._inP5HfQ3yIL(self.this, value)
        return returnValue

    
    def packUint(self, value):
        returnValue = libdirect._inP5HfQut3J(self.this, value)
        return returnValue

    
    def packInt64(self, value):
        returnValue = libdirect._inP5HfQCx0g(self.this, value)
        return returnValue

    
    def packUint64(self, value):
        returnValue = libdirect._inP5HfQZTfh(self.this, value)
        return returnValue

    
    def packString(self, value):
        returnValue = libdirect._inP5HfQCdT5(self.this, value)
        return returnValue

    
    def packLiteralValue(self, value):
        returnValue = libdirect._inP5HfQTx3e(self.this, value)
        return returnValue

    
    def packDefaultValue(self):
        returnValue = libdirect._inP5HfQTBAY(self.this)
        return returnValue

    
    def unpackDouble(self):
        returnValue = libdirect._inP5HfQT8q9(self.this)
        return returnValue

    
    def unpackInt(self):
        returnValue = libdirect._inP5HfQmv6O(self.this)
        return returnValue

    
    def unpackUint(self):
        returnValue = libdirect._inP5HfQ_P2V(self.this)
        return returnValue

    
    def unpackInt64(self):
        returnValue = libdirect._inP5HfQeXGO(self.this)
        return returnValue

    
    def unpackUint64(self):
        returnValue = libdirect._inP5HfQ_EJ8(self.this)
        return returnValue

    
    def unpackString(self):
        returnValue = libdirect._inP5HfQl8eu(self.this)
        return returnValue

    
    def unpackLiteralValue(self):
        returnValue = libdirect._inP5HfQRc82(self.this)
        return returnValue

    
    def unpackValidate(self):
        returnValue = libdirect._inP5HfQOtBs(self.this)
        return returnValue

    
    def unpackSkip(self):
        returnValue = libdirect._inP5HfQGmIK(self.this)
        return returnValue

    
    def packObject(self, object):
        returnValue = libdirect._inP5HfQbgXg(self.this, object)
        return returnValue

    
    def unpackObject(self):
        returnValue = libdirect._inP5HfQP6lw(self.this)
        return returnValue

    
    def _DCPacker__overloaded_parseAndPack_ptrDCPacker_atomicstring(self, formattedObject):
        returnValue = libdirect._inP5HfQOrNi(self.this, formattedObject)
        return returnValue

    
    def _DCPacker__overloaded_parseAndPack_ptrDCPacker_ptrIstream(self, _in):
        returnValue = libdirect._inP5HfQQffJ(self.this, _in.this)
        return returnValue

    
    def _DCPacker__overloaded_unpackAndFormat_ptrDCPacker(self):
        returnValue = libdirect._inP5HfQ7De7(self.this)
        return returnValue

    
    def _DCPacker__overloaded_unpackAndFormat_ptrDCPacker_ptrOstream(self, out):
        returnValue = libdirect._inP5HfQDezg(self.this, out.this)
        return returnValue

    
    def hadPackError(self):
        returnValue = libdirect._inP5HfQI5eb(self.this)
        return returnValue

    
    def hadRangeError(self):
        returnValue = libdirect._inP5HfQKmZZ(self.this)
        return returnValue

    
    def hadError(self):
        returnValue = libdirect._inP5HfQLzjv(self.this)
        return returnValue

    
    def getNumUnpackedBytes(self):
        returnValue = libdirect._inP5HfQ1vkq(self.this)
        return returnValue

    
    def getLength(self):
        returnValue = libdirect._inP5HfQt4l7(self.this)
        return returnValue

    
    def getString(self):
        returnValue = libdirect._inP5HfQhK1P(self.this)
        return returnValue

    
    def rawPackInt8(self, value):
        returnValue = libdirect._inP5HfQXuco(self.this, value)
        return returnValue

    
    def rawPackInt16(self, value):
        returnValue = libdirect._inP5HfQEvl1(self.this, value)
        return returnValue

    
    def rawPackInt32(self, value):
        returnValue = libdirect._inP5HfQf5du(self.this, value)
        return returnValue

    
    def rawPackInt64(self, value):
        returnValue = libdirect._inP5HfQ02JY(self.this, value)
        return returnValue

    
    def rawPackUint8(self, value):
        returnValue = libdirect._inP5HfQ2c6b(self.this, value)
        return returnValue

    
    def rawPackUint16(self, value):
        returnValue = libdirect._inP5HfQ_5sg(self.this, value)
        return returnValue

    
    def rawPackUint32(self, value):
        returnValue = libdirect._inP5HfQbFo8(self.this, value)
        return returnValue

    
    def rawPackUint64(self, value):
        returnValue = libdirect._inP5HfQ1xJ4(self.this, value)
        return returnValue

    
    def rawPackFloat64(self, value):
        returnValue = libdirect._inP5HfQrDF_(self.this, value)
        return returnValue

    
    def rawPackString(self, value):
        returnValue = libdirect._inP5HfQojpx(self.this, value)
        return returnValue

    
    def rawUnpackInt8(self):
        returnValue = libdirect._inP5HfQWVWD(self.this)
        return returnValue

    
    def rawUnpackInt16(self):
        returnValue = libdirect._inP5HfQ30HM(self.this)
        return returnValue

    
    def rawUnpackInt32(self):
        returnValue = libdirect._inP5HfQFltJ(self.this)
        return returnValue

    
    def rawUnpackInt64(self):
        returnValue = libdirect._inP5HfQQ0_K(self.this)
        return returnValue

    
    def rawUnpackUint8(self):
        returnValue = libdirect._inP5HfQCUlV(self.this)
        return returnValue

    
    def rawUnpackUint16(self):
        returnValue = libdirect._inP5HfQBK3t(self.this)
        return returnValue

    
    def rawUnpackUint32(self):
        returnValue = libdirect._inP5HfQGD_g(self.this)
        return returnValue

    
    def rawUnpackUint64(self):
        returnValue = libdirect._inP5HfQh02J(self.this)
        return returnValue

    
    def rawUnpackFloat64(self):
        returnValue = libdirect._inP5HfQ0uTr(self.this)
        return returnValue

    
    def rawUnpackString(self):
        returnValue = libdirect._inP5HfQiaAh(self.this)
        return returnValue

    
    def parseAndPack(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DCPacker__overloaded_parseAndPack_ptrDCPacker_atomicstring(*_args)
            
            import Istream
            if isinstance(_args[0], Istream.Istream):
                return self._DCPacker__overloaded_parseAndPack_ptrDCPacker_ptrIstream(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <Istream.Istream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def seek(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._DCPacker__overloaded_seek_ptrDCPacker_int(*_args)
            
            if isinstance(_args[0], types.StringType):
                return self._DCPacker__overloaded_seek_ptrDCPacker_atomicstring(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def unpackAndFormat(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DCPacker__overloaded_unpackAndFormat_ptrDCPacker(*_args)
        elif numArgs == 1:
            return self._DCPacker__overloaded_unpackAndFormat_ptrDCPacker_ptrOstream(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


