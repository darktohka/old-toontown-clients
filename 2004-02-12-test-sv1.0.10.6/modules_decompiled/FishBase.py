# File: F (Python 2.2)

import FishGlobals
import Localizer
import DirectNotifyGlobal

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
        return Localizer.FishGenusNames[self.genus]

    
    def getSpeciesName(self):
        return Localizer.FishSpeciesNames[self.genus][self.species]

    
    def setNameIndexes(self, nameIndexes):
        self._FishBase__nameIndexes = nameIndexes
        if self.adopted:
            self.adoptedName = self.computeAdoptedName()
        else:
            self.adoptedName = ''

    
    def computeAdoptedName(self):
        first = Localizer.FishFirstNames[self._FishBase__nameIndexes[0]]
        lastPrefix = Localizer.FishLastPrefixNames[self._FishBase__nameIndexes[1]]
        lastSuffix = Localizer.FishLastSuffixNames[self._FishBase__nameIndexes[2]]
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

    
    def getActor(self):
        import Actor
        dict = FishGlobals.FishFileDict
        fileNames = dict.get(self.genus, dict[-1])
        prefix = 'phase_%s/models/char/' % fileNames[0]
        actor = Actor.Actor(prefix + fileNames[1], {
            'swim': prefix + fileNames[2] })
        return actor

    
    def __str__(self):
        return '%s, weight: %s value: %s' % (self.getSpeciesName(), self.weight, self.getValue())


