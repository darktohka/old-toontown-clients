# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\cogdominium\DistCogdoFlyingGame.py
from direct.distributed.ClockDelta import globalClockDelta
from toontown.toonbase import TTLocalizer
from CogdoFlyingGame import CogdoFlyingGame
from DistCogdoGame import DistCogdoGame
import CogdoFlyingGameGlobals, CogdoFlyingGameGlobals as Globals

class DistCogdoFlyingGame(DistCogdoGame):
    __module__ = __name__
    notify = directNotify.newCategory('DistCogdoFlyingGame')

    def __init__(self, cr):
        DistCogdoGame.__init__(self, cr)
        if __debug__ and base.config.GetBool('schellgames-dev', True):
            self.accept('onCodeReload', self.__sgOnCodeReload)
        self.game = CogdoFlyingGame(self)

    def delete(self):
        del self.game
        DistCogdoGame.delete(self)

    def getTitle(self):
        return TTLocalizer.CogdoFlyingGameTitle

    def getInstructions(self):
        return TTLocalizer.CogdoFlyingGameInstructions

    def placeEntranceElev(self, elev):
        self.game.placeEntranceElevator(elev)

    def d_sendRequestAction(self, action, data):
        self.sendUpdate('requestAction', [action, data])

    def doAction(self, action, data):
        messenger.send(self.getRemoteActionEventName(), [action, data])

    def toonSetAsEagleTarget(self, toonId, eagleId, networkTime):
        self.notify.debugCall()
        elapsedTime = globalClockDelta.localElapsedTime(networkTime)
        self.game.toonSetAsEagleTarget(toonId, eagleId, elapsedTime)

    def toonClearAsEagleTarget(self, toonId, eagleId, networkTime):
        self.notify.debugCall()
        elapsedTime = globalClockDelta.localElapsedTime(networkTime)
        self.game.toonClearAsEagleTarget(toonId, eagleId, elapsedTime)

    def eagleExitCooldown(self, eagleId, networkTime):
        self.notify.debugCall()
        elapsedTime = globalClockDelta.localElapsedTime(networkTime)
        self.game.eagleExitCooldown(eagleId, elapsedTime)

    def debuffPowerup(self, toonId, pickupType, networkTime):
        elapsedTime = globalClockDelta.localElapsedTime(networkTime)
        self.game.debuffPowerup(toonId, pickupType, elapsedTime)

    def toonDied(self, toonId, networkTime):
        if toonId != base.localAvatar.doId:
            elapsedTime = globalClockDelta.localElapsedTime(networkTime)
            self.game.toonDied(toonId, elapsedTime)

    def b_toonDied(self, toonId):
        self.game.toonDied(toonId, 0)
        self.d_sendRequestAction(Globals.AI.GameActions.Died, 0)

    def toonSpawn(self, toonId, networkTime):
        if toonId != base.localAvatar.doId:
            elapsedTime = globalClockDelta.localElapsedTime(networkTime)
            self.game.toonSpawn(toonId, elapsedTime)

    def b_toonSpawn(self, toonId):
        self.game.toonSpawn(toonId, 0)
        self.d_sendRequestAction(Globals.AI.GameActions.Spawn, 0)

    def pickUp(self, toonId, pickupNum, networkTime):
        if not self.getToon(base.localAvatar.doId):
            return
        elapsedTime = globalClockDelta.localElapsedTime(networkTime)
        self.game.pickUp(toonId, pickupNum, elapsedTime)

    def d_sendRequestPickup(self, pickupNum, pickupType):
        self.sendUpdate('requestPickUp', [pickupNum, pickupType])

    def toonSetBlades(self, toonId, fuelState):
        if toonId != base.localAvatar.doId:
            self.game.toonSetBlades(toonId, fuelState)

    def b_toonSetBlades(self, toonId, fuelState):
        self.game.toonSetBlades(toonId, fuelState)
        self.d_sendRequestAction(Globals.AI.GameActions.SetBlades, fuelState)

    def toonBladeLost(self, toonId):
        if toonId != base.localAvatar.doId:
            self.game.toonBladeLost(toonId)

    def b_toonBladeLost(self, toonId):
        self.game.toonBladeLost(toonId)
        self.d_sendRequestAction(Globals.AI.GameActions.BladeLost, 0)

    def getRemoteActionEventName(self):
        return self._remoteActionEventName

    def setToonSad(self, toonId):
        self.game.setToonSad(toonId)
        DistCogdoGame.setToonSad(self, toonId)

    def setToonDisconnect(self, toonId):
        self.game.setToonDisconnect(toonId)
        DistCogdoGame.setToonDisconnect(self, toonId)

    def __handleUnexpectedExit(self, toonId):
        self.notify.warning('%s: unexpected exit for %s' % (self.doId, toonId))
        self.game.removePlayer(toonId)

    def enterLoaded(self):
        DistCogdoGame.enterLoaded(self)
        self._remoteActionEventName = self.uniqueName('doAction')
        self.game.load()
        self.game.initPlayers()

    def exitLoaded(self):
        self.ignoreAll()
        self.game.unload()
        DistCogdoGame.exitLoaded(self)

    def enterVisible(self):
        DistCogdoGame.enterVisible(self)
        self.game.onstage()

    def exitVisible(self):
        DistCogdoGame.exitVisible(self)

    def enterIntro(self):
        DistCogdoGame.enterIntro(self, Globals.Gameplay.IntroDurationSeconds)
        self.game.startIntro()

    def exitIntro(self):
        DistCogdoGame.exitIntro(self)
        self.game.endIntro()
        self.stashEntranceElevator()

    def enterGame(self):
        DistCogdoGame.enterGame(self)
        self.game.start()

    def exitGame(self):
        self.game.exit()
        DistCogdoGame.exitGame(self)

    def enterFinish(self):
        DistCogdoGame.enterFinish(self)
        self.game.startFinish()

    def exitFinish(self):
        self.game.endFinish()
        self.game.offstage()
        DistCogdoGame.exitFinish(self)