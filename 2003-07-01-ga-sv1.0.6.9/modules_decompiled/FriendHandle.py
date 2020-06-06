# File: F (Python 2.2)

import ToontownGlobals

class FriendHandle:
    
    def __init__(self, doId, name, style):
        self.doId = doId
        self.name = name
        self.style = style
        self.commonChatFlags = 0

    
    def getDoId(self):
        return self.doId

    
    def getName(self):
        return self.name

    
    def getFont(self):
        return ToontownGlobals.getToonFont()

    
    def uniqueName(self, idString):
        return idString + '-' + str(self.getDoId())

    
    def d_battleSOS(self, requesterId):
        toonbase.localToon.sendUpdate('battleSOS', [
            requesterId], sendToId = self.doId)

    
    def d_teleportQuery(self, requesterId):
        toonbase.localToon.sendUpdate('teleportQuery', [
            requesterId], sendToId = self.doId)

    
    def d_teleportResponse(self, avId, available, shardId, hoodId, zoneId):
        toonbase.localToon.sendUpdate('teleportResponse', [
            avId,
            available,
            shardId,
            hoodId,
            zoneId], sendToId = self.doId)

    
    def d_teleportGiveup(self, requesterId):
        toonbase.localToon.sendUpdate('teleportGiveup', [
            requesterId], sendToId = self.doId)

    
    def isUnderstandable(self):
        if self.commonChatFlags & toonbase.localToon.commonChatFlags & ToontownGlobals.CommonChat:
            understandable = 1
        elif self.commonChatFlags & ToontownGlobals.SuperChat:
            understandable = 1
        elif toonbase.localToon.commonChatFlags & ToontownGlobals.SuperChat:
            understandable = 1
        elif toonbase.tcr.getFriendFlags(self.doId) & ToontownGlobals.FriendChat:
            understandable = 1
        else:
            understandable = 0
        return understandable


