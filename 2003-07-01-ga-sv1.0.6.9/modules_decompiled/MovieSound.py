# File: M (Python 2.2)

from IntervalGlobal import *
from BattleBase import *
from BattleProps import *
from BattleSounds import *
import MovieCamera
import DirectNotifyGlobal
import MovieUtil
notify = DirectNotifyGlobal.directNotify.newCategory('MovieSound')
soundFiles = ('AA_sound_bikehorn.mp3', 'AA_sound_whistle.mp3', 'AA_sound_bugle.mp3', 'AA_sound_aoogah.mp3', 'AA_sound_elephant.mp3', 'SZ_DD_foghorn.mp3')
tMegaphoneShrink = 3.5
dMegaphoneGrow = 0.69999999999999996
dMegaphoneShrink = 0.5
tSound = 2.4500000000000002
tSuitReact = 2.7999999999999998
BEFORE_STARS = 0.5
AFTER_STARS = 1.75

def doSounds(sounds):
    if len(sounds) == 0:
        return (None, None)
    
    tracks = []
    hitCount = 0
    prevLevel = 0
    prevSounds = [
        [],
        [],
        [],
        [],
        [],
        []]
    for sound in sounds:
        level = sound['level']
        prevSounds[level].append(sound)
        for target in sound['target']:
            if target['hp'] > 0:
                hitCount += 1
                break
            
        
    
    delay = 0.0
    for soundList in prevSounds:
        if len(soundList) > 0:
            tracks += __doSoundsLevel(soundList, delay, hitCount)
            delay += TOON_SOUND_DELAY
        
    
    mtrack = MultiTrack(tracks)
    targets = sounds[0]['target']
    camDuration = mtrack.getDuration()
    camTrack = MovieCamera.chooseSoundShot(sounds, targets, camDuration)
    return (mtrack, camTrack)


def __doSoundsLevel(sounds, delay, hitCount):
    lastSoundThatHit = None
    totalDamage = 0
    for sound in sounds:
        for target in sound['target']:
            if target['hp'] > 0:
                lastSoundThatHit = sound
                totalDamage += target['hp']
                break
            
        
    
    tracks = []
    for sound in sounds:
        toon = sound['toon']
        level = sound['level']
        targets = sound['target']
        hpbonus = sound['hpbonus']
        megaphone = globalPropPool.getProp('megaphone')
        megaphone2 = MovieUtil.copyProp(megaphone)
        megaphones = [
            megaphone,
            megaphone2]
        hands = toon.getRightHands()
        megaphoneIntervals = []
        megaphoneShow = FunctionInterval(MovieUtil.showProps, extraArgs = [
            megaphones,
            hands])
        megaphoneGrow = LerpScaleInterval(megaphone, dMegaphoneGrow, megaphone.getScale(), startScale = Point3(0.01, 0.01, 0.01))
        megaphoneShrink = LerpScaleInterval(megaphone, dMegaphoneShrink, Point3(0.01, 0.01, 0.01), megaphone.getScale())
        megaphoneHide = FunctionInterval(MovieUtil.removeProps, extraArgs = [
            megaphones])
        megaphoneIntervals.append((delay, megaphoneShow))
        megaphoneIntervals.append(megaphoneGrow)
        megaphoneIntervals.append((delay + tMegaphoneShrink, megaphoneShrink))
        megaphoneIntervals.append(megaphoneHide)
        tracks.append(Track(megaphoneIntervals))
        toonIntervals = []
        toonSound = ActorInterval(toon, 'sound')
        toonIntervals.append((delay, toonSound))
        toonIntervals.append(FunctionInterval(toon.loop, extraArgs = [
            'neutral']))
        tracks.append(Track(toonIntervals))
        soundEffect = globalBattleSoundCache.getSound(soundFiles[level])
        if soundEffect:
            soundIntervals = []
            playSound = SoundInterval(soundEffect, node = toon)
            soundIntervals.append((delay + tSound, playSound))
            tracks.append(Track(soundIntervals))
        
        for target in targets:
            suit = target['suit']
            if totalDamage > 0 and sound == lastSoundThatHit:
                hp = target['hp']
                died = target['died']
                battle = sound['battle']
                kbbonus = target['kbbonus']
                suitIntervals = []
                showDamage = FunctionInterval(suit.showLaffNumber, openEnded = 0, extraArgs = [
                    -totalDamage])
                updateHealthBar = FunctionInterval(suit.updateHealthBar, extraArgs = [
                    totalDamage])
                suitIntervals.append((delay + tSuitReact, showDamage))
                suitIntervals.append(updateHealthBar)
                if hitCount == 1:
                    suitIntervals.append(Parallel(ActorInterval(suit, 'squirt-small-react'), MovieUtil.createSuitStunInterval(suit, 0.5, 1.8)))
                else:
                    suitIntervals.append(ActorInterval(suit, 'squirt-small-react'))
                if kbbonus == 0:
                    suitIntervals.append(__createSuitResetPosTrack(suit, battle))
                    suitIntervals.append(Func(battle.unlureSuit, suit))
                
                bonusTrack = None
                if hpbonus > 0:
                    bonusTrack = Track([
                        (delay + tSuitReact + 0.75, FunctionInterval(suit.showLaffNumber, openEnded = 0, extraArgs = [
                            -hpbonus,
                            1]))])
                
                if died != 0:
                    suitIntervals.append(MovieUtil.createSuitDeathTrack(suit, toon, battle))
                else:
                    suitIntervals.append(FunctionInterval(suit.loop, extraArgs = [
                        'neutral']))
                if bonusTrack == None:
                    tracks.append(Track(suitIntervals))
                else:
                    tracks.append(MultiTrack([
                        Track(suitIntervals),
                        bonusTrack]))
            elif totalDamage <= 0:
                tracks.append(Track([
                    (2.8999999999999999, FunctionInterval(MovieUtil.indicateMissed, extraArgs = [
                        suit,
                        1.0]))]))
            
        
    
    return tracks


def __createSuitResetPosTrack(suit, battle):
    (resetPos, resetHpr) = battle.getActorPosHpr(suit)
    moveDist = Vec3(suit.getPos(battle) - resetPos).length()
    moveDuration = 0.5
    walkTrack = Track([
        FunctionInterval(suit.setHpr, extraArgs = [
            battle,
            resetHpr]),
        ActorInterval(suit, 'walk', startTime = 1, duration = moveDuration, endTime = 0.0001),
        FunctionInterval(suit.loop, extraArgs = [
            'neutral'])])
    moveTrack = Track([
        LerpPosInterval(suit, moveDuration, resetPos, other = battle)])
    return MultiTrack([
        walkTrack,
        moveTrack])

