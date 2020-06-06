# File: S (Python 2.2)

from PandaModules import *
from ClockDelta import *
import math
import whrandom
import Point3
import DirectNotifyGlobal
import SuitBattleGlobals
import SuitTimings
import AvatarDNA
import Localizer
TIME_BUFFER_PER_WPT = 0.25
TIME_DIVISOR = 100
DISTRIBUTE_TASK_CREATION = 0

class SuitBase:
    notify = DirectNotifyGlobal.directNotify.newCategory('SuitBase')
    
    def __init__(self):
        self.dna = None
        self.level = 0
        self.maxHP = 10
        self.currHP = 10

    
    def delete(self):
        return None

    
    def getStyleName(self):
        if self.dna:
            return self.dna.name
        else:
            self.notify.error('called getStyleName() before dna was set!')
            return 'unknown'

    
    def getStyleDept(self):
        if self.dna:
            return AvatarDNA.getDeptFullname(self.dna.dept)
        else:
            self.notify.error('called getStyleDept() before dna was set!')
            return 'unknown'

    
    def getLevel(self):
        return self.level

    
    def setLevel(self, level):
        self.level = level
        nameWLevel = Localizer.SuitBaseNameWithLevel % {
            'name': self.name,
            'dept': self.getStyleDept(),
            'level': self.getActualLevel() }
        self.setDisplayName(nameWLevel)
        attributes = SuitBattleGlobals.SuitAttributes[self.dna.name]
        self.maxHP = attributes['hp'][self.level]
        self.currHP = self.maxHP

    
    def setDisplayName(self, str):
        self.notify.debug('setDisplayName(): setting suit name')
        self.nametag.setDisplayName(str)

    
    def getActualLevel(self):
        return SuitBattleGlobals.getActualFromRelativeLevel(self.getStyleName(), self.level) + 1

    
    def setPath(self, path):
        self.path = path
        self.pathLength = self.path.getNumPoints()

    
    def getPath(self):
        return self.path

    
    def printPath(self):
        print '%d points in path' % self.pathLength
        for currPathPt in range(self.pathLength):
            indexVal = self.path.getPointIndex(currPathPt)
            print '\t', self.sp.dnaStore.getSuitPointWithIndex(indexVal)
        

    
    def makeLegList(self):
        self.legList = SuitLegList(self.path, self.sp.dnaStore, self.sp.suitWalkSpeed, SuitTimings.fromSky, SuitTimings.toSky, SuitTimings.fromSuitBuilding, SuitTimings.toSuitBuilding, SuitTimings.toToonBuilding)


