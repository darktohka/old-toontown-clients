# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\uberdog\DistributedInGameNewsMgr.py
import socket, datetime, os
from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from direct.distributed.DistributedObject import DistributedObject
from toontown.toonbase import ToontownGlobals
from toontown.uberdog import InGameNewsResponses

class DistributedInGameNewsMgr(DistributedObject):
    __module__ = __name__
    notify = directNotify.newCategory('InGameNewsMgr')
    neverDisable = 1

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        base.cr.inGameNewsMgr = self

    def delete(self):
        DistributedObject.delete(self)
        self.cr.inGameNewsMgr = None
        return

    def disable(self):
        self.notify.debug("i'm disabling InGameNewsMgr  rightnow.")
        DistributedObject.disable(self)

    def generate(self):
        self.notify.debug('BASE: generate')
        DistributedObject.generate(self)

    def setLatestIssueStr(self, issueStr):
        self.latestIssueStr = issueStr
        self.latestIssue = base.cr.toontownTimeManager.convertUtcStrToToontownTime(issueStr)
        messenger.send('newIssueOut')
        self.notify.info('latestIssue=%s' % self.latestIssue)

    def getLatestIssueStr(self):
        pass

    def getLatestIssue(self):
        return self.latestIssue