# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TypedReferenceCount

class DNABattleCell(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self, width, height, pos):
        self.this = libtoontown._inPet4yg_xl(width, height, pos.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPet4y5DYV:
            libtoontown._inPet4y5DYV(self.this)
        

    
    def getClassType():
        returnValue = libtoontown._inPet4yTx1s()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setWidthHeight(self, width, height):
        returnValue = libtoontown._inPet4y5NZM(self.this, width, height)
        return returnValue

    
    def getWidth(self):
        returnValue = libtoontown._inPet4yKZCb(self.this)
        return returnValue

    
    def getHeight(self):
        returnValue = libtoontown._inPet4yS5qA(self.this)
        return returnValue

    
    def setPos(self, pos):
        returnValue = libtoontown._inPet4yZfPn(self.this, pos.this)
        return returnValue

    
    def getPos(self):
        returnValue = libtoontown._inPet4ytrDR(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def output(self, out):
        returnValue = libtoontown._inPet4y_PDC(self.this, out.this)
        return returnValue

    
    def _DNABattleCell__overloaded_traverse_ptrDNABattleCell_ptrNodePath_ptrDNAStorage_int(self, parent, store, editing):
        returnValue = libtoontown._inPet4ySEkl(self.this, parent.this, store.this, editing)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _DNABattleCell__overloaded_traverse_ptrDNABattleCell_ptrNodePath_ptrDNAStorage(self, parent, store):
        returnValue = libtoontown._inPet4yBJrd(self.this, parent.this, store.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _DNABattleCell__overloaded_write_ptrConstDNABattleCell_ptrOstream_ptrDNAStorage_int(self, out, store, indentLevel):
        returnValue = libtoontown._inPet4yFXoo(self.this, out.this, store.this, indentLevel)
        return returnValue

    
    def _DNABattleCell__overloaded_write_ptrConstDNABattleCell_ptrOstream_ptrDNAStorage(self, out, store):
        returnValue = libtoontown._inPet4yrN1q(self.this, out.this, store.this)
        return returnValue

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                import DNAStorage
                if isinstance(_args[1], DNAStorage.DNAStorage):
                    return self._DNABattleCell__overloaded_write_ptrConstDNABattleCell_ptrOstream_ptrDNAStorage(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <DNAStorage.DNAStorage> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 3:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                import DNAStorage
                if isinstance(_args[1], DNAStorage.DNAStorage):
                    if isinstance(_args[2], types.IntType):
                        return self._DNABattleCell__overloaded_write_ptrConstDNABattleCell_ptrOstream_ptrDNAStorage_int(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <DNAStorage.DNAStorage> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def traverse(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            import NodePath
            if isinstance(_args[0], NodePath.NodePath):
                import DNAStorage
                if isinstance(_args[1], DNAStorage.DNAStorage):
                    return self._DNABattleCell__overloaded_traverse_ptrDNABattleCell_ptrNodePath_ptrDNAStorage(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <DNAStorage.DNAStorage> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> '
        elif numArgs == 3:
            import NodePath
            if isinstance(_args[0], NodePath.NodePath):
                import DNAStorage
                if isinstance(_args[1], DNAStorage.DNAStorage):
                    if isinstance(_args[2], types.IntType):
                        return self._DNABattleCell__overloaded_traverse_ptrDNABattleCell_ptrNodePath_ptrDNAStorage_int(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <DNAStorage.DNAStorage> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


