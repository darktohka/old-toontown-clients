# File: D (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TypedObject

class Datagram(TypedObject.TypedObject, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _Datagram__overloaded_constructor(self):
        self.this = libpandaexpress._inPJoxtDJxx()
        self.userManagesMemory = 1

    
    def _Datagram__overloaded_constructor_ptrConstDatagram(self, copy):
        self.this = libpandaexpress._inPJoxteUaC(copy.this)
        self.userManagesMemory = 1

    
    def _Datagram__overloaded_constructor_atomicstring(self, data):
        self.this = libpandaexpress._inPJoxthu3g(data)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPJoxtEv_2:
            libpandaexpress._inPJoxtEv_2(self.this)
        

    
    def getClassType():
        returnValue = libpandaexpress._inPJoxt5Vv_()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaexpress._inPJoxtePb_(self.this, copy.this)
        returnObject = Datagram(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def clear(self):
        returnValue = libpandaexpress._inPJoxtRYfy(self.this)
        return returnValue

    
    def dumpHex(self, out):
        returnValue = libpandaexpress._inPJoxtPUpE(self.this, out.this)
        return returnValue

    
    def addBool(self, value):
        returnValue = libpandaexpress._inPJoxtO0pV(self.this, value)
        return returnValue

    
    def addInt8(self, value):
        returnValue = libpandaexpress._inPJoxtmQ0b(self.this, value)
        return returnValue

    
    def addUint8(self, value):
        returnValue = libpandaexpress._inPJoxttZzT(self.this, value)
        return returnValue

    
    def addInt16(self, value):
        returnValue = libpandaexpress._inPJoxtR6wM(self.this, value)
        return returnValue

    
    def addInt32(self, value):
        returnValue = libpandaexpress._inPJoxtdRJV(self.this, value)
        return returnValue

    
    def addInt64(self, value):
        returnValue = libpandaexpress._inPJoxt2_qH(self.this, value)
        return returnValue

    
    def addUint16(self, value):
        returnValue = libpandaexpress._inPJoxtMwfl(self.this, value)
        return returnValue

    
    def addUint32(self, value):
        returnValue = libpandaexpress._inPJoxtklNj(self.this, value)
        return returnValue

    
    def addUint64(self, value):
        returnValue = libpandaexpress._inPJoxtnyp3(self.this, value)
        return returnValue

    
    def addFloat32(self, value):
        returnValue = libpandaexpress._inPJoxt9aTM(self.this, value)
        return returnValue

    
    def addFloat64(self, value):
        returnValue = libpandaexpress._inPJoxti7H7(self.this, value)
        return returnValue

    
    def addBeInt16(self, value):
        returnValue = libpandaexpress._inPJoxtdtGs(self.this, value)
        return returnValue

    
    def addBeInt32(self, value):
        returnValue = libpandaexpress._inPJoxtQvnt(self.this, value)
        return returnValue

    
    def addBeInt64(self, value):
        returnValue = libpandaexpress._inPJoxtja1n(self.this, value)
        return returnValue

    
    def addBeUint16(self, value):
        returnValue = libpandaexpress._inPJoxtumv8(self.this, value)
        return returnValue

    
    def addBeUint32(self, value):
        returnValue = libpandaexpress._inPJoxtKwYO(self.this, value)
        return returnValue

    
    def addBeUint64(self, value):
        returnValue = libpandaexpress._inPJoxteEpz(self.this, value)
        return returnValue

    
    def addBeFloat32(self, value):
        returnValue = libpandaexpress._inPJoxtgJGy(self.this, value)
        return returnValue

    
    def addBeFloat64(self, value):
        returnValue = libpandaexpress._inPJoxtl_M8(self.this, value)
        return returnValue

    
    def addString(self, str):
        returnValue = libpandaexpress._inPJoxtLkWU(self.this, str)
        return returnValue

    
    def addString32(self, str):
        returnValue = libpandaexpress._inPJoxtWlwF(self.this, str)
        return returnValue

    
    def addZString(self, str):
        returnValue = libpandaexpress._inPJoxtfOXB(self.this, str)
        return returnValue

    
    def addFixedString(self, str, size):
        returnValue = libpandaexpress._inPJoxt7J1o(self.this, str, size)
        return returnValue

    
    def padBytes(self, size):
        returnValue = libpandaexpress._inPJoxtrdvo(self.this, size)
        return returnValue

    
    def appendData(self, data):
        returnValue = libpandaexpress._inPJoxt1lCb(self.this, data)
        return returnValue

    
    def getMessage(self):
        returnValue = libpandaexpress._inPJoxtqWvj(self.this)
        return returnValue

    
    def getData(self):
        returnValue = libpandaexpress._inPJoxtT0sE(self.this)
        return returnValue

    
    def getLength(self):
        returnValue = libpandaexpress._inPJoxtnk_0(self.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpandaexpress._inPJoxtN2MM(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpandaexpress._inPJoxtrt7L(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpandaexpress._inPJoxtiPT3(self.this, other.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Datagram__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._Datagram__overloaded_constructor_atomicstring(_args[0])
            elif isinstance(_args[0], Datagram):
                return self._Datagram__overloaded_constructor_ptrConstDatagram(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <Datagram> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def putArg(self, arg, subatomicType, divisor = 1):
        import DCSubatomicType
        if divisor == 1:
            if subatomicType == DCSubatomicType.STInt8:
                self.addInt8(int(arg))
            elif subatomicType == DCSubatomicType.STInt16:
                self.addInt16(int(arg))
            elif subatomicType == DCSubatomicType.STInt32:
                self.addInt32(int(arg))
            elif subatomicType == DCSubatomicType.STInt64:
                self.addInt64(int(arg))
            elif subatomicType == DCSubatomicType.STUint8:
                self.addUint8(int(arg))
            elif subatomicType == DCSubatomicType.STUint16:
                self.addUint16(int(arg))
            elif subatomicType == DCSubatomicType.STUint32:
                self.addUint32(int(arg))
            elif subatomicType == DCSubatomicType.STUint64:
                self.addUint64(int(arg))
            elif subatomicType == DCSubatomicType.STFloat64:
                self.addFloat64(arg)
            elif subatomicType == DCSubatomicType.STString:
                self.addString(arg)
            elif subatomicType == DCSubatomicType.STBlob:
                self.addString(arg)
            elif hasattr(DCSubatomicType, 'STBlob32') and subatomicType == DCSubatomicType.STBlob32:
                self.addString32(arg)
            elif subatomicType == DCSubatomicType.STInt8array:
                self.addUint16(len(arg))
                for i in arg:
                    self.addInt8(int(i))
                
            elif subatomicType == DCSubatomicType.STInt16array:
                self.addUint16(len(arg) << 1)
                for i in arg:
                    self.addInt16(int(i))
                
            elif subatomicType == DCSubatomicType.STInt32array:
                self.addUint16(len(arg) << 2)
                for i in arg:
                    self.addInt32(int(i))
                
            elif subatomicType == DCSubatomicType.STUint8array:
                self.addUint16(len(arg))
                for i in arg:
                    self.addUint8(int(i))
                
            elif subatomicType == DCSubatomicType.STUint16array:
                self.addUint16(len(arg) << 1)
                for i in arg:
                    self.addUint16(int(i))
                
            elif subatomicType == DCSubatomicType.STUint32array:
                self.addUint16(len(arg) << 2)
                for i in arg:
                    self.addUint32(int(i))
                
            elif subatomicType == DCSubatomicType.STUint32uint8array:
                self.addUint16(len(arg) * 5)
                for i in arg:
                    self.addUint32(int(i[0]))
                    self.addUint8(int(i[1]))
                
            else:
                raise Exception('Error: No such type as: ' + str(subatomicType))
        elif subatomicType == DCSubatomicType.STInt8:
            self.addInt8(int(round(arg * divisor)))
        elif subatomicType == DCSubatomicType.STInt16:
            self.addInt16(int(round(arg * divisor)))
        elif subatomicType == DCSubatomicType.STInt32:
            self.addInt32(int(round(arg * divisor)))
        elif subatomicType == DCSubatomicType.STInt64:
            self.addInt64(int(round(arg * divisor)))
        elif subatomicType == DCSubatomicType.STUint8:
            self.addUint8(int(round(arg * divisor)))
        elif subatomicType == DCSubatomicType.STUint16:
            self.addUint16(int(round(arg * divisor)))
        elif subatomicType == DCSubatomicType.STUint32:
            self.addUint32(int(round(arg * divisor)))
        elif subatomicType == DCSubatomicType.STUint64:
            self.addUint64(int(round(arg * divisor)))
        elif subatomicType == DCSubatomicType.STInt8array:
            self.addUint16(len(arg))
            for i in arg:
                self.addInt8(int(round(i * divisor)))
            
        elif subatomicType == DCSubatomicType.STInt16array:
            self.addUint16(len(arg) << 1)
            for i in arg:
                self.addInt16(int(round(i * divisor)))
            
        elif subatomicType == DCSubatomicType.STInt32array:
            self.addUint16(len(arg) << 2)
            for i in arg:
                self.addInt32(int(round(i * divisor)))
            
        elif subatomicType == DCSubatomicType.STUint8array:
            self.addUint16(len(arg))
            for i in arg:
                self.addUint8(int(round(i * divisor)))
            
        elif subatomicType == DCSubatomicType.STUint16array:
            self.addUint16(len(arg) << 1)
            for i in arg:
                self.addUint16(int(round(i * divisor)))
            
        elif subatomicType == DCSubatomicType.STUint32array:
            self.addUint16(len(arg) << 2)
            for i in arg:
                self.addUint32(int(round(i * divisor)))
            
        elif subatomicType == DCSubatomicType.STUint32uint8array:
            self.addUint16(len(arg) * 5)
            for i in arg:
                self.addUint32(int(round(i[0] * divisor)))
                self.addUint8(int(round(i[1] * divisor)))
            
        else:
            raise Exception('Error: type does not accept divisor: ' + str(subatomicType))
        return None


