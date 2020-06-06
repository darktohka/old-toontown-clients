# File: M (Python 2.2)

from PandaModules import *
from IntervalGlobal import *
from BattleBase import *
from BattleProps import *
from BattleSounds import *
from AvatarDNA import *
import DirectNotifyGlobal
import whrandom
import MovieCamera
import MovieUtil
notify = DirectNotifyGlobal.directNotify.newCategory('MovieThrow')
hitSoundFiles = ('AA_tart_only.mp3', 'AA_slice_only.mp3', 'AA_slice_only.mp3', 'AA_slice_only.mp3', 'AA_slice_only.mp3', 'AA_wholepie_only.mp3')
tPieLeavesHand = 2.7000000000000002
tPieHitsSuit = 3.0
tSuitDodges = 2.4500000000000002
ratioMissToHit = 1.5
tPieShrink = 0.69999999999999996
pieFlyTaskName = 'MovieThrow-pieFly'
pieNames = ('tart', 'fruitpie-slice', 'creampie-slice', 'fruitpie', 'creampie', 'birthday-cake')

def doThrows(throws):
    if len(throws) == 0:
        return (None, None)
    
    suitThrowsDict = { }
    for throw in throws:
        suitId = throw['target']['suit'].doId
        if suitThrowsDict.has_key(suitId):
            suitThrowsDict[suitId].append(throw)
        else:
            suitThrowsDict[suitId] = [
                throw]
    
    suitThrows = suitThrowsDict.values()
    
    def compFunc(a, b):
        if len(a) > len(b):
            return 1
        elif len(a) < len(b):
            return -1
        
        return 0

    suitThrows.sort(compFunc)
    delay = 0.0
    tracks = []
    for st in suitThrows:
        if len(st) > 0:
            ival = __doSuitThrows(st)
            if ival:
                tracks.append(Track([
                    (delay, ival)]))
            
            delay = delay + TOON_THROW_SUIT_DELAY
        
    
    mtrack = MultiTrack(tracks)
    camDuration = mtrack.getDuration()
    camTrack = MovieCamera.chooseThrowShot(throws, suitThrowsDict, camDuration)
    return (mtrack, camTrack)


def __doSuitThrows(throws):
    toonTracks = []
    delay = 0.0
    hitCount = 0
    for throw in throws:
        if throw['target']['hp'] > 0:
            hitCount += 1
        else:
            break
    
    for throw in throws:
        tracks = __throwPie(throw, delay, hitCount)
        if tracks:
            for track in tracks:
                toonTracks.append(track)
            
        
        delay = delay + TOON_THROW_DELAY
    
    return MultiTrack(toonTracks)


def __showProp(prop, parent, pos):
    prop.reparentTo(parent)
    prop.setPos(pos)


def __animProp(props, propName, propType):
    if 'actor' == propType:
        for prop in props:
            prop.play(propName)
        
    elif 'model' == propType:
        pass
    else:
        self.notify.error('No such propType as: %s' % propType)


def __billboardProp(prop):
    scale = prop.getScale()
    prop.setBillboardPointWorld()
    prop.setScale(scale)


def __suitMissPoint(suit, other = render):
    pnt = suit.getPos(other)
    pnt.setZ(pnt[2] + suit.getHeight() * 1.3)
    return pnt


def __propPreflight(props, suit, toon, battle):
    prop = props[0]
    toon.update(0)
    prop.wrtReparentTo(battle)
    props[1].reparentTo(hidden)
    for ci in range(prop.getNumChildren()):
        prop.getChild(ci).setHpr(0, -90, 0)
    
    targetPnt = MovieUtil.avatarFacePoint(suit, other = battle)
    prop.lookAt(targetPnt)


def __piePreMiss(missDict, pie, suitPoint, other = render):
    missDict['pie'] = pie
    missDict['startScale'] = pie.getScale()
    missDict['startPos'] = pie.getPos(other)
    v = Vec3(suitPoint - missDict['startPos'])
    endPos = missDict['startPos'] + v * ratioMissToHit
    missDict['endPos'] = endPos


