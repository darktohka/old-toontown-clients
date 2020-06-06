# File: D (Python 2.2)

from ToontownGlobals import *
from ToonBaseGlobal import *
from ShowBaseGlobal import *
from IntervalGlobal import *
from ClockDelta import *
import DirectNotifyGlobal
import FSM
import DistributedObject
import State
import DNADoor
import random
import ToonInteriorColors
import CollisionSphere
import CollisionNode
import ZoneUtil
import AvatarDNA
import ToonHead
import HouseGlobals

class DistributedHouseInterior(DistributedObject.DistributedObject):
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.fsm = FSM.FSM('DistributedHouseInterior', [
            State.State('toon', self.enterToon, self.exitToon, [
                'off']),
            State.State('off', self.enterOff, self.exitOff, [
                'toon'])], 'off', 'off')
        self.houseId = 0
        self.houseIndex = 0
        self.wallColorIndex = 0
        self.interior = None
        self.interiorType = 2
        self.storageDNAFile = 'phase_5.5/dna/storage_house_interior.dna'
        self.fsm.enterInitialState()

    
    def generate(self):
        DistributedObject.DistributedObject.generate(self)

    
    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)
        self.setup()

    
    def disable(self):
        self.interior.removeNode()
        del self.interior

    
    def delete(self):
        self.ignore(self.uniqueName('enterclosetSphere'))
        del self.fsm
        self.closetNode.removeNode()
        del self.closetNode
        self.bankNode.removeNode()
        del self.bankNode
        DistributedObject.DistributedObject.delete(self)

    
    def randomDNAItem(self, category, findFunc):
        codeCount = self.dnaStore.getNumCatalogCodes(category)
        index = self.randomGenerator.randint(0, codeCount - 1)
        code = self.dnaStore.getCatalogCode(category, index)
        print '%s, int = %s, code = %s' % (category, index, code)
        return findFunc(code)

    
    def replaceRandomInModel(self, model):
        baseTag = 'random_'
        npc = model.findAllMatches('**/' + baseTag + '???_*')
        for i in range(npc.getNumPaths()):
            np = npc.getPath(i)
            name = np.getName()
            b = len(baseTag)
            category = name[b + 4:]
            key1 = name[b]
            key2 = name[b + 1]
            if key1 == 'm':
                model = self.randomDNAItem(category, self.dnaStore.findNode)
                newNP = model.copyTo(np)
                if key2 == 'r':
                    self.replaceRandomInModel(newNP)
                
            elif key1 == 't':
                texture = self.randomDNAItem(category, self.dnaStore.findTexture)
                np.setTexture(texture, 100)
                newNP = np
            
            if key2 == 'c':
                newNP.setColorScale(self.randomGenerator.choice(self.colors[category]))
            
        

    
    def setup(self):
        self.dnaStore = toonbase.tcr.playGame.dnaStore
        self.randomGenerator = random.Random()
        seed = self.houseId >> 1 & 15
        self.randomGenerator.seed(seed)
        self.dnaFile = HouseGlobals.interiors[self.interiorType][0]
        loader.loadDNAFile(self.dnaStore, self.storageDNAFile)
        node = loader.loadDNAFile(self.dnaStore, self.dnaFile)
        if node.getNumParents() == 0:
            interior = NodePath(node)
        
        self.interior = interior
        self.interior.reparentTo(render)
        hoodId = MyEstate
        self.colors = ToonInteriorColors.colors[hoodId]
        doorModelName = 'door_double_round_ur'
        if doorModelName[-1:] == 'r':
            doorModelName = doorModelName[:-1] + 'l'
        else:
            doorModelName = doorModelName[:-1] + 'r'
        door = self.dnaStore.findNode(doorModelName)
        door_origin = interior.find('**/door_origin')
        door_origin.setH(180)
        doorNP = door.copyTo(door_origin)
        doorNP.ls()
        door_origin.setScale(0.80000000000000004, 0.80000000000000004, 0.80000000000000004)
        door_origin.setPos(door_origin, 0, -0.025000000000000001, 0)
        houseColor = HouseGlobals.atticWood
        color = Vec4(houseColor[0], houseColor[1], houseColor[2], 1)
        DNADoor.DNADoor.setupDoor(doorNP, self.interior, door_origin, self.dnaStore, str(self.houseId), color)
        doorFrame = doorNP.find('door_*_flat')
        doorFrame.wrtReparentTo(self.interior)
        doorFrame.setColor(color)
        del self.colors
        del self.dnaStore
        del self.randomGenerator
        self._DistributedHouseInterior__setupClosetNode()
        self._DistributedHouseInterior__setupBankNode()
        self._DistributedHouseInterior__colorWalls()
        self._DistributedHouseInterior__setupWindowBoxes()
        self.fsm.request('toon')

    
    def _DistributedHouseInterior__colorWalls(self):
        sideWallNames = [
            'wall_side_top',
            'wall_side_middle',
            'wall_side_bottom']
        frontWallNames = [
            'wall_front_top',
            'wall_front_middle',
            'wall_front_bottom']
        frontWindows = [
            'windowcut_c',
            'windowcut_e',
            'windowcut_f']
        sideWindows = [
            'windowcut_a',
            'windowcut_b',
            'windowcut_d']
        woods = [
            'wall_side_top',
            'wall_side_bottom',
            'wall_front_top',
            'wall_front_bottom',
            'floor']
        
        def clamp(k, col):
            (a, b, c) = col
            a = a * k
            b = b * k
            c = c * k
            if a > 1.0:
                a = 1.0
            
            if b > 1.0:
                b = 1.0
            
            if c > 1.0:
                c = 1.0
            
            return [
                a,
                b,
                c]

        ks = 1.0
        kf = 1.0
        kt = 1.0
        col = HouseGlobals.interiorColors[self.wallColorIndex]
        side = clamp(ks, col)
        front = clamp(kf, col)
        top = clamp(kt, col)
        sideNode = self.interior.find('**/' + sideWallNames[1])
        sideNode.setColorScale(side[0], side[1], side[2], 1)
        frontNode = self.interior.find('**/' + frontWallNames[1])
        frontNode.setColorScale(front[0], front[1], front[2], 1)
        for window in sideWindows:
            node = self.interior.find('**/' + window)
            node.setColorScale(side[0], side[1], side[2], 1)
        
        for window in frontWindows:
            node = self.interior.find('**/' + window)
            node.setColorScale(front[0], front[1], front[2], 1)
        
        node = self.interior.find('**/ceiling')
        node.setColorScale(top[0], top[1], top[2], 1)
        woodCol = HouseGlobals.interiorWood[self.wallColorIndex]
        for wood in woods:
            node = self.interior.find('**/' + wood)
            node.setColorScale(woodCol[0], woodCol[1], woodCol[2], 1)
        
        archCol = HouseGlobals.archWood
        arch = self.interior.find('**/arch')
        arch.setColorScale(archCol[0], archCol[1], archCol[2], 1)
        arch1 = self.interior.find('**/arch1')
        arch1.setColorScale(archCol[0], archCol[1], archCol[2], 1)

    
    def _DistributedHouseInterior__setupClosetNode(self):
        (x, y, z, h, p, r) = HouseGlobals.interiors[self.interiorType][1]
        self.closetNode = self.interior.find('**/closet*').attachNewNode('closet_origin')

    
    def _DistributedHouseInterior__setupBankNode(self):
        (x, y, z, h, p, r) = HouseGlobals.interiors[self.interiorType][2]
        self.bankNode = self.interior.find('**/jellybeanBank*').attachNewNode('bank_origin')

    
    def _DistributedHouseInterior__setupWindowBoxes(self):
        windowcuts = HouseGlobals.interiors[self.interiorType][3]
        for cut in windowcuts:
            self.interior.find('**/windowcut_' + cut).reparentTo(hidden)
        
        col = HouseGlobals.windowWood
        frameColor = Vec4(col[0], col[1], col[2], 1)
        windowFrames = self.interior.findAllMatches('**/window')
        for frameNum in range(0, windowFrames.getNumPaths()):
            windowFrames.getPath(frameNum).setColor(frameColor)
        

    
    def _DistributedHouseInterior__setupWindowBoxesHardCoded(self):
        windowA = self.interior.find('**/windowcut_a')
        windowB = self.interior.find('**/windowcut_b')
        box1 = loader.loadModel('phase_5.5/models/estate/Garden1.bam')
        nodeA = box1.copyTo(windowA)
        nodeB = box1.copyTo(windowB)
        nodeA.wrtReparentTo(windowA.getParent())
        nodeB.wrtReparentTo(windowB.getParent())
        windowA.hide()
        windowB.hide()
        windowC = self.interior.find('**/windowcut_c')
        box2 = loader.loadModel('phase_5.5/models/estate/city1.bam')
        nodeC = box2.copyTo(windowC)
        nodeC.wrtReparentTo(windowC.getParent())
        windowC.hide()
        toonbase.localToon.windows = [
            nodeA,
            nodeB,
            nodeC]

    
    def _DistributedHouseInterior__setupFurniture(self):
        bedModels = [
            'phase_5.5/models/estate/regular_bed.bam',
            'phase_5.5/models/estate/girly_bed.bam',
            'phase_5.5/models/estate/bathtub_bed.bam']
        fireplaceModels = [
            'phase_5.5/models/estate/FireplaceSq.bam',
            'phase_5.5/models/estate/FireplaceGirlee.bam',
            'phase_5.5/models/estate/FireplaceRound.bam']
        instrumentModels = [
            'phase_5.5/models/estate/Piano.bam',
            'phase_5.5/models/estate/Organ.bam']
        chairModels = [
            'phase_5.5/models/estate/chairA.bam']
        bed = loader.loadModel(bedModels[0])
        fireplace = loader.loadModel(fireplaceModels[0])
        chair = loader.loadModel(chairModels[0])
        bed.reparentTo(self.interior)
        bed.setPosHpr(-21.9712, 5.00176, 0.025000000000000001, 135, 0, 0)
        fireplace.reparentTo(self.interior)
        fireplace.setPosHpr(16.0425, -8.7587100000000007, 0.025000000000000001, -90, 0, 0)
        chair.reparentTo(self.interior)
        chair.setScale(12)
        chair.setPosHpr(3.73875, -1.8299799999999999, 0.025000000000000001, 22.5, 0, 0)
        chair2 = chair.copyTo(self.interior)
        chair2.setScale(12)
        chair2.setPosHpr(8.8294300000000003, 0, 0.025000000000000001, -45, 0, 0)

    
    def enter(self):
        self.fsm.request('toon')

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterToon(self):
        pass

    
    def exitToon(self):
        pass

    
    def setHouseId(self, index):
        self.houseId = index

    
    def setHouseIndex(self, index):
        self.houseIndex = index

    
    def setWallColor(self, index):
        self.wallColorIndex = index

    
    def handleEnterSphere(self, collEntry):
        messenger.send('enterCloset', [
            collEntry])


