# File: D (Python 2.2)

from direct.distributed.ClockDelta import *
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject

class DistributedGuild(DistributedObject.DistributedObject):
    
    def __init__(self, air):
        DistributedObject.DistributedObject.__init__(self, air)

    
    def delete(self):
        self.ignoreAll()
        DistributedObject.DistributedObject.delete(self)

    
    def setName(self, name):
        self.name = name

    
    def setDateCreated(self, dateCreated):
        self.dateCreated = dateCreated

    
    def setOwnerAvatarId(self, ownerAvatarId):
        self.ownerAvatarId = ownerAvatarId

    
    def setGuldStatus(self, guildStatus):
        self.guildStatus = guildStatus

    
    def setReputations(self, reputations):
        self.reputations = reputations

    
    def setMemberListId(self, memberListId):
        self.memberListId = memberListId


