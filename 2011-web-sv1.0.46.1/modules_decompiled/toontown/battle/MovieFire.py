# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\battle\MovieFire.py
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from BattleBase import *
from BattleProps import *
from BattleSounds import *
from toontown.toon.ToonDNA import *
from toontown.suit.SuitDNA import *
from direct.directnotify import DirectNotifyGlobal
import random, MovieCamera, MovieUtil
from MovieUtil import calcAvgSuitPos
notify = DirectNotifyGlobal.directNotify.newCategory('MovieThrow')
hitSoundFiles = ('AA_tart_only.mp3', 'AA_slice_only.mp3', 'AA_slice_only.mp3', 'AA_slice_only.mp3',
                 'AA_slice_only.mp3', 'AA_wholepie_only.mp3', 'AA_wholepie_only.mp3')
tPieLeavesHand = 2.7
tPieHitsSuit = 3.0
tSuitDodges = 2.45
ratioMissToHit = 1.5
tPieShrink = 0.7
pieFlyTaskName = 'MovieThrow-pieFly'

def addHit(dict, suitId, hitCount):
    if dict.has_key(suitId):
        dict[suitId] += hitCount
    else:
        dict[suitId] = hitCount


def doFires--- This code section failed: ---

 L.  71         0  LOAD_GLOBAL           0  'len'
                3  LOAD_FAST             0  'fires'
                6  CALL_FUNCTION_1       1  None
                9  LOAD_CONST               0
               12  COMPARE_OP            2  ==
               15  JUMP_IF_FALSE         8  'to 26'
             18_0  THEN                     27
               18  POP_TOP          

 L.  72        19  LOAD_CONST               (None, None)
               22  RETURN_VALUE     
               23  JUMP_FORWARD          1  'to 27'
             26_0  COME_FROM            15  '15'
               26  POP_TOP          
             27_0  COME_FROM            23  '23'

 L.  75        27  BUILD_MAP             0 
               30  STORE_FAST            5  'suitFiresDict'

 L.  78        33  SETUP_LOOP           81  'to 117'
               36  LOAD_FAST             0  'fires'
               39  GET_ITER         
               40  FOR_ITER             73  'to 116'
               43  STORE_FAST            4  'fire'

 L.  79        46  LOAD_FAST             4  'fire'
               49  LOAD_CONST               'target'
               52  BINARY_SUBSCR    
               53  LOAD_CONST               'suit'
               56  BINARY_SUBSCR    
               57  LOAD_ATTR             5  'doId'
               60  STORE_FAST            7  'suitId'

 L.  80        63  LOAD_FAST             5  'suitFiresDict'
               66  LOAD_ATTR             7  'has_key'
               69  LOAD_FAST             7  'suitId'
               72  CALL_FUNCTION_1       1  None
               75  JUMP_IF_FALSE        21  'to 99'
               78  POP_TOP          

 L.  81        79  LOAD_FAST             5  'suitFiresDict'
               82  LOAD_FAST             7  'suitId'
               85  BINARY_SUBSCR    
               86  LOAD_ATTR             8  'append'
               89  LOAD_FAST             4  'fire'
               92  CALL_FUNCTION_1       1  None
               95  POP_TOP          
               96  JUMP_BACK            40  'to 40'
             99_0  COME_FROM            75  '75'
               99  POP_TOP          

 L.  83       100  LOAD_FAST             4  'fire'
              103  BUILD_LIST_1          1 
              106  LOAD_FAST             5  'suitFiresDict'
              109  LOAD_FAST             7  'suitId'
              112  STORE_SUBSCR     
              113  JUMP_BACK            40  'to 40'
              116  POP_BLOCK        
            117_0  COME_FROM            33  '33'

 L.  86       117  LOAD_FAST             5  'suitFiresDict'
              120  LOAD_ATTR             9  'values'
              123  CALL_FUNCTION_0       0  None
              126  STORE_FAST           14  'suitFires'

 L.  88       129  LOAD_CODE                <code_object compFunc>
              132  MAKE_FUNCTION_0       0  None
              135  STORE_FAST           11  'compFunc'

 L.  94       138  LOAD_FAST            14  'suitFires'
              141  LOAD_ATTR            12  'sort'
              144  LOAD_FAST            11  'compFunc'
              147  CALL_FUNCTION_1       1  None
              150  POP_TOP          

 L.  98       151  BUILD_MAP             0 
              154  STORE_FAST           10  'totalHitDict'

 L.  99       157  BUILD_MAP             0 
              160  STORE_FAST            1  'singleHitDict'

 L. 100       163  BUILD_MAP             0 
              166  STORE_FAST            6  'groupHitDict'

 L. 102       169  SETUP_LOOP          124  'to 296'
              172  LOAD_FAST             0  'fires'
              175  GET_ITER         
              176  FOR_ITER            116  'to 295'
              179  STORE_FAST            4  'fire'

 L. 104       182  LOAD_FAST             4  'fire'
              185  LOAD_CONST               'target'
              188  BINARY_SUBSCR    
              189  LOAD_CONST               'suit'
              192  BINARY_SUBSCR    
              193  LOAD_ATTR             5  'doId'
              196  STORE_FAST            7  'suitId'

 L. 105       199  LOAD_FAST             4  'fire'
              202  LOAD_CONST               'target'
              205  BINARY_SUBSCR    
              206  LOAD_CONST               'hp'
              209  BINARY_SUBSCR    
              210  LOAD_CONST               0
              213  COMPARE_OP            4  >
              216  JUMP_IF_FALSE        36  'to 255'
              219  POP_TOP          

 L. 106       220  LOAD_GLOBAL          16  'addHit'
              223  LOAD_FAST             1  'singleHitDict'
              226  LOAD_FAST             7  'suitId'
              229  LOAD_CONST               1
              232  CALL_FUNCTION_3       3  None
              235  POP_TOP          

 L. 107       236  LOAD_GLOBAL          16  'addHit'
              239  LOAD_FAST            10  'totalHitDict'
              242  LOAD_FAST             7  'suitId'
              245  LOAD_CONST               1
              248  CALL_FUNCTION_3       3  None
              251  POP_TOP          
              252  JUMP_ABSOLUTE       292  'to 292'
            255_0  COME_FROM           216  '216'
              255  POP_TOP          

 L. 109       256  LOAD_GLOBAL          16  'addHit'
              259  LOAD_FAST             1  'singleHitDict'
              262  LOAD_FAST             7  'suitId'
              265  LOAD_CONST               0
              268  CALL_FUNCTION_3       3  None
              271  POP_TOP          

 L. 110       272  LOAD_GLOBAL          16  'addHit'
              275  LOAD_FAST            10  'totalHitDict'
              278  LOAD_FAST             7  'suitId'
              281  LOAD_CONST               0
              284  CALL_FUNCTION_3       3  None
              287  POP_TOP          
              288  JUMP_BACK           176  'to 176'
              291  POP_TOP          
              292  JUMP_BACK           176  'to 176'
              295  POP_BLOCK        
            296_0  COME_FROM           169  '169'

 L. 112       296  LOAD_GLOBAL          17  'notify'
              299  LOAD_ATTR            18  'debug'
              302  LOAD_CONST               'singleHitDict = %s'
              305  LOAD_FAST             1  'singleHitDict'
              308  BINARY_MODULO    
              309  CALL_FUNCTION_1       1  None
              312  POP_TOP          

 L. 113       313  LOAD_GLOBAL          17  'notify'
              316  LOAD_ATTR            18  'debug'
              319  LOAD_CONST               'groupHitDict = %s'
              322  LOAD_FAST             6  'groupHitDict'
              325  BINARY_MODULO    
              326  CALL_FUNCTION_1       1  None
              329  POP_TOP          

 L. 114       330  LOAD_GLOBAL          17  'notify'
              333  LOAD_ATTR            18  'debug'
              336  LOAD_CONST               'totalHitDict = %s'
              339  LOAD_FAST            10  'totalHitDict'
              342  BINARY_MODULO    
              343  CALL_FUNCTION_1       1  None
              346  POP_TOP          

 L. 118       347  LOAD_CONST               0.0
              350  STORE_FAST            3  'delay'

 L. 119       353  LOAD_GLOBAL          20  'Parallel'
              356  CALL_FUNCTION_0       0  None
              359  STORE_FAST            9  'mtrack'

 L. 120       362  BUILD_LIST_0          0 
              365  STORE_FAST           13  'firedTargets'

 L. 121       368  SETUP_LOOP           98  'to 469'
              371  LOAD_FAST            14  'suitFires'
              374  GET_ITER         
              375  FOR_ITER             90  'to 468'
              378  STORE_FAST           16  'sf'

 L. 122       381  LOAD_GLOBAL           0  'len'
              384  LOAD_FAST            16  'sf'
              387  CALL_FUNCTION_1       1  None
              390  LOAD_CONST               0
              393  COMPARE_OP            4  >
              396  JUMP_IF_FALSE        65  'to 464'
              399  POP_TOP          

 L. 123       400  LOAD_GLOBAL          24  '__doSuitFires'
              403  LOAD_FAST            16  'sf'
              406  CALL_FUNCTION_1       1  None
              409  STORE_FAST           15  'ival'

 L. 124       412  LOAD_FAST            15  'ival'
              415  JUMP_IF_FALSE        32  'to 450'
            418_0  THEN                     451
              418  POP_TOP          

 L. 125       419  LOAD_FAST             9  'mtrack'
              422  LOAD_ATTR             8  'append'
              425  LOAD_GLOBAL          26  'Sequence'
              428  LOAD_GLOBAL          27  'Wait'
              431  LOAD_FAST             3  'delay'
              434  CALL_FUNCTION_1       1  None
              437  LOAD_FAST            15  'ival'
              440  CALL_FUNCTION_2       2  None
              443  CALL_FUNCTION_1       1  None
              446  POP_TOP          
              447  JUMP_FORWARD          1  'to 451'
            450_0  COME_FROM           415  '415'
              450  POP_TOP          
            451_0  COME_FROM           447  '447'

 L. 126       451  LOAD_FAST             3  'delay'
              454  LOAD_GLOBAL          28  'TOON_FIRE_SUIT_DELAY'
              457  BINARY_ADD       
              458  STORE_FAST            3  'delay'
              461  JUMP_BACK           375  'to 375'
            464_0  COME_FROM           396  '396'
              464  POP_TOP          
              465  JUMP_BACK           375  'to 375'
              468  POP_BLOCK        
            469_0  COME_FROM           368  '368'

 L. 128       469  LOAD_GLOBAL          26  'Sequence'
              472  CALL_FUNCTION_0       0  None
              475  STORE_FAST            2  'retTrack'

 L. 129       478  LOAD_FAST             2  'retTrack'
              481  LOAD_ATTR             8  'append'
              484  LOAD_FAST             9  'mtrack'
              487  CALL_FUNCTION_1       1  None
              490  POP_TOP          

 L. 134       491  LOAD_FAST             2  'retTrack'
              494  LOAD_ATTR            30  'getDuration'
              497  CALL_FUNCTION_0       0  None
              500  STORE_FAST           12  'camDuration'

 L. 135       503  LOAD_GLOBAL          32  'MovieCamera'
              506  LOAD_ATTR            33  'chooseFireShot'
              509  LOAD_FAST             0  'fires'
              512  LOAD_FAST             5  'suitFiresDict'

 L. 136       515  LOAD_FAST            12  'camDuration'
              518  CALL_FUNCTION_3       3  None
              521  STORE_FAST            8  'camTrack'

 L. 137       524  LOAD_FAST             2  'retTrack'
              527  LOAD_FAST             8  'camTrack'
              530  BUILD_TUPLE_2         2 
              533  RETURN_VALUE     

