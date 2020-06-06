# File: P (Python 2.2)

from direct.showbase.PythonUtil import Enum, invertDictLossless
from direct.interval.IntervalGlobal import *
import types
import random
Tricks = Enum('JUMP, BEG, PLAYDEAD, ROLLOVER, BACKFLIP, DANCE, SPEAK, BALK,')
NonHappyMinActualTrickAptitude = 0.10000000000000001
NonHappyMaxActualTrickAptitude = 0.59999999999999998
MinActualTrickAptitude = 0.5
MaxActualTrickAptitude = 0.96999999999999997
AptitudeIncrementDidTrick = 0.00050000000000000001
MaxAptitudeIncrementGotPraise = 0.00029999999999999997
MaxTrickFatigue = 0.65000000000000002
MinTrickFatigue = 0.10000000000000001
ScId2trickId = {
    21200: Tricks.JUMP,
    21201: Tricks.BEG,
    21202: Tricks.PLAYDEAD,
    21203: Tricks.ROLLOVER,
    21204: Tricks.BACKFLIP,
    21205: Tricks.DANCE,
    21206: Tricks.SPEAK }
TrickId2scIds = invertDictLossless(ScId2trickId)
TrickAnims = {
    Tricks.JUMP: 'jump',
    Tricks.BEG: ('toBeg', 'beg', 'fromBeg'),
    Tricks.PLAYDEAD: ('playDead', 'fromPlayDead'),
    Tricks.ROLLOVER: 'rollover',
    Tricks.BACKFLIP: 'backflip',
    Tricks.DANCE: 'dance',
    Tricks.SPEAK: 'speak',
    Tricks.BALK: 'neutral' }
TrickLengths = {
    Tricks.JUMP: 2.0,
    Tricks.BEG: 5.1669999999999998,
    Tricks.PLAYDEAD: 15.210000000000001,
    Tricks.ROLLOVER: 8.0,
    Tricks.BACKFLIP: 4.8799999999999999,
    Tricks.DANCE: 7.4199999999999999,
    Tricks.SPEAK: 0.75,
    Tricks.BALK: 1.0 }
TrickAccuracies = {
    Tricks.JUMP: 1.0,
    Tricks.BEG: 0.90000000000000002,
    Tricks.PLAYDEAD: 0.80000000000000004,
    Tricks.ROLLOVER: 0.69999999999999996,
    Tricks.BACKFLIP: 0.59999999999999998,
    Tricks.DANCE: 0.5,
    Tricks.SPEAK: 0.40000000000000002,
    Tricks.BALK: 1.0 }
TrickHeals = {
    Tricks.JUMP: (5, 10),
    Tricks.BEG: (6, 12),
    Tricks.PLAYDEAD: (7, 14),
    Tricks.ROLLOVER: (8, 16),
    Tricks.BACKFLIP: (9, 18),
    Tricks.DANCE: (10, 20),
    Tricks.SPEAK: (11, 22),
    Tricks.BALK: (0, 0) }
TrickSounds = {
    Tricks.BACKFLIP: 'phase_5/audio/sfx/backflip.mp3',
    Tricks.ROLLOVER: 'phase_5/audio/sfx/rollover.mp3',
    Tricks.PLAYDEAD: 'phase_5/audio/sfx/play_dead.mp3',
    Tricks.BEG: 'phase_5/audio/sfx/beg.mp3',
    Tricks.DANCE: 'phase_5/audio/sfx/heal_dance.mp3',
    Tricks.JUMP: 'phase_5/audio/sfx/jump.mp3',
    Tricks.SPEAK: 'phase_5/audio/sfx/speak_v1.mp3' }

def getSoundIval(trickId):
    sounds = TrickSounds.get(trickId, None)
    if sounds:
        if type(sounds) == types.StringType:
            sound = loader.loadSfx(sounds)
            return SoundInterval(sound)
        else:
            soundIval = Sequence()
            for s in sounds:
                sound = loader.loadSfx(s)
                soundIval.append(SoundInterval(sound))
            
            return soundIval
    
    return None


def getTrickIval(pet, trickId):
    anims = TrickAnims[trickId]
    animRate = random.uniform(0.90000000000000002, 1.1000000000000001)
    waitTime = random.uniform(0.0, 1.0)
    if type(anims) == types.StringType:
        if trickId == Tricks.JUMP:
            animIval = Parallel()
            animIval.append(ActorInterval(pet, anims, playRate = animRate))
            animIval.append(Sequence(Wait(0.35999999999999999), ProjectileInterval(pet, startPos = pet.getPos(), endPos = pet.getPos(), duration = 1.0, gravityMult = 0.5)))
        elif trickId == Tricks.ROLLOVER:
            animIval = Sequence()
            animIval.append(ActorInterval(pet, anims, playRate = animRate))
            animIval.append(ActorInterval(pet, anims, playRate = -1.0 * animRate))
        elif trickId == Tricks.SPEAK:
            animIval = ActorInterval(pet, anims, startFrame = 10, playRate = animRate)
        else:
            animIval = ActorInterval(pet, anims, playRate = animRate)
    else:
        animIval = Sequence()
        for anim in anims:
            animIval.append(ActorInterval(pet, anim, playRate = animRate))
        
    trickIval = Parallel(animIval)
    soundIval = getSoundIval(trickId)
    if soundIval:
        trickIval.append(soundIval)
    
    return Sequence(Func(pet.lockPet), Wait(waitTime), trickIval, Func(pet.unlockPet))

