# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
from direct.ffi import FFIExternalObject

class DNAStorage(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libtoontown._inPdt4y1ZFR()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPdt4ybqD8:
            libtoontown._inPdt4ybqD8(self.this)
        

    
    def printNodeStorage(self):
        returnValue = libtoontown._inPdt4yuzwk(self.this)
        return returnValue

    
    def printTextureStorage(self):
        returnValue = libtoontown._inPdt4yriYa(self.this)
        return returnValue

    
    def printFontStorage(self):
        returnValue = libtoontown._inPdt4yczQC(self.this)
        return returnValue

    
    def printSuitPointStorage(self):
        returnValue = libtoontown._inPdt4yGsM_(self.this)
        return returnValue

    
    def printBattleCellStorage(self):
        returnValue = libtoontown._inPdt4yZH2Z(self.this)
        return returnValue

    
    def storeTexture(self, codeString, texture):
        returnValue = libtoontown._inPdt4y_9Ok(self.this, codeString, texture.this)
        return returnValue

    
    def storeFont(self, codeString, font):
        returnValue = libtoontown._inPdt4yPpZl(self.this, codeString, font.this)
        return returnValue

    
    def _DNAStorage__overloaded_storeNode_ptrDNAStorage_atomicstring_ptrNodePath_atomicstring(self, codeString, node, codeCategory):
        returnValue = libtoontown._inPdt4ykLDF(self.this, codeString, node.this, codeCategory)
        return returnValue

    
    def _DNAStorage__overloaded_storeNode_ptrDNAStorage_atomicstring_ptrNodePath(self, codeString, node):
        returnValue = libtoontown._inPdt4yBtk7(self.this, codeString, node.this)
        return returnValue

    
    def _DNAStorage__overloaded_storeHoodNode_ptrDNAStorage_atomicstring_ptrNodePath_atomicstring(self, codeString, node, codeCategory):
        returnValue = libtoontown._inPdt4yKFup(self.this, codeString, node.this, codeCategory)
        return returnValue

    
    def _DNAStorage__overloaded_storeHoodNode_ptrDNAStorage_atomicstring_ptrNodePath(self, codeString, node):
        returnValue = libtoontown._inPdt4yP0tW(self.this, codeString, node.this)
        return returnValue

    
    def _DNAStorage__overloaded_storePlaceNode_ptrDNAStorage_atomicstring_ptrNodePath_atomicstring(self, codeString, node, codeCategory):
        returnValue = libtoontown._inPdt4yNIgc(self.this, codeString, node.this, codeCategory)
        return returnValue

    
    def _DNAStorage__overloaded_storePlaceNode_ptrDNAStorage_atomicstring_ptrNodePath(self, codeString, node):
        returnValue = libtoontown._inPdt4y_Bg6(self.this, codeString, node.this)
        return returnValue

    
    def _DNAStorage__overloaded_storeSuitPoint_ptrDNAStorage___enum__DNASuitPointType_ptrLPoint3f(self, type, pos):
        returnValue = libtoontown._inPdt4yo1kA(self.this, type, pos.this)
        import DNASuitPoint
        returnObject = DNASuitPoint.DNASuitPoint(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _DNAStorage__overloaded_storeSuitPoint_ptrDNAStorage_ptrDNASuitPoint(self, parameter1):
        returnValue = libtoontown._inPdt4yEhAr(self.this, parameter1.this)
        return returnValue

    
    def getHighestSuitPointIndex(self):
        returnValue = libtoontown._inPdt4yuwaV(self.this)
        return returnValue

    
    def removeSuitPoint(self, parameter1):
        returnValue = libtoontown._inPdt4y1UVm(self.this, parameter1.this)
        return returnValue

    
    def storeBlockNumber(self, block, zoneId):
        returnValue = libtoontown._inPdt4yfH3h(self.this, block, zoneId)
        return returnValue

    
    def storeBlockDoorPosHpr(self, block, pos, hpr):
        returnValue = libtoontown._inPdt4yjxgm(self.this, block, pos.this, hpr.this)
        return returnValue

    
    def storeBlockSignTransform(self, block, mat):
        returnValue = libtoontown._inPdt4y8j4y(self.this, block, mat.this)
        return returnValue

    
    def storeBlockTitle(self, block, title):
        returnValue = libtoontown._inPdt4yK106(self.this, block, title)
        return returnValue

    
    def storeBlockArticle(self, block, article):
        returnValue = libtoontown._inPdt4ycNsd(self.this, block, article)
        return returnValue

    
    def storeBattleCell(self, parameter1):
        returnValue = libtoontown._inPdt4yNkDh(self.this, parameter1.this)
        return returnValue

    
    def removeBattleCell(self, parameter1):
        returnValue = libtoontown._inPdt4yKnto(self.this, parameter1.this)
        return returnValue

    
    def _DNAStorage__overloaded_storeSuitEdge_ptrDNAStorage_ptrDNASuitEdge(self, parameter1):
        returnValue = libtoontown._inPdt4yVErq(self.this, parameter1.this)
        import DNASuitEdge
        returnObject = DNASuitEdge.DNASuitEdge(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _DNAStorage__overloaded_storeSuitEdge_ptrDNAStorage_int_int_atomicstring(self, startIndex, endIndex, zoneId):
        returnValue = libtoontown._inPdt4yUQZ8(self.this, startIndex, endIndex, zoneId)
        import DNASuitEdge
        returnObject = DNASuitEdge.DNASuitEdge(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def removeSuitEdge(self, parameter1):
        returnValue = libtoontown._inPdt4yuWHb(self.this, parameter1.this)
        return returnValue

    
    def deleteUnusedSuitPoints(self):
        returnValue = libtoontown._inPdt4yzNi7(self.this)
        return returnValue

    
    def fixCoincidentSuitPoints(self):
        returnValue = libtoontown._inPdt4ykZjO(self.this)
        return returnValue

    
    def resetNodes(self):
        returnValue = libtoontown._inPdt4yYe4o(self.this)
        return returnValue

    
    def resetTextures(self):
        returnValue = libtoontown._inPdt4ybEjQ(self.this)
        return returnValue

    
    def resetHood(self):
        returnValue = libtoontown._inPdt4ygO48(self.this)
        return returnValue

    
    def resetHoodNodes(self):
        returnValue = libtoontown._inPdt4yWsns(self.this)
        return returnValue

    
    def resetPlaceNodes(self):
        returnValue = libtoontown._inPdt4yuCLk(self.this)
        return returnValue

    
    def resetSuitPoints(self):
        returnValue = libtoontown._inPdt4ybk05(self.this)
        return returnValue

    
    def resetBattleCells(self):
        returnValue = libtoontown._inPdt4ymT1N(self.this)
        return returnValue

    
    def resetBlockNumbers(self):
        returnValue = libtoontown._inPdt4y_J6Q(self.this)
        return returnValue

    
    def resetBlockDoorPosHprs(self):
        returnValue = libtoontown._inPdt4yV_iW(self.this)
        return returnValue

    
    def resetBlockSignTransforms(self):
        returnValue = libtoontown._inPdt4yAGek(self.this)
        return returnValue

    
    def resetBlockTitle(self):
        returnValue = libtoontown._inPdt4y1OEc(self.this)
        return returnValue

    
    def resetBlockArticle(self):
        returnValue = libtoontown._inPdt4y6HVk(self.this)
        return returnValue

    
    def findTexture(self, dnaString):
        returnValue = libtoontown._inPdt4ysgKy(self.this, dnaString)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def findNode(self, dnaString):
        returnValue = libtoontown._inPdt4yw7Kg(self.this, dnaString)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def findFont(self, dnaString):
        returnValue = libtoontown._inPdt4yKEGD(self.this, dnaString)
        import TextFont
        returnObject = TextFont.TextFont(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNumCatalogCodes(self, catalogString):
        returnValue = libtoontown._inPdt4y0qRV(self.this, catalogString)
        return returnValue

    
    def getCatalogCode(self, catalogString, i):
        returnValue = libtoontown._inPdt4yhTPT(self.this, catalogString, i)
        return returnValue

    
    def storeCatalogString(self, catalogString, dnaString):
        returnValue = libtoontown._inPdt4y09hu(self.this, catalogString, dnaString)
        return returnValue

    
    def printCatalog(self):
        returnValue = libtoontown._inPdt4yeZRO(self.this)
        return returnValue

    
    def storeDNAGroup(self, parameter1, parameter2):
        returnValue = libtoontown._inPdt4y58dz(self.this, parameter1.this, parameter2.this)
        return returnValue

    
    def _DNAStorage__overloaded_removeDNAGroup_ptrDNAStorage_ptrDNAGroup(self, parameter1):
        returnValue = libtoontown._inPdt4yfgHa(self.this, parameter1.this)
        return returnValue

    
    def _DNAStorage__overloaded_removeDNAGroup_ptrDNAStorage_ptrPandaNode(self, parameter1):
        returnValue = libtoontown._inPdt4yPPXi(self.this, parameter1.this)
        return returnValue

    
    def findDNAGroup(self, parameter1):
        returnValue = libtoontown._inPdt4yrclV(self.this, parameter1.this)
        import DNAGroup
        returnObject = DNAGroup.DNAGroup(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def findPandaNode(self, parameter1):
        returnValue = libtoontown._inPdt4yXv_S(self.this, parameter1.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getZoneFromBlockNumber(self, blockNumber):
        returnValue = libtoontown._inPdt4y3eC0(self.this, blockNumber)
        return returnValue

    
    def getBlockNumberAt(self, index):
        returnValue = libtoontown._inPdt4yWn20(self.this, index)
        return returnValue

    
    def getNumBlockNumbers(self):
        returnValue = libtoontown._inPdt4y02aC(self.this)
        return returnValue

    
    def getDoorPosHprFromBlockNumber(self, blockNumber):
        returnValue = libtoontown._inPdt4yZL72(self.this, blockNumber)
        import PosHpr
        returnObject = PosHpr.PosHpr(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getDoorPosHprBlockAt(self, index):
        returnValue = libtoontown._inPdt4yV0BN(self.this, index)
        return returnValue

    
    def getNumBlockDoorPosHprs(self):
        returnValue = libtoontown._inPdt4ypwq_(self.this)
        return returnValue

    
    def getSignTransformFromBlockNumber(self, blockNumber):
        returnValue = libtoontown._inPdt4y0D3d(self.this, blockNumber)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getSignTransformBlockAt(self, index):
        returnValue = libtoontown._inPdt4ys3CU(self.this, index)
        return returnValue

    
    def getNumBlockSignTransforms(self):
        returnValue = libtoontown._inPdt4ybqAy(self.this)
        return returnValue

    
    def resetDNAGroups(self):
        returnValue = libtoontown._inPdt4yZDEH(self.this)
        return returnValue

    
    def getTitleFromBlockNumber(self, blockNumber):
        returnValue = libtoontown._inPdt4y7PHJ(self.this, blockNumber)
        return returnValue

    
    def getTitleBlockAt(self, index):
        returnValue = libtoontown._inPdt4yPXb6(self.this, index)
        return returnValue

    
    def getNumBlockTitles(self):
        returnValue = libtoontown._inPdt4yKg0v(self.this)
        return returnValue

    
    def getArticleFromBlockNumber(self, blockNumber):
        returnValue = libtoontown._inPdt4y2hU1(self.this, blockNumber)
        return returnValue

    
    def storeBlockBuildingType(self, block, type):
        returnValue = libtoontown._inPdt4yaOzR(self.this, block, type)
        return returnValue

    
    def getBlockBuildingType(self, blockNumber):
        returnValue = libtoontown._inPdt4y66IJ(self.this, blockNumber)
        return returnValue

    
    def storeDNAVisGroup(self, parameter1, parameter2):
        returnValue = libtoontown._inPdt4yEMo_(self.this, parameter1.this, parameter2.this)
        return returnValue

    
    def removeDNAVisGroup(self, parameter1):
        returnValue = libtoontown._inPdt4ynHea(self.this, parameter1.this)
        return returnValue

    
    def findDNAVisGroup(self, parameter1):
        returnValue = libtoontown._inPdt4yylbh(self.this, parameter1.this)
        import DNAVisGroup
        returnObject = DNAVisGroup.DNAVisGroup(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def resetDNAVisGroups(self):
        returnValue = libtoontown._inPdt4yfVv1(self.this)
        return returnValue

    
    def getNumDNAVisGroups(self):
        returnValue = libtoontown._inPdt4yvTr_(self.this)
        return returnValue

    
    def getDNAVisGroup(self, i):
        returnValue = libtoontown._inPdt4yENmU(self.this, i)
        import DNAVisGroup
        returnObject = DNAVisGroup.DNAVisGroup(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNumVisiblesInDNAVisGroup(self, i):
        returnValue = libtoontown._inPdt4yjPwk(self.this, i)
        return returnValue

    
    def getDNAVisGroupName(self, i):
        returnValue = libtoontown._inPdt4yECe3(self.this, i)
        return returnValue

    
    def getVisibleName(self, visgroupIndex, visibleIndex):
        returnValue = libtoontown._inPdt4yLlmc(self.this, visgroupIndex, visibleIndex)
        return returnValue

    
    def storeDNAVisGroupAI(self, parameter1):
        returnValue = libtoontown._inPdt4yub1T(self.this, parameter1.this)
        return returnValue

    
    def getNumDNAVisGroupsAI(self):
        returnValue = libtoontown._inPdt4yOfP2(self.this)
        return returnValue

    
    def getDNAVisGroupAI(self, i):
        returnValue = libtoontown._inPdt4y6luo(self.this, i)
        import DNAVisGroup
        returnObject = DNAVisGroup.DNAVisGroup(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def resetDNAVisGroupsAI(self):
        returnValue = libtoontown._inPdt4ySaG0(self.this)
        return returnValue

    
    def getNumPandaNodes(self):
        returnValue = libtoontown._inPdt4yIV4p(self.this)
        return returnValue

    
    def getPandaNodeAt(self, i):
        returnValue = libtoontown._inPdt4yl1j8(self.this, i)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def printPandaNodes(self):
        returnValue = libtoontown._inPdt4yQHj_(self.this)
        return returnValue

    
    def getSuitEdgeZone(self, startIndex, endIndex):
        returnValue = libtoontown._inPdt4yTH_i(self.this, startIndex, endIndex)
        return returnValue

    
    def getSuitEdgeTravelTime(self, startIndex, endIndex, rate):
        returnValue = libtoontown._inPdt4y_vok(self.this, startIndex, endIndex, rate)
        return returnValue

    
    def getNumSuitPoints(self):
        returnValue = libtoontown._inPdt4yK942(self.this)
        return returnValue

    
    def getSuitPointAtIndex(self, index):
        returnValue = libtoontown._inPdt4yjv3i(self.this, index)
        import DNASuitPoint
        returnObject = DNASuitPoint.DNASuitPoint(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getSuitPointWithIndex(self, index):
        returnValue = libtoontown._inPdt4yw37H(self.this, index)
        import DNASuitPoint
        returnObject = DNASuitPoint.DNASuitPoint(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getSuitPath(self, startPoint, endPoint, minLength, maxLength):
        returnValue = libtoontown._inPdt4ywYaP(self.this, startPoint.this, endPoint.this, minLength, maxLength)
        import DNASuitPath
        returnObject = DNASuitPath.DNASuitPath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getAdjacentPoints(self, startPoint):
        returnValue = libtoontown._inPdt4y0G80(self.this, startPoint.this)
        import DNASuitPath
        returnObject = DNASuitPath.DNASuitPath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def discoverContinuity(self):
        returnValue = libtoontown._inPdt4ysx_x(self.this)
        return returnValue

    
    def getBlock(self, name):
        returnValue = libtoontown._inPdt4yh1k3(self.this, name)
        return returnValue

    
    def fixup(self):
        returnValue = libtoontown._inPdt4ylyrU(self.this)
        return returnValue

    
    def write(self, out, indentLevel):
        returnValue = libtoontown._inPdt4yyhF4(self.this, out.this, indentLevel)
        return returnValue

    
    def storeHoodNode(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._DNAStorage__overloaded_storeHoodNode_ptrDNAStorage_atomicstring_ptrNodePath(*_args)
        elif numArgs == 3:
            return self._DNAStorage__overloaded_storeHoodNode_ptrDNAStorage_atomicstring_ptrNodePath_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def removeDNAGroup(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                return self._DNAStorage__overloaded_removeDNAGroup_ptrDNAStorage_ptrPandaNode(*_args)
            
            import DNAGroup
            if isinstance(_args[0], DNAGroup.DNAGroup):
                return self._DNAStorage__overloaded_removeDNAGroup_ptrDNAStorage_ptrDNAGroup(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <PandaNode.PandaNode> <DNAGroup.DNAGroup> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def storeSuitEdge(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._DNAStorage__overloaded_storeSuitEdge_ptrDNAStorage_ptrDNASuitEdge(*_args)
        elif numArgs == 3:
            return self._DNAStorage__overloaded_storeSuitEdge_ptrDNAStorage_int_int_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def storeSuitPoint(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._DNAStorage__overloaded_storeSuitPoint_ptrDNAStorage_ptrDNASuitPoint(*_args)
        elif numArgs == 2:
            return self._DNAStorage__overloaded_storeSuitPoint_ptrDNAStorage___enum__DNASuitPointType_ptrLPoint3f(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def storeNode(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._DNAStorage__overloaded_storeNode_ptrDNAStorage_atomicstring_ptrNodePath(*_args)
        elif numArgs == 3:
            return self._DNAStorage__overloaded_storeNode_ptrDNAStorage_atomicstring_ptrNodePath_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def storePlaceNode(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._DNAStorage__overloaded_storePlaceNode_ptrDNAStorage_atomicstring_ptrNodePath(*_args)
        elif numArgs == 3:
            return self._DNAStorage__overloaded_storePlaceNode_ptrDNAStorage_atomicstring_ptrNodePath_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


