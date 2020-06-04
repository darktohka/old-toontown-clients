# File: N (Python 2.2)

import types
import libotp
import libotpDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import ReferenceCount
import ClickablePopup

class Nametag(ReferenceCount.ReferenceCount, ClickablePopup.ClickablePopup, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libotpDowncasts,
        libpandaexpressDowncasts]
    CThought = 4
    CName = 1
    CSpeech = 2
    
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
        if libotp and libotp._inPPj7bRtH6:
            libotp._inPPj7bRtH6(self.this)
        

    
    def getClassType():
        returnValue = libotp._inPPj7byGKv()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setContents(self, flags):
        returnValue = libotp._inPPj7bLEaT(self.this, flags)
        return returnValue

    
    def getContents(self):
        returnValue = libotp._inPPj7bJEgG(self.this)
        return returnValue

    
    def setActive(self, active):
        returnValue = libotp._inPPj7bSryD(self.this, active)
        return returnValue

    
    def isActive(self):
        returnValue = libotp._inPPj7boM1i(self.this)
        return returnValue

    
    def displayAsActive(self):
        returnValue = libotp._inPPj7bKRcp(self.this)
        return returnValue

    
    def hasGroup(self):
        returnValue = libotp._inPPj7bTIee(self.this)
        return returnValue

    
    def getGroup(self):
        returnValue = libotp._inPPj7bbjNp(self.this)
        import NametagGroup
        returnObject = NametagGroup.NametagGroup(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setDrawOrder(self, drawOrder):
        returnValue = libotp._inPPj7bhTHf(self.this, drawOrder)
        return returnValue

    
    def clearDrawOrder(self):
        returnValue = libotp._inPPj7bGzp7(self.this)
        return returnValue

    
    def setChatWordwrap(self, wordwrap):
        returnValue = libotp._inPPj7bC_0k(self.this, wordwrap)
        return returnValue

    
    def getChatWordwrap(self):
        returnValue = libotp._inPPj7bidZX(self.this)
        return returnValue

    
    def setAvatar(self, node):
        returnValue = libotp._inPPj7bcwUo(self.this, node.this)
        return returnValue

    
    def clearAvatar(self):
        returnValue = libotp._inPPj7blVEl(self.this)
        return returnValue

    
    def getAvatar(self):
        returnValue = libotp._inPPj7bA2vB(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getType(self):
        returnValue = libotp._inPPj7bRdXg(self.this)
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def upcastToReferenceCount(self):
        returnValue = libotp._inPPj7bkgq5(self.this)
        import ReferenceCount
        returnObject = ReferenceCount.ReferenceCount(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToClickablePopup(self):
        returnValue = libotp._inPPj7btut_(self.this)
        import ClickablePopup
        returnObject = ClickablePopup.ClickablePopup(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getRefCount(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtP11_(upcastSelf.this)
        return returnValue

    
    def ref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtaS5_(upcastSelf.this)
        return returnValue

    
    def unref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtwyVy(upcastSelf.this)
        return returnValue

    
    def testRefCountIntegrity(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtvpj2(upcastSelf.this)
        return returnValue


