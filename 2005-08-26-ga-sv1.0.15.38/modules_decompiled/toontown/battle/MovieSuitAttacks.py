# File: M (Python 2.2)

from toontown.toonbase.ToontownGlobals import *
from SuitBattleGlobals import *
from direct.interval.IntervalGlobal import *
from BattleBase import *
from BattleProps import *
from toontown.suit.SuitDNA import *
from BattleBase import *
from BattleSounds import *
import MovieCamera
from direct.directnotify import DirectNotifyGlobal
import MovieUtil
from direct.particles import ParticleEffect
import BattleParticles
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
notify = DirectNotifyGlobal.directNotify.newCategory('MovieSuitAttacks')

def __doDamage(toon, dmg, died):
    if dmg > 0 and toon.hp != None:
        toon.takeDamage(dmg)
    


def __showProp(prop, parent, pos, hpr = None, scale = None):
    prop.reparentTo(parent)
    prop.setPos(pos)
    if hpr:
        prop.setHpr(hpr)
    
    if scale:
        prop.setScale(scale)
    


def __animProp(prop, propName, propType = 'actor'):
    if 'actor' == propType:
        prop.play(propName)
    elif 'model' == propType:
        pass
    else:
        self.notify.error('No such propType as: %s' % propType)


def __suitFacePoint(suit, zOffset = 0):
    pnt = suit.getPos()
    pnt.setZ(pnt[2] + suit.shoulderHeight + 0.29999999999999999 + zOffset)
    return Point3(pnt)


def __toonFacePoint(toon, zOffset = 0, parent = render):
    pnt = toon.getPos(parent)
    pnt.setZ(pnt[2] + toon.shoulderHeight + 0.29999999999999999 + zOffset)
    return Point3(pnt)


def __toonTorsoPoint(toon, zOffset = 0):
    pnt = toon.getPos()
    pnt.setZ(pnt[2] + toon.shoulderHeight - 0.20000000000000001)
    return Point3(pnt)


def __toonGroundPoint(attack, toon, zOffset = 0, parent = render):
    pnt = toon.getPos(parent)
    battle = attack['battle']
    pnt.setZ(battle.getZ(parent) + zOffset)
    return Point3(pnt)


def __toonGroundMissPoint(attack, prop, toon, zOffset = 0):
    point = __toonMissPoint(prop, toon)
    battle = attack['battle']
    point.setZ(battle.getZ() + zOffset)
    return Point3(point)


def __toonMissPoint(prop, toon, yOffset = 0, parent = None):
    if parent:
        p = __toonFacePoint(toon) - prop.getPos(parent)
    else:
        p = __toonFacePoint(toon) - prop.getPos()
    v = Vec3(p)
    baseDistance = v.length()
    v.normalize()
    if parent:
        endPos = prop.getPos(parent) + v * (baseDistance + 5 + yOffset)
    else:
        endPos = prop.getPos() + v * (baseDistance + 5 + yOffset)
    return Point3(endPos)


def __toonMissBehindPoint(toon, parent = render, offset = 0):
    point = toon.getPos(parent)
    point.setY((point.getY() - 5) + offset)
    return point


def __throwBounceHitPoint(prop, toon):
    startPoint = prop.getPos()
    endPoint = __toonFacePoint(toon)
    return __throwBouncePoint(startPoint, endPoint)


def __throwBounceMissPoint(prop, toon):
    startPoint = prop.getPos()
    endPoint = __toonFacePoint(toon)
    return __throwBouncePoint(startPoint, endPoint)


def __throwBouncePoint(startPoint, endPoint):
    midPoint = startPoint + (endPoint - startPoint) / 2.0
    midPoint.setZ(0)
    return Point3(midPoint)


def doSuitAttack(attack):
    notify.debug('building suit attack in doSuitAttack: %s' % attack['name'])
    name = attack['id']
    if name == AUDIT:
        suitTrack = doAudit(attack)
    elif name == BITE:
        suitTrack = doBite(attack)
    elif name == BOUNCE_CHECK:
        suitTrack = doBounceCheck(attack)
    elif name == BRAIN_STORM:
        suitTrack = doBrainStorm(attack)
    elif name == BUZZ_WORD:
        suitTrack = doBuzzWord(attack)
    elif name == CALCULATE:
        suitTrack = doCalculate(attack)
    elif name == CANNED:
        suitTrack = doCanned(attack)
    elif name == CHOMP:
        suitTrack = doChomp(attack)
    elif name == CIGAR_SMOKE:
        suitTrack = doDefault(attack)
    elif name == CLIPON_TIE:
        suitTrack = doClipOnTie(attack)
    elif name == CRUNCH:
        suitTrack = doCrunch(attack)
    elif name == DEMOTION:
        suitTrack = doDemotion(attack)
    elif name == DOUBLE_TALK:
        suitTrack = doDoubleTalk(attack)
    elif name == DOWNSIZE:
        suitTrack = doDownsize(attack)
    elif name == EVICTION_NOTICE:
        suitTrack = doEvictionNotice(attack)
    elif name == EVIL_EYE:
        suitTrack = doEvilEye(attack)
    elif name == FILIBUSTER:
        suitTrack = doFilibuster(attack)
    elif name == FILL_WITH_LEAD:
        suitTrack = doFillWithLead(attack)
    elif name == FINGER_WAG:
        suitTrack = doFingerWag(attack)
    elif name == FIRED:
        suitTrack = doFired(attack)
    elif name == FIVE_O_CLOCK_SHADOW:
        suitTrack = doDefault(attack)
    elif name == FLOOD_THE_MARKET:
        suitTrack = doDefault(attack)
    elif name == FOUNTAIN_PEN:
        suitTrack = doFountainPen(attack)
    elif name == FREEZE_ASSETS:
        suitTrack = doFreezeAssets(attack)
    elif name == GAVEL:
        suitTrack = doDefault(attack)
    elif name == GLOWER_POWER:
        suitTrack = doGlowerPower(attack)
    elif name == GUILT_TRIP:
        suitTrack = doGuiltTrip(attack)
    elif name == HALF_WINDSOR:
        suitTrack = doHalfWindsor(attack)
    elif name == HANG_UP:
        suitTrack = doHangUp(attack)
    elif name == HEAD_SHRINK:
        suitTrack = doHeadShrink(attack)
    elif name == HOT_AIR:
        suitTrack = doHotAir(attack)
    elif name == JARGON:
        suitTrack = doJargon(attack)
    elif name == LEGALESE:
        suitTrack = doLegalese(attack)
    elif name == LIQUIDATE:
        suitTrack = doLiquidate(attack)
    elif name == MARKET_CRASH:
        suitTrack = doMarketCrash(attack)
    elif name == MUMBO_JUMBO:
        suitTrack = doMumboJumbo(attack)
    elif name == PARADIGM_SHIFT:
        suitTrack = doParadigmShift(attack)
    elif name == PECKING_ORDER:
        suitTrack = doPeckingOrder(attack)
    elif name == PICK_POCKET:
        suitTrack = doPickPocket(attack)
    elif name == PINK_SLIP:
        suitTrack = doPinkSlip(attack)
    elif name == PLAY_HARDBALL:
        suitTrack = doPlayHardball(attack)
    elif name == POUND_KEY:
        suitTrack = doPoundKey(attack)
    elif name == POWER_TIE:
        suitTrack = doPowerTie(attack)
    elif name == POWER_TRIP:
        suitTrack = doPowerTrip(attack)
    elif name == QUAKE:
        suitTrack = doQuake(attack)
    elif name == RAZZLE_DAZZLE:
        suitTrack = doRazzleDazzle(attack)
    elif name == RED_TAPE:
        suitTrack = doRedTape(attack)
    elif name == RE_ORG:
        suitTrack = doReOrg(attack)
    elif name == RESTRAINING_ORDER:
        suitTrack = doRestrainingOrder(attack)
    elif name == ROLODEX:
        suitTrack = doRolodex(attack)
    elif name == RUBBER_STAMP:
        suitTrack = doRubberStamp(attack)
    elif name == RUB_OUT:
        suitTrack = doRubOut(attack)
    elif name == SACKED:
        suitTrack = doSacked(attack)
    elif name == SANDTRAP:
        suitTrack = doDefault(attack)
    elif name == SCHMOOZE:
        suitTrack = doSchmooze(attack)
    elif name == SHAKE:
        suitTrack = doShake(attack)
    elif name == SHRED:
        suitTrack = doShred(attack)
    elif name == SONG_AND_DANCE:
        suitTrack = doDefault(attack)
    elif name == SPIN:
        suitTrack = doSpin(attack)
    elif name == SYNERGY:
        suitTrack = doSynergy(attack)
    elif name == TABULATE:
        suitTrack = doTabulate(attack)
    elif name == TEE_OFF:
        suitTrack = doTeeOff(attack)
    elif name == THROW_BOOK:
        suitTrack = doDefault(attack)
    elif name == TREMOR:
        suitTrack = doTremor(attack)
    elif name == WATERCOOLER:
        suitTrack = doWatercooler(attack)
    elif name == WITHDRAWAL:
        suitTrack = doWithdrawal(attack)
    elif name == WRITE_OFF:
        suitTrack = doWriteOff(attack)
    else:
        notify.warning('unknown attack: %d substituting Finger Wag' % name)
        suitTrack = doDefault(attack)
    camTrack = MovieCamera.chooseSuitShot(attack, suitTrack.getDuration())
    battle = attack['battle']
    target = attack['target']
    groupStatus = attack['group']
    if groupStatus == ATK_TGT_SINGLE:
        toon = target['toon']
        toonHprTrack = Sequence(Func(toon.headsUp, battle, MovieUtil.PNT3_ZERO), Func(toon.loop, 'neutral'))
    else:
        toonHprTrack = Parallel()
        for t in target:
            toon = t['toon']
            toonHprTrack.append(Sequence(Func(toon.headsUp, battle, MovieUtil.PNT3_ZERO), Func(toon.loop, 'neutral')))
        
    suit = attack['suit']
    neutralIval = Func(suit.loop, 'neutral')
    suitTrack = Sequence(suitTrack, neutralIval, toonHprTrack)
    suitPos = suit.getPos(battle)
    (resetPos, resetHpr) = battle.getActorPosHpr(suit)
    if battle.isSuitLured(suit):
        resetTrack = getResetTrack(suit, battle)
        resetSuitTrack = Sequence(resetTrack, suitTrack)
        waitTrack = Sequence(Wait(resetTrack.getDuration()), Func(battle.unlureSuit, suit))
        resetCamTrack = Sequence(waitTrack, camTrack)
        return (resetSuitTrack, resetCamTrack)
    else:
        return (suitTrack, camTrack)


def getResetTrack(suit, battle):
    (resetPos, resetHpr) = battle.getActorPosHpr(suit)
    moveDist = Vec3(suit.getPos(battle) - resetPos).length()
    moveDuration = 0.5
    walkTrack = Sequence(Func(suit.setHpr, battle, resetHpr), ActorInterval(suit, 'walk', startTime = 1, duration = moveDuration, endTime = 1.0000000000000001e-005), Func(suit.loop, 'neutral'))
    moveTrack = LerpPosInterval(suit, moveDuration, resetPos, other = battle)
    return Parallel(walkTrack, moveTrack)


def __makeCancelledNodePath():
    tn = TextNode('CANCELLED')
    tn.setFont(getSuitFont())
    tn.setText(TTLocalizer.MovieSuitCancelled)
    tn.setAlign(TextNode.ACenter)
    tntop = hidden.attachNewNode('CancelledTop')
    tnpath = tntop.attachNewNode(tn)
    tnpath.setPosHpr(0, 0, 0, 0, 0, 0)
    tnpath.setScale(1)
    tnpath.setColor(0.69999999999999996, 0, 0, 1)
    tnpathback = tnpath.instanceUnderNode(tntop, 'backside')
    tnpathback.setPosHpr(0, 0, 0, 180, 0, 0)
    tnpath.setScale(1)
    return tntop


def doDefault(attack):
    notify.debug('building suit attack in doDefault')
    suitName = attack['suitName']
    if suitName == 'f':
        attack['id'] = POUND_KEY
        attack['name'] = 'PoundKey'
        attack['animName'] = 'phone'
        return doPoundKey(attack)
    elif suitName == 'p':
        attack['id'] = FOUNTAIN_PEN
        attack['name'] = 'FountainPen'
        attack['animName'] = 'pen-squirt'
        return doFountainPen(attack)
    elif suitName == 'ym':
        attack['id'] = RUBBER_STAMP
        attack['name'] = 'RubberStamp'
        attack['animName'] = 'rubber-stamp'
        return doRubberStamp(attack)
    elif suitName == 'mm':
        attack['id'] = FINGER_WAG
        attack['name'] = 'FingerWag'
        attack['animName'] = 'finger-wag'
        return doFingerWag(attack)
    elif suitName == 'ds':
        attack['id'] = DEMOTION
        attack['name'] = 'Demotion'
        attack['animName'] = 'magic1'
        return doDemotion(attack)
    elif suitName == 'hh':
        attack['id'] = GLOWER_POWER
        attack['name'] = 'GlowerPower'
        attack['animName'] = 'glower'
        return doGlowerPower(attack)
    elif suitName == 'cr':
        attack['id'] = PICK_POCKET
        attack['name'] = 'PickPocket'
        attack['animName'] = 'pickpocket'
        return doPickPocket(attack)
    elif suitName == 'tbc':
        attack['id'] = GLOWER_POWER
        attack['name'] = 'GlowerPower'
        attack['animName'] = 'glower'
        return doGlowerPower(attack)
    elif suitName == 'cc':
        attack['id'] = POUND_KEY
        attack['name'] = 'PoundKey'
        attack['animName'] = 'phone'
        return doPoundKey(attack)
    elif suitName == 'tm':
        attack['id'] = CLIPON_TIE
        attack['name'] = 'ClipOnTie'
        attack['animName'] = 'throw-paper'
        return doClipOnTie(attack)
    elif suitName == 'nd':
        attack['id'] = PICK_POCKET
        attack['name'] = 'PickPocket'
        attack['animName'] = 'pickpocket'
        return doPickPocket(attack)
    elif suitName == 'gh':
        attack['id'] = FOUNTAIN_PEN
        attack['name'] = 'FountainPen'
        attack['animName'] = 'pen-squirt'
        return doFountainPen(attack)
    elif suitName == 'ms':
        attack['id'] = BRAIN_STORM
        attack['name'] = 'BrainStorm'
        attack['animName'] = 'effort'
        return doBrainStorm(attack)
    elif suitName == 'tf':
        attack['id'] = RED_TAPE
        attack['name'] = 'RedTape'
        attack['animName'] = 'throw-object'
        return doRedTape(attack)
    elif suitName == 'm':
        attack['id'] = BUZZ_WORD
        attack['name'] = 'BuzzWord'
        attack['animName'] = 'speak'
        return doBuzzWord(attack)
    elif suitName == 'mh':
        attack['id'] = RAZZLE_DAZZLE
        attack['name'] = 'RazzleDazzle'
        attack['animName'] = 'smile'
        return doRazzleDazzle(attack)
    elif suitName == 'sc':
        attack['id'] = WATERCOOLER
        attack['name'] = 'Watercooler'
        attack['animName'] = 'water-cooler'
        return doWatercooler(attack)
    elif suitName == 'pp':
        attack['id'] = BOUNCE_CHECK
        attack['name'] = 'BounceCheck'
        attack['animName'] = 'throw-paper'
        return doBounceCheck(attack)
    elif suitName == 'tw':
        attack['id'] = GLOWER_POWER
        attack['name'] = 'GlowerPower'
        attack['animName'] = 'glower'
        return doGlowerPower(attack)
    elif suitName == 'bc':
        attack['id'] = AUDIT
        attack['name'] = 'Audit'
        attack['animName'] = 'phone'
        return doAudit(attack)
    elif suitName == 'nc':
        attack['id'] = RED_TAPE
        attack['name'] = 'RedTape'
        attack['animName'] = 'throw-object'
        return doRedTape(attack)
    elif suitName == 'mb':
        attack['id'] = LIQUIDATE
        attack['name'] = 'Liquidate'
        attack['animName'] = 'magic1'
        return doLiquidate(attack)
    elif suitName == 'ls':
        attack['id'] = WRITE_OFF
        attack['name'] = 'WriteOff'
        attack['animName'] = 'hold-pencil'
        return doWriteOff(attack)
    elif suitName == 'rb':
        attack['id'] = TEE_OFF
        attack['name'] = 'TeeOff'
        attack['animName'] = 'golf-club-swing'
        return doTeeOff(attack)
    elif suitName == 'bf':
        attack['id'] = RUBBER_STAMP
        attack['name'] = 'RubberStamp'
        attack['animName'] = 'rubber-stamp'
        return doRubberStamp(attack)
    elif suitName == 'b':
        attack['id'] = EVICTION_NOTICE
        attack['name'] = 'EvictionNotice'
        attack['animName'] = 'throw-paper'
        return doEvictionNotice(attack)
    elif suitName == 'dt':
        attack['id'] = RUBBER_STAMP
        attack['name'] = 'RubberStamp'
        attack['animName'] = 'rubber-stamp'
        return doRubberStamp(attack)
    elif suitName == 'ac':
        attack['id'] = RED_TAPE
        attack['name'] = 'RedTape'
        attack['animName'] = 'throw-object'
        return doRedTape(attack)
    elif suitName == 'bs':
        attack['id'] = FINGER_WAG
        attack['name'] = 'FingerWag'
        attack['animName'] = 'finger-wag'
        return doFingerWag(attack)
    elif suitName == 'sd':
        attack['id'] = WRITE_OFF
        attack['name'] = 'WriteOff'
        attack['animName'] = 'hold-pencil'
        return doWriteOff(attack)
    elif suitName == 'le':
        attack['id'] = JARGON
        attack['name'] = 'Jargon'
        attack['animName'] = 'speak'
        return doJargon(attack)
    elif suitName == 'bw':
        attack['id'] = FINGER_WAG
        attack['name'] = 'FingerWag'
        attack['animName'] = 'finger-wag'
        return doFingerWag(attack)
    else:
        self.notify.error('doDefault() - unsupported suit type: %s' % suitName)
    return None


def getSuitTrack(attack, delay = 9.9999999999999995e-007, splicedAnims = None):
    suit = attack['suit']
    battle = attack['battle']
    tauntIndex = attack['taunt']
    target = attack['target']
    toon = target['toon']
    targetPos = toon.getPos(battle)
    taunt = getAttackTaunt(attack['name'], tauntIndex)
    trapStorage = { }
    trapStorage['trap'] = None
    track = Sequence(Wait(delay), Func(suit.setChatAbsolute, taunt, CFSpeech | CFTimeout))
    
    def reparentTrap(suit = suit, battle = battle, trapStorage = trapStorage):
        trapProp = suit.battleTrapProp
        if trapProp != None:
            trapProp.wrtReparentTo(battle)
            trapStorage['trap'] = trapProp
        

    track.append(Func(reparentTrap))
    track.append(Func(suit.headsUp, battle, targetPos))
    if splicedAnims:
        track.append(getSplicedAnimsTrack(splicedAnims, actor = suit))
    else:
        track.append(ActorInterval(suit, attack['animName']))
    (origPos, origHpr) = battle.getActorPosHpr(suit)
    track.append(Func(suit.setHpr, battle, origHpr))
    
    def returnTrapToSuit(suit = suit, trapStorage = trapStorage):
        trapProp = trapStorage['trap']
        if trapProp != None:
            trapProp.wrtReparentTo(suit)
            suit.battleTrapProp = trapProp
        

    track.append(Func(returnTrapToSuit))
    track.append(Func(suit.clearChat))
    return track


def getSuitAnimTrack(attack, delay = 0):
    suit = attack['suit']
    tauntIndex = attack['taunt']
    taunt = getAttackTaunt(attack['name'], tauntIndex)
    return Sequence(Wait(delay), Func(suit.setChatAbsolute, taunt, CFSpeech | CFTimeout), ActorInterval(attack['suit'], attack['animName']), Func(suit.clearChat))


def getPartTrack(particleEffect, startDelay, durationDelay, partExtraArgs):
    particleEffect = partExtraArgs[0]
    parent = partExtraArgs[1]
    if len(partExtraArgs) > 2:
        worldRelative = partExtraArgs[2]
    else:
        worldRelative = 1
    return Sequence(Wait(startDelay), ParticleInterval(particleEffect, parent, worldRelative, duration = durationDelay))


def getToonTrack(attack, damageDelay = 9.9999999999999995e-007, damageAnimNames = None, dodgeDelay = 0.0001, dodgeAnimNames = None, splicedDamageAnims = None, splicedDodgeAnims = None, target = None, showDamageExtraTime = 0.01, showMissedExtraTime = 0.5):
    if not target:
        target = attack['target']
    
    toon = target['toon']
    battle = attack['battle']
    suit = attack['suit']
    suitPos = suit.getPos(battle)
    dmg = target['hp']
    animTrack = Sequence()
    animTrack.append(Func(toon.headsUp, battle, suitPos))
    if dmg > 0:
        animTrack.append(getToonTakeDamageTrack(toon, target['died'], dmg, damageDelay, damageAnimNames, splicedDamageAnims, showDamageExtraTime))
        return animTrack
    else:
        animTrack.append(getToonDodgeTrack(target, dodgeDelay, dodgeAnimNames, splicedDodgeAnims, showMissedExtraTime))
        indicatorTrack = Sequence(Wait(dodgeDelay + showMissedExtraTime), Func(MovieUtil.indicateMissed, toon))
        return Parallel(animTrack, indicatorTrack)


def getToonTracks(attack, damageDelay = 9.9999999999999995e-007, damageAnimNames = None, dodgeDelay = 9.9999999999999995e-007, dodgeAnimNames = None, splicedDamageAnims = None, splicedDodgeAnims = None, showDamageExtraTime = 0.01, showMissedExtraTime = 0.5):
    toonTracks = Parallel()
    targets = attack['target']
    for i in range(len(targets)):
        tgt = targets[i]
        toonTracks.append(getToonTrack(attack, damageDelay, damageAnimNames, dodgeDelay, dodgeAnimNames, splicedDamageAnims, splicedDodgeAnims, target = tgt, showDamageExtraTime = showDamageExtraTime, showMissedExtraTime = showMissedExtraTime))
    
    return toonTracks


def getToonDodgeTrack(target, dodgeDelay, dodgeAnimNames, splicedDodgeAnims, showMissedExtraTime):
    toon = target['toon']
    toonTrack = Sequence()
    toonTrack.append(Wait(dodgeDelay))
    if dodgeAnimNames:
        for d in dodgeAnimNames:
            if d == 'sidestep':
                toonTrack.append(getAllyToonsDodgeParallel(target))
            else:
                toonTrack.append(ActorInterval(toon, d))
        
    else:
        toonTrack.append(getSplicedAnimsTrack(splicedDodgeAnims, actor = toon))
    toonTrack.append(Func(toon.loop, 'neutral'))
    return toonTrack


def getAllyToonsDodgeParallel(target):
    toon = target['toon']
    leftToons = target['leftToons']
    rightToons = target['rightToons']
    if len(leftToons) > len(rightToons):
        PoLR = rightToons
        PoMR = leftToons
    else:
        PoLR = leftToons
        PoMR = rightToons
    upper = 1 + 4 * abs(len(leftToons) - len(rightToons))
    if whrandom.randint(0, upper) > 0:
        toonDodgeList = PoLR
    else:
        toonDodgeList = PoMR
    if toonDodgeList is leftToons:
        sidestepAnim = 'sidestep-left'
        soundEffect = globalBattleSoundCache.getSound('AV_side_step.mp3')
    else:
        sidestepAnim = 'sidestep-right'
        soundEffect = globalBattleSoundCache.getSound('AV_jump_to_side.mp3')
    toonTracks = Parallel()
    for t in toonDodgeList:
        toonTracks.append(Sequence(ActorInterval(t, sidestepAnim), Func(t.loop, 'neutral')))
    
    toonTracks.append(Sequence(ActorInterval(toon, sidestepAnim), Func(toon.loop, 'neutral')))
    toonTracks.append(Sequence(Wait(0.5), SoundInterval(soundEffect, node = toon)))
    return toonTracks


def getPropTrack(prop, parent, posPoints, appearDelay, remainDelay, scaleUpPoint = Point3(1), scaleUpTime = 0.5, scaleDownTime = 0.5, startScale = Point3(0.01), anim = 0, propName = 'none', animDuration = 0.0, animStartTime = 0.0):
    if anim == 1:
        track = Sequence(Wait(appearDelay), Func(__showProp, prop, parent, *posPoints), LerpScaleInterval(prop, scaleUpTime, scaleUpPoint, startScale = startScale), ActorInterval(prop, propName, duration = animDuration, startTime = animStartTime), Wait(remainDelay), Func(MovieUtil.removeProp, prop))
    else:
        track = Sequence(Wait(appearDelay), Func(__showProp, prop, parent, *posPoints), LerpScaleInterval(prop, scaleUpTime, scaleUpPoint, startScale = startScale), Wait(remainDelay), LerpScaleInterval(prop, scaleDownTime, MovieUtil.PNT3_NEARZERO), Func(MovieUtil.removeProp, prop))
    return track


def getPropAppearTrack(prop, parent, posPoints, appearDelay, scaleUpPoint = Point3(1), scaleUpTime = 0.5, startScale = Point3(0.01), poseExtraArgs = None):
    propTrack = Sequence(Wait(appearDelay), Func(__showProp, prop, parent, *posPoints))
    if poseExtraArgs:
        propTrack.append(Func(prop.pose, *poseExtraArgs))
    
    propTrack.append(LerpScaleInterval(prop, scaleUpTime, scaleUpPoint, startScale = startScale))
    return propTrack


def getPropThrowTrack(attack, prop, hitPoints = [], missPoints = [], hitDuration = 0.5, missDuration = 0.5, hitPointNames = 'none', missPointNames = 'none', lookAt = 'none', groundPointOffSet = 0, missScaleDown = None, parent = render):
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    battle = attack['battle']
    
    def getLambdas(list, prop, toon):
        for i in range(len(list)):
            if list[i] == 'face':
                
                list[i] = lambda toon = toon: __toonFacePoint(toon)
            elif list[i] == 'miss':
                
                list[i] = lambda prop = prop, toon = toon: __toonMissPoint(prop, toon)
            elif list[i] == 'bounceHit':
                
                list[i] = lambda prop = prop, toon = toon: __throwBounceHitPoint(prop, toon)
            elif list[i] == 'bounceMiss':
                
                list[i] = lambda prop = prop, toon = toon: __throwBounceMissPoint(prop, toon)
            
        
        return list

    if hitPointNames != 'none':
        hitPoints = getLambdas(hitPointNames, prop, toon)
    
    if missPointNames != 'none':
        missPoints = getLambdas(missPointNames, prop, toon)
    
    propTrack = Sequence()
    propTrack.append(Func(battle.movie.needRestoreRenderProp, prop))
    propTrack.append(Func(prop.wrtReparentTo, parent))
    if lookAt != 'none':
        propTrack.append(Func(prop.lookAt, lookAt))
    
    if dmg > 0:
        for i in range(len(hitPoints)):
            pos = hitPoints[i]
            propTrack.append(LerpPosInterval(prop, hitDuration, pos = pos))
        
    else:
        for i in range(len(missPoints)):
            pos = missPoints[i]
            propTrack.append(LerpPosInterval(prop, missDuration, pos = pos))
        
        if missScaleDown:
            propTrack.append(LerpScaleInterval(prop, missScaleDown, MovieUtil.PNT3_NEARZERO))
        
    propTrack.append(Func(MovieUtil.removeProp, prop))
    propTrack.append(Func(battle.movie.clearRenderProp, prop))
    return propTrack


def getThrowTrack(object, target, duration = 1.0, parent = render, gravity = -32.143999999999998):
    values = { }
    
    def calcOriginAndVelocity(object = object, target = target, values = values, duration = duration, parent = parent, gravity = gravity):
        if callable(target):
            target = target()
        
        object.wrtReparentTo(parent)
        values['origin'] = object.getPos(parent)
        origin = object.getPos(parent)
        values['velocity'] = (target[2] - origin[2] - 0.5 * gravity * duration * duration) / duration

    return Sequence(Func(calcOriginAndVelocity), LerpFunctionInterval(throwPos, fromData = 0.0, toData = 1.0, duration = duration, extraArgs = [
        object,
        duration,
        target,
        values,
        gravity]))


def throwPos(t, object, duration, target, values, gravity = -32.143999999999998):
    origin = values['origin']
    velocity = values['velocity']
    if callable(target):
        target = target()
    
    x = origin[0] * (1 - t) + target[0] * t
    y = origin[1] * (1 - t) + target[1] * t
    time = t * duration
    z = origin[2] + velocity * time + 0.5 * gravity * time * time
    object.setPos(x, y, z)


def getToonTakeDamageTrack(toon, died, dmg, delay, damageAnimNames = None, splicedDamageAnims = None, showDamageExtraTime = 0.01):
    toonTrack = Sequence()
    toonTrack.append(Wait(delay))
    if damageAnimNames:
        for d in damageAnimNames:
            toonTrack.append(ActorInterval(toon, d))
        
        indicatorTrack = Sequence(Wait(delay + showDamageExtraTime), Func(__doDamage, toon, dmg, died))
    else:
        splicedAnims = getSplicedAnimsTrack(splicedDamageAnims, actor = toon)
        toonTrack.append(splicedAnims)
        indicatorTrack = Sequence(Wait(delay + showDamageExtraTime), Func(__doDamage, toon, dmg, died))
    toonTrack.append(Func(toon.loop, 'neutral'))
    if died:
        toonTrack.append(Wait(5.0))
    
    return Parallel(toonTrack, indicatorTrack)


def getSplicedAnimsTrack(anims, actor = None):
    track = Sequence()
    for nextAnim in anims:
        delay = 9.9999999999999995e-007
        if len(nextAnim) >= 2:
            if nextAnim[1] > 0:
                delay = nextAnim[1]
            
        
        if len(nextAnim) <= 0:
            track.append(Wait(delay))
        elif len(nextAnim) == 1:
            track.append(ActorInterval(actor, nextAnim[0]))
        elif len(nextAnim) == 2:
            track.append(Wait(delay))
            track.append(ActorInterval(actor, nextAnim[0]))
        elif len(nextAnim) == 3:
            track.append(Wait(delay))
            track.append(ActorInterval(actor, nextAnim[0], startTime = nextAnim[2]))
        elif len(nextAnim) == 4:
            track.append(Wait(delay))
            duration = nextAnim[3]
            if duration < 0:
                startTime = nextAnim[2]
                endTime = startTime + duration
                if endTime <= 0:
                    endTime = 0.01
                
                track.append(ActorInterval(actor, nextAnim[0], startTime = startTime, endTime = endTime))
            else:
                track.append(ActorInterval(actor, nextAnim[0], startTime = nextAnim[2], duration = duration))
        elif len(nextAnim) == 5:
            track.append(Wait(delay))
            track.append(ActorInterval(nextAnim[4], nextAnim[0], startTime = nextAnim[2], duration = nextAnim[3]))
        
    
    return track


def getSplicedLerpAnims(animName, origDuration, newDuration, startTime = 0, fps = 30, reverse = 0):
    anims = []
    addition = 0
    numAnims = origDuration * fps
    timeInterval = newDuration / numAnims
    animInterval = origDuration / numAnims
    if reverse == 1:
        animInterval = -animInterval
    
    for i in range(0, numAnims):
        anims.append([
            animName,
            timeInterval,
            startTime + addition,
            animInterval])
        addition += animInterval
    
    return anims


def getSoundTrack(fileName, delay = 0.01, duration = None, node = None):
    soundEffect = globalBattleSoundCache.getSound(fileName)
    if duration:
        return Sequence(Wait(delay), SoundInterval(soundEffect, duration = duration, node = node))
    else:
        return Sequence(Wait(delay), SoundInterval(soundEffect, node = node))


