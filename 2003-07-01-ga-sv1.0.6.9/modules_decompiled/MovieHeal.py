# File: M (Python 2.2)

from IntervalGlobal import *
from BattleProps import *
from BattleSounds import *
import DirectNotifyGlobal
import MovieCamera
import whrandom
import MovieUtil
import BattleParticles
import HealJokes
import Localizer
from ToontownBattleGlobals import AvPropDamage
notify = DirectNotifyGlobal.directNotify.newCategory('MovieHeal')
soundFiles = ('AA_heal_tickle.mp3', 'AA_heal_telljoke.mp3', 'AA_heal_smooch.mp3', 'AA_heal_happydance.mp3', 'AA_heal_pixiedust.mp3', 'AA_heal_juggle.mp3')
healPos = Point3(0, 0, 0)
healHpr = Vec3(180.0, 0, 0)
runHealTime = 1.0

def doHeals(heals):
    if len(heals) == 0:
        return (None, None)
    
    ivals = []
    for h in heals:
        ival = __doHealLevel(h)
        if ival:
            ivals.append(ival)
        
    
    mtrack = Track(ivals)
    camDuration = mtrack.getDuration()
    camTrack = MovieCamera.chooseHealShot(heals, camDuration)
    return (mtrack, camTrack)


def __doHealLevel(heal):
    level = heal['level']
    if level == 0:
        return __healTickle(heal)
    elif level == 1:
        return __healJoke(heal)
    elif level == 2:
        return __healSmooch(heal)
    elif level == 3:
        return __healDance(heal)
    elif level == 4:
        return __healSprinkle(heal)
    elif level == 5:
        return __healJuggle(heal)
    
    return None


def __runToHealSpot(heal):
    toon = heal['toon']
    battle = heal['battle']
    level = heal['level']
    (origPos, origHpr) = battle.getActorPosHpr(toon)
    runAnimI = ActorInterval(toon, 'run', duration = runHealTime)
    a = FunctionInterval(toon.headsUp, extraArgs = [
        battle,
        healPos])
    b = MultiTrack([
        Track([
            runAnimI]),
        Track([
            LerpPosInterval(toon, runHealTime, healPos, other = battle)])])
    if level % 2:
        c = FunctionInterval(toon.setHpr, extraArgs = [
            battle,
            healHpr])
    else:
        target = heal['target']['toon']
        targetPos = target.getPos(battle)
        c = FunctionInterval(toon.headsUp, extraArgs = [
            battle,
            targetPos])
    return [
        a,
        b,
        c]


def __returnToBase(heal):
    toon = heal['toon']
    battle = heal['battle']
    (origPos, origHpr) = battle.getActorPosHpr(toon)
    runAnimI = ActorInterval(toon, 'run', duration = runHealTime)
    a = FunctionInterval(toon.headsUp, extraArgs = [
        battle,
        origPos])
    b = MultiTrack([
        Track([
            runAnimI]),
        Track([
            LerpPosInterval(toon, runHealTime, origPos, other = battle)])])
    c = FunctionInterval(toon.setHpr, extraArgs = [
        battle,
        origHpr])
    d = FunctionInterval(toon.loop, extraArgs = [
        'neutral'])
    return [
        a,
        b,
        c,
        d]


def __healToon(toon, hp, ineffective):
    notify.debug('healToon() - toon: %d hp: %d ineffective: %d' % (toon.doId, hp, ineffective))
    if ineffective == 1:
        laughter = whrandom.choice(Localizer.MovieHealLaughterMisses)
    else:
        maxDam = AvPropDamage[0][1][0][1]
        if hp >= maxDam - 1:
            laughter = whrandom.choice(Localizer.MovieHealLaughterHits2)
        else:
            laughter = whrandom.choice(Localizer.MovieHealLaughterHits1)
    toon.setChatAbsolute(laughter, CFSpeech | CFTimeout)
    if hp > 0 and toon.hp != None:
        toon.setHp(min(toon.maxHp, toon.hp + hp))
    else:
        notify.debug('__healToon() - toon: %d hp: %d' % (toon.doId, hp))


