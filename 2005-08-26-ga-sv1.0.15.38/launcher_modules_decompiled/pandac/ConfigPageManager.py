# File: C (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class ConfigPageManager(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getGlobalPtr():
        returnValue = libpandaexpress._inPKoxtH_23()
        returnObject = ConfigPageManager(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getGlobalPtr = staticmethod(getGlobalPtr)
    
    def loadedImplicitPages(self):
        returnValue = libpandaexpress._inPKoxtTibR(self.this)
        return returnValue

    
    def loadImplicitPages(self):
        returnValue = libpandaexpress._inPKoxt6EjB(self.this)
        return returnValue

    
    def reloadImplicitPages(self):
        returnValue = libpandaexpress._inPKoxtSIdn(self.this)
        return returnValue

    
    def getSearchPath(self):
        returnValue = libpandaexpress._inPKoxtBr_C(self.this)
        import DSearchPath
        returnObject = DSearchPath.DSearchPath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNumPrcPatterns(self):
        returnValue = libpandaexpress._inPKoxtOjrt(self.this)
        return returnValue

    
    def getPrcPattern(self, n):
        returnValue = libpandaexpress._inPKoxt7pmq(self.this, n)
        return returnValue

    
    def getNumPrcExecutablePatterns(self):
        returnValue = libpandaexpress._inPKoxtwzxf(self.this)
        return returnValue

    
    def getPrcExecutablePattern(self, n):
        returnValue = libpandaexpress._inPKoxtHOFD(self.this, n)
        return returnValue

    
    def makeExplicitPage(self, name):
        returnValue = libpandaexpress._inPKoxt1BwY(self.this, name)
        import ConfigPage
        returnObject = ConfigPage.ConfigPage(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def deleteExplicitPage(self, page):
        returnValue = libpandaexpress._inPKoxtFhLr(self.this, page.this)
        return returnValue

    
    def getNumImplicitPages(self):
        returnValue = libpandaexpress._inPKoxtNpX6(self.this)
        return returnValue

    
    def getImplicitPage(self, n):
        returnValue = libpandaexpress._inPKoxt5iN2(self.this, n)
        import ConfigPage
        returnObject = ConfigPage.ConfigPage(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNumExplicitPages(self):
        returnValue = libpandaexpress._inPKoxtHC4q(self.this)
        return returnValue

    
    def getExplicitPage(self, n):
        returnValue = libpandaexpress._inPKoxtlDa_(self.this, n)
        import ConfigPage
        returnObject = ConfigPage.ConfigPage(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def output(self, out):
        returnValue = libpandaexpress._inPKoxtdhHl(self.this, out.this)
        return returnValue

    
    def write(self, out):
        returnValue = libpandaexpress._inPKoxtN841(self.this, out.this)
        return returnValue


