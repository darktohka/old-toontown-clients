# File: T (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class TypeHandle(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _TypeHandle__overloaded_constructor(self):
        self.this = libpandaexpress._inPKoxtN5ho()
        self.userManagesMemory = 1

    
    def _TypeHandle__overloaded_constructor_ptrConstTypeHandle(self, copy):
        self.this = libpandaexpress._inPKoxtGniZ(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxtWx5B:
            libpandaexpress._inPKoxtWx5B(self.this)
        

    
    def none():
        returnValue = libpandaexpress._inPKoxtp1S_()
        returnObject = TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    none = staticmethod(none)
    
    def eq(self, other):
        returnValue = libpandaexpress._inPKoxtxgMZ(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpandaexpress._inPKoxt9A0H(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpandaexpress._inPKoxt0HOQ(self.this, other.this)
        return returnValue

    
    def lessThanOrEqual(self, other):
        returnValue = libpandaexpress._inPKoxtx4bP(self.this, other.this)
        return returnValue

    
    def greaterThan(self, other):
        returnValue = libpandaexpress._inPKoxt0Xwj(self.this, other.this)
        return returnValue

    
    def greaterThanOrEqual(self, other):
        returnValue = libpandaexpress._inPKoxtxo9i(self.this, other.this)
        return returnValue

    
    def compareTo(self, other):
        returnValue = libpandaexpress._inPKoxtbjGQ(self.this, other.this)
        return returnValue

    
    def getHash(self):
        returnValue = libpandaexpress._inPKoxt3PTn(self.this)
        return returnValue

    
    def _TypeHandle__overloaded_getName_ptrConstTypeHandle_ptrTypedObject(self, object):
        returnValue = libpandaexpress._inPKoxtRQdg(self.this, object.this)
        return returnValue

    
    def _TypeHandle__overloaded_getName_ptrConstTypeHandle(self):
        returnValue = libpandaexpress._inPKoxthwj6(self.this)
        return returnValue

    
    def _TypeHandle__overloaded_isDerivedFrom_ptrConstTypeHandle_ptrTypeHandle_ptrTypedObject(self, parent, object):
        returnValue = libpandaexpress._inPKoxtvx87(self.this, parent.this, object.this)
        return returnValue

    
    def _TypeHandle__overloaded_isDerivedFrom_ptrConstTypeHandle_ptrTypeHandle(self, parent):
        returnValue = libpandaexpress._inPKoxtviuC(self.this, parent.this)
        return returnValue

    
    def _TypeHandle__overloaded_getNumParentClasses_ptrConstTypeHandle_ptrTypedObject(self, object):
        returnValue = libpandaexpress._inPKoxthY1k(self.this, object.this)
        return returnValue

    
    def _TypeHandle__overloaded_getNumParentClasses_ptrConstTypeHandle(self):
        returnValue = libpandaexpress._inPKoxt_rZb(self.this)
        return returnValue

    
    def getParentClass(self, index):
        returnValue = libpandaexpress._inPKoxt4htB(self.this, index)
        returnObject = TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _TypeHandle__overloaded_getNumChildClasses_ptrConstTypeHandle_ptrTypedObject(self, object):
        returnValue = libpandaexpress._inPKoxtbcCX(self.this, object.this)
        return returnValue

    
    def _TypeHandle__overloaded_getNumChildClasses_ptrConstTypeHandle(self):
        returnValue = libpandaexpress._inPKoxt3vxm(self.this)
        return returnValue

    
    def getChildClass(self, index):
        returnValue = libpandaexpress._inPKoxtUvhk(self.this, index)
        returnObject = TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _TypeHandle__overloaded_getParentTowards_ptrConstTypeHandle_ptrTypeHandle_ptrTypedObject(self, ancestor, object):
        returnValue = libpandaexpress._inPKoxtCbxt(self.this, ancestor.this, object.this)
        returnObject = TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _TypeHandle__overloaded_getParentTowards_ptrConstTypeHandle_ptrTypeHandle(self, ancestor):
        returnValue = libpandaexpress._inPKoxtjV7z(self.this, ancestor.this)
        returnObject = TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getIndex(self):
        returnValue = libpandaexpress._inPKoxtPmiQ(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inPKoxtVMV9(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._TypeHandle__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._TypeHandle__overloaded_constructor_ptrConstTypeHandle(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getParentTowards(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._TypeHandle__overloaded_getParentTowards_ptrConstTypeHandle_ptrTypeHandle(*_args)
        elif numArgs == 2:
            return self._TypeHandle__overloaded_getParentTowards_ptrConstTypeHandle_ptrTypeHandle_ptrTypedObject(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getName(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._TypeHandle__overloaded_getName_ptrConstTypeHandle(*_args)
        elif numArgs == 1:
            return self._TypeHandle__overloaded_getName_ptrConstTypeHandle_ptrTypedObject(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getNumParentClasses(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._TypeHandle__overloaded_getNumParentClasses_ptrConstTypeHandle(*_args)
        elif numArgs == 1:
            return self._TypeHandle__overloaded_getNumParentClasses_ptrConstTypeHandle_ptrTypedObject(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getNumChildClasses(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._TypeHandle__overloaded_getNumChildClasses_ptrConstTypeHandle(*_args)
        elif numArgs == 1:
            return self._TypeHandle__overloaded_getNumChildClasses_ptrConstTypeHandle_ptrTypedObject(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def isDerivedFrom(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._TypeHandle__overloaded_isDerivedFrom_ptrConstTypeHandle_ptrTypeHandle(*_args)
        elif numArgs == 2:
            return self._TypeHandle__overloaded_isDerivedFrom_ptrConstTypeHandle_ptrTypeHandle_ptrTypedObject(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


