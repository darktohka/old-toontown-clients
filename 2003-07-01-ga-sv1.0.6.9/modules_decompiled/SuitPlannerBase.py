# File: S (Python 2.2)

from PandaModules import *
import whrandom
import string
import DirectNotifyGlobal
import ZoneUtil
import ToontownGlobals

class SuitPlannerBase:
    notify = DirectNotifyGlobal.directNotify.newCategory('SuitPlannerBase')
    
    def __init__(self):
        self.suitWalkSpeed = ToontownGlobals.SuitWalkSpeed
        self.dnaStore = None
        self.pointIndexes = { }
        return None

    
    def setupDNA(self):
        if self.dnaStore:
            return None
        
        self.dnaStore = DNAStorage()
        dnaFileName = self.genDNAFileName()
        
        try:
            simbase.air.loadDNAFileAI(self.dnaStore, dnaFileName)
        except:
            loader.loadDNAFileAI(self.dnaStore, dnaFileName)

        self.initDNAInfo()

    
    def genDNAFileName(self):
        
        try:
            return simbase.air.genDNAFileName(self.getZoneId())
        except:
            zone = self.getZoneId()
            hoodId = ZoneUtil.getHoodId(zone)
            hood = ToontownGlobals.dnaMap[hoodId]
            phase = ToontownGlobals.streetPhaseMap[hoodId]
            return 'phase_%s/dna/%s_%s.dna' % (phase, hood, zone)


    
    def getZoneId(self):
        return self.zoneId

    
    def setZoneId(self, zoneId):
        self.notify.debug('setting zone id for suit planner')
        self.zoneId = zoneId
        self.setupDNA()

    
    def extractGroupName(self, groupFullName):
        return string.split(groupFullName, ':', 1)[0]

    
    def initDNAInfo(self):
        self.battlePosDict = { }
        for i in range(self.dnaStore.getNumDNAVisGroupsAI()):
            vg = self.dnaStore.getDNAVisGroupAI(i)
            zoneId = int(self.extractGroupName(vg.getName()))
            if vg.getNumBattleCells() == 1:
                self.battlePosDict[zoneId] = vg.getBattleCell(0).getPos()
            elif vg.getNumBattleCells() > 1:
                self.notify.warning('multiple battle cells for zone: %d' % zoneId)
                self.battlePosDict[zoneId] = vg.getBattleCell(0).getPos()
            else:
                self.notify.warning('no battle cell for zone: %d' % zoneId)
                self.battlePosDict[zoneId] = Point3(0, 0, 0)
        
        self.dnaStore.resetDNAGroups()
        self.dnaStore.resetDNAVisGroups()
        self.dnaStore.resetDNAVisGroupsAI()
        self.streetPointList = []
        self.frontdoorPointList = []
        self.sidedoorPointList = []
        numPoints = self.dnaStore.getNumSuitPoints()
        for i in range(numPoints):
            point = self.dnaStore.getSuitPointAtIndex(i)
            if point.getPointType() == DNASuitPoint.STREETPOINT:
                self.streetPointList.append(point)
            elif point.getPointType() == DNASuitPoint.FRONTDOORPOINT:
                self.frontdoorPointList.append(point)
            elif point.getPointType() == DNASuitPoint.SIDEDOORPOINT:
                self.sidedoorPointList.append(point)
            
            self.pointIndexes[point.getIndex()] = point
        
        return None

    
    def performPathTest(self):
        if not self.notify.getDebug():
            return None
        
        startAndEnd = self.pickPath()
        if not startAndEnd:
            return None
        
        startPoint = startAndEnd[0]
        endPoint = startAndEnd[1]
        path = self.dnaStore.getSuitPath(startPoint, endPoint)
        numPathPoints = path.getNumPoints()
        for i in range(numPathPoints - 1):
            zone = self.dnaStore.getSuitEdgeZone(path.getPointIndex(i), path.getPointIndex(i + 1))
            travelTime = self.dnaStore.getSuitEdgeTravelTime(path.getPointIndex(i), path.getPointIndex(i + 1), self.suitWalkSpeed)
            self.notify.debug('edge from point ' + `i` + ' to point ' + `i + 1` + ' is in zone: ' + `zone` + ' and will take ' + `travelTime` + ' seconds to walk.')
        
        return None

    
    def genPath(self, startPoint, endPoint):
        if startPoint == endPoint:
            return None
        
        return self.dnaStore.getSuitPath(startPoint, endPoint)

    
    def getDnaStore(self):
        return self.dnaStore


