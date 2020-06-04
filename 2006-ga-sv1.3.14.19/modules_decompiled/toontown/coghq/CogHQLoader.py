# File: C (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
from direct.fsm import ClassicFSM
from direct.fsm import State
import CogHQExterior
import CogHQLobby
import CogHQBossBattle
import FactoryExterior
import FactoryInterior
from toontown.hood import QuietZoneState
from toontown.town import TownBattle
from toontown.toon import Toon
from toontown.suit import Suit
from pandac.PandaModules import *

class CogHQLoader(StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('CogHQLoader')
    
    def __init__(self, hood, parentFSMState, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.hood = hood
        self.parentFSMState = parentFSMState
        self.placeDoneEvent = 'cogHQLoaderPlaceDone'
        self.townBattleDoneEvent = 'town-battle-done'
        self.fsm = ClassicFSM.ClassicFSM('CogHQLoader', [
            State.State('start', None, None, [
                'quietZone',
                'factoryExterior',
                'cogHQExterior',
                'cogHQBossBattle']),
            State.State('cogHQExterior', self.enterCogHQExterior, self.exitCogHQExterior, [
                'quietZone',
                'factoryExterior',
                'cogHQLobby']),
            State.State('cogHQLobby', self.enterCogHQLobby, self.exitCogHQLobby, [
                'quietZone',
                'cogHQExterior',
                'cogHQBossBattle']),
            State.State('cogHQBossBattle', self.enterCogHQBossBattle, self.exitCogHQBossBattle, [
                'quietZone']),
            State.State('factoryExterior', self.enterFactoryExterior, self.exitFactoryExterior, [
                'quietZone',
                'factoryInterior',
                'cogHQExterior']),
            State.State('factoryInterior', self.enterFactoryInterior, self.exitFactoryInterior, [
                'quietZone',
                'factoryExterior']),
            State.State('quietZone', self.enterQuietZone, self.exitQuietZone, [
                'cogHQExterior',
                'cogHQLobby',
                'cogHQBossBattle',
                'factoryExterior',
                'factoryInterior']),
            State.State('final', None, None, [
                'start'])], 'start', 'final')

    
    def load(self, zoneId):
        self.parentFSMState.addChild(self.fsm)
        self.music = base.loadMusic(self.musicFile)
        self.battleMusic = base.loadMusic('phase_9/audio/bgm/encntr_suit_winning.mid')
        self.townBattle = TownBattle.TownBattle(self.townBattleDoneEvent)
        self.townBattle.load()
        Suit.loadSuits(3)
        Toon.loadCogHQAnims()
        self.loadPlaceGeom(zoneId)

    
    def loadPlaceGeom(self, zoneId):
        return None

    
    def unloadPlaceGeom(self):
        return None

    
    def unload(self):
        self.unloadPlaceGeom()
        self.parentFSMState.removeChild(self.fsm)
        del self.parentFSMState
        del self.fsm
        self.townBattle.unload()
        self.townBattle.cleanup()
        del self.townBattle
        del self.battleMusic
        Suit.unloadSuits(3)
        Suit.unloadSkelDialog()
        Toon.unloadCogHQAnims()
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()

    
    def enter(self, requestStatus):
        self.fsm.enterInitialState()
        self.fsm.request(requestStatus['where'], [
            requestStatus])

    
    def exit(self):
        self.ignoreAll()

    
    def enterQuietZone(self, requestStatus):
        self.quietZoneDoneEvent = 'quietZoneDone'
        self.acceptOnce(self.quietZoneDoneEvent, self.handleQuietZoneDone)
        self.quietZoneStateData = QuietZoneState.QuietZoneState(self.quietZoneDoneEvent)
        self.quietZoneStateData.load()
        self.quietZoneStateData.enter(requestStatus)

    
    def exitQuietZone(self):
        self.ignore(self.quietZoneDoneEvent)
        del self.quietZoneDoneEvent
        self.quietZoneStateData.exit()
        self.quietZoneStateData.unload()
        self.quietZoneStateData = None

    
    def handleQuietZoneDone(self):
        status = base.cr.handlerArgs
        self.fsm.request(status['where'], [
            status])

    
    def enterPlace(self, requestStatus):
        self.acceptOnce(self.placeDoneEvent, self.placeDone)
        self.place = self.placeClass(self, self.fsm, self.placeDoneEvent)
        base.cr.playGame.setPlace(self.place)
        self.place.load()
        self.place.enter(requestStatus)

    
    def exitPlace(self):
        self.ignore(self.placeDoneEvent)
        self.place.exit()
        self.place.unload()
        self.place = None
        base.cr.playGame.setPlace(self.place)

    
    def placeDone(self):
        self.requestStatus = self.place.doneStatus
        status = self.place.doneStatus
        if status['loader'] == 'cogHQLoader' and status.get('shardId') == None:
            self.unloadPlaceGeom()
            zoneId = status['zoneId']
            self.loadPlaceGeom(zoneId)
            self.fsm.request('quietZone', [
                status])
        else:
            self.doneStatus = status
            messenger.send(self.doneEvent)

    
    def enterCogHQExterior(self, requestStatus):
        self.placeClass = CogHQExterior.CogHQExterior
        self.enterPlace(requestStatus)
        self.hood.spawnTitleText(requestStatus['zoneId'])

    
    def exitCogHQExterior(self):
        taskMgr.remove('titleText')
        self.hood.hideTitleText()
        self.exitPlace()
        self.placeClass = None

    
    def enterCogHQLobby(self, requestStatus):
        self.placeClass = CogHQLobby.CogHQLobby
        self.enterPlace(requestStatus)
        self.hood.spawnTitleText(requestStatus['zoneId'])

    
    def exitCogHQLobby(self):
        taskMgr.remove('titleText')
        self.hood.hideTitleText()
        self.exitPlace()
        self.placeClass = None

    
    def enterCogHQBossBattle(self, requestStatus):
        self.placeClass = CogHQBossBattle.CogHQBossBattle
        self.enterPlace(requestStatus)

    
    def exitCogHQBossBattle(self):
        self.exitPlace()
        self.placeClass = None

    
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


