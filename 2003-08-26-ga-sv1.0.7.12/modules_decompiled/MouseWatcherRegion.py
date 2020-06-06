# File: M (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TypedReferenceCount
import Namable

class MouseWatcherRegion(TypedReferenceCount.TypedReferenceCount, Namable.Namable, FFIExternalObject.FFIExternalObject):
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
        
        apply(self.constructor, _args)

    
    def _MouseWatcherRegion__overloaded_constructor_atomicstring_ptrConstLVecBase4f(self, name, frame):
        self.this = libpanda._inPziw5XN0b(name, frame.this)
        self.userManagesMemory = 1

    
    def _MouseWatcherRegion__overloaded_constructor_atomicstring_float_float_float_float(self, name, left, right, bottom, top):
        self.this = libpanda._inPziw5VKEG(name, left, right, bottom, top)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPziw5gc_U:
            libpanda._inPziw5gc_U(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPziw5ft1g()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _MouseWatcherRegion__overloaded_setFrame_ptrMouseWatcherRegion_ptrConstLVecBase4f(self, frame):
        returnValue = libpanda._inPziw5uRlo(self.this, frame.this)
        return returnValue

    
    def _MouseWatcherRegion__overloaded_setFrame_ptrMouseWatcherRegion_float_float_float_float(self, left, right, bottom, top):
        returnValue = libpanda._inPziw5UI04(self.this, left, right, bottom, top)
        return returnValue

    
    def getFrame(self):
        returnValue = libpanda._inPziw5C2td(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getArea(self):
        returnValue = libpanda._inPziw5xwAe(self.this)
        return returnValue

    
    def setSort(self, sort):
        returnValue = libpanda._inPziw5uUjJ(self.this, sort)
        return returnValue

    
    def getSort(self):
        returnValue = libpanda._inPziw5xQ_6(self.this)
        return returnValue

    
    def setActive(self, active):
        returnValue = libpanda._inPziw5G96x(self.this, active)
        return returnValue

    
    def getActive(self):
        returnValue = libpanda._inPziw5BoGH(self.this)
        return returnValue

    
    def setKeyboard(self, keyboard):
        returnValue = libpanda._inPziw5_wOd(self.this, keyboard)
        return returnValue

    
    def getKeyboard(self):
        returnValue = libpanda._inPziw53JK8(self.this)
        return returnValue

    
    def setSuppressFlags(self, suppressFlags):
        returnValue = libpanda._inPziw5TWvO(self.this, suppressFlags)
        return returnValue

    
    def getSuppressFlags(self):
        returnValue = libpanda._inPziw5yKjf(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPziw5kvVL(self.this, out.this)
        return returnValue

    
    def _MouseWatcherRegion__overloaded_write_ptrConstMouseWatcherRegion_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPziw5ijOS(self.this, out.this, indentLevel)
        return returnValue

    
    def _MouseWatcherRegion__overloaded_write_ptrConstMouseWatcherRegion_ptrOstream(self, out):
        returnValue = libpanda._inPziw5yqaj(self.this, out.this)
        return returnValue

    
    def upcastToNamable(self):
        returnValue = libpanda._inPziw5vEXk(self.this)
        import Namable
        returnObject = Namable.Namable(None)
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

    
    def assign(self, other):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtp1bI(upcastSelf.this, other.this)
        import Namable
        returnObject = Namable.Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setName(self, name):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtLNBW(upcastSelf.this, name)
        return returnValue

    
    def clearName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtavUl(upcastSelf.this)
        return returnValue

    
    def hasName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtYjhC(upcastSelf.this)
        return returnValue

    
    def getName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtfARN(upcastSelf.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.StringType):
                import VBase4
                if isinstance(_args[1], VBase4.VBase4):
                    return self._MouseWatcherRegion__overloaded_constructor_atomicstring_ptrConstLVecBase4f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase4.VBase4> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 5:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                return self._MouseWatcherRegion__overloaded_constructor_atomicstring_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4])
                            else:
                                raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 5 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._MouseWatcherRegion__overloaded_write_ptrConstMouseWatcherRegion_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._MouseWatcherRegion__overloaded_write_ptrConstMouseWatcherRegion_ptrOstream_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setFrame(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase4
            if isinstance(_args[0], VBase4.VBase4):
                return self._MouseWatcherRegion__overloaded_setFrame_ptrMouseWatcherRegion_ptrConstLVecBase4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
        elif numArgs == 4:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._MouseWatcherRegion__overloaded_setFrame_ptrMouseWatcherRegion_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
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

    
    def setRelative(self, np, left, right, bottom, top):
        import Point3
        mat = np.getMat(render2d)
        ll = mat.xformPoint(Point3.Point3(left, 0, bottom))
        ur = mat.xformPoint(Point3.Point3(right, 0, top))
        self.setFrame(ll[0], ur[0], ll[2], ur[2])


