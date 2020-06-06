# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import DNANode

class DNASignBaseline(DNANode.DNANode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _DNASignBaseline__overloaded_constructor_ptrConstDNASignBaseline(self, sign):
        self.this = libtoontown._inPdt4y0llq(sign.this)
        self.userManagesMemory = 1

    
    def _DNASignBaseline__overloaded_constructor_atomicstring(self, initialName):
        self.this = libtoontown._inPdt4y3ZTT(initialName)
        self.userManagesMemory = 1

    
    def _DNASignBaseline__overloaded_constructor(self):
        self.this = libtoontown._inPdt4yqnlX()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPdt4yNYDv:
            libtoontown._inPdt4yNYDv(self.this)
        

    
    def getClassType():
        returnValue = libtoontown._inPdt4y6kHB()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setCode(self, code):
        returnValue = libtoontown._inPdt4yTl8n(self.this, code)
        return returnValue

    
    def getCode(self):
        returnValue = libtoontown._inPdt4yeXt1(self.this)
        return returnValue

    
    def setColor(self, color):
        returnValue = libtoontown._inPdt4yupch(self.this, color.this)
        return returnValue

    
    def getColor(self):
        returnValue = libtoontown._inPdt4y80Vf(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setFont(self, font):
        returnValue = libtoontown._inPdt4yvSVm(self.this, font.this)
        return returnValue

    
    def getFont(self):
        returnValue = libtoontown._inPdt4ycqSf(self.this)
        import TextFont
        returnObject = TextFont.TextFont(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setIndent(self, indent):
        returnValue = libtoontown._inPdt4yY_9C(self.this, indent)
        return returnValue

    
    def getIndent(self):
        returnValue = libtoontown._inPdt4yiw_D(self.this)
        return returnValue

    
    def setKern(self, kern):
        returnValue = libtoontown._inPdt4yDTpR(self.this, kern)
        return returnValue

    
    def getKern(self):
        returnValue = libtoontown._inPdt4yx0nT(self.this)
        return returnValue

    
    def getCurrentKern(self):
        returnValue = libtoontown._inPdt4yScMV(self.this)
        return returnValue

    
    def setWiggle(self, wiggle):
        returnValue = libtoontown._inPdt4yNbX1(self.this, wiggle)
        return returnValue

    
    def getWiggle(self):
        returnValue = libtoontown._inPdt4yCMa2(self.this)
        return returnValue

    
    def getCurrentWiggle(self):
        returnValue = libtoontown._inPdt4yljiJ(self.this)
        return returnValue

    
    def setStumble(self, stumble):
        returnValue = libtoontown._inPdt4yqvDo(self.this, stumble)
        return returnValue

    
    def getStumble(self):
        returnValue = libtoontown._inPdt4yHj8K(self.this)
        return returnValue

    
    def getCurrentStumble(self):
        returnValue = libtoontown._inPdt4yEa4q(self.this)
        return returnValue

    
    def setStomp(self, stomp):
        returnValue = libtoontown._inPdt4yoFe_(self.this, stomp)
        return returnValue

    
    def getStomp(self):
        returnValue = libtoontown._inPdt4yZjf_(self.this)
        return returnValue

    
    def getCurrentStomp(self):
        returnValue = libtoontown._inPdt4yLME1(self.this)
        return returnValue

    
    def setWidth(self, width):
        returnValue = libtoontown._inPdt4yEA_Z(self.this, width)
        return returnValue

    
    def getWidth(self):
        returnValue = libtoontown._inPdt4yXl_Z(self.this)
        return returnValue

    
    def setHeight(self, height):
        returnValue = libtoontown._inPdt4yqSo_(self.this, height)
        return returnValue

    
    def getHeight(self):
        returnValue = libtoontown._inPdt4y6BrA(self.this)
        return returnValue

    
    def setFlags(self, flags):
        returnValue = libtoontown._inPdt4yaObB(self.this, flags)
        return returnValue

    
    def getFlags(self):
        returnValue = libtoontown._inPdt4yjmx5(self.this)
        return returnValue

    
    def isFirstLetterOfWord(self, letter):
        returnValue = libtoontown._inPdt4yngKi(self.this, letter)
        return returnValue

    
    def resetCounter(self):
        returnValue = libtoontown._inPdt4yNWmo(self.this)
        return returnValue

    
    def incCounter(self):
        returnValue = libtoontown._inPdt4yzeoR(self.this)
        return returnValue

    
    def baselineNextPosHprScale(self, pos, hpr, scale, size):
        returnValue = libtoontown._inPdt4yI_UE(self.this, pos.this, hpr.this, scale.this, size.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DNASignBaseline__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DNASignBaseline__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], DNASignBaseline):
                return self._DNASignBaseline__overloaded_constructor_ptrConstDNASignBaseline(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNASignBaseline> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


