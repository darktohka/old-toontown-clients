# File: T (Python 2.2)

import Avatar
import AvatarDNA
import Actor
import string
from ToonHead import *
from PandaModules import *
from IntervalGlobal import *
import DirectNotifyGlobal
import ToontownGlobals
import Localizer
import random
import Wake
import Emote
import Motion
import ZoneUtil
SLEEP_STRING = Localizer.ToonSleepString
STAND_INDEX = 0
WALK_INDEX = 1
RUN_INDEX = 2
REVERSE_INDEX = 3
DogDialogueArray = []
CatDialogueArray = []
HorseDialogueArray = []
RabbitDialogueArray = []
MouseDialogueArray = []
DuckDialogueArray = []
LegsAnimDict = { }
TorsoAnimDict = { }
HeadAnimDict = { }
Preloaded = []
Phase3AnimList = (('neutral', 'neutral'), ('run', 'run'))
Phase3_5AnimList = (('walk', 'walk'), ('teleport', 'teleport'), ('book', 'book'), ('jump', 'jump'), ('running-jump', 'running-jump'), ('pushbutton', 'press-button'), ('throw', 'pie-throw'), ('victory', 'victory-dance'), ('sidestep-left', 'sidestep-left'), ('conked', 'conked'), ('cringe', 'cringe'), ('wave', 'wave'), ('shrug', 'shrug'), ('angry', 'angry'), ('tutorial-neutral', 'tutorial-neutral'), ('left-point', 'left-point'), ('right-point', 'right-point'), ('right-point-start', 'right-point-start'), ('give-props', 'give-props'), ('give-props-start', 'give-props-start'), ('right-hand', 'right-hand'), ('right-hand-start', 'right-hand-start'), ('duck', 'duck'), ('sidestep-right', 'jump-back-right'), ('periscope', 'periscope'))
Phase4AnimList = (('sit', 'sit'), ('sit-start', 'intoSit'), ('swim', 'swim'), ('tug-o-war', 'tug-o-war'), ('sad-walk', 'losewalk'), ('sad-neutral', 'sad-neutral'), ('up', 'up'), ('down', 'down'), ('left', 'left'), ('right', 'right'), ('applause', 'applause'), ('confused', 'confused'), ('bow', 'bow'), ('curtsy', 'curtsy'), ('cast', 'fish'), ('slip-forward', 'slip-forward'), ('slip-backward', 'slip-backward'), ('catch-neutral', 'gameneutral'), ('catch-run', 'gamerun'), ('catch-eatneutral', 'eat_neutral'), ('catch-eatnrun', 'eatnrun'), ('catch-intro-throw', 'gameThrow'))
Phase5AnimList = (('water-gun', 'water-gun'), ('hold-bottle', 'hold-bottle'), ('firehose', 'firehose'), ('spit', 'spit'), ('tickle', 'tickle'), ('smooch', 'smooch'), ('happy-dance', 'happy-dance'), ('sprinkle-dust', 'sprinkle-dust'), ('juggle', 'juggle'), ('sound', 'shout'), ('toss', 'toss'), ('hold-magnet', 'hold-magnet'), ('hypnotize', 'hypnotize'), ('struggle', 'struggle'), ('lose', 'lose'), ('think', 'think'), ('melt', 'melt'))
Phase5_5AnimList = (('takePhone', 'takePhone'), ('phoneNeutral', 'phoneNeutral'), ('phoneBack', 'phoneBack'), ('bank', 'jellybeanJar'))
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

        for shirt in AvatarDNA.Shirts:
            loadTex(shirt)
        
        for sleeve in AvatarDNA.Sleeves:
            loadTex(sleeve)
        
        for short in AvatarDNA.BoyShorts:
            loadTex(short)
        
        for bottom in AvatarDNA.GirlBottoms:
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
    else:
        self.notify.error('Unknown phase string %s' % phaseStr)
    for key in LegDict.keys():
        for anim in animList:
            if loadFlag:
                pass
            1
            if LegsAnimDict[key].has_key(anim[0]):
                if toonbase.localToon.style.legs == key:
                    toonbase.localToon.unloadAnims([
                        anim[0]], 'legs', None)
                
            
        
    
    for key in TorsoDict.keys():
        for anim in animList:
            if loadFlag:
                pass
            1
            if TorsoAnimDict[key].has_key(anim[0]):
                if toonbase.localToon.style.torso == key:
                    toonbase.localToon.unloadAnims([
                        anim[0]], 'torso', None)
                
            
        
    
    for key in HeadDict.keys():
        if string.find(key, 'd') >= 0:
            for anim in animList:
                if loadFlag:
                    pass
                1
                if HeadAnimDict[key].has_key(anim[0]):
                    if toonbase.localToon.style.head == key:
                        toonbase.localToon.unloadAnims([
                            anim[0]], 'head', None)
                    
                
            
        
    


