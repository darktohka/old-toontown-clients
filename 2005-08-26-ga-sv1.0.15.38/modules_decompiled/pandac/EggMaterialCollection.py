# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
from direct.ffi import FFIExternalObject

class EggMaterialCollection(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EggMaterialCollection__overloaded_constructor(self):
        self.this = libpandaegg._inPkAOM2_LL()
        self.userManagesMemory = 1

    
    def _EggMaterialCollection__overloaded_constructor_ptrConstEggMaterialCollection(self, copy):
        self.this = libpandaegg._inPkAOMI3vE(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOMZ6R2:
            libpandaegg._inPkAOMZ6R2(self.this)
        

    
    def replaceMaterials(node, replace):
        returnValue = libpandaegg._inPkAOM0Vhs(node.this, replace.this)
        return returnValue

    replaceMaterials = staticmethod(replaceMaterials)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOMEcH7(self.this, copy.this)
        returnObject = EggMaterialCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def clear(self):
        returnValue = libpandaegg._inPkAOMUC81(self.this)
        return returnValue

    
    def extractMaterials(self, node):
        returnValue = libpandaegg._inPkAOMOymL(self.this, node.this)
        return returnValue

    
    def findUsedMaterials(self, node):
        returnValue = libpandaegg._inPkAOMxG5C(self.this, node.this)
        return returnValue

    
    def removeUnusedMaterials(self, node):
        returnValue = libpandaegg._inPkAOM74xc(self.this, node.this)
        return returnValue

    
    def _EggMaterialCollection__overloaded_collapseEquivalentMaterials_ptrEggMaterialCollection_int_ptrEggGroupNode(self, eq, node):
        returnValue = libpandaegg._inPkAOM8xlm(self.this, eq, node.this)
        return returnValue

    
    def _EggMaterialCollection__overloaded_collapseEquivalentMaterials_ptrEggMaterialCollection_int_ptrMapPointerToEggMaterialPointerToEggMaterial(self, eq, removed):
        returnValue = libpandaegg._inPkAOMV3rv(self.this, eq, removed.this)
        return returnValue

    
    def uniquifyMrefs(self):
        returnValue = libpandaegg._inPkAOMcBOS(self.this)
        return returnValue

    
    def sortByMref(self):
        returnValue = libpandaegg._inPkAOMs9_r(self.this)
        return returnValue

    
    def addMaterial(self, material):
        returnValue = libpandaegg._inPkAOMJriL(self.this, material.this)
        return returnValue

    
    def removeMaterial(self, material):
        returnValue = libpandaegg._inPkAOMzqxK(self.this, material.this)
        return returnValue

    
    def createUniqueMaterial(self, copy, eq):
        returnValue = libpandaegg._inPkAOMyOi1(self.this, copy.this, eq)
        import EggMaterial
        returnObject = EggMaterial.EggMaterial(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def findMref(self, mrefName):
        returnValue = libpandaegg._inPkAOMcDwq(self.this, mrefName)
        import EggMaterial
        returnObject = EggMaterial.EggMaterial(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggMaterialCollection__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._EggMaterialCollection__overloaded_constructor_ptrConstEggMaterialCollection(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def collapseEquivalentMaterials(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                import MapPointerToEggMaterialPointerToEggMaterial
                if isinstance(_args[1], MapPointerToEggMaterialPointerToEggMaterial.MapPointerToEggMaterialPointerToEggMaterial):
                    return self._EggMaterialCollection__overloaded_collapseEquivalentMaterials_ptrEggMaterialCollection_int_ptrMapPointerToEggMaterialPointerToEggMaterial(*_args)
                
                import EggGroupNode
                if isinstance(_args[1], EggGroupNode.EggGroupNode):
                    return self._EggMaterialCollection__overloaded_collapseEquivalentMaterials_ptrEggMaterialCollection_int_ptrEggGroupNode(*_args)
                
                raise TypeError, 'Invalid argument 1, expected one of: <MapPointerToEggMaterialPointerToEggMaterial.MapPointerToEggMaterialPointerToEggMaterial> <EggGroupNode.EggGroupNode> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '


