# File: D (Python 2.2)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
from DirectGui import *
from ClockDelta import *
import ToontownGlobals
import DistributedObject
import DirectNotifyGlobal
import FSM
import State
import AvatarDNA
import MinigameRulesPanel
import Toon
import RandomNumGen
import Localizer
import random
import MinigameGlobals
import DelayDelete
import PythonUtil
import Emote

class DistributedMinigame(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedMinigame')
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.waitingStartLabel = DirectLabel(text = Localizer.MinigameWaitingForOtherPlayers, text_fg = VBase4(1, 1, 1, 1), relief = None, pos = (-0.59999999999999998, 0, -0.75), scale = 0.074999999999999997)
        self.waitingStartLabel.hide()
        self.avIdList = []
        self.remoteAvIdList = []
        self.localAvId = toonbase.localToon.doId
        self.frameworkFSM = FSM.FSM('DistributedMinigame', [
            State.State('frameworkInit', self.enterFrameworkInit, self.exitFrameworkInit, [
                'frameworkRules',
                'frameworkCleanup',
                'frameworkAvatarExited']),
            State.State('frameworkRules', self.enterFrameworkRules, self.exitFrameworkRules, [
                'frameworkWaitServerStart',
                'frameworkCleanup',
                'frameworkAvatarExited']),
            State.State('frameworkWaitServerStart', self.enterFrameworkWaitServerStart, self.exitFrameworkWaitServerStart, [
                'frameworkGame',
                'frameworkCleanup',
                'frameworkAvatarExited']),
            State.State('frameworkGame', self.enterFrameworkGame, self.exitFrameworkGame, [
                'frameworkWaitServerFinish',
                'frameworkCleanup',
                'frameworkAvatarExited']),
            State.State('frameworkWaitServerFinish', self.enterFrameworkWaitServerFinish, self.exitFrameworkWaitServerFinish, [
                'frameworkCleanup']),
            State.State('frameworkAvatarExited', self.enterFrameworkAvatarExited, self.exitFrameworkAvatarExited, [
                'frameworkCleanup']),
            State.State('frameworkCleanup', self.enterFrameworkCleanup, self.exitFrameworkCleanup, [])], 'frameworkInit', 'frameworkCleanup')
        hoodMinigameState = self.cr.playGame.hood.fsm.getStateNamed('minigame')
        hoodMinigameState.addChild(self.frameworkFSM)
        self.rulesDoneEvent = 'rulesDone'
        self.acceptOnce('minigameAbort', self.d_requestExit)
        toonbase.curMinigame = self
        self.modelCount = 500
        self.cleanupActions = []
        self.usesSmoothing = 0
        self.usesLookAround = 0
        self.difficultyOverride = None
        self.trolleyZoneOverride = None
        self.frameworkFSM.enterInitialState()

    
    def addChildGameFSM(self, gameFSM):
        self.frameworkFSM.getStateNamed('frameworkGame').addChild(gameFSM)

    
    def removeChildGameFSM(self, gameFSM):
        self.frameworkFSM.getStateNamed('frameworkGame').removeChild(gameFSM)

    
    def setUsesSmoothing(self):
        self.usesSmoothing = 1

    
    def setUsesLookAround(self):
        self.usesLookAround = 1

    
    def getTitle(self):
        return Localizer.DefaultMinigameTitle

    
    def getInstructions(self):
        return Localizer.DefaultMinigameInstructions

    
    def getMaxDuration(self):
        raise Exception('Minigame implementer: you must override getMaxDuration()')

    
    def _DistributedMinigame__createRandomNumGen(self):
        self.notify.debug('BASE: self.doId=0x%08X' % self.doId)
        self.randomNumGen = RandomNumGen.RandomNumGen(self.doId)
        
        def destroy(self = self):
            self.notify.debug('BASE: destroying random num gen')
            del self.randomNumGen

        self.cleanupActions.append(destroy)

    
    def generate(self):
        self.notify.debug('BASE: generate, %s' % self.getTitle())
        DistributedObject.DistributedObject.generate(self)
        self._DistributedMinigame__createRandomNumGen()
        self.announceGenerateName = self.uniqueName('generate')
        self.accept(self.announceGenerateName, self.handleAnnounceGenerate)

    
    def handleAnnounceGenerate(self, obj):
        self.notify.debug('BASE: handleAnnounceGenerate: send setAvatarJoined')
        self.ignore(self.announceGenerateName)
        self._DistributedMinigame__delayDelete = DelayDelete.DelayDelete(self)
        if toonbase.randomMinigameNetworkPlugPull and random.random() < 1.0 / 25:
            print '*** DOING RANDOM MINIGAME NETWORK-PLUG-PULL BEFORE SENDING setAvatarJoined ***'
            toonbase.tcr.pullNetworkPlug()
        
        self.sendUpdate('setAvatarJoined', [])
        self.normalExit = 1
        count = self.modelCount
        loader.beginBulkLoad('minigame', Localizer.HeadingToMinigameTitle % self.getTitle(), count, 1, Localizer.TIP_MINIGAME)
        self.load()
        loader.endBulkLoad('minigame')
        globalClock.syncFrameTime()
        self.onstage()
        
        def cleanup(self = self):
            self.notify.debug('BASE: cleanup: normalExit=%s' % self.normalExit)
            self.offstage()
            toonbase.tcr.renderFrame()
            if self.normalExit:
                self.sendUpdate('setAvatarExited', [])
            

        self.cleanupActions.append(cleanup)
        self.frameworkFSM.request('frameworkRules')

    
    def disable(self):
        self.notify.debug('BASE: disable')
        taskMgr.remove(self.uniqueName('random-abort'))
        taskMgr.remove(self.uniqueName('random-disconnect'))
        taskMgr.remove(self.uniqueName('random-netplugpull'))
        DistributedObject.DistributedObject.disable(self)

    
    def delete(self):
        self.notify.debug('BASE: delete')
        self.unload()
        self.ignoreAll()
        hoodMinigameState = self.cr.playGame.hood.fsm.getStateNamed('minigame')
        hoodMinigameState.removeChild(self.frameworkFSM)
        self.waitingStartLabel.destroy()
        del self.waitingStartLabel
        del self.frameworkFSM
        DistributedObject.DistributedObject.delete(self)

    
    def load(self):
        self.notify.debug('BASE: load')
        Toon.loadMinigameAnims()

    
    def onstage(self):
        self.notify.debug('BASE: onstage')
        
        def calcMaxDuration(self = self):
            return (self.getMaxDuration() + MinigameGlobals.rulesDuration) * 1.1000000000000001

        if not toonbase.tcr.networkPlugPulled():
            if toonbase.randomMinigameAbort:
                maxDuration = calcMaxDuration()
                self.randomAbortDelay = random.random() * maxDuration
                taskMgr.doMethodLater(self.randomAbortDelay, self.doRandomAbort, self.uniqueName('random-abort'))
            
            if toonbase.randomMinigameDisconnect:
                maxDuration = calcMaxDuration()
                self.randomDisconnectDelay = random.random() * maxDuration
                taskMgr.doMethodLater(self.randomDisconnectDelay, self.doRandomDisconnect, self.uniqueName('random-disconnect'))
            
            if toonbase.randomMinigameNetworkPlugPull:
                maxDuration = calcMaxDuration()
                self.randomNetPlugPullDelay = random.random() * maxDuration
                taskMgr.doMethodLater(self.randomNetPlugPullDelay, self.doRandomNetworkPlugPull, self.uniqueName('random-netplugpull'))
            
        

    
    def doRandomAbort(self, task):
        print '*** DOING RANDOM MINIGAME ABORT AFTER %.2f SECONDS ***' % self.randomAbortDelay
        self.d_requestExit()
        return Task.done

    
    def doRandomDisconnect(self, task):
        print '*** DOING RANDOM MINIGAME DISCONNECT AFTER %.2f SECONDS ***' % self.randomDisconnectDelay
        self.sendUpdate('setGameReady')
        return Task.done

    
    def doRandomNetworkPlugPull(self, task):
        print '*** DOING RANDOM MINIGAME NETWORK-PLUG-PULL AFTER %.2f SECONDS ***' % self.randomNetPlugPullDelay
        toonbase.tcr.pullNetworkPlug()
        return Task.done

    
    def offstage(self):
        self.notify.debug('BASE: offstage')
        for avId in self.avIdList:
            av = self.getAvatar(avId)
            if av:
                av.reparentTo(hidden)
            
        
        messenger.send('minigameOffstage')

    
    def unload(self):
        self.notify.debug('BASE: unload')
        if hasattr(toonbase, 'curMinigame'):
            del toonbase.curMinigame
        
        Toon.unloadMinigameAnims()

    
    def setParticipants(self, avIds):
        self.avIdList = avIds
        self.numPlayers = len(self.avIdList)
        if self.localAvId not in self.avIdList:
            self.notify.error('localToon (%s) not in list of minigame players: %s' % (self.localAvId, self.avIdList))
        
        self.notify.debug('BASE: setParticipants: game will be played ' + 'by these avatars: %s' % self.avIdList)
        self.remoteAvIdList = []
        for avId in self.avIdList:
            if avId != self.localAvId:
                self.remoteAvIdList.append(avId)
            
        

    
    def setTrolleyZone(self, trolleyZone):
        self.notify.debug('BASE: setTrolleyZone: %s' % trolleyZone)
        self.trolleyZone = trolleyZone

    
    def setDifficultyOverrides(self, difficultyOverride, trolleyZoneOverride):
        if difficultyOverride != MinigameGlobals.NoDifficultyOverride:
            self.difficultyOverride = difficultyOverride / float(MinigameGlobals.DifficultyOverrideMult)
        
        if trolleyZoneOverride != MinigameGlobals.NoTrolleyZoneOverride:
            self.trolleyZoneOverride = trolleyZoneOverride
        

    
    def setGameReady(self):
        self.notify.debug('BASE: setGameReady: Ready for game with avatars: %s' % self.avIdList)
        self.notify.debug('  safezone: %s' % self.getSafezoneId())
        self.notify.debug('difficulty: %s' % self.getDifficulty())
        self._DistributedMinigame__serverFinished = 0
        for avId in self.remoteAvIdList:
            if not self.cr.doId2do.has_key(avId):
                self.notify.warning('BASE: toon %s already left or has not yet arrived; waiting for server to abort the game' % avId)
                return 1
            
        
        for avId in self.remoteAvIdList:
            avatar = self.cr.doId2do[avId]
            event = avatar.uniqueName('disable')
            self.acceptOnce(event, self.handleDisabledAvatar, [
                avId])
            
            def ignoreToonDisable(self = self, event = event):
                self.ignore(event)

            self.cleanupActions.append(ignoreToonDisable)
        
        for avId in self.avIdList:
            avatar = self.getAvatar(avId)
            if avatar:
                if not (self.usesSmoothing):
                    avatar.stopSmooth()
                
                if not (self.usesLookAround):
                    avatar.stopLookAround()
                
            
        
        return 0

    
    def setGameStart(self, timestamp):
        self.notify.debug('BASE: setGameStart: Starting game')
        self.gameStartTime = globalClockDelta.networkToLocalTime(timestamp)
        self.frameworkFSM.request('frameworkGame')

    
    def setGameAbort(self):
        self.notify.warning('BASE: setGameAbort: Aborting game')
        self.normalExit = 0
        self.frameworkFSM.request('frameworkCleanup')

    
    def gameOver(self):
        self.notify.debug('BASE: gameOver')
        self.frameworkFSM.request('frameworkWaitServerFinish')

    
    def getAvatar(self, avId):
        if self.cr.doId2do.has_key(avId):
            return self.cr.doId2do[avId]
        else:
            self.notify.warning('BASE: getAvatar: No avatar in doId2do with id: ' + str(avId))
            return None

    
    def getAvatarName(self, avId):
        avatar = self.getAvatar(avId)
        if avatar:
            return avatar.getName()
        else:
            return 'Unknown'

    
    def isSinglePlayer(self):
        if self.numPlayers == 1:
            return 1
        else:
            return 0

    
    def handleDisabledAvatar(self, avId):
        self.notify.warning('BASE: handleDisabledAvatar: disabled avId: ' + str(avId))
        self.frameworkFSM.request('frameworkAvatarExited')

    
    def d_requestExit(self):
        self.notify.debug('BASE: Sending requestExit')
        self.sendUpdate('requestExit', [])

    
    def enterFrameworkInit(self):
        self.notify.debug('BASE: enterFrameworkInit')
        self.setEmotes()
        self.cleanupActions.append(self.unsetEmotes)

    
    def exitFrameworkInit(self):
        pass

    
    def enterFrameworkRules(self):
        self.notify.debug('BASE: enterFrameworkRules')
        self.accept(self.rulesDoneEvent, self.handleRulesDone)
        self.rulesPanel = MinigameRulesPanel.MinigameRulesPanel('MinigameRulesPanel', self.getTitle(), self.getInstructions(), self.rulesDoneEvent)
        self.rulesPanel.load()
        self.rulesPanel.enter()

    
    def exitFrameworkRules(self):
        self.ignore(self.rulesDoneEvent)
        self.rulesPanel.exit()
        self.rulesPanel.unload()
        del self.rulesPanel

    
    def handleRulesDone(self):
        self.notify.debug('BASE: handleRulesDone')
        self.sendUpdate('setAvatarReady', [])
        self.frameworkFSM.request('frameworkWaitServerStart')

    
    def enterFrameworkWaitServerStart(self):
        self.notify.debug('BASE: enterFrameworkWaitServerStart')
        if self.numPlayers > 1:
            msg = Localizer.MinigameWaitingForOtherPlayers
        else:
            msg = Localizer.MinigamePleaseWait
        self.waitingStartLabel['text'] = msg
        self.waitingStartLabel.show()

    
    def exitFrameworkWaitServerStart(self):
        self.waitingStartLabel.hide()

    
    def enterFrameworkGame(self):
        self.notify.debug('BASE: enterFrameworkGame')

    
    def exitFrameworkGame(self):
        pass

    
    def enterFrameworkWaitServerFinish(self):
        self.notify.debug('BASE: enterFrameworkWaitServerFinish')
        if self._DistributedMinigame__serverFinished:
            self.frameworkFSM.request('frameworkCleanup')
        

    
    def setGameExit(self):
        self.notify.debug('BASE: setGameExit: now safe to exit game')
        if self.frameworkFSM.getCurrentState().getName() != 'frameworkWaitServerFinish':
            self._DistributedMinigame__serverFinished = 1
        else:
            self.frameworkFSM.request('frameworkCleanup')

    
    def exitFrameworkWaitServerFinish(self):
        pass

    
    def enterFrameworkAvatarExited(self):
        self.notify.debug('BASE: enterFrameworkAvatarExited')

    
    def exitFrameworkAvatarExited(self):
        pass

    
    def enterFrameworkCleanup(self):
        self.notify.debug('BASE: enterFrameworkCleanup')
        for action in self.cleanupActions:
            action()
        
        self.ignoreAll()
        for avId in self.avIdList:
            avatar = self.getAvatar(avId)
            if avatar:
                avatar.stopSmooth()
                avatar.startLookAround()
            
        
        messenger.send(self.cr.playGame.hood.minigameDoneEvent)
        hoodMinigameState = self.cr.playGame.hood.fsm.getStateNamed('minigame')
        hoodMinigameState.removeChild(self.frameworkFSM)
        del self._DistributedMinigame__delayDelete

    
    def exitFrameworkCleanup(self):
        pass

    
    def local2GameTime(self, timestamp):
        return timestamp - self.gameStartTime

    
    def game2LocalTime(self, timestamp):
        return timestamp + self.gameStartTime

    
    def getCurrentGameTime(self):
        return self.local2GameTime(globalClock.getFrameTime())

    
    def getDifficulty(self):
        if self.difficultyOverride is not None:
            return self.difficultyOverride
        
        if hasattr(toonbase, 'minigameDifficulty'):
            return float(toonbase.minigameDifficulty)
        
        return MinigameGlobals.getDifficulty(self.getSafezoneId())

    
    def getSafezoneId(self):
        if self.trolleyZoneOverride is not None:
            return self.trolleyZoneOverride
        
        if hasattr(toonbase, 'minigameSafezoneId'):
            return MinigameGlobals.getSafezoneId(toonbase.minigameSafezoneId)
        
        return MinigameGlobals.getSafezoneId(self.trolleyZone)

    
    def setEmotes(self):
        Emote.DisableAll(toonbase.localToon)

    
    def unsetEmotes(self):
        Emote.ReleaseAll(toonbase.localToon)


