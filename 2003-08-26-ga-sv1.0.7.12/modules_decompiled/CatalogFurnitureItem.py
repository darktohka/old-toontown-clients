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
FurnitureTypes = {
    100: ('phase_5.5/models/estate/chairA', None, None, 80),
    110: ('phase_3.5/models/modules/chair', None, None, 40),
    200: ('phase_5.5/models/estate/regular_bed', None, None, 400),
    210: ('phase_5.5/models/estate/girly_bed', None, None, 450),
    220: ('phase_5.5/models/estate/bathtub_bed', None, None, 550),
    300: ('phase_5.5/models/estate/Piano', None, None, 1000, FLIsTable),
    310: ('phase_5.5/models/estate/Organ', None, None, 5000),
    400: ('phase_5.5/models/estate/FireplaceSq', None, None, 800),
    410: ('phase_5.5/models/estate/FireplaceGirlee', None, None, 800),
    420: ('phase_5.5/models/estate/FireplaceRound', None, None, 800),
    500: ('phase_5.5/models/estate/closetBoy', None, None, 500, FLCloset),
    510: ('phase_5.5/models/estate/closetGirl', None, None, 500, FLCloset),
    600: ('phase_3.5/models/modules/lamp_short', None, None, 45, FLOnTable),
    610: ('phase_3.5/models/modules/lamp_tall', None, None, 45),
    620: ('phase_5.5/models/estate/lampA', None, None, 35, FLOnTable),
    700: ('phase_3.5/models/modules/couch_1person', None, None, 230),
    710: ('phase_3.5/models/modules/couch_2person', None, None, 230),
    800: ('phase_3.5/models/modules/desk_only_wo_phone', None, None, 65, FLIsTable),
    900: ('phase_3.5/models/modules/umbrella_stand', None, None, 30),
    910: ('phase_3.5/models/modules/coatrack', None, None, 75),
    920: ('phase_3.5/models/modules/paper_trashcan', None, None, 30),
    1000: ('phase_3.5/models/modules/rug', None, None, 75, FLRug),
    1010: ('phase_5.5/models/estate/rugA', None, None, 75, FLRug),
    1020: ('phase_5.5/models/estate/rugB', None, None, 75, FLRug, 2.5),
    1100: ('phase_5.5/models/estate/cabinetRwood', None, None, 825),
    1110: ('phase_5.5/models/estate/cabinetYwood', None, None, 825),
    1120: ('phase_3.5/models/modules/bookcase', None, None, 800, FLIsTable),
    1130: ('phase_3.5/models/modules/bookcase_low', None, None, 650, FLIsTable),
    1200: ('phase_3.5/models/modules/ending_table', None, None, 60, FLIsTable),
    1210: ('phase_5.5/models/estate/table_radio', None, None, 60, FLIsTable, 50.0),
    1300: ('phase_5.5/models/estate/jellybeanBank', None, None, 0, FLBank, 0.75),
    1310: ('phase_5.5/models/estate/jellybeanBank', None, None, 400, FLBank, 1.0),
    1320: ('phase_5.5/models/estate/jellybeanBank', None, None, 800, FLBank, 1.2),
    1399: ('phase_5.5/models/estate/prop_phone-mod', None, None, 0, FLPhone),
    1400: ('phase_5.5/models/estate/cezanne_toon', None, None, 425, FLPainting, 2.0),
    1410: ('phase_5.5/models/estate/flowers', None, None, 425, FLPainting, 2.0),
    1420: ('phase_5.5/models/estate/modernistMickey', None, None, 425, FLPainting, 2.0),
    1430: ('phase_5.5/models/estate/rembrandt_toon', None, None, 425, FLPainting, 2.0),
    1500: ('phase_5.5/models/estate/RADIO_A', None, None, 25, FLOnTable, 15.0),
    1510: ('phase_5.5/models/estate/RADIO_B', None, None, 25, FLOnTable, 15.0),
    1510: ('phase_5.5/models/estate/radio_c', None, None, 25, FLOnTable, 15.0),
    1600: ('phase_5.5/models/estate/vaseA_short', None, None, 120, FLOnTable),
    1610: ('phase_5.5/models/estate/vaseA_tall', None, None, 120, FLOnTable),
    1620: ('phase_5.5/models/estate/vaseB_short', None, None, 120, FLOnTable),
    1630: ('phase_5.5/models/estate/vaseB_tall', None, None, 120, FLOnTable),
    1640: ('phase_5.5/models/estate/vaseC_short', None, None, 120, FLOnTable),
    1650: ('phase_5.5/models/estate/vaseD_short', None, None, 120, FLOnTable) }

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

    
    def isDeletable(self):
        return self.getFlags() & (FLBank | FLCloset | FLPhone) == 0

    
    def getMaxBankMoney(self):
        if self.furnitureType == 1300:
            return 1000
        elif self.furnitureType == 1310:
            return 2500
        elif self.furnitureType == 1320:
            return 5000
        else:
            return None

    
    def reachedPurchaseLimit(self, avatar):
        if self.getFlags() & FLBank:
            if self.getMaxBankMoney() <= avatar.getMaxBankMoney():
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
            model.setBin('unsorted', 0, 1)
        elif flags & FLPainting:
            spin = 0
        
        return self.makeFrameModel(model, spin)

    
    def output(self, store = -1):
        return 'CatalogFurnitureItem(%s%s)' % (self.furnitureType, self.formatOptionalData(store))

    
    def compareTo(self, other):
        return self.furnitureType - other.furnitureType

    
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
        if FurnitureTypes[self.furnitureType][FTColorOptions]:
            if store & CatalogAtticItem.Customization:
                self.colorOption = di.getUint8()
            
        

    
    def encodeDatagram(self, dg, store):
        CatalogAtticItem.CatalogAtticItem.encodeDatagram(self, dg, store)
        dg.addInt16(self.furnitureType)
        if FurnitureTypes[self.furnitureType][FTColorOptions]:
            if store & CatalogAtticItem.Customization:
                dg.addUint8(self.colorOption)
            
        


