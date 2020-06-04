# File: M (Python 2.2)

from IntervalGlobal import *
from BattleBase import *
from BattleProps import *
from BattleSounds import *
import MovieUtil
import MovieCamera
import DirectNotifyGlobal
import ToontownBattleGlobals
import Actor
import ParticleEffect
import BattleParticles
import BattleProps
import MovieNPCSOS
notify = DirectNotifyGlobal.directNotify.newCategory('MovieTrap')

def doTraps(traps):
    if len(traps) == 0:
        return (None, None)
    
    (npcArrivals, npcDepartures, npcs) = MovieNPCSOS.doNPCTeleports(traps)
    suitTrapsDict = { }
    for trap in traps:
        targets = trap['target']
        if len(targets) == 1:
            suitId = targets[0]['suit'].doId
            if suitTrapsDict.has_key(suitId):
                suitTrapsDict[suitId].append(trap)
            else:
                suitTrapsDict[suitId] = [
                    trap]
        else:
            for target in targets:
                suitId = target['suit'].doId
                if not suitTrapsDict.has_key(suitId):
                    suitTrapsDict[suitId] = [
                        trap]
                    break
                
            
    
    suitTrapLists = suitTrapsDict.values()
    mtrack = Parallel()
    for trapList in suitTrapLists:
        trapPropList = []
        for i in range(len(trapList)):
            trap = trapList[i]
            level = trap['level']
            if level == 0:
                banana = globalPropPool.getProp('banana')
                banana2 = MovieUtil.copyProp(banana)
                trapPropList.append([
                    banana,
                    banana2])
            elif level == 1:
                rake = globalPropPool.getProp('rake')
                rake2 = MovieUtil.copyProp(rake)
                rake.pose('rake', 0)
                rake2.pose('rake', 0)
                trapPropList.append([
                    rake,
                    rake2])
            elif level == 2:
                marbles = globalPropPool.getProp('marbles')
                marbles2 = MovieUtil.copyProp(marbles)
                trapPropList.append([
                    marbles,
                    marbles2])
            elif level == 3:
                trapPropList.append([
                    globalPropPool.getProp('quicksand')])
            elif level == 4:
                trapPropList.append([
                    globalPropPool.getProp('trapdoor')])
            elif level == 5:
                tnt = globalPropPool.getProp('tnt')
                tnt2 = MovieUtil.copyProp(tnt)
                trapPropList.append([
                    tnt,
                    tnt2])
            else:
                notify.warning('__doTraps() - Incorrect trap level:                 %d' % level)
        
        if len(trapList) == 1:
            ival = __doTrapLevel(trapList[0], trapPropList[0])
            if ival:
                mtrack.append(ival)
            
        else:
            subMtrack = Parallel()
            for i in range(len(trapList)):
                trap = trapList[i]
                trapProps = trapPropList[i]
                ival = __doTrapLevel(trap, trapProps, explode = 1)
                if ival:
                    subMtrack.append(ival)
                
            
            mtrack.append(subMtrack)
    
    trapTrack = Sequence(npcArrivals, mtrack, npcDepartures)
    camDuration = mtrack.getDuration()
    enterDuration = npcArrivals.getDuration()
    exitDuration = npcDepartures.getDuration()
    camTrack = MovieCamera.chooseTrapShot(traps, camDuration, enterDuration, exitDuration)
    return (trapTrack, camTrack)


def __doTrapLevel(trap, trapProps, explode = 0):
    level = trap['level']
    if level == 0:
        return __trapBanana(trap, trapProps, explode)
    elif level == 1:
        return __trapRake(trap, trapProps, explode)
    elif level == 2:
        return __trapMarbles(trap, trapProps, explode)
    elif level == 3:
        return __trapQuicksand(trap, trapProps, explode)
    elif level == 4:
        return __trapTrapdoor(trap, trapProps, explode)
    elif level == 5:
        return __trapTNT(trap, trapProps, explode)
    
    return None


def getSoundTrack(fileName, delay = 0.01, duration = None, node = None):
    soundEffect = globalBattleSoundCache.getSound(fileName)
    if duration:
        return Sequence(Wait(delay), SoundInterval(soundEffect, duration = duration, node = node))
    else:
        return Sequence(Wait(delay), SoundInterval(soundEffect, node = node))


