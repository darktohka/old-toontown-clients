# File: F (Python 2.2)

import ToontownGlobals
import ShtikerPage
from DirectGui import *
import Localizer
import FishPicker
import FishBrowser
import FishGlobals
import ToontownDialog
FishPage_Tank = 0
FishPage_Collection = 1
FishPage_Trophy = 2

class FishPage(ShtikerPage.ShtikerPage):
    
    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.avatar = None
        self.mode = FishPage_Collection

    
    def enter(self):
        self.updatePage()
        ShtikerPage.ShtikerPage.enter(self)
        return None

    
    def exit(self):
        ShtikerPage.ShtikerPage.exit(self)
        return None

    
    def setAvatar(self, av):
        self.avatar = av

    
    def getAvatar(self):
        return self.avatar

    
    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        gui = loader.loadModelCopy('phase_3.5/models/gui/fishingBook')
        self.title = DirectLabel(parent = self, relief = None, text = '', text_scale = 0.10000000000000001, pos = (0, 0, 0.65000000000000002))
        self.picker = FishPicker.FishPicker(self)
        self.picker.load()
        self.picker.setPos(-0.55500000000000005, 0, 0.10000000000000001)
        self.picker.setScale(0.94999999999999996)
        rodFrame = gui.find('**/bucket/fram1')
        rodFrame.removeNode()
        self.rod = DirectLabel(parent = self.picker, relief = None, text = '', text_align = TextNode.ALeft, text_scale = 0.059999999999999998, pos = (0.90000000000000002, 0, -0.65000000000000002))
        self.browser = FishBrowser.FishBrowser(self)
        self.browser.load()
        self.browser.setScale(1.1000000000000001)
        self.collectedTotal = DirectLabel(parent = self.browser, relief = None, text = '', text_scale = 0.059999999999999998, pos = (0, 0, -0.60999999999999999))
        trophyCase = gui.find('**/trophyCase1')
        trophyCase.find('glass1').reparentTo(trophyCase, -1)
        trophyCase.find('shelf').reparentTo(trophyCase, -1)
        self.trophyFrame = DirectFrame(parent = self, relief = None, image = trophyCase, image_pos = (0, 1, 0), image_scale = 0.034000000000000002)
        self.trophyFrame.hide()
        self.trophies = []
        offset = -0.5
        for (level, trophyDesc) in FishGlobals.TrophyDict.items():
            trophy = FishingTrophy(-1)
            trophy.nameLabel['text'] = trophyDesc[0]
            trophy.reparentTo(self.trophyFrame)
            trophy.setPos(offset, 0, 0)
            trophy.setScale(0.35999999999999999)
            offset += 0.25
            self.trophies.append(trophy)
        
        self.tankTab = DirectButton(parent = self, relief = None, text = Localizer.FishPageTankTab, text_scale = 0.070000000000000007, text_align = TextNode.ALeft, image = gui.find('**/tabs/polySurface1'), image_pos = (0.55000000000000004, 1, -0.91000000000000003), image_hpr = (0, 0, 90), image_scale = (0.033000000000000002, 0.033000000000000002, 0.035000000000000003), text_fg = Vec4(0.20000000000000001, 0.10000000000000001, 0, 1), text1_bg = Vec4(0.90000000000000002, 0.59999999999999998, 0.40000000000000002, 0.84999999999999998), text2_bg = Vec4(0.90000000000000002, 0.59999999999999998, 0.40000000000000002, 0.25), command = self.setMode, extraArgs = [
            FishPage_Tank], pos = (0.92000000000000004, 0, 0.55000000000000004))
        self.collectionTab = DirectButton(parent = self, relief = None, text = Localizer.FishPageCollectionTab, text_scale = 0.070000000000000007, text_align = TextNode.ALeft, image = gui.find('**/tabs/polySurface2'), image_pos = (0.12, 1, -0.91000000000000003), image_hpr = (0, 0, 90), image_scale = (0.033000000000000002, 0.033000000000000002, 0.035000000000000003), text_fg = Vec4(0.20000000000000001, 0.10000000000000001, 0, 1), text1_bg = Vec4(0.90000000000000002, 0.59999999999999998, 0.40000000000000002, 0.84999999999999998), text2_bg = Vec4(0.90000000000000002, 0.59999999999999998, 0.40000000000000002, 0.25), command = self.setMode, extraArgs = [
            FishPage_Collection], pos = (0.92000000000000004, 0, 0.10000000000000001))
        self.trophyTab = DirectButton(parent = self, relief = None, text = Localizer.FishPageTrophyTab, text_scale = 0.070000000000000007, text_align = TextNode.ALeft, image = gui.find('**/tabs/polySurface3'), image_pos = (-0.28000000000000003, 1, -0.91000000000000003), image_hpr = (0, 0, 90), image_scale = (0.033000000000000002, 0.033000000000000002, 0.035000000000000003), text_fg = Vec4(0.20000000000000001, 0.10000000000000001, 0, 1), text1_bg = Vec4(0.90000000000000002, 0.59999999999999998, 0.40000000000000002, 0.84999999999999998), text2_bg = Vec4(0.90000000000000002, 0.59999999999999998, 0.40000000000000002, 0.25), command = self.setMode, extraArgs = [
            FishPage_Trophy], pos = (0.92000000000000004, 0, -0.29999999999999999))
        self.tankTab.setPos(-0.55000000000000004, 0, 0.77500000000000002)
        self.collectionTab.setPos(-0.13, 0, 0.77500000000000002)
        self.trophyTab.setPos(0.28000000000000003, 0, 0.77500000000000002)
        self.setMode(FishPage_Tank)

    
    def setMode(self, mode):
        messenger.send('wakeup')
        if self.mode == mode:
            return None
        else:
            self.mode = mode
        if mode == FishPage_Tank:
            self.title['text'] = Localizer.FishPageTitleTank
            self.picker.show()
            self.browser.hide()
            self.trophyFrame.hide()
            self.tankTab['image_color'] = Vec4(1, 1, 1, 1)
            self.collectionTab['image_color'] = Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1)
            self.trophyTab['image_color'] = Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1)
        elif mode == FishPage_Collection:
            self.title['text'] = Localizer.FishPageTitleCollection
            self.picker.hide()
            self.browser.show()
            self.trophyFrame.hide()
            self.tankTab['image_color'] = Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1)
            self.collectionTab['image_color'] = Vec4(1, 1, 1, 1)
            self.trophyTab['image_color'] = Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1)
        elif mode == FishPage_Trophy:
            self.title['text'] = Localizer.FishPageTitleTrophy
            self.picker.hide()
            self.browser.hide()
            self.trophyFrame.show()
            self.tankTab['image_color'] = Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1)
            self.collectionTab['image_color'] = Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1)
            self.trophyTab['image_color'] = Vec4(1, 1, 1, 1)
        

    
    def unload(self):
        del self.trophies
        ShtikerPage.ShtikerPage.unload(self)

    
    def updatePage(self):
        newTankFish = toonbase.localToon.fishTank.getFish()
        self.picker.update(newTankFish)
        self.collectedTotal['text'] = Localizer.FishPageCollectedTotal % (len(toonbase.localToon.fishCollection), FishGlobals.getTotalNumFish())
        rod = toonbase.localToon.fishingRod
        rodName = Localizer.FishingRodNameDict[rod]
        rodWeightRange = FishGlobals.getRodWeightRange(rod)
        self.rod['text'] = Localizer.FishPageRodInfo % (rodName, rodWeightRange[0], rodWeightRange[1])
        self.browser.update()
        for trophy in self.trophies:
            trophy.setLevel(-1)
        
        for trophyId in toonbase.localToon.getFishingTrophies():
            self.trophies[trophyId].setLevel(trophyId)
        



