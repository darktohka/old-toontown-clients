# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import DNANode

class DNASignGraphic(DNANode.DNANode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _DNASignGraphic__overloaded_constructor_ptrConstDNASignGraphic(self, graphic):
        self.this = libtoontown._inPet4yW2kO(graphic.this)
        self.userManagesMemory = 1

    
    def _DNASignGraphic__overloaded_constructor_atomicstring(self, initialName):
        self.this = libtoontown._inPet4y0oUg(initialName)
        self.userManagesMemory = 1

    
    def _DNASignGraphic__overloaded_constructor(self):
        self.this = libtoontown._inPet4yCWR_()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPet4yMbZX:
            libtoontown._inPet4yMbZX(self.this)
        

    
    def getClassType():
        returnValue = libtoontown._inPet4yvTfh()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setCode(self, code):
        returnValue = libtoontown._inPet4yOepc(self.this, code)
        return returnValue

    
    def getCode(self):
        returnValue = libtoontown._inPet4ywnGX(self.this)
        return returnValue

    
    def setColor(self, color):
        returnValue = libtoontown._inPet4yrrdI(self.this, color.this)
        return returnValue

    
    def getColor(self):
        returnValue = libtoontown._inPet4yfBaa(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setWidth(self, width):
        returnValue = libtoontown._inPet4yT6PO(self.this, width)
        return returnValue

    
    def getWidth(self):
        returnValue = libtoontown._inPet4y_6Po(self.this)
        return returnValue

    
    def setHeight(self, height):
        returnValue = libtoontown._inPet4yGOaD(self.this, height)
        return returnValue

    
    def getHeight(self):
        returnValue = libtoontown._inPet4yJhcb(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DNASignGraphic__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DNASignGraphic__overloaded_constructor_atomicstring(_args[0])
            elif isinstance(_args[0], DNASignGraphic):
                return self._DNASignGraphic__overloaded_constructor_ptrConstDNASignGraphic(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNASignGraphic> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


