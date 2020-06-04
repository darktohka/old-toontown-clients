# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggNode

class EggMaterial(EggNode.EggNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    EAttributes = 1
    EMrefName = 2
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EggMaterial__overloaded_constructor_ptrConstEggMaterial(self, copy):
        self.this = libpandaegg._inPkAOM4BtE(copy.this)
        self.userManagesMemory = 1

    
    def _EggMaterial__overloaded_constructor_atomicstring(self, mrefName):
        self.this = libpandaegg._inPkAOM9ThA(mrefName)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOMUz1i:
            libpandaegg._inPkAOMUz1i(self.this)
        

    
    def getClassType():
        returnValue = libpandaegg._inPkAOM6GjJ()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def isEquivalentTo(self, other, eq):
        returnValue = libpandaegg._inPkAOM7WW0(self.this, other.this, eq)
        return returnValue

    
    def sortsLessThan(self, other, eq):
        returnValue = libpandaegg._inPkAOMOiSX(self.this, other.this, eq)
        return returnValue

    
    def setDiff(self, diff):
        returnValue = libpandaegg._inPkAOM2XHn(self.this, diff.this)
        return returnValue

    
    def clearDiff(self):
        returnValue = libpandaegg._inPkAOMpXQH(self.this)
        return returnValue

    
    def hasDiff(self):
        returnValue = libpandaegg._inPkAOM5VsI(self.this)
        return returnValue

    
    def getDiff(self):
        returnValue = libpandaegg._inPkAOMVUXF(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setAmb(self, amb):
        returnValue = libpandaegg._inPkAOMkoW3(self.this, amb.this)
        return returnValue

    
    def clearAmb(self):
        returnValue = libpandaegg._inPkAOMM1fj(self.this)
        return returnValue

    
    def hasAmb(self):
        returnValue = libpandaegg._inPkAOMAF9W(self.this)
        return returnValue

    
    def getAmb(self):
        returnValue = libpandaegg._inPkAOM6EmT(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setEmit(self, emit):
        returnValue = libpandaegg._inPkAOMBinD(self.this, emit.this)
        return returnValue

    
    def clearEmit(self):
        returnValue = libpandaegg._inPkAOMho4b(self.this)
        return returnValue

    
    def hasEmit(self):
        returnValue = libpandaegg._inPkAOMQHMl(self.this)
        return returnValue

    
    def getEmit(self):
        returnValue = libpandaegg._inPkAOM6G3h(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setSpec(self, spec):
        returnValue = libpandaegg._inPkAOMLAce(self.this, spec.this)
        return returnValue

    
    def clearSpec(self):
        returnValue = libpandaegg._inPkAOM_Bc2(self.this)
        return returnValue

    
    def hasSpec(self):
        returnValue = libpandaegg._inPkAOMNpCA(self.this)
        return returnValue

    
    def getSpec(self):
        returnValue = libpandaegg._inPkAOM0ot8(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setShininess(self, shininess):
        returnValue = libpandaegg._inPkAOMifeq(self.this, shininess)
        return returnValue

    
    def clearShininess(self):
        returnValue = libpandaegg._inPkAOMNivw(self.this)
        return returnValue

    
    def hasShininess(self):
        returnValue = libpandaegg._inPkAOMqZE6(self.this)
        return returnValue

    
    def getShininess(self):
        returnValue = libpandaegg._inPkAOM8bv2(self.this)
        return returnValue

    
    def setLocal(self, local):
        returnValue = libpandaegg._inPkAOMJOXd(self.this, local)
        return returnValue

    
    def clearLocal(self):
        returnValue = libpandaegg._inPkAOM0Bui(self.this)
        return returnValue

    
    def hasLocal(self):
        returnValue = libpandaegg._inPkAOMmJXP(self.this)
        return returnValue

    
    def getLocal(self):
        returnValue = libpandaegg._inPkAOMcKAM(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._EggMaterial__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], EggMaterial):
                return self._EggMaterial__overloaded_constructor_ptrConstEggMaterial(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <EggMaterial> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


