# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import Namable

class CardMaker(Namable.Namable, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpanda._inPXs2xJ3MS(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPXs2xCFkv:
            libpanda._inPXs2xCFkv(self.this)
        

    
    def reset(self):
        returnValue = libpanda._inPXs2xcuRh(self.this)
        return returnValue

    
    def setUvRange(self, ll, ur):
        returnValue = libpanda._inPXs2x_5fw(self.this, ll.this, ur.this)
        return returnValue

    
    def setHasUvs(self, flag):
        returnValue = libpanda._inPXs2x_g_I(self.this, flag)
        return returnValue

    
    def _CardMaker__overloaded_setFrame_ptrCardMaker_ptrConstLVecBase4f(self, frame):
        returnValue = libpanda._inPXs2xKOM1(self.this, frame.this)
        return returnValue

    
    def _CardMaker__overloaded_setFrame_ptrCardMaker_float_float_float_float(self, left, right, bottom, top):
        returnValue = libpanda._inPXs2x3xT3(self.this, left, right, bottom, top)
        return returnValue

    
    def _CardMaker__overloaded_setColor_ptrCardMaker_ptrConstLVecBase4f(self, color):
        returnValue = libpanda._inPXs2xolpK(self.this, color.this)
        return returnValue

    
    def _CardMaker__overloaded_setColor_ptrCardMaker_float_float_float_float(self, r, g, b, a):
        returnValue = libpanda._inPXs2x0RvM(self.this, r, g, b, a)
        return returnValue

    
    def setSourceGeometry(self, node, frame):
        returnValue = libpanda._inPXs2xvDmZ(self.this, node.this, frame.this)
        return returnValue

    
    def clearSourceGeometry(self):
        returnValue = libpanda._inPXs2xH1YC(self.this)
        return returnValue

    
    def generate(self):
        returnValue = libpanda._inPXs2xscLf(self.this)
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
            return self._CardMaker__overloaded_setColor_ptrCardMaker_ptrConstLVecBase4f(*_args)
        elif numArgs == 4:
            return self._CardMaker__overloaded_setColor_ptrCardMaker_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 4 '

    
    def setFrame(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._CardMaker__overloaded_setFrame_ptrCardMaker_ptrConstLVecBase4f(*_args)
        elif numArgs == 4:
            return self._CardMaker__overloaded_setFrame_ptrCardMaker_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 4 '


