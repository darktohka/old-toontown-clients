# File: C (Python 2.2)

import CatalogItem
import ToontownGlobals
import Localizer
import AvatarDNA
import random
import PythonUtil
from PandaModules import *
CTArticle = 0
CTString = 1
CTBasePrice = 2
ABoysShirt = 0
AGirlsShirt = 1
ABoysShorts = 2
AGirlsShorts = 3
AGirlsSkirt = 4
ClothingTypes = {
    101: (ABoysShirt, 'bss1', 40),
    102: (ABoysShirt, 'bss2', 40),
    103: (ABoysShirt, 'bss3', 40),
    105: (ABoysShirt, 'bss4', 40),
    104: (ABoysShirt, 'bss5', 40),
    106: (ABoysShirt, 'bss6', 40),
    107: (ABoysShirt, 'bss7', 40),
    108: (ABoysShirt, 'bss8', 40),
    109: (ABoysShirt, 'bss9', 40),
    111: (ABoysShirt, 'bss11', 40),
    115: (ABoysShirt, 'bss15', 40),
    116: (ABoysShirt, 'bss16', 80),
    117: (ABoysShirt, 'bss17', 80),
    118: (ABoysShirt, 'bss18', 80),
    119: (ABoysShirt, 'bss19', 80),
    201: (AGirlsShirt, 'gss1', 40),
    202: (AGirlsShirt, 'gss2', 40),
    203: (AGirlsShirt, 'gss3', 40),
    205: (AGirlsShirt, 'gss4', 40),
    204: (AGirlsShirt, 'gss5', 40),
    206: (AGirlsShirt, 'gss6', 40),
    207: (AGirlsShirt, 'gss7', 40),
    208: (AGirlsShirt, 'gss8', 40),
    209: (AGirlsShirt, 'gss9', 40),
    211: (AGirlsShirt, 'gss11', 40),
    215: (AGirlsShirt, 'gss15', 40),
    216: (AGirlsShirt, 'gss16', 80),
    217: (AGirlsShirt, 'gss17', 80),
    218: (AGirlsShirt, 'gss18', 80),
    219: (AGirlsShirt, 'gss19', 80),
    301: (ABoysShorts, 'bbs1', 50),
    302: (ABoysShorts, 'bbs2', 50),
    303: (ABoysShorts, 'bbs3', 50),
    304: (ABoysShorts, 'bbs4', 50),
    305: (ABoysShorts, 'bbs5', 50),
    308: (ABoysShorts, 'bbs8', 50),
    401: (AGirlsSkirt, 'gsk1', 50),
    403: (AGirlsSkirt, 'gsk3', 50),
    404: (AGirlsSkirt, 'gsk4', 50),
    405: (AGirlsSkirt, 'gsk5', 50),
    407: (AGirlsSkirt, 'gsk7', 50),
    408: (AGirlsSkirt, 'gsk8', 100),
    409: (AGirlsSkirt, 'gsk9', 100),
    410: (AGirlsSkirt, 'gsk10', 100),
    451: (AGirlsShorts, 'gsh1', 50),
    452: (AGirlsShorts, 'gsh2', 50),
    453: (AGirlsShorts, 'gsh3', 50) }

