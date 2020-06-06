# File: D (Python 2.2)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
from DirectGui import *
from ClockDelta import *
from OrthoWalk import *
from string import *
import ToontownGlobals
import DistributedObject
import DirectNotifyGlobal
import FSM
import State
import Toon
import AvatarDNA
import RandomNumGen
import Localizer
import random
import DelayDelete
import PythonUtil
import Place
import HouseGlobals
import DNADoor
import ToonInteriorColors

class DistributedHouse(DistributedObject.DistributedObject):
    notify = directNotify.newCategory('DistributedHouse')
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.houseType = None
        self.avId = -1
        self.ownerId = 0
        self.colorIndex = 0
        self.house = None
        self.houseNode = None
        self.name = ''
        self.namePlate = None
        self.nameText = None
        self.nametag = None
        self.floorMat = None
        self.matText = None
        self.randomGenerator = None
        self.housePosInd = 0

    
    def disable(self):
        pass

    
    def delete(self):
        self.notify.debug('delete')
        self.unload()
        del self.door_origin
        self.clearNametag()
        if self.namePlate:
            self.namePlate.removeNode()
            del self.namePlate
            self.namePlate = None
        
        if self.floorMat:
            self.floorMat.removeNode()
            del self.floorMat
            self.floorMat = None
        
        del self.randomGenerator
        DistributedObject.DistributedObject.delete(self)

    
    def clearNametag(self):
        if self.nametag != None:
            self.nametag.unmanage(toonbase.marginManager)
            self.nametag.setAvatar(NodePath())
            self.nametag = None
        

    
    def load(self):
        self.notify.debug('load')
        chars = [
            'a',
            'b',
            'c',
            'd',
            'e',
            'f']
        myChar = chars[self.housePosInd]
        model = [
            'houseA.bam',
            'houseB.bam']
        mhouse = model[0]
        posHpr = HouseGlobals.houseDrops[self.housePosInd]
        self.house = loader.loadModel('phase_5.5/models/estate/' + mhouse)
        self._DistributedHouse__setHouseColor()
        houseNode = self.cr.playGame.estateLoader.geom.attachNewNode(myChar + '__esHouse')
        houseNode.setPosHpr(*posHpr)
        self.house.reparentTo(houseNode)
        houseNode.show()
        self.houseNode = houseNode
        self._DistributedHouse__setupDoor()

    
    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)
        messenger.send('setBuilding-' + str(self.doId))

    
    def _DistributedHouse__setupDoor(self):
        self.notify.debug('setupDoor')
        self.dnaStore = self.cr.playGame.dnaStore
        doorModelName = 'door_double_round_ul'
        if doorModelName[-1:] == 'r':
            doorModelName = doorModelName[:-1] + 'l'
        else:
            doorModelName = doorModelName[:-1] + 'r'
        door = self.dnaStore.findNode(doorModelName)
        door_origin = self.house.find('**/door_origin')
        door_origin.setHpr(90, 0, 0)
        door_origin.setScale(0.59999999999999998, 0.59999999999999998, 0.80000000000000004)
        door_origin.setPos(door_origin, -0.025000000000000001, 0, 0.10000000000000001)
        doorNP = door.copyTo(door_origin)
        doorNP.ls()
        self.door_origin = door_origin
        self.randomGenerator = random.Random()
        self.randomGenerator.seed(self.doId)
        houseColor = HouseGlobals.stairWood
        color = Vec4(houseColor[0], houseColor[1], houseColor[2], 1)
        DNADoor.DNADoor.setupDoor(doorNP, door_origin, door_origin, self.dnaStore, str(self.doId), color)
        self._DistributedHouse__setupNamePlate()
        self._DistributedHouse__setupFloorMat()
        self._DistributedHouse__setupNametag()

    
    def _DistributedHouse__setupNamePlate(self):
        self.notify.debug('__setupNamePlate')
        if self.namePlate:
            self.namePlate.removeNode()
            del self.namePlate
            self.namePlate = None
        
        nameText = TextNode('nameText')
        r = self.randomGenerator.random()
        g = self.randomGenerator.random()
        b = self.randomGenerator.random()
        nameText.setTextColor(r, g, b, 1)
        nameText.setAlign(nameText.ACenter)
        nameText.setFont(ToontownGlobals.getSignFont())
        xScale = 1.0
        numLines = 0
        if self.name == '':
            houseName = ''
        else:
            (prettyName, numLines, xScale) = self._DistributedHouse__getPrettyName(16)
            houseName = Localizer.AvatarsHouse % Localizer.GetPossesive(prettyName)
        nameText.setText(houseName)
        self.nameText = nameText
        sign_origin = self.house.find('**/sign_origin')
        pos = sign_origin.getPos()
        sign_origin.setPosHpr(pos[0], pos[1], pos[2] + 0.14999999999999999 * numLines, 90, 0, 0)
        self.namePlate = sign_origin.attachNewNode(self.nameText)
        self.namePlate.setPos(0, -0.050000000000000003, 0)
        self.namePlate.setScale(xScale)

    
    def _DistributedHouse__setupFloorMat(self):
        if self.floorMat:
            self.floorMat.removeNode()
            del self.floorMat
            self.floorMat = None
        
        mat = self.house.find('**/mat')
        mat.setColor(0.40000000000000002, 0.35699999999999998, 0.25900000000000001, 1.0)
        color = HouseGlobals.houseColors[self.housePosInd]
        matText = TextNode('matText')
        matText.setTextColor(color[0], color[1], color[2], 1)
        matText.setAlign(matText.ACenter)
        matText.setFont(ToontownGlobals.getSignFont())
        xScale = 1.0
        numLines = 0
        if self.name == '':
            houseName = ''
        else:
            (prettyName, numLines, xScale) = self._DistributedHouse__getPrettyName(9)
            houseName = Localizer.AvatarsHouse % Localizer.GetPossesive(prettyName)
        matText.setText(houseName)
        self.matText = matText
        mat_origin = self.house.find('**/mat_origin')
        pos = mat_origin.getPos()
        mat_origin.setPosHpr(pos[0] - 0.14999999999999999 * numLines, pos[1], pos[2], 90, -90, 0)
        self.floorMat = mat_origin.attachNewNode(self.matText)
        self.floorMat.setPos(0, -0.025000000000000001, 0)
        self.floorMat.setScale(0.5 * xScale)

    
    def _DistributedHouse__setupNametag(self):
        if self.nametag:
            self.clearNametag()
        
        if self.name == '':
            houseName = ''
        else:
            houseName = Localizer.AvatarsHouse % Localizer.GetPossesive(self.name)
        self.nametag = NametagGroup()
        self.nametag.setFont(ToontownGlobals.getSignFont())
        self.nametag.setContents(Nametag.CName)
        self.nametag.setColorCode(NametagGroup.CCHouseBuilding)
        self.nametag.setActive(0)
        self.nametag.setAvatar(self.house)
        self.nametag.setObjectCode(self.doId)
        self.nametag.setName(houseName)
        self.nametag.manage(toonbase.marginManager)

    
    def _DistributedHouse__getPrettyName(self, maxLen):
        prettyName = ''
        numLines = 0
        lastLine = prettyName
        name = split(self.name)
        longestLine = len(prettyName)
        for i in range(len(name)):
            temp = lastLine + ' ' + name[i]
            if len(temp) < maxLen:
                prettyName = prettyName + ' ' + name[i]
                lastLine = temp
            else:
                prettyName = prettyName + '\n' + name[i]
                numLines = numLines + 1
                lastLine = name[i]
            if len(lastLine) > longestLine:
                longestLine = len(lastLine)
            
            scale = 1.0
            if longestLine > maxLen:
                scale = float(maxLen) / longestLine
            
        
        return (prettyName, numLines, scale)

    
    def unload(self):
        self.notify.debug('unload')
        self.ignoreAll()
        if self.houseNode:
            self.houseNode.removeNode()
            del self.houseNode
            del self.house
        

    
    def setHouseReady(self):
        self.notify.debug('setHouseReady')
        
        try:
            pass
        except:
            self.House_initialized = 1
            self.load()


    
    def setHousePos(self, index):
        self.notify.debug('setHousePos')
        self.housePosInd = index
        self._DistributedHouse__setHouseColor()

    
    def setHouseType(self, index):
        self.notify.debug('setHouseType')
        self.houseType = index

    
    def setFavoriteNum(self, index):
        self.notify.debug('setFavoriteNum')
        self.favoriteNum = index

    
    def _DistributedHouse__setHouseColor(self):
        if self.house:
            bwall = self.house.find('**/*back')
            rwall = self.house.find('**/*right')
            fwall = self.house.find('**/*front')
            lwall = self.house.find('**/*left')
            kd = 0.80000000000000004
            color = HouseGlobals.houseColors[self.colorIndex]
            dark = (kd * color[0], kd * color[1], kd * color[2])
            if not bwall.isEmpty():
                bwall.setColor(color[0], color[1], color[2], 1)
            
            if not fwall.isEmpty():
                fwall.setColor(color[0], color[1], color[2], 1)
            
            if not rwall.isEmpty():
                rwall.setColor(dark[0], dark[1], dark[2], 1)
            
            if not lwall.isEmpty():
                lwall.setColor(dark[0], dark[1], dark[2], 1)
            
            aColor = HouseGlobals.atticWood
            attic = self.house.find('**/attic')
            if not attic.isEmpty():
                attic.setColor(aColor[0], aColor[1], aColor[2], 1)
            
            chimney = self.house.find('**/chim*')
            if not chimney.isEmpty():
                color = HouseGlobals.houseColors2[self.colorIndex]
                chimney.setColor(color[0], color[1], color[2], 1)
            
        

    
    def setAvId(self, id):
        self.avId = id

    
    def setAvatarId(self, avId):
        self.notify.debug('setAvatarId = %s' % avId)
        self.ownerId = avId

    
    def getAvatarId(self):
        self.notify.debug('getAvatarId')
        return self.ownerId

    
    def setName(self, name):
        self.name = name
        if self.nameText and self.nameText.getText() != self.name:
            if self.name == '':
                self.nameText.setText('')
            else:
                self.nameText.setText(self.name + "'s\n House")
        

    
    def getName(self):
        return self.name

    
    def b_setColor(self, colorInd):
        self.setColor(colorInd)
        self.d_setColor(colorInd)

    
    def d_setColor(self, colorInd):
        self.sendUpdate('setColor', [
            colorInd])

    
    def setColor(self, colorInd):
        self.colorIndex = colorInd
        if self.house:
            self._DistributedHouse__setHouseColor()
        

    
    def getColor(self):
        return self.colorIndex