def __createThrownTrapMultiTrack(trap, propList, propName, propPos = None, propHpr = None, anim = 0, explode = 0):
    toon = trap['toon']
    level = trap['level']
    battle = trap['battle']
    target = trap['target']
    suit = target[0]['suit']
    targetPos = suit.getPos(battle)
    thrownProp = propList[0]
    unthrownProp = propList[1]
    torso = toon.style.torso
    torso = torso[0]
    if torso == 'l':
        throwDelay = 2.2999999999999998
    elif torso == 'm':
        throwDelay = 2.2999999999999998
    else:
        throwDelay = 1.8999999999999999
    throwDuration = 0.90000000000000002
    animBreakPoint = throwDelay + throwDuration
    animDelay = 3.1000000000000001
    trapTrack = ToontownBattleGlobals.TRAP_TRACK
    trapTrackNames = ToontownBattleGlobals.AvProps[trapTrack]
    trapName = trapTrackNames[level]
    hands = toon.getRightHands()
    propTrack = Sequence()
    if propPos and propHpr:
        propTrack.append(Func(MovieUtil.showProps, propList, hands, propPos, propHpr))
    else:
        propTrack.append(Func(MovieUtil.showProps, propList, hands))
    if anim == 1:
        pTracks = Parallel()
        for prop in propList:
            pTracks.append(ActorInterval(prop, propName, duration = animBreakPoint))
        
        propTrack.append(pTracks)
    
    throwTrack = Sequence()
    throwTrack.append(Wait(throwDelay))
    throwTrack.append(Func(unthrownProp.reparentTo, hidden))
    throwTrack.append(Func(toon.update))
    if suit.battleTrap != NO_TRAP:
        notify.debug('trapSuit() - trap: %d destroyed existing trap: %d' % (level, suit.battleTrap))
        battle.removeTrap(suit)
    
    if trapName == 'rake':
        trapProp = globalPropPool.getProp('rake-react')
    else:
        trapProp = MovieUtil.copyProp(thrownProp)
    suit.battleTrapProp = trapProp
    suit.battleTrap = level
    suit.battleTrapIsFresh = 1
    if trapName == 'banana':
        (trapPoint, trapHpr) = battle.getActorPosHpr(suit)
        trapPoint.setY(MovieUtil.SUIT_TRAP_DISTANCE)
        slidePoint = Vec3(trapPoint.getX(), trapPoint.getY() - 2, trapPoint.getZ())
        throwingTrack = createThrowingTrack(thrownProp, slidePoint, duration = 0.90000000000000002, parent = battle)
        moveTrack = LerpPosInterval(thrownProp, 0.80000000000000004, pos = trapPoint, other = battle)
        animTrack = ActorInterval(thrownProp, propName, startTime = animBreakPoint)
        slideTrack = Parallel(moveTrack, animTrack)
        motionTrack = Sequence(throwingTrack, slideTrack)
        hprTrack = LerpHprInterval(thrownProp, 1.7, hpr = Point3(0, 0, 0))
        soundTrack = getSoundTrack('TL_banana.mp3', node = toon)
        scaleTrack = LerpScaleInterval(thrownProp, 1.7, scale = MovieUtil.PNT3_ONE)
        throwTrack.append(Wait(0.25))
        throwTrack.append(Func(thrownProp.wrtReparentTo, suit))
        throwTrack.append(Parallel(motionTrack, hprTrack, scaleTrack, soundTrack))
    elif trapName == 'tnt':
        (trapPoint, trapHpr) = battle.getActorPosHpr(suit)
        trapPoint.setY(MovieUtil.SUIT_TRAP_TNT_DISTANCE - 3.8999999999999999)
        trapPoint.setZ(trapPoint.getZ() + 0.40000000000000002)
        throwingTrack = createThrowingTrack(thrownProp, trapPoint, duration = throwDuration, parent = battle)
        hprTrack = LerpHprInterval(thrownProp, 0.90000000000000002, hpr = Point3(0, 90, 0))
        scaleTrack = LerpScaleInterval(thrownProp, 0.90000000000000002, scale = MovieUtil.PNT3_ONE)
        soundTrack = getSoundTrack('TL_dynamite.mp3', delay = 0.80000000000000004, duration = 0.69999999999999996, node = suit)
        throwTrack.append(Wait(0.20000000000000001))
        throwTrack.append(Parallel(throwingTrack, hprTrack, scaleTrack, soundTrack))
    elif trapName == 'marbles':
        (trapPoint, trapHpr) = battle.getActorPosHpr(suit)
        trapPoint.setY(MovieUtil.SUIT_TRAP_MARBLES_DISTANCE)
        flingDuration = 0.20000000000000001
        rollDuration = 1.0
        throwDuration = flingDuration + rollDuration
        landPoint = Point3(0, trapPoint.getY() + 2, trapPoint.getZ())
        throwPoint = Point3(0, trapPoint.getY(), trapPoint.getZ())
        moveTrack = Sequence(Func(thrownProp.wrtReparentTo, suit), Func(thrownProp.setHpr, Point3(94, 0, 0)), LerpPosInterval(thrownProp, flingDuration, pos = landPoint, other = suit), LerpPosInterval(thrownProp, rollDuration, pos = throwPoint, other = suit))
        animTrack = ActorInterval(thrownProp, propName, startTime = throwDelay + 0.90000000000000002)
        scaleTrack = LerpScaleInterval(thrownProp, throwDuration, scale = MovieUtil.PNT3_ONE)
        soundTrack = getSoundTrack('TL_marbles.mp3', delay = 0.10000000000000001, node = toon)
        throwTrack.append(Wait(0.20000000000000001))
        throwTrack.append(Parallel(moveTrack, animTrack, scaleTrack, soundTrack))
    elif trapName == 'rake':
        (trapPoint, trapHpr) = battle.getActorPosHpr(suit)
        trapPoint.setY(MovieUtil.SUIT_TRAP_RAKE_DISTANCE)
        throwDuration = 1.1000000000000001
        throwingTrack = createThrowingTrack(thrownProp, trapPoint, duration = throwDuration, parent = suit)
        hprTrack = LerpHprInterval(thrownProp, throwDuration, hpr = Point3(180, 90, -180))
        scaleTrack = LerpScaleInterval(thrownProp, 0.90000000000000002, scale = Point3(0.69999999999999996, 0.69999999999999996, 0.69999999999999996))
        soundTrack = SoundInterval(globalBattleSoundCache.getSound('TL_rake_throw_only.mp3'), duration = 1.1000000000000001, node = suit)
        throwTrack.append(Wait(0.20000000000000001))
        throwTrack.append(Parallel(throwingTrack, hprTrack, scaleTrack, soundTrack))
    else:
        notify.warning('__createThrownTrapMultiTrack() - Incorrect trap:                          %s thrown from toon' % trapName)
    
    def placeTrap(trapProp, suit, battle = battle, trapName = trapName):
        if not trapProp or trapProp.isEmpty():
            return None
        
        trapProp.wrtReparentTo(suit)
        trapProp.show()
        if trapName == 'rake':
            trapProp.setPos(0, MovieUtil.SUIT_TRAP_RAKE_DISTANCE, 0)
            trapProp.setHpr(Point3(0, 270, 0))
            trapProp.setScale(Point3(0.69999999999999996, 0.69999999999999996, 0.69999999999999996))
            rakeOffset = MovieUtil.getSuitRakeOffset(suit)
            trapProp.setY(trapProp.getY() + rakeOffset)
        elif trapName == 'banana':
            trapProp.setHpr(0, 0, 0)
            trapProp.setPos(0, MovieUtil.SUIT_TRAP_DISTANCE, -0.34999999999999998)
            trapProp.pose(trapName, trapProp.getNumFrames(trapName) - 1)
        elif trapName == 'marbles':
            trapProp.setHpr(Point3(94, 0, 0))
            trapProp.setPos(0, MovieUtil.SUIT_TRAP_MARBLES_DISTANCE, 0)
            trapProp.pose(trapName, trapProp.getNumFrames(trapName) - 1)
        elif trapName == 'tnt':
            trapProp.setHpr(0, 90, 0)
            trapProp.setPos(0, MovieUtil.SUIT_TRAP_TNT_DISTANCE, 0.40000000000000002)
        else:
            notify.warning('placeTrap() - Incorrect trap: %s placed on a suit' % trapName)

    dustNode = hidden.attachNewNode('DustNode')
    
    def placeDustExplosion(dustNode = dustNode, thrownProp = thrownProp, battle = battle):
        dustNode.reparentTo(battle)
        dustNode.setPos(thrownProp.getPos(battle))

    if explode == 1:
        throwTrack.append(Func(thrownProp.wrtReparentTo, hidden))
        throwTrack.append(Func(placeDustExplosion))
        throwTrack.append(createCartoonExplosionTrack(dustNode, 'dust', explosionPoint = Point3(0, 0, 0)))
        throwTrack.append(Func(battle.removeTrap, suit))
    else:
        throwTrack.append(Func(placeTrap, trapProp, suit))
        if trapName == 'tnt':
            tip = trapProp.find('**/joint-attachEmitter')
            sparks = BattleParticles.createParticleEffect(file = 'tnt')
            trapProp.sparksEffect = sparks
            throwTrack.append(Func(sparks.start, tip))
        
    throwTrack.append(Func(MovieUtil.removeProps, propList))
    toonTrack = Sequence(Func(toon.headsUp, battle, targetPos), ActorInterval(toon, 'toss'), Func(toon.loop, 'neutral'))
    return Parallel(propTrack, throwTrack, toonTrack)


