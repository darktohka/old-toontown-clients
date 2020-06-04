# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\distributed\PyDatagramIterator.py
from pandac.PandaModules import *

class PyDatagramIterator(DatagramIterator):
    __module__ = __name__
    FuncDict = {STInt8: DatagramIterator.getInt8, STInt16: DatagramIterator.getInt16, STInt32: DatagramIterator.getInt32, STInt64: DatagramIterator.getInt64, STUint8: DatagramIterator.getUint8, STUint16: DatagramIterator.getUint16, STUint32: DatagramIterator.getUint32, STUint64: DatagramIterator.getUint64, STFloat64: DatagramIterator.getFloat64, STString: DatagramIterator.getString, STBlob: DatagramIterator.getString, STBlob32: DatagramIterator.getString32}
    getChannel = DatagramIterator.getUint64

    def getArg(self, subatomicType, divisor=1):
        if divisor == 1:
            getFunc = self.FuncDict.get(subatomicType)
            if getFunc:
                retVal = getFunc(self)
            elif subatomicType == STInt8array:
                len = self.getUint16()
                retVal = []
                for i in range(len):
                    retVal.append(self.getInt8())

            elif subatomicType == STInt16array:
                len = self.getUint16() >> 1
                retVal = []
                for i in range(len):
                    retVal.append(self.getInt16())

            elif subatomicType == STInt32array:
                len = self.getUint16() >> 2
                retVal = []
                for i in range(len):
                    retVal.append(self.getInt32())

            elif subatomicType == STUint8array:
                len = self.getUint16()
                retVal = []
                for i in range(len):
                    retVal.append(self.getUint8())

            elif subatomicType == STUint16array:
                len = self.getUint16() >> 1
                retVal = []
                for i in range(len):
                    retVal.append(self.getUint16())

            elif subatomicType == STUint32array:
                len = self.getUint16() >> 2
                retVal = []
                for i in range(len):
                    retVal.append(self.getUint32())

            elif subatomicType == STUint32uint8array:
                len = self.getUint16() / 5
                retVal = []
                for i in range(len):
                    a = self.getUint32()
                    b = self.getUint8()
                    retVal.append((a, b))

            else:
                raise Exception('Error: No such type as: ' + str(subAtomicType))
        else:
            getFunc = self.FuncDict.get(subatomicType)
            if getFunc:
                retVal = getFunc(self) / float(divisor)
            elif subatomicType == STInt8array:
                len = self.getUint8() >> 1
                retVal = []
                for i in range(len):
                    retVal.append(self.getInt8() / float(divisor))

            elif subatomicType == STInt16array:
                len = self.getUint16() >> 1
                retVal = []
                for i in range(len):
                    retVal.append(self.getInt16() / float(divisor))

            elif subatomicType == STInt32array:
                len = self.getUint16() >> 2
                retVal = []
                for i in range(len):
                    retVal.append(self.getInt32() / float(divisor))

            elif subatomicType == STUint8array:
                len = self.getUint8() >> 1
                retVal = []
                for i in range(len):
                    retVal.append(self.getUint8() / float(divisor))

            elif subatomicType == STUint16array:
                len = self.getUint16() >> 1
                retVal = []
                for i in range(len):
                    retVal.append(self.getUint16() / float(divisor))

            elif subatomicType == STUint32array:
                len = self.getUint16() >> 2
                retVal = []
                for i in range(len):
                    retVal.append(self.getUint32() / float(divisor))

            elif subatomicType == STUint32uint8array:
                len = self.getUint16() / 5
                retVal = []
                for i in range(len):
                    a = self.getUint32()
                    b = self.getUint8()
                    retVal.append((a / float(divisor), b / float(divisor)))

            else:
                raise Exception('Error: No such type as: ' + str(subatomicType))
        return retVal