def compileGlobalAnimList():
    phaseList = [
        Phase3AnimList,
        Phase3_5AnimList,
        Phase4AnimList,
        Phase5AnimList,
        Phase5_5AnimList]
    phaseStrList = [
        'phase_3',
        'phase_3.5',
        'phase_4',
        'phase_5',
        'phase_5.5']
    for animList in phaseList:
        phaseStr = phaseStrList[phaseList.index(animList)]
        for key in LegDict.keys():
            if not LegsAnimDict.has_key(key):
                LegsAnimDict[key] = { }
            
            for anim in animList:
                file = phaseStr + LegDict[key] + anim[1]
                LegsAnimDict[key][anim[0]] = file
            
        
        for key in TorsoDict.keys():
            if not TorsoAnimDict.has_key(key):
                TorsoAnimDict[key] = { }
            
            for anim in animList:
                file = phaseStr + TorsoDict[key] + anim[1]
                TorsoAnimDict[key][anim[0]] = file
            
        
        for key in HeadDict.keys():
            if string.find(key, 'd') >= 0:
                if not HeadAnimDict.has_key(key):
                    HeadAnimDict[key] = { }
                
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
    


def unloadDialog():
    global DogDialogueArray, CatDialogueArray, HorseDialogueArray, RabbitDialogueArray, MouseDialogueArray, DuckDialogueArray
    DogDialogueArray = []
    CatDialogueArray = []
    HorseDialogueArray = []
    RabbitDialogueArray = []
    MouseDialogueArray = []
    DuckDialogueArray = []


