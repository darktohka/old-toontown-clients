# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from DistributedNPCToonBase import *
from toontown.quest import QuestParser
from toontown.quest import QuestChoiceGui
from toontown.quest import TrackChoiceGui
from toontown.toonbase import TTLocalizer
ChoiceTimeout = 20

class DistributedNPCToon(DistributedNPCToonBase):
    
    def __init__(self, cr):
        DistributedNPCToonBase.__init__(self, cr)
        self.curQuestMovie = None
        self.questChoiceGui = None
        self.trackChoiceGui = None

    
    def disable(self):
        self.cleanupMovie()
        DistributedNPCToonBase.disable(self)

    
    def cleanupMovie(self):
        self.clearChat()
        self.ignore('chooseQuest')
        if self.questChoiceGui:
            self.questChoiceGui.destroy()
            self.questChoiceGui = None
        
        self.ignore(self.uniqueName('doneChatPage'))
        if self.curQuestMovie:
            self.curQuestMovie.timeout(fFinish = 1)
            self.curQuestMovie.cleanup()
            self.curQuestMovie = None
        
        if self.trackChoiceGui:
            self.trackChoiceGui.destroy()
            self.trackChoiceGui = None
        

    
    def handleCollisionSphereEnter(self, collEntry):
        base.cr.playGame.getPlace().fsm.request('quest', [
            self])
        self.sendUpdate('avatarEnter', [])

    
    def finishMovie(self, av, isLocalToon, elapsedTime):
        self.cleanupMovie()
        av.startLookAround()
        self.startLookAround()
        self.detectAvatars()
        self.clearMat()
        if isLocalToon:
            taskMgr.remove(self.uniqueName('lerpCamera'))
            base.localAvatar.posCamera(0, 0)
            base.cr.playGame.getPlace().setState('walk')
            self.sendUpdate('setMovieDone', [])
        

    
    def setupCamera(self, mode):
        camera.wrtReparentTo(render)
        if mode == NPCToons.QUEST_MOVIE_QUEST_CHOICE or mode == NPCToons.QUEST_MOVIE_TRACK_CHOICE:
            camera.lerpPosHpr(5, 9, self.getHeight() - 0.5, 155, -2, 0, 1, other = self, blendType = 'easeOut', task = self.uniqueName('lerpCamera'))
        else:
            camera.lerpPosHpr(-5, 9, self.getHeight() - 0.5, -150, -2, 0, 1, other = self, blendType = 'easeOut', task = self.uniqueName('lerpCamera'))

    
    def setMovie(self, mode, npcId, avId, quests, timestamp):
        timeStamp = ClockDelta.globalClockDelta.localElapsedTime(timestamp)
        isLocalToon = avId == base.localAvatar.doId
        if mode == NPCToons.QUEST_MOVIE_CLEAR:
            self.cleanupMovie()
            return None
        
        if mode == NPCToons.QUEST_MOVIE_TIMEOUT:
            self.cleanupMovie()
            if isLocalToon:
                self.freeAvatar()
            
            self.setPageNumber(0, -1)
            self.clearChat()
            self.startLookAround()
            self.detectAvatars()
            return None
        
        av = base.cr.doId2do.get(avId)
        if av is None:
            self.notify.warning('Avatar %d not found in doId' % avId)
            return None
        
        if mode == NPCToons.QUEST_MOVIE_REJECT:
            rejectString = Quests.chooseQuestDialogReject()
            rejectString = Quests.fillInQuestNames(rejectString, avName = av.name)
            self.setChatAbsolute(rejectString, CFSpeech | CFTimeout)
            if isLocalToon:
                base.localAvatar.posCamera(0, 0)
                base.cr.playGame.getPlace().setState('walk')
            
            return None
        
        if mode == NPCToons.QUEST_MOVIE_TIER_NOT_DONE:
            rejectString = Quests.chooseQuestDialogTierNotDone()
            rejectString = Quests.fillInQuestNames(rejectString, avName = av.name)
            self.setChatAbsolute(rejectString, CFSpeech | CFTimeout)
            if isLocalToon:
                base.localAvatar.posCamera(0, 0)
                base.cr.playGame.getPlace().setState('walk')
            
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
            fullString = TTLocalizer.QuestMovieQuestChoiceCancel
        elif mode == NPCToons.QUEST_MOVIE_TRACK_CHOICE_CANCEL:
            fullString = TTLocalizer.QuestMovieTrackChoiceCancel
        elif mode == NPCToons.QUEST_MOVIE_INCOMPLETE:
            (questId, completeStatus, toNpcId) = quests
            scriptId = 'quest_incomplete_' + str(questId)
            if QuestParser.questDefined(scriptId):
                if self.curQuestMovie:
                    self.curQuestMovie.timeout()
                    self.curQuestMovie.cleanup()
                    self.curQuestMovie = None
                
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
                if self.curQuestMovie:
                    self.curQuestMovie.timeout()
                    self.curQuestMovie.cleanup()
                    self.curQuestMovie = None
                
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
            
            self.setChatAbsolute(TTLocalizer.QuestMovieQuestChoice, CFSpeech)
            if isLocalToon:
                self.acceptOnce('chooseQuest', self.sendChooseQuest)
                self.questChoiceGui = QuestChoiceGui.QuestChoiceGui()
                self.questChoiceGui.setQuests(quests, npcId, ChoiceTimeout)
            
            return None
        elif mode == NPCToons.QUEST_MOVIE_TRACK_CHOICE:
            if isLocalToon:
                self.setupCamera(mode)
            
            tracks = quests
            self.setChatAbsolute(TTLocalizer.QuestMovieTrackChoice, CFSpeech)
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


