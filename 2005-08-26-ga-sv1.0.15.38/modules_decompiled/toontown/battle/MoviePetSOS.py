# File: M (Python 2.2)

from direct.interval.IntervalGlobal import *
from BattleProps import *
from BattleSounds import *
from direct.directnotify import DirectNotifyGlobal
import MovieCamera
import whrandom
import MovieUtil
import BattleParticles
import HealJokes
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownBattleGlobals
from toontown.pets import Pet, PetTricks
notify = DirectNotifyGlobal.directNotify.newCategory('MoviePetSOS')
soundFiles = ('AA_heal_tickle.mp3', 'AA_heal_telljoke.mp3', 'AA_heal_smooch.mp3', 'AA_heal_happydance.mp3', 'AA_heal_pixiedust.mp3', 'AA_heal_juggle.mp3')
offset = Point3(0, 4.0, 0)

def doPetSOSs(PetSOSs):
    if len(PetSOSs) == 0:
        return (None, None)
    
    track = Sequence()
    textTrack = Sequence()
    for p in PetSOSs:
        ival = __doPetSOS(p)
        if ival:
            track.append(ival)
        
    
    camDuration = track.getDuration()
    camTrack = MovieCamera.chooseHealShot(PetSOSs, camDuration)
    return (track, camTrack)


def __doPetSOS(sos):
    return __healJuggle(sos)


def __healToon(toon, hp, gender, callerToonId, ineffective = 0):
    notify.debug('healToon() - toon: %d hp: %d ineffective: %d' % (toon.doId, hp, ineffective))
    nolaughter = 0
    if ineffective == 1:
        if callerToonId == toon.doId:
            laughter = TTLocalizer.MoviePetSOSTrickFail
        else:
            nolaughter = 1
    else:
        maxDam = ToontownBattleGlobals.AvPropDamage[0][1][0][1]
        if callerToonId == toon.doId:
            if gender == 1:
                laughter = TTLocalizer.MoviePetSOSTrickSucceedBoy
            else:
                laughter = TTLocalizer.MoviePetSOSTrickSucceedGirl
        elif hp >= maxDam - 1:
            laughter = whrandom.choice(TTLocalizer.MovieHealLaughterHits2)
        else:
            laughter = whrandom.choice(TTLocalizer.MovieHealLaughterHits1)
    if nolaughter == 0:
        toon.setChatAbsolute(laughter, CFSpeech | CFTimeout)
    
    if hp > 0 and toon.hp != None:
        toon.toonUp(hp)
    else:
        notify.debug('__healToon() - toon: %d hp: %d' % (toon.doId, hp))


def __teleportIn(attack, pet, pos = Point3(0, 0, 0), hpr = Vec3(180.0, 0.0, 0.0)):
    a = Func(pet.reparentTo, attack['battle'])
    b = Func(pet.setPos, pos)
    c = Func(pet.setHpr, hpr)
    d = Func(pet.pose, 'reappear', 0)
    e = pet.getTeleportInTrack()
    g = Func(pet.loop, 'neutral')
    return Sequence(a, b, c, d, e, g)


def __teleportOut(attack, pet):
    a = pet.getTeleportOutTrack()
    c = Func(pet.reparentTo, hidden)
    return Sequence(a, c)


def __doPet(attack, level, hp):
    track = __doSprinkle(attack, 'suits', hp)
    pbpText = attack['playByPlayText']
    pbpTrack = pbpText.getShowInterval(TTLocalizer.MovieNPCSOSCogsMiss, track.getDuration())
    return (track, pbpTrack)


def __healJuggle(heal):
    petProxyId = heal['petId']
    pet = Pet.Pet()
    gender = 0
    if base.cr.doId2do.has_key(petProxyId):
        petProxy = base.cr.doId2do[petProxyId]
        if petProxy == None:
            return None
        
        pet.setDNA(petProxy.style)
        pet.setName(petProxy.petName)
        gender = petProxy.gender
    else:
        pet.setDNA([
            -1,
            0,
            0,
            -1,
            2,
            0,
            4,
            0,
            1])
        pet.setName('Smiley')
    targets = heal['target']
    ineffective = heal['sidestep']
    level = heal['level']
    track = Sequence(__teleportIn(heal, pet))
    if ineffective:
        trickTrack = Parallel(Wait(1.0), Func(pet.loop, 'neutralSad'), Func(pet.showMood, 'confusion'))
    else:
        trickTrack = PetTricks.getTrickIval(pet, level)
    track.append(trickTrack)
    delay = 4.0
    first = 1
    targetTrack = Sequence()
    for target in targets:
        targetToon = target['toon']
        hp = target['hp']
        callerToonId = heal['toonId']
        reactIval = Func(__healToon, targetToon, hp, gender, callerToonId, ineffective)
        if first == 1:
            first = 0
        
        targetTrack.append(reactIval)
    
    mtrack = Parallel(Wait(2.0), targetTrack)
    track.append(mtrack)
    track.append(Sequence(Func(pet.clearMood)))
    track.append(__teleportOut(heal, pet))
    for target in targets:
        targetToon = target['toon']
        track.append(Func(targetToon.clearChat))
    
    return track

