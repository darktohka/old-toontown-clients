# File: A (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ReferenceCount

class AudioManager(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
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
        if libpanda and libpanda._inPPC2_n5Hd:
            libpanda._inPPC2_n5Hd(self.this)
        

    
    def createAudioManager():
        returnValue = libpanda._inPPC2_vL8W()
        returnObject = AudioManager(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    createAudioManager = staticmethod(createAudioManager)
    
    def isValid(self):
        returnValue = libpanda._inPPC2_YnlD(self.this)
        return returnValue

    
    def getSound(self, fileName):
        returnValue = libpanda._inPPC2_yCgN(self.this, fileName)
        import AudioSound
        returnObject = AudioSound.AudioSound(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getNullSound(self):
        returnValue = libpanda._inPPC2_o8vb(self.this)
        import AudioSound
        returnObject = AudioSound.AudioSound(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def uncacheSound(self, fileName):
        returnValue = libpanda._inPPC2_PTiB(self.this, fileName)
        return returnValue

    
    def clearCache(self):
        returnValue = libpanda._inPPC2_V3uV(self.this)
        return returnValue

    
    def setCacheLimit(self, count):
        returnValue = libpanda._inPPC2__3NU(self.this, count)
        return returnValue

    
    def getCacheLimit(self):
        returnValue = libpanda._inPPC2_5Q76(self.this)
        return returnValue

    
    def setMutuallyExclusive(self, bExclusive):
        returnValue = libpanda._inPPC2_Kj6N(self.this, bExclusive)
        return returnValue

    
    def setVolume(self, volume):
        returnValue = libpanda._inPPC2_qSxW(self.this, volume)
        return returnValue

    
    def getVolume(self):
        returnValue = libpanda._inPPC2_5V2w(self.this)
        return returnValue

    
    def setActive(self, flag):
        returnValue = libpanda._inPPC2_J_GE(self.this, flag)
        return returnValue

    
    def getActive(self):
        returnValue = libpanda._inPPC2_aQ9m(self.this)
        return returnValue


