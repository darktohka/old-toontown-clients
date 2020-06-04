# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\shtiker\NewbiePurchaseManager.py
import PurchaseManager
from toontown.quest import QuestParser
from toontown.toon import NPCToons

class NewbiePurchaseManager(PurchaseManager.PurchaseManager):
    __module__ = __name__

    def setOwnedNewbieId(self, ownedNewbieId):
        self.ownedNewbieId = ownedNewbieId

    def calcHasLocalToon(self):
        return base.localAvatar.doId == self.ownedNewbieId

    def announceGenerate(self):
        PurchaseManager.PurchaseManager.announceGenerate(self)
        if self.hasLocalToon:
            self.npc = NPCToons.createLocalNPC(2011)
            self.npc.addActive()

            def getDoId():
                return 0

            self.npc.getDoId = getDoId

            def acquireDelayDelete(name):
                return serialNum()

            self.npc.acquireDelayDelete = acquireDelayDelete

            def releaseDelayDelete(token):
                pass

            self.npc.releaseDelayDelete = releaseDelayDelete

            def uniqueName(string):
                return string

            self.npc.uniqueName = uniqueName
            self.accept('gagScreenIsUp', self.playMovie)
            self.purchase = base.cr.playGame.hood.purchase
            self.purchase.enterTutorialMode(self.ownedNewbieId)

    def disable(self):
        PurchaseManager.PurchaseManager.disable(self)
        if hasattr(self, 'movie'):
            self.npc.removeActive()
            self.npc.delete()
            del self.npc
            del self.movie

    def playMovie(self):
        self.movie = QuestParser.NPCMoviePlayer('gag_intro', base.localAvatar, self.npc)
        self.movie.setVar('backToPlaygroundButton', self.purchase.backToPlayground)
        self.movie.setVar('playAgainButton', self.purchase.playAgain)
        self.movie.setVar('purchaseBg', self.purchase.bg)
        self.movie.play()