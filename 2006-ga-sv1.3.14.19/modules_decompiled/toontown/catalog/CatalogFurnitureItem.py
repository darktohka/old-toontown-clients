# File: C (Python 2.2)

import CatalogAtticItem
import CatalogItem
import random
from toontown.toonbase import TTLocalizer
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
FLBillboard = 128
furnitureColors = [
    (0.79200000000000004, 0.35299999999999998, 0.28999999999999998, 1.0),
    (0.17599999999999999, 0.59199999999999997, 0.439, 1.0),
    (0.439, 0.42399999999999999, 0.68200000000000005, 1.0),
    (0.32500000000000001, 0.57999999999999996, 0.83499999999999996, 1.0),
    (0.753, 0.34499999999999997, 0.55700000000000005, 1.0),
    (0.99199999999999999, 0.84299999999999997, 0.39200000000000002, 1.0)]
woodColors = [
    (0.93300000000000005, 0.77300000000000002, 0.56899999999999995, 1.0),
    (0.93330000000000002, 0.67849999999999999, 0.055, 1.0),
    (0.54500000000000004, 0.45100000000000001, 0.33300000000000002, 1.0),
    (0.54100000000000004, 0.0, 0.0, 1.0),
    (0.54510000000000003, 0.27060000000000001, 0.074499999999999997, 1.0),
    (0.54510000000000003, 0.4118, 0.4118, 1.0)]
BankToMoney = {
    1300: 1000,
    1310: 2500,
    1320: 5000,
    1330: 7500,
    1340: 10000 }
MoneyToBank = { }
for (bankId, maxMoney) in BankToMoney.items():
    MoneyToBank[maxMoney] = bankId