def __pieMissLerpCallback(t, missDict):
    pie = missDict['pie']
    newPos = missDict['startPos'] * (1.0 - t) + missDict['endPos'] * t
    if t < tPieShrink:
        tScale = 0.0001
    else:
        tScale = (t - tPieShrink) / (1.0 - tPieShrink)
    newScale = missDict['startScale'] * max(1.0 - tScale, 0.01)
    pie.setPos(newPos)
    pie.setScale(newScale)


def __getSoundTrack(level, hitSuit, node = None):
    soundIvals = []
    throwSound = globalBattleSoundCache.getSound('AA_pie_throw_only.mp3')
    throwTrack = Track([
        (2.6000000000000001, SoundInterval(throwSound, node = node))])
    if hitSuit:
        hitSound = globalBattleSoundCache.getSound(hitSoundFiles[level])
        hitTrack = Track([
            (tPieLeavesHand, SoundInterval(hitSound, node = node))])
        return MultiTrack([
            throwTrack,
            hitTrack])
    else:
        return throwTrack


def __throwPie(throw, delay, hitCount):
    toon = throw['toon']
    hpbonus = throw['hpbonus']
    target = throw['target']
    suit = target['suit']
    hp = target['hp']
    kbbonus = target['kbbonus']
    sidestep = throw['sidestep']
    died = target['died']
    leftSuits = target['leftSuits']
    rightSuits = target['rightSuits']
    level = throw['level']
    battle = throw['battle']
    suitPos = suit.getPos(battle)
    origHpr = toon.getHpr(battle)
    notify.debug('toon: %s throws tart at suit: %d for hp: %d died: %d' % (toon.getName(), suit.doId, hp, died))
    pieName = pieNames[level]
    hitSuit = hp > 0
    pie = globalPropPool.getProp(pieName)
    pieType = globalPropPool.getPropType(pieName)
    pie2 = MovieUtil.copyProp(pie)
    pies = [
        pie,
        pie2]
    hands = toon.getRightHands()
    splatName = 'splat-' + pieName
    splat = globalPropPool.getProp(splatName)
    splatType = globalPropPool.getPropType(splatName)
    toonIvals = []
    toonFace = FunctionInterval(toon.headsUp, extraArgs = [
        battle,
        suitPos])
    toonIvals.append((delay, toonFace))
    toonIvals.append(ActorInterval(toon, 'throw'))
    toonIvals.append(FunctionInterval(toon.loop, extraArgs = [
        'neutral']))
    toonIvals.append(FunctionInterval(toon.setHpr, extraArgs = [
        battle,
        origHpr]))
    toonTrack = Track(toonIvals)
    pieIntervals = []
    pieShow = FunctionInterval(MovieUtil.showProps, extraArgs = [
        pies,
        hands])
    pieAnim = FunctionInterval(__animProp, extraArgs = [
        pies,
        pieName,
        pieType])
    pieScale1 = LerpScaleInterval(pie, 1.0, pie.getScale(), startScale = MovieUtil.PNT3_NEARZERO)
    pieScale2 = LerpScaleInterval(pie2, 1.0, pie2.getScale(), startScale = MovieUtil.PNT3_NEARZERO)
    pieScale = MultiTrack([
        Track([
            pieScale1]),
        Track([
            pieScale2])])
    piePreflight = FunctionInterval(__propPreflight, extraArgs = [
        pies,
        suit,
        toon,
        battle])
    pieIntervals.append((delay, pieShow))
    pieIntervals.append(pieAnim)
    pieIntervals.append(pieScale)
    pieIntervals.append(FunctionInterval(battle.movie.needRestoreRenderProp, extraArgs = [
        pies[0]]))
    pieIntervals.append((delay + tPieLeavesHand, piePreflight))
    soundTrack = __getSoundTrack(level, hitSuit, toon)
    if hitSuit:
        pieFly = LerpPosInterval(pie, tPieHitsSuit - tPieLeavesHand, pos = MovieUtil.avatarFacePoint(suit, other = battle), name = pieFlyTaskName, other = battle)
        pieHide = FunctionInterval(MovieUtil.removeProps, extraArgs = [
            pies])
        splatShow = FunctionInterval(__showProp, extraArgs = [
            splat,
            suit,
            Point3(0, 0, suit.getHeight())])
        splatBillboard = FunctionInterval(__billboardProp, extraArgs = [
            splat])
        splatAnim = ActorInterval(splat, splatName)
        splatHide = FunctionInterval(MovieUtil.removeProp, extraArgs = [
            splat])
        pieIntervals.append((delay + tPieLeavesHand, pieFly))
        pieIntervals.append(pieHide)
        pieIntervals.append(FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
            pies[0]]))
        pieIntervals.append(splatShow)
        pieIntervals.append(splatBillboard)
        pieIntervals.append(splatAnim)
        pieIntervals.append(splatHide)
    else:
        missDict = { }
        if sidestep:
            suitPoint = MovieUtil.avatarFacePoint(suit, other = battle)
        else:
            suitPoint = __suitMissPoint(suit, other = battle)
        piePreMiss = FunctionInterval(__piePreMiss, extraArgs = [
            missDict,
            pie,
            suitPoint,
            battle])
        pieMiss = LerpFunctionInterval(__pieMissLerpCallback, extraArgs = [
            missDict], duration = (tPieHitsSuit - tPieLeavesHand) * ratioMissToHit)
        pieHide = FunctionInterval(MovieUtil.removeProps, extraArgs = [
            pies])
        pieIntervals.append((delay + tPieLeavesHand, piePreMiss))
        pieIntervals.append(pieMiss)
        pieIntervals.append(pieHide)
        pieIntervals.append(FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
            pies[0]]))
    pieTrack = Track(pieIntervals)
    if hitSuit:
        suitIntervals = []
        showDamage = FunctionInterval(suit.showLaffNumber, openEnded = 0, extraArgs = [
            -hp])
        updateHealthBar = FunctionInterval(suit.updateHealthBar, extraArgs = [
            hp])
        sival = []
        if kbbonus > 0:
            (suitPos, suitHpr) = battle.getActorPosHpr(suit)
            suitType = getSuitBodyType(suit.getStyleName())
            animIvals = []
            animIvals.append(ActorInterval(suit, 'pie-small-react', duration = 0.20000000000000001))
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
        elif hitCount == 1:
            sival = Parallel(ActorInterval(suit, 'pie-small-react'), MovieUtil.createSuitStunInterval(suit, 0.29999999999999999, 1.3))
        else:
            sival = ActorInterval(suit, 'pie-small-react')
        suitIntervals.append((delay + tPieHitsSuit, showDamage))
        suitIntervals.append(updateHealthBar)
        suitIntervals.append(sival)
        bonusTrack = None
        bonusIvals = []
        if kbbonus > 0:
            bonusIvals.append((delay + tPieHitsSuit + 0.75, FunctionInterval(suit.showLaffNumber, openEnded = 0, extraArgs = [
                -kbbonus,
                2])))
        
        if hpbonus > 0:
            if kbbonus > 0:
                bonusIvals.append((0.75, FunctionInterval(suit.showLaffNumber, openEnded = 0, extraArgs = [
                    -hpbonus,
                    1]), PREVIOUS_END))
            else:
                bonusIvals.append((delay + tPieHitsSuit + 0.75, FunctionInterval(suit.showLaffNumber, openEnded = 0, extraArgs = [
                    -hpbonus,
                    1])))
        
        if len(bonusIvals) > 0:
            bonusTrack = Track(bonusIvals)
        
        if died != 0:
            suitIntervals.append(MovieUtil.createSuitDeathTrack(suit, toon, battle))
        else:
            suitIntervals.append(FunctionInterval(suit.loop, extraArgs = [
                'neutral']))
        if bonusTrack == None:
            suitResponseTrack = Track(suitIntervals)
        else:
            suitResponseTrack = MultiTrack([
                Track(suitIntervals),
                bonusTrack])
    else:
        suitResponseTrack = MovieUtil.createSuitDodgeMultitrack(delay + tSuitDodges, suit, leftSuits, rightSuits)
    if not hitSuit and delay > 0:
        return [
            toonTrack,
            soundTrack,
            pieTrack]
    else:
        return [
            toonTrack,
            soundTrack,
            pieTrack,
            suitResponseTrack]

