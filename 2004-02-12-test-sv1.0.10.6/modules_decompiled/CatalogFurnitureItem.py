# File: C (Python 2.2)

import CatalogAtticItem
import Localizer
FTModelName = 0
FTColor = 1
FTColorOptions = 2
FTBasePrice = 3
FTFlags = 4
FTScale = 5
FLBank = 1
FLCloset = 2
FLRug = 4
FLPainting = 8
FLOnTable = 16
FLIsTable = 32
FLPhone = 64
BankToMoney = {
    1300: 1000,
    1310: 2500,
    1320: 5000 }
MoneyToBank = { }
for (bankId, maxMoney) in BankToMoney.items():
    MoneyToBank[maxMoney] = bankId

MaxBankId = 1320
FurnitureTypes = {
    100: ('phase_5.5/models/estate/chairA', None, None, 80),
    110: ('phase_3.5/models/modules/chair', None, None, 40),
    120: ('phase_5.5/models/estate/deskChair', None, None, 60),
    130: ('phase_5.5/models/estate/BugRoomChair', None, None, 160),
    140: ('phase_5.5/models/estate/UWlobsterChair', None, None, 200),
    145: ('phase_5.5/models/estate/UWlifeSaverChair', None, None, 200),
    200: ('phase_5.5/models/estate/regular_bed', None, None, 400),
    210: ('phase_5.5/models/estate/girly_bed', None, None, 450),
    220: ('phase_5.5/models/estate/bathtub_bed', None, None, 550),
    230: ('phase_5.5/models/estate/bugRoomBed', None, None, 600),
    240: ('phase_5.5/models/estate/UWBoatBed', None, None, 600),
    300: ('phase_5.5/models/estate/Piano', None, None, 1000, FLIsTable),
    310: ('phase_5.5/models/estate/Organ', None, None, 2500),
    400: ('phase_5.5/models/estate/FireplaceSq', None, None, 800),
    410: ('phase_5.5/models/estate/FireplaceGirlee', None, None, 800),
    420: ('phase_5.5/models/estate/FireplaceRound', None, None, 800),
    430: ('phase_5.5/models/estate/bugRoomFireplace', None, None, 800),
    500: ('phase_5.5/models/estate/closetBoy', None, None, 500, FLCloset, 0.84999999999999998),
    502: ('phase_5.5/models/estate/closetBoy', None, None, 500, FLCloset, 1.0),
    510: ('phase_5.5/models/estate/closetGirl', None, None, 500, FLCloset, 0.84999999999999998),
    512: ('phase_5.5/models/estate/closetGirl', None, None, 500, FLCloset, 1.0),
    600: ('phase_3.5/models/modules/lamp_short', None, None, 45, FLOnTable),
    610: ('phase_3.5/models/modules/lamp_tall', None, None, 45),
    620: ('phase_5.5/models/estate/lampA', None, None, 35, FLOnTable),
    630: ('phase_5.5/models/estate/bugRoomDaisyLamp1', None, None, 55),
    640: ('phase_5.5/models/estate/bugRoomDaisyLamp2', None, None, 55),
    650: ('phase_5.5/models/estate/UWlamp_jellyfish', None, None, 55, FLOnTable),
    660: ('phase_5.5/models/estate/UWlamps_jellyfishB', None, None, 55, FLOnTable),
    700: ('phase_3.5/models/modules/couch_1person', None, None, 230),
    710: ('phase_3.5/models/modules/couch_2person', None, None, 230),
    800: ('phase_3.5/models/modules/desk_only_wo_phone', None, None, 65, FLIsTable),
    810: ('phase_5.5/models/estate/BugRoomDesk', None, None, 125, FLIsTable),
    900: ('phase_3.5/models/modules/umbrella_stand', None, None, 30),
    910: ('phase_3.5/models/modules/coatrack', None, None, 75),
    920: ('phase_3.5/models/modules/paper_trashcan', None, None, 30),
    930: ('phase_5.5/models/estate/BugRoomRedMushroomPot', None, None, 60),
    940: ('phase_5.5/models/estate/BugRoomYellowMushroomPot', None, None, 60),
    950: ('phase_5.5/models/estate/UWcoralClothRack', None, None, 75),
    1000: ('phase_3.5/models/modules/rug', None, None, 75, FLRug),
    1010: ('phase_5.5/models/estate/rugA', None, None, 75, FLRug),
    1020: ('phase_5.5/models/estate/rugB', None, None, 75, FLRug, 2.5),
    1030: ('phase_5.5/models/estate/bugRoomLeafMat', None, None, 75, FLRug),
    1100: ('phase_5.5/models/estate/cabinetRwood', None, None, 825),
    1110: ('phase_5.5/models/estate/cabinetYwood', None, None, 825),
    1120: ('phase_3.5/models/modules/bookcase', None, None, 650, FLIsTable),
    1130: ('phase_3.5/models/modules/bookcase_low', None, None, 650, FLIsTable),
    1200: ('phase_3.5/models/modules/ending_table', None, None, 60, FLIsTable),
    1210: ('phase_5.5/models/estate/table_radio', None, None, 60, FLIsTable, 50.0),
    1220: ('phase_5.5/models/estate/coffeetableSq', None, None, 180, FLIsTable),
    1230: ('phase_5.5/models/estate/coffeetableSq_BW', None, None, 180, FLIsTable),
    1240: ('phase_5.5/models/estate/UWtable', None, None, 180, FLIsTable),
    1300: ('phase_5.5/models/estate/jellybeanBank', None, None, 0, FLBank, 0.75),
    1310: ('phase_5.5/models/estate/jellybeanBank', None, None, 400, FLBank, 1.0),
    1320: ('phase_5.5/models/estate/jellybeanBank', None, None, 800, FLBank, 1.2),
    1399: ('phase_5.5/models/estate/prop_phone-mod', None, None, 0, FLPhone),
    1400: ('phase_5.5/models/estate/cezanne_toon', None, None, 425, FLPainting, 2.0),
    1410: ('phase_5.5/models/estate/flowers', None, None, 425, FLPainting, 2.0),
    1420: ('phase_5.5/models/estate/modernistMickey', None, None, 425, FLPainting, 2.0),
    1430: ('phase_5.5/models/estate/rembrandt_toon', None, None, 425, FLPainting, 2.0),
    1440: ('phase_5.5/models/estate/landscape', None, None, 425, FLPainting, 100.0),
    1441: ('phase_5.5/models/estate/whistler-horse', None, None, 425, FLPainting, 2.0),
    1442: ('phase_5.5/models/estate/degasHorseStar', None, None, 425, FLPainting, 2.5),
    1443: ('phase_5.5/models/estate/MagPie', None, None, 425, FLPainting, 2.0),
    1500: ('phase_5.5/models/estate/RADIO_A', None, None, 25, FLOnTable, 15.0),
    1510: ('phase_5.5/models/estate/RADIO_B', None, None, 25, FLOnTable, 15.0),
    1520: ('phase_5.5/models/estate/radio_c', None, None, 25, FLOnTable, 15.0),
    1530: ('phase_5.5/models/estate/bugRoomTV', None, None, 675),
    1600: ('phase_5.5/models/estate/vaseA_short', None, None, 120, FLOnTable),
    1610: ('phase_5.5/models/estate/vaseA_tall', None, None, 120, FLOnTable),
    1620: ('phase_5.5/models/estate/vaseB_short', None, None, 120, FLOnTable),
    1630: ('phase_5.5/models/estate/vaseB_tall', None, None, 120, FLOnTable),
    1640: ('phase_5.5/models/estate/vaseC_short', None, None, 120, FLOnTable),
    1650: ('phase_5.5/models/estate/vaseD_short', None, None, 120, FLOnTable),
    1660: ('phase_5.5/models/estate/UWcoralVase2', None, None, 120, FLOnTable),
    1661: ('phase_5.5/models/estate/UWshellVase7', None, None, 120, FLOnTable),
    1700: ('phase_5.5/models/estate/popcornCart', None, None, 400),
    1710: ('phase_5.5/models/estate/bugRoomLadyBug', None, None, 260),
    1720: ('phase_5.5/models/estate/UWfountain', None, None, 450),
    1725: ('phase_5.5/models/estate/UWOceanDryer', None, None, 400),
    1800: ('phase_5.5/models/estate/UWskullBowl', None, None, 120, FLOnTable),
    1810: ('phase_5.5/models/estate/UWlizardBowl', None, None, 120, FLOnTable),
    1900: ('phase_5.5/models/estate/UWswordFish', None, None, 425, FLPainting, 0.5),
    1910: ('phase_5.5/models/estate/UWhammerhead', None, None, 425, FLPainting),
    10000: ('phase_5.5/models/estate/pumpkin_short', None, None, 200, FLOnTable),
    10010: ('phase_5.5/models/estate/pumpkin_tall', None, None, 250, FLOnTable) }

