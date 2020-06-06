# File: M (Python 2.2)

from IntervalGlobal import *
from BattleBase import *
from BattleProps import *
from BattleSounds import *
from AvatarDNA import *
import MovieUtil
import MovieCamera
import DirectNotifyGlobal
import BattleParticles
import Toon
notify = DirectNotifyGlobal.directNotify.newCategory('MovieSquirt')
hitSoundFiles = ('AA_squirt_flowersquirt.mp3', 'AA_squirt_glasswater.mp3', 'AA_squirt_neonwatergun.mp3', 'AA_squirt_seltzer.mp3', 'firehose_spray.mp3', 'AA_throw_stormcloud.mp3')
missSoundFiles = ('AA_squirt_flowersquirt_miss.mp3', 'AA_squirt_glasswater_miss.mp3', 'AA_squirt_neonwatergun_miss.mp3', 'AA_squirt_seltzer_miss.mp3', 'firehose_spray.mp3', 'AA_throw_stormcloud_miss.mp3')
sprayScales = [
    0.20000000000000001,
    0.29999999999999999,
    0.10000000000000001,
    0.59999999999999998,
    0.80000000000000004,
    1.0]
WaterSprayColor = Point4(0.75, 0.75, 1.0, 0.80000000000000004)

def doSquirts(squirts):
    if len(squirts) == 0:
        return (None, None)
    
    suitSquirtsDict = { }
    for squirt in squirts:
        suitId = squirt['target']['suit'].doId
        if suitSquirtsDict.has_key(suitId):
            suitSquirtsDict[suitId].append(squirt)
        else:
            suitSquirtsDict[suitId] = [
                squirt]
    
    suitSquirts = suitSquirtsDict.values()
    
    def compFunc(a, b):
        if len(a) > len(b):
            return 1
        elif len(a) < len(b):
            return -1
        
        return 0

    suitSquirts.sort(compFunc)
    delay = 0.0
    tracks = []
    for st in suitSquirts:
        if len(st) > 0:
            ival = __doSuitSquirts(st)
            if ival:
                tracks.append(Track([
                    (delay, ival)]))
            
            delay = delay + TOON_SQUIRT_SUIT_DELAY
        
    
    mtrack = MultiTrack(tracks)
    camDuration = mtrack.getDuration()
    camTrack = MovieCamera.chooseSquirtShot(squirts, suitSquirtsDict, camDuration)
    return (mtrack, camTrack)


def __doSuitSquirts(squirts):
    toonTracks = []
    delay = 0.0
    if len(squirts) == 1 and squirts[0]['target']['hp'] > 0:
        fShowStun = 1
    else:
        fShowStun = 0
    for s in squirts:
        tracks = __doSquirt(s, delay, fShowStun)
        if tracks:
            for track in tracks:
                toonTracks.append(track)
            
        
        delay = delay + TOON_SQUIRT_DELAY
    
    return MultiTrack(toonTracks)


def __doSquirt(squirt, delay, fShowStun):
    notify.debug('toon: %s squirts prop: %d at suit: %d for hp: %d' % (squirt['toon'].getName(), squirt['level'], squirt['target']['suit'].doId, squirt['target']['hp']))
    waitTrack = Track([
        WaitInterval(delay)])
    attackMTrack = squirtfn_array[squirt['level']](squirt, delay, fShowStun)
    return [
        Track([
            waitTrack,
            attackMTrack])]


def __suitTargetPoint(suit):
    pnt = suit.getPos()
    pnt.setZ(pnt[2] + suit.getHeight() * 0.66000000000000003)
    return Point3(pnt)


def __getSplashTrack(point, scale, delay, battle, splashHold = 0.01):
    
    def prepSplash(splash, point):
        if callable(point):
            point = point()
        
        splash.reparentTo(render)
        splash.setPos(point)
        scale = splash.getScale()
        splash.setBillboardPointWorld()
        splash.setScale(scale)

    splash = globalPropPool.getProp('splash-from-splat')
    splash.setScale(scale)
    return Track([
        FunctionInterval(battle.movie.needRestoreRenderProp, extraArgs = [
            splash]),
        (delay, FunctionInterval(prepSplash, extraArgs = [
            splash,
            point])),
        ActorInterval(splash, 'splash-from-splat'),
        WaitInterval(splashHold),
        FunctionInterval(MovieUtil.removeProp, extraArgs = [
            splash]),
        FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
            splash])])


def __getSuitTrack(suit, tContact, tDodge, hp, hpbonus, kbbonus, anim, died, leftSuits, rightSuits, battle, toon, fShowStun, beforeStun = 0.5, afterStun = 1.8):
    if hp > 0:
        suitIvals = []
        sival = ActorInterval(suit, anim)
        sival = []
        if kbbonus > 0:
            (suitPos, suitHpr) = battle.getActorPosHpr(suit)
            suitType = getSuitBodyType(suit.getStyleName())
            animIvals = []
            animIvals.append(ActorInterval(suit, anim, duration = 0.20000000000000001))
            if suitType == 'a':
                animIvals.append(ActorInterval(suit, 'slip-forward', startTime = 2.4300000000000002))
            elif suitType == 'b':
                animIvals.append(ActorInterval(suit, 'slip-forward', startTime = 1.9399999999999999, duration = 1.03))
            elif suitType == 'c':
                animIvals.append(ActorInterval(suit, 'slip-forward', startTime = 2.5800000000000001))
            
            animIvals.append(Func(battle.unlureSuit, suit))
            animTrack = Track(animIvals)
            moveTrack = Track([
                WaitInterval(0.20000000000000001),
                LerpPosInterval(suit, 0.59999999999999998, pos = suitPos, other = battle)])
            sival = MultiTrack([
                animTrack,
                moveTrack])
        elif fShowStun == 1:
            sival = Parallel(ActorInterval(suit, anim), MovieUtil.createSuitStunInterval(suit, beforeStun, afterStun))
        else:
            sival = ActorInterval(suit, anim)
        showDamage = FunctionInterval(suit.showLaffNumber, openEnded = 0, extraArgs = [
            -hp])
        updateHealthBar = FunctionInterval(suit.updateHealthBar, extraArgs = [
            hp])
        suitIvals.append((tContact, showDamage))
        suitIvals.append(updateHealthBar)
        suitIvals.append(sival)
        bonusTrack = None
        bonusIvals = []
        if kbbonus > 0:
            bonusIvals.append((tContact + 0.75, FunctionInterval(suit.showLaffNumber, openEnded = 0, extraArgs = [
                -kbbonus,
                2])))
        
        if hpbonus > 0:
            if kbbonus > 0:
                bonusIvals.append((0.75, FunctionInterval(suit.showLaffNumber, openEnded = 0, extraArgs = [
                    -hpbonus,
                    1]), PREVIOUS_END))
            else:
                bonusIvals.append((tContact + 0.75, FunctionInterval(suit.showLaffNumber, openEnded = 0, extraArgs = [
                    -hpbonus,
                    1])))
        
        if len(bonusIvals) > 0:
            bonusTrack = Track(bonusIvals)
        
        if died != 0:
            suitIvals.append(MovieUtil.createSuitDeathTrack(suit, toon, battle))
        else:
            suitIvals.append(FunctionInterval(suit.loop, extraArgs = [
                'neutral']))
        if bonusTrack == None:
            return Track(suitIvals)
        else:
            return MultiTrack([
                Track(suitIvals),
                bonusTrack])
    else:
        return MovieUtil.createSuitDodgeMultitrack(tDodge, suit, leftSuits, rightSuits)


def __getSoundTrack(level, hitSuit, delay, node = None):
    if hitSuit:
        soundEffect = globalBattleSoundCache.getSound(hitSoundFiles[level])
    else:
        soundEffect = globalBattleSoundCache.getSound(missSoundFiles[level])
    soundIntervals = []
    if soundEffect:
        soundIntervals.append(WaitInterval(delay))
        soundIntervals.append(SoundInterval(soundEffect, node = node))
    else:
        soundIntervals.append(WaitInterval(0.10000000000000001))
    return Track(soundIntervals)


def __doFlower(squirt, delay, fShowStun):
    toon = squirt['toon']
    level = squirt['level']
    hpbonus = squirt['hpbonus']
    target = squirt['target']
    suit = target['suit']
    hp = target['hp']
    kbbonus = target['kbbonus']
    died = target['died']
    leftSuits = target['leftSuits']
    rightSuits = target['rightSuits']
    battle = squirt['battle']
    suitPos = suit.getPos(battle)
    origHpr = toon.getHpr(battle)
    hitSuit = hp > 0
    scale = sprayScales[level]
    tTotalFlowerToonAnimationTime = 2.5
    tFlowerFirstAppears = 1.0
    dFlowerScaleTime = 0.5
    tSprayStarts = tTotalFlowerToonAnimationTime
    dSprayScale = 0.20000000000000001
    dSprayHold = 0.10000000000000001
    tContact = tSprayStarts + dSprayScale
    tSuitDodges = tTotalFlowerToonAnimationTime
    tracks = []
    button = globalPropPool.getProp('button')
    button2 = MovieUtil.copyProp(button)
    buttons = [
        button,
        button2]
    hands = toon.getLeftHands()
    toonIvals = []
    toonIvals.append(FunctionInterval(MovieUtil.showProps, extraArgs = [
        buttons,
        hands]))
    toonIvals.append(FunctionInterval(toon.headsUp, extraArgs = [
        battle,
        suitPos]))
    toonIvals.append(ActorInterval(toon, 'pushbutton'))
    toonIvals.append(FunctionInterval(MovieUtil.removeProps, extraArgs = [
        buttons]))
    toonIvals.append(FunctionInterval(toon.loop, extraArgs = [
        'neutral']))
    toonIvals.append(FunctionInterval(toon.setHpr, extraArgs = [
        battle,
        origHpr]))
    tracks.append(Track(toonIvals))
    tracks.append(__getSoundTrack(level, hitSuit, tTotalFlowerToonAnimationTime - 0.40000000000000002, toon))
    flower = globalPropPool.getProp('squirting-flower')
    flower.setScale(1.5, 1.5, 1.5)
    
    targetPoint = lambda suit = suit: __suitTargetPoint(suit)
    
    def getSprayStartPos(flower = flower):
        toon.update(0)
        return flower.getPos(render)

    sprayIvals = MovieUtil.getSprayIntervals(battle, WaterSprayColor, getSprayStartPos, targetPoint, dSprayScale, dSprayHold, dSprayScale, horizScale = scale, vertScale = scale)
    lodnames = toon.getLODNames()
    toonlod0 = toon.getLOD(lodnames[0])
    toonlod1 = toon.getLOD(lodnames[1])
    flower_joint0 = toonlod0.find('**/joint-attachFlower')
    flower_joint1 = toonlod1.find('**/joint-attachFlower')
    flower_jointpath0 = flower_joint0.attachNewNode('attachFlower-InstanceNode')
    flower_jointpath1 = flower_jointpath0.instanceTo(flower_joint1)
    flowerIntervals = [
        WaitInterval(tFlowerFirstAppears),
        FunctionInterval(flower.reparentTo, extraArgs = [
            flower_jointpath0]),
        LerpScaleInterval(flower, dFlowerScaleTime, flower.getScale(), startScale = MovieUtil.PNT3_NEARZERO),
        WaitInterval(tTotalFlowerToonAnimationTime - dFlowerScaleTime - tFlowerFirstAppears)]
    flowerIntervals.append(WaitInterval(0.5))
    flowerIntervals.extend(sprayIvals)
    flowerIntervals.append(LerpScaleInterval(flower, dFlowerScaleTime, MovieUtil.PNT3_NEARZERO))
    flowerIntervals.append(FunctionInterval(flower_jointpath1.removeNode, extraArgs = []))
    flowerIntervals.append(FunctionInterval(flower_jointpath0.removeNode, extraArgs = []))
    flowerIntervals.append(FunctionInterval(MovieUtil.removeProp, extraArgs = [
        flower]))
    tracks.append(Track(flowerIntervals))
    if hp > 0:
        tracks.append(__getSplashTrack(targetPoint, scale, tSprayStarts + dSprayScale, battle))
    
    if hp > 0 or delay <= 0:
        tracks.append(__getSuitTrack(suit, tContact, tSuitDodges, hp, hpbonus, kbbonus, 'squirt-small-react', died, leftSuits, rightSuits, battle, toon, fShowStun))
    
    return MultiTrack(tracks)


def __doWaterGlass(squirt, delay, fShowStun):
    toon = squirt['toon']
    level = squirt['level']
    hpbonus = squirt['hpbonus']
    target = squirt['target']
    suit = target['suit']
    hp = target['hp']
    kbbonus = target['kbbonus']
    died = target['died']
    leftSuits = target['leftSuits']
    rightSuits = target['rightSuits']
    battle = squirt['battle']
    suitPos = suit.getPos(battle)
    origHpr = toon.getHpr(battle)
    hitSuit = hp > 0
    scale = sprayScales[level]
    dGlassHold = 5.0
    dGlassScale = 0.5
    tSpray = 82.0 / toon.getFrameRate('spit')
    sprayPoseFrame = 88
    dSprayScale = 0.10000000000000001
    dSprayHold = 0.10000000000000001
    tContact = tSpray + dSprayScale
    tSuitDodges = max(tSpray - 0.5, 0.0)
    tracks = []
    toonIntervals = [
        ActorInterval(toon, 'spit')]
    tracks.append(Track(toonIntervals))
    soundTrack = __getSoundTrack(level, hitSuit, 1.7, toon)
    tracks.append(soundTrack)
    glass = globalPropPool.getProp('glass')
    hands = toon.getRightHands()
    hand_jointpath0 = hands[0].attachNewNode('handJoint0-path')
    hand_jointpath1 = hand_jointpath0.instanceTo(hands[1])
    glassIntervals = [
        FunctionInterval(MovieUtil.showProp, extraArgs = [
            glass,
            hand_jointpath0]),
        ActorInterval(glass, 'glass'),
        FunctionInterval(hand_jointpath1.removeNode, extraArgs = []),
        FunctionInterval(hand_jointpath0.removeNode, extraArgs = []),
        FunctionInterval(MovieUtil.removeProp, extraArgs = [
            glass])]
    tracks.append(Track(glassIntervals))
    
    targetPoint = lambda suit = suit: __suitTargetPoint(suit)
    
    def getSprayStartPos(toon = toon):
        toon.update(0)
        lod0 = toon.getLOD(toon.getLODNames()[0])
        joint = lod0.find('**/joint-head')
        n = hidden.attachNewNode('pointInFrontOfHead')
        n.reparentTo(toon)
        n.setPos(joint.getPos(toon) + Point3(0, 0.29999999999999999, -0.20000000000000001))
        p = n.getPos(render)
        n.removeNode()
        del n
        return p

    sprayIvals = MovieUtil.getSprayIntervals(battle, WaterSprayColor, getSprayStartPos, targetPoint, dSprayScale, dSprayHold, dSprayScale, horizScale = scale, vertScale = scale)
    tracks.append(Track([
        WaitInterval(tSpray)] + sprayIvals))
    if hp > 0:
        tracks.append(__getSplashTrack(targetPoint, scale, tSpray + dSprayScale, battle))
    
    if hp > 0 or delay <= 0:
        tracks.append(__getSuitTrack(suit, tContact, tSuitDodges, hp, hpbonus, kbbonus, 'squirt-small-react', died, leftSuits, rightSuits, battle, toon, fShowStun))
    
    return MultiTrack(tracks)


def __doWaterGun(squirt, delay, fShowStun):
    toon = squirt['toon']
    level = squirt['level']
    hpbonus = squirt['hpbonus']
    target = squirt['target']
    suit = target['suit']
    hp = target['hp']
    kbbonus = target['kbbonus']
    died = target['died']
    leftSuits = target['leftSuits']
    rightSuits = target['rightSuits']
    battle = squirt['battle']
    suitPos = suit.getPos(battle)
    origHpr = toon.getHpr(battle)
    hitSuit = hp > 0
    scale = sprayScales[level]
    tPistol = 0.0
    dPistolScale = 0.5
    dPistolHold = 1.8
    tSpray = 48.0 / toon.getFrameRate('water-gun')
    sprayPoseFrame = 63
    dSprayScale = 0.10000000000000001
    dSprayHold = 0.29999999999999999
    tContact = tSpray + dSprayScale
    tSuitDodges = 1.1000000000000001
    tracks = []
    toonIntervals = [
        FunctionInterval(toon.headsUp, extraArgs = [
            battle,
            suitPos]),
        ActorInterval(toon, 'water-gun'),
        FunctionInterval(toon.loop, extraArgs = [
            'neutral']),
        FunctionInterval(toon.setHpr, extraArgs = [
            battle,
            origHpr])]
    tracks.append(Track(toonIntervals))
    soundTrack = __getSoundTrack(level, hitSuit, 1.8, toon)
    tracks.append(soundTrack)
    pistol = globalPropPool.getProp('water-gun')
    hands = toon.getRightHands()
    hand_jointpath0 = hands[0].attachNewNode('handJoint0-path')
    hand_jointpath1 = hand_jointpath0.instanceTo(hands[1])
    
    targetPoint = lambda suit = suit: __suitTargetPoint(suit)
    
    def getSprayStartPos(pistol = pistol, toon = toon):
        toon.update(0)
        joint = pistol.find('**/joint-nozzle')
        p = joint.getPos(render)
        return p

    sprayIvals = MovieUtil.getSprayIntervals(battle, WaterSprayColor, getSprayStartPos, targetPoint, dSprayScale, dSprayHold, dSprayScale, horizScale = scale, vertScale = scale)
    pistolPos = Point3(0.28000000000000003, 0.10000000000000001, 0.080000000000000002)
    pistolHpr = Point3(-4.7599999999999998, -85.599999999999994, -85.909999999999997)
    pistolIvals = [
        FunctionInterval(MovieUtil.showProp, extraArgs = [
            pistol,
            hand_jointpath0,
            pistolPos,
            pistolHpr]),
        LerpScaleInterval(pistol, dPistolScale, pistol.getScale(), startScale = MovieUtil.PNT3_NEARZERO),
        WaitInterval(tSpray - dPistolScale)]
    pistolIvals.extend(sprayIvals)
    pistolIvals.append(WaitInterval(dPistolHold))
    pistolIvals.append(LerpScaleInterval(pistol, dPistolScale, MovieUtil.PNT3_NEARZERO))
    pistolIvals.append(FunctionInterval(hand_jointpath1.removeNode, extraArgs = []))
    pistolIvals.append(FunctionInterval(hand_jointpath0.removeNode, extraArgs = []))
    pistolIvals.append(FunctionInterval(MovieUtil.removeProp, extraArgs = [
        pistol]))
    tracks.append(Track(pistolIvals))
    if hp > 0:
        tracks.append(__getSplashTrack(targetPoint, 0.29999999999999999, tSpray + dSprayScale, battle))
    
    if hp > 0 or delay <= 0:
        tracks.append(__getSuitTrack(suit, tContact, tSuitDodges, hp, hpbonus, kbbonus, 'squirt-small-react', died, leftSuits, rightSuits, battle, toon, fShowStun))
    
    return MultiTrack(tracks)


def __doSeltzerBottle(squirt, delay, fShowStun):
    toon = squirt['toon']
    level = squirt['level']
    hpbonus = squirt['hpbonus']
    target = squirt['target']
    suit = target['suit']
    hp = target['hp']
    kbbonus = target['kbbonus']
    died = target['died']
    leftSuits = target['leftSuits']
    rightSuits = target['rightSuits']
    battle = squirt['battle']
    suitPos = suit.getPos(battle)
    origHpr = toon.getHpr(battle)
    hitSuit = hp > 0
    scale = sprayScales[level]
    tBottle = 0.0
    dBottleScale = 0.5
    dBottleHold = 3.0
    tSpray = 53.0 / toon.getFrameRate('hold-bottle') + 0.050000000000000003
    dSprayScale = 0.20000000000000001
    dSprayHold = 0.10000000000000001
    tContact = tSpray + dSprayScale
    tSuitDodges = max(tContact - 0.69999999999999996, 0.0)
    tracks = []
    toonIntervals = [
        FunctionInterval(toon.headsUp, extraArgs = [
            battle,
            suitPos]),
        ActorInterval(toon, 'hold-bottle'),
        FunctionInterval(toon.loop, extraArgs = [
            'neutral']),
        FunctionInterval(toon.setHpr, extraArgs = [
            battle,
            origHpr])]
    tracks.append(Track(toonIntervals))
    soundTrack = __getSoundTrack(level, hitSuit, tSpray - 0.10000000000000001, toon)
    tracks.append(soundTrack)
    bottle = globalPropPool.getProp('bottle')
    hands = toon.getRightHands()
    
    targetPoint = lambda suit = suit: __suitTargetPoint(suit)
    
    def getSprayStartPos(bottle = bottle, toon = toon):
        toon.update(0)
        joint = bottle.find('**/joint-toSpray')
        n = hidden.attachNewNode('pointBehindSprayProp')
        n.reparentTo(toon)
        n.setPos(joint.getPos(toon) + Point3(0, -0.40000000000000002, 0))
        p = n.getPos(render)
        n.removeNode()
        del n
        return p

    sprayIvals = MovieUtil.getSprayIntervals(battle, WaterSprayColor, getSprayStartPos, targetPoint, dSprayScale, dSprayHold, dSprayScale, horizScale = scale, vertScale = scale)
    hand_jointpath0 = hands[0].attachNewNode('handJoint0-path')
    hand_jointpath1 = hand_jointpath0.instanceTo(hands[1])
    bottleIntervals = [
        FunctionInterval(MovieUtil.showProp, extraArgs = [
            bottle,
            hand_jointpath0]),
        LerpScaleInterval(bottle, dBottleScale, bottle.getScale(), startScale = MovieUtil.PNT3_NEARZERO),
        WaitInterval(tSpray - dBottleScale)]
    bottleIntervals.extend(sprayIvals)
    bottleIntervals.append(WaitInterval(dBottleHold))
    bottleIntervals.append(LerpScaleInterval(bottle, dBottleScale, MovieUtil.PNT3_NEARZERO))
    bottleIntervals.append(FunctionInterval(hand_jointpath1.removeNode, extraArgs = []))
    bottleIntervals.append(FunctionInterval(hand_jointpath0.removeNode, extraArgs = []))
    bottleIntervals.append(FunctionInterval(MovieUtil.removeProp, extraArgs = [
        bottle]))
    tracks.append(Track(bottleIntervals))
    if hp > 0:
        tracks.append(__getSplashTrack(targetPoint, scale, tSpray + dSprayScale, battle))
    
    if hp > 0 or delay <= 0:
        tracks.append(__getSuitTrack(suit, tContact, tSuitDodges, hp, hpbonus, kbbonus, 'squirt-small-react', died, leftSuits, rightSuits, battle, toon, fShowStun))
    
    return MultiTrack(tracks)


