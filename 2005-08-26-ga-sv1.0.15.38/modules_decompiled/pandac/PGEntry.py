# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
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
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpanda._inPVvimoxCL(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getAcceptPrefix():
        returnValue = libpanda._inPVvimRNBk()
        return returnValue

    getAcceptPrefix = staticmethod(getAcceptPrefix)
    
    def getOverflowPrefix():
        returnValue = libpanda._inPVvimOCNR()
        return returnValue

    getOverflowPrefix = staticmethod(getOverflowPrefix)
    
    def getTypePrefix():
        returnValue = libpanda._inPVvimPQ4_()
        return returnValue

    getTypePrefix = staticmethod(getTypePrefix)
    
    def getErasePrefix():
        returnValue = libpanda._inPVvimG7IQ()
        return returnValue

    getErasePrefix = staticmethod(getErasePrefix)
    
    def getClassType():
        returnValue = libpanda._inPVvimChug()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setup(self, width, numLines):
        returnValue = libpanda._inPVvimiwtL(self.this, width, numLines)
        return returnValue

    
    def setText(self, text):
        returnValue = libpanda._inPVvimAMDl(self.this, text)
        return returnValue

    
    def getText(self):
        returnValue = libpanda._inPVvim_QSc(self.this)
        return returnValue

    
    def setCursorPosition(self, position):
        returnValue = libpanda._inPVvimlsp8(self.this, position)
        return returnValue

    
    def getCursorPosition(self):
        returnValue = libpanda._inPVvim1AtR(self.this)
        return returnValue

    
    def setMaxChars(self, maxChars):
        returnValue = libpanda._inPVvimnPHw(self.this, maxChars)
        return returnValue

    
    def getMaxChars(self):
        returnValue = libpanda._inPVvim_r6z(self.this)
        return returnValue

    
    def setMaxWidth(self, maxWidth):
        returnValue = libpanda._inPVvimKWva(self.this, maxWidth)
        return returnValue

    
    def getMaxWidth(self):
        returnValue = libpanda._inPVvimXxhk(self.this)
        return returnValue

    
    def setNumLines(self, numLines):
        returnValue = libpanda._inPVvimTDLT(self.this, numLines)
        return returnValue

    
    def getNumLines(self):
        returnValue = libpanda._inPVvimzX9W(self.this)
        return returnValue

    
    def setBlinkRate(self, blinkRate):
        returnValue = libpanda._inPVvimnROV(self.this, blinkRate)
        return returnValue

    
    def getBlinkRate(self):
        returnValue = libpanda._inPVvimKf8v(self.this)
        return returnValue

    
    def getCursorDef(self):
        returnValue = libpanda._inPVvimlf6N(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def clearCursorDef(self):
        returnValue = libpanda._inPVvimLvwG(self.this)
        return returnValue

    
    def setCursorKeysActive(self, flag):
        returnValue = libpanda._inPVvimkpvF(self.this, flag)
        return returnValue

    
    def getCursorKeysActive(self):
        returnValue = libpanda._inPVvimWRyA(self.this)
        return returnValue

    
    def setObscureMode(self, flag):
        returnValue = libpanda._inPVvimQRdS(self.this, flag)
        return returnValue

    
    def getObscureMode(self):
        returnValue = libpanda._inPVvimCY2e(self.this)
        return returnValue

    
    def setCandidateActive(self, candidateActive):
        returnValue = libpanda._inPVvimuuvU(self.this, candidateActive)
        return returnValue

    
    def getCandidateActive(self):
        returnValue = libpanda._inPVvimfCwe(self.this)
        return returnValue

    
    def setCandidateInactive(self, candidateInactive):
        returnValue = libpanda._inPVvimwfZx(self.this, candidateInactive)
        return returnValue

    
    def getCandidateInactive(self):
        returnValue = libpanda._inPVvimmgOn(self.this)
        return returnValue

    
    def setTextDef(self, state, node):
        returnValue = libpanda._inPVvimMxrH(self.this, state, node.this)
        return returnValue

    
    def getTextDef(self, state):
        returnValue = libpanda._inPVvimGmBt(self.this, state)
        import TextNode
        returnObject = TextNode.TextNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getAcceptEvent(self, button):
        returnValue = libpanda._inPVvimwkhs(self.this, button.this)
        return returnValue

    
    def getOverflowEvent(self):
        returnValue = libpanda._inPVvimBqQn(self.this)
        return returnValue

    
    def getTypeEvent(self):
        returnValue = libpanda._inPVvimFeug(self.this)
        return returnValue

    
    def getEraseEvent(self):
        returnValue = libpanda._inPVvimIEsr(self.this)
        return returnValue