def __getPartTrack(particleEffect, startDelay, durationDelay, partExtraArgs):
    pEffect = partExtraArgs[0]
    parent = partExtraArgs[1]
    if len(partExtraArgs) == 3:
        worldRelative = partExtraArgs[2]
    else:
        worldRelative = 1
    return Track([
        (startDelay, ParticleInterval(pEffect, parent, worldRelative, loop = 0, duration = durationDelay))])


def __getSoundTrack(level, delay, duration = None, node = None):
    soundEffect = globalBattleSoundCache.getSound(soundFiles[level])
    soundIntervals = []
    if soundEffect:
        if duration:
            playSound = SoundInterval(soundEffect, duration = duration, node = node)
        else:
            playSound = SoundInterval(soundEffect, node = node)
        soundIntervals.append((delay, playSound))
    else:
        soundIntervals.append(WaitInterval(0.10000000000000001))
    return Track(soundIntervals)


def __healTickle(heal):
    toon = heal['toon']
    target = heal['target']['toon']
    hp = heal['target']['hp']
    ineffective = heal['sidestep']
    level = heal['level']
    ivals = __runToHealSpot(heal)
    feather = globalPropPool.getProp('feather')
    feather2 = MovieUtil.copyProp(feather)
    feathers = [
        feather,
        feather2]
    hands = toon.getRightHands()
    
    def scaleFeathers(feathers, toon = toon, target = target):
        toon.pose('tickle', 63)
        toon.update(0)
        hand = toon.getRightHands()[0]
        horizDistance = Vec3(hand.getPos(render) - target.getPos(render))
        horizDistance.setZ(0)
        distance = horizDistance.length()
        if target.style.torso[0] == 's':
            distance -= 0.5
        else:
            distance -= 0.29999999999999999
        featherLen = 2.3999999999999999
        scale = distance / featherLen * hand.getScale(render)[0]
        for feather in feathers:
            feather.setScale(scale)
        

    tFeatherScaleUp = 0.5
    dFeatherScaleUp = 0.5
    dFeatherScaleDown = 0.5
    featherTrack = MultiTrack([
        MovieUtil.getActorIntervals(feathers, 'feather'),
        Track([
            WaitInterval(tFeatherScaleUp),
            FunctionInterval(MovieUtil.showProps, extraArgs = [
                feathers,
                hands]),
            FunctionInterval(scaleFeathers, extraArgs = [
                feathers]),
            MovieUtil.getScaleIntervals(feathers, dFeatherScaleUp, MovieUtil.PNT3_NEARZERO, feathers[0].getScale)]),
        Track([
            WaitInterval(toon.getDuration('tickle') - dFeatherScaleDown),
            MovieUtil.getScaleIntervals(feathers, dFeatherScaleDown, None, MovieUtil.PNT3_NEARZERO)])])
    tHeal = 3.0
    mtrack = MultiTrack([
        featherTrack,
        Track([
            ActorInterval(toon, 'tickle')]),
        __getSoundTrack(level, 1, node = toon),
        Track([
            (tHeal, FunctionInterval(__healToon, extraArgs = [
                target,
                hp,
                ineffective])),
            ActorInterval(target, 'cringe', startTime = 20.0 / target.getFrameRate('cringe'))])])
    ivals.append(mtrack)
    ivals.append(FunctionInterval(MovieUtil.removeProps, extraArgs = [
        feathers]))
    ivals += __returnToBase(heal)
    ivals.append(FunctionInterval(target.clearChat))
    return Track(ivals)


def __healJoke(heal):
    toon = heal['toon']
    targets = heal['target']
    ineffective = heal['sidestep']
    level = heal['level']
    jokeIndex = heal['hpbonus'] % len(HealJokes.toonHealJokes)
    ivals = __runToHealSpot(heal)
    tracks = []
    fSpeakPunchline = 58
    tSpeakSetup = 0.0
    tSpeakPunchline = 3.0
    dPunchLine = 3.0
    tTargetReact = tSpeakPunchline + 1.0
    dTargetLaugh = 1.5
    tRunBack = tSpeakPunchline + dPunchLine
    tDoSoundAnimation = tSpeakPunchline - float(fSpeakPunchline) / toon.getFrameRate('sound')
    megaphone = globalPropPool.getProp('megaphone')
    megaphone2 = MovieUtil.copyProp(megaphone)
    megaphones = [
        megaphone,
        megaphone2]
    hands = toon.getRightHands()
    dMegaphoneScale = 0.5
    tracks.append(Track([
        WaitInterval(tDoSoundAnimation),
        FunctionInterval(MovieUtil.showProps, extraArgs = [
            megaphones,
            hands]),
        MovieUtil.getScaleIntervals(megaphones, dMegaphoneScale, MovieUtil.PNT3_NEARZERO, MovieUtil.PNT3_ONE),
        WaitInterval(toon.getDuration('sound') - 2.0 * dMegaphoneScale),
        MovieUtil.getScaleIntervals(megaphones, dMegaphoneScale, MovieUtil.PNT3_ONE, MovieUtil.PNT3_NEARZERO),
        FunctionInterval(MovieUtil.removeProps, extraArgs = [
            megaphones])]))
    tracks.append(Track([
        WaitInterval(tDoSoundAnimation),
        ActorInterval(toon, 'sound')]))
    soundTrack = __getSoundTrack(level, 2.0, node = toon)
    tracks.append(soundTrack)
    joke = HealJokes.toonHealJokes[jokeIndex]
    tracks.append(Track([
        WaitInterval(tSpeakSetup),
        FunctionInterval(toon.setChatAbsolute, extraArgs = [
            joke[0],
            CFSpeech | CFTimeout])]))
    tracks.append(Track([
        WaitInterval(tSpeakPunchline),
        FunctionInterval(toon.setChatAbsolute, extraArgs = [
            joke[1],
            CFSpeech | CFTimeout])]))
    reactIvals = [
        WaitInterval(tTargetReact)]
    for target in targets:
        targetToon = target['toon']
        hp = target['hp']
        reactIvals.append(FunctionInterval(__healToon, extraArgs = [
            targetToon,
            hp,
            ineffective]))
    
    reactIvals.append(WaitInterval(dTargetLaugh))
    for target in targets:
        targetToon = target['toon']
        reactIvals.append(FunctionInterval(targetToon.clearChat))
    
    tracks.append(Track(reactIvals))
    tracks.append(Track([
        WaitInterval(tRunBack),
        FunctionInterval(toon.clearChat)] + __returnToBase(heal)))
    ivals.append(MultiTrack(tracks))
    return Track(ivals)


