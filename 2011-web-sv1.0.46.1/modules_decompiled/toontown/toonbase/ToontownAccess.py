# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\toonbase\ToontownAccess.py
from pandac.PandaModules import listProcessModules
from direct.task import Task
from toontown.hood import ZoneUtil
from toontown.toonbase import ToontownGlobals

class ToontownAccess:
    __module__ = __name__

    def __init__(self):
        self.startupModules = []

    def initModuleInfo(self):
        self.startupModules = self.getModuleList()
        taskMgr.doMethodLater(300, self.checkModuleInfo, 'moduleListTask')

    def delete(self):
        taskMgr.remove('moduleListTask')
        del self.startupModules

    def checkModuleInfo(self, task):
        currentModuleList = self.getModuleList()
        newModules = []
        for module in currentModuleList:
            if module not in self.startupModules:
                self.startupModules.insert(0, module)
                newModules.insert(0, module)

        self.sendUpdate('setModuleInfo', [newModules])
        return task.again

    def getModuleList(self):
        moduleString = listProcessModules()
        moduleList = []
        if moduleString:
            moduleList = moduleString.split(',')
        return moduleList

    def sendUpdate(self, fieldName, args=[], sendToId=None):
        if base.cr and hasattr(base, 'localAvatar'):
            dg = base.localAvatar.dclass.clientFormatUpdate(fieldName, sendToId or base.localAvatar.doId, args)
            base.cr.send(dg)

    def canAccess(self, zoneId=None):
        if base.cr.isPaid():
            return True
        allowed = False
        allowedZones = [ToontownGlobals.ToontownCentral, ToontownGlobals.MyEstate, ToontownGlobals.GoofySpeedway, ToontownGlobals.Tutorial]
        specialZones = [
         ToontownGlobals.SellbotLobby]
        if hasattr(base.cr, 'newsManager') and base.cr.newsManager:
            holidayIds = base.cr.newsManager.getHolidayIdList()
            if ToontownGlobals.SELLBOT_NERF_HOLIDAY in holidayIds:
                specialZones.append(ToontownGlobals.SellbotHQ)
        place = base.cr.playGame.getPlace()
        if zoneId:
            myHoodId = ZoneUtil.getCanonicalHoodId(zoneId)
        else:
            myHoodId = ZoneUtil.getCanonicalHoodId(place.zoneId)
        if hasattr(place, 'id'):
            myHoodId = place.id
        if myHoodId in allowedZones:
            allowed = True
        elif zoneId and zoneId in specialZones:
            allowed = True
        return allowed