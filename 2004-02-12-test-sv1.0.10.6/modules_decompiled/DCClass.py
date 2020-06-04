# File: D (Python 2.2)

import types
import libdirect
import libdirectDowncasts
import FFIExternalObject

class DCClass(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libdirectDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libdirect and libdirect._inP5HfQ11Cw:
            libdirect._inP5HfQ11Cw(self.this)
        

    
    def getNumber(self):
        returnValue = libdirect._inP5HfQ7r2k(self.this)
        return returnValue

    
    def getName(self):
        returnValue = libdirect._inP5HfQBfkV(self.this)
        return returnValue

    
    def hasParent(self):
        returnValue = libdirect._inP5HfQ5Lb8(self.this)
        return returnValue

    
    def getParent(self):
        returnValue = libdirect._inP5HfQ0pIH(self.this)
        returnObject = DCClass(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNumFields(self):
        returnValue = libdirect._inP5HfQ6prE(self.this)
        return returnValue

    
    def getField(self, n):
        returnValue = libdirect._inP5HfQSfGD(self.this, n)
        import DCField
        returnObject = DCField.DCField(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getFieldByName(self, name):
        returnValue = libdirect._inP5HfQJ8KR(self.this, name)
        import DCField
        returnObject = DCField.DCField(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNumInheritedFields(self):
        returnValue = libdirect._inP5HfQTQ1_(self.this)
        return returnValue

    
    def getInheritedField(self, n):
        returnValue = libdirect._inP5HfQ4vTD(self.this, n)
        import DCField
        returnObject = DCField.DCField(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject


