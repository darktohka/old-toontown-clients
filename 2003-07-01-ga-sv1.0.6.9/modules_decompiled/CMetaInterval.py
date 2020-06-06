# File: C (Python 2.2)

import types
import libdirect
import libdirectDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
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
        
        apply(self.constructor, _args)

    
    def constructor(self, name):
        self.this = libdirect._inPSpsCell2(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libdirect and libdirect._inPSpsCAEo2:
            libdirect._inPSpsCAEo2(self.this)
        

    
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
        returnValue = libdirect._inPSpsCR3bp(self.this)
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
        returnValue = libdirect._inPSpsCDQho(self.this, duration)
        return returnValue

    
    def _CMetaInterval__overloaded_popLevel_ptrCMetaInterval(self):
        returnValue = libdirect._inPSpsCbB29(self.this)
        return returnValue

    
    def _CMetaInterval__overloaded_setIntervalStartTime_ptrCMetaInterval_atomicstring_double___enum__RelativeStart(self, name, relTime, relTo):
        returnValue = libdirect._inPSpsCaNvh(self.this, name, relTime, relTo)
        return returnValue

    
    def _CMetaInterval__overloaded_setIntervalStartTime_ptrCMetaInterval_atomicstring_double(self, name, relTime):
        returnValue = libdirect._inPSpsCDRqF(self.this, name, relTime)
        return returnValue

    
    def getIntervalStartTime(self, name):
        returnValue = libdirect._inPSpsCnjRJ(self.this, name)
        return returnValue

    
    def getIntervalEndTime(self, name):
        returnValue = libdirect._inPSpsC3xHv(self.this, name)
        return returnValue

    
    def getNumDefs(self):
        returnValue = libdirect._inPSpsC4MwM(self.this)
        return returnValue

    
    def getDefType(self, n):
        returnValue = libdirect._inPSpsCmeqy(self.this, n)
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
        returnValue = libdirect._inPSpsCH_g4(self.this)
        return returnValue

    
    def getEventIndex(self):
        returnValue = libdirect._inPSpsCaJvv(self.this)
        return returnValue

    
    def getEventT(self):
        returnValue = libdirect._inPSpsCPQNU(self.this)
        return returnValue

    
    def getEventType(self):
        returnValue = libdirect._inPSpsCvP8v(self.this)
        return returnValue

    
    def popEvent(self):
        returnValue = libdirect._inPSpsC_v7o(self.this)
        return returnValue

    
    def timeline(self, out):
        returnValue = libdirect._inPSpsCWzrj(self.this, out.this)
        return returnValue

    
    def setIntervalStartTime(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._CMetaInterval__overloaded_setIntervalStartTime_ptrCMetaInterval_atomicstring_double(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.IntType):
                        return self._CMetaInterval__overloaded_setIntervalStartTime_ptrCMetaInterval_atomicstring_double___enum__RelativeStart(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def popLevel(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._CMetaInterval__overloaded_popLevel_ptrCMetaInterval()
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._CMetaInterval__overloaded_popLevel_ptrCMetaInterval_double(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


