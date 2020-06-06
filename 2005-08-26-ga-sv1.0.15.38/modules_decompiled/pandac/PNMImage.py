# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject
import PNMImageHeader

class PNMImage(PNMImageHeader.PNMImageHeader, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _PNMImage__overloaded_constructor(self):
        self.this = libpanda._inP5U4kJuU_()
        self.userManagesMemory = 1

    
    def _PNMImage__overloaded_constructor_ptrConstFilename_ptrPNMFileType(self, filename, type):
        self.this = libpanda._inP5U4kZniN(filename.this, type.this)
        self.userManagesMemory = 1

    
    def _PNMImage__overloaded_constructor_ptrConstFilename(self, filename):
        self.this = libpanda._inP5U4kGo3y(filename.this)
        self.userManagesMemory = 1

    
    def _PNMImage__overloaded_constructor_ptrConstPNMImage(self, copy):
        self.this = libpanda._inP5U4k9JI_(copy.this)
        self.userManagesMemory = 1

    
    def _PNMImage__overloaded_constructor_int_int_int_shortUnsignedshortint_ptrPNMFileType(self, xSize, ySize, numChannels, maxval, type):
        self.this = libpanda._inP5U4kGUHz(xSize, ySize, numChannels, maxval, type.this)
        self.userManagesMemory = 1

    
    def _PNMImage__overloaded_constructor_int_int_int_shortUnsignedshortint(self, xSize, ySize, numChannels, maxval):
        self.this = libpanda._inP5U4k3kSc(xSize, ySize, numChannels, maxval)
        self.userManagesMemory = 1

    
    def _PNMImage__overloaded_constructor_int_int_int(self, xSize, ySize, numChannels):
        self.this = libpanda._inP5U4k0Ehq(xSize, ySize, numChannels)
        self.userManagesMemory = 1

    
    def _PNMImage__overloaded_constructor_int_int(self, xSize, ySize):
        self.this = libpanda._inP5U4kxphz(xSize, ySize)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inP5U4k1pIY:
            libpanda._inP5U4k1pIY(self.this)
        

    
    def assign(self, copy):
        returnValue = libpanda._inP5U4kW6D7(self.this, copy.this)
        returnObject = PNMImage(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def clampVal(self, inputValue):
        returnValue = libpanda._inP5U4k1Od2(self.this, inputValue)
        return returnValue

    
    def toVal(self, inputValue):
        returnValue = libpanda._inP5U4kJVnd(self.this, inputValue)
        return returnValue

    
    def fromVal(self, inputValue):
        returnValue = libpanda._inP5U4k78bW(self.this, inputValue)
        return returnValue

    
    def _PNMImage__overloaded_clear_ptrPNMImage(self):
        returnValue = libpanda._inP5U4kgRyO(self.this)
        return returnValue

    
    def _PNMImage__overloaded_clear_ptrPNMImage_int_int_int_shortUnsignedshortint_ptrPNMFileType(self, xSize, ySize, numChannels, maxval, type):
        returnValue = libpanda._inP5U4kFn3z(self.this, xSize, ySize, numChannels, maxval, type.this)
        return returnValue

    
    def _PNMImage__overloaded_clear_ptrPNMImage_int_int_int_shortUnsignedshortint(self, xSize, ySize, numChannels, maxval):
        returnValue = libpanda._inP5U4k32h2(self.this, xSize, ySize, numChannels, maxval)
        return returnValue

    
    def _PNMImage__overloaded_clear_ptrPNMImage_int_int_int(self, xSize, ySize, numChannels):
        returnValue = libpanda._inP5U4kJDi_(self.this, xSize, ySize, numChannels)
        return returnValue

    
    def _PNMImage__overloaded_clear_ptrPNMImage_int_int(self, xSize, ySize):
        returnValue = libpanda._inP5U4kJQp3(self.this, xSize, ySize)
        return returnValue

    
    def copyFrom(self, copy):
        returnValue = libpanda._inP5U4k1EcB(self.this, copy.this)
        return returnValue

    
    def copyHeaderFrom(self, header):
        returnValue = libpanda._inP5U4kfIQ5(self.this, header.this)
        return returnValue

    
    def _PNMImage__overloaded_fill_ptrPNMImage_double(self, gray):
        returnValue = libpanda._inP5U4kVQQT(self.this, gray)
        return returnValue

    
    def _PNMImage__overloaded_fill_ptrPNMImage(self):
        returnValue = libpanda._inP5U4k_Hno(self.this)
        return returnValue

    
    def _PNMImage__overloaded_fill_ptrPNMImage_double_double_double(self, red, green, blue):
        returnValue = libpanda._inP5U4kFZy4(self.this, red, green, blue)
        return returnValue

    
    def _PNMImage__overloaded_fillVal_ptrPNMImage_shortUnsignedshortint(self, gray):
        returnValue = libpanda._inP5U4k9TTf(self.this, gray)
        return returnValue

    
    def _PNMImage__overloaded_fillVal_ptrPNMImage(self):
        returnValue = libpanda._inP5U4kgsJ_(self.this)
        return returnValue

    
    def _PNMImage__overloaded_fillVal_ptrPNMImage_shortUnsignedshortint_shortUnsignedshortint_shortUnsignedshortint(self, red, green, blue):
        returnValue = libpanda._inP5U4kJAW_(self.this, red, green, blue)
        return returnValue

    
    def _PNMImage__overloaded_alphaFill_ptrPNMImage_double(self, alpha):
        returnValue = libpanda._inP5U4kJekT(self.this, alpha)
        return returnValue

    
    def _PNMImage__overloaded_alphaFill_ptrPNMImage(self):
        returnValue = libpanda._inP5U4kZk_o(self.this)
        return returnValue

    
    def _PNMImage__overloaded_alphaFillVal_ptrPNMImage_shortUnsignedshortint(self, alpha):
        returnValue = libpanda._inP5U4k_dAZ(self.this, alpha)
        return returnValue

    
    def _PNMImage__overloaded_alphaFillVal_ptrPNMImage(self):
        returnValue = libpanda._inP5U4k7C1N(self.this)
        return returnValue

    
    def _PNMImage__overloaded_read_ptrPNMImage_ptrConstFilename_ptrPNMFileType(self, filename, type):
        returnValue = libpanda._inP5U4kPAvM(self.this, filename.this, type.this)
        return returnValue

    
    def _PNMImage__overloaded_read_ptrPNMImage_ptrConstFilename(self, filename):
        returnValue = libpanda._inP5U4kvCUh(self.this, filename.this)
        return returnValue

    
    def _PNMImage__overloaded_read_ptrPNMImage_ptrPNMReader(self, reader):
        returnValue = libpanda._inP5U4kdJLw(self.this, reader.this)
        return returnValue

    
    def _PNMImage__overloaded_read_ptrPNMImage_ptrIstream_atomicstring_ptrPNMFileType(self, data, filename, type):
        returnValue = libpanda._inP5U4kwKxG(self.this, data.this, filename, type.this)
        return returnValue

    
    def _PNMImage__overloaded_read_ptrPNMImage_ptrIstream_atomicstring(self, data, filename):
        returnValue = libpanda._inP5U4kgtc5(self.this, data.this, filename)
        return returnValue

    
    def _PNMImage__overloaded_read_ptrPNMImage_ptrIstream(self, data):
        returnValue = libpanda._inP5U4k5luU(self.this, data.this)
        return returnValue

    
    def _PNMImage__overloaded_write_ptrConstPNMImage_ptrConstFilename_ptrPNMFileType(self, filename, type):
        returnValue = libpanda._inP5U4kryAQ(self.this, filename.this, type.this)
        return returnValue

    
    def _PNMImage__overloaded_write_ptrConstPNMImage_ptrConstFilename(self, filename):
        returnValue = libpanda._inP5U4kibdu(self.this, filename.this)
        return returnValue

    
    def _PNMImage__overloaded_write_ptrConstPNMImage_ptrPNMWriter(self, writer):
        returnValue = libpanda._inP5U4kl0d0(self.this, writer.this)
        return returnValue

    
    def _PNMImage__overloaded_write_ptrConstPNMImage_ptrOstream_atomicstring_ptrPNMFileType(self, data, filename, type):
        returnValue = libpanda._inP5U4k3I_7(self.this, data.this, filename, type.this)
        return returnValue

    
    def _PNMImage__overloaded_write_ptrConstPNMImage_ptrOstream_atomicstring(self, data, filename):
        returnValue = libpanda._inP5U4kSl_y(self.this, data.this, filename)
        return returnValue

    
    def _PNMImage__overloaded_write_ptrConstPNMImage_ptrOstream(self, data):
        returnValue = libpanda._inP5U4klWrL(self.this, data.this)
        return returnValue

    
    def isValid(self):
        returnValue = libpanda._inP5U4kbtI8(self.this)
        return returnValue

    
    def setNumChannels(self, numChannels):
        returnValue = libpanda._inP5U4kvlnH(self.this, numChannels)
        return returnValue

    
    def setColorType(self, colorType):
        returnValue = libpanda._inP5U4kHw_e(self.this, colorType)
        return returnValue

    
    def addAlpha(self):
        returnValue = libpanda._inP5U4kudkF(self.this)
        return returnValue

    
    def removeAlpha(self):
        returnValue = libpanda._inP5U4kuXS6(self.this)
        return returnValue

    
    def _PNMImage__overloaded_makeGrayscale_ptrPNMImage(self):
        returnValue = libpanda._inP5U4kvd8W(self.this)
        return returnValue

    
    def _PNMImage__overloaded_makeGrayscale_ptrPNMImage_double_double_double(self, rc, gc, bc):
        returnValue = libpanda._inP5U4ksKwX(self.this, rc, gc, bc)
        return returnValue

    
    def makeRgb(self):
        returnValue = libpanda._inP5U4kWxCH(self.this)
        return returnValue

    
    def setMaxval(self, maxval):
        returnValue = libpanda._inP5U4kqQ4f(self.this, maxval)
        return returnValue

    
    def getXelVal(self, x, y):
        returnValue = libpanda._inP5U4kZ_t1(self.this, x, y)
        import Xel
        returnObject = Xel.Xel(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _PNMImage__overloaded_setXelVal_ptrPNMImage_int_int_ptrConstXel(self, x, y, value):
        returnValue = libpanda._inP5U4kBLQe(self.this, x, y, value.this)
        return returnValue

    
    def _PNMImage__overloaded_setXelVal_ptrPNMImage_int_int_shortUnsignedshortint(self, x, y, gray):
        returnValue = libpanda._inP5U4kwSca(self.this, x, y, gray)
        return returnValue

    
    def _PNMImage__overloaded_setXelVal_ptrPNMImage_int_int_shortUnsignedshortint_shortUnsignedshortint_shortUnsignedshortint(self, x, y, r, g, b):
        returnValue = libpanda._inP5U4keokV(self.this, x, y, r, g, b)
        return returnValue

    
    def getRedVal(self, x, y):
        returnValue = libpanda._inP5U4kvbnu(self.this, x, y)
        return returnValue

    
    def getGreenVal(self, x, y):
        returnValue = libpanda._inP5U4kim_o(self.this, x, y)
        return returnValue

    
    def getBlueVal(self, x, y):
        returnValue = libpanda._inP5U4kfY0A(self.this, x, y)
        return returnValue

    
    def getGrayVal(self, x, y):
        returnValue = libpanda._inP5U4k3oeE(self.this, x, y)
        return returnValue

    
    def getAlphaVal(self, x, y):
        returnValue = libpanda._inP5U4kKba3(self.this, x, y)
        return returnValue

    
    def setRedVal(self, x, y, r):
        returnValue = libpanda._inP5U4kB1WT(self.this, x, y, r)
        return returnValue

    
    def setGreenVal(self, x, y, g):
        returnValue = libpanda._inP5U4k4_Bi(self.this, x, y, g)
        return returnValue

    
    def setBlueVal(self, x, y, b):
        returnValue = libpanda._inP5U4kq9d9(self.this, x, y, b)
        return returnValue

    
    def setGrayVal(self, x, y, gray):
        returnValue = libpanda._inP5U4kjFIB(self.this, x, y, gray)
        return returnValue

    
    def setAlphaVal(self, x, y, a):
        returnValue = libpanda._inP5U4kjmcw(self.this, x, y, a)
        return returnValue

    
    def getChannelVal(self, x, y, channel):
        returnValue = libpanda._inP5U4k5dxI(self.this, x, y, channel)
        return returnValue

    
    def setChannelVal(self, x, y, channel, value):
        returnValue = libpanda._inP5U4k4AHG(self.this, x, y, channel, value)
        return returnValue

    
    def getXel(self, x, y):
        returnValue = libpanda._inP5U4kE1Ub(self.this, x, y)
        import VBase3D
        returnObject = VBase3D.VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _PNMImage__overloaded_setXel_ptrPNMImage_int_int_ptrConstLVecBase3d(self, x, y, value):
        returnValue = libpanda._inP5U4klCyT(self.this, x, y, value.this)
        return returnValue

    
    def _PNMImage__overloaded_setXel_ptrPNMImage_int_int_double(self, x, y, gray):
        returnValue = libpanda._inP5U4kkAzw(self.this, x, y, gray)
        return returnValue

    
    def _PNMImage__overloaded_setXel_ptrPNMImage_int_int_double_double_double(self, x, y, r, g, b):
        returnValue = libpanda._inP5U4kJNjN(self.this, x, y, r, g, b)
        return returnValue

    
    def getRed(self, x, y):
        returnValue = libpanda._inP5U4k2WPU(self.this, x, y)
        return returnValue

    
    def getGreen(self, x, y):
        returnValue = libpanda._inP5U4khyC9(self.this, x, y)
        return returnValue

    
    def getBlue(self, x, y):
        returnValue = libpanda._inP5U4kWrcz(self.this, x, y)
        return returnValue

    
    def getGray(self, x, y):
        returnValue = libpanda._inP5U4k55I3(self.this, x, y)
        return returnValue

    
    def getAlpha(self, x, y):
        returnValue = libpanda._inP5U4ka6eL(self.this, x, y)
        return returnValue

    
    def setRed(self, x, y, r):
        returnValue = libpanda._inP5U4kWqtp(self.this, x, y, r)
        return returnValue

    
    def setGreen(self, x, y, g):
        returnValue = libpanda._inP5U4k2K1_(self.this, x, y, g)
        return returnValue

    
    def setBlue(self, x, y, b):
        returnValue = libpanda._inP5U4kr0aG(self.this, x, y, b)
        return returnValue

    
    def setGray(self, x, y, gray):
        returnValue = libpanda._inP5U4kiwGK(self.this, x, y, gray)
        return returnValue

    
    def setAlpha(self, x, y, a):
        returnValue = libpanda._inP5U4k9QPO(self.this, x, y, a)
        return returnValue

    
    def getChannel(self, x, y, channel):
        returnValue = libpanda._inP5U4kjZD3(self.this, x, y, channel)
        return returnValue

    
    def setChannel(self, x, y, channel, value):
        returnValue = libpanda._inP5U4kPshy(self.this, x, y, channel, value)
        return returnValue

    
    def _PNMImage__overloaded_getBright_ptrConstPNMImage_int_int(self, x, y):
        returnValue = libpanda._inP5U4kcpGI(self.this, x, y)
        return returnValue

    
    def _PNMImage__overloaded_getBright_ptrConstPNMImage_int_int_double_double_double(self, x, y, rc, gc, bc):
        returnValue = libpanda._inP5U4kN9Lp(self.this, x, y, rc, gc, bc)
        return returnValue

    
    def _PNMImage__overloaded_getBright_ptrConstPNMImage_int_int_double_double_double_double(self, x, y, rc, gc, bc, ac):
        returnValue = libpanda._inP5U4k1KaX(self.this, x, y, rc, gc, bc, ac)
        return returnValue

    
    def _PNMImage__overloaded_blend_ptrPNMImage_int_int_ptrConstLVecBase3d_double(self, x, y, val, alpha):
        returnValue = libpanda._inP5U4kVicO(self.this, x, y, val.this, alpha)
        return returnValue

    
    def _PNMImage__overloaded_blend_ptrPNMImage_int_int_double_double_double_double(self, x, y, r, g, b, alpha):
        returnValue = libpanda._inP5U4k9I6e(self.this, x, y, r, g, b, alpha)
        return returnValue

    
    def _PNMImage__overloaded___getitem___ptrPNMImage_int(self, y):
        returnValue = libpanda._inP5U4k_EKA(self.this, y)
        import Xel
        returnObject = Xel.Xel(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _PNMImage__overloaded___getitem___ptrConstPNMImage_int(self, y):
        returnValue = libpanda._inP5U4kwxq_(self.this, y)
        import Xel
        returnObject = Xel.Xel(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _PNMImage__overloaded_copySubImage_ptrPNMImage_ptrConstPNMImage_int_int_int_int_int_int(self, copy, xto, yto, xfrom, yfrom, xSize, ySize):
        returnValue = libpanda._inP5U4kiW_W(self.this, copy.this, xto, yto, xfrom, yfrom, xSize, ySize)
        return returnValue

    
    def _PNMImage__overloaded_copySubImage_ptrPNMImage_ptrConstPNMImage_int_int_int_int_int(self, copy, xto, yto, xfrom, yfrom, xSize):
        returnValue = libpanda._inP5U4kxEW3(self.this, copy.this, xto, yto, xfrom, yfrom, xSize)
        return returnValue

    
    def _PNMImage__overloaded_copySubImage_ptrPNMImage_ptrConstPNMImage_int_int_int_int(self, copy, xto, yto, xfrom, yfrom):
        returnValue = libpanda._inP5U4kWkin(self.this, copy.this, xto, yto, xfrom, yfrom)
        return returnValue

    
    def _PNMImage__overloaded_copySubImage_ptrPNMImage_ptrConstPNMImage_int_int_int(self, copy, xto, yto, xfrom):
        returnValue = libpanda._inP5U4kXAof(self.this, copy.this, xto, yto, xfrom)
        return returnValue

    
    def _PNMImage__overloaded_copySubImage_ptrPNMImage_ptrConstPNMImage_int_int(self, copy, xto, yto):
        returnValue = libpanda._inP5U4krmrb(self.this, copy.this, xto, yto)
        return returnValue

    
    def _PNMImage__overloaded_blendSubImage_ptrPNMImage_ptrConstPNMImage_int_int_int_int_int_int(self, copy, xto, yto, xfrom, yfrom, xSize, ySize):
        returnValue = libpanda._inP5U4knnVh(self.this, copy.this, xto, yto, xfrom, yfrom, xSize, ySize)
        return returnValue

    
    def _PNMImage__overloaded_blendSubImage_ptrPNMImage_ptrConstPNMImage_int_int_int_int_int(self, copy, xto, yto, xfrom, yfrom, xSize):
        returnValue = libpanda._inP5U4k_Jps(self.this, copy.this, xto, yto, xfrom, yfrom, xSize)
        return returnValue

    
    def _PNMImage__overloaded_blendSubImage_ptrPNMImage_ptrConstPNMImage_int_int_int_int(self, copy, xto, yto, xfrom, yfrom):
        returnValue = libpanda._inP5U4k9rTy(self.this, copy.this, xto, yto, xfrom, yfrom)
        return returnValue

    
    def _PNMImage__overloaded_blendSubImage_ptrPNMImage_ptrConstPNMImage_int_int_int(self, copy, xto, yto, xfrom):
        returnValue = libpanda._inP5U4kHoI1(self.this, copy.this, xto, yto, xfrom)
        return returnValue

    
    def _PNMImage__overloaded_blendSubImage_ptrPNMImage_ptrConstPNMImage_int_int(self, copy, xto, yto):
        returnValue = libpanda._inP5U4k5Bk2(self.this, copy.this, xto, yto)
        return returnValue

    
    def _PNMImage__overloaded_boxFilter_ptrPNMImage_double(self, radius):
        returnValue = libpanda._inP5U4k0QpA(self.this, radius)
        return returnValue

    
    def _PNMImage__overloaded_boxFilter_ptrPNMImage(self):
        returnValue = libpanda._inP5U4kKBDW(self.this)
        return returnValue

    
    def _PNMImage__overloaded_gaussianFilter_ptrPNMImage_double(self, radius):
        returnValue = libpanda._inP5U4kSjEC(self.this, radius)
        return returnValue

    
    def _PNMImage__overloaded_gaussianFilter_ptrPNMImage(self):
        returnValue = libpanda._inP5U4kN02s(self.this)
        return returnValue

    
    def boxFilterFrom(self, radius, copy):
        returnValue = libpanda._inP5U4kPYod(self.this, radius, copy.this)
        return returnValue

    
    def gaussianFilterFrom(self, radius, copy):
        returnValue = libpanda._inP5U4kRiE8(self.this, radius, copy.this)
        return returnValue

    
    def _PNMImage__overloaded_quickFilterFrom_ptrPNMImage_ptrConstPNMImage_int_int(self, copy, xborder, yborder):
        returnValue = libpanda._inP5U4k2C4m(self.this, copy.this, xborder, yborder)
        return returnValue

    
    def _PNMImage__overloaded_quickFilterFrom_ptrPNMImage_ptrConstPNMImage_int(self, copy, xborder):
        returnValue = libpanda._inP5U4kocJ5(self.this, copy.this, xborder)
        return returnValue

    
    def _PNMImage__overloaded_quickFilterFrom_ptrPNMImage_ptrConstPNMImage(self, copy):
        returnValue = libpanda._inP5U4kRBRi(self.this, copy.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PNMImage__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], PNMImage):
                return self._PNMImage__overloaded_constructor_ptrConstPNMImage(*_args)
            
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._PNMImage__overloaded_constructor_ptrConstFilename(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <PNMImage> <Filename.Filename> '
        elif numArgs == 2:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._PNMImage__overloaded_constructor_int_int(*_args)
            
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._PNMImage__overloaded_constructor_ptrConstFilename_ptrPNMFileType(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <Filename.Filename> '
        elif numArgs == 3:
            return self._PNMImage__overloaded_constructor_int_int_int(*_args)
        elif numArgs == 4:
            return self._PNMImage__overloaded_constructor_int_int_int_shortUnsignedshortint(*_args)
        elif numArgs == 5:
            return self._PNMImage__overloaded_constructor_int_int_int_shortUnsignedshortint_ptrPNMFileType(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 3 4 5 '

    
    def alphaFillVal(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PNMImage__overloaded_alphaFillVal_ptrPNMImage(*_args)
        elif numArgs == 1:
            return self._PNMImage__overloaded_alphaFillVal_ptrPNMImage_shortUnsignedshortint(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PNMWriter
            if isinstance(_args[0], PNMWriter.PNMWriter):
                return self._PNMImage__overloaded_write_ptrConstPNMImage_ptrPNMWriter(*_args)
            
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._PNMImage__overloaded_write_ptrConstPNMImage_ptrOstream(*_args)
            
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._PNMImage__overloaded_write_ptrConstPNMImage_ptrConstFilename(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <PNMWriter.PNMWriter> <Ostream.Ostream> <Filename.Filename> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._PNMImage__overloaded_write_ptrConstPNMImage_ptrOstream_atomicstring(*_args)
            
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._PNMImage__overloaded_write_ptrConstPNMImage_ptrConstFilename_ptrPNMFileType(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> <Filename.Filename> '
        elif numArgs == 3:
            return self._PNMImage__overloaded_write_ptrConstPNMImage_ptrOstream_atomicstring_ptrPNMFileType(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

    
    def __getitem__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._PNMImage__overloaded___getitem___ptrConstPNMImage_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def blendSubImage(self, *_args):
        numArgs = len(_args)
        if numArgs == 3:
            return self._PNMImage__overloaded_blendSubImage_ptrPNMImage_ptrConstPNMImage_int_int(*_args)
        elif numArgs == 4:
            return self._PNMImage__overloaded_blendSubImage_ptrPNMImage_ptrConstPNMImage_int_int_int(*_args)
        elif numArgs == 5:
            return self._PNMImage__overloaded_blendSubImage_ptrPNMImage_ptrConstPNMImage_int_int_int_int(*_args)
        elif numArgs == 6:
            return self._PNMImage__overloaded_blendSubImage_ptrPNMImage_ptrConstPNMImage_int_int_int_int_int(*_args)
        elif numArgs == 7:
            return self._PNMImage__overloaded_blendSubImage_ptrPNMImage_ptrConstPNMImage_int_int_int_int_int_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 5 6 7 '

    
    def read(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PNMReader
            if isinstance(_args[0], PNMReader.PNMReader):
                return self._PNMImage__overloaded_read_ptrPNMImage_ptrPNMReader(*_args)
            
            import Istream
            if isinstance(_args[0], Istream.Istream):
                return self._PNMImage__overloaded_read_ptrPNMImage_ptrIstream(*_args)
            
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._PNMImage__overloaded_read_ptrPNMImage_ptrConstFilename(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <PNMReader.PNMReader> <Istream.Istream> <Filename.Filename> '
        elif numArgs == 2:
            import Istream
            if isinstance(_args[0], Istream.Istream):
                return self._PNMImage__overloaded_read_ptrPNMImage_ptrIstream_atomicstring(*_args)
            
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._PNMImage__overloaded_read_ptrPNMImage_ptrConstFilename_ptrPNMFileType(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Istream.Istream> <Filename.Filename> '
        elif numArgs == 3:
            return self._PNMImage__overloaded_read_ptrPNMImage_ptrIstream_atomicstring_ptrPNMFileType(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

    
    def setXelVal(self, *_args):
        numArgs = len(_args)
        if numArgs == 3:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                if isinstance(_args[1], types.IntType) or isinstance(_args[1], types.LongType):
                    if isinstance(_args[2], types.IntType) or isinstance(_args[2], types.LongType):
                        return self._PNMImage__overloaded_setXelVal_ptrPNMImage_int_int_shortUnsignedshortint(*_args)
                    
                    import Xel
                    if isinstance(_args[2], Xel.Xel):
                        return self._PNMImage__overloaded_setXelVal_ptrPNMImage_int_int_ptrConstXel(*_args)
                    
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Xel.Xel> '
                
                raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 5:
            return self._PNMImage__overloaded_setXelVal_ptrPNMImage_int_int_shortUnsignedshortint_shortUnsignedshortint_shortUnsignedshortint(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 5 '

    
    def clear(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PNMImage__overloaded_clear_ptrPNMImage(*_args)
        elif numArgs == 2:
            return self._PNMImage__overloaded_clear_ptrPNMImage_int_int(*_args)
        elif numArgs == 3:
            return self._PNMImage__overloaded_clear_ptrPNMImage_int_int_int(*_args)
        elif numArgs == 4:
            return self._PNMImage__overloaded_clear_ptrPNMImage_int_int_int_shortUnsignedshortint(*_args)
        elif numArgs == 5:
            return self._PNMImage__overloaded_clear_ptrPNMImage_int_int_int_shortUnsignedshortint_ptrPNMFileType(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 2 3 4 5 '

    
    def quickFilterFrom(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._PNMImage__overloaded_quickFilterFrom_ptrPNMImage_ptrConstPNMImage(*_args)
        elif numArgs == 2:
            return self._PNMImage__overloaded_quickFilterFrom_ptrPNMImage_ptrConstPNMImage_int(*_args)
        elif numArgs == 3:
            return self._PNMImage__overloaded_quickFilterFrom_ptrPNMImage_ptrConstPNMImage_int_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

    
    def setXel(self, *_args):
        numArgs = len(_args)
        if numArgs == 3:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                if isinstance(_args[1], types.IntType) or isinstance(_args[1], types.LongType):
                    if isinstance(_args[2], types.FloatType) and isinstance(_args[2], types.IntType) or isinstance(_args[2], types.LongType):
                        return self._PNMImage__overloaded_setXel_ptrPNMImage_int_int_double(*_args)
                    
                    import VBase3D
                    if isinstance(_args[2], VBase3D.VBase3D):
                        return self._PNMImage__overloaded_setXel_ptrPNMImage_int_int_ptrConstLVecBase3d(*_args)
                    
                    raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> <VBase3D.VBase3D> '
                
                raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 5:
            return self._PNMImage__overloaded_setXel_ptrPNMImage_int_int_double_double_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 5 '

    
    def boxFilter(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PNMImage__overloaded_boxFilter_ptrPNMImage(*_args)
        elif numArgs == 1:
            return self._PNMImage__overloaded_boxFilter_ptrPNMImage_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getBright(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._PNMImage__overloaded_getBright_ptrConstPNMImage_int_int(*_args)
        elif numArgs == 5:
            return self._PNMImage__overloaded_getBright_ptrConstPNMImage_int_int_double_double_double(*_args)
        elif numArgs == 6:
            return self._PNMImage__overloaded_getBright_ptrConstPNMImage_int_int_double_double_double_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 5 6 '

    
    def makeGrayscale(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PNMImage__overloaded_makeGrayscale_ptrPNMImage(*_args)
        elif numArgs == 3:
            return self._PNMImage__overloaded_makeGrayscale_ptrPNMImage_double_double_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 3 '

    
    def alphaFill(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PNMImage__overloaded_alphaFill_ptrPNMImage(*_args)
        elif numArgs == 1:
            return self._PNMImage__overloaded_alphaFill_ptrPNMImage_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def fillVal(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PNMImage__overloaded_fillVal_ptrPNMImage(*_args)
        elif numArgs == 1:
            return self._PNMImage__overloaded_fillVal_ptrPNMImage_shortUnsignedshortint(*_args)
        elif numArgs == 3:
            return self._PNMImage__overloaded_fillVal_ptrPNMImage_shortUnsignedshortint_shortUnsignedshortint_shortUnsignedshortint(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 3 '

    
    def copySubImage(self, *_args):
        numArgs = len(_args)
        if numArgs == 3:
            return self._PNMImage__overloaded_copySubImage_ptrPNMImage_ptrConstPNMImage_int_int(*_args)
        elif numArgs == 4:
            return self._PNMImage__overloaded_copySubImage_ptrPNMImage_ptrConstPNMImage_int_int_int(*_args)
        elif numArgs == 5:
            return self._PNMImage__overloaded_copySubImage_ptrPNMImage_ptrConstPNMImage_int_int_int_int(*_args)
        elif numArgs == 6:
            return self._PNMImage__overloaded_copySubImage_ptrPNMImage_ptrConstPNMImage_int_int_int_int_int(*_args)
        elif numArgs == 7:
            return self._PNMImage__overloaded_copySubImage_ptrPNMImage_ptrConstPNMImage_int_int_int_int_int_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 5 6 7 '

    
    def blend(self, *_args):
        numArgs = len(_args)
        if numArgs == 4:
            return self._PNMImage__overloaded_blend_ptrPNMImage_int_int_ptrConstLVecBase3d_double(*_args)
        elif numArgs == 6:
            return self._PNMImage__overloaded_blend_ptrPNMImage_int_int_double_double_double_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 4 6 '

    
    def gaussianFilter(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PNMImage__overloaded_gaussianFilter_ptrPNMImage(*_args)
        elif numArgs == 1:
            return self._PNMImage__overloaded_gaussianFilter_ptrPNMImage_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def fill(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PNMImage__overloaded_fill_ptrPNMImage(*_args)
        elif numArgs == 1:
            return self._PNMImage__overloaded_fill_ptrPNMImage_double(*_args)
        elif numArgs == 3:
            return self._PNMImage__overloaded_fill_ptrPNMImage_double_double_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 3 '


