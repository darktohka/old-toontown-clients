# File: T (Python 2.2)

import Toon
from direct.interval.IntervalGlobal import *
from otp.otpbase import OTPLocalizer
from toontown.toonbase import TTLocalizer
from otp.otpbase import OTPLocalizer
import types
from direct.showbase import PythonUtil
from pandac.PandaModules import *
from otp.avatar import Emote
EmoteSleepIndex = 4
EmoteClear = -1

def doVictory(toon):
    duration = toon.getDuration('victory', 'legs')
    sfx = base.loadSfx('phase_3.5/audio/sfx/ENC_Win.mp3')
    sfxDuration = duration - 1.0
    sfxTrack = SoundInterval(sfx, loop = 1, duration = sfxDuration, node = toon)
    track = Sequence(Func(toon.play, 'victory'), sfxTrack, duration = 0)
    return (track, duration, None)


def doJump(toon):
    track = Sequence(Func(toon.play, 'jump'))
    return (track, 0, None)


def doDead(toon):
    toon.animFSM.request('Sad')
    return (None, 0, None)


def doAnnoyed(toon):
    duration = toon.getDuration('angry', 'torso')
    sfx = base.loadSfx('phase_3.5/audio/sfx/avatar_emotion_angry.mp3')
    
    def playSfx():
        base.playSfx(sfx, volume = 1, node = toon)

    track = Sequence(Func(toon.angryEyes), Func(toon.blinkEyes), Func(toon.play, 'angry'), Func(playSfx))
    exitTrack = Sequence(Func(toon.normalEyes), Func(toon.blinkEyes))
    return (track, duration, exitTrack)


def doAngryEyes(toon):
    track = Sequence(Func(toon.angryEyes), Func(toon.blinkEyes), Wait(10.0), Func(toon.normalEyes))
    return (track, 0.10000000000000001, None)


def doHappy(toon):
    track = Sequence(Func(toon.play, 'jump'), Func(toon.normalEyes), Func(toon.blinkEyes))
    duration = toon.getDuration('jump', 'legs')
    return (track, duration, None)


def doSad(toon):
    track = Sequence(Func(toon.sadEyes), Func(toon.blinkEyes), Wait(10.0), Func(toon.normalEyes))
    return (track, 0.10000000000000001, None)


def doSleep(toon):
    duration = 4
    track = Sequence(Func(toon.stopLookAround), Func(toon.stopBlink), Func(toon.closeEyes), Func(toon.lerpLookAt, Point3(0, 1, -4)), Func(toon.loop, 'neutral'), Func(toon.setPlayRate, 0.40000000000000002, 'neutral'), Func(toon.setChatAbsolute, TTLocalizer.ToonSleepString, CFThought))
    
    def wakeUpFromSleepEmote():
        toon.startLookAround()
        toon.openEyes()
        toon.startBlink()
        if toon.nametag.getChat() == TTLocalizer.ToonSleepString:
            toon.clearChat()
        
        toon.lerpLookAt(Point3(0, 1, 0), time = 0.25)

    exitTrack = Sequence(Func(wakeUpFromSleepEmote))
    return (track, duration, exitTrack)


