# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import FFIExternalObject

class DNAStorage(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libtoontown._inPet4y1ZFR()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPet4yEqD8:
            libtoontown._inPet4yEqD8(self.this)
        

    
    def printNodeStorage(self):
        returnValue = libtoontown._inPet4yvzwk(self.this)
        return returnValue

    
    def printTextureStorage(self):
        returnValue = libtoontown._inPet4yriYa(self.this)
        return returnValue

    
    def printFontStorage(self):
        returnValue = libtoontown._inPet4yczQC(self.this)
        return returnValue

    
    def printSuitPointStorage(self):
        returnValue = libtoontown._inPet4yHsM_(self.this)
        return returnValue

    
    def printBattleCellStorage(self):
        returnValue = libtoontown._inPet4yZH2Z(self.this)
        return returnValue

    
    def storeTexture(self, codeString, texture):
        returnValue = libtoontown._inPet4y_9Ok(self.this, codeString, texture.this)
        return returnValue

    
    def storeFont(self, codeString, font):
        returnValue = libtoontown._inPet4yOpZl(self.this, codeString, font.this)
        return returnValue

    
    def storeNode(self, codeString, node):
        returnValue = libtoontown._inPet4yCtk7(self.this, codeString, node.this)
        return returnValue

    
    def storeHoodNode(self, codeString, node):
        returnValue = libtoontown._inPet4yP0tW(self.this, codeString, node.this)
        return returnValue

    
    def storePlaceNode(self, codeString, node):
        returnValue = libtoontown._inPet4y_Bg6(self.this, codeString, node.this)
        return returnValue

    
    def _DNAStorage__overloaded_storeSuitPoint_ptrDNAStorage___enum__DNASuitPointType_ptrLPoint3f(self, type, pos):
        returnValue = libtoontown._inPet4yo1kA(self.this, type, pos.this)
        import DNASuitPoint
        returnObject = DNASuitPoint.DNASuitPoint(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _DNAStorage__overloaded_storeSuitPoint_ptrDNAStorage_ptrDNASuitPoint(self, parameter1):
        returnValue = libtoontown._inPet4yDhAr(self.this, parameter1.this)
        return returnValue

    
    def getHighestSuitPointIndex(self):
        returnValue = libtoontown._inPet4yuwaV(self.this)
        return returnValue

    
    def removeSuitPoint(self, parameter1):
        returnValue = libtoontown._inPet4yKUVm(self.this, parameter1.this)
        return returnValue

    
    def storeBlockNumber(self, block, zoneId):
        returnValue = libtoontown._inPet4yYH3h(self.this, block, zoneId)
        return returnValue

    
    def storeBlockDoorPosHpr(self, block, pos, hpr):
        returnValue = libtoontown._inPet4yixgm(self.this, block, pos.this, hpr.this)
        return returnValue

    
    def storeBlockSignTransform(self, block, mat):
        returnValue = libtoontown._inPet4y_j4y(self.this, block, mat.this)
        return returnValue

    
    def storeBlockTitle(self, block, title):
        returnValue = libtoontown._inPet4yL106(self.this, block, title)
        return returnValue

    
    def storeBattleCell(self, parameter1):
        returnValue = libtoontown._inPet4yMkDh(self.this, parameter1.this)
        return returnValue

    
    def removeBattleCell(self, parameter1):
        returnValue = libtoontown._inPet4yLnto(self.this, parameter1.this)
        return returnValue

    
    def _DNAStorage__overloaded_storeSuitEdge_ptrDNAStorage_ptrDNASuitEdge(self, parameter1):
        returnValue = libtoontown._inPet4yWErq(self.this, parameter1.this)
        import DNASuitEdge
        returnObject = DNASuitEdge.DNASuitEdge(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _DNAStorage__overloaded_storeSuitEdge_ptrDNAStorage_int_int_atomicstring(self, startIndex, endIndex, zoneId):
        returnValue = libtoontown._inPet4yXQZ8(self.this, startIndex, endIndex, zoneId)
        import DNASuitEdge
        returnObject = DNASuitEdge.DNASuitEdge(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def removeSuitEdge(self, parameter1):
        returnValue = libtoontown._inPet4yuWHb(self.this, parameter1.this)
        return returnValue

    
    def deleteUnusedSuitPoints(self):
        returnValue = libtoontown._inPet4yyNi7(self.this)
        return returnValue

    
    def fixCoincidentSuitPoints(self):
        returnValue = libtoontown._inPet4ykZjO(self.this)
        return returnValue

    
    def resetNodes(self):
        returnValue = libtoontown._inPet4ybe4o(self.this)
        return returnValue

    
    def resetTextures(self):
        returnValue = libtoontown._inPet4ybEjQ(self.this)
        return returnValue

    
    def resetHood(self):
        returnValue = libtoontown._inPet4yhO48(self.this)
        return returnValue

    
    def resetHoodNodes(self):
        returnValue = libtoontown._inPet4yprns(self.this)
        return returnValue

    
    def resetPlaceNodes(self):
        returnValue = libtoontown._inPet4yhCLk(self.this)
        return returnValue

    
    def resetSuitPoints(self):
        returnValue = libtoontown._inPet4yak05(self.this)
        return returnValue

    
    def resetBattleCells(self):
        returnValue = libtoontown._inPet4ymT1N(self.this)
        return returnValue

    
    def resetBlockNumbers(self):
        returnValue = libtoontown._inPet4y_J6Q(self.this)
        return returnValue

    
    def resetBlockDoorPosHprs(self):
        returnValue = libtoontown._inPet4yV_iW(self.this)
        return returnValue

    
    def resetBlockSignTransforms(self):
        returnValue = libtoontown._inPet4yBGek(self.this)
        return returnValue

    
    def resetBlockTitle(self):
        returnValue = libtoontown._inPet4y1OEc(self.this)
        return returnValue

    
    def findTexture(self, dnaString):
        returnValue = libtoontown._inPet4yrgKy(self.this, dnaString)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def findNode(self, dnaString):
        returnValue = libtoontown._inPet4yz7Kg(self.this, dnaString)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def findFont(self, dnaString):
        returnValue = libtoontown._inPet4yKEGD(self.this, dnaString)
        import TextFont
        returnObject = TextFont.TextFont(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNumCatalogCodes(self, catalogString):
        returnValue = libtoontown._inPet4y0qRV(self.this, catalogString)
        return returnValue

    
    def getCatalogCode(self, catalogString, i):
        returnValue = libtoontown._inPet4yhTPT(self.this, catalogString, i)
        return returnValue

    
    def storeCatalogString(self, catalogString, dnaString):
        returnValue = libtoontown._inPet4y19hu(self.this, catalogString, dnaString)
        return returnValue

    
    def printCatalog(self):
        returnValue = libtoontown._inPet4yeZRO(self.this)
        return returnValue

    
    def storeDNAGroup(self, parameter1, parameter2):
        returnValue = libtoontown._inPet4yG9dz(self.this, parameter1.this, parameter2.this)
        return returnValue

    
    def _DNAStorage__overloaded_removeDNAGroup_ptrDNAStorage_ptrDNAGroup(self, parameter1):
        returnValue = libtoontown._inPet4yfgHa(self.this, parameter1.this)
        return returnValue

    
    def _DNAStorage__overloaded_removeDNAGroup_ptrDNAStorage_ptrPandaNode(self, parameter1):
        returnValue = libtoontown._inPet4yAPXi(self.this, parameter1.this)
        return returnValue

    
    def findDNAGroup(self, parameter1):
        returnValue = libtoontown._inPet4yrclV(self.this, parameter1.this)
        import DNAGroup
        returnObject = DNAGroup.DNAGroup(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def findPandaNode(self, parameter1):
        returnValue = libtoontown._inPet4yXv_S(self.this, parameter1.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getZoneFromBlockNumber(self, blockNumber):
        returnValue = libtoontown._inPet4yweC0(self.this, blockNumber)
        return returnValue

    
    def getBlockNumberAt(self, index):
        returnValue = libtoontown._inPet4yVn20(self.this, index)
        return returnValue

    
    def getNumBlockNumbers(self):
        returnValue = libtoontown._inPet4y02aC(self.this)
        return returnValue

    
    def getDoorPosHprFromBlockNumber(self, blockNumber):
        returnValue = libtoontown._inPet4yYL72(self.this, blockNumber)
        import PosHpr
        returnObject = PosHpr.PosHpr(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getDoorPosHprBlockAt(self, index):
        returnValue = libtoontown._inPet4yV0BN(self.this, index)
        return returnValue

    
    def getNumBlockDoorPosHprs(self):
        returnValue = libtoontown._inPet4yqwq_(self.this)
        return returnValue

    
    def getSignTransformFromBlockNumber(self, blockNumber):
        returnValue = libtoontown._inPet4y0D3d(self.this, blockNumber)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getSignTransformBlockAt(self, index):
        returnValue = libtoontown._inPet4ys3CU(self.this, index)
        return returnValue

    
    def getNumBlockSignTransforms(self):
        returnValue = libtoontown._inPet4yaqAy(self.this)
        return returnValue

    
    def resetDNAGroups(self):
        returnValue = libtoontown._inPet4yZDEH(self.this)
        return returnValue

    
    def getTitleFromBlockNumber(self, blockNumber):
        returnValue = libtoontown._inPet4y7PHJ(self.this, blockNumber)
        return returnValue

    
    def getTitleBlockAt(self, index):
        returnValue = libtoontown._inPet4yOXb6(self.this, index)
        return returnValue

    
    def getNumBlockTitles(self):
        returnValue = libtoontown._inPet4yLg0v(self.this)
        return returnValue

    
    def storeBlockBuildingType(self, block, type):
        returnValue = libtoontown._inPet4yaOzR(self.this, block, type)
        return returnValue

    
    def getBlockBuildingType(self, blockNumber):
        returnValue = libtoontown._inPet4y66IJ(self.this, blockNumber)
        return returnValue

    
    def storeDNAVisGroup(self, parameter1, parameter2):
        returnValue = libtoontown._inPet4yLMo_(self.this, parameter1.this, parameter2.this)
        return returnValue

    
    def removeDNAVisGroup(self, parameter1):
        returnValue = libtoontown._inPet4ynHea(self.this, parameter1.this)
        return returnValue

    
    def findDNAVisGroup(self, parameter1):
        returnValue = libtoontown._inPet4yxlbh(self.this, parameter1.this)
        import DNAVisGroup
        returnObject = DNAVisGroup.DNAVisGroup(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def resetDNAVisGroups(self):
        returnValue = libtoontown._inPet4yAVv1(self.this)
        return returnValue

    
    def getNumDNAVisGroups(self):
        returnValue = libtoontown._inPet4ysTr_(self.this)
        return returnValue

    
    def getDNAVisGroup(self, i):
        returnValue = libtoontown._inPet4yENmU(self.this, i)
        import DNAVisGroup
        returnObject = DNAVisGroup.DNAVisGroup(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNumVisiblesInDNAVisGroup(self, i):
        returnValue = libtoontown._inPet4ysPwk(self.this, i)
        return returnValue

    
    def getDNAVisGroupName(self, i):
        returnValue = libtoontown._inPet4yHCe3(self.this, i)
        return returnValue

    
    def getVisibleName(self, visgroupIndex, visibleIndex):
        returnValue = libtoontown._inPet4yLlmc(self.this, visgroupIndex, visibleIndex)
        return returnValue

    
    def storeDNAVisGroupAI(self, parameter1):
        returnValue = libtoontown._inPet4yub1T(self.this, parameter1.this)
        return returnValue

    
    def getNumDNAVisGroupsAI(self):
        returnValue = libtoontown._inPet4yNfP2(self.this)
        return returnValue

    
    def getDNAVisGroupAI(self, i):
        returnValue = libtoontown._inPet4y7luo(self.this, i)
        import DNAVisGroup
        returnObject = DNAVisGroup.DNAVisGroup(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def resetDNAVisGroupsAI(self):
        returnValue = libtoontown._inPet4yRaG0(self.this)
        return returnValue

    
    def getNumPandaNodes(self):
        returnValue = libtoontown._inPet4yJV4p(self.this)
        return returnValue

    
    def getPandaNodeAt(self, i):
        returnValue = libtoontown._inPet4yk1j8(self.this, i)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def printPandaNodes(self):
        returnValue = libtoontown._inPet4yRHj_(self.this)
        return returnValue

    
    def getSuitEdgeZone(self, startIndex, endIndex):
        returnValue = libtoontown._inPet4yUH_i(self.this, startIndex, endIndex)
        return returnValue

    
    def getSuitEdgeTravelTime(self, startIndex, endIndex, rate):
        returnValue = libtoontown._inPet4y_vok(self.this, startIndex, endIndex, rate)
        return returnValue

    
    def getNumSuitPoints(self):
        returnValue = libtoontown._inPet4yN942(self.this)
        return returnValue

    
    def getSuitPointAtIndex(self, index):
        returnValue = libtoontown._inPet4ysv3i(self.this, index)
        import DNASuitPoint
        returnObject = DNASuitPoint.DNASuitPoint(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getSuitPointWithIndex(self, index):
        returnValue = libtoontown._inPet4yw37H(self.this, index)
        import DNASuitPoint
        returnObject = DNASuitPoint.DNASuitPoint(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getSuitPath(self, startPoint, endPoint):
        returnValue = libtoontown._inPet4yNHHg(self.this, startPoint.this, endPoint.this)
        import DNASuitPath
        returnObject = DNASuitPath.DNASuitPath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getAdjacentPoints(self, startPoint):
        returnValue = libtoontown._inPet4yzG80(self.this, startPoint.this)
        import DNASuitPath
        returnObject = DNASuitPath.DNASuitPath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getBlock(self, name):
        returnValue = libtoontown._inPet4yi1k3(self.this, name)
        return returnValue

    
    def fixup(self):
        returnValue = libtoontown._inPet4ylyrU(self.this)
        return returnValue

    
    def write(self, out, indentLevel):
        returnValue = libtoontown._inPet4yzhF4(self.this, out.this, indentLevel)
        return returnValue

    
    def storeSuitPoint(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import DNASuitPoint
            if isinstance(_args[0], DNASuitPoint.DNASuitPoint):
                return self._DNAStorage__overloaded_storeSuitPoint_ptrDNAStorage_ptrDNASuitPoint(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <DNASuitPoint.DNASuitPoint> '
        elif numArgs == 2:
            if isinstance(_args[0], types.IntType):
                import Point3
                if isinstance(_args[1], Point3.Point3):
                    return self._DNAStorage__overloaded_storeSuitPoint_ptrDNAStorage___enum__DNASuitPointType_ptrLPoint3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def removeDNAGroup(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            import DNAGroup
            if isinstance(_args[0], PandaNode.PandaNode):
                return self._DNAStorage__overloaded_removeDNAGroup_ptrDNAStorage_ptrPandaNode(_args[0])
            elif isinstance(_args[0], DNAGroup.DNAGroup):
                return self._DNAStorage__overloaded_removeDNAGroup_ptrDNAStorage_ptrDNAGroup(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PandaNode.PandaNode> <DNAGroup.DNAGroup> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def storeSuitEdge(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import DNASuitEdge
            if isinstance(_args[0], DNASuitEdge.DNASuitEdge):
                return self._DNAStorage__overloaded_storeSuitEdge_ptrDNAStorage_ptrDNASuitEdge(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <DNASuitEdge.DNASuitEdge> '
        elif numArgs == 3:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.StringType):
                        return self._DNAStorage__overloaded_storeSuitEdge_ptrDNAStorage_int_int_atomicstring(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.StringType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


