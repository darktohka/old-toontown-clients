# File: A (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedReferenceCount

class AudioManager(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
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
        

    
    def createAudioManager():
        returnValue = libpanda._inPMC2_vL8W()
        returnObject = AudioManager(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    createAudioManager = staticmethod(createAudioManager)
    
    def getClassType():
        returnValue = libpanda._inPMC2_bs2a()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def isValid(self):
        returnValue = libpanda._inPMC2_YnlD(self.this)
        return returnValue

    
    def _AudioManager__overloaded_getSound_ptrAudioManager_atomicstring_bool(self, fileName, positional):
        returnValue = libpanda._inPMC2_z8cY(self.this, fileName, positional)
        import AudioSound
        returnObject = AudioSound.AudioSound(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _AudioManager__overloaded_getSound_ptrAudioManager_atomicstring(self, fileName):
        returnValue = libpanda._inPMC2_yCgN(self.this, fileName)
        import AudioSound
        returnObject = AudioSound.AudioSound(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNullSound(self):
        returnValue = libpanda._inPMC2_o8vb(self.this)
        import AudioSound
        returnObject = AudioSound.AudioSound(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def uncacheSound(self, fileName):
        returnValue = libpanda._inPMC2_PTiB(self.this, fileName)
        return returnValue

    
    def clearCache(self):
        returnValue = libpanda._inPMC2_V3uV(self.this)
        return returnValue

    
    def setCacheLimit(self, count):
        returnValue = libpanda._inPMC2_JsMW(self.this, count)
        return returnValue

    
    def getCacheLimit(self):
        returnValue = libpanda._inPMC2_Zu93(self.this)
        return returnValue

    
    def setVolume(self, volume):
        returnValue = libpanda._inPMC2_qSxW(self.this, volume)
        return returnValue

    
    def getVolume(self):
        returnValue = libpanda._inPMC2_r_Wv(self.this)
        return returnValue

    
    def setActive(self, flag):
        returnValue = libpanda._inPMC2_J_GE(self.this, flag)
        return returnValue

    
    def getActive(self):
        returnValue = libpanda._inPMC2_b_cl(self.this)
        return returnValue

    
    def _AudioManager__overloaded_setConcurrentSoundLimit_ptrAudioManager_unsignedint(self, limit):
        returnValue = libpanda._inPMC2_0VhR(self.this, limit)
        return returnValue

    
    def _AudioManager__overloaded_setConcurrentSoundLimit_ptrAudioManager(self):
        returnValue = libpanda._inPMC2_RuKw(self.this)
        return returnValue

    
    def getConcurrentSoundLimit(self):
        returnValue = libpanda._inPMC2_4gS3(self.this)
        return returnValue

    
    def reduceSoundsPlayingTo(self, count):
        returnValue = libpanda._inPMC2_UjBl(self.this, count)
        return returnValue

    
    def stopAllSounds(self):
        returnValue = libpanda._inPMC2_BZTi(self.this)
        return returnValue

    
    def audio3dUpdate(self):
        returnValue = libpanda._inPMC2_KRZx(self.this)
        return returnValue

    
    def audio3dSetListenerAttributes(self, px, py, pz, vx, vy, vz, fx, fy, fz, ux, uy, uz):
        returnValue = libpanda._inPMC2_BiqK(self.this, px, py, pz, vx, vy, vz, fx, fy, fz, ux, uy, uz)
        return returnValue

    
    def audio3dSetDistanceFactor(self, factor):
        returnValue = libpanda._inPMC2_BlhR(self.this, factor)
        return returnValue

    
    def audio3dGetDistanceFactor(self):
        returnValue = libpanda._inPMC2_hJ5G(self.this)
        return returnValue

    
    def audio3dSetDopplerFactor(self, factor):
        returnValue = libpanda._inPMC2_R8Fh(self.this, factor)
        return returnValue

    
    def audio3dGetDopplerFactor(self):
        returnValue = libpanda._inPMC2_hs_N(self.this)
        return returnValue

    
    def audio3dSetDropOffFactor(self, factor):
        returnValue = libpanda._inPMC2_QhOE(self.this, factor)
        return returnValue

    
    def audio3dGetDropOffFactor(self):
        returnValue = libpanda._inPMC2_V1m5(self.this)
        return returnValue

    
    def getSound(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._AudioManager__overloaded_getSound_ptrAudioManager_atomicstring(*_args)
        elif numArgs == 2:
            return self._AudioManager__overloaded_getSound_ptrAudioManager_atomicstring_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setConcurrentSoundLimit(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._AudioManager__overloaded_setConcurrentSoundLimit_ptrAudioManager(*_args)
        elif numArgs == 1:
            return self._AudioManager__overloaded_setConcurrentSoundLimit_ptrAudioManager_unsignedint(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


