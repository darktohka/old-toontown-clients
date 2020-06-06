# File: M (Python 2.2)

from PandaModules import *
from IntervalGlobal import *
from BattleBase import *
from BattleProps import *
from ToontownBattleGlobals import *
from SuitBattleGlobals import *
import DirectNotifyGlobal
import whrandom
import MovieUtil
notify = DirectNotifyGlobal.directNotify.newCategory('MovieCamera')

def chooseHealShot(heals, attackDuration):
    openShot = chooseHealOpenShot(heals, attackDuration)
    openDuration = openShot.getDuration()
    openName = openShot.getName()
    closeShot = chooseHealCloseShot(heals, openDuration, openName, attackDuration)
    track = Track([
        openShot,
        closeShot])
    return track


def chooseHealOpenShot(heals, attackDuration):
    numHeals = len(heals)
    av = None
    duration = 2.7999999999999998
    shotChoices = [
        toonGroupShot]
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseHealCloseShot(heals, openDuration, openName, attackDuration):
    av = None
    duration = attackDuration - openDuration
    shotChoices = [
        toonGroupShot]
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseTrapShot(traps, attackDuration):
    openShot = chooseTrapOpenShot(traps, attackDuration)
    openDuration = openShot.getDuration()
    openName = openShot.getName()
    closeShot = chooseTrapCloseShot(traps, openDuration, openName, attackDuration)
    track = Track([
        openShot,
        closeShot])
    return track


def chooseTrapOpenShot(traps, attackDuration):
    numTraps = len(traps)
    av = None
    duration = 3.0
    shotChoices = [
        allGroupLowShot]
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseTrapCloseShot(traps, openDuration, openName, attackDuration):
    av = None
    duration = attackDuration - openDuration
    shotChoices = [
        allGroupLowShot]
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseLureShot(lures, attackDuration):
    openShot = chooseLureOpenShot(lures, attackDuration)
    openDuration = openShot.getDuration()
    openName = openShot.getName()
    closeShot = chooseLureCloseShot(lures, openDuration, openName, attackDuration)
    track = Track([
        openShot,
        closeShot])
    return track


def chooseLureOpenShot(lures, attackDuration):
    numLures = len(lures)
    av = None
    duration = 3.0
    shotChoices = [
        allGroupLowShot]
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseLureCloseShot(lures, openDuration, openName, attackDuration):
    av = None
    duration = attackDuration - openDuration
    shotChoices = [
        allGroupLowShot]
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseSoundShot(sounds, targets, attackDuration):
    openShot = chooseSoundOpenShot(sounds, targets, attackDuration)
    openDuration = openShot.getDuration()
    openName = openShot.getName()
    closeShot = chooseSoundCloseShot(sounds, targets, openDuration, openName, attackDuration)
    track = Track([
        openShot,
        closeShot])
    return track


