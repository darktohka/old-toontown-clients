# File: G (Python 2.2)

import Actor
import Avatar
import AvatarDNA
import ToontownGlobals
from PandaModules import *
import Localizer
AnimDict = {
    'pg': (('walk', '-walk'), ('collapse', '-collapse'), ('recovery', '-recovery')) }
ModelDict = {
    'pg': 'phase_9/models/char/Cog_Goonie' }

class Goon(Avatar.Avatar):
    
    def __init__(self, dnaName):
        
        try:
            pass
        except:
            self.Goon_initialized = 1
            Avatar.Avatar.__init__(self)
            dna = AvatarDNA.AvatarDNA()
            dna.newGoon(dnaName)
            self.setDNA(dna)


    
    def delete(self):
        
        try:
            pass
        except:
            self.Goon_deleted = 1
            filePrefix = ModelDict[self.style.name]
            loader.unloadModel(filePrefix + '-zero')
            animList = AnimDict[self.style.name]
            for anim in animList:
                loader.unloadModel(filePrefix + anim[1])
            
            Avatar.Avatar.delete(self)

        return None

    
    def generateGoon(self):
        dna = self.style
        filePrefix = ModelDict[dna.name]
        self.loadModel(filePrefix + '-zero')
        animDict = { }
        animList = AnimDict[dna.name]
        for anim in animList:
            animDict[anim[0]] = filePrefix + anim[1]
        
        self.loadAnims(animDict)

    
    def getShadowJoint(self):
        return self.getGeomNode()

    
    def getNametagJoints(self):
        return []


