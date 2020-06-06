# File: D (Python 2.2)

from ShowBaseGlobal import *
from DistributedNPCToonBase import *
import QuestParser
import QuestChoiceGui
import TrackChoiceGui
import Localizer
ChoiceTimeout = 20

class DistributedNPCToon(DistributedNPCToonBase):
    
    def __init__(self, cr):
        DistributedNPCToonBase.__init__(self, cr)
        self.curQuestMovie = None
        self.questChoiceGui = None

    
    def disable(self):
        self.ignore('chooseQuest')
        if self.questChoiceGui:
            self.questChoiceGui.destroy()
            self.questChoiceGui = None
        
        if self.curQuestMovie:
            self.curQuestMovie.timeout(fFinish = 1)
            self.curQuestMovie.cleanup()
            self.curQuestMovie = None
        
        self.ignore(self.uniqueName('doneChatPage'))
        DistributedNPCToonBase.disable(self)

    
    def handleCollisionSphereEnter(self, collEntry):
        self.notify.info('Entering collision sphere...')
        toonbase.tcr.playGame.getPlace().fsm.request('quest', [
            self])
        self.sendUpdate('avatarEnter', [])

    
    def finishMovie(self, av, isLocalToon, elapsedTime):
        if self.curQuestMovie:
            self.curQuestMovie.cleanup()
            self.curQuestMovie = None
        
        if isLocalToon:
            taskMgr.remove(self.uniqueName('lerpCamera'))
            toonbase.localToon.posCamera(0, 0)
            toonbase.tcr.playGame.getPlace().setState('walk')
            self.sendUpdate('setMovieDone', [])
        
        if self.questChoiceGui:
            self.questChoiceGui.destroy()
            self.questChoiceGui = None
        
        av.startLookAround()
        self.startLookAround()
        self.detectAvatars()
        self.clearMat()

    
    def setupCamera(self, mode):
        camera.wrtReparentTo(render)
        if mode == NPCToons.QUEST_MOVIE_QUEST_CHOICE or mode == NPCToons.QUEST_MOVIE_TRACK_CHOICE:
            camera.lerpPosHpr(5, 9, self.getHeight() - 0.5, 155, -2, 0, 1, other = self, blendType = 'easeOut', task = self.uniqueName('lerpCamera'))
        else:
            camera.lerpPosHpr(-5, 9, self.getHeight() - 0.5, -150, -2, 0, 1, other = self, blendType = 'easeOut', task = self.uniqueName('lerpCamera'))

    
    def setMovie(self, mode, npcId, avId, quests, timestamp):
        timeStamp = ClockDelta.globalClockDelta.localElapsedTime(timestamp)
        isLocalToon = avId == toonbase.localToon.doId
        self.notify.info('setMovie: %s %s %s %s %s %s' % (mode, npcId, avId, quests, timeStamp, isLocalToon))
        if mode == NPCToons.QUEST_MOVIE_CLEAR:
            self.notify.info('setMovie: movie cleared')
            return None
        
        if mode == NPCToons.QUEST_MOVIE_TIMEOUT:
            self.notify.info('setMovie: movie timeout')
            self.ignore(self.uniqueName('doneChatPage'))
            self.ignore('chooseQuest')
            if self.curQuestMovie:
                self.curQuestMovie.timeout()
                self.curQuestMovie.cleanup()
                self.curQuestMovie = None
            
            if self.questChoiceGui:
                self.questChoiceGui.destroy()
                self.questChoiceGui = None
            
            if isLocalToon:
                self.freeAvatar()
            
            self.setPageNumber(0, -1)
            self.clearChat()
            self.startLookAround()
            self.detectAvatars()
            return None
        
        av = toonbase.tcr.doId2do.get(avId)
        if av is None:
            self.notify.warning('Avatar %d not found in doId' % avId)
            return None
        
        if mode == NPCToons.QUEST_MOVIE_REJECT:
            rejectString = Quests.chooseQuestDialogReject()
            rejectString = Quests.fillInQuestNames(rejectString, avName = av.name)
            self.setChatAbsolute(rejectString, CFSpeech | CFTimeout)
            if isLocalToon:
                toonbase.localToon.posCamera(0, 0)
                toonbase.tcr.playGame.getPlace().setState('walk')
            
            return None
        
        if mode == NPCToons.QUEST_MOVIE_TIER_NOT_DONE:
            rejectString = Quests.chooseQuestDialogTierNotDone()
            rejectString = Quests.fillInQuestNames(rejectString, avName = av.name)
            self.setChatAbsolute(rejectString, CFSpeech | CFTimeout)
            if isLocalToon:
                toonbase.localToon.posCamera(0, 0)
                toonbase.tcr.playGame.getPlace().setState('walk')
            
            return None
        
        self.setupAvatars(av)
        fullString = ''
        toNpcId = None
        if mode == NPCToons.QUEST_MOVIE_COMPLETE:
            (questId, rewardId, toNpcId) = quests
            scriptId = 'quest_complete_' + str(questId)
            if QuestParser.questDefined(scriptId):
                self.curQuestMovie = QuestParser.NPCMoviePlayer(scriptId, av, self)
                self.curQuestMovie.play()
                return None
            
            if isLocalToon:
                self.setupCamera(mode)
            
            greetingString = Quests.chooseQuestDialog(questId, Quests.GREETING)
            if greetingString:
                fullString += greetingString + '\x7'
            
            fullString += Quests.chooseQuestDialog(questId, Quests.COMPLETE) + '\x7'
            if rewardId:
                fullString += Quests.getReward(rewardId).getString()
            
            leavingString = Quests.chooseQuestDialog(questId, Quests.LEAVING)
            if leavingString:
                fullString += '\x7' + leavingString
            
        elif mode == NPCToons.QUEST_MOVIE_QUEST_CHOICE_CANCEL:
            fullString = Localizer.QuestMovieQuestChoiceCancel
        elif mode == NPCToons.QUEST_MOVIE_TRACK_CHOICE_CANCEL:
            fullString = Localizer.QuestMovieTrackChoiceCancel
        elif mode == NPCToons.QUEST_MOVIE_INCOMPLETE:
            (questId, completeStatus, toNpcId) = quests
            scriptId = 'quest_incomplete_' + str(questId)
            if QuestParser.questDefined(scriptId):
                self.curQuestMovie = QuestParser.NPCMoviePlayer(scriptId, av, self)
                self.curQuestMovie.play()
                return None
            
            if isLocalToon:
                self.setupCamera(mode)
            
            greetingString = Quests.chooseQuestDialog(questId, Quests.GREETING)
            if greetingString:
                fullString += greetingString + '\x7'
            
            fullString += Quests.chooseQuestDialog(questId, completeStatus)
            leavingString = Quests.chooseQuestDialog(questId, Quests.LEAVING)
            if leavingString:
                fullString += '\x7' + leavingString
            
        elif mode == NPCToons.QUEST_MOVIE_ASSIGN:
            (questId, rewardId, toNpcId) = quests
            scriptId = 'quest_assign_' + str(questId)
            if QuestParser.questDefined(scriptId):
                self.curQuestMovie = QuestParser.NPCMoviePlayer(scriptId, av, self)
                self.curQuestMovie.play()
                return None
            
            if isLocalToon:
                self.setupCamera(mode)
            
            fullString += Quests.chooseQuestDialog(questId, Quests.QUEST)
            leavingString = Quests.chooseQuestDialog(questId, Quests.LEAVING)
            if leavingString:
                fullString += '\x7' + leavingString
            
        elif mode == NPCToons.QUEST_MOVIE_QUEST_CHOICE:
            if isLocalToon:
                self.setupCamera(mode)
            
            self.notify.debug('QUEST_MOVIE_QUEST_CHOICE: %s' % quests)
            self.setChatAbsolute(Localizer.QuestMovieQuestChoice, CFSpeech)
            if isLocalToon:
                self.acceptOnce('chooseQuest', self.sendChooseQuest)
                self.questChoiceGui = QuestChoiceGui.QuestChoiceGui()
                self.questChoiceGui.setQuests(quests, npcId, ChoiceTimeout)
            
            return None
        elif mode == NPCToons.QUEST_MOVIE_TRACK_CHOICE:
            if isLocalToon:
                self.setupCamera(mode)
            
            tracks = quests
            self.notify.debug('QUEST_MOVIE_TRACK_CHOICE: %s' % tracks)
            self.setChatAbsolute(Localizer.QuestMovieTrackChoice, CFSpeech)
            if isLocalToon:
                self.acceptOnce('chooseTrack', self.sendChooseTrack)
                self.trackChoiceGui = TrackChoiceGui.TrackChoiceGui(tracks, ChoiceTimeout)
            
            return None
        
        fullString = Quests.fillInQuestNames(fullString, avName = av.name, fromNpcId = npcId, toNpcId = toNpcId)
        self.acceptOnce(self.uniqueName('doneChatPage'), self.finishMovie, extraArgs = [
            av,
            isLocalToon])
        self.setPageChat(avId, 0, fullString, 1)

    
    def sendChooseQuest(self, questId):
        if self.questChoiceGui:
            self.questChoiceGui.destroy()
            self.questChoiceGui = None
        
        self.sendUpdate('chooseQuest', [
            questId])

    
    def sendChooseTrack(self, trackId):
        if self.trackChoiceGui:
            self.trackChoiceGui.destroy()
            self.trackChoiceGui = None
        
        self.sendUpdate('chooseTrack', [
            trackId])


