# File: M (Python 2.2)

from direct.interval.IntervalGlobal import *
from BattleBase import *
from BattleProps import *
from BattleSounds import *
import MovieCamera
from direct.directnotify import DirectNotifyGlobal
import MovieUtil
import MovieNPCSOS
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
    
    (npcArrivals, npcDepartures, npcs) = MovieNPCSOS.doNPCTeleports(sounds)
    mtrack = Parallel()
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
            mtrack.append(__doSoundsLevel(soundList, delay, hitCount, npcs))
            delay += TOON_SOUND_DELAY
        
    
    soundTrack = Sequence(npcArrivals, mtrack, npcDepartures)
    targets = sounds[0]['target']
    camDuration = mtrack.getDuration()
    enterDuration = npcArrivals.getDuration()
    exitDuration = npcDepartures.getDuration()
    camTrack = MovieCamera.chooseSoundShot(sounds, targets, camDuration, enterDuration, exitDuration)
    return (soundTrack, camTrack)


def __doSoundsLevel(sounds, delay, hitCount, npcs):
    lastSoundThatHit = None
    totalDamage = 0
    for sound in sounds:
        for target in sound['target']:
            if target['hp'] > 0:
                lastSoundThatHit = sound
                totalDamage += target['hp']
                break
            
        
    
    tracks = Parallel()
    for sound in sounds:
        toon = sound['toon']
        if sound.has_key('npc'):
            toon = sound['npc']
        
        level = sound['level']
        targets = sound['target']
        hpbonus = sound['hpbonus']
        megaphone = globalPropPool.getProp('megaphone')
        megaphone2 = MovieUtil.copyProp(megaphone)
        megaphones = [
            megaphone,
            megaphone2]
        hands = toon.getRightHands()
        megaphoneShow = Func(MovieUtil.showProps, megaphones, hands)
        megaphoneGrow = LerpScaleInterval(megaphone, dMegaphoneGrow, megaphone.getScale(), startScale = Point3(0.01, 0.01, 0.01))
        megaphoneShrink = LerpScaleInterval(megaphone, dMegaphoneShrink, Point3(0.01, 0.01, 0.01), megaphone.getScale())
        megaphoneHide = Func(MovieUtil.removeProps, megaphones)
        megaphoneTrack = Sequence(Wait(delay), megaphoneShow, Parallel(megaphoneGrow, Sequence(Wait(tMegaphoneShrink), megaphoneShrink)), megaphoneHide)
        tracks.append(megaphoneTrack)
        toonTrack = Sequence(Wait(delay), ActorInterval(toon, 'sound'), Func(toon.loop, 'neutral'))
        tracks.append(toonTrack)
        soundEffect = globalBattleSoundCache.getSound(soundFiles[level])
        if soundEffect:
            soundTrack = Sequence(Wait(delay + tSound), SoundInterval(soundEffect, node = toon))
            tracks.append(soundTrack)
        
        for target in targets:
            suit = target['suit']
            if totalDamage > 0 and sound == lastSoundThatHit:
                hp = target['hp']
                died = target['died']
                battle = sound['battle']
                kbbonus = target['kbbonus']
                suitTrack = Sequence()
                showDamage = Func(suit.showHpText, -totalDamage, openEnded = 0)
                updateHealthBar = Func(suit.updateHealthBar, totalDamage)
                suitTrack.append(Wait(delay + tSuitReact))
                suitTrack.append(showDamage)
                suitTrack.append(updateHealthBar)
                if hitCount == 1:
                    suitTrack.append(Parallel(ActorInterval(suit, 'squirt-small-react'), MovieUtil.createSuitStunInterval(suit, 0.5, 1.8)))
                else:
                    suitTrack.append(ActorInterval(suit, 'squirt-small-react'))
                if kbbonus == 0:
                    suitTrack.append(__createSuitResetPosTrack(suit, battle))
                    suitTrack.append(Func(battle.unlureSuit, suit))
                
                bonusTrack = None
                if hpbonus > 0:
                    bonusTrack = Sequence(Wait(delay + tSuitReact + 0.75), Func(suit.showHpText, -hpbonus, 1, openEnded = 0))
                
                if died != 0:
                    suitTrack.append(MovieUtil.createSuitDeathTrack(suit, toon, battle, npcs))
                else:
                    suitTrack.append(Func(suit.loop, 'neutral'))
                if bonusTrack == None:
                    tracks.append(suitTrack)
                else:
                    tracks.append(Parallel(suitTrack, bonusTrack))
            elif totalDamage <= 0:
                tracks.append(Sequence(Wait(2.8999999999999999), Func(MovieUtil.indicateMissed, suit, 1.0)))
            
        
    
    return tracks


def __createSuitResetPosTrack(suit, battle):
    (resetPos, resetHpr) = battle.getActorPosHpr(suit)
    moveDist = Vec3(suit.getPos(battle) - resetPos).length()
    moveDuration = 0.5
    walkTrack = Sequence(Func(suit.setHpr, battle, resetHpr), ActorInterval(suit, 'walk', startTime = 1, duration = moveDuration, endTime = 0.0001), Func(suit.loop, 'neutral'))
    moveTrack = LerpPosInterval(suit, moveDuration, resetPos, other = battle)
    return Parallel(walkTrack, moveTrack)

