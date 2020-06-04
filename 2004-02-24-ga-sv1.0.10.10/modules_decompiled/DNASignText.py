# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import DNANode

class DNASignText(DNANode.DNANode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _DNASignText__overloaded_constructor_ptrConstDNASignText(self, signText):
        self.this = libtoontown._inPet4yNeb4(signText.this)
        self.userManagesMemory = 1

    
    def _DNASignText__overloaded_constructor_atomicstring(self, initialName):
        self.this = libtoontown._inPet4yVHjl(initialName)
        self.userManagesMemory = 1

    
    def _DNASignText__overloaded_constructor(self):
        self.this = libtoontown._inPet4ykRFc()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPet4yYwX9:
            libtoontown._inPet4yYwX9(self.this)
        

    
    def getClassType():
        returnValue = libtoontown._inPet4yljAS()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setCode(self, code):
        returnValue = libtoontown._inPet4y5Aw_(self.this, code)
        return returnValue

    
    def getCode(self):
        returnValue = libtoontown._inPet4yF_Rb(self.this)
        return returnValue

    
    def setColor(self, color):
        returnValue = libtoontown._inPet4ytOiX(self.this, color.this)
        return returnValue

    
    def getColor(self):
        returnValue = libtoontown._inPet4yiIc1(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setLetters(self, letters):
        returnValue = libtoontown._inPet4yGPYM(self.this, letters)
        return returnValue

    
    def getLetters(self):
        returnValue = libtoontown._inPet4yovbX(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DNASignText__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DNASignText__overloaded_constructor_atomicstring(_args[0])
            elif isinstance(_args[0], DNASignText):
                return self._DNASignText__overloaded_constructor_ptrConstDNASignText(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNASignText> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


