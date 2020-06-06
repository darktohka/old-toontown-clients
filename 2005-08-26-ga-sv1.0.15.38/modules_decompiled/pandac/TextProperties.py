# File: T (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class TextProperties(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    ALeft = 0
    ARight = 1
    ACenter = 2
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _TextProperties__overloaded_constructor(self):
        self.this = libpanda._inPpUk_ZcXD()
        self.userManagesMemory = 1

    
    def _TextProperties__overloaded_constructor_ptrConstTextProperties(self, copy):
        self.this = libpanda._inPpUk_thC2(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPpUk_mQl8:
            libpanda._inPpUk_mQl8(self.this)
        

    
    def setDefaultFont(parameter0):
        returnValue = libpanda._inPpUk_lPdf(parameter0.this)
        return returnValue

    setDefaultFont = staticmethod(setDefaultFont)
    
    def getDefaultFont():
        returnValue = libpanda._inPpUk_aGgR()
        import TextFont
        returnObject = TextFont.TextFont(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    getDefaultFont = staticmethod(getDefaultFont)
    
    def getClassType():
        returnValue = libpanda._inPpUk__CJ5()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpanda._inPpUk_k70w(self.this, copy.this)
        returnObject = TextProperties(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def clear(self):
        returnValue = libpanda._inPpUk_1GAn(self.this)
        return returnValue

    
    def isAnySpecified(self):
        returnValue = libpanda._inPpUk_K3ac(self.this)
        return returnValue

    
    def setFont(self, font):
        returnValue = libpanda._inPpUk_LLTe(self.this, font.this)
        return returnValue

    
    def clearFont(self):
        returnValue = libpanda._inPpUk__wmu(self.this)
        return returnValue

    
    def hasFont(self):
        returnValue = libpanda._inPpUk_zzFD(self.this)
        return returnValue

    
    def getFont(self):
        returnValue = libpanda._inPpUk_aRE2(self.this)
        import TextFont
        returnObject = TextFont.TextFont(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setSmallCaps(self, smallCaps):
        returnValue = libpanda._inPpUk_IHvI(self.this, smallCaps)
        return returnValue

    
    def clearSmallCaps(self):
        returnValue = libpanda._inPpUk_jTKU(self.this)
        return returnValue

    
    def hasSmallCaps(self):
        returnValue = libpanda._inPpUk_68B0(self.this)
        return returnValue

    
    def getSmallCaps(self):
        returnValue = libpanda._inPpUk_CZAn(self.this)
        return returnValue

    
    def setSmallCapsScale(self, smallCapsScale):
        returnValue = libpanda._inPpUk_uF_9(self.this, smallCapsScale)
        return returnValue

    
    def clearSmallCapsScale(self):
        returnValue = libpanda._inPpUk_VrrU(self.this)
        return returnValue

    
    def hasSmallCapsScale(self):
        returnValue = libpanda._inPpUk_fV3a(self.this)
        return returnValue

    
    def getSmallCapsScale(self):
        returnValue = libpanda._inPpUk_3_2N(self.this)
        return returnValue

    
    def setSlant(self, slant):
        returnValue = libpanda._inPpUk_Q85E(self.this, slant)
        return returnValue

    
    def clearSlant(self):
        returnValue = libpanda._inPpUk_Hlo1(self.this)
        return returnValue

    
    def hasSlant(self):
        returnValue = libpanda._inPpUk_iZ7r(self.this)
        return returnValue

    
    def getSlant(self):
        returnValue = libpanda._inPpUk_KL7e(self.this)
        return returnValue

    
    def setAlign(self, alignType):
        returnValue = libpanda._inPpUk_7ogz(self.this, alignType)
        return returnValue

    
    def clearAlign(self):
        returnValue = libpanda._inPpUk_WteE(self.this)
        return returnValue

    
    def hasAlign(self):
        returnValue = libpanda._inPpUk_SdzH(self.this)
        return returnValue

    
    def getAlign(self):
        returnValue = libpanda._inPpUk_l2z6(self.this)
        return returnValue

    
    def setIndent(self, indent):
        returnValue = libpanda._inPpUk_C_M9(self.this, indent)
        return returnValue

    
    def clearIndent(self):
        returnValue = libpanda._inPpUk_IAtK(self.this)
        return returnValue

    
    def hasIndent(self):
        returnValue = libpanda._inPpUk_7oOi(self.this)
        return returnValue

    
    def getIndent(self):
        returnValue = libpanda._inPpUk_TLOV(self.this)
        return returnValue

    
    def setWordwrap(self, wordwrap):
        returnValue = libpanda._inPpUk_lTPz(self.this, wordwrap)
        return returnValue

    
    def clearWordwrap(self):
        returnValue = libpanda._inPpUk_q0Vt(self.this)
        return returnValue

    
    def hasWordwrap(self):
        returnValue = libpanda._inPpUk_2SM7(self.this)
        return returnValue

    
    def getWordwrap(self):
        returnValue = libpanda._inPpUk_O3Nu(self.this)
        return returnValue

    
    def setPreserveTrailingWhitespace(self, preserveTrailingWhitespace):
        returnValue = libpanda._inPpUk_GPH5(self.this, preserveTrailingWhitespace)
        return returnValue

    
    def clearPreserveTrailingWhitespace(self):
        returnValue = libpanda._inPpUk_k_Vr(self.this)
        return returnValue

    
    def hasPreserveTrailingWhitespace(self):
        returnValue = libpanda._inPpUk_gu7s(self.this)
        return returnValue

    
    def getPreserveTrailingWhitespace(self):
        returnValue = libpanda._inPpUk_4J6f(self.this)
        return returnValue

    
    def _TextProperties__overloaded_setTextColor_ptrTextProperties_ptrConstLVecBase4f(self, textColor):
        returnValue = libpanda._inPpUk_lx5m(self.this, textColor.this)
        return returnValue

    
    def _TextProperties__overloaded_setTextColor_ptrTextProperties_float_float_float_float(self, r, g, b, a):
        returnValue = libpanda._inPpUk_qqgv(self.this, r, g, b, a)
        return returnValue

    
    def clearTextColor(self):
        returnValue = libpanda._inPpUk_6ttP(self.this)
        return returnValue

    
    def hasTextColor(self):
        returnValue = libpanda._inPpUk_5OXS(self.this)
        return returnValue

    
    def getTextColor(self):
        returnValue = libpanda._inPpUk_BzWF(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _TextProperties__overloaded_setShadowColor_ptrTextProperties_ptrConstLVecBase4f(self, shadowColor):
        returnValue = libpanda._inPpUk_MYoy(self.this, shadowColor.this)
        return returnValue

    
    def _TextProperties__overloaded_setShadowColor_ptrTextProperties_float_float_float_float(self, r, g, b, a):
        returnValue = libpanda._inPpUk_L_2W(self.this, r, g, b, a)
        return returnValue

    
    def clearShadowColor(self):
        returnValue = libpanda._inPpUk_CS3R(self.this)
        return returnValue

    
    def hasShadowColor(self):
        returnValue = libpanda._inPpUk_Bnqk(self.this)
        return returnValue

    
    def getShadowColor(self):
        returnValue = libpanda._inPpUk_ZaqX(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _TextProperties__overloaded_setShadow_ptrTextProperties_ptrConstLVecBase2f(self, shadowOffset):
        returnValue = libpanda._inPpUk_apcN(self.this, shadowOffset.this)
        return returnValue

    
    def _TextProperties__overloaded_setShadow_ptrTextProperties_float_float(self, xoffset, yoffset):
        returnValue = libpanda._inPpUk_3fZ9(self.this, xoffset, yoffset)
        return returnValue

    
    def clearShadow(self):
        returnValue = libpanda._inPpUk__RkQ(self.this)
        return returnValue

    
    def hasShadow(self):
        returnValue = libpanda._inPpUk_I1O1(self.this)
        return returnValue

    
    def getShadow(self):
        returnValue = libpanda._inPpUk_grOo(self.this)
        import Vec2
        returnObject = Vec2.Vec2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setBin(self, bin):
        returnValue = libpanda._inPpUk_LXjT(self.this, bin)
        return returnValue

    
    def clearBin(self):
        returnValue = libpanda._inPpUk_AeJK(self.this)
        return returnValue

    
    def hasBin(self):
        returnValue = libpanda._inPpUk_mxqz(self.this)
        return returnValue

    
    def getBin(self):
        returnValue = libpanda._inPpUk_OWqm(self.this)
        return returnValue

    
    def setDrawOrder(self, drawOrder):
        returnValue = libpanda._inPpUk_0od6(self.this, drawOrder)
        return returnValue

    
    def clearDrawOrder(self):
        returnValue = libpanda._inPpUk_P1HS(self.this)
        return returnValue

    
    def hasDrawOrder(self):
        returnValue = libpanda._inPpUk_VlQH(self.this)
        return returnValue

    
    def getDrawOrder(self):
        returnValue = libpanda._inPpUk__LP6(self.this)
        return returnValue

    
    def setTabWidth(self, tabWidth):
        returnValue = libpanda._inPpUk_Fusw(self.this, tabWidth)
        return returnValue

    
    def clearTabWidth(self):
        returnValue = libpanda._inPpUk_pdwn(self.this)
        return returnValue

    
    def hasTabWidth(self):
        returnValue = libpanda._inPpUk_npZ0(self.this)
        return returnValue

    
    def getTabWidth(self):
        returnValue = libpanda._inPpUk_PKYn(self.this)
        return returnValue

    
    def setGlyphScale(self, glyphScale):
        returnValue = libpanda._inPpUk_UBRK(self.this, glyphScale)
        return returnValue

    
    def clearGlyphScale(self):
        returnValue = libpanda._inPpUk_89_H(self.this)
        return returnValue

    
    def hasGlyphScale(self):
        returnValue = libpanda._inPpUk_Qy8B(self.this)
        return returnValue

    
    def getGlyphScale(self):
        returnValue = libpanda._inPpUk_5U70(self.this)
        return returnValue

    
    def setGlyphShift(self, glyphShift):
        returnValue = libpanda._inPpUk__nuw(self.this, glyphShift)
        return returnValue

    
    def clearGlyphShift(self):
        returnValue = libpanda._inPpUk_Tz3h(self.this)
        return returnValue

    
    def hasGlyphShift(self):
        returnValue = libpanda._inPpUk_zIZo(self.this)
        return returnValue

    
    def getGlyphShift(self):
        returnValue = libpanda._inPpUk_rrYb(self.this)
        return returnValue

    
    def addProperties(self, other):
        returnValue = libpanda._inPpUk_lo22(self.this, other.this)
        return returnValue

    
    def _TextProperties__overloaded_write_ptrConstTextProperties_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPpUk_dHuP(self.this, out.this, indentLevel)
        return returnValue

    
    def _TextProperties__overloaded_write_ptrConstTextProperties_ptrOstream(self, out):
        returnValue = libpanda._inPpUk_dtgi(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._TextProperties__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._TextProperties__overloaded_constructor_ptrConstTextProperties(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._TextProperties__overloaded_write_ptrConstTextProperties_ptrOstream(*_args)
        elif numArgs == 2:
            return self._TextProperties__overloaded_write_ptrConstTextProperties_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setShadow(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._TextProperties__overloaded_setShadow_ptrTextProperties_ptrConstLVecBase2f(*_args)
        elif numArgs == 2:
            return self._TextProperties__overloaded_setShadow_ptrTextProperties_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setTextColor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._TextProperties__overloaded_setTextColor_ptrTextProperties_ptrConstLVecBase4f(*_args)
        elif numArgs == 4:
            return self._TextProperties__overloaded_setTextColor_ptrTextProperties_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 4 '

    
    def setShadowColor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._TextProperties__overloaded_setShadowColor_ptrTextProperties_ptrConstLVecBase4f(*_args)
        elif numArgs == 4:
            return self._TextProperties__overloaded_setShadowColor_ptrTextProperties_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 4 '