def doClipOnTie(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    tie = globalPropPool.getProp('clip-on-tie')
    suitType = getSuitBodyType(attack['suitName'])
    if suitType == 'a':
        throwDelay = 2.1699999999999999
        damageDelay = 3.2999999999999998
        dodgeDelay = 3.1000000000000001
    elif suitType == 'b':
        throwDelay = 2.1699999999999999
        damageDelay = 3.2999999999999998
        dodgeDelay = 3.1000000000000001
    elif suitType == 'c':
        throwDelay = 1.45
        damageDelay = 2.6099999999999999
        dodgeDelay = 2.3399999999999999
    
    suitTrack = getSuitTrack(attack)
    posPoints = [
        Point3(0.66000000000000003, 0.51000000000000001, 0.28000000000000003),
        VBase3(-69.652000000000001, -17.199000000000002, 67.959999999999994)]
    tiePropTrack = Sequence(getPropAppearTrack(tie, suit.getRightHand(), posPoints, 0.5, MovieUtil.PNT3_ONE, scaleUpTime = 0.5, poseExtraArgs = [
        'clip-on-tie',
        0]))
    if dmg > 0:
        tiePropTrack.append(ActorInterval(tie, 'clip-on-tie', duration = throwDelay, startTime = 1.1000000000000001))
    else:
        tiePropTrack.append(Wait(throwDelay))
    tiePropTrack.append(Func(tie.setHpr, Point3(0, -90, 0)))
    tiePropTrack.append(getPropThrowTrack(attack, tie, [
        __toonFacePoint(toon)], [
        __toonGroundPoint(attack, toon, 0.10000000000000001)], hitDuration = 0.40000000000000002, missDuration = 0.80000000000000004, missScaleDown = 1.2))
    toonTrack = getToonTrack(attack, damageDelay, [
        'conked'], dodgeDelay, [
        'sidestep'])
    throwSound = getSoundTrack('SA_powertie_throw.mp3', delay = throwDelay + 1, node = suit)
    return Parallel(suitTrack, toonTrack, tiePropTrack, throwSound)


def doPoundKey(attack):
    suit = attack['suit']
    battle = attack['battle']
    phone = globalPropPool.getProp('phone')
    receiver = globalPropPool.getProp('receiver')
    BattleParticles.loadParticles()
    particleEffect = BattleParticles.createParticleEffect('PoundKey')
    BattleParticles.setEffectTexture(particleEffect, 'poundsign', color = Vec4(0, 0, 0, 1))
    suitTrack = getSuitTrack(attack)
    partTrack = getPartTrack(particleEffect, 2.1000000000000001, 1.55, [
        particleEffect,
        suit,
        0])
    phonePosPoints = [
        Point3(0.23000000000000001, 0.17000000000000001, -0.11),
        VBase3(5.9390000000000001, 2.7629999999999999, -177.59100000000001)]
    receiverPosPoints = [
        Point3(0.23000000000000001, 0.17000000000000001, -0.11),
        VBase3(5.9390000000000001, 2.7629999999999999, -177.59100000000001)]
    propTrack = Sequence(Wait(0.29999999999999999), Func(__showProp, phone, suit.getLeftHand(), phonePosPoints[0], phonePosPoints[1]), Func(__showProp, receiver, suit.getLeftHand(), receiverPosPoints[0], receiverPosPoints[1]), LerpScaleInterval(phone, 0.5, MovieUtil.PNT3_ONE, MovieUtil.PNT3_NEARZERO), Wait(0.73999999999999999), Func(receiver.wrtReparentTo, suit.getRightHand()), LerpPosHprInterval(receiver, 0.0001, Point3(-0.45000000000000001, 0.47999999999999998, -0.62), VBase3(-87.469999999999999, -18.210000000000001, 7.8200000000000003)), Wait(3.1400000000000001), Func(receiver.wrtReparentTo, phone), Wait(0.62), LerpScaleInterval(phone, 0.5, MovieUtil.PNT3_NEARZERO), Func(MovieUtil.removeProps, [
        receiver,
        phone]))
    toonTrack = getToonTrack(attack, 2.7000000000000002, [
        'cringe'], 1.8999999999999999, [
        'sidestep'])
    soundTrack = getSoundTrack('SA_hangup.mp3', delay = 1.3, node = suit)
    return Parallel(suitTrack, toonTrack, propTrack, partTrack, soundTrack)


def doShred(attack):
    suit = attack['suit']
    battle = attack['battle']
    paper = globalPropPool.getProp('shredder-paper')
    shredder = globalPropPool.getProp('shredder')
    particleEffect = BattleParticles.createParticleEffect('Shred')
    suitTrack = getSuitTrack(attack)
    partTrack = getPartTrack(particleEffect, 3.5, 1.8999999999999999, [
        particleEffect,
        suit,
        0])
    paperPosPoints = [
        Point3(0.58999999999999997, -0.31, 0.81000000000000005),
        VBase3(79.224000000000004, 32.576000000000001, -179.44900000000001)]
    paperPropTrack = getPropTrack(paper, suit.getRightHand(), paperPosPoints, 2.3999999999999999, 1.0000000000000001e-005, scaleUpTime = 0.20000000000000001, anim = 1, propName = 'shredder-paper', animDuration = 1.5, animStartTime = 2.7999999999999998)
    shredderPosPoints = [
        Point3(0, -0.12, -0.34000000000000002),
        VBase3(-90.0, -53.770000000000003, -0.0)]
    shredderPropTrack = getPropTrack(shredder, suit.getLeftHand(), shredderPosPoints, 1, 3, scaleUpPoint = Point3(4.8099999999999996, 4.8099999999999996, 4.8099999999999996))
    toonTrack = getToonTrack(attack, suitTrack.getDuration() - 1.1000000000000001, [
        'conked'], suitTrack.getDuration() - 3.1000000000000001, [
        'sidestep'])
    soundTrack = getSoundTrack('SA_shred.mp3', delay = 3.3999999999999999, node = suit)
    return Parallel(suitTrack, paperPropTrack, shredderPropTrack, partTrack, toonTrack, soundTrack)


def doFillWithLead(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    pencil = globalPropPool.getProp('pencil')
    sharpener = globalPropPool.getProp('sharpener')
    BattleParticles.loadParticles()
    sprayEffect = BattleParticles.createParticleEffect(file = 'fillWithLeadSpray')
    headSmotherEffect = BattleParticles.createParticleEffect(file = 'fillWithLeadSmother')
    torsoSmotherEffect = BattleParticles.createParticleEffect(file = 'fillWithLeadSmother')
    legsSmotherEffect = BattleParticles.createParticleEffect(file = 'fillWithLeadSmother')
    BattleParticles.setEffectTexture(sprayEffect, 'roll-o-dex', color = Vec4(0, 0, 0, 1))
    BattleParticles.setEffectTexture(headSmotherEffect, 'roll-o-dex', color = Vec4(0, 0, 0, 1))
    BattleParticles.setEffectTexture(torsoSmotherEffect, 'roll-o-dex', color = Vec4(0, 0, 0, 1))
    BattleParticles.setEffectTexture(legsSmotherEffect, 'roll-o-dex', color = Vec4(0, 0, 0, 1))
    suitTrack = getSuitTrack(attack)
    sprayTrack = getPartTrack(sprayEffect, 2.5, 1.8999999999999999, [
        sprayEffect,
        suit,
        0])
    pencilPosPoints = [
        Point3(-0.28999999999999998, -0.33000000000000002, -0.13),
        VBase3(160.565, -11.653, -169.244)]
    pencilPropTrack = getPropTrack(pencil, suit.getRightHand(), pencilPosPoints, 0.69999999999999996, 3.2000000000000002, scaleUpTime = 0.20000000000000001)
    sharpenerPosPoints = [
        Point3(0.0, 0.0, -0.029999999999999999),
        MovieUtil.PNT3_ZERO]
    sharpenerPropTrack = getPropTrack(sharpener, suit.getLeftHand(), sharpenerPosPoints, 1.3, 2.2999999999999998, scaleUpPoint = MovieUtil.PNT3_ONE)
    damageAnims = []
    damageAnims.append([
        'conked',
        suitTrack.getDuration() - 1.5,
        1.0000000000000001e-005,
        1.3999999999999999])
    damageAnims.append([
        'conked',
        1.0000000000000001e-005,
        0.69999999999999996,
        0.69999999999999996])
    damageAnims.append([
        'conked',
        1.0000000000000001e-005,
        0.69999999999999996,
        0.69999999999999996])
    damageAnims.append([
        'conked',
        1.0000000000000001e-005,
        1.3999999999999999])
    toonTrack = getToonTrack(attack, splicedDamageAnims = damageAnims, dodgeDelay = suitTrack.getDuration() - 3.1000000000000001, dodgeAnimNames = [
        'sidestep'], showDamageExtraTime = 4.5, showMissedExtraTime = 1.6000000000000001)
    animal = toon.style.getAnimal()
    bodyScale = ToontownGlobals.toonBodyScales[animal]
    headEffectHeight = __toonFacePoint(toon).getZ()
    legsHeight = ToontownGlobals.legHeightDict[toon.style.legs] * bodyScale
    torsoEffectHeight = ToontownGlobals.torsoHeightDict[toon.style.torso] * bodyScale / 2 + legsHeight
    legsEffectHeight = legsHeight / 2
    effectX = headSmotherEffect.getX()
    effectY = headSmotherEffect.getY()
    headSmotherEffect.setPos(effectX, effectY - 1.5, headEffectHeight)
    torsoSmotherEffect.setPos(effectX, effectY - 1, torsoEffectHeight)
    legsSmotherEffect.setPos(effectX, effectY - 0.59999999999999998, legsEffectHeight)
    partDelay = 3.5
    partIvalDelay = 0.69999999999999996
    partDuration = 1.0
    headTrack = getPartTrack(headSmotherEffect, partDelay, partDuration, [
        headSmotherEffect,
        toon,
        0])
    torsoTrack = getPartTrack(torsoSmotherEffect, partDelay + partIvalDelay, partDuration, [
        torsoSmotherEffect,
        toon,
        0])
    legsTrack = getPartTrack(legsSmotherEffect, partDelay + partIvalDelay * 2, partDuration, [
        legsSmotherEffect,
        toon,
        0])
    
    def colorParts(parts):
        track = Parallel()
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            track.append(Func(nextPart.setColorScale, Vec4(0, 0, 0, 1)))
        
        return track

    
    def resetParts(parts):
        track = Parallel()
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            track.append(Func(nextPart.clearColorScale))
        
        return track

    if dmg > 0:
        colorTrack = Sequence()
        headParts = toon.getHeadParts()
        torsoParts = toon.getTorsoParts()
        legsParts = toon.getLegsParts()
        colorTrack.append(Wait(partDelay + 0.20000000000000001))
        colorTrack.append(Func(battle.movie.needRestoreColor))
        colorTrack.append(colorParts(headParts))
        colorTrack.append(Wait(partIvalDelay))
        colorTrack.append(colorParts(torsoParts))
        colorTrack.append(Wait(partIvalDelay))
        colorTrack.append(colorParts(legsParts))
        colorTrack.append(Wait(2.5))
        colorTrack.append(resetParts(headParts))
        colorTrack.append(resetParts(torsoParts))
        colorTrack.append(resetParts(legsParts))
        colorTrack.append(Func(battle.movie.clearRestoreColor))
        return Parallel(suitTrack, pencilPropTrack, sharpenerPropTrack, sprayTrack, headTrack, torsoTrack, legsTrack, colorTrack, toonTrack)
    else:
        return Parallel(suitTrack, pencilPropTrack, sharpenerPropTrack, sprayTrack, toonTrack)


def doFountainPen(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    pen = globalPropPool.getProp('pen')
    
    def getPenTip(pen = pen):
        tip = pen.find('**/joint-toSpray')
        return tip.getPos(render)

    
    hitPoint = lambda toon = toon: __toonFacePoint(toon)
    
    missPoint = lambda prop = pen, toon = toon: __toonMissPoint(prop, toon, 0, parent = render)
    hitSprayTrack = MovieUtil.getSprayTrack(battle, VBase4(0, 0, 0, 1), getPenTip, hitPoint, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, horizScale = 0.10000000000000001, vertScale = 0.10000000000000001)
    missSprayTrack = MovieUtil.getSprayTrack(battle, VBase4(0, 0, 0, 1), getPenTip, missPoint, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, horizScale = 0.10000000000000001, vertScale = 0.10000000000000001)
    suitTrack = getSuitTrack(attack)
    propTrack = Sequence(Wait(0.01), Func(__showProp, pen, suit.getRightHand(), MovieUtil.PNT3_ZERO), LerpScaleInterval(pen, 0.5, Point3(1.5, 1.5, 1.5)), Wait(1.05))
    if dmg > 0:
        propTrack.append(hitSprayTrack)
    else:
        propTrack.append(missSprayTrack)
    propTrack += [
        LerpScaleInterval(pen, 0.5, MovieUtil.PNT3_NEARZERO),
        Func(MovieUtil.removeProp, pen)]
    splashTrack = Sequence()
    if dmg > 0:
        
        def prepSplash(splash, targetPoint):
            splash.reparentTo(render)
            splash.setPos(targetPoint)
            scale = splash.getScale()
            splash.setBillboardPointWorld()
            splash.setScale(scale)

        splash = globalPropPool.getProp('splash-from-splat')
        splash.setColor(0, 0, 0, 1)
        splash.setScale(0.14999999999999999)
        splashTrack = Sequence(Func(battle.movie.needRestoreRenderProp, splash), Wait(1.6499999999999999), Func(prepSplash, splash, __toonFacePoint(toon)), ActorInterval(splash, 'splash-from-splat'), Func(MovieUtil.removeProp, splash), Func(battle.movie.clearRenderProp, splash))
        headParts = toon.getHeadParts()
        splashTrack.append(Func(battle.movie.needRestoreColor))
        for partNum in range(0, headParts.getNumPaths()):
            nextPart = headParts.getPath(partNum)
            splashTrack.append(Func(nextPart.setColorScale, Vec4(0, 0, 0, 1)))
        
        splashTrack.append(Func(MovieUtil.removeProp, splash))
        splashTrack.append(Wait(2.6000000000000001))
        for partNum in range(0, headParts.getNumPaths()):
            nextPart = headParts.getPath(partNum)
            splashTrack.append(Func(nextPart.clearColorScale))
        
        splashTrack.append(Func(battle.movie.clearRestoreColor))
    
    penSpill = BattleParticles.createParticleEffect(file = 'penSpill')
    penSpill.setPos(getPenTip())
    penSpillTrack = getPartTrack(penSpill, 1.3999999999999999, 0.69999999999999996, [
        penSpill,
        pen,
        0])
    toonTrack = getToonTrack(attack, 1.8100000000000001, [
        'conked'], dodgeDelay = 0.11, splicedDodgeAnims = [
        [
            'duck',
            0.01,
            0.59999999999999998]], showMissedExtraTime = 1.6599999999999999)
    soundTrack = getSoundTrack('SA_fountain_pen.mp3', delay = 1.6000000000000001, node = suit)
    return Parallel(suitTrack, toonTrack, propTrack, soundTrack, penSpillTrack, splashTrack)


def doRubOut(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    pad = globalPropPool.getProp('pad')
    pencil = globalPropPool.getProp('pencil')
    headEffect = BattleParticles.createParticleEffect('RubOut', color = toon.style.getHeadColor())
    torsoEffect = BattleParticles.createParticleEffect('RubOut', color = toon.style.getArmColor())
    legsEffect = BattleParticles.createParticleEffect('RubOut', color = toon.style.getLegColor())
    suitTrack = getSuitTrack(attack)
    padPosPoints = [
        Point3(-0.66000000000000003, 0.81000000000000005, -0.059999999999999998),
        VBase3(14.93, -2.29, 180.0)]
    padPropTrack = getPropTrack(pad, suit.getLeftHand(), padPosPoints, 0.5, 2.5699999999999998)
    pencilPosPoints = [
        Point3(0.040000000000000001, -0.38, -0.10000000000000001),
        VBase3(-170.22300000000001, -3.762, -62.929000000000002)]
    pencilPropTrack = getPropTrack(pencil, suit.getRightHand(), pencilPosPoints, 0.5, 2.5699999999999998)
    toonTrack = getToonTrack(attack, 2.2000000000000002, [
        'conked'], 2.0, [
        'jump'])
    hideTrack = Sequence()
    headParts = toon.getHeadParts()
    torsoParts = toon.getTorsoParts()
    legsParts = toon.getLegsParts()
    animal = toon.style.getAnimal()
    bodyScale = ToontownGlobals.toonBodyScales[animal]
    headEffectHeight = __toonFacePoint(toon).getZ()
    legsHeight = ToontownGlobals.legHeightDict[toon.style.legs] * bodyScale
    torsoEffectHeight = ToontownGlobals.torsoHeightDict[toon.style.torso] * bodyScale / 2 + legsHeight
    legsEffectHeight = legsHeight / 2
    effectX = headEffect.getX()
    effectY = headEffect.getY()
    headEffect.setPos(effectX, effectY - 1.5, headEffectHeight)
    torsoEffect.setPos(effectX, effectY - 1, torsoEffectHeight)
    legsEffect.setPos(effectX, effectY - 0.59999999999999998, legsEffectHeight)
    partDelay = 2.5
    headTrack = getPartTrack(headEffect, partDelay + 0, 0.5, [
        headEffect,
        toon,
        0])
    torsoTrack = getPartTrack(torsoEffect, partDelay + 1.1000000000000001, 0.5, [
        torsoEffect,
        toon,
        0])
    legsTrack = getPartTrack(legsEffect, partDelay + 2.2000000000000002, 0.5, [
        legsEffect,
        toon,
        0])
    
    def hideParts(parts):
        track = Parallel()
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            track.append(Func(nextPart.setTransparency, 1))
            track.append(LerpFunctionInterval(nextPart.setAlphaScale, fromData = 1, toData = 0, duration = 0.20000000000000001))
        
        return track

    
    def showParts(parts):
        track = Parallel()
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            track.append(Func(nextPart.clearColorScale))
            track.append(Func(nextPart.clearTransparency))
        
        return track

    soundTrack = getSoundTrack('SA_rubout.mp3', delay = 1.7, node = suit)
    if dmg > 0:
        hideTrack.append(Wait(2.2000000000000002))
        hideTrack.append(Func(battle.movie.needRestoreColor))
        hideTrack.append(hideParts(headParts))
        hideTrack.append(Wait(0.40000000000000002))
        hideTrack.append(hideParts(torsoParts))
        hideTrack.append(Wait(0.40000000000000002))
        hideTrack.append(hideParts(legsParts))
        hideTrack.append(Wait(1))
        hideTrack.append(showParts(headParts))
        hideTrack.append(showParts(torsoParts))
        hideTrack.append(showParts(legsParts))
        hideTrack.append(Func(battle.movie.clearRestoreColor))
        return Parallel(suitTrack, toonTrack, padPropTrack, pencilPropTrack, soundTrack, hideTrack, headTrack, torsoTrack, legsTrack)
    else:
        return Parallel(suitTrack, toonTrack, padPropTrack, pencilPropTrack, soundTrack)


def doFingerWag(attack):
    suit = attack['suit']
    battle = attack['battle']
    BattleParticles.loadParticles()
    particleEffect = BattleParticles.createParticleEffect('FingerWag')
    BattleParticles.setEffectTexture(particleEffect, 'blah', color = Vec4(0.55000000000000004, 0, 0.55000000000000004, 1))
    suitType = getSuitBodyType(attack['suitName'])
    if suitType == 'a':
        partDelay = 1.3
        damageDelay = 2.7000000000000002
        dodgeDelay = 1.7
    elif suitType == 'b':
        partDelay = 1.3
        damageDelay = 2.7000000000000002
        dodgeDelay = 1.8
    elif suitType == 'c':
        partDelay = 1.3
        damageDelay = 2.7000000000000002
        dodgeDelay = 2.0
    
    suitTrack = getSuitTrack(attack)
    partTrack = getPartTrack(particleEffect, partDelay, 2, [
        particleEffect,
        suit,
        0])
    suitName = attack['suitName']
    if suitName == 'mm':
        particleEffect.setPos(0.16700000000000001, 1.5, 2.7309999999999999)
    elif suitName == 'tw':
        particleEffect.setPos(0.16700000000000001, 1.8, 5)
        particleEffect.setHpr(-90.0, -60.0, 180.0)
    elif suitName == 'pp':
        particleEffect.setPos(0.16700000000000001, 1, 4.0999999999999996)
    elif suitName == 'bs':
        particleEffect.setPos(0.16700000000000001, 1, 5.0999999999999996)
    elif suitName == 'bw':
        particleEffect.setPos(0.16700000000000001, 1.8999999999999999, suit.getHeight() - 1.8)
        particleEffect.setP(-110)
    
    toonTrack = getToonTrack(attack, damageDelay, [
        'slip-backward'], dodgeDelay, [
        'sidestep'])
    soundTrack = getSoundTrack('SA_finger_wag.mp3', delay = 1.3, node = suit)
    return Parallel(suitTrack, toonTrack, partTrack, soundTrack)


def doWriteOff(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    pad = globalPropPool.getProp('pad')
    pencil = globalPropPool.getProp('pencil')
    BattleParticles.loadParticles()
    checkmark = MovieUtil.copyProp(BattleParticles.getParticle('checkmark'))
    checkmark.setBillboardPointEye()
    suitTrack = getSuitTrack(attack)
    padPosPoints = [
        Point3(-0.25, 1.3799999999999999, -0.080000000000000002),
        VBase3(-19.077999999999999, -6.6029999999999998, -171.59399999999999)]
    padPropTrack = getPropTrack(pad, suit.getLeftHand(), padPosPoints, 0.5, 2.5699999999999998, Point3(1.8899999999999999, 1.8899999999999999, 1.8899999999999999))
    
    missPoint = lambda checkmark = checkmark, toon = toon: __toonMissPoint(checkmark, toon)
    pencilPosPoints = [
        Point3(-0.46999999999999997, 1.0800000000000001, 0.28000000000000003),
        VBase3(21.045000000000002, 12.702, -176.374)]
    extraArgsForShowProp = [
        pencil,
        suit.getRightHand()]
    extraArgsForShowProp.extend(pencilPosPoints)
    pencilPropTrack = Sequence(Wait(0.5), Func(__showProp, *extraArgsForShowProp), LerpScaleInterval(pencil, 0.5, Point3(1.5, 1.5, 1.5), startScale = Point3(0.01)), Wait(2), Func(battle.movie.needRestoreRenderProp, checkmark), Func(checkmark.reparentTo, render), Func(checkmark.setScale, 1.6000000000000001), Func(checkmark.setPosHpr, pencil, 0, 0, 0, 0, 0, 0), Func(checkmark.setP, 0), Func(checkmark.setR, 0))
    pencilPropTrack.append(getPropThrowTrack(attack, checkmark, [
        __toonFacePoint(toon)], [
        missPoint]))
    pencilPropTrack.append(Func(MovieUtil.removeProp, checkmark))
    pencilPropTrack.append(Func(battle.movie.clearRenderProp, checkmark))
    pencilPropTrack.append(Wait(0.29999999999999999))
    pencilPropTrack.append(LerpScaleInterval(pencil, 0.5, MovieUtil.PNT3_NEARZERO))
    pencilPropTrack.append(Func(MovieUtil.removeProp, pencil))
    toonTrack = getToonTrack(attack, 3.3999999999999999, [
        'slip-forward'], 2.3999999999999999, [
        'sidestep'])
    soundTrack = Sequence(Wait(2.2999999999999998), SoundInterval(globalBattleSoundCache.getSound('SA_writeoff_pen_only.mp3'), duration = 0.90000000000000002, node = suit), SoundInterval(globalBattleSoundCache.getSound('SA_writeoff_ding_only.mp3'), node = suit))
    return Parallel(suitTrack, toonTrack, padPropTrack, pencilPropTrack, soundTrack)


def doRubberStamp(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    suitTrack = getSuitTrack(attack)
    stamp = globalPropPool.getProp('rubber-stamp')
    pad = globalPropPool.getProp('pad')
    cancelled = __makeCancelledNodePath()
    suitType = getSuitBodyType(attack['suitName'])
    if suitType == 'a':
        padPosPoints = [
            Point3(-0.65000000000000002, 0.82999999999999996, -0.040000000000000001),
            VBase3(5.625, 4.4560000000000004, -165.125)]
        stampPosPoints = [
            Point3(-0.64000000000000001, -0.17000000000000001, -0.029999999999999999),
            MovieUtil.PNT3_ZERO]
    elif suitType == 'c':
        padPosPoints = [
            Point3(0.19, -0.55000000000000004, -0.20999999999999999),
            VBase3(-166.75999999999999, -4.0010000000000003, -1.6579999999999999)]
        stampPosPoints = [
            Point3(-0.64000000000000001, -0.080000000000000002, 0.11),
            MovieUtil.PNT3_ZERO]
    else:
        padPosPoints = [
            Point3(-0.65000000000000002, 0.82999999999999996, -0.040000000000000001),
            VBase3(5.625, 4.4560000000000004, -165.125)]
        stampPosPoints = [
            Point3(-0.64000000000000001, -0.17000000000000001, -0.029999999999999999),
            MovieUtil.PNT3_ZERO]
    padPropTrack = getPropTrack(pad, suit.getLeftHand(), padPosPoints, 9.9999999999999995e-007, 3.2000000000000002)
    
    missPoint = lambda cancelled = cancelled, toon = toon: __toonMissPoint(cancelled, toon)
    propTrack = Sequence(Func(__showProp, stamp, suit.getRightHand(), stampPosPoints[0], stampPosPoints[1]), LerpScaleInterval(stamp, 0.5, MovieUtil.PNT3_ONE), Wait(2.6000000000000001), Func(battle.movie.needRestoreRenderProp, cancelled), Func(cancelled.reparentTo, render), Func(cancelled.setScale, 0.59999999999999998), Func(cancelled.setPosHpr, stamp, 0.81000000000000005, -1.1100000000000001, -0.16, 0, 0, 90), Func(cancelled.setP, 0), Func(cancelled.setR, 0))
    propTrack.append(getPropThrowTrack(attack, cancelled, [
        __toonFacePoint(toon)], [
        missPoint]))
    propTrack.append(Func(MovieUtil.removeProp, cancelled))
    propTrack.append(Func(battle.movie.clearRenderProp, cancelled))
    propTrack.append(Wait(0.29999999999999999))
    propTrack.append(LerpScaleInterval(stamp, 0.5, MovieUtil.PNT3_NEARZERO))
    propTrack.append(Func(MovieUtil.removeProp, stamp))
    toonTrack = getToonTrack(attack, 3.3999999999999999, [
        'conked'], 1.8999999999999999, [
        'sidestep'])
    soundTrack = getSoundTrack('SA_rubber_stamp.mp3', delay = 1.3, duration = 1.1000000000000001, node = suit)
    return Parallel(suitTrack, toonTrack, propTrack, padPropTrack, soundTrack)


def doRazzleDazzle(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    hitSuit = dmg > 0
    sign = globalPropPool.getProp('smile')
    BattleParticles.loadParticles()
    particleEffect = BattleParticles.createParticleEffect('Smile')
    suitTrack = getSuitTrack(attack)
    signPosPoints = [
        Point3(0.0, -0.41999999999999998, -0.040000000000000001),
        VBase3(105.715, 73.977000000000004, 65.932000000000002)]
    if hitSuit:
        
        hitPoint = lambda toon = toon: __toonFacePoint(toon)
    else:
        
        hitPoint = lambda particleEffect = particleEffect, toon = toon, suit = suit: __toonMissPoint(particleEffect, toon, parent = suit.getRightHand())
    signPropTrack = Sequence(Wait(0.5), Func(__showProp, sign, suit.getRightHand(), signPosPoints[0], signPosPoints[1]), LerpScaleInterval(sign, 0.5, Point3(1.3899999999999999, 1.3899999999999999, 1.3899999999999999)), Wait(0.5), Func(battle.movie.needRestoreParticleEffect, particleEffect), Func(particleEffect.start, sign), Func(particleEffect.wrtReparentTo, render), LerpPosInterval(particleEffect, 2.0, pos = hitPoint), Func(particleEffect.cleanup), Func(battle.movie.clearRestoreParticleEffect, particleEffect))
    signPropAnimTrack = ActorInterval(sign, 'smile', duration = 4, startTime = 0)
    toonTrack = getToonTrack(attack, 2.6000000000000001, [
        'cringe'], 1.8999999999999999, [
        'sidestep'])
    soundTrack = getSoundTrack('SA_razzle_dazzle.mp3', delay = 1.6000000000000001, node = suit)
    return Sequence(Parallel(suitTrack, signPropTrack, signPropAnimTrack, toonTrack, soundTrack), Func(MovieUtil.removeProp, sign))


def doSynergy(attack):
    suit = attack['suit']
    battle = attack['battle']
    targets = attack['target']
    damageDelay = 1.7
    hitAtleastOneToon = 0
    for t in targets:
        if t['hp'] > 0:
            hitAtleastOneToon = 1
        
    
    particleEffect = BattleParticles.createParticleEffect('Synergy')
    waterfallEffect = BattleParticles.createParticleEffect(file = 'synergyWaterfall')
    suitTrack = getSuitAnimTrack(attack)
    partTrack = getPartTrack(particleEffect, 1.0, 1.8999999999999999, [
        particleEffect,
        suit,
        0])
    waterfallTrack = getPartTrack(waterfallEffect, 0.80000000000000004, 1.8999999999999999, [
        waterfallEffect,
        suit,
        0])
    damageAnims = [
        [
            'slip-forward']]
    dodgeAnims = []
    dodgeAnims.append([
        'jump',
        0.01,
        0,
        0.59999999999999998])
    dodgeAnims.extend(getSplicedLerpAnims('jump', 0.31, 1.3, startTime = 0.59999999999999998))
    dodgeAnims.append([
        'jump',
        0,
        0.91000000000000003])
    toonTracks = getToonTracks(attack, damageDelay = damageDelay, damageAnimNames = [
        'slip-forward'], dodgeDelay = 0.91000000000000003, splicedDodgeAnims = dodgeAnims, showMissedExtraTime = 1.0)
    synergySoundTrack = Sequence(Wait(0.90000000000000002), SoundInterval(globalBattleSoundCache.getSound('SA_synergy.mp3'), node = suit))
    if hitAtleastOneToon > 0:
        fallingSoundTrack = Sequence(Wait(damageDelay + 0.5), SoundInterval(globalBattleSoundCache.getSound('Toon_bodyfall_synergy.mp3'), node = suit))
        return Parallel(suitTrack, partTrack, waterfallTrack, synergySoundTrack, fallingSoundTrack, toonTracks)
    else:
        return Parallel(suitTrack, partTrack, waterfallTrack, synergySoundTrack, toonTracks)


def doTeeOff(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    club = globalPropPool.getProp('golf-club')
    ball = globalPropPool.getProp('golf-ball')
    suitTrack = getSuitTrack(attack)
    clubPosPoints = [
        MovieUtil.PNT3_ZERO,
        VBase3(63.097000000000001, 43.988, -18.434999999999999)]
    clubPropTrack = getPropTrack(club, suit.getLeftHand(), clubPosPoints, 0.5, 5.2000000000000002, Point3(1.1000000000000001, 1.1000000000000001, 1.1000000000000001))
    suitName = attack['suitName']
    if suitName == 'ym':
        ballPosPoints = [
            Point3(2.1000000000000001, 0, 0.10000000000000001)]
    elif suitName == 'tbc':
        ballPosPoints = [
            Point3(4.0999999999999996, 0, 0.10000000000000001)]
    elif suitName == 'm':
        ballPosPoints = [
            Point3(3.2000000000000002, 0, 0.10000000000000001)]
    elif suitName == 'rb':
        ballPosPoints = [
            Point3(4.2000000000000002, 0, 0.10000000000000001)]
    else:
        ballPosPoints = [
            Point3(2.1000000000000001, 0, 0.10000000000000001)]
    ballPropTrack = Sequence(getPropAppearTrack(ball, suit, ballPosPoints, 1.7, Point3(1.5, 1.5, 1.5)), Func(battle.movie.needRestoreRenderProp, ball), Func(ball.wrtReparentTo, render), Wait(2.1499999999999999))
    
    missPoint = lambda ball = ball, toon = toon: __toonMissPoint(ball, toon)
    ballPropTrack.append(getPropThrowTrack(attack, ball, [
        __toonFacePoint(toon)], [
        missPoint]))
    ballPropTrack.append(Func(battle.movie.clearRenderProp, ball))
    dodgeDelay = suitTrack.getDuration() - 4.3499999999999996
    toonTrack = getToonTrack(attack, suitTrack.getDuration() - 2.25, [
        'conked'], dodgeDelay, [
        'duck'], showMissedExtraTime = 1.7)
    soundTrack = getSoundTrack('SA_tee_off.mp3', delay = 4.0999999999999996, node = suit)
    return Parallel(suitTrack, toonTrack, clubPropTrack, ballPropTrack, soundTrack)


def doBrainStorm(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    BattleParticles.loadParticles()
    snowEffect = BattleParticles.createParticleEffect('BrainStorm')
    snowEffect2 = BattleParticles.createParticleEffect('BrainStorm')
    snowEffect3 = BattleParticles.createParticleEffect('BrainStorm')
    effectColor = Vec4(0.65000000000000002, 0.79000000000000004, 0.93000000000000005, 0.29999999999999999)
    BattleParticles.setEffectTexture(snowEffect, 'brainstorm-box', color = effectColor)
    BattleParticles.setEffectTexture(snowEffect2, 'brainstorm-env', color = effectColor)
    BattleParticles.setEffectTexture(snowEffect3, 'brainstorm-track', color = effectColor)
    cloud = globalPropPool.getProp('stormcloud')
    suitType = getSuitBodyType(attack['suitName'])
    if suitType == 'a':
        partDelay = 1.2
        damageDelay = 4.5
        dodgeDelay = 3.2999999999999998
    elif suitType == 'b':
        partDelay = 1.2
        damageDelay = 4.5
        dodgeDelay = 3.2999999999999998
    elif suitType == 'c':
        partDelay = 1.2
        damageDelay = 4.5
        dodgeDelay = 3.2999999999999998
    
    suitTrack = getSuitTrack(attack, delay = 0.90000000000000002)
    initialCloudHeight = suit.height + 3
    cloudPosPoints = [
        Point3(0, 3, initialCloudHeight),
        VBase3(180, 0, 0)]
    cloudPropTrack = Sequence()
    cloudPropTrack.append(Func(cloud.pose, 'stormcloud', 0))
    cloudPropTrack.append(getPropAppearTrack(cloud, suit, cloudPosPoints, 9.9999999999999995e-007, Point3(3, 3, 3), scaleUpTime = 0.69999999999999996))
    cloudPropTrack.append(Func(battle.movie.needRestoreRenderProp, cloud))
    cloudPropTrack.append(Func(cloud.wrtReparentTo, render))
    targetPoint = __toonFacePoint(toon)
    targetPoint.setZ(targetPoint[2] + 3)
    cloudPropTrack.append(Wait(1.1000000000000001))
    cloudPropTrack.append(LerpPosInterval(cloud, 1, pos = targetPoint))
    cloudPropTrack.append(Wait(partDelay))
    cloudPropTrack.append(Parallel(ParticleInterval(snowEffect, cloud, worldRelative = 0, duration = 2.2000000000000002), Sequence(Wait(0.5), ParticleInterval(snowEffect2, cloud, worldRelative = 0, duration = 1.7)), Sequence(Wait(1.0), ParticleInterval(snowEffect3, cloud, worldRelative = 0, duration = 1.2)), Sequence(ActorInterval(cloud, 'stormcloud', startTime = 3, duration = 0.5), ActorInterval(cloud, 'stormcloud', startTime = 2.5, duration = 0.5), ActorInterval(cloud, 'stormcloud', startTime = 1, duration = 1.5))))
    cloudPropTrack.append(Wait(0.40000000000000002))
    cloudPropTrack.append(LerpScaleInterval(cloud, 0.5, MovieUtil.PNT3_NEARZERO))
    cloudPropTrack.append(Func(MovieUtil.removeProp, cloud))
    cloudPropTrack.append(Func(battle.movie.clearRenderProp, cloud))
    damageAnims = [
        [
            'cringe',
            0.01,
            0.40000000000000002,
            0.80000000000000004],
        [
            'duck',
            9.9999999999999995e-007,
            1.6000000000000001]]
    toonTrack = getToonTrack(attack, damageDelay = damageDelay, splicedDamageAnims = damageAnims, dodgeDelay = dodgeDelay, dodgeAnimNames = [
        'sidestep'], showMissedExtraTime = 1.1000000000000001)
    soundTrack = getSoundTrack('SA_brainstorm.mp3', delay = 2.6000000000000001, node = suit)
    return Parallel(suitTrack, toonTrack, cloudPropTrack, soundTrack)


def doBuzzWord(attack):
    suit = attack['suit']
    target = attack['target']
    toon = target['toon']
    battle = attack['battle']
    BattleParticles.loadParticles()
    particleEffects = []
    texturesList = [
        'buzzwords-crash',
        'buzzwords-inc',
        'buzzwords-main',
        'buzzwords-over',
        'buzzwords-syn']
    for i in range(0, 5):
        effect = BattleParticles.createParticleEffect('BuzzWord')
        if whrandom.random() > 0.5:
            BattleParticles.setEffectTexture(effect, texturesList[i], color = Vec4(1, 0.93999999999999995, 0.02, 1))
        else:
            BattleParticles.setEffectTexture(effect, texturesList[i], color = Vec4(0, 0, 0, 1))
        particleEffects.append(effect)
    
    suitType = getSuitBodyType(attack['suitName'])
    if suitType == 'a':
        partDelay = 4.0
        partDuration = 2.2000000000000002
        damageDelay = 4.5
        dodgeDelay = 3.7999999999999998
    elif suitType == 'b':
        partDelay = 1.3
        partDuration = 2
        damageDelay = 2.5
        dodgeDelay = 1.8
    elif suitType == 'c':
        partDelay = 4.0
        partDuration = 2.2000000000000002
        damageDelay = 4.5
        dodgeDelay = 3.7999999999999998
    
    suitName = suit.getStyleName()
    if suitName == 'm':
        for effect in particleEffects:
            effect.setPos(0, 2.7999999999999998, suit.getHeight() - 2.5)
            effect.setHpr(0, -20, 0)
        
    elif suitName == 'mm':
        for effect in particleEffects:
            effect.setPos(0, 2.1000000000000001, suit.getHeight() - 0.80000000000000004)
        
    
    suitTrack = getSuitTrack(attack)
    particleTracks = []
    for effect in particleEffects:
        particleTracks.append(getPartTrack(effect, partDelay, partDuration, [
            effect,
            suit,
            0]))
    
    toonTrack = getToonTrack(attack, damageDelay = damageDelay, damageAnimNames = [
        'cringe'], splicedDodgeAnims = [
        [
            'duck',
            dodgeDelay,
            1.3999999999999999]], showMissedExtraTime = dodgeDelay + 0.5)
    soundTrack = getSoundTrack('SA_buzz_word.mp3', delay = 3.8999999999999999, node = suit)
    return Parallel(suitTrack, toonTrack, soundTrack, *particleTracks)


def doDemotion(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    BattleParticles.loadParticles()
    sprayEffect = BattleParticles.createParticleEffect('DemotionSpray')
    freezeEffect = BattleParticles.createParticleEffect('DemotionFreeze')
    unFreezeEffect = BattleParticles.createParticleEffect(file = 'demotionUnFreeze')
    BattleParticles.setEffectTexture(sprayEffect, 'snow-particle')
    BattleParticles.setEffectTexture(freezeEffect, 'snow-particle')
    BattleParticles.setEffectTexture(unFreezeEffect, 'snow-particle')
    facePoint = __toonFacePoint(toon)
    freezeEffect.setPos(0, 0, facePoint.getZ())
    unFreezeEffect.setPos(0, 0, facePoint.getZ())
    suitTrack = getSuitTrack(attack)
    partTrack = getPartTrack(sprayEffect, 0.69999999999999996, 1.1000000000000001, [
        sprayEffect,
        suit,
        0])
    partTrack2 = getPartTrack(freezeEffect, 1.3999999999999999, 2.8999999999999999, [
        freezeEffect,
        toon,
        0])
    partTrack3 = getPartTrack(unFreezeEffect, 6.6500000000000004, 0.5, [
        unFreezeEffect,
        toon,
        0])
    dodgeAnims = [
        [
            'duck',
            9.9999999999999995e-007,
            0.80000000000000004]]
    damageAnims = []
    damageAnims.append([
        'cringe',
        0.01,
        0,
        0.5])
    damageAnims.extend(getSplicedLerpAnims('cringe', 0.40000000000000002, 0.5, startTime = 0.5))
    damageAnims.extend(getSplicedLerpAnims('cringe', 0.29999999999999999, 0.5, startTime = 0.90000000000000002))
    damageAnims.extend(getSplicedLerpAnims('cringe', 0.29999999999999999, 0.59999999999999998, startTime = 1.2))
    damageAnims.append([
        'cringe',
        2.6000000000000001,
        1.5])
    toonTrack = getToonTrack(attack, damageDelay = 1.0, splicedDamageAnims = damageAnims, splicedDodgeAnims = dodgeAnims, showMissedExtraTime = 1.6000000000000001, showDamageExtraTime = 1.3)
    soundTrack = getSoundTrack('SA_demotion.mp3', delay = 1.2, node = suit)
    if dmg > 0:
        return Parallel(suitTrack, toonTrack, soundTrack, partTrack, partTrack2, partTrack3)
    else:
        return Parallel(suitTrack, toonTrack, soundTrack, partTrack)


def doCanned(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    dmg = target['hp']
    toon = target['toon']
    hips = toon.getHipsParts()
    propDelay = 0.80000000000000004
    suitType = getSuitBodyType(attack['suitName'])
    if suitType == 'c':
        suitDelay = 1.1299999999999999
        dodgeDelay = 3.1000000000000001
    else:
        suitDelay = 1.8300000000000001
        dodgeDelay = 3.6000000000000001
    throwDuration = 1.5
    can = globalPropPool.getProp('can')
    scale = 26
    torso = toon.style.torso
    torso = torso[0]
    if torso == 's':
        scaleUpPoint = Point3(scale * 2.6299999999999999, scale * 2.6299999999999999, scale * 1.9975000000000001)
    elif torso == 'm':
        scaleUpPoint = Point3(scale * 2.6299999999999999, scale * 2.6299999999999999, scale * 1.7975000000000001)
    elif torso == 'l':
        scaleUpPoint = Point3(scale * 2.6299999999999999, scale * 2.6299999999999999, scale * 2.3100000000000001)
    
    canHpr = VBase3(-173.47, -0.41999999999999998, 162.09)
    suitTrack = getSuitTrack(attack)
    posPoints = [
        Point3(-0.14000000000000001, 0.14999999999999999, 0.080000000000000002),
        VBase3(-10.584, 11.945, -161.684)]
    throwTrack = Sequence(getPropAppearTrack(can, suit.getRightHand(), posPoints, propDelay, Point3(6, 6, 6), scaleUpTime = 0.5))
    propDelay = propDelay + 0.5
    throwTrack.append(Wait(suitDelay))
    hitPoint = toon.getPos(battle)
    hitPoint.setX(hitPoint.getX() + 1.1000000000000001)
    hitPoint.setY(hitPoint.getY() - 0.5)
    hitPoint.setZ(hitPoint.getZ() + toon.height + 1.1000000000000001)
    throwTrack.append(Func(battle.movie.needRestoreRenderProp, can))
    throwTrack.append(getThrowTrack(can, hitPoint, duration = throwDuration, parent = battle))
    if dmg > 0:
        can2 = MovieUtil.copyProp(can)
        hips1 = hips.getPath(2)
        hips2 = hips.getPath(1)
        can2Point = Point3(hitPoint.getX(), hitPoint.getY() + 6.4000000000000004, hitPoint.getZ())
        can2.setPos(can2Point)
        can2.setScale(scaleUpPoint)
        can2.setHpr(canHpr)
        throwTrack.append(Func(battle.movie.needRestoreHips))
        throwTrack.append(Func(can.wrtReparentTo, hips1))
        throwTrack.append(Func(can2.reparentTo, hips2))
        throwTrack.append(Wait(2.3999999999999999))
        throwTrack.append(Func(MovieUtil.removeProp, can2))
        throwTrack.append(Func(battle.movie.clearRestoreHips))
        scaleTrack = Sequence(Wait(propDelay + suitDelay), LerpScaleInterval(can, throwDuration, scaleUpPoint))
        hprTrack = Sequence(Wait(propDelay + suitDelay), LerpHprInterval(can, throwDuration, canHpr))
        soundTrack = Sequence(Wait(2.6000000000000001), SoundInterval(globalBattleSoundCache.getSound('SA_canned_tossup_only.mp3'), node = suit), SoundInterval(globalBattleSoundCache.getSound('SA_canned_impact_only.mp3'), node = suit))
    else:
        land = toon.getPos(battle)
        land.setZ(land.getZ() + 0.69999999999999996)
        bouncePoint1 = Point3(land.getX(), land.getY() - 1.5, land.getZ() + 2.5)
        bouncePoint2 = Point3(land.getX(), land.getY() - 2.1000000000000001, land.getZ() - 0.20000000000000001)
        bouncePoint3 = Point3(land.getX(), land.getY() - 3.1000000000000001, land.getZ() + 1.5)
        bouncePoint4 = Point3(land.getX(), land.getY() - 4.0999999999999996, land.getZ() + 0.29999999999999999)
        throwTrack.append(LerpPosInterval(can, 0.40000000000000002, land))
        throwTrack.append(LerpPosInterval(can, 0.40000000000000002, bouncePoint1))
        throwTrack.append(LerpPosInterval(can, 0.29999999999999999, bouncePoint2))
        throwTrack.append(LerpPosInterval(can, 0.29999999999999999, bouncePoint3))
        throwTrack.append(LerpPosInterval(can, 0.29999999999999999, bouncePoint4))
        throwTrack.append(Wait(1.1000000000000001))
        throwTrack.append(LerpScaleInterval(can, 0.29999999999999999, MovieUtil.PNT3_NEARZERO))
        scaleTrack = Sequence(Wait(propDelay + suitDelay), LerpScaleInterval(can, throwDuration, Point3(11, 11, 11)))
        hprTrack = Sequence(Wait(propDelay + suitDelay), LerpHprInterval(can, throwDuration, canHpr), Wait(0.40000000000000002), LerpHprInterval(can, 0.40000000000000002, Point3(83.269999999999996, 19.52, -177.91999999999999)), LerpHprInterval(can, 0.29999999999999999, Point3(95.239999999999995, -72.090000000000003, 88.650000000000006)), LerpHprInterval(can, 0.20000000000000001, Point3(-96.340000000000003, -2.6299999999999999, 179.88999999999999)))
        soundTrack = getSoundTrack('SA_canned_tossup_only.mp3', delay = 2.6000000000000001, node = suit)
    canTrack = Sequence(Parallel(throwTrack, scaleTrack, hprTrack), Func(MovieUtil.removeProp, can), Func(battle.movie.clearRenderProp, can))
    damageAnims = [
        [
            'struggle',
            propDelay + suitDelay + throwDuration,
            0.01,
            0.69999999999999996],
        [
            'slip-backward',
            0.01,
            0.45000000000000001]]
    toonTrack = getToonTrack(attack, splicedDamageAnims = damageAnims, dodgeDelay = dodgeDelay, dodgeAnimNames = [
        'sidestep'], showDamageExtraTime = propDelay + suitDelay + 2.3999999999999999)
    return Parallel(suitTrack, toonTrack, canTrack, soundTrack)


def doDownsize(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    damageDelay = 2.2999999999999998
    sprayEffect = BattleParticles.createParticleEffect(file = 'downsizeSpray')
    cloudEffect = BattleParticles.createParticleEffect(file = 'downsizeCloud')
    toonPos = toon.getPos(toon)
    cloudPos = Point3(toonPos.getX(), toonPos.getY(), toonPos.getZ() + toon.getHeight() * 0.55000000000000004)
    cloudEffect.setPos(cloudPos)
    suitTrack = getSuitTrack(attack)
    sprayTrack = getPartTrack(sprayEffect, 1.0, 1.28, [
        sprayEffect,
        suit,
        0])
    cloudTrack = getPartTrack(cloudEffect, 2.1000000000000001, 1.8999999999999999, [
        cloudEffect,
        toon,
        0])
    if dmg > 0:
        initialScale = toon.getScale()
        downScale = Vec3(0.40000000000000002, 0.40000000000000002, 0.40000000000000002)
        shrinkTrack = Sequence(Wait(damageDelay + 0.5), Func(battle.movie.needRestoreToonScale), LerpScaleInterval(toon, 1.0, downScale * 1.1000000000000001), LerpScaleInterval(toon, 0.10000000000000001, downScale * 0.90000000000000002), LerpScaleInterval(toon, 0.10000000000000001, downScale * 1.05), LerpScaleInterval(toon, 0.10000000000000001, downScale * 0.94999999999999996), LerpScaleInterval(toon, 0.10000000000000001, downScale), Wait(2.1000000000000001), LerpScaleInterval(toon, 0.5, initialScale * 1.5), LerpScaleInterval(toon, 0.14999999999999999, initialScale * 0.5), LerpScaleInterval(toon, 0.14999999999999999, initialScale * 1.2), LerpScaleInterval(toon, 0.14999999999999999, initialScale * 0.80000000000000004), LerpScaleInterval(toon, 0.14999999999999999, initialScale), Func(battle.movie.clearRestoreToonScale))
    
    damageAnims = []
    damageAnims.append([
        'juggle',
        0.01,
        0.87,
        0.5])
    damageAnims.append([
        'lose',
        0.01,
        2.1699999999999999,
        0.93000000000000005])
    damageAnims.append([
        'lose',
        0.01,
        3.1000000000000001,
        -0.93000000000000005])
    damageAnims.append([
        'struggle',
        0.01,
        0.80000000000000004,
        1.8])
    damageAnims.append([
        'sidestep-right',
        0.01,
        2.9700000000000002,
        1.49])
    toonTrack = getToonTrack(attack, damageDelay = damageDelay, splicedDamageAnims = damageAnims, dodgeDelay = 0.59999999999999998, dodgeAnimNames = [
        'sidestep'])
    if dmg > 0:
        return Parallel(suitTrack, sprayTrack, cloudTrack, shrinkTrack, toonTrack)
    else:
        return Parallel(suitTrack, sprayTrack, toonTrack)


def doPinkSlip(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    paper = globalPropPool.getProp('pink-slip')
    throwDelay = 3.0299999999999998
    throwDuration = 0.5
    suitTrack = getSuitTrack(attack)
    posPoints = [
        Point3(0.070000000000000007, -0.059999999999999998, -0.17999999999999999),
        VBase3(-172.07499999999999, -26.715, -89.131)]
    paperAppearTrack = Sequence(getPropAppearTrack(paper, suit.getRightHand(), posPoints, 0.80000000000000004, Point3(8, 8, 8), scaleUpTime = 0.5))
    paperAppearTrack.append(Wait(1.73))
    hitPoint = __toonGroundPoint(attack, toon, 0.20000000000000001, parent = battle)
    paperAppearTrack.append(Func(battle.movie.needRestoreRenderProp, paper))
    paperAppearTrack.append(Func(paper.wrtReparentTo, battle))
    paperAppearTrack.append(LerpPosInterval(paper, throwDuration, hitPoint))
    if dmg > 0:
        paperPause = 0.01
        slidePoint = Point3(hitPoint.getX(), hitPoint.getY() - 5, hitPoint.getZ() + 4)
        landPoint = Point3(hitPoint.getX(), hitPoint.getY() - 5, hitPoint.getZ())
        paperAppearTrack.append(Wait(paperPause))
        paperAppearTrack.append(LerpPosInterval(paper, 0.20000000000000001, slidePoint))
        paperAppearTrack.append(LerpPosInterval(paper, 1.1000000000000001, landPoint))
        paperSpinTrack = Sequence(Wait(throwDelay), LerpHprInterval(paper, throwDuration, VBase3(300, 0, 0)), Wait(paperPause), LerpHprInterval(paper, 1.3, VBase3(-200, 100, 100)))
    else:
        slidePoint = Point3(hitPoint.getX(), hitPoint.getY() - 5, hitPoint.getZ())
        paperAppearTrack.append(LerpPosInterval(paper, 0.5, slidePoint))
        paperSpinTrack = Sequence(Wait(throwDelay), LerpHprInterval(paper, throwDuration, VBase3(300, 0, 0)), LerpHprInterval(paper, 0.5, VBase3(10, 0, 0)))
    propTrack = Sequence()
    propTrack.append(Parallel(paperAppearTrack, paperSpinTrack))
    propTrack.append(LerpScaleInterval(paper, 0.40000000000000002, MovieUtil.PNT3_NEARZERO))
    propTrack.append(Func(MovieUtil.removeProp, paper))
    propTrack.append(Func(battle.movie.clearRenderProp, paper))
    damageAnims = [
        [
            'jump',
            0.01,
            0.29999999999999999,
            0.69999999999999996],
        [
            'slip-forward',
            0.01]]
    toonTrack = getToonTrack(attack, damageDelay = 2.8100000000000001, splicedDamageAnims = damageAnims, dodgeDelay = 2.7999999999999998, dodgeAnimNames = [
        'jump'], showDamageExtraTime = 0.90000000000000002)
    soundTrack = getSoundTrack('SA_pink_slip.mp3', delay = 2.8999999999999999, duration = 1.1000000000000001, node = suit)
    return Parallel(suitTrack, toonTrack, propTrack, soundTrack)


def doReOrg(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    damageDelay = 1.7
    attackDelay = 1.7
    sprayEffect = BattleParticles.createParticleEffect(file = 'reorgSpray')
    suitTrack = getSuitTrack(attack)
    partTrack = getPartTrack(sprayEffect, 1.0, 1.8999999999999999, [
        sprayEffect,
        suit,
        0])
    if dmg > 0:
        headParts = toon.getHeadParts()
        print '***********headParts pos=', headParts[0].getPos()
        print '***********headParts hpr=', headParts[0].getHpr()
        headTracks = Parallel()
        for partNum in range(0, headParts.getNumPaths()):
            part = headParts.getPath(partNum)
            x = part.getX()
            y = part.getY()
            z = part.getZ()
            h = part.getH()
            p = part.getP()
            r = part.getR()
            headTracks.append(Sequence(Wait(attackDelay), LerpPosInterval(part, 0.10000000000000001, Point3(x - 0.20000000000000001, y, z - 0.029999999999999999)), LerpPosInterval(part, 0.10000000000000001, Point3(x + 0.40000000000000002, y, z - 0.029999999999999999)), LerpPosInterval(part, 0.10000000000000001, Point3(x - 0.40000000000000002, y, z - 0.029999999999999999)), LerpPosInterval(part, 0.10000000000000001, Point3(x + 0.40000000000000002, y, z - 0.029999999999999999)), LerpPosInterval(part, 0.10000000000000001, Point3(x - 0.20000000000000001, y, z - 0.040000000000000001)), LerpPosInterval(part, 0.25, Point3(x, y, z + 2.2000000000000002)), LerpHprInterval(part, 0.40000000000000002, VBase3(360, 0, 180)), LerpPosInterval(part, 0.29999999999999999, Point3(x, y, z + 3.1000000000000001)), LerpPosInterval(part, 0.14999999999999999, Point3(x, y, z + 0.29999999999999999)), Wait(0.14999999999999999), LerpHprInterval(part, 0.59999999999999998, VBase3(-745, 0, 180), startHpr = VBase3(0, 0, 180)), LerpHprInterval(part, 0.80000000000000004, VBase3(25, 0, 180), startHpr = VBase3(0, 0, 180)), LerpPosInterval(part, 0.14999999999999999, Point3(x, y, z + 1)), LerpHprInterval(part, 0.29999999999999999, VBase3(h, p, r)), Wait(0.20000000000000001), LerpPosInterval(part, 0.10000000000000001, Point3(x, y, z)), Wait(0.90000000000000002)))
        
        
        def getChestTrack(part, attackDelay = attackDelay):
            origScale = part.getScale()
            return Sequence(Wait(attackDelay), LerpHprInterval(part, 1.1000000000000001, VBase3(180, 0, 0)), Wait(1.1000000000000001), LerpHprInterval(part, 1.1000000000000001, part.getHpr()))

        chestTracks = Parallel()
        arms = toon.findAllMatches('**/arms')
        sleeves = toon.findAllMatches('**/sleeves')
        hands = toon.findAllMatches('**/hands')
        print '*************arms hpr=', arms[0].getHpr()
        for partNum in range(0, arms.getNumPaths()):
            chestTracks.append(getChestTrack(arms.getPath(partNum)))
            chestTracks.append(getChestTrack(sleeves.getPath(partNum)))
            chestTracks.append(getChestTrack(hands.getPath(partNum)))
        
    
    damageAnims = [
        [
            'neutral',
            0.01,
            0.01,
            0.5],
        [
            'juggle',
            0.01,
            0.01,
            1.48],
        [
            'think',
            0.01,
            2.2799999999999998]]
    dodgeAnims = []
    dodgeAnims.append([
        'think',
        0.01,
        0,
        0.59999999999999998])
    toonTrack = getToonTrack(attack, damageDelay = damageDelay, splicedDamageAnims = damageAnims, dodgeDelay = 0.01, dodgeAnimNames = [
        'duck'], showDamageExtraTime = 2.1000000000000001, showMissedExtraTime = 2.0)
    if dmg > 0:
        return Parallel(suitTrack, partTrack, toonTrack, headTracks, chestTracks)
    else:
        return Parallel(suitTrack, partTrack, toonTrack)


def doSacked(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    dmg = target['hp']
    toon = target['toon']
    hips = toon.getHipsParts()
    propDelay = 0.84999999999999998
    suitDelay = 1.9299999999999999
    throwDuration = 0.90000000000000002
    sack = globalPropPool.getProp('sandbag')
    initialScale = Point3(0.65000000000000002, 1.47, 1.28)
    scaleUpPoint = Point3(1.05, 1.6699999999999999, 0.97999999999999998) * 4.0999999999999996
    sackHpr = VBase3(-154.33000000000001, -6.3300000000000001, 163.80000000000001)
    suitTrack = getSuitTrack(attack)
    posPoints = [
        Point3(0.51000000000000001, -2.0299999999999998, -0.72999999999999998),
        VBase3(90.0, -24.98, 77.730000000000004)]
    sackAppearTrack = Sequence(getPropAppearTrack(sack, suit.getRightHand(), posPoints, propDelay, initialScale, scaleUpTime = 0.20000000000000001))
    propDelay = propDelay + 0.20000000000000001
    sackAppearTrack.append(Wait(suitDelay))
    hitPoint = toon.getPos(battle)
    if dmg > 0:
        hitPoint.setX(hitPoint.getX() + 2.1000000000000001)
        hitPoint.setY(hitPoint.getY() + 0.90000000000000002)
        hitPoint.setZ(hitPoint.getZ() + toon.height + 1.2)
    else:
        hitPoint.setZ(hitPoint.getZ() - 0.20000000000000001)
    sackAppearTrack.append(Func(battle.movie.needRestoreRenderProp, sack))
    sackAppearTrack.append(getThrowTrack(sack, hitPoint, duration = throwDuration, parent = battle))
    if dmg > 0:
        sack2 = MovieUtil.copyProp(sack)
        hips1 = hips.getPath(2)
        hips2 = hips.getPath(1)
        sack2.hide()
        sack2.reparentTo(battle)
        sack2.setPos(Point3(hitPoint.getX(), hitPoint.getY(), hitPoint.getZ()))
        sack2.setScale(scaleUpPoint)
        sack2.setHpr(sackHpr)
        sackAppearTrack.append(Func(battle.movie.needRestoreHips))
        sackAppearTrack.append(Func(sack.wrtReparentTo, hips1))
        sackAppearTrack.append(Func(sack2.show))
        sackAppearTrack.append(Func(sack2.wrtReparentTo, hips2))
        sackAppearTrack.append(Wait(2.3999999999999999))
        sackAppearTrack.append(Func(MovieUtil.removeProp, sack2))
        sackAppearTrack.append(Func(battle.movie.clearRestoreHips))
        scaleTrack = Sequence(Wait(propDelay + suitDelay), LerpScaleInterval(sack, throwDuration, scaleUpPoint), Wait(1.8), LerpScaleInterval(sack, 0.29999999999999999, MovieUtil.PNT3_NEARZERO))
        hprTrack = Sequence(Wait(propDelay + suitDelay), LerpHprInterval(sack, throwDuration, sackHpr))
        sackTrack = Sequence(Parallel(sackAppearTrack, scaleTrack, hprTrack), Func(MovieUtil.removeProp, sack), Func(battle.movie.clearRenderProp, sack))
    else:
        sackAppearTrack.append(Wait(1.1000000000000001))
        sackAppearTrack.append(LerpScaleInterval(sack, 0.29999999999999999, MovieUtil.PNT3_NEARZERO))
        sackTrack = Sequence(sackAppearTrack, Func(MovieUtil.removeProp, sack), Func(battle.movie.clearRenderProp, sack))
    damageAnims = [
        [
            'struggle',
            0.01,
            0.01,
            0.69999999999999996],
        [
            'slip-backward',
            0.01,
            0.45000000000000001]]
    toonTrack = getToonTrack(attack, damageDelay = propDelay + suitDelay + throwDuration, splicedDamageAnims = damageAnims, dodgeDelay = 3.0, dodgeAnimNames = [
        'sidestep'], showDamageExtraTime = 1.8, showMissedExtraTime = 0.80000000000000004)
    return Parallel(suitTrack, toonTrack, sackTrack)


def doGlowerPower(attack):
    suit = attack['suit']
    battle = attack['battle']
    leftKnives = []
    rightKnives = []
    for i in range(0, 3):
        leftKnives.append(globalPropPool.getProp('dagger'))
        rightKnives.append(globalPropPool.getProp('dagger'))
    
    suitTrack = getSuitTrack(attack)
    suitName = suit.getStyleName()
    if suitName == 'hh':
        leftPosPoints = [
            Point3(0.29999999999999999, 4.2999999999999998, 5.2999999999999998),
            MovieUtil.PNT3_ZERO]
        rightPosPoints = [
            Point3(-0.29999999999999999, 4.2999999999999998, 5.2999999999999998),
            MovieUtil.PNT3_ZERO]
    elif suitName == 'tbc':
        leftPosPoints = [
            Point3(0.59999999999999998, 4.5, 6),
            MovieUtil.PNT3_ZERO]
        rightPosPoints = [
            Point3(-0.59999999999999998, 4.5, 6),
            MovieUtil.PNT3_ZERO]
    else:
        leftPosPoints = [
            Point3(0.40000000000000002, 3.7999999999999998, 3.7000000000000002),
            MovieUtil.PNT3_ZERO]
        rightPosPoints = [
            Point3(-0.40000000000000002, 3.7999999999999998, 3.7000000000000002),
            MovieUtil.PNT3_ZERO]
    leftKnifeTracks = Parallel()
    rightKnifeTracks = Parallel()
    for i in range(0, 3):
        knifeDelay = 0.11
        leftTrack = Sequence()
        leftTrack.append(Wait(1.1000000000000001))
        leftTrack.append(Wait(i * knifeDelay))
        leftTrack.append(getPropAppearTrack(leftKnives[i], suit, leftPosPoints, 9.9999999999999995e-007, Point3(0.40000000000000002, 0.40000000000000002, 0.40000000000000002), scaleUpTime = 0.10000000000000001))
        leftTrack.append(getPropThrowTrack(attack, leftKnives[i], hitPointNames = [
            'face'], missPointNames = [
            'miss'], hitDuration = 0.29999999999999999, missDuration = 0.29999999999999999))
        leftKnifeTracks.append(leftTrack)
        rightTrack = Sequence()
        rightTrack.append(Wait(1.1000000000000001))
        rightTrack.append(Wait(i * knifeDelay))
        rightTrack.append(getPropAppearTrack(rightKnives[i], suit, rightPosPoints, 9.9999999999999995e-007, Point3(0.40000000000000002, 0.40000000000000002, 0.40000000000000002), scaleUpTime = 0.10000000000000001))
        rightTrack.append(getPropThrowTrack(attack, rightKnives[i], hitPointNames = [
            'face'], missPointNames = [
            'miss'], hitDuration = 0.29999999999999999, missDuration = 0.29999999999999999))
        rightKnifeTracks.append(rightTrack)
    
    damageAnims = [
        [
            'slip-backward',
            0.01,
            0.34999999999999998]]
    toonTrack = getToonTrack(attack, damageDelay = 1.6000000000000001, splicedDamageAnims = damageAnims, dodgeDelay = 0.69999999999999996, dodgeAnimNames = [
        'sidestep'])
    soundTrack = getSoundTrack('SA_glower_power.mp3', delay = 1.1000000000000001, node = suit)
    return Parallel(suitTrack, toonTrack, soundTrack, leftKnifeTracks, rightKnifeTracks)


def doHalfWindsor(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    tie = globalPropPool.getProp('half-windsor')
    throwDelay = 2.1699999999999999
    damageDelay = 3.3999999999999999
    dodgeDelay = 2.3999999999999999
    suitTrack = getSuitTrack(attack)
    posPoints = [
        Point3(0.02, 0.88, 0.47999999999999998),
        VBase3(99, -3, -108.2)]
    tiePropTrack = getPropAppearTrack(tie, suit.getRightHand(), posPoints, 0.5, Point3(7, 7, 7), scaleUpTime = 0.5)
    tiePropTrack.append(Wait(throwDelay))
    missPoint = __toonMissBehindPoint(toon, parent = battle)
    missPoint.setX(missPoint.getX() - 1.1000000000000001)
    missPoint.setZ(missPoint.getZ() + 4)
    hitPoint = __toonFacePoint(toon, parent = battle)
    hitPoint.setX(hitPoint.getX() - 1.1000000000000001)
    hitPoint.setY(hitPoint.getY() - 0.69999999999999996)
    hitPoint.setZ(hitPoint.getZ() + 0.90000000000000002)
    tiePropTrack.append(getPropThrowTrack(attack, tie, [
        hitPoint], [
        missPoint], hitDuration = 0.40000000000000002, missDuration = 0.80000000000000004, missScaleDown = 0.29999999999999999, parent = battle))
    damageAnims = [
        [
            'conked',
            0.01,
            0.01,
            0.40000000000000002],
        [
            'cringe',
            0.01,
            0.69999999999999996]]
    toonTrack = getToonTrack(attack, damageDelay = damageDelay, splicedDamageAnims = damageAnims, dodgeDelay = dodgeDelay, dodgeAnimNames = [
        'sidestep'])
    return Parallel(suitTrack, toonTrack, tiePropTrack)


def doHeadShrink(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    damageDelay = 2.1000000000000001
    dodgeDelay = 1.3999999999999999
    shrinkSpray = BattleParticles.createParticleEffect(file = 'headShrinkSpray')
    shrinkCloud = BattleParticles.createParticleEffect(file = 'headShrinkCloud')
    shrinkDrop = BattleParticles.createParticleEffect(file = 'headShrinkDrop')
    suitTrack = getSuitTrack(attack)
    sprayTrack = getPartTrack(shrinkSpray, 0.29999999999999999, 1.3999999999999999, [
        shrinkSpray,
        suit,
        0])
    shrinkCloud.reparentTo(battle)
    adjust = 0.40000000000000002
    x = toon.getX(battle)
    y = toon.getY(battle) - adjust
    z = 8
    shrinkCloud.setPos(Point3(x, y, z))
    shrinkDrop.setPos(Point3(0, 0 - adjust, 7.5))
    off = 0.69999999999999996
    cloudPoints = [
        Point3(x + off, y, z),
        Point3(x + off / 2, y + off / 2, z),
        Point3(x, y + off, z),
        Point3(x - off / 2, y + off / 2, z),
        Point3(x - off, y, z),
        Point3(x - off / 2, y - off / 2, z),
        Point3(x, y - off, z),
        Point3(x + off / 2, y - off / 2, z),
        Point3(x + off, y, z),
        Point3(x, y, z)]
    circleTrack = Sequence()
    for point in cloudPoints:
        circleTrack.append(LerpPosInterval(shrinkCloud, 0.14000000000000001, point, other = battle))
    
    cloudTrack = Sequence()
    cloudTrack.append(Wait(1.4199999999999999))
    cloudTrack.append(Func(battle.movie.needRestoreParticleEffect, shrinkCloud))
    cloudTrack.append(Func(shrinkCloud.start, battle))
    cloudTrack.append(circleTrack)
    cloudTrack.append(circleTrack)
    cloudTrack.append(LerpFunctionInterval(shrinkCloud.setAlphaScale, fromData = 1, toData = 0, duration = 0.69999999999999996))
    cloudTrack.append(Func(shrinkCloud.cleanup))
    cloudTrack.append(Func(battle.movie.clearRestoreParticleEffect, shrinkCloud))
    shrinkDelay = 0.80000000000000004
    shrinkDuration = 1.1000000000000001
    shrinkTrack = Sequence()
    if dmg > 0:
        headParts = toon.getHeadParts()
        initialScale = headParts.getPath(0).getScale()[0]
        shrinkTrack.append(Wait(damageDelay + shrinkDelay))
        
        def scaleHeadParallel(scale, duration, headParts = headParts):
            headTracks = Parallel()
            for partNum in range(0, headParts.getNumPaths()):
                nextPart = headParts.getPath(partNum)
                headTracks.append(LerpScaleInterval(nextPart, duration, Point3(scale, scale, scale)))
            
            return headTracks

        shrinkTrack.append(Func(battle.movie.needRestoreHeadScale))
        shrinkTrack.append(scaleHeadParallel(0.59999999999999998, shrinkDuration))
        shrinkTrack.append(Wait(1.6000000000000001))
        shrinkTrack.append(scaleHeadParallel(initialScale * 3.2000000000000002, 0.40000000000000002))
        shrinkTrack.append(scaleHeadParallel(initialScale * 0.69999999999999996, 0.40000000000000002))
        shrinkTrack.append(scaleHeadParallel(initialScale * 2.5, 0.29999999999999999))
        shrinkTrack.append(scaleHeadParallel(initialScale * 0.80000000000000004, 0.29999999999999999))
        shrinkTrack.append(scaleHeadParallel(initialScale * 1.8999999999999999, 0.20000000000000001))
        shrinkTrack.append(scaleHeadParallel(initialScale * 0.84999999999999998, 0.20000000000000001))
        shrinkTrack.append(scaleHeadParallel(initialScale * 1.7, 0.14999999999999999))
        shrinkTrack.append(scaleHeadParallel(initialScale * 0.90000000000000002, 0.14999999999999999))
        shrinkTrack.append(scaleHeadParallel(initialScale * 1.3, 0.10000000000000001))
        shrinkTrack.append(scaleHeadParallel(initialScale, 0.10000000000000001))
        shrinkTrack.append(Func(battle.movie.clearRestoreHeadScale))
        shrinkTrack.append(Wait(0.69999999999999996))
    
    dropTrack = getPartTrack(shrinkDrop, 1.5, 2.5, [
        shrinkDrop,
        toon,
        0])
    damageAnims = []
    damageAnims.append([
        'cringe',
        0.01,
        0.65000000000000002,
        0.20000000000000001])
    damageAnims.extend(getSplicedLerpAnims('cringe', 0.64000000000000001, 1.0, startTime = 0.84999999999999998))
    damageAnims.append([
        'cringe',
        0.40000000000000002,
        1.49])
    damageAnims.append([
        'conked',
        0.01,
        3.6000000000000001,
        -1.6000000000000001])
    damageAnims.append([
        'conked',
        0.01,
        3.1000000000000001,
        0.40000000000000002])
    toonTrack = getToonTrack(attack, damageDelay = damageDelay, splicedDamageAnims = damageAnims, dodgeDelay = dodgeDelay, dodgeAnimNames = [
        'sidestep'])
    if dmg > 0:
        shrinkSound = globalBattleSoundCache.getSound('SA_head_shrink_only.mp3')
        growSound = globalBattleSoundCache.getSound('SA_head_grow_back_only.mp3')
        soundTrack = Sequence(Wait(2.1000000000000001), SoundInterval(shrinkSound, duration = 2.1000000000000001, node = suit), Wait(1.6000000000000001), SoundInterval(growSound, node = suit))
        return Parallel(suitTrack, sprayTrack, cloudTrack, dropTrack, toonTrack, shrinkTrack, soundTrack)
    else:
        return Parallel(suitTrack, sprayTrack, cloudTrack, dropTrack, toonTrack)


def doRolodex(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    rollodex = globalPropPool.getProp('rollodex')
    particleEffect2 = BattleParticles.createParticleEffect(file = 'rollodexWaterfall')
    particleEffect3 = BattleParticles.createParticleEffect(file = 'rollodexStream')
    suitType = getSuitBodyType(attack['suitName'])
    if suitType == 'a':
        propPosPoints = [
            Point3(-0.51000000000000001, -0.029999999999999999, -0.10000000000000001),
            VBase3(89.673000000000002, 2.1659999999999999, 177.786)]
        propScale = Point3(1.2, 1.2, 1.2)
        partDelay = 2.6000000000000001
        part2Delay = 2.7999999999999998
        part3Delay = 3.2000000000000002
        partDuration = 1.6000000000000001
        part2Duration = 1.8999999999999999
        part3Duration = 1
        damageDelay = 3.7999999999999998
        dodgeDelay = 2.5
    elif suitType == 'b':
        propPosPoints = [
            Point3(0.12, 0.23999999999999999, 0.01),
            VBase3(99.031999999999996, 5.9729999999999999, -179.839)]
        propScale = Point3(0.91000000000000003, 0.91000000000000003, 0.91000000000000003)
        partDelay = 2.8999999999999999
        part2Delay = 3.1000000000000001
        part3Delay = 3.5
        partDuration = 1.6000000000000001
        part2Duration = 1.8999999999999999
        part3Duration = 1
        damageDelay = 4
        dodgeDelay = 2.5
    elif suitType == 'c':
        propPosPoints = [
            Point3(-0.51000000000000001, -0.029999999999999999, -0.10000000000000001),
            VBase3(89.673000000000002, 2.1659999999999999, 177.786)]
        propScale = Point3(1.2, 1.2, 1.2)
        partDelay = 2.2999999999999998
        part2Delay = 2.7999999999999998
        part3Delay = 3.2000000000000002
        partDuration = 1.8999999999999999
        part2Duration = 1.8999999999999999
        part3Duration = 1
        damageDelay = 3.5
        dodgeDelay = 2.5
    
    
    hitPoint = lambda toon = toon: __toonFacePoint(toon)
    partTrack2 = getPartTrack(particleEffect2, part2Delay, part2Duration, [
        particleEffect2,
        suit,
        0])
    partTrack3 = getPartTrack(particleEffect3, part3Delay, part3Duration, [
        particleEffect3,
        suit,
        0])
    suitTrack = getSuitTrack(attack)
    propTrack = getPropTrack(rollodex, suit.getLeftHand(), propPosPoints, 9.9999999999999995e-007, 4.7000000000000002, scaleUpPoint = propScale, anim = 0, propName = 'rollodex', animDuration = 0, animStartTime = 0)
    toonTrack = getToonTrack(attack, damageDelay, [
        'conked'], dodgeDelay, [
        'sidestep'])
    soundTrack = getSoundTrack('SA_rolodex.mp3', delay = 2.7999999999999998, node = suit)
    return Parallel(suitTrack, toonTrack, propTrack, soundTrack, partTrack2, partTrack3)


def doEvilEye(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    eye = globalPropPool.getProp('evil-eye')
    damageDelay = 2.4399999999999999
    dodgeDelay = 1.6399999999999999
    suitName = suit.getStyleName()
    if suitName == 'cr':
        posPoints = [
            Point3(-0.46000000000000002, 4.8499999999999996, 5.2800000000000002),
            VBase3(-155.0, -20.0, 0.0)]
    elif suitName == 'tf':
        posPoints = [
            Point3(-0.40000000000000002, 3.6499999999999999, 5.0099999999999998),
            VBase3(-155.0, -20.0, 0.0)]
    elif suitName == 'le':
        posPoints = [
            Point3(-0.64000000000000001, 4.4500000000000002, 5.9100000000000001),
            VBase3(-155.0, -20.0, 0.0)]
    else:
        posPoints = [
            Point3(-0.40000000000000002, 3.6499999999999999, 5.0099999999999998),
            VBase3(-155.0, -20.0, 0.0)]
    appearDelay = 0.80000000000000004
    suitHoldStart = 1.0600000000000001
    suitHoldStop = 1.6899999999999999
    suitHoldDuration = suitHoldStop - suitHoldStart
    eyeHoldDuration = 1.1000000000000001
    moveDuration = 1.1000000000000001
    suitSplicedAnims = []
    suitSplicedAnims.append([
        'glower',
        0.01,
        0.01,
        suitHoldStart])
    suitSplicedAnims.extend(getSplicedLerpAnims('glower', suitHoldDuration, 1.1000000000000001, startTime = suitHoldStart))
    suitSplicedAnims.append([
        'glower',
        0.01,
        suitHoldStop])
    suitTrack = getSuitTrack(attack, splicedAnims = suitSplicedAnims)
    eyeAppearTrack = Sequence(Wait(suitHoldStart), Func(__showProp, eye, suit, posPoints[0], posPoints[1]), LerpScaleInterval(eye, suitHoldDuration, Point3(11, 11, 11)), Wait(eyeHoldDuration * 0.29999999999999999), LerpHprInterval(eye, 0.02, Point3(205, 40, 0)), Wait(eyeHoldDuration * 0.69999999999999996), Func(battle.movie.needRestoreRenderProp, eye), Func(eye.wrtReparentTo, battle))
    toonFace = __toonFacePoint(toon, parent = battle)
    if dmg > 0:
        lerpInterval = LerpPosInterval(eye, moveDuration, toonFace)
    else:
        lerpInterval = LerpPosInterval(eye, moveDuration, Point3(toonFace.getX(), toonFace.getY() - 5, toonFace.getZ() - 2))
    eyeMoveTrack = lerpInterval
    eyeRollTrack = LerpHprInterval(eye, moveDuration, Point3(0, 0, -180))
    eyePropTrack = Sequence(eyeAppearTrack, Parallel(eyeMoveTrack, eyeRollTrack), Func(battle.movie.clearRenderProp, eye), Func(MovieUtil.removeProp, eye))
    damageAnims = [
        [
            'duck',
            0.01,
            0.01,
            1.3999999999999999],
        [
            'cringe',
            0.01,
            0.29999999999999999]]
    toonTrack = getToonTrack(attack, splicedDamageAnims = damageAnims, damageDelay = damageDelay, dodgeDelay = dodgeDelay, dodgeAnimNames = [
        'duck'], showDamageExtraTime = 1.7, showMissedExtraTime = 1.7)
    soundTrack = getSoundTrack('SA_evil_eye.mp3', delay = 1.3, node = suit)
    return Parallel(suitTrack, toonTrack, eyePropTrack, soundTrack)


def doPlayHardball(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    ball = globalPropPool.getProp('baseball')
    suitType = getSuitBodyType(attack['suitName'])
    if suitType == 'a':
        suitDelay = 1.0900000000000001
        damageDelay = 2.7599999999999998
        dodgeDelay = 1.8600000000000001
    elif suitType == 'b':
        suitDelay = 1.79
        damageDelay = 3.46
        dodgeDelay = 2.5600000000000001
    elif suitType == 'c':
        suitDelay = 1.0900000000000001
        damageDelay = 2.7599999999999998
        dodgeDelay = 1.8600000000000001
    
    suitTrack = getSuitTrack(attack)
    ballPosPoints = [
        Point3(0.040000000000000001, 0.029999999999999999, -0.31),
        VBase3(-1.1519999999999999, 86.581000000000003, -76.784000000000006)]
    propTrack = Sequence(getPropAppearTrack(ball, suit.getRightHand(), ballPosPoints, 0.80000000000000004, Point3(5, 5, 5), scaleUpTime = 0.5))
    propTrack.append(Wait(suitDelay))
    propTrack.append(Func(battle.movie.needRestoreRenderProp, ball))
    propTrack.append(Func(ball.wrtReparentTo, battle))
    toonPos = toon.getPos(battle)
    x = toonPos.getX()
    y = toonPos.getY()
    z = toonPos.getZ()
    z = z + 0.20000000000000001
    if dmg > 0:
        propTrack.append(LerpPosInterval(ball, 0.5, __toonFacePoint(toon, parent = battle)))
        propTrack.append(LerpPosInterval(ball, 0.5, Point3(x, y + 3, z)))
        propTrack.append(LerpPosInterval(ball, 0.40000000000000002, Point3(x, y + 5, z + 2)))
        propTrack.append(LerpPosInterval(ball, 0.29999999999999999, Point3(x, y + 6, z)))
        propTrack.append(LerpPosInterval(ball, 0.10000000000000001, Point3(x, y + 7, z + 1)))
        propTrack.append(LerpPosInterval(ball, 0.10000000000000001, Point3(x, y + 8, z)))
        propTrack.append(LerpPosInterval(ball, 0.10000000000000001, Point3(x, y + 8.5, z + 0.59999999999999998)))
        propTrack.append(LerpPosInterval(ball, 0.10000000000000001, Point3(x, y + 9, z + 0.20000000000000001)))
        propTrack.append(Wait(0.40000000000000002))
        soundTrack = getSoundTrack('SA_hardball_impact_only.mp3', delay = 2.7999999999999998, node = suit)
    else:
        propTrack.append(LerpPosInterval(ball, 0.5, Point3(x, y + 2, z)))
        propTrack.append(LerpPosInterval(ball, 0.40000000000000002, Point3(x, y - 1, z + 2)))
        propTrack.append(LerpPosInterval(ball, 0.29999999999999999, Point3(x, y - 3, z)))
        propTrack.append(LerpPosInterval(ball, 0.10000000000000001, Point3(x, y - 4, z + 1)))
        propTrack.append(LerpPosInterval(ball, 0.10000000000000001, Point3(x, y - 5, z)))
        propTrack.append(LerpPosInterval(ball, 0.10000000000000001, Point3(x, y - 5.5, z + 0.59999999999999998)))
        propTrack.append(LerpPosInterval(ball, 0.10000000000000001, Point3(x, y - 6, z + 0.20000000000000001)))
        propTrack.append(Wait(0.40000000000000002))
        soundTrack = getSoundTrack('SA_hardball.mp3', delay = 3.1000000000000001, node = suit)
    propTrack.append(LerpScaleInterval(ball, 0.29999999999999999, MovieUtil.PNT3_NEARZERO))
    propTrack.append(Func(MovieUtil.removeProp, ball))
    propTrack.append(Func(battle.movie.clearRenderProp, ball))
    damageAnims = [
        [
            'conked',
            damageDelay,
            0.01,
            0.5],
        [
            'slip-backward',
            0.01,
            0.69999999999999996]]
    toonTrack = getToonTrack(attack, splicedDamageAnims = damageAnims, dodgeDelay = dodgeDelay, dodgeAnimNames = [
        'sidestep'], showDamageExtraTime = 3.8999999999999999)
    return Parallel(suitTrack, toonTrack, propTrack, soundTrack)


def doPowerTie(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    tie = globalPropPool.getProp('power-tie')
    suitType = getSuitBodyType(attack['suitName'])
    if suitType == 'a':
        throwDelay = 2.1699999999999999
        damageDelay = 3.2999999999999998
        dodgeDelay = 3.1000000000000001
    elif suitType == 'b':
        throwDelay = 2.1699999999999999
        damageDelay = 3.2999999999999998
        dodgeDelay = 3.1000000000000001
    elif suitType == 'c':
        throwDelay = 1.45
        damageDelay = 2.6099999999999999
        dodgeDelay = 2.3399999999999999
    
    suitTrack = getSuitTrack(attack)
    posPoints = [
        Point3(1.1599999999999999, 0.23999999999999999, 0.63),
        VBase3(171.56100000000001, 1.7450000000000001, -163.44300000000001)]
    tiePropTrack = Sequence(getPropAppearTrack(tie, suit.getRightHand(), posPoints, 0.5, Point3(3.5, 3.5, 3.5), scaleUpTime = 0.5))
    tiePropTrack.append(Wait(throwDelay))
    tiePropTrack.append(Func(tie.setBillboardPointEye))
    tiePropTrack.append(getPropThrowTrack(attack, tie, [
        __toonFacePoint(toon)], [
        __toonGroundPoint(attack, toon, 0.10000000000000001)], hitDuration = 0.40000000000000002, missDuration = 0.80000000000000004))
    toonTrack = getToonTrack(attack, damageDelay, [
        'conked'], dodgeDelay, [
        'sidestep'])
    throwSound = getSoundTrack('SA_powertie_throw.mp3', delay = 2.2999999999999998, node = suit)
    if dmg > 0:
        hitSound = getSoundTrack('SA_powertie_impact.mp3', delay = 2.8999999999999999, node = suit)
        return Parallel(suitTrack, toonTrack, tiePropTrack, throwSound, hitSound)
    else:
        return Parallel(suitTrack, toonTrack, tiePropTrack, throwSound)


def doDoubleTalk(attack):
    suit = attack['suit']
    battle = attack['battle']
    BattleParticles.loadParticles()
    particleEffect = BattleParticles.createParticleEffect('DoubleTalkLeft')
    particleEffect2 = BattleParticles.createParticleEffect('DoubleTalkRight')
    BattleParticles.setEffectTexture(particleEffect, 'doubletalk-double', color = Vec4(0, 1.0, 0.0, 1))
    BattleParticles.setEffectTexture(particleEffect2, 'doubletalk-good', color = Vec4(0, 1.0, 0.0, 1))
    suitType = getSuitBodyType(attack['suitName'])
    if suitType == 'a':
        partDelay = 3.2999999999999998
        damageDelay = 3.5
        dodgeDelay = 3.2999999999999998
    elif suitType == 'b':
        partDelay = 3.2999999999999998
        damageDelay = 3.5
        dodgeDelay = 3.2999999999999998
    elif suitType == 'c':
        partDelay = 3.2999999999999998
        damageDelay = 3.5
        dodgeDelay = 3.2999999999999998
    
    suitTrack = getSuitTrack(attack)
    partTrack = getPartTrack(particleEffect, partDelay, 1.8, [
        particleEffect,
        suit,
        0])
    partTrack2 = getPartTrack(particleEffect2, partDelay, 1.8, [
        particleEffect2,
        suit,
        0])
    damageAnims = [
        [
            'duck',
            0.01,
            0.40000000000000002,
            1.05],
        [
            'cringe',
            9.9999999999999995e-007,
            0.80000000000000004]]
    toonTrack = getToonTrack(attack, damageDelay = damageDelay, splicedDamageAnims = damageAnims, dodgeDelay = dodgeDelay, splicedDodgeAnims = [
        [
            'duck',
            0.01,
            1.3999999999999999]], showMissedExtraTime = 0.90000000000000002, showDamageExtraTime = 0.80000000000000004)
    soundTrack = getSoundTrack('SA_filibuster.mp3', delay = 2.5, node = suit)
    return Parallel(suitTrack, toonTrack, partTrack, partTrack2, soundTrack)


def doFreezeAssets(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    BattleParticles.loadParticles()
    snowEffect = BattleParticles.createParticleEffect('FreezeAssets')
    BattleParticles.setEffectTexture(snowEffect, 'snow-particle')
    cloud = globalPropPool.getProp('stormcloud')
    suitType = getSuitBodyType(attack['suitName'])
    if suitType == 'a':
        partDelay = 0.20000000000000001
        damageDelay = 3.5
        dodgeDelay = 2.2999999999999998
    elif suitType == 'b':
        partDelay = 0.20000000000000001
        damageDelay = 3.5
        dodgeDelay = 2.2999999999999998
    elif suitType == 'c':
        partDelay = 0.20000000000000001
        damageDelay = 3.5
        dodgeDelay = 2.2999999999999998
    
    suitTrack = getSuitTrack(attack, delay = 0.90000000000000002)
    initialCloudHeight = suit.height + 3
    cloudPosPoints = [
        Point3(0, 3, initialCloudHeight),
        MovieUtil.PNT3_ZERO]
    cloudPropTrack = Sequence()
    cloudPropTrack.append(Func(cloud.pose, 'stormcloud', 0))
    cloudPropTrack.append(getPropAppearTrack(cloud, suit, cloudPosPoints, 9.9999999999999995e-007, Point3(3, 3, 3), scaleUpTime = 0.69999999999999996))
    cloudPropTrack.append(Func(battle.movie.needRestoreRenderProp, cloud))
    cloudPropTrack.append(Func(cloud.wrtReparentTo, render))
    targetPoint = __toonFacePoint(toon)
    targetPoint.setZ(targetPoint[2] + 3)
    cloudPropTrack.append(Wait(1.1000000000000001))
    cloudPropTrack.append(LerpPosInterval(cloud, 1, pos = targetPoint))
    cloudPropTrack.append(Wait(partDelay))
    cloudPropTrack.append(ParticleInterval(snowEffect, cloud, worldRelative = 0, duration = 2.1000000000000001))
    cloudPropTrack.append(Wait(0.40000000000000002))
    cloudPropTrack.append(LerpScaleInterval(cloud, 0.5, MovieUtil.PNT3_NEARZERO))
    cloudPropTrack.append(Func(MovieUtil.removeProp, cloud))
    cloudPropTrack.append(Func(battle.movie.clearRenderProp, cloud))
    damageAnims = [
        [
            'cringe',
            0.01,
            0.40000000000000002,
            0.80000000000000004],
        [
            'duck',
            0.01,
            1.6000000000000001]]
    toonTrack = getToonTrack(attack, damageDelay = damageDelay, splicedDamageAnims = damageAnims, dodgeDelay = dodgeDelay, dodgeAnimNames = [
        'sidestep'], showMissedExtraTime = 1.2)
    return Parallel(suitTrack, toonTrack, cloudPropTrack)


def doHotAir(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    BattleParticles.loadParticles()
    sprayEffect = BattleParticles.createParticleEffect('HotAir')
    baseFlameEffect = BattleParticles.createParticleEffect(file = 'firedBaseFlame')
    flameEffect = BattleParticles.createParticleEffect('FiredFlame')
    flecksEffect = BattleParticles.createParticleEffect('SpriteFiredFlecks')
    BattleParticles.setEffectTexture(sprayEffect, 'fire')
    BattleParticles.setEffectTexture(baseFlameEffect, 'fire')
    BattleParticles.setEffectTexture(flameEffect, 'fire')
    BattleParticles.setEffectTexture(flecksEffect, 'roll-o-dex', color = Vec4(200, 200, 200, 1))
    sprayDelay = 1.3
    flameDelay = 3.2000000000000002
    flameDuration = 2.6000000000000001
    flecksDelay = flameDelay + 0.80000000000000004
    flecksDuration = flameDuration - 0.80000000000000004
    damageDelay = 3.6000000000000001
    dodgeDelay = 2.0
    suitTrack = getSuitTrack(attack)
    sprayTrack = getPartTrack(sprayEffect, sprayDelay, 2.2999999999999998, [
        sprayEffect,
        suit,
        0])
    baseFlameTrack = getPartTrack(baseFlameEffect, flameDelay, flameDuration, [
        baseFlameEffect,
        toon,
        0])
    flameTrack = getPartTrack(flameEffect, flameDelay, flameDuration, [
        flameEffect,
        toon,
        0])
    flecksTrack = getPartTrack(flecksEffect, flecksDelay, flecksDuration, [
        flecksEffect,
        toon,
        0])
    
    def changeColor(parts):
        track = Parallel()
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            track.append(Func(nextPart.setColorScale, Vec4(0, 0, 0, 1)))
        
        return track

    
    def resetColor(parts):
        track = Parallel()
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            track.append(Func(nextPart.clearColorScale))
        
        return track

    if dmg > 0:
        headParts = toon.getHeadParts()
        torsoParts = toon.getTorsoParts()
        legsParts = toon.getLegsParts()
        colorTrack = Sequence()
        colorTrack.append(Wait(4.0))
        colorTrack.append(Func(battle.movie.needRestoreColor))
        colorTrack.append(changeColor(headParts))
        colorTrack.append(changeColor(torsoParts))
        colorTrack.append(changeColor(legsParts))
        colorTrack.append(Wait(3.5))
        colorTrack.append(resetColor(headParts))
        colorTrack.append(resetColor(torsoParts))
        colorTrack.append(resetColor(legsParts))
        colorTrack.append(Func(battle.movie.clearRestoreColor))
    
    damageAnims = []
    damageAnims.append([
        'cringe',
        0.01,
        0.69999999999999996,
        0.62])
    damageAnims.append([
        'slip-forward',
        0.01,
        0.40000000000000002,
        1.2])
    damageAnims.append([
        'slip-forward',
        0.01,
        1.0])
    toonTrack = getToonTrack(attack, damageDelay = damageDelay, splicedDamageAnims = damageAnims, dodgeDelay = dodgeDelay, dodgeAnimNames = [
        'sidestep'])
    soundTrack = getSoundTrack('SA_hot_air.mp3', delay = 1.6000000000000001, node = suit)
    if dmg > 0:
        return Parallel(suitTrack, toonTrack, sprayTrack, soundTrack, baseFlameTrack, flameTrack, flecksTrack, colorTrack)
    else:
        return Parallel(suitTrack, toonTrack, sprayTrack, soundTrack)


def doPickPocket(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    dmg = target['hp']
    bill = globalPropPool.getProp('1dollar')
    suitTrack = getSuitTrack(attack)
    billPosPoints = [
        Point3(-0.01, 0.45000000000000001, -0.25),
        VBase3(136.42400000000001, -46.433999999999997, -129.71199999999999)]
    billPropTrack = getPropTrack(bill, suit.getRightHand(), billPosPoints, 0.59999999999999998, 0.55000000000000004, scaleUpPoint = Point3(1.4099999999999999, 1.4099999999999999, 1.4099999999999999))
    toonTrack = getToonTrack(attack, 0.59999999999999998, [
        'cringe'], 0.01, [
        'sidestep'])
    multiTrackList = Parallel(suitTrack, toonTrack)
    if dmg > 0:
        soundTrack = getSoundTrack('SA_pick_pocket.mp3', delay = 0.20000000000000001, node = suit)
        multiTrackList.append(billPropTrack)
        multiTrackList.append(soundTrack)
    
    return multiTrackList


def doFilibuster(attack):
    suit = attack['suit']
    target = attack['target']
    dmg = target['hp']
    battle = attack['battle']
    BattleParticles.loadParticles()
    sprayEffect = BattleParticles.createParticleEffect(file = 'filibusterSpray')
    sprayEffect2 = BattleParticles.createParticleEffect(file = 'filibusterSpray')
    sprayEffect3 = BattleParticles.createParticleEffect(file = 'filibusterSpray')
    sprayEffect4 = BattleParticles.createParticleEffect(file = 'filibusterSpray')
    color = Vec4(0.40000000000000002, 0, 0, 1)
    BattleParticles.setEffectTexture(sprayEffect, 'filibuster-cut', color = color)
    BattleParticles.setEffectTexture(sprayEffect2, 'filibuster-fiscal', color = color)
    BattleParticles.setEffectTexture(sprayEffect3, 'filibuster-impeach', color = color)
    BattleParticles.setEffectTexture(sprayEffect4, 'filibuster-inc', color = color)
    partDelay = 1.3
    partDuration = 1.1499999999999999
    damageDelay = 2.4500000000000002
    dodgeDelay = 1.7
    suitTrack = getSuitTrack(attack)
    sprayTrack = getPartTrack(sprayEffect, partDelay, partDuration, [
        sprayEffect,
        suit,
        0])
    sprayTrack2 = getPartTrack(sprayEffect2, partDelay + 0.80000000000000004, partDuration, [
        sprayEffect2,
        suit,
        0])
    sprayTrack3 = getPartTrack(sprayEffect3, partDelay + 1.6000000000000001, partDuration, [
        sprayEffect3,
        suit,
        0])
    sprayTrack4 = getPartTrack(sprayEffect4, partDelay + 2.3999999999999999, partDuration, [
        sprayEffect4,
        suit,
        0])
    damageAnims = []
    for i in range(0, 4):
        damageAnims.append([
            'cringe',
            1.0000000000000001e-005,
            0.29999999999999999,
            0.80000000000000004])
    
    toonTrack = getToonTrack(attack, damageDelay = damageDelay, splicedDamageAnims = damageAnims, dodgeDelay = dodgeDelay, dodgeAnimNames = [
        'sidestep'])
    soundTrack = getSoundTrack('SA_filibuster.mp3', delay = 1.1000000000000001, node = suit)
    if dmg > 0:
        return Parallel(suitTrack, toonTrack, soundTrack, sprayTrack, sprayTrack2, sprayTrack3, sprayTrack4)
    else:
        return Parallel(suitTrack, toonTrack, soundTrack, sprayTrack, sprayTrack2, sprayTrack3)


def doSchmooze(attack):
    suit = attack['suit']
    battle = attack['battle']
    BattleParticles.loadParticles()
    upperEffects = []
    lowerEffects = []
    textureNames = [
        'schmooze-genius',
        'schmooze-instant',
        'schmooze-master',
        'schmooze-viz']
    for i in range(0, 4):
        upperEffect = BattleParticles.createParticleEffect(file = 'schmoozeUpperSpray')
        lowerEffect = BattleParticles.createParticleEffect(file = 'schmoozeLowerSpray')
        BattleParticles.setEffectTexture(upperEffect, textureNames[i], color = Vec4(0, 0, 1, 1))
        BattleParticles.setEffectTexture(lowerEffect, textureNames[i], color = Vec4(0, 0, 1, 1))
        upperEffects.append(upperEffect)
        lowerEffects.append(lowerEffect)
    
    suitType = getSuitBodyType(attack['suitName'])
    if suitType == 'a':
        partDelay = 1.3
        damageDelay = 1.8
        dodgeDelay = 1.1000000000000001
    elif suitType == 'b':
        partDelay = 1.3
        damageDelay = 2.5
        dodgeDelay = 1.8
    elif suitType == 'c':
        partDelay = 1.3
        damageDelay = partDelay + 1.3999999999999999
        dodgeDelay = 0.90000000000000002
    
    suitTrack = getSuitTrack(attack)
    upperPartTracks = Parallel()
    lowerPartTracks = Parallel()
    for i in range(0, 4):
        upperPartTracks.append(getPartTrack(upperEffects[i], partDelay + i * 0.65000000000000002, 0.80000000000000004, [
            upperEffects[i],
            suit,
            0]))
        lowerPartTracks.append(getPartTrack(lowerEffects[i], partDelay + i * 0.65000000000000002 + 0.69999999999999996, 1.0, [
            lowerEffects[i],
            suit,
            0]))
    
    damageAnims = []
    for i in range(0, 3):
        damageAnims.append([
            'conked',
            0.01,
            0.29999999999999999,
            0.70999999999999996])
    
    damageAnims.append([
        'conked',
        0.01,
        0.29999999999999999])
    dodgeAnims = []
    dodgeAnims.append([
        'duck',
        0.01,
        0.20000000000000001,
        2.7000000000000002])
    dodgeAnims.append([
        'duck',
        0.01,
        1.22,
        1.28])
    dodgeAnims.append([
        'duck',
        0.01,
        3.1600000000000001])
    toonTrack = getToonTrack(attack, damageDelay = damageDelay, splicedDamageAnims = damageAnims, dodgeDelay = dodgeDelay, splicedDodgeAnims = dodgeAnims, showMissedExtraTime = 1.8999999999999999, showDamageExtraTime = 1.1000000000000001)
    return Parallel(suitTrack, toonTrack, upperPartTracks, lowerPartTracks)


def doQuake(attack):
    suit = attack['suit']
    suitTrack = getSuitAnimTrack(attack)
    damageAnims = [
        [
            'slip-forward'],
        [
            'slip-forward',
            0.01]]
    dodgeAnims = [
        [
            'jump'],
        [
            'jump',
            0.01],
        [
            'jump',
            0.01]]
    toonTracks = getToonTracks(attack, damageDelay = 1.8, splicedDamageAnims = damageAnims, dodgeDelay = 1.1000000000000001, splicedDodgeAnims = dodgeAnims, showMissedExtraTime = 2.7999999999999998, showDamageExtraTime = 1.1000000000000001)
    return Parallel(suitTrack, toonTracks)


def doShake(attack):
    suit = attack['suit']
    suitTrack = getSuitAnimTrack(attack)
    damageAnims = [
        [
            'slip-forward'],
        [
            'slip-forward',
            0.01]]
    dodgeAnims = [
        [
            'jump'],
        [
            'jump',
            0.01]]
    toonTracks = getToonTracks(attack, damageDelay = 1.1000000000000001, splicedDamageAnims = damageAnims, dodgeDelay = 0.69999999999999996, splicedDodgeAnims = dodgeAnims, showMissedExtraTime = 2.7999999999999998, showDamageExtraTime = 1.1000000000000001)
    return Parallel(suitTrack, toonTracks)


def doTremor(attack):
    suit = attack['suit']
    suitTrack = getSuitAnimTrack(attack)
    damageAnims = [
        [
            'slip-forward'],
        [
            'slip-forward',
            0.01]]
    dodgeAnims = [
        [
            'jump'],
        [
            'jump',
            0.01]]
    toonTracks = getToonTracks(attack, damageDelay = 1.1000000000000001, splicedDamageAnims = damageAnims, dodgeDelay = 0.69999999999999996, splicedDodgeAnims = dodgeAnims, showMissedExtraTime = 2.7999999999999998, showDamageExtraTime = 1.1000000000000001)
    soundTrack = getSoundTrack('SA_tremor.mp3', delay = 0.90000000000000002, node = suit)
    return Parallel(suitTrack, soundTrack, toonTracks)


def doHangUp(attack):
    suit = attack['suit']
    battle = attack['battle']
    phone = globalPropPool.getProp('phone')
    receiver = globalPropPool.getProp('receiver')
    suitTrack = getSuitTrack(attack)
    suitName = suit.getStyleName()
    if suitName == 'tf':
        phonePosPoints = [
            Point3(-0.23000000000000001, 0.01, -0.26000000000000001),
            VBase3(5.9390000000000001, 2.7629999999999999, -177.59100000000001)]
        receiverPosPoints = [
            Point3(-0.13, -0.070000000000000007, -0.059999999999999998),
            VBase3(-1.8540000000000001, 2.4340000000000002, -177.57900000000001)]
        receiverAdjustScale = Point3(0.80000000000000004, 0.80000000000000004, 0.80000000000000004)
        pickupDelay = 0.44
        dialDuration = 3.0699999999999998
        finalPhoneDelay = 0.01
        scaleUpPoint = Point3(0.75, 0.75, 0.75)
    else:
        phonePosPoints = [
            Point3(0.23000000000000001, 0.17000000000000001, -0.11),
            VBase3(5.9390000000000001, 2.7629999999999999, -177.59100000000001)]
        receiverPosPoints = [
            Point3(0.23000000000000001, 0.17000000000000001, -0.11),
            VBase3(5.9390000000000001, 2.7629999999999999, -177.59100000000001)]
        receiverAdjustScale = MovieUtil.PNT3_ONE
        pickupDelay = 0.73999999999999999
        dialDuration = 3.0699999999999998
        finalPhoneDelay = 0.68999999999999995
        scaleUpPoint = MovieUtil.PNT3_ONE
    propTrack = Sequence(Wait(0.29999999999999999), Func(__showProp, phone, suit.getLeftHand(), phonePosPoints[0], phonePosPoints[1]), Func(__showProp, receiver, suit.getLeftHand(), receiverPosPoints[0], receiverPosPoints[1]), LerpScaleInterval(phone, 0.5, scaleUpPoint, MovieUtil.PNT3_NEARZERO), Wait(pickupDelay), Func(receiver.wrtReparentTo, suit.getRightHand()), LerpScaleInterval(receiver, 0.01, receiverAdjustScale), LerpPosHprInterval(receiver, 0.0001, Point3(-0.53000000000000003, 0.20999999999999999, -0.54000000000000004), VBase3(-99.489999999999995, -35.270000000000003, 1.8400000000000001)), Wait(dialDuration), Func(receiver.wrtReparentTo, phone), Wait(finalPhoneDelay), LerpScaleInterval(phone, 0.5, MovieUtil.PNT3_NEARZERO), Func(MovieUtil.removeProps, [
        receiver,
        phone]))
    toonTrack = getToonTrack(attack, 5.5, [
        'slip-backward'], 4.7000000000000002, [
        'jump'])
    soundTrack = getSoundTrack('SA_hangup.mp3', delay = 1.3, node = suit)
    return Parallel(suitTrack, toonTrack, propTrack, soundTrack)


def doRedTape(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    tape = globalPropPool.getProp('redtape')
    tubes = []
    for i in range(0, 3):
        tubes.append(globalPropPool.getProp('redtape-tube'))
    
    suitTrack = getSuitTrack(attack)
    suitName = suit.getStyleName()
    if suitName == 'tf' or suitName == 'nc':
        tapePosPoints = [
            Point3(-0.23999999999999999, 0.089999999999999997, -0.38),
            VBase3(-1.1519999999999999, 86.581000000000003, -76.784000000000006)]
    else:
        tapePosPoints = [
            Point3(0.23999999999999999, 0.089999999999999997, -0.38),
            VBase3(-1.1519999999999999, 86.581000000000003, -76.784000000000006)]
    tapeScaleUpPoint = Point3(0.90000000000000002, 0.90000000000000002, 0.23999999999999999)
    propTrack = Sequence(getPropAppearTrack(tape, suit.getRightHand(), tapePosPoints, 0.80000000000000004, tapeScaleUpPoint, scaleUpTime = 0.5))
    propTrack.append(Wait(1.73))
    
    hitPoint = lambda toon = toon: __toonTorsoPoint(toon)
    propTrack.append(getPropThrowTrack(attack, tape, [
        hitPoint], [
        __toonGroundPoint(attack, toon, 0.69999999999999996)]))
    hips = toon.getHipsParts()
    animal = toon.style.getAnimal()
    scale = ToontownGlobals.toonBodyScales[animal]
    legs = toon.style.legs
    torso = toon.style.torso
    torso = torso[0]
    animal = animal[0]
    tubeHeight = -0.80000000000000004
    if torso == 's':
        scaleUpPoint = Point3(scale * 2.0299999999999998, scale * 2.0299999999999998, scale * 0.79749999999999999)
    elif torso == 'm':
        scaleUpPoint = Point3(scale * 2.0299999999999998, scale * 2.0299999999999998, scale * 0.79749999999999999)
    elif torso == 'l':
        scaleUpPoint = Point3(scale * 2.0299999999999998, scale * 2.0299999999999998, scale * 1.1100000000000001)
    
    if animal == 'h' or animal == 'd':
        tubeHeight = -0.87
        scaleUpPoint = Point3(scale * 1.6899999999999999, scale * 1.6899999999999999, scale * 0.67000000000000004)
    
    tubePosPoints = [
        Point3(0, 0, tubeHeight),
        MovieUtil.PNT3_ZERO]
    tubeTracks = Parallel()
    tubeTracks.append(Func(battle.movie.needRestoreHips))
    for partNum in range(0, hips.getNumPaths()):
        nextPart = hips.getPath(partNum)
        tubeTracks.append(getPropTrack(tubes[partNum], nextPart, tubePosPoints, 3.25, 3.1699999999999999, scaleUpPoint = scaleUpPoint))
    
    tubeTracks.append(Func(battle.movie.clearRestoreHips))
    toonTrack = getToonTrack(attack, 3.3999999999999999, [
        'struggle'], 2.7999999999999998, [
        'jump'])
    soundTrack = getSoundTrack('SA_red_tape.mp3', delay = 2.8999999999999999, node = suit)
    if dmg > 0:
        return Parallel(suitTrack, toonTrack, propTrack, soundTrack, tubeTracks)
    else:
        return Parallel(suitTrack, toonTrack, propTrack, soundTrack)


def doParadigmShift(attack):
    suit = attack['suit']
    battle = attack['battle']
    targets = attack['target']
    hitAtleastOneToon = 0
    for t in targets:
        if t['hp'] > 0:
            hitAtleastOneToon = 1
        
    
    damageDelay = 1.95
    dodgeDelay = 0.94999999999999996
    sprayEffect = BattleParticles.createParticleEffect('ShiftSpray')
    suitName = suit.getStyleName()
    if suitName == 'm':
        sprayEffect.setPos(Point3(-5.2000000000000002, 4.5999999999999996, 2.7000000000000002))
    elif suitName == 'sd':
        sprayEffect.setPos(Point3(-5.2000000000000002, 4.5999999999999996, 2.7000000000000002))
    else:
        sprayEffect.setPos(Point3(0.10000000000000001, 4.5999999999999996, 2.7000000000000002))
    suitTrack = getSuitAnimTrack(attack)
    sprayTrack = getPartTrack(sprayEffect, 1.0, 1.8999999999999999, [
        sprayEffect,
        suit,
        0])
    liftTracks = Parallel()
    toonRiseTracks = Parallel()
    for t in targets:
        toon = t['toon']
        dmg = t['hp']
        if dmg > 0:
            liftEffect = BattleParticles.createParticleEffect('ShiftLift')
            liftEffect.setPos(toon.getPos(battle))
            liftEffect.setZ(liftEffect.getZ() - 1.3)
            liftTracks.append(getPartTrack(liftEffect, 1.1000000000000001, 4.0999999999999996, [
                liftEffect,
                battle,
                0]))
            shadow = toon.dropShadow
            fakeShadow = MovieUtil.copyProp(shadow)
            x = toon.getX()
            y = toon.getY()
            z = toon.getZ()
            height = 3
            groundPoint = Point3(x, y, z)
            risePoint = Point3(x, y, z + height)
            shakeRight = Point3(x, y + 0.69999999999999996, z + height)
            shakeLeft = Point3(x, y - 0.69999999999999996, z + height)
            shakeTrack = Sequence()
            shakeTrack.append(Wait(damageDelay + 0.25))
            shakeTrack.append(Func(shadow.hide))
            shakeTrack.append(LerpPosInterval(toon, 1.1000000000000001, risePoint))
            for i in range(0, 17):
                shakeTrack.append(LerpPosInterval(toon, 0.029999999999999999, shakeLeft))
                shakeTrack.append(LerpPosInterval(toon, 0.029999999999999999, shakeRight))
            
            shakeTrack.append(LerpPosInterval(toon, 0.10000000000000001, risePoint))
            shakeTrack.append(LerpPosInterval(toon, 0.10000000000000001, groundPoint))
            shakeTrack.append(Func(shadow.show))
            shadowTrack = Sequence()
            shadowTrack.append(Func(battle.movie.needRestoreRenderProp, fakeShadow))
            shadowTrack.append(Wait(damageDelay + 0.25))
            shadowTrack.append(Func(fakeShadow.hide))
            shadowTrack.append(Func(fakeShadow.setScale, 0.27000000000000002))
            shadowTrack.append(Func(fakeShadow.reparentTo, toon))
            shadowTrack.append(Func(fakeShadow.setPos, MovieUtil.PNT3_ZERO))
            shadowTrack.append(Func(fakeShadow.wrtReparentTo, battle))
            shadowTrack.append(Func(fakeShadow.show))
            shadowTrack.append(LerpScaleInterval(fakeShadow, 0.40000000000000002, Point3(0.17000000000000001, 0.17000000000000001, 0.17000000000000001)))
            shadowTrack.append(Wait(1.8100000000000001))
            shadowTrack.append(LerpScaleInterval(fakeShadow, 0.10000000000000001, Point3(0.27000000000000002, 0.27000000000000002, 0.27000000000000002)))
            shadowTrack.append(Func(MovieUtil.removeProp, fakeShadow))
            shadowTrack.append(Func(battle.movie.clearRenderProp, fakeShadow))
            toonRiseTracks.append(Parallel(shakeTrack, shadowTrack))
        
    
    damageAnims = []
    damageAnims.extend(getSplicedLerpAnims('think', 0.66000000000000003, 1.8999999999999999, startTime = 2.0600000000000001))
    damageAnims.append([
        'slip-backward',
        0.01,
        0.5])
    dodgeAnims = []
    dodgeAnims.append([
        'jump',
        0.01,
        0,
        0.59999999999999998])
    dodgeAnims.extend(getSplicedLerpAnims('jump', 0.31, 1.0, startTime = 0.59999999999999998))
    dodgeAnims.append([
        'jump',
        0,
        0.91000000000000003])
    toonTracks = getToonTracks(attack, damageDelay = damageDelay, splicedDamageAnims = damageAnims, dodgeDelay = dodgeDelay, splicedDodgeAnims = dodgeAnims, showDamageExtraTime = 2.7000000000000002)
    if hitAtleastOneToon == 1:
        soundTrack = getSoundTrack('SA_paradigm_shift.mp3', delay = 2.1000000000000001, node = suit)
        return Parallel(suitTrack, sprayTrack, soundTrack, liftTracks, toonTracks, toonRiseTracks)
    else:
        return Parallel(suitTrack, sprayTrack, liftTracks, toonTracks, toonRiseTracks)


def doPowerTrip(attack):
    suit = attack['suit']
    battle = attack['battle']
    centerColor = Vec4(0.10000000000000001, 0.10000000000000001, 0.10000000000000001, 0.40000000000000002)
    edgeColor = Vec4(0.40000000000000002, 0.10000000000000001, 0.90000000000000002, 0.69999999999999996)
    powerBar1 = BattleParticles.createParticleEffect(file = 'powertrip')
    powerBar2 = BattleParticles.createParticleEffect(file = 'powertrip2')
    powerBar1.setPos(0, 6.0999999999999996, 0.40000000000000002)
    powerBar1.setHpr(-60, 0, 0)
    powerBar2.setPos(0, 6.0999999999999996, 0.40000000000000002)
    powerBar2.setHpr(60, 0, 0)
    powerBar1Particles = powerBar1.getParticlesNamed('particles-1')
    powerBar2Particles = powerBar2.getParticlesNamed('particles-1')
    powerBar1Particles.renderer.setCenterColor(centerColor)
    powerBar1Particles.renderer.setEdgeColor(edgeColor)
    powerBar2Particles.renderer.setCenterColor(centerColor)
    powerBar2Particles.renderer.setEdgeColor(edgeColor)
    waterfallEffect = BattleParticles.createParticleEffect('Waterfall')
    waterfallEffect.setScale(11)
    waterfallParticles = waterfallEffect.getParticlesNamed('particles-1')
    waterfallParticles.renderer.setCenterColor(centerColor)
    waterfallParticles.renderer.setEdgeColor(edgeColor)
    suitName = suit.getStyleName()
    if suitName == 'mh':
        waterfallEffect.setPos(0, 4, 3.6000000000000001)
    
    suitTrack = getSuitAnimTrack(attack)
    
    def getPowerTrack(effect, suit = suit, battle = battle):
        partTrack = Sequence(Wait(1.0), Func(battle.movie.needRestoreParticleEffect, effect), Func(effect.start, suit), Wait(0.40000000000000002), LerpPosInterval(effect, 1.0, Point3(0, 15, 0.40000000000000002)), LerpFunctionInterval(effect.setAlphaScale, fromData = 1, toData = 0, duration = 0.40000000000000002), Func(effect.cleanup), Func(battle.movie.clearRestoreParticleEffect, effect))
        return partTrack

    partTrack1 = getPowerTrack(powerBar1)
    partTrack2 = getPowerTrack(powerBar2)
    waterfallTrack = getPartTrack(waterfallEffect, 0.59999999999999998, 1.3, [
        waterfallEffect,
        suit,
        0])
    toonTracks = getToonTracks(attack, 1.8, [
        'slip-forward'], 1.29, [
        'jump'])
    return Parallel(suitTrack, partTrack1, partTrack2, waterfallTrack, toonTracks)


def getThrowEndPoint(suit, toon, battle, whichBounce):
    pnt = toon.getPos(toon)
    if whichBounce == 'one':
        pnt.setY(pnt[1] + 8)
    elif whichBounce == 'two':
        pnt.setY(pnt[1] + 5)
    elif whichBounce == 'threeHit':
        pnt.setZ(pnt[2] + toon.shoulderHeight + 0.29999999999999999)
    elif whichBounce == 'threeMiss':
        pass
    elif whichBounce == 'four':
        pnt.setY(pnt[1] - 5)
    
    return Point3(pnt)


def doBounceCheck(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    battle = attack['battle']
    toon = target['toon']
    dmg = target['hp']
    hitSuit = dmg > 0
    check = globalPropPool.getProp('bounced-check')
    checkPosPoints = [
        MovieUtil.PNT3_ZERO,
        VBase3(95.247, 79.025000000000006, 88.849000000000004)]
    
    bounce1Point = lambda suit = suit, toon = toon, battle = battle: getThrowEndPoint(suit, toon, battle, 'one')
    
    bounce2Point = lambda suit = suit, toon = toon, battle = battle: getThrowEndPoint(suit, toon, battle, 'two')
    
    hit3Point = lambda suit = suit, toon = toon, battle = battle: getThrowEndPoint(suit, toon, battle, 'threeHit')
    
    miss3Point = lambda suit = suit, toon = toon, battle = battle: getThrowEndPoint(suit, toon, battle, 'threeMiss')
    
    bounce4Point = lambda suit = suit, toon = toon, battle = battle: getThrowEndPoint(suit, toon, battle, 'four')
    suitType = getSuitBodyType(attack['suitName'])
    if suitType == 'a':
        throwDelay = 2.5
        dodgeDelay = 4.2999999999999998
        damageDelay = 5.0999999999999996
    elif suitType == 'b':
        throwDelay = 1.8
        dodgeDelay = 3.6000000000000001
        damageDelay = 4.4000000000000004
    elif suitType == 'c':
        throwDelay = 1.8
        dodgeDelay = 3.6000000000000001
        damageDelay = 4.4000000000000004
    
    suitTrack = getSuitTrack(attack)
    checkPropTrack = Sequence(getPropAppearTrack(check, suit.getRightHand(), checkPosPoints, 1.0000000000000001e-005, Point3(8.5, 8.5, 8.5), startScale = MovieUtil.PNT3_ONE))
    checkPropTrack.append(Wait(throwDelay))
    checkPropTrack.append(Func(check.wrtReparentTo, toon))
    checkPropTrack.append(Func(check.setHpr, Point3(0, -90, 0)))
    checkPropTrack.append(getThrowTrack(check, bounce1Point, duration = 0.5, parent = toon))
    checkPropTrack.append(getThrowTrack(check, bounce2Point, duration = 0.90000000000000002, parent = toon))
    if hitSuit:
        checkPropTrack.append(getThrowTrack(check, hit3Point, duration = 0.69999999999999996, parent = toon))
    else:
        checkPropTrack.append(getThrowTrack(check, miss3Point, duration = 0.69999999999999996, parent = toon))
        checkPropTrack.append(getThrowTrack(check, bounce4Point, duration = 0.69999999999999996, parent = toon))
        checkPropTrack.append(LerpScaleInterval(check, 0.29999999999999999, MovieUtil.PNT3_NEARZERO))
    checkPropTrack.append(Func(MovieUtil.removeProp, check))
    toonTrack = getToonTrack(attack, damageDelay, [
        'conked'], dodgeDelay, [
        'sidestep'])
    soundTracks = Sequence(getSoundTrack('SA_pink_slip.mp3', delay = throwDelay + 0.5, duration = 0.59999999999999998, node = suit), getSoundTrack('SA_pink_slip.mp3', delay = 0.40000000000000002, duration = 0.59999999999999998, node = suit))
    return Parallel(suitTrack, checkPropTrack, toonTrack, soundTracks)


def doWatercooler(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    watercooler = globalPropPool.getProp('watercooler')
    
    def getCoolerSpout(watercooler = watercooler):
        spout = watercooler.find('**/joint-toSpray')
        return spout.getPos(render)

    
    hitPoint = lambda toon = toon: __toonFacePoint(toon)
    
    missPoint = lambda prop = watercooler, toon = toon: __toonMissPoint(prop, toon, 0, parent = render)
    hitSprayTrack = MovieUtil.getSprayTrack(battle, Point4(0.75, 0.75, 1.0, 0.80000000000000004), getCoolerSpout, hitPoint, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, horizScale = 0.29999999999999999, vertScale = 0.29999999999999999)
    missSprayTrack = MovieUtil.getSprayTrack(battle, Point4(0.75, 0.75, 1.0, 0.80000000000000004), getCoolerSpout, missPoint, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, horizScale = 0.29999999999999999, vertScale = 0.29999999999999999)
    suitTrack = getSuitTrack(attack)
    posPoints = [
        Point3(0.47999999999999998, 0.11, -0.92000000000000004),
        VBase3(20.402999999999999, 33.158000000000001, 69.510999999999996)]
    propTrack = Sequence(Wait(1.01), Func(__showProp, watercooler, suit.getLeftHand(), posPoints[0], posPoints[1]), LerpScaleInterval(watercooler, 0.5, Point3(1.1499999999999999, 1.1499999999999999, 1.1499999999999999)), Wait(1.6000000000000001))
    if dmg > 0:
        propTrack.append(hitSprayTrack)
    else:
        propTrack.append(missSprayTrack)
    propTrack += [
        Wait(0.01),
        LerpScaleInterval(watercooler, 0.5, MovieUtil.PNT3_NEARZERO),
        Func(MovieUtil.removeProp, watercooler)]
    splashTrack = Sequence()
    if dmg > 0:
        
        def prepSplash(splash, targetPoint):
            splash.reparentTo(render)
            splash.setPos(targetPoint)
            scale = splash.getScale()
            splash.setBillboardPointWorld()
            splash.setScale(scale)

        splash = globalPropPool.getProp('splash-from-splat')
        splash.setColor(0.75, 0.75, 1, 0.80000000000000004)
        splash.setScale(0.29999999999999999)
        splashTrack = Sequence(Func(battle.movie.needRestoreRenderProp, splash), Wait(3.2000000000000002), Func(prepSplash, splash, __toonFacePoint(toon)), ActorInterval(splash, 'splash-from-splat'), Func(MovieUtil.removeProp, splash), Func(battle.movie.clearRenderProp, splash))
    
    toonTrack = getToonTrack(attack, suitTrack.getDuration() - 1.5, [
        'cringe'], 2.3999999999999999, [
        'sidestep'])
    soundTrack = Sequence(Wait(1.1000000000000001), SoundInterval(globalBattleSoundCache.getSound('SA_watercooler_appear_only.mp3'), node = suit, duration = 1.4722), Wait(0.40000000000000002), SoundInterval(globalBattleSoundCache.getSound('SA_watercooler_spray_only.mp3'), node = suit, duration = 2.3130000000000002))
    return Parallel(suitTrack, toonTrack, propTrack, soundTrack, splashTrack)


def doFired(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    BattleParticles.loadParticles()
    baseFlameEffect = BattleParticles.createParticleEffect(file = 'firedBaseFlame')
    flameEffect = BattleParticles.createParticleEffect('FiredFlame')
    flecksEffect = BattleParticles.createParticleEffect('SpriteFiredFlecks')
    BattleParticles.setEffectTexture(baseFlameEffect, 'fire')
    BattleParticles.setEffectTexture(flameEffect, 'fire')
    BattleParticles.setEffectTexture(flecksEffect, 'roll-o-dex', color = Vec4(200, 200, 200, 1))
    baseFlameSmall = BattleParticles.createParticleEffect(file = 'firedBaseFlame')
    flameSmall = BattleParticles.createParticleEffect('FiredFlame')
    flecksSmall = BattleParticles.createParticleEffect('SpriteFiredFlecks')
    BattleParticles.setEffectTexture(baseFlameSmall, 'fire')
    BattleParticles.setEffectTexture(flameSmall, 'fire')
    BattleParticles.setEffectTexture(flecksSmall, 'roll-o-dex', color = Vec4(200, 200, 200, 1))
    baseFlameSmall.setScale(0.69999999999999996)
    flameSmall.setScale(0.69999999999999996)
    flecksSmall.setScale(0.69999999999999996)
    suitTrack = getSuitTrack(attack)
    baseFlameTrack = getPartTrack(baseFlameEffect, 1.0, 1.8999999999999999, [
        baseFlameEffect,
        toon,
        0])
    flameTrack = getPartTrack(flameEffect, 1.0, 1.8999999999999999, [
        flameEffect,
        toon,
        0])
    flecksTrack = getPartTrack(flecksEffect, 1.8, 1.1000000000000001, [
        flecksEffect,
        toon,
        0])
    baseFlameSmallTrack = getPartTrack(baseFlameSmall, 1.0, 1.8999999999999999, [
        baseFlameSmall,
        toon,
        0])
    flameSmallTrack = getPartTrack(flameSmall, 1.0, 1.8999999999999999, [
        flameSmall,
        toon,
        0])
    flecksSmallTrack = getPartTrack(flecksSmall, 1.8, 1.1000000000000001, [
        flecksSmall,
        toon,
        0])
    
    def changeColor(parts):
        track = Parallel()
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            track.append(Func(nextPart.setColorScale, Vec4(0, 0, 0, 1)))
        
        return track

    
    def resetColor(parts):
        track = Parallel()
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            track.append(Func(nextPart.clearColorScale))
        
        return track

    if dmg > 0:
        headParts = toon.getHeadParts()
        torsoParts = toon.getTorsoParts()
        legsParts = toon.getLegsParts()
        colorTrack = Sequence()
        colorTrack.append(Wait(2.0))
        colorTrack.append(Func(battle.movie.needRestoreColor))
        colorTrack.append(changeColor(headParts))
        colorTrack.append(changeColor(torsoParts))
        colorTrack.append(changeColor(legsParts))
        colorTrack.append(Wait(3.5))
        colorTrack.append(resetColor(headParts))
        colorTrack.append(resetColor(torsoParts))
        colorTrack.append(resetColor(legsParts))
        colorTrack.append(Func(battle.movie.clearRestoreColor))
    
    damageAnims = []
    damageAnims.append([
        'cringe',
        0.01,
        0.69999999999999996,
        0.62])
    damageAnims.append([
        'slip-forward',
        1.0000000000000001e-005,
        0.40000000000000002,
        1.2])
    damageAnims.extend(getSplicedLerpAnims('slip-forward', 0.31, 0.80000000000000004, startTime = 1.2))
    toonTrack = getToonTrack(attack, damageDelay = 1.5, splicedDamageAnims = damageAnims, dodgeDelay = 0.29999999999999999, dodgeAnimNames = [
        'sidestep'])
    soundTrack = getSoundTrack('SA_hot_air.mp3', delay = 1.0, node = suit)
    if dmg > 0:
        return Parallel(suitTrack, baseFlameTrack, flameTrack, flecksTrack, toonTrack, colorTrack, soundTrack)
    else:
        return Parallel(suitTrack, baseFlameSmallTrack, flameSmallTrack, flecksSmallTrack, toonTrack, soundTrack)


def doAudit(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    calculator = globalPropPool.getProp('calculator')
    BattleParticles.loadParticles()
    particleEffect = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect, 'audit-one', color = Vec4(0, 0, 0, 1))
    particleEffect2 = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect2, 'audit-two', color = Vec4(0, 0, 0, 1))
    particleEffect3 = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect3, 'audit-three', color = Vec4(0, 0, 0, 1))
    particleEffect4 = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect4, 'audit-four', color = Vec4(0, 0, 0, 1))
    particleEffect5 = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect5, 'audit-mult', color = Vec4(0, 0, 0, 1))
    suitTrack = getSuitTrack(attack)
    partTrack = getPartTrack(particleEffect, 2.1000000000000001, 1.8999999999999999, [
        particleEffect,
        suit,
        0])
    partTrack2 = getPartTrack(particleEffect2, 2.2000000000000002, 2.0, [
        particleEffect2,
        suit,
        0])
    partTrack3 = getPartTrack(particleEffect3, 2.2999999999999998, 2.1000000000000001, [
        particleEffect3,
        suit,
        0])
    partTrack4 = getPartTrack(particleEffect4, 2.3999999999999999, 2.2000000000000002, [
        particleEffect4,
        suit,
        0])
    partTrack5 = getPartTrack(particleEffect5, 2.5, 2.2999999999999998, [
        particleEffect5,
        suit,
        0])
    suitName = attack['suitName']
    if suitName == 'nc':
        calcPosPoints = [
            Point3(-0.14999999999999999, 0.37, 0.029999999999999999),
            VBase3(1.3520000000000001, -6.5179999999999998, -6.0449999999999999)]
        calcDuration = 0.76000000000000001
        scaleUpPoint = Point3(1.1000000000000001, 1.8500000000000001, 1.8100000000000001)
    else:
        calcPosPoints = [
            Point3(0.34999999999999998, 0.52000000000000002, 0.029999999999999999),
            VBase3(1.3520000000000001, -6.5179999999999998, -6.0449999999999999)]
        calcDuration = 1.8700000000000001
        scaleUpPoint = Point3(1.0, 1.3700000000000001, 1.3100000000000001)
    calcPropTrack = getPropTrack(calculator, suit.getLeftHand(), calcPosPoints, 9.9999999999999995e-007, calcDuration, scaleUpPoint = scaleUpPoint, anim = 1, propName = 'calculator', animStartTime = 0.5, animDuration = 3.3999999999999999)
    toonTrack = getToonTrack(attack, 3.2000000000000002, [
        'conked'], 0.90000000000000002, [
        'duck'], showMissedExtraTime = 2.2000000000000002)
    soundTrack = getSoundTrack('SA_audit.mp3', delay = 1.8999999999999999, node = suit)
    return Parallel(suitTrack, toonTrack, calcPropTrack, soundTrack, partTrack, partTrack2, partTrack3, partTrack4, partTrack5)


def doCalculate(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    calculator = globalPropPool.getProp('calculator')
    BattleParticles.loadParticles()
    particleEffect = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect, 'audit-one', color = Vec4(0, 0, 0, 1))
    particleEffect2 = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect2, 'audit-plus', color = Vec4(0, 0, 0, 1))
    particleEffect3 = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect3, 'audit-mult', color = Vec4(0, 0, 0, 1))
    particleEffect4 = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect4, 'audit-three', color = Vec4(0, 0, 0, 1))
    particleEffect5 = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect5, 'audit-div', color = Vec4(0, 0, 0, 1))
    suitTrack = getSuitTrack(attack)
    partTrack = getPartTrack(particleEffect, 2.1000000000000001, 1.8999999999999999, [
        particleEffect,
        suit,
        0])
    partTrack2 = getPartTrack(particleEffect2, 2.2000000000000002, 2.0, [
        particleEffect2,
        suit,
        0])
    partTrack3 = getPartTrack(particleEffect3, 2.2999999999999998, 2.1000000000000001, [
        particleEffect3,
        suit,
        0])
    partTrack4 = getPartTrack(particleEffect4, 2.3999999999999999, 2.2000000000000002, [
        particleEffect4,
        suit,
        0])
    partTrack5 = getPartTrack(particleEffect5, 2.5, 2.2999999999999998, [
        particleEffect5,
        suit,
        0])
    suitName = attack['suitName']
    if suitName == 'nc':
        calcPosPoints = [
            Point3(-0.14999999999999999, 0.37, 0.029999999999999999),
            VBase3(1.3520000000000001, -6.5179999999999998, -6.0449999999999999)]
        calcDuration = 0.76000000000000001
        scaleUpPoint = Point3(1.1000000000000001, 1.8500000000000001, 1.8100000000000001)
    else:
        calcPosPoints = [
            Point3(0.34999999999999998, 0.52000000000000002, 0.029999999999999999),
            VBase3(1.3520000000000001, -6.5179999999999998, -6.0449999999999999)]
        calcDuration = 1.8700000000000001
        scaleUpPoint = Point3(1.0, 1.3700000000000001, 1.3100000000000001)
    calcPropTrack = getPropTrack(calculator, suit.getLeftHand(), calcPosPoints, 9.9999999999999995e-007, calcDuration, scaleUpPoint = scaleUpPoint, anim = 1, propName = 'calculator', animStartTime = 0.5, animDuration = 3.3999999999999999)
    toonTrack = getToonTrack(attack, 3.2000000000000002, [
        'conked'], 1.8, [
        'sidestep'])
    return Parallel(suitTrack, toonTrack, calcPropTrack, partTrack, partTrack2, partTrack3, partTrack4, partTrack5)


def doTabulate(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    calculator = globalPropPool.getProp('calculator')
    BattleParticles.loadParticles()
    particleEffect = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect, 'audit-plus', color = Vec4(0, 0, 0, 1))
    particleEffect2 = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect2, 'audit-minus', color = Vec4(0, 0, 0, 1))
    particleEffect3 = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect3, 'audit-mult', color = Vec4(0, 0, 0, 1))
    particleEffect4 = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect4, 'audit-div', color = Vec4(0, 0, 0, 1))
    particleEffect5 = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect5, 'audit-one', color = Vec4(0, 0, 0, 1))
    suitTrack = getSuitTrack(attack)
    partTrack = getPartTrack(particleEffect, 2.1000000000000001, 1.8999999999999999, [
        particleEffect,
        suit,
        0])
    partTrack2 = getPartTrack(particleEffect2, 2.2000000000000002, 2.0, [
        particleEffect2,
        suit,
        0])
    partTrack3 = getPartTrack(particleEffect3, 2.2999999999999998, 2.1000000000000001, [
        particleEffect3,
        suit,
        0])
    partTrack4 = getPartTrack(particleEffect4, 2.3999999999999999, 2.2000000000000002, [
        particleEffect4,
        suit,
        0])
    partTrack5 = getPartTrack(particleEffect5, 2.5, 2.2999999999999998, [
        particleEffect5,
        suit,
        0])
    suitName = attack['suitName']
    if suitName == 'nc':
        calcPosPoints = [
            Point3(-0.14999999999999999, 0.37, 0.029999999999999999),
            VBase3(1.3520000000000001, -6.5179999999999998, -6.0449999999999999)]
        calcDuration = 0.76000000000000001
        scaleUpPoint = Point3(1.1000000000000001, 1.8500000000000001, 1.8100000000000001)
    else:
        calcPosPoints = [
            Point3(0.34999999999999998, 0.52000000000000002, 0.029999999999999999),
            VBase3(1.3520000000000001, -6.5179999999999998, -6.0449999999999999)]
        calcDuration = 1.8700000000000001
        scaleUpPoint = Point3(1.0, 1.3700000000000001, 1.3100000000000001)
    calcPropTrack = getPropTrack(calculator, suit.getLeftHand(), calcPosPoints, 9.9999999999999995e-007, calcDuration, scaleUpPoint = scaleUpPoint, anim = 1, propName = 'calculator', animStartTime = 0.5, animDuration = 3.3999999999999999)
    toonTrack = getToonTrack(attack, 3.2000000000000002, [
        'conked'], 1.8, [
        'sidestep'])
    return Parallel(suitTrack, toonTrack, calcPropTrack, partTrack, partTrack2, partTrack3, partTrack4, partTrack5)


def doCrunch(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    throwDuration = 3.0299999999999998
    suitTrack = getSuitTrack(attack)
    numberNames = [
        'one',
        'two',
        'three',
        'four',
        'five',
        'six']
    BattleParticles.loadParticles()
    numberSpill1 = BattleParticles.createParticleEffect(file = 'numberSpill')
    numberSpill2 = BattleParticles.createParticleEffect(file = 'numberSpill')
    spillTexture1 = whrandom.choice(numberNames)
    spillTexture2 = whrandom.choice(numberNames)
    BattleParticles.setEffectTexture(numberSpill1, 'audit-' + spillTexture1)
    BattleParticles.setEffectTexture(numberSpill2, 'audit-' + spillTexture2)
    numberSpillTrack1 = getPartTrack(numberSpill1, 1.1000000000000001, 2.2000000000000002, [
        numberSpill1,
        suit,
        0])
    numberSpillTrack2 = getPartTrack(numberSpill2, 1.5, 1.0, [
        numberSpill2,
        suit,
        0])
    numberSprayTracks = Parallel()
    numOfNumbers = whrandom.randint(5, 9)
    for i in range(0, numOfNumbers - 1):
        nextSpray = BattleParticles.createParticleEffect(file = 'numberSpray')
        nextTexture = whrandom.choice(numberNames)
        BattleParticles.setEffectTexture(nextSpray, 'audit-' + nextTexture)
        nextStartTime = whrandom.random() * 0.59999999999999998 + throwDuration
        nextDuration = whrandom.random() * 0.40000000000000002 + 1.3999999999999999
        nextSprayTrack = getPartTrack(nextSpray, nextStartTime, nextDuration, [
            nextSpray,
            suit,
            0])
        numberSprayTracks.append(nextSprayTrack)
    
    numberTracks = Parallel()
    for i in range(0, numOfNumbers):
        texture = whrandom.choice(numberNames)
        next = MovieUtil.copyProp(BattleParticles.getParticle('audit-' + texture))
        next.reparentTo(suit.getRightHand())
        next.setScale(0.01, 0.01, 0.01)
        next.setColor(Vec4(0.0, 0.0, 0.0, 1.0))
        next.setPos(whrandom.random() * 0.59999999999999998 - 0.29999999999999999, whrandom.random() * 0.59999999999999998 - 0.29999999999999999, whrandom.random() * 0.59999999999999998 - 0.29999999999999999)
        next.setHpr(VBase3(-1.1499999999999999, 86.579999999999998, -76.780000000000001))
        numberTrack = Sequence(Wait(0.90000000000000002), LerpScaleInterval(next, 0.59999999999999998, MovieUtil.PNT3_ONE), Wait(1.7), Func(MovieUtil.removeProp, next))
        numberTracks.append(numberTrack)
    
    damageAnims = []
    damageAnims.append([
        'cringe',
        0.01,
        0.14000000000000001,
        0.28000000000000003])
    damageAnims.append([
        'cringe',
        0.01,
        0.16,
        0.29999999999999999])
    damageAnims.append([
        'cringe',
        0.01,
        0.13,
        0.22])
    damageAnims.append([
        'slip-forward',
        0.01,
        0.59999999999999998])
    toonTrack = getToonTrack(attack, damageDelay = 4.7000000000000002, splicedDamageAnims = damageAnims, dodgeDelay = 3.6000000000000001, dodgeAnimNames = [
        'sidestep'])
    return Parallel(suitTrack, toonTrack, numberSpillTrack1, numberSpillTrack2, numberTracks, numberSprayTracks)


def doLiquidate(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    dmg = target['hp']
    toon = target['toon']
    BattleParticles.loadParticles()
    rainEffect = BattleParticles.createParticleEffect(file = 'liquidate')
    rainEffect2 = BattleParticles.createParticleEffect(file = 'liquidate')
    rainEffect3 = BattleParticles.createParticleEffect(file = 'liquidate')
    cloud = globalPropPool.getProp('stormcloud')
    suitType = getSuitBodyType(attack['suitName'])
    if suitType == 'a':
        partDelay = 0.20000000000000001
        damageDelay = 3.5
        dodgeDelay = 2.4500000000000002
    elif suitType == 'b':
        partDelay = 0.20000000000000001
        damageDelay = 3.5
        dodgeDelay = 2.4500000000000002
    elif suitType == 'c':
        partDelay = 0.20000000000000001
        damageDelay = 3.5
        dodgeDelay = 2.4500000000000002
    
    suitTrack = getSuitTrack(attack, delay = 0.90000000000000002)
    initialCloudHeight = suit.height + 3
    cloudPosPoints = [
        Point3(0, 3, initialCloudHeight),
        VBase3(180, 0, 0)]
    cloudPropTrack = Sequence()
    cloudPropTrack.append(Func(cloud.pose, 'stormcloud', 0))
    cloudPropTrack.append(getPropAppearTrack(cloud, suit, cloudPosPoints, 9.9999999999999995e-007, Point3(3, 3, 3), scaleUpTime = 0.69999999999999996))
    cloudPropTrack.append(Func(battle.movie.needRestoreRenderProp, cloud))
    cloudPropTrack.append(Func(cloud.wrtReparentTo, render))
    targetPoint = __toonFacePoint(toon)
    targetPoint.setZ(targetPoint[2] + 3)
    cloudPropTrack.append(Wait(1.1000000000000001))
    cloudPropTrack.append(LerpPosInterval(cloud, 1, pos = targetPoint))
    cloudPropTrack.append(Wait(partDelay))
    cloudPropTrack.append(Parallel(Sequence(ParticleInterval(rainEffect, cloud, worldRelative = 0, duration = 2.1000000000000001)), Sequence(Wait(0.10000000000000001), ParticleInterval(rainEffect2, cloud, worldRelative = 0, duration = 2.0)), Sequence(Wait(0.10000000000000001), ParticleInterval(rainEffect3, cloud, worldRelative = 0, duration = 2.0)), Sequence(ActorInterval(cloud, 'stormcloud', startTime = 3, duration = 0.10000000000000001), ActorInterval(cloud, 'stormcloud', startTime = 1, duration = 2.2999999999999998))))
    cloudPropTrack.append(Wait(0.40000000000000002))
    cloudPropTrack.append(LerpScaleInterval(cloud, 0.5, MovieUtil.PNT3_NEARZERO))
    cloudPropTrack.append(Func(MovieUtil.removeProp, cloud))
    cloudPropTrack.append(Func(battle.movie.clearRenderProp, cloud))
    damageAnims = [
        [
            'melt'],
        [
            'jump',
            1.5,
            0.40000000000000002]]
    toonTrack = getToonTrack(attack, damageDelay = damageDelay, splicedDamageAnims = damageAnims, dodgeDelay = dodgeDelay, dodgeAnimNames = [
        'sidestep'])
    soundTrack = getSoundTrack('SA_liquidate.mp3', delay = 2.0, node = suit)
    if dmg > 0:
        puddle = globalPropPool.getProp('quicksand')
        puddle.setColor(Vec4(0.0, 0.0, 1.0, 1))
        puddle.setHpr(Point3(120, 0, 0))
        puddle.setScale(0.01)
        puddleTrack = Sequence(Func(battle.movie.needRestoreRenderProp, puddle), Wait(damageDelay - 0.69999999999999996), Func(puddle.reparentTo, battle), Func(puddle.setPos, toon.getPos(battle)), LerpScaleInterval(puddle, 1.7, Point3(1.7, 1.7, 1.7), startScale = MovieUtil.PNT3_NEARZERO), Wait(3.2000000000000002), LerpFunctionInterval(puddle.setAlphaScale, fromData = 1, toData = 0, duration = 0.80000000000000004), Func(MovieUtil.removeProp, puddle), Func(battle.movie.clearRenderProp, puddle))
        return Parallel(suitTrack, toonTrack, cloudPropTrack, soundTrack, puddleTrack)
    else:
        return Parallel(suitTrack, toonTrack, cloudPropTrack, soundTrack)


def doMarketCrash(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    suitDelay = 1.3200000000000001
    propDelay = 0.59999999999999998
    throwDuration = 1.5
    paper = globalPropPool.getProp('newspaper')
    suitTrack = getSuitTrack(attack)
    posPoints = [
        Point3(-0.070000000000000007, 0.17000000000000001, -0.13),
        VBase3(161.86699999999999, -33.149000000000001, -48.085999999999999)]
    paperTrack = Sequence(getPropAppearTrack(paper, suit.getRightHand(), posPoints, propDelay, Point3(3, 3, 3), scaleUpTime = 0.5))
    paperTrack.append(Wait(suitDelay))
    hitPoint = toon.getPos(battle)
    hitPoint.setX(hitPoint.getX() + 1.2)
    hitPoint.setY(hitPoint.getY() + 1.5)
    if dmg > 0:
        hitPoint.setZ(hitPoint.getZ() + 1.1000000000000001)
    
    movePoint = Point3(hitPoint.getX(), hitPoint.getY() - 1.8, hitPoint.getZ() + 0.20000000000000001)
    paperTrack.append(Func(battle.movie.needRestoreRenderProp, paper))
    paperTrack.append(Func(paper.wrtReparentTo, battle))
    paperTrack.append(getThrowTrack(paper, hitPoint, duration = throwDuration, parent = battle))
    paperTrack.append(Wait(0.59999999999999998))
    paperTrack.append(LerpPosInterval(paper, 0.40000000000000002, movePoint))
    spinTrack = Sequence(Wait(propDelay + suitDelay + 0.20000000000000001), LerpHprInterval(paper, throwDuration, Point3(-360, 0, 0)))
    sizeTrack = Sequence(Wait(propDelay + suitDelay + 0.20000000000000001), LerpScaleInterval(paper, throwDuration, Point3(6, 6, 6)), Wait(0.94999999999999996), LerpScaleInterval(paper, 0.40000000000000002, MovieUtil.PNT3_NEARZERO))
    propTrack = Sequence(Parallel(paperTrack, spinTrack, sizeTrack), Func(MovieUtil.removeProp, paper), Func(battle.movie.clearRenderProp, paper))
    damageAnims = []
    damageAnims.append([
        'cringe',
        0.01,
        0.20999999999999999,
        0.080000000000000002])
    damageAnims.append([
        'slip-forward',
        0.01,
        0.59999999999999998,
        0.84999999999999998])
    damageAnims.extend(getSplicedLerpAnims('slip-forward', 0.31, 0.94999999999999996, startTime = 1.2))
    damageAnims.append([
        'slip-forward',
        0.01,
        1.51])
    toonTrack = getToonTrack(attack, damageDelay = 3.7999999999999998, splicedDamageAnims = damageAnims, dodgeDelay = 2.3999999999999999, dodgeAnimNames = [
        'sidestep'], showDamageExtraTime = 0.40000000000000002, showMissedExtraTime = 1.3)
    return Parallel(suitTrack, toonTrack, propTrack)


def doBite(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    teeth = globalPropPool.getProp('teeth')
    propDelay = 0.80000000000000004
    propScaleUpTime = 0.5
    suitDelay = 1.73
    throwDelay = propDelay + propScaleUpTime + suitDelay
    throwDuration = 0.40000000000000002
    suitTrack = getSuitTrack(attack)
    posPoints = [
        Point3(-0.050000000000000003, 0.40999999999999998, -0.54000000000000004),
        VBase3(4.4649999999999999, -3.5630000000000002, 51.478999999999999)]
    teethAppearTrack = Sequence(getPropAppearTrack(teeth, suit.getRightHand(), posPoints, propDelay, Point3(3, 3, 3), scaleUpTime = propScaleUpTime))
    teethAppearTrack.append(Wait(suitDelay))
    teethAppearTrack.append(Func(battle.movie.needRestoreRenderProp, teeth))
    teethAppearTrack.append(Func(teeth.wrtReparentTo, battle))
    if dmg > 0:
        x = toon.getX(battle)
        y = toon.getY(battle)
        z = toon.getZ(battle)
        toonHeight = z + toon.getHeight()
        flyPoint = Point3(x, y + 2.7000000000000002, toonHeight * 0.80000000000000004)
        teethAppearTrack.append(LerpPosInterval(teeth, throwDuration, pos = flyPoint))
        teethAppearTrack.append(LerpPosInterval(teeth, 0.40000000000000002, pos = Point3(x, y + 3.2000000000000002, toonHeight * 0.69999999999999996)))
        teethAppearTrack.append(LerpPosInterval(teeth, 0.29999999999999999, pos = Point3(x, y + 4.7000000000000002, toonHeight * 0.5)))
        teethAppearTrack.append(Wait(0.20000000000000001))
        teethAppearTrack.append(LerpPosInterval(teeth, 0.10000000000000001, pos = Point3(x, y - 0.20000000000000001, toonHeight * 0.90000000000000002)))
        teethAppearTrack.append(Wait(0.40000000000000002))
        scaleTrack = Sequence(Wait(throwDelay), LerpScaleInterval(teeth, throwDuration, Point3(8, 8, 8)), Wait(0.90000000000000002), LerpScaleInterval(teeth, 0.20000000000000001, Point3(14, 14, 14)), Wait(1.2), LerpScaleInterval(teeth, 0.29999999999999999, MovieUtil.PNT3_NEARZERO))
        hprTrack = Sequence(Wait(throwDelay), LerpHprInterval(teeth, 0.29999999999999999, Point3(180, 0, 0)), Wait(0.20000000000000001), LerpHprInterval(teeth, 0.40000000000000002, Point3(180, -35, 0), startHpr = Point3(180, 0, 0)), Wait(0.59999999999999998), LerpHprInterval(teeth, 0.10000000000000001, Point3(180, -75, 0), startHpr = Point3(180, -35, 0)))
        animTrack = Sequence(Wait(throwDelay), ActorInterval(teeth, 'teeth', duration = throwDuration), ActorInterval(teeth, 'teeth', duration = 0.29999999999999999), Func(teeth.pose, 'teeth', 1), Wait(0.69999999999999996), ActorInterval(teeth, 'teeth', duration = 0.90000000000000002))
        propTrack = Sequence(Parallel(teethAppearTrack, scaleTrack, hprTrack, animTrack), Func(MovieUtil.removeProp, teeth), Func(battle.movie.clearRenderProp, teeth))
    else:
        flyPoint = __toonFacePoint(toon, parent = battle)
        flyPoint.setY(flyPoint.getY() - 7.0999999999999996)
        teethAppearTrack.append(LerpPosInterval(teeth, throwDuration, pos = flyPoint))
        teethAppearTrack.append(Func(MovieUtil.removeProp, teeth))
        teethAppearTrack.append(Func(battle.movie.clearRenderProp, teeth))
        propTrack = teethAppearTrack
    damageAnims = [
        [
            'cringe',
            0.01,
            0.69999999999999996,
            1.2],
        [
            'conked',
            0.01,
            0.20000000000000001,
            2.1000000000000001],
        [
            'conked',
            0.01,
            3.2000000000000002]]
    dodgeAnims = [
        [
            'cringe',
            0.01,
            0.69999999999999996,
            0.20000000000000001],
        [
            'duck',
            0.01,
            1.6000000000000001]]
    toonTrack = getToonTrack(attack, damageDelay = 3.2000000000000002, splicedDamageAnims = damageAnims, dodgeDelay = 2.8999999999999999, splicedDodgeAnims = dodgeAnims, showDamageExtraTime = 2.3999999999999999)
    return Parallel(suitTrack, toonTrack, propTrack)


def doChomp(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    teeth = globalPropPool.getProp('teeth')
    propDelay = 0.80000000000000004
    propScaleUpTime = 0.5
    suitDelay = 1.73
    throwDelay = propDelay + propScaleUpTime + suitDelay
    throwDuration = 0.40000000000000002
    suitTrack = getSuitTrack(attack)
    posPoints = [
        Point3(-0.050000000000000003, 0.40999999999999998, -0.54000000000000004),
        VBase3(4.4649999999999999, -3.5630000000000002, 51.478999999999999)]
    teethAppearTrack = Sequence(getPropAppearTrack(teeth, suit.getRightHand(), posPoints, propDelay, Point3(3, 3, 3), scaleUpTime = propScaleUpTime))
    teethAppearTrack.append(Wait(suitDelay))
    teethAppearTrack.append(Func(battle.movie.needRestoreRenderProp, teeth))
    teethAppearTrack.append(Func(teeth.wrtReparentTo, battle))
    if dmg > 0:
        x = toon.getX(battle)
        y = toon.getY(battle)
        z = toon.getZ(battle)
        toonHeight = z + toon.getHeight()
        flyPoint = Point3(x, y + 2.7000000000000002, toonHeight * 0.69999999999999996)
        teethAppearTrack.append(LerpPosInterval(teeth, throwDuration, pos = flyPoint))
        teethAppearTrack.append(LerpPosInterval(teeth, 0.40000000000000002, pos = Point3(x, y + 3.2000000000000002, toonHeight * 0.69999999999999996)))
        teethAppearTrack.append(LerpPosInterval(teeth, 0.29999999999999999, pos = Point3(x, y + 4.7000000000000002, toonHeight * 0.5)))
        teethAppearTrack.append(Wait(0.20000000000000001))
        teethAppearTrack.append(LerpPosInterval(teeth, 0.10000000000000001, pos = Point3(x, y, toonHeight + 3)))
        teethAppearTrack.append(LerpPosInterval(teeth, 0.10000000000000001, pos = Point3(x, y - 1.2, toonHeight * 0.69999999999999996)))
        teethAppearTrack.append(LerpPosInterval(teeth, 0.10000000000000001, pos = Point3(x, y - 0.69999999999999996, toonHeight * 0.40000000000000002)))
        teethAppearTrack.append(Wait(0.40000000000000002))
        scaleTrack = Sequence(Wait(throwDelay), LerpScaleInterval(teeth, throwDuration, Point3(6, 6, 6)), Wait(0.90000000000000002), LerpScaleInterval(teeth, 0.20000000000000001, Point3(10, 10, 10)), Wait(1.2), LerpScaleInterval(teeth, 0.29999999999999999, MovieUtil.PNT3_NEARZERO))
        hprTrack = Sequence(Wait(throwDelay), LerpHprInterval(teeth, 0.29999999999999999, Point3(180, 0, 0)), Wait(0.20000000000000001), LerpHprInterval(teeth, 0.40000000000000002, Point3(180, -35, 0), startHpr = Point3(180, 0, 0)), Wait(0.59999999999999998), LerpHprInterval(teeth, 0.10000000000000001, Point3(0, -35, 0), startHpr = Point3(180, -35, 0)))
        animTrack = Sequence(Wait(throwDelay), ActorInterval(teeth, 'teeth', duration = throwDuration), ActorInterval(teeth, 'teeth', duration = 0.29999999999999999), Func(teeth.pose, 'teeth', 1), Wait(0.69999999999999996), ActorInterval(teeth, 'teeth', duration = 0.90000000000000002))
        propTrack = Sequence(Parallel(teethAppearTrack, scaleTrack, hprTrack, animTrack), Func(MovieUtil.removeProp, teeth), Func(battle.movie.clearRenderProp, teeth))
    else:
        x = toon.getX(battle)
        y = toon.getY(battle)
        z = toon.getZ(battle)
        z = z + 0.20000000000000001
        flyPoint = Point3(x, y - 2.1000000000000001, z)
        teethAppearTrack.append(LerpPosInterval(teeth, throwDuration, pos = flyPoint))
        teethAppearTrack.append(Wait(0.20000000000000001))
        teethAppearTrack.append(LerpPosInterval(teeth, 0.20000000000000001, pos = Point3(x + 0.5, y - 2.5, z)))
        teethAppearTrack.append(LerpPosInterval(teeth, 0.20000000000000001, pos = Point3(x + 1.0, y - 3.0, z + 0.40000000000000002)))
        teethAppearTrack.append(LerpPosInterval(teeth, 0.20000000000000001, pos = Point3(x + 1.3, y - 3.6000000000000001, z)))
        teethAppearTrack.append(LerpPosInterval(teeth, 0.20000000000000001, pos = Point3(x + 0.90000000000000002, y - 3.1000000000000001, z + 0.40000000000000002)))
        teethAppearTrack.append(LerpPosInterval(teeth, 0.20000000000000001, pos = Point3(x + 0.29999999999999999, y - 2.6000000000000001, z)))
        teethAppearTrack.append(LerpPosInterval(teeth, 0.20000000000000001, pos = Point3(x - 0.10000000000000001, y - 2.2000000000000002, z + 0.40000000000000002)))
        teethAppearTrack.append(LerpPosInterval(teeth, 0.20000000000000001, pos = Point3(x - 0.40000000000000002, y - 1.8999999999999999, z)))
        teethAppearTrack.append(LerpPosInterval(teeth, 0.20000000000000001, pos = Point3(x - 0.69999999999999996, y - 2.1000000000000001, z + 0.40000000000000002)))
        teethAppearTrack.append(LerpPosInterval(teeth, 0.20000000000000001, pos = Point3(x - 0.80000000000000004, y - 2.2999999999999998, z)))
        teethAppearTrack.append(LerpScaleInterval(teeth, 0.59999999999999998, MovieUtil.PNT3_NEARZERO))
        hprTrack = Sequence(Wait(throwDelay), LerpHprInterval(teeth, 0.29999999999999999, Point3(180, 0, 0)), Wait(0.5), LerpHprInterval(teeth, 0.40000000000000002, Point3(80, 0, 0), startHpr = Point3(180, 0, 0)), LerpHprInterval(teeth, 0.80000000000000004, Point3(-10, 0, 0), startHpr = Point3(80, 0, 0)))
        animTrack = Sequence(Wait(throwDelay), ActorInterval(teeth, 'teeth', duration = 3.6000000000000001))
        propTrack = Sequence(Parallel(teethAppearTrack, hprTrack, animTrack), Func(MovieUtil.removeProp, teeth), Func(battle.movie.clearRenderProp, teeth))
    damageAnims = [
        [
            'cringe',
            0.01,
            0.69999999999999996,
            1.2],
        [
            'spit',
            0.01,
            2.9500000000000002,
            1.47],
        [
            'spit',
            0.01,
            4.4199999999999999,
            0.070000000000000007],
        [
            'spit',
            0.080000000000000002,
            4.4900000000000002,
            -0.070000000000000007],
        [
            'spit',
            0.080000000000000002,
            4.4199999999999999,
            0.070000000000000007],
        [
            'spit',
            0.080000000000000002,
            4.4900000000000002,
            -0.070000000000000007],
        [
            'spit',
            0.080000000000000002,
            4.4199999999999999,
            0.070000000000000007],
        [
            'spit',
            0.080000000000000002,
            4.4900000000000002,
            -0.070000000000000007],
        [
            'spit',
            0.01,
            4.4199999999999999]]
    dodgeAnims = [
        [
            'jump',
            0.01,
            0.01]]
    toonTrack = getToonTrack(attack, damageDelay = 3.2000000000000002, splicedDamageAnims = damageAnims, dodgeDelay = 2.75, splicedDodgeAnims = dodgeAnims, showDamageExtraTime = 1.3999999999999999)
    return Parallel(suitTrack, toonTrack, propTrack)


def doEvictionNotice(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    paper = globalPropPool.getProp('shredder-paper')
    suitTrack = getSuitTrack(attack)
    posPoints = [
        Point3(-0.040000000000000001, 0.14999999999999999, -1.3799999999999999),
        VBase3(10.584, -11.945, 18.315999999999999)]
    propTrack = Sequence(getPropAppearTrack(paper, suit.getRightHand(), posPoints, 0.80000000000000004, MovieUtil.PNT3_ONE, scaleUpTime = 0.5))
    propTrack.append(Wait(1.73))
    hitPoint = __toonFacePoint(toon, parent = battle)
    hitPoint.setX(hitPoint.getX() - 1.3999999999999999)
    missPoint = __toonGroundPoint(attack, toon, 0.69999999999999996, parent = battle)
    missPoint.setX(missPoint.getX() - 1.1000000000000001)
    propTrack.append(getPropThrowTrack(attack, paper, [
        hitPoint], [
        missPoint], parent = battle))
    toonTrack = getToonTrack(attack, 3.3999999999999999, [
        'conked'], 2.7999999999999998, [
        'jump'])
    return Parallel(suitTrack, toonTrack, propTrack)


def doWithdrawal(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    BattleParticles.loadParticles()
    particleEffect = BattleParticles.createParticleEffect('Withdrawal')
    BattleParticles.setEffectTexture(particleEffect, 'snow-particle')
    suitTrack = getSuitAnimTrack(attack)
    partTrack = getPartTrack(particleEffect, 1.0000000000000001e-005, suitTrack.getDuration() + 1.2, [
        particleEffect,
        suit,
        0])
    toonTrack = getToonTrack(attack, 1.2, [
        'cringe'], 0.20000000000000001, splicedDodgeAnims = [
        [
            'duck',
            1.0000000000000001e-005,
            0.80000000000000004]], showMissedExtraTime = 0.80000000000000004)
    headParts = toon.getHeadParts()
    torsoParts = toon.getTorsoParts()
    legsParts = toon.getLegsParts()
    
    def changeColor(parts):
        track = Parallel()
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            track.append(Func(nextPart.setColorScale, Vec4(0, 0, 0, 1)))
        
        return track

    
    def resetColor(parts):
        track = Parallel()
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            track.append(Func(nextPart.clearColorScale))
        
        return track

    soundTrack = getSoundTrack('SA_withdrawl.mp3', delay = 1.3999999999999999, node = suit)
    if dmg > 0:
        colorTrack = Sequence()
        colorTrack.append(Wait(1.6000000000000001))
        colorTrack.append(Func(battle.movie.needRestoreColor))
        colorTrack.append(Parallel(changeColor(headParts), changeColor(torsoParts), changeColor(legsParts)))
        colorTrack.append(Wait(2.8999999999999999))
        colorTrack.append(resetColor(headParts))
        colorTrack.append(resetColor(torsoParts))
        colorTrack.append(resetColor(legsParts))
        colorTrack.append(Func(battle.movie.clearRestoreColor))
        return Parallel(suitTrack, partTrack, toonTrack, soundTrack, colorTrack)
    else:
        return Parallel(suitTrack, partTrack, toonTrack, soundTrack)


def doJargon(attack):
    suit = attack['suit']
    battle = attack['battle']
    BattleParticles.loadParticles()
    particleEffect = BattleParticles.createParticleEffect(file = 'jargonSpray')
    particleEffect2 = BattleParticles.createParticleEffect(file = 'jargonSpray')
    particleEffect3 = BattleParticles.createParticleEffect(file = 'jargonSpray')
    particleEffect4 = BattleParticles.createParticleEffect(file = 'jargonSpray')
    BattleParticles.setEffectTexture(particleEffect, 'jargon-brow', color = Vec4(1, 0, 0, 1))
    BattleParticles.setEffectTexture(particleEffect2, 'jargon-deep', color = Vec4(0, 0, 0, 1))
    BattleParticles.setEffectTexture(particleEffect3, 'jargon-hoop', color = Vec4(1, 0, 0, 1))
    BattleParticles.setEffectTexture(particleEffect4, 'jargon-ipo', color = Vec4(0, 0, 0, 1))
    damageDelay = 2.2000000000000002
    dodgeDelay = 1.5
    partDelay = 1.1000000000000001
    partInterval = 1.2
    suitTrack = getSuitTrack(attack)
    partTrack = getPartTrack(particleEffect, partDelay + partInterval * 0, 2, [
        particleEffect,
        suit,
        0])
    partTrack2 = getPartTrack(particleEffect2, partDelay + partInterval * 1, 2, [
        particleEffect2,
        suit,
        0])
    partTrack3 = getPartTrack(particleEffect3, partDelay + partInterval * 2, 2, [
        particleEffect3,
        suit,
        0])
    partTrack4 = getPartTrack(particleEffect4, partDelay + partInterval * 3, 1.0, [
        particleEffect4,
        suit,
        0])
    damageAnims = []
    damageAnims.append([
        'conked',
        0.0001,
        0,
        0.40000000000000002])
    damageAnims.append([
        'conked',
        0.0001,
        2.7000000000000002,
        0.84999999999999998])
    damageAnims.append([
        'conked',
        0.0001,
        0.40000000000000002,
        0.089999999999999997])
    damageAnims.append([
        'conked',
        0.0001,
        0.40000000000000002,
        0.089999999999999997])
    damageAnims.append([
        'conked',
        0.0001,
        0.40000000000000002,
        0.66000000000000003])
    damageAnims.append([
        'conked',
        0.0001,
        0.40000000000000002,
        0.089999999999999997])
    damageAnims.append([
        'conked',
        0.0001,
        0.40000000000000002,
        0.089999999999999997])
    damageAnims.append([
        'conked',
        0.0001,
        0.40000000000000002,
        0.85999999999999999])
    damageAnims.append([
        'conked',
        0.0001,
        0.40000000000000002,
        0.14000000000000001])
    damageAnims.append([
        'conked',
        0.0001,
        0.40000000000000002,
        0.14000000000000001])
    damageAnims.append([
        'conked',
        0.0001,
        0.40000000000000002])
    dodgeAnims = [
        [
            'duck',
            0.0001,
            1.2],
        [
            'duck',
            0.0001,
            1.3]]
    toonTrack = getToonTrack(attack, damageDelay = damageDelay, splicedDamageAnims = damageAnims, dodgeDelay = dodgeDelay, splicedDodgeAnims = dodgeAnims, showMissedExtraTime = 1.6000000000000001, showDamageExtraTime = 0.69999999999999996)
    soundTrack = getSoundTrack('SA_jargon.mp3', delay = 2.1000000000000001, node = suit)
    return Parallel(suitTrack, toonTrack, soundTrack, partTrack, partTrack2, partTrack3, partTrack4)


def doMumboJumbo(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    BattleParticles.loadParticles()
    particleEffect = BattleParticles.createParticleEffect(file = 'mumboJumboSpray')
    particleEffect2 = BattleParticles.createParticleEffect(file = 'mumboJumboSpray')
    particleEffect3 = BattleParticles.createParticleEffect(file = 'mumboJumboSmother')
    particleEffect4 = BattleParticles.createParticleEffect(file = 'mumboJumboSmother')
    particleEffect5 = BattleParticles.createParticleEffect(file = 'mumboJumboSmother')
    BattleParticles.setEffectTexture(particleEffect, 'mumbojumbo-boiler', color = Vec4(1, 0, 0, 1))
    BattleParticles.setEffectTexture(particleEffect2, 'mumbojumbo-creative', color = Vec4(1, 0, 0, 1))
    BattleParticles.setEffectTexture(particleEffect3, 'mumbojumbo-deben', color = Vec4(1, 0, 0, 1))
    BattleParticles.setEffectTexture(particleEffect4, 'mumbojumbo-high', color = Vec4(1, 0, 0, 1))
    BattleParticles.setEffectTexture(particleEffect5, 'mumbojumbo-iron', color = Vec4(1, 0, 0, 1))
    suitTrack = getSuitTrack(attack)
    partTrack = getPartTrack(particleEffect, 2.5, 2, [
        particleEffect,
        suit,
        0])
    partTrack2 = getPartTrack(particleEffect2, 2.5, 2, [
        particleEffect2,
        suit,
        0])
    partTrack3 = getPartTrack(particleEffect3, 3.2999999999999998, 1.7, [
        particleEffect3,
        toon,
        0])
    partTrack4 = getPartTrack(particleEffect4, 3.2999999999999998, 1.7, [
        particleEffect4,
        toon,
        0])
    partTrack5 = getPartTrack(particleEffect5, 3.2999999999999998, 1.7, [
        particleEffect5,
        toon,
        0])
    toonTrack = getToonTrack(attack, 3.2000000000000002, [
        'cringe'], 2.2000000000000002, [
        'sidestep'])
    soundTrack = getSoundTrack('SA_mumbo_jumbo.mp3', delay = 2.5, node = suit)
    if dmg > 0:
        return Parallel(suitTrack, toonTrack, soundTrack, partTrack, partTrack2, partTrack3, partTrack4, partTrack5)
    else:
        return Parallel(suitTrack, toonTrack, soundTrack, partTrack, partTrack2)


def doGuiltTrip(attack):
    suit = attack['suit']
    battle = attack['battle']
    centerColor = Vec4(1.0, 0.20000000000000001, 0.20000000000000001, 0.90000000000000002)
    edgeColor = Vec4(0.90000000000000002, 0.90000000000000002, 0.90000000000000002, 0.40000000000000002)
    powerBar1 = BattleParticles.createParticleEffect(file = 'guiltTrip')
    powerBar2 = BattleParticles.createParticleEffect(file = 'guiltTrip')
    powerBar1.setPos(0, 6.0999999999999996, 0.40000000000000002)
    powerBar1.setHpr(-90, 0, 0)
    powerBar2.setPos(0, 6.0999999999999996, 0.40000000000000002)
    powerBar2.setHpr(90, 0, 0)
    powerBar1.setScale(5)
    powerBar2.setScale(5)
    powerBar1Particles = powerBar1.getParticlesNamed('particles-1')
    powerBar2Particles = powerBar2.getParticlesNamed('particles-1')
    powerBar1Particles.renderer.setCenterColor(centerColor)
    powerBar1Particles.renderer.setEdgeColor(edgeColor)
    powerBar2Particles.renderer.setCenterColor(centerColor)
    powerBar2Particles.renderer.setEdgeColor(edgeColor)
    waterfallEffect = BattleParticles.createParticleEffect('Waterfall')
    waterfallEffect.setScale(11)
    waterfallParticles = waterfallEffect.getParticlesNamed('particles-1')
    waterfallParticles.renderer.setCenterColor(centerColor)
    waterfallParticles.renderer.setEdgeColor(edgeColor)
    suitTrack = getSuitAnimTrack(attack)
    
    def getPowerTrack(effect, suit = suit, battle = battle):
        partTrack = Sequence(Wait(0.69999999999999996), Func(battle.movie.needRestoreParticleEffect, effect), Func(effect.start, suit), Wait(0.40000000000000002), LerpPosInterval(effect, 1.0, Point3(0, 15, 0.40000000000000002)), LerpFunctionInterval(effect.setAlphaScale, fromData = 1, toData = 0, duration = 0.40000000000000002), Func(effect.cleanup), Func(battle.movie.clearRestoreParticleEffect, effect))
        return partTrack

    partTrack1 = getPowerTrack(powerBar1)
    partTrack2 = getPowerTrack(powerBar2)
    waterfallTrack = getPartTrack(waterfallEffect, 0.59999999999999998, 0.59999999999999998, [
        waterfallEffect,
        suit,
        0])
    toonTracks = getToonTracks(attack, 1.5, [
        'slip-forward'], 0.85999999999999999, [
        'jump'])
    soundTrack = getSoundTrack('SA_guilt_trip.mp3', delay = 1.1000000000000001, node = suit)
    return Parallel(suitTrack, partTrack1, partTrack2, soundTrack, waterfallTrack, toonTracks)


def doRestrainingOrder(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    paper = globalPropPool.getProp('shredder-paper')
    suitTrack = getSuitTrack(attack)
    posPoints = [
        Point3(-0.040000000000000001, 0.14999999999999999, -1.3799999999999999),
        VBase3(10.584, -11.945, 18.315999999999999)]
    propTrack = Sequence(getPropAppearTrack(paper, suit.getRightHand(), posPoints, 0.80000000000000004, MovieUtil.PNT3_ONE, scaleUpTime = 0.5))
    propTrack.append(Wait(1.73))
    hitPoint = __toonFacePoint(toon, parent = battle)
    hitPoint.setX(hitPoint.getX() - 1.3999999999999999)
    missPoint = __toonGroundPoint(attack, toon, 0.69999999999999996, parent = battle)
    missPoint.setX(missPoint.getX() - 1.1000000000000001)
    propTrack.append(getPropThrowTrack(attack, paper, [
        hitPoint], [
        missPoint], parent = battle))
    damageAnims = [
        [
            'conked',
            0.01,
            0.29999999999999999,
            0.20000000000000001],
        [
            'struggle',
            0.01,
            0.20000000000000001]]
    toonTrack = getToonTrack(attack, damageDelay = 3.3999999999999999, splicedDamageAnims = damageAnims, dodgeDelay = 2.7999999999999998, dodgeAnimNames = [
        'sidestep'])
    if dmg > 0:
        restraintCloud = BattleParticles.createParticleEffect(file = 'restrainingOrderCloud')
        restraintCloud.setPos(hitPoint.getX(), hitPoint.getY() + 0.5, hitPoint.getZ())
        cloudTrack = getPartTrack(restraintCloud, 3.5, 0.20000000000000001, [
            restraintCloud,
            battle,
            0])
        return Parallel(suitTrack, cloudTrack, toonTrack, propTrack)
    else:
        return Parallel(suitTrack, toonTrack, propTrack)


def doSpin(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    damageDelay = 1.7
    sprayEffect = BattleParticles.createParticleEffect(file = 'spinSpray')
    spinEffect1 = BattleParticles.createParticleEffect(file = 'spinEffect')
    spinEffect2 = BattleParticles.createParticleEffect(file = 'spinEffect')
    spinEffect3 = BattleParticles.createParticleEffect(file = 'spinEffect')
    spinEffect1.reparentTo(toon)
    spinEffect2.reparentTo(toon)
    spinEffect3.reparentTo(toon)
    height1 = toon.getHeight() * (whrandom.random() * 0.20000000000000001 + 0.69999999999999996)
    height2 = toon.getHeight() * (whrandom.random() * 0.20000000000000001 + 0.40000000000000002)
    height3 = toon.getHeight() * (whrandom.random() * 0.20000000000000001 + 0.10000000000000001)
    spinEffect1.setPos(Point3(0, -1.3, height1))
    spinEffect1.setHpr(0, 0, -whrandom.random() * 10 - 85)
    spinEffect1.setHpr(spinEffect1, 0, 50, 0)
    spinEffect2.setPos(0, -1.3, height2)
    spinEffect2.setHpr(0, 0, -whrandom.random() * 10 - 85)
    spinEffect2.setHpr(spinEffect2, 0, 50, 0)
    spinEffect3.setPos(0, -1.3, height3)
    spinEffect3.setHpr(0, 0, -whrandom.random() * 10 - 85)
    spinEffect3.setHpr(spinEffect3, 0, 50, 0)
    spinEffect1.wrtReparentTo(battle)
    spinEffect2.wrtReparentTo(battle)
    spinEffect3.wrtReparentTo(battle)
    suitTrack = getSuitTrack(attack)
    sprayTrack = getPartTrack(sprayEffect, 1.0, 1.8999999999999999, [
        sprayEffect,
        suit,
        0])
    spinTrack1 = getPartTrack(spinEffect1, 2.1000000000000001, 3.8999999999999999, [
        spinEffect1,
        battle,
        0])
    spinTrack2 = getPartTrack(spinEffect2, 2.1000000000000001, 3.8999999999999999, [
        spinEffect2,
        battle,
        0])
    spinTrack3 = getPartTrack(spinEffect3, 2.1000000000000001, 3.8999999999999999, [
        spinEffect3,
        battle,
        0])
    damageAnims = []
    damageAnims.append([
        'duck',
        0.01,
        0.01,
        1.1000000000000001])
    damageAnims.extend(getSplicedLerpAnims('think', 0.66000000000000003, 1.1000000000000001, startTime = 2.2599999999999998))
    damageAnims.extend(getSplicedLerpAnims('think', 0.66000000000000003, 1.1000000000000001, startTime = 2.2599999999999998))
    toonTrack = getToonTrack(attack, damageDelay = damageDelay, splicedDamageAnims = damageAnims, dodgeDelay = 0.91000000000000003, dodgeAnimNames = [
        'sidestep'], showDamageExtraTime = 2.1000000000000001, showMissedExtraTime = 1.0)
    if dmg > 0:
        toonSpinTrack = Sequence(Wait(damageDelay + 0.90000000000000002), LerpHprInterval(toon, 0.69999999999999996, Point3(-10, 0, 0)), LerpHprInterval(toon, 0.5, Point3(-30, 0, 0)), LerpHprInterval(toon, 0.20000000000000001, Point3(-60, 0, 0)), LerpHprInterval(toon, 0.69999999999999996, Point3(-700, 0, 0)), LerpHprInterval(toon, 1.0, Point3(-1310, 0, 0)), LerpHprInterval(toon, 0.40000000000000002, toon.getHpr()), Wait(0.5))
        return Parallel(suitTrack, sprayTrack, toonTrack, toonSpinTrack, spinTrack1, spinTrack2, spinTrack3)
    else:
        return Parallel(suitTrack, sprayTrack, toonTrack)


def doLegalese(attack):
    suit = attack['suit']
    BattleParticles.loadParticles()
    sprayEffect1 = BattleParticles.createParticleEffect(file = 'legaleseSpray')
    sprayEffect2 = BattleParticles.createParticleEffect(file = 'legaleseSpray')
    sprayEffect3 = BattleParticles.createParticleEffect(file = 'legaleseSpray')
    color = Vec4(0.40000000000000002, 0, 0, 1)
    BattleParticles.setEffectTexture(sprayEffect1, 'legalese-hc', color = color)
    BattleParticles.setEffectTexture(sprayEffect2, 'legalese-qpq', color = color)
    BattleParticles.setEffectTexture(sprayEffect3, 'legalese-vd', color = color)
    partDelay = 1.3
    partDuration = 1.1499999999999999
    damageDelay = 1.8999999999999999
    dodgeDelay = 1.1000000000000001
    suitTrack = getSuitTrack(attack)
    sprayTrack1 = getPartTrack(sprayEffect1, partDelay, partDuration, [
        sprayEffect1,
        suit,
        0])
    sprayTrack2 = getPartTrack(sprayEffect2, partDelay + 0.80000000000000004, partDuration, [
        sprayEffect2,
        suit,
        0])
    sprayTrack3 = getPartTrack(sprayEffect3, partDelay + 1.6000000000000001, partDuration, [
        sprayEffect3,
        suit,
        0])
    damageAnims = []
    damageAnims.append([
        'cringe',
        1.0000000000000001e-005,
        0.29999999999999999,
        0.80000000000000004])
    damageAnims.append([
        'cringe',
        1.0000000000000001e-005,
        0.29999999999999999,
        0.80000000000000004])
    damageAnims.append([
        'cringe',
        1.0000000000000001e-005,
        0.29999999999999999])
    toonTrack = getToonTrack(attack, damageDelay = damageDelay, splicedDamageAnims = damageAnims, dodgeDelay = dodgeDelay, dodgeAnimNames = [
        'sidestep'], showMissedExtraTime = 0.80000000000000004)
    return Parallel(suitTrack, toonTrack, sprayTrack1, sprayTrack2, sprayTrack3)


def doPeckingOrder(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    throwDuration = 3.0299999999999998
    throwDelay = 3.2000000000000002
    suitTrack = getSuitTrack(attack)
    numBirds = whrandom.randint(4, 7)
    birdTracks = Parallel()
    propDelay = 1.5
    for i in range(0, numBirds):
        next = globalPropPool.getProp('bird')
        next.setScale(0.01)
        next.reparentTo(suit.getRightHand())
        next.setPos(whrandom.random() * 0.59999999999999998 - 0.29999999999999999, whrandom.random() * 0.59999999999999998 - 0.29999999999999999, whrandom.random() * 0.59999999999999998 - 0.29999999999999999)
        if dmg > 0:
            hitPoint = Point3(whrandom.random() * 5 - 2.5, whrandom.random() * 2 - 1 - 6, (whrandom.random() * 3 - 1.5) + toon.getHeight() - 0.90000000000000002)
        else:
            hitPoint = Point3(whrandom.random() * 2 - 1, whrandom.random() * 4 - 2 - 15, (whrandom.random() * 4 - 2) + 2.2000000000000002)
        birdTrack = Sequence(Wait(throwDelay), Func(battle.movie.needRestoreRenderProp, next), Func(next.wrtReparentTo, battle), Func(next.setHpr, Point3(90, 20, 0)), LerpPosInterval(next, 1.1000000000000001, hitPoint))
        scaleTrack = Sequence(Wait(throwDelay), LerpScaleInterval(next, 0.14999999999999999, Point3(9, 9, 9)))
        birdTracks.append(Sequence(Parallel(birdTrack, scaleTrack), Func(MovieUtil.removeProp, next)))
    
    damageAnims = []
    damageAnims.append([
        'cringe',
        0.01,
        0.14000000000000001,
        0.20999999999999999])
    damageAnims.append([
        'cringe',
        0.01,
        0.14000000000000001,
        0.13])
    damageAnims.append([
        'cringe',
        0.01,
        0.42999999999999999])
    toonTrack = getToonTrack(attack, damageDelay = 4.2000000000000002, splicedDamageAnims = damageAnims, dodgeDelay = 2.7999999999999998, dodgeAnimNames = [
        'sidestep'], showMissedExtraTime = 1.1000000000000001)
    return Parallel(suitTrack, toonTrack, birdTracks)

