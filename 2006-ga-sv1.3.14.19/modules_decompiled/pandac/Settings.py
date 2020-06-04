# File: S (Python 2.2)

import types
import libotp
import libotpDowncasts
from direct.ffi import FFIExternalObject

class Settings(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libotpDowncasts]
    DDEFAULT = 2
    DX9 = 3
    DX8 = 5
    DX7 = 1
    GL = 0
    DNONE = 4
    DEVELOPMENT = 1
    DEBUG = 2
    SNONE = 3
    PRODUCTION = 0
    R640x480 = 0
    RNONE = 5
    R1280x1024 = 3
    R1600x1200 = 4
    R800x600 = 1
    R1024x768 = 2
    
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
        

    
    def destructor(self):
        if libotp and libotp._inPvzzkBOGO:
            libotp._inPvzzkBOGO(self.this)
        

    
    def getSfx():
        returnValue = libotp._inPvzzks4E_()
        return returnValue

    getSfx = staticmethod(getSfx)
    
    def getMusic():
        returnValue = libotp._inPvzzkepCV()
        return returnValue

    getMusic = staticmethod(getMusic)
    
    def getForceSwMidi():
        returnValue = libotp._inPvzzk236s()
        return returnValue

    getForceSwMidi = staticmethod(getForceSwMidi)
    
    def getWindowedMode():
        returnValue = libotp._inPvzzk2FPf()
        return returnValue

    getWindowedMode = staticmethod(getWindowedMode)
    
    def wantChatLog():
        returnValue = libotp._inPvzzku4rU()
        return returnValue

    wantChatLog = staticmethod(wantChatLog)
    
    def getShowFpsmeter():
        returnValue = libotp._inPvzzkRscm()
        return returnValue

    getShowFpsmeter = staticmethod(getShowFpsmeter)
    
    def wantCustomMouseCursor():
        returnValue = libotp._inPvzzk4lpw()
        return returnValue

    wantCustomMouseCursor = staticmethod(wantCustomMouseCursor)
    
    def getSfxVolume():
        returnValue = libotp._inPvzzkuR_I()
        return returnValue

    getSfxVolume = staticmethod(getSfxVolume)
    
    def getMusicVolume():
        returnValue = libotp._inPvzzk_80e()
        return returnValue

    getMusicVolume = staticmethod(getMusicVolume)
    
    def displayDriver():
        returnValue = libotp._inPvzzkioaR()
        return returnValue

    displayDriver = staticmethod(displayDriver)
    
    def getResolution():
        returnValue = libotp._inPvzzkSKJ6()
        return returnValue

    getResolution = staticmethod(getResolution)
    
    def serverType():
        returnValue = libotp._inPvzzkj_Ac()
        return returnValue

    serverType = staticmethod(serverType)
    
    def setSfx(parameter0):
        returnValue = libotp._inPvzzkucU5(parameter0)
        return returnValue

    setSfx = staticmethod(setSfx)
    
    def setMusic(parameter0):
        returnValue = libotp._inPvzzktTiE(parameter0)
        return returnValue

    setMusic = staticmethod(setMusic)
    
    def setForceSwMidi(parameter0):
        returnValue = libotp._inPvzzku1SX(parameter0)
        return returnValue

    setForceSwMidi = staticmethod(setForceSwMidi)
    
    def setCustomMouseCursor(parameter0):
        returnValue = libotp._inPvzzkanHQ(parameter0)
        return returnValue

    setCustomMouseCursor = staticmethod(setCustomMouseCursor)
    
    def setChatLog(parameter0):
        returnValue = libotp._inPvzzkWMX_(parameter0)
        return returnValue

    setChatLog = staticmethod(setChatLog)
    
    def setWindowedMode(parameter0):
        returnValue = libotp._inPvzzkX2kJ(parameter0)
        return returnValue

    setWindowedMode = staticmethod(setWindowedMode)
    
    def setSfxVolume(parameter0):
        returnValue = libotp._inPvzzkWXyv(parameter0)
        return returnValue

    setSfxVolume = staticmethod(setSfxVolume)
    
    def setMusicVolume(parameter0):
        returnValue = libotp._inPvzzkUR8p(parameter0)
        return returnValue

    setMusicVolume = staticmethod(setMusicVolume)
    
    def setDisplayDriver(parameter0):
        returnValue = libotp._inPvzzkh3tg(parameter0)
        return returnValue

    setDisplayDriver = staticmethod(setDisplayDriver)
    
    def setResolution(parameter0):
        returnValue = libotp._inPvzzksPdA(parameter0)
        return returnValue

    setResolution = staticmethod(setResolution)
    
    def setResolutionDimensions(xsize, ysize):
        returnValue = libotp._inPvzzkN9or(xsize, ysize)
        return returnValue

    setResolutionDimensions = staticmethod(setResolutionDimensions)
    
    def setServerType(parameter0):
        returnValue = libotp._inPvzzkbcgR(parameter0)
        return returnValue

    setServerType = staticmethod(setServerType)
    
    def setShowFpsmeter(parameter0):
        returnValue = libotp._inPvzzk1bzQ(parameter0)
        return returnValue

    setShowFpsmeter = staticmethod(setShowFpsmeter)
    
    def doSavedSettingsExist():
        returnValue = libotp._inPvzzkqBON()
        return returnValue

    doSavedSettingsExist = staticmethod(doSavedSettingsExist)
    
    def writeSettings():
        returnValue = libotp._inPvzzkHhMG()
        return returnValue

    writeSettings = staticmethod(writeSettings)

