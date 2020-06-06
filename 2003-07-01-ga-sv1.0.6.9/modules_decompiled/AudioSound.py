# File: A (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ReferenceCount

class AudioSound(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
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
        
        apply(self.constructor, _args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPPC2__Ha6:
            libpanda._inPPC2__Ha6(self.this)
        

    
    def play(self):
        returnValue = libpanda._inPPC2_9vhh(self.this)
        return returnValue

    
    def stop(self):
        returnValue = libpanda._inPPC2_dOiG(self.this)
        return returnValue

    
    def _AudioSound__overloaded_setLoop_ptrAudioSound_bool(self, loop):
        returnValue = libpanda._inPPC2_tQm7(self.this, loop)
        return returnValue

    
    def _AudioSound__overloaded_setLoop_ptrAudioSound(self):
        returnValue = libpanda._inPPC2_RpXp(self.this)
        return returnValue

    
    def getLoop(self):
        returnValue = libpanda._inPPC2_j9fo(self.this)
        return returnValue

    
    def _AudioSound__overloaded_setLoopCount_ptrAudioSound_longUnsignedlongint(self, loopCount):
        returnValue = libpanda._inPPC2_ZahU(self.this, loopCount)
        return returnValue

    
    def _AudioSound__overloaded_setLoopCount_ptrAudioSound(self):
        returnValue = libpanda._inPPC2_WL64(self.this)
        return returnValue

    
    def getLoopCount(self):
        returnValue = libpanda._inPPC2_VTas(self.this)
        return returnValue

    
    def _AudioSound__overloaded_setTime_ptrAudioSound_float(self, startTime):
        returnValue = libpanda._inPPC2_sxJX(self.this, startTime)
        return returnValue

    
    def _AudioSound__overloaded_setTime_ptrAudioSound(self):
        returnValue = libpanda._inPPC2_1n_4(self.this)
        return returnValue

    
    def getTime(self):
        returnValue = libpanda._inPPC2_gsI4(self.this)
        return returnValue

    
    def _AudioSound__overloaded_setVolume_ptrAudioSound_float(self, volume):
        returnValue = libpanda._inPPC2_f1I3(self.this, volume)
        return returnValue

    
    def _AudioSound__overloaded_setVolume_ptrAudioSound(self):
        returnValue = libpanda._inPPC2_7_nT(self.this)
        return returnValue

    
    def getVolume(self):
        returnValue = libpanda._inPPC2_yxr3(self.this)
        return returnValue

    
    def _AudioSound__overloaded_setBalance_ptrAudioSound_float(self, balanceRight):
        returnValue = libpanda._inPPC2_mpIq(self.this, balanceRight)
        return returnValue

    
    def _AudioSound__overloaded_setBalance_ptrAudioSound(self):
        returnValue = libpanda._inPPC2_I3_4(self.this)
        return returnValue

    
    def getBalance(self):
        returnValue = libpanda._inPPC2_3Rl7(self.this)
        return returnValue

    
    def _AudioSound__overloaded_setActive_ptrAudioSound_bool(self, flag):
        returnValue = libpanda._inPPC2__M0J(self.this, flag)
        return returnValue

    
    def _AudioSound__overloaded_setActive_ptrAudioSound(self):
        returnValue = libpanda._inPPC2_THGV(self.this)
        return returnValue

    
    def getActive(self):
        returnValue = libpanda._inPPC2_tDK5(self.this)
        return returnValue

    
    def getName(self):
        returnValue = libpanda._inPPC2_00F5(self.this)
        return returnValue

    
    def length(self):
        returnValue = libpanda._inPPC2_6TDx(self.this)
        return returnValue

    
    def status(self):
        returnValue = libpanda._inPPC2_mGiV(self.this)
        return returnValue

    
    def setLoopCount(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._AudioSound__overloaded_setLoopCount_ptrAudioSound()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._AudioSound__overloaded_setLoopCount_ptrAudioSound_longUnsignedlongint(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setTime(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._AudioSound__overloaded_setTime_ptrAudioSound()
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._AudioSound__overloaded_setTime_ptrAudioSound_float(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setBalance(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._AudioSound__overloaded_setBalance_ptrAudioSound()
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._AudioSound__overloaded_setBalance_ptrAudioSound_float(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setActive(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._AudioSound__overloaded_setActive_ptrAudioSound()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._AudioSound__overloaded_setActive_ptrAudioSound_bool(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setLoop(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._AudioSound__overloaded_setLoop_ptrAudioSound()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._AudioSound__overloaded_setLoop_ptrAudioSound_bool(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setVolume(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._AudioSound__overloaded_setVolume_ptrAudioSound()
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._AudioSound__overloaded_setVolume_ptrAudioSound_float(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


