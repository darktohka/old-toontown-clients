# File: C (Python 2.2)

import CatalogItem
import ToontownGlobals
import Localizer
from IntervalGlobal import *

class CatalogEmoteItem(CatalogItem.CatalogItem):
    sequenceNumber = 0
    
    def makeNewItem(self, emoteIndex):
        self.emoteIndex = emoteIndex
        CatalogItem.CatalogItem.makeNewItem(self)

    
    def getPurchaseLimit(self):
        return 1

    
    def reachedPurchaseLimit(self, avatar):
        return avatar.emoteAccess[self.emoteIndex] != 0

    
    def saveHistory(self):
        return 1

    
    def getTypeName(self):
        return Localizer.EmoteTypeName

    
    def getName(self):
        return Localizer.EmoteList[self.emoteIndex]

    
    def recordPurchase(self, avatar, optional):
        if self.emoteIndex < 0 or self.emoteIndex > len(avatar.emoteAccess):
            self.notify.warning('Invalid emote access: %s for avatar %s' % (self.emoteIndex, avatar.doId))
            return ToontownGlobals.P_InvalidIndex
        
        avatar.emoteAccess[self.emoteIndex] = 1
        avatar.d_setEmoteAccess(avatar.emoteAccess)
        return ToontownGlobals.P_ItemAvailable

    
    def getPicture(self, avatar):
        import Toon
        import ToonHead
        import Emote
        if self.emoteIndex in Emote.HeadEmotes:
            toon = ToonHead.ToonHead()
            toon.setupHead(avatar.style, forGui = 1)
        else:
            toon = Toon.Toon()
            toon.setDNA(avatar.style)
            toon.loop('neutral')
        toon.setH(180)
        (model, ival) = self.makeFrameModel(toon, 0)
        (track, duration) = Emote.DoEmote(toon, self.emoteIndex)
        if duration == None:
            duration = 0
        
        name = 'emote-item-%s' % self.sequenceNumber
        CatalogEmoteItem.sequenceNumber += 1
        if track != None:
            track = Sequence(Sequence(track, duration = 0), Wait(duration + 2), name = name)
        else:
            track = Sequence(Func(Emote.DoEmote, toon, self.emoteIndex), Wait(duration + 4), name = name)
        return (model, track)

    
    def output(self, store = -1):
        return 'CatalogEmoteItem(%s%s)' % (self.emoteIndex, self.formatOptionalData(store))

    
    def compareTo(self, other):
        return self.emoteIndex - other.emoteIndex

    
    def getBasePrice(self):
        return 550

    
    def decodeDatagram(self, di, versionNumber, store):
        CatalogItem.CatalogItem.decodeDatagram(self, di, versionNumber, store)
        self.emoteIndex = di.getUint8()

    
    def encodeDatagram(self, dg, store):
        CatalogItem.CatalogItem.encodeDatagram(self, dg, store)
        dg.addUint8(self.emoteIndex)


