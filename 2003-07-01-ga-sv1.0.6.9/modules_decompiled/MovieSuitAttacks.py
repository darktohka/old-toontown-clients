# File: M (Python 2.2)

from ToontownGlobals import *
from SuitBattleGlobals import *
from IntervalGlobal import *
from BattleBase import *
from BattleProps import *
from AvatarDNA import *
from BattleBase import *
from BattleSounds import *
import MovieCamera
import DirectNotifyGlobal
import MovieUtil
import ParticleEffect
import BattleParticles
import Toon
import Localizer
notify = DirectNotifyGlobal.directNotify.newCategory('MovieSuitAttacks')

def __doDamage(toon, dmg, died):
    if dmg > 0 and toon.hp != None:
        if died != 0:
            hp = 0
        else:
            hp = toon.hp - dmg
        if hp > 0 or died != 0:
            notify.debug('setting toon: %s hp: %d' % (toon.getName(), hp))
            toon.setHp(hp)
        else:
            notify.warning('__doDamage() - hp: %d' % hp)
    


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
        toonHprTrack = Track([
            FunctionInterval(toon.headsUp, extraArgs = [
                battle,
                MovieUtil.PNT3_ZERO]),
            FunctionInterval(toon.loop, extraArgs = [
                'neutral'])])
    else:
        toonTracks = []
        for t in target:
            toon = t['toon']
            toonTracks.append(Track([
                FunctionInterval(toon.headsUp, extraArgs = [
                    battle,
                    MovieUtil.PNT3_ZERO]),
                FunctionInterval(toon.loop, extraArgs = [
                    'neutral'])]))
        
        toonHprTrack = MultiTrack(toonTracks)
    suit = attack['suit']
    neutralIval = FunctionInterval(suit.loop, extraArgs = [
        'neutral'])
    suitTrack = Track([
        suitTrack,
        neutralIval,
        toonHprTrack])
    suitPos = suit.getPos(battle)
    (resetPos, resetHpr) = battle.getActorPosHpr(suit)
    if battle.isSuitLured(suit):
        resetTrack = getResetTrack(suit, battle)
        resetSuitTrack = Track([
            resetTrack,
            suitTrack])
        waitTrack = Track([
            WaitInterval(resetTrack.getDuration()),
            FunctionInterval(battle.unlureSuit, extraArgs = [
                suit])])
        resetCamTrack = Track([
            waitTrack,
            camTrack])
        return (resetSuitTrack, resetCamTrack)
    else:
        return (suitTrack, camTrack)


def getResetTrack(suit, battle):
    (resetPos, resetHpr) = battle.getActorPosHpr(suit)
    moveDist = Vec3(suit.getPos(battle) - resetPos).length()
    moveDuration = 0.5
    walkTrack = Track([
        FunctionInterval(suit.setHpr, extraArgs = [
            battle,
            resetHpr]),
        ActorInterval(suit, 'walk', startTime = 1, duration = moveDuration, endTime = 1.0000000000000001e-005),
        FunctionInterval(suit.loop, extraArgs = [
            'neutral'])])
    moveTrack = Track([
        LerpPosInterval(suit, moveDuration, resetPos, other = battle)])
    return MultiTrack([
        walkTrack,
        moveTrack])


def __makeCancelledNodePath():
    tn = TextNode('CANCELLED')
    tn.setFont(getSuitFont())
    tn.setText(Localizer.MovieSuitCancelled)
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
    ivals = [
        WaitInterval(delay),
        FunctionInterval(suit.setChatAbsolute, extraArgs = [
            taunt,
            CFSpeech | CFTimeout])]
    
    def reparentTrap(suit = suit, battle = battle, trapStorage = trapStorage):
        trapProp = suit.battleTrapProp
        if trapProp != None:
            trapProp.wrtReparentTo(battle)
            trapStorage['trap'] = trapProp
        

    ivals.append(FunctionInterval(reparentTrap))
    ivals.append(FunctionInterval(suit.headsUp, extraArgs = [
        battle,
        targetPos]))
    if splicedAnims:
        ivals.extend(getSplicedAnims(splicedAnims, actor = suit))
    else:
        ivals.append(ActorInterval(suit, attack['animName']))
    (origPos, origHpr) = battle.getActorPosHpr(suit)
    ivals.append(FunctionInterval(suit.setHpr, extraArgs = [
        battle,
        origHpr]))
    
    def returnTrapToSuit(suit = suit, trapStorage = trapStorage):
        trapProp = trapStorage['trap']
        if trapProp != None:
            trapProp.wrtReparentTo(suit)
            suit.battleTrapProp = trapProp
        

    ivals.append(FunctionInterval(returnTrapToSuit))
    ivals.append(FunctionInterval(suit.clearChat))
    return Track(ivals)


def getSuitAnimTrack(attack, delay = 0):
    suit = attack['suit']
    tauntIndex = attack['taunt']
    taunt = getAttackTaunt(attack['name'], tauntIndex)
    return Track([
        WaitInterval(delay),
        FunctionInterval(suit.setChatAbsolute, extraArgs = [
            taunt,
            CFSpeech | CFTimeout]),
        ActorInterval(attack['suit'], attack['animName']),
        FunctionInterval(suit.clearChat)])


def getPartTrack(particleEffect, startDelay, durationDelay, partExtraArgs):
    particleEffect = partExtraArgs[0]
    parent = partExtraArgs[1]
    if len(partExtraArgs) > 2:
        worldRelative = partExtraArgs[2]
    else:
        worldRelative = 1
    return Track([
        (startDelay, ParticleInterval(particleEffect, parent, worldRelative, duration = durationDelay))])


def getToonTrack(attack, damageDelay = 9.9999999999999995e-007, damageAnimNames = None, dodgeDelay = 0.0001, dodgeAnimNames = None, splicedDamageAnims = None, splicedDodgeAnims = None, target = None, showDamageExtraTime = 0.01, showMissedExtraTime = 0.5):
    if not target:
        target = attack['target']
    
    toon = target['toon']
    battle = attack['battle']
    suit = attack['suit']
    suitPos = suit.getPos(battle)
    dmg = target['hp']
    ivals = []
    ivals.append(FunctionInterval(toon.headsUp, extraArgs = [
        battle,
        suitPos]))
    if dmg > 0:
        ivals.append(getToonTakeDamageIntervals(toon, target['died'], dmg, damageDelay, damageAnimNames, splicedDamageAnims, showDamageExtraTime))
        return Track(ivals)
    else:
        ivals.extend(getToonDodgeMultiTrack(target, dodgeDelay, dodgeAnimNames, splicedDodgeAnims, showMissedExtraTime))
        animTrack = Track(ivals)
        indicatorTrack = Track([
            WaitInterval(dodgeDelay + showMissedExtraTime),
            FunctionInterval(MovieUtil.indicateMissed, extraArgs = [
                toon])])
        return MultiTrack([
            animTrack,
            indicatorTrack])


def getToonTracks(attack, damageDelay = 9.9999999999999995e-007, damageAnimNames = None, dodgeDelay = 9.9999999999999995e-007, dodgeAnimNames = None, splicedDamageAnims = None, splicedDodgeAnims = None, showDamageExtraTime = 0.01, showMissedExtraTime = 0.5):
    toonTracks = []
    targets = attack['target']
    for i in range(len(targets)):
        tgt = targets[i]
        toonTracks.append(getToonTrack(attack, damageDelay, damageAnimNames, dodgeDelay, dodgeAnimNames, splicedDamageAnims, splicedDodgeAnims, target = tgt, showDamageExtraTime = showDamageExtraTime, showMissedExtraTime = showMissedExtraTime))
    
    return toonTracks


def getToonDodgeMultiTrack(target, dodgeDelay, dodgeAnimNames, splicedDodgeAnims, showMissedExtraTime):
    toon = target['toon']
    toonAnims = []
    toonAnims.append(WaitInterval(dodgeDelay))
    if dodgeAnimNames:
        for d in dodgeAnimNames:
            if d == 'sidestep':
                toonAnims.append(getAllyToonsDodgeMultiTrack(target))
            else:
                toonAnims.append(ActorInterval(toon, d))
        
    else:
        toonAnims.extend(getSplicedAnims(splicedDodgeAnims, actor = toon))
    toonAnims.append(FunctionInterval(toon.loop, extraArgs = [
        'neutral']))
    return toonAnims


def getAllyToonsDodgeMultiTrack(target):
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
    toonTracks = []
    for t in toonDodgeList:
        toonTracks.append(Track([
            ActorInterval(t, sidestepAnim),
            FunctionInterval(t.loop, extraArgs = [
                'neutral'])]))
    
    toonTracks.append(Track([
        ActorInterval(toon, sidestepAnim),
        FunctionInterval(toon.loop, extraArgs = [
            'neutral'])]))
    toonTracks.append(Track([
        WaitInterval(0.5),
        SoundInterval(soundEffect, node = toon)]))
    return MultiTrack(toonTracks)


def getPropTrack(prop, parent, posPoints, appearDelay, remainDelay, scaleUpPoint = Point3(1), scaleUpTime = 0.5, scaleDownTime = 0.5, startScale = Point3(0.01), anim = 0, propName = 'none', animDuration = 0.0, animStartTime = 0.0, onlyIvals = 0):
    extraArgsForShowProp = [
        prop,
        parent]
    extraArgsForShowProp.extend(posPoints)
    if anim == 1:
        ivals = [
            WaitInterval(appearDelay),
            FunctionInterval(__showProp, extraArgs = extraArgsForShowProp),
            LerpScaleInterval(prop, scaleUpTime, scaleUpPoint, startScale = startScale),
            ActorInterval(prop, propName, duration = animDuration, startTime = animStartTime),
            WaitInterval(remainDelay),
            FunctionInterval(MovieUtil.removeProp, extraArgs = [
                prop])]
    else:
        ivals = [
            WaitInterval(appearDelay),
            FunctionInterval(__showProp, extraArgs = extraArgsForShowProp),
            LerpScaleInterval(prop, scaleUpTime, scaleUpPoint, startScale = startScale),
            WaitInterval(remainDelay),
            LerpScaleInterval(prop, scaleDownTime, MovieUtil.PNT3_NEARZERO),
            FunctionInterval(MovieUtil.removeProp, extraArgs = [
                prop])]
    if onlyIvals == 1:
        return ivals
    else:
        return Track(ivals)


def getPropAppearIntervals(prop, parent, posPoints, appearDelay, scaleUpPoint = Point3(1), scaleUpTime = 0.5, startScale = Point3(0.01), poseExtraArgs = []):
    showPropExtraArgs = [
        prop,
        parent]
    showPropExtraArgs.extend(posPoints)
    propIvals = [
        WaitInterval(appearDelay),
        FunctionInterval(__showProp, extraArgs = showPropExtraArgs)]
    if poseExtraArgs != []:
        propIvals.append(FunctionInterval(prop.pose, extraArgs = poseExtraArgs))
    
    propIvals.append(LerpScaleInterval(prop, scaleUpTime, scaleUpPoint, startScale = startScale))
    return propIvals


def getPropThrowIntervals(attack, prop, hitPoints = [], missPoints = [], hitDuration = 0.5, missDuration = 0.5, hitPointNames = 'none', missPointNames = 'none', lookAt = 'none', groundPointOffSet = 0, missScaleDown = None, parent = render):
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
    
    propIvals = []
    propIvals.append(FunctionInterval(battle.movie.needRestoreRenderProp, extraArgs = [
        prop]))
    propIvals.append(FunctionInterval(prop.wrtReparentTo, extraArgs = [
        parent]))
    if lookAt != 'none':
        propIvals.append(FunctionInterval(prop.lookAt, extraArgs = lookAt))
    
    if dmg > 0:
        for i in range(len(hitPoints)):
            pos = hitPoints[i]
            propIvals.append(LerpPosInterval(prop, hitDuration, pos = pos))
        
    else:
        for i in range(len(missPoints)):
            pos = missPoints[i]
            propIvals.append(LerpPosInterval(prop, missDuration, pos = pos))
        
        if missScaleDown:
            propIvals.append(LerpScaleInterval(prop, missScaleDown, MovieUtil.PNT3_NEARZERO))
        
    propIvals.append(FunctionInterval(MovieUtil.removeProp, extraArgs = [
        prop]))
    propIvals.append(FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
        prop]))
    return propIvals


def getThrowIvals(object, target, duration = 1.0, parent = render, gravity = -32.143999999999998):
    values = { }
    
    def calcOriginAndVelocity(object = object, target = target, values = values, duration = duration, parent = parent, gravity = gravity):
        if callable(target):
            target = target()
        
        object.wrtReparentTo(parent)
        values['origin'] = object.getPos(parent)
        origin = object.getPos(parent)
        values['velocity'] = (target[2] - origin[2] - 0.5 * gravity * duration * duration) / duration

    return [
        FunctionInterval(calcOriginAndVelocity),
        LerpFunctionInterval(throwPos, fromData = 0.0, toData = 1.0, duration = duration, extraArgs = [
            object,
            duration,
            target,
            values,
            gravity])]


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


def getToonTakeDamageIntervals(toon, died, dmg, delay, damageAnimNames = None, splicedDamageAnims = None, showDamageExtraTime = 0.01):
    toonIvals = []
    toonIvals.append(WaitInterval(delay))
    if damageAnimNames:
        for d in damageAnimNames:
            toonIvals.append(ActorInterval(toon, d))
        
        indicatorTrack = Track([
            (delay + showDamageExtraTime, FunctionInterval(__doDamage, extraArgs = [
                toon,
                dmg,
                died]))])
    else:
        splicedAnims = getSplicedAnims(splicedDamageAnims, actor = toon)
        firstAnim = splicedAnims[0]
        remainingAnims = splicedAnims[1:]
        toonIvals.append(firstAnim)
        toonIvals.extend(remainingAnims)
        indicatorTrack = Track([
            (delay + showDamageExtraTime, FunctionInterval(__doDamage, extraArgs = [
                toon,
                dmg,
                died]))])
    if died != 0:
        loseIval = ActorInterval(toon, 'lose')
        delay = loseIval.getDuration() * 0.80000000000000004
        shrinkDur = loseIval.getDuration() * 0.20000000000000001
        soundTrack = getSoundTrack('ENC_Lose.mp3', delay = 0.90000000000000002, node = toon)
        toonIvals.append(MultiTrack([
            Track([
                loseIval]),
            Track([
                (delay, LerpScaleInterval(toon, shrinkDur, MovieUtil.PNT3_NEARZERO))]),
            soundTrack]))
        toonIvals.append(FunctionInterval(toon.reparentTo, extraArgs = [
            hidden]))
        toonIvals.append(FunctionInterval(toon.setScale, extraArgs = [
            MovieUtil.PNT3_ONE]))
    else:
        toonIvals.append(FunctionInterval(toon.loop, extraArgs = [
            'neutral']))
    return MultiTrack([
        Track(toonIvals),
        indicatorTrack])


def getSplicedAnims(anims, actor = None):
    ivals = []
    for nextAnim in anims:
        delay = 9.9999999999999995e-007
        if len(nextAnim) >= 2:
            if nextAnim[1] > 0:
                delay = nextAnim[1]
            
        
        if len(nextAnim) <= 0:
            ivals.append(WaitInterval(delay))
        elif len(nextAnim) == 1:
            ivals.append(ActorInterval(actor, nextAnim[0]))
        elif len(nextAnim) == 2:
            ivals.append(WaitInterval(delay))
            ivals.append(ActorInterval(actor, nextAnim[0]))
        elif len(nextAnim) == 3:
            ivals.append(WaitInterval(delay))
            ivals.append(ActorInterval(actor, nextAnim[0], startTime = nextAnim[2]))
        elif len(nextAnim) == 4:
            ivals.append(WaitInterval(delay))
            duration = nextAnim[3]
            if duration < 0:
                startTime = nextAnim[2]
                endTime = startTime + duration
                if endTime <= 0:
                    endTime = 0.01
                
                ivals.append(ActorInterval(actor, nextAnim[0], startTime = startTime, endTime = endTime))
            else:
                ivals.append(ActorInterval(actor, nextAnim[0], startTime = nextAnim[2], duration = duration))
        elif len(nextAnim) == 5:
            ivals.append(WaitInterval(delay))
            ivals.append(ActorInterval(nextAnim[4], nextAnim[0], startTime = nextAnim[2], duration = nextAnim[3]))
        
    
    return ivals


def getSplicedLerpAnims(animName, origDuration, newDuration, startTime = 0, fps = 30, reverse = 0):
    ivals = []
    addition = 0
    numIvals = origDuration * fps
    timeInterval = newDuration / numIvals
    animInterval = origDuration / numIvals
    if reverse == 1:
        animInterval = -animInterval
    
    for i in range(0, numIvals):
        ivals.append([
            animName,
            timeInterval,
            startTime + addition,
            animInterval])
        addition += animInterval
    
    return ivals


