# File: A (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedReferenceCount

class AudioSound(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    READY = 1
    BAD = 0
    PLAYING = 2
    
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
        

    
    def getClassType():
        returnValue = libpanda._inPMC2_wXI1()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def play(self):
        returnValue = libpanda._inPMC2__vhh(self.this)
        return returnValue

    
    def stop(self):
        returnValue = libpanda._inPMC2_dOiG(self.this)
        return returnValue

    
    def _AudioSound__overloaded_setLoop_ptrAudioSound_bool(self, loop):
        returnValue = libpanda._inPMC2_sQm7(self.this, loop)
        return returnValue

    
    def _AudioSound__overloaded_setLoop_ptrAudioSound(self):
        returnValue = libpanda._inPMC2_epXp(self.this)
        return returnValue

    
    def getLoop(self):
        returnValue = libpanda._inPMC2_k9fo(self.this)
        return returnValue

    
    def _AudioSound__overloaded_setLoopCount_ptrAudioSound_longUnsignedlongint(self, loopCount):
        returnValue = libpanda._inPMC2_ZahU(self.this, loopCount)
        return returnValue

    
    def _AudioSound__overloaded_setLoopCount_ptrAudioSound(self):
        returnValue = libpanda._inPMC2_VL64(self.this)
        return returnValue

    
    def getLoopCount(self):
        returnValue = libpanda._inPMC2_UTas(self.this)
        return returnValue

    
    def _AudioSound__overloaded_setTime_ptrAudioSound_float(self, startTime):
        returnValue = libpanda._inPMC2_sxJX(self.this, startTime)
        return returnValue

    
    def _AudioSound__overloaded_setTime_ptrAudioSound(self):
        returnValue = libpanda._inPMC2_2n_4(self.this)
        return returnValue

    
    def getTime(self):
        returnValue = libpanda._inPMC2_hsI4(self.this)
        return returnValue

    
    def _AudioSound__overloaded_setVolume_ptrAudioSound_float(self, volume):
        returnValue = libpanda._inPMC2_e1I3(self.this, volume)
        return returnValue

    
    def _AudioSound__overloaded_setVolume_ptrAudioSound(self):
        returnValue = libpanda._inPMC2_7_nT(self.this)
        return returnValue

    
    def getVolume(self):
        returnValue = libpanda._inPMC2_zxr3(self.this)
        return returnValue

    
    def _AudioSound__overloaded_setBalance_ptrAudioSound_float(self, balanceRight):
        returnValue = libpanda._inPMC2_npIq(self.this, balanceRight)
        return returnValue

    
    def _AudioSound__overloaded_setBalance_ptrAudioSound(self):
        returnValue = libpanda._inPMC2_J3_4(self.this)
        return returnValue

    
    def getBalance(self):
        returnValue = libpanda._inPMC2_wRl7(self.this)
        return returnValue

    
    def _AudioSound__overloaded_setActive_ptrAudioSound_bool(self, flag):
        returnValue = libpanda._inPMC2__M0J(self.this, flag)
        return returnValue

    
    def _AudioSound__overloaded_setActive_ptrAudioSound(self):
        returnValue = libpanda._inPMC2_THGV(self.this)
        return returnValue

    
    def getActive(self):
        returnValue = libpanda._inPMC2_yDK5(self.this)
        return returnValue

    
    def setFinishedEvent(self, event):
        returnValue = libpanda._inPMC2_kLpd(self.this, event)
        return returnValue

    
    def getFinishedEvent(self):
        returnValue = libpanda._inPMC2_yGD1(self.this)
        return returnValue

    
    def getName(self):
        returnValue = libpanda._inPMC2_10F5(self.this)
        return returnValue

    
    def length(self):
        returnValue = libpanda._inPMC2_1TDx(self.this)
        return returnValue

    
    def set3dAttributes(self, px, py, pz, vx, vy, vz):
        returnValue = libpanda._inPMC2_OwRY(self.this, px, py, pz, vx, vy, vz)
        return returnValue

    
    def status(self):
        returnValue = libpanda._inPMC2_mGiV(self.this)
        return returnValue

    
    def setLoopCount(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._AudioSound__overloaded_setLoopCount_ptrAudioSound(*_args)
        elif numArgs == 1:
            return self._AudioSound__overloaded_setLoopCount_ptrAudioSound_longUnsignedlongint(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setTime(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._AudioSound__overloaded_setTime_ptrAudioSound(*_args)
        elif numArgs == 1:
            return self._AudioSound__overloaded_setTime_ptrAudioSound_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setBalance(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._AudioSound__overloaded_setBalance_ptrAudioSound(*_args)
        elif numArgs == 1:
            return self._AudioSound__overloaded_setBalance_ptrAudioSound_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setActive(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._AudioSound__overloaded_setActive_ptrAudioSound(*_args)
        elif numArgs == 1:
            return self._AudioSound__overloaded_setActive_ptrAudioSound_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setLoop(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._AudioSound__overloaded_setLoop_ptrAudioSound(*_args)
        elif numArgs == 1:
            return self._AudioSound__overloaded_setLoop_ptrAudioSound_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setVolume(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._AudioSound__overloaded_setVolume_ptrAudioSound(*_args)
        elif numArgs == 1:
            return self._AudioSound__overloaded_setVolume_ptrAudioSound_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


