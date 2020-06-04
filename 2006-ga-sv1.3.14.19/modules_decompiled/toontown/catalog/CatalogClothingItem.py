# File: C (Python 2.2)

import CatalogItem
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.toon import ToonDNA
import random
from direct.showbase import PythonUtil
from pandac.PandaModules import *
CTArticle = 0
CTString = 1
CTBasePrice = 2
ABoysShirt = 0
AGirlsShirt = 1
AShirt = 2
ABoysShorts = 3
AGirlsShorts = 4
AGirlsSkirt = 5
AShorts = 6
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
    116: (ABoysShirt, 'c_ss1', 80),
    117: (ABoysShirt, 'c_ss2', 80),
    118: (ABoysShirt, 'c_bss1', 80),
    119: (ABoysShirt, 'c_bss2', 80),
    120: (ABoysShirt, 'c_ss3', 80),
    121: (ABoysShirt, 'c_bss3', 80),
    122: (ABoysShirt, 'c_bss4', 80),
    123: (ABoysShirt, 'c_ss4', 120),
    124: (ABoysShirt, 'c_ss5', 120),
    125: (AShirt, 'c_ss6', 120),
    126: (AShirt, 'c_ss7', 120),
    127: (AShirt, 'c_ss8', 120),
    128: (AShirt, 'c_ss9', 120),
    129: (AShirt, 'c_ss10', 120),
    130: (AShirt, 'c_ss11', 120),
    131: (ABoysShirt, 'c_ss12', 160),
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
    216: (AGirlsShirt, 'c_ss1', 80),
    217: (AGirlsShirt, 'c_ss2', 80),
    218: (AGirlsShirt, 'c_gss1', 80),
    219: (AGirlsShirt, 'c_gss2', 80),
    220: (AGirlsShirt, 'c_ss3', 80),
    221: (AGirlsShirt, 'c_gss3', 80),
    222: (AGirlsShirt, 'c_gss4', 80),
    223: (AGirlsShirt, 'c_gss5', 80),
    224: (AGirlsShirt, 'c_ss4', 120),
    225: (AGirlsShirt, 'c_ss13', 160),
    301: (ABoysShorts, 'bbs1', 50),
    302: (ABoysShorts, 'bbs2', 50),
    303: (ABoysShorts, 'bbs3', 50),
    304: (ABoysShorts, 'bbs4', 50),
    305: (ABoysShorts, 'bbs5', 50),
    308: (ABoysShorts, 'bbs8', 50),
    310: (ABoysShorts, 'c_bs1', 120),
    311: (ABoysShorts, 'c_bs2', 120),
    312: (ABoysShorts, 'c_bs3', 120),
    313: (ABoysShorts, 'c_bs4', 120),
    314: (ABoysShorts, 'c_bs5', 160),
    401: (AGirlsSkirt, 'gsk1', 50),
    403: (AGirlsSkirt, 'gsk3', 50),
    404: (AGirlsSkirt, 'gsk4', 50),
    405: (AGirlsSkirt, 'gsk5', 50),
    407: (AGirlsSkirt, 'gsk7', 50),
    408: (AGirlsSkirt, 'c_gsk1', 100),
    409: (AGirlsSkirt, 'c_gsk2', 100),
    410: (AGirlsSkirt, 'c_gsk3', 100),
    411: (AGirlsSkirt, 'c_gsk4', 120),
    412: (AGirlsSkirt, 'c_gsk5', 120),
    413: (AGirlsSkirt, 'c_gsk6', 120),
    414: (AGirlsSkirt, 'c_gsk7', 160),
    451: (AGirlsShorts, 'gsh1', 50),
    452: (AGirlsShorts, 'gsh2', 50),
    453: (AGirlsShorts, 'gsh3', 50),
    1001: (AShirt, 'hw_ss1', 200),
    1002: (AShirt, 'hw_ss2', 200),
    1100: (AShirt, 'wh_ss1', 200),
    1101: (AShirt, 'wh_ss2', 200),
    1102: (AShirt, 'wh_ss3', 200),
    1103: (AShirt, 'wh_ss4', 200),
    1200: (AGirlsShirt, 'vd_ss1', 200),
    1201: (AShirt, 'vd_ss2', 200),
    1202: (ABoysShirt, 'vd_ss3', 200),
    1203: (AGirlsShirt, 'vd_ss4', 200),
    1204: (AGirlsSkirt, 'vd_gs1', 200),
    1205: (ABoysShorts, 'vd_bs1', 200),
    1300: (AShirt, 'sd_ss1', 200),
    1301: (AShirt, 'sd_ss2', 225),
    1302: (AGirlsShorts, 'sd_gs1', 200),
    1303: (ABoysShorts, 'sd_bs1', 200),
    1400: (AShirt, 'tc_ss1', 200),
    1401: (AShirt, 'tc_ss2', 200),
    1402: (AShirt, 'tc_ss3', 200),
    1500: (AShirt, 'j4_ss1', 200),
    1501: (AShirt, 'j4_ss2', 200),
    1502: (ABoysShorts, 'j4_bs1', 200),
    1503: (AGirlsSkirt, 'j4_gs1', 200) }

