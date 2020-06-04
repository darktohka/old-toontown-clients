# File: S (Python 2.2)

from direct.actor import Actor
from otp.avatar import Avatar
import SuitDNA
from toontown.toonbase import ToontownGlobals
from pandac.PandaModules import *
from toontown.battle import SuitBattleGlobals
from direct.task import Task
from toontown.battle import BattleProps
from toontown.toonbase import TTLocalizer
import string
aSize = 6.0599999999999996
bSize = 5.29
cSize = 4.1399999999999997
SuitDialogArray = []
SkelSuitDialogArray = []
AllSuits = (('walk', 'walk'), ('run', 'walk'))
AllSuitsMinigame = (('victory', 'victory'), ('flail', 'flailing'), ('tug-o-war', 'tug-o-war'), ('slip-backward', 'slip-backward'), ('slip-forward', 'slip-forward'))
AllSuitsTutorialBattle = (('lose', 'lose'), ('pie-small-react', 'pie-small'), ('squirt-small-react', 'squirt-small'))
AllSuitsBattle = (('drop-react', 'anvil-drop'), ('flatten', 'drop'), ('sidestep-left', 'sidestep-left'), ('sidestep-right', 'sidestep-right'), ('squirt-large-react', 'squirt-large'), ('landing', 'landing'), ('reach', 'walknreach'), ('rake-react', 'rake'), ('hypnotized', 'hypnotize'), ('soak', 'soak'))
f = (('throw-paper', 'throw-paper', 3.5), ('phone', 'phone', 3.5), ('shredder', 'shredder', 3.5))
p = (('pencil-sharpener', 'pencil-sharpener', 5), ('pen-squirt', 'pen-squirt', 5), ('hold-eraser', 'hold-eraser', 5), ('finger-wag', 'finger-wag', 5), ('hold-pencil', 'hold-pencil', 5))
ym = (('throw-paper', 'throw-paper', 5), ('golf-club-swing', 'golf-club-swing', 5), ('magic3', 'magic3', 5), ('rubber-stamp', 'rubber-stamp', 5), ('smile', 'smile', 5))
mm = (('speak', 'speak', 5), ('effort', 'effort', 5), ('magic1', 'magic1', 5), ('pen-squirt', 'fountain-pen', 5), ('finger-wag', 'finger-wag', 5))
ds = (('magic1', 'magic1', 5), ('magic2', 'magic2', 5), ('throw-paper', 'throw-paper', 5), ('magic3', 'magic3', 5))
hh = (('pen-squirt', 'fountain-pen', 7), ('glower', 'glower', 5), ('throw-paper', 'throw-paper', 5), ('magic1', 'magic1', 5), ('roll-o-dex', 'roll-o-dex', 5))
cr = (('pickpocket', 'pickpocket', 5), ('throw-paper', 'throw-paper', 3.5), ('glower', 'glower', 5))
tbc = (('cigar-smoke', 'cigar-smoke', 8), ('glower', 'glower', 5), ('song-and-dance', 'song-and-dance', 8), ('golf-club-swing', 'golf-club-swing', 5))
cc = (('speak', 'speak', 5), ('glower', 'glower', 5), ('phone', 'phone', 3.5), ('finger-wag', 'finger-wag', 5))
tm = (('speak', 'speak', 5), ('throw-paper', 'throw-paper', 5), ('pickpocket', 'pickpocket', 5), ('roll-o-dex', 'roll-o-dex', 5), ('finger-wag', 'finger-wag', 5))
nd = (('pickpocket', 'pickpocket', 5), ('roll-o-dex', 'roll-o-dex', 5), ('magic3', 'magic3', 5), ('smile', 'smile', 5))
gh = (('speak', 'speak', 5), ('pen-squirt', 'fountain-pen', 5), ('rubber-stamp', 'rubber-stamp', 5))
ms = (('effort', 'effort', 5), ('throw-paper', 'throw-paper', 5), ('stomp', 'stomp', 5), ('quick-jump', 'jump', 6))
tf = (('phone', 'phone', 5), ('smile', 'smile', 5), ('throw-object', 'throw-object', 5), ('glower', 'glower', 5))
m = (('speak', 'speak', 5), ('magic2', 'magic2', 5), ('magic1', 'magic1', 5), ('golf-club-swing', 'golf-club-swing', 5))
mh = (('magic1', 'magic1', 5), ('smile', 'smile', 5), ('golf-club-swing', 'golf-club-swing', 5), ('song-and-dance', 'song-and-dance', 5))
sc = (('throw-paper', 'throw-paper', 3.5), ('watercooler', 'watercooler', 5), ('pickpocket', 'pickpocket', 5))
pp = (('throw-paper', 'throw-paper', 5), ('glower', 'glower', 5), ('finger-wag', 'fingerwag', 5))
tw = (('throw-paper', 'throw-paper', 3.5), ('glower', 'glower', 5), ('magic2', 'magic2', 5), ('finger-wag', 'finger-wag', 5))
bc = (('phone', 'phone', 5), ('hold-pencil', 'hold-pencil', 5))
nc = (('phone', 'phone', 5), ('throw-object', 'throw-object', 5))
mb = (('magic1', 'magic1', 5), ('throw-paper', 'throw-paper', 3.5))
ls = (('throw-paper', 'throw-paper', 5), ('throw-object', 'throw-object', 5), ('hold-pencil', 'hold-pencil', 5))
rb = (('glower', 'glower', 5), ('magic1', 'magic1', 5), ('golf-club-swing', 'golf-club-swing', 5))
bf = (('pickpocket', 'pickpocket', 5), ('rubber-stamp', 'rubber-stamp', 5), ('shredder', 'shredder', 3.5), ('watercooler', 'watercooler', 5))
b = (('effort', 'effort', 5), ('throw-paper', 'throw-paper', 5), ('throw-object', 'throw-object', 5), ('magic1', 'magic1', 5))
dt = (('rubber-stamp', 'rubber-stamp', 5), ('throw-paper', 'throw-paper', 5), ('speak', 'speak', 5), ('finger-wag', 'fingerwag', 5))
ac = (('throw-object', 'throw-object', 5), ('roll-o-dex', 'roll-o-dex', 5), ('stomp', 'stomp', 5), ('phone', 'phone', 5))
bs = (('magic1', 'magic1', 5), ('throw-paper', 'throw-paper', 5), ('finger-wag', 'fingerwag', 5))
sd = (('magic2', 'magic2', 5), ('quick-jump', 'jump', 6), ('stomp', 'stomp', 5), ('magic3', 'magic3', 5), ('hold-pencil', 'hold-pencil', 5))
le = (('speak', 'speak', 5), ('throw-object', 'throw-object', 5), ('glower', 'glower', 5))
bw = (('finger-wag', 'fingerwag', 5), ('cigar-smoke', 'cigar-smoke', 8), ('gavel', 'gavel', 8), ('magic1', 'magic1', 5), ('throw-object', 'throw-object', 5))
ModelDict = {
    'a': ('/models/char/suitA-', 5),
    'b': ('/models/char/suitB-', 5),
    'c': ('/models/char/suitC-', 3.5) }
HeadModelDict = {
    'a': ('/models/char/suitA-', 4),
    'b': ('/models/char/suitB-', 4),
    'c': ('/models/char/suitC-', 3.5) }

def loadTutorialSuit():
    loader.loadModelNode('phase_3.5/models/char/suitC-mod')
    loadDialog(1)


def loadSuits(level):
    loadSuitModelsAndAnims(level, flag = 1)
    loadDialog(level)


def unloadSuits(level):
    loadSuitModelsAndAnims(level, flag = 0)
    unloadDialog(level)


def loadSuitModelsAndAnims(level, flag = 0):
    for key in ModelDict.keys():
        (model, phase) = ModelDict[key]
        (headModel, headPhase) = HeadModelDict[key]
        if flag:
            loader.loadModelNode('phase_3.5' + model + 'mod')
            loader.loadModelNode('phase_' + str(headPhase) + headModel + 'heads')
        else:
            loader.unloadModel('phase_3.5' + model + 'mod')
            loader.unloadModel('phase_' + str(headPhase) + headModel + 'heads')
    


def loadSuitAnims(suit, flag = 1):
    if suit in SuitDNA.suitHeadTypes:
        
        try:
            animList = eval(suit)
        except NameError:
            animList = ()

    else:
        print 'Invalid suit name: ', suit
        return -1
    for anim in animList:
        phase = 'phase_' + str(anim[2])
        filePrefix = ModelDict[bodyType][0]
        animName = filePrefix + anim[1]
        if flag:
            loader.loadModelNode(animName)
        else:
            loader.unloadModel(animName)
    


