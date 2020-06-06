# File: C (Python 2.2)

from pandac.PandaModules import *
import CatalogItem
from toontown.toonbase import ToontownGlobals
from otp.otpbase import OTPLocalizer
from toontown.toonbase import TTLocalizer

class CatalogChatItem(CatalogItem.CatalogItem):
    
    def makeNewItem(self, customIndex):
        self.customIndex = customIndex
        CatalogItem.CatalogItem.makeNewItem(self)

    
    def getPurchaseLimit(self):
        return 1

    
    def reachedPurchaseLimit(self, avatar):
        return avatar.customMessages.count(self.customIndex) != 0

    
    def getTypeName(self):
        return TTLocalizer.ChatTypeName

    
    def getName(self):
        return TTLocalizer.ChatItemQuotes % OTPLocalizer.CustomSCStrings[self.customIndex]

    
    def getDisplayName(self):
        return OTPLocalizer.CustomSCStrings[self.customIndex]

    
    def recordPurchase(self, avatar, optional):
        if avatar.customMessages.count(self.customIndex) != 0:
            return ToontownGlobals.P_ReachedPurchaseLimit
        
        if len(avatar.customMessages) >= ToontownGlobals.MaxCustomMessages:
            if optional >= 0 and optional < len(avatar.customMessages):
                del avatar.customMessages[optional]
            
            if len(avatar.customMessages) >= ToontownGlobals.MaxCustomMessages:
                return ToontownGlobals.P_NoRoomForItem
            
        
        avatar.customMessages.append(self.customIndex)
        avatar.d_setCustomMessages(avatar.customMessages)
        return ToontownGlobals.P_ItemAvailable

    
    def output(self, store = -1):
        return 'CatalogChatItem(%s%s)' % (self.customIndex, self.formatOptionalData(store))

    
    def compareTo(self, other):
        return self.customIndex - other.customIndex

    
    def getHashContents(self):
        return self.customIndex

    
    def getBasePrice(self):
        if self.customIndex >= 10000:
            return 150
        
        return 100

    
    def decodeDatagram(self, di, versionNumber, store):
        CatalogItem.CatalogItem.decodeDatagram(self, di, versionNumber, store)
        self.customIndex = di.getUint16()
        text = OTPLocalizer.CustomSCStrings[self.customIndex]

    
    def encodeDatagram(self, dg, store):
        CatalogItem.CatalogItem.encodeDatagram(self, dg, store)
        dg.addUint16(self.customIndex)

    
    def requestPurchase(self, phone, callback):
        if len(base.localAvatar.customMessages) < ToontownGlobals.MaxCustomMessages:
            CatalogItem.CatalogItem.requestPurchase(self, phone, callback)
        else:
            self.showMessagePicker(phone, callback)

    
    def showMessagePicker(self, phone, callback):
        self.phone = phone
        self.callback = callback
        import CatalogChatItemPicker
        self.messagePicker = CatalogChatItemPicker.CatalogChatItemPicker(self._CatalogChatItem__handlePickerDone, self.customIndex)
        self.messagePicker.show()

    
    def _CatalogChatItem__handlePickerDone(self, status, pickedMessage = None):
        if status == 'pick':
            CatalogItem.CatalogItem.requestPurchase(self, self.phone, self.callback, pickedMessage)
        
        self.messagePicker.hide()
        self.messagePicker.destroy()
        del self.messagePicker
        del self.callback
        del self.phone

    
    def getPicture(self, avatar):
        chatBalloon = loader.loadModelCopy('phase_3/models/props/chatbox.bam')
        chatBalloon.find('**/top').setPos(1, 0, 5)
        chatBalloon.find('**/middle').setScale(1, 1, 3)
        frame = self.makeFrame()
        chatBalloon.reparentTo(frame)
        chatBalloon.setPos(-1.9199999999999999, 0, -1.53)
        chatBalloon.setScale(0.34999999999999998)
        return (frame, None)



def getChatRange(fromIndex, toIndex, *otherRanges):
    list = []
    froms = [
        fromIndex]
    tos = [
        toIndex]
    i = 0
    while i < len(otherRanges):
        froms.append(otherRanges[i])
        tos.append(otherRanges[i + 1])
        i += 2
    for chatId in OTPLocalizer.CustomSCStrings.keys():
        for (fromIndex, toIndex) in zip(froms, tos):
            if chatId >= fromIndex and chatId <= toIndex:
                list.append(CatalogChatItem(chatId))
            
        
    
    return list

