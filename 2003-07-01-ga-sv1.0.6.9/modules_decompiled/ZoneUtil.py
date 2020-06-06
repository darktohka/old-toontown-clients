# File: Z (Python 2.2)

from ToontownGlobals import *
import DirectNotifyGlobal
zoneUtilNotify = DirectNotifyGlobal.directNotify.newCategory('ZoneUtil')
tutorialDict = None

def getStreetName(branchId):
    if tutorialDict:
        return StreetNames[20000][1]
    else:
        return StreetNames[branchId][1]


def getLoaderName(zoneId):
    if tutorialDict:
        if zoneId == ToontownCentral:
            loaderName = 'safeZoneLoader'
        else:
            loaderName = 'townLoader'
    else:
        suffix = zoneId % 1000
        if suffix >= 500:
            suffix -= 500
        
        if suffix < 100:
            loaderName = 'safeZoneLoader'
        else:
            loaderName = 'townLoader'
    return loaderName


def getBranchLoaderName(zoneId):
    return getLoaderName(getBranchZone(zoneId))


def getSuitWhereName(zoneId):
    where = getWhereName(zoneId, 0)
    return where


def getToonWhereName(zoneId):
    where = getWhereName(zoneId, 1)
    return where


def isPlayground(zoneId):
    if zoneId % 1000 == 0:
        pass
    return zoneId < 19999


def getWhereName(zoneId, isToon):
    if tutorialDict:
        if zoneId in tutorialDict['interiors']:
            where = 'toonInterior'
        elif zoneId in tutorialDict['exteriors']:
            where = 'street'
        elif zoneId == ToontownCentral:
            where = 'playground'
        else:
            zoneUtilNotify.error('No known zone: ' + str(zoneId))
    else:
        suffix = zoneId % 1000
        if suffix == 0:
            where = 'playground'
        elif suffix >= 500:
            if isToon:
                where = 'toonInterior'
            else:
                where = 'suitInterior'
        else:
            where = 'street'
    return where


def getBranchZone(zoneId):
    if tutorialDict:
        branchId = tutorialDict['branch']
    else:
        branchId = zoneId - zoneId % 100
        if zoneId % 1000 >= 500:
            branchId -= 500
        
    return branchId


def getHoodId(zoneId):
    if tutorialDict:
        hoodId = Tutorial
    else:
        hoodId = zoneId - zoneId % 1000
    return hoodId


def isInterior(zoneId):
    if tutorialDict:
        if zoneId in tutorialDict['interiors']:
            r = 1
        else:
            r = 0
    else:
        r = zoneId % 1000 >= 500
    return r


def overrideOn(branch, exteriorList, interiorList):
    global tutorialDict
    print 'OVERRIDE ON: '
    print exteriorList
    print interiorList
    if tutorialDict:
        zoneUtilNotify.warning('setTutorialDict: tutorialDict is already set!')
    
    tutorialDict = {
        'branch': branch,
        'exteriors': exteriorList,
        'interiors': interiorList }


def overrideOff():
    global tutorialDict
    print 'OVERRIDE OFF:'
    tutorialDict = None

