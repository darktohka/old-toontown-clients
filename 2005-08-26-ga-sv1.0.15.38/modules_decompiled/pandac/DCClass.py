# File: D (Python 2.2)

import types
import libdirect
import libdirectDowncasts
from direct.ffi import FFIExternalObject
import DCDeclaration

class DCClass(DCDeclaration.DCDeclaration, FFIExternalObject.FFIExternalObject):
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
        if libdirect and libdirect._inP5HfQ9AVj:
            libdirect._inP5HfQ9AVj(self.this)
        

    
    def getName(self):
        returnValue = libdirect._inP5HfQBfkV(self.this)
        return returnValue

    
    def getNumber(self):
        returnValue = libdirect._inP5HfQ4r2k(self.this)
        return returnValue

    
    def hasParent(self):
        returnValue = libdirect._inP5HfQGEb8(self.this)
        return returnValue

    
    def getParent(self):
        returnValue = libdirect._inP5HfQ0pIH(self.this)
        returnObject = DCClass(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def hasConstructor(self):
        returnValue = libdirect._inP5HfQMas6(self.this)
        return returnValue

    
    def getConstructor(self):
        returnValue = libdirect._inP5HfQlqaF(self.this)
        import DCField
        returnObject = DCField.DCField(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNumFields(self):
        returnValue = libdirect._inP5HfQdQnw(self.this)
        return returnValue

    
    def getField(self, n):
        returnValue = libdirect._inP5HfQv5gR(self.this, n)
        import DCField
        returnObject = DCField.DCField(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getFieldByName(self, name):
        returnValue = libdirect._inP5HfQcyie(self.this, name)
        import DCField
        returnObject = DCField.DCField(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNumInheritedFields(self):
        returnValue = libdirect._inP5HfQ_Xnu(self.this)
        return returnValue

    
    def getInheritedField(self, n):
        returnValue = libdirect._inP5HfQlQ88(self.this, n)
        import DCField
        returnObject = DCField.DCField(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def isStruct(self):
        returnValue = libdirect._inP5HfQ1VbT(self.this)
        return returnValue

    
    def isBogusClass(self):
        returnValue = libdirect._inP5HfQo9se(self.this)
        return returnValue

    
    def startGenerate(self):
        returnValue = libdirect._inP5HfQ2Fc9(self.this)
        return returnValue

    
    def stopGenerate(self):
        returnValue = libdirect._inP5HfQdkTw(self.this)
        return returnValue

    
    def hasClassDef(self):
        returnValue = libdirect._inP5HfQoeOv(self.this)
        return returnValue

    
    def setClassDef(self, classDef):
        returnValue = libdirect._inP5HfQnYZY(self.this, classDef)
        return returnValue

    
    def getClassDef(self):
        returnValue = libdirect._inP5HfQS395(self.this)
        return returnValue

    
    def receiveUpdate(self, distobj, di):
        returnValue = libdirect._inP5HfQQPjh(self.this, distobj, di.this)
        return returnValue

    
    def receiveUpdateBroadcastRequired(self, distobj, di):
        returnValue = libdirect._inP5HfQLA_2(self.this, distobj, di.this)
        return returnValue

    
    def receiveUpdateAllRequired(self, distobj, di):
        returnValue = libdirect._inP5HfQkwBe(self.this, distobj, di.this)
        return returnValue

    
    def receiveUpdateOther(self, distobj, di):
        returnValue = libdirect._inP5HfQ5Jl7(self.this, distobj, di.this)
        return returnValue

    
    def _DCClass__overloaded_directUpdate_ptrDCClass_ptrPyObject_atomicstring_ptrConstDatagram(self, distobj, fieldName, datagram):
        returnValue = libdirect._inP5HfQTp_A(self.this, distobj, fieldName, datagram.this)
        return returnValue

    
    def _DCClass__overloaded_directUpdate_ptrDCClass_ptrPyObject_atomicstring_atomicstring(self, distobj, fieldName, valueBlob):
        returnValue = libdirect._inP5HfQx5ko(self.this, distobj, fieldName, valueBlob)
        return returnValue

    
    def _DCClass__overloaded_packRequiredField_ptrConstDCClass_ptrDCPacker_ptrPyObject_ptrConstDCField(self, packer, distobj, field):
        returnValue = libdirect._inP5HfQQSyU(self.this, packer.this, distobj, field.this)
        return returnValue

    
    def _DCClass__overloaded_packRequiredField_ptrConstDCClass_ptrDatagram_ptrPyObject_ptrConstDCField(self, datagram, distobj, field):
        returnValue = libdirect._inP5HfQAQnH(self.this, datagram.this, distobj, field.this)
        return returnValue

    
    def clientFormatUpdate(self, fieldName, doId, args):
        returnValue = libdirect._inP5HfQqX_e(self.this, fieldName, doId, args)
        import Datagram
        returnObject = Datagram.Datagram(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def aiFormatUpdate(self, fieldName, doId, toId, fromId, args):
        returnValue = libdirect._inP5HfQ28_N(self.this, fieldName, doId, toId, fromId, args)
        import Datagram
        returnObject = Datagram.Datagram(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def aiFormatGenerate(self, distobj, doId, parentId, zoneId, districtChannelId, fromChannelId, optionalFields):
        returnValue = libdirect._inP5HfQFfyH(self.this, distobj, doId, parentId, zoneId, districtChannelId, fromChannelId, optionalFields)
        import Datagram
        returnObject = Datagram.Datagram(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def clientFormatGenerate(self, distobj, doId, zoneId, optionalFields):
        returnValue = libdirect._inP5HfQqGXN(self.this, distobj, doId, zoneId, optionalFields)
        import Datagram
        returnObject = Datagram.Datagram(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def packRequiredField(self, *_args):
        numArgs = len(_args)
        if numArgs == 3:
            import Datagram
            if isinstance(_args[0], Datagram.Datagram):
                return self._DCClass__overloaded_packRequiredField_ptrConstDCClass_ptrDatagram_ptrPyObject_ptrConstDCField(*_args)
            
            import DCPacker
            if isinstance(_args[0], DCPacker.DCPacker):
                return self._DCClass__overloaded_packRequiredField_ptrConstDCClass_ptrDCPacker_ptrPyObject_ptrConstDCField(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Datagram.Datagram> <DCPacker.DCPacker> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 '

    
    def directUpdate(self, *_args):
        numArgs = len(_args)
        if numArgs == 3:
            if 1:
                if isinstance(_args[1], types.StringType):
                    if isinstance(_args[2], types.StringType):
                        return self._DCClass__overloaded_directUpdate_ptrDCClass_ptrPyObject_atomicstring_atomicstring(*_args)
                    
                    import Datagram
                    if isinstance(_args[2], Datagram.Datagram):
                        return self._DCClass__overloaded_directUpdate_ptrDCClass_ptrPyObject_atomicstring_ptrConstDatagram(*_args)
                    
                    raise TypeError, 'Invalid argument 2, expected one of: <types.StringType> <Datagram.Datagram> '
                
                raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <.> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 '


