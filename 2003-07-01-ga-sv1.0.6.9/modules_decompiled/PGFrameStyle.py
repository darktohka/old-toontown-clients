# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class PGFrameStyle(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    TGroove = 4
    TRidge = 5
    TFlat = 1
    TBevelOut = 2
    TBevelIn = 3
    TNone = 0
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _PGFrameStyle__overloaded_constructor(self):
        self.this = libpanda._inPWvimeplg()
        self.userManagesMemory = 1

    
    def _PGFrameStyle__overloaded_constructor_ptrConstPGFrameStyle(self, copy):
        self.this = libpanda._inPWvimkhUl(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPWvimYC6A:
            libpanda._inPWvimYC6A(self.this)
        

    
    def assign(self, copy):
        returnValue = libpanda._inPWvimnTPY(self.this, copy.this)
        returnObject = PGFrameStyle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setType(self, type):
        returnValue = libpanda._inPWvimJ8_1(self.this, type)
        return returnValue

    
    def getType(self):
        returnValue = libpanda._inPWvimeRTB(self.this)
        return returnValue

    
    def _PGFrameStyle__overloaded_setColor_ptrPGFrameStyle_ptrConstLVecBase4f(self, color):
        returnValue = libpanda._inPWvimrDgP(self.this, color.this)
        return returnValue

    
    def _PGFrameStyle__overloaded_setColor_ptrPGFrameStyle_float_float_float_float(self, r, g, b, a):
        returnValue = libpanda._inPWvimLqux(self.this, r, g, b, a)
        return returnValue

    
    def getColor(self):
        returnValue = libpanda._inPWvimarWM(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _PGFrameStyle__overloaded_setWidth_ptrPGFrameStyle_ptrConstLVecBase2f(self, width):
        returnValue = libpanda._inPWvimIq9R(self.this, width.this)
        return returnValue

    
    def _PGFrameStyle__overloaded_setWidth_ptrPGFrameStyle_float_float(self, x, y):
        returnValue = libpanda._inPWvimgZn4(self.this, x, y)
        return returnValue

    
    def getWidth(self):
        returnValue = libpanda._inPWvimP9TS(self.this)
        import VBase2
        returnObject = VBase2.VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def output(self, out):
        returnValue = libpanda._inPWvimp6gR(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PGFrameStyle__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], PGFrameStyle):
                return self._PGFrameStyle__overloaded_constructor_ptrConstPGFrameStyle(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PGFrameStyle> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setWidth(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase2
            if isinstance(_args[0], VBase2.VBase2):
                return self._PGFrameStyle__overloaded_setWidth_ptrPGFrameStyle_ptrConstLVecBase2f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase2.VBase2> '
        elif numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._PGFrameStyle__overloaded_setWidth_ptrPGFrameStyle_float_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setColor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase4
            if isinstance(_args[0], VBase4.VBase4):
                return self._PGFrameStyle__overloaded_setColor_ptrPGFrameStyle_ptrConstLVecBase4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
        elif numArgs == 4:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._PGFrameStyle__overloaded_setColor_ptrPGFrameStyle_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
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


