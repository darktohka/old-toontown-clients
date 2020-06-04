# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import PGItem

class PGEntry(PGItem.PGItem, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    SFocus = 0
    SInactive = 2
    SNoFocus = 1
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self, name):
        self.this = libpanda._inPWvimoxCL(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getAcceptPrefix():
        returnValue = libpanda._inPWvimQNBk()
        return returnValue

    getAcceptPrefix = staticmethod(getAcceptPrefix)
    
    def getOverflowPrefix():
        returnValue = libpanda._inPWvimOCNR()
        return returnValue

    getOverflowPrefix = staticmethod(getOverflowPrefix)
    
    def getTypePrefix():
        returnValue = libpanda._inPWvimMQ4_()
        return returnValue

    getTypePrefix = staticmethod(getTypePrefix)
    
    def getErasePrefix():
        returnValue = libpanda._inPWvimG7IQ()
        return returnValue

    getErasePrefix = staticmethod(getErasePrefix)
    
    def getClassType():
        returnValue = libpanda._inPWvimNhug()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setup(self, width, numLines):
        returnValue = libpanda._inPWvimiwtL(self.this, width, numLines)
        return returnValue

    
    def setText(self, text):
        returnValue = libpanda._inPWvimDMDl(self.this, text)
        return returnValue

    
    def getText(self):
        returnValue = libpanda._inPWvim_QSc(self.this)
        return returnValue

    
    def setCursorPosition(self, position):
        returnValue = libpanda._inPWvimksp8(self.this, position)
        return returnValue

    
    def getCursorPosition(self):
        returnValue = libpanda._inPWvim1AtR(self.this)
        return returnValue

    
    def setMaxChars(self, maxChars):
        returnValue = libpanda._inPWvimmPHw(self.this, maxChars)
        return returnValue

    
    def getMaxChars(self):
        returnValue = libpanda._inPWvim4r6z(self.this)
        return returnValue

    
    def setMaxWidth(self, maxWidth):
        returnValue = libpanda._inPWvimKWva(self.this, maxWidth)
        return returnValue

    
    def getMaxWidth(self):
        returnValue = libpanda._inPWvimUxhk(self.this)
        return returnValue

    
    def setNumLines(self, numLines):
        returnValue = libpanda._inPWvimTDLT(self.this, numLines)
        return returnValue

    
    def getNumLines(self):
        returnValue = libpanda._inPWvimzX9W(self.this)
        return returnValue

    
    def setBlinkRate(self, blinkRate):
        returnValue = libpanda._inPWvimnROV(self.this, blinkRate)
        return returnValue

    
    def getBlinkRate(self):
        returnValue = libpanda._inPWvimLf8v(self.this)
        return returnValue

    
    def getCursorDef(self):
        returnValue = libpanda._inPWvimlf6N(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def clearCursorDef(self):
        returnValue = libpanda._inPWvimLvwG(self.this)
        return returnValue

    
    def setCursorKeysActive(self, flag):
        returnValue = libpanda._inPWvimkpvF(self.this, flag)
        return returnValue

    
    def getCursorKeysActive(self):
        returnValue = libpanda._inPWvimWRyA(self.this)
        return returnValue

    
    def setObscureMode(self, flag):
        returnValue = libpanda._inPWvimQRdS(self.this, flag)
        return returnValue

    
    def getObscureMode(self):
        returnValue = libpanda._inPWvimCY2e(self.this)
        return returnValue

    
    def setTextDef(self, state, node):
        returnValue = libpanda._inPWvimMxrH(self.this, state, node.this)
        return returnValue

    
    def getTextDef(self, state):
        returnValue = libpanda._inPWvimHmBt(self.this, state)
        import TextNode
        returnObject = TextNode.TextNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getAcceptEvent(self, button):
        returnValue = libpanda._inPWvimPkhs(self.this, button.this)
        return returnValue

    
    def getOverflowEvent(self):
        returnValue = libpanda._inPWvimCqQn(self.this)
        return returnValue

    
    def getTypeEvent(self):
        returnValue = libpanda._inPWvimEeug(self.this)
        return returnValue

    
    def getEraseEvent(self):
        returnValue = libpanda._inPWvimLEsr(self.this)
        return returnValue


