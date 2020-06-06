# File: D (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TextFont

class DynamicTextFont(TextFont.TextFont, FFIExternalObject.FFIExternalObject):
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
        if libpanda and libpanda._inPmUk_ftUU:
            libpanda._inPmUk_ftUU(self.this)
        

    
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


