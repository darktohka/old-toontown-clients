# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import DNAGroup

class DNAVisGroup(DNAGroup.DNAGroup, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _DNAVisGroup__overloaded_constructor_ptrConstDNAVisGroup(self, group):
        self.this = libtoontown._inPdt4yJYfu(group.this)
        self.userManagesMemory = 1

    
    def _DNAVisGroup__overloaded_constructor_atomicstring(self, initialName):
        self.this = libtoontown._inPdt4y2lmR(initialName)
        self.userManagesMemory = 1

    
    def _DNAVisGroup__overloaded_constructor(self):
        self.this = libtoontown._inPdt4yesJI()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPdt4yfswV:
            libtoontown._inPdt4yfswV(self.this)
        

    
    def getClassType():
        returnValue = libtoontown._inPdt4yxLTy()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def addVisible(self, visGroupName):
        returnValue = libtoontown._inPdt4yrAIa(self.this, visGroupName)
        return returnValue

    
    def removeVisible(self, visGroupName):
        returnValue = libtoontown._inPdt4y5V81(self.this, visGroupName)
        return returnValue

    
    def getNumVisibles(self):
        returnValue = libtoontown._inPdt4yqnTT(self.this)
        return returnValue

    
    def getVisibleName(self, i):
        returnValue = libtoontown._inPdt4yEJX6(self.this, i)
        return returnValue

    
    def addSuitEdge(self, edge):
        returnValue = libtoontown._inPdt4y42Hm(self.this, edge.this)
        return returnValue

    
    def removeSuitEdge(self, edge):
        returnValue = libtoontown._inPdt4ysL9U(self.this, edge.this)
        return returnValue

    
    def getNumSuitEdges(self):
        returnValue = libtoontown._inPdt4yDKQf(self.this)
        return returnValue

    
    def getSuitEdge(self, i):
        returnValue = libtoontown._inPdt4yGgTQ(self.this, i)
        import DNASuitEdge
        returnObject = DNASuitEdge.DNASuitEdge(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def addBattleCell(self, cell):
        returnValue = libtoontown._inPdt4yNPzx(self.this, cell.this)
        return returnValue

    
    def removeBattleCell(self, cell):
        returnValue = libtoontown._inPdt4ynwfH(self.this, cell.this)
        return returnValue

    
    def getNumBattleCells(self):
        returnValue = libtoontown._inPdt4yDFHg(self.this)
        return returnValue

    
    def getBattleCell(self, i):
        returnValue = libtoontown._inPdt4ykfde(self.this, i)
        import DNABattleCell
        returnObject = DNABattleCell.DNABattleCell(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DNAVisGroup__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DNAVisGroup__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], DNAVisGroup):
                return self._DNAVisGroup__overloaded_constructor_ptrConstDNAVisGroup(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNAVisGroup> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


