# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToonBaseGlobal import *
from direct.distributed.ClockDelta import *
from DistributedMinigame import *
from direct.gui.DirectGui import *
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.task import Task
from toontown.toonbase import ToontownTimer
import RaceGameGlobals
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer

class DistributedRaceGame(DistributedMinigame):
    
    def __init__(self, cr):
        DistributedMinigame.__init__(self, cr)
        self.gameFSM = ClassicFSM.ClassicFSM('DistributedRaceGame', [
            State.State('off', self.enterOff, self.exitOff, [
                'inputChoice']),
            State.State('inputChoice', self.enterInputChoice, self.exitInputChoice, [
                'waitServerChoices',
                'moveAvatars',
                'cleanup']),
            State.State('waitServerChoices', self.enterWaitServerChoices, self.exitWaitServerChoices, [
                'moveAvatars',
                'cleanup']),
            State.State('moveAvatars', self.enterMoveAvatars, self.exitMoveAvatars, [
                'inputChoice',
                'winMovie',
                'cleanup']),
            State.State('winMovie', self.enterWinMovie, self.exitWinMovie, [
                'cleanup']),
            State.State('cleanup', self.enterCleanup, self.exitCleanup, [])], 'off', 'cleanup')
        self.addChildGameFSM(self.gameFSM)
        self.posHprArray = (((-9.0299999999999994, 0.059999999999999998, 0.025000000000000001, -152.90000000000001), (-7.4299999999999997, -2.7599999999999998, 0.025000000000000001, -152.68000000000001), (-6.0199999999999996, -5.4800000000000004, 0.025000000000000001, -157.53999999999999), (-5.0099999999999998, -8.3200000000000003, 0.025000000000000001, -160.66), (-4.0499999999999998, -11.359999999999999, 0.025000000000000001, -170.22), (-3.4900000000000002, -14.18, 0.025000000000000001, -175.75999999999999), (-3.1200000000000001, -17.149999999999999, 0.025000000000000001, -177.72999999999999), (-3.0, -20.32, 0.025000000000000001, 178.49000000000001), (-3.0899999999999999, -23.440000000000001, 0.025000000000000001, 176.59), (-3.4300000000000002, -26.539999999999999, 0.025000000000000001, 171.44), (-4.0700000000000003, -29.440000000000001, 0.025000000000000001, 163.75), (-5.0899999999999999, -32.270000000000003, 0.025000000000000001, 158.19999999999999), (-6.1100000000000003, -35.159999999999997, 0.025000000000000001, 154.97999999999999), (-7.5700000000000003, -37.780000000000001, 0.025000000000000001, 154.97999999999999), (-9.2799999999999994, -40.649999999999999, 0.025000000000000001, 150.41)), ((-6.1200000000000001, 1.6200000000000001, 0.025000000000000001, -152.90000000000001), (-4.3799999999999999, -1.3500000000000001, 0.025000000000000001, -150.91999999999999), (-3.0800000000000001, -4.2999999999999998, 0.025000000000000001, -157.90000000000001), (-1.8500000000000001, -7.2599999999999998, 0.025000000000000001, -162.53999999999999), (-0.93000000000000005, -10.49, 0.025000000000000001, -167.71000000000001), (-0.20999999999999999, -13.710000000000001, 0.025000000000000001, -171.78999999999999), (0.20999999999999999, -17.079999999999998, 0.025000000000000001, -174.91999999999999), (0.31, -20.199999999999999, 0.025000000000000001, 177.09999999999999), (0.17000000000000001, -23.66, 0.025000000000000001, 174.81999999999999), (-0.23000000000000001, -26.91, 0.025000000000000001, 170.50999999999999), (-0.98999999999999999, -30.199999999999999, 0.025000000000000001, 162.53999999999999), (-2.02, -33.280000000000001, 0.025000000000000001, 160.47999999999999), (-3.2799999999999998, -36.380000000000003, 0.025000000000000001, 157.96000000000001), (-4.6699999999999999, -39.170000000000002, 0.025000000000000001, 154.13), (-6.3099999999999996, -42.149999999999999, 0.025000000000000001, 154.13)), ((-2.9900000000000002, 3.0899999999999999, 0.025000000000000001, -154.37), (-1.3799999999999999, -0.050000000000000003, 0.025000000000000001, -154.75), (-0.19, -3.29, 0.025000000000000001, -159.22), (1.1699999999999999, -6.5099999999999998, 0.025000000000000001, -162.74000000000001), (2.2799999999999998, -9.8000000000000007, 0.025000000000000001, -168.72999999999999), (3.0899999999999999, -13.279999999999999, 0.025000000000000001, -173.49000000000001), (3.46, -16.629999999999999, 0.025000000000000001, -176.81), (3.6899999999999999, -20.379999999999999, 0.025000000000000001, 179.13999999999999), (3.6099999999999999, -24.120000000000001, 0.025000000000000001, 175.78), (3.0, -27.550000000000001, 0.025000000000000001, 170.87), (2.1499999999999999, -30.719999999999999, 0.025000000000000001, 167.41), (1.04, -34.259999999999998, 0.025000000000000001, 162.11000000000001), (-0.14999999999999999, -37.439999999999998, 0.025000000000000001, 158.59), (-1.6399999999999999, -40.520000000000003, 0.025000000000000001, 153.88999999999999), (-3.4199999999999999, -43.630000000000003, 0.025000000000000001, 153.88999999999999)), ((0.0, 4.3499999999999996, 0.025000000000000001, -154.37), (1.52, 1.3, 0.025000000000000001, -155.66999999999999), (3.1699999999999999, -2.0699999999999998, 0.025000000000000001, -155.66999999999999), (4.4699999999999998, -5.4100000000000001, 0.025000000000000001, -163.0), (5.5599999999999996, -9.1899999999999995, 0.025000000000000001, -168.88999999999999), (6.2199999999999998, -12.66, 0.025000000000000001, -171.66999999999999), (6.6699999999999999, -16.559999999999999, 0.025000000000000001, -176.53), (6.9299999999999997, -20.329999999999998, 0.025000000000000001, 179.87), (6.8099999999999996, -24.32, 0.025000000000000001, 175.19), (6.2199999999999998, -27.969999999999999, 0.025000000000000001, 170.81), (5.5899999999999999, -31.73, 0.025000000000000001, 167.53999999999999), (4.4800000000000004, -35.420000000000002, 0.025000000000000001, 161.91999999999999), (3.0600000000000001, -38.82, 0.025000000000000001, 158.56), (1.3999999999999999, -42.0, 0.025000000000000001, 154.31999999999999), (-0.70999999999999996, -45.170000000000002, 0.025000000000000001, 153.27000000000001)))
        self.avatarPositions = { }
        self.modelCount = 8
        self.cameraTopView = (-22.780000000000001, -41.649999999999999, 31.530000000000001, -51.549999999999997, -42.68, -2.96)
        self.timer = None
        self.timerStartTime = None

    
    def getTitle(self):
        return TTLocalizer.RaceGameTitle

    
    def getInstructions(self):
        return TTLocalizer.RaceGameInstructions

    
    def getMaxDuration(self):
        return 60

    
    def load(self):
        self.notify.debug('load')
        DistributedMinigame.load(self)
        self.raceBoard = loader.loadModel('phase_4/models/minigames/race')
        self.raceBoard.setPosHpr(0, 0, 0, 0, 0, 0)
        self.raceBoard.setScale(0.80000000000000004)
        self.dice = loader.loadModel('phase_4/models/minigames/dice')
        self.dice1 = self.dice.find('**/dice_button1')
        self.dice2 = self.dice.find('**/dice_button2')
        self.dice3 = self.dice.find('**/dice_button3')
        self.dice4 = self.dice.find('**/dice_button4')
        self.diceList = [
            self.dice1,
            self.dice2,
            self.dice3,
            self.dice4]
        self.music = base.loadMusic('phase_4/audio/bgm/minigame_race.mid')
        self.posBuzzer = base.loadSfx('phase_4/audio/sfx/MG_pos_buzzer.wav')
        self.negBuzzer = base.loadSfx('phase_4/audio/sfx/MG_neg_buzzer.wav')
        self.winSting = base.loadSfx('phase_4/audio/sfx/MG_win.mp3')
        self.loseSting = base.loadSfx('phase_4/audio/sfx/MG_lose.mp3')
        self.diceButtonList = []
        for i in range(1, 5):
            button = self.dice.find('**/dice_button' + str(i))
            button_down = self.dice.find('**/dice_button' + str(i) + '_down')
            button_ro = self.dice.find('**/dice_button' + str(i) + '_ro')
            diceButton = DirectButton(image = (button, button_down, button_ro, None), relief = None, pos = (-0.90000000000000002 + (i - 1) * 0.20000000000000001, 0.0, -0.84999999999999998), scale = 0.25, command = self.handleInputChoice, extraArgs = [
                i])
            diceButton.hide()
            self.diceButtonList.append(diceButton)
        
        self.waitingChoicesLabel = DirectLabel(text = TTLocalizer.RaceGameWaitingChoices, text_fg = VBase4(1, 1, 1, 1), relief = None, pos = (-0.59999999999999998, 0, -0.75), scale = 0.074999999999999997)
        self.waitingChoicesLabel.hide()
        self.chanceMarker = loader.loadModelOnce('phase_4/models/minigames/question_mark')
        self.chanceCard = loader.loadModelOnce('phase_4/models/minigames/chance_card')
        self.chanceCard.text = OnscreenText('', fg = (1.0, 0, 0, 1), scale = 0.14000000000000001, font = ToontownGlobals.getSignFont(), wordwrap = 14, pos = (0.0, 0.20000000000000001), mayChange = 1)
        self.chanceCard.text.hide()
        self.cardSound = base.loadSfx('phase_3.5/audio/sfx/GUI_stickerbook_turn.mp3')
        self.chanceMarkers = []

    
    def unload(self):
        self.notify.debug('unload')
        DistributedMinigame.unload(self)
        self.raceBoard.removeNode()
        del self.raceBoard
        self.dice.removeNode()
        del self.dice
        self.chanceMarker.removeNode()
        del self.chanceMarker
        self.chanceCard.text.removeNode()
        del self.chanceCard.text
        self.chanceCard.removeNode()
        del self.chanceCard
        self.waitingChoicesLabel.destroy()
        del self.waitingChoicesLabel
        del self.music
        del self.posBuzzer
        del self.negBuzzer
        del self.winSting
        del self.loseSting
        del self.cardSound
        for button in self.diceButtonList:
            button.destroy()
        
        del self.diceButtonList
        for marker in self.chanceMarkers:
            marker.removeNode()
            del marker
        
        del self.chanceMarkers
        self.removeChildGameFSM(self.gameFSM)
        del self.gameFSM

    
    def onstage(self):
        self.notify.debug('onstage')
        DistributedMinigame.onstage(self)
        base.playMusic(self.music, looping = 1, volume = 0.80000000000000004)
        self.raceBoard.reparentTo(render)
        camera.reparentTo(render)
        p = self.cameraTopView
        camera.setPosHpr(p[0], p[1], p[2], p[3], p[4], p[5])
        base.transitions.irisIn(0.40000000000000002)
        base.setBackgroundColor(0.1875, 0.79290000000000005, 0)

    
    def offstage(self):
        self.notify.debug('offstage')
        DistributedMinigame.offstage(self)
        self.music.stop()
        base.setBackgroundColor(ToontownGlobals.DefaultBackgroundColor)
        self.raceBoard.reparentTo(hidden)
        self.chanceCard.reparentTo(hidden)
        self.chanceCard.text.hide()
        if hasattr(self, 'chanceMarkers'):
            for marker in self.chanceMarkers:
                marker.reparentTo(hidden)
            
        
        taskMgr.remove('lerpCamera')

    
    def setGameReady(self):
        if not (self.hasLocalToon):
            return None
        
        self.notify.debug('setGameReady')
        if DistributedMinigame.setGameReady(self):
            return None
        
        self.resetPositions()
        for i in range(self.numPlayers):
            avId = self.avIdList[i]
            if self.localAvId == avId:
                self.localAvLane = i
            
            avatar = self.getAvatar(avId)
            if avatar:
                avatar.reparentTo(render)
                avatar.setAnimState('neutral', 1)
                self.positionInPlace(avatar, i, 0)
            
        

    
    def setGameStart(self, timestamp):
        if not (self.hasLocalToon):
            return None
        
        self.notify.debug('setGameStart')
        DistributedMinigame.setGameStart(self, timestamp)
        self.gameFSM.request('inputChoice')

    
    def enterOff(self):
        self.notify.debug('enterOff')

    
    def exitOff(self):
        pass

    
    def enterInputChoice(self):
        self.notify.debug('enterInputChoice')
        for button in self.diceButtonList:
            button.show()
        
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.hide()
        if self.timerStartTime != None:
            self.startTimer()
        

    
    def startTimer(self):
        now = globalClock.getFrameTime()
        elapsed = now - self.timerStartTime
        self.timer.posInTopRightCorner()
        self.timer.setTime(RaceGameGlobals.InputTimeout)
        self.timer.countdown(RaceGameGlobals.InputTimeout - elapsed, self.handleChoiceTimeout)
        self.timer.show()

    
    def setTimerStartTime(self, timestamp):
        if not (self.hasLocalToon):
            return None
        
        self.timerStartTime = globalClockDelta.networkToLocalTime(timestamp)
        if self.timer != None:
            self.startTimer()
        

    
    def exitInputChoice(self):
        for button in self.diceButtonList:
            button.hide()
        
        if self.timer != None:
            self.timer.destroy()
            self.timer = None
        
        self.timerStartTime = None
        self.ignore('diceButton')

    
    def handleChoiceTimeout(self):
        self.sendUpdate('setAvatarChoice', [
            0])
        self.gameFSM.request('waitServerChoices')

    
    def handleInputChoice(self, choice):
        self.sendUpdate('setAvatarChoice', [
            choice])
        self.gameFSM.request('waitServerChoices')

    
    def enterWaitServerChoices(self):
        self.notify.debug('enterWaitServerChoices')
        self.waitingChoicesLabel.show()

    
    def exitWaitServerChoices(self):
        self.waitingChoicesLabel.hide()

    
    def localToonWon(self):
        localToonPosition = self.avatarPositions[self.localAvId]
        if localToonPosition >= RaceGameGlobals.NumberToWin:
            self.notify.debug('localToon won')
            return 1
        else:
            return 0

    
    def anyAvatarWon(self):
        for position in self.avatarPositions.values():
            if position >= RaceGameGlobals.NumberToWin:
                self.notify.debug('anyAvatarWon: Somebody won')
                return 1
            
        
        self.notify.debug('anyAvatarWon: Nobody won')
        return 0

    
    def showNumbers(self, task):
        self.notify.debug('showing numbers...')
        self.diceInstanceList = []
        for i in range(len(task.choiceList)):
            avId = self.avIdList[i]
            choice = task.choiceList[i]
            if choice == 0:
                self.diceInstanceList.append(None)
            else:
                diceInstance = self.diceList[choice - 1].copyTo(self.raceBoard)
                self.diceInstanceList.append(diceInstance)
                dicePosition = self.avatarPositions[avId] + 1
                diceInstance.setScale(4.0)
                self.positionInPlace(diceInstance, i, dicePosition)
                diceInstance.setP(-90)
                diceInstance.setZ(0.050000000000000003)
        
        return Task.done

    
    def showMatches(self, task):
        self.notify.debug('showing matches...')
        for i in range(len(task.choiceList)):
            avId = self.avIdList[i]
            choice = task.choiceList[i]
            if choice != 0:
                diceInstance = self.diceInstanceList[i]
                freq = task.choiceList.count(choice)
                if freq == 1:
                    diceInstance.setColor(0.20000000000000001, 1, 0.20000000000000001, 1)
                    if avId == self.localAvId:
                        base.playSfx(self.posBuzzer)
                    
                else:
                    diceInstance.setColor(1, 0.20000000000000001, 0.20000000000000001, 1)
                    if avId == self.localAvId:
                        base.playSfx(self.negBuzzer)
                    
            
        
        return Task.done

    
    def hideNumbers(self, task):
        self.notify.debug('hiding numbers...')
        for dice in self.diceInstanceList:
            if dice:
                dice.removeNode()
            
        
        self.diceInstanceList = []
        return Task.done

    
    def enterMoveAvatars(self, choiceList, positionList, rewardList):
        self.notify.debug('in enterMoveAvatars:')
        tasks = []
        self.avatarPositionsCopy = self.avatarPositions.copy()
        for i in range(0, len(choiceList) / self.numPlayers):
            startIndex = i * self.numPlayers
            endIndex = startIndex + self.numPlayers
            self.choiceList = choiceList[startIndex:endIndex]
            self.positionList = positionList[startIndex:endIndex]
            self.rewardList = rewardList[startIndex:endIndex]
            self.notify.debug('           turn: ' + str(i + 1))
            self.notify.debug('     choiceList: ' + str(self.choiceList))
            self.notify.debug('   positionList: ' + str(self.positionList))
            self.notify.debug('     rewardList: ' + str(self.rewardList))
            longestLerpTime = self.getLongestLerpTime(i > 0)
            self.notify.debug('longestLerpTime: ' + str(longestLerpTime))
            if i == 0:
                snt = Task.Task(self.showNumbers)
                snt.choiceList = self.choiceList
                smt = Task.Task(self.showMatches)
                smt.choiceList = self.choiceList
                tasks += [
                    snt,
                    Task.pause(0.5),
                    smt]
            
            if longestLerpTime > 0.0:
                self.notify.debug('someone moved...')
                mat = Task.Task(self.moveAvatars)
                mat.choiceList = self.choiceList
                mat.positionList = self.positionList
                mat.rewardList = self.rewardList
                mat.name = 'moveAvatars'
                if i == 0:
                    tasks += [
                        Task.pause(0.75),
                        mat,
                        Task.pause(0.75),
                        Task.Task(self.hideNumbers),
                        Task.pause(longestLerpTime - 0.5)]
                else:
                    mat.chance = 1
                    tasks += [
                        mat,
                        Task.pause(longestLerpTime)]
                tasks += self.showChanceRewards()
            else:
                self.notify.debug('no one moved...')
                tasks += [
                    Task.pause(1.0),
                    Task.Task(self.hideNumbers)]
        
        self.notify.debug('task list : ' + str(tasks))
        wdt = Task.Task(self.walkDone)
        wdt.name = 'walk done'
        tasks.append(wdt)
        moveTask = Task.sequence(*tasks)
        taskMgr.add(moveTask, 'moveAvatars')

    
    def walkDone(self, task):
        self.choiceList = []
        self.positionList = []
        if self.anyAvatarWon():
            self.gameFSM.request('winMovie')
        else:
            self.gameFSM.request('inputChoice')
        return Task.done

    
    def getLongestLerpTime(self, afterFirst):
        self.notify.debug('afterFirst: ' + str(afterFirst))
        longestTime = 0.0
        for i in range(len(self.choiceList)):
            freq = self.choiceList.count(self.choiceList[i])
            if afterFirst or freq == 1:
                oldPosition = self.avatarPositionsCopy[self.avIdList[i]]
                newPosition = self.positionList[i]
                self.avatarPositionsCopy[self.avIdList[i]] = newPosition
                squares_walked = abs(newPosition - oldPosition)
                longestTime = max(longestTime, self.getWalkDuration(squares_walked))
            
        
        return longestTime

    
    def showChanceRewards(self):
        tasks = []
        for reward in self.rewardList:
            self.notify.debug('showChanceRewards: reward = ' + str(reward))
            index = self.rewardList.index(reward)
            if reward != -1:
                self.notify.debug('adding tasks!')
                hcc = Task.Task(self.hideChanceMarker)
                hcc.chanceMarkers = self.chanceMarkers
                hcc.index = index
                sct = Task.Task(self.showChanceCard)
                sct.chanceCard = self.chanceCard
                sct.cardSound = self.cardSound
                stt = Task.Task(self.showChanceCardText)
                rewardEntry = RaceGameGlobals.ChanceRewards[reward]
                stt.rewardIdx = reward
                if rewardEntry[0][0] < 0 or rewardEntry[0][1] > 0:
                    stt.sound = self.negBuzzer
                else:
                    stt.sound = self.posBuzzer
                stt.picker = self.avIdList[index]
                stt.chanceCard = self.chanceCard
                rct = Task.Task(self.resetChanceCard)
                rct.chanceCard = self.chanceCard
                task = Task.sequence(hcc, sct, Task.pause(1.0), stt, Task.pause(3.0), rct, Task.pause(0.25))
                task.name = 'show chance card'
                tasks.append(task)
            
        
        return tasks

    
    def showChanceCard(self, task):
        base.playSfx(task.cardSound)
        task.chanceCard.reparentTo(render)
        task.chanceCard.lerpPosHpr(19.620000000000001, 13.41, 13.140000000000001, 270, 0, -85.239999999999995, 1.0, other = camera, task = 'cardLerp')
        return Task.done

    
    def hideChanceMarker(self, task):
        task.chanceMarkers[task.index].reparentTo(hidden)
        return Task.done

    
    def showChanceCardText(self, task):
        self.notify.debug('showing chance reward: ' + str(task.rewardIdx))
        name = self.getAvatar(task.picker).getName()
        rewardEntry = RaceGameGlobals.ChanceRewards[task.rewardIdx]
        cardText = ''
        if rewardEntry[1] != -1:
            rewardstr_fmt = TTLocalizer.RaceGameCardText
            if rewardEntry[2] > 0:
                rewardstr_fmt = TTLocalizer.RaceGameCardTextBeans
            
            cardText = rewardstr_fmt % {
                'name': name,
                'reward': rewardEntry[1] }
        else:
            rewardstr_fmt = TTLocalizer.RaceGameCardTextHi1
            cardText = rewardstr_fmt % {
                'name': name }
        base.playSfx(task.sound)
        task.chanceCard.text.setText(cardText)
        task.chanceCard.text.show()
        return Task.done

    
    def resetChanceCard(self, task):
        task.chanceCard.text.hide()
        task.chanceCard.reparentTo(hidden)
        task.chanceCard.setPosHpr(0, 0, 0, 0, 0, 0)
        return Task.done

    
    def moveCamera(self):
        bestPosIdx = self.avatarPositions.values()[0]
        best_lane = 0
        cur_lane = 0
        for pos in self.avatarPositions.values():
            if pos > bestPosIdx:
                bestPosIdx = pos
                best_lane = cur_lane
            
            cur_lane = cur_lane + 1
        
        bestPosIdx = min(RaceGameGlobals.NumberToWin, bestPosIdx)
        localToonPosition = self.avatarPositions[self.localAvId]
        savedCamPos = camera.getPos()
        savedCamHpr = camera.getHpr()
        pos1_idx = min(RaceGameGlobals.NumberToWin - 4, localToonPosition)
        pos1 = self.posHprArray[self.localAvLane][pos1_idx]
        bestPosLookAtIdx = bestPosIdx + 1
        localToonLookAtIdx = localToonPosition + 4
        if localToonLookAtIdx >= bestPosLookAtIdx:
            pos2_idx = localToonLookAtIdx
            pos2_idx = min(RaceGameGlobals.NumberToWin, pos2_idx)
            pos2 = self.posHprArray[self.localAvLane][pos2_idx]
        else:
            pos2_idx = bestPosLookAtIdx
            pos2_idx = min(RaceGameGlobals.NumberToWin, pos2_idx)
            pos2 = self.posHprArray[best_lane][pos2_idx]
        posDeltaVecX = pos2[0] - pos1[0]
        posDeltaVecY = pos2[1] - pos1[1]
        DistanceMultiplier = 0.80000000000000004
        camposX = pos2[0] + DistanceMultiplier * posDeltaVecX
        camposY = pos2[1] + DistanceMultiplier * posDeltaVecY
        race_fraction = bestPosIdx / float(RaceGameGlobals.NumberToWin)
        CamHeight = 10.0 * race_fraction + (1.0 - race_fraction) * 22.0
        CamPos = Vec3(camposX, camposY, pos2[2] + CamHeight)
        camera.setPos(CamPos)
        camera_lookat_idx = min(RaceGameGlobals.NumberToWin - 6, localToonPosition)
        posLookAt = self.posHprArray[self.localAvLane][camera_lookat_idx]
        camera.lookAt(posLookAt[0], posLookAt[1], posLookAt[2])
        CamHpr = camera.getHpr()
        camera.setPos(savedCamPos)
        camera.setHpr(savedCamHpr)
        camera.lerpPosHpr(CamPos[0], CamPos[1], CamPos[2], CamHpr[0], CamHpr[1], CamHpr[2], 0.75, task = 'lerpCamera')

    
    def getWalkDuration(self, squares_walked):
        walkDuration = abs(squares_walked / 1.2)
        if squares_walked > 4:
            walkDuration = walkDuration * 0.29999999999999999
        
        return walkDuration

    
    def moveAvatars(self, task):
        self.notify.debug('In moveAvatars: ')
        self.notify.debug('    choiceList: ' + str(task.choiceList))
        self.notify.debug('  positionList: ' + str(task.positionList))
        self.notify.debug('  rewardList: ' + str(task.rewardList))
        for i in range(len(self.choiceList)):
            avId = self.avIdList[i]
            choice = task.choiceList[i]
            position = task.positionList[i]
            chance = max(0, hasattr(task, 'chance'))
            if choice != 0:
                oldPosition = self.avatarPositions[avId]
                self.avatarPositions[avId] = position
                self.moveCamera()
                if not chance and task.choiceList.count(choice) != 1:
                    self.notify.debug('duplicate choice!')
                else:
                    avatar = self.getAvatar(avId)
                    if avatar:
                        squares_walked = abs(position - oldPosition)
                        if squares_walked > 4:
                            self.notify.debug('running')
                            avatar.setPlayRate(1.0, 'run')
                            self.runInPlace(avatar, i, oldPosition, position, self.getWalkDuration(squares_walked))
                        elif choice > 0:
                            self.notify.debug('walking forwards')
                            avatar.setPlayRate(1.0, 'walk')
                        else:
                            self.notify.debug('walking backwards')
                            avatar.setPlayRate(-1.0, 'walk')
                        self.walkInPlace(avatar, i, position, self.getWalkDuration(squares_walked))
                    
            
        
        return Task.done

    
    def exitMoveAvatars(self):
        self.notify.debug('In exitMoveAvatars: removing hooks')
        taskMgr.remove('moveAvatars')
        return None

    
    def gameOverCallback(self, task):
        self.gameOver()
        return Task.done

    
    def enterWinMovie(self):
        self.notify.debug('enterWinMovie')
        if self.localToonWon():
            base.playSfx(self.winSting)
        else:
            base.playSfx(self.loseSting)
        for avId in self.avIdList:
            avPosition = self.avatarPositions[avId]
            if avPosition >= RaceGameGlobals.NumberToWin:
                avatar = self.getAvatar(avId)
                if avatar:
                    lane = str(self.avIdList.index(avId))
                    taskMgr.remove('runAvatar-' + lane)
                    taskMgr.remove('walkAvatar-' + lane)
                    avatar.setAnimState('jump', 1.0)
                
            
        
        taskMgr.doMethodLater(4.0, self.gameOverCallback, 'playMovie')

    
    def exitWinMovie(self):
        taskMgr.remove('playMovie')
        self.winSting.stop()
        self.loseSting.stop()

    
    def enterCleanup(self):
        self.notify.debug('enterCleanup')

    
    def exitCleanup(self):
        pass

    
    def positionInPlace(self, avatar, lane, place):
        place = min(place, len(self.posHprArray[lane]) - 1)
        posH = self.posHprArray[lane][place]
        avatar.setPosHpr(self.raceBoard, posH[0], posH[1], posH[2], posH[3], 0, 0)

    
    def walkInPlace(self, avatar, lane, place, time):
        place = min(place, len(self.posHprArray[lane]) - 1)
        posH = self.posHprArray[lane][place]
        
        def startWalk(task):
            task.avatar.setAnimState('walk', 1)
            return Task.done

        startWalkTask = Task.Task(startWalk, 'startWalk-' + str(lane))
        startWalkTask.avatar = avatar
        
        def stopWalk(task, raceBoard = self.raceBoard, posH = posH):
            task.avatar.setAnimState('neutral', 1)
            if raceBoard.isEmpty():
                task.avatar.setPosHpr(0, 0, 0, 0, 0, 0)
            else:
                task.avatar.setPosHpr(raceBoard, posH[0], posH[1], posH[2], posH[3], 0, 0)
            return Task.done

        stopWalkTask = Task.Task(stopWalk, 'stopWalk-' + str(lane))
        stopWalkTask.avatar = avatar
        walkTask = Task.sequence(startWalkTask, avatar.lerpPosHpr(posH[0], posH[1], posH[2], posH[3], 0, 0, time, other = self.raceBoard), stopWalkTask)
        walkTask.avatar = avatar
        walkTask.posH = posH
        walkTask.raceBoard = self.raceBoard
        taskMgr.add(walkTask, 'walkAvatar-' + str(lane))

    
    def runInPlace(self, avatar, lane, currentPlace, newPlace, time):
        place = min(newPlace, len(self.posHprArray[lane]) - 1)
        step = (place - currentPlace) / 3
        pos1 = self.posHprArray[lane][currentPlace + step]
        pos2 = self.posHprArray[lane][currentPlace + 2 * step]
        pos3 = self.posHprArray[lane][place]
        
        def startRun(task):
            task.avatar.setAnimState('run', 1)
            return Task.done

        startRunTask = Task.Task(startRun, 'startRun-' + str(lane))
        startRunTask.avatar = avatar
        
        def stopRun(task, raceBoard = self.raceBoard, pos3 = pos3):
            task.avatar.setAnimState('neutral', 1)
            task.avatar.setPosHpr(raceBoard, pos3[0], pos3[1], pos3[2], pos3[3], 0, 0)
            return Task.done

        stopRunTask = Task.Task(startRun, 'stopRun-' + str(lane))
        stopRunTask.avatar = avatar
        runTask = Task.sequence(startRunTask, avatar.lerpPosHpr(pos1[0], pos1[1], pos1[2], pos1[3], 0, 0, time / 3.0, other = self.raceBoard), avatar.lerpPosHpr(pos2[0], pos2[1], pos2[2], pos2[3], 0, 0, time / 3.0, other = self.raceBoard), avatar.lerpPosHpr(pos3[0], pos3[1], pos3[2], pos3[3], 0, 0, time / 3.0, other = self.raceBoard), stopRunTask)
        runTask.avatar = avatar
        runTask.pos3 = pos3
        runTask.raceBoard = self.raceBoard
        taskMgr.add(runTask, 'runAvatar-' + str(lane))

    
    def setAvatarChoice(self, choice):
        self.notify.error('setAvatarChoice should not be called on the client')

    
    def setAvatarChose(self, avId):
        if not (self.hasLocalToon):
            return None
        
        self.notify.debug('setAvatarChose: avatar: ' + str(avId) + ' choose a number')

    
    def setChancePositions(self, positions):
        if not (self.hasLocalToon):
            return None
        
        row = 0
        for pos in positions:
            marker = self.chanceMarker.copyTo(render)
            posHpr = self.posHprArray[row][pos]
            marker.setPosHpr(self.raceBoard, posHpr[0], posHpr[1], posHpr[2], posHpr[3] + 180, 0, 0.025000000000000001)
            marker.setScale(0.69999999999999996)
            self.chanceMarkers.append(marker)
            row += 1
        

    
    def setServerChoices(self, choices, positions, rewards):
        if not (self.hasLocalToon):
            return None
        
        for i in range(len(positions)):
            if positions[i] > RaceGameGlobals.NumberToWin:
                positions[i] = RaceGameGlobals.NumberToWin
            
            if positions[i] < 0:
                positions[i] = 0
            
        
        self.notify.debug('setServerChoices: %s positions: %s rewards: %s ' % (choices, positions, rewards))
        self.gameFSM.request('moveAvatars', [
            choices,
            positions,
            rewards])

    
    def resetPositions(self):
        for avId in self.avIdList:
            self.avatarPositions[avId] = 0
        


