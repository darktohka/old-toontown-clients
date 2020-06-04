# File: F (Python 2.2)

import FishGlobals
from toontown.toonbase import TTLocalizer
from direct.directnotify import DirectNotifyGlobal

class FishBase:
    notify = DirectNotifyGlobal.directNotify.newCategory('FishBase')
    
    def __init__(self, genus, species, weight, adopted = 0, nameIndexes = (0, 0, 0)):
        self.genus = genus
        self.species = species
        self.weight = weight
        self.adopted = adopted
        self.setNameIndexes(nameIndexes)

    
    def getGenus(self):
        return self.genus

    
    def getSpecies(self):
        return self.species

    
    def getWeight(self):
        return self.weight

    
    def setWeight(self, weight):
        self.weight = weight

    
    def getVitals(self):
        return (self.genus, self.species, self.weight)

    
    def getValue(self):
        return FishGlobals.getValue(self.genus, self.species, self.weight)

    
    def getGenusName(self):
        return TTLocalizer.FishGenusNames[self.genus]

    
    def getSpeciesName(self):
        return TTLocalizer.FishSpeciesNames[self.genus][self.species]

    
    def setNameIndexes(self, nameIndexes):
        self._FishBase__nameIndexes = nameIndexes
        if self.adopted:
            self.adoptedName = self.computeAdoptedName()
        else:
            self.adoptedName = ''

    
    def computeAdoptedName(self):
        first = TTLocalizer.FishFirstNames[self._FishBase__nameIndexes[0]]
        lastPrefix = TTLocalizer.FishLastPrefixNames[self._FishBase__nameIndexes[1]]
        lastSuffix = TTLocalizer.FishLastSuffixNames[self._FishBase__nameIndexes[2]]
        last = lastPrefix + lastSuffix
        if first and last:
            return first + ' ' + last
        elif first and not last:
            return first
        elif last and not first:
            return last
        else:
            return ''

    
    def getAdoptedName(self):
        return self.adoptedName

    
    def getNameIndexes(self):
        return self._FishBase__nameIndexes

    
    def getRarity(self):
        return FishGlobals.getRarity(self.genus, self.species)

    
    def getPhase(self):
        dict = FishGlobals.FishFileDict
        fileInfo = dict.get(self.genus, dict[-1])
        return fileInfo[0]

    
    def getActor(self):
        prefix = 'phase_%s/models/char/' % self.getPhase()
        dict = FishGlobals.FishFileDict
        fileInfo = dict.get(self.genus, dict[-1])
        Actor = Actor
        import direct.actor
        actor = Actor.Actor(prefix + fileInfo[1], {
            'intro': prefix + fileInfo[2],
            'swim': prefix + fileInfo[3] })
        return actor

    
    def getSound(self):
        sound = None
        loop = None
        delay = None
        playRate = None
        if base.config.GetBool('want-fish-audio', 1):
            soundDict = FishGlobals.FishAudioFileDict
            fileInfo = soundDict.get(self.genus, None)
            if fileInfo:
                prefix = 'phase_%s/audio/sfx/' % self.getPhase()
                sound = loader.loadSfx(prefix + soundDict[self.genus][0])
                loop = soundDict[self.genus][1]
                delay = soundDict[self.genus][2]
                playRate = soundDict[self.genus][3]
            
        
        return (sound, loop, delay, playRate)

    
    def __str__(self):
        return '%s, weight: %s value: %s' % (self.getSpeciesName(), self.weight, self.getValue())


