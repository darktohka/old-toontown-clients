# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TypedReferenceCount
import MouseWatcherParameter

class PGMouseWatcherParameter(TypedReferenceCount.TypedReferenceCount, MouseWatcherParameter.MouseWatcherParameter, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
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
        if libpanda and libpanda._inPWvimm_5X:
            libpanda._inPWvimm_5X(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPWvim93gq()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def output(self, out):
        returnValue = libpanda._inPWvimb5i_(self.this, out.this)
        return returnValue

    
    def upcastToMouseWatcherParameter(self):
        returnValue = libpanda._inPWvimjvJV(self.this)
        import MouseWatcherParameter
        returnObject = MouseWatcherParameter.MouseWatcherParameter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToReferenceCount(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPJoxtKE8f(upcastSelf.this)
        import ReferenceCount
        returnObject = ReferenceCount.ReferenceCount(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getType(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPJoxt1uxI(upcastSelf.this)
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getTypeIndex(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPJoxtm7AU(upcastSelf.this)
        return returnValue

    
    def isOfType(self, handle):
        upcastSelf = self
        returnValue = libpandaexpress._inPJoxtmFKt(upcastSelf.this, handle.this)
        return returnValue

    
    def isExactType(self, handle):
        upcastSelf = self
        returnValue = libpandaexpress._inPJoxtkXzz(upcastSelf.this, handle.this)
        return returnValue

    
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

    
    def hasButton(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
        returnValue = libpanda._inPziw5HdBJ(upcastSelf.this)
        return returnValue

    
    def getButton(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
        returnValue = libpanda._inPziw5Xbt7(upcastSelf.this)
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def hasKeycode(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
        returnValue = libpanda._inPziw5ssPh(upcastSelf.this)
        return returnValue

    
    def getKeycode(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
        returnValue = libpanda._inPziw5Lr7T(upcastSelf.this)
        return returnValue

    
    def getModifierButtons(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
        returnValue = libpanda._inPziw5A2au(upcastSelf.this)
        import ModifierButtons
        returnObject = ModifierButtons.ModifierButtons(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def hasMouse(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
        returnValue = libpanda._inPziw50Y9y(upcastSelf.this)
        return returnValue

    
    def getMouse(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
        returnValue = libpanda._inPziw5kFpl(upcastSelf.this)
        import Point2
        returnObject = Point2.Point2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def isOutside(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
        returnValue = libpanda._inPziw5CuZd(upcastSelf.this)
        return returnValue