def getSoundTrack(fileName, delay = 0.01, duration = None, node = None):
    soundEffect = globalBattleSoundCache.getSound(fileName)
    if duration:
        return Track([
            (delay, SoundInterval(soundEffect, duration = duration, node = node))])
    else:
        return Track([
            (delay, SoundInterval(soundEffect, node = node))])


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
        Point3(-26.559999999999999, 68.200000000000003, -98.129999999999995)]
    tiePropIvals = getPropAppearIntervals(tie, suit.getRightHand(), posPoints, 0.5, MovieUtil.PNT3_ONE, scaleUpTime = 0.5, poseExtraArgs = [
        'clip-on-tie',
        0])
    if dmg > 0:
        tiePropIvals.append(ActorInterval(tie, 'clip-on-tie', duration = throwDelay, startTime = 1.1000000000000001))
    else:
        tiePropIvals.append(WaitInterval(throwDelay))
    tiePropIvals.append(FunctionInterval(tie.setHpr, extraArgs = [
        Point3(0, -90, 0)]))
    tiePropIvals.extend(getPropThrowIntervals(attack, tie, [
        __toonFacePoint(toon)], [
        __toonGroundPoint(attack, toon, 0.10000000000000001)], hitDuration = 0.40000000000000002, missDuration = 0.80000000000000004, missScaleDown = 1.2))
    tiePropTrack = Track(tiePropIvals)
    toonTrack = getToonTrack(attack, damageDelay, [
        'conked'], dodgeDelay, [
        'sidestep'])
    throwSound = getSoundTrack('SA_powertie_throw.mp3', delay = throwDelay + 1, node = suit)
    return MultiTrack([
        suitTrack,
        toonTrack,
        tiePropTrack,
        throwSound])


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
        Point3(-6.0499999999999998, -2.5099999999999998, 177.58000000000001)]
    receiverPosPoints = [
        Point3(0.23000000000000001, 0.17000000000000001, -0.11),
        Point3(-6.0499999999999998, -2.5099999999999998, 177.58000000000001)]
    propTrack = Track([
        WaitInterval(0.29999999999999999),
        FunctionInterval(__showProp, extraArgs = [
            phone,
            suit.getLeftHand(),
            phonePosPoints[0],
            phonePosPoints[1]]),
        FunctionInterval(__showProp, extraArgs = [
            receiver,
            suit.getLeftHand(),
            receiverPosPoints[0],
            receiverPosPoints[1]]),
        LerpScaleInterval(phone, 0.5, MovieUtil.PNT3_ONE, MovieUtil.PNT3_NEARZERO),
        WaitInterval(0.73999999999999999),
        FunctionInterval(receiver.wrtReparentTo, extraArgs = [
            suit.getRightHand()]),
        LerpPosHprInterval(receiver, 0.0001, Point3(-0.45000000000000001, 0.47999999999999998, -0.62), Point3(-82.569999999999993, 71.109999999999999, -89.480000000000004)),
        WaitInterval(3.1400000000000001),
        FunctionInterval(receiver.wrtReparentTo, extraArgs = [
            phone]),
        WaitInterval(0.62),
        LerpScaleInterval(phone, 0.5, MovieUtil.PNT3_NEARZERO),
        FunctionInterval(MovieUtil.removeProps, extraArgs = [
            [
                receiver,
                phone]])])
    toonTrack = getToonTrack(attack, 2.7000000000000002, [
        'cringe'], 1.8999999999999999, [
        'sidestep'])
    soundTrack = getSoundTrack('SA_hangup.mp3', delay = 1.3, node = suit)
    return MultiTrack([
        suitTrack,
        toonTrack,
        propTrack,
        partTrack,
        soundTrack])


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
        Point3(-79.510000000000005, -30.07, 177.44999999999999)]
    paperPropTrack = getPropTrack(paper, suit.getRightHand(), paperPosPoints, 2.3999999999999999, 1.0000000000000001e-005, scaleUpTime = 0.20000000000000001, anim = 1, propName = 'shredder-paper', animDuration = 1.5, animStartTime = 2.7999999999999998)
    shredderPosPoints = [
        Point3(0, -0.12, -0.34000000000000002),
        Point3(-90.0, -48.439999999999998, -5.3300000000000001)]
    shredderPropTrack = getPropTrack(shredder, suit.getLeftHand(), shredderPosPoints, 1, 3, scaleUpPoint = Point3(4.8099999999999996, 4.8099999999999996, 4.8099999999999996))
    toonTrack = getToonTrack(attack, suitTrack.getDuration() - 1.1000000000000001, [
        'conked'], suitTrack.getDuration() - 3.1000000000000001, [
        'sidestep'])
    soundTrack = getSoundTrack('SA_shred.mp3', delay = 3.3999999999999999, node = suit)
    return MultiTrack([
        suitTrack,
        paperPropTrack,
        shredderPropTrack,
        partTrack,
        toonTrack,
        soundTrack])


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
        Point3(-158.75, 7.71, -168.69)]
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
    bodyScale = Toon.toonBodyScales[animal]
    headEffectHeight = __toonFacePoint(toon).getZ()
    legsHeight = Toon.legHeightDict[toon.style.legs] * bodyScale
    torsoEffectHeight = Toon.torsoHeightDict[toon.style.torso] * bodyScale / 2 + legsHeight
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
        ivals = []
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            ivals.append(FunctionInterval(nextPart.setColorScale, extraArgs = [
                Vec4(0, 0, 0, 1)]))
        
        return ivals

    
    def resetParts(parts):
        ivals = []
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            ivals.append(FunctionInterval(nextPart.clearColorScale))
        
        return ivals

    if dmg > 0:
        colorIvals = []
        headParts = toon.getHeadParts()
        torsoParts = toon.getTorsoParts()
        legsParts = toon.getLegsParts()
        colorIvals.append(WaitInterval(partDelay + 0.20000000000000001))
        colorIvals.append(FunctionInterval(battle.movie.needRestoreColor))
        colorIvals.extend(colorParts(headParts))
        colorIvals.append(WaitInterval(partIvalDelay))
        colorIvals.extend(colorParts(torsoParts))
        colorIvals.append(WaitInterval(partIvalDelay))
        colorIvals.extend(colorParts(legsParts))
        colorIvals.append(WaitInterval(2.5))
        colorIvals.extend(resetParts(headParts))
        colorIvals.extend(resetParts(torsoParts))
        colorIvals.extend(resetParts(legsParts))
        colorIvals.append(FunctionInterval(battle.movie.clearRestoreColor))
        colorTrack = Track(colorIvals)
        return MultiTrack([
            suitTrack,
            pencilPropTrack,
            sharpenerPropTrack,
            sprayTrack,
            headTrack,
            torsoTrack,
            legsTrack,
            colorTrack,
            toonTrack])
    else:
        return MultiTrack([
            suitTrack,
            pencilPropTrack,
            sharpenerPropTrack,
            sprayTrack,
            toonTrack])


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
    hitSprayIvals = MovieUtil.getSprayIntervals(battle, VBase4(0, 0, 0, 1), getPenTip, hitPoint, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, horizScale = 0.10000000000000001, vertScale = 0.10000000000000001)
    missSprayIvals = MovieUtil.getSprayIntervals(battle, VBase4(0, 0, 0, 1), getPenTip, missPoint, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, horizScale = 0.10000000000000001, vertScale = 0.10000000000000001)
    suitTrack = getSuitTrack(attack)
    propIvals = [
        WaitInterval(0.01),
        FunctionInterval(__showProp, extraArgs = [
            pen,
            suit.getRightHand(),
            MovieUtil.PNT3_ZERO]),
        LerpScaleInterval(pen, 0.5, Point3(1.5, 1.5, 1.5)),
        WaitInterval(1.05)]
    if dmg > 0:
        propIvals += hitSprayIvals
    else:
        propIvals += missSprayIvals
    propIvals += [
        LerpScaleInterval(pen, 0.5, MovieUtil.PNT3_NEARZERO),
        FunctionInterval(MovieUtil.removeProp, extraArgs = [
            pen])]
    propTrack = Track(propIvals)
    splashTrack = []
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
        splashIvals = [
            FunctionInterval(battle.movie.needRestoreRenderProp, extraArgs = [
                splash]),
            (1.6499999999999999, FunctionInterval(prepSplash, extraArgs = [
                splash,
                __toonFacePoint(toon)])),
            ActorInterval(splash, 'splash-from-splat'),
            FunctionInterval(MovieUtil.removeProp, extraArgs = [
                splash]),
            FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
                splash])]
        headParts = toon.getHeadParts()
        splashIvals.append(FunctionInterval(battle.movie.needRestoreColor))
        for partNum in range(0, headParts.getNumPaths()):
            nextPart = headParts.getPath(partNum)
            splashIvals.append(FunctionInterval(nextPart.setColorScale, extraArgs = [
                Vec4(0, 0, 0, 1)]))
        
        splashIvals.append(FunctionInterval(MovieUtil.removeProp, extraArgs = [
            splash]))
        splashIvals.append(WaitInterval(2.6000000000000001))
        for partNum in range(0, headParts.getNumPaths()):
            nextPart = headParts.getPath(partNum)
            splashIvals.append(FunctionInterval(nextPart.clearColorScale))
        
        splashIvals.append(FunctionInterval(battle.movie.clearRestoreColor))
        splashTrack.append(Track(splashIvals))
    
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
    return MultiTrack([
        suitTrack,
        toonTrack,
        propTrack,
        soundTrack,
        penSpillTrack] + splashTrack)


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
        Point3(-14.93, 2.29, 180.0)]
    padPropTrack = getPropTrack(pad, suit.getLeftHand(), padPosPoints, 0.5, 2.5699999999999998)
    pencilPosPoints = [
        Point3(0.040000000000000001, -0.38, -0.10000000000000001),
        Point3(-172.25, 7.0599999999999996, -63.729999999999997)]
    pencilPropTrack = getPropTrack(pencil, suit.getRightHand(), pencilPosPoints, 0.5, 2.5699999999999998)
    toonTrack = getToonTrack(attack, 2.2000000000000002, [
        'conked'], 2.0, [
        'jump'])
    hideIvals = []
    headParts = toon.getHeadParts()
    torsoParts = toon.getTorsoParts()
    legsParts = toon.getLegsParts()
    animal = toon.style.getAnimal()
    bodyScale = Toon.toonBodyScales[animal]
    headEffectHeight = __toonFacePoint(toon).getZ()
    legsHeight = Toon.legHeightDict[toon.style.legs] * bodyScale
    torsoEffectHeight = Toon.torsoHeightDict[toon.style.torso] * bodyScale / 2 + legsHeight
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
        ivals = []
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            ivals.append(FunctionInterval(nextPart.setTransparency, extraArgs = [
                1]))
            ivals.append(LerpFunctionInterval(nextPart.setAlphaScale, fromData = 1, toData = 0, duration = 0.20000000000000001))
        
        return ivals

    
    def showParts(parts):
        ivals = []
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            ivals.append(FunctionInterval(nextPart.clearColorScale))
            ivals.append(FunctionInterval(nextPart.clearTransparency))
        
        return ivals

    soundTrack = getSoundTrack('SA_rubout.mp3', delay = 1.7, node = suit)
    if dmg > 0:
        hideIvals.append(WaitInterval(2.2000000000000002))
        hideIvals.append(FunctionInterval(battle.movie.needRestoreColor))
        hideIvals.extend(hideParts(headParts))
        hideIvals.append(WaitInterval(0.40000000000000002))
        hideIvals.extend(hideParts(torsoParts))
        hideIvals.append(WaitInterval(0.40000000000000002))
        hideIvals.extend(hideParts(legsParts))
        hideIvals.append(WaitInterval(1))
        hideIvals.extend(showParts(headParts))
        hideIvals.extend(showParts(torsoParts))
        hideIvals.extend(showParts(legsParts))
        hideIvals.append(FunctionInterval(battle.movie.clearRestoreColor))
        hideTrack = Track(hideIvals)
        return MultiTrack([
            suitTrack,
            toonTrack,
            padPropTrack,
            pencilPropTrack,
            soundTrack,
            hideTrack,
            headTrack,
            torsoTrack,
            legsTrack])
    else:
        return MultiTrack([
            suitTrack,
            toonTrack,
            padPropTrack,
            pencilPropTrack,
            soundTrack])


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
        particleEffect.setHpr(90.0, -120, -0.019)
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
    return MultiTrack([
        suitTrack,
        toonTrack,
        partTrack,
        soundTrack])


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
        Point3(19.829999999999998, 3.6400000000000001, 171.12)]
    padPropTrack = getPropTrack(pad, suit.getLeftHand(), padPosPoints, 0.5, 2.5699999999999998, Point3(1.8899999999999999, 1.8899999999999999, 1.8899999999999999))
    
    missPoint = lambda checkmark = checkmark, toon = toon: __toonMissPoint(checkmark, toon)
    pencilPosPoints = [
        Point3(-0.46999999999999997, 1.0800000000000001, 0.28000000000000003),
        Point3(-21.800000000000001, -11.31, 176.19)]
    extraArgsForShowProp = [
        pencil,
        suit.getRightHand()]
    extraArgsForShowProp.extend(pencilPosPoints)
    pencilPropIvals = [
        WaitInterval(0.5),
        FunctionInterval(__showProp, extraArgs = extraArgsForShowProp),
        LerpScaleInterval(pencil, 0.5, Point3(1.5, 1.5, 1.5), startScale = Point3(0.01)),
        WaitInterval(2),
        FunctionInterval(battle.movie.needRestoreRenderProp, extraArgs = [
            checkmark]),
        FunctionInterval(checkmark.reparentTo, extraArgs = [
            render]),
        FunctionInterval(checkmark.setScale, extraArgs = [
            1.6000000000000001]),
        FunctionInterval(checkmark.setPosHpr, extraArgs = [
            pencil,
            0,
            0,
            0,
            0,
            0,
            0]),
        FunctionInterval(checkmark.setP, extraArgs = [
            0]),
        FunctionInterval(checkmark.setR, extraArgs = [
            0])]
    pencilPropIvals.extend(getPropThrowIntervals(attack, checkmark, [
        __toonFacePoint(toon)], [
        missPoint]))
    pencilPropIvals.append(FunctionInterval(MovieUtil.removeProp, extraArgs = [
        checkmark]))
    pencilPropIvals.append(FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
        checkmark]))
    pencilPropIvals.append(WaitInterval(0.29999999999999999))
    pencilPropIvals.append(LerpScaleInterval(pencil, 0.5, MovieUtil.PNT3_NEARZERO))
    pencilPropIvals.append(FunctionInterval(MovieUtil.removeProp, extraArgs = [
        pencil]))
    pencilPropTrack = Track(pencilPropIvals)
    toonTrack = getToonTrack(attack, 3.3999999999999999, [
        'slip-forward'], 2.3999999999999999, [
        'sidestep'])
    soundTrack = Track([
        WaitInterval(2.2999999999999998),
        SoundInterval(globalBattleSoundCache.getSound('SA_writeoff_pen_only.mp3'), duration = 0.90000000000000002, node = suit),
        SoundInterval(globalBattleSoundCache.getSound('SA_writeoff_ding_only.mp3'), node = suit)])
    return MultiTrack([
        suitTrack,
        toonTrack,
        padPropTrack,
        pencilPropTrack,
        soundTrack])


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
            Point3(-6.5800000000000001, -2.8599999999999999, 165.06999999999999)]
        stampPosPoints = [
            Point3(-0.64000000000000001, -0.17000000000000001, -0.029999999999999999),
            MovieUtil.PNT3_ZERO]
    elif suitType == 'c':
        padPosPoints = [
            Point3(0.19, -0.55000000000000004, -0.20999999999999999),
            Point3(-166.65000000000001, -3.6099999999999999, -1.7)]
        stampPosPoints = [
            Point3(-0.64000000000000001, -0.080000000000000002, 0.11),
            MovieUtil.PNT3_ZERO]
    else:
        padPosPoints = [
            Point3(-0.65000000000000002, 0.82999999999999996, -0.040000000000000001),
            Point3(-6.5800000000000001, -2.8599999999999999, 165.06999999999999)]
        stampPosPoints = [
            Point3(-0.64000000000000001, -0.17000000000000001, -0.029999999999999999),
            MovieUtil.PNT3_ZERO]
    padPropTrack = getPropTrack(pad, suit.getLeftHand(), padPosPoints, 9.9999999999999995e-007, 3.2000000000000002)
    
    missPoint = lambda cancelled = cancelled, toon = toon: __toonMissPoint(cancelled, toon)
    propIvals = [
        FunctionInterval(__showProp, extraArgs = [
            stamp,
            suit.getRightHand(),
            stampPosPoints[0],
            stampPosPoints[1]]),
        LerpScaleInterval(stamp, 0.5, MovieUtil.PNT3_ONE),
        WaitInterval(2.6000000000000001),
        FunctionInterval(battle.movie.needRestoreRenderProp, extraArgs = [
            cancelled]),
        FunctionInterval(cancelled.reparentTo, extraArgs = [
            render]),
        FunctionInterval(cancelled.setScale, extraArgs = [
            0.59999999999999998]),
        FunctionInterval(cancelled.setPosHpr, extraArgs = [
            stamp,
            0.81000000000000005,
            -1.1100000000000001,
            -0.16,
            0,
            0,
            270]),
        FunctionInterval(cancelled.setP, extraArgs = [
            0]),
        FunctionInterval(cancelled.setR, extraArgs = [
            0])]
    propIvals.extend(getPropThrowIntervals(attack, cancelled, [
        __toonFacePoint(toon)], [
        missPoint]))
    propIvals.append(FunctionInterval(MovieUtil.removeProp, extraArgs = [
        cancelled]))
    propIvals.append(FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
        cancelled]))
    propIvals.append(WaitInterval(0.29999999999999999))
    propIvals.append(LerpScaleInterval(stamp, 0.5, MovieUtil.PNT3_NEARZERO))
    propIvals.append(FunctionInterval(MovieUtil.removeProp, extraArgs = [
        stamp]))
    propTrack = Track(propIvals)
    toonTrack = getToonTrack(attack, 3.3999999999999999, [
        'conked'], 1.8999999999999999, [
        'sidestep'])
    soundTrack = getSoundTrack('SA_rubber_stamp.mp3', delay = 1.3, duration = 1.1000000000000001, node = suit)
    return MultiTrack([
        suitTrack,
        toonTrack,
        propTrack,
        padPropTrack,
        soundTrack])


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
        Point3(171.09, 85.659999999999997, 14.779999999999999)]
    if hitSuit:
        
        hitPoint = lambda toon = toon: __toonFacePoint(toon)
    else:
        
        hitPoint = lambda particleEffect = particleEffect, toon = toon, suit = suit: __toonMissPoint(particleEffect, toon, parent = suit.getRightHand())
    signPropIvals = [
        WaitInterval(0.5),
        FunctionInterval(__showProp, extraArgs = [
            sign,
            suit.getRightHand(),
            signPosPoints[0],
            signPosPoints[1]]),
        LerpScaleInterval(sign, 0.5, Point3(1.3899999999999999, 1.3899999999999999, 1.3899999999999999)),
        WaitInterval(0.5),
        FunctionInterval(battle.movie.needRestoreParticleEffect, extraArgs = [
            particleEffect]),
        FunctionInterval(particleEffect.start, extraArgs = [
            sign]),
        FunctionInterval(particleEffect.wrtReparentTo, extraArgs = [
            render]),
        LerpPosInterval(particleEffect, 2.0, pos = hitPoint),
        FunctionInterval(particleEffect.cleanup),
        FunctionInterval(battle.movie.clearRestoreParticleEffect, extraArgs = [
            particleEffect])]
    signPropTrack = Track(signPropIvals)
    signPropAnimInterval = [
        ActorInterval(sign, 'smile', duration = 4, startTime = 0)]
    signPropAnimTrack = Track(signPropAnimInterval)
    toonTrack = getToonTrack(attack, 2.6000000000000001, [
        'cringe'], 1.8999999999999999, [
        'sidestep'])
    soundTrack = getSoundTrack('SA_razzle_dazzle.mp3', delay = 1.6000000000000001, node = suit)
    return Track([
        MultiTrack([
            suitTrack,
            signPropTrack,
            signPropAnimTrack,
            toonTrack,
            soundTrack]),
        FunctionInterval(MovieUtil.removeProp, extraArgs = [
            sign])])


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
    synergySoundTrack = Track([
        (0.90000000000000002, SoundInterval(globalBattleSoundCache.getSound('SA_synergy.mp3'), node = suit))])
    if hitAtleastOneToon > 0:
        fallingSoundTrack = Track([
            (damageDelay + 0.5, SoundInterval(globalBattleSoundCache.getSound('Toon_bodyfall_synergy.mp3'), node = suit))])
        return MultiTrack([
            suitTrack,
            partTrack,
            waterfallTrack,
            synergySoundTrack,
            fallingSoundTrack] + toonTracks)
    else:
        return MultiTrack([
            suitTrack,
            partTrack,
            waterfallTrack,
            synergySoundTrack] + toonTracks)


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
        Point3(48.299999999999997, 60.700000000000003, 20.0)]
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
    ballIvals = getPropAppearIntervals(ball, suit, ballPosPoints, 1.7, Point3(1.5, 1.5, 1.5))
    ballIvals.append(FunctionInterval(battle.movie.needRestoreRenderProp, extraArgs = [
        ball]))
    ballIvals.append(FunctionInterval(ball.wrtReparentTo, extraArgs = [
        render]))
    ballIvals.append(WaitInterval(2.1499999999999999))
    
    missPoint = lambda ball = ball, toon = toon: __toonMissPoint(ball, toon)
    ballIvals.extend(getPropThrowIntervals(attack, ball, [
        __toonFacePoint(toon)], [
        missPoint]))
    ballIvals.append(FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
        ball]))
    ballPropTrack = Track(ballIvals)
    dodgeDelay = suitTrack.getDuration() - 4.3499999999999996
    toonTrack = getToonTrack(attack, suitTrack.getDuration() - 2.25, [
        'conked'], dodgeDelay, [
        'duck'], showMissedExtraTime = 1.7)
    soundTrack = getSoundTrack('SA_tee_off.mp3', delay = 4.0999999999999996, node = suit)
    return MultiTrack([
        suitTrack,
        toonTrack,
        clubPropTrack,
        ballPropTrack,
        soundTrack])


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
        Point3(180, 0, 0)]
    cloudIvals = []
    cloudIvals.append(FunctionInterval(cloud.pose, extraArgs = [
        'stormcloud',
        0]))
    cloudIvals.extend(getPropAppearIntervals(cloud, suit, cloudPosPoints, 9.9999999999999995e-007, Point3(3, 3, 3), scaleUpTime = 0.69999999999999996))
    cloudIvals.append(FunctionInterval(battle.movie.needRestoreRenderProp, extraArgs = [
        cloud]))
    cloudIvals.append(FunctionInterval(cloud.wrtReparentTo, extraArgs = [
        render]))
    targetPoint = __toonFacePoint(toon)
    targetPoint.setZ(targetPoint[2] + 3)
    cloudIvals.append(WaitInterval(1.1000000000000001))
    cloudIvals.append(LerpPosInterval(cloud, 1, pos = targetPoint))
    cloudIvals.append(WaitInterval(partDelay))
    pivals = []
    pivals.append(Track([
        ParticleInterval(snowEffect, cloud, worldRelative = 0, duration = 2.2000000000000002)]))
    pivals.append(Track([
        (0.5, ParticleInterval(snowEffect2, cloud, worldRelative = 0, duration = 1.7))]))
    pivals.append(Track([
        (1.0, ParticleInterval(snowEffect3, cloud, worldRelative = 0, duration = 1.2))]))
    pivals.append(Track([
        ActorInterval(cloud, 'stormcloud', startTime = 3, duration = 0.5),
        ActorInterval(cloud, 'stormcloud', startTime = 2.5, duration = 0.5),
        ActorInterval(cloud, 'stormcloud', startTime = 1, duration = 1.5)]))
    cloudIvals.append(MultiTrack(pivals))
    cloudIvals.append(WaitInterval(0.40000000000000002))
    cloudIvals.append(LerpScaleInterval(cloud, 0.5, MovieUtil.PNT3_NEARZERO))
    cloudIvals.append(FunctionInterval(MovieUtil.removeProp, extraArgs = [
        cloud]))
    cloudIvals.append(FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
        cloud]))
    cloudPropTrack = Track(cloudIvals)
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
    return MultiTrack([
        suitTrack,
        toonTrack,
        cloudPropTrack,
        soundTrack])


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
    return MultiTrack([
        suitTrack,
        toonTrack,
        soundTrack] + particleTracks)


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
        return MultiTrack([
            suitTrack,
            toonTrack,
            soundTrack,
            partTrack,
            partTrack2,
            partTrack3])
    else:
        return MultiTrack([
            suitTrack,
            toonTrack,
            soundTrack,
            partTrack])


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
    
    canHpr = Point3(6.3399999999999999, -181.62, -18.02)
    suitTrack = getSuitTrack(attack)
    posPoints = [
        Point3(-0.14000000000000001, 0.14999999999999999, 0.080000000000000002),
        Point3(6.3399999999999999, -14.619999999999999, -198.02000000000001)]
    canIvals = getPropAppearIntervals(can, suit.getRightHand(), posPoints, propDelay, Point3(6, 6, 6), scaleUpTime = 0.5)
    propDelay = propDelay + 0.5
    canIvals.append(WaitInterval(suitDelay))
    hitPoint = toon.getPos(battle)
    hitPoint.setX(hitPoint.getX() + 1.1000000000000001)
    hitPoint.setY(hitPoint.getY() - 0.5)
    hitPoint.setZ(hitPoint.getZ() + toon.height + 1.1000000000000001)
    canIvals.append(FunctionInterval(battle.movie.needRestoreRenderProp, extraArgs = [
        can]))
    canIvals.extend(getThrowIvals(can, hitPoint, duration = throwDuration, parent = battle))
    if dmg > 0:
        can2 = MovieUtil.copyProp(can)
        hips1 = hips.getPath(2)
        hips2 = hips.getPath(1)
        can2Point = Point3(hitPoint.getX(), hitPoint.getY() + 6.4000000000000004, hitPoint.getZ())
        can2.setPos(can2Point)
        can2.setScale(scaleUpPoint)
        can2.setHpr(canHpr)
        canIvals.append(FunctionInterval(battle.movie.needRestoreHips))
        canIvals.append(FunctionInterval(can.wrtReparentTo, extraArgs = [
            hips1]))
        canIvals.append(FunctionInterval(can2.reparentTo, extraArgs = [
            hips2]))
        canIvals.append(WaitInterval(2.3999999999999999))
        canIvals.append(FunctionInterval(MovieUtil.removeProp, extraArgs = [
            can2]))
        canIvals.append(FunctionInterval(battle.movie.clearRestoreHips))
        scaleTrack = Track([
            WaitInterval(propDelay + suitDelay),
            LerpScaleInterval(can, throwDuration, scaleUpPoint)])
        hprTrack = Track([
            WaitInterval(propDelay + suitDelay),
            LerpHprInterval(can, throwDuration, canHpr)])
        soundTrack = Track([
            WaitInterval(2.6000000000000001),
            SoundInterval(globalBattleSoundCache.getSound('SA_canned_tossup_only.mp3'), node = suit),
            SoundInterval(globalBattleSoundCache.getSound('SA_canned_impact_only.mp3'), node = suit)])
    else:
        land = toon.getPos(battle)
        land.setZ(land.getZ() + 0.69999999999999996)
        bouncePoint1 = Point3(land.getX(), land.getY() - 1.5, land.getZ() + 2.5)
        bouncePoint2 = Point3(land.getX(), land.getY() - 2.1000000000000001, land.getZ() - 0.20000000000000001)
        bouncePoint3 = Point3(land.getX(), land.getY() - 3.1000000000000001, land.getZ() + 1.5)
        bouncePoint4 = Point3(land.getX(), land.getY() - 4.0999999999999996, land.getZ() + 0.29999999999999999)
        canIvals.append(LerpPosInterval(can, 0.40000000000000002, land))
        canIvals.append(LerpPosInterval(can, 0.40000000000000002, bouncePoint1))
        canIvals.append(LerpPosInterval(can, 0.29999999999999999, bouncePoint2))
        canIvals.append(LerpPosInterval(can, 0.29999999999999999, bouncePoint3))
        canIvals.append(LerpPosInterval(can, 0.29999999999999999, bouncePoint4))
        canIvals.append(WaitInterval(1.1000000000000001))
        canIvals.append(LerpScaleInterval(can, 0.29999999999999999, MovieUtil.PNT3_NEARZERO))
        scaleTrack = Track([
            WaitInterval(propDelay + suitDelay),
            LerpScaleInterval(can, throwDuration, Point3(11, 11, 11))])
        hprTrack = Track([
            WaitInterval(propDelay + suitDelay),
            LerpHprInterval(can, throwDuration, canHpr),
            WaitInterval(0.40000000000000002),
            LerpHprInterval(can, 0.40000000000000002, Point3(-96.340000000000003, -181.62, -18.02)),
            LerpHprInterval(can, 0.29999999999999999, Point3(6.3399999999999999, -91.620000000000005, -18.02)),
            LerpHprInterval(can, 0.20000000000000001, Point3(96.340000000000003, 1.6200000000000001, -181.02000000000001))])
        soundTrack = getSoundTrack('SA_canned_tossup_only.mp3', delay = 2.6000000000000001, node = suit)
    throwTrack = Track(canIvals)
    canTrack = Track([
        MultiTrack([
            throwTrack,
            scaleTrack,
            hprTrack]),
        FunctionInterval(MovieUtil.removeProp, extraArgs = [
            can]),
        FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
            can])])
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
    return MultiTrack([
        suitTrack,
        toonTrack,
        canTrack,
        soundTrack])


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
        shrinkTrack = Track([
            WaitInterval(damageDelay + 0.5),
            FunctionInterval(battle.movie.needRestoreToonScale),
            LerpScaleInterval(toon, 1.0, downScale * 1.1000000000000001),
            LerpScaleInterval(toon, 0.10000000000000001, downScale * 0.90000000000000002),
            LerpScaleInterval(toon, 0.10000000000000001, downScale * 1.05),
            LerpScaleInterval(toon, 0.10000000000000001, downScale * 0.94999999999999996),
            LerpScaleInterval(toon, 0.10000000000000001, downScale),
            WaitInterval(2.1000000000000001),
            LerpScaleInterval(toon, 0.5, initialScale * 1.5),
            LerpScaleInterval(toon, 0.14999999999999999, initialScale * 0.5),
            LerpScaleInterval(toon, 0.14999999999999999, initialScale * 1.2),
            LerpScaleInterval(toon, 0.14999999999999999, initialScale * 0.80000000000000004),
            LerpScaleInterval(toon, 0.14999999999999999, initialScale),
            FunctionInterval(battle.movie.clearRestoreToonScale)])
    
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
        return MultiTrack([
            suitTrack,
            sprayTrack,
            cloudTrack,
            shrinkTrack,
            toonTrack])
    else:
        return MultiTrack([
            suitTrack,
            sprayTrack,
            toonTrack])


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
        Point3(-153.43000000000001, 8.4299999999999997, -93.010000000000005)]
    paperIvals = getPropAppearIntervals(paper, suit.getRightHand(), posPoints, 0.80000000000000004, Point3(8, 8, 8), scaleUpTime = 0.5)
    paperIvals.append(WaitInterval(1.73))
    hitPoint = __toonGroundPoint(attack, toon, 0.20000000000000001, parent = battle)
    paperIvals.append(FunctionInterval(battle.movie.needRestoreRenderProp, extraArgs = [
        paper]))
    paperIvals.append(FunctionInterval(paper.wrtReparentTo, extraArgs = [
        battle]))
    paperIvals.append(LerpPosInterval(paper, throwDuration, hitPoint))
    if dmg > 0:
        paperPause = 0.01
        slidePoint = Point3(hitPoint.getX(), hitPoint.getY() - 5, hitPoint.getZ() + 4)
        landPoint = Point3(hitPoint.getX(), hitPoint.getY() - 5, hitPoint.getZ())
        paperIvals.append(WaitInterval(paperPause))
        paperIvals.append(LerpPosInterval(paper, 0.20000000000000001, slidePoint))
        paperIvals.append(LerpPosInterval(paper, 1.1000000000000001, landPoint))
        paperAppearTrack = Track(paperIvals)
        paperSpinTrack = Track([
            WaitInterval(throwDelay),
            LerpHprInterval(paper, throwDuration, Point3(300, 0, 0)),
            WaitInterval(paperPause),
            LerpHprInterval(paper, 1.3, Point3(-200, 100, 100))])
    else:
        slidePoint = Point3(hitPoint.getX(), hitPoint.getY() - 5, hitPoint.getZ())
        paperIvals.append(LerpPosInterval(paper, 0.5, slidePoint))
        paperAppearTrack = Track(paperIvals)
        paperSpinTrack = Track([
            WaitInterval(throwDelay),
            LerpHprInterval(paper, throwDuration, Point3(300, 0, 0)),
            LerpHprInterval(paper, 0.5, Point3(10, 0, 0))])
    propIvals = []
    propIvals.append(MultiTrack([
        paperAppearTrack,
        paperSpinTrack]))
    propIvals.append(LerpScaleInterval(paper, 0.40000000000000002, MovieUtil.PNT3_NEARZERO))
    propIvals.append(FunctionInterval(MovieUtil.removeProp, extraArgs = [
        paper]))
    propIvals.append(FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
        paper]))
    propTrack = Track(propIvals)
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
    return MultiTrack([
        suitTrack,
        toonTrack,
        propTrack,
        soundTrack])


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
        headTracks = []
        for partNum in range(0, headParts.getNumPaths()):
            part = headParts.getPath(partNum)
            x = part.getX()
            y = part.getY()
            z = part.getZ()
            h = part.getH()
            p = part.getP()
            r = part.getR()
            headTracks.append(Track([
                WaitInterval(attackDelay),
                LerpPosInterval(part, 0.10000000000000001, Point3(x - 0.20000000000000001, y, z - 0.029999999999999999)),
                LerpPosInterval(part, 0.10000000000000001, Point3(x + 0.40000000000000002, y, z - 0.029999999999999999)),
                LerpPosInterval(part, 0.10000000000000001, Point3(x - 0.40000000000000002, y, z - 0.029999999999999999)),
                LerpPosInterval(part, 0.10000000000000001, Point3(x + 0.40000000000000002, y, z - 0.029999999999999999)),
                LerpPosInterval(part, 0.10000000000000001, Point3(x - 0.20000000000000001, y, z - 0.040000000000000001)),
                LerpPosInterval(part, 0.25, Point3(x, y, z + 2.2000000000000002)),
                LerpHprInterval(part, 0.40000000000000002, Point3(360, 0, 180)),
                LerpPosInterval(part, 0.29999999999999999, Point3(x, y, z + 3.1000000000000001)),
                LerpPosInterval(part, 0.14999999999999999, Point3(x, y, z + 0.29999999999999999)),
                WaitInterval(0.14999999999999999),
                LerpHprInterval(part, 0.59999999999999998, Point3(-745, 0, 180), startHpr = Point3(0, 0, 180)),
                LerpHprInterval(part, 0.80000000000000004, Point3(25, 0, 180), startHpr = Point3(0, 0, 180)),
                LerpPosInterval(part, 0.14999999999999999, Point3(x, y, z + 1)),
                LerpHprInterval(part, 0.29999999999999999, Point3(h, p, r)),
                WaitInterval(0.20000000000000001),
                LerpPosInterval(part, 0.10000000000000001, Point3(x, y, z)),
                WaitInterval(0.90000000000000002)]))
        
        
        def getChestTrack(part, attackDelay = attackDelay):
            origScale = part.getScale()
            return Track([
                WaitInterval(attackDelay),
                LerpHprInterval(part, 1.1000000000000001, Point3(180, 0, 0)),
                WaitInterval(1.1000000000000001),
                LerpHprInterval(part, 1.1000000000000001, part.getHpr())])

        chestTracks = []
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
        return MultiTrack([
            suitTrack,
            partTrack,
            toonTrack] + headTracks + chestTracks)
    else:
        return MultiTrack([
            suitTrack,
            partTrack,
            toonTrack])


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
    sackHpr = Point3(26.34, -181.62, -18.02)
    suitTrack = getSuitTrack(attack)
    posPoints = [
        Point3(0.51000000000000001, -2.0299999999999998, -0.72999999999999998),
        Point3(12.27, -90.0, -65.019999999999996)]
    sackIvals = getPropAppearIntervals(sack, suit.getRightHand(), posPoints, propDelay, initialScale, scaleUpTime = 0.20000000000000001)
    propDelay = propDelay + 0.20000000000000001
    sackIvals.append(WaitInterval(suitDelay))
    hitPoint = toon.getPos(battle)
    if dmg > 0:
        hitPoint.setX(hitPoint.getX() + 2.1000000000000001)
        hitPoint.setY(hitPoint.getY() + 0.90000000000000002)
        hitPoint.setZ(hitPoint.getZ() + toon.height + 1.2)
    else:
        hitPoint.setZ(hitPoint.getZ() - 0.20000000000000001)
    sackIvals.append(FunctionInterval(battle.movie.needRestoreRenderProp, extraArgs = [
        sack]))
    sackIvals.extend(getThrowIvals(sack, hitPoint, duration = throwDuration, parent = battle))
    if dmg > 0:
        sack2 = MovieUtil.copyProp(sack)
        hips1 = hips.getPath(2)
        hips2 = hips.getPath(1)
        sack2.hide()
        sack2.reparentTo(battle)
        sack2.setPos(Point3(hitPoint.getX(), hitPoint.getY(), hitPoint.getZ()))
        sack2.setScale(scaleUpPoint)
        sack2.setHpr(sackHpr)
        sackIvals.append(FunctionInterval(battle.movie.needRestoreHips))
        sackIvals.append(FunctionInterval(sack.wrtReparentTo, extraArgs = [
            hips1]))
        sackIvals.append(FunctionInterval(sack2.show))
        sackIvals.append(FunctionInterval(sack2.wrtReparentTo, extraArgs = [
            hips2]))
        sackIvals.append(WaitInterval(2.3999999999999999))
        sackIvals.append(FunctionInterval(MovieUtil.removeProp, extraArgs = [
            sack2]))
        sackIvals.append(FunctionInterval(battle.movie.clearRestoreHips))
        scaleTrack = Track([
            WaitInterval(propDelay + suitDelay),
            LerpScaleInterval(sack, throwDuration, scaleUpPoint),
            WaitInterval(1.8),
            LerpScaleInterval(sack, 0.29999999999999999, MovieUtil.PNT3_NEARZERO)])
        hprTrack = Track([
            WaitInterval(propDelay + suitDelay),
            LerpHprInterval(sack, throwDuration, sackHpr)])
        sackTrack = Track([
            MultiTrack([
                Track(sackIvals),
                scaleTrack,
                hprTrack]),
            FunctionInterval(MovieUtil.removeProp, extraArgs = [
                sack]),
            FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
                sack])])
    else:
        sackIvals.append(WaitInterval(1.1000000000000001))
        sackIvals.append(LerpScaleInterval(sack, 0.29999999999999999, MovieUtil.PNT3_NEARZERO))
        sackTrack = Track([
            Track(sackIvals),
            FunctionInterval(MovieUtil.removeProp, extraArgs = [
                sack]),
            FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
                sack])])
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
    return MultiTrack([
        suitTrack,
        toonTrack,
        sackTrack])


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
    leftKnifeTracks = []
    rightKnifeTracks = []
    for i in range(0, 3):
        knifeDelay = 0.11
        leftIvals = []
        leftIvals.append(WaitInterval(1.1000000000000001))
        leftIvals.append(WaitInterval(i * knifeDelay))
        leftIvals.extend(getPropAppearIntervals(leftKnives[i], suit, leftPosPoints, 9.9999999999999995e-007, Point3(0.40000000000000002, 0.40000000000000002, 0.40000000000000002), scaleUpTime = 0.10000000000000001))
        leftIvals.extend(getPropThrowIntervals(attack, leftKnives[i], hitPointNames = [
            'face'], missPointNames = [
            'miss'], hitDuration = 0.29999999999999999, missDuration = 0.29999999999999999))
        leftKnifeTracks.append(Track(leftIvals))
        rightIvals = []
        rightIvals.append(WaitInterval(1.1000000000000001))
        rightIvals.append(WaitInterval(i * knifeDelay))
        rightIvals.extend(getPropAppearIntervals(rightKnives[i], suit, rightPosPoints, 9.9999999999999995e-007, Point3(0.40000000000000002, 0.40000000000000002, 0.40000000000000002), scaleUpTime = 0.10000000000000001))
        rightIvals.extend(getPropThrowIntervals(attack, rightKnives[i], hitPointNames = [
            'face'], missPointNames = [
            'miss'], hitDuration = 0.29999999999999999, missDuration = 0.29999999999999999))
        rightKnifeTracks.append(Track(rightIvals))
    
    damageAnims = [
        [
            'slip-backward',
            0.01,
            0.34999999999999998]]
    toonTrack = getToonTrack(attack, damageDelay = 1.6000000000000001, splicedDamageAnims = damageAnims, dodgeDelay = 0.69999999999999996, dodgeAnimNames = [
        'sidestep'])
    soundTrack = getSoundTrack('SA_glower_power.mp3', delay = 1.1000000000000001, node = suit)
    return MultiTrack([
        suitTrack,
        toonTrack,
        soundTrack] + leftKnifeTracks + rightKnifeTracks)


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
        Point3(-161.56, -80.540000000000006, -90.0)]
    tiePropIvals = getPropAppearIntervals(tie, suit.getRightHand(), posPoints, 0.5, Point3(7, 7, 7), scaleUpTime = 0.5)
    tiePropIvals.append(WaitInterval(throwDelay))
    missPoint = __toonMissBehindPoint(toon, parent = battle)
    missPoint.setX(missPoint.getX() - 1.1000000000000001)
    missPoint.setZ(missPoint.getZ() + 4)
    hitPoint = __toonFacePoint(toon, parent = battle)
    hitPoint.setX(hitPoint.getX() - 1.1000000000000001)
    hitPoint.setY(hitPoint.getY() - 0.69999999999999996)
    hitPoint.setZ(hitPoint.getZ() + 0.90000000000000002)
    tiePropIvals.extend(getPropThrowIntervals(attack, tie, [
        hitPoint], [
        missPoint], hitDuration = 0.40000000000000002, missDuration = 0.80000000000000004, missScaleDown = 0.29999999999999999, parent = battle))
    tiePropTrack = Track(tiePropIvals)
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
    return MultiTrack([
        suitTrack,
        toonTrack,
        tiePropTrack])


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
    circleIvals = []
    for point in cloudPoints:
        circleIvals.append(LerpPosInterval(shrinkCloud, 0.14000000000000001, point, other = battle))
    
    cloudIvals = []
    cloudIvals.append(WaitInterval(1.4199999999999999))
    cloudIvals.append(FunctionInterval(battle.movie.needRestoreParticleEffect, extraArgs = [
        shrinkCloud]))
    cloudIvals.append(FunctionInterval(shrinkCloud.start, extraArgs = [
        battle]))
    cloudIvals.extend(circleIvals)
    cloudIvals.extend(circleIvals)
    cloudIvals.append(LerpFunctionInterval(shrinkCloud.setAlphaScale, fromData = 1, toData = 0, duration = 0.69999999999999996))
    cloudIvals.append(FunctionInterval(shrinkCloud.cleanup))
    cloudIvals.append(FunctionInterval(battle.movie.clearRestoreParticleEffect, extraArgs = [
        shrinkCloud]))
    cloudTrack = Track(cloudIvals)
    shrinkDelay = 0.80000000000000004
    shrinkDuration = 1.1000000000000001
    shrinkIvals = []
    if dmg > 0:
        headParts = toon.getHeadParts()
        initialScale = headParts.getPath(0).getScale()[0]
        shrinkIvals.append(WaitInterval(damageDelay + shrinkDelay))
        headTracks = []
        
        def scaleHeadMultiTrack(scale, duration, headParts = headParts):
            headTracks = []
            for partNum in range(0, headParts.getNumPaths()):
                nextPart = headParts.getPath(partNum)
                headTracks.append(Track([
                    LerpScaleInterval(nextPart, duration, Point3(scale, scale, scale))]))
            
            return MultiTrack(headTracks)

        shrinkIvals.append(FunctionInterval(battle.movie.needRestoreHeadScale))
        shrinkIvals.append(scaleHeadMultiTrack(0.59999999999999998, shrinkDuration))
        shrinkIvals.append(WaitInterval(1.6000000000000001))
        shrinkIvals.append(scaleHeadMultiTrack(initialScale * 3.2000000000000002, 0.40000000000000002))
        shrinkIvals.append(scaleHeadMultiTrack(initialScale * 0.69999999999999996, 0.40000000000000002))
        shrinkIvals.append(scaleHeadMultiTrack(initialScale * 2.5, 0.29999999999999999))
        shrinkIvals.append(scaleHeadMultiTrack(initialScale * 0.80000000000000004, 0.29999999999999999))
        shrinkIvals.append(scaleHeadMultiTrack(initialScale * 1.8999999999999999, 0.20000000000000001))
        shrinkIvals.append(scaleHeadMultiTrack(initialScale * 0.84999999999999998, 0.20000000000000001))
        shrinkIvals.append(scaleHeadMultiTrack(initialScale * 1.7, 0.14999999999999999))
        shrinkIvals.append(scaleHeadMultiTrack(initialScale * 0.90000000000000002, 0.14999999999999999))
        shrinkIvals.append(scaleHeadMultiTrack(initialScale * 1.3, 0.10000000000000001))
        shrinkIvals.append(scaleHeadMultiTrack(initialScale, 0.10000000000000001))
        shrinkIvals.append(FunctionInterval(battle.movie.clearRestoreHeadScale))
        shrinkIvals.append(WaitInterval(0.69999999999999996))
        shrinkTrack = Track(shrinkIvals)
    
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
        soundTrack = Track([
            WaitInterval(2.1000000000000001),
            SoundInterval(shrinkSound, duration = 2.1000000000000001, node = suit),
            WaitInterval(1.6000000000000001),
            SoundInterval(growSound, node = suit)])
        return MultiTrack([
            suitTrack,
            sprayTrack,
            cloudTrack,
            dropTrack,
            toonTrack,
            shrinkTrack,
            soundTrack])
    else:
        return MultiTrack([
            suitTrack,
            sprayTrack,
            cloudTrack,
            dropTrack,
            toonTrack])


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
            Point3(-87.75, -81.640000000000001, -100.52)]
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
            Point3(-99.049999999999997, -6.9800000000000004, -178.97999999999999)]
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
            Point3(-87.75, -81.640000000000001, -100.52)]
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
    return MultiTrack([
        suitTrack,
        toonTrack,
        propTrack,
        soundTrack,
        partTrack2,
        partTrack3])


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
            Point3(205, -20, 0)]
    elif suitName == 'tf':
        posPoints = [
            Point3(-0.40000000000000002, 3.6499999999999999, 5.0099999999999998),
            Point3(205, -20, 0)]
    elif suitName == 'le':
        posPoints = [
            Point3(-0.64000000000000001, 4.4500000000000002, 5.9100000000000001),
            Point3(205, -20, 0)]
    else:
        posPoints = [
            Point3(-0.40000000000000002, 3.6499999999999999, 5.0099999999999998),
            Point3(205, -20, 0)]
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
    eyeAppearTrack = Track([
        WaitInterval(suitHoldStart),
        FunctionInterval(__showProp, extraArgs = [
            eye,
            suit,
            posPoints[0],
            posPoints[1]]),
        LerpScaleInterval(eye, suitHoldDuration, Point3(11, 11, 11)),
        WaitInterval(eyeHoldDuration * 0.29999999999999999),
        LerpHprInterval(eye, 0.02, Point3(205, 40, 0)),
        WaitInterval(eyeHoldDuration * 0.69999999999999996),
        FunctionInterval(battle.movie.needRestoreRenderProp, extraArgs = [
            eye]),
        FunctionInterval(eye.wrtReparentTo, extraArgs = [
            battle])])
    toonFace = __toonFacePoint(toon, parent = battle)
    if dmg > 0:
        lerpInterval = LerpPosInterval(eye, moveDuration, toonFace)
    else:
        lerpInterval = LerpPosInterval(eye, moveDuration, Point3(toonFace.getX(), toonFace.getY() - 5, toonFace.getZ() - 2))
    eyeMoveTrack = Track([
        lerpInterval])
    eyeRollTrack = Track([
        LerpHprInterval(eye, moveDuration, Point3(0, 0, 180))])
    eyePropTrack = Track([
        eyeAppearTrack,
        MultiTrack([
            eyeMoveTrack,
            eyeRollTrack]),
        FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
            eye]),
        FunctionInterval(MovieUtil.removeProp, extraArgs = [
            eye])])
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
    return MultiTrack([
        suitTrack,
        toonTrack,
        eyePropTrack,
        soundTrack])


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
        Point3(-77.469999999999999, 74.049999999999997, 15.52)]
    ballIvals = getPropAppearIntervals(ball, suit.getRightHand(), ballPosPoints, 0.80000000000000004, Point3(5, 5, 5), scaleUpTime = 0.5)
    ballIvals.append(WaitInterval(suitDelay))
    ballIvals.append(FunctionInterval(battle.movie.needRestoreRenderProp, extraArgs = [
        ball]))
    ballIvals.append(FunctionInterval(ball.wrtReparentTo, extraArgs = [
        battle]))
    toonPos = toon.getPos(battle)
    x = toonPos.getX()
    y = toonPos.getY()
    z = toonPos.getZ()
    z = z + 0.20000000000000001
    if dmg > 0:
        ballIvals.append(LerpPosInterval(ball, 0.5, __toonFacePoint(toon, parent = battle)))
        ballIvals.append(LerpPosInterval(ball, 0.5, Point3(x, y + 3, z)))
        ballIvals.append(LerpPosInterval(ball, 0.40000000000000002, Point3(x, y + 5, z + 2)))
        ballIvals.append(LerpPosInterval(ball, 0.29999999999999999, Point3(x, y + 6, z)))
        ballIvals.append(LerpPosInterval(ball, 0.10000000000000001, Point3(x, y + 7, z + 1)))
        ballIvals.append(LerpPosInterval(ball, 0.10000000000000001, Point3(x, y + 8, z)))
        ballIvals.append(LerpPosInterval(ball, 0.10000000000000001, Point3(x, y + 8.5, z + 0.59999999999999998)))
        ballIvals.append(LerpPosInterval(ball, 0.10000000000000001, Point3(x, y + 9, z + 0.20000000000000001)))
        ballIvals.append(WaitInterval(0.40000000000000002))
        soundTrack = getSoundTrack('SA_hardball_impact_only.mp3', delay = 2.7999999999999998, node = suit)
    else:
        ballIvals.append(LerpPosInterval(ball, 0.5, Point3(x, y + 2, z)))
        ballIvals.append(LerpPosInterval(ball, 0.40000000000000002, Point3(x, y - 1, z + 2)))
        ballIvals.append(LerpPosInterval(ball, 0.29999999999999999, Point3(x, y - 3, z)))
        ballIvals.append(LerpPosInterval(ball, 0.10000000000000001, Point3(x, y - 4, z + 1)))
        ballIvals.append(LerpPosInterval(ball, 0.10000000000000001, Point3(x, y - 5, z)))
        ballIvals.append(LerpPosInterval(ball, 0.10000000000000001, Point3(x, y - 5.5, z + 0.59999999999999998)))
        ballIvals.append(LerpPosInterval(ball, 0.10000000000000001, Point3(x, y - 6, z + 0.20000000000000001)))
        ballIvals.append(WaitInterval(0.40000000000000002))
        soundTrack = getSoundTrack('SA_hardball.mp3', delay = 3.1000000000000001, node = suit)
    ballIvals.append(LerpScaleInterval(ball, 0.29999999999999999, MovieUtil.PNT3_NEARZERO))
    ballIvals.append(FunctionInterval(MovieUtil.removeProp, extraArgs = [
        ball]))
    ballIvals.append(FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
        ball]))
    propTrack = Track(ballIvals)
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
    return MultiTrack([
        suitTrack,
        toonTrack,
        propTrack,
        soundTrack])


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
        Point3(-172.41, -4.0899999999999999, -163.30000000000001)]
    tiePropIvals = getPropAppearIntervals(tie, suit.getRightHand(), posPoints, 0.5, Point3(3.5, 3.5, 3.5), scaleUpTime = 0.5)
    tiePropIvals.append(WaitInterval(throwDelay))
    tiePropIvals.append(FunctionInterval(tie.setBillboardPointEye))
    tiePropIvals.extend(getPropThrowIntervals(attack, tie, [
        __toonFacePoint(toon)], [
        __toonGroundPoint(attack, toon, 0.10000000000000001)], hitDuration = 0.40000000000000002, missDuration = 0.80000000000000004))
    tiePropTrack = Track(tiePropIvals)
    toonTrack = getToonTrack(attack, damageDelay, [
        'conked'], dodgeDelay, [
        'sidestep'])
    throwSound = getSoundTrack('SA_powertie_throw.mp3', delay = 2.2999999999999998, node = suit)
    if dmg > 0:
        hitSound = getSoundTrack('SA_powertie_impact.mp3', delay = 2.8999999999999999, node = suit)
        return MultiTrack([
            suitTrack,
            toonTrack,
            tiePropTrack,
            throwSound,
            hitSound])
    else:
        return MultiTrack([
            suitTrack,
            toonTrack,
            tiePropTrack,
            throwSound])


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
    return MultiTrack([
        suitTrack,
        toonTrack,
        partTrack,
        partTrack2,
        soundTrack])


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
    cloudIvals = []
    cloudIvals.append(FunctionInterval(cloud.pose, extraArgs = [
        'stormcloud',
        0]))
    cloudIvals.extend(getPropAppearIntervals(cloud, suit, cloudPosPoints, 9.9999999999999995e-007, Point3(3, 3, 3), scaleUpTime = 0.69999999999999996))
    cloudIvals.append(FunctionInterval(battle.movie.needRestoreRenderProp, extraArgs = [
        cloud]))
    cloudIvals.append(FunctionInterval(cloud.wrtReparentTo, extraArgs = [
        render]))
    targetPoint = __toonFacePoint(toon)
    targetPoint.setZ(targetPoint[2] + 3)
    cloudIvals.append(WaitInterval(1.1000000000000001))
    cloudIvals.append(LerpPosInterval(cloud, 1, pos = targetPoint))
    cloudIvals.append(WaitInterval(partDelay))
    cloudIvals.append(ParticleInterval(snowEffect, cloud, worldRelative = 0, duration = 2.1000000000000001))
    cloudIvals.append(WaitInterval(0.40000000000000002))
    cloudIvals.append(LerpScaleInterval(cloud, 0.5, MovieUtil.PNT3_NEARZERO))
    cloudIvals.append(FunctionInterval(MovieUtil.removeProp, extraArgs = [
        cloud]))
    cloudIvals.append(FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
        cloud]))
    cloudPropTrack = Track(cloudIvals)
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
    return MultiTrack([
        suitTrack,
        toonTrack,
        cloudPropTrack])


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
        ivals = []
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            ivals.append(FunctionInterval(nextPart.setColorScale, extraArgs = [
                Vec4(0, 0, 0, 1)]))
        
        return ivals

    
    def resetColor(parts):
        ivals = []
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            ivals.append(FunctionInterval(nextPart.clearColorScale))
        
        return ivals

    if dmg > 0:
        headParts = toon.getHeadParts()
        torsoParts = toon.getTorsoParts()
        legsParts = toon.getLegsParts()
        colorIvals = []
        colorIvals.append(WaitInterval(4.0))
        colorIvals.append(FunctionInterval(battle.movie.needRestoreColor))
        colorIvals.extend(changeColor(headParts))
        colorIvals.extend(changeColor(torsoParts))
        colorIvals.extend(changeColor(legsParts))
        colorIvals.append(WaitInterval(3.5))
        colorIvals.extend(resetColor(headParts))
        colorIvals.extend(resetColor(torsoParts))
        colorIvals.extend(resetColor(legsParts))
        colorIvals.append(FunctionInterval(battle.movie.clearRestoreColor))
        colorTrack = Track(colorIvals)
    
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
        return MultiTrack([
            suitTrack,
            toonTrack,
            sprayTrack,
            soundTrack,
            baseFlameTrack,
            flameTrack,
            flecksTrack,
            colorTrack])
    else:
        return MultiTrack([
            suitTrack,
            toonTrack,
            sprayTrack,
            soundTrack])


