# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggFilenameNode
import EggRenderMode

class EggTexture(EggFilenameNode.EggFilenameNode, EggRenderMode.EggRenderMode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    ETransform = 8
    EExtension = 2
    ECompleteFilename = 7
    EDirname = 4
    EBasename = 1
    EAttributes = 16
    ETrefName = 32
    FRgba = 1
    FRgba12 = 3
    FBlue = 14
    FRgb332 = 11
    FGreen = 13
    FRgb12 = 8
    FLuminanceAlphamask = 18
    FLuminanceAlpha = 17
    FRgbm = 2
    FRed = 12
    FAlpha = 15
    FRgba8 = 4
    FRgb = 7
    FRgb5 = 10
    FRgb8 = 9
    FLuminance = 16
    FUnspecified = 0
    FRgba4 = 5
    FRgba5 = 6
    WMUnspecified = 0
    WMClamp = 2
    WMRepeat = 1
    FTLinearMipmapNearest = 4
    FTNearestMipmapNearest = 3
    FTNearest = 1
    FTLinearMipmapLinear = 6
    FTLinear = 2
    FTUnspecified = 0
    FTNearestMipmapLinear = 5
    ETBlend = 3
    ETReplace = 4
    ETDecal = 2
    ETModulate = 1
    ETAdd = 5
    ETUnspecified = 0
    CMDot3Rgba = 8
    CMDot3Rgb = 7
    CMInterpolate = 5
    CMReplace = 1
    CMAdd = 3
    CMAddSigned = 4
    CMModulate = 2
    CMUnspecified = 0
    CMSubtract = 6
    CCAlpha = 1
    CCRgb = 0
    CCNumChannels = 2
    CINumIndices = 3
    CSConstant = 2
    CSTexture = 1
    CSPrimaryColor = 3
    CSPrevious = 4
    CSUnspecified = 0
    COUnspecified = 0
    COOneMinusSrcColor = 2
    COOneMinusSrcAlpha = 4
    COSrcAlpha = 3
    COSrcColor = 1
    TGWorldPosition = 3
    TGObjectPosition = 4
    TGSphereMap = 1
    TGUnspecified = 0
    TGEyePosition = 5
    TGCubeMap = 2
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EggTexture__overloaded_constructor_ptrConstEggTexture(self, copy):
        self.this = libpandaegg._inPkAOMhng8(copy.this)
        self.userManagesMemory = 1

    
    def _EggTexture__overloaded_constructor_atomicstring_atomicstring(self, trefName, filename):
        self.this = libpandaegg._inPkAOMezxT(trefName, filename)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOMsk4I:
            libpandaegg._inPkAOMsk4I(self.this)
        

    
    def stringFormat(cString):
        returnValue = libpandaegg._inPkAOM0Tc1(cString)
        return returnValue

    stringFormat = staticmethod(stringFormat)
    
    def stringWrapMode(cString):
        returnValue = libpandaegg._inPkAOM_IIf(cString)
        return returnValue

    stringWrapMode = staticmethod(stringWrapMode)
    
    def stringFilterType(cString):
        returnValue = libpandaegg._inPkAOM3nqW(cString)
        return returnValue

    stringFilterType = staticmethod(stringFilterType)
    
    def stringEnvType(cString):
        returnValue = libpandaegg._inPkAOM_bFc(cString)
        return returnValue

    stringEnvType = staticmethod(stringEnvType)
    
    def stringCombineMode(cString):
        returnValue = libpandaegg._inPkAOMjFLT(cString)
        return returnValue

    stringCombineMode = staticmethod(stringCombineMode)
    
    def stringCombineSource(cString):
        returnValue = libpandaegg._inPkAOMEKtK(cString)
        return returnValue

    stringCombineSource = staticmethod(stringCombineSource)
    
    def stringCombineOperand(cString):
        returnValue = libpandaegg._inPkAOMnTQ1(cString)
        return returnValue

    stringCombineOperand = staticmethod(stringCombineOperand)
    
    def stringTexGen(cString):
        returnValue = libpandaegg._inPkAOMyeH3(cString)
        return returnValue

    stringTexGen = staticmethod(stringTexGen)
    
    def getClassType():
        returnValue = libpandaegg._inPkAOMTKZT()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOM0TMq(self.this, copy.this)
        returnObject = EggTexture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def write(self, out, indentLevel):
        returnValue = libpandaegg._inPkAOMBpY9(self.this, out.this, indentLevel)
        return returnValue

    
    def isEquivalentTo(self, other, eq):
        returnValue = libpandaegg._inPkAOMUj_f(self.this, other.this, eq)
        return returnValue

    
    def sortsLessThan(self, other, eq):
        returnValue = libpandaegg._inPkAOMzib2(self.this, other.this, eq)
        return returnValue

    
    def hasAlphaChannel(self, numComponents):
        returnValue = libpandaegg._inPkAOMmUrS(self.this, numComponents)
        return returnValue

    
    def setFormat(self, format):
        returnValue = libpandaegg._inPkAOMN8dF(self.this, format)
        return returnValue

    
    def getFormat(self):
        returnValue = libpandaegg._inPkAOMkehA(self.this)
        return returnValue

    
    def setWrapMode(self, mode):
        returnValue = libpandaegg._inPkAOMDsmU(self.this, mode)
        return returnValue

    
    def getWrapMode(self):
        returnValue = libpandaegg._inPkAOM8r0r(self.this)
        return returnValue

    
    def setWrapU(self, mode):
        returnValue = libpandaegg._inPkAOMgtfQ(self.this, mode)
        return returnValue

    
    def getWrapU(self):
        returnValue = libpandaegg._inPkAOMefXa(self.this)
        return returnValue

    
    def determineWrapU(self):
        returnValue = libpandaegg._inPkAOMHY2e(self.this)
        return returnValue

    
    def setWrapV(self, mode):
        returnValue = libpandaegg._inPkAOMglQa(self.this, mode)
        return returnValue

    
    def getWrapV(self):
        returnValue = libpandaegg._inPkAOMeXIk(self.this)
        return returnValue

    
    def determineWrapV(self):
        returnValue = libpandaegg._inPkAOM9buP(self.this)
        return returnValue

    
    def setMinfilter(self, type):
        returnValue = libpandaegg._inPkAOMqq6L(self.this, type)
        return returnValue

    
    def getMinfilter(self):
        returnValue = libpandaegg._inPkAOMmUr5(self.this)
        return returnValue

    
    def setMagfilter(self, type):
        returnValue = libpandaegg._inPkAOM6hL5(self.this, type)
        return returnValue

    
    def getMagfilter(self):
        returnValue = libpandaegg._inPkAOMsd7m(self.this)
        return returnValue

    
    def setAnisotropicDegree(self, anisotropicDegree):
        returnValue = libpandaegg._inPkAOMKwkc(self.this, anisotropicDegree)
        return returnValue

    
    def clearAnisotropicDegree(self):
        returnValue = libpandaegg._inPkAOMc_H7(self.this)
        return returnValue

    
    def hasAnisotropicDegree(self):
        returnValue = libpandaegg._inPkAOMvvBL(self.this)
        return returnValue

    
    def getAnisotropicDegree(self):
        returnValue = libpandaegg._inPkAOMrl66(self.this)
        return returnValue

    
    def setEnvType(self, type):
        returnValue = libpandaegg._inPkAOM5MIV(self.this, type)
        return returnValue

    
    def getEnvType(self):
        returnValue = libpandaegg._inPkAOMm3Xk(self.this)
        return returnValue

    
    def setCombineMode(self, channel, cm):
        returnValue = libpandaegg._inPkAOMc01z(self.this, channel, cm)
        return returnValue

    
    def getCombineMode(self, channel):
        returnValue = libpandaegg._inPkAOMmQoH(self.this, channel)
        return returnValue

    
    def setCombineSource(self, channel, n, cs):
        returnValue = libpandaegg._inPkAOM0GKW(self.this, channel, n, cs)
        return returnValue

    
    def getCombineSource(self, channel, n):
        returnValue = libpandaegg._inPkAOM7qA3(self.this, channel, n)
        return returnValue

    
    def setCombineOperand(self, channel, n, co):
        returnValue = libpandaegg._inPkAOMBmvl(self.this, channel, n, co)
        return returnValue

    
    def getCombineOperand(self, channel, n):
        returnValue = libpandaegg._inPkAOMDf6C(self.this, channel, n)
        return returnValue

    
    def setTexGen(self, texGen):
        returnValue = libpandaegg._inPkAOM2fGJ(self.this, texGen)
        return returnValue

    
    def getTexGen(self):
        returnValue = libpandaegg._inPkAOMNv5D(self.this)
        return returnValue

    
    def setStageName(self, stageName):
        returnValue = libpandaegg._inPkAOMe7XX(self.this, stageName)
        return returnValue

    
    def clearStageName(self):
        returnValue = libpandaegg._inPkAOMiXJB(self.this)
        return returnValue

    
    def hasStageName(self):
        returnValue = libpandaegg._inPkAOMDGGJ(self.this)
        return returnValue

    
    def getStageName(self):
        returnValue = libpandaegg._inPkAOM2aA5(self.this)
        return returnValue

    
    def setPriority(self, priority):
        returnValue = libpandaegg._inPkAOMUObk(self.this, priority)
        return returnValue

    
    def clearPriority(self):
        returnValue = libpandaegg._inPkAOMnuob(self.this)
        return returnValue

    
    def hasPriority(self):
        returnValue = libpandaegg._inPkAOMlRHd(self.this)
        return returnValue

    
    def getPriority(self):
        returnValue = libpandaegg._inPkAOMlpBN(self.this)
        return returnValue

    
    def setColor(self, color):
        returnValue = libpandaegg._inPkAOM1PlD(self.this, color.this)
        return returnValue

    
    def clearColor(self):
        returnValue = libpandaegg._inPkAOMlDQn(self.this)
        return returnValue

    
    def hasColor(self):
        returnValue = libpandaegg._inPkAOMYqny(self.this)
        return returnValue

    
    def getColor(self):
        returnValue = libpandaegg._inPkAOMZ8gi(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setUvName(self, uvName):
        returnValue = libpandaegg._inPkAOMbLpF(self.this, uvName)
        return returnValue

    
    def clearUvName(self):
        returnValue = libpandaegg._inPkAOMA8X4(self.this)
        return returnValue

    
    def hasUvName(self):
        returnValue = libpandaegg._inPkAOMY3F6(self.this)
        return returnValue

    
    def getUvName(self):
        returnValue = libpandaegg._inPkAOMSj_p(self.this)
        return returnValue

    
    def setTransform(self, transform):
        returnValue = libpandaegg._inPkAOMSZkw(self.this, transform.this)
        return returnValue

    
    def clearTransform(self):
        returnValue = libpandaegg._inPkAOM7rEE(self.this)
        return returnValue

    
    def hasTransform(self):
        returnValue = libpandaegg._inPkAOMANLz(self.this)
        return returnValue

    
    def getTransform(self):
        returnValue = libpandaegg._inPkAOM2NFj(self.this)
        import Mat3D
        returnObject = Mat3D.Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def transformIsIdentity(self):
        returnValue = libpandaegg._inPkAOM2Ku_(self.this)
        return returnValue

    
    def setAlphaFilename(self, filename):
        returnValue = libpandaegg._inPkAOMHJuv(self.this, filename.this)
        return returnValue

    
    def clearAlphaFilename(self):
        returnValue = libpandaegg._inPkAOMdOt2(self.this)
        return returnValue

    
    def hasAlphaFilename(self):
        returnValue = libpandaegg._inPkAOMHCpy(self.this)
        return returnValue

    
    def getAlphaFilename(self):
        returnValue = libpandaegg._inPkAOMUIki(self.this)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setAlphaFullpath(self, fullpath):
        returnValue = libpandaegg._inPkAOMOxMH(self.this, fullpath.this)
        return returnValue

    
    def getAlphaFullpath(self):
        returnValue = libpandaegg._inPkAOMDkA6(self.this)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setAlphaFileChannel(self, alphaFileChannel):
        returnValue = libpandaegg._inPkAOMidkB(self.this, alphaFileChannel)
        return returnValue

    
    def clearAlphaFileChannel(self):
        returnValue = libpandaegg._inPkAOMXTSW(self.this)
        return returnValue

    
    def hasAlphaFileChannel(self):
        returnValue = libpandaegg._inPkAOMER_v(self.this)
        return returnValue

    
    def getAlphaFileChannel(self):
        returnValue = libpandaegg._inPkAOMK55f(self.this)
        return returnValue

    
    def clearMultitexture(self):
        returnValue = libpandaegg._inPkAOMSUMy(self.this)
        return returnValue

    
    def multitextureOver(self, other):
        returnValue = libpandaegg._inPkAOM3XDK(self.this, other.this)
        return returnValue

    
    def getMultitextureSort(self):
        returnValue = libpandaegg._inPkAOMjbNS(self.this)
        return returnValue

    
    def upcastToEggRenderMode(self):
        returnValue = libpandaegg._inPkAOM2rIs(self.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getDefaultExtension(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMXj7g(upcastSelf.this)
        return returnValue

    
    def getFilename(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMXJxZ(upcastSelf.this)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setFilename(self, filename):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMA0g1(upcastSelf.this, filename.this)
        return returnValue

    
    def getFullpath(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM8Thq(upcastSelf.this)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setFullpath(self, fullpath):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMI1PG(upcastSelf.this, fullpath.this)
        return returnValue

    
    def getParent(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMcWNY(upcastSelf.this)
        import EggGroupNode
        returnObject = EggGroupNode.EggGroupNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def getDepth(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMyhAk(upcastSelf.this)
        return returnValue

    
    def isUnderInstance(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM3MCH(upcastSelf.this)
        return returnValue

    
    def isUnderTransform(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMaghw(upcastSelf.this)
        return returnValue

    
    def isLocalCoord(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMyHkj(upcastSelf.this)
        return returnValue

    
    def getVertexFrame(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMtrwF(upcastSelf.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNodeFrame(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMsUiB(upcastSelf.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getVertexFrameInv(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMN4KR(upcastSelf.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNodeFrameInv(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMv1_V(upcastSelf.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getVertexToNode(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMXcNr(upcastSelf.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNodeToVertex(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMNv_a(upcastSelf.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getVertexFramePtr(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMv1HP(upcastSelf.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNodeFramePtr(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM_tqL(upcastSelf.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getVertexFrameInvPtr(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM3nvZ(upcastSelf.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNodeFrameInvPtr(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMKkmK(upcastSelf.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getVertexToNodePtr(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMB_1f(upcastSelf.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNodeToVertexPtr(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM3soP(upcastSelf.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def transform(self, mat):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMoQ8D(upcastSelf.this, mat.this)
        return returnValue

    
    def transformVerticesOnly(self, mat):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM2Yja(upcastSelf.this, mat.this)
        return returnValue

    
    def flattenTransforms(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM7nS3(upcastSelf.this)
        return returnValue

    
    def applyTexmats(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMpzMK(upcastSelf.this)
        return returnValue

    
    def isJoint(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMHHnM(upcastSelf.this)
        return returnValue

    
    def isAnimMatrix(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM82MW(upcastSelf.this)
        return returnValue

    
    def determineAlphaMode(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMuPXv(upcastSelf.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def determineDepthWriteMode(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMNEGB(upcastSelf.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def determineDepthTestMode(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMUWLJ(upcastSelf.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def determineVisibilityMode(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMf8Wt(upcastSelf.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def determineDrawOrder(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMx2w6(upcastSelf.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def determineBin(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM6z27(upcastSelf.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def determineIndexed(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM6Ucg(upcastSelf.this)
        return returnValue

    
    def parseEgg(self, eggSyntax):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMZKVQ(upcastSelf.this, eggSyntax)
        return returnValue

    
    def testUnderIntegrity(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMp6_k(upcastSelf.this)
        return returnValue

    
    def output(self, out):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMjJfG(upcastSelf.this, out.this)
        return returnValue

    
    def upcastToNamable(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMQtFW(upcastSelf.this)
        import Namable
        returnObject = Namable.Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setUserData(self, userData):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMi4s0(upcastSelf.this, userData.this)
        return returnValue

    
    def getUserData(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMWm2j(upcastSelf.this)
        import EggUserData
        returnObject = EggUserData.EggUserData(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _EggTexture__overloaded_hasUserData_ptrConstEggObject(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMibXq(upcastSelf.this)
        return returnValue

    
    def _EggTexture__overloaded_hasUserData_ptrConstEggObject_ptrTypeHandle(self, type):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMvhRl(upcastSelf.this, type.this)
        return returnValue

    
    def clearUserData(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM0OqA(upcastSelf.this)
        return returnValue

    
    def hasUserData(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggTexture__overloaded_hasUserData_ptrConstEggObject(*_args)
        elif numArgs == 1:
            return self._EggTexture__overloaded_hasUserData_ptrConstEggObject_ptrTypeHandle(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def upcastToReferenceCount(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxtKE8f(upcastSelf.this)
        import ReferenceCount
        returnObject = ReferenceCount.ReferenceCount(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getType(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxt1uxI(upcastSelf.this)
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getTypeIndex(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxtm7AU(upcastSelf.this)
        return returnValue

    
    def isOfType(self, handle):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxtnFKt(upcastSelf.this, handle.this)
        return returnValue

    
    def isExactType(self, handle):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxt7Xzz(upcastSelf.this, handle.this)
        return returnValue

    
    def getRefCount(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtP11_(upcastSelf.this)
        return returnValue

    
    def ref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtaS5_(upcastSelf.this)
        return returnValue

    
    def unref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtwyVy(upcastSelf.this)
        return returnValue

    
    def testRefCountIntegrity(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtvpj2(upcastSelf.this)
        return returnValue

    
    def setName(self, name):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtLNBW(upcastSelf.this, name)
        return returnValue

    
    def clearName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtZvUl(upcastSelf.this)
        return returnValue

    
    def hasName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtYjhC(upcastSelf.this)
        return returnValue

    
    def getName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtfARN(upcastSelf.this)
        return returnValue

    
    def setAlphaMode(self, mode):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOM7kse(upcastSelf.this, mode)
        return returnValue

    
    def getAlphaMode(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOM3t3A(upcastSelf.this)
        return returnValue

    
    def setDepthWriteMode(self, mode):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMCEUa(upcastSelf.this, mode)
        return returnValue

    
    def getDepthWriteMode(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMaHHZ(upcastSelf.this)
        return returnValue

    
    def setDepthTestMode(self, mode):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMOa7S(upcastSelf.this, mode)
        return returnValue

    
    def getDepthTestMode(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMkkuX(upcastSelf.this)
        return returnValue

    
    def setVisibilityMode(self, mode):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMreNq(upcastSelf.this, mode)
        return returnValue

    
    def getVisibilityMode(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMta47(upcastSelf.this)
        return returnValue

    
    def setDrawOrder(self, order):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOM1SSq(upcastSelf.this, order)
        return returnValue

    
    def getDrawOrder(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMY4RM(upcastSelf.this)
        return returnValue

    
    def hasDrawOrder(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMV5rc(upcastSelf.this)
        return returnValue

    
    def clearDrawOrder(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMgDCN(upcastSelf.this)
        return returnValue

    
    def setBin(self, bin):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMOpBx(upcastSelf.this, bin)
        return returnValue

    
    def getBin(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMtssd(upcastSelf.this)
        return returnValue

    
    def hasBin(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOM6rGu(upcastSelf.this)
        return returnValue

    
    def clearBin(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMlrzU(upcastSelf.this)
        return returnValue

    
    def eq(self, other):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMpyzm(upcastSelf.this, other.this)
        return returnValue

    
    def ne(self, other):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMV_Rm(upcastSelf.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMT1ZU(upcastSelf.this, other.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._EggTexture__overloaded_constructor_ptrConstEggTexture(*_args)
        elif numArgs == 2:
            return self._EggTexture__overloaded_constructor_atomicstring_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


