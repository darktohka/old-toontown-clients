# File: T (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import PandaNode
import TextEncoder
import TextProperties

class TextNode(PandaNode.PandaNode, TextEncoder.TextEncoder, TextProperties.TextProperties, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _TextNode__overloaded_constructor_atomicstring(self, name):
        self.this = libpanda._inPpUk_xTrj(name)
        self.userManagesMemory = 1

    
    def _TextNode__overloaded_constructor_atomicstring_ptrConstTextProperties(self, name, copy):
        self.this = libpanda._inPpUk_NhOQ(name, copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPpUk_EIWc:
            libpanda._inPpUk_EIWc(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPpUk_xuS_()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getLineHeight(self):
        returnValue = libpanda._inPpUk_64_2(self.this)
        return returnValue

    
    def setMaxRows(self, maxRows):
        returnValue = libpanda._inPpUk_gyMC(self.this, maxRows)
        return returnValue

    
    def clearMaxRows(self):
        returnValue = libpanda._inPpUk_Iv_f(self.this)
        return returnValue

    
    def hasMaxRows(self):
        returnValue = libpanda._inPpUk_afTN(self.this)
        return returnValue

    
    def getMaxRows(self):
        returnValue = libpanda._inPpUk__cGl(self.this)
        return returnValue

    
    def hasOverflow(self):
        returnValue = libpanda._inPpUk_P7gc(self.this)
        return returnValue

    
    def _TextNode__overloaded_setFrameColor_ptrTextNode_ptrConstLVecBase4f(self, frameColor):
        returnValue = libpanda._inPpUk_F8Bv(self.this, frameColor.this)
        return returnValue

    
    def _TextNode__overloaded_setFrameColor_ptrTextNode_float_float_float_float(self, r, g, b, a):
        returnValue = libpanda._inPpUk_UbTz(self.this, r, g, b, a)
        return returnValue

    
    def getFrameColor(self):
        returnValue = libpanda._inPpUk_gap6(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setCardBorder(self, size, uvPortion):
        returnValue = libpanda._inPpUk_AoPk(self.this, size, uvPortion)
        return returnValue

    
    def clearCardBorder(self):
        returnValue = libpanda._inPpUk_3G6F(self.this)
        return returnValue

    
    def getCardBorderSize(self):
        returnValue = libpanda._inPpUk_rI81(self.this)
        return returnValue

    
    def getCardBorderUvPortion(self):
        returnValue = libpanda._inPpUk_0YDM(self.this)
        return returnValue

    
    def hasCardBorder(self):
        returnValue = libpanda._inPpUk__Hvs(self.this)
        return returnValue

    
    def _TextNode__overloaded_setCardColor_ptrTextNode_ptrConstLVecBase4f(self, cardColor):
        returnValue = libpanda._inPpUk_zpf9(self.this, cardColor.this)
        return returnValue

    
    def _TextNode__overloaded_setCardColor_ptrTextNode_float_float_float_float(self, r, g, b, a):
        returnValue = libpanda._inPpUk__JmF(self.this, r, g, b, a)
        return returnValue

    
    def getCardColor(self):
        returnValue = libpanda._inPpUk_JA_Y(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setCardTexture(self, cardTexture):
        returnValue = libpanda._inPpUk_hpTx(self.this, cardTexture.this)
        return returnValue

    
    def clearCardTexture(self):
        returnValue = libpanda._inPpUk_zHSq(self.this)
        return returnValue

    
    def hasCardTexture(self):
        returnValue = libpanda._inPpUk_7f88(self.this)
        return returnValue

    
    def getCardTexture(self):
        returnValue = libpanda._inPpUk_pfvU(self.this)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setFrameAsMargin(self, left, right, bottom, top):
        returnValue = libpanda._inPpUk_fW_a(self.this, left, right, bottom, top)
        return returnValue

    
    def setFrameActual(self, left, right, bottom, top):
        returnValue = libpanda._inPpUk_7_wM(self.this, left, right, bottom, top)
        return returnValue

    
    def clearFrame(self):
        returnValue = libpanda._inPpUk_utht(self.this)
        return returnValue

    
    def hasFrame(self):
        returnValue = libpanda._inPpUk_4KuG(self.this)
        return returnValue

    
    def isFrameAsMargin(self):
        returnValue = libpanda._inPpUk_8doH(self.this)
        return returnValue

    
    def getFrameAsSet(self):
        returnValue = libpanda._inPpUk_LXz1(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getFrameActual(self):
        returnValue = libpanda._inPpUk_Ma1R(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setFrameLineWidth(self, lineWidth):
        returnValue = libpanda._inPpUk_lIlf(self.this, lineWidth)
        return returnValue

    
    def getFrameLineWidth(self):
        returnValue = libpanda._inPpUk_M20H(self.this)
        return returnValue

    
    def setFrameCorners(self, corners):
        returnValue = libpanda._inPpUk_kMsJ(self.this, corners)
        return returnValue

    
    def getFrameCorners(self):
        returnValue = libpanda._inPpUk_sWF6(self.this)
        return returnValue

    
    def setCardAsMargin(self, left, right, bottom, top):
        returnValue = libpanda._inPpUk_r1zs(self.this, left, right, bottom, top)
        return returnValue

    
    def setCardActual(self, left, right, bottom, top):
        returnValue = libpanda._inPpUk_QVW0(self.this, left, right, bottom, top)
        return returnValue

    
    def clearCard(self):
        returnValue = libpanda._inPpUk_92SD(self.this)
        return returnValue

    
    def hasCard(self):
        returnValue = libpanda._inPpUk_tTVI(self.this)
        return returnValue

    
    def isCardAsMargin(self):
        returnValue = libpanda._inPpUk__1k2(self.this)
        return returnValue

    
    def getCardAsSet(self):
        returnValue = libpanda._inPpUk_Io16(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getCardActual(self):
        returnValue = libpanda._inPpUk_svt7(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getCardTransformed(self):
        returnValue = libpanda._inPpUk___32(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setTransform(self, transform):
        returnValue = libpanda._inPpUk_PbTJ(self.this, transform.this)
        return returnValue

    
    def getTransform(self):
        returnValue = libpanda._inPpUk_ot_Q(self.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setCoordinateSystem(self, cs):
        returnValue = libpanda._inPpUk_q9jN(self.this, cs)
        return returnValue

    
    def getCoordinateSystem(self):
        returnValue = libpanda._inPpUk_8bzG(self.this)
        return returnValue

    
    def setFont(self, font):
        returnValue = libpanda._inPpUk_GF3a(self.this, font.this)
        return returnValue

    
    def clearFont(self):
        returnValue = libpanda._inPpUk_f1JB(self.this)
        return returnValue

    
    def setSmallCaps(self, smallCaps):
        returnValue = libpanda._inPpUk__Vg7(self.this, smallCaps)
        return returnValue

    
    def clearSmallCaps(self):
        returnValue = libpanda._inPpUk_wdub(self.this)
        return returnValue

    
    def setSmallCapsScale(self, smallCapsScale):
        returnValue = libpanda._inPpUk_UbUd(self.this, smallCapsScale)
        return returnValue

    
    def clearSmallCapsScale(self):
        returnValue = libpanda._inPpUk_INuw(self.this)
        return returnValue

    
    def setSlant(self, slant):
        returnValue = libpanda._inPpUk_b_en(self.this, slant)
        return returnValue

    
    def clearSlant(self):
        returnValue = libpanda._inPpUk_SyQo(self.this)
        return returnValue

    
    def setAlign(self, alignType):
        returnValue = libpanda._inPpUk_LgJS(self.this, alignType)
        return returnValue

    
    def clearAlign(self):
        returnValue = libpanda._inPpUk_6Qem(self.this)
        return returnValue

    
    def setIndent(self, indent):
        returnValue = libpanda._inPpUk_QfWK(self.this, indent)
        return returnValue

    
    def clearIndent(self):
        returnValue = libpanda._inPpUk_mAkO(self.this)
        return returnValue

    
    def setWordwrap(self, wordwrap):
        returnValue = libpanda._inPpUk_9HMt(self.this, wordwrap)
        return returnValue

    
    def clearWordwrap(self):
        returnValue = libpanda._inPpUk_fZHt(self.this)
        return returnValue

    
    def _TextNode__overloaded_setTextColor_ptrTextNode_ptrConstLVecBase4f(self, textColor):
        returnValue = libpanda._inPpUk__L_O(self.this, textColor.this)
        return returnValue

    
    def _TextNode__overloaded_setTextColor_ptrTextNode_float_float_float_float(self, r, g, b, a):
        returnValue = libpanda._inPpUk_IuGX(self.this, r, g, b, a)
        return returnValue

    
    def clearTextColor(self):
        returnValue = libpanda._inPpUk_rIpB(self.this)
        return returnValue

    
    def _TextNode__overloaded_setShadowColor_ptrTextNode_ptrConstLVecBase4f(self, shadowColor):
        returnValue = libpanda._inPpUk_MFJk(self.this, shadowColor.this)
        return returnValue

    
    def _TextNode__overloaded_setShadowColor_ptrTextNode_float_float_float_float(self, r, g, b, a):
        returnValue = libpanda._inPpUk_wKru(self.this, r, g, b, a)
        return returnValue

    
    def clearShadowColor(self):
        returnValue = libpanda._inPpUk_y9rr(self.this)
        return returnValue

    
    def _TextNode__overloaded_setShadow_ptrTextNode_ptrConstLVecBase2f(self, shadowOffset):
        returnValue = libpanda._inPpUk_mLmp(self.this, shadowOffset.this)
        return returnValue

    
    def _TextNode__overloaded_setShadow_ptrTextNode_float_float(self, xoffset, yoffset):
        returnValue = libpanda._inPpUk_GBV_(self.this, xoffset, yoffset)
        return returnValue

    
    def clearShadow(self):
        returnValue = libpanda._inPpUk_7Hq_(self.this)
        return returnValue

    
    def setBin(self, bin):
        returnValue = libpanda._inPpUk_Ggph(self.this, bin)
        return returnValue

    
    def clearBin(self):
        returnValue = libpanda._inPpUk_vUkz(self.this)
        return returnValue

    
    def setDrawOrder(self, drawOrder):
        returnValue = libpanda._inPpUk_RbS_(self.this, drawOrder)
        return returnValue

    
    def clearDrawOrder(self):
        returnValue = libpanda._inPpUk_ejrP(self.this)
        return returnValue

    
    def setTabWidth(self, tabWidth):
        returnValue = libpanda._inPpUk_ZrKk(self.this, tabWidth)
        return returnValue

    
    def clearTabWidth(self):
        returnValue = libpanda._inPpUk_ELAu(self.this)
        return returnValue

    
    def setGlyphScale(self, glyphScale):
        returnValue = libpanda._inPpUk_gJjt(self.this, glyphScale)
        return returnValue

    
    def clearGlyphScale(self):
        returnValue = libpanda._inPpUk_Q6h8(self.this)
        return returnValue

    
    def setGlyphShift(self, glyphShift):
        returnValue = libpanda._inPpUk_6XIO(self.this, glyphShift)
        return returnValue

    
    def clearGlyphShift(self):
        returnValue = libpanda._inPpUk_a77j(self.this)
        return returnValue

    
    def _TextNode__overloaded_setText_ptrTextNode_atomicstring(self, text):
        returnValue = libpanda._inPpUk_hRrL(self.this, text)
        return returnValue

    
    def _TextNode__overloaded_setText_ptrTextNode_atomicstring___enum__Encoding(self, text, encoding):
        returnValue = libpanda._inPpUk_0t8R(self.this, text, encoding)
        return returnValue

    
    def clearText(self):
        returnValue = libpanda._inPpUk_ExTx(self.this)
        return returnValue

    
    def appendText(self, text):
        returnValue = libpanda._inPpUk_p36A(self.this, text)
        return returnValue

    
    def appendUnicodeChar(self, character):
        returnValue = libpanda._inPpUk_B42h(self.this, character)
        return returnValue

    
    def getWordwrappedText(self):
        returnValue = libpanda._inPpUk_wRGG(self.this)
        return returnValue

    
    def _TextNode__overloaded_calcWidth_ptrConstTextNode_atomicstring(self, line):
        returnValue = libpanda._inPpUk_03Il(self.this, line)
        return returnValue

    
    def _TextNode__overloaded_calcWidth_ptrConstTextNode_int(self, character):
        returnValue = libpanda._inPpUk_nWg7(self.this, character)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPpUk_mp7p(self.this, out.this)
        return returnValue

    
    def _TextNode__overloaded_write_ptrConstTextNode_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPpUk_IFnr(self.this, out.this, indentLevel)
        return returnValue

    
    def _TextNode__overloaded_write_ptrConstTextNode_ptrOstream(self, out):
        returnValue = libpanda._inPpUk_em6v(self.this, out.this)
        return returnValue

    
    def getLeft(self):
        returnValue = libpanda._inPpUk_UosZ(self.this)
        return returnValue

    
    def getRight(self):
        returnValue = libpanda._inPpUk_AxZW(self.this)
        return returnValue

    
    def getBottom(self):
        returnValue = libpanda._inPpUk_qsLg(self.this)
        return returnValue

    
    def getTop(self):
        returnValue = libpanda._inPpUk_D4yi(self.this)
        return returnValue

    
    def getHeight(self):
        returnValue = libpanda._inPpUk_pjNJ(self.this)
        return returnValue

    
    def getWidth(self):
        returnValue = libpanda._inPpUk_W_Z2(self.this)
        return returnValue

    
    def getUpperLeft3d(self):
        returnValue = libpanda._inPpUk_ObuQ(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getLowerRight3d(self):
        returnValue = libpanda._inPpUk_z0ox(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getNumRows(self):
        returnValue = libpanda._inPpUk_4Pci(self.this)
        return returnValue

    
    def generate(self):
        returnValue = libpanda._inPpUk_fMjA(self.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def update(self):
        returnValue = libpanda._inPpUk_g9eZ(self.this)
        return returnValue

    
    def forceUpdate(self):
        returnValue = libpanda._inPpUk_Z_1G(self.this)
        return returnValue

    
    def upcastToTextEncoder(self):
        returnValue = libpanda._inPpUk_2clc(self.this)
        import TextEncoder
        returnObject = TextEncoder.TextEncoder(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToTextProperties(self):
        returnValue = libpanda._inPpUk_rYU8(self.this)
        import TextProperties
        returnObject = TextProperties.TextProperties(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def copySubgraph(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyoFYnx(upcastSelf.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNumParents(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyoI9bH(upcastSelf.this)
        return returnValue

    
    def getParent(self, n):
        upcastSelf = self
        returnValue = libpanda._inPnJyoh0xF(upcastSelf.this, n)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def findParent(self, node):
        upcastSelf = self
        returnValue = libpanda._inPnJyoMWG_(upcastSelf.this, node.this)
        return returnValue

    
    def getNumChildren(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyo78Bo(upcastSelf.this)
        return returnValue

    
    def getChild(self, n):
        upcastSelf = self
        returnValue = libpanda._inPnJyokZg9(upcastSelf.this, n)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getChildSort(self, n):
        upcastSelf = self
        returnValue = libpanda._inPnJyoMzeG(upcastSelf.this, n)
        return returnValue

    
    def findChild(self, node):
        upcastSelf = self
        returnValue = libpanda._inPnJyoKHuN(upcastSelf.this, node.this)
        return returnValue

    
    def _TextNode__overloaded_addChild_ptrPandaNode_ptrPandaNode_int(self, childNode, sort):
        upcastSelf = self
        returnValue = libpanda._inPnJyoA9tQ(upcastSelf.this, childNode.this, sort)
        return returnValue

    
    def _TextNode__overloaded_addChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        returnValue = libpanda._inPnJyo27ri(upcastSelf.this, childNode.this)
        return returnValue

    
    def _TextNode__overloaded_removeChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        returnValue = libpanda._inPnJyozFZb(upcastSelf.this, childNode.this)
        return returnValue

    
    def _TextNode__overloaded_removeChild_ptrPandaNode_int(self, n):
        upcastSelf = self
        returnValue = libpanda._inPnJyoDqN1(upcastSelf.this, n)
        return returnValue

    
    def replaceChild(self, origChild, newChild):
        upcastSelf = self
        returnValue = libpanda._inPnJyogW5Y(upcastSelf.this, origChild.this, newChild.this)
        return returnValue

    
    def _TextNode__overloaded_stashChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        returnValue = libpanda._inPnJyojC1w(upcastSelf.this, childNode.this)
        return returnValue

    
    def _TextNode__overloaded_stashChild_ptrPandaNode_int(self, childIndex):
        upcastSelf = self
        returnValue = libpanda._inPnJyorWqz(upcastSelf.this, childIndex)
        return returnValue

    
    def _TextNode__overloaded_unstashChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        returnValue = libpanda._inPnJyoqJGM(upcastSelf.this, childNode.this)
        return returnValue

    
    def _TextNode__overloaded_unstashChild_ptrPandaNode_int(self, stashedIndex):
        upcastSelf = self
        returnValue = libpanda._inPnJyoeWxF(upcastSelf.this, stashedIndex)
        return returnValue

    
    def getNumStashed(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyoOR8_(upcastSelf.this)
        return returnValue

    
    def getStashed(self, n):
        upcastSelf = self
        returnValue = libpanda._inPnJyok8qw(upcastSelf.this, n)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getStashedSort(self, n):
        upcastSelf = self
        returnValue = libpanda._inPnJyoE1FX(upcastSelf.this, n)
        return returnValue

    
    def findStashed(self, node):
        upcastSelf = self
        returnValue = libpanda._inPnJyoyw9C(upcastSelf.this, node.this)
        return returnValue

    
    def _TextNode__overloaded_addStashed_ptrPandaNode_ptrPandaNode_int(self, childNode, sort):
        upcastSelf = self
        returnValue = libpanda._inPnJyoXQ0n(upcastSelf.this, childNode.this, sort)
        return returnValue

    
    def _TextNode__overloaded_addStashed_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        returnValue = libpanda._inPnJyoswLI(upcastSelf.this, childNode.this)
        return returnValue

    
    def removeStashed(self, n):
        upcastSelf = self
        returnValue = libpanda._inPnJyoZHe7(upcastSelf.this, n)
        return returnValue

    
    def removeAllChildren(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyobyap(upcastSelf.this)
        return returnValue

    
    def stealChildren(self, other):
        upcastSelf = self
        returnValue = libpanda._inPnJyojgnr(upcastSelf.this, other.this)
        return returnValue

    
    def copyChildren(self, other):
        upcastSelf = self
        returnValue = libpanda._inPnJyohfED(upcastSelf.this, other.this)
        return returnValue

    
    def _TextNode__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib_int(self, attrib, override):
        upcastSelf = self
        returnValue = libpanda._inPnJyo48Bd(upcastSelf.this, attrib.this, override)
        return returnValue

    
    def _TextNode__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib(self, attrib):
        upcastSelf = self
        returnValue = libpanda._inPnJyoDD5k(upcastSelf.this, attrib.this)
        return returnValue

    
    def getAttrib(self, type):
        upcastSelf = self
        returnValue = libpanda._inPnJyoaDfJ(upcastSelf.this, type.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def hasAttrib(self, type):
        upcastSelf = self
        returnValue = libpanda._inPnJyo2W_P(upcastSelf.this, type.this)
        return returnValue

    
    def clearAttrib(self, type):
        upcastSelf = self
        returnValue = libpanda._inPnJyoDSEu(upcastSelf.this, type.this)
        return returnValue

    
    def setEffect(self, effect):
        upcastSelf = self
        returnValue = libpanda._inPnJyoKWvI(upcastSelf.this, effect.this)
        return returnValue

    
    def getEffect(self, type):
        upcastSelf = self
        returnValue = libpanda._inPnJyo07Hl(upcastSelf.this, type.this)
        import RenderEffect
        returnObject = RenderEffect.RenderEffect(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def hasEffect(self, type):
        upcastSelf = self
        returnValue = libpanda._inPnJyoI1nr(upcastSelf.this, type.this)
        return returnValue

    
    def clearEffect(self, type):
        upcastSelf = self
        returnValue = libpanda._inPnJyoNUJ2(upcastSelf.this, type.this)
        return returnValue

    
    def setState(self, state):
        upcastSelf = self
        returnValue = libpanda._inPnJyoGDjV(upcastSelf.this, state.this)
        return returnValue

    
    def getState(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyoJocj(upcastSelf.this)
        import RenderState
        returnObject = RenderState.RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def clearState(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyotySF(upcastSelf.this)
        return returnValue

    
    def setEffects(self, effects):
        upcastSelf = self
        returnValue = libpanda._inPnJyoxlpj(upcastSelf.this, effects.this)
        return returnValue

    
    def getEffects(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyo1WLf(upcastSelf.this)
        import RenderEffects
        returnObject = RenderEffects.RenderEffects(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def clearEffects(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyo6yPH(upcastSelf.this)
        return returnValue

    
    def clearTransform(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyoEjK_(upcastSelf.this)
        return returnValue

    
    def setPrevTransform(self, transform):
        upcastSelf = self
        returnValue = libpanda._inPnJyo_3nJ(upcastSelf.this, transform.this)
        return returnValue

    
    def getPrevTransform(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyor3cO(upcastSelf.this)
        import TransformState
        returnObject = TransformState.TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def resetPrevTransform(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyoGfcO(upcastSelf.this)
        return returnValue

    
    def setTag(self, key, value):
        upcastSelf = self
        returnValue = libpanda._inPnJyoTNEJ(upcastSelf.this, key, value)
        return returnValue

    
    def getTag(self, key):
        upcastSelf = self
        returnValue = libpanda._inPnJyo5tVl(upcastSelf.this, key)
        return returnValue

    
    def hasTag(self, key):
        upcastSelf = self
        returnValue = libpanda._inPnJyote2r(upcastSelf.this, key)
        return returnValue

    
    def clearTag(self, key):
        upcastSelf = self
        returnValue = libpanda._inPnJyoiRPE(upcastSelf.this, key)
        return returnValue

    
    def copyTags(self, other):
        upcastSelf = self
        returnValue = libpanda._inPnJyoxMQi(upcastSelf.this, other.this)
        return returnValue

    
    def _TextNode__overloaded_listTags_ptrConstPandaNode_ptrOstream_atomicstring(self, out, separator):
        upcastSelf = self
        returnValue = libpanda._inPnJyo3itg(upcastSelf.this, out.this, separator)
        return returnValue

    
    def _TextNode__overloaded_listTags_ptrConstPandaNode_ptrOstream(self, out):
        upcastSelf = self
        returnValue = libpanda._inPnJyocRES(upcastSelf.this, out.this)
        return returnValue

    
    def setDrawMask(self, mask):
        upcastSelf = self
        returnValue = libpanda._inPnJyofzL6(upcastSelf.this, mask.this)
        return returnValue

    
    def getDrawMask(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyoWJXI(upcastSelf.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setIntoCollideMask(self, mask):
        upcastSelf = self
        returnValue = libpanda._inPnJyoK9VT(upcastSelf.this, mask.this)
        return returnValue

    
    def getIntoCollideMask(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyoc3Cf(upcastSelf.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getLegalCollideMask(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyotnOA(upcastSelf.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getNetCollideMask(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyo4l_T(upcastSelf.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def ls(self, out, indentLevel):
        upcastSelf = self
        returnValue = libpanda._inPnJyopBSg(upcastSelf.this, out.this, indentLevel)
        return returnValue

    
    def _TextNode__overloaded_setBound_ptrPandaNode___enum__BoundingVolumeType(self, type):
        upcastSelf = self
        returnValue = libpanda._inPnJyomd5g(upcastSelf.this, type)
        return returnValue

    
    def _TextNode__overloaded_setBound_ptrPandaNode_ptrConstBoundingVolume(self, volume):
        upcastSelf = self
        returnValue = libpanda._inPnJyo4Bq1(upcastSelf.this, volume.this)
        return returnValue

    
    def getBound(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyoif0y(upcastSelf.this)
        import BoundingVolume
        returnObject = BoundingVolume.BoundingVolume(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getInternalBound(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyoJ_J4(upcastSelf.this)
        import BoundingVolume
        returnObject = BoundingVolume.BoundingVolume(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def isGeomNode(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyoxAx3(upcastSelf.this)
        return returnValue

    
    def isLodNode(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyohW8z(upcastSelf.this)
        return returnValue

    
    def asLight(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyobCbs(upcastSelf.this)
        import Light
        returnObject = Light.Light(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setBound(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._TextNode__overloaded_setBound_ptrPandaNode___enum__BoundingVolumeType(*_args)
            
            import BoundingVolume
            if isinstance(_args[0], BoundingVolume.BoundingVolume):
                return self._TextNode__overloaded_setBound_ptrPandaNode_ptrConstBoundingVolume(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <BoundingVolume.BoundingVolume> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._TextNode__overloaded_addChild_ptrPandaNode_ptrPandaNode(*_args)
        elif numArgs == 2:
            return self._TextNode__overloaded_addChild_ptrPandaNode_ptrPandaNode_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def unstashChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._TextNode__overloaded_unstashChild_ptrPandaNode_int(*_args)
            
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                return self._TextNode__overloaded_unstashChild_ptrPandaNode_ptrPandaNode(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def listTags(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._TextNode__overloaded_listTags_ptrConstPandaNode_ptrOstream(*_args)
        elif numArgs == 2:
            return self._TextNode__overloaded_listTags_ptrConstPandaNode_ptrOstream_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setAttrib(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._TextNode__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib(*_args)
        elif numArgs == 2:
            return self._TextNode__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def stashChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._TextNode__overloaded_stashChild_ptrPandaNode_int(*_args)
            
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                return self._TextNode__overloaded_stashChild_ptrPandaNode_ptrPandaNode(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def removeChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._TextNode__overloaded_removeChild_ptrPandaNode_int(*_args)
            
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                return self._TextNode__overloaded_removeChild_ptrPandaNode_ptrPandaNode(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addStashed(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._TextNode__overloaded_addStashed_ptrPandaNode_ptrPandaNode(*_args)
        elif numArgs == 2:
            return self._TextNode__overloaded_addStashed_ptrPandaNode_ptrPandaNode_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def upcastToNamable(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyojprb(upcastSelf.this)
        import Namable
        returnObject = Namable.Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToBoundedObject(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyo7YS5(upcastSelf.this)
        import BoundedObject
        returnObject = BoundedObject.BoundedObject(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToReferenceCount(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyogdrc(upcastSelf.this)
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

    
    def assign(self, other):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtp1bI(upcastSelf.this, other.this)
        import Namable
        returnObject = Namable.Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
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

    
    def markBoundStale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPG4uI(upcastSelf.this)
        return returnValue

    
    def forceBoundStale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPj1Pw(upcastSelf.this)
        return returnValue

    
    def isBoundStale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPkac5(upcastSelf.this)
        return returnValue

    
    def setFinal(self, flag):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPy9vH(upcastSelf.this, flag)
        return returnValue

    
    def isFinal(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPbuL4(upcastSelf.this)
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

    
    def setEncoding(self, encoding):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPKoxtrlQJ(upcastSelf.this, encoding)
        return returnValue

    
    def getEncoding(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPKoxtMWo7(upcastSelf.this)
        return returnValue

    
    def hasText(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPKoxt97oh(upcastSelf.this)
        return returnValue

    
    def makeUpper(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPKoxtqMP7(upcastSelf.this)
        return returnValue

    
    def makeLower(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPKoxtT0Ve(upcastSelf.this)
        return returnValue

    
    def _TextNode__overloaded_getText_ptrConstTextEncoder(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPKoxtp9Te(upcastSelf.this)
        return returnValue

    
    def _TextNode__overloaded_getText_ptrConstTextEncoder___enum__Encoding(self, encoding):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPKoxtJTNv(upcastSelf.this, encoding)
        return returnValue

    
    def getNumChars(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPKoxt5x3n(upcastSelf.this)
        return returnValue

    
    def getUnicodeChar(self, index):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPKoxtjULv(upcastSelf.this, index)
        return returnValue

    
    def setUnicodeChar(self, index, character):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPKoxtSkrk(upcastSelf.this, index, character)
        return returnValue

    
    def _TextNode__overloaded_getEncodedChar_ptrConstTextEncoder_int(self, index):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPKoxtIGUu(upcastSelf.this, index)
        return returnValue

    
    def _TextNode__overloaded_getEncodedChar_ptrConstTextEncoder_int___enum__Encoding(self, index, encoding):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPKoxtJIi_(upcastSelf.this, index, encoding)
        return returnValue

    
    def getTextAsAscii(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextEncoder()
        returnValue = libpandaexpress._inPKoxtzcrI(upcastSelf.this)
        return returnValue

    
    def getEncodedChar(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._TextNode__overloaded_getEncodedChar_ptrConstTextEncoder_int(*_args)
        elif numArgs == 2:
            return self._TextNode__overloaded_getEncodedChar_ptrConstTextEncoder_int___enum__Encoding(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getText(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._TextNode__overloaded_getText_ptrConstTextEncoder(*_args)
        elif numArgs == 1:
            return self._TextNode__overloaded_getText_ptrConstTextEncoder___enum__Encoding(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, copy):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_k70w(upcastSelf.this, copy.this)
        import TextProperties
        returnObject = TextProperties.TextProperties(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def clear(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_1GAn(upcastSelf.this)
        return returnValue

    
    def isAnySpecified(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_K3ac(upcastSelf.this)
        return returnValue

    
    def hasFont(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_zzFD(upcastSelf.this)
        return returnValue

    
    def getFont(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_aRE2(upcastSelf.this)
        import TextFont
        returnObject = TextFont.TextFont(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def hasSmallCaps(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_68B0(upcastSelf.this)
        return returnValue

    
    def getSmallCaps(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_CZAn(upcastSelf.this)
        return returnValue

    
    def hasSmallCapsScale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_fV3a(upcastSelf.this)
        return returnValue

    
    def getSmallCapsScale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_3_2N(upcastSelf.this)
        return returnValue

    
    def hasSlant(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_iZ7r(upcastSelf.this)
        return returnValue

    
    def getSlant(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_KL7e(upcastSelf.this)
        return returnValue

    
    def hasAlign(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_SdzH(upcastSelf.this)
        return returnValue

    
    def getAlign(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_l2z6(upcastSelf.this)
        return returnValue

    
    def hasIndent(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_7oOi(upcastSelf.this)
        return returnValue

    
    def getIndent(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_TLOV(upcastSelf.this)
        return returnValue

    
    def hasWordwrap(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_2SM7(upcastSelf.this)
        return returnValue

    
    def getWordwrap(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_O3Nu(upcastSelf.this)
        return returnValue

    
    def setPreserveTrailingWhitespace(self, preserveTrailingWhitespace):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_GPH5(upcastSelf.this, preserveTrailingWhitespace)
        return returnValue

    
    def clearPreserveTrailingWhitespace(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_k_Vr(upcastSelf.this)
        return returnValue

    
    def hasPreserveTrailingWhitespace(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_gu7s(upcastSelf.this)
        return returnValue

    
    def getPreserveTrailingWhitespace(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_4J6f(upcastSelf.this)
        return returnValue

    
    def hasTextColor(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_5OXS(upcastSelf.this)
        return returnValue

    
    def getTextColor(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_BzWF(upcastSelf.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def hasShadowColor(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_Bnqk(upcastSelf.this)
        return returnValue

    
    def getShadowColor(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_ZaqX(upcastSelf.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def hasShadow(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_I1O1(upcastSelf.this)
        return returnValue

    
    def getShadow(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_grOo(upcastSelf.this)
        import Vec2
        returnObject = Vec2.Vec2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def hasBin(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_mxqz(upcastSelf.this)
        return returnValue

    
    def getBin(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_OWqm(upcastSelf.this)
        return returnValue

    
    def hasDrawOrder(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_VlQH(upcastSelf.this)
        return returnValue

    
    def getDrawOrder(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk__LP6(upcastSelf.this)
        return returnValue

    
    def hasTabWidth(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_npZ0(upcastSelf.this)
        return returnValue

    
    def getTabWidth(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_PKYn(upcastSelf.this)
        return returnValue

    
    def hasGlyphScale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_Qy8B(upcastSelf.this)
        return returnValue

    
    def getGlyphScale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_5U70(upcastSelf.this)
        return returnValue

    
    def hasGlyphShift(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_zIZo(upcastSelf.this)
        return returnValue

    
    def getGlyphShift(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_rrYb(upcastSelf.this)
        return returnValue

    
    def addProperties(self, other):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToTextProperties()
        returnValue = libpanda._inPpUk_lo22(upcastSelf.this, other.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._TextNode__overloaded_constructor_atomicstring(*_args)
        elif numArgs == 2:
            return self._TextNode__overloaded_constructor_atomicstring_ptrConstTextProperties(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._TextNode__overloaded_write_ptrConstTextNode_ptrOstream(*_args)
        elif numArgs == 2:
            return self._TextNode__overloaded_write_ptrConstTextNode_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def calcWidth(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._TextNode__overloaded_calcWidth_ptrConstTextNode_int(*_args)
            
            if isinstance(_args[0], types.StringType):
                return self._TextNode__overloaded_calcWidth_ptrConstTextNode_atomicstring(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def setShadow(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._TextNode__overloaded_setShadow_ptrTextNode_ptrConstLVecBase2f(*_args)
        elif numArgs == 2:
            return self._TextNode__overloaded_setShadow_ptrTextNode_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setShadowColor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._TextNode__overloaded_setShadowColor_ptrTextNode_ptrConstLVecBase4f(*_args)
        elif numArgs == 4:
            return self._TextNode__overloaded_setShadowColor_ptrTextNode_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 4 '

    
    def setText(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._TextNode__overloaded_setText_ptrTextNode_atomicstring(*_args)
        elif numArgs == 2:
            return self._TextNode__overloaded_setText_ptrTextNode_atomicstring___enum__Encoding(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setCardColor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._TextNode__overloaded_setCardColor_ptrTextNode_ptrConstLVecBase4f(*_args)
        elif numArgs == 4:
            return self._TextNode__overloaded_setCardColor_ptrTextNode_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 4 '

    
    def setFrameColor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._TextNode__overloaded_setFrameColor_ptrTextNode_ptrConstLVecBase4f(*_args)
        elif numArgs == 4:
            return self._TextNode__overloaded_setFrameColor_ptrTextNode_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 4 '

    
    def setTextColor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._TextNode__overloaded_setTextColor_ptrTextNode_ptrConstLVecBase4f(*_args)
        elif numArgs == 4:
            return self._TextNode__overloaded_setTextColor_ptrTextNode_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 4 '


