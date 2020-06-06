# File: T (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedWritableReferenceCount

class TextureStage(TypedWritableReferenceCount.TypedWritableReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    MAdd = 4
    MReplace = 3
    MDecal = 1
    MCombine = 5
    MBlend = 2
    MModulate = 0
    CMDot3Rgba = 8
    CMDot3Rgb = 7
    CMUndefined = 0
    CMInterpolate = 5
    CMReplace = 1
    CMAdd = 3
    CMAddSigned = 4
    CMModulate = 2
    CMSubtract = 6
    CSConstant = 2
    CSTexture = 1
    CSPrimaryColor = 3
    CSPrevious = 4
    CSUndefined = 0
    COUndefined = 0
    COOneMinusSrcAlpha = 4
    COOneMinusSrcColor = 2
    COSrcAlpha = 3
    COSrcColor = 1
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _TextureStage__overloaded_constructor_ptrTextureStage(self, copy):
        self.this = libpanda._inPMAKPb46Y(copy.this)
        self.userManagesMemory = 1

    
    def _TextureStage__overloaded_constructor_atomicstring(self, name):
        self.this = libpanda._inPMAKPMbzz(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getDefault():
        returnValue = libpanda._inPMAKPHR5s()
        returnObject = TextureStage(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    getDefault = staticmethod(getDefault)
    
    def getSortSeq():
        returnValue = libpanda._inPMAKPs_II()
        import UpdateSeq
        returnObject = UpdateSeq.UpdateSeq(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getSortSeq = staticmethod(getSortSeq)
    
    def getClassType():
        returnValue = libpanda._inPMAKPpjIT()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setName(self, name):
        returnValue = libpanda._inPMAKPCd_b(self.this, name)
        return returnValue

    
    def getName(self):
        returnValue = libpanda._inPMAKPqybK(self.this)
        return returnValue

    
    def setSort(self, sort):
        returnValue = libpanda._inPMAKPx_xd(self.this, sort)
        return returnValue

    
    def getSort(self):
        returnValue = libpanda._inPMAKPediB(self.this)
        return returnValue

    
    def setPriority(self, priority):
        returnValue = libpanda._inPMAKP53u_(self.this, priority)
        return returnValue

    
    def getPriority(self):
        returnValue = libpanda._inPMAKPvd5l(self.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPMAKPc8r6(self.this, other.this)
        return returnValue

    
    def assign(self, copy):
        returnValue = libpanda._inPMAKPAOWV(self.this, copy.this)
        returnObject = TextureStage(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _TextureStage__overloaded_setTexcoordName_ptrTextureStage_ptrConstTexCoordName(self, name):
        returnValue = libpanda._inPMAKPpBUC(self.this, name.this)
        return returnValue

    
    def _TextureStage__overloaded_setTexcoordName_ptrTextureStage_atomicstring(self, texcoordName):
        returnValue = libpanda._inPMAKPSh4R(self.this, texcoordName)
        return returnValue

    
    def getTexcoordName(self):
        returnValue = libpanda._inPMAKP6ntn(self.this)
        import TexCoordName
        returnObject = TexCoordName.TexCoordName(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setMode(self, mode):
        returnValue = libpanda._inPMAKP_lwU(self.this, mode)
        return returnValue

    
    def getMode(self):
        returnValue = libpanda._inPMAKPHG0A(self.this)
        return returnValue

    
    def setColor(self, color):
        returnValue = libpanda._inPMAKPtRyD(self.this, color.this)
        return returnValue

    
    def getColor(self):
        returnValue = libpanda._inPMAKPX3mA(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _TextureStage__overloaded_setCombineRgb_ptrTextureStage___enum__CombineMode___enum__CombineSource___enum__CombineOperand(self, mode, source0, operand0):
        returnValue = libpanda._inPMAKPjFHN(self.this, mode, source0, operand0)
        return returnValue

    
    def _TextureStage__overloaded_setCombineRgb_ptrTextureStage___enum__CombineMode___enum__CombineSource___enum__CombineOperand___enum__CombineSource___enum__CombineOperand(self, mode, source0, operand0, source1, operand1):
        returnValue = libpanda._inPMAKPgYLT(self.this, mode, source0, operand0, source1, operand1)
        return returnValue

    
    def _TextureStage__overloaded_setCombineRgb_ptrTextureStage___enum__CombineMode___enum__CombineSource___enum__CombineOperand___enum__CombineSource___enum__CombineOperand___enum__CombineSource___enum__CombineOperand(self, mode, source0, operand0, source1, operand1, source2, operand2):
        returnValue = libpanda._inPMAKPmXix(self.this, mode, source0, operand0, source1, operand1, source2, operand2)
        return returnValue

    
    def getCombineRgbMode(self):
        returnValue = libpanda._inPMAKP0fyd(self.this)
        return returnValue

    
    def getNumCombineRgbOperands(self):
        returnValue = libpanda._inPMAKPIBF9(self.this)
        return returnValue

    
    def getCombineRgbSource0(self):
        returnValue = libpanda._inPMAKPqKNk(self.this)
        return returnValue

    
    def getCombineRgbOperand0(self):
        returnValue = libpanda._inPMAKPNrxE(self.this)
        return returnValue

    
    def getCombineRgbSource1(self):
        returnValue = libpanda._inPMAKPrKSy(self.this)
        return returnValue

    
    def getCombineRgbOperand1(self):
        returnValue = libpanda._inPMAKPkrRI(self.this)
        return returnValue

    
    def getCombineRgbSource2(self):
        returnValue = libpanda._inPMAKPpKbA(self.this)
        return returnValue

    
    def getCombineRgbOperand2(self):
        returnValue = libpanda._inPMAKP7oxL(self.this)
        return returnValue

    
    def _TextureStage__overloaded_setCombineAlpha_ptrTextureStage___enum__CombineMode___enum__CombineSource___enum__CombineOperand(self, mode, source0, operand0):
        returnValue = libpanda._inPMAKPrsCd(self.this, mode, source0, operand0)
        return returnValue

    
    def _TextureStage__overloaded_setCombineAlpha_ptrTextureStage___enum__CombineMode___enum__CombineSource___enum__CombineOperand___enum__CombineSource___enum__CombineOperand(self, mode, source0, operand0, source1, operand1):
        returnValue = libpanda._inPMAKPuvSR(self.this, mode, source0, operand0, source1, operand1)
        return returnValue

    
    def _TextureStage__overloaded_setCombineAlpha_ptrTextureStage___enum__CombineMode___enum__CombineSource___enum__CombineOperand___enum__CombineSource___enum__CombineOperand___enum__CombineSource___enum__CombineOperand(self, mode, source0, operand0, source1, operand1, source2, operand2):
        returnValue = libpanda._inPMAKPjhJH(self.this, mode, source0, operand0, source1, operand1, source2, operand2)
        return returnValue

    
    def getCombineAlphaMode(self):
        returnValue = libpanda._inPMAKPTu_C(self.this)
        return returnValue

    
    def getNumCombineAlphaOperands(self):
        returnValue = libpanda._inPMAKPOFQQ(self.this)
        return returnValue

    
    def getCombineAlphaSource0(self):
        returnValue = libpanda._inPMAKPqzUQ(self.this)
        return returnValue

    
    def getCombineAlphaOperand0(self):
        returnValue = libpanda._inPMAKP7D7X(self.this)
        return returnValue

    
    def getCombineAlphaSource1(self):
        returnValue = libpanda._inPMAKPEkUA(self.this)
        return returnValue

    
    def getCombineAlphaOperand1(self):
        returnValue = libpanda._inPMAKPDSFY(self.this)
        return returnValue

    
    def getCombineAlphaSource2(self):
        returnValue = libpanda._inPMAKPuaUw(self.this)
        return returnValue

    
    def getCombineAlphaOperand2(self):
        returnValue = libpanda._inPMAKPLhOY(self.this)
        return returnValue

    
    def write(self, out):
        returnValue = libpanda._inPMAKPMLKu(self.this, out.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPMAKPkmyF(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._TextureStage__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], TextureStage):
                return self._TextureStage__overloaded_constructor_ptrTextureStage(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <TextureStage> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def setCombineAlpha(self, *_args):
        numArgs = len(_args)
        if numArgs == 3:
            return self._TextureStage__overloaded_setCombineAlpha_ptrTextureStage___enum__CombineMode___enum__CombineSource___enum__CombineOperand(*_args)
        elif numArgs == 5:
            return self._TextureStage__overloaded_setCombineAlpha_ptrTextureStage___enum__CombineMode___enum__CombineSource___enum__CombineOperand___enum__CombineSource___enum__CombineOperand(*_args)
        elif numArgs == 7:
            return self._TextureStage__overloaded_setCombineAlpha_ptrTextureStage___enum__CombineMode___enum__CombineSource___enum__CombineOperand___enum__CombineSource___enum__CombineOperand___enum__CombineSource___enum__CombineOperand(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 5 7 '

    
    def setTexcoordName(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._TextureStage__overloaded_setTexcoordName_ptrTextureStage_atomicstring(*_args)
            
            import TexCoordName
            if isinstance(_args[0], TexCoordName.TexCoordName):
                return self._TextureStage__overloaded_setTexcoordName_ptrTextureStage_ptrConstTexCoordName(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <TexCoordName.TexCoordName> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def setCombineRgb(self, *_args):
        numArgs = len(_args)
        if numArgs == 3:
            return self._TextureStage__overloaded_setCombineRgb_ptrTextureStage___enum__CombineMode___enum__CombineSource___enum__CombineOperand(*_args)
        elif numArgs == 5:
            return self._TextureStage__overloaded_setCombineRgb_ptrTextureStage___enum__CombineMode___enum__CombineSource___enum__CombineOperand___enum__CombineSource___enum__CombineOperand(*_args)
        elif numArgs == 7:
            return self._TextureStage__overloaded_setCombineRgb_ptrTextureStage___enum__CombineMode___enum__CombineSource___enum__CombineOperand___enum__CombineSource___enum__CombineOperand___enum__CombineSource___enum__CombineOperand(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 5 7 '


