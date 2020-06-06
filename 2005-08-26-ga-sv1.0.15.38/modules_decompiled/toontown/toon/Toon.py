# File: T (Python 2.2)

from otp.avatar import Avatar
import ToonDNA
from toontown.suit import SuitDNA
from direct.actor import Actor
import string
from ToonHead import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from otp.otpbase import OTPLocalizer
from toontown.toonbase import TTLocalizer
import random
from toontown.effects import Wake
import TTEmote
from otp.avatar import Emote
import Motion
from toontown.hood import ZoneUtil
from toontown.battle import SuitBattleGlobals
from otp.otpbase import OTPGlobals
SLEEP_STRING = TTLocalizer.ToonSleepString
DogDialogueArray = []
CatDialogueArray = []
HorseDialogueArray = []
RabbitDialogueArray = []
MouseDialogueArray = []
DuckDialogueArray = []
MonkeyDialogueArray = []
LegsAnimDict = { }
TorsoAnimDict = { }
HeadAnimDict = { }
Preloaded = []
Phase3AnimList = (('neutral', 'neutral'), ('run', 'run'))
Phase3_5AnimList = (('walk', 'walk'), ('teleport', 'teleport'), ('book', 'book'), ('jump', 'jump'), ('running-jump', 'running-jump'), ('jump-squat', 'jump-zstart'), ('jump-idle', 'jump-zhang'), ('jump-land', 'jump-zend'), ('running-jump-squat', 'leap_zstart'), ('running-jump-idle', 'leap_zhang'), ('running-jump-land', 'leap_zend'), ('pushbutton', 'press-button'), ('throw', 'pie-throw'), ('victory', 'victory-dance'), ('sidestep-left', 'sidestep-left'), ('conked', 'conked'), ('cringe', 'cringe'), ('wave', 'wave'), ('shrug', 'shrug'), ('angry', 'angry'), ('tutorial-neutral', 'tutorial-neutral'), ('left-point', 'left-point'), ('right-point', 'right-point'), ('right-point-start', 'right-point-start'), ('give-props', 'give-props'), ('give-props-start', 'give-props-start'), ('right-hand', 'right-hand'), ('right-hand-start', 'right-hand-start'), ('duck', 'duck'), ('sidestep-right', 'jump-back-right'), ('periscope', 'periscope'))
Phase4AnimList = (('sit', 'sit'), ('sit-start', 'intoSit'), ('swim', 'swim'), ('tug-o-war', 'tug-o-war'), ('sad-walk', 'losewalk'), ('sad-neutral', 'sad-neutral'), ('up', 'up'), ('down', 'down'), ('left', 'left'), ('right', 'right'), ('applause', 'applause'), ('confused', 'confused'), ('bow', 'bow'), ('curtsy', 'curtsy'), ('bored', 'bored'), ('think', 'think'), ('battlecast', 'fish'), ('cast', 'cast'), ('castlong', 'castlong'), ('fish-end', 'fishEND'), ('fish-neutral', 'fishneutral'), ('fish-again', 'fishAGAIN'), ('reel', 'reel'), ('reel-H', 'reelH'), ('reel-neutral', 'reelneutral'), ('pole', 'pole'), ('pole-neutral', 'poleneutral'), ('slip-forward', 'slip-forward'), ('slip-backward', 'slip-backward'), ('catch-neutral', 'gameneutral'), ('catch-run', 'gamerun'), ('catch-eatneutral', 'eat_neutral'), ('catch-eatnrun', 'eatnrun'), ('catch-intro-throw', 'gameThrow'), ('pet-start', 'petin'), ('pet-loop', 'petloop'), ('pet-end', 'petend'))
Phase5AnimList = (('water-gun', 'water-gun'), ('hold-bottle', 'hold-bottle'), ('firehose', 'firehose'), ('spit', 'spit'), ('tickle', 'tickle'), ('smooch', 'smooch'), ('happy-dance', 'happy-dance'), ('sprinkle-dust', 'sprinkle-dust'), ('juggle', 'juggle'), ('sound', 'shout'), ('toss', 'toss'), ('hold-magnet', 'hold-magnet'), ('hypnotize', 'hypnotize'), ('struggle', 'struggle'), ('lose', 'lose'), ('melt', 'melt'))
Phase5_5AnimList = (('takePhone', 'takePhone'), ('phoneNeutral', 'phoneNeutral'), ('phoneBack', 'phoneBack'), ('bank', 'jellybeanJar'), ('callPet', 'callPet'), ('feedPet', 'feedPet'))
Phase9AnimList = (('push', 'push'),)
Phase10AnimList = (('leverReach', 'leverReach'), ('leverPull', 'leverPull'), ('leverNeutral', 'leverNeutral'))
LegDict = {
    's': '/models/char/dogSS_Shorts-legs-',
    'm': '/models/char/dogMM_Shorts-legs-',
    'l': '/models/char/dogLL_Shorts-legs-' }
TorsoDict = {
    's': '/models/char/dogSS_Naked-torso-',
    'm': '/models/char/dogMM_Naked-torso-',
    'l': '/models/char/dogLL_Naked-torso-',
    'ss': '/models/char/dogSS_Shorts-torso-',
    'ms': '/models/char/dogMM_Shorts-torso-',
    'ls': '/models/char/dogLL_Shorts-torso-',
    'sd': '/models/char/dogSS_Skirt-torso-',
    'md': '/models/char/dogMM_Skirt-torso-',
    'ld': '/models/char/dogLL_Skirt-torso-' }

def loadModels():
    preloadAvatars = base.config.GetBool('preload-avatars', 0)
    if preloadAvatars:
        
        def loadTex(path):
            tex = loader.loadTexture(path)
            tex.setMinfilter(Texture.FTLinearMipmapLinear)
            tex.setMagfilter(Texture.FTLinear)
            Preloaded.append(tex)

        for shirt in ToonDNA.Shirts:
            loadTex(shirt)
        
        for sleeve in ToonDNA.Sleeves:
            loadTex(sleeve)
        
        for short in ToonDNA.BoyShorts:
            loadTex(short)
        
        for bottom in ToonDNA.GirlBottoms:
            loadTex(bottom[0])
        
        for key in LegDict.keys():
            fileRoot = LegDict[key]
            model = loader.loadModelNode('phase_3' + fileRoot + '1000')
            Preloaded.append(model)
            model = loader.loadModelNode('phase_3' + fileRoot + '500')
            Preloaded.append(model)
            model = loader.loadModelNode('phase_3' + fileRoot + '250')
            Preloaded.append(model)
        
        for key in TorsoDict.keys():
            fileRoot = TorsoDict[key]
            model = loader.loadModelNode('phase_3' + fileRoot + '1000')
            Preloaded.append(model)
            if len(key) > 1:
                model = loader.loadModelNode('phase_3' + fileRoot + '500')
                Preloaded.append(model)
                model = loader.loadModelNode('phase_3' + fileRoot + '250')
                Preloaded.append(model)
            
        
        for key in HeadDict.keys():
            fileRoot = HeadDict[key]
            model = loader.loadModelNode('phase_3' + fileRoot + '1000')
            Preloaded.append(model)
            model = loader.loadModelNode('phase_3' + fileRoot + '500')
            Preloaded.append(model)
            model = loader.loadModelNode('phase_3' + fileRoot + '250')
            Preloaded.append(model)
        
    


def loadBasicAnims():
    loadPhaseAnims()


def unloadBasicAnims():
    loadPhaseAnims(0)


def loadTutorialBattleAnims():
    loadPhaseAnims('phase_3.5')


def unloadTutorialBattleAnims():
    loadPhaseAnims('phase_3.5', 0)


def loadMinigameAnims():
    loadPhaseAnims('phase_4')


def unloadMinigameAnims():
    loadPhaseAnims('phase_4', 0)


def loadBattleAnims():
    loadPhaseAnims('phase_5')


def unloadBattleAnims():
    loadPhaseAnims('phase_5', 0)


def loadSellbotHQAnims():
    loadPhaseAnims('phase_9')


def unloadSellbotHQAnims():
    loadPhaseAnims('phase_9', 0)


def loadCashbotHQAnims():
    loadPhaseAnims('phase_10')


def unloadCashbotHQAnims():
    loadPhaseAnims('phase_10', 0)


def loadPhaseAnims(phaseStr = 'phase_3', loadFlag = 1):
    if phaseStr == 'phase_3':
        animList = Phase3AnimList
    elif phaseStr == 'phase_3.5':
        animList = Phase3_5AnimList
    elif phaseStr == 'phase_4':
        animList = Phase4AnimList
    elif phaseStr == 'phase_5':
        animList = Phase5AnimList
    elif phaseStr == 'phase_5.5':
        animList = Phase5_5AnimList
    elif phaseStr == 'phase_9':
        animList = Phase9AnimList
    elif phaseStr == 'phase_10':
        animList = Phase10AnimList
    else:
        self.notify.error('Unknown phase string %s' % phaseStr)
    for key in LegDict.keys():
        for anim in animList:
            if loadFlag:
                pass
            1
            if LegsAnimDict[key].has_key(anim[0]):
                if base.localAvatar.style.legs == key:
                    base.localAvatar.unloadAnims([
                        anim[0]], 'legs', None)
                
            
        
    
    for key in TorsoDict.keys():
        for anim in animList:
            if loadFlag:
                pass
            1
            if TorsoAnimDict[key].has_key(anim[0]):
                if base.localAvatar.style.torso == key:
                    base.localAvatar.unloadAnims([
                        anim[0]], 'torso', None)
                
            
        
    
    for key in HeadDict.keys():
        if string.find(key, 'd') >= 0:
            for anim in animList:
                if loadFlag:
                    pass
                1
                if HeadAnimDict[key].has_key(anim[0]):
                    if base.localAvatar.style.head == key:
                        base.localAvatar.unloadAnims([
                            anim[0]], 'head', None)
                    
                
            
        
    


def compileGlobalAnimList():
    phaseList = [
        Phase3AnimList,
        Phase3_5AnimList,
        Phase4AnimList,
        Phase5AnimList,
        Phase5_5AnimList,
        Phase9AnimList,
        Phase10AnimList]
    phaseStrList = [
        'phase_3',
        'phase_3.5',
        'phase_4',
        'phase_5',
        'phase_5.5',
        'phase_9',
        'phase_10']
    for animList in phaseList:
        phaseStr = phaseStrList[phaseList.index(animList)]
        for key in LegDict.keys():
            LegsAnimDict.setdefault(key, { })
            for anim in animList:
                file = phaseStr + LegDict[key] + anim[1]
                LegsAnimDict[key][anim[0]] = file
            
        
        for key in TorsoDict.keys():
            TorsoAnimDict.setdefault(key, { })
            for anim in animList:
                file = phaseStr + TorsoDict[key] + anim[1]
                TorsoAnimDict[key][anim[0]] = file
            
        
        for key in HeadDict.keys():
            if string.find(key, 'd') >= 0:
                HeadAnimDict.setdefault(key, { })
                for anim in animList:
                    file = phaseStr + HeadDict[key] + anim[1]
                    HeadAnimDict[key][anim[0]] = file
                
            
        
    