def loadDialog(level):
    if len(SuitDialogArray) > 0:
        return None
    else:
        loadPath = 'phase_3.5/audio/dial/'
        SuitDialogFiles = [
            'COG_VO_grunt',
            'COG_VO_murmur',
            'COG_VO_statement',
            'COG_VO_question']
        for file in SuitDialogFiles:
            SuitDialogArray.append(base.loadSfx(loadPath + file + '.mp3'))
        
        SuitDialogArray.append(SuitDialogArray[2])
        SuitDialogArray.append(SuitDialogArray[2])


def loadSkelDialog():
    global SkelSuitDialogArray
    if len(SkelSuitDialogArray) > 0:
        return None
    else:
        grunt = loader.loadSfx('phase_5/audio/sfx/Skel_COG_VO_grunt.mp3')
        murmur = loader.loadSfx('phase_5/audio/sfx/Skel_COG_VO_murmur.mp3')
        statement = loader.loadSfx('phase_5/audio/sfx/Skel_COG_VO_statement.mp3')
        question = loader.loadSfx('phase_5/audio/sfx/Skel_COG_VO_question.mp3')
        SkelSuitDialogArray = [
            grunt,
            murmur,
            statement,
            question,
            statement,
            statement]


def unloadDialog(level):
    global SuitDialogArray
    SuitDialogArray = []


def unloadSkelDialog():
    global SkelSuitDialogArray
    SkelSuitDialogArray = []


class Suit(Avatar.Avatar):
    healthColors = (Vec4(0, 1, 0, 1), Vec4(1, 1, 0, 1), Vec4(1, 0.5, 0, 1), Vec4(1, 0, 0, 1), Vec4(0.29999999999999999, 0.29999999999999999, 0.29999999999999999, 1))
    healthGlowColors = (Vec4(0.25, 1, 0.25, 0.5), Vec4(1, 1, 0.25, 0.5), Vec4(1, 0.5, 0.25, 0.5), Vec4(1, 0.25, 0.25, 0.5), Vec4(0.29999999999999999, 0.29999999999999999, 0.29999999999999999, 0))
    medallionColors = {
        'c': Vec4(0.86299999999999999, 0.77600000000000002, 0.76900000000000002, 1.0),
        's': Vec4(0.84299999999999997, 0.745, 0.745, 1.0),
        'l': Vec4(0.749, 0.77600000000000002, 0.82399999999999995, 1.0),
        'm': Vec4(0.749, 0.76900000000000002, 0.749, 1.0) }
    
    def __init__(self):
        
        try:
            return None
        except:
            self.Suit_initialized = 1

        Avatar.Avatar.__init__(self)
        self.setFont(ToontownGlobals.getSuitFont())
        self.setPlayerType(NametagGroup.CCSuit)
        self.setPickable(1)
        self.leftHand = None
        self.rightHand = None
        self.shadowJoint = None
        self.nametagJoint = None
        self.headParts = []
        self.healthBar = None
        self.healthCondition = 0
        self.isDisguised = 0

    
    def delete(self):
        
        try:
            pass
        except:
            self.Suit_deleted = 1
            if self.leftHand:
                self.leftHand.removeNode()
                self.leftHand = None
            
            if self.rightHand:
                self.rightHand.removeNode()
                self.rightHand = None
            
            if self.shadowJoint:
                self.shadowJoint.removeNode()
                self.shadowJoint = None
            
            if self.nametagJoint:
                self.nametagJoint.removeNode()
                self.nametagJoint = None
            
            for part in self.headParts:
                part.removeNode()
            
            self.headParts = []
            self.removeHealthBar()
            Avatar.Avatar.delete(self)

        return None

    
    def setHeight(self, height):
        Avatar.Avatar.setHeight(self, height)
        self.nametag3d.setPos(0, 0, height + 1.0)

    
    def getRadius(self):
        return 2

    
    def setDNAString(self, dnaString):
        self.dna = SuitDNA.SuitDNA()
        self.dna.makeFromNetString(dnaString)
        self.setDNA(self.dna)

    
    def setDNA(self, dna):
        if self.style:
            pass
        1
        self.style = dna
        self.generateSuit()
        self.initializeDropShadow()
        self.initializeNametag3d()

    
    def generateSuit(self):
        dna = self.style
        self.headParts = []
        self.headColor = None
        self.headTexture = None
        self.loseActor = None
        self.isSkeleton = 0
        if dna.name == 'f':
            self.scale = 4.0 / cSize
            self.handColor = SuitDNA.corpPolyColor
            self.generateBody()
            self.generateHead('flunky')
            self.generateHead('glasses')
            self.setHeight(4.8799999999999999)
        elif dna.name == 'p':
            self.scale = 3.3500000000000001 / bSize
            self.handColor = SuitDNA.corpPolyColor
            self.generateBody()
            self.generateHead('pencilpusher')
            self.setHeight(5.0)
        elif dna.name == 'ym':
            self.scale = 4.125 / aSize
            self.handColor = SuitDNA.corpPolyColor
            self.generateBody()
            self.generateHead('yesman')
            self.setHeight(5.2800000000000002)
        elif dna.name == 'mm':
            self.scale = 2.5 / cSize
            self.handColor = SuitDNA.corpPolyColor
            self.generateBody()
            self.generateHead('micromanager')
            self.setHeight(3.25)
        elif dna.name == 'ds':
            self.scale = 4.5 / bSize
            self.handColor = SuitDNA.corpPolyColor
            self.generateBody()
            self.generateHead('beancounter')
            self.setHeight(6.0800000000000001)
        elif dna.name == 'hh':
            self.scale = 6.5 / aSize
            self.handColor = SuitDNA.corpPolyColor
            self.generateBody()
            self.generateHead('headhunter')
            self.setHeight(7.4500000000000002)
        elif dna.name == 'cr':
            self.scale = 6.75 / cSize
            self.handColor = VBase4(0.84999999999999998, 0.55000000000000004, 0.55000000000000004, 1.0)
            self.generateBody()
            self.headTexture = 'corporate-raider.jpg'
            self.generateHead('flunky')
            self.setHeight(8.2300000000000004)
        elif dna.name == 'tbc':
            self.scale = 7.0 / aSize
            self.handColor = VBase4(0.75, 0.94999999999999996, 0.75, 1.0)
            self.generateBody()
            self.generateHead('bigcheese')
            self.setHeight(9.3399999999999999)
        elif dna.name == 'bf':
            self.scale = 4.0 / cSize
            self.handColor = SuitDNA.legalPolyColor
            self.generateBody()
            self.headTexture = 'bottom-feeder.jpg'
            self.generateHead('tightwad')
            self.setHeight(4.8099999999999996)
        elif dna.name == 'b':
            self.scale = 4.375 / bSize
            self.handColor = VBase4(0.94999999999999996, 0.94999999999999996, 1.0, 1.0)
            self.generateBody()
            self.headTexture = 'blood-sucker.jpg'
            self.generateHead('movershaker')
            self.setHeight(6.1699999999999999)
        elif dna.name == 'dt':
            self.scale = 4.25 / aSize
            self.handColor = SuitDNA.legalPolyColor
            self.generateBody()
            self.headTexture = 'double-talker.jpg'
            self.generateHead('twoface')
            self.setHeight(5.6299999999999999)
        elif dna.name == 'ac':
            self.scale = 4.3499999999999996 / bSize
            self.handColor = SuitDNA.legalPolyColor
            self.generateBody()
            self.generateHead('ambulancechaser')
            self.setHeight(6.3899999999999997)
        elif dna.name == 'bs':
            self.scale = 4.5 / aSize
            self.handColor = SuitDNA.legalPolyColor
            self.generateBody()
            self.generateHead('backstabber')
            self.setHeight(6.71)
        elif dna.name == 'sd':
            self.scale = 5.6500000000000004 / bSize
            self.handColor = VBase4(0.5, 0.80000000000000004, 0.75, 1.0)
            self.generateBody()
            self.headTexture = 'spin-doctor.jpg'
            self.generateHead('telemarketer')
            self.setHeight(7.9000000000000004)
        elif dna.name == 'le':
            self.scale = 7.125 / aSize
            self.handColor = VBase4(0.25, 0.25, 0.5, 1.0)
            self.generateBody()
            self.generateHead('legaleagle')
            self.setHeight(8.2699999999999996)
        elif dna.name == 'bw':
            self.scale = 7.0 / aSize
            self.handColor = SuitDNA.legalPolyColor
            self.generateBody()
            self.generateHead('bigwig')
            self.setHeight(8.6899999999999995)
        elif dna.name == 'sc':
            self.scale = 3.6000000000000001 / cSize
            self.handColor = SuitDNA.moneyPolyColor
            self.generateBody()
            self.generateHead('coldcaller')
            self.setHeight(4.7699999999999996)
        elif dna.name == 'pp':
            self.scale = 3.5499999999999998 / aSize
            self.handColor = VBase4(1.0, 0.5, 0.59999999999999998, 1.0)
            self.generateBody()
            self.generateHead('pennypincher')
            self.setHeight(5.2599999999999998)
        elif dna.name == 'tw':
            self.scale = 4.5 / cSize
            self.handColor = SuitDNA.moneyPolyColor
            self.generateBody()
            self.generateHead('tightwad')
            self.setHeight(5.4100000000000001)
        elif dna.name == 'bc':
            self.scale = 4.4000000000000004 / bSize
            self.handColor = SuitDNA.moneyPolyColor
            self.generateBody()
            self.generateHead('beancounter')
            self.setHeight(5.9500000000000002)
        elif dna.name == 'nc':
            self.scale = 5.25 / aSize
            self.handColor = SuitDNA.moneyPolyColor
            self.generateBody()
            self.generateHead('numbercruncher')
            self.setHeight(7.2199999999999998)
        elif dna.name == 'mb':
            self.scale = 5.2999999999999998 / cSize
            self.handColor = SuitDNA.moneyPolyColor
            self.generateBody()
            self.generateHead('moneybags')
            self.setHeight(6.9699999999999998)
        elif dna.name == 'ls':
            self.scale = 6.5 / bSize
            self.handColor = VBase4(0.5, 0.84999999999999998, 0.75, 1.0)
            self.generateBody()
            self.generateHead('loanshark')
            self.setHeight(8.5800000000000001)
        elif dna.name == 'rb':
            self.scale = 7.0 / aSize
            self.handColor = SuitDNA.moneyPolyColor
            self.generateBody()
            self.headTexture = 'robber-baron.jpg'
            self.generateHead('yesman')
            self.setHeight(8.9499999999999993)
        elif dna.name == 'cc':
            self.scale = 3.5 / cSize
            self.handColor = VBase4(0.55000000000000004, 0.65000000000000002, 1.0, 1.0)
            self.headColor = VBase4(0.25, 0.34999999999999998, 1.0, 1.0)
            self.generateBody()
            self.generateHead('coldcaller')
            self.setHeight(4.6299999999999999)
        elif dna.name == 'tm':
            self.scale = 3.75 / bSize
            self.handColor = SuitDNA.salesPolyColor
            self.generateBody()
            self.generateHead('telemarketer')
            self.setHeight(5.2400000000000002)
        elif dna.name == 'nd':
            self.scale = 4.3499999999999996 / aSize
            self.handColor = SuitDNA.salesPolyColor
            self.generateBody()
            self.headTexture = 'name-dropper.jpg'
            self.generateHead('numbercruncher')
            self.setHeight(5.9800000000000004)
        elif dna.name == 'gh':
            self.scale = 4.75 / cSize
            self.handColor = SuitDNA.salesPolyColor
            self.generateBody()
            self.generateHead('gladhander')
            self.setHeight(6.4000000000000004)
        elif dna.name == 'ms':
            self.scale = 4.75 / bSize
            self.handColor = SuitDNA.salesPolyColor
            self.generateBody()
            self.generateHead('movershaker')
            self.setHeight(6.7000000000000002)
        elif dna.name == 'tf':
            self.scale = 5.25 / aSize
            self.handColor = SuitDNA.salesPolyColor
            self.generateBody()
            self.generateHead('twoface')
            self.setHeight(6.9500000000000002)
        elif dna.name == 'm':
            self.scale = 5.75 / aSize
            self.handColor = SuitDNA.salesPolyColor
            self.generateBody()
            self.headTexture = 'mingler.jpg'
            self.generateHead('twoface')
            self.setHeight(7.6100000000000003)
        elif dna.name == 'mh':
            self.scale = 7.0 / aSize
            self.handColor = SuitDNA.salesPolyColor
            self.generateBody()
            self.generateHead('yesman')
            self.setHeight(8.9499999999999993)
        
        self.setName(SuitBattleGlobals.SuitAttributes[dna.name]['name'])
        self.getGeomNode().setScale(self.scale)
        self.generateHealthBar()
        self.generateCorporateMedallion()

    
    def generateBody(self):
        (filePrefix, bodyPhase) = ModelDict[self.style.body]
        animDict = self.generateAnimDict(filePrefix, bodyPhase)
        self.loadModel('phase_3.5' + filePrefix + 'mod')
        self.loadAnims(animDict)
        self.setSuitClothes()

    
    def generateAnimDict(self, filePrefix, bodyPhase):
        animDict = { }
        for anim in AllSuits:
            animDict[anim[0]] = 'phase_' + str(bodyPhase) + filePrefix + anim[1]
        
        for anim in AllSuitsMinigame:
            animDict[anim[0]] = 'phase_4' + filePrefix + anim[1]
        
        for anim in AllSuitsTutorialBattle:
            animDict[anim[0]] = 'phase_' + str(bodyPhase) + filePrefix + anim[1]
        
        for anim in AllSuitsBattle:
            animDict[anim[0]] = 'phase_5' + filePrefix + anim[1]
        
        if self.style.body == 'a':
            animDict['neutral'] = 'phase_4/models/char/suitA-neutral'
        elif self.style.body == 'b':
            animDict['neutral'] = 'phase_4/models/char/suitB-neutral'
        elif self.style.body == 'c':
            animDict['neutral'] = 'phase_3.5/models/char/suitC-neutral'
        
        
        try:
            animList = eval(self.style.name)
        except NameError:
            animList = ()

        for anim in animList:
            phase = 'phase_' + str(anim[2])
            animDict[anim[0]] = phase + filePrefix + anim[1]
        
        return animDict

    
    def setSuitClothes(self, modelRoot = None):
        if not modelRoot:
            modelRoot = self
        
        dept = self.style.dept
        phase = 3.5
        torsoTex = loader.loadTexture('phase_%s/maps/%s_blazer.jpg' % (phase, dept))
        torsoTex.setMinfilter(Texture.FTLinearMipmapLinear)
        torsoTex.setMagfilter(Texture.FTLinear)
        legTex = loader.loadTexture('phase_%s/maps/%s_leg.jpg' % (phase, dept))
        legTex.setMinfilter(Texture.FTLinearMipmapLinear)
        legTex.setMagfilter(Texture.FTLinear)
        armTex = loader.loadTexture('phase_%s/maps/%s_sleeve.jpg' % (phase, dept))
        armTex.setMinfilter(Texture.FTLinearMipmapLinear)
        armTex.setMagfilter(Texture.FTLinear)
        modelRoot.find('**/torso').setTexture(torsoTex, 1)
        modelRoot.find('**/arms').setTexture(armTex, 1)
        modelRoot.find('**/legs').setTexture(legTex, 1)
        self.leftHand = self.find('**/joint-Lhold')
        self.rightHand = self.find('**/joint-Rhold')
        self.shadowJoint = self.find('**/joint-shadow')
        self.nametagJoint = self.find('**/joint-nameTag')
        modelRoot.find('**/hands').setColor(self.handColor)

    
    def generateHead(self, headType):
        (filePrefix, phase) = HeadModelDict[self.style.body]
        headModel = loader.loadModelCopy('phase_' + str(phase) + filePrefix + 'heads')
        headReferences = headModel.findAllMatches('**/' + headType)
        for i in range(0, headReferences.getNumPaths()):
            headPart = self.instance(headReferences.getPath(i), 'modelRoot', 'joint-head')
            if self.headTexture:
                headTex = loader.loadTexture('phase_' + str(phase) + '/maps/' + self.headTexture)
                headTex.setMinfilter(Texture.FTLinearMipmapLinear)
                headTex.setMagfilter(Texture.FTLinear)
                headPart.setTexture(headTex, 1)
            
            if self.headColor:
                headPart.setColor(self.headColor)
            
            self.headParts.append(headPart)
        
        headModel.removeNode()

    
    def generateCorporateMedallion(self):
        icons = loader.loadModelOnce('phase_3/models/gui/cog_icons')
        dept = self.style.dept
        chestNull = self.find('**/joint-attachMeter')
        if dept == 'c':
            self.corpMedallion = icons.find('**/CorpIcon').copyTo(chestNull)
        elif dept == 's':
            self.corpMedallion = icons.find('**/SalesIcon').copyTo(chestNull)
        elif dept == 'l':
            self.corpMedallion = icons.find('**/LegalIcon').copyTo(chestNull)
        elif dept == 'm':
            self.corpMedallion = icons.find('**/MoneyIcon').copyTo(chestNull)
        
        self.corpMedallion.setPosHprScale(0.02, 0.050000000000000003, 0.040000000000000001, 180.0, 0.0, 0.0, 0.51000000000000001, 0.51000000000000001, 0.51000000000000001)
        self.corpMedallion.setColor(self.medallionColors[dept])
        icons.removeNode()

    
    def generateHealthBar(self):
        model = loader.loadModelCopy('phase_3.5/models/gui/matching_game_gui')
        button = model.find('**/minnieCircle')
        button.setScale(3.0)
        button.setH(180.0)
        button.setColor(self.healthColors[0])
        chestNull = self.find('**/joint-attachMeter')
        button.reparentTo(chestNull)
        self.healthBar = button
        glow = BattleProps.globalPropPool.getProp('glow')
        glow.reparentTo(self.healthBar)
        glow.setScale(0.28000000000000003)
        glow.setPos(-0.0050000000000000001, 0.01, 0.014999999999999999)
        glow.setColor(self.healthGlowColors[0])
        self.healthBarGlow = glow
        self.healthBar.hide()
        self.healthCondition = 0

    
    def updateHealthBar(self, hp):
        if hp > self.currHP:
            hp = self.currHP
        
        self.currHP -= hp
        health = float(self.currHP) / float(self.maxHP)
        if health > 0.94999999999999996:
            condition = 0
        elif health > 0.69999999999999996:
            condition = 1
        elif health > 0.29999999999999999:
            condition = 2
        elif health > 0.050000000000000003:
            condition = 3
        elif health > 0.0:
            condition = 4
        else:
            condition = 5
        if self.healthCondition != condition:
            if condition == 4:
                blinkTask = Task.loop(Task.Task(self._Suit__blinkRed), Task.pause(0.75), Task.Task(self._Suit__blinkGray), Task.pause(0.10000000000000001))
                taskMgr.add(blinkTask, self.uniqueName('blink-task'))
            elif condition == 5:
                if self.healthCondition == 4:
                    taskMgr.remove(self.uniqueName('blink-task'))
                
                blinkTask = Task.loop(Task.Task(self._Suit__blinkRed), Task.pause(0.25), Task.Task(self._Suit__blinkGray), Task.pause(0.10000000000000001))
                taskMgr.add(blinkTask, self.uniqueName('blink-task'))
            else:
                self.healthBar.setColor(self.healthColors[condition])
                self.healthBarGlow.setColor(self.healthGlowColors[condition])
            self.healthCondition = condition
        

    
    def _Suit__blinkRed(self, task):
        self.healthBar.setColor(self.healthColors[3])
        self.healthBarGlow.setColor(self.healthGlowColors[3])
        if self.healthCondition == 5:
            self.healthBar.setScale(3.5)
        
        return Task.done

    
    def _Suit__blinkGray(self, task):
        self.healthBar.setColor(self.healthColors[4])
        self.healthBarGlow.setColor(self.healthGlowColors[4])
        if self.healthCondition == 5:
            self.healthBar.setScale(3.0)
        
        return Task.done

    
    def removeHealthBar(self):
        if self.healthBar:
            self.healthBar.removeNode()
            self.healthBar = None
        
        if self.healthCondition == 4 or self.healthCondition == 5:
            taskMgr.remove(self.uniqueName('blink-task'))
        
        self.healthCondition = 0

    
    def getLoseActor(self):
        if self.loseActor == None:
            if not (self.isSkeleton):
                (filePrefix, phase) = ModelDict[self.style.body]
                loseModel = 'phase_' + str(phase) + filePrefix + 'lose-mod'
                loseAnim = 'phase_' + str(phase) + filePrefix + 'lose'
                self.loseActor = Actor.Actor(loseModel, {
                    'lose': loseAnim })
                loseNeck = self.loseActor.find('**/joint-head')
                for part in self.headParts:
                    part.instanceTo(loseNeck)
                
                self.setSuitClothes(self.loseActor)
            else:
                loseModel = 'phase_5/models/char/cog' + string.upper(self.style.body) + '_robot-lose-mod'
                (filePrefix, phase) = ModelDict[self.style.body]
                loseAnim = 'phase_' + str(phase) + filePrefix + 'lose'
                self.loseActor = Actor.Actor(loseModel, {
                    'lose': loseAnim })
        
        self.loseActor.setScale(self.scale)
        self.loseActor.setPos(self.getPos())
        self.loseActor.setHpr(self.getHpr())
        shadowJoint = self.loseActor.find('**/joint-shadow')
        dropShadow = loader.loadModelCopy('phase_3/models/props/drop_shadow')
        dropShadow.setScale(0.45000000000000001)
        dropShadow.setColor(0.0, 0.0, 0.0, 0.5)
        dropShadow.reparentTo(shadowJoint)
        return self.loseActor

    
    def cleanupLoseActor(self):
        self.notify.debug('cleanupLoseActor()')
        if self.loseActor != None:
            self.notify.debug('cleanupLoseActor() - got one')
            self.loseActor.cleanup()
        
        self.loseActor = None

    
    def makeSkeleton(self):
        model = 'phase_5/models/char/cog' + string.upper(self.style.body) + '_robot-zero'
        (filePrefix, phase) = ModelDict[self.style.body]
        anims = self.generateAnimDict(filePrefix, phase)
        anim = self.getCurrentAnim()
        dropShadow = self.dropShadow
        if not dropShadow.isEmpty():
            dropShadow.reparentTo(hidden)
        
        self.removePart('modelRoot')
        self.loadModel(model)
        self.loadAnims(anims)
        self.getGeomNode().setScale(self.scale * 1.0173000000000001)
        self.generateHealthBar()
        self.generateCorporateMedallion()
        self.setHeight(self.height)
        parts = self.findAllMatches('**/pPlane*')
        for partNum in range(0, parts.getNumPaths()):
            bb = parts.getPath(partNum)
            bb.setTwoSided(1)
        
        self.setName(TTLocalizer.Skeleton)
        nameInfo = TTLocalizer.SuitBaseNameWithLevel % {
            'name': self.name,
            'dept': self.getStyleDept(),
            'level': self.getActualLevel() }
        self.setDisplayName(nameInfo)
        self.leftHand = self.find('**/joint-Lhold')
        self.rightHand = self.find('**/joint-Rhold')
        self.shadowJoint = self.find('**/joint-shadow')
        self.nametagNull = self.find('**/joint-nameTag')
        if not dropShadow.isEmpty():
            dropShadow.setScale(0.75)
            if not self.shadowJoint.isEmpty():
                dropShadow.reparentTo(self.shadowJoint)
            
        
        self.loop(anim)
        self.isSkeleton = 1

    
    def getHeadParts(self):
        return self.headParts

    
    def getRightHand(self):
        return self.rightHand

    
    def getLeftHand(self):
        return self.leftHand

    
    def getShadowJoint(self):
        return self.shadowJoint

    
    def getNametagJoints(self):
        return []

    
    def getDialogueArray(self):
        if self.isSkeleton:
            loadSkelDialog()
            return SkelSuitDialogArray
        else:
            return SuitDialogArray


