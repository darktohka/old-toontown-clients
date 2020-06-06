# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedWritableReferenceCount
import MouseWatcherParameter

class PGMouseWatcherParameter(TypedWritableReferenceCount.TypedWritableReferenceCount, MouseWatcherParameter.MouseWatcherParameter, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
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
        if libpanda and libpanda._inPVvimm_5X:
            libpanda._inPVvimm_5X(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPVvim63gq()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def output(self, out):
        returnValue = libpanda._inPVvimY5i_(self.this, out.this)
        return returnValue

    
    def upcastToMouseWatcherParameter(self):
        returnValue = libpanda._inPVvimjvJV(self.this)
        import MouseWatcherParameter
        returnObject = MouseWatcherParameter.MouseWatcherParameter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToReferenceCount(self):
        upcastSelf = self
        returnValue = libpanda._inPflbokcf_(upcastSelf.this)
        import ReferenceCount
        returnObject = ReferenceCount.ReferenceCount(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getType(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxt1uxI(upcastSelf.this)
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getTypeIndex(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxtm7AU(upcastSelf.this)
        return returnValue

    
    def isOfType(self, handle):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxtnFKt(upcastSelf.this, handle.this)
        return returnValue

    
    def isExactType(self, handle):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxt7Xzz(upcastSelf.this, handle.this)
        return returnValue

    
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

    
    def hasButton(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
        returnValue = libpanda._inPyiw5HdBJ(upcastSelf.this)
        return returnValue

    
    def getButton(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
        returnValue = libpanda._inPyiw5Wbt7(upcastSelf.this)
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
        returnValue = libpanda._inPyiw5jsPh(upcastSelf.this)
        return returnValue

    
    def getKeycode(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
        returnValue = libpanda._inPyiw5Lr7T(upcastSelf.this)
        return returnValue

    
    def hasCandidate(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
        returnValue = libpanda._inPyiw5m3E2(upcastSelf.this)
        return returnValue

    
    def _PGMouseWatcherParameter__overloaded_getCandidateStringEncoded_ptrConstMouseWatcherParameter(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
        returnValue = libpanda._inPyiw5JON1(upcastSelf.this)
        return returnValue

    
    def _PGMouseWatcherParameter__overloaded_getCandidateStringEncoded_ptrConstMouseWatcherParameter___enum__Encoding(self, encoding):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
        returnValue = libpanda._inPyiw5ggbz(upcastSelf.this, encoding)
        return returnValue

    
    def getHighlightStart(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
        returnValue = libpanda._inPyiw52Qq_(upcastSelf.this)
        return returnValue

    
    def getHighlightEnd(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
        returnValue = libpanda._inPyiw5wcQ5(upcastSelf.this)
        return returnValue

    
    def getCursorPos(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
        returnValue = libpanda._inPyiw55fsc(upcastSelf.this)
        return returnValue

    
    def getModifierButtons(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
        returnValue = libpanda._inPyiw5D2au(upcastSelf.this)
        import ModifierButtons
        returnObject = ModifierButtons.ModifierButtons(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def hasMouse(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
        returnValue = libpanda._inPyiw53Y9y(upcastSelf.this)
        return returnValue

    
    def getMouse(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
        returnValue = libpanda._inPyiw5nFpl(upcastSelf.this)
        import Point2
        returnObject = Point2.Point2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def isOutside(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
        returnValue = libpanda._inPyiw5CuZd(upcastSelf.this)
        return returnValue

    
    def getCandidateStringEncoded(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PGMouseWatcherParameter__overloaded_getCandidateStringEncoded_ptrConstMouseWatcherParameter(*_args)
        elif numArgs == 1:
            return self._PGMouseWatcherParameter__overloaded_getCandidateStringEncoded_ptrConstMouseWatcherParameter___enum__Encoding(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