def loadDialog():
    loadPath = 'phase_3.5/audio/dial/'
    DogDialogueFiles = ('AV_dog_short', 'AV_dog_med', 'AV_dog_long', 'AV_dog_question', 'AV_dog_exclaim', 'AV_dog_howl')
    for file in DogDialogueFiles:
        DogDialogueArray.append(base.loadSfx(loadPath + file + '.mp3'))
    
    catDialogueFiles = ('AV_cat_short', 'AV_cat_med', 'AV_cat_long', 'AV_cat_question', 'AV_cat_exclaim', 'AV_cat_howl')
    for file in catDialogueFiles:
        CatDialogueArray.append(base.loadSfx(loadPath + file + '.mp3'))
    
    horseDialogueFiles = ('AV_horse_short', 'AV_horse_med', 'AV_horse_long', 'AV_horse_question', 'AV_horse_exclaim', 'AV_horse_howl')
    for file in horseDialogueFiles:
        HorseDialogueArray.append(base.loadSfx(loadPath + file + '.mp3'))
    
    rabbitDialogueFiles = ('AV_rabbit_short', 'AV_rabbit_med', 'AV_rabbit_long', 'AV_rabbit_question', 'AV_rabbit_exclaim', 'AV_rabbit_howl')
    for file in rabbitDialogueFiles:
        RabbitDialogueArray.append(base.loadSfx(loadPath + file + '.mp3'))
    
    mouseDialogueFiles = ('AV_mouse_short', 'AV_mouse_med', 'AV_mouse_long', 'AV_mouse_question', 'AV_mouse_exclaim', 'AV_mouse_howl')
    for file in mouseDialogueFiles:
        MouseDialogueArray.append(base.loadSfx(loadPath + file + '.mp3'))
    
    duckDialogueFiles = ('AV_duck_short', 'AV_duck_med', 'AV_duck_long', 'AV_duck_question', 'AV_duck_exclaim', 'AV_duck_howl')
    for file in duckDialogueFiles:
        DuckDialogueArray.append(base.loadSfx(loadPath + file + '.mp3'))
    
    monkeyDialogueFiles = ('AV_monkey_short', 'AV_monkey_med', 'AV_monkey_long', 'AV_monkey_question', 'AV_monkey_exclaim', 'AV_monkey_howl')
    for file in monkeyDialogueFiles:
        MonkeyDialogueArray.append(base.loadSfx(loadPath + file + '.mp3'))
    


def unloadDialog():
    global DogDialogueArray, CatDialogueArray, HorseDialogueArray, RabbitDialogueArray, MouseDialogueArray, DuckDialogueArray, MonkeyDialogueArray
    DogDialogueArray = []
    CatDialogueArray = []
    HorseDialogueArray = []
    RabbitDialogueArray = []
    MouseDialogueArray = []
    DuckDialogueArray = []
    MonkeyDialogueArray = []