def chooseSoundOpenShot(sounds, targets, attackDuration):
    numSounds = len(sounds)
    av = None
    duration = 3.1000000000000001
    if numSounds == 1:
        av = sounds[0]['toon']
        shotChoices = [
            avatarCloseUpThreeQuarterRightShot,
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    elif numSounds >= 2 and numSounds <= 4:
        shotChoices = [
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    else:
        notify.error('Bad number of sounds: %s' % numSounds)
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseSoundCloseShot(sounds, targets, openDuration, openName, attackDuration):
    numSuits = len(targets)
    av = None
    duration = attackDuration - openDuration
    if numSuits == 1:
        av = targets[0]['suit']
        shotChoices = [
            avatarCloseUpThrowShot,
            avatarCloseUpThreeQuarterLeftShot,
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    elif numSuits >= 2 and numSuits <= 4:
        shotChoices = [
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    else:
        notify.error('Bad number of suits: %s' % numSuits)
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseThrowShot(throws, suitThrowsDict, attackDuration):
    openShot = chooseThrowOpenShot(throws, suitThrowsDict, attackDuration)
    openDuration = openShot.getDuration()
    openName = openShot.getName()
    closeShot = chooseThrowCloseShot(throws, suitThrowsDict, openDuration, openName, attackDuration)
    track = Track([
        openShot,
        closeShot])
    return track


def chooseThrowOpenShot(throws, suitThrowsDict, attackDuration):
    numThrows = len(throws)
    av = None
    duration = 3.0
    if numThrows == 1:
        av = throws[0]['toon']
        shotChoices = [
            avatarCloseUpThrowShot,
            avatarCloseUpThreeQuarterRightShot,
            avatarBehindShot,
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    elif numThrows >= 2 and numThrows <= 4:
        shotChoices = [
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    else:
        notify.error('Bad number of throws: %s' % numThrows)
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseThrowCloseShot(throws, suitThrowsDict, openDuration, openName, attackDuration):
    numSuits = len(suitThrowsDict)
    av = None
    duration = attackDuration - openDuration
    if numSuits == 1:
        av = toonbase.tcr.doId2do[suitThrowsDict.keys()[0]]
        shotChoices = [
            avatarCloseUpThrowShot,
            avatarCloseUpThreeQuarterLeftShot,
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    elif numSuits >= 2 and numSuits <= 4:
        shotChoices = [
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    else:
        notify.error('Bad number of suits: %s' % numSuits)
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseSquirtShot(squirts, suitSquirtsDict, attackDuration):
    openShot = chooseSquirtOpenShot(squirts, suitSquirtsDict, attackDuration)
    openDuration = openShot.getDuration()
    openName = openShot.getName()
    closeShot = chooseSquirtCloseShot(squirts, suitSquirtsDict, openDuration, openName, attackDuration)
    track = Track([
        openShot,
        closeShot])
    return track


def chooseSquirtOpenShot(squirts, suitSquirtsDict, attackDuration):
    numSquirts = len(squirts)
    av = None
    duration = 3.0
    if numSquirts == 1:
        av = squirts[0]['toon']
        shotChoices = [
            avatarCloseUpThrowShot,
            avatarCloseUpThreeQuarterRightShot,
            avatarBehindShot,
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    elif numSquirts >= 2 and numSquirts <= 4:
        shotChoices = [
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    else:
        notify.error('Bad number of squirts: %s' % numSquirts)
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseSquirtCloseShot(squirts, suitSquirtsDict, openDuration, openName, attackDuration):
    numSuits = len(suitSquirtsDict)
    av = None
    duration = attackDuration - openDuration
    if numSuits == 1:
        av = toonbase.tcr.doId2do[suitSquirtsDict.keys()[0]]
        shotChoices = [
            avatarCloseUpThrowShot,
            avatarCloseUpThreeQuarterLeftShot,
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    elif numSuits >= 2 and numSuits <= 4:
        shotChoices = [
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    else:
        notify.error('Bad number of suits: %s' % numSuits)
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseDropShot(drops, suitDropsDict, attackDuration):
    openShot = chooseDropOpenShot(drops, suitDropsDict, attackDuration)
    openDuration = openShot.getDuration()
    openName = openShot.getName()
    closeShot = chooseDropCloseShot(drops, suitDropsDict, openDuration, openName, attackDuration)
    track = Track([
        openShot,
        closeShot])
    return track


def chooseDropOpenShot(drops, suitDropsDict, attackDuration):
    numDrops = len(drops)
    av = None
    duration = 3.0
    if numDrops == 1:
        av = drops[0]['toon']
        shotChoices = [
            avatarCloseUpThrowShot,
            avatarCloseUpThreeQuarterRightShot,
            avatarBehindShot,
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    elif numDrops >= 2 and numDrops <= 4:
        shotChoices = [
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    else:
        notify.error('Bad number of drops: %s' % numDrops)
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseDropCloseShot(drops, suitDropsDict, openDuration, openName, attackDuration):
    numSuits = len(suitDropsDict)
    av = None
    duration = attackDuration - openDuration
    if numSuits == 1:
        av = toonbase.tcr.doId2do[suitDropsDict.keys()[0]]
        shotChoices = [
            avatarCloseUpThrowShot,
            avatarCloseUpThreeQuarterLeftShot,
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    elif numSuits >= 2 and numSuits <= 4:
        shotChoices = [
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    else:
        notify.error('Bad number of suits: %s' % numSuits)
    choice = whrandom.choice(shotChoices)
    track = apply(choice, [
        av,
        duration])
    return track


def chooseSuitShot(attack, attackDuration):
    groupStatus = attack['group']
    target = attack['target']
    if groupStatus == ATK_TGT_SINGLE:
        toon = target['toon']
    
    suit = attack['suit']
    name = attack['id']
    battle = attack['battle']
    camIvals = []
    
    def defaultCamera(attack = attack, attackDuration = attackDuration, openShotDuration = 3.5, target = target):
        if attack['group'] == ATK_TGT_GROUP:
            return randomGroupAttackCam(attack['suit'], target, attack['battle'], attackDuration, openShotDuration)
        else:
            return randomAttackCam(attack['suit'], target['toon'], attack['battle'], attackDuration, openShotDuration, 'suit')

    if name == AUDIT:
        camIvals.append(defaultCamera())
    elif name == BITE:
        camIvals.append(defaultCamera(openShotDuration = 2.7999999999999998))
    elif name == BOUNCE_CHECK:
        camIvals.append(defaultCamera())
    elif name == BRAIN_STORM:
        camIvals.append(defaultCamera(openShotDuration = 2.3999999999999999))
    elif name == BUZZ_WORD:
        camIvals.append(defaultCamera(openShotDuration = 4.7000000000000002))
    elif name == CALCULATE:
        camIvals.append(defaultCamera())
    elif name == CANNED:
        camIvals.append(defaultCamera(openShotDuration = 2.8999999999999999))
    elif name == CHOMP:
        camIvals.append(defaultCamera(openShotDuration = 2.7999999999999998))
    elif name == CLIPON_TIE:
        camIvals.append(defaultCamera(openShotDuration = 3.2999999999999998))
    elif name == CRUNCH:
        camIvals.append(defaultCamera(openShotDuration = 3.3999999999999999))
    elif name == DEMOTION:
        camIvals.append(defaultCamera(openShotDuration = 1.7))
    elif name == DOUBLE_TALK:
        camIvals.append(defaultCamera(openShotDuration = 3.8999999999999999))
    elif name == EVICTION_NOTICE:
        camIvals.append(defaultCamera(openShotDuration = 3.2000000000000002))
    elif name == EVIL_EYE:
        camIvals.append(defaultCamera(openShotDuration = 2.7000000000000002))
    elif name == FILIBUSTER:
        camIvals.append(defaultCamera(openShotDuration = 2.7000000000000002))
    elif name == FILL_WITH_LEAD:
        camIvals.append(defaultCamera(openShotDuration = 3.2000000000000002))
    elif name == FINGER_WAG:
        camIvals.append(defaultCamera(openShotDuration = 2.2999999999999998))
    elif name == FIRED:
        camIvals.append(defaultCamera(openShotDuration = 1.7))
    elif name == FOUNTAIN_PEN:
        camIvals.append(defaultCamera(openShotDuration = 2.6000000000000001))
    elif name == FREEZE_ASSETS:
        camIvals.append(defaultCamera(openShotDuration = 2.5))
    elif name == HALF_WINDSOR:
        camIvals.append(defaultCamera(openShotDuration = 2.7999999999999998))
    elif name == HEAD_SHRINK:
        camIvals.append(defaultCamera(openShotDuration = 1.3))
    elif name == GLOWER_POWER:
        camIvals.append(defaultCamera(openShotDuration = 1.3999999999999999))
    elif name == GUILT_TRIP:
        camIvals.append(defaultCamera(openShotDuration = 0.90000000000000002))
    elif name == HANG_UP:
        camIvals.append(defaultCamera(openShotDuration = 5.0999999999999996))
    elif name == HOT_AIR:
        camIvals.append(defaultCamera(openShotDuration = 2.5))
    elif name == JARGON:
        camIvals.append(defaultCamera())
    elif name == LEGALESE:
        camIvals.append(defaultCamera(openShotDuration = 1.5))
    elif name == LIQUIDATE:
        camIvals.append(defaultCamera(openShotDuration = 2.5))
    elif name == MARKET_CRASH:
        camIvals.append(defaultCamera(openShotDuration = 2.8999999999999999))
    elif name == MUMBO_JUMBO:
        camIvals.append(defaultCamera(openShotDuration = 2.7999999999999998))
    elif name == PARADIGM_SHIFT:
        camIvals.append(defaultCamera(openShotDuration = 1.6000000000000001))
    elif name == PECKING_ORDER:
        camIvals.append(defaultCamera(openShotDuration = 2.7999999999999998))
    elif name == PLAY_HARDBALL:
        camIvals.append(defaultCamera(openShotDuration = 2.2999999999999998))
    elif name == PICK_POCKET:
        camIvals.append(apply(allGroupLowShot, [
            suit,
            2.7000000000000002]))
    elif name == PINK_SLIP:
        camIvals.append(defaultCamera(openShotDuration = 2.7999999999999998))
    elif name == POUND_KEY:
        camIvals.append(defaultCamera(openShotDuration = 2.7999999999999998))
    elif name == POWER_TIE:
        camIvals.append(defaultCamera(openShotDuration = 2.3999999999999999))
    elif name == POWER_TRIP:
        camIvals.append(defaultCamera(openShotDuration = 1.1000000000000001))
    elif name == QUAKE:
        shakeIntensity = 5.1500000000000004
        quake = 1
        camIvals.append(apply(suitCameraShakeShot, [
            suit,
            attackDuration,
            shakeIntensity,
            quake]))
    elif name == RAZZLE_DAZZLE:
        camIvals.append(defaultCamera(openShotDuration = 2.2000000000000002))
    elif name == RED_TAPE:
        camIvals.append(defaultCamera(openShotDuration = 3.5))
    elif name == RE_ORG:
        camIvals.append(defaultCamera(openShotDuration = 1.1000000000000001))
    elif name == RESTRAINING_ORDER:
        camIvals.append(defaultCamera(openShotDuration = 2.7999999999999998))
    elif name == ROLODEX:
        camIvals.append(defaultCamera())
    elif name == RUBBER_STAMP:
        camIvals.append(defaultCamera(openShotDuration = 3.2000000000000002))
    elif name == RUB_OUT:
        camIvals.append(defaultCamera(openShotDuration = 2.2000000000000002))
    elif name == SACKED:
        camIvals.append(defaultCamera(openShotDuration = 2.8999999999999999))
    elif name == SCHMOOZE:
        camIvals.append(defaultCamera(openShotDuration = 2.7999999999999998))
    elif name == SHAKE:
        shakeIntensity = 1.75
        camIvals.append(apply(suitCameraShakeShot, [
            suit,
            attackDuration,
            shakeIntensity]))
    elif name == SHRED:
        camIvals.append(defaultCamera(openShotDuration = 4.0999999999999996))
    elif name == SPIN:
        camIvals.append(defaultCamera(openShotDuration = 1.7))
    elif name == SYNERGY:
        camIvals.append(defaultCamera(openShotDuration = 1.7))
    elif name == TABULATE:
        camIvals.append(defaultCamera())
    elif name == TEE_OFF:
        camIvals.append(defaultCamera(openShotDuration = 4.5))
    elif name == TREMOR:
        shakeIntensity = 0.25
        camIvals.append(apply(suitCameraShakeShot, [
            suit,
            attackDuration,
            shakeIntensity]))
    elif name == WATERCOOLER:
        camIvals.append(defaultCamera())
    elif name == WITHDRAWAL:
        camIvals.append(defaultCamera(openShotDuration = 1.2))
    elif name == WRITE_OFF:
        camIvals.append(defaultCamera())
    else:
        notify.warning('unknown attack id in chooseSuitShot: %d using default cam' % name)
        camIvals.append(defaultCamera())
    camTrack = Track(camIvals)
    pbpText = attack['playByPlayText']
    displayName = Localizer.SuitAttackNames[attack['name']]
    pbpTrack = pbpText.getShowInterval(displayName, 3.5)
    return MultiTrack([
        camTrack,
        pbpTrack])


def chooseSuitCloseShot(attack, openDuration, openName, attackDuration):
    av = None
    duration = attackDuration - openDuration
    if duration < 0:
        duration = 9.9999999999999995e-007
    
    groupStatus = attack['group']
    diedTrack = None
    if groupStatus == ATK_TGT_SINGLE:
        av = attack['target']['toon']
        shotChoices = [
            avatarCloseUpThreeQuarterRightShot,
            suitGroupThreeQuarterLeftBehindShot]
        died = attack['target']['died']
        if died != 0:
            pbpText = attack['playByPlayText']
            diedText = av.getName() + ' was defeated!'
            diedTextList = [
                diedText]
            diedTrack = pbpText.getToonsDiedInterval(diedTextList, duration)
        
    elif groupStatus == ATK_TGT_GROUP:
        av = None
        shotChoices = [
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
        deadToons = []
        targetDicts = attack['target']
        for targetDict in targetDicts:
            died = targetDict['died']
            if died != 0:
                deadToons.append(targetDict['toon'])
            
        
        if len(deadToons) > 0:
            pbpText = attack['playByPlayText']
            diedTextList = []
            for toon in deadToons:
                pbpText = attack['playByPlayText']
                diedTextList.append(toon.getName() + ' was defeated!')
            
            diedTrack = pbpText.getToonsDiedInterval(diedTextList, duration)
        
    else:
        notify.error('Bad groupStatus: %s' % groupStatus)
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    if diedTrack == None:
        return track
    else:
        mtrack = MultiTrack([
            track,
            diedTrack])
        return mtrack


def makeShot(x, y, z, h, p, r, duration, other = None, name = 'makeShot'):
    if other:
        return heldRelativeShot(other, x, y, z, h, p, r, duration, name)
    else:
        return heldShot(x, y, z, h, p, r, duration, name)


def focusShot(x, y, z, duration, target, other = None, splitFocusPoint = None, name = 'focusShot'):
    ivals = []
    if other:
        ivals.append(FunctionInterval(camera.setPos, extraArgs = [
            other,
            Point3(x, y, z)]))
    else:
        ivals.append(FunctionInterval(camera.setPos, extraArgs = [
            Point3(x, y, z)]))
    if splitFocusPoint:
        (ivals.append(FunctionInterval(focusCameraBetweenPoints, extraArgs = [
            target,
            splitFocusPoint])),)
    else:
        ivals.append(FunctionInterval(camera.lookAt, extraArgs = [
            target]))
    ivals.append(WaitInterval(duration))
    return Track(ivals)


def moveShot(x, y, z, h, p, r, duration, other = None, name = 'moveShot'):
    return motionShot(x, y, z, h, p, r, duration, other, name)


def focusMoveShot(x, y, z, duration, target, other = None, name = 'focusMoveShot'):
    camera.setPos(Point3(x, y, z))
    camera.lookAt(target)
    hpr = camera.getHpr()
    return motionShot(x, y, z, hpr[0], hpr[1], hpr[2], duration, other, name)


def chooseSOSShot(av, duration):
    shotChoices = [
        avatarCloseUpThreeQuarterRightShot,
        avatarBehindShot,
        avatarBehindHighShot,
        suitGroupThreeQuarterLeftBehindShot]
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseRewardShot(av, duration):
    
    def chooseRewardShotNow(av):
        if av.playingAnim == 'victory':
            shotChoices = [
                (0, 8, av.getHeight() * 0.66000000000000003, 179, 15, 0),
                (5.2000000000000002, 5.4500000000000002, av.getHeight() * 0.66000000000000003, 131.5, 3.6000000000000001, 0)]
            shot = whrandom.choice(shotChoices)
            camera.setPosHpr(av, *shot)
        else:
            camera.setPosHpr(10, 0, 10, 115, -30, 0)

    return Sequence(Func(chooseRewardShotNow, av), Wait(duration))


def heldShot(x, y, z, h, p, r, duration, name = 'heldShot'):
    intervalList = []
    intervalList.append(FunctionInterval(camera.setPosHpr, extraArgs = [
        x,
        y,
        z,
        h,
        p,
        r]))
    intervalList.append(WaitInterval(duration))
    track = Track(intervalList, name)
    return track


def heldRelativeShot(other, x, y, z, h, p, r, duration, name = 'heldRelativeShot'):
    intervalList = []
    intervalList.append(FunctionInterval(camera.setPosHpr, extraArgs = [
        other,
        x,
        y,
        z,
        h,
        p,
        r]))
    intervalList.append(WaitInterval(duration))
    track = Track(intervalList, name)
    return track


def motionShot(x, y, z, h, p, r, duration, other = None, name = 'motionShot'):
    if other:
        posTrack = Track([
            LerpPosInterval(camera, duration, pos = Point3(x, y, z), other = other)])
        hprTrack = Track([
            LerpHprInterval(camera, duration, hpr = Point3(h, p, r), other = other)])
    else:
        posTrack = Track([
            LerpPosInterval(camera, duration, pos = Point3(x, y, z))])
        hprTrack = Track([
            LerpHprInterval(camera, duration, hpr = Point3(h, p, r))])
    return MultiTrack([
        posTrack,
        hprTrack])


def allGroupShot(avatar, duration):
    return heldShot(10, 0, 10, 89, -30, 0, duration, 'allGroupShot')


def allGroupLowShot(avatar, duration):
    return heldShot(15, 0, 3, 89, 0, 0, duration, 'allGroupLowShot')


def allGroupLowDiagonalShot(avatar, duration):
    return heldShot(7, 5, 6, 119, -30, 0, duration, 'allGroupLowShot')


def toonGroupShot(avatar, duration):
    return heldShot(10, 0, 10, 115, -30, 0, duration, 'toonGroupShot')


def suitGroupShot(avatar, duration):
    return heldShot(10, 0, 10, 65, -30, 0, duration, 'suitGroupShot')


def suitGroupLowLeftShot(avatar, duration):
    return heldShot(8.4000000000000004, -3.8500000000000001, 2.75, 36.299999999999997, 3.25, 0, duration, 'suitGroupLowLeftShot')


def suitGroupThreeQuarterLeftBehindShot(avatar, duration):
    if whrandom.random() > 0.5:
        x = 12.369999999999999
        h = 134.61000000000001
    else:
        x = -12.369999999999999
        h = -134.61000000000001
    return heldShot(x, 11.5, 8.1600000000000001, h, -22.699999999999999, 0, duration, 'suitGroupThreeQuarterLeftBehindShot')


def suitWakeUpShot(avatar, duration):
    return heldShot(10, -5, 10, 65, -30, 0, duration, 'suitWakeUpShot')


def suitCameraShakeShot(avatar, duration, shakeIntensity, quake = 0):
    intervalList = []
    if quake == 1:
        shakeDelay = 1.1000000000000001
        numShakes = 4
    else:
        shakeDelay = 0.29999999999999999
        numShakes = 5
    postShakeDelay = 0.5
    shakeTime = (duration - shakeDelay - postShakeDelay) / numShakes
    shakeDuration = shakeTime * (1.0 / numShakes)
    shakeWaitInterval = shakeTime * ((numShakes - 1.0) / numShakes)
    
    def shakeCameraIvals(intensity, shakeWaitInterval = shakeWaitInterval, quake = quake, shakeDuration = shakeDuration, numShakes = numShakes):
        vertShakeTrack = Track([
            WaitInterval(shakeWaitInterval),
            FunctionInterval(camera.setZ, extraArgs = [
                camera.getZ() + intensity / 2]),
            WaitInterval(shakeDuration / 2),
            FunctionInterval(camera.setZ, extraArgs = [
                camera.getZ() - intensity]),
            WaitInterval(shakeDuration / 2),
            FunctionInterval(camera.setZ, extraArgs = [
                camera.getZ() + intensity / 2])])
        horizShakeTrack = Track([
            WaitInterval(shakeWaitInterval - shakeDuration / 2),
            FunctionInterval(camera.setY, extraArgs = [
                camera.getY() + intensity / 4]),
            WaitInterval(shakeDuration / 2),
            FunctionInterval(camera.setY, extraArgs = [
                camera.getY() - intensity / 2]),
            WaitInterval(shakeDuration / 2),
            FunctionInterval(camera.setY, extraArgs = [
                camera.getY() + intensity / 4]),
            WaitInterval(shakeDuration / 2),
            FunctionInterval(camera.lookAt, extraArgs = [
                Point3(0, 0, 0)])])
        ivals = []
        for i in range(0, numShakes):
            if quake == 0:
                ivals.append(vertShakeTrack)
            else:
                ivals.append(MultiTrack([
                    vertShakeTrack,
                    horizShakeTrack]))
        
        return ivals

    x = 10 + whrandom.random() * 3
    if whrandom.random() > 0.5:
        x = -x
    
    z = 7 + whrandom.random() * 3
    intervalList.append(FunctionInterval(camera.setPos, extraArgs = [
        x,
        -5,
        z]))
    intervalList.append(FunctionInterval(camera.lookAt, extraArgs = [
        Point3(0, 0, 0)]))
    intervalList.append(WaitInterval(shakeDelay))
    intervalList.extend(shakeCameraIvals(shakeIntensity))
    intervalList.append(WaitInterval(postShakeDelay))
    return Track(intervalList, 'suitShakeCameraShot')


def avatarCloseUpShot(avatar, duration):
    return heldRelativeShot(avatar, 0, 8, avatar.getHeight() * 0.66000000000000003, 179, 15, 0, duration, 'avatarCloseUpShot')


def avatarCloseUpThrowShot(avatar, duration):
    return heldRelativeShot(avatar, 3, 8, avatar.getHeight() * 0.66000000000000003, 159, 3.6000000000000001, 0, duration, 'avatarCloseUpThrowShot')


def avatarCloseUpThreeQuarterRightShot(avatar, duration):
    return heldRelativeShot(avatar, 5.2000000000000002, 5.4500000000000002, avatar.getHeight() * 0.66000000000000003, 131.5, 3.6000000000000001, 0, duration, 'avatarCloseUpThreeQuarterRightShot')


def avatarCloseUpThreeQuarterLeftShot(avatar, duration):
    return heldRelativeShot(avatar, -5.2000000000000002, 5.4500000000000002, avatar.getHeight() * 0.66000000000000003, -131.5, 3.6000000000000001, 0, duration, 'avatarCloseUpThreeQuarterLeftShot')


def avatarCloseUpThreeQuarterRightFollowShot(avatar, duration):
    intervalList = []
    intervalList.append(heldRelativeShot(avatar, 5.2000000000000002, 5.4500000000000002, avatar.getHeight() * 0.66000000000000003, 131.5, 3.6000000000000001, 0, duration * 0.65000000000000002))
    intervalList.append(LerpHprInterval(node = camera, other = avatar, duration = duration * 0.20000000000000001, hpr = Point3(110, 3.6000000000000001, 0), blendType = 'easeInOut'))
    intervalList.append(WaitInterval(duration * 0.25))
    track = Track(intervalList, 'avatarCloseUpThreeQuarterRightFollowShot')
    return track


def avatarCloseUpZoomShot(avatar, duration):
    intervalList = []
    intervalList.append(LerpPosHprInterval(node = camera, other = avatar, duration = duration / 2, startPos = Point3(0, 10, avatar.getHeight()), startHpr = Point3(179, -10, 0), pos = Point3(0, 6, avatar.getHeight()), hpr = Point3(179, -10, 0), blendType = 'easeInOut'))
    intervalList.append(WaitInterval(duration / 2))
    track = Track(intervalList, 'avatarCloseUpZoomShot')
    return track


def avatarBehindShot(avatar, duration):
    return heldRelativeShot(avatar, 5, -7, avatar.getHeight(), 40, -12, 0, duration, 'avatarBehindShot')


def avatarBehindHighShot(avatar, duration):
    return heldRelativeShot(avatar, -4, -7, 5 + avatar.getHeight(), -30, -35, 0, duration, 'avatarBehindHighShot')


def avatarBehindThreeQuarterRightShot(avatar, duration):
    return heldRelativeShot(avatar, 7.6699999999999999, -8.5199999999999996, avatar.getHeight() * 0.66000000000000003, 25, 7.5, 0, duration, 'avatarBehindThreeQuarterRightShot')


def avatarSideFollowAttack(suit, toon, duration, battle):
    windupDuration = duration * (0.10000000000000001 + whrandom.random() * 0.10000000000000001)
    projectDuration = duration * 0.75
    impactDuration = duration - windupDuration - projectDuration
    suitHeight = suit.getHeight()
    toonHeight = toon.getHeight()
    suitCentralPoint = suit.getPos(battle)
    suitCentralPoint.setZ(suitCentralPoint.getZ() + suitHeight * 0.75)
    toonCentralPoint = toon.getPos(battle)
    toonCentralPoint.setZ(toonCentralPoint.getZ() + toonHeight * 0.75)
    initialX = whrandom.randint(12, 14)
    finalX = whrandom.randint(7, 8)
    initialY = whrandom.randint(-3, 0)
    finalY = whrandom.randint(-3, 0)
    initialZ = suitHeight * 0.5 + whrandom.random() * suitHeight
    finalZ = toonHeight * 0.5 + whrandom.random() * toonHeight
    if whrandom.random() > 0.5:
        initialX = -initialX
        finalX = -finalX
    
    return Track([
        focusShot(initialX, initialY, initialZ, windupDuration, suitCentralPoint),
        focusMoveShot(finalX, finalY, finalZ, projectDuration, toonCentralPoint),
        WaitInterval(impactDuration)])


def focusCameraBetweenPoints(point1, point2):
    if point1[0] > point2[0]:
        x = point2[0] + (point1[0] - point2[0]) * 0.5
    else:
        x = point1[0] + (point2[0] - point1[0]) * 0.5
    if point1[1] > point2[1]:
        y = point2[1] + (point1[1] - point2[1]) * 0.5
    else:
        y = point1[1] + (point2[1] - point1[1]) * 0.5
    if point1[2] > point2[2]:
        z = point2[2] + (point1[2] - point2[2]) * 0.5
    else:
        z = point1[2] + (point2[2] - point1[2]) * 0.5
    camera.lookAt(Point3(x, y, z))


def randomCamera(suit, toon, battle, attackDuration, openShotDuration):
    return randomAttackCam(suit, toon, battle, attackDuration, openShotDuration, 'suit')


def randomAttackCam(suit, toon, battle, attackDuration, openShotDuration, attackerString = 'suit'):
    if openShotDuration > attackDuration:
        openShotDuration = attackDuration
    
    closeShotDuration = attackDuration - openShotDuration
    if attackerString == 'suit':
        attacker = suit
        defender = toon
        defenderString = 'toon'
    else:
        attacker = toon
        defender = suit
        defenderString = 'suit'
    randomDouble = whrandom.random()
    if randomDouble > 0.59999999999999998:
        openShot = randomActorShot(attacker, battle, openShotDuration, attackerString)
    elif randomDouble > 0.20000000000000001:
        openShot = randomOverShoulderShot(suit, toon, battle, openShotDuration, focus = attackerString)
    else:
        openShot = randomSplitShot(attacker, defender, battle, openShotDuration)
    randomDouble = whrandom.random()
    if randomDouble > 0.59999999999999998:
        closeShot = randomActorShot(defender, battle, closeShotDuration, defenderString)
    elif randomDouble > 0.20000000000000001:
        closeShot = randomOverShoulderShot(suit, toon, battle, closeShotDuration, focus = defenderString)
    else:
        closeShot = randomSplitShot(attacker, defender, battle, closeShotDuration)
    return Track([
        openShot,
        closeShot])


def randomGroupAttackCam(suit, targets, battle, attackDuration, openShotDuration):
    if openShotDuration > attackDuration:
        openShotDuration = attackDuration
    
    closeShotDuration = attackDuration - openShotDuration
    randomDouble = whrandom.random()
    if randomDouble > 0:
        openShot = randomActorShot(suit, battle, openShotDuration, 'suit', groupShot = 0)
    
    closeShot = randomToonGroupShot(targets, suit, closeShotDuration, battle)
    return Track([
        openShot,
        closeShot])


def randomActorShot(actor, battle, duration, actorType, groupShot = 0):
    height = actor.getHeight()
    centralPoint = actor.getPos(battle)
    centralPoint.setZ(centralPoint.getZ() + height * 0.75)
    if actorType == 'suit':
        x = 4 + whrandom.random() * 8
        y = -2 - whrandom.random() * 4
        z = height * 0.5 + whrandom.random() * height * 1.5
        if groupShot == 1:
            y = -4
            z = height * 0.5
        
    else:
        x = 2 + whrandom.random() * 8
        y = -2 + whrandom.random() * 3
        z = height + whrandom.random() * height * 1.5
        if groupShot == 1:
            y = y + 3
            z = height * 0.5
        
    if MovieUtil.shotDirection == 'left':
        x = -x
    
    return focusShot(x, y, z, duration, centralPoint)


def randomSplitShot(suit, toon, battle, duration):
    suitHeight = suit.getHeight()
    toonHeight = toon.getHeight()
    suitCentralPoint = suit.getPos(battle)
    suitCentralPoint.setZ(suitCentralPoint.getZ() + suitHeight * 0.75)
    toonCentralPoint = toon.getPos(battle)
    toonCentralPoint.setZ(toonCentralPoint.getZ() + toonHeight * 0.75)
    x = 9 + whrandom.random() * 2
    y = -2 - whrandom.random() * 2
    z = suitHeight * 0.5 + whrandom.random() * suitHeight
    if MovieUtil.shotDirection == 'left':
        x = -x
    
    return focusShot(x, y, z, duration, toonCentralPoint, splitFocusPoint = suitCentralPoint)


def randomOverShoulderShot(suit, toon, battle, duration, focus):
    suitHeight = suit.getHeight()
    toonHeight = toon.getHeight()
    suitCentralPoint = suit.getPos(battle)
    suitCentralPoint.setZ(suitCentralPoint.getZ() + suitHeight * 0.75)
    toonCentralPoint = toon.getPos(battle)
    toonCentralPoint.setZ(toonCentralPoint.getZ() + toonHeight * 0.75)
    x = 2 + whrandom.random() * 10
    if focus == 'toon':
        y = 8 + whrandom.random() * 6
        z = suitHeight * 1.2 + whrandom.random() * suitHeight
    else:
        y = -10 - whrandom.random() * 6
        z = toonHeight * 1.5
    if MovieUtil.shotDirection == 'left':
        x = -x
    
    return focusShot(x, y, z, duration, toonCentralPoint, splitFocusPoint = suitCentralPoint)


def randomCameraSelection(suit, attack, attackDuration, openShotDuration):
    shotChoices = [
        avatarCloseUpThrowShot,
        avatarCloseUpThreeQuarterLeftShot,
        allGroupLowShot,
        suitGroupLowLeftShot,
        avatarBehindHighShot]
    if openShotDuration > attackDuration:
        openShotDuration = attackDuration
    
    closeShotDuration = attackDuration - openShotDuration
    openShot = apply(whrandom.choice(shotChoices), [
        suit,
        openShotDuration])
    closeShot = chooseSuitCloseShot(attack, closeShotDuration, openShot.getName(), attackDuration)
    return Track([
        openShot,
        closeShot])


def randomToonGroupShot(toons, suit, duration, battle):
    sum = 0
    for t in toons:
        toon = t['toon']
        height = toon.getHeight()
        sum = sum + height
    
    avgHeight = (sum / len(toons)) * 0.75
    suitPos = suit.getPos(battle)
    x = 1 + whrandom.random() * 6
    if suitPos.getX() > 0:
        x = -x
    
    if whrandom.random() > 0.5:
        y = 4 + whrandom.random() * 1
        z = avgHeight + whrandom.random() * 6
    else:
        y = 11 + whrandom.random() * 2
        z = 13 + whrandom.random() * 2
    focalPoint = Point3(0, -4, avgHeight)
    return focusShot(x, y, z, duration, focalPoint)

