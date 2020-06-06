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
    tracks = []
    if localToonActive == 1:
        tracks.append(Func(rpanel.show))
        tracks.append(Func(NametagGlobals.setOnscreenChatForced, 1))
    
    camTracks = []
    endTracks = []
    danceSound = globalBattleSoundCache.getSound('ENC_Win.mp3')
    for t in toons:
        rdict = __findToonReward(rewardDicts, t)
        expTrack = rpanel.getExpTrack(t, rdict['origExp'], rdict['earnedExp'], deathList, rdict['items'], rdict['missedItems'], toons)
        if expTrack:
            tracks.append(expTrack)
            camDuration = expTrack.getDuration()
            camExpTrack = MovieCamera.chooseRewardShot(t, camDuration)
            camTracks.append(MovieCamera.chooseRewardShot(t, camDuration))
        
    
    if localToonActive == 1:
        tracks.append(Func(rpanel.hide))
        tracks.append(Func(NametagGlobals.setOnscreenChatForced, 0))
    
    tracks = tracks + endTracks
    seq = Sequence(tracks)
    seqdur = seq.getDuration()
    print 'dance duration: ', seqdur
    soundTrack = SoundInterval(danceSound, duration = seqdur, loop = 1)
    mtrack = Parallel(Sequence(tracks), soundTrack)
    camTrack = Track(camTracks)
    return (mtrack, camTrack)

