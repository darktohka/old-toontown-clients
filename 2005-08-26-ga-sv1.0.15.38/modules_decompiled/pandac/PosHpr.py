# File: P (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
from direct.ffi import FFIExternalObject

class PosHpr(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _PosHpr__overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f(self, pos, hpr):
        self.this = libtoontown._inPdt4yJ_mZ(pos.this, hpr.this)
        self.userManagesMemory = 1

    
    def _PosHpr__overloaded_constructor_ptrConstLPoint3f(self, pos):
        self.this = libtoontown._inPdt4yD1B1(pos.this)
        self.userManagesMemory = 1

    
    def _PosHpr__overloaded_constructor(self):
        self.this = libtoontown._inPdt4yz9z8()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPdt4ykD4a:
            libtoontown._inPdt4ykD4a(self.this)
        

    
    def getPos(self):
        returnValue = libtoontown._inPdt4yKdTP(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getHpr(self):
        returnValue = libtoontown._inPdt4yEm7x(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PosHpr__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._PosHpr__overloaded_constructor_ptrConstLPoint3f(*_args)
        elif numArgs == 2:
            return self._PosHpr__overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