def __doFireHose(squirt, delay, fShowStun):
    toon = squirt['toon']
    level = squirt['level']
    hpbonus = squirt['hpbonus']
    target = squirt['target']
    suit = target['suit']
    hp = target['hp']
    kbbonus = target['kbbonus']
    died = target['died']
    leftSuits = target['leftSuits']
    rightSuits = target['rightSuits']
    battle = squirt['battle']
    suitPos = suit.getPos(battle)
    origHpr = toon.getHpr(battle)
    hitSuit = hp > 0
    scale = 0.29999999999999999
    tAppearDelay = 0.69999999999999996
    dHoseHold = 0.69999999999999996
    dAnimHold = 5.0999999999999996
    tSprayDelay = 2.7999999999999998
    tSpray = 0.20000000000000001
    dSprayScale = 0.10000000000000001
    dSprayHold = 1.8
    tContact = 2.8999999999999999
    tSuitDodges = 2.1000000000000001
    tracks = []
    toonIntervals = [
        WaitInterval(tAppearDelay),
        FunctionInterval(toon.headsUp, extraArgs = [
            battle,
            suitPos]),
        ActorInterval(toon, 'firehose'),
        FunctionInterval(toon.loop, extraArgs = [
            'neutral']),
        FunctionInterval(toon.setHpr, extraArgs = [
            battle,
            origHpr])]
    tracks.append(Track(toonIntervals))
    soundTrack = __getSoundTrack(level, hitSuit, tSprayDelay, toon)
    tracks.append(soundTrack)
    hose = globalPropPool.getProp('firehose')
    hydrant = globalPropPool.getProp('hydrant')
    hands = toon.getRightHands()
    scale = Toon.toonBodyScales[toon.style.getAnimal()]
    hydrantPos = toon.getPos()
    hydrantZ = hydrantPos[2]
    hosePos = Point3(hydrantPos)
    hydrantHpr = toon.getHpr()
    hoseHpr = hydrantHpr
    baseHeight = 0
    base = hydrant.find('**/base')
    base.setColor(1, 1, 1, 0.5)
    
    def moveZ(num, hydrantPos = hydrantPos):
        hydrantPos.setZ(hydrantPos.getZ() + num)
        return hydrantPos

    animal = toon.style.getAnimal()
    legs = toon.style.legs
    torso = toon.style.torso
    torso = torso[0]
    if legs == 's':
        if torso == 's':
            pass
        1
        if torso == 'm':
            hydrantZ = -0.25
            baseHeight = baseHeight + 0.25
        elif torso == 'l':
            pass
        
    elif legs == 'm':
        if torso == 's':
            if animal == 'dog' or animal == 'horse':
                hydrantZ = 0.40000000000000002
                baseHeight = baseHeight - 0.40000000000000002
            elif animal == 'cat' or animal == 'rabbit':
                hydrantZ = 0.32000000000000001
                baseHeight = baseHeight - 0.32000000000000001
            elif animal == 'mouse' or animal == 'fowl':
                hydrantZ = 0.26000000000000001
                baseHeight = baseHeight - 0.26000000000000001
            
        elif torso == 'm':
            pass
        elif torso == 'l':
            if animal == 'dog' or animal == 'horse':
                hydrantZ = 0.35999999999999999
                baseHeight = baseHeight - 0.35999999999999999
            elif animal == 'cat' or animal == 'rabbit':
                hydrantZ = 0.32000000000000001
                baseHeight = baseHeight - 0.32000000000000001
            elif animal == 'mouse' or animal == 'fowl':
                hydrantZ = 0.28999999999999998
                baseHeight = baseHeight - 0.28999999999999998
            
        
    elif legs == 'l':
        if torso == 's':
            if animal == 'dog' or animal == 'horse':
                hydrantZ = 1.0600000000000001
                baseHeight = baseHeight - 1.0600000000000001
            elif animal == 'cat' or animal == 'rabbit':
                hydrantZ = 0.93999999999999995
                baseHeight = baseHeight - 0.93999999999999995
            elif animal == 'mouse' or animal == 'fowl':
                hydrantZ = 0.79000000000000004
                baseHeight = baseHeight - 0.79000000000000004
            
        elif torso == 'm':
            if animal == 'dog' or animal == 'horse':
                hydrantZ = 0.73999999999999999
                baseHeight = baseHeight - 0.73999999999999999
            elif animal == 'cat' or animal == 'rabbit':
                hydrantZ = 0.64000000000000001
                baseHeight = baseHeight - 0.64000000000000001
            elif animal == 'mouse' or animal == 'fowl':
                hydrantZ = 0.51000000000000001
                baseHeight = baseHeight - 0.51000000000000001
            
        elif torso == 'l':
            if animal == 'dog' or animal == 'horse':
                hydrantZ = 1.0600000000000001
                baseHeight = baseHeight - 1.0600000000000001
            elif animal == 'cat' or animal == 'rabbit':
                hydrantZ = 0.91000000000000003
                baseHeight = baseHeight - 0.91000000000000003
            elif animal == 'mouse' or animal == 'fowl':
                hydrantZ = 0.76000000000000001
                baseHeight = baseHeight - 0.76000000000000001
            
        
    
    hosePos.setZ(hydrantZ)
    
    targetPoint = lambda suit = suit: __suitTargetPoint(suit)
    
    def getSprayStartPos(hose = hose, toon = toon, targetPoint = targetPoint):
        toon.update(0)
        if hose.isEmpty() == 1:
            if callable(targetPoint):
                return targetPoint()
            else:
                return targetPoint
        
        joint = hose.find('**/joint-water_stream')
        n = hidden.attachNewNode('pointBehindSprayProp')
        n.reparentTo(toon)
        n.setPos(joint.getPos(toon) + Point3(0, -0.55000000000000004, 0))
        p = n.getPos(render)
        n.removeNode()
        del n
        return p

    sprayIvals = []
    sprayIvals.append(WaitInterval(tSprayDelay))
    sprayIvals.extend(MovieUtil.getSprayIntervals(battle, WaterSprayColor, getSprayStartPos, targetPoint, dSprayScale, dSprayHold, dSprayScale, horizScale = scale, vertScale = scale))
    tracks.append(Track(sprayIvals))
    propIvals = [
        Func(battle.movie.needRestoreRenderProp, base),
        Func(battle.movie.needRestoreRenderProp, hydrant),
        Func(base.setPos, hydrantPos),
        Func(base.setHpr, hydrantHpr),
        Func(base.headsUp, battle, suitPos),
        Func(base.setScale, scale),
        Func(base.wrtReparentTo, render),
        Func(base.setZ, battle.getZ()),
        Func(hydrant.reparentTo, base),
        Func(hydrant.setZ, toon, hydrantZ),
        LerpScaleInterval(base, tAppearDelay * 0.5, Point3(scale, scale, scale * 1.3999999999999999), startScale = Point3(scale, scale, 0.01)),
        LerpScaleInterval(base, tAppearDelay * 0.29999999999999999, Point3(scale, scale, scale * 0.80000000000000004), startScale = Point3(scale, scale, scale * 1.3999999999999999)),
        LerpScaleInterval(base, tAppearDelay * 0.10000000000000001, Point3(scale, scale, scale * 1.2), startScale = Point3(scale, scale, scale * 0.80000000000000004)),
        LerpScaleInterval(base, tAppearDelay * 0.10000000000000001, Point3(scale, scale, scale), startScale = Point3(scale, scale, scale * 1.2)),
        Func(battle.movie.needRestoreRenderProp, hose),
        Func(hose.reparentTo, hydrant),
        Func(hose.setPos, 0, 0, 0),
        Func(hose.setHpr, 0, 0, 0),
        Func(hose.setScale, 1, 1, 1),
        FunctionInterval(hose.pose, extraArgs = [
            'firehose',
            2]),
        ActorInterval(hose, 'firehose', duration = dAnimHold),
        WaitInterval(dHoseHold - 0.20000000000000001),
        LerpScaleInterval(base, 0.20000000000000001, Point3(scale, scale, 0.01), startScale = Point3(scale, scale, scale)),
        FunctionInterval(MovieUtil.removeProps, extraArgs = [
            [
                hydrant,
                hose]]),
        FunctionInterval(MovieUtil.removeProps, extraArgs = [
            [
                base]]),
        FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
            hydrant]),
        FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
            hose]),
        FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
            base])]
    tracks.append(Track(propIvals))
    if hp > 0:
        tracks.append(__getSplashTrack(targetPoint, 0.40000000000000002, 2.7000000000000002, battle, splashHold = 1.5))
    
    if hp > 0 or delay <= 0:
        tracks.append(__getSuitTrack(suit, tContact, tSuitDodges, hp, hpbonus, kbbonus, 'squirt-small-react', died, leftSuits, rightSuits, battle, toon, fShowStun))
    
    return MultiTrack(tracks)


