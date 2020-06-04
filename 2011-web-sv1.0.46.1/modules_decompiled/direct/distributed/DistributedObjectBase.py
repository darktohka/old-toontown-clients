# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\distributed\DistributedObjectBase.py
from direct.showbase.DirectObject import DirectObject

class DistributedObjectBase(DirectObject):
    __module__ = __name__
    notify = directNotify.newCategory('DistributedObjectBase')

    def __init__(self, cr):
        self.cr = cr
        self.children = {}
        self.parentId = None
        self.zoneId = None
        return

    def getLocation(self):
        try:
            if self.parentId == 0 and self.zoneId == 0:
                return
            if self.parentId == 4294967295 and self.zoneId == 4294967295:
                return
            return (
             self.parentId, self.zoneId)
        except AttributeError:
            return

        return

    def handleChildArrive(self, childObj, zoneId):
        pass

    def handleChildArriveZone(self, childObj, zoneId):
        pass

    def handleChildLeave(self, childObj, zoneId):
        pass

    def handleChildLeaveZone(self, childObj, zoneId):
        pass

    def handleQueryObjectChildrenLocalDone(self, context):
        pass

    def getParentObj(self):
        if self.parentId is None:
            return
        return self.cr.doId2do.get(self.parentId)

    def hasParentingRules(self):
        return self.dclass.getFieldByName('setParentingRules') != None