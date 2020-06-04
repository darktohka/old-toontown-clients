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

    
    def getSound(self, fileName):
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

    
    def setConcurrentSoundLimit(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._AudioManager__overloaded_setConcurrentSoundLimit_ptrAudioManager(*_args)
        elif numArgs == 1:
            return self._AudioManager__overloaded_setConcurrentSoundLimit_ptrAudioManager_unsignedint(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


