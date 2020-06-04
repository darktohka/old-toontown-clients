# File: D (Python 2.2)

from ToonBaseGlobal import *
from ShowBaseGlobal import *
from IntervalGlobal import *
from ClockDelta import *
import ToontownGlobals
import cPickle
import ToonInterior
import DirectNotifyGlobal
import FSM
import DistributedObject
import State
import random
import ToonInteriorColors
import ZoneUtil
import AvatarDNA
import ToonHead
SIGN_LEFT = -4
SIGN_RIGHT = 4
SIGN_BOTTOM = -3.5
SIGN_TOP = 1.5
FrameScale = 1.3999999999999999

class DistributedToonInterior(DistributedObject.DistributedObject):
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.fsm = FSM.FSM('DistributedToonInterior', [
            State.State('toon', self.enterToon, self.exitToon, [
                'beingTakenOver']),
            State.State('beingTakenOver', self.enterBeingTakenOver, self.exitBeingTakenOver, []),
            State.State('off', self.enterOff, self.exitOff, [])], 'toon', 'off')
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
        del self.fsm
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
                if category == 'TI_wallpaper' or category == 'TI_wallpaper_border':
                    self.randomGenerator.seed(self.zoneId)
                    newNP.setColorScale(self.randomGenerator.choice(self.colors[category]))
                else:
                    newNP.setColorScale(self.randomGenerator.choice(self.colors[category]))
            
        

    
    def setup(self):
        self.dnaStore = toonbase.tcr.playGame.dnaStore
        self.randomGenerator = random.Random()
        self.randomGenerator.seed(self.zoneId)
        interior = self.randomDNAItem('TI_room', self.dnaStore.findNode)
        self.interior = interior.copyTo(render)
        hoodId = ZoneUtil.getCanonicalHoodId(self.zoneId)
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
        DNADoor.setupDoor(doorNP, self.interior, door_origin, self.dnaStore, str(self.block), color)
        doorFrame = doorNP.find('door_*_flat')
        doorFrame.wrtReparentTo(self.interior)
        doorFrame.setColor(color)
        sign = hidden.find('**/tb' + str(self.block) + ':*_landmark_*_DNARoot/**/sign;+s')
        if not sign.isEmpty():
            signOrigin = self.interior.find('**/sign_origin;+s')
            newSignNP = sign.copyTo(signOrigin)
            mat = self.dnaStore.getSignTransformFromBlockNumber(int(self.block))
            inv = Mat4()
            inv.invertFrom(mat)
            newSignNP.setMat(inv)
            newSignNP.flattenLight()
            ll = Point3()
            ur = Point3()
            newSignNP.calcTightBounds(ll, ur)
            width = ur[0] - ll[0]
            height = ur[2] - ll[2]
            if width != 0 and height != 0:
                xScale = (SIGN_RIGHT - SIGN_LEFT) / width
                zScale = (SIGN_TOP - SIGN_BOTTOM) / height
                scale = min(xScale, zScale)
                xCenter = (ur[0] + ll[0]) / 2.0
                zCenter = (ur[2] + ll[2]) / 2.0
                newSignNP.setPosHprScale((SIGN_RIGHT + SIGN_LEFT) / 2.0 - xCenter * scale, -0.10000000000000001, (SIGN_TOP + SIGN_BOTTOM) / 2.0 - zCenter * scale, 0.0, 0.0, 0.0, scale, scale, scale)
            
        
        trophyOrigin = self.interior.find('**/trophy_origin')
        trophy = self.buildTrophy()
        if trophy:
            trophy.reparentTo(trophyOrigin)
        
        del self.colors
        del self.dnaStore
        del self.randomGenerator
        self.interior.flattenMedium()

    
    def setZoneIdAndBlock(self, zoneId, block):
        self.zoneId = zoneId
        self.block = block

    
    def setToonData(self, toonData):
        savedBy = cPickle.loads(toonData)
        self.savedBy = savedBy

    
    def buildTrophy(self):
        if self.savedBy == None:
            return None
        
        numToons = len(self.savedBy)
        pos = 1.25 - 1.25 * numToons
        trophy = hidden.attachNewNode('trophy')
        for (avId, name, dnaTuple) in self.savedBy:
            frame = self.buildFrame(name, dnaTuple)
            frame.reparentTo(trophy)
            frame.setPos(pos, 0, 0)
            pos += 2.5
        
        return trophy

    
    def buildFrame(self, name, dnaTuple):
        frame = loader.loadModelCopy('phase_3.5/models/modules/trophy_frame')
        dna = AvatarDNA.AvatarDNA()
        apply(dna.newToonFromProperties, dnaTuple)
        head = ToonHead.ToonHead()
        head.setupHead(dna)
        head.setPosHprScale(0, -0.050000000000000003, -0.050000000000000003, 180, 0, 0, 0.55000000000000004, 0.02, 0.55000000000000004)
        if dna.head[0] == 'r':
            head.setZ(-0.14999999999999999)
        elif dna.head[0] == 'h':
            head.setZ(0.050000000000000003)
        elif dna.head[0] == 'm':
            head.setScale(0.45000000000000001, 0.02, 0.45000000000000001)
        
        head.reparentTo(frame)
        nameText = TextNode('trophy')
        nameText.setFont(ToontownGlobals.getToonFont())
        nameText.setAlign(TextNode.ACenter)
        nameText.setTextColor(0, 0, 0, 1)
        nameText.setWordwrap(5.3600000000000003 * FrameScale)
        nameText.setText(name)
        namePath = frame.attachNewNode(nameText.generate())
        namePath.setPos(0, -0.029999999999999999, -0.59999999999999998)
        namePath.setScale(0.186 / FrameScale)
        frame.setScale(FrameScale, 1.0, FrameScale)
        return frame

    
    def setState(self, state, timestamp):
        self.fsm.request(state, [
            globalClockDelta.localElapsedTime(timestamp)])

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterToon(self):
        pass

    
    def exitToon(self):
        pass

    
    def enterBeingTakenOver(self, ts):
        messenger.send('clearOutToonInterior')

    
    def exitBeingTakenOver(self):
        pass


