# File: A (Python 2.2)

from ShowBaseGlobal import *
from PandaObject import *
from PandaModules import *
import ToontownGlobals
import Actor
import AvatarDNA
import ClockDelta
import Localizer
import ShadowPlacer

def reconsiderAllUnderstandable():
    for av in Avatar.ActiveAvatars:
        av.considerUnderstandable()
    


class Avatar(Actor.Actor):
    notify = Actor.directNotify.newCategory('Avatar')
    ActiveAvatars = []
    
    def __init__(self):
        self.name = ''
        
        try:
            return None
        except:
            self.Avatar_initialized = 1

        Actor.Actor.__init__(self)
        self._Avatar__font = ToontownGlobals.getToonFont()
        self.soundChatBubble = base.loadSfx('phase_3/audio/sfx/GUI_balloon_popup.mp3')
        self._Avatar__nameVisible = 1
        self.nametag = NametagGroup()
        self.nametag.setAvatar(self)
        self.nametag.setFont(ToontownGlobals.getInterfaceFont())
        self.nametag2dContents = Nametag.CName | Nametag.CSpeech
        self.nametag2dDist = Nametag.CName | Nametag.CSpeech
        self.nametag2dNormalContents = Nametag.CName | Nametag.CSpeech
        self.nametag3d = self.attachNewNode('nametag3d')
        self.dropShadow = None
        self.shadowPlacer = None
        self.activeShadow = 0
        self.collTube = None
        self.scale = 1.0
        self.nametagScale = 1.0
        self.height = 0.0
        self.style = None
        self.commonChatFlags = 0
        self.understandable = 1
        self.setPlayerType(NametagGroup.CCNormal)
        self.ghostMode = 0
        self._Avatar__chatParagraph = None
        self._Avatar__chatMessage = None
        self._Avatar__chatFlags = 0
        self._Avatar__chatPageNumber = None
        self._Avatar__chatAddressee = None
        self._Avatar__chatDialogueList = []
        self._Avatar__chatSet = 0
        self._Avatar__chatLocal = 0
        self._Avatar__currentDialogue = None

    
    def delete(self):
        
        try:
            pass
        except:
            self.Avatar_deleted = 1
            del self._Avatar__font
            del self.style
            self.deleteNametag3d()
            del self.soundChatBubble
            del self.nametag
            self.nametag3d.removeNode()
            self.deleteDropShadow()
            Actor.Actor.delete(self)


    
    def isLocal(self):
        return 0

    
    def setPlayerType(self, playerType):
        self.playerType = playerType
        if self.isUnderstandable():
            self.nametag.setColorCode(self.playerType)
        else:
            self.nametag.setColorCode(NametagGroup.CCNoChat)

    
    def setCommonChatFlags(self, commonChatFlags):
        self.commonChatFlags = commonChatFlags
        self.considerUnderstandable()
        if self == toonbase.localToon:
            reconsiderAllUnderstandable()
        

    
    def considerUnderstandable(self):
        if self == toonbase.localToon:
            self.understandable = 1
        elif self.playerType != NametagGroup.CCNormal:
            self.understandable = 1
        elif self.commonChatFlags & toonbase.localToon.commonChatFlags & ToontownGlobals.CommonChat:
            self.understandable = 1
        elif self.commonChatFlags & ToontownGlobals.SuperChat:
            self.understandable = 1
        elif toonbase.localToon.commonChatFlags & ToontownGlobals.SuperChat:
            self.understandable = 1
        elif toonbase.tcr.getFriendFlags(self.doId) & ToontownGlobals.FriendChat:
            self.understandable = 1
        else:
            self.understandable = 0
        if self.understandable:
            self.nametag.setColorCode(self.playerType)
        else:
            self.nametag.setColorCode(NametagGroup.CCNoChat)

    
    def isUnderstandable(self):
        return self.understandable

    
    def setDNAString(self, dnaString):
        newDNA = AvatarDNA.AvatarDNA()
        newDNA.makeFromNetString(dnaString)
        self.setDNA(newDNA)

    
    def setDNA(self, dna):
        if hasattr(self, 'isDisguised'):
            if self.isDisguised:
                return None
            
        
        if self.style:
            type = dna.type
            if type == AvatarDNA.toonType:
                self.updateToonDNA(dna)
            elif type == AvatarDNA.charType:
                self.updateCharDNA(dna)
            
        else:
            self.style = dna
            type = dna.type
            if type == AvatarDNA.toonType:
                self.generateToon()
            elif type == AvatarDNA.suitType:
                self.generateSuit()
            elif type == AvatarDNA.bossType:
                self.generateBossCog()
            elif type == AvatarDNA.charType:
                self.generateChar()
            elif type == AvatarDNA.goonType:
                self.generateGoon()
            else:
                Avatar.notify.error('unknown DNA type: %s' % type)
            self.initializeDropShadow()
            self.initializeNametag3d()

    
    def getAvatarScale(self):
        return self.scale

    
    def setAvatarScale(self, scale):
        if self.scale != scale:
            self.scale = scale
            self.getGeomNode().setScale(scale)
            self.setHeight(self.height)
        

    
    def getNametagScale(self):
        return self.nametagScale

    
    def setNametagScale(self, scale):
        self.nametagScale = scale
        self.nametag3d.setScale(scale)

    
    def getHeight(self):
        return self.height

    
    def setHeight(self, height):
        self.height = height
        self.nametag3d.setPos(0, 0, height + 0.5)
        if self.collTube:
            self.collTube.setPointB(0, 0, height - self.getRadius())
            if self.collNodePath:
                self.collNodePath.forceRecomputeBounds()
            
        

    
    def getRadius(self):
        return 1

    
    def getName(self):
        return self.name

    
    def setName(self, name):
        if hasattr(self, 'isDisguised'):
            if self.isDisguised:
                return None
            
        
        self.name = name
        self.nametag.setName(name)

    
    def setDisplayName(self, str):
        if hasattr(self, 'isDisguised'):
            if self.isDisguised:
                return None
            
        
        self.nametag.setDisplayName(str)

    
    def getFont(self):
        return self._Avatar__font

    
    def setFont(self, font):
        self._Avatar__font = font
        self.nametag.setFont(font)

    
    def getStyle(self):
        return self.style

    
    def setStyle(self, style):
        self.style = style

    
    def getDialogueArray(self):
        return None

    
    def playCurrentDialogue(self, dialogue, chatFlags, interrupt = 1):
        if interrupt and self._Avatar__currentDialogue is not None:
            self._Avatar__currentDialogue.stop()
        
        self._Avatar__currentDialogue = dialogue
        if dialogue:
            base.playSfx(dialogue, node = self)
        elif chatFlags & CFSpeech != 0 and self.nametag.getNumChatPages() > 0:
            self.playDialogueForString(self.nametag.getChat())
            base.playSfx(self.soundChatBubble, node = self)
        

    
    def playDialogue(self, type, length):
        dialogueArray = self.getDialogueArray()
        if dialogueArray == None:
            return None
        
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
        

    
    def playDialogueForString(self, chatString):
        searchString = string.lower(chatString)
        if string.find(searchString, Localizer.DialogSpecial) >= 0:
            type = 'special'
        elif string.find(searchString, Localizer.DialogExclamation) >= 0:
            type = 'exclamation'
        elif string.find(searchString, Localizer.DialogQuestion) >= 0:
            type = 'question'
        else:
            animal = self.getStyle().getType()
            if animal == 'dog' and animal == 'horse' or animal == 'duck':
                type = 'statementA'
            else:
                type = 'statementB'
        stringLength = len(chatString)
        if stringLength <= Localizer.DialogLength1:
            length = 1
        elif stringLength <= Localizer.DialogLength2:
            length = 2
        elif stringLength <= Localizer.DialogLength3:
            length = 3
        else:
            length = 4
        self.playDialogue(type, length)
        return None

    
    def setChatAbsolute(self, chatString, chatFlags, dialogue = None, interrupt = 1):
        self.nametag.setChat(chatString, chatFlags)
        self.playCurrentDialogue(dialogue, chatFlags, interrupt)

    
    def clearChat(self):
        self.nametag.clearChat()

    
    def isInView(self):
        pos = self.getPos(camera)
        eyePos = Point3(pos[0], pos[1], pos[2] + self.getHeight())
        return base.camNode.isInView(eyePos)

    
    def getNameVisible(self):
        return self._Avatar__nameVisible

    
    def setNameVisible(self, bool):
        self._Avatar__nameVisible = bool
        if bool:
            self.showName()
        
        if not bool:
            self.hideName()
        

    
    def hideName(self):
        self.nametag.getNametag3d().setContents(Nametag.CSpeech | Nametag.CThought)

    
    def showName(self):
        if self._Avatar__nameVisible and not (self.ghostMode):
            self.nametag.getNametag3d().setContents(Nametag.CName | Nametag.CSpeech | Nametag.CThought)
        

    
    def hideNametag2d(self):
        self.nametag2dContents = 0
        self.nametag.getNametag2d().setContents(self.nametag2dContents & self.nametag2dDist)

    
    def showNametag2d(self):
        self.nametag2dContents = self.nametag2dNormalContents
        if self.ghostMode:
            self.nametag2dContents = Nametag.CSpeech
        
        self.nametag.getNametag2d().setContents(self.nametag2dContents & self.nametag2dDist)

    
    def hideNametag3d(self):
        self.nametag.getNametag3d().setContents(0)

    
    def showNametag3d(self):
        if self._Avatar__nameVisible and not (self.ghostMode):
            self.nametag.getNametag3d().setContents(Nametag.CName | Nametag.CSpeech | Nametag.CThought)
        else:
            self.nametag.getNametag3d().setContents(0)

    
    def setPickable(self, flag):
        self.nametag.setActive(flag)

    
    def clickedNametag(self):
        if self.nametag.hasButton():
            self.advancePageNumber()
        elif self.nametag.isActive():
            messenger.send('clickedNametag', [
                self])
        

    
    def setPageChat(self, addressee, paragraph, message, quitButton, extraChatFlags = None, dialogueList = []):
        self._Avatar__chatAddressee = addressee
        self._Avatar__chatPageNumber = None
        self._Avatar__chatParagraph = paragraph
        self._Avatar__chatMessage = message
        if extraChatFlags is None:
            self._Avatar__chatFlags = CFSpeech
        else:
            self._Avatar__chatFlags = CFSpeech | extraChatFlags
        self._Avatar__chatDialogueList = dialogueList
        self._Avatar__chatSet = 0
        self._Avatar__chatLocal = 0
        self._Avatar__updatePageChat()
        if addressee == toonbase.localToon.doId:
            self._Avatar__chatFlags |= CFPageButton
            if quitButton:
                self._Avatar__chatFlags |= CFQuitButton
            
            self.b_setPageNumber(self._Avatar__chatParagraph, 0)
        

    
    def setLocalPageChat(self, message, quitButton, extraChatFlags = None, dialogueList = []):
        self._Avatar__chatAddressee = toonbase.localToon.doId
        self._Avatar__chatPageNumber = None
        self._Avatar__chatParagraph = None
        self._Avatar__chatMessage = message
        if extraChatFlags is None:
            self._Avatar__chatFlags = CFSpeech
        else:
            self._Avatar__chatFlags = CFSpeech | extraChatFlags
        self._Avatar__chatDialogueList = dialogueList
        self._Avatar__chatSet = 1
        self._Avatar__chatLocal = 1
        self._Avatar__chatFlags |= CFPageButton
        if quitButton:
            self._Avatar__chatFlags |= CFQuitButton
        
        if len(dialogueList) > 0:
            dialogue = dialogueList[0]
        else:
            dialogue = None
        self.setChatAbsolute(message, self._Avatar__chatFlags, dialogue)
        self.setPageNumber(None, 0)

    
    def setPageNumber(self, paragraph, pageNumber, timestamp = None):
        if timestamp == None:
            elapsed = 0.0
        else:
            elapsed = ClockDelta.globalClockDelta.localElapsedTime(timestamp)
        self._Avatar__chatPageNumber = [
            paragraph,
            pageNumber]
        self._Avatar__updatePageChat()
        if hasattr(self, 'uniqueName'):
            if pageNumber >= 0:
                messenger.send(self.uniqueName('nextChatPage'), [
                    pageNumber,
                    elapsed])
            else:
                messenger.send(self.uniqueName('doneChatPage'), [
                    elapsed])
        elif pageNumber >= 0:
            messenger.send('nextChatPage', [
                pageNumber,
                elapsed])
        else:
            messenger.send('doneChatPage', [
                elapsed])

    
    def advancePageNumber(self):
        if self._Avatar__chatAddressee == toonbase.localToon.doId and self._Avatar__chatPageNumber != None and self._Avatar__chatPageNumber[0] == self._Avatar__chatParagraph:
            pageNumber = self._Avatar__chatPageNumber[1]
            if pageNumber >= 0:
                pageNumber += 1
                if pageNumber >= self.nametag.getNumChatPages():
                    pageNumber = -1
                
                if self._Avatar__chatLocal:
                    self.setPageNumber(self._Avatar__chatParagraph, pageNumber)
                else:
                    self.b_setPageNumber(self._Avatar__chatParagraph, pageNumber)
            
        

    
    def _Avatar__updatePageChat(self):
        if self._Avatar__chatPageNumber != None and self._Avatar__chatPageNumber[0] == self._Avatar__chatParagraph:
            pageNumber = self._Avatar__chatPageNumber[1]
            if pageNumber >= 0:
                if not (self._Avatar__chatSet):
                    if len(self._Avatar__chatDialogueList) > 0:
                        dialogue = self._Avatar__chatDialogueList[0]
                    else:
                        dialogue = None
                    self.setChatAbsolute(self._Avatar__chatMessage, self._Avatar__chatFlags, dialogue)
                    self._Avatar__chatSet = 1
                
                if pageNumber < self.nametag.getNumChatPages():
                    self.nametag.setPageNumber(pageNumber)
                    if pageNumber > 0:
                        if len(self._Avatar__chatDialogueList) > pageNumber:
                            dialogue = self._Avatar__chatDialogueList[pageNumber]
                        else:
                            dialogue = None
                        self.playCurrentDialogue(dialogue, self._Avatar__chatFlags)
                    
                else:
                    self.clearChat()
            else:
                self.clearChat()
        

    
    def getAirborneHeight(self):
        height = self.getPos(self.shadowPlacer.shadowNodePath)
        return height.getZ() + 0.025000000000000001

    
    def initializeDropShadow(self):
        self.deleteDropShadow()
        self.getGeomNode().setZ(0.025000000000000001)
        dropShadow = loader.loadModelCopy('phase_3/models/props/drop_shadow')
        dropShadow.setScale(0.40000000000000002)
        shadowJoint = self.getShadowJoint()
        copy = dropShadow.copyTo(shadowJoint)
        copy.flattenMedium()
        copy.setBillboardAxis(2)
        copy.setColor(0.0, 0.0, 0.0, 0.5, 1)
        self.shadowPlacer = ShadowPlacer.ShadowPlacer(base.shadowTrav, copy, ToontownGlobals.WallBitmask, ToontownGlobals.FloorBitmask)
        self.dropShadow = copy
        dropShadow.removeNode()
        self.setActiveShadow(self.activeShadow)

    
    def deleteDropShadow(self):
        if self.shadowPlacer:
            self.shadowPlacer.delete()
            self.shadowPlacer = None
        
        if self.dropShadow:
            self.dropShadow.removeNode()
            self.dropShadow = None
        

    
    def setActiveShadow(self, isActive = 1):
        if self.shadowPlacer is not None:
            if self.activeShadow != isActive:
                self.activeShadow = isActive
                if isActive:
                    self.shadowPlacer.on()
                else:
                    self.shadowPlacer.off()
            
        

    
    def setShadowHeight(self, shadowHeight):
        if self.dropShadow:
            self.dropShadow.setZ(-shadowHeight)
        

    
    def initializeNametag3d(self):
        self.deleteNametag3d()
        nametagNode = self.nametag.getNametag3d().upcastToPandaNode()
        self.nametag3d.attachNewNode(nametagNode)
        iconNodePath = self.nametag.getNameIcon()
        for cJoint in self.getNametagJoints():
            cJoint.clearNetTransforms()
            cJoint.addNetTransform(nametagNode)
        

    
    def deleteNametag3d(self):
        children = self.nametag3d.getChildren()
        for i in range(children.getNumPaths()):
            children[i].removeNode()
        

    
    def initializeBodyCollisions(self, collIdStr):
        self.collTube = CollisionTube(0, 0, 0.5, 0, 0, self.height - self.getRadius(), self.getRadius())
        self.collNode = CollisionNode(collIdStr)
        self.collNode.addSolid(self.collTube)
        self.collNodePath = self.attachNewNode(self.collNode)
        if self.ghostMode:
            self.collNode.setCollideMask(ToontownGlobals.GhostBitmask)
        else:
            self.collNode.setCollideMask(ToontownGlobals.WallBitmask | ToontownGlobals.PieBitmask)

    
    def disableBodyCollisions(self):
        if hasattr(self, 'collNodePath'):
            self.collNodePath.removeNode()
            del self.collNodePath
        
        self.collTube = None

    
    def addActive(self):
        self.notify.debug('Adding avatar %s' % self.getName())
        
        try:
            Avatar.ActiveAvatars.remove(self)
        except ValueError:
            pass

        Avatar.ActiveAvatars.append(self)
        self.nametag.manage(toonbase.marginManager)
        self.accept(self.nametag.getUniqueId(), self.clickedNametag)

    
    def removeActive(self):
        self.notify.debug('Removing avatar %s' % self.getName())
        
        try:
            Avatar.ActiveAvatars.remove(self)
        except ValueError:
            self.notify.warning('%s was not present...' % self.getName())

        self.nametag.unmanage(toonbase.marginManager)
        self.ignore(self.nametag.getUniqueId())


