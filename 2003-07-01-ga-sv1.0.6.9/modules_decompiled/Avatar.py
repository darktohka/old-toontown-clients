# File: A (Python 2.2)

from ShowBaseGlobal import *
from PandaObject import *
from PandaModules import *
import ToontownGlobals
import Actor
import AvatarDNA
import ClockDelta
import Localizer

def reconsiderAllUnderstandable():
    for av in Avatar.ActiveAvatars:
        av.considerUnderstandable()
    


class Avatar(Actor.Actor):
    notify = Actor.directNotify.newCategory('Avatar')
    ActiveAvatars = []
    
    def __init__(self):
        
        try:
            pass
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
            self.nametag3d = self.attachNewNode('nametag3d')
            self.dropShadows = []
            self.scale = 1.0
            self.nametagScale = 1.0
            self.height = 0.0
            self.name = ''
            self.style = None
            self.commonChatFlags = 0
            self.understandable = 1
            self.setPlayerType(NametagGroup.CCNormal)
            self._Avatar__chatParagraph = None
            self._Avatar__chatMessage = None
            self._Avatar__chatFlags = 0
            self._Avatar__chatPageNumber = None
            self._Avatar__chatAddressee = None
            self._Avatar__chatSet = 0
            self._Avatar__chatLocal = 0

        return None

    
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
            elif type == AvatarDNA.charType:
                self.generateChar()
            else:
                Avatar.notify.error('unknown DNA type: %s' % type)
            self.initializeDropShadow()
            self.initializeNametag3d()
        return None

    
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

    
    def getName(self):
        return self.name

    
    def setName(self, name):
        self.name = name
        self.nametag.setName(name)

    
    def getFont(self):
        return self._Avatar__font

    
    def setFont(self, font):
        self._Avatar__font = font
        self.nametag.setFont(font)

    
    def getStyle(self):
        return self.style

    
    def setStyle(self, style):
        self.style = style

    
    def playDialogue(self, type, length):
        pass

    
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

    
    def setChatAbsolute(self, chatString, chatFlags):
        self.nametag.setChat(chatString, chatFlags)
        if chatFlags & CFSpeech != 0 and self.nametag.getNumChatPages() > 0:
            if self.getDistance(camera) < 100.0:
                self.playDialogueForString(self.nametag.getChat())
                base.playSfx(self.soundChatBubble, node = self)
            
        

    
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
        if self._Avatar__nameVisible:
            self.nametag.getNametag3d().setContents(Nametag.CName | Nametag.CSpeech | Nametag.CThought)
        

    
    def hideNametag2d(self):
        self.nametag2dContents = 0
        self.nametag.getNametag2d().setContents(self.nametag2dContents & self.nametag2dDist)

    
    def showNametag2d(self):
        self.nametag2dContents = Nametag.CName | Nametag.CSpeech
        self.nametag.getNametag2d().setContents(self.nametag2dContents & self.nametag2dDist)

    
    def hideNametag3d(self):
        self.nametag.getNametag3d().setContents(0)

    
    def showNametag3d(self):
        self.nametag.getNametag3d().setContents(Nametag.CName | Nametag.CSpeech | Nametag.CThought)

    
    def setPickable(self, flag):
        self.nametag.setActive(flag)

    
    def clickedNametag(self):
        if self.nametag.hasButton():
            self.advancePageNumber()
        else:
            messenger.send('clickedNametag', [
                self])

    
    def setPageChat(self, addressee, paragraph, message, quitButton, extraChatFlags = None):
        self._Avatar__chatAddressee = addressee
        self._Avatar__chatPageNumber = None
        self._Avatar__chatParagraph = paragraph
        self._Avatar__chatMessage = message
        if extraChatFlags is None:
            self._Avatar__chatFlags = CFSpeech
        else:
            self._Avatar__chatFlags = CFSpeech | extraChatFlags
        self._Avatar__chatSet = 0
        self._Avatar__chatLocal = 0
        self._Avatar__updatePageChat()
        if addressee == toonbase.localToon.doId:
            self._Avatar__chatFlags |= CFPageButton
            if quitButton:
                self._Avatar__chatFlags |= CFQuitButton
            
            self.b_setPageNumber(self._Avatar__chatParagraph, 0)
        

    
    def setLocalPageChat(self, message, quitButton, extraChatFlags = None):
        self._Avatar__chatAddressee = toonbase.localToon.doId
        self._Avatar__chatPageNumber = None
        self._Avatar__chatParagraph = None
        self._Avatar__chatMessage = message
        if extraChatFlags is None:
            self._Avatar__chatFlags = CFSpeech
        else:
            self._Avatar__chatFlags = CFSpeech | extraChatFlags
        self._Avatar__chatSet = 1
        self._Avatar__chatLocal = 1
        self._Avatar__chatFlags |= CFPageButton
        if quitButton:
            self._Avatar__chatFlags |= CFQuitButton
        
        self.setChatAbsolute(message, self._Avatar__chatFlags)
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
            if self._Avatar__chatPageNumber[1] >= 0:
                if not (self._Avatar__chatSet):
                    self.setChatAbsolute(self._Avatar__chatMessage, self._Avatar__chatFlags)
                    self._Avatar__chatSet = 1
                
                if self._Avatar__chatPageNumber[1] < self.nametag.getNumChatPages():
                    self.nametag.setPageNumber(self._Avatar__chatPageNumber[1])
                else:
                    self.clearChat()
            else:
                self.clearChat()
        

    
    def initializeDropShadow(self):
        self.deleteDropShadow()
        self.getGeomNode().setZ(0.025000000000000001)
        dropShadow = loader.loadModelCopy('phase_3/models/props/drop_shadow')
        dropShadow.setScale(0.40000000000000002)
        self.dropShadows = []
        for shadowJoint in self.getShadowJoints():
            copy = dropShadow.copyTo(shadowJoint)
            copy.flattenMedium()
            copy.setBillboardAxis(2)
            copy.setColor(0.0, 0.0, 0.0, 0.5, 1)
            self.dropShadows.append(copy)
        
        dropShadow.removeNode()

    
    def deleteDropShadow(self):
        for shadow in self.dropShadows:
            shadow.removeNode()
        
        self.dropShadows = []

    
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
        self.collSphere = CollisionSphere(0, 0, 0.5, 1.0)
        self.collNode = CollisionNode(collIdStr)
        self.collNode.addSolid(self.collSphere)
        self.collNodePath = self.attachNewNode(self.collNode)
        self.collNodePath.hide()
        self.collNode.setCollideMask(ToontownGlobals.WallBitmask)
        return None

    
    def disableBodyCollisions(self):
        self.collNodePath.removeNode()
        del self.collNodePath
        del self.collNode
        del self.collSphere

    
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


