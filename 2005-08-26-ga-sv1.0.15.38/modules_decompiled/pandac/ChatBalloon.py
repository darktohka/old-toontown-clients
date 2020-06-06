# File: C (Python 2.2)

import types
import libotp
import libotpDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import ReferenceCount

class ChatBalloon(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libotpDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, rootNode):
        self.this = libotp._inPPj7bjxU9(rootNode.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libotp and libotp._inPPj7b_A4o:
            libotp._inPPj7b_A4o(self.this)
        

    
    def generate(self, text, font, wordwrap, textColor, balloonColor, for3d, hasDrawOrder, drawOrder, pageButton, spaceForButton, reversed, newButton):
        returnValue = libotp._inPPj7bFPvd(self.this, text, font.this, wordwrap, textColor.this, balloonColor.this, for3d, hasDrawOrder, drawOrder, pageButton.this, spaceForButton, reversed, newButton.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()


