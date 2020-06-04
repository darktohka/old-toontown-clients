# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\shtiker\NewbiePurchaseManagerAI.py
import PurchaseManagerAI

class NewbiePurchaseManagerAI(PurchaseManagerAI.PurchaseManagerAI):
    __module__ = __name__

    def __init__(self, air, newbieId, playerArray, mpArray, previousMinigameId, trolleyZone):
        self.ownedNewbieId = newbieId
        newbieList = []
        PurchaseManagerAI.PurchaseManagerAI.__init__(self, air, playerArray, mpArray, previousMinigameId, trolleyZone, newbieList)

    def startCountdown(self):
        pass

    def getOwnedNewbieId(self):
        return self.ownedNewbieId

    def getInvolvedPlayerIds(self):
        return [
         self.ownedNewbieId]

    def handlePlayerLeaving(self, avId):
        toon = self.air.doId2do.get(avId)
        if toon:
            self.air.questManager.toonRodeTrolleyFirstTime(toon)