def __healSmooch(heal):
    toon = heal['toon']
    target = heal['target']['toon']
    level = heal['level']
    hp = heal['target']['hp']
    ineffective = heal['sidestep']
    ivals = __runToHealSpot(heal)
    lipstick = globalPropPool.getProp('lipstick')
    lipstick2 = MovieUtil.copyProp(lipstick)
    lipsticks = [
        lipstick,
        lipstick2]
    rightHands = toon.getRightHands()
    dScale = 0.5
    lipstickIvals = [
        FunctionInterval(MovieUtil.showProps, extraArgs = [
            lipsticks,
            rightHands,
            Point3(-0.27000000000000002, -0.23999999999999999, -0.94999999999999996),
            Point3(-123.69, 33.689999999999998, -50.710000000000001)]),
        MovieUtil.getScaleIntervals(lipsticks, dScale, MovieUtil.PNT3_NEARZERO, MovieUtil.PNT3_ONE),
        WaitInterval(toon.getDuration('smooch') - 2.0 * dScale),
        MovieUtil.getScaleIntervals(lipsticks, dScale, MovieUtil.PNT3_ONE, MovieUtil.PNT3_NEARZERO),
        FunctionInterval(MovieUtil.removeProps, extraArgs = [
            lipsticks])]
    lips = globalPropPool.getProp('lips')
    dScale = 0.5
    tLips = 2.5
    tThrow = 115.0 / toon.getFrameRate('smooch')
    dThrow = 0.5
    
    def getLipPos(toon = toon):
        toon.pose('smooch', 57)
        toon.update(0)
        hand = toon.getRightHands()[0]
        return hand.getPos(render)

    lipsIvals = [
        WaitInterval(tLips),
        FunctionInterval(MovieUtil.showProp, extraArgs = [
            lips,
            render,
            getLipPos]),
        LerpScaleInterval(lips, dScale, Point3(3, 3, 3), startScale = MovieUtil.PNT3_NEARZERO),
        WaitInterval(tThrow - tLips - dScale),
        LerpPosInterval(lips, dThrow, Point3(target.getPos() + Point3(0, 0, target.getHeight()))),
        FunctionInterval(MovieUtil.removeProp, extraArgs = [
            lips])]
    delay = tThrow + dThrow
    mtrack = MultiTrack([
        Track(lipstickIvals),
        Track(lipsIvals),
        __getSoundTrack(level, 2, node = toon),
        Track([
            ActorInterval(toon, 'smooch')] + __returnToBase(heal)),
        Track([
            (delay, ActorInterval(target, 'conked'))]),
        Track([
            (delay, FunctionInterval(__healToon, extraArgs = [
                target,
                hp,
                ineffective]))])])
    ivals.append(mtrack)
    ivals.append(FunctionInterval(target.clearChat))
    return Track(ivals)


def __healDance(heal):
    toon = heal['toon']
    targets = heal['target']
    ineffective = heal['sidestep']
    level = heal['level']
    ivals = __runToHealSpot(heal)
    delay = 3.0
    first = 1
    targetIvals = []
    for target in targets:
        targetToon = target['toon']
        hp = target['hp']
        reactIval = FunctionInterval(__healToon, extraArgs = [
            targetToon,
            hp,
            ineffective])
        if first == 1:
            targetIvals.append((delay, reactIval, PREVIOUS_END))
            first = 0
        else:
            targetIvals.append(reactIval)
    
    hat = globalPropPool.getProp('hat')
    hat2 = MovieUtil.copyProp(hat)
    hats = [
        hat,
        hat2]
    cane = globalPropPool.getProp('cane')
    cane2 = MovieUtil.copyProp(cane)
    canes = [
        cane,
        cane2]
    leftHands = toon.getLeftHands()
    rightHands = toon.getRightHands()
    dScale = 0.5
    propIvals = [
        FunctionInterval(MovieUtil.showProps, extraArgs = [
            hats,
            rightHands,
            Point3(0.23000000000000001, 0.089999999999999997, 0.68999999999999995),
            Point3(180, 0, 0)]),
        FunctionInterval(MovieUtil.showProps, extraArgs = [
            canes,
            leftHands,
            Point3(-0.28000000000000003, 0.0, 0.14000000000000001),
            Point3(0.0, 0.0, 150.0)]),
        MovieUtil.getScaleIntervals(hats + canes, dScale, MovieUtil.PNT3_NEARZERO, MovieUtil.PNT3_ONE),
        WaitInterval(toon.getDuration('happy-dance') - 2.0 * dScale),
        MovieUtil.getScaleIntervals(hats + canes, dScale, MovieUtil.PNT3_ONE, MovieUtil.PNT3_NEARZERO),
        FunctionInterval(MovieUtil.removeProps, extraArgs = [
            hats + canes])]
    mtrack = MultiTrack([
        Track(propIvals),
        Track([
            ActorInterval(toon, 'happy-dance')]),
        __getSoundTrack(level, 0.20000000000000001, duration = 6.4000000000000004, node = toon),
        Track(targetIvals)])
    ivals.append(FunctionInterval(toon.loop, extraArgs = [
        'neutral']))
    ivals.append(WaitInterval(0.10000000000000001))
    ivals.append(mtrack)
    ivals += __returnToBase(heal)
    for target in targets:
        targetToon = target['toon']
        ivals.append(FunctionInterval(targetToon.clearChat))
    
    return Track(ivals)