def __createPlacedTrapMultiTrack(trap, prop, propName, propPos = None, propHpr = None, explode = 0):
    toon = trap['toon']
    if trap.has_key('npc'):
        toon = trap['npc']
    
    level = trap['level']
    battle = trap['battle']
    origHpr = toon.getHpr(battle)
    trapPoint = Point3(0, MovieUtil.SUIT_TRAP_DISTANCE, 0.025000000000000001)
    trapDelay = 2.5
    hands = toon.getLeftHands()
    
    def placeDustExplosion(dustNode, trapProp, battle):
        dustNode.reparentTo(battle)
        dustNode.setPos(trapProp.getPos(battle))

    trapTracks = Parallel()
    firstTime = 1
    targets = trap['target']
    for target in targets:
        suit = target['suit']
        suitPos = suit.getPos(battle)
        targetPos = suitPos
        trapProp = MovieUtil.copyProp(prop)
        trapTrack = Sequence()
        trapTrack.append(Wait(trapDelay))
        trapTrack.append(Func(trapProp.show))
        trapTrack.append(Func(trapProp.setScale, Point3(0.10000000000000001, 0.10000000000000001, 0.10000000000000001)))
        trapTrack.append(Func(trapProp.reparentTo, suit))
        trapTrack.append(Func(trapProp.setPos, trapPoint))
        trapTrack.append(LerpScaleInterval(trapProp, 1.2, Point3(1.7, 1.7, 1.7)))
        if explode == 1:
            dustNode = hidden.attachNewNode('DustNode')
            trapTrack.append(Func(trapProp.wrtReparentTo, hidden))
            trapTrack.append(Func(placeDustExplosion, dustNode, trapProp, battle))
            trapTrack.append(createCartoonExplosionTrack(dustNode, 'dust', explosionPoint = Point3(0, 0, 0)))
            trapTrack.append(Func(MovieUtil.removeProp, trapProp))
            trapTrack.append(Func(battle.removeTrap, suit))
        elif suit.battleTrap != NO_TRAP:
            notify.debug('trapSuit() - trap: %d destroyed existing trap: %d' % (level, suit.battleTrap))
            battle.removeTrap(suit)
        
        suit.battleTrapProp = trapProp
        suit.battleTrap = level
        suit.battleTrapIsFresh = 1
        trapTracks.append(trapTrack)
    
    button = globalPropPool.getProp('button')
    button2 = MovieUtil.copyProp(button)
    buttons = [
        button,
        button2]
    toonTrack = Sequence()
    toonTrack.append(Func(MovieUtil.showProps, buttons, hands))
    toonTrack.append(Func(toon.headsUp, battle, suitPos))
    toonTrack.append(ActorInterval(toon, 'pushbutton'))
    toonTrack.append(Func(MovieUtil.removeProps, buttons))
    toonTrack.append(Func(toon.loop, 'neutral'))
    toonTrack.append(Func(toon.setHpr, battle, origHpr))
    if propName == 'quicksand':
        propSound = globalBattleSoundCache.getSound('TL_quicksand.mp3')
    else:
        propSound = globalBattleSoundCache.getSound('TL_trap_door.mp3')
    soundTrack = Sequence(Wait(2.2999999999999998), SoundInterval(globalBattleSoundCache.getSound('AA_drop_trigger_box.mp3'), node = toon), Wait(0.29999999999999999), SoundInterval(propSound, duration = 0.5, node = toon))
    return Parallel(trapTracks, toonTrack, soundTrack)


def __trapBanana(trap, trapProps, explode):
    toon = trap['toon']
    suit = trap['target'][0]['suit']
    notify.debug('toon: %s lays banana peel in front of suit: %d' % (toon.getName(), suit.doId))
    bananas = trapProps
    return __createThrownTrapMultiTrack(trap, bananas, 'banana', anim = 1, explode = explode)


def __trapRake(trap, trapProps, explode):
    toon = trap['toon']
    suit = trap['target'][0]['suit']
    notify.debug('toon: %s lays rake in front of suit: %d' % (toon.getName(), suit.doId))
    rakes = trapProps
    return __createThrownTrapMultiTrack(trap, rakes, 'rake', anim = 1, explode = explode)


def __trapMarbles(trap, trapProps, explode):
    toon = trap['toon']
    suit = trap['target'][0]['suit']
    notify.debug('toon: %s lays marbles in front of suit: %d' % (toon.getName(), suit.doId))
    bothMarbles = trapProps
    pos = Point3(0, 0, 0)
    hpr = Point3(0, 0, 30)
    return __createThrownTrapMultiTrack(trap, bothMarbles, 'marbles', pos, hpr, anim = 1, explode = explode)


def __trapQuicksand(trap, trapProps, explode):
    toon = trap['toon']
    suit = trap['target'][0]['suit']
    notify.debug('toon: %s lays quicksand in front of suit: %d' % (toon.getName(), suit.doId))
    quicksand = trapProps[0]
    return __createPlacedTrapMultiTrack(trap, quicksand, 'quicksand', explode = explode)


