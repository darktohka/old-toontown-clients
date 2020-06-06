# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import PandaNode

class PGItem(PandaNode.PandaNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpanda._inPVvimuWRQ(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getEnterPrefix():
        returnValue = libpanda._inPVvimjBNc()
        return returnValue

    getEnterPrefix = staticmethod(getEnterPrefix)
    
    def getExitPrefix():
        returnValue = libpanda._inPVvimKWYV()
        return returnValue

    getExitPrefix = staticmethod(getExitPrefix)
    
    def getWithinPrefix():
        returnValue = libpanda._inPVvimm_4t()
        return returnValue

    getWithinPrefix = staticmethod(getWithinPrefix)
    
    def getWithoutPrefix():
        returnValue = libpanda._inPVvime6SQ()
        return returnValue

    getWithoutPrefix = staticmethod(getWithoutPrefix)
    
    def getFocusInPrefix():
        returnValue = libpanda._inPVvimocSU()
        return returnValue

    getFocusInPrefix = staticmethod(getFocusInPrefix)
    
    def getFocusOutPrefix():
        returnValue = libpanda._inPVvimAosI()
        return returnValue

    getFocusOutPrefix = staticmethod(getFocusOutPrefix)
    
    def getPressPrefix():
        returnValue = libpanda._inPVvimKHW8()
        return returnValue

    getPressPrefix = staticmethod(getPressPrefix)
    
    def getReleasePrefix():
        returnValue = libpanda._inPVvimlGfV()
        return returnValue

    getReleasePrefix = staticmethod(getReleasePrefix)
    
    def getKeystrokePrefix():
        returnValue = libpanda._inPVvimjmbk()
        return returnValue

    getKeystrokePrefix = staticmethod(getKeystrokePrefix)
    
    def getTextNode():
        returnValue = libpanda._inPVvimLv2y()
        import TextNode
        returnObject = TextNode.TextNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    getTextNode = staticmethod(getTextNode)
    
    def setTextNode(node):
        returnValue = libpanda._inPVvimsbIh(node.this)
        return returnValue

    setTextNode = staticmethod(setTextNode)
    
    def getFocusItem():
        returnValue = libpanda._inPVvimYwJY()
        returnObject = PGItem(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    getFocusItem = staticmethod(getFocusItem)
    
    def getClassType():
        returnValue = libpanda._inPVvimHSTl()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _PGItem__overloaded_setFrame_ptrPGItem_ptrConstLVecBase4f(self, frame):
        returnValue = libpanda._inPVvimfDEN(self.this, frame.this)
        return returnValue

    
    def _PGItem__overloaded_setFrame_ptrPGItem_float_float_float_float(self, left, right, bottom, top):
        returnValue = libpanda._inPVvimblkh(self.this, left, right, bottom, top)
        return returnValue

    
    def getFrame(self):
        returnValue = libpanda._inPVvimfpB8(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def hasFrame(self):
        returnValue = libpanda._inPVvimYZs9(self.this)
        return returnValue

    
    def clearFrame(self):
        returnValue = libpanda._inPVvimTDLq(self.this)
        return returnValue

    
    def setState(self, state):
        returnValue = libpanda._inPVvim6vne(self.this, state)
        return returnValue

    
    def getState(self):
        returnValue = libpanda._inPVvim19g7(self.this)
        return returnValue

    
    def setActive(self, active):
        returnValue = libpanda._inPVvimrA9v(self.this, active)
        return returnValue

    
    def getActive(self):
        returnValue = libpanda._inPVvimGMel(self.this)
        return returnValue

    
    def setFocus(self, focus):
        returnValue = libpanda._inPVvimXfx_(self.this, focus)
        return returnValue

    
    def getFocus(self):
        returnValue = libpanda._inPVvimPdFX(self.this)
        return returnValue

    
    def setBackgroundFocus(self, focus):
        returnValue = libpanda._inPVvimz__5(self.this, focus)
        return returnValue

    
    def getBackgroundFocus(self):
        returnValue = libpanda._inPVvim6AEP(self.this)
        return returnValue

    
    def setSuppressFlags(self, suppressFlags):
        returnValue = libpanda._inPVvimQIma(self.this, suppressFlags)
        return returnValue

    
    def getSuppressFlags(self):
        returnValue = libpanda._inPVvimsd1r(self.this)
        return returnValue

    
    def getNumStateDefs(self):
        returnValue = libpanda._inPVvim_Z0S(self.this)
        return returnValue

    
    def clearStateDef(self, state):
        returnValue = libpanda._inPVvimDziL(self.this, state)
        return returnValue

    
    def hasStateDef(self, state):
        returnValue = libpanda._inPVvim526N(self.this, state)
        return returnValue

    
    def getStateDef(self, state):
        returnValue = libpanda._inPVvim_yvN(self.this, state)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def instanceToStateDef(self, state, path):
        returnValue = libpanda._inPVvimQ1k9(self.this, state, path.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getFrameStyle(self, state):
        returnValue = libpanda._inPVvim3KSW(self.this, state)
        import PGFrameStyle
        returnObject = PGFrameStyle.PGFrameStyle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setFrameStyle(self, state, style):
        returnValue = libpanda._inPVvimOzMg(self.this, state, style.this)
        return returnValue

    
    def getId(self):
        returnValue = libpanda._inPVvimVj1_(self.this)
        return returnValue

    
    def setId(self, id):
        returnValue = libpanda._inPVvimDlim(self.this, id)
        return returnValue

    
    def getEnterEvent(self):
        returnValue = libpanda._inPVvimWeD9(self.this)
        return returnValue

    
    def getExitEvent(self):
        returnValue = libpanda._inPVvimt5Yg(self.this)
        return returnValue

    
    def getWithinEvent(self):
        returnValue = libpanda._inPVvimjAdJ(self.this)
        return returnValue

    
    def getWithoutEvent(self):
        returnValue = libpanda._inPVvimXN7D(self.this)
        return returnValue

    
    def getFocusInEvent(self):
        returnValue = libpanda._inPVvim9R_I(self.this)
        return returnValue

    
    def getFocusOutEvent(self):
        returnValue = libpanda._inPVvimdwwe(self.this)
        return returnValue

    
    def getPressEvent(self, button):
        returnValue = libpanda._inPVvimKP2p(self.this, button.this)
        return returnValue

    
    def getReleaseEvent(self, button):
        returnValue = libpanda._inPVvims5_d(self.this, button.this)
        return returnValue

    
    def getKeystrokeEvent(self):
        returnValue = libpanda._inPVvimuXe6(self.this)
        return returnValue

    
    def getFrameInvXform(self):
        returnValue = libpanda._inPVvimRwfE(self.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setSound(self, event, sound):
        returnValue = libpanda._inPVvimnEhS(self.this, event, sound.this)
        return returnValue

    
    def clearSound(self, event):
        returnValue = libpanda._inPVvimNJW1(self.this, event)
        return returnValue

    
    def getSound(self, event):
        returnValue = libpanda._inPVvimhCA4(self.this, event)
        import AudioSound
        returnObject = AudioSound.AudioSound(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def hasSound(self, event):
        returnValue = libpanda._inPVvimsdq5(self.this, event)
        return returnValue

    
    def setFrame(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._PGItem__overloaded_setFrame_ptrPGItem_ptrConstLVecBase4f(*_args)
        elif numArgs == 4:
            return self._PGItem__overloaded_setFrame_ptrPGItem_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 4 '


