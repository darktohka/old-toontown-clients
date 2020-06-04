# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Namable

class CardMaker(Namable.Namable, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self, name):
        self.this = libpanda._inPWs2xJ3MS(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPWs2xFFkv:
            libpanda._inPWs2xFFkv(self.this)
        

    
    def reset(self):
        returnValue = libpanda._inPWs2xbuRh(self.this)
        return returnValue

    
    def setUvRange(self, ll, ur):
        returnValue = libpanda._inPWs2x_5fw(self.this, ll.this, ur.this)
        return returnValue

    
    def setHasUvs(self, flag):
        returnValue = libpanda._inPWs2x_g_I(self.this, flag)
        return returnValue

    
    def _CardMaker__overloaded_setFrame_ptrCardMaker_ptrConstLVecBase4f(self, frame):
        returnValue = libpanda._inPWs2xLOM1(self.this, frame.this)
        return returnValue

    
    def _CardMaker__overloaded_setFrame_ptrCardMaker_float_float_float_float(self, left, right, bottom, top):
        returnValue = libpanda._inPWs2x2xT3(self.this, left, right, bottom, top)
        return returnValue

    
    def _CardMaker__overloaded_setColor_ptrCardMaker_ptrConstLVecBase4f(self, color):
        returnValue = libpanda._inPWs2xolpK(self.this, color.this)
        return returnValue

    
    def _CardMaker__overloaded_setColor_ptrCardMaker_float_float_float_float(self, r, g, b, a):
        returnValue = libpanda._inPWs2x0RvM(self.this, r, g, b, a)
        return returnValue

    
    def setSourceGeometry(self, node, frame):
        returnValue = libpanda._inPWs2xvDmZ(self.this, node.this, frame.this)
        return returnValue

    
    def clearSourceGeometry(self):
        returnValue = libpanda._inPWs2xH1YC(self.this)
        return returnValue

    
    def generate(self):
        returnValue = libpanda._inPWs2xscLf(self.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setColor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase4
            if isinstance(_args[0], VBase4.VBase4):
                return self._CardMaker__overloaded_setColor_ptrCardMaker_ptrConstLVecBase4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
        elif numArgs == 4:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._CardMaker__overloaded_setColor_ptrCardMaker_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
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

    
    def setFrame(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase4
            if isinstance(_args[0], VBase4.VBase4):
                return self._CardMaker__overloaded_setFrame_ptrCardMaker_ptrConstLVecBase4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
        elif numArgs == 4:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._CardMaker__overloaded_setFrame_ptrCardMaker_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
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


