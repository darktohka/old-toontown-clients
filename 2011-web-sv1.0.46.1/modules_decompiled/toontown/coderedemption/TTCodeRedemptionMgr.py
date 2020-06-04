# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coderedemption\TTCodeRedemptionMgr.py
from direct.distributed.DistributedObject import DistributedObject
from direct.directnotify.DirectNotifyGlobal import directNotify

class TTCodeRedemptionMgr(DistributedObject):
    __module__ = __name__
    neverDisable = 1
    notify = directNotify.newCategory('TTCodeRedemptionMgr')

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)

    def announceGenerate(self):
        DistributedObject.announceGenerate(self)
        base.codeRedemptionMgr = self
        self._contextGen = SerialMaskedGen(4294967295)
        self._context2callback = {}

    def delete(self):
        if hasattr(base, 'codeRedemptionMgr'):
            if base.codeRedemptionMgr is self:
                del base.codeRedemptionMgr
        self._context2callback = None
        self._contextGen = None
        DistributedObject.delete(self)
        return

    def redeemCode(self, code, callback):
        context = self._contextGen.next()
        self._context2callback[context] = callback
        self.notify.debug('redeemCode(%s, %s)' % (context, code))
        self.sendUpdate('redeemCode', [context, code])

    def redeemCodeResult(self, context, result, awardMgrResult):
        self.notify.debug('redeemCodeResult(%s, %s, %s)' % (context, result, awardMgrResult))
        callback = self._context2callback.pop(context)
        callback(result, awardMgrResult)