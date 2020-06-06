# File: H (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.showbase import DirectObject
from direct.directnotify import DirectNotifyGlobal
from toontown.launcher import DownloadForceAcknowledge
import string
import whrandom
from toontown.toonbase import ToontownGlobals
from toontown.hood import ZoneUtil

class HoodMgr(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('HoodMgr')
    ToontownCentralInitialDropPoints = ([
        -90.700000000000003,
        -60.0,
        0.025000000000000001,
        102.575,
        0,
        0], [
        -91.400000000000006,
        -40.5,
        -3.948,
        125.76300000000001,
        0,
        0], [
        -107.8,
        -17.800000000000001,
        -1.9370000000000001,
        149.45599999999999,
        0,
        0], [
        -108.7,
        12.800000000000001,
        -1.7669999999999999,
        158.756,
        0,
        0], [
        -42.100000000000001,
        -22.800000000000001,
        -1.3280000000000001,
        -248.09999999999999,
        0,
        0], [
        -35.200000000000003,
        -60.200000000000003,
        0.025000000000000001,
        -265.63900000000001,
        0,
        0])
    ToontownCentralHQDropPoints = ([
        -43.5,
        42.600000000000001,
        -0.55000000000000004,
        -100.45399999999999,
        0,
        0], [
        -53.0,
        12.5,
        -2.948,
        281.50200000000001,
        0,
        0], [
        -40.299999999999997,
        -18.5,
        -0.91300000000000003,
        -56.673999999999999,
        0,
        0], [
        -1.8999999999999999,
        -37.0,
        0.025000000000000001,
        -23.43,
        0,
        0], [
        1.8999999999999999,
        -5.9000000000000004,
        4.0,
        -37.941000000000003,
        0,
        0])
    ToontownCentralTunnelDropPoints = ([
        -28.300000000000001,
        40.100000000000001,
        0.25,
        17.25,
        0,
        0], [
        -63.75,
        58.960000000000001,
        -0.5,
        -23.75,
        0,
        0], [
        -106.93000000000001,
        17.66,
        -2.2000000000000002,
        99.0,
        0,
        0], [
        -116.0,
        -21.5,
        -0.037999999999999999,
        50.0,
        0,
        0], [
        74.879999999999995,
        -115.0,
        2.5299999999999998,
        -224.41,
        0,
        0], [
        30.488,
        -101.5,
        2.5299999999999998,
        -179.22999999999999,
        0,
        0])
    dropPoints = {
        ToontownGlobals.DonaldsDock: ([
            -28.0,
            -2.5,
            5.7999999999999998,
            120.0,
            0.0,
            0.0], [
            -22,
            13,
            5.7999999999999998,
            155.59999999999999,
            0.0,
            0.0], [
            67,
            47,
            5.7000000000000002,
            134.69999999999999,
            0.0,
            0.0], [
            62,
            19,
            5.7000000000000002,
            97.0,
            0.0,
            0.0], [
            66,
            -27,
            5.7000000000000002,
            80.5,
            0.0,
            0.0], [
            -114,
            -7,
            5.7000000000000002,
            -97.0,
            -0.0,
            0.0], [
            -108,
            36,
            5.7000000000000002,
            -153.80000000000001,
            -0.0,
            0.0], [
            -116,
            -46,
            5.7000000000000002,
            -70.099999999999994,
            -0.0,
            0.0], [
            -63,
            -79,
            5.7000000000000002,
            -41.200000000000003,
            -0.0,
            0.0], [
            -2,
            -79,
            5.7000000000000002,
            57.399999999999999,
            -0.0,
            0.0], [
            -38,
            -78,
            5.7000000000000002,
            9.0999999999999996,
            -0.0,
            0.0]),
        ToontownGlobals.ToontownCentral: ([
            -60,
            -8,
            1.3,
            -90,
            0,
            0], [
            -66,
            -9,
            1.3,
            -274,
            0,
            0], [
            17,
            -28,
            4.0999999999999996,
            -44,
            0,
            0], [
            87.700000000000003,
            -22,
            4,
            66,
            0,
            0], [
            -9.5999999999999996,
            61.100000000000001,
            0,
            132,
            0,
            0], [
            -109.0,
            -2.5,
            -1.6559999999999999,
            -90,
            0,
            0], [
            -35.399999999999999,
            -81.299999999999997,
            0.5,
            -4,
            0,
            0], [
            -103,
            72,
            0,
            -141,
            0,
            0], [
            93.5,
            -148.40000000000001,
            2.5,
            43,
            0,
            0], [
            25,
            123.40000000000001,
            2.5499999999999998,
            272,
            0,
            0], [
            48,
            39,
            4,
            201,
            0,
            0], [
            -80,
            -61,
            0.10000000000000001,
            -265,
            0,
            0], [
            -46.875,
            43.68,
            -1.05,
            124,
            0,
            0], [
            34,
            -105,
            2.5499999999999998,
            45,
            0,
            0], [
            16,
            -75,
            2.5499999999999998,
            56,
            0,
            0], [
            -27,
            -56,
            0.10000000000000001,
            45,
            0,
            0], [
            100,
            27,
            4.0999999999999996,
            150,
            0,
            0], [
            -70,
            4.5999999999999996,
            -1.8999999999999999,
            90,
            0,
            0], [
            -130.69999999999999,
            50,
            0.55000000000000004,
            -111,
            0,
            0]),
        ToontownGlobals.TheBrrrgh: ([
            35,
            -32,
            6.2000000000000002,
            138,
            0.0,
            0.0], [
            26,
            -105,
            6.2000000000000002,
            -339,
            0.0,
            0.0], [
            -29,
            -139,
            6.2000000000000002,
            -385,
            0.0,
            0.0], [
            -79,
            -123,
            6.2000000000000002,
            -369,
            0.0,
            0.0], [
            -114,
            -86,
            3,
            -54,
            0.0,
            0.0], [
            -136,
            9,
            6.2000000000000002,
            -125,
            0.0,
            0.0], [
            -75,
            92,
            6.2000000000000002,
            -187,
            0.0,
            0.0], [
            -7,
            75,
            6.2000000000000002,
            -187,
            0.0,
            0.0], [
            -106,
            -42,
            8.5999999999999996,
            -111,
            0.0,
            0.0], [
            -116,
            -44,
            8.3000000000000007,
            -20,
            0.0,
            0.0]),
        ToontownGlobals.MinniesMelodyland: ([
            86,
            44,
            -13.5,
            121.09999999999999,
            0.0,
            0.0], [
            88,
            -8,
            -13.5,
            91,
            0,
            0], [
            92,
            -76,
            -13.5,
            62.5,
            0.0,
            0.0], [
            53,
            -112,
            6.5,
            65.799999999999997,
            0.0,
            0.0], [
            -69,
            -71,
            6.5,
            -67.200000000000003,
            0.0,
            0.0], [
            -75,
            21,
            6.5,
            -100.90000000000001,
            0.0,
            0.0], [
            -21,
            72,
            6.5,
            -129.5,
            0.0,
            0.0], [
            56,
            72,
            6.5,
            138.19999999999999,
            0.0,
            0.0], [
            -41,
            47,
            6.5,
            -98.900000000000006,
            0.0,
            0.0]),
        ToontownGlobals.DaisyGardens: ([
            0,
            0,
            0,
            -10.5,
            0,
            0], [
            76,
            35,
            1.1000000000000001,
            -30.199999999999999,
            0.0,
            0.0], [
            97,
            106,
            0.0,
            51.399999999999999,
            0.0,
            0.0], [
            51,
            180,
            10.0,
            22.600000000000001,
            0.0,
            0.0], [
            -14,
            203,
            10.0,
            85.599999999999994,
            0.0,
            0.0], [
            -58,
            158,
            10.0,
            -146.90000000000001,
            0.0,
            0.0], [
            -86,
            128,
            0.0,
            -178.90000000000001,
            0.0,
            0.0], [
            -64,
            65,
            0.0,
            17.699999999999999,
            0.0,
            0.0], [
            -13,
            39,
            0.0,
            -15.699999999999999,
            0.0,
            0.0], [
            -12,
            193,
            0.0,
            -112.40000000000001,
            0.0,
            0.0], [
            87,
            128,
            0.0,
            45.399999999999999,
            0.0,
            0.0]),
        ToontownGlobals.DonaldsDreamland: ([
            77,
            91,
            0.0,
            124.40000000000001,
            0.0,
            0.0], [
            29,
            92,
            0.0,
            -154.5,
            0.0,
            0.0], [
            -28,
            49,
            -16.399999999999999,
            -142.0,
            0.0,
            0.0], [
            21,
            40,
            -16.0,
            -65.099999999999994,
            0.0,
            0.0], [
            48,
            27,
            -15.4,
            -161.0,
            0.0,
            0.0], [
            -2,
            -22,
            -15.199999999999999,
            -132.09999999999999,
            0.0,
            0.0], [
            -92,
            -88,
            0.0,
            -116.3,
            0.0,
            0.0], [
            -56,
            -93,
            0.0,
            -21.5,
            0.0,
            0.0], [
            20,
            -88,
            0.0,
            -123.40000000000001,
            0.0,
            0.0], [
            76,
            -90,
            0.0,
            11.0,
            0.0,
            0.0]),
        ToontownGlobals.Tutorial: ([
            130.90000000000001,
            -8.5999999999999996,
            -1.3,
            105.5,
            0,
            0],),
        ToontownGlobals.SellbotHQ: ([
            64,
            -128,
            0.26000000000000001,
            36,
            0,
            0], [
            9,
            -140,
            0.26000000000000001,
            0,
            0,
            0], [
            -82,
            -112,
            0.26000000000000001,
            -127,
            0,
            0], [
            -73,
            -213,
            0.26000000000000001,
            -23,
            0,
            0], [
            -20,
            -243,
            0.26000000000000001,
            -9,
            0,
            0], [
            79,
            -208,
            0.26000000000000001,
            43,
            0,
            0]),
        ToontownGlobals.CashbotHQ: ([
            102,
            -437,
            -23.439,
            360,
            0,
            0], [
            124,
            -437,
            -23.439,
            360,
            0,
            0], [
            110,
            -446,
            -23.439,
            360,
            0,
            0], [
            132,
            -446,
            -23.439,
            360,
            0,
            0]) }
    hoodName2Id = {
        'dd': ToontownGlobals.DonaldsDock,
        'tt': ToontownGlobals.ToontownCentral,
        'br': ToontownGlobals.TheBrrrgh,
        'mm': ToontownGlobals.MinniesMelodyland,
        'dg': ToontownGlobals.DaisyGardens,
        'cz': ToontownGlobals.ConstructionZone,
        'ff': ToontownGlobals.FunnyFarm,
        'gs': ToontownGlobals.GoofyStadium,
        'dl': ToontownGlobals.DonaldsDreamland,
        'bosshq': ToontownGlobals.BossbotHQ,
        'sellhq': ToontownGlobals.SellbotHQ,
        'cashhq': ToontownGlobals.CashbotHQ,
        'lawhq': ToontownGlobals.LawbotHQ }
    hoodId2Name = {
        ToontownGlobals.DonaldsDock: 'dd',
        ToontownGlobals.ToontownCentral: 'tt',
        ToontownGlobals.Tutorial: 'tt',
        ToontownGlobals.TheBrrrgh: 'br',
        ToontownGlobals.MinniesMelodyland: 'mm',
        ToontownGlobals.DaisyGardens: 'dg',
        ToontownGlobals.ConstructionZone: 'cz',
        ToontownGlobals.FunnyFarm: 'ff',
        ToontownGlobals.GoofyStadium: 'gs',
        ToontownGlobals.DonaldsDreamland: 'dl',
        ToontownGlobals.BossbotHQ: 'bosshq',
        ToontownGlobals.SellbotHQ: 'sellhq',
        ToontownGlobals.CashbotHQ: 'cashhq',
        ToontownGlobals.LawbotHQ: 'lawhq' }
    DefaultDropPoint = [
        0,
        0,
        0,
        0,
        0,
        0]
    dbgDropMode = 0
    currentDropPoint = 0
    
    def __init__(self, cr):
        self.cr = cr

    
    def getDropPoint(self, dropPointList):
        if self.dbgDropMode == 0:
            return whrandom.choice(dropPointList)
        else:
            droppnt = self.currentDropPoint % len(dropPointList)
            self.currentDropPoint = (self.currentDropPoint + 1) % len(dropPointList)
            return dropPointList[droppnt]

    
    def getAvailableZones(self):
        if base.launcher == None:
            return self.getZonesInPhase(4) + self.getZonesInPhase(6) + self.getZonesInPhase(8) + self.getZonesInPhase(9) + self.getZonesInPhase(10)
        else:
            first = base.launcher.firstPhase
            final = base.launcher.finalPhase
            zones = []
            for phase in range(first, final + 1):
                if base.launcher.getPhaseComplete(phase):
                    zones = zones + self.getZonesInPhase(phase)
                
            
            return zones

    
    def getZonesInPhase(self, phase):
        p = []
        for i in ToontownGlobals.phaseMap.items():
            if i[1] == phase:
                p.append(i[0])
            
        
        return p

    
    def getPhaseFromHood(self, hoodId):
        hoodId = ZoneUtil.getCanonicalHoodId(hoodId)
        return ToontownGlobals.phaseMap[hoodId]

    
    def getPlaygroundCenterFromId(self, hoodId):
        dropPointList = self.dropPoints.get(hoodId, None)
        if dropPointList:
            return self.getDropPoint(dropPointList)
        else:
            self.notify.warning('getPlaygroundCenterFromId: No such hood name as: ' + str(hoodId))
            return self.DefaultDropPoint

    
    def getIdFromName(self, hoodName):
        id = self.hoodName2Id.get(hoodName)
        if id:
            return id
        else:
            self.notify.error('No such hood name as: %s' % hoodName)
            return None

    
    def getNameFromId(self, hoodId):
        name = self.hoodId2Name.get(hoodId)
        if name:
            return name
        else:
            self.notify.error('No such hood id as: %s' % hoodId)
            return None

    
    def getFullnameFromId(self, hoodId):
        hoodId = ZoneUtil.getCanonicalZoneId(hoodId)
        return ToontownGlobals.hoodNameMap[hoodId][-1]

    
    def addLinkTunnelHooks(self, hoodPart, nodeList, currentZoneId):
        tunnelOriginList = []
        for i in nodeList:
            linkTunnelNPC = i.findAllMatches('**/linktunnel*')
            for p in range(linkTunnelNPC.getNumPaths()):
                linkTunnel = linkTunnelNPC.getPath(p)
                name = linkTunnel.getName()
                nameParts = name.split('_')
                hoodStr = nameParts[1]
                zoneStr = nameParts[2]
                hoodId = self.getIdFromName(hoodStr)
                zoneId = int(zoneStr)
                hoodId = ZoneUtil.getTrueZoneId(hoodId, currentZoneId)
                zoneId = ZoneUtil.getTrueZoneId(zoneId, currentZoneId)
                linkSphere = linkTunnel.find('**/tunnel_trigger')
                if linkSphere.isEmpty():
                    linkSphere = linkTunnel.find('**/tunnel_sphere')
                
                if not linkSphere.isEmpty():
                    cnode = linkSphere.node()
                    cnode.setName('tunnel_trigger_' + hoodStr + '_' + zoneStr)
                    cnode.setCollideMask(ToontownGlobals.WallBitmask | ToontownGlobals.GhostBitmask)
                else:
                    linkSphere = linkTunnel.find('**/tunnel_trigger_' + hoodStr + '_' + zoneStr)
                    if linkSphere.isEmpty():
                        self.notify.error('tunnel_trigger not found')
                    
                tunnelOrigin = linkTunnel.find('**/tunnel_origin')
                if tunnelOrigin.isEmpty():
                    self.notify.error('tunnel_origin not found')
                
                tunnelOriginPlaceHolder = render.attachNewNode('toph_' + hoodStr + '_' + zoneStr)
                tunnelOriginList.append(tunnelOriginPlaceHolder)
                tunnelOriginPlaceHolder.setPos(tunnelOrigin.getPos(render))
                tunnelOriginPlaceHolder.setHpr(tunnelOrigin.getHpr(render))
                hood = base.localAvatar.cr.playGame.hood
                if ZoneUtil.tutorialDict:
                    how = 'teleportIn'
                    tutorialFlag = 1
                else:
                    how = 'tunnelIn'
                    tutorialFlag = 0
                hoodPart.accept('enter' + linkSphere.getName(), hoodPart.handleEnterTunnel, [
                    {
                        'loader': ZoneUtil.getLoaderName(zoneId),
                        'where': ZoneUtil.getToonWhereName(zoneId),
                        'how': how,
                        'hoodId': hoodId,
                        'zoneId': zoneId,
                        'shardId': None,
                        'tunnelOrigin': tunnelOriginPlaceHolder,
                        'tutorial': tutorialFlag }])
            
        
        return tunnelOriginList

    
    def extractGroupName(self, groupFullName):
        return string.split(groupFullName, ':', 1)[0]

    
    def makeLinkTunnelName(self, hoodId, currentZone):
        return '**/toph_' + self.getNameFromId(hoodId) + '_' + str(currentZone)


