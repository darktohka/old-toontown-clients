# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedReferenceCount
import Namable

class DNAGroup(TypedReferenceCount.TypedReferenceCount, Namable.Namable, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _DNAGroup__overloaded_constructor_ptrConstDNAGroup(self, group):
        self.this = libtoontown._inPdt4yQTN4(group.this)
        self.userManagesMemory = 1

    
    def _DNAGroup__overloaded_constructor_atomicstring(self, initialName):
        self.this = libtoontown._inPdt4yISCp(initialName)
        self.userManagesMemory = 1

    
    def _DNAGroup__overloaded_constructor(self):
        self.this = libtoontown._inPdt4yvZ75()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPdt4y9d9M:
            libtoontown._inPdt4y9d9M(self.this)
        

    
    def getClassType():
        returnValue = libtoontown._inPdt4yfV_Z()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _DNAGroup__overloaded_traverse_ptrDNAGroup_ptrNodePath_ptrDNAStorage_int(self, parent, store, editing):
        returnValue = libtoontown._inPdt4yyAUW(self.this, parent.this, store.this, editing)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _DNAGroup__overloaded_traverse_ptrDNAGroup_ptrNodePath_ptrDNAStorage(self, parent, store):
        returnValue = libtoontown._inPdt4yeeXS(self.this, parent.this, store.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _DNAGroup__overloaded_topLevelTraverse_ptrDNAGroup_ptrNodePath_ptrDNAStorage_int(self, parent, store, editing):
        returnValue = libtoontown._inPdt4ysXhv(self.this, parent.this, store.this, editing)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _DNAGroup__overloaded_topLevelTraverse_ptrDNAGroup_ptrNodePath_ptrDNAStorage(self, parent, store):
        returnValue = libtoontown._inPdt4yVnuf(self.this, parent.this, store.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def add(self, group):
        returnValue = libtoontown._inPdt4yflZo(self.this, group.this)
        return returnValue

    
    def remove(self, group):
        returnValue = libtoontown._inPdt4yuG_w(self.this, group.this)
        return returnValue

    
    def at(self, index):
        returnValue = libtoontown._inPdt4y538n(self.this, index)
        returnObject = DNAGroup(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def current(self):
        returnValue = libtoontown._inPdt4ynRHn(self.this)
        returnObject = DNAGroup(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNumChildren(self):
        returnValue = libtoontown._inPdt4yaTa8(self.this)
        return returnValue

    
    def getParent(self):
        returnValue = libtoontown._inPdt4ypj1A(self.this)
        returnObject = DNAGroup(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _DNAGroup__overloaded_write_ptrConstDNAGroup_ptrOstream_ptrDNAStorage_int(self, out, store, indentLevel):
        returnValue = libtoontown._inPdt4yzQ3X(self.this, out.this, store.this, indentLevel)
        return returnValue

    
    def _DNAGroup__overloaded_write_ptrConstDNAGroup_ptrOstream_ptrDNAStorage(self, out, store):
        returnValue = libtoontown._inPdt4ykM94(self.this, out.this, store.this)
        return returnValue

    
    def ls(self):
        returnValue = libtoontown._inPdt4y5DWD(self.this)
        return returnValue

    
    def upcastToNamable(self):
        returnValue = libtoontown._inPdt4yAv1q(self.this)
        import Namable
        returnObject = Namable.Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToReferenceCount(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxtKE8f(upcastSelf.this)
        import ReferenceCount
        returnObject = ReferenceCount.ReferenceCount(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getType(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxt1uxI(upcastSelf.this)
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getTypeIndex(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxtm7AU(upcastSelf.this)
        return returnValue

    
    def isOfType(self, handle):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxtnFKt(upcastSelf.this, handle.this)
        return returnValue

    
    def isExactType(self, handle):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxt7Xzz(upcastSelf.this, handle.this)
        return returnValue

    
    def getRefCount(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtP11_(upcastSelf.this)
        return returnValue

    
    def ref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtaS5_(upcastSelf.this)
        return returnValue

    
    def unref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtwyVy(upcastSelf.this)
        return returnValue

    
    def testRefCountIntegrity(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtvpj2(upcastSelf.this)
        return returnValue

    
    def assign(self, other):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtp1bI(upcastSelf.this, other.this)
        import Namable
        returnObject = Namable.Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setName(self, name):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtLNBW(upcastSelf.this, name)
        return returnValue

    
    def clearName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtZvUl(upcastSelf.this)
        return returnValue

    
    def hasName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtYjhC(upcastSelf.this)
        return returnValue

    
    def getName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtfARN(upcastSelf.this)
        return returnValue

    
    def output(self, out):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtoz7q(upcastSelf.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DNAGroup__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DNAGroup__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], DNAGroup):
                return self._DNAGroup__overloaded_constructor_ptrConstDNAGroup(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNAGroup> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._DNAGroup__overloaded_write_ptrConstDNAGroup_ptrOstream_ptrDNAStorage(*_args)
        elif numArgs == 3:
            return self._DNAGroup__overloaded_write_ptrConstDNAGroup_ptrOstream_ptrDNAStorage_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def traverse(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._DNAGroup__overloaded_traverse_ptrDNAGroup_ptrNodePath_ptrDNAStorage(*_args)
        elif numArgs == 3:
            return self._DNAGroup__overloaded_traverse_ptrDNAGroup_ptrNodePath_ptrDNAStorage_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def topLevelTraverse(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._DNAGroup__overloaded_topLevelTraverse_ptrDNAGroup_ptrNodePath_ptrDNAStorage(*_args)
        elif numArgs == 3:
            return self._DNAGroup__overloaded_topLevelTraverse_ptrDNAGroup_ptrNodePath_ptrDNAStorage_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


