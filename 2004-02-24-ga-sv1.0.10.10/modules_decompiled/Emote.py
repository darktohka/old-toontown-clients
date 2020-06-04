# File: E (Python 2.2)

import Toon
from IntervalGlobal import *
import Localizer
import types
import PythonUtil
from PandaModules import *
EmoteEnableStateChanged = 'EmoteEnableStateChanged'
EmoteSleepIndex = 4

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
    track = Sequence(Func(toon.stopLookAround), Func(toon.stopBlink), Func(toon.closeEyes), Func(toon.lerpLookAt, Point3(0, 1, -4)), Func(toon.loop, 'neutral'), Func(toon.setPlayRate, 0.40000000000000002, 'neutral'), Func(toon.setChatAbsolute, Localizer.ToonSleepString, CFThought))
    
    def wakeUpFromSleepEmote():
        toon.startLookAround()
        toon.openEyes()
        toon.startBlink()
        if toon.nametag.getChat() == Localizer.ToonSleepString:
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


def doNothing(toon):
    return (None, 0, None)


def returnToLastAnim(toon):
    if hasattr(toon, 'playingAnim') and toon.playingAnim:
        toon.loop(toon.playingAnim)
    elif not hasattr(toon, 'hp') or toon.hp > 0:
        toon.loop('neutral')
    else:
        toon.loop('sad-neutral')


def DoEmote(toon, emoteIndex, ts = 0):
    
    try:
        func = EmoteFunc[emoteIndex][0]
    except:
        print 'Error in finding emote func %s' % emoteIndex
        return (None, None)

    
    def clearEmoteTrack():
        toonbase.localToon.emoteTrack = None

    (track, duration, exitTrack) = func(toon)
    if track != None:
        track = Sequence(track, Func(DisableAll, toon, 'doEmote'))
        if duration > 0:
            track = Sequence(track, Wait(duration))
        
        if exitTrack != None:
            track = Sequence(track, exitTrack)
        
        if duration > 0:
            track = Sequence(track, Func(returnToLastAnim, toon))
        
        track = Sequence(track, Func(ReleaseAll, toon, 'doEmote'), autoFinish = 1)
        if toon.isLocal():
            track = Sequence(track, Func(clearEmoteTrack))
        
    
    if track != None:
        if toon.emote != None:
            toon.emote.finish()
            toon.emote = None
        
        toon.emote = track
        track.start(ts)
    
    return (track, duration)

SLEEP_INDEX = 4
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
        doNothing,
        0],
    [
        doBored,
        0],
    [
        doApplause,
        0],
    [
        doNothing,
        0],
    [
        doConfused,
        0],
    [
        doNothing,
        0],
    [
        doBow,
        0],
    [
        doNothing,
        0],
    [
        doNothing,
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
BodyEmotes = [
    0,
    1,
    3,
    4,
    5,
    6,
    8,
    9,
    11,
    13]
HeadEmotes = [
    2,
    17,
    18,
    19]

def PrintEmoteState(action, msg):
    pass


def DisableAll(toon, msg = None):
    if toon != toonbase.localToon:
        return None
    
    DisableGroup(range(len(EmoteFunc)), toon)


def ReleaseAll(toon, msg = None):
    if toon != toonbase.localToon:
        return None
    
    EnableGroup(range(len(EmoteFunc)), toon)


def DisableBody(toon, msg = None):
    if toon != toonbase.localToon:
        return None
    
    DisableGroup(BodyEmotes, toon)


def ReleaseBody(toon, msg = None):
    if toon != toonbase.localToon:
        return None
    
    EnableGroup(BodyEmotes, toon)


def DisableHead(toon, msg = None):
    if toon != toonbase.localToon:
        return None
    
    DisableGroup(HeadEmotes, toon)


def ReleaseHead(toon, msg = None):
    if toon != toonbase.localToon:
        return None
    
    EnableGroup(HeadEmotes, toon)


def DisableGroup(indices, toon):
    LockStateChangeMsg()
    for i in indices:
        Disable(i, toon)
    
    UnlockStateChangeMsg()


def EnableGroup(indices, toon):
    LockStateChangeMsg()
    for i in indices:
        Enable(i, toon)
    
    UnlockStateChangeMsg()


def Disable(index, toon):
    if isinstance(index, types.StringType):
        index = Localizer.EmoteFuncDict[index]
    
    EmoteFunc[index][1] = EmoteFunc[index][1] + 1
    if toon is toonbase.localToon:
        if EmoteFunc[index][1] == 1:
            emoteEnableStateChanged()
        
    


def Enable(index, toon):
    if isinstance(index, types.StringType):
        index = Localizer.EmoteFuncDict[index]
    
    EmoteFunc[index][1] = EmoteFunc[index][1] - 1
    if toon is toonbase.localToon:
        if EmoteFunc[index][1] == 0:
            emoteEnableStateChanged()
        
    

StateChangeMsgLocks = 0
StateHasChanged = 0

def LockStateChangeMsg():
    global StateChangeMsgLocks
    StateChangeMsgLocks += 1


def UnlockStateChangeMsg():
    global StateChangeMsgLocks, StateHasChanged
    if StateChangeMsgLocks <= 0:
        print PythonUtil.lineTag() + ': someone unlocked too many times'
        return None
    
    StateChangeMsgLocks -= 1
    if StateChangeMsgLocks == 0 and StateHasChanged:
        messenger.send(EmoteEnableStateChanged)
        StateHasChanged = 0
    


def emoteEnableStateChanged():
    global StateHasChanged
    if StateChangeMsgLocks > 0:
        StateHasChanged = 1
    else:
        messenger.send(EmoteEnableStateChanged)


def IsEnabled(index):
    if isinstance(index, types.StringType):
        index = Localizer.EmoteFuncDict[index]
    
    if EmoteFunc[index][1] == 0:
        return 1
    
    return 0


class Emote:
    
    def __init__(self):
        if len(EmoteFunc) != len(Localizer.EmoteList):
            self.notify.error('Emote.EmoteFunc and Localizer.EmoteList are different lengths.')
        
        self.track = None