class FishingTrophy(DirectFrame):
    
    def __init__(self, level):
        DirectFrame.__init__(self, relief = None)
        self.initialiseoptions(FishingTrophy)
        self.trophy = loader.loadModelCopy('phase_3.5/models/gui/fishingTrophy')
        self.trophy.reparentTo(self)
        self.trophy.setPos(0, 1, 0)
        self.trophy.setScale(0.10000000000000001)
        self.base = self.trophy.find('**/trophyBase')
        self.column = self.trophy.find('**/trophyColumn')
        self.top = self.trophy.find('**/trophyTop')
        self.topBase = self.trophy.find('**/trophyTopBase')
        self.statue = self.trophy.find('**/trophyStatue')
        self.base.setColorScale(1, 1, 0.80000000000000004, 1)
        self.nameLabel = DirectLabel(parent = self, relief = None, pos = (0, 0, -0.14999999999999999), text = 'Trophy Text', text_scale = 0.125, text_fg = Vec4(0.90000000000000002, 0.90000000000000002, 0.40000000000000002, 1))
        self.shadow = loader.loadModelCopy('phase_3/models/props/drop_shadow')
        self.shadow.reparentTo(self)
        self.shadow.setColor(1, 1, 1, 0.20000000000000001)
        self.shadow.setPosHprScale(0, 1, 0.34999999999999998, 0, 90, 0, 0.10000000000000001, 0.14000000000000001, 0.10000000000000001)
        self.setLevel(level)

    
    def setLevel(self, level):
        self.level = level
        if level == -1:
            self.trophy.hide()
            self.nameLabel.hide()
        elif level == 0:
            self.trophy.show()
            self.nameLabel.show()
            self.column.setScale(1.3229, 1.26468, 1.1187800000000001)
            self.top.setPos(0, 0, -1)
            self._FishingTrophy__bronze()
        elif level == 1:
            self.trophy.show()
            self.nameLabel.show()
            self.column.setScale(1.3229, 1.26468, 1.6187800000000001)
            self.top.setPos(0, 0, -0.5)
            self._FishingTrophy__bronze()
        elif level == 2:
            self.trophy.show()
            self.nameLabel.show()
            self.column.setScale(1.3229, 1.26468, 2.1187800000000001)
            self.top.setPos(0, 0, 0)
            self._FishingTrophy__silver()
        elif level == 3:
            self.trophy.show()
            self.nameLabel.show()
            self.column.setScale(1.3229, 1.26468, 2.6187800000000001)
            self.top.setPos(0, 0, 0.5)
            self._FishingTrophy__silver()
        elif level >= 4:
            self.trophy.show()
            self.nameLabel.show()
            self.column.setScale(1.3229, 1.26468, 3.1187800000000001)
            self.top.setPos(0, 0, 1)
            self._FishingTrophy__gold()
        

    
    def _FishingTrophy__bronze(self):
        self.top.setColorScale(0.90000000000000002, 0.59999999999999998, 0.33000000000000002, 1)

    
    def _FishingTrophy__silver(self):
        self.top.setColorScale(0.90000000000000002, 0.90000000000000002, 1, 1)

    
    def _FishingTrophy__gold(self):
        self.top.setColorScale(1, 0.94999999999999996, 0.10000000000000001, 1)

    
    def destroy(self):
        self.trophy.removeNode()
        self.shadow.removeNode()
        DirectFrame.destroy(self)


