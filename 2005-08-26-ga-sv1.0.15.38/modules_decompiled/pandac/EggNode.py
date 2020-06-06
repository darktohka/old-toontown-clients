# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggNamedObject

class EggNode(EggNamedObject.EggNamedObject, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOMKmaF:
            libpandaegg._inPkAOMKmaF(self.this)
        

    
    def getClassType():
        returnValue = libpandaegg._inPkAOMrFAL()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOMj5Y4(self.this, copy.this)
        returnObject = EggNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getParent(self):
        returnValue = libpandaegg._inPkAOMcWNY(self.this)
        import EggGroupNode
        returnObject = EggGroupNode.EggGroupNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def getDepth(self):
        returnValue = libpandaegg._inPkAOMyhAk(self.this)
        return returnValue

    
    def isUnderInstance(self):
        returnValue = libpandaegg._inPkAOM3MCH(self.this)
        return returnValue

    
    def isUnderTransform(self):
        returnValue = libpandaegg._inPkAOMaghw(self.this)
        return returnValue

    
    def isLocalCoord(self):
        returnValue = libpandaegg._inPkAOMyHkj(self.this)
        return returnValue

    
    def getVertexFrame(self):
        returnValue = libpandaegg._inPkAOMtrwF(self.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNodeFrame(self):
        returnValue = libpandaegg._inPkAOMsUiB(self.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getVertexFrameInv(self):
        returnValue = libpandaegg._inPkAOMN4KR(self.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNodeFrameInv(self):
        returnValue = libpandaegg._inPkAOMv1_V(self.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getVertexToNode(self):
        returnValue = libpandaegg._inPkAOMXcNr(self.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNodeToVertex(self):
        returnValue = libpandaegg._inPkAOMNv_a(self.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getVertexFramePtr(self):
        returnValue = libpandaegg._inPkAOMv1HP(self.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNodeFramePtr(self):
        returnValue = libpandaegg._inPkAOM_tqL(self.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getVertexFrameInvPtr(self):
        returnValue = libpandaegg._inPkAOM3nvZ(self.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNodeFrameInvPtr(self):
        returnValue = libpandaegg._inPkAOMKkmK(self.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getVertexToNodePtr(self):
        returnValue = libpandaegg._inPkAOMB_1f(self.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNodeToVertexPtr(self):
        returnValue = libpandaegg._inPkAOM3soP(self.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def transform(self, mat):
        returnValue = libpandaegg._inPkAOMoQ8D(self.this, mat.this)
        return returnValue

    
    def transformVerticesOnly(self, mat):
        returnValue = libpandaegg._inPkAOM2Yja(self.this, mat.this)
        return returnValue

    
    def flattenTransforms(self):
        returnValue = libpandaegg._inPkAOM7nS3(self.this)
        return returnValue

    
    def applyTexmats(self):
        returnValue = libpandaegg._inPkAOMpzMK(self.this)
        return returnValue

    
    def isJoint(self):
        returnValue = libpandaegg._inPkAOMHHnM(self.this)
        return returnValue

    
    def isAnimMatrix(self):
        returnValue = libpandaegg._inPkAOM82MW(self.this)
        return returnValue

    
    def determineAlphaMode(self):
        returnValue = libpandaegg._inPkAOMuPXv(self.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def determineDepthWriteMode(self):
        returnValue = libpandaegg._inPkAOMNEGB(self.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def determineDepthTestMode(self):
        returnValue = libpandaegg._inPkAOMUWLJ(self.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def determineVisibilityMode(self):
        returnValue = libpandaegg._inPkAOMf8Wt(self.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def determineDrawOrder(self):
        returnValue = libpandaegg._inPkAOMx2w6(self.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def determineBin(self):
        returnValue = libpandaegg._inPkAOM6z27(self.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def determineIndexed(self):
        returnValue = libpandaegg._inPkAOM6Ucg(self.this)
        return returnValue

    
    def write(self, out, indentLevel):
        returnValue = libpandaegg._inPkAOMIrWM(self.this, out.this, indentLevel)
        return returnValue

    
    def parseEgg(self, eggSyntax):
        returnValue = libpandaegg._inPkAOMZKVQ(self.this, eggSyntax)
        return returnValue

    
    def testUnderIntegrity(self):
        returnValue = libpandaegg._inPkAOMp6_k(self.this)
        return returnValue


