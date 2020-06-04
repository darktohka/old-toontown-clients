# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import DNAGroup

class DNANode(DNAGroup.DNAGroup, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _DNANode__overloaded_constructor_ptrConstDNANode(self, node):
        self.this = libtoontown._inPet4ynf58(node.this)
        self.userManagesMemory = 1

    
    def _DNANode__overloaded_constructor_atomicstring(self, initialName):
        self.this = libtoontown._inPet4yrVoe(initialName)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPet4y2a26:
            libtoontown._inPet4y2a26(self.this)
        

    
    def getClassType():
        returnValue = libtoontown._inPet4y87tV()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setPos(self, pos):
        returnValue = libtoontown._inPet4yLriI(self.this, pos.this)
        return returnValue

    
    def getPos(self):
        returnValue = libtoontown._inPet4yErPN(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setHpr(self, hpr):
        returnValue = libtoontown._inPet4yTGac(self.this, hpr.this)
        return returnValue

    
    def getHpr(self):
        returnValue = libtoontown._inPet4yrcGh(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setScale(self, scale):
        returnValue = libtoontown._inPet4yhI61(self.this, scale.this)
        return returnValue

    
    def getScale(self):
        returnValue = libtoontown._inPet4y_yMF(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DNANode__overloaded_constructor_atomicstring(_args[0])
            elif isinstance(_args[0], DNANode):
                return self._DNANode__overloaded_constructor_ptrConstDNANode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNANode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


