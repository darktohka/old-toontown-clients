# File: P (Python 2.2)

from pandac.PandaModules import *
from pandac.DCSubatomicType import *

class PyDatagram(Datagram):
    FuncDict = {
        STInt8: (Datagram.addInt8, int),
        STInt16: (Datagram.addInt16, int),
        STInt32: (Datagram.addInt32, int),
        STInt64: (Datagram.addInt64, int),
        STUint8: (Datagram.addUint8, int),
        STUint16: (Datagram.addUint16, int),
        STUint32: (Datagram.addUint32, int),
        STUint64: (Datagram.addUint64, int),
        STFloat64: (Datagram.addFloat64, None),
        STString: (Datagram.addString, None),
        STBlob: (Datagram.addString, None),
        STBlob32: (Datagram.addString32, None) }
    addChannel = Datagram.addUint64
    
    def putArg(self, arg, subatomicType, divisor = 1):
        if divisor == 1:
            funcSpecs = self.FuncDict.get(subatomicType)
            if funcSpecs:
                (addFunc, argFunc) = funcSpecs
                if argFunc:
                    arg = argFunc(arg)
                
                addFunc(self, arg)
            elif subatomicType == STInt8array:
                self.addUint16(len(arg))
                for i in arg:
                    self.addInt8(int(i))
                
            elif subatomicType == STInt16array:
                self.addUint16(len(arg) << 1)
                for i in arg:
                    self.addInt16(int(i))
                
            elif subatomicType == STInt32array:
                self.addUint16(len(arg) << 2)
                for i in arg:
                    self.addInt32(int(i))
                
            elif subatomicType == STUint8array:
                self.addUint16(len(arg))
                for i in arg:
                    self.addUint8(int(i))
                
            elif subatomicType == STUint16array:
                self.addUint16(len(arg) << 1)
                for i in arg:
                    self.addUint16(int(i))
                
            elif subatomicType == STUint32array:
                self.addUint16(len(arg) << 2)
                for i in arg:
                    self.addUint32(int(i))
                
            elif subatomicType == STUint32uint8array:
                self.addUint16(len(arg) * 5)
                for i in arg:
                    self.addUint32(int(i[0]))
                    self.addUint8(int(i[1]))
                
            else:
                raise Exception('Error: No such type as: ' + str(subatomicType))
        else:
            funcSpecs = self.FuncDict.get(subatomicType)
            if funcSpecs:
                (addFunc, argFunc) = funcSpecs
                addFunc(self, int(round(arg * divisor)))
            elif subatomicType == STInt8array:
                self.addUint16(len(arg))
                for i in arg:
                    self.addInt8(int(round(i * divisor)))
                
            elif subatomicType == STInt16array:
                self.addUint16(len(arg) << 1)
                for i in arg:
                    self.addInt16(int(round(i * divisor)))
                
            elif subatomicType == STInt32array:
                self.addUint16(len(arg) << 2)
                for i in arg:
                    self.addInt32(int(round(i * divisor)))
                
            elif subatomicType == STUint8array:
                self.addUint16(len(arg))
                for i in arg:
                    self.addUint8(int(round(i * divisor)))
                
            elif subatomicType == STUint16array:
                self.addUint16(len(arg) << 1)
                for i in arg:
                    self.addUint16(int(round(i * divisor)))
                
            elif subatomicType == STUint32array:
                self.addUint16(len(arg) << 2)
                for i in arg:
                    self.addUint32(int(round(i * divisor)))
                
            elif subatomicType == STUint32uint8array:
                self.addUint16(len(arg) * 5)
                for i in arg:
                    self.addUint32(int(round(i[0] * divisor)))
                    self.addUint8(int(round(i[1] * divisor)))
                
            else:
                raise Exception('Error: type does not accept divisor: ' + str(subatomicType))


