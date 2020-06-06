# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import DNANode

class DNASignBaseline(DNANode.DNANode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _DNASignBaseline__overloaded_constructor_ptrConstDNASignBaseline(self, sign):
        self.this = libtoontown._inPet4yzllq(sign.this)
        self.userManagesMemory = 1

    
    def _DNASignBaseline__overloaded_constructor_atomicstring(self, initialName):
        self.this = libtoontown._inPet4y3ZTT(initialName)
        self.userManagesMemory = 1

    
    def _DNASignBaseline__overloaded_constructor(self):
        self.this = libtoontown._inPet4yqnlX()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPet4yMYDv:
            libtoontown._inPet4yMYDv(self.this)
        

    
    def getClassType():
        returnValue = libtoontown._inPet4y6kHB()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setCode(self, code):
        returnValue = libtoontown._inPet4yQl8n(self.this, code)
        return returnValue

    
    def getCode(self):
        returnValue = libtoontown._inPet4yfXt1(self.this)
        return returnValue

    
    def setColor(self, color):
        returnValue = libtoontown._inPet4ytpch(self.this, color.this)
        return returnValue

    
    def getColor(self):
        returnValue = libtoontown._inPet4y80Vf(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setFont(self, font):
        returnValue = libtoontown._inPet4ysSVm(self.this, font.this)
        return returnValue

    
    def getFont(self):
        returnValue = libtoontown._inPet4ycqSf(self.this)
        import TextFont
        returnObject = TextFont.TextFont(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setIndent(self, indent):
        returnValue = libtoontown._inPet4yY_9C(self.this, indent)
        return returnValue

    
    def getIndent(self):
        returnValue = libtoontown._inPet4yiw_D(self.this)
        return returnValue

    
    def setKern(self, kern):
        returnValue = libtoontown._inPet4yDTpR(self.this, kern)
        return returnValue

    
    def getKern(self):
        returnValue = libtoontown._inPet4yx0nT(self.this)
        return returnValue

    
    def getCurrentKern(self):
        returnValue = libtoontown._inPet4yScMV(self.this)
        return returnValue

    
    def setWiggle(self, wiggle):
        returnValue = libtoontown._inPet4yMbX1(self.this, wiggle)
        return returnValue

    
    def getWiggle(self):
        returnValue = libtoontown._inPet4yDMa2(self.this)
        return returnValue

    
    def getCurrentWiggle(self):
        returnValue = libtoontown._inPet4yljiJ(self.this)
        return returnValue

    
    def setStumble(self, stumble):
        returnValue = libtoontown._inPet4yrvDo(self.this, stumble)
        return returnValue

    
    def getStumble(self):
        returnValue = libtoontown._inPet4yHj8K(self.this)
        return returnValue

    
    def getCurrentStumble(self):
        returnValue = libtoontown._inPet4yFa4q(self.this)
        return returnValue

    
    def setStomp(self, stomp):
        returnValue = libtoontown._inPet4ypFe_(self.this, stomp)
        return returnValue

    
    def getStomp(self):
        returnValue = libtoontown._inPet4yajf_(self.this)
        return returnValue

    
    def getCurrentStomp(self):
        returnValue = libtoontown._inPet4yUME1(self.this)
        return returnValue

    
    def setWidth(self, width):
        returnValue = libtoontown._inPet4yEA_Z(self.this, width)
        return returnValue

    
    def getWidth(self):
        returnValue = libtoontown._inPet4yXl_Z(self.this)
        return returnValue

    
    def setHeight(self, height):
        returnValue = libtoontown._inPet4ylSo_(self.this, height)
        return returnValue

    
    def getHeight(self):
        returnValue = libtoontown._inPet4y6BrA(self.this)
        return returnValue

    
    def setFlags(self, flags):
        returnValue = libtoontown._inPet4yaObB(self.this, flags)
        return returnValue

    
    def getFlags(self):
        returnValue = libtoontown._inPet4ygmx5(self.this)
        return returnValue

    
    def isFirstLetterOfWord(self, letter):
        returnValue = libtoontown._inPet4ykgKi(self.this, letter)
        return returnValue

    
    def resetCounter(self):
        returnValue = libtoontown._inPet4yMWmo(self.this)
        return returnValue

    
    def incCounter(self):
        returnValue = libtoontown._inPet4yzeoR(self.this)
        return returnValue

    
    def baselineNextPosHprScale(self, pos, hpr, scale, size):
        returnValue = libtoontown._inPet4yI_UE(self.this, pos.this, hpr.this, scale.this, size.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DNASignBaseline__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DNASignBaseline__overloaded_constructor_atomicstring(_args[0])
            elif isinstance(_args[0], DNASignBaseline):
                return self._DNASignBaseline__overloaded_constructor_ptrConstDNASignBaseline(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNASignBaseline> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


