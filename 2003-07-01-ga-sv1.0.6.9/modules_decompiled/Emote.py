# File: E (Python 2.2)

import Toon
from IntervalGlobal import *
import Localizer
import types
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
    track = Sequence(Func(toon.sadEyes), Func(toon.blinkEyes))
    exitTrack = Track(Func(toon.normalEyes), Func(toon.blinkEyes))
    return (track, 5.0, exitTrack)


def doSleep(toon):
    if toon == toonbase.localToon:
        toon.gotoSleep()
    
    return (None, 0, None)


def doYes(toon):
    tracks = []
    for lod in toon.getLODNames():
        h = toon.getPart('head', lod)
        track = Sequence(LerpHprInterval(h, 0.10000000000000001, Vec3(0, -30, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(0, 20, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(0, -20, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(0, 20, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(0, -20, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(0, 20, 0)), LerpHprInterval(h, 0.10000000000000001, Vec3(0, 0, 0)))
        tracks.append(track)
    
    track = Parallel(tracks)
    track.play()
    return (None, 0, None)


def doNo(toon):
    tracks = []
    for lod in toon.getLODNames():
        h = toon.getPart('head', lod)
        track = Sequence(LerpHprInterval(h, 0.10000000000000001, Vec3(40, 0, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(-40, 0, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(40, 0, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(-40, 0, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(20, 0, 0)), LerpHprInterval(h, 0.14999999999999999, Vec3(-20, 0, 0)), LerpHprInterval(h, 0.10000000000000001, Vec3(0, 0, 0)))
        tracks.append(track)
    
    track = Parallel(tracks)
    track.play()
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


def doNothing(toon):
    return (None, 0, None)


def returnToLastAnim(toon):
    if toon.playingAnim:
        toon.loop(toon.playingAnim)
    elif toon.hp > 0:
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
        
        track = Sequence(track, Func(ReleaseAll, toon))
    
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
        doNothing,
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
        doNothing,
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
    2,
    3,
    4,
    5]
HeadEmotes = [
    17,
    18,
    19]

def DisableAll(toon, msg = None):
    if toon != toonbase.localToon:
        return None
    
    for i in range(len(EmoteFunc)):
        EmoteFunc[i][1] = EmoteFunc[i][1] + 1
    


def ReleaseAll(toon, msg = None):
    if toon != toonbase.localToon:
        return None
    
    for i in range(len(EmoteFunc)):
        EmoteFunc[i][1] = EmoteFunc[i][1] - 1
    


def DisableBody(toon, msg = None):
    if toon != toonbase.localToon:
        return None
    
    for i in BodyEmotes:
        EmoteFunc[i][1] = EmoteFunc[i][1] + 1
    


def ReleaseBody(toon, msg = None):
    if toon != toonbase.localToon:
        return None
    
    for i in BodyEmotes:
        EmoteFunc[i][1] = EmoteFunc[i][1] - 1
    


def DisableHead(toon):
    if toon != toonbase.localToon:
        return None
    
    for i in HeadEmotes:
        EmoteFunc[i][1] = EmoteFunc[i][1] + 1
    


def ReleaseHead(toon):
    if toon != toonbase.localToon:
        return None
    
    for i in HeadEmotes:
        EmoteFunc[i][1] = EmoteFunc[i][1] - 1
    


def Disable(index, toon):
    if isinstance(index, types.StringType):
        index = Localizer.EmoteFuncDict[index]
    
    EmoteFunc[index][1] = EmoteFunc[index][1] + 1


def Enable(index, toon):
    if isinstance(index, types.StringType):
        index = Localizer.EmoteFuncDict[index]
    
    EmoteFunc[index][1] = EmoteFunc[index][1] - 1


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


