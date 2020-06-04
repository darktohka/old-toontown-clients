# File: D (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
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
        
        apply(self.constructor, _args)

    
    def _DynamicTextFont__overloaded_constructor_ptrConstFilename_int(self, fontFilename, faceIndex):
        self.this = libpanda._inPmUk_NkXk(fontFilename.this, faceIndex)
        self.userManagesMemory = 1

    
    def _DynamicTextFont__overloaded_constructor_ptrConstFilename(self, fontFilename):
        self.this = libpanda._inPmUk_jio2(fontFilename.this)
        self.userManagesMemory = 1

    
    def _DynamicTextFont__overloaded_constructor_atomicstring_int_int(self, fontData, dataLength, faceIndex):
        self.this = libpanda._inPmUk_K5pQ(fontData, dataLength, faceIndex)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPmUk_tKBU:
            libpanda._inPmUk_tKBU(self.this)
        

    
    def setUpdateClearedGlyphs(updateClearedGlyphs):
        returnValue = libpanda._inPmUk_HkWI(updateClearedGlyphs)
        return returnValue

    setUpdateClearedGlyphs = staticmethod(setUpdateClearedGlyphs)
    
    def getUpdateClearedGlyphs():
        returnValue = libpanda._inPmUk_tbTq()
        return returnValue

    getUpdateClearedGlyphs = staticmethod(getUpdateClearedGlyphs)
    
    def getClassType():
        returnValue = libpanda._inPmUk_KwHA()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getName(self):
        returnValue = libpanda._inPmUk__u_H(self.this)
        return returnValue

    
    def setPointSize(self, pointSize):
        returnValue = libpanda._inPmUk_HMaP(self.this, pointSize)
        return returnValue

    
    def getPointSize(self):
        returnValue = libpanda._inPmUk_faBi(self.this)
        return returnValue

    
    def setPixelsPerUnit(self, pixelsPerUnit):
        returnValue = libpanda._inPmUk_wHlG(self.this, pixelsPerUnit)
        return returnValue

    
    def getPixelsPerUnit(self):
        returnValue = libpanda._inPmUk_8_b_(self.this)
        return returnValue

    
    def setScaleFactor(self, scaleFactor):
        returnValue = libpanda._inPmUk_nves(self.this, scaleFactor)
        return returnValue

    
    def getScaleFactor(self):
        returnValue = libpanda._inPmUk_2S6E(self.this)
        return returnValue

    
    def setNativeAntialias(self, nativeAntialias):
        returnValue = libpanda._inPmUk__XCc(self.this, nativeAntialias)
        return returnValue

    
    def getNativeAntialias(self):
        returnValue = libpanda._inPmUk_4rqO(self.this)
        return returnValue

    
    def getFontPixelSize(self):
        returnValue = libpanda._inPmUk_oAyj(self.this)
        return returnValue

    
    def getLineHeight(self):
        returnValue = libpanda._inPmUk_SLGS(self.this)
        return returnValue

    
    def getSpaceAdvance(self):
        returnValue = libpanda._inPmUk_IitQ(self.this)
        return returnValue

    
    def setTextureMargin(self, textureMargin):
        returnValue = libpanda._inPmUk__M4T(self.this, textureMargin)
        return returnValue

    
    def getTextureMargin(self):
        returnValue = libpanda._inPmUk__YB2(self.this)
        return returnValue

    
    def setPolyMargin(self, polyMargin):
        returnValue = libpanda._inPmUk_ksfM(self.this, polyMargin)
        return returnValue

    
    def getPolyMargin(self):
        returnValue = libpanda._inPmUk_YyNh(self.this)
        return returnValue

    
    def setPageSize(self, xSize, ySize):
        returnValue = libpanda._inPmUk_5kww(self.this, xSize, ySize)
        return returnValue

    
    def getPageXSize(self):
        returnValue = libpanda._inPmUk__gFL(self.this)
        return returnValue

    
    def getPageYSize(self):
        returnValue = libpanda._inPmUk__Qme(self.this)
        return returnValue

    
    def setMinfilter(self, filter):
        returnValue = libpanda._inPmUk_62Sw(self.this, filter)
        return returnValue

    
    def getMinfilter(self):
        returnValue = libpanda._inPmUk__eoM(self.this)
        return returnValue

    
    def setMagfilter(self, filter):
        returnValue = libpanda._inPmUk_XnyK(self.this, filter)
        return returnValue

    
    def getMagfilter(self):
        returnValue = libpanda._inPmUk_SvIn(self.this)
        return returnValue

    
    def setAnisotropicDegree(self, anisotropicDegree):
        returnValue = libpanda._inPmUk_D2hS(self.this, anisotropicDegree)
        return returnValue

    
    def getAnisotropicDegree(self):
        returnValue = libpanda._inPmUk_gQMP(self.this)
        return returnValue

    
    def getNumPages(self):
        returnValue = libpanda._inPmUk_nWpf(self.this)
        return returnValue

    
    def getPage(self, n):
        returnValue = libpanda._inPmUk_62Ni(self.this, n)
        import DynamicTextPage
        returnObject = DynamicTextPage.DynamicTextPage(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def garbageCollect(self):
        returnValue = libpanda._inPmUk_qlNW(self.this)
        return returnValue

    
    def updateTextureMemory(self):
        returnValue = libpanda._inPmUk_7DLI(self.this)
        return returnValue

    
    def clear(self):
        returnValue = libpanda._inPmUk_A6z6(self.this)
        return returnValue

    
    def write(self, out, indentLevel):
        returnValue = libpanda._inPmUk_OAFU(self.this, out.this, indentLevel)
        return returnValue

    
    def upcastToFreetypeFont(self):
        returnValue = libpanda._inPmUk_HSLy(self.this)
        import FreetypeFont
        returnObject = FreetypeFont.FreetypeFont(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def isValid(self):
        upcastSelf = self
        returnValue = libpanda._inPmUk_9LaW(upcastSelf.this)
        return returnValue

    
    def setLineHeight(self, lineHeight):
        upcastSelf = self
        returnValue = libpanda._inPmUk_MJXZ(upcastSelf.this, lineHeight)
        return returnValue

    
    def setSpaceAdvance(self, spaceAdvance):
        upcastSelf = self
        returnValue = libpanda._inPmUk_HPSY(upcastSelf.this, spaceAdvance)
        return returnValue

    
    def _DynamicTextFont__overloaded_calcWidth_ptrTextFont_atomicstring(self, line):
        upcastSelf = self
        returnValue = libpanda._inPmUk_HU_T(upcastSelf.this, line)
        return returnValue

    
    def _DynamicTextFont__overloaded_calcWidth_ptrTextFont_int(self, character):
        upcastSelf = self
        returnValue = libpanda._inPmUk_wfnF(upcastSelf.this, character)
        return returnValue

    
    def wordwrapTo(self, text, wordwrapWidth, preserveTrailingWhitespace):
        upcastSelf = self
        returnValue = libpanda._inPmUk_IkA5(upcastSelf.this, text, wordwrapWidth, preserveTrailingWhitespace)
        return returnValue

    
    def calcWidth(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._DynamicTextFont__overloaded_calcWidth_ptrTextFont_int(_args[0])
            elif isinstance(_args[0], types.StringType):
                return self._DynamicTextFont__overloaded_calcWidth_ptrTextFont_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def upcastToNamable(self):
        upcastSelf = self
        returnValue = libpanda._inPmUk_SvLG(upcastSelf.this)
        import Namable
        returnObject = Namable.Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToReferenceCount(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPJoxtKE8f(upcastSelf.this)
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

    
    def output(self, out):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtvz7q(upcastSelf.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._DynamicTextFont__overloaded_constructor_ptrConstFilename(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
        elif numArgs == 2:
            import Filename
            if isinstance(_args[0], Filename.Filename):
                if isinstance(_args[1], types.IntType):
                    return self._DynamicTextFont__overloaded_constructor_ptrConstFilename_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
        elif numArgs == 3:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.IntType):
                        return self._DynamicTextFont__overloaded_constructor_atomicstring_int_int(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '


