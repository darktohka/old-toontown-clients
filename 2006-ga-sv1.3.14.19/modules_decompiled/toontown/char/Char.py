# File: C (Python 2.2)

from otp.avatar import Avatar
from pandac.PandaModules import *
from direct.task import Task
import whrandom
from direct.showbase.ShowBaseGlobal import *
from direct.directnotify import DirectNotifyGlobal
AnimDict = {
    'mk': (('walk', '-walk', 3), ('run', '-run', 3), ('neutral', '-wait', 3), ('left-point-start', '-left-start', 3.5), ('left-point', '-left', 3.5), ('right-point-start', '-right-start', 3.5), ('right-point', '-right', 3.5)),
    'mn': (('walk', '-walk', 3), ('run', '-run', 3), ('neutral', '-wait', 3), ('left-point-start', '-start-Lpoint', 3.5), ('left-point', '-Lpoint', 3.5), ('right-point-start', '-start-Rpoint', 3.5), ('right-point', '-Rpoint', 3.5), ('up', '-up', 4), ('down', '-down', 4), ('left', '-left', 4), ('right', '-right', 4)),
    'g': (('walk', 'Walk', 6), ('run', 'Run', 6), ('neutral', 'Wait', 6)),
    'd': (('walk', '-walk', 6), ('trans', '-transition', 6), ('neutral', '-neutral', 6), ('trans-back', '-transBack', 6)),
    'dw': (('wheel', '-wheel', 6),),
    'p': (('walk', '-walk', 6), ('sit', '-sit', 6), ('neutral', '-neutral', 6), ('stand', '-stand', 6)),
    'cl': () }
ModelDict = {
    'mk': 'phase_3/models/char/mickey',
    'mn': 'phase_3/models/char/minnie',
    'g': 'phase_6/models/char/TT_G',
    'd': 'phase_6/models/char/DL_donald',
    'dw': 'phase_6/models/char/donald-wheel',
    'p': 'phase_6/models/char/pluto',
    'cl': 'phase_5.5/models/estate/Clara_pose2' }
LODModelDict = {
    'mk': [
        1200,
        800,
        400],
    'mn': [
        1200,
        800,
        400],
    'g': [
        1500,
        1000,
        500],
    'd': [
        1000,
        500,
        250],
    'dw': [
        1000],
    'p': [
        1000,
        500,
        300],
    'cl': [] }

class Char(Avatar.Avatar):
    notify = DirectNotifyGlobal.directNotify.newCategory('Char')
    
    def __init__(self):
        
        try:
            pass
        except:
            self.Char_initialized = 1
            Avatar.Avatar.__init__(self)
            self.setPickable(0)
            self.setPlayerType(NametagGroup.CCNonPlayer)
            self.dialogueArray = []
            self.chatterArray = [
                [],
                [],
                []]


    
    def delete(self):
        
        try:
            pass
        except:
            self.Char_deleted = 1
            self.unloadDialogue()
            Avatar.Avatar.delete(self)


    
    def updateCharDNA(self, newDNA):
        if newDNA.name != self.style.name:
            self.swapCharModel(newDNA)
        

    
    def setDNAString(self, dnaString):
        newDNA = CharDNA.CharDNA()
        newDNA.makeFromNetString(dnaString)
        self.setDNA(newDNA)

    
    def setDNA(self, dna):
        if self.style:
            self.updateCharDNA(dna)
        else:
            self.style = dna
            self.generateChar()
            self.initializeDropShadow()
            self.initializeNametag3d()

    
    def setLODs(self):
        self.setLODNode()
        levelOneIn = base.config.GetInt('lod1-in', 50)
        levelOneOut = base.config.GetInt('lod1-out', 1)
        levelTwoIn = base.config.GetInt('lod2-in', 100)
        levelTwoOut = base.config.GetInt('lod2-out', 50)
        levelThreeIn = base.config.GetInt('lod3-in', 280)
        levelThreeOut = base.config.GetInt('lod3-out', 100)
        self.addLOD(LODModelDict[self.style.name][2], levelThreeIn, levelThreeOut)
        self.addLOD(LODModelDict[self.style.name][1], levelTwoIn, levelTwoOut)
        self.addLOD(LODModelDict[self.style.name][0], levelOneIn, levelOneOut)

    
    def generateChar(self):
        dna = self.style
        self.name = dna.getCharName()
        if len(LODModelDict[dna.name]) > 1:
            self.setLODs()
        
        filePrefix = ModelDict[dna.name]
        if self.name == 'mickey':
            height = 3.0
        elif self.name == 'minnie':
            height = 3.0
        elif self.name == 'goofy':
            height = 4.7999999999999998
        elif self.name == 'donald' or self.name == 'donald-wheel':
            height = 4.5
        elif self.name == 'pluto':
            height = 3.0
        elif self.name == 'clarabelle':
            height = 3.0
        
        self.lodStrings = []
        for lod in LODModelDict[self.style.name]:
            self.lodStrings.append(str(lod))
        
        if self.lodStrings:
            for lodStr in self.lodStrings:
                if len(self.lodStrings) > 1:
                    lodName = lodStr
                else:
                    lodName = 'lodRoot'
                self.loadModel(filePrefix + '-' + lodStr, lodName = lodName)
            
        else:
            self.loadModel(filePrefix)
        animDict = { }
        animList = AnimDict[self.style.name]
        for anim in animList:
            animFilePrefix = filePrefix[:6] + str(anim[2]) + filePrefix[7:]
            animDict[anim[0]] = animFilePrefix + anim[1]
        
        for lodStr in self.lodStrings:
            if len(self.lodStrings) > 1:
                lodName = lodStr
            else:
                lodName = 'lodRoot'
            self.loadAnims(animDict, lodName = lodName)
        
        self.setHeight(height)
        self.loadDialogue(dna.name)
        self.ears = []
        if self.name == 'mickey' or self.name == 'minnie':
            for bundle in self.getPartBundleDict().values():
                charNodepath = bundle['modelRoot']
                char = charNodepath.node()
                earNull = char.getBundle().findChild('sphere3')
                earNull.clearNetTransforms()
                ears = charNodepath.find('**/sphere3')
                earRoot = charNodepath.attachNewNode('earRoot')
                earPitch = earRoot.attachNewNode('earPitch')
                earPitch.setP(40.0)
                ears.reparentTo(earPitch)
                earNull.addNetTransform(earRoot.node())
                ears.clearMat()
                ears.node().setPreserveTransform(ModelNode.PTNone)
                ears.setP(-40.0)
                ears.flattenMedium()
                self.ears.append(ears)
                ears.setBillboardAxis()
            
        
        self.eyes = None
        self.lpupil = None
        self.rpupil = None
        self.eyesOpen = None
        self.eyesClosed = None
        if self.name == 'mickey' or self.name == 'minnie':
            self.eyesOpen = loader.loadTexture('phase_3/maps/eyes1.jpg', 'phase_3/maps/eyes1_a.rgb')
            self.eyesClosed = loader.loadTexture('phase_3/maps/mickey_eyes_closed.jpg', 'phase_3/maps/mickey_eyes_closed_a.rgb')
            self.eyes = self.find('**/1200/**/eyes')
            self.eyes.setBin('transparent', 0)
            self.lpupil = self.find('**/1200/**/joint-pupilL')
            self.rpupil = self.find('**/1200/**/joint-pupilR')
            for lodName in self.getLODNames():
                self.drawInFront('joint-pupil?', 'eyes*', -3, lodName = lodName)
            
        elif self.name == 'pluto':
            self.eyesOpen = loader.loadTexture('phase_6/maps/plutoEyesOpen.jpg', 'phase_6/maps/plutoEyesOpen_a.rgb')
            self.eyesClosed = loader.loadTexture('phase_6/maps/plutoEyesClosed.jpg', 'phase_6/maps/plutoEyesClosed_a.rgb')
            self.eyes = self.find('**/1000/**/eyes')
            self.lpupil = self.find('**/1000/**/joint-pupilL')
            self.rpupil = self.find('**/1000/**/joint-pupilR')
            for lodName in self.getLODNames():
                self.drawInFront('joint-pupil?', 'eyes*', -3, lodName = lodName)
            
        elif self.name == 'donald-wheel':
            self.eyes = self.find('**/eyes')
            self.lpupil = self.find('**/joint-pupilL')
            self.rpupil = self.find('**/joint-pupilR')
            self.drawInFront('joint-pupil?', 'eyes*', -3)
        
        if self.lpupil != None:
            self.lpupil.adjustAllPriorities(1)
            self.rpupil.adjustAllPriorities(1)
        
        if self.eyesOpen:
            self.eyesOpen.setMinfilter(Texture.FTLinear)
            self.eyesOpen.setMagfilter(Texture.FTLinear)
        
        if self.eyesClosed:
            self.eyesClosed.setMinfilter(Texture.FTLinear)
            self.eyesClosed.setMagfilter(Texture.FTLinear)
        
        if self.name == 'mickey':
            pupilParent = self.rpupil.getParent()
            pupilOffsetNode = pupilParent.attachNewNode('pupilOffsetNode')
            pupilOffsetNode.setPos(0, 0.025000000000000001, 0)
            self.rpupil.reparentTo(pupilOffsetNode)
        
        self._Char__blinkName = 'blink-' + self.name

    
    def swapCharModel(self, charStyle):
        for lodStr in self.lodStrings:
            if len(self.lodStrings) > 1:
                lodName = lodStr
            else:
                lodName = 'lodRoot'
            self.removePart('modelRoot', lodName = lodName)
        
        self.setStyle(charStyle)
        self.generateChar()

    
    def getDialogue(self, type, length):
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
            self.notify.error('unrecognized dialogue type: ', type)
        if sfxIndex != None and sfxIndex < len(self.dialogueArray) and self.dialogueArray[sfxIndex] != None:
            return self.dialogueArray[sfxIndex]
        else:
            return None

    
    def playDialogue(self, type, length):
        dialogue = self.getDialogue(type, length)
        base.playSfx(dialogue)

    
    def getChatterDialogue(self, category, msg):
        
        try:
            return self.chatterArray[category][msg]
        except IndexError:
            return None


    
    def getShadowJoint(self):
        return self.getGeomNode()

    
    def getNametagJoints(self):
        return []

    
    def loadChatterDialogue(self, name, audioIndexArray, loadPath, language):
        chatterTypes = [
            'greetings',
            'comments',
            'goodbyes']
        for categoryIndex in range(len(audioIndexArray)):
            chatterType = chatterTypes[categoryIndex]
            for fileIndex in audioIndexArray[categoryIndex]:
                if fileIndex:
                    self.chatterArray[categoryIndex].append(base.loadSfx('%s/CC_%s_chatter_%s%02d.mp3' % (loadPath, name, chatterType, fileIndex)))
                else:
                    self.chatterArray[categoryIndex].append(None)
            
        

    
    def loadDialogue(self, char):
        if self.dialogueArray:
            self.notify.warning('loadDialogue() called twice.')
        
        self.unloadDialogue()
        language = base.config.GetString('language', 'english')
        if char == 'mk':
            dialogueFile = base.loadSfx('phase_3/audio/dial/mickey.wav')
            for i in range(0, 6):
                self.dialogueArray.append(dialogueFile)
            
            if language == 'japanese':
                chatterIndexArray = ([
                    1,
                    2], [
                    1,
                    2,
                    3,
                    4], [
                    1,
                    2,
                    3,
                    4,
                    5])
                self.loadChatterDialogue('mickey', chatterIndexArray, 'phase_3/audio/dial', language)
            
        elif char == 'mn':
            dialogueFile = base.loadSfx('phase_3/audio/dial/minnie.wav')
            for i in range(0, 6):
                self.dialogueArray.append(dialogueFile)
            
            if language == 'japanese':
                chatterIndexArray = ([
                    1,
                    2], [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17], [
                    1,
                    2,
                    3])
                self.loadChatterDialogue('minnie', chatterIndexArray, 'phase_3/audio/dial', language)
            
        elif char == 'g':
            dialogueFile = base.loadSfx('phase_6/audio/dial/goofy.wav')
            for i in range(0, 6):
                self.dialogueArray.append(dialogueFile)
            
            if language == 'japanese':
                chatterIndexArray = ([
                    1,
                    2,
                    3], [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12], [
                    1,
                    2,
                    3,
                    4])
                self.loadChatterDialogue('goofy', chatterIndexArray, 'phase_6/audio/dial', language)
            
        elif char == 'd' or char == 'dw':
            dialogueFile = base.loadSfx('phase_6/audio/dial/donald.wav')
            for i in range(0, 6):
                self.dialogueArray.append(dialogueFile)
            
            if char == 'd':
                if language == 'japanese':
                    chatterIndexArray = ([
                        1,
                        2], [
                        1,
                        2,
                        3,
                        4,
                        5,
                        6,
                        7,
                        8,
                        9,
                        10,
                        11], [
                        1,
                        2,
                        3,
                        4])
                    self.loadChatterDialogue('donald', chatterIndexArray, 'phase_6/audio/dial', language)
                
            
        elif char == 'p':
            dialogueFile = base.loadSfx('phase_3.5/audio/dial/AV_dog_med.mp3')
            for i in range(0, 6):
                self.dialogueArray.append(dialogueFile)
            
        elif char == 'cl':
            dialogueFile = base.loadSfx('phase_3.5/audio/dial/AV_dog_med.mp3')
            for i in range(0, 6):
                self.dialogueArray.append(dialogueFile)
            
        else:
            self.notify.error('unknown character %s' % char)

    
    def unloadDialogue(self):
        self.dialogueArray = []
        self.chatterArray = [
            [],
            [],
            []]

    
    def _Char__blinkOpenEyes(self, task):
        self.openEyes()
        r = whrandom.random()
        if r < 0.10000000000000001:
            t = 0.20000000000000001
        else:
            t = r * 4.0 + 1.0
        taskMgr.doMethodLater(t, self._Char__blinkCloseEyes, self._Char__blinkName)
        return Task.done

    
    def _Char__blinkCloseEyes(self, task):
        self.closeEyes()
        taskMgr.doMethodLater(0.125, self._Char__blinkOpenEyes, self._Char__blinkName)
        return Task.done

    
    def openEyes(self):
        self.eyes.setTexture(self.eyesOpen, 1)
        self.lpupil.show()
        self.rpupil.show()

    
    def closeEyes(self):
        self.eyes.setTexture(self.eyesClosed, 1)
        self.lpupil.hide()
        self.rpupil.hide()

    
    def startBlink(self):
        if self.eyesOpen:
            taskMgr.remove(self._Char__blinkName)
            taskMgr.doMethodLater(whrandom.random() * 4 + 1, self._Char__blinkCloseEyes, self._Char__blinkName)
        

    
    def stopBlink(self):
        if self.eyesOpen:
            taskMgr.remove(self._Char__blinkName)
            self.openEyes()
        

    
    def startEarTask(self):
        pass

    
    def stopEarTask(self):
        pass

    
    def uniqueName(self, idString):
        return idString + '-' + str(self.this)