class Toon(Avatar.Avatar, ToonHead):
    notify = DirectNotifyGlobal.directNotify.newCategory('Toon')
    afkTimeout = base.config.GetInt('afk-timeout', 600)
    seeGhosts = base.config.GetBool('see-ghosts', 0)
    
    def __init__(self):
        
        try:
            pass
        except:
            self.Toon_initialized = 1
            Avatar.Avatar.__init__(self)
            ToonHead.__init__(self)
            self.forwardSpeed = 0.0
            self.rotateSpeed = 0.0
            self.motion = Motion.Motion(self)
            self.standWalkRunReverse = None
            self.playingAnim = None
            self.soundTeleport = None
            self.cheesyEffect = ToontownGlobals.CENormal
            self.effectTrack = None
            self.emoteTrack = None
            self.emote = None
            self.bookActors = []
            self.holeActors = []
            self.holeClipPath = None
            self.wake = None
            self.lastWakeTime = 0
            self.isSuit = 0
            self.animFSM = FSM.FSM('Toon', [
                State.State('off', self.enterOff, self.exitOff),
                State.State('neutral', self.enterNeutral, self.exitNeutral),
                State.State('victory', self.enterVictory, self.exitVictory),
                State.State('Happy', self.enterHappy, self.exitHappy),
                State.State('Sad', self.enterSad, self.exitSad),
                State.State('Catching', self.enterCatching, self.exitCatching),
                State.State('CatchEating', self.enterCatchEating, self.exitCatchEating),
                State.State('Sleep', self.enterSleep, self.exitSleep),
                State.State('walk', self.enterWalk, self.exitWalk),
                State.State('jump', self.enterJump, self.exitJump),
                State.State('run', self.enterRun, self.exitRun),
                State.State('swim', self.enterSwim, self.exitSwim),
                State.State('OpenBook', self.enterOpenBook, self.exitOpenBook),
                State.State('ReadBook', self.enterReadBook, self.exitReadBook),
                State.State('CloseBook', self.enterCloseBook, self.exitCloseBook),
                State.State('TeleportOut', self.enterTeleportOut, self.exitTeleportOut),
                State.State('TeleportedOut', self.enterTeleportedOut, self.exitTeleportedOut),
                State.State('TeleportIn', self.enterTeleportIn, self.exitTeleportIn),
                State.State('Emote', self.enterEmote, self.exitEmote),
                State.State('SitStart', self.enterSitStart, self.exitSitStart),
                State.State('Sit', self.enterSit, self.exitSit)], 'off', 'off')

        self.animFSM.enterInitialState()

    
    def delete(self):
        
        try:
            pass
        except:
            self.Toon_deleted = 1
            self.rightHands = None
            self.rightHand = None
            self.leftHands = None
            self.leftHand = None
            self.headParts = None
            self.torsoParts = None
            self.hipsParts = None
            self.legsParts = None
            del self.animFSM
            for bookActor in self.bookActors:
                bookActor.cleanup()
            
            self.bookActors = []
            for holeActor in self.holeActors:
                holeActor.cleanup()
            
            self.holeActors = []
            self.soundTeleport = None
            if self.wake:
                self.wake.stop()
                self.wake.destroy()
                self.wake = None
            
            self.motion.delete()
            self.motion = None
            if self.emoteTrack != None:
                self.emoteTrack.finish()
                self.emoteTrack = None
            
            Avatar.Avatar.delete(self)
            ToonHead.delete(self)


    
    def updateToonDNA(self, newDNA):
        oldDNA = self.style
        if newDNA.head != oldDNA.head:
            self.swapToonHead(newDNA.head)
        
        if newDNA.torso != oldDNA.torso:
            self.swapToonTorso(newDNA.torso, genClothes = 0)
            self.loop('neutral')
        
        if newDNA.legs != oldDNA.legs:
            self.swapToonLegs(newDNA.legs)
        
        self.swapToonColor(newDNA)
        self._Toon__swapToonClothes(newDNA)

    
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
        self.rightHand = NodePath('rightHand')
        self.rightHands = []
        self.leftHand = NodePath('leftHand')
        self.leftHands = []
        for lodName in self.getLODNames():
            hand = self.getPart('torso', lodName).find('**/joint-Rhold')
            self.rightHands.append(hand)
            self.rightHand.instanceTo(hand)
            hand = self.getPart('torso', lodName).find('**/joint-Lhold')
            self.leftHands.append(hand)
            self.leftHand.instanceTo(hand)
        
        self.headParts = self.findAllMatches('**/__Actor_head')
        self.hipsParts = self.findAllMatches('**/joint-hips')
        self.torsoParts = self.findAllMatches('**/__Actor_torso')
        self.legsParts = self.findAllMatches('**/__Actor_legs')
        if not launcher and launcher and launcher.getPhaseComplete(3.5):
            bookActor = Actor.Actor('phase_3.5/models/props/book-mod', {
                'book': 'phase_3.5/models/props/book-chan' })
            bookActor2 = Actor.Actor(other = bookActor)
            bookActor3 = Actor.Actor(other = bookActor)
            self.bookActors = [
                bookActor,
                bookActor2,
                bookActor3]
            hands = self.getRightHands()
            index = 0
            for bookActor in self.bookActors:
                bookActor.reparentTo(hands[index])
                bookActor.hide()
                index += 1
            
            holeActor = Actor.Actor('phase_3.5/models/props/portal-mod', {
                'hole': 'phase_3.5/models/props/portal-chan' })
            holeActor2 = Actor.Actor(other = holeActor)
            holeActor3 = Actor.Actor(other = holeActor)
            self.holeActors = [
                holeActor,
                holeActor2,
                holeActor3]
        else:
            self.bookActors = []
            self.holeActors = []

    
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
        if LegDict.has_key(legStyle):
            filePrefix = LegDict[legStyle]
        else:
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
        self.initializeDropShadow()
        self.initializeNametag3d()

    
    def generateToonTorso(self, copy = 1, genClothes = 1):
        torsoStyle = self.style.torso
        if TorsoDict.has_key(torsoStyle):
            filePrefix = TorsoDict[torsoStyle]
        else:
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
        dna = self.style
        parts = self.findAllMatches('**/arms')
        for partNum in range(0, parts.getNumPaths()):
            parts.getPath(partNum).setColor(dna.getArmColor())
        
        parts = self.findAllMatches('**/neck')
        for partNum in range(0, parts.getNumPaths()):
            parts.getPath(partNum).setColor(dna.getArmColor())
        
        parts = self.findAllMatches('**/hands')
        for partNum in range(0, parts.getNumPaths()):
            parts.getPath(partNum).setColor(dna.getGloveColor())
        
        if len(self.style.torso) == 1:
            parts = self.findAllMatches('**/torso*')
            for partNum in range(0, parts.getNumPaths()):
                parts.getPath(partNum).setColor(dna.getArmColor())
            
        
        parts = self.findAllMatches('**/legs')
        for partNum in range(0, parts.getNumPaths()):
            parts.getPath(partNum).setColor(dna.getLegColor())
        
        parts = self.findAllMatches('**/feet')
        for partNum in range(0, parts.getNumPaths()):
            parts.getPath(partNum).setColor(dna.getLegColor())
        

    
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
                bottomPair = AvatarDNA.GirlBottoms[self.style.botTex]
                if self.style.torso[1] == 's' and bottomPair[1] == AvatarDNA.SKIRT:
                    self.swapToonTorso(self.style.torso[0] + 'd', genClothes = 0)
                    swappedTorso = 1
                elif self.style.torso[1] == 'd' and bottomPair[1] == AvatarDNA.SHORTS:
                    self.swapToonTorso(self.style.torso[0] + 's', genClothes = 0)
                    swappedTorso = 1
                
            
            for lodName in self.getLODNames():
                thisPart = self.getPart('torso', lodName)
                texName = AvatarDNA.Shirts[self.style.topTex]
                shirtTex = loader.loadTexture(texName)
                shirtTex.setMinfilter(Texture.FTLinearMipmapLinear)
                shirtTex.setMagfilter(Texture.FTLinear)
                top = thisPart.find('**/torso-top')
                top.setTexture(shirtTex, 1)
                color = AvatarDNA.ClothesColors[self.style.topTexColor]
                top.setColor(color)
                texName = AvatarDNA.Sleeves[self.style.sleeveTex]
                sleeveTex = loader.loadTexture(texName)
                sleeveTex.setMinfilter(Texture.FTLinearMipmapLinear)
                sleeveTex.setMagfilter(Texture.FTLinear)
                sleeves = thisPart.find('**/sleeves')
                sleeves.setTexture(sleeveTex, 1)
                color = AvatarDNA.ClothesColors[self.style.sleeveTexColor]
                sleeves.setColor(color)
                if self.style.getGender() == 'm':
                    texName = AvatarDNA.BoyShorts[self.style.botTex]
                else:
                    texName = AvatarDNA.GirlBottoms[self.style.botTex][0]
                bottomTex = loader.loadTexture(texName)
                bottomTex.setMinfilter(Texture.FTLinearMipmapLinear)
                bottomTex.setMagfilter(Texture.FTLinear)
                bottoms = thisPart.findAllMatches('**/torso-bot')
                color = AvatarDNA.ClothesColors[self.style.botTexColor]
                for bottomNum in range(0, bottoms.getNumPaths()):
                    bottom = bottoms.getPath(bottomNum)
                    bottom.setTexture(bottomTex, 1)
                    bottom.setColor(color)
                
                caps = thisPart.findAllMatches('**/torso-bot-cap')
                for capNum in range(0, caps.getNumPaths()):
                    cap = caps.getPath(capNum)
                    cap.setColor(color[0] * 0.5, color[1] * 0.5, color[2] * 0.5, 1)
                
            
        
        return swappedTorso

    
    def playDialogue(self, type, length):
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
        elif animalType == 'fowl':
            dialogueArray = DuckDialogueArray
        
        sfxIndex = None
        if type == 'statementA' or type == 'statementB':
            if length == 1:
                sfxIndex = 0
            elif length == 2:
                sfxIndex = 1
            elif length >= 3:
                sfxIndex = 2
            
        elif type == 'question':
            sfxIndex = 3
        elif type == 'exclamation':
            sfxIndex = 4
        elif type == 'special':
            sfxIndex = 5
        else:
            notify.error('unrecognized dialogue type: ', type)
        if sfxIndex != None and sfxIndex < len(dialogueArray) and dialogueArray[sfxIndex] != None:
            base.playSfx(dialogueArray[sfxIndex], node = self)
        

    
    def getShadowJoints(self):
        shadows = []
        for lodName in self.getLODNames():
            shadow = self.getPart('legs', lodName).find('**/joint-shadow')
            shadows.append(shadow)
        
        return shadows

    
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
        if whrandom.random() < 0.10000000000000001 or not hasattr(self, 'cr'):
            x = whrandom.choice((-0.80000000000000004, -0.5, 0, 0.5, 0.80000000000000004))
            y = whrandom.choice((-0.5, 0, 0.5, 0.80000000000000004))
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
                if whrandom.random() < 0.90000000000000002:
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
        for bookActor in self.bookActors:
            bookActor.show()
        

    
    def hideBooks(self):
        for bookActor in self.bookActors:
            bookActor.hide()
        

    
    def getWake(self):
        if not (self.wake):
            self.wake = Wake.Wake(render, self)
        
        return self.wake

    
    def setSpeed(self, forwardSpeed, rotateSpeed):
        self.forwardSpeed = forwardSpeed
        self.rotateSpeed = rotateSpeed
        action = None
        if self.standWalkRunReverse != None:
            if forwardSpeed >= ToontownGlobals.RunCutOff:
                action = RUN_INDEX
            elif forwardSpeed > ToontownGlobals.WalkCutOff:
                action = WALK_INDEX
            elif forwardSpeed < -(ToontownGlobals.WalkCutOff):
                action = REVERSE_INDEX
            elif rotateSpeed != 0.0:
                action = WALK_INDEX
            else:
                action = STAND_INDEX
            (anim, rate) = self.standWalkRunReverse[action]
            self.motion.enter()
            self.motion.setState(anim, rate)
            if anim != self.playingAnim:
                self.playingAnim = anim
                self.playingRate = rate
                self.stop()
                self.loop(anim)
                self.setPlayRate(rate, anim)
                if self.isSuit:
                    self.suit.stop()
                    self.suit.loop(anim)
                    self.suit.setPlayRate(rate, anim)
                
            elif rate != self.playingRate:
                self.playingRate = rate
                if not (self.isSuit):
                    self.setPlayRate(rate, anim)
                else:
                    self.suit.setPlayRate(rate, anim)
            
            
            try:
                hoodId = toonbase.tcr.playGame.getPlaceId()
                zoneId = toonbase.tcr.playGame.getPlace().getZoneId()
                canonicalZoneId = ZoneUtil.getCanonicalZoneId(zoneId)
                if canonicalZoneId == ToontownGlobals.DonaldsDock:
                    wakeWaterHeight = ToontownGlobals.DDWakeWaterHeight
                    showWake = 1
                elif canonicalZoneId == ToontownGlobals.ToontownCentral:
                    wakeWaterHeight = ToontownGlobals.TTWakeWaterHeight
                    showWake = 1
                elif hoodId == ToontownGlobals.MyEstate:
                    wakeWaterHeight = ToontownGlobals.EstateWakeWaterHeight
                    showWake = 1
                else:
                    showWake = 0
                if showWake and self.getZ(render) < wakeWaterHeight and abs(forwardSpeed) > ToontownGlobals.WalkCutOff:
                    currT = globalClock.getFrameTime()
                    deltaT = currT - self.lastWakeTime
                    if action == RUN_INDEX and deltaT > ToontownGlobals.WakeRunDelta or deltaT > ToontownGlobals.WakeWalkDelta:
                        self.getWake().createRipple(wakeWaterHeight, rate = 1, startFrame = 4)
                        self.lastWakeTime = currT
                    
            except AttributeError:
                pass

        
        return action

    
    def enterOff(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        pass

    
    def exitOff(self):
        pass

    
    def enterNeutral(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        anim = 'neutral'
        self.pose(anim, int(self.getNumFrames(anim) * random.random()))
        self.loop(anim, restart = 0)
        self.setPlayRate(animMultiplier, anim)
        self.playingAnim = anim

    
    def exitNeutral(self):
        self.stop()

    
    def enterVictory(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        anim = 'victory'
        frame = int(ts * self.getFrameRate(anim) * animMultiplier)
        self.pose(anim, frame)
        self.loop('victory', restart = 0)
        self.setPlayRate(animMultiplier, 'victory')
        self.playingAnim = anim

    
    def exitVictory(self):
        self.stop()

    
    def enterHappy(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        self.playingAnim = None
        self.playingRate = None
        self.standWalkRunReverse = (('neutral', 1.0), ('walk', 1.0), ('run', 1.0), ('walk', -1.0))
        self.setSpeed(self.forwardSpeed, self.rotateSpeed)

    
    def exitHappy(self):
        self.standWalkRunReverse = None
        self.stop()
        self.motion.exit()

    
    def enterSad(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        self.playingAnim = 'sad'
        self.playingRate = None
        self.standWalkRunReverse = (('sad-neutral', 1.0), ('sad-walk', 1.2), ('sad-walk', 1.2), ('sad-walk', -1.0))
        self.setSpeed(self.forwardSpeed, self.rotateSpeed)
        Emote.DisableBody(self)

    
    def exitSad(self):
        self.standWalkRunReverse = None
        self.stop()
        self.motion.exit()
        Emote.ReleaseAll(self)

    
    def enterCatching(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        self.playingAnim = None
        self.playingRate = None
        self.standWalkRunReverse = (('catch-neutral', 1.0), ('catch-run', 1.0), ('catch-run', 1.0), ('catch-run', -1.0))
        self.setSpeed(self.forwardSpeed, self.rotateSpeed)

    
    def exitCatching(self):
        self.standWalkRunReverse = None
        self.stop()
        self.motion.exit()

    
    def enterCatchEating(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        self.playingAnim = None
        self.playingRate = None
        self.standWalkRunReverse = (('catch-eatneutral', 1.0), ('catch-eatnrun', 1.0), ('catch-eatnrun', 1.0), ('catch-eatnrun', -1.0))
        self.setSpeed(self.forwardSpeed, self.rotateSpeed)

    
    def exitCatchEating(self):
        self.standWalkRunReverse = None
        self.stop()
        self.motion.exit()

    
    def enterWalk(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        self.loop('walk')
        self.setPlayRate(animMultiplier, 'walk')

    
    def exitWalk(self):
        self.stop()

    
    def getJumpDuration(self):
        if self.playingAnim == 'neutral':
            return self.getDuration('jump', 'legs')
        else:
            return self.getDuration('running-jump', 'legs')

    
    def enterJump(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        if not (self.isSuit):
            if self.playingAnim == 'neutral':
                self.playingAnim = 'jump'
                self.setPlayRate(animMultiplier, 'jump')
                self.loop('jump')
            else:
                self.playingAnim = 'running-jump'
                self.setPlayRate(animMultiplier, 'running-jump')
                self.loop('running-jump')
        

    
    def exitJump(self):
        self.stop()
        self.playingAnim = 'neutral'

    
    def enterRun(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        self.loop('run')
        self.setPlayRate(animMultiplier, 'run')
        Emote.DisableBody(self, 'toon, enterRun')

    
    def exitRun(self):
        self.stop()
        Emote.ReleaseBody(self, 'toon, exitRun')

    
    def enterSwim(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        Emote.DisableAll(self)
        self.playingAnim = 'swim'
        self.loop('swim')
        self.setPlayRate(animMultiplier, 'swim')
        self.getGeomNode().setP(-89.0)
        for shadow in self.dropShadows:
            shadow.hide()
        
        self.nametag3d.setPos(0, -2, 1)
        self.startBobSwimTask()

    
    def exitSwim(self):
        self.stop()
        self.playingAnim = 'neutral'
        self.stopBobSwimTask()
        self.getGeomNode().setPosHpr(0, 0, 0, 0, 0, 0)
        for shadow in self.dropShadows:
            shadow.show()
        
        self.nametag3d.setPos(0, 0, self.height + 0.5)
        Emote.ReleaseAll(self)

    
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
        Emote.DisableAll(self)
        self.playingAnim = 'openBook'
        self.stopLookAround()
        self.lerpLookAt(Point3(0, 1, -2))
        bookTracks = Parallel()
        for bookActor in self.bookActors:
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

    
    def exitOpenBook(self):
        self.playingAnim = 'neutralob'
        if self.track != None:
            self.ignore(self.track.getName())
            self.track.finish()
            self.track = None
        
        self.hideBooks()
        self.startLookAround()
        Emote.ReleaseAll(self)

    
    def enterReadBook(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        Emote.DisableBody(self)
        self.playingAnim = 'readBook'
        self.stopLookAround()
        self.lerpLookAt(Point3(0, 1, -2))
        self.showBooks()
        for bookActor in self.bookActors:
            bookActor.pingpong('book', 38, 118)
        
        self.pingpong('book', 38, 118)

    
    def exitReadBook(self):
        self.playingAnim = 'neutralrb'
        self.hideBooks()
        for bookActor in self.bookActors:
            bookActor.stop()
        
        self.startLookAround()
        Emote.ReleaseBody(self)

    
    def enterCloseBook(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        Emote.DisableAll(self)
        self.playingAnim = 'closeBook'
        bookTracks = Parallel()
        for bookActor in self.bookActors:
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

    
    def exitCloseBook(self):
        self.playingAnim = 'neutralcb'
        if self.track != None:
            self.ignore(self.track.getName())
            self.track.finish()
            self.track = None
        
        Emote.ReleaseAll(self)

    
    def getSoundTeleport(self):
        if not (self.soundTeleport):
            self.soundTeleport = base.loadSfx('phase_3.5/audio/sfx/AV_teleport.mp3')
        
        return self.soundTeleport

    
    def enterTeleportOut(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        if self.ghostMode:
            if callback:
                callback(*extraArgs)
            
            return None
        
        
        def showHoles(holes, hands):
            index = 0
            for hole in holes:
                hole.reparentTo(hands[index])
                index += 1
            

        
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

        self.playingAnim = 'teleport'
        Emote.DisableAll(self)
        holes = self.holeActors
        hands = self.getRightHands()
        holeTrack = Track((0.0, Func(showHoles, holes, hands)), (0.5, SoundInterval(self.getSoundTeleport())), (1.708, Func(reparentHoles, holes, self)), (3.3999999999999999, Func(cleanupHoles, holes)))
        if hasattr(self, 'uniqueName'):
            trackName = self.uniqueName('teleportOut')
        else:
            trackName = 'teleportOut'
        if self.isLocal():
            autoFinishTrack = 0
        else:
            autoFinishTrack = 1
        self.track = Parallel(holeTrack, name = trackName, autoFinish = autoFinishTrack)
        for hole in holes:
            self.track.append(ActorInterval(hole, 'hole', duration = 3.3999999999999999))
        
        self.track.append(ActorInterval(self, 'teleport', duration = 3.3999999999999999))
        self.teleportOutCallback = callback
        self.teleportOutCallbackArgs = extraArgs
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
        self.getGeomNode().node().clearAttrib(cpaType)
        self.nametag3d.node().clearAttrib(cpaType)
        if self.holeClipPath:
            self.holeClipPath.removeNode()
            self.holeClipPath = None
        
        Emote.ReleaseAll(self)
        self.show()

    
    def enterTeleportedOut(self):
        return None

    
    def exitTeleportedOut(self):
        return None

    
    def enterTeleportIn(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        if self.ghostMode:
            if callback:
                callback(*extraArgs)
            
            return None
        
        self.playingAnim = 'teleport'
        Emote.DisableAll(self)
        hole = self.holeActors[0]
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
        self.pose('teleport', self.getNumFrames('teleport') - 1)
        self.getGeomNode().hide()
        self.nametag3d.hide()
        toonTrack = Sequence(Wait(0.29999999999999999), Func(self.getGeomNode().show), Func(self.nametag3d.show), ActorInterval(self, 'jump', startTime = 0.45000000000000001))
        if hasattr(self, 'uniqueName'):
            trackName = self.uniqueName('teleportIn')
        else:
            trackName = 'teleportIn'
        self.track = Parallel(holeTrack, toonTrack, name = trackName)
        if callback:
            self.track.setDoneEvent(self.track.getName())
            self.acceptOnce(self.track.getName(), callback, extraArgs)
        
        self.track.start(ts)

    
    def exitTeleportIn(self):
        self.playingAnim = None
        if self.track != None:
            self.ignore(self.track.getName())
            self.track.finish()
            self.track = None
        
        if not (self.ghostMode):
            self.getGeomNode().show()
            self.nametag3d.show()
        
        Emote.ReleaseAll(self)

    
    def enterSitStart(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        Emote.DisableBody(self)
        self.playingAnim = 'sit-start'
        if self.isLocal():
            self.track = Sequence(ActorInterval(self, 'sit-start'), Func(self.b_setAnimState, 'Sit', animMultiplier))
        else:
            self.track = Sequence(ActorInterval(self, 'sit-start'))
        self.track.start(ts)

    
    def exitSitStart(self):
        self.playingAnim = 'neutral'
        if self.track != None:
            self.track.finish()
            self.track = None
        
        Emote.ReleaseBody(self)

    
    def enterSit(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        Emote.DisableBody(self)
        self.playingAnim = 'sit'
        self.loop('sit')

    
    def exitSit(self):
        self.playingAnim = 'neutral'
        Emote.ReleaseBody(self)

    
    def enterSleep(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        self.stopLookAround()
        self.stopBlink()
        self.closeEyes()
        self.lerpLookAt(Point3(0, 1, -4))
        self.loop('neutral')
        self.setPlayRate(animMultiplier * 0.40000000000000002, 'neutral')
        self.setChatAbsolute(SLEEP_STRING, CFThought)
        if self == toonbase.localToon:
            taskMgr.doMethodLater(self.afkTimeout, self._Toon__handleAfkTimeout, self.uniqueName('afkTimeout'))
        
        return None

    
    def _Toon__handleAfkTimeout(self, task):
        self.ignore('wakeup')
        toonbase.tcr.playGame.getPlace().fsm.request('final')
        self.b_setAnimState('TeleportOut', 1, self._Toon__handleAfkExitTeleport, [
            0])
        return Task.done

    
    def _Toon__handleAfkExitTeleport(self, requestStatus):
        toonbase.tcr.loginFSM.request('afkTimeout')

    
    def exitSleep(self):
        taskMgr.remove(self.uniqueName('afkTimeout'))
        self.startLookAround()
        self.openEyes()
        self.startBlink()
        if self.nametag.getChat() == SLEEP_STRING:
            self.clearChat()
        
        self.lerpLookAt(Point3(0, 1, 0), time = 0.25)
        self.stop()
        return None

    
    def enterEmote(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        if len(extraArgs) > 0:
            emoteIndex = extraArgs[0]
        else:
            return None
        self.playingAnim = None
        self.playingRate = None
        self.standWalkRunReverse = (('neutral', 1.0), ('walk', 1.0), ('run', 1.0), ('walk', -1.0))
        self.setSpeed(self.forwardSpeed, self.rotateSpeed)
        if self.isLocal() and emoteIndex != Emote.EmoteSleepIndex:
            if self.sleepFlag:
                self.b_setAnimState('Happy', self.animMultiplier)
            
            self.wakeUp()
        
        duration = 0
        (self.emoteTrack, duration) = Emote.DoEmote(self, emoteIndex, ts)
        if emoteIndex != Emote.EmoteSleepIndex:
            taskMgr.doMethodLater(duration, self._Toon__finishEmote, self.taskName('finishEmote'))
        

    
    def doEmote(self, emoteIndex, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        duration = 0
        if self == toonbase.localToon:
            self.wakeUp()
        
        (self.emoteTrack, duration) = Emote.DoEmote(self, emoteIndex, ts)

    
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

    
    def _Toon__doToonColorScale(self, scale, lerpTime):
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
        pieces = self.getPieces(('torso', ('arms', 'neck')), ('legs', ('legs', 'feet')), ('head', '*'))
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
            return self._Toon__doToonColorScale(VBase4(1, 1, 1, 0.59999999999999998), lerpTime)
        elif effect == ToontownGlobals.CENoColor:
            return self._Toon__doToonColor(VBase4(1, 1, 1, 1), lerpTime)
        elif effect == ToontownGlobals.CEInvisible:
            return self._Toon__doPartsColorScale(VBase4(1, 1, 1, 0), lerpTime)
        elif effect == ToontownGlobals.CEGhost:
            alpha = 0
            if self.seeGhosts:
                alpha = 0.20000000000000001
            
            return Sequence(self._Toon__doToonColorScale(VBase4(1, 1, 1, alpha), lerpTime), Func(self.nametag3d.hide))
        
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
            return self._Toon__doToonColorScale(None, lerpTime)
        elif effect == ToontownGlobals.CENoColor:
            return self._Toon__doToonColor(None, lerpTime)
        elif effect == ToontownGlobals.CEInvisible:
            return self._Toon__doPartsColorScale(None, lerpTime)
        elif effect == ToontownGlobals.CEGhost:
            return Sequence(Func(self.nametag3d.show), self._Toon__doToonColorScale(None, lerpTime))
        
        return Sequence()

    
    def putOnSuit(self, suitType):
        if self.isSuit:
            self.takeOffSuit()
        
        import Suit
        import AvatarDNA
        suit = Suit.Suit()
        dna = AvatarDNA.AvatarDNA()
        dna.newSuit(suitType)
        suit.setStyle(dna)
        suit.generateSuit()
        suit.initializeDropShadow()
        suit.setPos(self.getPos())
        suit.setHpr(self.getHpr())
        for part in suit.getHeadParts():
            part.hide()
        
        suitHeadNull = suit.find('**/joint-head')
        toonHead = self.find('**/1000/**/__Actor_head')
        toonGeom = self.find('**/actorGeom')
        toonGeom.hide()
        worldScale = toonHead.getScale(render)
        self.headOrigScale = toonHead.getScale()
        toonHead.reparentTo(suitHeadNull)
        toonHead.setPos(0, 0, 0.125)
        toonHead.setScale(render, worldScale)
        suitGeom = suit.find('**/actorGeom')
        suitGeom.reparentTo(self)
        self.suit = suit
        self.suitGeom = suitGeom
        self.oldHeight = self.getHeight()
        self.setHeight(suit.getHeight())
        self.isSuit = 1
        self.oldForward = ToontownGlobals.ToonForwardSpeed
        self.oldReverse = ToontownGlobals.ToonReverseSpeed
        self.oldRotate = ToontownGlobals.ToonRotateSpeed
        ToontownGlobals.ToonForwardSpeed = ToontownGlobals.SuitWalkSpeed
        ToontownGlobals.ToonReverseSpeed = ToontownGlobals.SuitWalkSpeed
        ToontownGlobals.ToonRotateSpeed = ToontownGlobals.ToonRotateSlowSpeed
        self.stopTrackAnimToSpeed()
        self.startTrackAnimToSpeed()
        if self.isLocal():
            self.book.obscureButton(1)
        

    
    def takeOffSuit(self):
        if not (self.isSuit):
            return None
        
        toonHeadNull = self.find('**/1000/**/joint-head')
        toonHead = self.getHeadParts()[2]
        toonHead.reparentTo(toonHeadNull)
        toonHead.setScale(self.headOrigScale)
        toonHead.setPos(0, 0, 0)
        self.suitGeom.reparentTo(self.suit)
        self.setHeight(self.oldHeight)
        toonGeom = self.find('**/actorGeom')
        toonGeom.show()
        self.isSuit = 0
        ToontownGlobals.ToonForwardSpeed = self.oldForward
        ToontownGlobals.ToonReverseSpeed = self.oldReverse
        ToontownGlobals.ToonRotateSpeed = self.oldRotate
        toonbase.localToon.stopTrackAnimToSpeed()
        toonbase.localToon.startTrackAnimToSpeed()
        if self.isLocal():
            self.book.obscureButton(0)
            self.book.showButton()
        
        del self.oldHeight
        del self.suit
        del self.suitGeom
        del self.oldForward
        del self.oldReverse
        del self.oldRotate


loadModels()
compileGlobalAnimList()
