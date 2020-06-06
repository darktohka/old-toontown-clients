# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import DNAGroup

class DNACornice(DNAGroup.DNAGroup, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _DNACornice__overloaded_constructor_ptrConstDNACornice(self, cornice):
        self.this = libtoontown._inPet4y17vQ(cornice.this)
        self.userManagesMemory = 1

    
    def _DNACornice__overloaded_constructor_atomicstring(self, initialName):
        self.this = libtoontown._inPet4yruOf(initialName)
        self.userManagesMemory = 1

    
    def _DNACornice__overloaded_constructor(self):
        self.this = libtoontown._inPet4yj6YA()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPet4yEN2j:
            libtoontown._inPet4yEN2j(self.this)
        

    
    def getClassType():
        returnValue = libtoontown._inPet4ynZxg()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setCode(self, code):
        returnValue = libtoontown._inPet4yIWIU(self.this, code)
        return returnValue

    
    def getCode(self):
        returnValue = libtoontown._inPet4ykAD7(self.this)
        return returnValue

    
    def setColor(self, color):
        returnValue = libtoontown._inPet4yZI6Q(self.this, color.this)
        return returnValue

    
    def getColor(self):
        returnValue = libtoontown._inPet4yJq3v(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DNACornice__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DNACornice__overloaded_constructor_atomicstring(_args[0])
            elif isinstance(_args[0], DNACornice):
                return self._DNACornice__overloaded_constructor_ptrConstDNACornice(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNACornice> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


