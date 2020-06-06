# File: S (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
import CogHQLoader
from toontown.toonbase import ToontownGlobals
from pandac.PandaModules import *
from direct.gui import DirectGui
from toontown.toonbase import TTLocalizer
from toontown.toon import Toon
from direct.fsm import State
import FactoryExterior
import FactoryInterior
import SellbotHQExterior
import SellbotHQBossBattle
aspectSF = 0.72270000000000001

class SellbotCogHQLoader(CogHQLoader.CogHQLoader):
    notify = DirectNotifyGlobal.directNotify.newCategory('SellbotCogHQLoader')
    notify.setDebug(True)
    
    def __init__(self, hood, parentFSMState, doneEvent):
        CogHQLoader.CogHQLoader.__init__(self, hood, parentFSMState, doneEvent)
        self.fsm.addState(State.State('factoryExterior', self.enterFactoryExterior, self.exitFactoryExterior, [
            'quietZone',
            'factoryInterior',
            'cogHQExterior']))
        for stateName in [
            'start',
            'cogHQExterior',
            'quietZone']:
            state = self.fsm.getStateNamed(stateName)
            state.addTransition('factoryExterior')
        
        self.fsm.addState(State.State('factoryInterior', self.enterFactoryInterior, self.exitFactoryInterior, [
            'quietZone',
            'factoryExterior']))
        for stateName in [
            'quietZone']:
            state = self.fsm.getStateNamed(stateName)
            state.addTransition('factoryInterior')
        
        self.musicFile = 'phase_9/audio/bgm/encntr_suit_HQ_nbrhood.mid'
        self.cogHQExteriorModelPath = 'phase_9/models/cogHQ/SellbotHQExterior'
        self.cogHQLobbyModelPath = 'phase_9/models/cogHQ/SellbotHQLobby'
        self.factoryExteriorModelPath = 'phase_9/models/cogHQ/SellbotFactoryExterior'
        self.geom = None

    
    def load(self, zoneId):
        CogHQLoader.CogHQLoader.load(self, zoneId)
        Toon.loadSellbotHQAnims()

    
    def unloadPlaceGeom(self):
        if self.geom:
            self.geom.removeNode()
            self.geom = None
        
        CogHQLoader.CogHQLoader.unloadPlaceGeom(self)

    
    def loadPlaceGeom(self, zoneId):
        self.notify.info('loadPlaceGeom: %s' % zoneId)
        zoneId = zoneId - zoneId % 100
        if zoneId == ToontownGlobals.SellbotHQ:
            self.geom = loader.loadModel(self.cogHQExteriorModelPath)
            dgLinkTunnel = self.geom.find('**/Tunnel1')
            dgLinkTunnel.setName('linktunnel_dg_5316_DNARoot')
            factoryLinkTunnel = self.geom.find('**/Tunnel2')
            factoryLinkTunnel.setName('linktunnel_sellhq_11200_DNARoot')
            cogSignModel = loader.loadModel('phase_4/models/props/sign_sellBotHeadHQ')
            cogSign = cogSignModel.find('**/sign_sellBotHeadHQ')
            cogSignSF = 23
            dgSign = cogSign.copyTo(dgLinkTunnel)
            dgSign.setPosHprScale(0.0, -291.5, 29, 180.0, 0.0, 0.0, cogSignSF, cogSignSF, cogSignSF * aspectSF)
            dgSign.node().setEffect(DecalEffect.make())
            dgText = DirectGui.OnscreenText(text = TTLocalizer.DaisyGardens[-1], font = ToontownGlobals.getSuitFont(), pos = (0, -0.29999999999999999), scale = 0.10000000000000001, parent = dgSign)
            dgText.setDepthWrite(0)
            factorySign = cogSign.copyTo(factoryLinkTunnel)
            factorySign.setPosHprScale(148.625, -155, 27, -90.0, 0.0, 0.0, cogSignSF, cogSignSF, cogSignSF * aspectSF)
            factorySign.node().setEffect(DecalEffect.make())
            factoryTypeText = DirectGui.OnscreenText(text = TTLocalizer.Sellbot, font = ToontownGlobals.getSuitFont(), pos = (0, -0.25), scale = 0.074999999999999997, parent = factorySign)
            factoryTypeText.setDepthWrite(0)
            factoryText = DirectGui.OnscreenText(text = TTLocalizer.Factory, font = ToontownGlobals.getSuitFont(), pos = (0, -0.34000000000000002), scale = 0.12, parent = factorySign)
            factoryText.setDepthWrite(0)
            doors = self.geom.find('**/doors')
            door0 = doors.find('**/door_0')
            door1 = doors.find('**/door_1')
            door2 = doors.find('**/door_2')
            door3 = doors.find('**/door_3')
            index = 0
            for door in [
                door0,
                door1,
                door2,
                door3]:
                doorFrame = door.find('**/doorDoubleFlat/+GeomNode')
                door.find('**/doorFrameHoleLeft').wrtReparentTo(doorFrame)
                door.find('**/doorFrameHoleRight').wrtReparentTo(doorFrame)
                doorFrame.node().setEffect(DecalEffect.make())
                index += 1
            
        elif zoneId == ToontownGlobals.SellbotFactoryExt:
            self.geom = loader.loadModel(self.factoryExteriorModelPath)
            factoryLinkTunnel = self.geom.find('**/tunnel_group2')
            factoryLinkTunnel.setName('linktunnel_sellhq_11000_DNARoot')
            factoryLinkTunnel.find('**/tunnel_sphere').setName('tunnel_trigger')
            cogSignModel = loader.loadModel('phase_4/models/props/sign_sellBotHeadHQ')
            cogSign = cogSignModel.find('**/sign_sellBotHeadHQ')
            cogSignSF = 23
            elevatorSignSF = 15
            hqSign = cogSign.copyTo(factoryLinkTunnel)
            hqSign.setPosHprScale(0.0, -353, 27.5, -180.0, 0.0, 0.0, cogSignSF, cogSignSF, cogSignSF * aspectSF)
            hqSign.node().setEffect(DecalEffect.make())
            hqTypeText = DirectGui.OnscreenText(text = TTLocalizer.Sellbot, font = ToontownGlobals.getSuitFont(), pos = (0, -0.25), scale = 0.074999999999999997, parent = hqSign)
            hqTypeText.setDepthWrite(0)
            hqText = DirectGui.OnscreenText(text = TTLocalizer.Headquarters, font = ToontownGlobals.getSuitFont(), pos = (0, -0.34000000000000002), scale = 0.10000000000000001, parent = hqSign)
            hqText.setDepthWrite(0)
            frontDoor = self.geom.find('**/doorway1')
            fdSign = cogSign.copyTo(frontDoor)
            fdSign.setPosHprScale(62.740000000000002, -87.989999999999995, 17.260000000000002, 2.7200000000000002, 0.0, 0.0, elevatorSignSF, elevatorSignSF, elevatorSignSF * aspectSF)
            fdSign.node().setEffect(DecalEffect.make())
            fdTypeText = DirectGui.OnscreenText(text = TTLocalizer.Factory, font = ToontownGlobals.getSuitFont(), pos = (0, -0.25), scale = 0.074999999999999997, parent = fdSign)
            fdTypeText.setDepthWrite(0)
            fdText = DirectGui.OnscreenText(text = TTLocalizer.SellbotFrontEntrance, font = ToontownGlobals.getSuitFont(), pos = (0, -0.34000000000000002), scale = 0.10000000000000001, parent = fdSign)
            fdText.setDepthWrite(0)
            sideDoor = self.geom.find('**/doorway2')
            sdSign = cogSign.copyTo(sideDoor)
            sdSign.setPosHprScale(-164.78, 26.280000000000001, 17.25, -89.890000000000001, 0.0, 0.0, elevatorSignSF, elevatorSignSF, elevatorSignSF * aspectSF)
            sdSign.node().setEffect(DecalEffect.make())
            sdTypeText = DirectGui.OnscreenText(text = TTLocalizer.Factory, font = ToontownGlobals.getSuitFont(), pos = (0, -0.25), scale = 0.074999999999999997, parent = sdSign)
            sdTypeText.setDepthWrite(0)
            sdText = DirectGui.OnscreenText(text = TTLocalizer.SellbotSideEntrance, font = ToontownGlobals.getSuitFont(), pos = (0, -0.34000000000000002), scale = 0.10000000000000001, parent = sdSign)
            sdText.setDepthWrite(0)
        elif zoneId == ToontownGlobals.SellbotLobby:
            self.geom = loader.loadModel(self.cogHQLobbyModelPath)
            front = self.geom.find('**/frontWall')
            front.node().setEffect(DecalEffect.make())
            door = self.geom.find('**/door_0')
            parent = door.getParent()
            door.wrtReparentTo(front)
            doorFrame = door.find('**/doorDoubleFlat/+GeomNode')
            door.find('**/doorFrameHoleLeft').wrtReparentTo(doorFrame)
            door.find('**/doorFrameHoleRight').wrtReparentTo(doorFrame)
            doorFrame.node().setEffect(DecalEffect.make())
            door.find('**/leftDoor').wrtReparentTo(parent)
            door.find('**/rightDoor').wrtReparentTo(parent)
        else:
            self.notify.warning('loadPlaceGeom: unclassified zone %s' % zoneId)
        CogHQLoader.CogHQLoader.loadPlaceGeom(self, zoneId)

    
    def unload(self):
        CogHQLoader.CogHQLoader.unload(self)
        Toon.unloadSellbotHQAnims()

    
    def enterFactoryExterior(self, requestStatus):
        self.placeClass = FactoryExterior.FactoryExterior
        self.enterPlace(requestStatus)
        self.hood.spawnTitleText(requestStatus['zoneId'])

    
    def exitFactoryExterior(self):
        taskMgr.remove('titleText')
        self.hood.hideTitleText()
        self.exitPlace()
        self.placeClass = None

    
    def enterFactoryInterior(self, requestStatus):
        self.placeClass = FactoryInterior.FactoryInterior
        self.enterPlace(requestStatus)

    
    def exitFactoryInterior(self):
        self.exitPlace()
        self.placeClass = None

    
    def getExteriorPlaceClass(self):
        return SellbotHQExterior.SellbotHQExterior

    
    def getBossPlaceClass(self):
        return SellbotHQBossBattle.SellbotHQBossBattle


