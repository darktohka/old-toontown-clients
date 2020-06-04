# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import DNANode

class DNALandmarkBuilding(DNANode.DNANode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _DNALandmarkBuilding__overloaded_constructor_ptrConstDNALandmarkBuilding(self, building):
        self.this = libtoontown._inPet4yUFuh(building.this)
        self.userManagesMemory = 1

    
    def _DNALandmarkBuilding__overloaded_constructor_atomicstring(self, initialName):
        self.this = libtoontown._inPet4yHgBm(initialName)
        self.userManagesMemory = 1

    
    def _DNALandmarkBuilding__overloaded_constructor(self):
        self.this = libtoontown._inPet4ydemh()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPet4ya0eY:
            libtoontown._inPet4ya0eY(self.this)
        

    
    def getClassType():
        returnValue = libtoontown._inPet4yFe2l()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setTitle(self, title):
        returnValue = libtoontown._inPet4y5j5T(self.this, title)
        return returnValue

    
    def getTitle(self):
        returnValue = libtoontown._inPet4y3Ybf(self.this)
        return returnValue

    
    def setArticle(self, article):
        returnValue = libtoontown._inPet4yj8_2(self.this, article)
        return returnValue

    
    def getArticle(self):
        returnValue = libtoontown._inPet4y6Kl7(self.this)
        return returnValue

    
    def setCode(self, code):
        returnValue = libtoontown._inPet4yo6Oc(self.this, code)
        return returnValue

    
    def getCode(self):
        returnValue = libtoontown._inPet4yHbJR(self.this)
        return returnValue

    
    def setWallColor(self, color):
        returnValue = libtoontown._inPet4yicmK(self.this, color.this)
        return returnValue

    
    def getWallColor(self):
        returnValue = libtoontown._inPet4yl_gH(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setBuildingType(self, type):
        returnValue = libtoontown._inPet4y6Fyh(self.this, type)
        return returnValue

    
    def getBuildingType(self):
        returnValue = libtoontown._inPet4y_o7Z(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DNALandmarkBuilding__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DNALandmarkBuilding__overloaded_constructor_atomicstring(_args[0])
            elif isinstance(_args[0], DNALandmarkBuilding):
                return self._DNALandmarkBuilding__overloaded_constructor_ptrConstDNALandmarkBuilding(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNALandmarkBuilding> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


