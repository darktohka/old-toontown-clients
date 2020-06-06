# File: S (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import FFIExternalObject

class Settings(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts]
    DX7 = 1
    GL = 0
    DNONE = 3
    DX8 = 2
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
        
        apply(self.constructor, _args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPszzkBOGO:
            libtoontown._inPszzkBOGO(self.this)
        

    
    def getSfx():
        returnValue = libtoontown._inPszzkt4E_()
        return returnValue

    getSfx = staticmethod(getSfx)
    
    def getMusic():
        returnValue = libtoontown._inPszzkepCV()
        return returnValue

    getMusic = staticmethod(getMusic)
    
    def getForceSwMidi():
        returnValue = libtoontown._inPszzk536s()
        return returnValue

    getForceSwMidi = staticmethod(getForceSwMidi)
    
    def getWindowedMode():
        returnValue = libtoontown._inPszzk2FPf()
        return returnValue

    getWindowedMode = staticmethod(getWindowedMode)
    
    def wantChatLog():
        returnValue = libtoontown._inPszzku4rU()
        return returnValue

    wantChatLog = staticmethod(wantChatLog)
    
    def getShowFpsmeter():
        returnValue = libtoontown._inPszzkQscm()
        return returnValue

    getShowFpsmeter = staticmethod(getShowFpsmeter)
    
    def wantCustomMouseCursor():
        returnValue = libtoontown._inPszzk_lpw()
        return returnValue

    wantCustomMouseCursor = staticmethod(wantCustomMouseCursor)
    
    def getSfxVolume():
        returnValue = libtoontown._inPszzkuR_I()
        return returnValue

    getSfxVolume = staticmethod(getSfxVolume)
    
    def getMusicVolume():
        returnValue = libtoontown._inPszzk_80e()
        return returnValue

    getMusicVolume = staticmethod(getMusicVolume)
    
    def displayDriver():
        returnValue = libtoontown._inPszzkioaR()
        return returnValue

    displayDriver = staticmethod(displayDriver)
    
    def getResolution():
        returnValue = libtoontown._inPszzkTKJ6()
        return returnValue

    getResolution = staticmethod(getResolution)
    
    def serverType():
        returnValue = libtoontown._inPszzkj_Ac()
        return returnValue

    serverType = staticmethod(serverType)
    
    def setSfx(parameter0):
        returnValue = libtoontown._inPszzkvcU5(parameter0)
        return returnValue

    setSfx = staticmethod(setSfx)
    
    def setMusic(parameter0):
        returnValue = libtoontown._inPszzktTiE(parameter0)
        return returnValue

    setMusic = staticmethod(setMusic)
    
    def setForceSwMidi(parameter0):
        returnValue = libtoontown._inPszzku1SX(parameter0)
        return returnValue

    setForceSwMidi = staticmethod(setForceSwMidi)
    
    def setCustomMouseCursor(parameter0):
        returnValue = libtoontown._inPszzkanHQ(parameter0)
        return returnValue

    setCustomMouseCursor = staticmethod(setCustomMouseCursor)
    
    def setChatLog(parameter0):
        returnValue = libtoontown._inPszzkVMX_(parameter0)
        return returnValue

    setChatLog = staticmethod(setChatLog)
    
    def setWindowedMode(parameter0):
        returnValue = libtoontown._inPszzkX2kJ(parameter0)
        return returnValue

    setWindowedMode = staticmethod(setWindowedMode)
    
    def setSfxVolume(parameter0):
        returnValue = libtoontown._inPszzkVXyv(parameter0)
        return returnValue

    setSfxVolume = staticmethod(setSfxVolume)
    
    def setMusicVolume(parameter0):
        returnValue = libtoontown._inPszzkXR8p(parameter0)
        return returnValue

    setMusicVolume = staticmethod(setMusicVolume)
    
    def setDisplayDriver(parameter0):
        returnValue = libtoontown._inPszzkm3tg(parameter0)
        return returnValue

    setDisplayDriver = staticmethod(setDisplayDriver)
    
    def setResolution(parameter0):
        returnValue = libtoontown._inPszzksPdA(parameter0)
        return returnValue

    setResolution = staticmethod(setResolution)
    
    def setResolutionDimensions(xsize, ysize):
        returnValue = libtoontown._inPszzkM9or(xsize, ysize)
        return returnValue

    setResolutionDimensions = staticmethod(setResolutionDimensions)
    
    def setServerType(parameter0):
        returnValue = libtoontown._inPszzkbcgR(parameter0)
        return returnValue

    setServerType = staticmethod(setServerType)
    
    def setShowFpsmeter(parameter0):
        returnValue = libtoontown._inPszzk1bzQ(parameter0)
        return returnValue

    setShowFpsmeter = staticmethod(setShowFpsmeter)
    
    def doSavedSettingsExist():
        returnValue = libtoontown._inPszzkqBON()
        return returnValue

    doSavedSettingsExist = staticmethod(doSavedSettingsExist)
    
    def writeSettings():
        returnValue = libtoontown._inPszzkHhMG()
        return returnValue

    writeSettings = staticmethod(writeSettings)

