# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
from direct.ffi import FFIExternalObject

class EggTextureCollection(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EggTextureCollection__overloaded_constructor(self):
        self.this = libpandaegg._inPkAOMbU7L()
        self.userManagesMemory = 1

    
    def _EggTextureCollection__overloaded_constructor_ptrConstEggTextureCollection(self, copy):
        self.this = libpandaegg._inPkAOM8vVa(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOM_Gn7:
            libpandaegg._inPkAOM_Gn7(self.this)
        

    
    def replaceTextures(node, replace):
        returnValue = libpandaegg._inPkAOMeVh6(node.this, replace.this)
        return returnValue

    replaceTextures = staticmethod(replaceTextures)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOMw9Zk(self.this, copy.this)
        returnObject = EggTextureCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def clear(self):
        returnValue = libpandaegg._inPkAOMGhyi(self.this)
        return returnValue

    
    def extractTextures(self, node):
        returnValue = libpandaegg._inPkAOMrcPl(self.this, node.this)
        return returnValue

    
    def isEmpty(self):
        returnValue = libpandaegg._inPkAOM8UpD(self.this)
        return returnValue

    
    def getNumTextures(self):
        returnValue = libpandaegg._inPkAOMsDuL(self.this)
        return returnValue

    
    def getTexture(self, index):
        returnValue = libpandaegg._inPkAOMWocW(self.this, index)
        import EggTexture
        returnObject = EggTexture.EggTexture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def findUsedTextures(self, node):
        returnValue = libpandaegg._inPkAOMKek0(self.this, node.this)
        return returnValue

    
    def removeUnusedTextures(self, node):
        returnValue = libpandaegg._inPkAOM9oZ4(self.this, node.this)
        return returnValue

    
    def _EggTextureCollection__overloaded_collapseEquivalentTextures_ptrEggTextureCollection_int_ptrEggGroupNode(self, eq, node):
        returnValue = libpandaegg._inPkAOMqFH7(self.this, eq, node.this)
        return returnValue

    
    def _EggTextureCollection__overloaded_collapseEquivalentTextures_ptrEggTextureCollection_int_ptrMapPointerToEggTexturePointerToEggTexture(self, eq, removed):
        returnValue = libpandaegg._inPkAOMKhTa(self.this, eq, removed.this)
        return returnValue

    
    def uniquifyTrefs(self):
        returnValue = libpandaegg._inPkAOMalB_(self.this)
        return returnValue

    
    def sortByTref(self):
        returnValue = libpandaegg._inPkAOM1R_8(self.this)
        return returnValue

    
    def addTexture(self, texture):
        returnValue = libpandaegg._inPkAOMTk2Y(self.this, texture.this)
        return returnValue

    
    def removeTexture(self, texture):
        returnValue = libpandaegg._inPkAOMyDeK(self.this, texture.this)
        return returnValue

    
    def createUniqueTexture(self, copy, eq):
        returnValue = libpandaegg._inPkAOMLULD(self.this, copy.this, eq)
        import EggTexture
        returnObject = EggTexture.EggTexture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def findTref(self, trefName):
        returnValue = libpandaegg._inPkAOM4Tew(self.this, trefName)
        import EggTexture
        returnObject = EggTexture.EggTexture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def findFilename(self, filename):
        returnValue = libpandaegg._inPkAOMQxLn(self.this, filename.this)
        import EggTexture
        returnObject = EggTexture.EggTexture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggTextureCollection__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._EggTextureCollection__overloaded_constructor_ptrConstEggTextureCollection(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def collapseEquivalentTextures(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                import MapPointerToEggTexturePointerToEggTexture
                if isinstance(_args[1], MapPointerToEggTexturePointerToEggTexture.MapPointerToEggTexturePointerToEggTexture):
                    return self._EggTextureCollection__overloaded_collapseEquivalentTextures_ptrEggTextureCollection_int_ptrMapPointerToEggTexturePointerToEggTexture(*_args)
                
                import EggGroupNode
                if isinstance(_args[1], EggGroupNode.EggGroupNode):
                    return self._EggTextureCollection__overloaded_collapseEquivalentTextures_ptrEggTextureCollection_int_ptrEggGroupNode(*_args)
                
                raise TypeError, 'Invalid argument 1, expected one of: <MapPointerToEggTexturePointerToEggTexture.MapPointerToEggTexturePointerToEggTexture> <EggGroupNode.EggGroupNode> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '


