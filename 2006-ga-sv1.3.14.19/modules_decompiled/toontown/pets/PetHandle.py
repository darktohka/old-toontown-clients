# File: P (Python 2.2)

from toontown.toonbase import ToontownGlobals
from toontown.pets import PetMood, PetTraits

class PetHandle:
    
    def __init__(self, avatar):
        self.doId = avatar.doId
        self.name = avatar.name
        self.style = avatar.style
        self.ownerId = avatar.ownerId
        self.setLastSeenTimestamp(avatar.lastSeenTimestamp)
        self.bFake = False
        self.cr = avatar.cr
        self.traits = PetTraits.PetTraits(avatar.traitSeed, avatar.safeZone, traitValueList = avatar.traitList)
        self.mood = avatar.lastKnownMood.makeCopy()
        self.mood.pet = self
        self.lastKnownMood = self.mood.makeCopy()
        self.updateOfflineMood()

    
    def getDoId(self):
        return self.doId

    
    def getOwnerId(self):
        return self.ownerId

    
    def isPet(self):
        return True

    
    def getName(self):
        return self.name

    
    def getDNA(self):
        return self.style

    
    def getFont(self):
        return ToontownGlobals.getToonFont()

    
    def setLastSeenTimestamp(self, timestamp):
        self.lastSeenTimestamp = timestamp

    
    def getTimeSinceLastSeen(self):
        t = self.cr.getServerTimeOfDay() - self.lastSeenTimestamp
        return max(0.0, t)

    
    def updateOfflineMood(self):
        self.mood.driftMood(dt = self.getTimeSinceLastSeen(), curMood = self.lastKnownMood)

    
    def getDominantMood(self):
        if not hasattr(self, 'mood'):
            return PetMood.PetMood.Neutral
        
        return self.mood.getDominantMood()

    
    def uniqueName(self, idString):
        return idString + '-' + str(self.getDoId())


