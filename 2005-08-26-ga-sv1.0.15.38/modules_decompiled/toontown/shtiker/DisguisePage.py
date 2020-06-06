# File: D (Python 2.2)

import ShtikerPage
from direct.gui.DirectGui import *
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.suit import SuitDNA
from toontown.battle import SuitBattleGlobals
from toontown.minigame import MinigamePowerMeter
from pandac.PandaModules import VBase4
from toontown.coghq import CogDisguiseGlobals
DeptColors = (Vec4(0.64700000000000002, 0.60799999999999998, 0.59599999999999997, 1.0), Vec4(0.58799999999999997, 0.63500000000000001, 0.67100000000000004, 1.0), Vec4(0.59599999999999997, 0.71399999999999997, 0.65900000000000003, 1.0), Vec4(0.76100000000000001, 0.67800000000000005, 0.68999999999999995, 1.0))
NumParts = max(CogDisguiseGlobals.PartsPerSuit)
PartNames = ('lUpleg', 'lLowleg', 'lShoe', 'rUpleg', 'rLowleg', 'rShoe', 'lShoulder', 'rShoulder', 'chest', 'waist', 'hip', 'lUparm', 'lLowarm', 'lHand', 'rUparm', 'rLowarm', 'rHand')

class DisguisePage(ShtikerPage.ShtikerPage):
    meterColor = Vec4(0.87, 0.87, 0.82699999999999996, 1.0)
    meterActiveColor = Vec4(0.69999999999999996, 0.29999999999999999, 0.29999999999999999, 1)
    
    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.activeTab = 0
        self.progressTitle = None

    
    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        gui = loader.loadModelCopy('phase_9/models/gui/cog_disguises')
        self.frame = DirectFrame(parent = self, relief = None, scale = 0.46999999999999997, pos = (0.02, 1, 0))
        self.bkgd = DirectFrame(parent = self.frame, geom = gui.find('**/base'), relief = None, scale = (0.97999999999999998, 1, 1))
        self.bkgd.setTextureOff(1)
        self.tabs = []
        self.pageFrame = DirectFrame(parent = self.frame, relief = None)
        for dept in SuitDNA.suitDepts:
            if dept == 'c':
                tabIndex = 1
                textPos = (1.5700000000000001, 0.75)
            elif dept == 'l':
                tabIndex = 2
                textPos = (1.5700000000000001, 0.12)
            elif dept == 'm':
                tabIndex = 3
                textPos = (1.5700000000000001, -0.46999999999999997)
            elif dept == 's':
                tabIndex = 4
                textPos = (1.5700000000000001, -1.05)
            
            pageGeom = gui.find('**/page%d' % tabIndex)
            tabGeom = gui.find('**/tab%d' % tabIndex)
            tab = DirectButton(parent = self.pageFrame, relief = None, geom = tabGeom, geom_color = DeptColors[tabIndex - 1], text = SuitDNA.suitDeptFullnames[dept], text_font = ToontownGlobals.getSuitFont(), text_pos = textPos, text_roll = -90, text_scale = 0.10000000000000001, text_align = TextNode.ACenter, text1_fg = Vec4(1, 0, 0, 1), text2_fg = Vec4(0.5, 0.40000000000000002, 0.40000000000000002, 1), text3_fg = Vec4(0.40000000000000002, 0.40000000000000002, 0.40000000000000002, 1), command = self.doTab, extraArgs = [
                len(self.tabs)], pressEffect = 0)
            self.tabs.append(tab)
            page = DirectFrame(parent = tab, relief = None, geom = pageGeom)
        
        self.deptLabel = DirectLabel(parent = self.frame, text = '', text_font = ToontownGlobals.getSuitFont(), text_scale = 0.17000000000000001, text_pos = (-0.10000000000000001, 0.80000000000000004))
        DirectFrame(parent = self.frame, relief = None, geom = gui.find('**/pipe_frame'))
        self.tube = DirectFrame(parent = self.frame, relief = None, geom = gui.find('**/tube'))
        DirectFrame(parent = self.frame, relief = None, geom = gui.find('**/robot/face'))
        DirectLabel(parent = self.frame, relief = None, geom = gui.find('**/text_cog_disguises'), geom_pos = (0, 0.10000000000000001, 0))
        self.meritTitle = DirectLabel(parent = self.frame, relief = None, geom = gui.find('**/text_merit_progress'), geom_pos = (0, 0.10000000000000001, 0))
        self.meritTitle.hide()
        self.cogbuckTitle = DirectLabel(parent = self.frame, relief = None, geom = gui.find('**/text_cashbuck_progress'), geom_pos = (0, 0.10000000000000001, 0))
        self.cogbuckTitle.hide()
        self.progressTitle = self.meritTitle
        self.promotionTitle = DirectLabel(parent = self.frame, relief = None, geom = gui.find('**/text_ready4promotion'), geom_pos = (0, 0.10000000000000001, 0))
        self.cogName = DirectLabel(parent = self.frame, relief = None, text = '', text_font = ToontownGlobals.getSuitFont(), text_scale = 0.092999999999999999, text_align = TextNode.ACenter, pos = (-0.94799999999999995, 0, -1.1499999999999999))
        self.cogLevel = DirectLabel(parent = self.frame, relief = None, text = '', text_font = ToontownGlobals.getSuitFont(), text_scale = 0.089999999999999997, text_align = TextNode.ACenter, pos = (-0.91000000000000003, 0, -1.02))
        self.partFrame = DirectFrame(parent = self.frame, relief = None)
        self.parts = []
        for partNum in range(0, NumParts):
            self.parts.append(DirectFrame(parent = self.partFrame, relief = None, geom = gui.find('**/robot/' + PartNames[partNum])))
        
        self.holes = []
        for partNum in range(0, NumParts):
            self.holes.append(DirectFrame(parent = self.partFrame, relief = None, geom = gui.find('**/robot_hole/' + PartNames[partNum])))
        
        self.cogPartRatio = DirectLabel(parent = self.frame, relief = None, text = '', text_font = ToontownGlobals.getSuitFont(), text_scale = 0.080000000000000002, text_align = TextNode.ACenter, pos = (-0.91000000000000003, 0, -0.81999999999999995))
        self.cogMeritRatio = DirectLabel(parent = self.frame, relief = None, text = '', text_font = ToontownGlobals.getSuitFont(), text_scale = 0.080000000000000002, text_align = TextNode.ACenter, pos = (0.45000000000000001, 0, -0.35999999999999999))
        meterFace = gui.find('**/meter_face_whole')
        meterFaceHalf = gui.find('**/meter_face_half')
        self.meterFace = DirectLabel(parent = self.frame, relief = None, geom = meterFace, color = self.meterColor, pos = (0.45500000000000002, 0.0, 0.040000000000000001))
        self.meterFaceHalf1 = DirectLabel(parent = self.frame, relief = None, geom = meterFaceHalf, color = self.meterActiveColor, pos = (0.45500000000000002, 0.0, 0.040000000000000001))
        self.meterFaceHalf2 = DirectLabel(parent = self.frame, relief = None, geom = meterFaceHalf, color = self.meterColor, pos = (0.45500000000000002, 0.0, 0.040000000000000001))
        self.frame.hide()
        self.activeTab = 3
        self.updatePage()

    
    def unload(self):
        ShtikerPage.ShtikerPage.unload(self)

    
    def enter(self):
        self.frame.show()
        ShtikerPage.ShtikerPage.enter(self)

    
    def exit(self):
        self.frame.hide()
        ShtikerPage.ShtikerPage.exit(self)

    
    def updatePage(self):
        self.doTab(self.activeTab)

    
    def updatePartsDisplay(self, index, numParts, numPartsRequired):
        partBitmask = 1
        groupingBitmask = CogDisguiseGlobals.PartsPerSuitBitmasks[index]
        previousPart = 0
        for part in self.parts:
            groupingBit = groupingBitmask & partBitmask
            if numParts & partBitmask & groupingBit:
                part.show()
                self.holes[self.parts.index(part)].hide()
                if groupingBit:
                    previousPart = 1
                
            elif not groupingBit and previousPart:
                part.show()
                self.holes[self.parts.index(part)].hide()
            else:
                self.holes[self.parts.index(part)].show()
                part.hide()
                previousPart = 0
            partBitmask = partBitmask << 1
        

    
    def updateMeritBar(self, dept):
        merits = base.localAvatar.cogMerits[dept]
        totalMerits = CogDisguiseGlobals.getTotalMerits(base.localAvatar, dept)
        if totalMerits == 0:
            progress = 1
        else:
            progress = min(merits / float(totalMerits), 1)
        self.updateMeritDial(progress)
        if base.localAvatar.readyForPromotion(dept):
            self.cogMeritRatio['text'] = TTLocalizer.DisguisePageMeritFull
            self.promotionTitle.show()
            self.progressTitle.hide()
        else:
            self.cogMeritRatio['text'] = '%d/%d' % (merits, totalMerits)
            self.promotionTitle.hide()
            self.progressTitle.show()

    
    def updateMeritDial(self, progress):
        if progress == 0:
            self.meterFaceHalf1.hide()
            self.meterFaceHalf2.hide()
            self.meterFace.setColor(self.meterColor)
        elif progress == 1:
            self.meterFaceHalf1.hide()
            self.meterFaceHalf2.hide()
            self.meterFace.setColor(self.meterActiveColor)
        else:
            self.meterFaceHalf1.show()
            self.meterFaceHalf2.show()
            self.meterFace.setColor(self.meterColor)
            if progress < 0.5:
                self.meterFaceHalf2.setColor(self.meterColor)
            else:
                self.meterFaceHalf2.setColor(self.meterActiveColor)
                progress = progress - 0.5
            self.meterFaceHalf2.setR(180 * (progress / 0.5))

    
    def doTab(self, index):
        self.activeTab = index
        self.tabs[index].reparentTo(self.pageFrame)
        for i in range(len(self.tabs)):
            tab = self.tabs[i]
            if i == index:
                tab['text0_fg'] = (1, 0, 0, 1)
                tab['text2_fg'] = (1, 0, 0, 1)
            else:
                tab['text0_fg'] = (0, 0, 0, 1)
                tab['text2_fg'] = (0.5, 0.40000000000000002, 0.40000000000000002, 1)
        
        self.bkgd.setColor(DeptColors[index])
        self.deptLabel['text'] = (SuitDNA.suitDeptFullnames[SuitDNA.suitDepts[index]],)
        cogIndex = base.localAvatar.cogTypes[index] + SuitDNA.suitsPerDept * index
        cog = SuitDNA.suitHeadTypes[cogIndex]
        self.progressTitle.hide()
        if SuitDNA.suitDepts[index] == 'm':
            self.progressTitle = self.cogbuckTitle
        else:
            self.progressTitle = self.meritTitle
        self.progressTitle.show()
        self.cogName['text'] = SuitBattleGlobals.SuitAttributes[cog]['name']
        cogLevel = base.localAvatar.cogLevels[index]
        self.cogLevel['text'] = TTLocalizer.DisguisePageCogLevel % str(cogLevel + 1)
        numParts = base.localAvatar.cogParts[index]
        numPartsRequired = CogDisguiseGlobals.PartsPerSuit[index]
        self.updatePartsDisplay(index, numParts, numPartsRequired)
        self.updateMeritBar(index)
        self.cogPartRatio['text'] = '%d/%d' % (CogDisguiseGlobals.getTotalParts(numParts), numPartsRequired)


