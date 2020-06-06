# File: T (Python 2.2)

from ToontownBattleGlobals import *
import types
import StateData
import FSM
import State
import TownBattleAttackPanel
import TownBattleWaitPanel
import TownBattleChooseAvatarPanel
import TownBattleSOSPanel
import TownBattleToonPanel
import ToontownDialog
import DirectNotifyGlobal
import BattleBase
import ToontownTimer
import PythonUtil
import Localizer

class TownBattle(StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('TownBattle')
    evenPos = (0.75, 0.25, -0.25, -0.75)
    oddPos = (0.5, 0, -0.5)
    
    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.numCogs = 1
        self.creditLevel = None
        self.luredIndices = []
        self.trappedIndices = []
        self.numToons = 1
        self.toons = []
        self.localNum = 0
        self.time = 0
        self.bldg = 0
        self.track = -1
        self.level = -1
        self.target = 0
        self.toonAttacks = [
            (-1, 0, 0),
            (-1, 0, 0),
            (-1, 0, 0),
            (-1, 0, 0)]
        self.fsm = FSM.FSM('TownBattle', [
            State.State('Off', self.enterOff, self.exitOff, [
                'Attack']),
            State.State('Attack', self.enterAttack, self.exitAttack, [
                'ChooseCog',
                'ChooseToon',
                'AttackWait',
                'Run',
                'SOS']),
            State.State('ChooseCog', self.enterChooseCog, self.exitChooseCog, [
                'AttackWait',
                'Attack']),
            State.State('AttackWait', self.enterAttackWait, self.exitAttackWait, [
                'ChooseCog',
                'ChooseToon',
                'Attack']),
            State.State('ChooseToon', self.enterChooseToon, self.exitChooseToon, [
                'AttackWait',
                'Attack']),
            State.State('Run', self.enterRun, self.exitRun, [
                'Attack']),
            State.State('SOS', self.enterSOS, self.exitSOS, [
                'Attack',
                'AttackWait'])], 'Off', 'Off')
        self.runPanel = ToontownDialog.ToontownDialog(dialogName = 'TownBattleRunPanel', text = Localizer.TownBattleRun, style = ToontownDialog.TwoChoice, command = self._TownBattle__handleRunPanelDone)
        self.runPanel.hide()
        self.attackPanelDoneEvent = 'attack-panel-done'
        self.attackPanel = TownBattleAttackPanel.TownBattleAttackPanel(self.attackPanelDoneEvent)
        self.waitPanelDoneEvent = 'wait-panel-done'
        self.waitPanel = TownBattleWaitPanel.TownBattleWaitPanel(self.waitPanelDoneEvent)
        self.chooseCogPanelDoneEvent = 'choose-cog-panel-done'
        self.chooseCogPanel = TownBattleChooseAvatarPanel.TownBattleChooseAvatarPanel(self.chooseCogPanelDoneEvent, 0)
        self.chooseToonPanelDoneEvent = 'choose-toon-panel-done'
        self.chooseToonPanel = TownBattleChooseAvatarPanel.TownBattleChooseAvatarPanel(self.chooseToonPanelDoneEvent, 1)
        self.SOSPanelDoneEvent = 'SOS-panel-done'
        self.SOSPanel = TownBattleSOSPanel.TownBattleSOSPanel(self.SOSPanelDoneEvent)
        self.toonPanels = (TownBattleToonPanel.TownBattleToonPanel(0), TownBattleToonPanel.TownBattleToonPanel(1), TownBattleToonPanel.TownBattleToonPanel(2), TownBattleToonPanel.TownBattleToonPanel(3))
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.setPos(1.1819999999999999, 0, 0.84199999999999997)
        self.timer.setScale(0.40000000000000002)
        self.timer.hide()
        return None

    
    def cleanup(self):
        self.unload()
        del self.fsm
        self.runPanel.cleanup()
        del self.runPanel
        del self.attackPanel
        del self.waitPanel
        del self.chooseCogPanel
        del self.chooseToonPanel
        del self.SOSPanel
        for toonPanel in self.toonPanels:
            toonPanel.cleanup()
        
        del self.toonPanels
        self.timer.destroy()
        del self.timer
        del self.toons
        return None

    
    def enter(self, event, parentFSMState, bldg = 0, creditMultiplier = 1, tutorialFlag = 0):
        self.parentFSMState = parentFSMState
        self.parentFSMState.addChild(self.fsm)
        if not (self.isLoaded):
            self.load()
        
        self.battleEvent = event
        self.fsm.enterInitialState()
        toonbase.localToon.laffMeter.start()
        self.numToons = 1
        self.numCogs = 1
        self.toons = [
            toonbase.localToon.doId]
        self.toonPanels[0].setLaffMeter(toonbase.localToon)
        self.bldg = bldg
        self.creditLevel = None
        self.creditMultiplier = creditMultiplier
        self.tutorialFlag = tutorialFlag
        toonbase.localToon.inventory.setBattleCreditMultiplier(self.creditMultiplier)
        toonbase.localToon.inventory.setActivateMode('battle', heal = 0, bldg = bldg, tutorialFlag = tutorialFlag)

    
    def exit(self):
        toonbase.localToon.laffMeter.stop()
        self.parentFSMState.removeChild(self.fsm)
        del self.parentFSMState
        toonbase.localToon.inventory.setBattleCreditMultiplier(1)

    
    def load(self):
        if self.isLoaded:
            return None
        
        self.attackPanel.load()
        self.waitPanel.load()
        self.chooseCogPanel.load()
        self.chooseToonPanel.load()
        self.SOSPanel.load()
        self.isLoaded = 1

    
    def unload(self):
        if not (self.isLoaded):
            return None
        
        self.attackPanel.unload()
        self.waitPanel.unload()
        self.chooseCogPanel.unload()
        self.chooseToonPanel.unload()
        self.SOSPanel.unload()
        self.isLoaded = 0

    
    def setState(self, state):
        if hasattr(self, 'fsm'):
            self.fsm.request(state)
        

    
    def updateTimer(self, time):
        self.time = time
        self.timer.setTime(time)
        return None

    
    def _TownBattle__enterPanels(self, num, localNum):
        self.notify.debug('enterPanels() num: %d localNum: %d' % (num, localNum))
        for toonPanel in self.toonPanels:
            toonPanel.hide()
            toonPanel.setPos(0, 0, -0.90000000000000002)
        
        if num == 1:
            self.toonPanels[0].setX(self.oddPos[1])
            self.toonPanels[0].show()
        elif num == 2:
            self.toonPanels[0].setX(self.evenPos[1])
            self.toonPanels[0].show()
            self.toonPanels[1].setX(self.evenPos[2])
            self.toonPanels[1].show()
        elif num == 3:
            self.toonPanels[0].setX(self.oddPos[0])
            self.toonPanels[0].show()
            self.toonPanels[1].setX(self.oddPos[1])
            self.toonPanels[1].show()
            self.toonPanels[2].setX(self.oddPos[2])
            self.toonPanels[2].show()
        elif num == 4:
            self.toonPanels[0].setX(self.evenPos[0])
            self.toonPanels[0].show()
            self.toonPanels[1].setX(self.evenPos[1])
            self.toonPanels[1].show()
            self.toonPanels[2].setX(self.evenPos[2])
            self.toonPanels[2].show()
            self.toonPanels[3].setX(self.evenPos[3])
            self.toonPanels[3].show()
        else:
            self.notify.error('Bad number of toons: %s' % num)
        return None

    
    def updateChosenAttacks(self, battleIndices, tracks, levels, targets):
        self.notify.debug('updateChosenAttacks bi=%s tracks=%s levels=%s targets=%s' % (battleIndices, tracks, levels, targets))
        for i in range(4):
            if battleIndices[i] == -1:
                pass
            1
            if tracks[i] == BattleBase.NO_ATTACK:
                numTargets = 0
                target = -2
            elif tracks[i] == BattleBase.SOS:
                numTargets = 0
                target = -2
            elif tracks[i] == HEAL_TRACK:
                numTargets = self.numToons
                if self._TownBattle__isGroupHeal(levels[i]):
                    target = -2
                else:
                    target = targets[i]
            else:
                numTargets = self.numCogs
                if self._TownBattle__isGroupAttack(tracks[i], levels[i]):
                    target = -1
                else:
                    target = targets[i]
                    if target == -1:
                        numTargets = None
                    
            self.toonPanels[battleIndices[i]].setValues(battleIndices[i], tracks[i], levels[i], numTargets, target, self.localNum)
        
        return None

    
    def chooseDefaultTarget(self):
        if self.track > -1:
            response = { }
            response['mode'] = 'Attack'
            response['track'] = self.track
            response['level'] = self.level
            response['target'] = self.target
            messenger.send(self.battleEvent, [
                response])
            return 1
        
        return 0

    
    def updateLaffMeter(self, toonNum, hp):
        self.toonPanels[toonNum].updateLaffMeter(hp)

    
    def enterOff(self):
        if self.isLoaded:
            for toonPanel in self.toonPanels:
                toonPanel.hide()
            
        
        self.toonAttacks = [
            (-1, 0, 0),
            (-1, 0, 0),
            (-1, 0, 0),
            (-1, 0, 0)]
        self.target = 0
        if hasattr(self, 'timer'):
            self.timer.hide()
        
        return None

    
    def exitOff(self):
        if self.isLoaded:
            self._TownBattle__enterPanels(self.numToons, self.localNum)
        
        self.timer.show()
        self.track = -1
        self.level = -1
        self.target = 0
        return None

    
    def enterAttack(self):
        self.attackPanel.enter()
        self.accept(self.attackPanelDoneEvent, self._TownBattle__handleAttackPanelDone)
        for toonPanel in self.toonPanels:
            toonPanel.setValues(0, BattleBase.NO_ATTACK)
        
        return None

    
    def exitAttack(self):
        self.ignore(self.attackPanelDoneEvent)
        self.attackPanel.exit()
        return None

    
    def _TownBattle__handleAttackPanelDone(self, doneStatus):
        self.notify.debug('doneStatus: %s' % doneStatus)
        mode = doneStatus['mode']
        if mode == 'Inventory':
            self.track = doneStatus['track']
            self.level = doneStatus['level']
            self.toonPanels[self.localNum].setValues(self.localNum, self.track, self.level)
            if self.track == HEAL_TRACK:
                if self._TownBattle__isGroupHeal(self.level):
                    response = { }
                    response['mode'] = 'Attack'
                    response['track'] = self.track
                    response['level'] = self.level
                    response['target'] = self.target
                    messenger.send(self.battleEvent, [
                        response])
                    self.fsm.request('AttackWait')
                elif self.numToons == 3 or self.numToons == 4:
                    self.fsm.request('ChooseToon')
                elif self.numToons == 2:
                    response = { }
                    response['mode'] = 'Attack'
                    response['track'] = self.track
                    response['level'] = self.level
                    if self.localNum == 0:
                        response['target'] = 1
                    elif self.localNum == 1:
                        response['target'] = 0
                    else:
                        self.notify.error('Bad localNum value: %s' % self.localNum)
                    messenger.send(self.battleEvent, [
                        response])
                    self.fsm.request('AttackWait')
                else:
                    self.notify.error('Heal was chosen when number of toons is %s' % self.numToons)
            elif self._TownBattle__isCogChoiceNecessary():
                self.notify.info('choice needed')
                self.fsm.request('ChooseCog')
                response = { }
                response['mode'] = 'Attack'
                response['track'] = self.track
                response['level'] = self.level
                response['target'] = -1
                messenger.send(self.battleEvent, [
                    response])
            else:
                self.notify.info('no choice needed')
                self.fsm.request('AttackWait')
                response = { }
                response['mode'] = 'Attack'
                response['track'] = self.track
                response['level'] = self.level
                response['target'] = 0
                messenger.send(self.battleEvent, [
                    response])
        elif mode == 'Run':
            self.fsm.request('Run')
        elif mode == 'SOS':
            self.fsm.request('SOS')
        elif mode == 'Pass':
            response = { }
            response['mode'] = 'Pass'
            response['id'] = -1
            messenger.send(self.battleEvent, [
                response])
            self.fsm.request('AttackWait')
        else:
            self.notify.warning('unknown mode: %s' % mode)

    
    def checkHealTrapLure(self):
        self.notify.debug('numToons: %s, numCogs: %s, lured: %s, trapped: %s' % (self.numToons, self.numCogs, self.luredIndices, self.trappedIndices))
        if len(PythonUtil.union(self.trappedIndices, self.luredIndices)) == self.numCogs:
            canTrap = 0
        else:
            canTrap = 1
        if len(self.luredIndices) == self.numCogs:
            canLure = 0
            canTrap = 0
        else:
            canLure = 1
        if self.numToons == 1:
            canHeal = 0
        else:
            canHeal = 1
        return (canHeal, canTrap, canLure)

    
    def adjustCogsAndToons(self, cogs, luredIndices, trappedIndices, toons):
        numCogs = len(cogs)
        self.notify.debug('adjustCogsAndToons() numCogs: %s self.numCogs: %s' % (numCogs, self.numCogs))
        self.notify.debug('adjustCogsAndToons() luredIndices: %s self.luredIndices: %s' % (luredIndices, self.luredIndices))
        self.notify.debug('adjustCogsAndToons() trappedIndices: %s self.trappedIndices: %s' % (trappedIndices, self.trappedIndices))
        toonIds = map(lambda toon: toon.doId, toons)
        self.notify.debug('adjustCogsAndToons() toonIds: %s self.toons: %s' % (toonIds, self.toons))
        maxSuitLevel = 0
        for cog in cogs:
            maxSuitLevel = max(maxSuitLevel, cog.getActualLevel())
        
        creditLevel = maxSuitLevel
        if numCogs == self.numCogs and creditLevel == self.creditLevel and luredIndices == self.luredIndices and trappedIndices == self.trappedIndices and toonIds == self.toons:
            resetActivateMode = 0
        else:
            resetActivateMode = 1
        self.notify.debug('adjustCogsAndToons() resetActivateMode: %s' % resetActivateMode)
        self.numCogs = numCogs
        self.creditLevel = creditLevel
        self.luredIndices = luredIndices
        self.trappedIndices = trappedIndices
        self.toons = toonIds
        self.numToons = len(toons)
        self.localNum = toons.index(toonbase.localToon)
        currStateName = self.fsm.getCurrentState().getName()
        if resetActivateMode:
            self._TownBattle__enterPanels(self.numToons, self.localNum)
            for i in range(len(toons)):
                self.toonPanels[i].setLaffMeter(toons[i])
            
            if currStateName == 'ChooseCog':
                self.chooseCogPanel.adjustCogs(self.numCogs, self.luredIndices, self.trappedIndices, self.track)
            elif currStateName == 'ChooseToon':
                self.chooseToonPanel.adjustToons(self.numToons, self.localNum)
            
            (canHeal, canTrap, canLure) = self.checkHealTrapLure()
            toonbase.localToon.inventory.setBattleCreditMultiplier(self.creditMultiplier)
            toonbase.localToon.inventory.setActivateMode('battle', heal = canHeal, trap = canTrap, lure = canLure, bldg = self.bldg, creditLevel = self.creditLevel, tutorialFlag = self.tutorialFlag)
        
        return None

    
    def enterChooseCog(self):
        self.cog = 0
        self.chooseCogPanel.enter(self.numCogs, luredIndices = self.luredIndices, trappedIndices = self.trappedIndices, track = self.track)
        self.accept(self.chooseCogPanelDoneEvent, self._TownBattle__handleChooseCogPanelDone)
        return None

    
    def exitChooseCog(self):
        self.ignore(self.chooseCogPanelDoneEvent)
        self.chooseCogPanel.exit()
        return None

    
    def _TownBattle__handleChooseCogPanelDone(self, doneStatus):
        mode = doneStatus['mode']
        if mode == 'Back':
            self.fsm.request('Attack')
        elif mode == 'Avatar':
            self.cog = doneStatus['avatar']
            self.target = self.cog
            self.fsm.request('AttackWait')
            response = { }
            response['mode'] = 'Attack'
            response['track'] = self.track
            response['level'] = self.level
            response['target'] = self.cog
            messenger.send(self.battleEvent, [
                response])
        else:
            self.notify.warning('unknown mode: %s' % mode)

    
    def enterAttackWait(self, chosenToon = -1):
        self.accept(self.waitPanelDoneEvent, self._TownBattle__handleAttackWaitBack)
        self.waitPanel.enter(self.numToons)

    
    def exitAttackWait(self):
        self.waitPanel.exit()
        self.ignore(self.waitPanelDoneEvent)

    
    def _TownBattle__handleAttackWaitBack(self, doneStatus):
        mode = doneStatus['mode']
        if mode == 'Back':
            if self.track == HEAL_TRACK:
                self.fsm.request('Attack')
            elif self.track == BattleBase.NO_ATTACK:
                self.fsm.request('Attack')
            elif self._TownBattle__isCogChoiceNecessary():
                self.fsm.request('ChooseCog')
            else:
                self.fsm.request('Attack')
            response = { }
            response['mode'] = 'UnAttack'
            messenger.send(self.battleEvent, [
                response])
        else:
            self.notify.error('unknown mode: %s' % mode)

    
    def enterChooseToon(self):
        self.toon = 0
        self.chooseToonPanel.enter(self.numToons, localNum = self.localNum)
        self.accept(self.chooseToonPanelDoneEvent, self._TownBattle__handleChooseToonPanelDone)
        return None

    
    def exitChooseToon(self):
        self.ignore(self.chooseToonPanelDoneEvent)
        self.chooseToonPanel.exit()
        return None

    
    def _TownBattle__handleChooseToonPanelDone(self, doneStatus):
        mode = doneStatus['mode']
        if mode == 'Back':
            self.fsm.request('Attack')
        elif mode == 'Avatar':
            self.toon = doneStatus['avatar']
            self.target = self.toon
            self.fsm.request('AttackWait', [
                self.toon])
            response = { }
            response['mode'] = 'Attack'
            response['track'] = self.track
            response['level'] = self.level
            response['target'] = self.toon
            messenger.send(self.battleEvent, [
                response])
        else:
            self.notify.warning('unknown mode: %s' % mode)

    
    def enterRun(self):
        self.runPanel.show()

    
    def exitRun(self):
        self.runPanel.hide()

    
    def _TownBattle__handleRunPanelDone(self, doneStatus):
        if doneStatus == ToontownDialog.DIALOG_OK:
            response = { }
            response['mode'] = 'Run'
            messenger.send(self.battleEvent, [
                response])
        else:
            self.fsm.request('Attack')

    
    def enterSOS(self):
        self.SOSPanel.enter()
        self.accept(self.SOSPanelDoneEvent, self._TownBattle__handleSOSPanelDone)
        return None

    
    def exitSOS(self):
        self.ignore(self.SOSPanelDoneEvent)
        self.SOSPanel.exit()
        return None

    
    def _TownBattle__handleSOSPanelDone(self, doneStatus):
        mode = doneStatus['mode']
        if mode == 'Friend':
            doId = doneStatus['friend']
            response = { }
            response['mode'] = 'SOS'
            response['id'] = doId
            messenger.send(self.battleEvent, [
                response])
            self.fsm.request('AttackWait')
        elif mode == 'Back':
            self.fsm.request('Attack')
        

    
    def _TownBattle__isCogChoiceNecessary(self):
        if self.numCogs > 1 and not self._TownBattle__isGroupAttack(self.track, self.level):
            return 1
        else:
            return 0

    
    def _TownBattle__isGroupAttack(self, trackNum, levelNum):
        if trackNum == SOUND_TRACK:
            return 1
        elif trackNum == LURE_TRACK and levelNum % 2:
            return 1
        else:
            return 0

    
    def _TownBattle__isGroupHeal(self, levelNum):
        if levelNum % 2:
            return 1
        else:
            return 0