Parse error at or near `POP_TOP' instruction at offset 291


def __doSuitFires(fires):
    toonTracks = Parallel()
    delay = 0.0
    hitCount = 0
    for fire in fires:
        if fire['target']['hp'] > 0:
            hitCount += 1
        else:
            break

    suitList = []
    for fire in fires:
        if fire['target']['suit'] not in suitList:
            suitList.append(fire['target']['suit'])

    for fire in fires:
        showSuitCannon = 1
        if fire['target']['suit'] not in suitList:
            showSuitCannon = 0
        else:
            suitList.remove(fire['target']['suit'])
        tracks = __throwPie(fire, delay, hitCount, showSuitCannon)
        if tracks:
            for track in tracks:
                toonTracks.append(track)

        delay = delay + TOON_THROW_DELAY

    return toonTracks


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
        notify.error('No such propType as: %s' % propType)


def __billboardProp(prop):
    scale = prop.getScale()
    prop.setBillboardPointWorld()
    prop.setScale(scale)


def __suitMissPoint(suit, other=render):
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

    targetPnt = MovieUtil.avatarFacePoint(suit, other=battle)
    prop.lookAt(targetPnt)


def __propPreflightGroup(props, suits, toon, battle):
    prop = props[0]
    toon.update(0)
    prop.wrtReparentTo(battle)
    props[1].reparentTo(hidden)
    for ci in range(prop.getNumChildren()):
        prop.getChild(ci).setHpr(0, -90, 0)

    avgTargetPt = Point3(0, 0, 0)
    for suit in suits:
        avgTargetPt += MovieUtil.avatarFacePoint(suit, other=battle)

    avgTargetPt /= len(suits)
    prop.lookAt(avgTargetPt)


def __piePreMiss(missDict, pie, suitPoint, other=render):
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


def __piePreMissGroup(missDict, pies, suitPoint, other=render):
    missDict['pies'] = pies
    missDict['startScale'] = pies[0].getScale()
    missDict['startPos'] = pies[0].getPos(other)
    v = Vec3(suitPoint - missDict['startPos'])
    endPos = missDict['startPos'] + v * ratioMissToHit
    missDict['endPos'] = endPos
    notify.debug('startPos=%s' % missDict['startPos'])
    notify.debug('v=%s' % v)
    notify.debug('endPos=%s' % missDict['endPos'])


def __pieMissGroupLerpCallback(t, missDict):
    pies = missDict['pies']
    newPos = missDict['startPos'] * (1.0 - t) + missDict['endPos'] * t
    if t < tPieShrink:
        tScale = 0.0001
    else:
        tScale = (t - tPieShrink) / (1.0 - tPieShrink)
    newScale = missDict['startScale'] * max(1.0 - tScale, 0.01)
    for pie in pies:
        pie.setPos(newPos)
        pie.setScale(newScale)


def __getSoundTrack(level, hitSuit, node=None):
    throwSound = globalBattleSoundCache.getSound('AA_drop_trigger_box.mp3')
    throwTrack = Sequence(Wait(2.15), SoundInterval(throwSound, node=node))
    return throwTrack


def __throwPie(throw, delay, hitCount, showCannon=1):
    toon = throw['toon']
    hpbonus = throw['hpbonus']
    target = throw['target']
    suit = target['suit']
    hp = target['hp']
    kbbonus = target['kbbonus']
    sidestep = throw['sidestep']
    died = target['died']
    revived = target['revived']
    leftSuits = target['leftSuits']
    rightSuits = target['rightSuits']
    level = throw['level']
    battle = throw['battle']
    suitPos = suit.getPos(battle)
    origHpr = toon.getHpr(battle)
    notify.debug('toon: %s throws tart at suit: %d for hp: %d died: %d' % (toon.getName(), suit.doId, hp, died))
    pieName = pieNames[0]
    hitSuit = hp > 0
    button = globalPropPool.getProp('button')
    buttonType = globalPropPool.getPropType('button')
    button2 = MovieUtil.copyProp(button)
    buttons = [button, button2]
    hands = toon.getLeftHands()
    toonTrack = Sequence()
    toonFace = Func(toon.headsUp, battle, suitPos)
    toonTrack.append(Wait(delay))
    toonTrack.append(toonFace)
    toonTrack.append(ActorInterval(toon, 'pushbutton'))
    toonTrack.append(ActorInterval(toon, 'wave', duration=2.0))
    toonTrack.append(ActorInterval(toon, 'duck'))
    toonTrack.append(Func(toon.loop, 'neutral'))
    toonTrack.append(Func(toon.setHpr, battle, origHpr))
    buttonTrack = Sequence()
    buttonShow = Func(MovieUtil.showProps, buttons, hands)
    buttonScaleUp = LerpScaleInterval(button, 1.0, button.getScale(), startScale=Point3(0.01, 0.01, 0.01))
    buttonScaleDown = LerpScaleInterval(button, 1.0, Point3(0.01, 0.01, 0.01), startScale=button.getScale())
    buttonHide = Func(MovieUtil.removeProps, buttons)
    buttonTrack.append(Wait(delay))
    buttonTrack.append(buttonShow)
    buttonTrack.append(buttonScaleUp)
    buttonTrack.append(Wait(2.5))
    buttonTrack.append(buttonScaleDown)
    buttonTrack.append(buttonHide)
    soundTrack = __getSoundTrack(level, hitSuit, toon)
    suitResponseTrack = Sequence()
    reactIval = Sequence()
    if showCannon:
        showDamage = Func(suit.showHpText, -hp, openEnded=0)
        updateHealthBar = Func(suit.updateHealthBar, hp)
        cannon = loader.loadModel('phase_4/models/minigames/toon_cannon')
        barrel = cannon.find('**/cannon')
        barrel.setHpr(0, 90, 0)
        cannonHolder = render.attachNewNode('CannonHolder')
        cannon.reparentTo(cannonHolder)
        cannon.setPos(0, 0, -8.6)
        cannonHolder.setPos(suit.getPos(render))
        cannonHolder.setHpr(suit.getHpr(render))
        cannonAttachPoint = barrel.attachNewNode('CannonAttach')
        kapowAttachPoint = barrel.attachNewNode('kapowAttach')
        scaleFactor = 1.6
        iScale = 1 / scaleFactor
        barrel.setScale(scaleFactor, 1, scaleFactor)
        cannonAttachPoint.setScale(iScale, 1, iScale)
        cannonAttachPoint.setPos(0, 6.7, 0)
        kapowAttachPoint.setPos(0, -0.5, 1.9)
        suit.reparentTo(cannonAttachPoint)
        suit.setPos(0, 0, 0)
        suit.setHpr(0, -90, 0)
        suitLevel = suit.getActualLevel()
        deep = 2.5 + suitLevel * 0.2
        suitScale = 0.9
        import math
        suitScale = 0.9 - math.sqrt(suitLevel) * 0.1
        sival = []
        posInit = cannonHolder.getPos()
        posFinal = Point3(posInit[0] + 0.0, posInit[1] + 0.0, posInit[2] + 7.0)
        kapow = globalPropPool.getProp('kapow')
        kapow.reparentTo(kapowAttachPoint)
        kapow.hide()
        kapow.setScale(0.25)
        kapow.setBillboardPointEye()
        smoke = loader.loadModel('phase_4/models/props/test_clouds')
        smoke.reparentTo(cannonAttachPoint)
        smoke.setScale(0.5)
        smoke.hide()
        smoke.setBillboardPointEye()
        soundBomb = base.loadSfx('phase_4/audio/sfx/MG_cannon_fire_alt.mp3')
        playSoundBomb = SoundInterval(soundBomb, node=cannonHolder)
        soundFly = base.loadSfx('phase_4/audio/sfx/firework_whistle_01.mp3')
        playSoundFly = SoundInterval(soundFly, node=cannonHolder)
        soundCannonAdjust = base.loadSfx('phase_4/audio/sfx/MG_cannon_adjust.mp3')
        playSoundCannonAdjust = SoundInterval(soundCannonAdjust, duration=0.6, node=cannonHolder)
        soundCogPanic = base.loadSfx('phase_5/audio/sfx/ENC_cogafssm.mp3')
        playSoundCogPanic = SoundInterval(soundCogPanic, node=cannonHolder)
        reactIval = Parallel(ActorInterval(suit, 'pie-small-react'), Sequence(Wait(0.0), LerpPosInterval(cannonHolder, 2.0, posFinal, startPos=posInit, blendType='easeInOut'), Parallel(LerpHprInterval(barrel, 0.6, Point3(0, 45, 0), startHpr=Point3(0, 90, 0), blendType='easeIn'), playSoundCannonAdjust), Wait(2.0), Parallel(LerpHprInterval(barrel, 0.6, Point3(0, 90, 0), startHpr=Point3(0, 45, 0), blendType='easeIn'), playSoundCannonAdjust), LerpPosInterval(cannonHolder, 1.0, posInit, startPos=posFinal, blendType='easeInOut')), Sequence(Wait(0.0), Parallel(ActorInterval(suit, 'flail'), suit.scaleInterval(1.0, suitScale), LerpPosInterval(suit, 0.25, Point3(0, -1.0, 0.0)), Sequence(Wait(0.25), Parallel(playSoundCogPanic, LerpPosInterval(suit, 1.5, Point3(0, -deep, 0.0), blendType='easeIn')))), Wait(2.5), Parallel(playSoundBomb, playSoundFly, Sequence(Func(smoke.show), Parallel(LerpScaleInterval(smoke, 0.5, 3), LerpColorScaleInterval(smoke, 0.5, Vec4(2, 2, 2, 0))), Func(smoke.hide)), Sequence(Func(kapow.show), ActorInterval(kapow, 'kapow'), Func(kapow.hide)), LerpPosInterval(suit, 3.0, Point3(0, 150.0, 0.0)), suit.scaleInterval(3.0, 0.01)), Func(suit.hide)))
        if hitCount == 1:
            sival = Sequence(Parallel(reactIval, MovieUtil.createSuitStunInterval(suit, 0.3, 1.3)), Wait(0.0), Func(cannonHolder.remove))
        else:
            sival = reactIval
        suitResponseTrack.append(Wait(delay + tPieHitsSuit))
        suitResponseTrack.append(showDamage)
        suitResponseTrack.append(updateHealthBar)
        suitResponseTrack.append(sival)
        bonusTrack = Sequence(Wait(delay + tPieHitsSuit))
        if kbbonus > 0:
            bonusTrack.append(Wait(0.75))
            bonusTrack.append(Func(suit.showHpText, -kbbonus, 2, openEnded=0))
        if hpbonus > 0:
            bonusTrack.append(Wait(0.75))
            bonusTrack.append(Func(suit.showHpText, -hpbonus, 1, openEnded=0))
        suitResponseTrack = Parallel(suitResponseTrack, bonusTrack)
    return [
     toonTrack, soundTrack, buttonTrack, suitResponseTrack]