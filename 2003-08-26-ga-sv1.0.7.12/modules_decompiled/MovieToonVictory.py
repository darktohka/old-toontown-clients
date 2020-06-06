# File: M (Python 2.2)

from IntervalGlobal import *
from RewardPanel import *
from BattleSounds import *
import MovieCamera
import DirectNotifyGlobal
notify = DirectNotifyGlobal.directNotify.newCategory('MovieToonVictory')

def __findToonReward(rewards, toon):
    for r in rewards:
        if r['toon'] == toon:
            return r
        
    
    return None


def doToonVictory(localToonActive, toons, rewardDicts, deathList, rpanel):
    track = Sequence()
    if localToonActive == 1:
        track.append(Func(rpanel.show))
        track.append(Func(NametagGlobals.setOnscreenChatForced, 1))
    
    camTrack = Sequence()
    endTrack = Sequence()
    danceSound = globalBattleSoundCache.getSound('ENC_Win.mp3')
    for t in toons:
        rdict = __findToonReward(rewardDicts, t)
        expTrack = rpanel.getExpTrack(t, rdict['origExp'], rdict['earnedExp'], deathList, rdict['items'], rdict['missedItems'], toons)
        if expTrack:
            track.append(expTrack)
            camDuration = expTrack.getDuration()
            camExpTrack = MovieCamera.chooseRewardShot(t, camDuration)
            camTrack.append(MovieCamera.chooseRewardShot(t, camDuration))
        
    
    if localToonActive == 1:
        track.append(Func(rpanel.hide))
        track.append(Func(NametagGlobals.setOnscreenChatForced, 0))
    
    track.append(endTrack)
    trackdur = track.getDuration()
    print 'dance duration: ', trackdur
    soundTrack = SoundInterval(danceSound, duration = trackdur, loop = 1)
    mtrack = Parallel(track, soundTrack)
    return (mtrack, camTrack)

