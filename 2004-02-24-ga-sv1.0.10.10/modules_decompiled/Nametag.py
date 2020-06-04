# File: N (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ReferenceCount
import ClickablePopup

class Nametag(ReferenceCount.ReferenceCount, ClickablePopup.ClickablePopup, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    CThought = 4
    CName = 1
    CSpeech = 2
    
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
        if libtoontown and libtoontown._inPPj7bQtH6:
            libtoontown._inPPj7bQtH6(self.this)
        

    
    def getClassType():
        returnValue = libtoontown._inPPj7b1GKv()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setContents(self, flags):
        returnValue = libtoontown._inPPj7bLEaT(self.this, flags)
        return returnValue

    
    def getContents(self):
        returnValue = libtoontown._inPPj7bJEgG(self.this)
        return returnValue

    
    def setActive(self, active):
        returnValue = libtoontown._inPPj7bSryD(self.this, active)
        return returnValue

    
    def isActive(self):
        returnValue = libtoontown._inPPj7brM1i(self.this)
        return returnValue

    
    def displayAsActive(self):
        returnValue = libtoontown._inPPj7bLRcp(self.this)
        return returnValue

    
    def hasGroup(self):
        returnValue = libtoontown._inPPj7bTIee(self.this)
        return returnValue

    
    def getGroup(self):
        returnValue = libtoontown._inPPj7bajNp(self.this)
        import NametagGroup
        returnObject = NametagGroup.NametagGroup(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setDrawOrder(self, drawOrder):
        returnValue = libtoontown._inPPj7bhTHf(self.this, drawOrder)
        return returnValue

    
    def clearDrawOrder(self):
        returnValue = libtoontown._inPPj7b5yp7(self.this)
        return returnValue

    
    def setChatWordwrap(self, wordwrap):
        returnValue = libtoontown._inPPj7b980k(self.this, wordwrap)
        return returnValue

    
    def getChatWordwrap(self):
        returnValue = libtoontown._inPPj7bidZX(self.this)
        return returnValue

    
    def setAvatar(self, node):
        returnValue = libtoontown._inPPj7bdwUo(self.this, node.this)
        return returnValue

    
    def clearAvatar(self):
        returnValue = libtoontown._inPPj7bkVEl(self.this)
        return returnValue

    
    def getAvatar(self):
        returnValue = libtoontown._inPPj7bA2vB(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getType(self):
        returnValue = libtoontown._inPPj7bSdXg(self.this)
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def upcastToReferenceCount(self):
        returnValue = libtoontown._inPPj7bngq5(self.this)
        import ReferenceCount
        returnObject = ReferenceCount.ReferenceCount(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToClickablePopup(self):
        returnValue = libtoontown._inPPj7buut_(self.this)
        import ClickablePopup
        returnObject = ClickablePopup.ClickablePopup(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getRefCount(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtM11_(upcastSelf.this)
        return returnValue

    
    def ref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtVS5_(upcastSelf.this)
        return returnValue

    
    def unref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtzyVy(upcastSelf.this)
        return returnValue

    
    def testRefCountIntegrity(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtupj2(upcastSelf.this)
        return returnValue


