# File: E (Python 2.2)

import Toon
from IntervalGlobal import *
import Localizer
import types
import PythonUtil
EmoteEnableStateChanged = 'EmoteEnableStateChanged'
EmoteSleepIndex = 4

def doDance(toon):
    track = Sequence(Func(toon.play, 'victory'))
    duration = toon.getDuration('victory', 'legs')
    return (track, duration, None)


def doJump(toon):
    track = Sequence(Func(toon.play, 'jump'))
    return (track, 0, None)


def doDead(toon):
    toon.animFSM.request('Sad')
    return (None, 0, None)


def doAnnoyed(toon):
    duration = toon.getDuration('angry', 'torso')
    track = Sequence(Func(toon.angryEyes), Func(toon.blinkEyes), Func(toon.play, 'angry'))
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
    if toon == toonbase.localToon:
        toon.gotoSleep()
    
    return (None, 0, None)


def doYes(toon):
    tracks = Parallel()
    for lod in toon.getLODNames():
        h = toon.getPart('head', lod)
        tracks.append(Sequence(LerpHprInterval(h, 0.10000000000000001, Vec3(0, -30, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(0, 20, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(0, -20, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(0, 20, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(0, -20, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(0, 20, 0)), LerpHprInterval(h, 0.10000000000000001, Vec3(0, 0, 0))))
    
    tracks.play()
    return (None, 0, None)


def doNo(toon):
    tracks = Parallel()
    for lod in toon.getLODNames():
        h = toon.getPart('head', lod)
        tracks.append(Sequence(LerpHprInterval(h, 0.10000000000000001, Vec3(40, 0, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(-40, 0, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(40, 0, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(-40, 0, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(20, 0, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(-20, 0, 0)), LerpHprInterval(h, 0.10000000000000001, Vec3(0, 0, 0))))
    
    tracks.play()
    return (None, 0, None)


def doOk(toon):
    return (None, 0, None)


def doHello(toon):
    return (None, 0, None)


def doBye(toon):
    return (None, 0, None)


def doShrug(toon):
    track = Sequence(Func(toon.play, 'shrug'))
    duration = toon.getDuration('shrug', 'torso')
    return (track, duration, None)


def doWave(toon):
    track = Sequence(Func(toon.play, 'wave'))
    duration = toon.getDuration('wave', 'torso')
    return (track, duration, None)


def doApplause(toon):
    track = Sequence(Func(toon.play, 'applause'))
    duration = toon.getDuration('applause', 'torso')
    return (track, duration, None)


def doConfused(toon):
    track = Sequence(Func(toon.play, 'confused'))
    duration = toon.getDuration('confused', 'torso')
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

    (track, duration, exitTrack) = func(toon)
    if track != None:
        track = Sequence(track, Func(DisableAll, toon))
        if duration > 0:
            track = Sequence(track, Wait(duration))
        
        if exitTrack != None:
            track = Sequence(track, exitTrack)
        
        if emoteIndex != EmoteSleepIndex and duration > 0:
            track = Sequence(track, Func(returnToLastAnim, toon))
        
        track = Sequence(track, Func(ReleaseAll, toon), autoFinish = 1)
    
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
        doNothing,
        0],
    [
        doNothing,
        0],
    [
        doNothing,
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
    9,
    11,
    13]
HeadEmotes = [
    2,
    17,
    18,
    19]

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


def DisableHead(toon):
    if toon != toonbase.localToon:
        return None
    
    DisableGroup(HeadEmotes, toon)


def ReleaseHead(toon):
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


