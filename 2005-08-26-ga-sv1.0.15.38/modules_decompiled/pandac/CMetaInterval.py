# File: C (Python 2.2)

import types
import libdirect
import libdirectDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import CInterval

class CMetaInterval(CInterval.CInterval, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libdirectDowncasts,
        libpandaexpressDowncasts]
    RSPreviousEnd = 0
    RSPreviousBegin = 1
    RSLevelBegin = 2
    DTExtIndex = 1
    DTPopLevel = 3
    DTPushLevel = 2
    DTCInterval = 0
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libdirect._inPSpsCfll2(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libdirect._inPSpsCQy_U()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setPrecision(self, precision):
        returnValue = libdirect._inPSpsCxSCe(self.this, precision)
        return returnValue

    
    def getPrecision(self):
        returnValue = libdirect._inPSpsC5PcZ(self.this)
        return returnValue

    
    def clearIntervals(self):
        returnValue = libdirect._inPSpsCS3bp(self.this)
        return returnValue

    
    def pushLevel(self, name, relTime, relTo):
        returnValue = libdirect._inPSpsCe1kF(self.this, name, relTime, relTo)
        return returnValue

    
    def addCInterval(self, cInterval, relTime, relTo):
        returnValue = libdirect._inPSpsC8fyX(self.this, cInterval.this, relTime, relTo)
        return returnValue

    
    def addExtIndex(self, extIndex, name, duration, openEnded, relTime, relTo):
        returnValue = libdirect._inPSpsCsI0L(self.this, extIndex, name, duration, openEnded, relTime, relTo)
        return returnValue

    
    def _CMetaInterval__overloaded_popLevel_ptrCMetaInterval_double(self, duration):
        returnValue = libdirect._inPSpsCAQho(self.this, duration)
        return returnValue

    
    def _CMetaInterval__overloaded_popLevel_ptrCMetaInterval(self):
        returnValue = libdirect._inPSpsCcB29(self.this)
        return returnValue

    
    def _CMetaInterval__overloaded_setIntervalStartTime_ptrCMetaInterval_atomicstring_double___enum__RelativeStart(self, name, relTime, relTo):
        returnValue = libdirect._inPSpsCbNvh(self.this, name, relTime, relTo)
        return returnValue

    
    def _CMetaInterval__overloaded_setIntervalStartTime_ptrCMetaInterval_atomicstring_double(self, name, relTime):
        returnValue = libdirect._inPSpsCDRqF(self.this, name, relTime)
        return returnValue

    
    def getIntervalStartTime(self, name):
        returnValue = libdirect._inPSpsCnjRJ(self.this, name)
        return returnValue

    
    def getIntervalEndTime(self, name):
        returnValue = libdirect._inPSpsCwxHv(self.this, name)
        return returnValue

    
    def getNumDefs(self):
        returnValue = libdirect._inPSpsC4MwM(self.this)
        return returnValue

    
    def getDefType(self, n):
        returnValue = libdirect._inPSpsCleqy(self.this, n)
        return returnValue

    
    def getCInterval(self, n):
        returnValue = libdirect._inPSpsClcyM(self.this, n)
        import CInterval
        returnObject = CInterval.CInterval(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getExtIndex(self, n):
        returnValue = libdirect._inPSpsCDZwS(self.this, n)
        return returnValue

    
    def isEventReady(self):
        returnValue = libdirect._inPSpsCG_g4(self.this)
        return returnValue

    
    def getEventIndex(self):
        returnValue = libdirect._inPSpsCdJvv(self.this)
        return returnValue

    
    def getEventT(self):
        returnValue = libdirect._inPSpsCPQNU(self.this)
        return returnValue

    
    def getEventType(self):
        returnValue = libdirect._inPSpsCsP8v(self.this)
        return returnValue

    
    def popEvent(self):
        returnValue = libdirect._inPSpsC4v7o(self.this)
        return returnValue

    
    def timeline(self, out):
        returnValue = libdirect._inPSpsCXzrj(self.this, out.this)
        return returnValue

    
    def setIntervalStartTime(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._CMetaInterval__overloaded_setIntervalStartTime_ptrCMetaInterval_atomicstring_double(*_args)
        elif numArgs == 3:
            return self._CMetaInterval__overloaded_setIntervalStartTime_ptrCMetaInterval_atomicstring_double___enum__RelativeStart(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def popLevel(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._CMetaInterval__overloaded_popLevel_ptrCMetaInterval(*_args)
        elif numArgs == 1:
            return self._CMetaInterval__overloaded_popLevel_ptrCMetaInterval_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


