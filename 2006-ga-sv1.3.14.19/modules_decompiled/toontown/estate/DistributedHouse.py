# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToonBaseGlobal import *
from direct.gui.DirectGui import *
from direct.distributed.ClockDelta import *
from toontown.minigame.OrthoWalk import *
from string import *
from toontown.toonbase import ToontownGlobals
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
from direct.fsm import State
from toontown.toon import Toon
from direct.showbase import RandomNumGen
from toontown.toonbase import TTLocalizer
import random
from direct.distributed import DelayDelete
from direct.showbase import PythonUtil
from toontown.hood import Place
import HouseGlobals
from toontown.building import ToonInteriorColors

class DistributedHouse(DistributedObject.DistributedObject):
    notify = directNotify.newCategory('DistributedHouse')
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.houseType = None
        self.avId = -1
        self.ownerId = 0
        self.colorIndex = 0
        self.house = None
        self.name = ''
        self.namePlate = None
        self.nameText = None
        self.nametag = None
        self.floorMat = None
        self.matText = None
        self.randomGenerator = None
        self.housePosInd = 0
        self.house_loaded = 0

    
    def disable(self):
        pass

    
    def delete(self):
        self.notify.debug('delete')
        self.unload()
        self.clearNametag()
        if self.namePlate:
            self.namePlate.removeNode()
            del self.namePlate
            self.namePlate = None
        
        if self.floorMat:
            self.floorMat.removeNode()
            del self.floorMat
            self.floorMat = None
        
        if self.house:
            self.house.removeNode()
            del self.house
        
        self.house_loaded = 0
        del self.randomGenerator
        DistributedObject.DistributedObject.delete(self)

    
    def clearNametag(self):
        if self.nametag != None:
            self.nametag.unmanage(base.marginManager)
            self.nametag.setAvatar(NodePath())
            self.nametag = None
        

    
    def load(self):
        self.notify.debug('load')
        if not (self.house_loaded):
            houseModel = self.cr.playGame.hood.loader.houseModels[HouseGlobals.HOUSE_DEFAULT]
            self.house = houseModel.copyTo(self.cr.playGame.hood.loader.houseNode[self.housePosInd])
            self.house_loaded = 1
            self.cr.playGame.hood.loader.houseId2house[self.doId] = self.house
            self._DistributedHouse__setHouseColor()
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
        self.door_origin = door_origin
        self.randomGenerator = random.Random()
        self.randomGenerator.seed(self.doId)
        houseColor = HouseGlobals.stairWood
        color = Vec4(houseColor[0], houseColor[1], houseColor[2], 1)
        DNADoor.setupDoor(doorNP, door_origin, door_origin, self.dnaStore, str(self.doId), color)
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
        nameText.setFont(ToontownGlobals.getBuildingNametagFont())
        nameText.setShadowColor(0, 0, 0, 1)
        nameText.setBin('fixed')
        if TTLocalizer.BuildingNametagShadow:
            nameText.setShadow(*TTLocalizer.BuildingNametagShadow)
        
        nameText.setWordwrap(16.0)
        xScale = 1.0
        numLines = 0
        if self.name == '':
            houseName = ''
        else:
            houseName = TTLocalizer.AvatarsHouse % TTLocalizer.GetPossesive(self.name)
        nameText.setText(houseName)
        self.nameText = nameText
        textHeight = nameText.getHeight() - 2
        textWidth = nameText.getWidth()
        xScale = 1.0
        if textWidth > 16:
            xScale = 16.0 / textWidth
        
        sign_origin = self.house.find('**/sign_origin')
        pos = sign_origin.getPos()
        sign_origin.setPosHpr(pos[0], pos[1], pos[2] + 0.14999999999999999 * textHeight, 90, 0, 0)
        self.namePlate = sign_origin.attachNewNode(self.nameText)
        self.namePlate.setDepthWrite(0)
        self.namePlate.setPos(0, -0.050000000000000003, 0)
        self.namePlate.setScale(xScale)
        return nameText

    
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
        matText.setFont(ToontownGlobals.getBuildingNametagFont())
        matText.setShadowColor(0, 0, 0, 1)
        matText.setBin('fixed')
        if TTLocalizer.BuildingNametagShadow:
            matText.setShadow(*TTLocalizer.BuildingNametagShadow)
        
        matText.setWordwrap(10.0)
        xScale = 1.0
        numLines = 0
        if self.name == '':
            houseName = ''
        else:
            houseName = TTLocalizer.AvatarsHouse % TTLocalizer.GetPossesive(self.name)
        matText.setText(houseName)
        self.matText = matText
        textHeight = matText.getHeight() - 2
        textWidth = matText.getWidth()
        xScale = 1.0
        if textWidth > 8:
            xScale = 8.0 / textWidth
        
        mat_origin = self.house.find('**/mat_origin')
        pos = mat_origin.getPos()
        mat_origin.setPosHpr(pos[0] - 0.14999999999999999 * textHeight, pos[1], pos[2], 90, -90, 0)
        self.floorMat = mat_origin.attachNewNode(self.matText)
        self.floorMat.setDepthWrite(0)
        self.floorMat.setPos(0, -0.025000000000000001, 0)
        self.floorMat.setScale(0.45000000000000001 * xScale)

    
    def _DistributedHouse__setupNametag(self):
        if self.nametag:
            self.clearNametag()
        
        if self.name == '':
            houseName = ''
        else:
            houseName = TTLocalizer.AvatarsHouse % TTLocalizer.GetPossesive(self.name)
        self.nametag = NametagGroup()
        self.nametag.setFont(ToontownGlobals.getBuildingNametagFont())
        if TTLocalizer.BuildingNametagShadow:
            self.nametag.setShadow(*TTLocalizer.BuildingNametagShadow)
        
        self.nametag.setContents(Nametag.CName)
        self.nametag.setColorCode(NametagGroup.CCHouseBuilding)
        self.nametag.setActive(0)
        self.nametag.setAvatar(self.house)
        self.nametag.setObjectCode(self.doId)
        self.nametag.setName(houseName)
        self.nametag.manage(base.marginManager)

    
    def unload(self):
        self.notify.debug('unload')
        self.ignoreAll()

    
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


