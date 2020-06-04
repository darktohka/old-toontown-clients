# File: T (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class TypeHandle(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _TypeHandle__overloaded_constructor(self):
        self.this = libpandaexpress._inPJoxtC5ho()
        self.userManagesMemory = 1

    
    def _TypeHandle__overloaded_constructor_ptrConstTypeHandle(self, copy):
        self.this = libpandaexpress._inPJoxtGniZ(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPJoxtWx5B:
            libpandaexpress._inPJoxtWx5B(self.this)
        

    
    def none():
        returnValue = libpandaexpress._inPJoxto1S_()
        returnObject = TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    none = staticmethod(none)
    
    def eq(self, other):
        returnValue = libpandaexpress._inPJoxtxgMZ(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpandaexpress._inPJoxt9A0H(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpandaexpress._inPJoxt0HOQ(self.this, other.this)
        return returnValue

    
    def lessThanOrEqual(self, other):
        returnValue = libpandaexpress._inPJoxtx4bP(self.this, other.this)
        return returnValue

    
    def greaterThan(self, other):
        returnValue = libpandaexpress._inPJoxt3Xwj(self.this, other.this)
        return returnValue

    
    def greaterThanOrEqual(self, other):
        returnValue = libpandaexpress._inPJoxtwo9i(self.this, other.this)
        return returnValue

    
    def _TypeHandle__overloaded_getName_ptrConstTypeHandle_ptrTypedObject(self, object):
        returnValue = libpandaexpress._inPJoxteQdg(self.this, object.this)
        return returnValue

    
    def _TypeHandle__overloaded_getName_ptrConstTypeHandle(self):
        returnValue = libpandaexpress._inPJoxtiwj6(self.this)
        return returnValue

    
    def _TypeHandle__overloaded_isDerivedFrom_ptrConstTypeHandle_ptrTypeHandle_ptrTypedObject(self, parent, object):
        returnValue = libpandaexpress._inPJoxtox87(self.this, parent.this, object.this)
        return returnValue

    
    def _TypeHandle__overloaded_isDerivedFrom_ptrConstTypeHandle_ptrTypeHandle(self, parent):
        returnValue = libpandaexpress._inPJoxtviuC(self.this, parent.this)
        return returnValue

    
    def _TypeHandle__overloaded_getNumParentClasses_ptrConstTypeHandle_ptrTypedObject(self, object):
        returnValue = libpandaexpress._inPJoxtiY1k(self.this, object.this)
        return returnValue

    
    def _TypeHandle__overloaded_getNumParentClasses_ptrConstTypeHandle(self):
        returnValue = libpandaexpress._inPJoxt_rZb(self.this)
        return returnValue

    
    def getParentClass(self, index):
        returnValue = libpandaexpress._inPJoxt4htB(self.this, index)
        returnObject = TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _TypeHandle__overloaded_getNumChildClasses_ptrConstTypeHandle_ptrTypedObject(self, object):
        returnValue = libpandaexpress._inPJoxtbcCX(self.this, object.this)
        return returnValue

    
    def _TypeHandle__overloaded_getNumChildClasses_ptrConstTypeHandle(self):
        returnValue = libpandaexpress._inPJoxt0vxm(self.this)
        return returnValue

    
    def getChildClass(self, index):
        returnValue = libpandaexpress._inPJoxtVvhk(self.this, index)
        returnObject = TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _TypeHandle__overloaded_getParentTowards_ptrConstTypeHandle_ptrTypeHandle_ptrTypedObject(self, ancestor, object):
        returnValue = libpandaexpress._inPJoxtDbxt(self.this, ancestor.this, object.this)
        returnObject = TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _TypeHandle__overloaded_getParentTowards_ptrConstTypeHandle_ptrTypeHandle(self, ancestor):
        returnValue = libpandaexpress._inPJoxtiV7z(self.this, ancestor.this)
        returnObject = TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getIndex(self):
        returnValue = libpandaexpress._inPJoxtPmiQ(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inPJoxtKMV9(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._TypeHandle__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], TypeHandle):
                return self._TypeHandle__overloaded_constructor_ptrConstTypeHandle(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <TypeHandle> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getParentTowards(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], TypeHandle):
                return self._TypeHandle__overloaded_getParentTowards_ptrConstTypeHandle_ptrTypeHandle(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <TypeHandle> '
        elif numArgs == 2:
            if isinstance(_args[0], TypeHandle):
                import TypedObject
                if isinstance(_args[1], TypedObject.TypedObject):
                    return self._TypeHandle__overloaded_getParentTowards_ptrConstTypeHandle_ptrTypeHandle_ptrTypedObject(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <TypedObject.TypedObject> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <TypeHandle> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getName(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._TypeHandle__overloaded_getName_ptrConstTypeHandle()
        elif numArgs == 1:
            import TypedObject
            if isinstance(_args[0], TypedObject.TypedObject):
                return self._TypeHandle__overloaded_getName_ptrConstTypeHandle_ptrTypedObject(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <TypedObject.TypedObject> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getNumParentClasses(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._TypeHandle__overloaded_getNumParentClasses_ptrConstTypeHandle()
        elif numArgs == 1:
            import TypedObject
            if isinstance(_args[0], TypedObject.TypedObject):
                return self._TypeHandle__overloaded_getNumParentClasses_ptrConstTypeHandle_ptrTypedObject(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <TypedObject.TypedObject> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getNumChildClasses(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._TypeHandle__overloaded_getNumChildClasses_ptrConstTypeHandle()
        elif numArgs == 1:
            import TypedObject
            if isinstance(_args[0], TypedObject.TypedObject):
                return self._TypeHandle__overloaded_getNumChildClasses_ptrConstTypeHandle_ptrTypedObject(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <TypedObject.TypedObject> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def isDerivedFrom(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], TypeHandle):
                return self._TypeHandle__overloaded_isDerivedFrom_ptrConstTypeHandle_ptrTypeHandle(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <TypeHandle> '
        elif numArgs == 2:
            if isinstance(_args[0], TypeHandle):
                import TypedObject
                if isinstance(_args[1], TypedObject.TypedObject):
                    return self._TypeHandle__overloaded_isDerivedFrom_ptrConstTypeHandle_ptrTypeHandle_ptrTypedObject(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <TypedObject.TypedObject> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <TypeHandle> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


