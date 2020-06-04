# File: F (Python 2.2)

from toontown.toonbase import ToontownGlobals

class FriendHandle:
    
    def __init__(self, doId, name, style, petId, isAPet = False):
        self.doId = doId
        self.name = name
        self.style = style
        self.commonChatFlags = 0
        self.petId = petId
        self.isAPet = isAPet

    
    def getDoId(self):
        return self.doId

    
    def getPetId(self):
        return self.petId

    
    def hasPet(self):
        return self.getPetId() != 0

    
    def isPet(self):
        return self.isAPet

    
    def getName(self):
        return self.name

    
    def getFont(self):
        return ToontownGlobals.getToonFont()

    
    def uniqueName(self, idString):
        return idString + '-' + str(self.getDoId())

    
    def d_battleSOS(self, requesterId):
        base.localAvatar.sendUpdate('battleSOS', [
            requesterId], sendToId = self.doId)

    
    def d_teleportQuery(self, requesterId):
        base.localAvatar.sendUpdate('teleportQuery', [
            requesterId], sendToId = self.doId)

    
    def d_teleportResponse(self, avId, available, shardId, hoodId, zoneId):
        base.localAvatar.sendUpdate('teleportResponse', [
            avId,
            available,
            shardId,
            hoodId,
            zoneId], sendToId = self.doId)

    
    def d_teleportGiveup(self, requesterId):
        base.localAvatar.sendUpdate('teleportGiveup', [
            requesterId], sendToId = self.doId)

    
    def isUnderstandable(self):
        if self.commonChatFlags & base.localAvatar.commonChatFlags & ToontownGlobals.CommonChat:
            understandable = 1
        elif self.commonChatFlags & ToontownGlobals.SuperChat:
            understandable = 1
        elif base.localAvatar.commonChatFlags & ToontownGlobals.SuperChat:
            understandable = 1
        elif base.cr.getFriendFlags(self.doId) & ToontownGlobals.FriendChat:
            understandable = 1
        else:
            understandable = 0
        return understandable