class CatalogClothingItem(CatalogItem.CatalogItem):
    
    def makeNewItem(self, clothingType, colorIndex):
        self.clothingType = clothingType
        self.colorIndex = colorIndex
        CatalogItem.CatalogItem.makeNewItem(self)

    
    def storedInCloset(self):
        return 1

    
    def notOffered(self, avatar):
        article = ClothingTypes[self.clothingType][CTArticle]
        if not article == ABoysShirt:
            pass
        forBoys = article == ABoysShorts
        if avatar.getStyle().getGender() == 'm':
            return not forBoys
        else:
            return forBoys

    
    def getPurchaseLimit(self):
        return 1

    
    def reachedPurchaseLimit(self, avatar):
        if avatar.onOrder.count(self) != 0:
            return 1
        
        if avatar.mailboxContents.count(self) != 0:
            return 1
        
        str = ClothingTypes[self.clothingType][CTString]
        dna = avatar.getStyle()
        if self.isShirt():
            defn = AvatarDNA.ShirtStyles[str]
            if dna.topTex == defn[0] and dna.topTexColor == defn[2][self.colorIndex][0] and dna.sleeveTex == defn[1] and dna.sleeveTexColor == defn[2][self.colorIndex][1]:
                return 1
            
            l = avatar.clothesTopsList
            for i in range(0, len(l), 4):
                if l[i] == defn[0] and l[i + 1] == defn[2][self.colorIndex][0] and l[i + 2] == defn[1] and l[i + 3] == defn[2][self.colorIndex][1]:
                    return 1
                
            
        else:
            defn = AvatarDNA.BottomStyles[str]
            if dna.botTex == defn[0] and dna.botTexColor == defn[1][self.colorIndex]:
                return 1
            
            l = avatar.clothesBottomsList
            for i in range(0, len(l), 2):
                if l[i] == defn[0] and l[i + 1] == defn[1][self.colorIndex]:
                    return 1
                
            
        return 0

    
    def getTypeName(self):
        return Localizer.ClothingTypeName

    
    def getName(self):
        article = ClothingTypes[self.clothingType][CTArticle]
        return Localizer.ClothingArticleNames[article]

    
    def recordPurchase(self, avatar, optional):
        if avatar.isClosetFull():
            return ToontownGlobals.P_NoRoomForItem
        
        str = ClothingTypes[self.clothingType][CTString]
        dna = avatar.getStyle()
        if self.isShirt():
            added = avatar.addToClothesTopsList(dna.topTex, dna.topTexColor, dna.sleeveTex, dna.sleeveTexColor)
            if added:
                avatar.b_setClothesTopsList(avatar.getClothesTopsList())
            else:
                self.notify.warning('Avatar %s %s lost current shirt; closet full.' % (avatar.doId, dna.asTuple()))
            defn = AvatarDNA.ShirtStyles[str]
            dna.topTex = defn[0]
            dna.topTexColor = defn[2][self.colorIndex][0]
            dna.sleeveTex = defn[1]
            dna.sleeveTexColor = defn[2][self.colorIndex][1]
        else:
            added = avatar.addToClothesBottomsList(dna.botTex, dna.botTexColor)
            if added:
                avatar.b_setClothesBottomsList(avatar.getClothesBottomsList())
            else:
                self.notify.warning('Avatar %s %s lost current bottoms; closet full.' % (avatar.doId, dna.asTuple()))
            defn = AvatarDNA.BottomStyles[str]
            dna.botTex = defn[0]
            dna.botTexColor = defn[1][self.colorIndex]
        avatar.b_setDNAString(dna.makeNetString())
        return ToontownGlobals.P_ItemAvailable

    
    def getDeliveryTime(self):
        return 60

    
    def getPicture(self, avatar):
        import Toon
        dna = AvatarDNA.AvatarDNA(type = 't', dna = avatar.style)
        str = ClothingTypes[self.clothingType][CTString]
        if self.isShirt():
            defn = AvatarDNA.ShirtStyles[str]
            dna.topTex = defn[0]
            dna.topTexColor = defn[2][self.colorIndex][0]
            dna.sleeveTex = defn[1]
            dna.sleeveTexColor = defn[2][self.colorIndex][1]
            pieceNames = ('**/1000/**/torso-top', '**/1000/**/sleeves')
        else:
            defn = AvatarDNA.BottomStyles[str]
            dna.botTex = defn[0]
            dna.botTexColor = defn[1][self.colorIndex]
            pieceNames = ('**/1000/**/torso-bot',)
        toon = Toon.Toon()
        toon.setDNA(dna)
        model = NodePath('clothing')
        for name in pieceNames:
            for piece in toon.findAllMatches(name).asList():
                piece.wrtReparentTo(model)
            
        
        model.setH(180)
        return self.makeFrameModel(model)

    
    def requestPurchase(self, phone, callback):
        import ToontownDialog
        avatar = toonbase.localToon
        clothesOnOrder = 0
        for item in avatar.onOrder + avatar.mailboxContents:
            if item.storedInCloset():
                clothesOnOrder += 1
            
        
        if avatar.isClosetFull(clothesOnOrder):
            self.requestPurchaseCleanup()
            buttonCallback = PythonUtil.Functor(self._CatalogClothingItem__handleFullPurchaseDialog, phone, callback)
            self.dialog = ToontownDialog.ToontownDialog(style = ToontownDialog.YesNo, text = Localizer.CatalogPurchaseClosetFull, text_wordwrap = 15, command = buttonCallback)
            self.dialog.show()
        else:
            CatalogItem.CatalogItem.requestPurchase(self, phone, callback)

    
    def requestPurchaseCleanup(self):
        if hasattr(self, 'dialog'):
            self.dialog.cleanup()
            del self.dialog
        

    
    def _CatalogClothingItem__handleFullPurchaseDialog(self, phone, callback, buttonValue):
        import ToontownDialog
        self.requestPurchaseCleanup()
        if buttonValue == ToontownDialog.DIALOG_OK:
            CatalogItem.CatalogItem.requestPurchase(self, phone, callback)
        else:
            callback(ToontownGlobals.P_UserCancelled, self)

    
    def getAcceptItemErrorText(self, retcode):
        if retcode == ToontownGlobals.P_ItemAvailable:
            if self.isShirt():
                return Localizer.CatalogAcceptShirt
            elif self.isSkirt():
                return Localizer.CatalogAcceptSkirt
            else:
                return Localizer.CatalogAcceptShorts
        elif retcode == ToontownGlobals.P_NoRoomForItem:
            return Localizer.CatalogAcceptClosetFull
        
        return CatalogItem.CatalogItem.getAcceptItemErrorText(self, retcode)

    
    def getColorChoices(self):
        str = ClothingTypes[self.clothingType][CTString]
        if self.isShirt():
            return AvatarDNA.ShirtStyles[str][2]
        else:
            return AvatarDNA.BottomStyles[str][1]

    
    def isShirt(self):
        article = ClothingTypes[self.clothingType][CTArticle]
        return article < ABoysShorts

    
    def isSkirt(self):
        article = ClothingTypes[self.clothingType][CTArticle]
        return article == AGirlsSkirt

    
    def output(self, store = -1):
        return 'CatalogClothingItem(%s, %s%s)' % (self.clothingType, self.colorIndex, self.formatOptionalData(store))

    
    def compareTo(self, other):
        if self.clothingType != other.clothingType:
            return self.clothingType - other.clothingType
        
        return self.colorIndex - other.colorIndex

    
    def getBasePrice(self):
        return ClothingTypes[self.clothingType][CTBasePrice]

    
    def decodeDatagram(self, di, versionNumber, store):
        CatalogItem.CatalogItem.decodeDatagram(self, di, versionNumber, store)
        self.clothingType = di.getUint16()
        self.colorIndex = di.getUint8()

    
    def encodeDatagram(self, dg, store):
        CatalogItem.CatalogItem.encodeDatagram(self, dg, store)
        dg.addUint16(self.clothingType)
        dg.addUint8(self.colorIndex)



def getAllClothes(*clothingTypes):
    list = []
    for clothingType in clothingTypes:
        base = CatalogClothingItem(clothingType, 0)
        list.append(base)
        for n in range(1, len(base.getColorChoices())):
            list.append(CatalogClothingItem(clothingType, n))
        
    
    return list

