# File: D (Python 2.2)

import types
import libdirect
import libdirectDowncasts
from direct.ffi import FFIExternalObject
import DCDeclaration

class DCSwitch(DCDeclaration.DCDeclaration, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libdirectDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libdirect and libdirect._inP5HfQ9AVj:
            libdirect._inP5HfQ9AVj(self.this)
        

    
    def getName(self):
        returnValue = libdirect._inP5HfQ5_NH(self.this)
        return returnValue

    
    def getKeyParameter(self):
        returnValue = libdirect._inP5HfQXw_6(self.this)
        import DCParameter
        returnObject = DCParameter.DCParameter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNumCases(self):
        returnValue = libdirect._inP5HfQeUzc(self.this)
        return returnValue

    
    def getCaseByValue(self, caseValue):
        returnValue = libdirect._inP5HfQ0ls8(self.this, caseValue)
        return returnValue

    
    def getCase(self, n):
        returnValue = libdirect._inP5HfQt2ll(self.this, n)
        import DCPackerInterface
        returnObject = DCPackerInterface.DCPackerInterface(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getValue(self, caseIndex):
        returnValue = libdirect._inP5HfQTRGr(self.this, caseIndex)
        return returnValue

    
    def getNumFields(self, caseIndex):
        returnValue = libdirect._inP5HfQlF1x(self.this, caseIndex)
        return returnValue

    
    def getField(self, caseIndex, n):
        returnValue = libdirect._inP5HfQJzsC(self.this, caseIndex, n)
        import DCField
        returnObject = DCField.DCField(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getFieldByName(self, caseIndex, name):
        returnValue = libdirect._inP5HfQwD_J(self.this, caseIndex, name)
        import DCField
        returnObject = DCField.DCField(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject


