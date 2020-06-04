# File: T (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class TextureStageCollection(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _TextureStageCollection__overloaded_constructor(self):
        self.this = libpanda._inPnJyoxpnH()
        self.userManagesMemory = 1

    
    def _TextureStageCollection__overloaded_constructor_ptrConstTextureStageCollection(self, copy):
        self.this = libpanda._inPnJyoWv2z(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPnJyoIE_W:
            libpanda._inPnJyoIE_W(self.this)
        

    
    def assign(self, copy):
        returnValue = libpanda._inPnJyoNQDB(self.this, copy.this)
        returnObject = TextureStageCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def addTextureStage(self, nodeTextureStage):
        returnValue = libpanda._inPnJyoGIjY(self.this, nodeTextureStage.this)
        return returnValue

    
    def removeTextureStage(self, nodeTextureStage):
        returnValue = libpanda._inPnJyoZ9r9(self.this, nodeTextureStage.this)
        return returnValue

    
    def addTextureStagesFrom(self, other):
        returnValue = libpanda._inPnJyoVfWB(self.this, other.this)
        return returnValue

    
    def removeTextureStagesFrom(self, other):
        returnValue = libpanda._inPnJyo8M8q(self.this, other.this)
        return returnValue

    
    def removeDuplicateTextureStages(self):
        returnValue = libpanda._inPnJyorJqC(self.this)
        return returnValue

    
    def hasTextureStage(self, textureStage):
        returnValue = libpanda._inPnJyoXvY1(self.this, textureStage.this)
        return returnValue

    
    def clear(self):
        returnValue = libpanda._inPnJyoT2Xf(self.this)
        return returnValue

    
    def findTextureStage(self, name):
        returnValue = libpanda._inPnJyo_5YH(self.this, name)
        import TextureStage
        returnObject = TextureStage.TextureStage(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNumTextureStages(self):
        returnValue = libpanda._inPnJyotfCs(self.this)
        return returnValue

    
    def getTextureStage(self, index):
        returnValue = libpanda._inPnJyo9Uz2(self.this, index)
        import TextureStage
        returnObject = TextureStage.TextureStage(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def __getitem__(self, index):
        returnValue = libpanda._inPnJyo5fT7(self.this, index)
        import TextureStage
        returnObject = TextureStage.TextureStage(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def output(self, out):
        returnValue = libpanda._inPnJyoI4CN(self.this, out.this)
        return returnValue

    
    def _TextureStageCollection__overloaded_write_ptrConstTextureStageCollection_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPnJyo5JdN(self.this, out.this, indentLevel)
        return returnValue

    
    def _TextureStageCollection__overloaded_write_ptrConstTextureStageCollection_ptrOstream(self, out):
        returnValue = libpanda._inPnJyoqJju(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._TextureStageCollection__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._TextureStageCollection__overloaded_constructor_ptrConstTextureStageCollection(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._TextureStageCollection__overloaded_write_ptrConstTextureStageCollection_ptrOstream(*_args)
        elif numArgs == 2:
            return self._TextureStageCollection__overloaded_write_ptrConstTextureStageCollection_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


