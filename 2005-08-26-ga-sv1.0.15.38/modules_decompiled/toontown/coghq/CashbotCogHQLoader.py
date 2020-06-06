# File: C (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
import CogHQLoader
import MintInterior
from toontown.toonbase import ToontownGlobals
from pandac.PandaModules import *
from direct.gui import DirectGui
from toontown.toonbase import TTLocalizer
from toontown.toon import Toon
from direct.fsm import State
import CashbotHQExterior
import CashbotHQBossBattle
aspectSF = 0.72270000000000001

class CashbotCogHQLoader(CogHQLoader.CogHQLoader):
    notify = DirectNotifyGlobal.directNotify.newCategory('CashbotCogHQLoader')
    notify.setDebug(True)
    
    def __init__(self, hood, parentFSMState, doneEvent):
        CogHQLoader.CogHQLoader.__init__(self, hood, parentFSMState, doneEvent)
        self.fsm.addState(State.State('mintInterior', self.enterMintInterior, self.exitMintInterior, [
            'quietZone',
            'cogHQExterior']))
        for stateName in [
            'start',
            'cogHQExterior',
            'quietZone']:
            state = self.fsm.getStateNamed(stateName)
            state.addTransition('mintInterior')
        
        self.musicFile = 'phase_9/audio/bgm/encntr_suit_HQ_nbrhood.mid'
        self.cogHQExteriorModelPath = 'phase_10/models/cogHQ/CashBotShippingStation'
        self.cogHQLobbyModelPath = 'phase_10/models/cogHQ/VaultLobby'
        self.geom = None

    
    def load(self, zoneId):
        CogHQLoader.CogHQLoader.load(self, zoneId)
        Toon.loadCashbotHQAnims()

    
    def unloadPlaceGeom(self):
        if self.geom:
            self.geom.removeNode()
            self.geom = None
        
        CogHQLoader.CogHQLoader.unloadPlaceGeom(self)

    
    def loadPlaceGeom(self, zoneId):
        self.notify.info('loadPlaceGeom: %s' % zoneId)
        zoneId = zoneId - zoneId % 100
        if zoneId == ToontownGlobals.CashbotHQ:
            self.geom = loader.loadModel(self.cogHQExteriorModelPath)
            ddLinkTunnel = self.geom.find('**/LinkTunnel1')
            ddLinkTunnel.setName('linktunnel_dl_9252_DNARoot')
            locator = self.geom.find('**/sign_origin')
            backgroundGeom = self.geom.find('**/EntranceFrameFront')
            backgroundGeom.node().setEffect(DecalEffect.make())
            signText = DirectGui.OnscreenText(text = TTLocalizer.DonaldsDreamland[-1], font = ToontownGlobals.getSuitFont(), scale = 3, fg = (0.87, 0.87, 0.87, 1), parent = backgroundGeom)
            signText.setPosHpr(locator, 0, 0, 0, 0, 0, 0)
            signText.setDepthWrite(0)
        elif zoneId == ToontownGlobals.CashbotLobby:
            self.geom = loader.loadModel(self.cogHQLobbyModelPath)
        else:
            self.notify.warning('loadPlaceGeom: unclassified zone %s' % zoneId)
        CogHQLoader.CogHQLoader.loadPlaceGeom(self, zoneId)

    
    def unload(self):
        CogHQLoader.CogHQLoader.unload(self)
        Toon.unloadCashbotHQAnims()

    
    def enterMintInterior(self, requestStatus):
        self.placeClass = MintInterior.MintInterior
        self.mintId = requestStatus['mintId']
        self.enterPlace(requestStatus)

    
    def exitMintInterior(self):
        self.exitPlace()
        self.placeClass = None
        del self.mintId

    
    def getExteriorPlaceClass(self):
        return CashbotHQExterior.CashbotHQExterior

    
    def getBossPlaceClass(self):
        return CashbotHQBossBattle.CashbotHQBossBattle


