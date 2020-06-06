# File: D (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TextFont
import FreetypeFont

class DynamicTextFont(TextFont.TextFont, FreetypeFont.FreetypeFont, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _DynamicTextFont__overloaded_constructor_ptrConstFilename_int(self, fontFilename, faceIndex):
        self.this = libpanda._inPpUk_OkXk(fontFilename.this, faceIndex)
        self.userManagesMemory = 1

    
    def _DynamicTextFont__overloaded_constructor_ptrConstFilename(self, fontFilename):
        self.this = libpanda._inPpUk_8io2(fontFilename.this)
        self.userManagesMemory = 1

    
    def _DynamicTextFont__overloaded_constructor_atomicstring_int_int(self, fontData, dataLength, faceIndex):
        self.this = libpanda._inPpUk_K5pQ(fontData, dataLength, faceIndex)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPpUk_tKBU:
            libpanda._inPpUk_tKBU(self.this)
        

    
    def setUpdateClearedGlyphs(updateClearedGlyphs):
        returnValue = libpanda._inPpUk_HkWI(updateClearedGlyphs)
        return returnValue

    setUpdateClearedGlyphs = staticmethod(setUpdateClearedGlyphs)
    
    def getUpdateClearedGlyphs():
        returnValue = libpanda._inPpUk_ibTq()
        return returnValue

    getUpdateClearedGlyphs = staticmethod(getUpdateClearedGlyphs)
    
    def getClassType():
        returnValue = libpanda._inPpUk_KwHA()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getName(self):
        returnValue = libpanda._inPpUk__u_H(self.this)
        return returnValue

    
    def setPointSize(self, pointSize):
        returnValue = libpanda._inPpUk_HMaP(self.this, pointSize)
        return returnValue

    
    def getPointSize(self):
        returnValue = libpanda._inPpUk_caBi(self.this)
        return returnValue

    
    def setPixelsPerUnit(self, pixelsPerUnit):
        returnValue = libpanda._inPpUk_wHlG(self.this, pixelsPerUnit)
        return returnValue

    
    def getPixelsPerUnit(self):
        returnValue = libpanda._inPpUk_7_b_(self.this)
        return returnValue

    
    def setScaleFactor(self, scaleFactor):
        returnValue = libpanda._inPpUk_mves(self.this, scaleFactor)
        return returnValue

    
    def getScaleFactor(self):
        returnValue = libpanda._inPpUk_2S6E(self.this)
        return returnValue

    
    def setNativeAntialias(self, nativeAntialias):
        returnValue = libpanda._inPpUk__XCc(self.this, nativeAntialias)
        return returnValue

    
    def getNativeAntialias(self):
        returnValue = libpanda._inPpUk_4rqO(self.this)
        return returnValue

    
    def getFontPixelSize(self):
        returnValue = libpanda._inPpUk_pAyj(self.this)
        return returnValue

    
    def getLineHeight(self):
        returnValue = libpanda._inPpUk_SLGS(self.this)
        return returnValue

    
    def getSpaceAdvance(self):
        returnValue = libpanda._inPpUk_IitQ(self.this)
        return returnValue

    
    def setTextureMargin(self, textureMargin):
        returnValue = libpanda._inPpUk__M4T(self.this, textureMargin)
        return returnValue

    
    def getTextureMargin(self):
        returnValue = libpanda._inPpUk__YB2(self.this)
        return returnValue

    
    def setPolyMargin(self, polyMargin):
        returnValue = libpanda._inPpUk_ksfM(self.this, polyMargin)
        return returnValue

    
    def getPolyMargin(self):
        returnValue = libpanda._inPpUk_ZyNh(self.this)
        return returnValue

    
    def setPageSize(self, xSize, ySize):
        returnValue = libpanda._inPpUk_mkww(self.this, xSize, ySize)
        return returnValue

    
    def getPageXSize(self):
        returnValue = libpanda._inPpUk__gFL(self.this)
        return returnValue

    
    def getPageYSize(self):
        returnValue = libpanda._inPpUk__Qme(self.this)
        return returnValue

    
    def setMinfilter(self, filter):
        returnValue = libpanda._inPpUk_72Sw(self.this, filter)
        return returnValue

    
    def getMinfilter(self):
        returnValue = libpanda._inPpUk__eoM(self.this)
        return returnValue

    
    def setMagfilter(self, filter):
        returnValue = libpanda._inPpUk_XnyK(self.this, filter)
        return returnValue

    
    def getMagfilter(self):
        returnValue = libpanda._inPpUk_NvIn(self.this)
        return returnValue

    
    def setAnisotropicDegree(self, anisotropicDegree):
        returnValue = libpanda._inPpUk_D2hS(self.this, anisotropicDegree)
        return returnValue

    
    def getAnisotropicDegree(self):
        returnValue = libpanda._inPpUk_gQMP(self.this)
        return returnValue

    
    def getNumPages(self):
        returnValue = libpanda._inPpUk_nWpf(self.this)
        return returnValue

    
    def getPage(self, n):
        returnValue = libpanda._inPpUk_72Ni(self.this, n)
        import DynamicTextPage
        returnObject = DynamicTextPage.DynamicTextPage(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def garbageCollect(self):
        returnValue = libpanda._inPpUk_qlNW(self.this)
        return returnValue

    
    def updateTextureMemory(self):
        returnValue = libpanda._inPpUk_7DLI(self.this)
        return returnValue

    
    def clear(self):
        returnValue = libpanda._inPpUk_H6z6(self.this)
        return returnValue

    
    def write(self, out, indentLevel):
        returnValue = libpanda._inPpUk_OAFU(self.this, out.this, indentLevel)
        return returnValue

    
    def upcastToFreetypeFont(self):
        returnValue = libpanda._inPpUk_GSLy(self.this)
        import FreetypeFont
        returnObject = FreetypeFont.FreetypeFont(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def isValid(self):
        upcastSelf = self
        returnValue = libpanda._inPpUk_9LaW(upcastSelf.this)
        return returnValue

    
    def setLineHeight(self, lineHeight):
        upcastSelf = self
        returnValue = libpanda._inPpUk_MJXZ(upcastSelf.this, lineHeight)
        return returnValue

    
    def setSpaceAdvance(self, spaceAdvance):
        upcastSelf = self
        returnValue = libpanda._inPpUk_HPSY(upcastSelf.this, spaceAdvance)
        return returnValue

    
    def upcastToNamable(self):
        upcastSelf = self
        returnValue = libpanda._inPpUk_SvLG(upcastSelf.this)
        import Namable
        returnObject = Namable.Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
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

    
    def output(self, out):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtoz7q(upcastSelf.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._DynamicTextFont__overloaded_constructor_ptrConstFilename(*_args)
        elif numArgs == 2:
            return self._DynamicTextFont__overloaded_constructor_ptrConstFilename_int(*_args)
        elif numArgs == 3:
            return self._DynamicTextFont__overloaded_constructor_atomicstring_int_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '


