# File: M (Python 2.2)

from IntervalGlobal import *
from BattleBase import *
from BattleProps import *
from BattleSounds import *
import MovieCamera
import DirectNotifyGlobal
import MovieUtil
notify = DirectNotifyGlobal.directNotify.newCategory('MovieDrop')
hitSoundFiles = ('AA_drop_flowerpot.mp3', 'AA_drop_sandbag.mp3', 'AA_drop_anvil.mp3', 'AA_drop_bigweight.mp3', 'AA_drop_safe.mp3', 'AA_drop_piano.mp3')
missSoundFiles = ('AA_drop_flowerpot_miss.mp3', 'AA_drop_sandbag_miss.mp3', 'AA_drop_anvil_miss.mp3', 'AA_drop_bigweight_miss.mp3', 'AA_drop_safe_miss.mp3', 'AA_drop_piano_miss.mp3')
tDropShadow = 1.3
tSuitDodges = 2.4500000000000002 + tDropShadow
tObjectAppears = 3.0 + tDropShadow
tButtonPressed = 2.4399999999999999
dShrink = 0.29999999999999999
dShrinkOnMiss = 0.10000000000000001
dPropFall = 0.59999999999999998
objects = ('flowerpot', 'sandbag', 'anvil', 'weight', 'safe', 'piano')
objZOffsets = (0.75, 0.75, 0.0, 0.0, 0.0, 0.0)
landFrames = (12, 4, 1, 11, 11, 11)
shoulderHeights = {
    'a': 13.279999999999999 / 4.0,
    'b': 13.74 / 4.0,
    'c': 10.02 / 4.0 }

def doDrops(drops):
    if len(drops) == 0:
        return (None, None)
    
    suitDropsDict = { }
    for drop in drops:
        suitId = drop['target']['suit'].doId
        if suitDropsDict.has_key(suitId):
            suitDropsDict[suitId].append(drop)
        else:
            suitDropsDict[suitId] = [
                drop]
    
    suitDrops = suitDropsDict.values()
    
    def compFunc(a, b):
        if len(a) > len(b):
            return 1
        elif len(a) < len(b):
            return -1
        
        return 0

    suitDrops.sort(compFunc)
    delay = 0.0
    tracks = []
    for st in suitDrops:
        if len(st) > 0:
            ival = __doSuitDrops(st)
            if ival:
                tracks.append(Track([
                    (delay, ival)]))
            
            delay = delay + TOON_DROP_SUIT_DELAY
        
    
    mtrack = MultiTrack(tracks, name = 'toplevel-drop')
    camDuration = mtrack.getDuration()
    camTrack = MovieCamera.chooseDropShot(drops, suitDropsDict, camDuration)
    return (mtrack, camTrack)


def __getSoundTrack(level, hitSuit, node = None):
    if hitSuit:
        soundEffect = globalBattleSoundCache.getSound(hitSoundFiles[level])
    else:
        soundEffect = globalBattleSoundCache.getSound(missSoundFiles[level])
    soundIntervals = []
    if soundEffect:
        buttonSound = globalBattleSoundCache.getSound('AA_drop_trigger_box.mp3')
        fallingSound = globalBattleSoundCache.getSound('incoming_whistleALT.mp3')
        buttonDelay = tButtonPressed - 0.29999999999999999
        fallingDuration = 1.5
        soundIntervals.append(WaitInterval(buttonDelay))
        soundIntervals.append(SoundInterval(buttonSound, node = node))
        soundIntervals.append(SoundInterval(fallingSound, duration = fallingDuration, node = node))
        soundIntervals.append(SoundInterval(soundEffect, node = node))
    else:
        soundIntervals.append(WaitInterval(0.10000000000000001))
    return Track(soundIntervals)


def __doSuitDrops(drops):
    toonTracks = []
    delay = 0.0
    alreadyDodged = 0
    alreadyTeased = 0
    for drop in drops:
        level = drop['level']
        objName = objects[level]
        ivals = __dropObject(drop, delay, objName, level, alreadyDodged, alreadyTeased)
        if ivals:
            toonTracks += ivals
            delay += TOON_DROP_DELAY
        
        hp = drop['target']['hp']
        if hp <= 0:
            if level >= 3:
                alreadyTeased = 1
            else:
                alreadyDodged = 1
        
    
    return MultiTrack(toonTracks)


def __dropObject(drop, delay, objName, level, alreadyDodged, alreadyTeased):
    toon = drop['toon']
    hpbonus = drop['hpbonus']
    target = drop['target']
    suit = target['suit']
    hp = target['hp']
    hitSuit = hp > 0
    died = target['died']
    leftSuits = target['leftSuits']
    rightSuits = target['rightSuits']
    kbbonus = target['kbbonus']
    battle = drop['battle']
    suitPos = suit.getPos(battle)
    origHpr = toon.getHpr(battle)
    majorObject = level >= 3
    button = globalPropPool.getProp('button')
    buttonType = globalPropPool.getPropType('button')
    button2 = MovieUtil.copyProp(button)
    buttons = [
        button,
        button2]
    hands = toon.getLeftHands()
    object = globalPropPool.getProp(objName)
    objectType = globalPropPool.getPropType(objName)
    if objName == 'weight':
        object.setScale(object.getScale() * 0.75)
    elif objName == 'safe':
        object.setScale(object.getScale() * 0.84999999999999998)
    
    node = object.node()
    node.setBound(OmniBoundingVolume())
    node.setFinal(1)
    soundTrack = __getSoundTrack(level, hitSuit, toon)
    toonIntervals = []
    toonFace = FunctionInterval(toon.headsUp, extraArgs = [
        battle,
        suitPos])
    toonIntervals.append((delay, toonFace))
    toonIntervals.append(ActorInterval(toon, 'pushbutton'))
    toonIntervals.append(FunctionInterval(toon.loop, extraArgs = [
        'neutral']))
    toonIntervals.append(FunctionInterval(toon.setHpr, extraArgs = [
        battle,
        origHpr]))
    toonTrack = Track(toonIntervals)
    buttonIntervals = []
    buttonShow = FunctionInterval(MovieUtil.showProps, extraArgs = [
        buttons,
        hands])
    buttonScaleUp = LerpScaleInterval(button, 1.0, button.getScale(), startScale = Point3(0.01, 0.01, 0.01))
    buttonScaleDown = LerpScaleInterval(button, 1.0, Point3(0.01, 0.01, 0.01), startScale = button.getScale())
    buttonHide = FunctionInterval(MovieUtil.removeProps, extraArgs = [
        buttons])
    buttonIntervals.append((delay, buttonShow))
    buttonIntervals.append(buttonScaleUp)
    buttonIntervals.append(WaitInterval(2.5))
    buttonIntervals.append(buttonScaleDown)
    buttonIntervals.append(buttonHide)
    buttonTrack = Track(buttonIntervals)
    objIntervals = []
    
    def posObject(object, suit, level, majorObject, miss, battle = battle):
        object.reparentTo(battle)
        if battle.isSuitLured(suit):
            (suitPos, suitHpr) = battle.getActorPosHpr(suit)
            object.setPos(suitPos)
            object.setHpr(suitHpr)
            if level >= 3:
                object.setY(object.getY() + 2)
            
        else:
            object.setPos(suit.getPos(battle))
            object.setHpr(suit.getHpr(battle))
            if miss and level >= 3:
                object.setY(object.getY(battle) + 5)
            
        if not majorObject:
            if not miss:
                shoulderHeight = shoulderHeights[suit.style.body] * suit.scale
                object.setZ(object.getPos(battle)[2] + shoulderHeight)
            
        
        object.setZ(object.getPos(battle)[2] + objZOffsets[level])

    objIntervals.append(FunctionInterval(battle.movie.needRestoreRenderProp, extraArgs = [
        object]))
    objInit = FunctionInterval(posObject, extraArgs = [
        object,
        suit,
        level,
        majorObject,
        hp <= 0])
    objIntervals.append((delay + tObjectAppears, objInit))
    if hp > 0 and level == 1 or level == 2:
        animProp = ActorInterval(object, objName)
        trackObjAnimate = Track([
            animProp])
        shrinkProp = LerpScaleInterval(object, dShrink, Point3(0.01, 0.01, 0.01), startScale = object.getScale())
        trackObjShrink = Track([
            (animProp.getDuration() - dShrink, shrinkProp)])
        objAnimShrink = MultiTrack([
            trackObjAnimate,
            trackObjShrink])
        objIntervals.append(objAnimShrink)
    else:
        animProp = ActorInterval(object, objName, duration = landFrames[level] / 24.0)
        
        def poseProp(prop, animName, level):
            prop.pose(animName, landFrames[level])

        poseProp = FunctionInterval(poseProp, extraArgs = [
            object,
            objName,
            level])
        wait = WaitInterval(1.0)
        shrinkProp = LerpScaleInterval(object, dShrinkOnMiss, Point3(0.01, 0.01, 0.01), startScale = object.getScale())
        objIntervals.append(animProp)
        objIntervals.append(poseProp)
        objIntervals.append(wait)
        objIntervals.append(shrinkProp)
    objIntervals.append(FunctionInterval(MovieUtil.removeProp, extraArgs = [
        object]))
    objIntervals.append(FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
        object]))
    objectTrack = Track(objIntervals)
    dropShadow = MovieUtil.copyProp(suit.getShadowJoints()[0])
    if level == 0:
        dropShadow.setScale(0.5)
    elif level <= 2:
        dropShadow.setScale(0.80000000000000004)
    elif level == 3:
        dropShadow.setScale(2.0)
    elif level == 4:
        dropShadow.setScale(2.2999999999999998)
    else:
        dropShadow.setScale(3.6000000000000001)
    
    def posShadow(dropShadow = dropShadow, suit = suit, battle = battle, hp = hp, level = level):
        dropShadow.reparentTo(battle)
        if battle.isSuitLured(suit):
            (suitPos, suitHpr) = battle.getActorPosHpr(suit)
            dropShadow.setPos(suitPos)
            dropShadow.setHpr(suitHpr)
            if level >= 3:
                dropShadow.setY(dropShadow.getY() + 2)
            
        else:
            dropShadow.setPos(suit.getPos(battle))
            dropShadow.setHpr(suit.getHpr(battle))
            if hp <= 0 and level >= 3:
                dropShadow.setY(dropShadow.getY(battle) + 5)
            
        dropShadow.setZ(dropShadow.getZ() + 0.5)

    shadowTrack = Track([
        WaitInterval(delay + tButtonPressed),
        FunctionInterval(battle.movie.needRestoreRenderProp, extraArgs = [
            dropShadow]),
        FunctionInterval(posShadow),
        LerpScaleInterval(dropShadow, tObjectAppears - tButtonPressed, dropShadow.getScale(), startScale = Point3(0.01, 0.01, 0.01)),
        WaitInterval(0.29999999999999999),
        FunctionInterval(MovieUtil.removeProp, extraArgs = [
            dropShadow]),
        FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
            dropShadow])])
    if hp > 0:
        suitIntervals = []
        showDamage = FunctionInterval(suit.showLaffNumber, openEnded = 0, extraArgs = [
            -hp])
        updateHealthBar = FunctionInterval(suit.updateHealthBar, extraArgs = [
            hp])
        if majorObject:
            anim = 'flatten'
        else:
            anim = 'drop-react'
        suitReact = ActorInterval(suit, anim)
        suitIntervals.append((delay + tObjectAppears, showDamage))
        suitIntervals.append(updateHealthBar)
        suitIntervals.append(suitReact)
        bonusTrack = None
        if hpbonus > 0:
            bonusTrack = Track([
                (delay + tObjectAppears + 0.75, FunctionInterval(suit.showLaffNumber, openEnded = 0, extraArgs = [
                    -hpbonus,
                    1]))])
        
        if died != 0:
            suitIntervals.append(MovieUtil.createSuitDeathTrack(suit, toon, battle))
        else:
            suitIntervals.append(FunctionInterval(suit.loop, extraArgs = [
                'neutral']))
        if bonusTrack == None:
            suitTrack = Track(suitIntervals)
        else:
            suitTrack = MultiTrack([
                Track(suitIntervals),
                bonusTrack])
    elif kbbonus == 0:
        suitTrack = Track([
            (delay + tObjectAppears, FunctionInterval(MovieUtil.indicateMissed, extraArgs = [
                suit,
                0.59999999999999998])),
            FunctionInterval(suit.loop, extraArgs = [
                'neutral'])])
    elif alreadyDodged > 0:
        return [
            toonTrack,
            soundTrack,
            buttonTrack,
            objectTrack,
            shadowTrack]
    
    if level >= 3:
        if alreadyTeased > 0:
            return [
                toonTrack,
                soundTrack,
                buttonTrack,
                objectTrack,
                shadowTrack]
        else:
            suitTrack = Track([
                MovieUtil.createSuitTeaseMultiTrack(suit, delay = delay + tObjectAppears)])
    else:
        suitTrack = MovieUtil.createSuitDodgeMultitrack(delay + tSuitDodges, suit, leftSuits, rightSuits)
    return [
        toonTrack,
        soundTrack,
        buttonTrack,
        objectTrack,
        shadowTrack,
        suitTrack]

