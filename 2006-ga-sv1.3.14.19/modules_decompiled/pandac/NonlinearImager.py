# File: N (Python 2.2)

import types
import libpandafx
import libpandafxDowncasts
from direct.ffi import FFIExternalObject

class NonlinearImager(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandafxDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpandafx._inP1uO4_PCJ()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandafx and libpandafx._inP1uO4HhNo:
            libpandafx._inP1uO4HhNo(self.this)
        

    
    def _NonlinearImager__overloaded_addScreen_ptrNonlinearImager_ptrConstNodePath_atomicstring(self, screen, name):
        returnValue = libpandafx._inP1uO4Id7Z(self.this, screen.this, name)
        return returnValue

    
    def _NonlinearImager__overloaded_addScreen_ptrNonlinearImager_ptrProjectionScreen(self, screen):
        returnValue = libpandafx._inP1uO4nWhU(self.this, screen.this)
        return returnValue

    
    def findScreen(self, screen):
        returnValue = libpandafx._inP1uO40gaK(self.this, screen.this)
        return returnValue

    
    def removeScreen(self, index):
        returnValue = libpandafx._inP1uO4LstH(self.this, index)
        return returnValue

    
    def removeAllScreens(self):
        returnValue = libpandafx._inP1uO40pJi(self.this)
        return returnValue

    
    def getNumScreens(self):
        returnValue = libpandafx._inP1uO42sj0(self.this)
        return returnValue

    
    def getScreen(self, index):
        returnValue = libpandafx._inP1uO44h98(self.this, index)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getBuffer(self, index):
        returnValue = libpandafx._inP1uO4MN_0(self.this, index)
        import GraphicsOutput
        returnObject = GraphicsOutput.GraphicsOutput(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setTextureSize(self, index, width, height):
        returnValue = libpandafx._inP1uO4Rw3d(self.this, index, width, height)
        return returnValue

    
    def setSourceCamera(self, index, sourceCamera):
        returnValue = libpandafx._inP1uO4k8BW(self.this, index, sourceCamera.this)
        return returnValue

    
    def setScreenActive(self, index, active):
        returnValue = libpandafx._inP1uO40keX(self.this, index, active)
        return returnValue

    
    def getScreenActive(self, index):
        returnValue = libpandafx._inP1uO4QBpp(self.this, index)
        return returnValue

    
    def addViewer(self, dr):
        returnValue = libpandafx._inP1uO4eOfi(self.this, dr.this)
        return returnValue

    
    def findViewer(self, dr):
        returnValue = libpandafx._inP1uO4bheq(self.this, dr.this)
        return returnValue

    
    def removeViewer(self, index):
        returnValue = libpandafx._inP1uO4Tqe9(self.this, index)
        return returnValue

    
    def removeAllViewers(self):
        returnValue = libpandafx._inP1uO4mtgF(self.this)
        return returnValue

    
    def setViewerCamera(self, index, viewerCamera):
        returnValue = libpandafx._inP1uO4r03_(self.this, index, viewerCamera.this)
        return returnValue

    
    def getViewerCamera(self, index):
        returnValue = libpandafx._inP1uO4m1Ke(self.this, index)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getViewerScene(self, index):
        returnValue = libpandafx._inP1uO4GLn8(self.this, index)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getNumViewers(self):
        returnValue = libpandafx._inP1uO4DQFt(self.this)
        return returnValue

    
    def getViewer(self, index):
        returnValue = libpandafx._inP1uO4C4VF(self.this, index)
        import DisplayRegion
        returnObject = DisplayRegion.DisplayRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getDarkRoom(self):
        returnValue = libpandafx._inP1uO4oAhd(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getGraphicsEngine(self):
        returnValue = libpandafx._inP1uO4jAJ5(self.this)
        import GraphicsEngine
        returnObject = GraphicsEngine.GraphicsEngine(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def recompute(self):
        returnValue = libpandafx._inP1uO4nMhO(self.this)
        return returnValue

    
    def addScreen(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NonlinearImager__overloaded_addScreen_ptrNonlinearImager_ptrProjectionScreen(*_args)
        elif numArgs == 2:
            return self._NonlinearImager__overloaded_addScreen_ptrNonlinearImager_ptrConstNodePath_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


