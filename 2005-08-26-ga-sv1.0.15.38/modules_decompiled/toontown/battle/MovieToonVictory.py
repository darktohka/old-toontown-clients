# File: M (Python 2.2)

from direct.interval.IntervalGlobal import *
from RewardPanel import *
from BattleSounds import *
import MovieCamera
from direct.directnotify import DirectNotifyGlobal
import types
notify = DirectNotifyGlobal.directNotify.newCategory('MovieToonVictory')

def __findToonReward(rewards, toon):
    for r in rewards:
        if r['toon'] == toon:
            return r
        
    
    return None


def doToonVictory(localToonActive, toons, rewardToonIds, rewardDicts, deathList, rpanel, allowGroupShot = 1):
    track = Sequence()
    if localToonActive == 1:
        track.append(Func(rpanel.show))
        track.append(Func(NametagGlobals.setOnscreenChatForced, 1))
    
    camTrack = Sequence()
    endTrack = Sequence()
    danceSound = globalBattleSoundCache.getSound('ENC_Win.mp3')
    toonList = []
    for t in toons:
        if isinstance(t, types.IntType):
            t = base.cr.doId2do.get(t)
        
        if t:
            toonList.append(t)
        
    
    toonId2toon = { }
    for toon in toonList:
        toonId2toon[toon.doId] = toon
    
    rewardToonList = []
    for id in rewardToonIds:
        rewardToonList.append(toonId2toon.get(id))
    
    for t in toonList:
        rdict = __findToonReward(rewardDicts, t)
        if rdict != None:
            expTrack = rpanel.getExpTrack(t, rdict['origExp'], rdict['earnedExp'], deathList, rdict['items'], rdict['missedItems'], rdict['origMerits'], rdict['merits'], rdict['parts'], rewardToonList)
            if expTrack:
                track.append(expTrack)
                camDuration = expTrack.getDuration()
                camExpTrack = MovieCamera.chooseRewardShot(t, camDuration)
                camTrack.append(MovieCamera.chooseRewardShot(t, camDuration, allowGroupShot = allowGroupShot))
            
        
    
    if localToonActive == 1:
        track.append(Func(rpanel.hide))
        track.append(Func(NametagGlobals.setOnscreenChatForced, 0))
    
    track.append(endTrack)
    trackdur = track.getDuration()
    soundTrack = SoundInterval(danceSound, duration = trackdur, loop = 1)
    mtrack = Parallel(track, soundTrack)
    return (mtrack, camTrack)