class CatalogFurnitureItem(CatalogAtticItem.CatalogAtticItem):
    
    def makeNewItem(self, furnitureType, colorOption = None, posHpr = None):
        self.furnitureType = furnitureType
        self.colorOption = colorOption
        self.posHpr = posHpr
        CatalogAtticItem.CatalogAtticItem.makeNewItem(self)

    
    def needsCustomize(self):
        if self.colorOption == None:
            pass
        return FurnitureTypes[self.furnitureType][FTColorOptions] != None

    
    def saveHistory(self):
        return 1

    
    def replacesExisting(self):
        return self.getFlags() & (FLCloset | FLBank) != 0

    
    def hasExisting(self):
        return 1

    
    def getYourOldDesc(self):
        if self.getFlags() & FLCloset:
            return Localizer.FurnitureYourOldCloset
        elif self.getFlags() & FLBank:
            return Localizer.FurnitureYourOldBank
        else:
            return None

    
    def notOfferedTo(self, avatar):
        if self.getFlags() & FLCloset:
            decade = self.furnitureType - self.furnitureType % 10
            forBoys = decade == 500
            if avatar.getStyle().getGender() == 'm':
                return not forBoys
            else:
                return forBoys
        
        return 0

    
    def isDeletable(self):
        return self.getFlags() & (FLBank | FLCloset | FLPhone) == 0

    
    def getMaxBankMoney(self):
        return BankToMoney.get(self.furnitureType)

    
    def getMaxClothes(self):
        index = self.furnitureType % 10
        if index == 0:
            return 10
        elif index == 2:
            return 15
        else:
            return None

    
    def reachedPurchaseLimit(self, avatar):
        if self.getFlags() & FLBank:
            if self.getMaxBankMoney() <= avatar.getMaxBankMoney():
                return 1
            
            if self in avatar.onOrder or self in avatar.mailboxContents:
                return 1
            
        
        if self.getFlags() & FLCloset:
            if self.getMaxClothes() <= avatar.getMaxClothes():
                return 1
            
            if self in avatar.onOrder or self in avatar.mailboxContents:
                return 1
            
        
        return 0

    
    def getTypeName(self):
        flags = self.getFlags()
        if flags & FLPainting:
            return Localizer.PaintingTypeName
        else:
            return Localizer.FurnitureTypeName

    
    def getName(self):
        return Localizer.FurnitureNames[self.furnitureType]

    
    def getFlags(self):
        defn = FurnitureTypes[self.furnitureType]
        if FTFlags < len(defn):
            return defn[FTFlags]
        else:
            return 0

    
    def recordPurchase(self, avatar, optional):
        (house, retcode) = self.getHouseInfo(avatar)
        if retcode >= 0:
            house.addAtticItem(self)
            if self.getFlags() & FLBank:
                avatar.b_setMaxBankMoney(self.getMaxBankMoney())
            
            if self.getFlags() & FLCloset:
                avatar.b_setMaxClothes(self.getMaxClothes())
            
        
        return retcode

    
    def getDeliveryTime(self):
        return 24 * 60

    
    def getPicture(self, avatar):
        model = self.loadModel()
        spin = 1
        flags = self.getFlags()
        if flags & FLRug:
            spin = 0
            model.setP(90)
        elif flags & FLPainting:
            spin = 0
        
        model.setBin('unsorted', 0, 1)
        return self.makeFrameModel(model, spin)

    
    def output(self, store = -1):
        return 'CatalogFurnitureItem(%s%s)' % (self.furnitureType, self.formatOptionalData(store))

    
    def getFilename(self):
        type = FurnitureTypes[self.furnitureType]
        return type[FTModelName]

    
    def compareTo(self, other):
        return self.furnitureType - other.furnitureType

    
    def getHashContents(self):
        return self.furnitureType

    
    def getBasePrice(self):
        return FurnitureTypes[self.furnitureType][FTBasePrice]

    
    def loadModel(self):
        type = FurnitureTypes[self.furnitureType]
        model = loader.loadModelCopy(type[FTModelName])
        self.applyColor(model, type[FTColor])
        if type[FTColorOptions] != None:
            if self.colorOption == None:
                option = random.choice(type[FTColorOptions].values())
            else:
                option = type[FTColorOptions].get(self.colorOption)
            self.applyColor(model, option)
        
        if FTScale < len(type):
            model.setScale(type[FTScale])
            model.flattenLight()
        
        return model

    
    def decodeDatagram(self, di, versionNumber, store):
        CatalogAtticItem.CatalogAtticItem.decodeDatagram(self, di, versionNumber, store)
        self.furnitureType = di.getInt16()
        self.colorOption = None
        type = FurnitureTypes[self.furnitureType]
        if type[FTColorOptions]:
            if store & CatalogAtticItem.Customization:
                self.colorOption = di.getUint8()
                option = type[FTColorOptions][self.colorOption]
            
        

    
    def encodeDatagram(self, dg, store):
        CatalogAtticItem.CatalogAtticItem.encodeDatagram(self, dg, store)
        dg.addInt16(self.furnitureType)
        if FurnitureTypes[self.furnitureType][FTColorOptions]:
            if store & CatalogAtticItem.Customization:
                dg.addUint8(self.colorOption)
            
        



def nextAvailableBank(avatar, duplicateItems):
    bankId = MoneyToBank.get(avatar.getMaxBankMoney())
    if bankId == None or bankId == MaxBankId:
        return None
    
    bankId += 10
    item = CatalogFurnitureItem(bankId)
    while item in avatar.onOrder or item in avatar.mailboxContents:
        bankId += 10
        if bankId > MaxBankId:
            return None
        
        item = CatalogFurnitureItem(bankId)
    return item


def getAllBanks():
    return BankToMoney.keys()

