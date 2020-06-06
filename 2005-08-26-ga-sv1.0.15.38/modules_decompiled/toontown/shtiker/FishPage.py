# File: F (Python 2.2)

from toontown.toonbase import ToontownGlobals
import ShtikerPage
from direct.directnotify import DirectNotifyGlobal
from direct.gui.DirectGui import *
from toontown.toonbase import TTLocalizer
from toontown.fishing import FishPicker
from toontown.fishing import FishBrowser
from toontown.fishing import FishGlobals
FishPage_Tank = 0
FishPage_Collection = 1
FishPage_Trophy = 2
TROPHIES_PER_ROW = 5

class FishPage(ShtikerPage.ShtikerPage):
    notify = DirectNotifyGlobal.directNotify.newCategory('FishPage')
    
    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.avatar = None
        self.mode = FishPage_Tank

    
    def enter(self):
        if not hasattr(self, 'title'):
            self.load()
        
        self.setMode(self.mode, 1)
        ShtikerPage.ShtikerPage.enter(self)

    
    def exit(self):
        if hasattr(self, 'picker'):
            self.picker.hide()
        
        if hasattr(self, 'browser'):
            self.browser.hide()
        
        ShtikerPage.ShtikerPage.exit(self)

    
    def setAvatar(self, av):
        self.avatar = av

    
    def getAvatar(self):
        return self.avatar

    
    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        gui = loader.loadModelCopy('phase_3.5/models/gui/fishingBook')
        rodFrame = gui.find('**/bucket/fram1')
        rodFrame.removeNode()
        trophyCase = gui.find('**/trophyCase1')
        trophyCase.find('glass1').reparentTo(trophyCase, -1)
        trophyCase.find('shelf').reparentTo(trophyCase, -1)
        self.trophyCase = trophyCase
        self.title = DirectLabel(parent = self, relief = None, text = '', text_scale = 0.10000000000000001, pos = (0, 0, 0.65000000000000002))
        normalColor = (1, 1, 1, 1)
        clickColor = (0.80000000000000004, 0.80000000000000004, 0, 1)
        rolloverColor = (0.14999999999999999, 0.81999999999999995, 1.0, 1)
        diabledColor = (1.0, 0.97999999999999998, 0.14999999999999999, 1)
        self.tankTab = DirectButton(parent = self, relief = None, text = TTLocalizer.FishPageTankTab, text_scale = 0.070000000000000007, text_align = TextNode.ALeft, image = gui.find('**/tabs/polySurface1'), image_pos = (0.55000000000000004, 1, -0.91000000000000003), image_hpr = (0, 0, -90), image_scale = (0.033000000000000002, 0.033000000000000002, 0.035000000000000003), image_color = normalColor, image1_color = clickColor, image2_color = rolloverColor, image3_color = diabledColor, text_fg = Vec4(0.20000000000000001, 0.10000000000000001, 0, 1), command = self.setMode, extraArgs = [
            FishPage_Tank], pos = (0.92000000000000004, 0, 0.55000000000000004))
        self.collectionTab = DirectButton(parent = self, relief = None, text = TTLocalizer.FishPageCollectionTab, text_scale = 0.070000000000000007, text_align = TextNode.ALeft, image = gui.find('**/tabs/polySurface2'), image_pos = (0.12, 1, -0.91000000000000003), image_hpr = (0, 0, -90), image_scale = (0.033000000000000002, 0.033000000000000002, 0.035000000000000003), image_color = normalColor, image1_color = clickColor, image2_color = rolloverColor, image3_color = diabledColor, text_fg = Vec4(0.20000000000000001, 0.10000000000000001, 0, 1), command = self.setMode, extraArgs = [
            FishPage_Collection], pos = (0.92000000000000004, 0, 0.10000000000000001))
        self.trophyTab = DirectButton(parent = self, relief = None, text = TTLocalizer.FishPageTrophyTab, text_scale = 0.070000000000000007, text_align = TextNode.ALeft, image = gui.find('**/tabs/polySurface3'), image_pos = (-0.28000000000000003, 1, -0.91000000000000003), image_hpr = (0, 0, -90), image_scale = (0.033000000000000002, 0.033000000000000002, 0.035000000000000003), image_color = normalColor, image1_color = clickColor, image2_color = rolloverColor, image3_color = diabledColor, text_fg = Vec4(0.20000000000000001, 0.10000000000000001, 0, 1), command = self.setMode, extraArgs = [
            FishPage_Trophy], pos = (0.92000000000000004, 0, -0.29999999999999999))
        self.tankTab.setPos(-0.55000000000000004, 0, 0.77500000000000002)
        self.collectionTab.setPos(-0.13, 0, 0.77500000000000002)
        self.trophyTab.setPos(0.28000000000000003, 0, 0.77500000000000002)

    
    def createFishPicker(self):
        if not hasattr(self, 'picker'):
            self.picker = FishPicker.FishPicker(self)
            self.picker.setPos(-0.55500000000000005, 0, 0.10000000000000001)
            self.picker.setScale(0.94999999999999996)
            self.rod = DirectLabel(parent = self.picker, relief = None, text = '', text_align = TextNode.ALeft, text_scale = 0.059999999999999998, pos = (0.90000000000000002, 0, -0.65000000000000002))
        

    
    def createFishBrowser(self):
        if not hasattr(self, 'browser'):
            self.browser = FishBrowser.FishBrowser(self)
            self.browser.setScale(1.1000000000000001)
            self.collectedTotal = DirectLabel(parent = self.browser, relief = None, text = '', text_scale = 0.059999999999999998, pos = (0, 0, -0.60999999999999999))
        

    
    def createFishTrophyFrame(self):
        if not hasattr(self, 'trophyFrame'):
            self.trophyFrame = DirectFrame(parent = self, relief = None, image = self.trophyCase, image_pos = (0, 1, 0), image_scale = 0.034000000000000002)
            self.trophyFrame.hide()
            self.trophies = []
            hOffset = -0.5
            vOffset = 0.40000000000000002
            for (level, trophyDesc) in FishGlobals.TrophyDict.items():
                trophy = FishingTrophy(-1)
                trophy.nameLabel['text'] = trophyDesc[0]
                trophy.reparentTo(self.trophyFrame)
                trophy.setScale(0.35999999999999999)
                if level % TROPHIES_PER_ROW == 0:
                    hOffset = -0.5
                    vOffset -= 0.40000000000000002
                
                trophy.setPos(hOffset, 0, vOffset)
                hOffset += 0.25
                self.trophies.append(trophy)
            
        

    
    def setMode(self, mode, updateAnyways = 0):
        messenger.send('wakeup')
        if not updateAnyways:
            if self.mode == mode:
                return None
            else:
                self.mode = mode
        
        if mode == FishPage_Tank:
            self.title['text'] = TTLocalizer.FishPageTitleTank
            if not hasattr(self, 'picker'):
                self.createFishPicker()
            
            self.picker.show()
            if hasattr(self, 'browser'):
                self.browser.hide()
            
            if hasattr(self, 'trophyFrame'):
                self.trophyFrame.hide()
            
            self.tankTab['state'] = DISABLED
            self.collectionTab['state'] = NORMAL
            self.trophyTab['state'] = NORMAL
        elif mode == FishPage_Collection:
            self.title['text'] = TTLocalizer.FishPageTitleCollection
            if hasattr(self, 'picker'):
                self.picker.hide()
            
            if not hasattr(self, 'browser'):
                self.createFishBrowser()
            
            self.browser.show()
            if hasattr(self, 'trophyFrame'):
                self.trophyFrame.hide()
            
            self.tankTab['state'] = NORMAL
            self.collectionTab['state'] = DISABLED
            self.trophyTab['state'] = NORMAL
        elif mode == FishPage_Trophy:
            self.title['text'] = TTLocalizer.FishPageTitleTrophy
            if hasattr(self, 'picker'):
                self.picker.hide()
            
            if hasattr(self, 'browser'):
                self.browser.hide()
            
            if not hasattr(self, 'trophyFrame'):
                self.createFishTrophyFrame()
            
            self.trophyFrame.show()
            self.tankTab['state'] = NORMAL
            self.collectionTab['state'] = NORMAL
            self.trophyTab['state'] = DISABLED
        
        self.updatePage()

    
    def unload(self):
        if hasattr(self, 'trophies'):
            del self.trophies
        
        if hasattr(self, 'trophyCase'):
            del self.trophyCase
        
        ShtikerPage.ShtikerPage.unload(self)

    
    def updatePage(self):
        if hasattr(self, 'collectedTotal'):
            self.collectedTotal['text'] = TTLocalizer.FishPageCollectedTotal % (len(base.localAvatar.fishCollection), FishGlobals.getTotalNumFish())
        
        if hasattr(self, 'rod'):
            rod = base.localAvatar.fishingRod
            rodName = TTLocalizer.FishingRodNameDict[rod]
            rodWeightRange = FishGlobals.getRodWeightRange(rod)
            self.rod['text'] = TTLocalizer.FishPageRodInfo % (rodName, rodWeightRange[0], rodWeightRange[1])
        
        if self.mode == FishPage_Tank:
            if hasattr(self, 'picker'):
                newTankFish = base.localAvatar.fishTank.getFish()
                self.picker.update(newTankFish)
            
        elif self.mode == FishPage_Collection:
            if hasattr(self, 'browser'):
                self.browser.update()
            
        elif self.mode == FishPage_Trophy:
            if hasattr(self, 'trophies'):
                for trophy in self.trophies:
                    trophy.setLevel(-1)
                
                for trophyId in base.localAvatar.getFishingTrophies():
                    self.trophies[trophyId].setLevel(trophyId)
                
            
        



