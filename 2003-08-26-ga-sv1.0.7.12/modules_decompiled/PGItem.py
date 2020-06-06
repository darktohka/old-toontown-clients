# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import PandaNode

class PGItem(PandaNode.PandaNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self, name):
        self.this = libpanda._inPWvimuWRQ(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getEnterPrefix():
        returnValue = libpanda._inPWvimjBNc()
        return returnValue

    getEnterPrefix = staticmethod(getEnterPrefix)
    
    def getExitPrefix():
        returnValue = libpanda._inPWvimKWYV()
        return returnValue

    getExitPrefix = staticmethod(getExitPrefix)
    
    def getWithinPrefix():
        returnValue = libpanda._inPWviml_4t()
        return returnValue

    getWithinPrefix = staticmethod(getWithinPrefix)
    
    def getWithoutPrefix():
        returnValue = libpanda._inPWvime6SQ()
        return returnValue

    getWithoutPrefix = staticmethod(getWithoutPrefix)
    
    def getFocusInPrefix():
        returnValue = libpanda._inPWvimocSU()
        return returnValue

    getFocusInPrefix = staticmethod(getFocusInPrefix)
    
    def getFocusOutPrefix():
        returnValue = libpanda._inPWvimAosI()
        return returnValue

    getFocusOutPrefix = staticmethod(getFocusOutPrefix)
    
    def getPressPrefix():
        returnValue = libpanda._inPWvimLHW8()
        return returnValue

    getPressPrefix = staticmethod(getPressPrefix)
    
    def getReleasePrefix():
        returnValue = libpanda._inPWvimlGfV()
        return returnValue

    getReleasePrefix = staticmethod(getReleasePrefix)
    
    def getKeystrokePrefix():
        returnValue = libpanda._inPWvimcmbk()
        return returnValue

    getKeystrokePrefix = staticmethod(getKeystrokePrefix)
    
    def getTextNode():
        returnValue = libpanda._inPWvimKv2y()
        import TextNode
        returnObject = TextNode.TextNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    getTextNode = staticmethod(getTextNode)
    
    def setTextNode(node):
        returnValue = libpanda._inPWvimtbIh(node.this)
        return returnValue

    setTextNode = staticmethod(setTextNode)
    
    def getFocusItem():
        returnValue = libpanda._inPWvimYwJY()
        returnObject = PGItem(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    getFocusItem = staticmethod(getFocusItem)
    
    def getClassType():
        returnValue = libpanda._inPWvimESTl()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _PGItem__overloaded_setFrame_ptrPGItem_ptrConstLVecBase4f(self, frame):
        returnValue = libpanda._inPWvimfDEN(self.this, frame.this)
        return returnValue

    
    def _PGItem__overloaded_setFrame_ptrPGItem_float_float_float_float(self, left, right, bottom, top):
        returnValue = libpanda._inPWvimYlkh(self.this, left, right, bottom, top)
        return returnValue

    
    def getFrame(self):
        returnValue = libpanda._inPWvimepB8(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def hasFrame(self):
        returnValue = libpanda._inPWvimbZs9(self.this)
        return returnValue

    
    def clearFrame(self):
        returnValue = libpanda._inPWvimSDLq(self.this)
        return returnValue

    
    def setState(self, state):
        returnValue = libpanda._inPWvim6vne(self.this, state)
        return returnValue

    
    def getState(self):
        returnValue = libpanda._inPWvim09g7(self.this)
        return returnValue

    
    def setActive(self, active):
        returnValue = libpanda._inPWvimqA9v(self.this, active)
        return returnValue

    
    def getActive(self):
        returnValue = libpanda._inPWvimBMel(self.this)
        return returnValue

    
    def setFocus(self, focus):
        returnValue = libpanda._inPWvimQfx_(self.this, focus)
        return returnValue

    
    def getFocus(self):
        returnValue = libpanda._inPWvimPdFX(self.this)
        return returnValue

    
    def setBackgroundFocus(self, focus):
        returnValue = libpanda._inPWvimM9_5(self.this, focus)
        return returnValue

    
    def getBackgroundFocus(self):
        returnValue = libpanda._inPWvim6AEP(self.this)
        return returnValue

    
    def setSuppressFlags(self, suppressFlags):
        returnValue = libpanda._inPWvimQIma(self.this, suppressFlags)
        return returnValue

    
    def getSuppressFlags(self):
        returnValue = libpanda._inPWvimtd1r(self.this)
        return returnValue

    
    def getNumStateDefs(self):
        returnValue = libpanda._inPWvim_Z0S(self.this)
        return returnValue

    
    def clearStateDef(self, state):
        returnValue = libpanda._inPWvimDziL(self.this, state)
        return returnValue

    
    def hasStateDef(self, state):
        returnValue = libpanda._inPWvim526N(self.this, state)
        return returnValue

    
    def getStateDef(self, state):
        returnValue = libpanda._inPWvim_yvN(self.this, state)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def instanceToStateDef(self, state, path):
        returnValue = libpanda._inPWvimR1k9(self.this, state, path.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getFrameStyle(self, state):
        returnValue = libpanda._inPWvim3KSW(self.this, state)
        import PGFrameStyle
        returnObject = PGFrameStyle.PGFrameStyle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setFrameStyle(self, state, style):
        returnValue = libpanda._inPWvimNzMg(self.this, state, style.this)
        return returnValue

    
    def getId(self):
        returnValue = libpanda._inPWvimqj1_(self.this)
        return returnValue

    
    def setId(self, id):
        returnValue = libpanda._inPWvimElim(self.this, id)
        return returnValue

    
    def getEnterEvent(self):
        returnValue = libpanda._inPWvimReD9(self.this)
        return returnValue

    
    def getExitEvent(self):
        returnValue = libpanda._inPWvims5Yg(self.this)
        return returnValue

    
    def getWithinEvent(self):
        returnValue = libpanda._inPWvimjAdJ(self.this)
        return returnValue

    
    def getWithoutEvent(self):
        returnValue = libpanda._inPWvimXN7D(self.this)
        return returnValue

    
    def getFocusInEvent(self):
        returnValue = libpanda._inPWvim9R_I(self.this)
        return returnValue

    
    def getFocusOutEvent(self):
        returnValue = libpanda._inPWvimdwwe(self.this)
        return returnValue

    
    def getPressEvent(self, button):
        returnValue = libpanda._inPWvimFP2p(self.this, button.this)
        return returnValue

    
    def getReleaseEvent(self, button):
        returnValue = libpanda._inPWvims5_d(self.this, button.this)
        return returnValue

    
    def getKeystrokeEvent(self):
        returnValue = libpanda._inPWvimvXe6(self.this)
        return returnValue

    
    def setSound(self, event, sound):
        returnValue = libpanda._inPWvimnEhS(self.this, event, sound.this)
        return returnValue

    
    def clearSound(self, event):
        returnValue = libpanda._inPWvimMJW1(self.this, event)
        return returnValue

    
    def getSound(self, event):
        returnValue = libpanda._inPWvimiCA4(self.this, event)
        import AudioSound
        returnObject = AudioSound.AudioSound(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def hasSound(self, event):
        returnValue = libpanda._inPWvimtdq5(self.this, event)
        return returnValue

    
    def setFrame(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase4
            if isinstance(_args[0], VBase4.VBase4):
                return self._PGItem__overloaded_setFrame_ptrPGItem_ptrConstLVecBase4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
        elif numArgs == 4:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._PGItem__overloaded_setFrame_ptrPGItem_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 4 '