class CatalogClothingItem(CatalogItem.CatalogItem):
    
    def makeNewItem(self, clothingType, colorIndex):
        self.clothingType = clothingType
        self.colorIndex = colorIndex
        CatalogItem.CatalogItem.makeNewItem(self)

    
    def storedInCloset(self):
        return 1

    
    def notOfferedTo(self, avatar):
        article = ClothingTypes[self.clothingType][CTArticle]
        if article == AShirt or article == AShorts:
            return 0
        
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
            defn = ToonDNA.ShirtStyles[str]
            if dna.topTex == defn[0] and dna.topTexColor == defn[2][self.colorIndex][0] and dna.sleeveTex == defn[1] and dna.sleeveTexColor == defn[2][self.colorIndex][1]:
                return 1
            
            l = avatar.clothesTopsList
            for i in range(0, len(l), 4):
                if l[i] == defn[0] and l[i + 1] == defn[2][self.colorIndex][0] and l[i + 2] == defn[1] and l[i + 3] == defn[2][self.colorIndex][1]:
                    return 1
                
            
        else:
            defn = ToonDNA.BottomStyles[str]
            if dna.botTex == defn[0] and dna.botTexColor == defn[1][self.colorIndex]:
                return 1
            
            l = avatar.clothesBottomsList
            for i in range(0, len(l), 2):
                if l[i] == defn[0] and l[i + 1] == defn[1][self.colorIndex]:
                    return 1
                
            
        return 0

    
    def getTypeName(self):
        return TTLocalizer.ClothingTypeName

    
    def getName(self):
        typeName = TTLocalizer.ClothingTypeNames.get(self.clothingType, 0)
        if typeName:
            return typeName
        else:
            article = ClothingTypes[self.clothingType][CTArticle]
            return TTLocalizer.ClothingArticleNames[article]

    
    def recordPurchase(self, avatar, optional):
        if avatar.isClosetFull():
            return ToontownGlobals.P_NoRoomForItem
        
        str = ClothingTypes[self.clothingType][CTString]
        dna = avatar.getStyle()
        if self.isShirt():
            added = avatar.addToClothesTopsList(dna.topTex, dna.topTexColor, dna.sleeveTex, dna.sleeveTexColor)
            if added:
                avatar.b_setClothesTopsList(avatar.getClothesTopsList())
                self.notify.info('Avatar %s put shirt %d,%d,%d,%d in closet.' % (avatar.doId, dna.topTex, dna.topTexColor, dna.sleeveTex, dna.sleeveTexColor))
            else:
                self.notify.warning('Avatar %s %s lost current shirt; closet full.' % (avatar.doId, dna.asTuple()))
            defn = ToonDNA.ShirtStyles[str]
            dna.topTex = defn[0]
            dna.topTexColor = defn[2][self.colorIndex][0]
            dna.sleeveTex = defn[1]
            dna.sleeveTexColor = defn[2][self.colorIndex][1]
        else:
            added = avatar.addToClothesBottomsList(dna.botTex, dna.botTexColor)
            if added:
                avatar.b_setClothesBottomsList(avatar.getClothesBottomsList())
                self.notify.info('Avatar %s put bottoms %d,%d in closet.' % (avatar.doId, dna.botTex, dna.botTexColor))
            else:
                self.notify.warning('Avatar %s %s lost current bottoms; closet full.' % (avatar.doId, dna.asTuple()))
            defn = ToonDNA.BottomStyles[str]
            dna.botTex = defn[0]
            dna.botTexColor = defn[1][self.colorIndex]
        avatar.b_setDNAString(dna.makeNetString())
        avatar.d_catalogGenClothes()
        return ToontownGlobals.P_ItemAvailable

    
    def getDeliveryTime(self):
        return 60

    
    def getPicture(self, avatar):
        Toon = Toon
        import toontown.toon
        dna = ToonDNA.ToonDNA(type = 't', dna = avatar.style)
        str = ClothingTypes[self.clothingType][CTString]
        if self.isShirt():
            defn = ToonDNA.ShirtStyles[str]
            dna.topTex = defn[0]
            dna.topTexColor = defn[2][self.colorIndex][0]
            dna.sleeveTex = defn[1]
            dna.sleeveTexColor = defn[2][self.colorIndex][1]
            pieceNames = ('**/1000/**/torso-top', '**/1000/**/sleeves')
        else:
            defn = ToonDNA.BottomStyles[str]
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
        TTDialog = TTDialog
        import toontown.toontowngui
        avatar = base.localAvatar
        clothesOnOrder = 0
        for item in avatar.onOrder + avatar.mailboxContents:
            if item.storedInCloset():
                clothesOnOrder += 1
            
        
        if avatar.isClosetFull(clothesOnOrder):
            self.requestPurchaseCleanup()
            buttonCallback = PythonUtil.Functor(self._CatalogClothingItem__handleFullPurchaseDialog, phone, callback)
            self.dialog = TTDialog.TTDialog(style = TTDialog.YesNo, text = TTLocalizer.CatalogPurchaseClosetFull, text_wordwrap = 15, command = buttonCallback)
            self.dialog.show()
        else:
            CatalogItem.CatalogItem.requestPurchase(self, phone, callback)

    
    def requestPurchaseCleanup(self):
        if hasattr(self, 'dialog'):
            self.dialog.cleanup()
            del self.dialog
        

    
    def _CatalogClothingItem__handleFullPurchaseDialog(self, phone, callback, buttonValue):
        TTDialog = TTDialog
        import toontown.toontowngui
        self.requestPurchaseCleanup()
        if buttonValue == TTDialog.DIALOG_OK:
            CatalogItem.CatalogItem.requestPurchase(self, phone, callback)
        else:
            callback(ToontownGlobals.P_UserCancelled, self)

    
    def getAcceptItemErrorText(self, retcode):
        if retcode == ToontownGlobals.P_ItemAvailable:
            if self.isShirt():
                return TTLocalizer.CatalogAcceptShirt
            elif self.isSkirt():
                return TTLocalizer.CatalogAcceptSkirt
            else:
                return TTLocalizer.CatalogAcceptShorts
        elif retcode == ToontownGlobals.P_NoRoomForItem:
            return TTLocalizer.CatalogAcceptClosetFull
        
        return CatalogItem.CatalogItem.getAcceptItemErrorText(self, retcode)

    
    def getColorChoices(self):
        str = ClothingTypes[self.clothingType][CTString]
        if self.isShirt():
            return ToonDNA.ShirtStyles[str][2]
        else:
            return ToonDNA.BottomStyles[str][1]

    
    def isShirt(self):
        article = ClothingTypes[self.clothingType][CTArticle]
        return article < ABoysShorts

    
    def isSkirt(self):
        article = ClothingTypes[self.clothingType][CTArticle]
        return article == AGirlsSkirt

    
    def output(self, store = -1):
        return 'CatalogClothingItem(%s, %s%s)' % (self.clothingType, self.colorIndex, self.formatOptionalData(store))

    
    def getFilename(self):
        str = ClothingTypes[self.clothingType][CTString]
        if self.isShirt():
            defn = ToonDNA.ShirtStyles[str]
            topTex = defn[0]
            return ToonDNA.Shirts[topTex]
        else:
            defn = ToonDNA.BottomStyles[str]
            botTex = defn[0]
            article = ClothingTypes[self.clothingType][CTArticle]
            if article == ABoysShorts:
                return ToonDNA.BoyShorts[botTex]
            else:
                return ToonDNA.GirlBottoms[botTex][0]

    
    def getColor(self):
        str = ClothingTypes[self.clothingType][CTString]
        if self.isShirt():
            defn = ToonDNA.ShirtStyles[str]
            topTexColor = defn[2][self.colorIndex][0]
            return ToonDNA.ClothesColors[topTexColor]
        else:
            defn = ToonDNA.BottomStyles[str]
            botTexColor = defn[1][self.colorIndex]
            return ToonDNA.ClothesColors[botTexColor]

    
    def compareTo(self, other):
        if self.clothingType != other.clothingType:
            return self.clothingType - other.clothingType
        
        return self.colorIndex - other.colorIndex

    
    def getHashContents(self):
        return (self.clothingType, self.colorIndex)

    
    def getBasePrice(self):
        return ClothingTypes[self.clothingType][CTBasePrice]

    
    def decodeDatagram(self, di, versionNumber, store):
        CatalogItem.CatalogItem.decodeDatagram(self, di, versionNumber, store)
        self.clothingType = di.getUint16()
        self.colorIndex = di.getUint8()
        str = ClothingTypes[self.clothingType][CTString]
        if self.isShirt():
            color = ToonDNA.ShirtStyles[str][2][self.colorIndex]
        else:
            color = ToonDNA.BottomStyles[str][1][self.colorIndex]

    
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