def doPickPocket(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    dmg = target['hp']
    bill = globalPropPool.getProp('1dollar')
    suitTrack = getSuitTrack(attack)
    billPosPoints = [
        Point3(-0.01, 0.45000000000000001, -0.25),
        Point3(-122.41, -21.32, -98.439999999999998)]
    billPropTrack = getPropTrack(bill, suit.getRightHand(), billPosPoints, 0.59999999999999998, 0.55000000000000004, scaleUpPoint = Point3(1.4099999999999999, 1.4099999999999999, 1.4099999999999999))
    toonTrack = getToonTrack(attack, 0.59999999999999998, [
        'cringe'], 0.01, [
        'sidestep'])
    multiTrackList = [
        suitTrack,
        toonTrack]
    if dmg > 0:
        soundTrack = getSoundTrack('SA_pick_pocket.mp3', delay = 0.20000000000000001, node = suit)
        multiTrackList.append(billPropTrack)
        multiTrackList.append(soundTrack)
    
    return MultiTrack(multiTrackList)


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
        return MultiTrack([
            suitTrack,
            toonTrack,
            soundTrack,
            sprayTrack,
            sprayTrack2,
            sprayTrack3,
            sprayTrack4])
    else:
        return MultiTrack([
            suitTrack,
            toonTrack,
            soundTrack,
            sprayTrack,
            sprayTrack2,
            sprayTrack3])


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
    upperPartTracks = []
    lowerPartTracks = []
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
    return MultiTrack([
        suitTrack,
        toonTrack] + upperPartTracks + lowerPartTracks)


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
    return MultiTrack([
        suitTrack] + toonTracks)


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
    return MultiTrack([
        suitTrack] + toonTracks)


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
    return MultiTrack([
        suitTrack,
        soundTrack] + toonTracks)


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
            Point3(-6.0499999999999998, -2.5099999999999998, 177.58000000000001)]
        receiverPosPoints = [
            Point3(-0.13, -0.070000000000000007, -0.059999999999999998),
            Point3(1.75, -2.5099999999999998, 177.58000000000001)]
        receiverAdjustScale = Point3(0.80000000000000004, 0.80000000000000004, 0.80000000000000004)
        pickupDelay = 0.44
        dialDuration = 3.0699999999999998
        finalPhoneDelay = 0.01
        scaleUpPoint = Point3(0.75, 0.75, 0.75)
    else:
        phonePosPoints = [
            Point3(0.23000000000000001, 0.17000000000000001, -0.11),
            Point3(-6.0499999999999998, -2.5099999999999998, 177.58000000000001)]
        receiverPosPoints = [
            Point3(0.23000000000000001, 0.17000000000000001, -0.11),
            Point3(-6.0499999999999998, -2.5099999999999998, 177.58000000000001)]
        receiverAdjustScale = MovieUtil.PNT3_ONE
        pickupDelay = 0.73999999999999999
        dialDuration = 3.0699999999999998
        finalPhoneDelay = 0.68999999999999995
        scaleUpPoint = MovieUtil.PNT3_ONE
    propTrack = Track([
        WaitInterval(0.29999999999999999),
        FunctionInterval(__showProp, extraArgs = [
            phone,
            suit.getLeftHand(),
            phonePosPoints[0],
            phonePosPoints[1]]),
        FunctionInterval(__showProp, extraArgs = [
            receiver,
            suit.getLeftHand(),
            receiverPosPoints[0],
            receiverPosPoints[1]]),
        LerpScaleInterval(phone, 0.5, scaleUpPoint, MovieUtil.PNT3_NEARZERO),
        WaitInterval(pickupDelay),
        FunctionInterval(receiver.wrtReparentTo, extraArgs = [
            suit.getRightHand()]),
        LerpScaleInterval(receiver, 0.01, receiverAdjustScale),
        LerpPosHprInterval(receiver, 0.0001, Point3(-0.53000000000000003, 0.20999999999999999, -0.54000000000000004), Point3(-100.66, -43.299999999999997, 8.1500000000000004)),
        WaitInterval(dialDuration),
        FunctionInterval(receiver.wrtReparentTo, extraArgs = [
            phone]),
        WaitInterval(finalPhoneDelay),
        LerpScaleInterval(phone, 0.5, MovieUtil.PNT3_NEARZERO),
        FunctionInterval(MovieUtil.removeProps, extraArgs = [
            [
                receiver,
                phone]])])
    toonTrack = getToonTrack(attack, 5.5, [
        'slip-backward'], 4.7000000000000002, [
        'jump'])
    soundTrack = getSoundTrack('SA_hangup.mp3', delay = 1.3, node = suit)
    return MultiTrack([
        suitTrack,
        toonTrack,
        propTrack,
        soundTrack])


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
            Point3(-77.469999999999999, 74.049999999999997, 15.52)]
    else:
        tapePosPoints = [
            Point3(0.23999999999999999, 0.089999999999999997, -0.38),
            Point3(-77.469999999999999, 74.049999999999997, 15.52)]
    tapeScaleUpPoint = Point3(0.90000000000000002, 0.90000000000000002, 0.23999999999999999)
    tapeIvals = getPropAppearIntervals(tape, suit.getRightHand(), tapePosPoints, 0.80000000000000004, tapeScaleUpPoint, scaleUpTime = 0.5)
    tapeIvals.append(WaitInterval(1.73))
    
    hitPoint = lambda toon = toon: __toonTorsoPoint(toon)
    tapeIvals.extend(getPropThrowIntervals(attack, tape, [
        hitPoint], [
        __toonGroundPoint(attack, toon, 0.69999999999999996)]))
    propTrack = Track(tapeIvals)
    hips = toon.getHipsParts()
    animal = toon.style.getAnimal()
    scale = Toon.toonBodyScales[animal]
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
    tubeTracks = []
    tubeTracks.append(FunctionInterval(battle.movie.needRestoreHips))
    for partNum in range(0, hips.getNumPaths()):
        nextPart = hips.getPath(partNum)
        tubeTracks.append(getPropTrack(tubes[partNum], nextPart, tubePosPoints, 3.25, 3.1699999999999999, scaleUpPoint = scaleUpPoint))
    
    tubeTracks.append(FunctionInterval(battle.movie.clearRestoreHips))
    toonTrack = getToonTrack(attack, 3.3999999999999999, [
        'struggle'], 2.7999999999999998, [
        'jump'])
    soundTrack = getSoundTrack('SA_red_tape.mp3', delay = 2.8999999999999999, node = suit)
    if dmg > 0:
        return MultiTrack([
            suitTrack,
            toonTrack,
            propTrack,
            soundTrack] + tubeTracks)
    else:
        return MultiTrack([
            suitTrack,
            toonTrack,
            propTrack,
            soundTrack])


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
    liftTracks = []
    toonRiseTracks = []
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
            shadows = toon.dropShadows
            fakeShadow = MovieUtil.copyProp(shadows[0])
            
            def showShadows(true, shadows = shadows):
                ivals = []
                for shadow in shadows:
                    if true == 0:
                        ivals.append(FunctionInterval(shadow.hide))
                    else:
                        ivals.append(FunctionInterval(shadow.show))
                
                return ivals

            x = toon.getX()
            y = toon.getY()
            z = toon.getZ()
            height = 3
            groundPoint = Point3(x, y, z)
            risePoint = Point3(x, y, z + height)
            shakeRight = Point3(x, y + 0.69999999999999996, z + height)
            shakeLeft = Point3(x, y - 0.69999999999999996, z + height)
            shakeIvals = []
            shakeIvals.append(WaitInterval(damageDelay + 0.25))
            shakeIvals.extend(showShadows(0))
            shakeIvals.append(LerpPosInterval(toon, 1.1000000000000001, risePoint))
            for i in range(0, 17):
                shakeIvals.append(LerpPosInterval(toon, 0.029999999999999999, shakeLeft))
                shakeIvals.append(LerpPosInterval(toon, 0.029999999999999999, shakeRight))
            
            shakeIvals.append(LerpPosInterval(toon, 0.10000000000000001, risePoint))
            shakeIvals.append(LerpPosInterval(toon, 0.10000000000000001, groundPoint))
            shakeIvals.extend(showShadows(1))
            shadowIvals = []
            shadowIvals.append(FunctionInterval(battle.movie.needRestoreRenderProp, extraArgs = [
                fakeShadow]))
            shadowIvals.append(WaitInterval(damageDelay + 0.25))
            shadowIvals.append(FunctionInterval(fakeShadow.hide))
            shadowIvals.append(FunctionInterval(fakeShadow.setScale, extraArgs = [
                0.27000000000000002]))
            shadowIvals.append(FunctionInterval(fakeShadow.reparentTo, extraArgs = [
                toon]))
            shadowIvals.append(FunctionInterval(fakeShadow.setPos, extraArgs = [
                MovieUtil.PNT3_ZERO]))
            shadowIvals.append(FunctionInterval(fakeShadow.wrtReparentTo, extraArgs = [
                battle]))
            shadowIvals.append(FunctionInterval(fakeShadow.show))
            shadowIvals.append(LerpScaleInterval(fakeShadow, 0.40000000000000002, Point3(0.17000000000000001, 0.17000000000000001, 0.17000000000000001)))
            shadowIvals.append(WaitInterval(1.8100000000000001))
            shadowIvals.append(LerpScaleInterval(fakeShadow, 0.10000000000000001, Point3(0.27000000000000002, 0.27000000000000002, 0.27000000000000002)))
            shadowIvals.append(FunctionInterval(MovieUtil.removeProp, extraArgs = [
                fakeShadow]))
            shadowIvals.append(FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
                fakeShadow]))
            toonRiseTracks.append(MultiTrack([
                Track(shakeIvals),
                Track(shadowIvals)]))
        
    
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
        return MultiTrack([
            suitTrack,
            sprayTrack,
            soundTrack] + liftTracks + toonTracks + toonRiseTracks)
    else:
        return MultiTrack([
            suitTrack,
            sprayTrack] + liftTracks + toonTracks + toonRiseTracks)


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
        partTrack = Track([
            (1.0, FunctionInterval(battle.movie.needRestoreParticleEffect, extraArgs = [
                effect])),
            FunctionInterval(effect.start, extraArgs = [
                suit]),
            WaitInterval(0.40000000000000002),
            LerpPosInterval(effect, 1.0, Point3(0, 15, 0.40000000000000002)),
            LerpFunctionInterval(effect.setAlphaScale, fromData = 1, toData = 0, duration = 0.40000000000000002),
            FunctionInterval(effect.cleanup),
            FunctionInterval(battle.movie.clearRestoreParticleEffect, extraArgs = [
                effect])])
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
    return MultiTrack([
        suitTrack,
        partTrack1,
        partTrack2,
        waterfallTrack] + toonTracks)


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
        Point3(-176, 89, 11)]
    
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
    checkIvals = getPropAppearIntervals(check, suit.getRightHand(), checkPosPoints, 1.0000000000000001e-005, Point3(8.5, 8.5, 8.5), startScale = MovieUtil.PNT3_ONE)
    checkIvals.append(WaitInterval(throwDelay))
    checkIvals.append(FunctionInterval(check.wrtReparentTo, extraArgs = [
        toon]))
    checkIvals.append(FunctionInterval(check.setHpr, extraArgs = [
        Point3(0, -90, 0)]))
    checkIvals.extend(getThrowIvals(check, bounce1Point, duration = 0.5, parent = toon))
    checkIvals.extend(getThrowIvals(check, bounce2Point, duration = 0.90000000000000002, parent = toon))
    if hitSuit:
        checkIvals.extend(getThrowIvals(check, hit3Point, duration = 0.69999999999999996, parent = toon))
    else:
        checkIvals.extend(getThrowIvals(check, miss3Point, duration = 0.69999999999999996, parent = toon))
        checkIvals.extend(getThrowIvals(check, bounce4Point, duration = 0.69999999999999996, parent = toon))
        checkIvals.append(LerpScaleInterval(check, 0.29999999999999999, MovieUtil.PNT3_NEARZERO))
    checkIvals.append(FunctionInterval(MovieUtil.removeProp, extraArgs = [
        check]))
    checkPropTrack = Track(checkIvals)
    toonTrack = getToonTrack(attack, damageDelay, [
        'conked'], dodgeDelay, [
        'sidestep'])
    soundTracks = Track(getSoundTrack('SA_pink_slip.mp3', delay = throwDelay + 0.5, duration = 0.59999999999999998, node = suit), getSoundTrack('SA_pink_slip.mp3', delay = 0.40000000000000002, duration = 0.59999999999999998, node = suit))
    return MultiTrack([
        suitTrack,
        checkPropTrack,
        toonTrack,
        soundTracks])


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
    hitSprayIvals = MovieUtil.getSprayIntervals(battle, Point4(0.75, 0.75, 1.0, 0.80000000000000004), getCoolerSpout, hitPoint, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, horizScale = 0.29999999999999999, vertScale = 0.29999999999999999)
    missSprayIvals = MovieUtil.getSprayIntervals(battle, Point4(0.75, 0.75, 1.0, 0.80000000000000004), getCoolerSpout, missPoint, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, horizScale = 0.29999999999999999, vertScale = 0.29999999999999999)
    suitTrack = getSuitTrack(attack)
    posPoints = [
        Point3(0.47999999999999998, 0.11, -0.92000000000000004),
        Point3(37.030000000000001, -10.619999999999999, -79.209999999999994)]
    propIvals = [
        WaitInterval(1.01),
        FunctionInterval(__showProp, extraArgs = [
            watercooler,
            suit.getLeftHand(),
            posPoints[0],
            posPoints[1]]),
        LerpScaleInterval(watercooler, 0.5, Point3(1.1499999999999999, 1.1499999999999999, 1.1499999999999999)),
        WaitInterval(1.6000000000000001)]
    if dmg > 0:
        propIvals += hitSprayIvals
    else:
        propIvals += missSprayIvals
    propIvals += [
        WaitInterval(0.01),
        LerpScaleInterval(watercooler, 0.5, MovieUtil.PNT3_NEARZERO),
        FunctionInterval(MovieUtil.removeProp, extraArgs = [
            watercooler])]
    propTrack = Track(propIvals)
    splashTrack = []
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
        splashIvals = [
            FunctionInterval(battle.movie.needRestoreRenderProp, extraArgs = [
                splash]),
            (3.2000000000000002, FunctionInterval(prepSplash, extraArgs = [
                splash,
                __toonFacePoint(toon)])),
            ActorInterval(splash, 'splash-from-splat'),
            FunctionInterval(MovieUtil.removeProp, extraArgs = [
                splash]),
            FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
                splash])]
        splashTrack.append(Track(splashIvals))
    
    toonTrack = getToonTrack(attack, suitTrack.getDuration() - 1.5, [
        'cringe'], 2.3999999999999999, [
        'sidestep'])
    soundTrack = Track([
        WaitInterval(1.1000000000000001),
        SoundInterval(globalBattleSoundCache.getSound('SA_watercooler_appear_only.mp3'), node = suit),
        WaitInterval(0.40000000000000002),
        SoundInterval(globalBattleSoundCache.getSound('SA_watercooler_spray_only.mp3'), node = suit)])
    return MultiTrack([
        suitTrack,
        toonTrack,
        propTrack,
        soundTrack] + splashTrack)


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
        ivals = []
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            ivals.append(FunctionInterval(nextPart.setColorScale, extraArgs = [
                Vec4(0, 0, 0, 1)]))
        
        return ivals

    
    def resetColor(parts):
        ivals = []
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            ivals.append(FunctionInterval(nextPart.clearColorScale))
        
        return ivals

    if dmg > 0:
        headParts = toon.getHeadParts()
        torsoParts = toon.getTorsoParts()
        legsParts = toon.getLegsParts()
        colorIvals = []
        colorIvals.append(WaitInterval(2.0))
        colorIvals.append(FunctionInterval(battle.movie.needRestoreColor))
        colorIvals.extend(changeColor(headParts))
        colorIvals.extend(changeColor(torsoParts))
        colorIvals.extend(changeColor(legsParts))
        colorIvals.append(WaitInterval(3.5))
        colorIvals.extend(resetColor(headParts))
        colorIvals.extend(resetColor(torsoParts))
        colorIvals.extend(resetColor(legsParts))
        colorIvals.append(FunctionInterval(battle.movie.clearRestoreColor))
        colorTrack = Track(colorIvals)
    
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
        return MultiTrack([
            suitTrack,
            baseFlameTrack,
            flameTrack,
            flecksTrack,
            toonTrack,
            colorTrack,
            soundTrack])
    else:
        return MultiTrack([
            suitTrack,
            baseFlameSmallTrack,
            flameSmallTrack,
            flecksSmallTrack,
            toonTrack,
            soundTrack])


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
            Point3(2.0299999999999998, -6.3399999999999999, 6.0099999999999998)]
        calcDuration = 0.76000000000000001
        scaleUpPoint = Point3(1.1000000000000001, 1.8500000000000001, 1.8100000000000001)
    else:
        calcPosPoints = [
            Point3(0.34999999999999998, 0.52000000000000002, 0.029999999999999999),
            Point3(2.0299999999999998, -6.3399999999999999, 6.0099999999999998)]
        calcDuration = 1.8700000000000001
        scaleUpPoint = Point3(1.0, 1.3700000000000001, 1.3100000000000001)
    calcPropTrack = getPropTrack(calculator, suit.getLeftHand(), calcPosPoints, 9.9999999999999995e-007, calcDuration, scaleUpPoint = scaleUpPoint, anim = 1, propName = 'calculator', animStartTime = 0.5, animDuration = 3.3999999999999999)
    toonTrack = getToonTrack(attack, 3.2000000000000002, [
        'conked'], 0.90000000000000002, [
        'duck'], showMissedExtraTime = 2.2000000000000002)
    soundTrack = getSoundTrack('SA_audit.mp3', delay = 1.8999999999999999, node = suit)
    return MultiTrack([
        suitTrack,
        toonTrack,
        calcPropTrack,
        soundTrack,
        partTrack,
        partTrack2,
        partTrack3,
        partTrack4,
        partTrack5])


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
            Point3(2.0299999999999998, -6.3399999999999999, 6.0099999999999998)]
        calcDuration = 0.76000000000000001
        scaleUpPoint = Point3(1.1000000000000001, 1.8500000000000001, 1.8100000000000001)
    else:
        calcPosPoints = [
            Point3(0.34999999999999998, 0.52000000000000002, 0.029999999999999999),
            Point3(2.0299999999999998, -6.3399999999999999, 6.0099999999999998)]
        calcDuration = 1.8700000000000001
        scaleUpPoint = Point3(1.0, 1.3700000000000001, 1.3100000000000001)
    calcPropTrack = getPropTrack(calculator, suit.getLeftHand(), calcPosPoints, 9.9999999999999995e-007, calcDuration, scaleUpPoint = scaleUpPoint, anim = 1, propName = 'calculator', animStartTime = 0.5, animDuration = 3.3999999999999999)
    toonTrack = getToonTrack(attack, 3.2000000000000002, [
        'conked'], 1.8, [
        'sidestep'])
    return MultiTrack([
        suitTrack,
        toonTrack,
        calcPropTrack,
        partTrack,
        partTrack2,
        partTrack3,
        partTrack4,
        partTrack5])


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
            Point3(2.0299999999999998, -6.3399999999999999, 6.0099999999999998)]
        calcDuration = 0.76000000000000001
        scaleUpPoint = Point3(1.1000000000000001, 1.8500000000000001, 1.8100000000000001)
    else:
        calcPosPoints = [
            Point3(0.34999999999999998, 0.52000000000000002, 0.029999999999999999),
            Point3(2.0299999999999998, -6.3399999999999999, 6.0099999999999998)]
        calcDuration = 1.8700000000000001
        scaleUpPoint = Point3(1.0, 1.3700000000000001, 1.3100000000000001)
    calcPropTrack = getPropTrack(calculator, suit.getLeftHand(), calcPosPoints, 9.9999999999999995e-007, calcDuration, scaleUpPoint = scaleUpPoint, anim = 1, propName = 'calculator', animStartTime = 0.5, animDuration = 3.3999999999999999)
    toonTrack = getToonTrack(attack, 3.2000000000000002, [
        'conked'], 1.8, [
        'sidestep'])
    return MultiTrack([
        suitTrack,
        toonTrack,
        calcPropTrack,
        partTrack,
        partTrack2,
        partTrack3,
        partTrack4,
        partTrack5])


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
    numberSprayTracks = []
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
    
    numbers = []
    numberTracks = []
    for i in range(0, numOfNumbers):
        texture = whrandom.choice(numberNames)
        next = MovieUtil.copyProp(BattleParticles.getParticle('audit-' + texture))
        next.reparentTo(suit.getRightHand())
        next.setScale(0.01, 0.01, 0.01)
        next.setColor(Vec4(0.0, 0.0, 0.0, 1.0))
        next.setPos(whrandom.random() * 0.59999999999999998 - 0.29999999999999999, whrandom.random() * 0.59999999999999998 - 0.29999999999999999, whrandom.random() * 0.59999999999999998 - 0.29999999999999999)
        next.setHpr(Point3(-77.469999999999999, 74.049999999999997, 15.52))
        numberTrack = Track([
            WaitInterval(0.90000000000000002),
            LerpScaleInterval(next, 0.59999999999999998, MovieUtil.PNT3_ONE),
            WaitInterval(1.7),
            FunctionInterval(MovieUtil.removeProp, extraArgs = [
                next])])
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
    return MultiTrack([
        suitTrack,
        toonTrack,
        numberSpillTrack1,
        numberSpillTrack2] + numberTracks + numberSprayTracks)


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
        Point3(180, 0, 0)]
    cloudIvals = []
    cloudIvals.append(FunctionInterval(cloud.pose, extraArgs = [
        'stormcloud',
        0]))
    cloudIvals.extend(getPropAppearIntervals(cloud, suit, cloudPosPoints, 9.9999999999999995e-007, Point3(3, 3, 3), scaleUpTime = 0.69999999999999996))
    cloudIvals.append(FunctionInterval(battle.movie.needRestoreRenderProp, extraArgs = [
        cloud]))
    cloudIvals.append(FunctionInterval(cloud.wrtReparentTo, extraArgs = [
        render]))
    targetPoint = __toonFacePoint(toon)
    targetPoint.setZ(targetPoint[2] + 3)
    cloudIvals.append(WaitInterval(1.1000000000000001))
    cloudIvals.append(LerpPosInterval(cloud, 1, pos = targetPoint))
    cloudIvals.append(WaitInterval(partDelay))
    pivals = []
    pivals.append(Track([
        ParticleInterval(rainEffect, cloud, worldRelative = 0, duration = 2.1000000000000001)]))
    pivals.append(Track([
        (0.10000000000000001, ParticleInterval(rainEffect2, cloud, worldRelative = 0, duration = 2.0))]))
    pivals.append(Track([
        (0.10000000000000001, ParticleInterval(rainEffect3, cloud, worldRelative = 0, duration = 2.0))]))
    pivals.append(Track([
        ActorInterval(cloud, 'stormcloud', startTime = 3, duration = 0.10000000000000001),
        ActorInterval(cloud, 'stormcloud', startTime = 1, duration = 2.2999999999999998)]))
    cloudIvals.append(MultiTrack(pivals))
    cloudIvals.append(WaitInterval(0.40000000000000002))
    cloudIvals.append(LerpScaleInterval(cloud, 0.5, MovieUtil.PNT3_NEARZERO))
    cloudIvals.append(FunctionInterval(MovieUtil.removeProp, extraArgs = [
        cloud]))
    cloudIvals.append(FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
        cloud]))
    cloudPropTrack = Track(cloudIvals)
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
        puddleTrack = Track([
            FunctionInterval(battle.movie.needRestoreRenderProp, extraArgs = [
                puddle]),
            WaitInterval(damageDelay - 0.69999999999999996),
            FunctionInterval(puddle.reparentTo, extraArgs = [
                battle]),
            FunctionInterval(puddle.setPos, extraArgs = [
                toon.getPos(battle)]),
            LerpScaleInterval(puddle, 1.7, Point3(1.7, 1.7, 1.7), startScale = MovieUtil.PNT3_NEARZERO),
            WaitInterval(3.2000000000000002),
            LerpFunctionInterval(puddle.setAlphaScale, fromData = 1, toData = 0, duration = 0.80000000000000004),
            FunctionInterval(MovieUtil.removeProp, extraArgs = [
                puddle]),
            FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
                puddle])])
        return MultiTrack([
            suitTrack,
            toonTrack,
            cloudPropTrack,
            soundTrack,
            puddleTrack])
    else:
        return MultiTrack([
            suitTrack,
            toonTrack,
            cloudPropTrack,
            soundTrack])


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
        Point3(-169.69999999999999, -36.030000000000001, -39.289999999999999)]
    paperIvals = getPropAppearIntervals(paper, suit.getRightHand(), posPoints, propDelay, Point3(3, 3, 3), scaleUpTime = 0.5)
    paperIvals.append(WaitInterval(suitDelay))
    hitPoint = toon.getPos(battle)
    hitPoint.setX(hitPoint.getX() + 1.2)
    hitPoint.setY(hitPoint.getY() + 1.5)
    if dmg > 0:
        hitPoint.setZ(hitPoint.getZ() + 1.1000000000000001)
    
    movePoint = Point3(hitPoint.getX(), hitPoint.getY() - 1.8, hitPoint.getZ() + 0.20000000000000001)
    paperIvals.append(FunctionInterval(battle.movie.needRestoreRenderProp, extraArgs = [
        paper]))
    paperIvals.append(FunctionInterval(paper.wrtReparentTo, extraArgs = [
        battle]))
    paperIvals.extend(getThrowIvals(paper, hitPoint, duration = throwDuration, parent = battle))
    paperIvals.append(WaitInterval(0.59999999999999998))
    paperIvals.append(LerpPosInterval(paper, 0.40000000000000002, movePoint))
    paperTrack = Track(paperIvals)
    spinTrack = Track([
        WaitInterval(propDelay + suitDelay + 0.20000000000000001),
        LerpHprInterval(paper, throwDuration, Point3(-360, 0, 0))])
    sizeTrack = Track([
        WaitInterval(propDelay + suitDelay + 0.20000000000000001),
        LerpScaleInterval(paper, throwDuration, Point3(6, 6, 6)),
        WaitInterval(0.94999999999999996),
        LerpScaleInterval(paper, 0.40000000000000002, MovieUtil.PNT3_NEARZERO)])
    propTrack = Track([
        MultiTrack([
            paperTrack,
            spinTrack,
            sizeTrack]),
        FunctionInterval(MovieUtil.removeProp, extraArgs = [
            paper]),
        FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
            paper])])
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
    return MultiTrack([
        suitTrack,
        toonTrack,
        propTrack])


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
        Point3(0.0, -5.71, -51.340000000000003)]
    teethIvals = getPropAppearIntervals(teeth, suit.getRightHand(), posPoints, propDelay, Point3(3, 3, 3), scaleUpTime = propScaleUpTime)
    teethIvals.append(WaitInterval(suitDelay))
    teethIvals.append(FunctionInterval(battle.movie.needRestoreRenderProp, extraArgs = [
        teeth]))
    teethIvals.append(FunctionInterval(teeth.wrtReparentTo, extraArgs = [
        battle]))
    if dmg > 0:
        x = toon.getX(battle)
        y = toon.getY(battle)
        z = toon.getZ(battle)
        toonHeight = z + toon.getHeight()
        flyPoint = Point3(x, y + 2.7000000000000002, toonHeight * 0.80000000000000004)
        teethIvals.append(LerpPosInterval(teeth, throwDuration, pos = flyPoint))
        teethIvals.append(LerpPosInterval(teeth, 0.40000000000000002, pos = Point3(x, y + 3.2000000000000002, toonHeight * 0.69999999999999996)))
        teethIvals.append(LerpPosInterval(teeth, 0.29999999999999999, pos = Point3(x, y + 4.7000000000000002, toonHeight * 0.5)))
        teethIvals.append(WaitInterval(0.20000000000000001))
        teethIvals.append(LerpPosInterval(teeth, 0.10000000000000001, pos = Point3(x, y - 0.20000000000000001, toonHeight * 0.90000000000000002)))
        teethIvals.append(WaitInterval(0.40000000000000002))
        scaleTrack = Track([
            (throwDelay, LerpScaleInterval(teeth, throwDuration, Point3(8, 8, 8))),
            WaitInterval(0.90000000000000002),
            LerpScaleInterval(teeth, 0.20000000000000001, Point3(14, 14, 14)),
            WaitInterval(1.2),
            LerpScaleInterval(teeth, 0.29999999999999999, MovieUtil.PNT3_NEARZERO)])
        hprTrack = Track([
            (throwDelay, LerpHprInterval(teeth, 0.29999999999999999, Point3(180, 0, 0))),
            WaitInterval(0.20000000000000001),
            LerpHprInterval(teeth, 0.40000000000000002, Point3(180, -35, 0), startHpr = Point3(180, 0, 0)),
            WaitInterval(0.59999999999999998),
            LerpHprInterval(teeth, 0.10000000000000001, Point3(180, -75, 0), startHpr = Point3(180, -35, 0))])
        animTrack = Track([
            (throwDelay, ActorInterval(teeth, 'teeth', duration = throwDuration)),
            ActorInterval(teeth, 'teeth', duration = 0.29999999999999999),
            FunctionInterval(teeth.pose, extraArgs = [
                'teeth',
                1]),
            WaitInterval(0.69999999999999996),
            ActorInterval(teeth, 'teeth', duration = 0.90000000000000002)])
        propTrack = Track([
            MultiTrack([
                Track(teethIvals),
                scaleTrack,
                hprTrack,
                animTrack]),
            FunctionInterval(MovieUtil.removeProp, extraArgs = [
                teeth]),
            FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
                teeth])])
    else:
        flyPoint = __toonFacePoint(toon, parent = battle)
        flyPoint.setY(flyPoint.getY() - 7.0999999999999996)
        teethIvals.append(LerpPosInterval(teeth, throwDuration, pos = flyPoint))
        teethIvals.append(FunctionInterval(MovieUtil.removeProp, extraArgs = [
            teeth]))
        teethIvals.append(FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
            teeth]))
        propTrack = Track(teethIvals)
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
    return MultiTrack([
        suitTrack,
        toonTrack,
        propTrack])


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
        Point3(0.0, -5.71, -51.340000000000003)]
    teethIvals = getPropAppearIntervals(teeth, suit.getRightHand(), posPoints, propDelay, Point3(3, 3, 3), scaleUpTime = propScaleUpTime)
    teethIvals.append(WaitInterval(suitDelay))
    teethIvals.append(FunctionInterval(battle.movie.needRestoreRenderProp, extraArgs = [
        teeth]))
    teethIvals.append(FunctionInterval(teeth.wrtReparentTo, extraArgs = [
        battle]))
    if dmg > 0:
        x = toon.getX(battle)
        y = toon.getY(battle)
        z = toon.getZ(battle)
        toonHeight = z + toon.getHeight()
        flyPoint = Point3(x, y + 2.7000000000000002, toonHeight * 0.69999999999999996)
        teethIvals.append(LerpPosInterval(teeth, throwDuration, pos = flyPoint))
        teethIvals.append(LerpPosInterval(teeth, 0.40000000000000002, pos = Point3(x, y + 3.2000000000000002, toonHeight * 0.69999999999999996)))
        teethIvals.append(LerpPosInterval(teeth, 0.29999999999999999, pos = Point3(x, y + 4.7000000000000002, toonHeight * 0.5)))
        teethIvals.append(WaitInterval(0.20000000000000001))
        teethIvals.append(LerpPosInterval(teeth, 0.10000000000000001, pos = Point3(x, y, toonHeight + 3)))
        teethIvals.append(LerpPosInterval(teeth, 0.10000000000000001, pos = Point3(x, y - 1.2, toonHeight * 0.69999999999999996)))
        teethIvals.append(LerpPosInterval(teeth, 0.10000000000000001, pos = Point3(x, y - 0.69999999999999996, toonHeight * 0.40000000000000002)))
        teethIvals.append(WaitInterval(0.40000000000000002))
        scaleTrack = Track([
            (throwDelay, LerpScaleInterval(teeth, throwDuration, Point3(6, 6, 6))),
            WaitInterval(0.90000000000000002),
            LerpScaleInterval(teeth, 0.20000000000000001, Point3(10, 10, 10)),
            WaitInterval(1.2),
            LerpScaleInterval(teeth, 0.29999999999999999, MovieUtil.PNT3_NEARZERO)])
        hprTrack = Track([
            (throwDelay, LerpHprInterval(teeth, 0.29999999999999999, Point3(180, 0, 0))),
            WaitInterval(0.20000000000000001),
            LerpHprInterval(teeth, 0.40000000000000002, Point3(180, -35, 0), startHpr = Point3(180, 0, 0)),
            WaitInterval(0.59999999999999998),
            LerpHprInterval(teeth, 0.10000000000000001, Point3(0, -35, 0), startHpr = Point3(180, -35, 0))])
        animTrack = Track([
            (throwDelay, ActorInterval(teeth, 'teeth', duration = throwDuration)),
            ActorInterval(teeth, 'teeth', duration = 0.29999999999999999),
            FunctionInterval(teeth.pose, extraArgs = [
                'teeth',
                1]),
            WaitInterval(0.69999999999999996),
            ActorInterval(teeth, 'teeth', duration = 0.90000000000000002)])
        propTrack = Track([
            MultiTrack([
                Track(teethIvals),
                scaleTrack,
                hprTrack,
                animTrack]),
            FunctionInterval(MovieUtil.removeProp, extraArgs = [
                teeth]),
            FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
                teeth])])
    else:
        x = toon.getX(battle)
        y = toon.getY(battle)
        z = toon.getZ(battle)
        z = z + 0.20000000000000001
        flyPoint = Point3(x, y - 2.1000000000000001, z)
        teethIvals.append(LerpPosInterval(teeth, throwDuration, pos = flyPoint))
        teethIvals.append(WaitInterval(0.20000000000000001))
        teethIvals.append(LerpPosInterval(teeth, 0.20000000000000001, pos = Point3(x + 0.5, y - 2.5, z)))
        teethIvals.append(LerpPosInterval(teeth, 0.20000000000000001, pos = Point3(x + 1.0, y - 3.0, z + 0.40000000000000002)))
        teethIvals.append(LerpPosInterval(teeth, 0.20000000000000001, pos = Point3(x + 1.3, y - 3.6000000000000001, z)))
        teethIvals.append(LerpPosInterval(teeth, 0.20000000000000001, pos = Point3(x + 0.90000000000000002, y - 3.1000000000000001, z + 0.40000000000000002)))
        teethIvals.append(LerpPosInterval(teeth, 0.20000000000000001, pos = Point3(x + 0.29999999999999999, y - 2.6000000000000001, z)))
        teethIvals.append(LerpPosInterval(teeth, 0.20000000000000001, pos = Point3(x - 0.10000000000000001, y - 2.2000000000000002, z + 0.40000000000000002)))
        teethIvals.append(LerpPosInterval(teeth, 0.20000000000000001, pos = Point3(x - 0.40000000000000002, y - 1.8999999999999999, z)))
        teethIvals.append(LerpPosInterval(teeth, 0.20000000000000001, pos = Point3(x - 0.69999999999999996, y - 2.1000000000000001, z + 0.40000000000000002)))
        teethIvals.append(LerpPosInterval(teeth, 0.20000000000000001, pos = Point3(x - 0.80000000000000004, y - 2.2999999999999998, z)))
        teethIvals.append(LerpScaleInterval(teeth, 0.59999999999999998, MovieUtil.PNT3_NEARZERO))
        hprTrack = Track([
            (throwDelay, LerpHprInterval(teeth, 0.29999999999999999, Point3(180, 0, 0))),
            WaitInterval(0.5),
            LerpHprInterval(teeth, 0.40000000000000002, Point3(80, 0, 0), startHpr = Point3(180, 0, 0)),
            LerpHprInterval(teeth, 0.80000000000000004, Point3(-10, 0, 0), startHpr = Point3(80, 0, 0))])
        animTrack = Track([
            (throwDelay, ActorInterval(teeth, 'teeth', duration = 3.6000000000000001))])
        propTrack = Track([
            MultiTrack([
                Track(teethIvals),
                hprTrack,
                animTrack]),
            FunctionInterval(MovieUtil.removeProp, extraArgs = [
                teeth]),
            FunctionInterval(battle.movie.clearRenderProp, extraArgs = [
                teeth])])
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
    return MultiTrack([
        suitTrack,
        toonTrack,
        propTrack])


