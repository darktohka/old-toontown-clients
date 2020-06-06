# File: T (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import PandaNode
import TextEncoder

class TextNode(PandaNode.PandaNode, TextEncoder.TextEncoder, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    ALeft = 0
    ARight = 1
    ACenter = 2
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self, name):
        self.this = libpanda._inPmUk_yTrj(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPmUk_EIWc:
            libpanda._inPmUk_EIWc(self.this)
        

    
    def setDefaultFont(parameter0):
        returnValue = libpanda._inPmUk_EY2O(parameter0.this)
        return returnValue

    setDefaultFont = staticmethod(setDefaultFont)
    
    def getDefaultFont():
        returnValue = libpanda._inPmUk_2rqi()
        import TextFont
        returnObject = TextFont.TextFont(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    getDefaultFont = staticmethod(getDefaultFont)
    
    def getClassType():
        returnValue = libpanda._inPmUk_yuS_()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def freeze(self):
        returnValue = libpanda._inPmUk_m2UZ(self.this)
        return returnValue

    
    def thaw(self):
        returnValue = libpanda._inPmUk_zyyW(self.this)
        return returnValue

    
    def setFont(self, font):
        returnValue = libpanda._inPmUk_GF3a(self.this, font.this)
        return returnValue

    
    def getFont(self):
        returnValue = libpanda._inPmUk_PzPi(self.this)
        import TextFont
        returnObject = TextFont.TextFont(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getLineHeight(self):
        returnValue = libpanda._inPmUk_74_2(self.this)
        return returnValue

    
    def setSmallCaps(self, smallCaps):
        returnValue = libpanda._inPmUk__Vg7(self.this, smallCaps)
        return returnValue

    
    def getSmallCaps(self):
        returnValue = libpanda._inPmUk_1K_b(self.this)
        return returnValue

    
    def setSmallCapsScale(self, smallCapsScale):
        returnValue = libpanda._inPmUk_UbUd(self.this, smallCapsScale)
        return returnValue

    
    def getSmallCapsScale(self):
        returnValue = libpanda._inPmUk_dTjF(self.this)
        return returnValue

    
    def setSlant(self, slant):
        returnValue = libpanda._inPmUk_a_en(self.this, slant)
        return returnValue

    
    def getSlant(self):
        returnValue = libpanda._inPmUk_Y44S(self.this)
        return returnValue

    
    def setAlign(self, alignType):
        returnValue = libpanda._inPmUk_S_68(self.this, alignType)
        return returnValue

    
    def getAlign(self):
        returnValue = libpanda._inPmUk_FwVq(self.this)
        return returnValue

    
    def setWordwrap(self, width):
        returnValue = libpanda._inPmUk_8HMt(self.this, width)
        return returnValue

    
    def clearWordwrap(self):
        returnValue = libpanda._inPmUk_eZHt(self.this)
        return returnValue

    
    def hasWordwrap(self):
        returnValue = libpanda._inPmUk_wjU_(self.this)
        return returnValue

    
    def getWordwrap(self):
        returnValue = libpanda._inPmUk_dsHW(self.this)
        return returnValue

    
    def _TextNode__overloaded_setTextColor_ptrTextNode_ptrConstLVecBase4f(self, textColor):
        returnValue = libpanda._inPmUk__L_O(self.this, textColor.this)
        return returnValue

    
    def _TextNode__overloaded_setTextColor_ptrTextNode_float_float_float_float(self, r, g, b, a):
        returnValue = libpanda._inPmUk_IuGX(self.this, r, g, b, a)
        return returnValue

    
    def clearTextColor(self):
        returnValue = libpanda._inPmUk_rIpB(self.this)
        return returnValue

    
    def hasTextColor(self):
        returnValue = libpanda._inPmUk_lsqS(self.this)
        return returnValue

    
    def getTextColor(self):
        returnValue = libpanda._inPmUk_Psdq(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _TextNode__overloaded_setFrameColor_ptrTextNode_ptrConstLVecBase4f(self, frameColor):
        returnValue = libpanda._inPmUk_E8Bv(self.this, frameColor.this)
        return returnValue

    
    def _TextNode__overloaded_setFrameColor_ptrTextNode_float_float_float_float(self, r, g, b, a):
        returnValue = libpanda._inPmUk_VbTz(self.this, r, g, b, a)
        return returnValue

    
    def getFrameColor(self):
        returnValue = libpanda._inPmUk_jap6(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setCardBorder(self, size, uvPortion):
        returnValue = libpanda._inPmUk_BoPk(self.this, size, uvPortion)
        return returnValue

    
    def clearCardBorder(self):
        returnValue = libpanda._inPmUk_3G6F(self.this)
        return returnValue

    
    def getCardBorderSize(self):
        returnValue = libpanda._inPmUk_qI81(self.this)
        return returnValue

    
    def getCardBorderUvPortion(self):
        returnValue = libpanda._inPmUk_0YDM(self.this)
        return returnValue

    
    def hasCardBorder(self):
        returnValue = libpanda._inPmUk_wHvs(self.this)
        return returnValue

    
    def _TextNode__overloaded_setCardColor_ptrTextNode_ptrConstLVecBase4f(self, cardColor):
        returnValue = libpanda._inPmUk_wpf9(self.this, cardColor.this)
        return returnValue

    
    def _TextNode__overloaded_setCardColor_ptrTextNode_float_float_float_float(self, r, g, b, a):
        returnValue = libpanda._inPmUk__JmF(self.this, r, g, b, a)
        return returnValue

    
    def getCardColor(self):
        returnValue = libpanda._inPmUk_JA_Y(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setCardTexture(self, cardTexture):
        returnValue = libpanda._inPmUk_gpTx(self.this, cardTexture.this)
        return returnValue

    
    def clearCardTexture(self):
        returnValue = libpanda._inPmUk_yHSq(self.this)
        return returnValue

    
    def hasCardTexture(self):
        returnValue = libpanda._inPmUk_6f88(self.this)
        return returnValue

    
    def getCardTexture(self):
        returnValue = libpanda._inPmUk_pfvU(self.this)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _TextNode__overloaded_setShadowColor_ptrTextNode_ptrConstLVecBase4f(self, shadowColor):
        returnValue = libpanda._inPmUk_NFJk(self.this, shadowColor.this)
        return returnValue

    
    def _TextNode__overloaded_setShadowColor_ptrTextNode_float_float_float_float(self, r, g, b, a):
        returnValue = libpanda._inPmUk_xKru(self.this, r, g, b, a)
        return returnValue

    
    def getShadowColor(self):
        returnValue = libpanda._inPmUk_0Suz(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setFrameAsMargin(self, left, right, bottom, top):
        returnValue = libpanda._inPmUk_fW_a(self.this, left, right, bottom, top)
        return returnValue

    
    def setFrameActual(self, left, right, bottom, top):
        returnValue = libpanda._inPmUk_7_wM(self.this, left, right, bottom, top)
        return returnValue

    
    def clearFrame(self):
        returnValue = libpanda._inPmUk_vtht(self.this)
        return returnValue

    
    def hasFrame(self):
        returnValue = libpanda._inPmUk_4KuG(self.this)
        return returnValue

    
    def isFrameAsMargin(self):
        returnValue = libpanda._inPmUk_8doH(self.this)
        return returnValue

    
    def getFrameAsSet(self):
        returnValue = libpanda._inPmUk_MXz1(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getFrameActual(self):
        returnValue = libpanda._inPmUk_Ma1R(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setFrameLineWidth(self, lineWidth):
        returnValue = libpanda._inPmUk_lIlf(self.this, lineWidth)
        return returnValue

    
    def getFrameLineWidth(self):
        returnValue = libpanda._inPmUk_M20H(self.this)
        return returnValue

    
    def setFrameCorners(self, corners):
        returnValue = libpanda._inPmUk_kMsJ(self.this, corners)
        return returnValue

    
    def getFrameCorners(self):
        returnValue = libpanda._inPmUk_tWF6(self.this)
        return returnValue

    
    def setCardAsMargin(self, left, right, bottom, top):
        returnValue = libpanda._inPmUk_s1zs(self.this, left, right, bottom, top)
        return returnValue

    
    def setCardActual(self, left, right, bottom, top):
        returnValue = libpanda._inPmUk_RVW0(self.this, left, right, bottom, top)
        return returnValue

    
    def clearCard(self):
        returnValue = libpanda._inPmUk_92SD(self.this)
        return returnValue

    
    def hasCard(self):
        returnValue = libpanda._inPmUk_tTVI(self.this)
        return returnValue

    
    def isCardAsMargin(self):
        returnValue = libpanda._inPmUk__1k2(self.this)
        return returnValue

    
    def getCardAsSet(self):
        returnValue = libpanda._inPmUk_Po16(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getCardActual(self):
        returnValue = libpanda._inPmUk_jvt7(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getCardTransformed(self):
        returnValue = libpanda._inPmUk___32(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setShadow(self, xoffset, yoffset):
        returnValue = libpanda._inPmUk_HBV_(self.this, xoffset, yoffset)
        return returnValue

    
    def clearShadow(self):
        returnValue = libpanda._inPmUk_6Hq_(self.this)
        return returnValue

    
    def hasShadow(self):
        returnValue = libpanda._inPmUk_diOX(self.this)
        return returnValue

    
    def getShadow(self):
        returnValue = libpanda._inPmUk_7iBv(self.this)
        import VBase2
        returnObject = VBase2.VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setBin(self, bin):
        returnValue = libpanda._inPmUk_Hgph(self.this, bin)
        return returnValue

    
    def clearBin(self):
        returnValue = libpanda._inPmUk_sUkz(self.this)
        return returnValue

    
    def hasBin(self):
        returnValue = libpanda._inPmUk_QMNg(self.this)
        return returnValue

    
    def getBin(self):
        returnValue = libpanda._inPmUk_tPA4(self.this)
        return returnValue

    
    def setDrawOrder(self, drawOrder):
        returnValue = libpanda._inPmUk_QbS_(self.this, drawOrder)
        return returnValue

    
    def getDrawOrder(self):
        returnValue = libpanda._inPmUk_2mSP(self.this)
        return returnValue

    
    def setTransform(self, transform):
        returnValue = libpanda._inPmUk_PbTJ(self.this, transform.this)
        return returnValue

    
    def getTransform(self):
        returnValue = libpanda._inPmUk_ot_Q(self.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setCoordinateSystem(self, cs):
        returnValue = libpanda._inPmUk_q9jN(self.this, cs)
        return returnValue

    
    def getCoordinateSystem(self):
        returnValue = libpanda._inPmUk_8bzG(self.this)
        return returnValue

    
    def _TextNode__overloaded_setText_ptrTextNode_atomicstring(self, text):
        returnValue = libpanda._inPmUk_hRrL(self.this, text)
        return returnValue

    
    def _TextNode__overloaded_setText_ptrTextNode_atomicstring___enum__Encoding(self, text, encoding):
        returnValue = libpanda._inPmUk_0t8R(self.this, text, encoding)
        return returnValue

    
    def clearText(self):
        returnValue = libpanda._inPmUk_FxTx(self.this)
        return returnValue

    
    def appendText(self, text):
        returnValue = libpanda._inPmUk_p36A(self.this, text)
        return returnValue

    
    def appendUnicodeChar(self, character):
        returnValue = libpanda._inPmUk_A42h(self.this, character)
        return returnValue

    
    def _TextNode__overloaded_calcWidth_ptrConstTextNode_atomicstring(self, line):
        returnValue = libpanda._inPmUk_33Il(self.this, line)
        return returnValue

    
    def _TextNode__overloaded_calcWidth_ptrConstTextNode_int(self, character):
        returnValue = libpanda._inPmUk_mWg7(self.this, character)
        return returnValue

    
    def wordwrapTo(self, text, wordwrapWidth, preserveTrailingWhitespace):
        returnValue = libpanda._inPmUk_Fvwk(self.this, text, wordwrapWidth, preserveTrailingWhitespace)
        return returnValue

    
    def _TextNode__overloaded_write_ptrConstTextNode_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPmUk_JFnr(self.this, out.this, indentLevel)
        return returnValue

    
    def _TextNode__overloaded_write_ptrConstTextNode_ptrOstream(self, out):
        returnValue = libpanda._inPmUk_dm6v(self.this, out.this)
        return returnValue

    
    def getLeft(self):
        returnValue = libpanda._inPmUk_UosZ(self.this)
        return returnValue

    
    def getRight(self):
        returnValue = libpanda._inPmUk_AxZW(self.this)
        return returnValue

    
    def getBottom(self):
        returnValue = libpanda._inPmUk_rsLg(self.this)
        return returnValue

    
    def getTop(self):
        returnValue = libpanda._inPmUk_C4yi(self.this)
        return returnValue

    
    def getHeight(self):
        returnValue = libpanda._inPmUk_pjNJ(self.this)
        return returnValue

    
    def getWidth(self):
        returnValue = libpanda._inPmUk_X_Z2(self.this)
        return returnValue

    
    def getUpperLeft3d(self):
        returnValue = libpanda._inPmUk_ObuQ(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getLowerRight3d(self):
        returnValue = libpanda._inPmUk_00ox(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getNumRows(self):
        returnValue = libpanda._inPmUk_5Pci(self.this)
        return returnValue

    
    def generate(self):
        returnValue = libpanda._inPmUk_fMjA(self.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def update(self):
        returnValue = libpanda._inPmUk_g9eZ(self.this)
        return returnValue

    
    def forceUpdate(self):
        returnValue = libpanda._inPmUk_Z_1G(self.this)
        return returnValue

    
    def upcastToTextEncoder(self):
        returnValue = libpanda._inPmUk_2clc(self.this)
        import TextEncoder
        returnObject = TextEncoder.TextEncoder(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def copySubgraph(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyoGYnx(upcastSelf.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNumParents(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyoI9bH(upcastSelf.this)
        return returnValue

    
    def getParent(self, n):
        upcastSelf = self
        returnValue = libpanda._inPkJyoh0xF(upcastSelf.this, n)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def findParent(self, node):
        upcastSelf = self
        returnValue = libpanda._inPkJyoNWG_(upcastSelf.this, node.this)
        return returnValue

    
    def getNumChildren(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyo68Bo(upcastSelf.this)
        return returnValue

    
    def getChild(self, n):
        upcastSelf = self
        returnValue = libpanda._inPkJyonZg9(upcastSelf.this, n)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getChildSort(self, n):
        upcastSelf = self
        returnValue = libpanda._inPkJyoMzeG(upcastSelf.this, n)
        return returnValue

    
    def findChild(self, node):
        upcastSelf = self
        returnValue = libpanda._inPkJyoKHuN(upcastSelf.this, node.this)
        return returnValue

    
    def _TextNode__overloaded_addChild_ptrPandaNode_ptrPandaNode_int(self, childNode, sort):
        upcastSelf = self
        returnValue = libpanda._inPkJyoA9tQ(upcastSelf.this, childNode.this, sort)
        return returnValue

    
    def _TextNode__overloaded_addChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        returnValue = libpanda._inPkJyo37ri(upcastSelf.this, childNode.this)
        return returnValue

    
    def _TextNode__overloaded_removeChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        returnValue = libpanda._inPkJyozFZb(upcastSelf.this, childNode.this)
        return returnValue

    
    def _TextNode__overloaded_removeChild_ptrPandaNode_int(self, n):
        upcastSelf = self
        returnValue = libpanda._inPkJyoCqN1(upcastSelf.this, n)
        return returnValue

    
    def replaceChild(self, origChild, newChild):
        upcastSelf = self
        returnValue = libpanda._inPkJyogW5Y(upcastSelf.this, origChild.this, newChild.this)
        return returnValue

    
    def _TextNode__overloaded_stashChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        returnValue = libpanda._inPkJyokC1w(upcastSelf.this, childNode.this)
        return returnValue

    
    def _TextNode__overloaded_stashChild_ptrPandaNode_int(self, childIndex):
        upcastSelf = self
        returnValue = libpanda._inPkJyoqWqz(upcastSelf.this, childIndex)
        return returnValue

    
    def _TextNode__overloaded_unstashChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        returnValue = libpanda._inPkJyoqJGM(upcastSelf.this, childNode.this)
        return returnValue

    
    def _TextNode__overloaded_unstashChild_ptrPandaNode_int(self, stashedIndex):
        upcastSelf = self
        returnValue = libpanda._inPkJyoeWxF(upcastSelf.this, stashedIndex)
        return returnValue

    
    def getNumStashed(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyoPR8_(upcastSelf.this)
        return returnValue

    
    def getStashed(self, n):
        upcastSelf = self
        returnValue = libpanda._inPkJyol8qw(upcastSelf.this, n)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getStashedSort(self, n):
        upcastSelf = self
        returnValue = libpanda._inPkJyoE1FX(upcastSelf.this, n)
        return returnValue

    
    def findStashed(self, node):
        upcastSelf = self
        returnValue = libpanda._inPkJyoyw9C(upcastSelf.this, node.this)
        return returnValue

    
    def _TextNode__overloaded_addStashed_ptrPandaNode_ptrPandaNode_int(self, childNode, sort):
        upcastSelf = self
        returnValue = libpanda._inPkJyoQQ0n(upcastSelf.this, childNode.this, sort)
        return returnValue

    
    def _TextNode__overloaded_addStashed_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        returnValue = libpanda._inPkJyoswLI(upcastSelf.this, childNode.this)
        return returnValue

    
    def removeStashed(self, n):
        upcastSelf = self
        returnValue = libpanda._inPkJyoYHe7(upcastSelf.this, n)
        return returnValue

    
    def removeAllChildren(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyoayap(upcastSelf.this)
        return returnValue

    
    def stealChildren(self, other):
        upcastSelf = self
        returnValue = libpanda._inPkJyoignr(upcastSelf.this, other.this)
        return returnValue

    
    def copyChildren(self, other):
        upcastSelf = self
        returnValue = libpanda._inPkJyohfED(upcastSelf.this, other.this)
        return returnValue

    
    def _TextNode__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib_int(self, attrib, override):
        upcastSelf = self
        returnValue = libpanda._inPkJyo48Bd(upcastSelf.this, attrib.this, override)
        return returnValue

    
    def _TextNode__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib(self, attrib):
        upcastSelf = self
        returnValue = libpanda._inPkJyoAD5k(upcastSelf.this, attrib.this)
        return returnValue

    
    def getAttrib(self, type):
        upcastSelf = self
        returnValue = libpanda._inPkJyoaDfJ(upcastSelf.this, type.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def hasAttrib(self, type):
        upcastSelf = self
        returnValue = libpanda._inPkJyo2W_P(upcastSelf.this, type.this)
        return returnValue

    
    def clearAttrib(self, type):
        upcastSelf = self
        returnValue = libpanda._inPkJyoCSEu(upcastSelf.this, type.this)
        return returnValue

    
    def setEffect(self, effect):
        upcastSelf = self
        returnValue = libpanda._inPkJyoKWvI(upcastSelf.this, effect.this)
        return returnValue

    
    def getEffect(self, type):
        upcastSelf = self
        returnValue = libpanda._inPkJyo17Hl(upcastSelf.this, type.this)
        import RenderEffect
        returnObject = RenderEffect.RenderEffect(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def hasEffect(self, type):
        upcastSelf = self
        returnValue = libpanda._inPkJyoJ1nr(upcastSelf.this, type.this)
        return returnValue

    
    def clearEffect(self, type):
        upcastSelf = self
        returnValue = libpanda._inPkJyoOUJ2(upcastSelf.this, type.this)
        return returnValue

    
    def setState(self, state):
        upcastSelf = self
        returnValue = libpanda._inPkJyoGDjV(upcastSelf.this, state.this)
        return returnValue

    
    def getState(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyoIocj(upcastSelf.this)
        import RenderState
        returnObject = RenderState.RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def clearState(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyotySF(upcastSelf.this)
        return returnValue

    
    def setEffects(self, effects):
        upcastSelf = self
        returnValue = libpanda._inPkJyo2lpj(upcastSelf.this, effects.this)
        return returnValue

    
    def getEffects(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyo1WLf(upcastSelf.this)
        import RenderEffects
        returnObject = RenderEffects.RenderEffects(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def clearEffects(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyo6yPH(upcastSelf.this)
        return returnValue

    
    def clearTransform(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyoHjK_(upcastSelf.this)
        return returnValue

    
    def setDrawMask(self, mask):
        upcastSelf = self
        returnValue = libpanda._inPkJyoSSGr(upcastSelf.this, mask.this)
        return returnValue

    
    def getDrawMask(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyoWJXI(upcastSelf.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getNetCollideMask(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyo4l_T(upcastSelf.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def output(self, out):
        upcastSelf = self
        returnValue = libpanda._inPkJyoW23T(upcastSelf.this, out.this)
        return returnValue

    
    def ls(self, out, indentLevel):
        upcastSelf = self
        returnValue = libpanda._inPkJyouBSg(upcastSelf.this, out.this, indentLevel)
        return returnValue

    
    def _TextNode__overloaded_setBound_ptrPandaNode___enum__BoundingVolumeType(self, type):
        upcastSelf = self
        returnValue = libpanda._inPkJyond5g(upcastSelf.this, type)
        return returnValue

    
    def _TextNode__overloaded_setBound_ptrPandaNode_ptrConstBoundingVolume(self, volume):
        upcastSelf = self
        returnValue = libpanda._inPkJyo7Bq1(upcastSelf.this, volume.this)
        return returnValue

    
    def getBound(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyohf0y(upcastSelf.this)
        import BoundingVolume
        returnObject = BoundingVolume.BoundingVolume(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getInternalBound(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyoI_J4(upcastSelf.this)
        import BoundingVolume
        returnObject = BoundingVolume.BoundingVolume(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setBound(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import BoundingVolume
            if isinstance(_args[0], types.IntType):
                return self._TextNode__overloaded_setBound_ptrPandaNode___enum__BoundingVolumeType(_args[0])
            elif isinstance(_args[0], BoundingVolume.BoundingVolume):
                return self._TextNode__overloaded_setBound_ptrPandaNode_ptrConstBoundingVolume(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <BoundingVolume.BoundingVolume> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                return self._TextNode__overloaded_addChild_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PandaNode.PandaNode> '
        elif numArgs == 2:
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                if isinstance(_args[1], types.IntType):
                    return self._TextNode__overloaded_addChild_ptrPandaNode_ptrPandaNode_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def unstashChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            if isinstance(_args[0], types.IntType):
                return self._TextNode__overloaded_unstashChild_ptrPandaNode_int(_args[0])
            elif isinstance(_args[0], PandaNode.PandaNode):
                return self._TextNode__overloaded_unstashChild_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addStashed(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                return self._TextNode__overloaded_addStashed_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PandaNode.PandaNode> '
        elif numArgs == 2:
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                if isinstance(_args[1], types.IntType):
                    return self._TextNode__overloaded_addStashed_ptrPandaNode_ptrPandaNode_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def removeChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            if isinstance(_args[0], types.IntType):
                return self._TextNode__overloaded_removeChild_ptrPandaNode_int(_args[0])
            elif isinstance(_args[0], PandaNode.PandaNode):
                return self._TextNode__overloaded_removeChild_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def stashChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            if isinstance(_args[0], types.IntType):
                return self._TextNode__overloaded_stashChild_ptrPandaNode_int(_args[0])
            elif isinstance(_args[0], PandaNode.PandaNode):
                return self._TextNode__overloaded_stashChild_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def setAttrib(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import RenderAttrib
            if isinstance(_args[0], RenderAttrib.RenderAttrib):
                return self._TextNode__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <RenderAttrib.RenderAttrib> '
        elif numArgs == 2:
            import RenderAttrib
            if isinstance(_args[0], RenderAttrib.RenderAttrib):
                if isinstance(_args[1], types.IntType):
                    return self._TextNode__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <RenderAttrib.RenderAttrib> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def upcastToNamable(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyojprb(upcastSelf.this)
        import Namable
        returnObject = Namable.Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToBoundedObject(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyo8YS5(upcastSelf.this)
        import BoundedObject
        returnObject = BoundedObject.BoundedObject(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToReferenceCount(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyogdrc(upcastSelf.this)
        import ReferenceCount
        returnObject = ReferenceCount.ReferenceCount(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getType(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPJoxt1uxI(upcastSelf.this)
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getTypeIndex(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPJoxtm7AU(upcastSelf.this)
        return returnValue

    
    def isOfType(self, handle):
        upcastSelf = self
        returnValue = libpandaexpress._inPJoxtmFKt(upcastSelf.this, handle.this)
        return returnValue

    
    def isExactType(self, handle):
        upcastSelf = self
        returnValue = libpandaexpress._inPJoxtkXzz(upcastSelf.this, handle.this)
        return returnValue

    
    def assign(self, other):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtp1bI(upcastSelf.this, other.this)
        import Namable
        returnObject = Namable.Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setName(self, name):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtLNBW(upcastSelf.this, name)
        return returnValue

    
    def clearName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtavUl(upcastSelf.this)
        return returnValue

    
    def hasName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtYjhC(upcastSelf.this)
        return returnValue

    
    def getName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtfARN(upcastSelf.this)
        return returnValue

    
    def output(self, out):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtvz7q(upcastSelf.this, out.this)
        return returnValue

    
    def _TextNode__overloaded_setBound_ptrBoundedObject___enum__BoundingVolumeType(self, type):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPC76J(upcastSelf.this, type)
        return returnValue

    
    def _TextNode__overloaded_setBound_ptrBoundedObject_ptrConstBoundingVolume(self, volume):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPXVRr(upcastSelf.this, volume.this)
        return returnValue

    
    def getBound(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPtOIb(upcastSelf.this)
        import BoundingVolume
        returnObject = BoundingVolume.BoundingVolume(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def markBoundStale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPG4uI(upcastSelf.this)
        return returnValue

    
    def forceBoundStale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPi1Pw(upcastSelf.this)
        return returnValue

    
    def isBoundStale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPjac5(upcastSelf.this)
        return returnValue

    
    def setFinal(self, flag):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPy9vH(upcastSelf.this, flag)
        return returnValue

    
    def isFinal(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPUuL4(upcastSelf.this)
        return returnValue

    
    def setBound(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import BoundingVolume
            if isinstance(_args[0], types.IntType):
                return self._TextNode__overloaded_setBound_ptrBoundedObject___enum__BoundingVolumeType(_args[0])
            elif isinstance(_args[0], BoundingVolume.BoundingVolume):
                return self._TextNode__overloaded_setBound_ptrBoundedObject_ptrConstBoundingVolume(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <BoundingVolume.BoundingVolume> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def getRefCount(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtM11_(upcastSelf.this)
        return returnValue

    
    def ref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtVS5_(upcastSelf.this)
        return returnValue

    
    def unref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtzyVy(upcastSelf.this)
        return returnValue

    
    def testRefCountIntegrity(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtupj2(upcastSelf.this)
        return returnValue

    
    def setEncoding(self, encoding):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPJoxtrlQJ(upcastSelf.this, encoding)
        return returnValue

    
    def getEncoding(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPJoxtLWo7(upcastSelf.this)
        return returnValue

    
    def hasText(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPJoxt_7oh(upcastSelf.this)
        return returnValue

    
    def makeUpper(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPJoxtlMP7(upcastSelf.this)
        return returnValue

    
    def makeLower(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPJoxtT0Ve(upcastSelf.this)
        return returnValue

    
    def _TextNode__overloaded_getText_ptrConstTextEncoder(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPJoxtp9Te(upcastSelf.this)
        return returnValue

    
    def _TextNode__overloaded_getText_ptrConstTextEncoder___enum__Encoding(self, encoding):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPJoxtGTNv(upcastSelf.this, encoding)
        return returnValue

    
    def getNumChars(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPJoxt4x3n(upcastSelf.this)
        return returnValue

    
    def getUnicodeChar(self, index):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPJoxtkULv(upcastSelf.this, index)
        return returnValue

    
    def setUnicodeChar(self, index, character):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPJoxtTkrk(upcastSelf.this, index, character)
        return returnValue

    
    def _TextNode__overloaded_getEncodedChar_ptrConstTextEncoder_int(self, index):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPJoxtPGUu(upcastSelf.this, index)
        return returnValue

    
    def _TextNode__overloaded_getEncodedChar_ptrConstTextEncoder_int___enum__Encoding(self, index, encoding):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPJoxtKIi_(upcastSelf.this, index, encoding)
        return returnValue

    
    def getTextAsAscii(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPJoxtzcrI(upcastSelf.this)
        return returnValue

    
    def getEncodedChar(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._TextNode__overloaded_getEncodedChar_ptrConstTextEncoder_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.IntType):
                    return self._TextNode__overloaded_getEncodedChar_ptrConstTextEncoder_int___enum__Encoding(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getText(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._TextNode__overloaded_getText_ptrConstTextEncoder()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._TextNode__overloaded_getText_ptrConstTextEncoder___enum__Encoding(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._TextNode__overloaded_write_ptrConstTextNode_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._TextNode__overloaded_write_ptrConstTextNode_ptrOstream_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def calcWidth(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._TextNode__overloaded_calcWidth_ptrConstTextNode_int(_args[0])
            elif isinstance(_args[0], types.StringType):
                return self._TextNode__overloaded_calcWidth_ptrConstTextNode_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def setShadowColor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase4
            if isinstance(_args[0], VBase4.VBase4):
                return self._TextNode__overloaded_setShadowColor_ptrTextNode_ptrConstLVecBase4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
        elif numArgs == 4:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._TextNode__overloaded_setShadowColor_ptrTextNode_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 4 '

    
    def setText(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._TextNode__overloaded_setText_ptrTextNode_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    return self._TextNode__overloaded_setText_ptrTextNode_atomicstring___enum__Encoding(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setCardColor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase4
            if isinstance(_args[0], VBase4.VBase4):
                return self._TextNode__overloaded_setCardColor_ptrTextNode_ptrConstLVecBase4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
        elif numArgs == 4:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._TextNode__overloaded_setCardColor_ptrTextNode_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 4 '

    
    def setFrameColor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase4
            if isinstance(_args[0], VBase4.VBase4):
                return self._TextNode__overloaded_setFrameColor_ptrTextNode_ptrConstLVecBase4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
        elif numArgs == 4:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._TextNode__overloaded_setFrameColor_ptrTextNode_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 4 '

    
    def setTextColor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase4
            if isinstance(_args[0], VBase4.VBase4):
                return self._TextNode__overloaded_setTextColor_ptrTextNode_ptrConstLVecBase4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
        elif numArgs == 4:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._TextNode__overloaded_setTextColor_ptrTextNode_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 4 '


