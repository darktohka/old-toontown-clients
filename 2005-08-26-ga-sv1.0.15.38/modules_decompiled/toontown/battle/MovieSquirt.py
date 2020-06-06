# File: M (Python 2.2)

from direct.interval.IntervalGlobal import *
from BattleBase import *
from BattleProps import *
from BattleSounds import *
from toontown.toon.ToonDNA import *
from toontown.suit.SuitDNA import *
import MovieUtil
import MovieCamera
from direct.directnotify import DirectNotifyGlobal
import BattleParticles
from toontown.toonbase import ToontownGlobals
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
    mtrack = Parallel()
    for st in suitSquirts:
        if len(st) > 0:
            ival = __doSuitSquirts(st)
            if ival:
                mtrack.append(Sequence(Wait(delay), ival))
            
            delay = delay + TOON_SQUIRT_SUIT_DELAY
        
    
    camDuration = mtrack.getDuration()
    camTrack = MovieCamera.chooseSquirtShot(squirts, suitSquirtsDict, camDuration)
    return (mtrack, camTrack)


def __doSuitSquirts(squirts):
    toonTracks = Parallel()
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
    
    return toonTracks


def __doSquirt(squirt, delay, fShowStun):
    notify.debug('toon: %s squirts prop: %d at suit: %d for hp: %d' % (squirt['toon'].getName(), squirt['level'], squirt['target']['suit'].doId, squirt['target']['hp']))
    attackMTrack = squirtfn_array[squirt['level']](squirt, delay, fShowStun)
    return [
        Sequence(Wait(delay), attackMTrack)]


def __suitTargetPoint(suit):
    pnt = suit.getPos(render)
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
    return Sequence(Func(battle.movie.needRestoreRenderProp, splash), Wait(delay), Func(prepSplash, splash, point), ActorInterval(splash, 'splash-from-splat'), Wait(splashHold), Func(MovieUtil.removeProp, splash), Func(battle.movie.clearRenderProp, splash))


def __getSuitTrack(suit, tContact, tDodge, hp, hpbonus, kbbonus, anim, died, leftSuits, rightSuits, battle, toon, fShowStun, beforeStun = 0.5, afterStun = 1.8):
    if hp > 0:
        suitTrack = Sequence()
        sival = ActorInterval(suit, anim)
        sival = []
        if kbbonus > 0:
            (suitPos, suitHpr) = battle.getActorPosHpr(suit)
            suitType = getSuitBodyType(suit.getStyleName())
            animTrack = Sequence()
            animTrack.append(ActorInterval(suit, anim, duration = 0.20000000000000001))
            if suitType == 'a':
                animTrack.append(ActorInterval(suit, 'slip-forward', startTime = 2.4300000000000002))
            elif suitType == 'b':
                animTrack.append(ActorInterval(suit, 'slip-forward', startTime = 1.9399999999999999))
            elif suitType == 'c':
                animTrack.append(ActorInterval(suit, 'slip-forward', startTime = 2.5800000000000001))
            
            animTrack.append(Func(battle.unlureSuit, suit))
            moveTrack = Sequence(Wait(0.20000000000000001), LerpPosInterval(suit, 0.59999999999999998, pos = suitPos, other = battle))
            sival = Parallel(animTrack, moveTrack)
        elif fShowStun == 1:
            sival = Parallel(ActorInterval(suit, anim), MovieUtil.createSuitStunInterval(suit, beforeStun, afterStun))
        else:
            sival = ActorInterval(suit, anim)
        showDamage = Func(suit.showHpText, -hp, openEnded = 0)
        updateHealthBar = Func(suit.updateHealthBar, hp)
        suitTrack.append(Wait(tContact))
        suitTrack.append(showDamage)
        suitTrack.append(updateHealthBar)
        suitTrack.append(sival)
        bonusTrack = Sequence(Wait(tContact))
        if kbbonus > 0:
            bonusTrack.append(Wait(0.75))
            bonusTrack.append(Func(suit.showHpText, -kbbonus, 2, openEnded = 0))
        
        if hpbonus > 0:
            bonusTrack.append(Wait(0.75))
            bonusTrack.append(Func(suit.showHpText, -hpbonus, 1, openEnded = 0))
        
        if died != 0:
            suitTrack.append(MovieUtil.createSuitDeathTrack(suit, toon, battle))
        else:
            suitTrack.append(Func(suit.loop, 'neutral'))
        return Parallel(suitTrack, bonusTrack)
    else:
        return MovieUtil.createSuitDodgeMultitrack(tDodge, suit, leftSuits, rightSuits)


def __getSoundTrack(level, hitSuit, delay, node = None):
    if hitSuit:
        soundEffect = globalBattleSoundCache.getSound(hitSoundFiles[level])
    else:
        soundEffect = globalBattleSoundCache.getSound(missSoundFiles[level])
    soundTrack = Sequence()
    if soundEffect:
        soundTrack.append(Wait(delay))
        soundTrack.append(SoundInterval(soundEffect, node = node))
    
    return soundTrack


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
    tracks = Parallel()
    button = globalPropPool.getProp('button')
    button2 = MovieUtil.copyProp(button)
    buttons = [
        button,
        button2]
    hands = toon.getLeftHands()
    toonTrack = Sequence(Func(MovieUtil.showProps, buttons, hands), Func(toon.headsUp, battle, suitPos), ActorInterval(toon, 'pushbutton'), Func(MovieUtil.removeProps, buttons), Func(toon.loop, 'neutral'), Func(toon.setHpr, battle, origHpr))
    tracks.append(toonTrack)
    tracks.append(__getSoundTrack(level, hitSuit, tTotalFlowerToonAnimationTime - 0.40000000000000002, toon))
    flower = globalPropPool.getProp('squirting-flower')
    flower.setScale(1.5, 1.5, 1.5)
    
    targetPoint = lambda suit = suit: __suitTargetPoint(suit)
    
    def getSprayStartPos(flower = flower):
        toon.update(0)
        return flower.getPos(render)

    sprayTrack = MovieUtil.getSprayTrack(battle, WaterSprayColor, getSprayStartPos, targetPoint, dSprayScale, dSprayHold, dSprayScale, horizScale = scale, vertScale = scale)
    lodnames = toon.getLODNames()
    toonlod0 = toon.getLOD(lodnames[0])
    toonlod1 = toon.getLOD(lodnames[1])
    flower_joint0 = toonlod0.find('**/joint-attachFlower')
    flower_joint1 = toonlod1.find('**/joint-attachFlower')
    flower_jointpath0 = flower_joint0.attachNewNode('attachFlower-InstanceNode')
    flower_jointpath1 = flower_jointpath0.instanceTo(flower_joint1)
    flowerTrack = Sequence(Wait(tFlowerFirstAppears), Func(flower.reparentTo, flower_jointpath0), LerpScaleInterval(flower, dFlowerScaleTime, flower.getScale(), startScale = MovieUtil.PNT3_NEARZERO), Wait(tTotalFlowerToonAnimationTime - dFlowerScaleTime - tFlowerFirstAppears))
    if hp <= 0:
        flowerTrack.append(Wait(0.5))
    
    flowerTrack.append(sprayTrack)
    flowerTrack.append(LerpScaleInterval(flower, dFlowerScaleTime, MovieUtil.PNT3_NEARZERO))
    flowerTrack.append(Func(flower_jointpath1.removeNode))
    flowerTrack.append(Func(flower_jointpath0.removeNode))
    flowerTrack.append(Func(MovieUtil.removeProp, flower))
    tracks.append(flowerTrack)
    if hp > 0:
        tracks.append(__getSplashTrack(targetPoint, scale, tSprayStarts + dSprayScale, battle))
    
    if hp > 0 or delay <= 0:
        tracks.append(__getSuitTrack(suit, tContact, tSuitDodges, hp, hpbonus, kbbonus, 'squirt-small-react', died, leftSuits, rightSuits, battle, toon, fShowStun))
    
    return tracks


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
    tracks = Parallel()
    tracks.append(ActorInterval(toon, 'spit'))
    soundTrack = __getSoundTrack(level, hitSuit, 1.7, toon)
    tracks.append(soundTrack)
    glass = globalPropPool.getProp('glass')
    hands = toon.getRightHands()
    hand_jointpath0 = hands[0].attachNewNode('handJoint0-path')
    hand_jointpath1 = hand_jointpath0.instanceTo(hands[1])
    glassTrack = Sequence(Func(MovieUtil.showProp, glass, hand_jointpath0), ActorInterval(glass, 'glass'), Func(hand_jointpath1.removeNode), Func(hand_jointpath0.removeNode), Func(MovieUtil.removeProp, glass))
    tracks.append(glassTrack)
    
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

    sprayTrack = MovieUtil.getSprayTrack(battle, WaterSprayColor, getSprayStartPos, targetPoint, dSprayScale, dSprayHold, dSprayScale, horizScale = scale, vertScale = scale)
    tracks.append(Sequence(Wait(tSpray), sprayTrack))
    if hp > 0:
        tracks.append(__getSplashTrack(targetPoint, scale, tSpray + dSprayScale, battle))
    
    if hp > 0 or delay <= 0:
        tracks.append(__getSuitTrack(suit, tContact, tSuitDodges, hp, hpbonus, kbbonus, 'squirt-small-react', died, leftSuits, rightSuits, battle, toon, fShowStun))
    
    return tracks


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
    tracks = Parallel()
    toonTrack = Sequence(Func(toon.headsUp, battle, suitPos), ActorInterval(toon, 'water-gun'), Func(toon.loop, 'neutral'), Func(toon.setHpr, battle, origHpr))
    tracks.append(toonTrack)
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

    sprayTrack = MovieUtil.getSprayTrack(battle, WaterSprayColor, getSprayStartPos, targetPoint, dSprayScale, dSprayHold, dSprayScale, horizScale = scale, vertScale = scale)
    pistolPos = Point3(0.28000000000000003, 0.10000000000000001, 0.080000000000000002)
    pistolHpr = VBase3(85.599999999999994, -4.4400000000000004, 94.430000000000007)
    pistolTrack = Sequence(Func(MovieUtil.showProp, pistol, hand_jointpath0, pistolPos, pistolHpr), LerpScaleInterval(pistol, dPistolScale, pistol.getScale(), startScale = MovieUtil.PNT3_NEARZERO), Wait(tSpray - dPistolScale))
    pistolTrack.append(sprayTrack)
    pistolTrack.append(Wait(dPistolHold))
    pistolTrack.append(LerpScaleInterval(pistol, dPistolScale, MovieUtil.PNT3_NEARZERO))
    pistolTrack.append(Func(hand_jointpath1.removeNode))
    pistolTrack.append(Func(hand_jointpath0.removeNode))
    pistolTrack.append(Func(MovieUtil.removeProp, pistol))
    tracks.append(pistolTrack)
    if hp > 0:
        tracks.append(__getSplashTrack(targetPoint, 0.29999999999999999, tSpray + dSprayScale, battle))
    
    if hp > 0 or delay <= 0:
        tracks.append(__getSuitTrack(suit, tContact, tSuitDodges, hp, hpbonus, kbbonus, 'squirt-small-react', died, leftSuits, rightSuits, battle, toon, fShowStun))
    
    return tracks


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
    tracks = Parallel()
    toonTrack = Sequence(Func(toon.headsUp, battle, suitPos), ActorInterval(toon, 'hold-bottle'), Func(toon.loop, 'neutral'), Func(toon.setHpr, battle, origHpr))
    tracks.append(toonTrack)
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

    sprayTrack = MovieUtil.getSprayTrack(battle, WaterSprayColor, getSprayStartPos, targetPoint, dSprayScale, dSprayHold, dSprayScale, horizScale = scale, vertScale = scale)
    hand_jointpath0 = hands[0].attachNewNode('handJoint0-path')
    hand_jointpath1 = hand_jointpath0.instanceTo(hands[1])
    bottleTrack = Sequence(Func(MovieUtil.showProp, bottle, hand_jointpath0), LerpScaleInterval(bottle, dBottleScale, bottle.getScale(), startScale = MovieUtil.PNT3_NEARZERO), Wait(tSpray - dBottleScale))
    bottleTrack.append(sprayTrack)
    bottleTrack.append(Wait(dBottleHold))
    bottleTrack.append(LerpScaleInterval(bottle, dBottleScale, MovieUtil.PNT3_NEARZERO))
    bottleTrack.append(Func(hand_jointpath1.removeNode))
    bottleTrack.append(Func(hand_jointpath0.removeNode))
    bottleTrack.append(Func(MovieUtil.removeProp, bottle))
    tracks.append(bottleTrack)
    if hp > 0:
        tracks.append(__getSplashTrack(targetPoint, scale, tSpray + dSprayScale, battle))
    
    if hp > 0 or delay <= 0:
        tracks.append(__getSuitTrack(suit, tContact, tSuitDodges, hp, hpbonus, kbbonus, 'squirt-small-react', died, leftSuits, rightSuits, battle, toon, fShowStun))
    
    return tracks


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
    tracks = Parallel()
    toonTrack = Sequence(Wait(tAppearDelay), Func(toon.headsUp, battle, suitPos), ActorInterval(toon, 'firehose'), Func(toon.loop, 'neutral'), Func(toon.setHpr, battle, origHpr))
    tracks.append(toonTrack)
    soundTrack = __getSoundTrack(level, hitSuit, tSprayDelay, toon)
    tracks.append(soundTrack)
    hose = globalPropPool.getProp('firehose')
    hydrant = globalPropPool.getProp('hydrant')
    hose.reparentTo(hydrant)
    (hose.pose('firehose', 2),)
    hydrantNode = toon.attachNewNode('hydrantNode')
    hydrantNode.clearTransform(toon.getGeomNode().getChild(0))
    hydrantScale = hydrantNode.attachNewNode('hydrantScale')
    hydrant.reparentTo(hydrantScale)
    toon.pose('firehose', 30)
    toon.update(0)
    torso = toon.getPart('torso', '1000')
    if toon.style.torso[0] == 'm':
        hydrant.setPos(torso, 0, 0, -1.8500000000000001)
    else:
        hydrant.setPos(torso, 0, 0, -1.45)
    hydrant.setPos(0, 0, hydrant.getZ())
    base = hydrant.find('**/base')
    base.setColor(1, 1, 1, 0.5)
    base.setPos(toon, 0, 0, 0)
    toon.loop('neutral')
    
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

    sprayTrack = Sequence()
    sprayTrack.append(Wait(tSprayDelay))
    sprayTrack.append(MovieUtil.getSprayTrack(battle, WaterSprayColor, getSprayStartPos, targetPoint, dSprayScale, dSprayHold, dSprayScale, horizScale = scale, vertScale = scale))
    tracks.append(sprayTrack)
    hydrantNode.detachNode()
    propTrack = Sequence(Func(battle.movie.needRestoreRenderProp, hydrantNode), Func(hydrantNode.reparentTo, toon), LerpScaleInterval(hydrantScale, tAppearDelay * 0.5, Point3(1, 1, 1.3999999999999999), startScale = Point3(1, 1, 0.01)), LerpScaleInterval(hydrantScale, tAppearDelay * 0.29999999999999999, Point3(1, 1, 0.80000000000000004), startScale = Point3(1, 1, 1.3999999999999999)), LerpScaleInterval(hydrantScale, tAppearDelay * 0.10000000000000001, Point3(1, 1, 1.2), startScale = Point3(1, 1, 0.80000000000000004)), LerpScaleInterval(hydrantScale, tAppearDelay * 0.10000000000000001, Point3(1, 1, 1), startScale = Point3(1, 1, 1.2)), ActorInterval(hose, 'firehose', duration = dAnimHold), Wait(dHoseHold - 0.20000000000000001), LerpScaleInterval(hydrantScale, 0.20000000000000001, Point3(1, 1, 0.01), startScale = Point3(1, 1, 1)), Func(MovieUtil.removeProps, [
        hydrantNode,
        hose]), Func(battle.movie.clearRenderProp, hydrantNode))
    tracks.append(propTrack)
    if hp > 0:
        tracks.append(__getSplashTrack(targetPoint, 0.40000000000000002, 2.7000000000000002, battle, splashHold = 1.5))
    
    if hp > 0 or delay <= 0:
        tracks.append(__getSuitTrack(suit, tContact, tSuitDodges, hp, hpbonus, kbbonus, 'squirt-small-react', died, leftSuits, rightSuits, battle, toon, fShowStun))
    
    return tracks


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
    tracks = Parallel()
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
    toonTrack = Sequence(Func(MovieUtil.showProps, buttons, hands), Func(toon.headsUp, battle, suitPos), ActorInterval(toon, 'pushbutton'), Func(MovieUtil.removeProps, buttons), Func(toon.loop, 'neutral'), Func(toon.setHpr, battle, origHpr))
    tracks.append(toonTrack)
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
    
    def getCloudTrack(cloud, suit, cloudPosPoint, scaleUpPoint, rainEffects, rainDelay, effectDelay, cloudHold, useEffect, battle = battle, trickleEffect = trickleEffect):
        track = Sequence(Func(MovieUtil.showProp, cloud, suit, cloudPosPoint), Func(cloud.pose, 'stormcloud', 0), LerpScaleInterval(cloud, 1.5, scaleUpPoint, startScale = MovieUtil.PNT3_NEARZERO), Wait(rainDelay))
        if useEffect == 1:
            ptrack = Parallel()
            delay = cloudHold * 0.25
            trickleDuration = cloudHold * 0.25
            trickleTrack = Sequence(Func(battle.movie.needRestoreParticleEffect, trickleEffect), ParticleInterval(trickleEffect, cloud, worldRelative = 0, duration = trickleDuration), Func(battle.movie.clearRestoreParticleEffect, trickleEffect))
            track.append(trickleTrack)
            for i in range(0, 3):
                dur = cloudHold - 2 * trickleDuration
                ptrack.append(Sequence(Func(battle.movie.needRestoreParticleEffect, rainEffects[i]), Wait(delay), ParticleInterval(rainEffects[i], cloud, worldRelative = 0, duration = dur), Func(battle.movie.clearRestoreParticleEffect, rainEffects[i])))
                delay += effectDelay
            
            ptrack.append(Sequence(Wait(3 * effectDelay), ActorInterval(cloud, 'stormcloud', startTime = 1, duration = cloudHold)))
            track.append(ptrack)
        else:
            track.append(ActorInterval(cloud, 'stormcloud', startTime = 1, duration = cloudHold))
        track.append(LerpScaleInterval(cloud, 0.5, MovieUtil.PNT3_NEARZERO))
        track.append(Func(MovieUtil.removeProp, cloud))
        return track

    tracks.append(getCloudTrack(cloud, suit, cloudPosPoint, scaleUpPoint, rainEffects, rainDelay, effectDelay, cloudHold, useEffect = 1))
    tracks.append(getCloudTrack(cloud2, suit, cloudPosPoint, scaleUpPoint, rainEffects, rainDelay, effectDelay, cloudHold, useEffect = 0))
    if hp > 0 or delay <= 0:
        tracks.append(__getSuitTrack(suit, tContact, tSuitDodges, hp, hpbonus, kbbonus, 'soak', died, leftSuits, rightSuits, battle, toon, fShowStun, beforeStun = 2.6000000000000001, afterStun = 2.2999999999999998))
    
    return tracks

squirtfn_array = (__doFlower, __doWaterGlass, __doWaterGun, __doSeltzerBottle, __doFireHose, __doStormCloud)
