# File: H (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class HTTPDate(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _HTTPDate__overloaded_constructor(self):
        self.this = libpandaexpress._inP2KOdxUCO()
        self.userManagesMemory = 1

    
    def _HTTPDate__overloaded_constructor_ptrConstHTTPDate(self, copy):
        self.this = libpandaexpress._inP2KOdCU7n(copy.this)
        self.userManagesMemory = 1

    
    def _HTTPDate__overloaded_constructor_atomicstring(self, format):
        self.this = libpandaexpress._inP2KOd3lK9(format)
        self.userManagesMemory = 1

    
    def _HTTPDate__overloaded_constructor_unsignedint(self, time):
        self.this = libpandaexpress._inP2KOdd8vm(time)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inP2KOd7_jg:
            libpandaexpress._inP2KOd7_jg(self.this)
        

    
    def now():
        returnValue = libpandaexpress._inP2KOdDz_E()
        returnObject = HTTPDate(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    now = staticmethod(now)
    
    def assign(self, copy):
        returnValue = libpandaexpress._inP2KOdRJN6(self.this, copy.this)
        returnObject = HTTPDate(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def isValid(self):
        returnValue = libpandaexpress._inP2KOdWkTy(self.this)
        return returnValue

    
    def getString(self):
        returnValue = libpandaexpress._inP2KOdLLsb(self.this)
        return returnValue

    
    def getTime(self):
        returnValue = libpandaexpress._inP2KOdjMJn(self.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpandaexpress._inP2KOda8yo(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpandaexpress._inP2KOd85ho(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpandaexpress._inP2KOdc7Fy(self.this, other.this)
        return returnValue

    
    def greaterThan(self, other):
        returnValue = libpandaexpress._inP2KOdXJHy(self.this, other.this)
        return returnValue

    
    def compareTo(self, other):
        returnValue = libpandaexpress._inP2KOd4D07(self.this, other.this)
        return returnValue

    
    def __iadd__(self, seconds):
        returnValue = libpandaexpress._inP2KOdiIFs(self.this, seconds)
        return self

    
    def __isub__(self, seconds):
        returnValue = libpandaexpress._inP2KOdr_Hs(self.this, seconds)
        return self

    
    def __add__(self, seconds):
        returnValue = libpandaexpress._inP2KOdNh_f(self.this, seconds)
        returnObject = HTTPDate(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _HTTPDate__overloaded___sub___ptrConstHTTPDate_ptrConstHTTPDate(self, other):
        returnValue = libpandaexpress._inP2KOdTh8R(self.this, other.this)
        return returnValue

    
    def _HTTPDate__overloaded___sub___ptrConstHTTPDate_int(self, seconds):
        returnValue = libpandaexpress._inP2KOd5wBg(self.this, seconds)
        returnObject = HTTPDate(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def input(self, _in):
        returnValue = libpandaexpress._inP2KOdDJiR(self.this, _in.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inP2KOdAj07(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._HTTPDate__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._HTTPDate__overloaded_constructor_unsignedint(_args[0])
            elif isinstance(_args[0], types.StringType):
                return self._HTTPDate__overloaded_constructor_atomicstring(_args[0])
            elif isinstance(_args[0], HTTPDate):
                return self._HTTPDate__overloaded_constructor_ptrConstHTTPDate(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <types.StringType> <HTTPDate> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def __sub__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._HTTPDate__overloaded___sub___ptrConstHTTPDate_int(_args[0])
            elif isinstance(_args[0], HTTPDate):
                return self._HTTPDate__overloaded___sub___ptrConstHTTPDate_ptrConstHTTPDate(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <HTTPDate> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


