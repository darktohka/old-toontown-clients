# File: N (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import FFIExternalObject

class NametagGlobals(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts]
    
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
        if libtoontown and libtoontown._inPPj7bUBF8:
            libtoontown._inPPj7bUBF8(self.this)
        

    
    def getNameWordwrap():
        returnValue = libtoontown._inPPj7bm9Im()
        return returnValue

    getNameWordwrap = staticmethod(getNameWordwrap)
    
    def getCardPad():
        returnValue = libtoontown._inPPj7bRaV7()
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getCardPad = staticmethod(getCardPad)
    
    def setCamera(node):
        returnValue = libtoontown._inPPj7bteog(node.this)
        return returnValue

    setCamera = staticmethod(setCamera)
    
    def getCamera():
        returnValue = libtoontown._inPPj7beEEo()
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getCamera = staticmethod(getCamera)
    
    def setToon(node):
        returnValue = libtoontown._inPPj7bMhdm(node.this)
        return returnValue

    setToon = staticmethod(setToon)
    
    def getToon():
        returnValue = libtoontown._inPPj7bu_Rg()
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getToon = staticmethod(getToon)
    
    def setArrowModel(node):
        returnValue = libtoontown._inPPj7bB2bD(node.this)
        return returnValue

    setArrowModel = staticmethod(setArrowModel)
    
    def getArrowModel():
        returnValue = libtoontown._inPPj7bet3M()
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getArrowModel = staticmethod(getArrowModel)
    
    def setPageButton(state, node):
        returnValue = libtoontown._inPPj7bSPiB(state, node.this)
        return returnValue

    setPageButton = staticmethod(setPageButton)
    
    def getPageButton(state):
        returnValue = libtoontown._inPPj7bHqo0(state)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getPageButton = staticmethod(getPageButton)
    
    def setQuitButton(state, node):
        returnValue = libtoontown._inPPj7buW_H(state, node.this)
        return returnValue

    setQuitButton = staticmethod(setQuitButton)
    
    def getQuitButton(state):
        returnValue = libtoontown._inPPj7bLDE7(state)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getQuitButton = staticmethod(getQuitButton)
    
    def setNametagCard(node, frame):
        returnValue = libtoontown._inPPj7bO7HT(node.this, frame.this)
        return returnValue

    setNametagCard = staticmethod(setNametagCard)
    
    def getNametagCard():
        returnValue = libtoontown._inPPj7bbqdr()
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getNametagCard = staticmethod(getNametagCard)
    
    def getNametagCardFrame():
        returnValue = libtoontown._inPPj7bq0Kj()
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getNametagCardFrame = staticmethod(getNametagCardFrame)
    
    def setRolloverSound(sound):
        returnValue = libtoontown._inPPj7br4M4(sound.this)
        return returnValue

    setRolloverSound = staticmethod(setRolloverSound)
    
    def getRolloverSound():
        returnValue = libtoontown._inPPj7bE66T()
        import AudioSound
        returnObject = AudioSound.AudioSound(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getRolloverSound = staticmethod(getRolloverSound)
    
    def setClickSound(sound):
        returnValue = libtoontown._inPPj7baRDq(sound.this)
        return returnValue

    setClickSound = staticmethod(setClickSound)
    
    def getClickSound():
        returnValue = libtoontown._inPPj7bQsf2()
        import AudioSound
        returnObject = AudioSound.AudioSound(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClickSound = staticmethod(getClickSound)
    
    def setMouseWatcher(watcher):
        returnValue = libtoontown._inPPj7bPlgS(watcher.this)
        return returnValue

    setMouseWatcher = staticmethod(setMouseWatcher)
    
    def getMouseWatcher():
        returnValue = libtoontown._inPPj7bjGmX()
        import MouseWatcher
        returnObject = MouseWatcher.MouseWatcher(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    getMouseWatcher = staticmethod(getMouseWatcher)
    
    def setSpeechBalloon2d(balloon):
        returnValue = libtoontown._inPPj7buc69(balloon.this)
        return returnValue

    setSpeechBalloon2d = staticmethod(setSpeechBalloon2d)
    
    def getSpeechBalloon2d():
        returnValue = libtoontown._inPPj7bD_yZ()
        import ChatBalloon
        returnObject = ChatBalloon.ChatBalloon(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getSpeechBalloon2d = staticmethod(getSpeechBalloon2d)
    
    def setThoughtBalloon2d(balloon):
        returnValue = libtoontown._inPPj7b2ehI(balloon.this)
        return returnValue

    setThoughtBalloon2d = staticmethod(setThoughtBalloon2d)
    
    def getThoughtBalloon2d():
        returnValue = libtoontown._inPPj7bezGc()
        import ChatBalloon
        returnObject = ChatBalloon.ChatBalloon(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getThoughtBalloon2d = staticmethod(getThoughtBalloon2d)
    
    def setSpeechBalloon3d(balloon):
        returnValue = libtoontown._inPPj7buuXA(balloon.this)
        return returnValue

    setSpeechBalloon3d = staticmethod(setSpeechBalloon3d)
    
    def getSpeechBalloon3d():
        returnValue = libtoontown._inPPj7bDJRc()
        import ChatBalloon
        returnObject = ChatBalloon.ChatBalloon(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getSpeechBalloon3d = staticmethod(getSpeechBalloon3d)
    
    def setThoughtBalloon3d(balloon):
        returnValue = libtoontown._inPPj7b1emW(balloon.this)
        return returnValue

    setThoughtBalloon3d = staticmethod(setThoughtBalloon3d)
    
    def getThoughtBalloon3d():
        returnValue = libtoontown._inPPj7bYzNq()
        import ChatBalloon
        returnObject = ChatBalloon.ChatBalloon(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getThoughtBalloon3d = staticmethod(getThoughtBalloon3d)
    
    def setMasterNametagsActive(active):
        returnValue = libtoontown._inPPj7b_2Ct(active)
        return returnValue

    setMasterNametagsActive = staticmethod(setMasterNametagsActive)
    
    def getMasterNametagsActive():
        returnValue = libtoontown._inPPj7b5f_m()
        return returnValue

    getMasterNametagsActive = staticmethod(getMasterNametagsActive)
    
    def setMasterArrowsOn(active):
        returnValue = libtoontown._inPPj7bXMYq(active)
        return returnValue

    setMasterArrowsOn = staticmethod(setMasterArrowsOn)
    
    def getMasterArrowsOn():
        returnValue = libtoontown._inPPj7bkJpy()
        return returnValue

    getMasterArrowsOn = staticmethod(getMasterArrowsOn)
    
    def setOnscreenChatForced(active):
        returnValue = libtoontown._inPPj7bocod(active)
        return returnValue

    setOnscreenChatForced = staticmethod(setOnscreenChatForced)
    
    def getOnscreenChatForced():
        returnValue = libtoontown._inPPj7beOQ_()
        return returnValue

    getOnscreenChatForced = staticmethod(getOnscreenChatForced)
    
    def setMax2dAlpha(alpha):
        returnValue = libtoontown._inPPj7bQT8N(alpha)
        return returnValue

    setMax2dAlpha = staticmethod(setMax2dAlpha)
    
    def getMax2dAlpha():
        returnValue = libtoontown._inPPj7bfARF()
        return returnValue

    getMax2dAlpha = staticmethod(getMax2dAlpha)
    
    def setMin2dAlpha(alpha):
        returnValue = libtoontown._inPPj7bhSrn(alpha)
        return returnValue

    setMin2dAlpha = staticmethod(setMin2dAlpha)
    
    def getMin2dAlpha():
        returnValue = libtoontown._inPPj7bPH_e()
        return returnValue

    getMin2dAlpha = staticmethod(getMin2dAlpha)
    
    def setGlobalNametagScale(scale):
        returnValue = libtoontown._inPPj7bE3w9(scale)
        return returnValue

    setGlobalNametagScale = staticmethod(setGlobalNametagScale)
    
    def getGlobalNametagScale():
        returnValue = libtoontown._inPPj7blbpg()
        return returnValue

    getGlobalNametagScale = staticmethod(getGlobalNametagScale)
    
    def getNameFg(colorCode, state):
        returnValue = libtoontown._inPPj7bZjWd(colorCode, state)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getNameFg = staticmethod(getNameFg)
    
    def getNameBg(colorCode, state):
        returnValue = libtoontown._inPPj7bZx6a(colorCode, state)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getNameBg = staticmethod(getNameBg)