def doYes(toon):
    tracks = Parallel(autoFinish = 1)
    for lod in toon.getLODNames():
        h = toon.getPart('head', lod)
        tracks.append(Sequence(LerpHprInterval(h, 0.10000000000000001, Vec3(0, -30, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(0, 20, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(0, -20, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(0, 20, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(0, -20, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(0, 20, 0)), LerpHprInterval(h, 0.10000000000000001, Vec3(0, 0, 0))))
    
    tracks.start()
    return (None, 0, None)


def doNo(toon):
    tracks = Parallel(autoFinish = 1)
    for lod in toon.getLODNames():
        h = toon.getPart('head', lod)
        tracks.append(Sequence(LerpHprInterval(h, 0.10000000000000001, Vec3(40, 0, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(-40, 0, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(40, 0, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(-40, 0, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(20, 0, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(-20, 0, 0)), LerpHprInterval(h, 0.10000000000000001, Vec3(0, 0, 0))))
    
    tracks.start()
    return (None, 0, None)


def doOk(toon):
    return (None, 0, None)


def doShrug(toon):
    sfx = base.loadSfx('phase_3.5/audio/sfx/avatar_emotion_shrug.mp3')
    
    def playSfx():
        base.playSfx(sfx, volume = 1, node = toon)

    track = Sequence(Func(toon.play, 'shrug'), Func(playSfx))
    duration = toon.getDuration('shrug', 'torso')
    return (track, duration, None)


def doWave(toon):
    track = Sequence(Func(toon.play, 'wave'))
    duration = toon.getDuration('wave', 'torso')
    return (track, duration, None)


def doApplause(toon):
    sfx = base.loadSfx('phase_4/audio/sfx/avatar_emotion_applause.mp3')
    
    def playSfx():
        base.playSfx(sfx, volume = 1, node = toon)

    track = Sequence(Func(toon.play, 'applause'), Func(playSfx))
    duration = toon.getDuration('applause', 'torso')
    return (track, duration, None)


def doConfused(toon):
    sfx = base.loadSfx('phase_4/audio/sfx/avatar_emotion_confused.mp3')
    
    def playSfx():
        base.playSfx(sfx, volume = 1, node = toon)

    track = Sequence(Func(toon.play, 'confused'), Func(playSfx))
    duration = toon.getDuration('confused', 'torso')
    return (track, duration, None)


def doSlipForward(toon):
    sfx = base.loadSfx('phase_4/audio/sfx/MG_cannon_hit_dirt.mp3')
    
    def playSfx():
        base.playSfx(sfx, volume = 1, node = toon)

    sfxDelay = 0.69999999999999996
    track = Sequence(Func(toon.play, 'slip-forward'), Wait(sfxDelay), Func(playSfx))
    duration = toon.getDuration('slip-forward', 'torso') - sfxDelay
    return (track, duration, None)


def doBored(toon):
    sfx = base.loadSfx('phase_4/audio/sfx/avatar_emotion_bored.mp3')
    
    def playSfx():
        base.playSfx(sfx, volume = 1, node = toon)

    sfxDelay = 2.2000000000000002
    track = Sequence(Func(toon.play, 'bored'), Wait(sfxDelay), Func(playSfx))
    duration = toon.getDuration('bored', 'torso') - sfxDelay
    return (track, duration, None)


def doBow(toon):
    if toon.style.torso[1] == 'd':
        track = Sequence(Func(toon.play, 'curtsy'))
        duration = toon.getDuration('curtsy', 'torso')
    else:
        track = Sequence(Func(toon.play, 'bow'))
        duration = toon.getDuration('bow', 'torso')
    return (track, duration, None)


def doSlipBackward(toon):
    sfx = base.loadSfx('phase_4/audio/sfx/MG_cannon_hit_dirt.mp3')
    
    def playSfx():
        base.playSfx(sfx, volume = 1, node = toon)

    sfxDelay = 0.69999999999999996
    track = Sequence(Func(toon.play, 'slip-backward'), Wait(sfxDelay), Func(playSfx))
    duration = toon.getDuration('slip-backward', 'torso') - sfxDelay
    return (track, duration, None)


def doThink(toon):
    duration = (47.0 / 24.0) * 2
    animTrack = Sequence(ActorInterval(toon, 'think', startFrame = 0, endFrame = 46), ActorInterval(toon, 'think', startFrame = 46, endFrame = 0))
    track = Sequence(animTrack, duration = 0)
    return (track, duration, None)


def doCringe(toon):
    track = Sequence(Func(toon.play, 'cringe'))
    duration = toon.getDuration('cringe', 'torso')
    return (track, duration, None)


def doResistanceSalute(toon):
    playRate = 0.75
    duration = (10.0 / 24.0) * (1 / playRate) * 2
    animTrack = Sequence(Func(toon.setChatAbsolute, OTPLocalizer.CustomSCStrings[4020], CFSpeech | CFTimeout), Func(toon.setPlayRate, playRate, 'victory'), ActorInterval(toon, 'victory', playRate = playRate, startFrame = 0, endFrame = 9), ActorInterval(toon, 'victory', playRate = playRate, startFrame = 9, endFrame = 0))
    track = Sequence(animTrack, duration = 0)
    return (track, duration, None)


def doNothing(toon):
    return (None, 0, None)


def returnToLastAnim(toon):
    if hasattr(toon, 'playingAnim') and toon.playingAnim:
        toon.loop(toon.playingAnim)
    elif not hasattr(toon, 'hp') or toon.hp > 0:
        toon.loop('neutral')
    else:
        toon.loop('sad-neutral')

EmoteFunc = [
    [
        doWave,
        0],
    [
        doHappy,
        0],
    [
        doSad,
        0],
    [
        doAnnoyed,
        0],
    [
        doSleep,
        0],
    [
        doShrug,
        0],
    [
        doVictory,
        0],
    [
        doThink,
        0],
    [
        doBored,
        0],
    [
        doApplause,
        0],
    [
        doCringe,
        0],
    [
        doConfused,
        0],
    [
        doSlipForward,
        0],
    [
        doBow,
        0],
    [
        doSlipBackward,
        0],
    [
        doResistanceSalute,
        0],
    [
        doNothing,
        0],
    [
        doYes,
        0],
    [
        doNo,
        0],
    [
        doOk,
        0]]

class TTEmote(Emote.Emote):
    SLEEP_INDEX = 4
    
    def __init__(self):
        self.emoteFunc = EmoteFunc
        self.bodyEmotes = [
            0,
            1,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15]
        self.headEmotes = [
            2,
            17,
            18,
            19]
        if len(self.emoteFunc) != len(OTPLocalizer.EmoteList):
            self.notify.error('Emote.EmoteFunc and OTPLocalizer.EmoteList are different lengths.')
        
        self.track = None
        self.stateChangeMsgLocks = 0
        self.stateHasChanged = 0

    
    def lockStateChangeMsg(self):
        self.stateChangeMsgLocks += 1

    
    def unlockStateChangeMsg(self):
        if self.stateChangeMsgLocks <= 0:
            print PythonUtil.lineTag() + ': someone unlocked too many times'
            return None
        
        self.stateChangeMsgLocks -= 1
        if self.stateChangeMsgLocks == 0 and self.stateHasChanged:
            messenger.send(self.EmoteEnableStateChanged)
            self.stateHasChanged = 0
        

    
    def emoteEnableStateChanged(self):
        if self.stateChangeMsgLocks > 0:
            self.stateHasChanged = 1
        else:
            messenger.send(self.EmoteEnableStateChanged)

    
    def disableAll(self, toon, msg = None):
        if toon != base.localAvatar:
            return None
        
        self.disableGroup(range(len(self.emoteFunc)), toon)

    
    def releaseAll(self, toon, msg = None):
        if toon != base.localAvatar:
            return None
        
        self.enableGroup(range(len(self.emoteFunc)), toon)

    
    def disableBody(self, toon, msg = None):
        if toon != base.localAvatar:
            return None
        
        self.disableGroup(self.bodyEmotes, toon)

    
    def releaseBody(self, toon, msg = None):
        if toon != base.localAvatar:
            return None
        
        self.enableGroup(self.bodyEmotes, toon)

    
    def disableHead(self, toon, msg = None):
        if toon != base.localAvatar:
            return None
        
        self.disableGroup(self.headEmotes, toon)

    
    def releaseHead(self, toon, msg = None):
        if toon != base.localAvatar:
            return None
        
        self.enableGroup(self.headEmotes, toon)

    
    def getHeadEmotes(self):
        return self.headEmotes

    
    def disableGroup(self, indices, toon):
        self.lockStateChangeMsg()
        for i in indices:
            self.disable(i, toon)
        
        self.unlockStateChangeMsg()

    
    def enableGroup(self, indices, toon):
        self.lockStateChangeMsg()
        for i in indices:
            self.enable(i, toon)
        
        self.unlockStateChangeMsg()

    
    def disable(self, index, toon):
        if isinstance(index, types.StringType):
            index = OTPLocalizer.EmoteFuncDict[index]
        
        self.emoteFunc[index][1] = self.emoteFunc[index][1] + 1
        if toon is base.localAvatar:
            if self.emoteFunc[index][1] == 1:
                self.emoteEnableStateChanged()
            
        

    
    def enable(self, index, toon):
        if isinstance(index, types.StringType):
            index = OTPLocalizer.EmoteFuncDict[index]
        
        self.emoteFunc[index][1] = self.emoteFunc[index][1] - 1
        if toon is base.localAvatar:
            if self.emoteFunc[index][1] == 0:
                self.emoteEnableStateChanged()
            
        

    
    def doEmote(self, toon, emoteIndex, ts = 0):
        
        try:
            func = self.emoteFunc[emoteIndex][0]
        except:
            print 'Error in finding emote func %s' % emoteIndex
            return (None, None)

        
        def clearEmoteTrack():
            base.localAvatar.emoteTrack = None
            base.localAvatar.d_setEmoteState(self.EmoteClear, 1.0)

        (track, duration, exitTrack) = func(toon)
        if track != None:
            track = Sequence(track, Func(self.disableAll, toon, 'doEmote'))
            if duration > 0:
                track = Sequence(track, Wait(duration))
            
            if exitTrack != None:
                track = Sequence(track, exitTrack)
            
            if duration > 0:
                track = Sequence(track, Func(returnToLastAnim, toon))
            
            track = Sequence(track, Func(self.releaseAll, toon, 'doEmote'), autoFinish = 1)
            if toon.isLocal():
                track = Sequence(track, Func(clearEmoteTrack))
            
        
        if track != None:
            if toon.emote != None:
                toon.emote.finish()
                toon.emote = None
            
            toon.emote = track
            track.start(ts)
        
        return (track, duration)

    
    def printEmoteState(self, action, msg):
        pass


Emote.globalEmote = TTEmote()