def doEvictionNotice(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    paper = globalPropPool.getProp('shredder-paper')
    suitTrack = getSuitTrack(attack)
    posPoints = [
        Point3(-0.040000000000000001, 0.14999999999999999, -1.3799999999999999),
        Point3(6.3399999999999999, -14.619999999999999, -18.02)]
    paperIvals = getPropAppearIntervals(paper, suit.getRightHand(), posPoints, 0.80000000000000004, MovieUtil.PNT3_ONE, scaleUpTime = 0.5)
    paperIvals.append(WaitInterval(1.73))
    hitPoint = __toonFacePoint(toon, parent = battle)
    hitPoint.setX(hitPoint.getX() - 1.3999999999999999)
    missPoint = __toonGroundPoint(attack, toon, 0.69999999999999996, parent = battle)
    missPoint.setX(missPoint.getX() - 1.1000000000000001)
    paperIvals.extend(getPropThrowIntervals(attack, paper, [
        hitPoint], [
        missPoint], parent = battle))
    propTrack = Track(paperIvals)
    toonTrack = getToonTrack(attack, 3.3999999999999999, [
        'conked'], 2.7999999999999998, [
        'jump'])
    return MultiTrack([
        suitTrack,
        toonTrack,
        propTrack])


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
        ivals = []
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            ivals.append(FunctionInterval(nextPart.setColorScale, extraArgs = [
                Vec4(0, 0, 0, 1)]))
        
        return Track(ivals)

    
    def resetColor(parts):
        ivals = []
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            ivals.append(FunctionInterval(nextPart.clearColorScale))
        
        return ivals

    soundTrack = getSoundTrack('SA_withdrawl.mp3', delay = 1.3999999999999999, node = suit)
    if dmg > 0:
        colorIvals = []
        colorIvals.append(WaitInterval(1.6000000000000001))
        colorIvals.append(FunctionInterval(battle.movie.needRestoreColor))
        colorIvals.append(MultiTrack([
            changeColor(headParts),
            changeColor(torsoParts),
            changeColor(legsParts)]))
        colorIvals.append(WaitInterval(2.8999999999999999))
        colorIvals.extend(resetColor(headParts))
        colorIvals.extend(resetColor(torsoParts))
        colorIvals.extend(resetColor(legsParts))
        colorIvals.append(FunctionInterval(battle.movie.clearRestoreColor))
        colorTrack = Track(colorIvals)
        return MultiTrack([
            suitTrack,
            partTrack,
            toonTrack,
            soundTrack,
            colorTrack])
    else:
        return MultiTrack([
            suitTrack,
            partTrack,
            toonTrack,
            soundTrack])


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
    return MultiTrack([
        suitTrack,
        toonTrack,
        soundTrack,
        partTrack,
        partTrack2,
        partTrack3,
        partTrack4])


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
        return MultiTrack([
            suitTrack,
            toonTrack,
            soundTrack,
            partTrack,
            partTrack2,
            partTrack3,
            partTrack4,
            partTrack5])
    else:
        return MultiTrack([
            suitTrack,
            toonTrack,
            soundTrack,
            partTrack,
            partTrack2])


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
        partTrack = Track([
            (0.69999999999999996, FunctionInterval(battle.movie.needRestoreParticleEffect, extraArgs = [
                effect])),
            FunctionInterval(effect.start, extraArgs = [
                suit]),
            WaitInterval(0.40000000000000002),
            LerpPosInterval(effect, 1.0, Point3(0, 15, 0.40000000000000002)),
            LerpFunctionInterval(effect.setAlphaScale, fromData = 1, toData = 0, duration = 0.40000000000000002),
            FunctionInterval(effect.cleanup),
            FunctionInterval(battle.movie.clearRestoreParticleEffect, extraArgs = [
                effect])])
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
    return MultiTrack([
        suitTrack,
        partTrack1,
        partTrack2,
        soundTrack,
        waterfallTrack] + toonTracks)


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
        Point3(6.3399999999999999, -14.619999999999999, -18.02)]
    paperIvals = getPropAppearIntervals(paper, suit.getRightHand(), posPoints, 0.80000000000000004, MovieUtil.PNT3_ONE, scaleUpTime = 0.5)
    paperIvals.append(WaitInterval(1.73))
    hitPoint = __toonFacePoint(toon, parent = battle)
    hitPoint.setX(hitPoint.getX() - 1.3999999999999999)
    missPoint = __toonGroundPoint(attack, toon, 0.69999999999999996, parent = battle)
    missPoint.setX(missPoint.getX() - 1.1000000000000001)
    paperIvals.extend(getPropThrowIntervals(attack, paper, [
        hitPoint], [
        missPoint], parent = battle))
    propTrack = Track(paperIvals)
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
        return MultiTrack([
            suitTrack,
            cloudTrack,
            toonTrack,
            propTrack])
    else:
        return MultiTrack([
            suitTrack,
            toonTrack,
            propTrack])


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
    spinEffect1.setHpr(Point3(0, 50, whrandom.random() * 10 + 85))
    spinEffect2.setPos(Point3(0, -1.3, height2))
    spinEffect2.setHpr(Point3(0, 50, whrandom.random() * 10 + 85))
    spinEffect3.setPos(Point3(0, -1.3, height3))
    spinEffect3.setHpr(Point3(0, 50, whrandom.random() * 10 + 85))
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
        toonSpinTrack = Track([
            WaitInterval(damageDelay + 0.90000000000000002),
            LerpHprInterval(toon, 0.69999999999999996, Point3(-10, 0, 0)),
            LerpHprInterval(toon, 0.5, Point3(-30, 0, 0)),
            LerpHprInterval(toon, 0.20000000000000001, Point3(-60, 0, 0)),
            LerpHprInterval(toon, 0.69999999999999996, Point3(-700, 0, 0)),
            LerpHprInterval(toon, 1.0, Point3(-1310, 0, 0)),
            LerpHprInterval(toon, 0.40000000000000002, toon.getHpr()),
            WaitInterval(0.5)])
        return MultiTrack([
            suitTrack,
            sprayTrack,
            toonTrack,
            toonSpinTrack,
            spinTrack1,
            spinTrack2,
            spinTrack3])
    else:
        return MultiTrack([
            suitTrack,
            sprayTrack,
            toonTrack])


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
    return MultiTrack([
        suitTrack,
        toonTrack,
        sprayTrack1,
        sprayTrack2,
        sprayTrack3])


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
    birdTracks = []
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
        birdTrack = Track([
            WaitInterval(throwDelay),
            FunctionInterval(battle.movie.needRestoreRenderProp, extraArgs = [
                next]),
            FunctionInterval(next.wrtReparentTo, extraArgs = [
                battle]),
            FunctionInterval(next.setHpr, extraArgs = [
                Point3(90, -20, -40)]),
            LerpPosInterval(next, 1.1000000000000001, hitPoint)])
        scaleTrack = Track([
            WaitInterval(throwDelay),
            LerpScaleInterval(next, 0.14999999999999999, Point3(9, 9, 9))])
        birdTracks.append(Track([
            MultiTrack([
                birdTrack,
                scaleTrack]),
            FunctionInterval(MovieUtil.removeProp, extraArgs = [
                next])]))
    
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
    return MultiTrack([
        suitTrack,
        toonTrack] + birdTracks)

