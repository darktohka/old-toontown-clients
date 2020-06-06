# File: M (Python 2.2)

from ToontownBattleGlobals import *
from BattleBase import *
from IntervalGlobal import *
import PandaObject
import MovieSOS
import MovieHeal
import MovieTrap
import MovieLure
import MovieSound
import MovieThrow
import MovieSquirt
import MovieDrop
import MovieSuitAttacks
import MovieToonVictory
import PlayByPlayText
import BattleParticles
import DelayDelete
from SuitBattleGlobals import *
import DirectNotifyGlobal
import RewardPanel
import whrandom
import MovieUtil
import Toon
import ToontownDialog
import copy
import Localizer
camPos = Point3(14, 0, 10)
camHpr = Vec3(89, -30, 0)
randomBattleTimestamp = base.config.GetBool('random-battle-timestamp', 0)

class Movie(PandaObject.PandaObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('Movie')
    
    def __init__(self, battle):
        self.battle = battle
        self.track = None
        self.rewardPanel = None
        self.playByPlayText = PlayByPlayText.PlayByPlayText()
        self.playByPlayText.hide()
        self.renderProps = []
        self.hasBeenReset = 0
        self.reset()
        self.rewardHasBeenReset = 0
        self.resetReward()

    
    def cleanup(self):
        self.reset()
        self.resetReward()
        self.battle = None
        if self.playByPlayText != None:
            self.playByPlayText.cleanup()
        
        self.playByPlayText = None
        if self.rewardPanel != None:
            self.rewardPanel.cleanup()
        
        self.rewardPanel = None

    
    def needRestoreColor(self):
        self.restoreColor = 1

    
    def clearRestoreColor(self):
        self.restoreColor = 0

    
    def needRestoreHips(self):
        self.restoreHips = 1

    
    def clearRestoreHips(self):
        self.restoreHips = 0

    
    def needRestoreHeadScale(self):
        self.restoreHeadScale = 1

    
    def clearRestoreHeadScale(self):
        self.restoreHeadScale = 0

    
    def needRestoreToonScale(self):
        self.restoreToonScale = 1

    
    def clearRestoreToonScale(self):
        self.restoreToonScale = 0

    
    def needRestoreParticleEffect(self, effect):
        self.specialParticleEffects.append(effect)

    
    def clearRestoreParticleEffect(self, effect):
        if self.specialParticleEffects.count(effect) > 0:
            self.specialParticleEffects.remove(effect)
        

    
    def needRestoreRenderProp(self, prop):
        self.renderProps.append(prop)

    
    def clearRenderProp(self, prop):
        if self.renderProps.count(prop) > 0:
            self.renderProps.remove(prop)
        

    
    def restore(self):
        return None
        for toon in self.battle.activeToons:
            toon.loop('neutral')
            (origPos, origHpr) = self.battle.getActorPosHpr(toon)
            toon.setPosHpr(self.battle, origPos, origHpr)
            hands = toon.getRightHands()[:]
            hands += toon.getLeftHands()
            for hand in hands:
                props = hand.getChildrenAsList()
                for prop in props:
                    if prop.getName() != 'book':
                        MovieUtil.removeProp(prop)
                    
                
            
            if self.restoreColor == 1:
                headParts = toon.getHeadParts()
                torsoParts = toon.getTorsoParts()
                legsParts = toon.getLegsParts()
                partsList = [
                    headParts,
                    torsoParts,
                    legsParts]
                for parts in partsList:
                    for partNum in range(0, parts.getNumPaths()):
                        nextPart = parts.getPath(partNum)
                        nextPart.clearColorScale()
                        nextPart.clearTransparency()
                    
                
            
            if self.restoreHips == 1:
                parts = toon.getHipsParts()
                for partNum in range(0, parts.getNumPaths()):
                    nextPart = parts.getPath(partNum)
                    props = nextPart.getChildrenAsList()
                    for prop in props:
                        if prop.getName() == 'redtape-tube.egg':
                            MovieUtil.removeProp(prop)
                        
                    
                
            
            if self.restoreHeadScale == 1:
                headScale = Toon.toonHeadScales[toon.style.getAnimal()]
                for lod in toon.getLODNames():
                    toon.getPart('head', lod).setScale(headScale)
                
            
            if self.restoreToonScale == 1:
                toon.setScale(1)
            
            headParts = toon.getHeadParts()
            for partNum in range(0, headParts.getNumPaths()):
                part = headParts.getPath(partNum)
                part.setHpr(0, 0, 0)
                part.setPos(0, 0, 0)
            
            arms = toon.findAllMatches('**/arms')
            sleeves = toon.findAllMatches('**/sleeves')
            hands = toon.findAllMatches('**/hands')
            for partNum in range(0, arms.getNumPaths()):
                armPart = arms.getPath(partNum)
                sleevePart = sleeves.getPath(partNum)
                handsPart = hands.getPath(partNum)
                armPart.setHpr(0, 0, 0)
                sleevePart.setHpr(0, 0, 0)
                handsPart.setHpr(0, 0, 0)
            
        
        for suit in self.battle.activeSuits:
            if suit._Actor__animControlDict != None:
                suit.loop('neutral')
                suit.battleTrapIsFresh = 0
                (origPos, origHpr) = self.battle.getActorPosHpr(suit)
                suit.setPosHpr(self.battle, origPos, origHpr)
                hands = [
                    suit.getRightHand(),
                    suit.getLeftHand()]
                for hand in hands:
                    props = hand.getChildrenAsList()
                    for prop in props:
                        MovieUtil.removeProp(prop)
                    
                
            
        
        for effect in self.specialParticleEffects:
            if effect != None:
                effect.cleanup()
            
        
        self.specialParticleEffects = []
        for prop in self.renderProps:
            MovieUtil.removeProp(prop)
        
        self.renderProps = []

    
    def reset(self, finish = 0):
        if self.hasBeenReset == 1:
            return None
        
        self.hasBeenReset = 1
        self.stop()
        self.track = None
        if finish == 1:
            self.restore()
        
        self.toonAttackDicts = []
        self.suitAttackDicts = []
        self.restoreColor = 0
        self.restoreHips = 0
        self.restoreHeadScale = 0
        self.restoreToonScale = 0
        self.specialParticleEffects = []
        for prop in self.renderProps:
            MovieUtil.removeProp(prop)
        
        self.renderProps = []

    
    def resetReward(self, finish = 0):
        if self.rewardHasBeenReset == 1:
            return None
        
        self.rewardHasBeenReset = 1
        self.stop()
        self.track = None
        if finish == 1:
            self.restore()
        
        self.toonRewardDicts = []
        if self.rewardPanel != None:
            self.rewardPanel.destroy()
        
        self.rewardPanel = None

    
    def play(self, ts, callback):
        self.hasBeenReset = 0
        plist = []
        camlist = []
        if whrandom.random() > 0.5:
            MovieUtil.shotDirection = 'left'
        else:
            MovieUtil.shotDirection = 'right'
        for s in self.battle.activeSuits:
            s.battleTrapIsFresh = 0
        
        (tattacks, tcam) = self._Movie__doToonAttacks()
        if tattacks:
            plist.append(tattacks)
            camlist.append(tcam)
        
        (sattacks, scam) = self._Movie__doSuitAttacks()
        if sattacks:
            plist.append(sattacks)
            camlist.append(scam)
        
        plist.append(FunctionInterval(callback))
        self.track = Sequence(plist, name = 'movie-track-%d' % self.battle.doId)
        if self.battle.localToonPendingOrActive():
            self.track = Parallel(self.track, Sequence(camlist), name = 'movie-track-with-cam-%d' % self.battle.doId)
        
        if randomBattleTimestamp == 1:
            randNum = whrandom.randint(0, 99)
            dur = self.track.getDuration()
            ts = (float(randNum) / 100.0) * dur
        
        self.track.delayDeletes = []
        for suit in self.battle.suits:
            self.track.delayDeletes.append(DelayDelete.DelayDelete(suit))
        
        for toon in self.battle.toons:
            self.track.delayDeletes.append(DelayDelete.DelayDelete(toon))
        
        self.track.start(ts)
        return None

    
    def playReward(self, ts, name, callback):
        self.rewardHasBeenReset = 0
        plist = []
        camlist = []
        self.rewardPanel = RewardPanel.RewardPanel(name)
        self.rewardPanel.hide()
        (victory, camVictory) = MovieToonVictory.doToonVictory(self.battle.localToonActive(), self.battle.activeToons, self.toonRewardDicts, self.deathList, self.rewardPanel)
        if victory:
            plist.append(victory)
            camlist.append(camVictory)
        
        plist.append(FunctionInterval(callback))
        self.track = Sequence(plist, name = 'movie-reward-track-%d' % self.battle.doId)
        if self.battle.localToonActive():
            self.track = Parallel(self.track, Sequence(camlist), name = 'movie-reward-track-with-cam-%d' % self.battle.doId)
        
        self.track.delayDeletes = []
        for t in self.battle.activeToons:
            self.track.delayDeletes.append(DelayDelete.DelayDelete(t))
        
        self.track.start(ts)
        return None

    
    def playTutorialReward(self, ts, name, callback):
        self.rewardHasBeenReset = 0
        self.rewardPanel = RewardPanel.RewardPanel(name)
        self.rewardCallback = callback
        camera.setPosHpr(0, 8, toonbase.localToon.getHeight() * 0.66000000000000003, 179, 15, 0)
        self.playTutorialReward_1()

    
    def playTutorialReward_1(self):
        self.tutRewardDialog_1 = ToontownDialog.ToontownDialog(text = Localizer.MovieTutorialReward1, command = self.playTutorialReward_2, style = ToontownDialog.Acknowledge, fadeScreen = None, pos = (0.65000000000000002, 0, 0.5), scale = 0.80000000000000004)
        self.tutRewardDialog_1.hide()
        trackList = [
            Func(self.rewardPanel.initGagFrame, toonbase.localToon, [
                0,
                0,
                0,
                0,
                0,
                0,
                0])]
        trackList += self.rewardPanel.getTrackIntervalList(toonbase.localToon, THROW_TRACK, 0, 1)
        trackList += [
            Func(self.tutRewardDialog_1.show)]
        self.track = Track(trackList, name = 'tutorial-reward-1')
        self.track.start()
        return None

    
    def playTutorialReward_2(self, value):
        self.tutRewardDialog_1.cleanup()
        self.tutRewardDialog_2 = ToontownDialog.ToontownDialog(text = Localizer.MovieTutorialReward2, command = self.playTutorialReward_3, style = ToontownDialog.Acknowledge, fadeScreen = None, pos = (0.65000000000000002, 0, 0.5), scale = 0.80000000000000004)
        self.tutRewardDialog_2.hide()
        trackList = [
            Wait(1.0)]
        trackList += self.rewardPanel.getTrackIntervalList(toonbase.localToon, SQUIRT_TRACK, 0, 1)
        trackList += [
            Func(self.tutRewardDialog_2.show)]
        self.track = Track(trackList, name = 'tutorial-reward-2')
        self.track.start()
        return None

    
    def playTutorialReward_3(self, value):
        self.tutRewardDialog_2.cleanup()
        import Toon
        import AvatarDNA
        
        def doneChat1(page, elapsed = 0):
            self.track2.start()

        
        def doneChat2(elapsed):
            self.track2.pause()
            self.track3.start()

        
        def uniqueName(hook):
            return 'TutorialTom-' + hook

        self.tutorialTom = Toon.Toon()
        dna = AvatarDNA.AvatarDNA()
        dnaList = ('dls', 'ms', 'm', 'm', 7, 0, 7, 7, 2, 6, 2, 6, 2, 16)
        dna.newToonFromProperties(*dnaList)
        self.tutorialTom.setDNA(dna)
        self.tutorialTom.setName(Localizer.NPCToonNames[20000])
        self.tutorialTom.uniqueName = uniqueName
        questList = self.rewardPanel.getQuestIntervalList(toonbase.localToon, [
            0,
            1])
        if questList:
            self.track1 = Sequence(Wait(1.0), Func(self.rewardPanel.initQuestFrame, toonbase.localToon, copy.deepcopy(toonbase.localToon.quests)), Wait(1.0), Sequence(questList), Wait(1.0), Func(self.rewardPanel.hide), Func(camera.setPosHpr, render, 34, 19.879999999999999, 3.48, 270.0, 60.0, 297.63999999999999), Func(toonbase.localToon.animFSM.request, 'neutral'), Func(toonbase.localToon.setPosHpr, 40.310000000000002, 22.0, -0.46999999999999997, 150.0, 360.0, 0.0), Wait(0.5), Func(self.tutorialTom.reparentTo, render), Func(self.tutorialTom.show), Func(self.tutorialTom.setPosHpr, 40.289999999999999, 17.899999999999999, -0.46999999999999997, 11.31, 0.0, 0.070000000000000007), Func(self.tutorialTom.animFSM.request, 'TeleportIn'), Wait(1.5169999999999999), Func(self.tutorialTom.animFSM.request, 'neutral'), Func(self.acceptOnce, self.tutorialTom.uniqueName('doneChatPage'), doneChat1), Func(self.tutorialTom.addActive), Func(self.tutorialTom.setLocalPageChat, Localizer.MovieTutorialReward3, None), name = 'tutorial-reward-3a')
            self.track2 = Sequence(Func(self.acceptOnce, self.tutorialTom.uniqueName('doneChatPage'), doneChat2), Func(self.tutorialTom.setLocalPageChat, Localizer.MovieTutorialReward4, 1), Func(self.tutorialTom.setPlayRate, 1.5, 'right-hand-start'), Func(self.tutorialTom.play, 'right-hand-start'), Wait(self.tutorialTom.getDuration('right-hand-start') / 1.5), Func(self.tutorialTom.loop, 'right-hand'), name = 'tutorial-reward-3b')
            self.track3 = Parallel(Sequence(Func(self.tutorialTom.setPlayRate, -1.8, 'right-hand-start'), Func(self.tutorialTom.play, 'right-hand-start'), Wait(self.tutorialTom.getDuration('right-hand-start') / 1.8), Func(self.tutorialTom.animFSM.request, 'neutral'), name = 'tutorial-reward-3ca'), Sequence(Wait(0.5), Func(self.tutorialTom.setChatAbsolute, Localizer.MovieTutorialReward5, CFSpeech | CFTimeout), Wait(1.0), Func(self.tutorialTom.animFSM.request, 'TeleportOut'), Wait(self.tutorialTom.getDuration('teleport')), Wait(1.0), Func(self.playTutorialReward_4, 0), name = 'tutorial-reward-3cb'), name = 'tutorial-reward-3c')
            self.track1.start()
        else:
            self.playTutorialReward_4(0)
        return None

    
    def playTutorialReward_4(self, value):
        toonbase.localToon.setH(270)
        self.tutorialTom.removeActive()
        self.tutorialTom.delete()
        self.rewardCallback()
        return None

    
    def stop(self):
        if self.track:
            self.track.finish()
            self.track = None
        
        if self.rewardPanel:
            self.rewardPanel.hide()
        
        if self.playByPlayText:
            self.playByPlayText.hide()
        

    
    def _Movie__doToonAttacks(self):
        if base.config.GetBool('want-toon-attack-anims', 1):
            ivals = []
            camIvals = []
            (ival, camIval) = MovieSOS.doSOSs(self._Movie__findToonAttack(SOS))
            if ival:
                ivals.append(ival)
                camIvals.append(camIval)
            
            (ival, camIval) = MovieHeal.doHeals(self._Movie__findToonAttack(HEAL))
            if ival:
                ivals.append(ival)
                camIvals.append(camIval)
            
            (ival, camIval) = MovieTrap.doTraps(self._Movie__findToonAttack(TRAP))
            if ival:
                ivals.append(ival)
                camIvals.append(camIval)
            
            (ival, camIval) = MovieLure.doLures(self._Movie__findToonAttack(LURE))
            if ival:
                ivals.append(ival)
                camIvals.append(camIval)
            
            (ival, camIval) = MovieSound.doSounds(self._Movie__findToonAttack(SOUND))
            if ival:
                ivals.append(ival)
                camIvals.append(camIval)
            
            (ival, camIval) = MovieThrow.doThrows(self._Movie__findToonAttack(THROW))
            if ival:
                ivals.append(ival)
                camIvals.append(camIval)
            
            (ival, camIval) = MovieSquirt.doSquirts(self._Movie__findToonAttack(SQUIRT))
            if ival:
                ivals.append(ival)
                camIvals.append(camIval)
            
            (ival, camIval) = MovieDrop.doDrops(self._Movie__findToonAttack(DROP))
            if ival:
                ivals.append(ival)
                camIvals.append(camIval)
            
            if len(ivals) == 0:
                return (None, None)
            else:
                return (Track(ivals, name = 'toon-attacks'), Track(camIvals, name = 'toon-attacks-cam'))
        else:
            return (None, None)

    
    def genRewardDicts(self, id0, origExp0, earnedExp0, items0, missedItems0, id1, origExp1, earnedExp1, items1, missedItems1, id2, origExp2, earnedExp2, items2, missedItems2, id3, origExp3, earnedExp3, items3, missedItems3, deathList):
        self.deathList = deathList
        entries = ((id0, origExp0, earnedExp0, items0, missedItems0), (id1, origExp1, earnedExp1, items1, missedItems1), (id2, origExp2, earnedExp2, items2, missedItems2), (id3, origExp3, earnedExp3, items3, missedItems3))
        self.toonRewardDicts = []
        for (toonId, origExp, earnedExp, items, missedItems) in entries:
            if toonId != -1:
                dict = { }
                toon = self.battle.findToon(toonId)
                if toon == None:
                    continue
                
                dict['toon'] = toon
                dict['origExp'] = origExp
                dict['earnedExp'] = earnedExp
                dict['items'] = items
                dict['missedItems'] = missedItems
                self.toonRewardDicts.append(dict)
            
        

    
    def genAttackDicts(self, toons, suits, id0, tr0, le0, tg0, hp0, ac0, hpb0, kbb0, died0, id1, tr1, le1, tg1, hp1, ac1, hpb1, kbb1, died1, id2, tr2, le2, tg2, hp2, ac2, hpb2, kbb2, died2, id3, tr3, le3, tg3, hp3, ac3, hpb3, kbb3, died3, sid0, at0, stg0, dm0, sd0, sb0, st0, sid1, at1, stg1, dm1, sd1, sb1, st1, sid2, at2, stg2, dm2, sd2, sb2, st2, sid3, at3, stg3, dm3, sd3, sb3, st3):
        if self.track and self.track.isPlaying():
            self.notify.warning('genAttackDicts() - track is playing!')
        
        toonAttacks = ((id0, tr0, le0, tg0, hp0, ac0, hpb0, kbb0, died0), (id1, tr1, le1, tg1, hp1, ac1, hpb1, kbb1, died1), (id2, tr2, le2, tg2, hp2, ac2, hpb2, kbb2, died2), (id3, tr3, le3, tg3, hp3, ac3, hpb3, kbb3, died3))
        self._Movie__genToonAttackDicts(toons, suits, toonAttacks)
        suitAttacks = ((sid0, at0, stg0, dm0, sd0, sb0, st0), (sid1, at1, stg1, dm1, sd1, sb1, st1), (sid2, at2, stg2, dm2, sd2, sb2, st2), (sid3, at3, stg3, dm3, sd3, sb3, st3))
        self._Movie__genSuitAttackDicts(toons, suits, suitAttacks)

    
    def _Movie__genToonAttackDicts(self, toons, suits, toonAttacks):
        for ta in toonAttacks:
            targetGone = 0
            track = ta[TOON_TRACK_COL]
            if track != NO_ATTACK:
                adict = { }
                toonIndex = ta[TOON_ID_COL]
                toonId = toons[toonIndex]
                toon = self.battle.findToon(toonId)
                if toon == None:
                    continue
                
                level = ta[TOON_LVL_COL]
                adict['toon'] = toon
                adict['track'] = track
                adict['level'] = level
                hps = ta[TOON_HP_COL]
                kbbonuses = ta[TOON_KBBONUS_COL]
                if track == SOS:
                    targetId = ta[TOON_TGT_COL]
                    if targetId == toonbase.localToon.doId:
                        target = toonbase.localToon
                        adict['targetType'] = 'callee'
                    elif toon == toonbase.localToon:
                        target = toonbase.tcr.identifyAvatar(targetId)
                        adict['targetType'] = 'caller'
                    else:
                        target = None
                        adict['targetType'] = 'observer'
                    adict['target'] = target
                elif track == HEAL:
                    if levelAffectsGroup(level):
                        targets = []
                        for t in toons:
                            if t != toonId and t != -1:
                                target = self.battle.findToon(t)
                                if target == None:
                                    continue
                                
                                tdict = { }
                                tdict['toon'] = target
                                tdict['hp'] = hps[toons.index(t)]
                                targets.append(tdict)
                            
                        
                        if len(targets) > 0:
                            adict['target'] = targets
                        else:
                            targetGone = 1
                    else:
                        targetIndex = ta[TOON_TGT_COL]
                        if targetIndex < 0:
                            targetGone = 1
                        else:
                            targetId = toons[targetIndex]
                            target = self.battle.findToon(targetId)
                            if target != None:
                                tdict = { }
                                tdict['toon'] = target
                                tdict['hp'] = hps[targetIndex]
                                adict['target'] = tdict
                            else:
                                targetGone = 1
                elif attackAffectsGroup(track, level):
                    targets = []
                    for s in suits:
                        if s != -1:
                            target = self.battle.findSuit(s)
                            targetIndex = suits.index(s)
                            sdict = { }
                            sdict['suit'] = target
                            sdict['hp'] = hps[targetIndex]
                            sdict['kbbonus'] = kbbonuses[targetIndex]
                            sdict['died'] = ta[SUIT_DIED_COL] & 1 << targetIndex
                            if sdict['died'] != 0:
                                pass
                            1
                            targets.append(sdict)
                        
                    
                    adict['target'] = targets
                else:
                    targetIndex = ta[TOON_TGT_COL]
                    if targetIndex < 0:
                        targetGone = 1
                    else:
                        targetId = suits[targetIndex]
                        target = self.battle.findSuit(targetId)
                        sdict = { }
                        sdict['suit'] = target
                        suitIndex = self.battle.activeSuits.index(target)
                        leftSuits = []
                        for si in range(0, suitIndex):
                            asuit = self.battle.activeSuits[si]
                            if self.battle.isSuitLured(asuit) == 0:
                                leftSuits.append(asuit)
                            
                        
                        lenSuits = len(self.battle.activeSuits)
                        rightSuits = []
                        if lenSuits > suitIndex + 1:
                            for si in range(suitIndex + 1, lenSuits):
                                asuit = self.battle.activeSuits[si]
                                if self.battle.isSuitLured(asuit) == 0:
                                    rightSuits.append(asuit)
                                
                            
                        
                        sdict['leftSuits'] = leftSuits
                        sdict['rightSuits'] = rightSuits
                        sdict['hp'] = hps[targetIndex]
                        sdict['kbbonus'] = kbbonuses[targetIndex]
                        sdict['died'] = ta[SUIT_DIED_COL] & 1 << targetIndex
                        if sdict['died'] != 0:
                            pass
                        1
                        adict['target'] = sdict
                adict['hpbonus'] = ta[TOON_HPBONUS_COL]
                adict['sidestep'] = ta[TOON_ACCBONUS_COL]
                adict['battle'] = self.battle
                adict['playByPlayText'] = self.playByPlayText
                if targetGone == 0:
                    self.toonAttackDicts.append(adict)
                else:
                    self.notify.warning('genToonAttackDicts() - target gone!')
            
        
        
        def compFunc(a, b):
            alevel = a['level']
            blevel = b['level']
            if alevel > blevel:
                return 1
            elif alevel < blevel:
                return -1
            
            return 0

        self.toonAttackDicts.sort(compFunc)

    
    def _Movie__findToonAttack(self, track):
        p = []
        for ta in self.toonAttackDicts:
            if ta['track'] == track:
                p.append(ta)
            
        
        return p

    
    def _Movie__genSuitAttackDicts(self, toons, suits, suitAttacks):
        for sa in suitAttacks:
            targetGone = 0
            attack = sa[SUIT_ATK_COL]
            if attack != NO_ATTACK:
                suitIndex = sa[SUIT_ID_COL]
                suitId = suits[suitIndex]
                suit = self.battle.findSuit(suitId)
                if suit == None:
                    self.notify.error('suit: %d not in battle!' % suitId)
                
                adict = getSuitAttack(suit.getStyleName(), suit.getLevel(), attack)
                adict['suit'] = suit
                adict['battle'] = self.battle
                adict['playByPlayText'] = self.playByPlayText
                adict['taunt'] = sa[SUIT_TAUNT_COL]
                hps = sa[SUIT_HP_COL]
                if adict['group'] == ATK_TGT_GROUP:
                    targets = []
                    for t in toons:
                        if t != -1:
                            target = self.battle.findToon(t)
                            if target == None:
                                continue
                            
                            targetIndex = toons.index(t)
                            tdict = { }
                            tdict['toon'] = target
                            tdict['hp'] = hps[targetIndex]
                            toonDied = sa[TOON_DIED_COL] & 1 << targetIndex
                            tdict['died'] = toonDied
                            targets.append(tdict)
                        
                    
                    if len(targets) > 0:
                        adict['target'] = targets
                    else:
                        targetGone = 1
                elif adict['group'] == ATK_TGT_SINGLE:
                    targetIndex = sa[SUIT_TGT_COL]
                    targetId = toons[targetIndex]
                    target = self.battle.findToon(targetId)
                    if target == None:
                        targetGone = 1
                        break
                    
                    tdict = { }
                    tdict['toon'] = target
                    tdict['hp'] = hps[targetIndex]
                    toonDied = sa[TOON_DIED_COL] & 1 << targetIndex
                    tdict['died'] = toonDied
                    toonIndex = self.battle.activeToons.index(target)
                    rightToons = []
                    for ti in range(0, toonIndex):
                        rightToons.append(self.battle.activeToons[ti])
                    
                    lenToons = len(self.battle.activeToons)
                    leftToons = []
                    if lenToons > toonIndex + 1:
                        for ti in range(toonIndex + 1, lenToons):
                            leftToons.append(self.battle.activeToons[ti])
                        
                    
                    tdict['leftToons'] = leftToons
                    tdict['rightToons'] = rightToons
                    adict['target'] = tdict
                else:
                    self.notify.warning('got suit attack not group or single!')
                if targetGone == 0:
                    self.suitAttackDicts.append(adict)
                else:
                    self.notify.warning('genSuitAttackDicts() - target gone!')
            
        

    
    def _Movie__doSuitAttacks(self):
        if base.config.GetBool('want-suit-anims', 1):
            ivals = []
            camIvals = []
            for a in self.suitAttackDicts:
                (ival, camIval) = MovieSuitAttacks.doSuitAttack(a)
                if ival:
                    ivals.append(ival)
                    camIvals.append(camIval)
                
            
            if len(ivals) == 0:
                return (None, None)
            
            return (Track(ivals), Track(camIvals))
        else:
            return (None, None)