class FishingTrophy(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('FishingTrophy')
    
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
        self.bowl = loader.loadModelCopy('phase_3.5/models/gui/fishingTrophyBowl')
        self.bowl.reparentTo(self)
        self.bowl.setPos(0, 1, 0)
        self.bowl.setScale(2.0)
        self.bowlTop = self.bowl.find('**/fishingTrophyGreyBowl')
        self.bowlBase = self.bowl.find('**/fishingTrophyBase')
        self.bowlBase.setScale(1.25, 1, 1)
        self.bowlBase.setColorScale(1, 1, 0.80000000000000004, 1)
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
            self.bowl.hide()
            self.nameLabel.hide()
        elif level == 0:
            self.trophy.show()
            self.bowl.hide()
            self.nameLabel.show()
            self.column.setScale(1.3229, 1.26468, 1.1187800000000001)
            self.top.setPos(0, 0, -1)
            self._FishingTrophy__bronze()
        elif level == 1:
            self.trophy.show()
            self.bowl.hide()
            self.nameLabel.show()
            self.column.setScale(1.3229, 1.26468, 1.6187800000000001)
            self.top.setPos(0, 0, -0.5)
            self._FishingTrophy__bronze()
        elif level == 2:
            self.trophy.show()
            self.bowl.hide()
            self.nameLabel.show()
            self.column.setScale(1.3229, 1.26468, 2.1187800000000001)
            self.top.setPos(0, 0, 0)
            self._FishingTrophy__silver()
        elif level == 3:
            self.trophy.show()
            self.bowl.hide()
            self.nameLabel.show()
            self.column.setScale(1.3229, 1.26468, 2.6187800000000001)
            self.top.setPos(0, 0, 0.5)
            self._FishingTrophy__silver()
        elif level == 4:
            self.trophy.show()
            self.bowl.hide()
            self.nameLabel.show()
            self.column.setScale(1.3229, 1.26468, 3.1187800000000001)
            self.top.setPos(0, 0, 1)
            self._FishingTrophy__gold()
        elif level == 5:
            self.trophy.hide()
            self.bowl.show()
            self.bowlTop.setScale(1.75)
            self.nameLabel.show()
            self._FishingTrophy__bronze()
        elif level == 6:
            self.trophy.hide()
            self.bowl.show()
            self.bowlTop.setScale(2.0)
            self.nameLabel.show()
            self._FishingTrophy__silver()
        elif level >= 7:
            self.trophy.hide()
            self.bowl.show()
            self.bowlTop.setScale(2.25)
            self.nameLabel.show()
            self._FishingTrophy__gold()
        

    
    def _FishingTrophy__bronze(self):
        self.top.setColorScale(0.90000000000000002, 0.59999999999999998, 0.33000000000000002, 1)
        self.bowlTop.setColorScale(0.90000000000000002, 0.59999999999999998, 0.33000000000000002, 1)

    
    def _FishingTrophy__silver(self):
        self.top.setColorScale(0.90000000000000002, 0.90000000000000002, 1, 1)
        self.bowlTop.setColorScale(0.90000000000000002, 0.90000000000000002, 1, 1)

    
    def _FishingTrophy__gold(self):
        self.top.setColorScale(1, 0.94999999999999996, 0.10000000000000001, 1)
        self.bowlTop.setColorScale(1, 0.94999999999999996, 0.10000000000000001, 1)

    
    def destroy(self):
        self.trophy.removeNode()
        self.bowl.removeNode()
        self.shadow.removeNode()
        DirectFrame.destroy(self)