def __doStormCloud(squirt, delay, fShowStun):
    toon = squirt['toon']
    level = squirt['level']
    hpbonus = squirt['hpbonus']
    target = squirt['target']
    suit = target['suit']
    hp = target['hp']
    kbbonus = target['kbbonus']
    died = target['died']
    leftSuits = target['leftSuits']
    rightSuits = target['rightSuits']
    battle = squirt['battle']
    suitPos = suit.getPos(battle)
    origHpr = toon.getHpr(battle)
    hitSuit = hp > 0
    scale = sprayScales[level]
    tButton = 0.0
    dButtonScale = 0.5
    dButtonHold = 3.0
    tContact = 2.8999999999999999
    tSpray = 1
    tSuitDodges = 1.8
    tracks = []
    soundTrack = __getSoundTrack(level, hitSuit, 2.2999999999999998, toon)
    soundTrack2 = __getSoundTrack(level, hitSuit, 4.5999999999999996, toon)
    tracks.append(soundTrack)
    tracks.append(soundTrack2)
    button = globalPropPool.getProp('button')
    button2 = MovieUtil.copyProp(button)
    buttons = [
        button,
        button2]
    hands = toon.getLeftHands()
    toonIvals = [
        FunctionInterval(MovieUtil.showProps, extraArgs = [
            buttons,
            hands]),
        FunctionInterval(toon.headsUp, extraArgs = [
            battle,
            suitPos]),
        ActorInterval(toon, 'pushbutton'),
        FunctionInterval(MovieUtil.removeProps, extraArgs = [
            buttons]),
        FunctionInterval(toon.loop, extraArgs = [
            'neutral']),
        FunctionInterval(toon.setHpr, extraArgs = [
            battle,
            origHpr])]
    tracks.append(Track(toonIvals))
    cloud = globalPropPool.getProp('stormcloud')
    cloud2 = MovieUtil.copyProp(cloud)
    BattleParticles.loadParticles()
    trickleEffect = BattleParticles.createParticleEffect(file = 'trickleLiquidate')
    rainEffect = BattleParticles.createParticleEffect(file = 'liquidate')
    rainEffect2 = BattleParticles.createParticleEffect(file = 'liquidate')
    rainEffect3 = BattleParticles.createParticleEffect(file = 'liquidate')
    cloudHeight = suit.height + 3
    cloudPosPoint = Point3(0, 0, cloudHeight)
    scaleUpPoint = Point3(3, 3, 3)
    rainEffects = [
        rainEffect,
        rainEffect2,
        rainEffect3]
    rainDelay = 1
    effectDelay = 0.29999999999999999
    if hp > 0:
        cloudHold = 4.7000000000000002
    else:
        cloudHold = 1.7
    
    def getCloudIvals(cloud, suit, cloudPosPoint, scaleUpPoint, rainEffects, rainDelay, effectDelay, cloudHold, useEffect, battle = battle, trickleEffect = trickleEffect):
        ivals = [
            FunctionInterval(MovieUtil.showProp, extraArgs = [
                cloud,
                suit,
                cloudPosPoint]),
            FunctionInterval(cloud.pose, extraArgs = [
                'stormcloud',
                0]),
            LerpScaleInterval(cloud, 1.5, scaleUpPoint, startScale = MovieUtil.PNT3_NEARZERO),
            WaitInterval(rainDelay)]
        if useEffect == 1:
            pivals = []
            delay = cloudHold * 0.25
            trickleDuration = cloudHold * 0.25
            trickleTrack = Track([
                FunctionInterval(battle.movie.needRestoreParticleEffect, extraArgs = [
                    trickleEffect]),
                ParticleInterval(trickleEffect, cloud, worldRelative = 0, duration = trickleDuration),
                FunctionInterval(battle.movie.clearRestoreParticleEffect, extraArgs = [
                    trickleEffect])])
            ivals.append(trickleTrack)
            for i in range(0, 3):
                dur = cloudHold - 2 * trickleDuration
                pivals.append(Track([
                    FunctionInterval(battle.movie.needRestoreParticleEffect, extraArgs = [
                        rainEffects[i]]),
                    WaitInterval(delay),
                    ParticleInterval(rainEffects[i], cloud, worldRelative = 0, duration = dur),
                    FunctionInterval(battle.movie.clearRestoreParticleEffect, extraArgs = [
                        rainEffects[i]])]))
                delay += effectDelay
            
            pivals.append(Track([
                (3 * effectDelay, ActorInterval(cloud, 'stormcloud', startTime = 1, duration = cloudHold))]))
            ivals.append(MultiTrack(pivals))
        else:
            ivals.append(ActorInterval(cloud, 'stormcloud', startTime = 1, duration = cloudHold))
        ivals.append(LerpScaleInterval(cloud, 0.5, MovieUtil.PNT3_NEARZERO))
        ivals.append(FunctionInterval(MovieUtil.removeProp, extraArgs = [
            cloud]))
        return Track(ivals)

    tracks.append(getCloudIvals(cloud, suit, cloudPosPoint, scaleUpPoint, rainEffects, rainDelay, effectDelay, cloudHold, useEffect = 1))
    tracks.append(getCloudIvals(cloud2, suit, cloudPosPoint, scaleUpPoint, rainEffects, rainDelay, effectDelay, cloudHold, useEffect = 0))
    if hp > 0 or delay <= 0:
        tracks.append(__getSuitTrack(suit, tContact, tSuitDodges, hp, hpbonus, kbbonus, 'soak', died, leftSuits, rightSuits, battle, toon, fShowStun, beforeStun = 2.6000000000000001, afterStun = 2.2999999999999998))
    
    return MultiTrack(tracks)

squirtfn_array = [
    __doFlower,
    __doWaterGlass,
    __doWaterGun,
    __doSeltzerBottle,
    __doFireHose,
    __doStormCloud]
