# File: M (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedWritableReferenceCount
import Namable

class MouseWatcherRegion(TypedWritableReferenceCount.TypedWritableReferenceCount, Namable.Namable, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    SFAnyButton = 3
    SFMousePosition = 4
    SFMouseButton = 1
    SFOtherButton = 2
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _MouseWatcherRegion__overloaded_constructor_atomicstring_ptrConstLVecBase4f(self, name, frame):
        self.this = libpanda._inPyiw5XN0b(name, frame.this)
        self.userManagesMemory = 1

    
    def _MouseWatcherRegion__overloaded_constructor_atomicstring_float_float_float_float(self, name, left, right, bottom, top):
        self.this = libpanda._inPyiw5VKEG(name, left, right, bottom, top)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPyiw5gc_U:
            libpanda._inPyiw5gc_U(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPyiw5et1g()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _MouseWatcherRegion__overloaded_setFrame_ptrMouseWatcherRegion_ptrConstLVecBase4f(self, frame):
        returnValue = libpanda._inPyiw5vRlo(self.this, frame.this)
        return returnValue

    
    def _MouseWatcherRegion__overloaded_setFrame_ptrMouseWatcherRegion_float_float_float_float(self, left, right, bottom, top):
        returnValue = libpanda._inPyiw5TI04(self.this, left, right, bottom, top)
        return returnValue

    
    def getFrame(self):
        returnValue = libpanda._inPyiw5C2td(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getArea(self):
        returnValue = libpanda._inPyiw5xwAe(self.this)
        return returnValue

    
    def setSort(self, sort):
        returnValue = libpanda._inPyiw5uUjJ(self.this, sort)
        return returnValue

    
    def getSort(self):
        returnValue = libpanda._inPyiw5wQ_6(self.this)
        return returnValue

    
    def setActive(self, active):
        returnValue = libpanda._inPyiw5H96x(self.this, active)
        return returnValue

    
    def getActive(self):
        returnValue = libpanda._inPyiw5BoGH(self.this)
        return returnValue

    
    def setKeyboard(self, keyboard):
        returnValue = libpanda._inPyiw5_wOd(self.this, keyboard)
        return returnValue

    
    def getKeyboard(self):
        returnValue = libpanda._inPyiw52JK8(self.this)
        return returnValue

    
    def setSuppressFlags(self, suppressFlags):
        returnValue = libpanda._inPyiw5TWvO(self.this, suppressFlags)
        return returnValue

    
    def getSuppressFlags(self):
        returnValue = libpanda._inPyiw5yKjf(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPyiw5kvVL(self.this, out.this)
        return returnValue

    
    def _MouseWatcherRegion__overloaded_write_ptrConstMouseWatcherRegion_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPyiw5ijOS(self.this, out.this, indentLevel)
        return returnValue

    
    def _MouseWatcherRegion__overloaded_write_ptrConstMouseWatcherRegion_ptrOstream(self, out):
        returnValue = libpanda._inPyiw51qaj(self.this, out.this)
        return returnValue

    
    def upcastToNamable(self):
        returnValue = libpanda._inPyiw5uEXk(self.this)
        import Namable
        returnObject = Namable.Namable(None)
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

    
    def assign(self, other):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtp1bI(upcastSelf.this, other.this)
        import Namable
        returnObject = Namable.Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setName(self, name):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtLNBW(upcastSelf.this, name)
        return returnValue

    
    def clearName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtZvUl(upcastSelf.this)
        return returnValue

    
    def hasName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtYjhC(upcastSelf.this)
        return returnValue

    
    def getName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtfARN(upcastSelf.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._MouseWatcherRegion__overloaded_constructor_atomicstring_ptrConstLVecBase4f(*_args)
        elif numArgs == 5:
            return self._MouseWatcherRegion__overloaded_constructor_atomicstring_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 5 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._MouseWatcherRegion__overloaded_write_ptrConstMouseWatcherRegion_ptrOstream(*_args)
        elif numArgs == 2:
            return self._MouseWatcherRegion__overloaded_write_ptrConstMouseWatcherRegion_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setFrame(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._MouseWatcherRegion__overloaded_setFrame_ptrMouseWatcherRegion_ptrConstLVecBase4f(*_args)
        elif numArgs == 4:
            return self._MouseWatcherRegion__overloaded_setFrame_ptrMouseWatcherRegion_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 4 '

    
    def setRelative(self, np, left, right, bottom, top):
        Point3 = Point3
        import pandac
        mat = np.getMat(render2d)
        ll = mat.xformPoint(Point3.Point3(left, 0, bottom))
        ur = mat.xformPoint(Point3.Point3(right, 0, top))
        self.setFrame(ll[0], ur[0], ll[2], ur[2])


