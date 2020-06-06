# File: N (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class NodePathCollection(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _NodePathCollection__overloaded_constructor(self):
        self.this = libpanda._inPkJyo2iXv()
        self.userManagesMemory = 1

    
    def _NodePathCollection__overloaded_constructor_ptrConstNodePathCollection(self, copy):
        self.this = libpanda._inPkJyo2o9H(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPkJyoiPHD:
            libpanda._inPkJyoiPHD(self.this)
        

    
    def assign(self, copy):
        returnValue = libpanda._inPkJyohGif(self.this, copy.this)
        returnObject = NodePathCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def addPath(self, nodePath):
        returnValue = libpanda._inPkJyopj7i(self.this, nodePath.this)
        return returnValue

    
    def removePath(self, nodePath):
        returnValue = libpanda._inPkJyo_4Zw(self.this, nodePath.this)
        return returnValue

    
    def addPathsFrom(self, other):
        returnValue = libpanda._inPkJyoD16c(self.this, other.this)
        return returnValue

    
    def removePathsFrom(self, other):
        returnValue = libpanda._inPkJyoPgsC(self.this, other.this)
        return returnValue

    
    def removeDuplicatePaths(self):
        returnValue = libpanda._inPkJyofBHO(self.this)
        return returnValue

    
    def hasPath(self, path):
        returnValue = libpanda._inPkJyoW5qJ(self.this, path.this)
        return returnValue

    
    def clear(self):
        returnValue = libpanda._inPkJyoNyfl(self.this)
        return returnValue

    
    def isEmpty(self):
        returnValue = libpanda._inPkJyoYTzI(self.this)
        return returnValue

    
    def getNumPaths(self):
        returnValue = libpanda._inPkJyo5KKi(self.this)
        return returnValue

    
    def getPath(self, index):
        returnValue = libpanda._inPkJyo02PJ(self.this, index)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __getitem__(self, index):
        returnValue = libpanda._inPkJyoziIl(self.this, index)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePathCollection__overloaded_ls_ptrConstNodePathCollection(self):
        returnValue = libpanda._inPkJyowQA8(self.this)
        return returnValue

    
    def _NodePathCollection__overloaded_ls_ptrConstNodePathCollection_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPkJyoQtqi(self.this, out.this, indentLevel)
        return returnValue

    
    def _NodePathCollection__overloaded_ls_ptrConstNodePathCollection_ptrOstream(self, out):
        returnValue = libpanda._inPkJyo0d_6(self.this, out.this)
        return returnValue

    
    def findAllMatches(self, path):
        returnValue = libpanda._inPkJyoXeNM(self.this, path)
        returnObject = NodePathCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def reparentTo(self, other):
        returnValue = libpanda._inPkJyob1jO(self.this, other.this)
        return returnValue

    
    def wrtReparentTo(self, other):
        returnValue = libpanda._inPkJyoqRqE(self.this, other.this)
        return returnValue

    
    def show(self):
        returnValue = libpanda._inPkJyo7UQK(self.this)
        return returnValue

    
    def hide(self):
        returnValue = libpanda._inPkJyo483n(self.this)
        return returnValue

    
    def stash(self):
        returnValue = libpanda._inPkJyoiPiS(self.this)
        return returnValue

    
    def unstash(self):
        returnValue = libpanda._inPkJyoITV5(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPkJyouSFB(self.this, out.this)
        return returnValue

    
    def _NodePathCollection__overloaded_write_ptrConstNodePathCollection_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPkJyocn9H(self.this, out.this, indentLevel)
        return returnValue

    
    def _NodePathCollection__overloaded_write_ptrConstNodePathCollection_ptrOstream(self, out):
        returnValue = libpanda._inPkJyo_nJZ(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePathCollection__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], NodePathCollection):
                return self._NodePathCollection__overloaded_constructor_ptrConstNodePathCollection(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePathCollection> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._NodePathCollection__overloaded_write_ptrConstNodePathCollection_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._NodePathCollection__overloaded_write_ptrConstNodePathCollection_ptrOstream_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def ls(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePathCollection__overloaded_ls_ptrConstNodePathCollection()
        elif numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._NodePathCollection__overloaded_ls_ptrConstNodePathCollection_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._NodePathCollection__overloaded_ls_ptrConstNodePathCollection_ptrOstream_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def asList(self):
        if self.isEmpty():
            return []
        else:
            npList = []
            for nodePathIndex in range(self.getNumPaths()):
                npList.append(self.getPath(nodePathIndex))
            
            return npList