class Toon(Avatar.Avatar, ToonHead):
    notify = DirectNotifyGlobal.directNotify.newCategory('Toon')
    afkTimeout = base.config.GetInt('afk-timeout', 600)
    
    def __init__(self):
        
        try:
            return None
        except:
            self.Toon_initialized = 1

        Avatar.Avatar.__init__(self)
        ToonHead.__init__(self)
        self.forwardSpeed = 0.0
        self.rotateSpeed = 0.0
        self.avatarType = 'toon'
        self.motion = Motion.Motion(self)
        self.standWalkRunReverse = None
        self.playingAnim = None
        self.soundTeleport = None
        self.cheesyEffect = ToontownGlobals.CENormal
        self.effectTrack = None
        self.emoteTrack = None
        self.emote = None
        self.stunTrack = None
        self._Toon__bookActors = []
        self._Toon__holeActors = []
        self.holeClipPath = None
        self.wake = None
        self.lastWakeTime = 0
        self.numPies = 0
        self.pieType = 0
        self.pieModel = None
        self._Toon__pieModelType = None
        self.isStunned = 0
        self.isDisguised = 0
        self.defaultColorScale = None
        self.jar = None
        self.setTag('pieCode', str(ToontownGlobals.PieCodeToon))
        self.setFont(ToontownGlobals.getToonFont())
        self.soundChatBubble = base.loadSfx('phase_3/audio/sfx/GUI_balloon_popup.mp3')
        self.animFSM = ClassicFSM('Toon', [
            State('off', self.enterOff, self.exitOff),
            State('neutral', self.enterNeutral, self.exitNeutral),
            State('victory', self.enterVictory, self.exitVictory),
            State('Happy', self.enterHappy, self.exitHappy),
            State('Sad', self.enterSad, self.exitSad),
            State('Catching', self.enterCatching, self.exitCatching),
            State('CatchEating', self.enterCatchEating, self.exitCatchEating),
            State('Sleep', self.enterSleep, self.exitSleep),
            State('walk', self.enterWalk, self.exitWalk),
            State('jumpSquat', self.enterJumpSquat, self.exitJumpSquat),
            State('jump', self.enterJump, self.exitJump),
            State('jumpAirborne', self.enterJumpAirborne, self.exitJumpAirborne),
            State('jumpLand', self.enterJumpLand, self.exitJumpLand),
            State('run', self.enterRun, self.exitRun),
            State('swim', self.enterSwim, self.exitSwim),
            State('OpenBook', self.enterOpenBook, self.exitOpenBook),
            State('ReadBook', self.enterReadBook, self.exitReadBook),
            State('CloseBook', self.enterCloseBook, self.exitCloseBook),
            State('TeleportOut', self.enterTeleportOut, self.exitTeleportOut),
            State('Died', self.enterDied, self.exitDied),
            State('TeleportedOut', self.enterTeleportedOut, self.exitTeleportedOut),
            State('TeleportIn', self.enterTeleportIn, self.exitTeleportIn),
            State('Emote', self.enterEmote, self.exitEmote),
            State('SitStart', self.enterSitStart, self.exitSitStart),
            State('Sit', self.enterSit, self.exitSit),
            State('Push', self.enterPush, self.exitPush),
            State('Squish', self.enterSquish, self.exitSquish),
            State('FallDown', self.enterFallDown, self.exitFallDown)], 'off', 'off')
        self.animFSM.enterInitialState()

    
    def stopAnimations(self):
        self.animFSM.request('off')
        if self.emoteTrack != None:
            self.emoteTrack.finish()
            self.emoteTrack = None
        
        if self.stunTrack != None:
            self.stunTrack.finish()
            self.stunTrack = None
        
        if self.wake:
            self.wake.stop()
            self.wake.destroy()
            self.wake = None
        
        self.cleanupPieModel()

    
    def delete(self):
        
        try:
            pass
        except:
            self.Toon_deleted = 1
            self.stopAnimations()
            self.rightHands = None
            self.rightHand = None
            self.leftHands = None
            self.leftHand = None
            self.headParts = None
            self.torsoParts = None
            self.hipsParts = None
            self.legsParts = None
            del self.animFSM
            for bookActor in self._Toon__bookActors:
                bookActor.cleanup()
            
            del self._Toon__bookActors
            for holeActor in self._Toon__holeActors:
                holeActor.cleanup()
            
            del self._Toon__holeActors
            self.soundTeleport = None
            self.motion.delete()
            self.motion = None
            Avatar.Avatar.delete(self)
            ToonHead.delete(self)


    
    def updateToonDNA(self, newDNA, fForce = 0):
        self.style.gender = newDNA.getGender()
        oldDNA = self.style
        if fForce or newDNA.head != oldDNA.head:
            self.swapToonHead(newDNA.head)
        
        if fForce or newDNA.torso != oldDNA.torso:
            self.swapToonTorso(newDNA.torso, genClothes = 0)
            self.loop('neutral')
        
        if fForce or newDNA.legs != oldDNA.legs:
            self.swapToonLegs(newDNA.legs)
        
        self.swapToonColor(newDNA)
        self._Toon__swapToonClothes(newDNA)

    
    def setDNAString(self, dnaString):
        newDNA = ToonDNA.ToonDNA()
        newDNA.makeFromNetString(dnaString)
        self.setDNA(newDNA)

    
    def setDNA(self, dna):
        if hasattr(self, 'isDisguised'):
            if self.isDisguised:
                return None
            
        
        if self.style:
            self.updateToonDNA(dna)
        else:
            self.style = dna
            self.generateToon()
            self.initializeDropShadow()
            self.initializeNametag3d()

    
    def parentToonParts(self):
        if self.hasLOD():
            for lodName in self.getLODNames():
                self.attach('head', 'torso', 'joint-head', lodName)
                self.attach('torso', 'legs', 'joint-hips', lodName)
            
        else:
            self.attach('head', 'torso', 'joint-head')
            self.attach('torso', 'legs', 'joint-hips')

    
    def unparentToonParts(self):
        if self.hasLOD():
            for lodName in self.getLODNames():
                self.getPart('head', lodName).reparentTo(self.getLOD(lodName))
                self.getPart('torso', lodName).reparentTo(self.getLOD(lodName))
                self.getPart('legs', lodName).reparentTo(self.getLOD(lodName))
            
        else:
            self.getPart('head').reparentTo(self.getGeomNode())
            self.getPart('torso').reparentTo(self.getGeomNode())
            self.getPart('legs').reparentTo(self.getGeomNode())

    
    def setLODs(self):
        self.setLODNode()
        levelOneIn = base.config.GetInt('lod1-in', 20)
        levelOneOut = base.config.GetInt('lod1-out', 0)
        levelTwoIn = base.config.GetInt('lod2-in', 80)
        levelTwoOut = base.config.GetInt('lod2-out', 20)
        levelThreeIn = base.config.GetInt('lod3-in', 280)
        levelThreeOut = base.config.GetInt('lod3-out', 80)
        self.addLOD(250, levelThreeIn, levelThreeOut)
        self.addLOD(500, levelTwoIn, levelTwoOut)
        self.addLOD(1000, levelOneIn, levelOneOut)

    
    def generateToon(self):
        self.setLODs()
        self.generateToonLegs()
        self.generateToonHead()
        self.generateToonTorso()
        self.generateToonColor()
        self.parentToonParts()
        self.rescaleToon()
        self.resetHeight()
        self.setupToonNodes()

    
    def setupToonNodes(self):
        rightHand = NodePath('rightHand')
        self.rightHand = None
        self.rightHands = []
        leftHand = NodePath('leftHand')
        self.leftHands = []
        self.leftHand = None
        for lodName in self.getLODNames():
            hand = self.getPart('torso', lodName).find('**/joint-Rhold')
            self.rightHands.append(hand)
            rightHand = rightHand.instanceTo(hand)
            hand = self.getPart('torso', lodName).find('**/joint-Lhold')
            self.leftHands.append(hand)
            leftHand = leftHand.instanceTo(hand)
            if self.rightHand == None:
                self.rightHand = rightHand
            
            if self.leftHand == None:
                self.leftHand = leftHand
            
        
        self.headParts = self.findAllMatches('**/__Actor_head')
        self.legsParts = self.findAllMatches('**/__Actor_legs')
        self.hipsParts = self.legsParts.findAllMatches('**/joint-hips')
        self.torsoParts = self.hipsParts.findAllMatches('**/__Actor_torso')

    
    def getBookActors(self):
        if self._Toon__bookActors:
            return self._Toon__bookActors
        
        bookActor = Actor.Actor('phase_3.5/models/props/book-mod', {
            'book': 'phase_3.5/models/props/book-chan' })
        bookActor2 = Actor.Actor(other = bookActor)
        bookActor3 = Actor.Actor(other = bookActor)
        self._Toon__bookActors = [
            bookActor,
            bookActor2,
            bookActor3]
        hands = self.getRightHands()
        for (bookActor, hand) in zip(self._Toon__bookActors, hands):
            bookActor.reparentTo(hand)
            bookActor.hide()
        
        return self._Toon__bookActors

    
    def getHoleActors(self):
        if self._Toon__holeActors:
            return self._Toon__holeActors
        
        holeActor = Actor.Actor('phase_3.5/models/props/portal-mod', {
            'hole': 'phase_3.5/models/props/portal-chan' })
        holeActor2 = Actor.Actor(other = holeActor)
        holeActor3 = Actor.Actor(other = holeActor)
        self._Toon__holeActors = [
            holeActor,
            holeActor2,
            holeActor3]
        return self._Toon__holeActors

    
    def rescaleToon(self):
        animalStyle = self.style.getAnimal()
        bodyScale = ToontownGlobals.toonBodyScales[animalStyle]
        headScale = ToontownGlobals.toonHeadScales[animalStyle]
        self.setAvatarScale(bodyScale)
        for lod in self.getLODNames():
            self.getPart('head', lod).setScale(headScale)
        

    
    def resetHeight(self):
        animal = self.style.getAnimal()
        bodyScale = ToontownGlobals.toonBodyScales[animal]
        headScale = ToontownGlobals.toonHeadScales[animal][2]
        shoulderHeight = ToontownGlobals.legHeightDict[self.style.legs] * bodyScale + ToontownGlobals.torsoHeightDict[self.style.torso] * bodyScale
        height = shoulderHeight + ToontownGlobals.headHeightDict[self.style.head] * headScale
        self.shoulderHeight = shoulderHeight
        if self.cheesyEffect == ToontownGlobals.CEBigToon:
            height *= ToontownGlobals.BigToonScale
        elif self.cheesyEffect == ToontownGlobals.CESmallToon:
            height *= ToontownGlobals.SmallToonScale
        
        self.setHeight(height)

    
    def generateToonLegs(self, copy = 1):
        legStyle = self.style.legs
        filePrefix = LegDict.get(legStyle)
        if filePrefix is None:
            self.notify.error('unknown leg style: %s' % legStyle)
        
        self.loadModel('phase_3' + filePrefix + '1000', 'legs', '1000', copy)
        self.loadModel('phase_3' + filePrefix + '500', 'legs', '500', copy)
        self.loadModel('phase_3' + filePrefix + '250', 'legs', '250', copy)
        if not copy:
            self.showPart('legs', '1000')
            self.showPart('legs', '500')
            self.showPart('legs', '250')
        
        self.loadAnims(LegsAnimDict[legStyle], 'legs', '1000')
        self.loadAnims(LegsAnimDict[legStyle], 'legs', '500')
        self.loadAnims(LegsAnimDict[legStyle], 'legs', '250')

    
    def swapToonLegs(self, legStyle, copy = 1):
        self.unparentToonParts()
        self.removePart('legs', '1000')
        self.removePart('legs', '500')
        self.removePart('legs', '250')
        self.style.legs = legStyle
        self.generateToonLegs(copy)
        self.generateToonColor()
        self.parentToonParts()
        self.rescaleToon()
        self.resetHeight()
        del self.shadowJoint
        self.initializeDropShadow()
        self.initializeNametag3d()

    
    def generateToonTorso(self, copy = 1, genClothes = 1):
        torsoStyle = self.style.torso
        filePrefix = TorsoDict.get(torsoStyle)
        if filePrefix is None:
            self.notify.error('unknown torso style: %s' % torsoStyle)
        
        self.loadModel('phase_3' + filePrefix + '1000', 'torso', '1000', copy)
        if len(torsoStyle) == 1:
            self.loadModel('phase_3' + filePrefix + '1000', 'torso', '500', copy)
            self.loadModel('phase_3' + filePrefix + '1000', 'torso', '250', copy)
        else:
            self.loadModel('phase_3' + filePrefix + '500', 'torso', '500', copy)
            self.loadModel('phase_3' + filePrefix + '250', 'torso', '250', copy)
        if not copy:
            self.showPart('torso', '1000')
            self.showPart('torso', '500')
            self.showPart('torso', '250')
        
        self.loadAnims(TorsoAnimDict[torsoStyle], 'torso', '1000')
        self.loadAnims(TorsoAnimDict[torsoStyle], 'torso', '500')
        self.loadAnims(TorsoAnimDict[torsoStyle], 'torso', '250')
        if genClothes == 1 and not (len(torsoStyle) == 1):
            self.generateToonClothes()
        

    
    def swapToonTorso(self, torsoStyle, copy = 1, genClothes = 1):
        self.unparentToonParts()
        self.removePart('torso', '1000')
        self.removePart('torso', '500')
        self.removePart('torso', '250')
        self.style.torso = torsoStyle
        self.generateToonTorso(copy, genClothes)
        self.generateToonColor()
        self.parentToonParts()
        self.rescaleToon()
        self.resetHeight()
        self.setupToonNodes()

    
    def generateToonHead(self, copy = 1):
        headHeight = ToonHead.generateToonHead(self, copy, self.style, ('1000', '500', '250'))
        if self.style.getAnimal() == 'dog':
            self.loadAnims(HeadAnimDict[self.style.head], 'head', '1000')
            self.loadAnims(HeadAnimDict[self.style.head], 'head', '500')
            self.loadAnims(HeadAnimDict[self.style.head], 'head', '250')
        

    
    def swapToonHead(self, headStyle, copy = 1):
        self.stopLookAroundNow()
        self.eyelids.request('open')
        self.unparentToonParts()
        self.removePart('head', '1000')
        self.removePart('head', '500')
        self.removePart('head', '250')
        self.style.head = headStyle
        self.generateToonHead(copy)
        self.generateToonColor()
        self.parentToonParts()
        self.rescaleToon()
        self.resetHeight()
        self.eyelids.request('open')
        self.startLookAround()

    
    def generateToonColor(self):
        ToonHead.generateToonColor(self, self.style)
        armColor = self.style.getArmColor()
        gloveColor = self.style.getGloveColor()
        legColor = self.style.getLegColor()
        for lodName in self.getLODNames():
            torso = self.getPart('torso', lodName)
            if len(self.style.torso) == 1:
                parts = torso.findAllMatches('**/torso*')
                parts.setColor(armColor)
            
            for pieceName in ('arms', 'neck'):
                piece = torso.find(pieceName)
                piece.setColor(armColor)
            
            hands = torso.find('hands')
            hands.setColor(gloveColor)
            legs = self.getPart('legs', lodName)
            for pieceName in ('legs', 'feet'):
                piece = legs.find(pieceName)
                piece.setColor(legColor)
            
        

    
    def swapToonColor(self, dna):
        self.setStyle(dna)
        self.generateToonColor()

    
    def _Toon__swapToonClothes(self, dna):
        self.setStyle(dna)
        self.generateToonClothes(fromNet = 1)

    
    def generateToonClothes(self, fromNet = 0):
        swappedTorso = 0
        if self.hasLOD():
            if self.style.getGender() == 'f' and fromNet == 0:
                
                try:
                    bottomPair = ToonDNA.GirlBottoms[self.style.botTex]
                except:
                    bottomPair = ToonDNA.GirlBottoms[0]

                if self.style.torso[1] == 's' and bottomPair[1] == ToonDNA.SKIRT:
                    self.swapToonTorso(self.style.torso[0] + 'd', genClothes = 0)
                    swappedTorso = 1
                elif self.style.torso[1] == 'd' and bottomPair[1] == ToonDNA.SHORTS:
                    self.swapToonTorso(self.style.torso[0] + 's', genClothes = 0)
                    swappedTorso = 1
                
            
            
            try:
                texName = ToonDNA.Shirts[self.style.topTex]
            except:
                texName = ToonDNA.Shirts[0]

            shirtTex = loader.loadTexture(texName)
            shirtTex.setMinfilter(Texture.FTLinearMipmapLinear)
            shirtTex.setMagfilter(Texture.FTLinear)
            
            try:
                shirtColor = ToonDNA.ClothesColors[self.style.topTexColor]
            except:
                shirtColor = ToonDNA.ClothesColors[0]

            
            try:
                texName = ToonDNA.Sleeves[self.style.sleeveTex]
            except:
                texName = ToonDNA.Sleeves[0]

            sleeveTex = loader.loadTexture(texName)
            sleeveTex.setMinfilter(Texture.FTLinearMipmapLinear)
            sleeveTex.setMagfilter(Texture.FTLinear)
            
            try:
                sleeveColor = ToonDNA.ClothesColors[self.style.sleeveTexColor]
            except:
                sleeveColor = ToonDNA.ClothesColors[0]

            if self.style.getGender() == 'm':
                
                try:
                    texName = ToonDNA.BoyShorts[self.style.botTex]
                except:
                    texName = ToonDNA.BoyShorts[0]

            else:
                
                try:
                    texName = ToonDNA.GirlBottoms[self.style.botTex][0]
                except:
                    texName = ToonDNA.GirlBottoms[0][0]

            bottomTex = loader.loadTexture(texName)
            bottomTex.setMinfilter(Texture.FTLinearMipmapLinear)
            bottomTex.setMagfilter(Texture.FTLinear)
            
            try:
                bottomColor = ToonDNA.ClothesColors[self.style.botTexColor]
            except:
                bottomColor = ToonDNA.ClothesColors[0]

            darkBottomColor = bottomColor * 0.5
            darkBottomColor.setW(1.0)
            for lodName in self.getLODNames():
                thisPart = self.getPart('torso', lodName)
                top = thisPart.find('**/torso-top')
                top.setTexture(shirtTex, 1)
                top.setColor(shirtColor)
                sleeves = thisPart.find('**/sleeves')
                sleeves.setTexture(sleeveTex, 1)
                sleeves.setColor(sleeveColor)
                bottoms = thisPart.findAllMatches('**/torso-bot')
                for bottomNum in range(0, bottoms.getNumPaths()):
                    bottom = bottoms.getPath(bottomNum)
                    bottom.setTexture(bottomTex, 1)
                    bottom.setColor(bottomColor)
                
                caps = thisPart.findAllMatches('**/torso-bot-cap')
                caps.setColor(darkBottomColor)
            
        
        return swappedTorso

    
    def getDialogueArray(self):
        animalType = self.style.getType()
        if animalType == 'dog':
            dialogueArray = DogDialogueArray
        elif animalType == 'cat':
            dialogueArray = CatDialogueArray
        elif animalType == 'horse':
            dialogueArray = HorseDialogueArray
        elif animalType == 'mouse':
            dialogueArray = MouseDialogueArray
        elif animalType == 'rabbit':
            dialogueArray = RabbitDialogueArray
        elif animalType == 'duck':
            dialogueArray = DuckDialogueArray
        elif animalType == 'monkey':
            dialogueArray = MonkeyDialogueArray
        else:
            dialogueArray = None
        return dialogueArray

    
    def getShadowJoint(self):
        if hasattr(self, 'shadowJoint'):
            return self.shadowJoint
        
        shadowJoint = NodePath('shadowJoint')
        for lodName in self.getLODNames():
            joint = self.getPart('legs', lodName).find('**/joint-shadow')
            shadowJoint = shadowJoint.instanceTo(joint)
        
        self.shadowJoint = shadowJoint
        return shadowJoint

    
    def getNametagJoints(self):
        joints = []
        for lodName in self.getLODNames():
            char = self.getPart('legs', lodName).node()
            joint = char.getBundle().findChild('joint-nameTag')
            if joint:
                joints.append(joint)
            
        
        return joints

    
    def getRightHands(self):
        return self.rightHands

    
    def getLeftHands(self):
        return self.leftHands

    
    def getHeadParts(self):
        return self.headParts

    
    def getHipsParts(self):
        return self.hipsParts

    
    def getTorsoParts(self):
        return self.torsoParts

    
    def getLegsParts(self):
        return self.legsParts

    
    def findSomethingToLookAt(self):
        if self.randGen.random() < 0.10000000000000001 or not hasattr(self, 'cr'):
            x = self.randGen.choice((-0.80000000000000004, -0.5, 0, 0.5, 0.80000000000000004))
            y = self.randGen.choice((-0.5, 0, 0.5, 0.80000000000000004))
            self.lerpLookAt(Point3(x, 1.5, y), blink = 1)
            return None
        
        nodePathList = []
        for (id, obj) in self.cr.doId2do.items():
            if hasattr(obj, 'getStareAtNodeAndOffset') and obj != self:
                (node, offset) = obj.getStareAtNodeAndOffset()
                if node.getY(self) > 0.0:
                    nodePathList.append((node, offset))
                
            
        
        if nodePathList:
            nodePathList.sort(lambda x, y: cmp(x[0].getDistance(self), y[0].getDistance(self)))
            if len(nodePathList) >= 2:
                if self.randGen.random() < 0.90000000000000002:
                    chosenNodePath = nodePathList[0]
                else:
                    chosenNodePath = nodePathList[1]
            else:
                chosenNodePath = nodePathList[0]
            self.lerpLookAt(chosenNodePath[0].getPos(self), blink = 1)
        else:
            ToonHead.findSomethingToLookAt(self)

    
    def setupPickTrigger(self):
        Avatar.Avatar.setupPickTrigger(self)
        torso = self.getPart('torso', '1000')
        if torso == None:
            return 0
        
        self.pickTriggerNp.reparentTo(torso)
        size = self.style.getTorsoSize()
        if size == 'short':
            self.pickTriggerNp.setPosHprScale(0, 0, 0.5, 0, 0, 0, 1.5, 1.5, 2)
        elif size == 'medium':
            self.pickTriggerNp.setPosHprScale(0, 0, 0.5, 0, 0, 0, 1, 1, 2)
        else:
            self.pickTriggerNp.setPosHprScale(0, 0, 1, 0, 0, 0, 1, 1, 2)
        return 1

    
    def showBooks(self):
        for bookActor in self.getBookActors():
            bookActor.show()
        

    
    def hideBooks(self):
        for bookActor in self.getBookActors():
            bookActor.hide()
        

    
    def getWake(self):
        if not (self.wake):
            self.wake = Wake.Wake(render, self)
        
        return self.wake

    
    def getJar(self):
        if not (self.jar):
            self.jar = loader.loadModelOnce('phase_5.5/models/estate/jellybeanJar')
            self.jar.setP(290.0)
            self.jar.setY(0.5)
            self.jar.setZ(0.5)
            self.jar.setScale(0.0)
        
        return self.jar

    
    def removeJar(self):
        if self.jar:
            self.jar.removeNode()
            self.jar = None
        

    
    def setSpeed(self, forwardSpeed, rotateSpeed):
        self.forwardSpeed = forwardSpeed
        self.rotateSpeed = rotateSpeed
        action = None
        if self.standWalkRunReverse != None:
            if forwardSpeed >= ToontownGlobals.RunCutOff:
                action = OTPGlobals.RUN_INDEX
            elif forwardSpeed > ToontownGlobals.WalkCutOff:
                action = OTPGlobals.WALK_INDEX
            elif forwardSpeed < -(ToontownGlobals.WalkCutOff):
                action = OTPGlobals.REVERSE_INDEX
            elif rotateSpeed != 0.0:
                action = OTPGlobals.WALK_INDEX
            else:
                action = OTPGlobals.STAND_INDEX
            (anim, rate) = self.standWalkRunReverse[action]
            self.motion.enter()
            self.motion.setState(anim, rate)
            if anim != self.playingAnim:
                self.playingAnim = anim
                self.playingRate = rate
                self.stop()
                self.loop(anim)
                self.setPlayRate(rate, anim)
                if self.isDisguised:
                    self.suit.stop()
                    self.suit.loop(anim)
                    self.suit.setPlayRate(rate, anim)
                
            elif rate != self.playingRate:
                self.playingRate = rate
                if not (self.isDisguised):
                    self.setPlayRate(rate, anim)
                else:
                    self.suit.setPlayRate(rate, anim)
            
            (showWake, wakeWaterHeight) = ZoneUtil.getWakeInfo()
            if showWake and self.getZ(render) < wakeWaterHeight and abs(forwardSpeed) > ToontownGlobals.WalkCutOff:
                currT = globalClock.getFrameTime()
                deltaT = currT - self.lastWakeTime
                if action == OTPGlobals.RUN_INDEX and deltaT > ToontownGlobals.WakeRunDelta or deltaT > ToontownGlobals.WakeWalkDelta:
                    self.getWake().createRipple(wakeWaterHeight, rate = 1, startFrame = 4)
                    self.lastWakeTime = currT
                
            
        
        return action

    
    def enterOff(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        self.setActiveShadow(0)
        self.playingAnim = None

    
    def exitOff(self):
        pass

    
    def enterNeutral(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        anim = 'neutral'
        self.pose(anim, int(self.getNumFrames(anim) * self.randGen.random()))
        self.loop(anim, restart = 0)
        self.setPlayRate(animMultiplier, anim)
        self.playingAnim = anim
        self.setActiveShadow(0)

    
    def exitNeutral(self):
        self.stop()

    
    def enterVictory(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        anim = 'victory'
        frame = int(ts * self.getFrameRate(anim) * animMultiplier)
        self.pose(anim, frame)
        self.loop('victory', restart = 0)
        self.setPlayRate(animMultiplier, 'victory')
        self.playingAnim = anim
        self.setActiveShadow(0)

    
    def exitVictory(self):
        self.stop()

    
    def enterHappy(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        self.playingAnim = None
        self.playingRate = None
        self.standWalkRunReverse = (('neutral', 1.0), ('walk', 1.0), ('run', 1.0), ('walk', -1.0))
        self.setSpeed(self.forwardSpeed, self.rotateSpeed)
        self.setActiveShadow(1)

    
    def exitHappy(self):
        self.standWalkRunReverse = None
        self.stop()
        self.motion.exit()

    
    def enterSad(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        self.playingAnim = 'sad'
        self.playingRate = None
        self.standWalkRunReverse = (('sad-neutral', 1.0), ('sad-walk', 1.2), ('sad-walk', 1.2), ('sad-walk', -1.0))
        self.setSpeed(0, 0)
        Emote.globalEmote.disableBody(self, 'toon, enterSad')
        self.setActiveShadow(1)

    
    def exitSad(self):
        self.standWalkRunReverse = None
        self.stop()
        self.motion.exit()
        Emote.globalEmote.releaseBody(self, 'toon, exitSad')

    
    def enterCatching(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        self.playingAnim = None
        self.playingRate = None
        self.standWalkRunReverse = (('catch-neutral', 1.0), ('catch-run', 1.0), ('catch-run', 1.0), ('catch-run', -1.0))
        self.setSpeed(self.forwardSpeed, self.rotateSpeed)
        self.setActiveShadow(1)

    
    def exitCatching(self):
        self.standWalkRunReverse = None
        self.stop()
        self.motion.exit()

    
    def enterCatchEating(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        self.playingAnim = None
        self.playingRate = None
        self.standWalkRunReverse = (('catch-eatneutral', 1.0), ('catch-eatnrun', 1.0), ('catch-eatnrun', 1.0), ('catch-eatnrun', -1.0))
        self.setSpeed(self.forwardSpeed, self.rotateSpeed)
        self.setActiveShadow(0)

    
    def exitCatchEating(self):
        self.standWalkRunReverse = None
        self.stop()
        self.motion.exit()

    
    def enterWalk(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        self.loop('walk')
        self.setPlayRate(animMultiplier, 'walk')
        self.setActiveShadow(1)

    
    def exitWalk(self):
        self.stop()

    
    def getJumpDuration(self):
        if self.playingAnim == 'neutral':
            return self.getDuration('jump', 'legs')
        else:
            return self.getDuration('running-jump', 'legs')

    
    def enterJump(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        if not (self.isDisguised):
            if self.playingAnim == 'neutral':
                anim = 'jump'
            else:
                anim = 'running-jump'
            self.playingAnim = anim
            self.setPlayRate(animMultiplier, anim)
            self.play(anim)
        
        self.setActiveShadow(1)

    
    def exitJump(self):
        self.stop()
        self.playingAnim = 'neutral'

    
    def enterJumpSquat(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        if not (self.isDisguised):
            if self.playingAnim == 'neutral':
                anim = 'jump-squat'
            else:
                anim = 'running-jump-squat'
            self.playingAnim = anim
            self.setPlayRate(animMultiplier, anim)
            self.play(anim)
        
        self.setActiveShadow(1)

    
    def exitJumpSquat(self):
        self.stop()
        self.playingAnim = 'neutral'

    
    def enterJumpAirborne(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        if not (self.isDisguised):
            if self.playingAnim == 'neutral':
                anim = 'jump-idle'
            else:
                anim = 'running-jump-idle'
            self.playingAnim = anim
            self.setPlayRate(animMultiplier, anim)
            self.loop(anim)
        
        self.setActiveShadow(1)

    
    def exitJumpAirborne(self):
        self.stop()
        self.playingAnim = 'neutral'

    
    def enterJumpLand(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        if not (self.isDisguised):
            if self.playingAnim == 'running-jump-idle':
                anim = 'running-jump-land'
                skipStart = 0.20000000000000001
            else:
                anim = 'jump-land'
                skipStart = 0.0
            self.playingAnim = anim
            self.setPlayRate(animMultiplier, anim)
            self.play(anim)
        
        self.setActiveShadow(1)

    
    def exitJumpLand(self):
        self.stop()
        self.playingAnim = 'neutral'

    
    def enterRun(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        self.loop('run')
        self.setPlayRate(animMultiplier, 'run')
        Emote.globalEmote.disableBody(self, 'toon, enterRun')
        self.setActiveShadow(1)

    
    def exitRun(self):
        self.stop()
        Emote.globalEmote.releaseBody(self, 'toon, exitRun')

    
    def enterSwim(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        Emote.globalEmote.disableAll(self, 'enterSwim')
        self.playingAnim = 'swim'
        self.loop('swim')
        self.setPlayRate(animMultiplier, 'swim')
        self.getGeomNode().setP(-89.0)
        self.dropShadow.hide()
        if self.isLocal():
            self.useSwimControls()
        
        self.nametag3d.setPos(0, -2, 1)
        self.startBobSwimTask()
        self.setActiveShadow(0)

    
    def exitSwim(self):
        self.stop()
        self.playingAnim = 'neutral'
        self.stopBobSwimTask()
        self.getGeomNode().setPosHpr(0, 0, 0, 0, 0, 0)
        self.dropShadow.show()
        if self.isLocal():
            self.useWalkControls()
        
        self.nametag3d.setPos(0, 0, self.height + 0.5)
        Emote.globalEmote.releaseAll(self, 'exitSwim')

    
    def startBobSwimTask(self):
        swimTaskName = self.taskName('swimBobTask')
        taskMgr.remove('swimTask')
        taskMgr.remove(swimTaskName)
        self.getGeomNode().setZ(4.0)
        self.nametag3d.setZ(5.0)
        newTask = Task.loop(self.getGeomNode().lerpPosXYZ(0, -3, 3, 1, blendType = 'easeInOut'), self.getGeomNode().lerpPosXYZ(0, -3, 4, 1, blendType = 'easeInOut'))
        taskMgr.add(newTask, swimTaskName)

    
    def stopBobSwimTask(self):
        swimTaskName = self.taskName('swimBobTask')
        taskMgr.remove(swimTaskName)
        self.getGeomNode().setPos(0, 0, 0)
        self.nametag3d.setZ(1.0)

    
    def enterOpenBook(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        Emote.globalEmote.disableAll(self, 'enterOpenBook')
        self.playingAnim = 'openBook'
        self.stopLookAround()
        self.lerpLookAt(Point3(0, 1, -2))
        bookTracks = Parallel()
        for bookActor in self.getBookActors():
            bookTracks.append(ActorInterval(bookActor, 'book', startTime = 1.2, endTime = 1.5))
        
        bookTracks.append(ActorInterval(self, 'book', startTime = 1.2, endTime = 1.5))
        if hasattr(self, 'uniqueName'):
            trackName = self.uniqueName('openBook')
        else:
            trackName = 'openBook'
        self.track = Sequence(Func(self.showBooks), bookTracks, Wait(0.10000000000000001), name = trackName)
        if callback:
            self.track.setDoneEvent(self.track.getName())
            self.acceptOnce(self.track.getName(), callback, extraArgs)
        
        self.track.start(ts)
        self.setActiveShadow(0)

    
    def exitOpenBook(self):
        self.playingAnim = 'neutralob'
        if self.track != None:
            self.ignore(self.track.getName())
            self.track.finish()
            self.track = None
        
        self.hideBooks()
        self.startLookAround()
        Emote.globalEmote.releaseAll(self, 'exitOpenBook')

    
    def enterReadBook(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        Emote.globalEmote.disableBody(self, 'enterReadBook')
        self.playingAnim = 'readBook'
        self.stopLookAround()
        self.lerpLookAt(Point3(0, 1, -2))
        self.showBooks()
        for bookActor in self.getBookActors():
            bookActor.pingpong('book', fromFrame = 38, toFrame = 118)
        
        self.pingpong('book', fromFrame = 38, toFrame = 118)
        self.setActiveShadow(0)

    
    def exitReadBook(self):
        self.playingAnim = 'neutralrb'
        self.hideBooks()
        for bookActor in self.getBookActors():
            bookActor.stop()
        
        self.startLookAround()
        Emote.globalEmote.releaseBody(self, 'exitReadBook')

    
    def enterCloseBook(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        Emote.globalEmote.disableAll(self, 'enterCloseBook')
        self.playingAnim = 'closeBook'
        bookTracks = Parallel()
        for bookActor in self.getBookActors():
            bookTracks.append(ActorInterval(bookActor, 'book', startTime = 4.96, endTime = 6.5))
        
        bookTracks.append(ActorInterval(self, 'book', startTime = 4.96, endTime = 6.5))
        if hasattr(self, 'uniqueName'):
            trackName = self.uniqueName('closeBook')
        else:
            trackName = 'closeBook'
        self.track = Sequence(Func(self.showBooks), bookTracks, Func(self.hideBooks), name = trackName)
        if callback:
            self.track.setDoneEvent(self.track.getName())
            self.acceptOnce(self.track.getName(), callback, extraArgs)
        
        self.track.start(ts)
        self.setActiveShadow(0)

    
    def exitCloseBook(self):
        self.playingAnim = 'neutralcb'
        if self.track != None:
            self.ignore(self.track.getName())
            self.track.finish()
            self.track = None
        
        Emote.globalEmote.releaseAll(self, 'exitCloseBook')

    
    def getSoundTeleport(self):
        if not (self.soundTeleport):
            self.soundTeleport = base.loadSfx('phase_3.5/audio/sfx/AV_teleport.mp3')
        
        return self.soundTeleport

    
    def getTeleportOutTrack(self, autoFinishTrack = 1):
        
        def showHoles(holes, hands):
            for (hole, hand) in zip(holes, hands):
                hole.reparentTo(hand)
            

        
        def reparentHoles(holes, toon):
            holes[0].reparentTo(toon)
            holes[1].reparentTo(hidden)
            holes[2].reparentTo(hidden)
            holes[0].setBin('shadow', 0)
            holes[0].setDepthTest(0)
            holes[0].setDepthWrite(0)

        
        def cleanupHoles(holes):
            holes[0].reparentTo(hidden)
            holes[0].clearBin()
            holes[0].clearDepthTest()
            holes[0].clearDepthWrite()

        holes = self.getHoleActors()
        hands = self.getRightHands()
        holeTrack = Track((0.0, Func(showHoles, holes, hands)), (0.5, SoundInterval(self.getSoundTeleport(), node = self)), (1.708, Func(reparentHoles, holes, self)), (3.3999999999999999, Func(cleanupHoles, holes)))
        if hasattr(self, 'uniqueName'):
            trackName = self.uniqueName('teleportOut')
        else:
            trackName = 'teleportOut'
        track = Parallel(holeTrack, name = trackName, autoFinish = autoFinishTrack)
        for hole in holes:
            track.append(ActorInterval(hole, 'hole', duration = 3.3999999999999999))
        
        track.append(ActorInterval(self, 'teleport', duration = 3.3999999999999999))
        return track

    
    def enterTeleportOut(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        if self.ghostMode or self.isDisguised:
            if callback:
                callback(*extraArgs)
            
            return None
        
        self.playingAnim = 'teleport'
        Emote.globalEmote.disableAll(self, 'enterTeleportOut')
        if self.isLocal():
            autoFinishTrack = 0
        else:
            autoFinishTrack = 1
        self.track = self.getTeleportOutTrack(autoFinishTrack)
        self.track.setDoneEvent(self.track.getName())
        self.acceptOnce(self.track.getName(), self.finishTeleportOut, [
            callback,
            extraArgs])
        holeClip = PlaneNode('holeClip')
        cpa = ClipPlaneAttrib.make(ClipPlaneAttrib.OAdd, holeClip)
        self.getGeomNode().node().setAttrib(cpa)
        self.nametag3d.node().setAttrib(cpa)
        self.holeClipPath = self.attachNewNode(holeClip)
        self.track.start(ts)
        self.setActiveShadow(0)

    
    def finishTeleportOut(self, callback = None, extraArgs = []):
        if self.track != None:
            self.ignore(self.track.getName())
            self.track.finish()
            self.track = None
        
        if hasattr(self, 'animFSM'):
            self.animFSM.request('TeleportedOut')
        
        if callback:
            callback(*extraArgs)
        

    
    def exitTeleportOut(self):
        if self.track != None:
            self.ignore(self.track.getName())
            self.track.finish()
            self.track = None
        
        cpaType = ClipPlaneAttrib.getClassType()
        if not self.getGeomNode().isEmpty():
            self.getGeomNode().node().clearAttrib(cpaType)
        
        if not self.nametag3d.isEmpty():
            self.nametag3d.node().clearAttrib(cpaType)
        
        if self.holeClipPath:
            self.holeClipPath.removeNode()
            self.holeClipPath = None
        
        Emote.globalEmote.releaseAll(self, 'exitTeleportOut')
        self.show()

    
    def enterTeleportedOut(self):
        self.setActiveShadow(0)

    
    def exitTeleportedOut(self):
        pass

    
    def getDiedInterval(self, autoFinishTrack = 1):
        sound = loader.loadSfx('phase_5/audio/sfx/ENC_Lose.mp3')
        if hasattr(self, 'uniqueName'):
            trackName = self.uniqueName('died')
        else:
            trackName = 'died'
        ival = Sequence(Func(Emote.globalEmote.disableBody, self), Func(self.sadEyes), Func(self.blinkEyes), Track((0, ActorInterval(self, 'lose')), (2, SoundInterval(sound, node = self)), (5.3330000000000002, self.scaleInterval(1.5, VBase3(0.01, 0.01, 0.01), blendType = 'easeInOut'))), Func(self.detachNode), Func(self.setScale, 1, 1, 1), Func(self.normalEyes), Func(self.blinkEyes), Func(Emote.globalEmote.releaseBody, self), name = trackName, autoFinish = autoFinishTrack)
        return ival

    
    def enterDied(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        if self.ghostMode or self.isDisguised:
            if callback:
                callback(*extraArgs)
            
            return None
        
        self.playingAnim = 'lose'
        Emote.globalEmote.disableAll(self, 'enterDied')
        if self.isLocal():
            autoFinishTrack = 0
        else:
            autoFinishTrack = 1
        if hasattr(self, 'jumpLandAnimFixTask') and self.jumpLandAnimFixTask:
            self.jumpLandAnimFixTask.remove()
            self.jumpLandAnimFixTask = None
        
        self.track = self.getDiedInterval(autoFinishTrack)
        if callback:
            self.track = Sequence(self.track, Func(callback, *extraArgs), autoFinish = autoFinishTrack)
        
        self.track.start(ts)
        self.setActiveShadow(0)

    
    def finishDied(self, callback = None, extraArgs = []):
        if self.track != None:
            self.ignore(self.track.getName())
            self.track.finish()
            self.track = None
        
        if hasattr(self, 'animFSM'):
            self.animFSM.request('TeleportedOut')
        
        if callback:
            callback(*extraArgs)
        

    
    def exitDied(self):
        if self.track != None:
            self.ignore(self.track.getName())
            self.track.finish()
            self.track = None
        
        Emote.globalEmote.releaseAll(self, 'exitDied')
        self.show()

    
    def getTeleportInTrack(self):
        hole = self.getHoleActors()[0]
        hole.setBin('shadow', 0)
        hole.setDepthTest(0)
        hole.setDepthWrite(0)
        holeTrack = Sequence()
        holeTrack.append(Func(hole.reparentTo, self))
        pos = Point3(0, -2.3999999999999999, 0)
        holeTrack.append(Func(hole.setPos, self, pos))
        holeTrack.append(ActorInterval(hole, 'hole', startTime = 3.3999999999999999, endTime = 3.1000000000000001))
        holeTrack.append(Wait(0.59999999999999998))
        holeTrack.append(ActorInterval(hole, 'hole', startTime = 3.1000000000000001, endTime = 3.3999999999999999))
        
        def restoreHole(hole):
            hole.setPos(0, 0, 0)
            hole.reparentTo(hidden)
            hole.clearBin()
            hole.clearDepthTest()
            hole.clearDepthWrite()

        holeTrack.append(Func(restoreHole, hole))
        toonTrack = Sequence(Wait(0.29999999999999999), Func(self.getGeomNode().show), Func(self.nametag3d.show), ActorInterval(self, 'jump', startTime = 0.45000000000000001))
        if hasattr(self, 'uniqueName'):
            trackName = self.uniqueName('teleportIn')
        else:
            trackName = 'teleportIn'
        return Parallel(holeTrack, toonTrack, name = trackName)

    
    def enterTeleportIn(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        if self.ghostMode or self.isDisguised:
            if callback:
                callback(*extraArgs)
            
            return None
        
        self.playingAnim = 'teleport'
        Emote.globalEmote.disableAll(self, 'enterTeleportIn')
        self.pose('teleport', self.getNumFrames('teleport') - 1)
        self.getGeomNode().hide()
        self.nametag3d.hide()
        self.track = self.getTeleportInTrack()
        if callback:
            self.track.setDoneEvent(self.track.getName())
            self.acceptOnce(self.track.getName(), callback, extraArgs)
        
        self.track.start(ts)
        self.setActiveShadow(0)

    
    def exitTeleportIn(self):
        self.playingAnim = None
        if self.track != None:
            self.ignore(self.track.getName())
            self.track.finish()
            self.track = None
        
        if not (self.ghostMode) and not (self.isDisguised):
            self.getGeomNode().show()
            self.nametag3d.show()
        
        Emote.globalEmote.releaseAll(self, 'exitTeleportIn')

    
    def enterSitStart(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        Emote.globalEmote.disableBody(self)
        self.playingAnim = 'sit-start'
        if self.isLocal():
            self.track = Sequence(ActorInterval(self, 'sit-start'), Func(self.b_setAnimState, 'Sit', animMultiplier))
        else:
            self.track = Sequence(ActorInterval(self, 'sit-start'))
        self.track.start(ts)
        self.setActiveShadow(0)

    
    def exitSitStart(self):
        self.playingAnim = 'neutral'
        if self.track != None:
            self.track.finish()
            self.track = None
        
        Emote.globalEmote.releaseBody(self)

    
    def enterSit(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        Emote.globalEmote.disableBody(self)
        self.playingAnim = 'sit'
        self.loop('sit')
        self.setActiveShadow(0)

    
    def exitSit(self):
        self.playingAnim = 'neutral'
        Emote.globalEmote.releaseBody(self)

    
    def enterSleep(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        self.stopLookAround()
        self.stopBlink()
        self.closeEyes()
        self.lerpLookAt(Point3(0, 1, -4))
        self.loop('neutral')
        self.setPlayRate(animMultiplier * 0.40000000000000002, 'neutral')
        self.setChatAbsolute(SLEEP_STRING, CFThought)
        if self == base.localAvatar:
            taskMgr.doMethodLater(self.afkTimeout, self._Toon__handleAfkTimeout, self.uniqueName('afkTimeout'))
        
        self.setActiveShadow(0)

    
    def _Toon__handleAfkTimeout(self, task):
        self.ignore('wakeup')
        self.takeOffSuit()
        base.cr.playGame.getPlace().fsm.request('final')
        self.b_setAnimState('TeleportOut', 1, self._Toon__handleAfkExitTeleport, [
            0])
        return Task.done

    
    def _Toon__handleAfkExitTeleport(self, requestStatus):
        base.cr.loginFSM.request('afkTimeout')

    
    def exitSleep(self):
        taskMgr.remove(self.uniqueName('afkTimeout'))
        self.startLookAround()
        self.openEyes()
        self.startBlink()
        if self.nametag.getChat() == SLEEP_STRING:
            self.clearChat()
        
        self.lerpLookAt(Point3(0, 1, 0), time = 0.25)
        self.stop()

    
    def enterPush(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        Emote.globalEmote.disableBody(self)
        self.playingAnim = 'push'
        self.track = Sequence(ActorInterval(self, 'push'))
        self.track.loop()
        self.setActiveShadow(1)

    
    def exitPush(self):
        self.playingAnim = 'neutral'
        if self.track != None:
            self.track.finish()
            self.track = None
        
        Emote.globalEmote.releaseBody(self)

    
    def enterEmote(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        if len(extraArgs) > 0:
            emoteIndex = extraArgs[0]
        else:
            return None
        self.playingAnim = None
        self.playingRate = None
        self.standWalkRunReverse = (('neutral', 1.0), ('walk', 1.0), ('run', 1.0), ('walk', -1.0))
        self.setSpeed(self.forwardSpeed, self.rotateSpeed)
        if self.isLocal() and emoteIndex != Emote.globalEmote.EmoteSleepIndex:
            if self.sleepFlag:
                self.b_setAnimState('Happy', self.animMultiplier)
            
            self.wakeUp()
        
        duration = 0
        (self.emoteTrack, duration) = Emote.globalEmote.doEmote(self, emoteIndex, ts)
        self.setActiveShadow(1)

    
    def doEmote(self, emoteIndex, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        duration = 0
        if self.isLocal():
            self.wakeUp()
            if self.hasTrackAnimToSpeed():
                self.trackAnimToSpeed(None)
            
        
        (self.emoteTrack, duration) = Emote.globalEmote.doEmote(self, emoteIndex, ts)

    
    def _Toon__returnToLastAnim(self, task):
        if self.playingAnim:
            self.loop(self.playingAnim)
        elif self.hp > 0:
            self.loop('neutral')
        else:
            self.loop('sad-neutral')
        return Task.done

    
    def _Toon__finishEmote(self, task):
        if self.isLocal():
            if self.hp > 0:
                self.b_setAnimState('Happy')
            else:
                self.b_setAnimState('Sad')
        
        return Task.done

    
    def exitEmote(self):
        self.stop()
        if self.emoteTrack != None:
            self.emoteTrack.finish()
            self.emoteTrack = None
        
        taskMgr.remove(self.taskName('finishEmote'))

    
    def enterSquish(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        Emote.globalEmote.disableAll(self)
        sound = loader.loadSfx('phase_9/audio/sfx/toon_decompress.mp3')
        lerpTime = 0.10000000000000001
        node = self.getGeomNode().getChild(0)
        origScale = node.getScale()
        self.track = Sequence(LerpScaleInterval(node, lerpTime, VBase3(2, 2, 0.025000000000000001), blendType = 'easeInOut'), Wait(1.0), Parallel(Sequence(Wait(0.40000000000000002), LerpScaleInterval(node, lerpTime, VBase3(1.3999999999999999, 1.3999999999999999, 1.3999999999999999), blendType = 'easeInOut'), LerpScaleInterval(node, lerpTime / 2.0, VBase3(0.80000000000000004, 0.80000000000000004, 0.80000000000000004), blendType = 'easeInOut'), LerpScaleInterval(node, lerpTime / 3.0, origScale, blendType = 'easeInOut')), ActorInterval(self, 'jump', startTime = 0.20000000000000001), SoundInterval(sound)))
        self.track.start(ts)
        self.setActiveShadow(1)

    
    def exitSquish(self):
        self.playingAnim = 'neutral'
        if self.track != None:
            self.track.finish()
            self.track = None
        
        Emote.globalEmote.releaseAll(self)

    
    def enterFallDown(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        self.playingAnim = 'fallDown'
        Emote.globalEmote.disableAll(self)
        self.track = Sequence(ActorInterval(self, 'slip-backward'), name = 'fallTrack')
        if callback:
            self.track.setDoneEvent(self.track.getName())
            self.acceptOnce(self.track.getName(), callback, extraArgs)
        
        self.track.start(ts)

    
    def exitFallDown(self):
        self.playingAnim = 'neutral'
        if self.track != None:
            self.ignore(self.track.getName())
            self.track.finish()
            self.track = None
        
        Emote.globalEmote.releaseAll(self)

    
    def stunToon(self, ts = 0, callback = None, knockdown = 0):
        if not (self.isStunned):
            if self.stunTrack:
                self.stunTrack.finish()
                self.stunTrack = None
            
            
            def setStunned(stunned):
                self.isStunned = stunned
                if self == base.localAvatar:
                    messenger.send('toonStunned-' + str(self.doId), [
                        self.isStunned])
                

            node = self.getGeomNode()
            lerpTime = 0.5
            down = self.doToonColorScale(VBase4(1, 1, 1, 0.59999999999999998), lerpTime)
            up = self.doToonColorScale(VBase4(1, 1, 1, 0.90000000000000002), lerpTime)
            clear = self.doToonColorScale(self.defaultColorScale, lerpTime)
            track = Sequence(Func(setStunned, 1), down, up, down, up, down, up, down, clear, Func(self.restoreDefaultColorScale), Func(setStunned, 0))
            if knockdown:
                self.stunTrack = Parallel(ActorInterval(self, animName = 'slip-backward'), track)
            else:
                self.stunTrack = track
            self.stunTrack.start()
        

    
    def getPieces(self, *pieces):
        results = []
        for lodName in self.getLODNames():
            for (partName, pieceNames) in pieces:
                part = self.getPart(partName, lodName)
                if part:
                    if type(pieceNames) == types.StringType:
                        pieceNames = (pieceNames,)
                    
                    for pieceName in pieceNames:
                        npc = part.findAllMatches(pieceName)
                        for i in range(npc.getNumPaths()):
                            results.append(npc[i])
                        
                    
                
            
        
        return results

    
    def applyCheesyEffect(self, effect, lerpTime = 0):
        if self.effectTrack != None:
            self.effectTrack.finish()
            self.effectTrack = None
        
        if self.cheesyEffect != effect:
            oldEffect = self.cheesyEffect
            self.cheesyEffect = effect
            if oldEffect == ToontownGlobals.CENormal:
                self.effectTrack = self._Toon__doCheesyEffect(effect, lerpTime)
            elif effect == ToontownGlobals.CENormal:
                self.effectTrack = self._Toon__undoCheesyEffect(oldEffect, lerpTime)
            else:
                self.effectTrack = Sequence(self._Toon__undoCheesyEffect(oldEffect, lerpTime / 2.0), self._Toon__doCheesyEffect(effect, lerpTime / 2.0))
            self.effectTrack.start()
        

    
    def clearCheesyEffect(self, lerpTime = 0):
        self.applyCheesyEffect(ToontownGlobals.CENormal, lerpTime = lerpTime)
        if self.effectTrack != None:
            self.effectTrack.finish()
            self.effectTrack = None
        

    
    def _Toon__doHeadScale(self, scale, lerpTime):
        if scale == None:
            scale = ToontownGlobals.toonHeadScales[self.style.getAnimal()]
        
        track = Parallel()
        for hi in range(self.headParts.getNumPaths()):
            head = self.headParts[hi]
            track.append(LerpScaleInterval(head, lerpTime, scale, blendType = 'easeInOut'))
        
        return track

    
    def _Toon__doLegsScale(self, scale, lerpTime):
        if scale == None:
            scale = 1
            invScale = 1
        else:
            invScale = 1.0 / scale
        track = Parallel()
        for li in range(self.legsParts.getNumPaths()):
            legs = self.legsParts[li]
            torso = self.torsoParts[li]
            track.append(LerpScaleInterval(legs, lerpTime, scale, blendType = 'easeInOut'))
            track.append(LerpScaleInterval(torso, lerpTime, invScale, blendType = 'easeInOut'))
        
        return track

    
    def _Toon__doToonScale(self, scale, lerpTime):
        if scale == None:
            scale = 1
        
        node = self.getGeomNode().getChild(0)
        track = Sequence(Parallel(LerpHprInterval(node, lerpTime, Vec3(0.0, 0.0, 0.0), blendType = 'easeInOut'), LerpScaleInterval(node, lerpTime, scale, blendType = 'easeInOut')), Func(self.resetHeight))
        return track

    
    def doToonColorScale(self, scale, lerpTime, keepDefault = 0):
        if keepDefault:
            self.defaultColorScale = scale
        
        if scale == None:
            scale = VBase4(1, 1, 1, 1)
        
        node = self.getGeomNode()
        caps = self.getPieces(('torso', 'torso-bot-cap'))
        track = Sequence()
        track.append(Func(node.setTransparency, 1))
        if scale[3] != 1:
            for cap in caps:
                track.append(HideInterval(cap))
            
        
        track.append(LerpColorScaleInterval(node, lerpTime, scale, blendType = 'easeInOut'))
        if scale[3] == 1:
            track.append(Func(node.clearTransparency))
            for cap in caps:
                track.append(ShowInterval(cap))
            
        elif scale[3] == 0:
            track.append(Func(node.clearTransparency))
        
        return track

    
    def _Toon__doToonGhostColorScale(self, scale, lerpTime, keepDefault = 0):
        if keepDefault:
            self.defaultColorScale = scale
        
        if scale == None:
            scale = VBase4(1, 1, 1, 1)
        
        node = self.getGeomNode()
        caps = self.getPieces(('torso', 'torso-bot-cap'))
        track = Sequence()
        track.append(Func(node.setTransparency, 1))
        track.append(ShowInterval(node))
        if scale[3] != 1:
            for cap in caps:
                track.append(HideInterval(cap))
            
        
        track.append(LerpColorScaleInterval(node, lerpTime, scale, blendType = 'easeInOut'))
        if scale[3] == 1:
            track.append(Func(node.clearTransparency))
            for cap in caps:
                track.append(ShowInterval(cap))
            
        elif scale[3] == 0:
            track.append(Func(node.clearTransparency))
            track.append(HideInterval(node))
        
        return track

    
    def restoreDefaultColorScale(self):
        node = self.getGeomNode()
        if self.defaultColorScale:
            node.setColorScale(self.defaultColorScale)
            if self.defaultColorScale[3] != 1:
                node.setTransparency(1)
            else:
                node.clearTransparency()
        else:
            node.clearColorScale()
            node.clearTransparency()

    
    def _Toon__doToonColor(self, color, lerpTime):
        node = self.getGeomNode()
        if color == None:
            return Func(node.clearColor)
        else:
            return Func(node.setColor, color, 1)

    
    def _Toon__doPartsColorScale(self, scale, lerpTime):
        if scale == None:
            scale = VBase4(1, 1, 1, 1)
        
        node = self.getGeomNode()
        pieces = self.getPieces(('torso', ('arms', 'neck')), ('legs', ('legs', 'feet')), ('head', '+GeomNode'))
        track = Sequence()
        track.append(Func(node.setTransparency, 1))
        for piece in pieces:
            track.append(ShowInterval(piece))
        
        p1 = Parallel()
        for piece in pieces:
            p1.append(LerpColorScaleInterval(piece, lerpTime, scale, blendType = 'easeInOut'))
        
        track.append(p1)
        if scale[3] == 1:
            track.append(Func(node.clearTransparency))
        elif scale[3] == 0:
            track.append(Func(node.clearTransparency))
            for piece in pieces:
                track.append(HideInterval(piece))
            
        
        return track

    
    def _Toon__doCheesyEffect(self, effect, lerpTime):
        if effect == ToontownGlobals.CEBigHead:
            return self._Toon__doHeadScale(2.5, lerpTime)
        elif effect == ToontownGlobals.CESmallHead:
            return self._Toon__doHeadScale(0.5, lerpTime)
        elif effect == ToontownGlobals.CEBigLegs:
            return self._Toon__doLegsScale(1.3999999999999999, lerpTime)
        elif effect == ToontownGlobals.CESmallLegs:
            return self._Toon__doLegsScale(0.59999999999999998, lerpTime)
        elif effect == ToontownGlobals.CEBigToon:
            return self._Toon__doToonScale(ToontownGlobals.BigToonScale, lerpTime)
        elif effect == ToontownGlobals.CESmallToon:
            return self._Toon__doToonScale(ToontownGlobals.SmallToonScale, lerpTime)
        elif effect == ToontownGlobals.CEFlatPortrait:
            return self._Toon__doToonScale(VBase3(1, 0.050000000000000003, 1), lerpTime)
        elif effect == ToontownGlobals.CEFlatProfile:
            return self._Toon__doToonScale(VBase3(0.050000000000000003, 1, 1), lerpTime)
        elif effect == ToontownGlobals.CETransparent:
            return self.doToonColorScale(VBase4(1, 1, 1, 0.59999999999999998), lerpTime, keepDefault = 1)
        elif effect == ToontownGlobals.CENoColor:
            return self._Toon__doToonColor(VBase4(1, 1, 1, 1), lerpTime)
        elif effect == ToontownGlobals.CEInvisible:
            return self._Toon__doPartsColorScale(VBase4(1, 1, 1, 0), lerpTime)
        elif effect == ToontownGlobals.CEGhost:
            alpha = 0
            if localAvatar.seeGhosts:
                alpha = 0.20000000000000001
            
            return Sequence(self._Toon__doToonGhostColorScale(VBase4(1, 1, 1, alpha), lerpTime, keepDefault = 1), Func(self.nametag3d.hide))
        
        return Sequence()

    
    def _Toon__undoCheesyEffect(self, effect, lerpTime):
        if effect == ToontownGlobals.CEBigHead:
            return self._Toon__doHeadScale(None, lerpTime)
        elif effect == ToontownGlobals.CESmallHead:
            return self._Toon__doHeadScale(None, lerpTime)
        
        if effect == ToontownGlobals.CEBigLegs:
            return self._Toon__doLegsScale(None, lerpTime)
        elif effect == ToontownGlobals.CESmallLegs:
            return self._Toon__doLegsScale(None, lerpTime)
        elif effect == ToontownGlobals.CEBigToon:
            return self._Toon__doToonScale(None, lerpTime)
        elif effect == ToontownGlobals.CESmallToon:
            return self._Toon__doToonScale(None, lerpTime)
        elif effect == ToontownGlobals.CEFlatPortrait:
            return self._Toon__doToonScale(None, lerpTime)
        elif effect == ToontownGlobals.CEFlatProfile:
            return self._Toon__doToonScale(None, lerpTime)
        elif effect == ToontownGlobals.CETransparent:
            return self.doToonColorScale(None, lerpTime, keepDefault = 1)
        elif effect == ToontownGlobals.CENoColor:
            return self._Toon__doToonColor(None, lerpTime)
        elif effect == ToontownGlobals.CEInvisible:
            return self._Toon__doPartsColorScale(None, lerpTime)
        elif effect == ToontownGlobals.CEGhost:
            return Sequence(Func(self.nametag3d.show), self._Toon__doToonGhostColorScale(None, lerpTime, keepDefault = 1))
        
        return Sequence()

    
    def putOnSuit(self, suitType, setDisplayName = True):
        if self.isDisguised:
            self.takeOffSuit()
        
        if launcher and not launcher.getPhaseComplete(5):
            return None
        
        Suit = Suit
        import toontown.suit
        suit = Suit.Suit()
        dna = SuitDNA.SuitDNA()
        dna.newSuit(suitType)
        suit.setStyle(dna)
        suit.isDisguised = 1
        suit.generateSuit()
        suit.initializeDropShadow()
        suit.setPos(self.getPos())
        suit.setHpr(self.getHpr())
        for part in suit.getHeadParts():
            part.hide()
        
        suitHeadNull = suit.find('**/joint-head')
        toonHead = self.find('**/1000/**/__Actor_head')
        Emote.globalEmote.disableAll(self)
        toonGeom = self.getGeomNode()
        toonGeom.hide()
        worldScale = toonHead.getScale(render)
        self.headOrigScale = toonHead.getScale()
        headPosNode = hidden.attachNewNode('headPos')
        toonHead.reparentTo(headPosNode)
        toonHead.setPos(0, 0, 0.20000000000000001)
        headPosNode.reparentTo(suitHeadNull)
        headPosNode.setScale(render, worldScale)
        suitGeom = suit.getGeomNode()
        suitGeom.reparentTo(self)
        self.suit = suit
        self.suitGeom = suitGeom
        self.setHeight(suit.getHeight())
        self.nametag3d.setPos(0, 0, self.height + 1.3)
        self.setFont(ToontownGlobals.getSuitFont())
        if setDisplayName:
            suitDept = SuitDNA.suitDepts.index(SuitDNA.getSuitDept(suitType))
            suitName = SuitBattleGlobals.SuitAttributes[suitType]['name']
            self.setDisplayName(TTLocalizer.SuitBaseNameWithLevel % {
                'name': self.getName(),
                'dept': suitName,
                'level': self.cogLevels[suitDept] + 1 })
            self.nametag.setNameWordwrap(9.0)
        
        if self.isLocal():
            if hasattr(self, 'book'):
                self.book.obscureButton(1)
            
            self.oldForward = ToontownGlobals.ToonForwardSpeed
            self.oldReverse = ToontownGlobals.ToonReverseSpeed
            self.oldRotate = ToontownGlobals.ToonRotateSpeed
            ToontownGlobals.ToonForwardSpeed = ToontownGlobals.SuitWalkSpeed
            ToontownGlobals.ToonReverseSpeed = ToontownGlobals.SuitWalkSpeed
            ToontownGlobals.ToonRotateSpeed = ToontownGlobals.ToonRotateSlowSpeed
            if self.hasTrackAnimToSpeed():
                self.stopTrackAnimToSpeed()
                self.startTrackAnimToSpeed()
            
            self.controlManager.disableAvatarJump()
            indices = range(OTPLocalizer.SCMenuCommonCogIndices[0], OTPLocalizer.SCMenuCommonCogIndices[1] + 1)
            customIndices = OTPLocalizer.SCMenuCustomCogIndices[suitType]
            indices += range(customIndices[0], customIndices[1] + 1)
            self.chatMgr.chatInputSpeedChat.addCogMenu(indices)
        
        self.suit.loop('neutral')
        self.isDisguised = 1

    
    def takeOffSuit(self):
        if not (self.isDisguised):
            return None
        
        suitType = self.suit.style.name
        toonHeadNull = self.find('**/1000/**/joint-head')
        toonHead = self.getHeadParts()[2]
        toonHead.reparentTo(toonHeadNull)
        toonHead.setScale(self.headOrigScale)
        toonHead.setPos(0, 0, 0)
        headPosNode = self.suitGeom.find('**/headPos')
        headPosNode.removeNode()
        self.suitGeom.reparentTo(self.suit)
        self.resetHeight()
        self.nametag3d.setPos(0, 0, self.height + 0.5)
        toonGeom = self.getGeomNode()
        toonGeom.show()
        Emote.globalEmote.releaseAll(self)
        self.isDisguised = 0
        self.setFont(ToontownGlobals.getToonFont())
        self.setDisplayName(self.getName())
        self.nametag.setNameWordwrap(-1)
        if self.isLocal():
            if hasattr(self, 'book'):
                self.book.obscureButton(0)
            
            ToontownGlobals.ToonForwardSpeed = self.oldForward
            ToontownGlobals.ToonReverseSpeed = self.oldReverse
            ToontownGlobals.ToonRotateSpeed = self.oldRotate
            if self.hasTrackAnimToSpeed():
                self.stopTrackAnimToSpeed()
                self.startTrackAnimToSpeed()
            
            del self.oldForward
            del self.oldReverse
            del self.oldRotate
            self.controlManager.enableAvatarJump()
            self.chatMgr.chatInputSpeedChat.removeCogMenu()
        
        del self.suit
        del self.suitGeom

    
    def getPieModel(self):
        ToontownBattleGlobals = ToontownBattleGlobals
        import toontown.toonbase
        BattleProps = BattleProps
        import toontown.battle
        if self.pieModel != None and self._Toon__pieModelType != self.pieType:
            self.pieModel.detachNode()
            self.pieModel = None
        
        if self.pieModel == None:
            self._Toon__pieModelType = self.pieType
            pieName = ToontownBattleGlobals.pieNames[self.pieType]
            self.pieModel = BattleProps.globalPropPool.getProp(pieName)
        
        return self.pieModel

    
    def getPresentPieInterval(self, x, y, z, h, p, r):
        ToontownBattleGlobals = ToontownBattleGlobals
        import toontown.toonbase
        BattleProps = BattleProps
        import toontown.battle
        MovieUtil = MovieUtil
        import toontown.battle
        pie = self.getPieModel()
        pieName = ToontownBattleGlobals.pieNames[self.pieType]
        pieType = BattleProps.globalPropPool.getPropType(pieName)
        animPie = Sequence()
        pingpongPie = Sequence()
        if pieType == 'actor':
            animPie = ActorInterval(pie, pieName, startFrame = 0, endFrame = 31)
            pingpongPie = Func(pie.pingpong, pieName, fromFrame = 32, toFrame = 47)
        
        track = Sequence(Func(self.setPosHpr, x, y, z, h, p, r), Func(pie.reparentTo, self.rightHand), Func(pie.setPosHpr, 0, 0, 0, 0, 0, 0), Parallel(pie.scaleInterval(1, pie.getScale(), startScale = MovieUtil.PNT3_NEARZERO), ActorInterval(self, 'throw', startFrame = 0, endFrame = 31), animPie), Func(self.pingpong, 'throw', fromFrame = 32, toFrame = 47), pingpongPie)
        return track

    
    def getTossPieInterval(self, x, y, z, h, p, r, power, beginFlyIval = Sequence()):
        ToontownBattleGlobals = ToontownBattleGlobals
        import toontown.toonbase
        BattleProps = BattleProps
        import toontown.battle
        pie = self.getPieModel()
        flyPie = pie.copyTo(NodePath('a'))
        pieName = ToontownBattleGlobals.pieNames[self.pieType]
        pieType = BattleProps.globalPropPool.getPropType(pieName)
        animPie = Sequence()
        if pieType == 'actor':
            animPie = ActorInterval(pie, pieName, startFrame = 48)
        
        sound = loader.loadSfx('phase_3.5/audio/sfx/AA_pie_throw_only.mp3')
        t = power / 100.0
        dist = 100 - 70 * t
        time = 1 + 0.5 * t
        proj = ProjectileInterval(None, startPos = Point3(0, 0, 0), endPos = Point3(0, dist, 0), duration = time)
        relVel = proj.startVel
        
        def getVelocity(toon = self, relVel = relVel):
            return render.getRelativeVector(toon, relVel)

        toss = Track((0, Sequence(Func(self.setPosHpr, x, y, z, h, p, r), Func(pie.reparentTo, self.rightHand), Func(pie.setPosHpr, 0, 0, 0, 0, 0, 0), Parallel(ActorInterval(self, 'throw', startFrame = 48), animPie), Func(self.loop, 'neutral'))), (16.0 / 24.0, Func(pie.detachNode)))
        fly = Track((14.0 / 24.0, SoundInterval(sound, node = self)), (16.0 / 24.0, Sequence(Func(flyPie.reparentTo, render), Func(flyPie.setPosHpr, self, 0.52000000000000002, 0.96999999999999997, 2.2400000000000002, 89.420000000000002, -10.56, 87.939999999999998), beginFlyIval, ProjectileInterval(flyPie, startVel = getVelocity, duration = 3), Func(flyPie.detachNode))))
        return (toss, fly, flyPie)

    
    def getPieSplatInterval(self, x, y, z, pieCode):
        ToontownBattleGlobals = ToontownBattleGlobals
        import toontown.toonbase
        BattleProps = BattleProps
        import toontown.battle
        pieName = ToontownBattleGlobals.pieNames[self.pieType]
        splatName = 'splat-%s' % pieName
        splat = BattleProps.globalPropPool.getProp(splatName)
        splat.setBillboardPointWorld(2)
        color = ToontownGlobals.PieCodeColors.get(pieCode)
        if color:
            splat.setColor(*color)
        
        sound = loader.loadSfx('phase_5/audio/sfx/AA_wholepie_only.mp3')
        ival = Parallel(Func(splat.reparentTo, render), Func(splat.setPos, x, y, z), SoundInterval(sound, node = splat), Sequence(ActorInterval(splat, splatName), Func(splat.detachNode)))
        return ival

    
    def cleanupPieModel(self):
        if self.pieModel != None:
            self.pieModel.detachNode()
            self.pieModel = None
        

    
    def getFeedPetIval(self):
        return Sequence(ActorInterval(self, 'feedPet'), Func(self.animFSM.request, 'neutral'))

    
    def getScratchPetIval(self):
        return Sequence(ActorInterval(self, 'pet-start'), ActorInterval(self, 'pet-loop'), ActorInterval(self, 'pet-end'))

    
    def getCallPetIval(self):
        return ActorInterval(self, 'callPet')


loadModels()
compileGlobalAnimList()