MaxBankId = 1340
FurnitureTypes = {
    100: ('phase_5.5/models/estate/chairA', None, None, 80),
    105: ('phase_5.5/models/estate/chairAdesat', None, {
        0: (('**/cushion*', furnitureColors[0]), ('**/arm*', furnitureColors[0])),
        1: (('**/cushion*', furnitureColors[1]), ('**/arm*', furnitureColors[1])),
        2: (('**/cushion*', furnitureColors[2]), ('**/arm*', furnitureColors[2])),
        3: (('**/cushion*', furnitureColors[3]), ('**/arm*', furnitureColors[3])),
        4: (('**/cushion*', furnitureColors[4]), ('**/arm*', furnitureColors[4])),
        5: (('**/cushion*', furnitureColors[5]), ('**/arm*', furnitureColors[5])) }, 160),
    110: ('phase_3.5/models/modules/chair', None, None, 40),
    120: ('phase_5.5/models/estate/deskChair', None, None, 60),
    130: ('phase_5.5/models/estate/BugRoomChair', None, None, 160),
    140: ('phase_5.5/models/estate/UWlobsterChair', None, None, 200),
    145: ('phase_5.5/models/estate/UWlifeSaverChair', None, None, 200),
    150: ('phase_5.5/models/estate/West_saddleStool2', None, None, 160),
    160: ('phase_5.5/models/estate/West_nativeChair', None, None, 160),
    170: ('phase_5.5/models/estate/cupcakeChair', None, None, 240),
    200: ('phase_5.5/models/estate/regular_bed', None, None, 400),
    205: ('phase_5.5/models/estate/regular_bed_desat', None, {
        0: (('**/bar*', woodColors[0]), ('**/post*', woodColors[0]), ('**/*support', woodColors[0]), ('**/top', woodColors[0]), ('**/bottom', woodColors[0]), ('**/pPlane*', woodColors[0])),
        1: (('**/bar*', woodColors[1]), ('**/post*', woodColors[1]), ('**/*support', woodColors[1]), ('**/top', woodColors[1]), ('**/bottom', woodColors[1]), ('**/pPlane*', woodColors[1])),
        2: (('**/bar*', woodColors[2]), ('**/post*', woodColors[2]), ('**/*support', woodColors[2]), ('**/top', woodColors[2]), ('**/bottom', woodColors[2]), ('**/pPlane*', woodColors[2])),
        3: (('**/bar*', woodColors[3]), ('**/post*', woodColors[3]), ('**/*support', woodColors[3]), ('**/top', woodColors[3]), ('**/bottom', woodColors[3]), ('**/pPlane*', woodColors[3])),
        4: (('**/bar*', woodColors[4]), ('**/post*', woodColors[4]), ('**/*support', woodColors[4]), ('**/top', woodColors[4]), ('**/bottom', woodColors[4]), ('**/pPlane*', woodColors[4])),
        5: (('**/bar*', woodColors[5]), ('**/post*', woodColors[5]), ('**/*support', woodColors[5]), ('**/top', woodColors[5]), ('**/bottom', woodColors[5]), ('**/pPlane*', woodColors[5])) }, 800),
    210: ('phase_5.5/models/estate/girly_bed', None, None, 450),
    220: ('phase_5.5/models/estate/bathtub_bed', None, None, 550),
    230: ('phase_5.5/models/estate/bugRoomBed', None, None, 600),
    240: ('phase_5.5/models/estate/UWBoatBed', None, None, 600),
    250: ('phase_5.5/models/estate/West_cactusHammoc', None, None, 550),
    260: ('phase_5.5/models/estate/icecreamBed', None, None, 700),
    300: ('phase_5.5/models/estate/Piano', None, None, 1000, FLIsTable),
    310: ('phase_5.5/models/estate/Organ', None, None, 2500),
    400: ('phase_5.5/models/estate/FireplaceSq', None, None, 800),
    410: ('phase_5.5/models/estate/FireplaceGirlee', None, None, 800),
    420: ('phase_5.5/models/estate/FireplaceRound', None, None, 800),
    430: ('phase_5.5/models/estate/bugRoomFireplace', None, None, 800),
    440: ('phase_5.5/models/estate/CarmelAppleFireplace', None, None, 800),
    500: ('phase_5.5/models/estate/closetBoy', None, None, 500, FLCloset, 0.84999999999999998),
    502: ('phase_5.5/models/estate/closetBoy', None, None, 500, FLCloset, 1.0),
    510: ('phase_5.5/models/estate/closetGirl', None, None, 500, FLCloset, 0.84999999999999998),
    512: ('phase_5.5/models/estate/closetGirl', None, None, 500, FLCloset, 1.0),
    600: ('phase_3.5/models/modules/lamp_short', None, None, 45, FLOnTable),
    610: ('phase_3.5/models/modules/lamp_tall', None, None, 45),
    620: ('phase_5.5/models/estate/lampA', None, None, 35, FLOnTable),
    625: ('phase_5.5/models/estate/lampADesat', None, {
        0: (('**/top', furnitureColors[0]),),
        1: (('**/top', furnitureColors[1]),),
        2: (('**/top', furnitureColors[2]),),
        3: (('**/top', furnitureColors[3]),),
        4: (('**/top', furnitureColors[4]),),
        5: (('**/top', furnitureColors[5]),) }, 70, FLOnTable),
    630: ('phase_5.5/models/estate/bugRoomDaisyLamp1', None, None, 55),
    640: ('phase_5.5/models/estate/bugRoomDaisyLamp2', None, None, 55),
    650: ('phase_5.5/models/estate/UWlamp_jellyfish', None, None, 55, FLOnTable),
    660: ('phase_5.5/models/estate/UWlamps_jellyfishB', None, None, 55, FLOnTable),
    670: ('phase_5.5/models/estate/West_cowboyLamp', None, None, 55, FLOnTable),
    700: ('phase_3.5/models/modules/couch_1person', None, None, 230),
    705: ('phase_5.5/models/estate/couch_1personDesat', None, {
        0: (('**/*couch', furnitureColors[0]),),
        1: (('**/*couch', furnitureColors[1]),),
        2: (('**/*couch', furnitureColors[2]),),
        3: (('**/*couch', furnitureColors[3]),),
        4: (('**/*couch', furnitureColors[4]),),
        5: (('**/*couch', furnitureColors[5]),) }, 460),
    710: ('phase_3.5/models/modules/couch_2person', None, None, 230),
    715: ('phase_5.5/models/estate/couch_2personDesat', None, {
        0: (('**/*couch', furnitureColors[0]),),
        1: (('**/*couch', furnitureColors[1]),),
        2: (('**/*couch', furnitureColors[2]),),
        3: (('**/*couch', furnitureColors[3]),),
        4: (('**/*couch', furnitureColors[4]),),
        5: (('**/*couch', furnitureColors[5]),) }, 460),
    720: ('phase_5.5/models/estate/West_HayCouch', None, None, 420),
    730: ('phase_5.5/models/estate/twinkieCouch', None, None, 480),
    800: ('phase_3.5/models/modules/desk_only_wo_phone', None, None, 65, FLIsTable),
    810: ('phase_5.5/models/estate/BugRoomDesk', None, None, 125, FLIsTable),
    900: ('phase_3.5/models/modules/umbrella_stand', None, None, 30),
    910: ('phase_3.5/models/modules/coatrack', None, None, 75),
    920: ('phase_3.5/models/modules/paper_trashcan', None, None, 30),
    930: ('phase_5.5/models/estate/BugRoomRedMushroomPot', None, None, 60),
    940: ('phase_5.5/models/estate/BugRoomYellowMushroomPot', None, None, 60),
    950: ('phase_5.5/models/estate/UWcoralClothRack', None, None, 75),
    960: ('phase_5.5/models/estate/west_barrelStand', None, None, 75),
    970: ('phase_5.5/models/estate/West_fatCactus', None, None, 75),
    980: ('phase_5.5/models/estate/West_Tepee', None, None, 150),
    1000: ('phase_3.5/models/modules/rug', None, None, 75, FLRug),
    1010: ('phase_5.5/models/estate/rugA', None, None, 75, FLRug),
    1015: ('phase_5.5/models/estate/rugADesat', None, {
        0: (('**/pPlane*', furnitureColors[0]),),
        1: (('**/pPlane*', furnitureColors[1]),),
        2: (('**/pPlane*', furnitureColors[2]),),
        3: (('**/pPlane*', furnitureColors[3]),),
        4: (('**/pPlane*', furnitureColors[4]),),
        5: (('**/pPlane*', furnitureColors[5]),) }, 150, FLRug),
    1020: ('phase_5.5/models/estate/rugB', None, None, 75, FLRug, 2.5),
    1030: ('phase_5.5/models/estate/bugRoomLeafMat', None, None, 75, FLRug),
    1100: ('phase_5.5/models/estate/cabinetRwood', None, None, 825),
    1110: ('phase_5.5/models/estate/cabinetYwood', None, None, 825),
    1120: ('phase_3.5/models/modules/bookcase', None, None, 650, FLIsTable),
    1130: ('phase_3.5/models/modules/bookcase_low', None, None, 650, FLIsTable),
    1140: ('phase_5.5/models/estate/icecreamChest', None, None, 750),
    1200: ('phase_3.5/models/modules/ending_table', None, None, 60, FLIsTable),
    1210: ('phase_5.5/models/estate/table_radio', None, None, 60, FLIsTable, 50.0),
    1215: ('phase_5.5/models/estate/table_radioDesat', None, {
        0: (('**/RADIOTABLE_*', woodColors[0]),),
        1: (('**/RADIOTABLE_*', woodColors[1]),),
        2: (('**/RADIOTABLE_*', woodColors[2]),),
        3: (('**/RADIOTABLE_*', woodColors[3]),),
        4: (('**/RADIOTABLE_*', woodColors[4]),),
        5: (('**/RADIOTABLE_*', woodColors[5]),) }, 120, FLIsTable, 50.0),
    1220: ('phase_5.5/models/estate/coffeetableSq', None, None, 180, FLIsTable),
    1230: ('phase_5.5/models/estate/coffeetableSq_BW', None, None, 180, FLIsTable),
    1240: ('phase_5.5/models/estate/UWtable', None, None, 180, FLIsTable),
    1250: ('phase_5.5/models/estate/cookieTableA', None, None, 220, FLIsTable),
    1260: ('phase_5.5/models/estate/TABLE_Bedroom_Desat', None, {
        0: (('**/Bedroom_Table', woodColors[0]),),
        1: (('**/Bedroom_Table', woodColors[1]),),
        2: (('**/Bedroom_Table', woodColors[2]),),
        3: (('**/Bedroom_Table', woodColors[3]),),
        4: (('**/Bedroom_Table', woodColors[4]),),
        5: (('**/Bedroom_Table', woodColors[5]),) }, 220, FLIsTable),
    1300: ('phase_5.5/models/estate/jellybeanBank', None, None, 0, FLBank, 0.75),
    1310: ('phase_5.5/models/estate/jellybeanBank', None, None, 400, FLBank, 1.0),
    1320: ('phase_5.5/models/estate/jellybeanBank', None, None, 800, FLBank, 1.125),
    1330: ('phase_5.5/models/estate/jellybeanBank', None, None, 1600, FLBank, 1.25),
    1340: ('phase_5.5/models/estate/jellybeanBank', None, None, 3200, FLBank, 1.5),
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
    1660: ('phase_5.5/models/estate/UWcoralVase', None, None, 120, FLOnTable | FLBillboard),
    1661: ('phase_5.5/models/estate/UWshellVase', None, None, 120, FLOnTable | FLBillboard),
    1700: ('phase_5.5/models/estate/popcornCart', None, None, 400),
    1710: ('phase_5.5/models/estate/bugRoomLadyBug', None, None, 260),
    1720: ('phase_5.5/models/estate/UWfountain', None, None, 450),
    1725: ('phase_5.5/models/estate/UWOceanDryer', None, None, 400),
    1800: ('phase_5.5/models/estate/UWskullBowl', None, None, 120, FLOnTable),
    1810: ('phase_5.5/models/estate/UWlizardBowl', None, None, 120, FLOnTable),
    1900: ('phase_5.5/models/estate/UWswordFish', None, None, 425, FLPainting, 0.5),
    1910: ('phase_5.5/models/estate/UWhammerhead', None, None, 425, FLPainting),
    1920: ('phase_5.5/models/estate/West_hangingHorns', None, None, 475, FLPainting),
    1930: ('phase_5.5/models/estate/West_Sombrero', None, None, 425, FLPainting),
    1940: ('phase_5.5/models/estate/West_fancySombrero', None, None, 450, FLPainting),
    1950: ('phase_5.5/models/estate/West_CoyotePawdecor', None, None, 475, FLPainting),
    1960: ('phase_5.5/models/estate/West_Horseshoe', None, None, 475, FLPainting),
    1970: ('phase_5.5/models/estate/West_bisonPortrait', None, None, 475, FLPainting),
    2000: ('phase_5.5/models/estate/candySwingSet', None, None, 300),
    2010: ('phase_5.5/models/estate/cakeSlide', None, None, 200),
    3000: ('phase_5.5/models/estate/BanannaSplitShower', None, None, 400),
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
            return TTLocalizer.FurnitureYourOldCloset
        elif self.getFlags() & FLBank:
            return TTLocalizer.FurnitureYourOldBank
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
            return TTLocalizer.PaintingTypeName
        else:
            return TTLocalizer.FurnitureTypeName

    
    def getName(self):
        return TTLocalizer.FurnitureNames[self.furnitureType]

    
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
        elif flags & FLBillboard:
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
            if store & CatalogItem.Customization:
                self.colorOption = di.getUint8()
                option = type[FTColorOptions][self.colorOption]
            
        

    
    def encodeDatagram(self, dg, store):
        CatalogAtticItem.CatalogAtticItem.encodeDatagram(self, dg, store)
        dg.addInt16(self.furnitureType)
        if FurnitureTypes[self.furnitureType][FTColorOptions]:
            if store & CatalogItem.Customization:
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
    list = []
    for bankId in BankToMoney.keys():
        list.append(CatalogFurnitureItem(bankId))
    
    return list


def getAllFurnitures(index):
    list = []
    colors = FurnitureTypes[index][FTColorOptions]
    for n in range(len(colors)):
        list.append(CatalogFurnitureItem(index, n))
    
    return list

