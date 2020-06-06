# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedReferenceCount

class DNABattleCell(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, width, height, pos):
        self.this = libtoontown._inPdt4yh_xl(width, height, pos.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPdt4y5DYV:
            libtoontown._inPdt4y5DYV(self.this)
        

    
    def getClassType():
        returnValue = libtoontown._inPdt4ySx1s()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setWidthHeight(self, width, height):
        returnValue = libtoontown._inPdt4y5NZM(self.this, width, height)
        return returnValue

    
    def getWidth(self):
        returnValue = libtoontown._inPdt4yKZCb(self.this)
        return returnValue

    
    def getHeight(self):
        returnValue = libtoontown._inPdt4yS5qA(self.this)
        return returnValue

    
    def setPos(self, pos):
        returnValue = libtoontown._inPdt4yYfPn(self.this, pos.this)
        return returnValue

    
    def getPos(self):
        returnValue = libtoontown._inPdt4ytrDR(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def output(self, out):
        returnValue = libtoontown._inPdt4y_PDC(self.this, out.this)
        return returnValue

    
    def _DNABattleCell__overloaded_traverse_ptrDNABattleCell_ptrNodePath_ptrDNAStorage_int(self, parent, store, editing):
        returnValue = libtoontown._inPdt4yREkl(self.this, parent.this, store.this, editing)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _DNABattleCell__overloaded_traverse_ptrDNABattleCell_ptrNodePath_ptrDNAStorage(self, parent, store):
        returnValue = libtoontown._inPdt4yBJrd(self.this, parent.this, store.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _DNABattleCell__overloaded_write_ptrConstDNABattleCell_ptrOstream_ptrDNAStorage_int(self, out, store, indentLevel):
        returnValue = libtoontown._inPdt4yGXoo(self.this, out.this, store.this, indentLevel)
        return returnValue

    
    def _DNABattleCell__overloaded_write_ptrConstDNABattleCell_ptrOstream_ptrDNAStorage(self, out, store):
        returnValue = libtoontown._inPdt4ysN1q(self.this, out.this, store.this)
        return returnValue

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._DNABattleCell__overloaded_write_ptrConstDNABattleCell_ptrOstream_ptrDNAStorage(*_args)
        elif numArgs == 3:
            return self._DNABattleCell__overloaded_write_ptrConstDNABattleCell_ptrOstream_ptrDNAStorage_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def traverse(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._DNABattleCell__overloaded_traverse_ptrDNABattleCell_ptrNodePath_ptrDNAStorage(*_args)
        elif numArgs == 3:
            return self._DNABattleCell__overloaded_traverse_ptrDNABattleCell_ptrNodePath_ptrDNAStorage_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


