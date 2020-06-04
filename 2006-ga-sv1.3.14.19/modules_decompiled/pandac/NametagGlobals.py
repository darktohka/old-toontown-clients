# File: N (Python 2.2)

import types
import libotp
import libotpDowncasts
from direct.ffi import FFIExternalObject

class NametagGlobals(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libotpDowncasts]
    
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
        if libotp and libotp._inPPj7bVBF8:
            libotp._inPPj7bVBF8(self.this)
        

    
    def getNameWordwrap():
        returnValue = libotp._inPPj7bn9Im()
        return returnValue

    getNameWordwrap = staticmethod(getNameWordwrap)
    
    def getCardPad():
        returnValue = libotp._inPPj7bQaV7()
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getCardPad = staticmethod(getCardPad)
    
    def setCamera(node):
        returnValue = libotp._inPPj7byeog(node.this)
        return returnValue

    setCamera = staticmethod(setCamera)
    
    def getCamera():
        returnValue = libotp._inPPj7bfEEo()
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getCamera = staticmethod(getCamera)
    
    def setToon(node):
        returnValue = libotp._inPPj7bLhdm(node.this)
        return returnValue

    setToon = staticmethod(setToon)
    
    def getToon():
        returnValue = libotp._inPPj7bv_Rg()
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getToon = staticmethod(getToon)
    
    def setArrowModel(node):
        returnValue = libotp._inPPj7bB2bD(node.this)
        return returnValue

    setArrowModel = staticmethod(setArrowModel)
    
    def getArrowModel():
        returnValue = libotp._inPPj7bet3M()
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getArrowModel = staticmethod(getArrowModel)
    
    def setPageButton(state, node):
        returnValue = libotp._inPPj7bSPiB(state, node.this)
        return returnValue

    setPageButton = staticmethod(setPageButton)
    
    def getPageButton(state):
        returnValue = libotp._inPPj7bGqo0(state)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getPageButton = staticmethod(getPageButton)
    
    def setQuitButton(state, node):
        returnValue = libotp._inPPj7buW_H(state, node.this)
        return returnValue

    setQuitButton = staticmethod(setQuitButton)
    
    def getQuitButton(state):
        returnValue = libotp._inPPj7bKDE7(state)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getQuitButton = staticmethod(getQuitButton)
    
    def setNametagCard(node, frame):
        returnValue = libotp._inPPj7bO7HT(node.this, frame.this)
        return returnValue

    setNametagCard = staticmethod(setNametagCard)
    
    def getNametagCard():
        returnValue = libotp._inPPj7baqdr()
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getNametagCard = staticmethod(getNametagCard)
    
    def getNametagCardFrame():
        returnValue = libotp._inPPj7br0Kj()
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getNametagCardFrame = staticmethod(getNametagCardFrame)
    
    def setRolloverSound(sound):
        returnValue = libotp._inPPj7bq4M4(sound.this)
        return returnValue

    setRolloverSound = staticmethod(setRolloverSound)
    
    def getRolloverSound():
        returnValue = libotp._inPPj7bE66T()
        import AudioSound
        returnObject = AudioSound.AudioSound(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    getRolloverSound = staticmethod(getRolloverSound)
    
    def setClickSound(sound):
        returnValue = libotp._inPPj7bbRDq(sound.this)
        return returnValue

    setClickSound = staticmethod(setClickSound)
    
    def getClickSound():
        returnValue = libotp._inPPj7bRsf2()
        import AudioSound
        returnObject = AudioSound.AudioSound(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    getClickSound = staticmethod(getClickSound)
    
    def setMouseWatcher(watcher):
        returnValue = libotp._inPPj7bPlgS(watcher.this)
        return returnValue

    setMouseWatcher = staticmethod(setMouseWatcher)
    
    def getMouseWatcher():
        returnValue = libotp._inPPj7bjGmX()
        import MouseWatcher
        returnObject = MouseWatcher.MouseWatcher(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    getMouseWatcher = staticmethod(getMouseWatcher)
    
    def setSpeechBalloon2d(balloon):
        returnValue = libotp._inPPj7bvc69(balloon.this)
        return returnValue

    setSpeechBalloon2d = staticmethod(setSpeechBalloon2d)
    
    def getSpeechBalloon2d():
        returnValue = libotp._inPPj7bD_yZ()
        import ChatBalloon
        returnObject = ChatBalloon.ChatBalloon(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getSpeechBalloon2d = staticmethod(getSpeechBalloon2d)
    
    def setThoughtBalloon2d(balloon):
        returnValue = libotp._inPPj7b2ehI(balloon.this)
        return returnValue

    setThoughtBalloon2d = staticmethod(setThoughtBalloon2d)
    
    def getThoughtBalloon2d():
        returnValue = libotp._inPPj7bezGc()
        import ChatBalloon
        returnObject = ChatBalloon.ChatBalloon(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getThoughtBalloon2d = staticmethod(getThoughtBalloon2d)
    
    def setSpeechBalloon3d(balloon):
        returnValue = libotp._inPPj7buuXA(balloon.this)
        return returnValue

    setSpeechBalloon3d = staticmethod(setSpeechBalloon3d)
    
    def getSpeechBalloon3d():
        returnValue = libotp._inPPj7bDJRc()
        import ChatBalloon
        returnObject = ChatBalloon.ChatBalloon(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getSpeechBalloon3d = staticmethod(getSpeechBalloon3d)
    
    def setThoughtBalloon3d(balloon):
        returnValue = libotp._inPPj7b1emW(balloon.this)
        return returnValue

    setThoughtBalloon3d = staticmethod(setThoughtBalloon3d)
    
    def getThoughtBalloon3d():
        returnValue = libotp._inPPj7bZzNq()
        import ChatBalloon
        returnObject = ChatBalloon.ChatBalloon(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getThoughtBalloon3d = staticmethod(getThoughtBalloon3d)
    
    def setMasterNametagsActive(active):
        returnValue = libotp._inPPj7bw2Ct(active)
        return returnValue

    setMasterNametagsActive = staticmethod(setMasterNametagsActive)
    
    def getMasterNametagsActive():
        returnValue = libotp._inPPj7b_f_m()
        return returnValue

    getMasterNametagsActive = staticmethod(getMasterNametagsActive)
    
    def setMasterArrowsOn(active):
        returnValue = libotp._inPPj7bUMYq(active)
        return returnValue

    setMasterArrowsOn = staticmethod(setMasterArrowsOn)
    
    def getMasterArrowsOn():
        returnValue = libotp._inPPj7brJpy()
        return returnValue

    getMasterArrowsOn = staticmethod(getMasterArrowsOn)
    
    def setOnscreenChatForced(active):
        returnValue = libotp._inPPj7bocod(active)
        return returnValue

    setOnscreenChatForced = staticmethod(setOnscreenChatForced)
    
    def getOnscreenChatForced():
        returnValue = libotp._inPPj7bZOQ_()
        return returnValue

    getOnscreenChatForced = staticmethod(getOnscreenChatForced)
    
    def setMax2dAlpha(alpha):
        returnValue = libotp._inPPj7bQT8N(alpha)
        return returnValue

    setMax2dAlpha = staticmethod(setMax2dAlpha)
    
    def getMax2dAlpha():
        returnValue = libotp._inPPj7bfARF()
        return returnValue

    getMax2dAlpha = staticmethod(getMax2dAlpha)
    
    def setMin2dAlpha(alpha):
        returnValue = libotp._inPPj7bgSrn(alpha)
        return returnValue

    setMin2dAlpha = staticmethod(setMin2dAlpha)
    
    def getMin2dAlpha():
        returnValue = libotp._inPPj7bPH_e()
        return returnValue

    getMin2dAlpha = staticmethod(getMin2dAlpha)
    
    def setGlobalNametagScale(scale):
        returnValue = libotp._inPPj7bF3w9(scale)
        return returnValue

    setGlobalNametagScale = staticmethod(setGlobalNametagScale)
    
    def getGlobalNametagScale():
        returnValue = libotp._inPPj7bmbpg()
        return returnValue

    getGlobalNametagScale = staticmethod(getGlobalNametagScale)
    
    def getNameFg(colorCode, state):
        returnValue = libotp._inPPj7bZjWd(colorCode, state)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getNameFg = staticmethod(getNameFg)
    
    def getNameBg(colorCode, state):
        returnValue = libotp._inPPj7bZx6a(colorCode, state)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getNameBg = staticmethod(getNameBg)