def __healSprinkle(heal):
    toon = heal['toon']
    target = heal['target']['toon']
    hp = heal['target']['hp']
    ineffective = heal['sidestep']
    level = heal['level']
    ivals = __runToHealSpot(heal)
    sprayEffect = BattleParticles.createParticleEffect(file = 'pixieSpray')
    dropEffect = BattleParticles.createParticleEffect(file = 'pixieDrop')
    explodeEffect = BattleParticles.createParticleEffect(file = 'pixieExplode')
    poofEffect = BattleParticles.createParticleEffect(file = 'pixiePoof')
    wallEffect = BattleParticles.createParticleEffect(file = 'pixieWall')
    
    def face90(toon = toon, target = target):
        vec = Point3(target.getPos() - toon.getPos())
        vec.setZ(0)
        temp = vec[0]
        vec.setX(-vec[1])
        vec.setY(temp)
        targetPoint = Point3(toon.getPos() + vec)
        toon.headsUp(render, targetPoint)

    delay = 2.5
    mtrack = MultiTrack([
        __getPartTrack(sprayEffect, 1.5, 0.5, [
            sprayEffect,
            toon,
            0]),
        __getPartTrack(dropEffect, 1.8999999999999999, 2.0, [
            dropEffect,
            target,
            0]),
        __getPartTrack(explodeEffect, 2.7000000000000002, 1.0, [
            explodeEffect,
            toon,
            0]),
        __getPartTrack(poofEffect, 3.3999999999999999, 1.0, [
            poofEffect,
            target,
            0]),
        __getPartTrack(wallEffect, 4.0499999999999998, 1.2, [
            wallEffect,
            toon,
            0]),
        __getSoundTrack(level, 2, duration = 4.0999999999999996, node = toon),
        Track([
            FunctionInterval(face90),
            ActorInterval(toon, 'sprinkle-dust')]),
        Track([
            (delay, FunctionInterval(__healToon, extraArgs = [
                target,
                hp,
                ineffective]))])])
    ivals.append(mtrack)
    ivals += __returnToBase(heal)
    ivals.append(FunctionInterval(target.clearChat))
    return Track(ivals)


def __healJuggle(heal):
    toon = heal['toon']
    targets = heal['target']
    ineffective = heal['sidestep']
    level = heal['level']
    ivals = __runToHealSpot(heal)
    delay = 4.0
    first = 1
    targetIvals = []
    for target in targets:
        targetToon = target['toon']
        hp = target['hp']
        reactIval = FunctionInterval(__healToon, extraArgs = [
            targetToon,
            hp,
            ineffective])
        if first == 1:
            targetIvals.append((delay, reactIval, PREVIOUS_END))
            first = 0
        else:
            targetIvals.append(reactIval)
    
    cube = globalPropPool.getProp('cubes')
    cube2 = MovieUtil.copyProp(cube)
    cubes = [
        cube,
        cube2]
    hips = [
        toon.getLOD(toon.getLODNames()[0]).find('**/joint-hips'),
        toon.getLOD(toon.getLODNames()[1]).find('**/joint-hips')]
    cubeIvals = [
        FunctionInterval(MovieUtil.showProps, extraArgs = [
            cubes,
            hips]),
        MovieUtil.getActorIntervals(cubes, 'cubes'),
        FunctionInterval(MovieUtil.removeProps, extraArgs = [
            cubes])]
    mtrack = MultiTrack([
        Track(cubeIvals),
        __getSoundTrack(level, 0.69999999999999996, duration = 7.7000000000000002, node = toon),
        Track([
            ActorInterval(toon, 'juggle')]),
        Track(targetIvals)])
    ivals.append(mtrack)
    ivals += __returnToBase(heal)
    for target in targets:
        targetToon = target['toon']
        ivals.append(FunctionInterval(targetToon.clearChat))
    
    return Track(ivals)

