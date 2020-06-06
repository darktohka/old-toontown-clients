# File: D (Python 2.2)

from ToonBaseGlobal import *
from ShowBaseGlobal import *
from IntervalGlobal import *
from ClockDelta import *
import ToontownGlobals
import ToonInterior
import DirectNotifyGlobal
import DistributedObject
import DNADoor
import random
import ToonInteriorColors
import ZoneUtil
import Char
import AvatarDNA
import Suit
import QuestParser

class DistributedTutorialInterior(DistributedObject.DistributedObject):
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    
    def generate(self):
        DistributedObject.DistributedObject.generate(self)

    
    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)
        self.setup()

    
    def disable(self):
        self.interior.removeNode()
        del self.interior
        self.street.removeNode()
        del self.street
        self.sky.removeNode()
        del self.sky
        self.mickeyMovie.cleanup()
        del self.mickeyMovie
        self.suitWalkTrack.finish()
        del self.suitWalkTrack
        self.suit.delete()
        del self.suit
        self.ignore('enterTutotialInterior')

    
    def delete(self):
        DistributedObject.DistributedObject.delete(self)

    
    def randomDNAItem(self, category, findFunc):
        codeCount = self.dnaStore.getNumCatalogCodes(category)
        index = self.randomGenerator.randint(0, codeCount - 1)
        code = self.dnaStore.getCatalogCode(category, index)
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
        self.randomGenerator.seed(self.zoneId)
        self.interior = loader.loadModel('phase_3.5/models/modules/toon_interior_tutorial')
        self.interior.reparentTo(render)
        dnaStore = DNAStorage()
        node = loader.loadDNAFile(self.cr.playGame.hood.dnaStore, 'phase_3.5/dna/tutorial_street.dna')
        self.street = render.attachNewNode(node)
        self.street.flattenMedium()
        self.street.setPosHpr(-12, 42, -0.5, 180, 0, 0)
        self.street.find('**/tb2:toon_landmark_TT_A1_DNARoot').stash()
        self.street.find('**/tb1:toon_landmark_hqTT_DNARoot/**/door_flat_0').stash()
        self.street.findAllMatches('**/+CollisionNode').stash()
        self.skyFile = 'phase_3.5/models/props/TT_sky'
        self.sky = loader.loadModel(self.skyFile)
        self.sky.setScale(0.80000000000000004)
        self.sky.reparentTo(render)
        self.sky.setDepthTest(0)
        self.sky.setDepthWrite(0)
        self.sky.setBin('background', 100)
        self.sky.find('**/Sky').reparentTo(self.sky, -1)
        hoodId = ZoneUtil.getHoodId(self.zoneId)
        self.colors = ToonInteriorColors.colors[hoodId]
        self.replaceRandomInModel(self.interior)
        doorModelName = 'door_double_round_ul'
        if doorModelName[-1:] == 'r':
            doorModelName = doorModelName[:-1] + 'l'
        else:
            doorModelName = doorModelName[:-1] + 'r'
        door = self.dnaStore.findNode(doorModelName)
        door_origin = render.find('**/door_origin;+s')
        doorNP = door.copyTo(door_origin)
        door_origin.setScale(0.80000000000000004, 0.80000000000000004, 0.80000000000000004)
        door_origin.setPos(door_origin, 0, -0.025000000000000001, 0)
        color = self.randomGenerator.choice(self.colors['TI_door'])
        DNADoor.DNADoor.setupDoor(doorNP, self.interior, door_origin, self.dnaStore, str(self.block), color)
        doorFrame = doorNP.find('door_*_flat')
        doorFrame.wrtReparentTo(self.interior)
        doorFrame.setColor(color)
        del self.colors
        del self.dnaStore
        del self.randomGenerator
        self.interior.flattenMedium()
        npcOrigin = self.interior.find('**/npc_origin_' + `self.npc.posIndex`)
        if not npcOrigin.isEmpty():
            self.npc.reparentTo(npcOrigin)
            self.npc.clearMat()
        
        self.createSuit()
        self.mickeyMovie = QuestParser.NPCMoviePlayer('tutorial_mickey', toonbase.localToon, self.npc)
        self.acceptOnce('enterTutorialInterior', self.mickeyMovie.play)

    
    def createSuit(self):
        self.suit = Suit.Suit()
        suitDNA = AvatarDNA.AvatarDNA()
        suitDNA.newSuit('f')
        self.suit.setDNA(suitDNA)
        self.suit.loop('neutral')
        self.suit.setPosHpr(-20, 8, 0, 0, 0, 0)
        self.suit.reparentTo(self.interior)
        self.suitWalkTrack = Sequence(self.suit.hprInterval(0.10000000000000001, Vec3(0, 0, 0)), Func(self.suit.loop, 'walk'), self.suit.posInterval(2, Point3(-20, 20, 0)), Func(self.suit.loop, 'neutral'), Wait(1.0), self.suit.hprInterval(0.10000000000000001, Vec3(180, 0, 0)), Func(self.suit.loop, 'walk'), self.suit.posInterval(2, Point3(-20, 10, 0)), Func(self.suit.loop, 'neutral'), Wait(1.0))
        self.suitWalkTrack.loop()

    
    def setZoneIdAndBlock(self, zoneId, block):
        self.zoneId = zoneId
        self.block = block

    
    def setTutorialNpcId(self, npcId):
        self.npcId = npcId
        self.npc = self.cr.doId2do[npcId]