def __trapTrapdoor(trap, trapProps, explode):
    toon = trap['toon']
    if trap.has_key('npc'):
        toon = trap['npc']
    
    targets = trap['target']
    for target in targets:
        suit = target['suit']
        notify.debug('toon: %s lays trapdoor in front of suit: %d' % (toon.getName(), suit.doId))
    
    trapdoor = trapProps[0]
    return __createPlacedTrapMultiTrack(trap, trapdoor, 'trapdoor', explode = explode)


def __trapTNT(trap, trapProps, explode):
    toon = trap['toon']
    suit = trap['target'][0]['suit']
    notify.debug('toon: %s lays TNT in front of suit: %d' % (toon.getName(), suit.doId))
    tnts = trapProps
    return __createThrownTrapMultiTrack(trap, tnts, 'tnt', anim = 0, explode = explode)


def createThrowingTrack(object, target, duration = 1.0, parent = render, gravity = -32.143999999999998):
    values = { }
    values['origin'] = None
    values['velocity'] = None
    
    def calcOriginAndVelocity(object = object, target = target, values = values, duration = duration, parent = parent, gravity = gravity):
        object.wrtReparentTo(parent)
        values['origin'] = object.getPos(parent)
        origin = object.getPos(parent)
        values['velocity'] = (target[2] - origin[2] - 0.5 * gravity * duration * duration) / duration

    
    def throwPos(t, object, duration, target, values = values, gravity = -32.143999999999998):
        if values['origin'] != None:
            origin = values['origin']
        else:
            origin = object.getPos()
        if values['velocity'] != None:
            velocity = values['velocity']
        else:
            velocity = 16
        x = origin[0] * (1 - t) + target[0] * t
        y = origin[1] * (1 - t) + target[1] * t
        time = t * duration
        z = origin[2] + velocity * time + 0.5 * gravity * time * time
        object.setPos(x, y, z)

    return Sequence(Func(calcOriginAndVelocity), LerpFunctionInterval(throwPos, fromData = 0.0, toData = 1.0, duration = duration, extraArgs = [
        object,
        duration,
        target]))


def createCartoonExplosionTrack(parent, animName, explosionPoint = None):
    explosionTrack = Sequence()
    explosion = BattleProps.globalPropPool.getProp(animName)
    explosion.setBillboardPointEye()
    if not explosionPoint:
        explosionPoint = Point3(0, 3.6000000000000001, 2.1000000000000001)
    
    if animName == 'dust':
        scale = Point3(0.10000000000000001, 0.90000000000000002, 1)
    
    explosionTrack.append(Func(explosion.reparentTo, parent))
    explosionTrack.append(Func(explosion.setPos, explosionPoint))
    explosionTrack.append(Func(explosion.setScale, scale))
    explosionTrack.append(ActorInterval(explosion, animName))
    explosionTrack.append(Func(MovieUtil.removeProp, explosion))
    return explosionTrack

