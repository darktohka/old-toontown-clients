# File: S (Python 2.2)

import ShtikerPage
from direct.gui.DirectGui import *
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.suit import SuitDNA
from toontown.suit import Suit
from toontown.battle import SuitBattleGlobals
from CogPageGlobals import *
SCALE_FACTOR = 1.5
RADAR_DELAY = 0.20000000000000001
BUILDING_RADAR_POS = (0.375, 0.065000000000000002, -0.22500000000000001, -0.5)
PANEL_COLORS = (Vec4(0.80000000000000004, 0.78000000000000003, 0.77000000000000002, 1), Vec4(0.75, 0.78000000000000003, 0.80000000000000004, 1), Vec4(0.75, 0.81999999999999995, 0.79000000000000004, 1), Vec4(0.82499999999999996, 0.76000000000000001, 0.77000000000000002, 1))
PANEL_COLORS_COMPLETE1 = (Vec4(0.69999999999999996, 0.72499999999999998, 0.54500000000000004, 1), Vec4(0.625, 0.72499999999999998, 0.65000000000000002, 1), Vec4(0.59999999999999998, 0.75, 0.52500000000000002, 1), Vec4(0.67500000000000004, 0.67500000000000004, 0.55000000000000004, 1))
PANEL_COLORS_COMPLETE2 = (Vec4(0.90000000000000002, 0.72499999999999998, 0.32000000000000001, 1), Vec4(0.82499999999999996, 0.72499999999999998, 0.45000000000000001, 1), Vec4(0.80000000000000004, 0.75, 0.32500000000000001, 1), Vec4(0.875, 0.67500000000000004, 0.34999999999999998, 1))
SHADOW_SCALE_POS = ((1.2250000000000001, 0, 10, -0.029999999999999999), (0.90000000000000002, 0, 10, 0), (1.125, 0, 10, -0.014999999999999999), (1.0, 0, 10, -0.02), (1.0, -0.02, 10, -0.01), (1.05, 0, 10, -0.042500000000000003), (1.0, 0, 10, -0.050000000000000003), (0.90000000000000002, -0.022499999999999999, 10, -0.025000000000000001), (1.25, 0, 10, -0.029999999999999999), (1.0, 0, 10, -0.01), (1.0, 0.0050000000000000001, 10, -0.01), (1.0, 0, 10, -0.01), (0.90000000000000002, 0.0050000000000000001, 10, -0.01), (0.94999999999999996, 0, 10, -0.01), (1.125, 0.0050000000000000001, 10, -0.035000000000000003), (0.84999999999999998, -0.0050000000000000001, 10, -0.035000000000000003), (1.2, 0, 10, -0.01), (1.05, 0, 10, 0), (1.1000000000000001, 0, 10, -0.040000000000000001), (1.0, 0, 10, 0), (0.94999999999999996, 0.017500000000000002, 10, -0.014999999999999999), (1.0, 0, 10, -0.059999999999999998), (0.94999999999999996, 0.02, 10, -0.017500000000000002), (0.90000000000000002, 0, 10, -0.029999999999999999), (1.1499999999999999, 0, 10, -0.01), (1.0, 0, 10, 0), (1.0, 0, 10, 0), (1.1000000000000001, 0, 10, -0.040000000000000001), (0.93000000000000005, 0.0050000000000000001, 10, -0.01), (0.94999999999999996, 0.0050000000000000001, 10, -0.01), (1.0, 0, 10, -0.02), (0.90000000000000002, 0.0025000000000000001, 10, -0.029999999999999999))

class SuitPage(ShtikerPage.ShtikerPage):
    
    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)

    
    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        frameModel = loader.loadModelOnce('phase_3.5/models/gui/suitpage_frame')
        frameModel.setScale(0.033750000000000002, 1, 0.044999999999999998)
        frameModel.setPos(0, 10, -0.57499999999999996)
        self.guiTop = NodePath('guiTop')
        self.guiTop.reparentTo(self)
        self.frameNode = NodePath('frameNode')
        self.frameNode.reparentTo(self.guiTop)
        self.panelNode = NodePath('panelNode')
        self.panelNode.reparentTo(self.guiTop)
        self.iconNode = NodePath('iconNode')
        self.iconNode.reparentTo(self.guiTop)
        self.enlargedPanelNode = NodePath('enlargedPanelNode')
        self.enlargedPanelNode.reparentTo(self.guiTop)
        frame = frameModel.find('**/frame')
        frame.wrtReparentTo(self.frameNode)
        screws = frameModel.find('**/screws')
        screws.wrtReparentTo(self.iconNode)
        icons = frameModel.find('**/icons')
        del frameModel
        self.title = DirectLabel(parent = self.iconNode, relief = None, text = TTLocalizer.SuitPageTitle, text_scale = 0.10000000000000001, text_pos = (0.040000000000000001, 0), textMayChange = 0)
        self.radarButtons = []
        icon = icons.find('**/corp_icon')
        self.corpRadarButton = DirectButton(parent = self.iconNode, relief = None, state = DISABLED, image = icon, image_scale = (0.033750000000000002, 1, 0.044999999999999998), image2_color = Vec4(1.0, 1.0, 1.0, 0.75), pos = (-0.20000000000000001, 10, -0.57499999999999996), command = self.toggleRadar, extraArgs = [
            0])
        self.radarButtons.append(self.corpRadarButton)
        icon = icons.find('**/legal_icon')
        self.legalRadarButton = DirectButton(parent = self.iconNode, relief = None, state = DISABLED, image = icon, image_scale = (0.033750000000000002, 1, 0.044999999999999998), image2_color = Vec4(1.0, 1.0, 1.0, 0.75), pos = (-0.20000000000000001, 10, -0.57499999999999996), command = self.toggleRadar, extraArgs = [
            1])
        self.radarButtons.append(self.legalRadarButton)
        icon = icons.find('**/money_icon')
        self.moneyRadarButton = DirectButton(parent = self.iconNode, relief = None, state = DISABLED, image = (icon, icon, icon), image_scale = (0.033750000000000002, 1, 0.044999999999999998), image2_color = Vec4(1.0, 1.0, 1.0, 0.75), pos = (-0.20000000000000001, 10, -0.57499999999999996), command = self.toggleRadar, extraArgs = [
            2])
        self.radarButtons.append(self.moneyRadarButton)
        icon = icons.find('**/sales_icon')
        self.salesRadarButton = DirectButton(parent = self.iconNode, relief = None, state = DISABLED, image = (icon, icon, icon), image_scale = (0.033750000000000002, 1, 0.044999999999999998), image2_color = Vec4(1.0, 1.0, 1.0, 0.75), pos = (-0.20000000000000001, 10, -0.57499999999999996), command = self.toggleRadar, extraArgs = [
            3])
        self.radarButtons.append(self.salesRadarButton)
        for radarButton in self.radarButtons:
            radarButton.building = 0
            radarButton.buildingRadarLabel = None
        
        gui = loader.loadModelOnce('phase_3.5/models/gui/suitpage_gui')
        self.panelModel = gui.find('**/card')
        self.shadowModels = []
        for index in range(1, len(SuitDNA.suitHeadTypes) + 1):
            self.shadowModels.append(gui.find('**/shadow' + str(index)))
        
        del gui
        self.makePanels()
        self.radarOn = [
            0,
            0,
            0,
            0]
        self.guiTop.setZ(0.625)

    
    def unload(self):
        self.title.destroy()
        self.corpRadarButton.destroy()
        self.legalRadarButton.destroy()
        self.moneyRadarButton.destroy()
        self.salesRadarButton.destroy()
        for panel in self.panels:
            panel.destroy()
        
        del self.panels
        for shadow in self.shadowModels:
            shadow.removeNode()
        
        self.panelModel.removeNode()
        ShtikerPage.ShtikerPage.unload(self)

    
    def enter(self):
        self.updatePage()
        ShtikerPage.ShtikerPage.enter(self)

    
    def exit(self):
        taskMgr.remove('buildingListResponseTimeout-later')
        taskMgr.remove('suitListResponseTimeout-later')
        taskMgr.remove('showCogRadarLater')
        taskMgr.remove('showBuildingRadarLater')
        for index in range(0, len(self.radarOn)):
            if self.radarOn[index]:
                self.toggleRadar(index)
                self.radarButtons[index]['state'] = NORMAL
            
        
        ShtikerPage.ShtikerPage.exit(self)

    
    def grow(self, panel, pos):
        panel.reparentTo(self.enlargedPanelNode)
        panel.setScale(panel.getScale() * SCALE_FACTOR)

    
    def shrink(self, panel, pos):
        panel.setScale(panel.scale)
        panel.reparentTo(self.panelNode)

    
    def toggleRadar(self, deptNum):
        messenger.send('wakeup')
        if self.radarOn[deptNum]:
            self.radarOn[deptNum] = 0
        else:
            self.radarOn[deptNum] = 1
        deptSize = SuitDNA.suitsPerDept
        panels = self.panels[deptSize * deptNum:SuitDNA.suitsPerDept * (deptNum + 1)]
        if self.radarOn[deptNum]:
            if hasattr(base.cr, 'currSuitPlanner'):
                if base.cr.currSuitPlanner != None:
                    base.cr.currSuitPlanner.d_suitListQuery()
                    self.acceptOnce('suitListResponse', self.updateCogRadar, extraArgs = [
                        deptNum,
                        panels])
                    taskMgr.doMethodLater(1.0, self.suitListResponseTimeout, 'suitListResponseTimeout-later', extraArgs = (deptNum, panels))
                    if self.radarButtons[deptNum].building:
                        base.cr.currSuitPlanner.d_buildingListQuery()
                        self.acceptOnce('buildingListResponse', self.updateBuildingRadar, extraArgs = [
                            deptNum])
                        taskMgr.doMethodLater(1.0, self.buildingListResponseTimeout, 'buildingListResponseTimeout-later', extraArgs = (deptNum,))
                    
                else:
                    self.updateCogRadar(deptNum, panels)
                    self.updateBuildingRadar(deptNum)
            else:
                self.updateCogRadar(deptNum, panels)
                self.updateBuildingRadar(deptNum)
            self.radarButtons[deptNum]['state'] = DISABLED
        else:
            self.updateCogRadar(deptNum, panels)
            self.updateBuildingRadar(deptNum)

    
    def suitListResponseTimeout(self, deptNum, panels):
        self.updateCogRadar(deptNum, panels, 1)

    
    def buildingListResponseTimeout(self, deptNum):
        self.updateBuildingRadar(deptNum, 1)

    
    def makePanels(self):
        self.panels = []
        xStart = -0.66000000000000003
        yStart = -0.17999999999999999
        xOffset = 0.19900000000000001
        yOffset = 0.28399999999999997
        for dept in range(0, len(SuitDNA.suitDepts)):
            row = []
            color = PANEL_COLORS[dept]
            for type in range(0, SuitDNA.suitsPerDept):
                panel = DirectLabel(parent = self.panelNode, pos = (xStart + type * xOffset, 0.0, yStart - dept * yOffset), relief = None, state = NORMAL, image = self.panelModel, image_scale = (1, 1, 1), image_color = color, text = TTLocalizer.SuitPageMystery, text_scale = 0.044999999999999998, text_fg = (0, 0, 0, 1), text_pos = (0, 0.185, 0), text_font = ToontownGlobals.getSuitFont(), text_wordwrap = 7)
                panel.bind(ENTER, self.grow, extraArgs = [
                    panel])
                panel.bind(EXIT, self.shrink, extraArgs = [
                    panel])
                panel.scale = 0.59999999999999998
                panel.setScale(panel.scale)
                panel.quotaLabel = None
                panel.head = None
                panel.shadow = None
                panel.count = 0
                self.addCogRadarLabel(panel)
                self.panels.append(panel)
            
        

    
    def addQuotaLabel(self, panel):
        index = self.panels.index(panel)
        count = str(base.localAvatar.cogCounts[index])
        if base.localAvatar.cogs[index] < COG_COMPLETE1:
            quota = str(COG_QUOTAS[0][index % SuitDNA.suitsPerDept])
        else:
            quota = str(COG_QUOTAS[1][index % SuitDNA.suitsPerDept])
        quotaLabel = DirectLabel(parent = panel, pos = (0.0, 0.0, -0.215), relief = None, state = DISABLED, text = TTLocalizer.SuitPageQuota % (count, quota), text_scale = 0.065000000000000002, text_fg = (0, 0, 0, 1), text_font = ToontownGlobals.getSuitFont())
        panel.quotaLabel = quotaLabel

    
    def addSuitHead(self, panel, suitName):
        panelIndex = self.panels.index(panel)
        shadow = panel.attachNewNode('shadow')
        shadowModel = self.shadowModels[panelIndex]
        shadowModel.copyTo(shadow)
        coords = SHADOW_SCALE_POS[panelIndex]
        shadow.setScale(coords[0])
        shadow.setPos(coords[1], coords[2], coords[3])
        panel.shadow = shadow
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit(suitName)
        suit = Suit.Suit()
        suit.setDNA(suitDNA)
        headParts = suit.getHeadParts()
        head = panel.attachNewNode('head')
        for part in headParts:
            copyPart = part.copyTo(head)
            copyPart.setDepthTest(1)
            copyPart.setDepthWrite(1)
        
        suit.delete()
        suit = None
        p1 = Point3()
        p2 = Point3()
        head.calcTightBounds(p1, p2)
        d = p2 - p1
        biggest = max(d[0], d[2])
        column = panelIndex % SuitDNA.suitsPerDept
        s = (0.20000000000000001 + column / 100.0) / biggest
        pos = -0.14000000000000001 + (SuitDNA.suitsPerDept - column - 1) / 135.0
        head.setPosHprScale(0, 10.0, pos, 180, 0, 0, s, s, s)
        panel.head = head

    
    def addCogRadarLabel(self, panel):
        cogRadarLabel = DirectLabel(parent = panel, pos = (0.0, 0.0, -0.215), relief = None, state = DISABLED, text = '', text_scale = 0.050000000000000003, text_fg = (0, 0, 0, 1), text_font = ToontownGlobals.getSuitFont())
        panel.cogRadarLabel = cogRadarLabel

    
    def addBuildingRadarLabel(self, button):
        gui = loader.loadModelOnce('phase_3.5/models/gui/suit_detail_panel')
        zPos = BUILDING_RADAR_POS[self.radarButtons.index(button)]
        buildingRadarLabel = DirectLabel(parent = button, relief = None, pos = (0.22500000000000001, 0.0, zPos), state = DISABLED, image = gui.find('**/avatar_panel'), image_hpr = (0, 0, 90), image_scale = (0.050000000000000003, 1, 0.10000000000000001), image_pos = (0, 0, 0.014999999999999999), text = TTLocalizer.SuitPageBuildingRadarP % '0', text_scale = 0.050000000000000003, text_fg = (1, 0, 0, 1), text_font = ToontownGlobals.getSuitFont())
        gui.removeNode()
        button.buildingRadarLabel = buildingRadarLabel

    
    def resetPanel(self, dept, type):
        panel = self.panels[dept * SuitDNA.suitsPerDept + type]
        panel['text'] = TTLocalizer.SuitPageMystery
        if panel.cogRadarLabel:
            panel.cogRadarLabel.hide()
        
        if panel.quotaLabel:
            panel.quotaLabel.hide()
        
        if panel.head:
            panel.head.hide()
        
        if panel.shadow:
            panel.shadow.hide()
        
        color = PANEL_COLORS[dept]
        panel['image_color'] = color
        for button in self.radarButtons:
            if button.buildingRadarLabel:
                button.buildingRadarLabel.hide()
            
        

    
    def setPanelStatus(self, panel, status):
        index = self.panels.index(panel)
        if status == COG_UNSEEN:
            panel['text'] = TTLocalizer.SuitPageMystery
        elif status == COG_BATTLED:
            suitName = SuitDNA.suitHeadTypes[index]
            suitFullName = SuitBattleGlobals.SuitAttributes[suitName]['name']
            panel['text'] = suitFullName
            if panel.quotaLabel:
                panel.quotaLabel.show()
            else:
                self.addQuotaLabel(panel)
            if panel.head and panel.shadow:
                panel.head.show()
                panel.shadow.show()
            else:
                self.addSuitHead(panel, suitName)
        elif status == COG_DEFEATED:
            count = str(base.localAvatar.cogCounts[index])
            if base.localAvatar.cogs[index] < COG_COMPLETE1:
                quota = str(COG_QUOTAS[0][index % SuitDNA.suitsPerDept])
            else:
                quota = str(COG_QUOTAS[1][index % SuitDNA.suitsPerDept])
            panel.quotaLabel['text'] = TTLocalizer.SuitPageQuota % (count, quota)
        elif status == COG_COMPLETE1:
            panel['image_color'] = PANEL_COLORS_COMPLETE1[index / SuitDNA.suitsPerDept]
        elif status == COG_COMPLETE2:
            panel['image_color'] = PANEL_COLORS_COMPLETE2[index / SuitDNA.suitsPerDept]
        

    
    def updateAllCogs(self, status):
        for index in range(0, len(base.localAvatar.cogs)):
            base.localAvatar.cogs[index] = status
        
        self.updatePage()

    
    def updatePage(self):
        index = 0
        cogs = base.localAvatar.cogs
        for dept in range(0, len(SuitDNA.suitDepts)):
            for type in range(0, SuitDNA.suitsPerDept):
                self.updateCogStatus(dept, type, cogs[index])
                index += 1
            
        
        self.updateCogRadarButtons(base.localAvatar.cogRadar)
        self.updateBuildingRadarButtons(base.localAvatar.buildingRadar)

    
    def updateCogStatus(self, dept, type, status):
        if dept < 0 or dept > len(SuitDNA.suitDepts):
            print 'ucs: bad cog dept: ', dept
        elif type < 0 or type > SuitDNA.suitsPerDept:
            print 'ucs: bad cog type: ', type
        elif status < COG_UNSEEN or status > COG_COMPLETE2:
            print 'ucs: bad status: ', status
        else:
            self.resetPanel(dept, type)
            panel = self.panels[dept * SuitDNA.suitsPerDept + type]
            if status == COG_UNSEEN:
                self.setPanelStatus(panel, COG_UNSEEN)
            elif status == COG_BATTLED:
                self.setPanelStatus(panel, COG_BATTLED)
            elif status == COG_DEFEATED:
                self.setPanelStatus(panel, COG_BATTLED)
                self.setPanelStatus(panel, COG_DEFEATED)
            elif status == COG_COMPLETE1:
                self.setPanelStatus(panel, COG_BATTLED)
                self.setPanelStatus(panel, COG_DEFEATED)
                self.setPanelStatus(panel, COG_COMPLETE1)
            elif status == COG_COMPLETE2:
                self.setPanelStatus(panel, COG_BATTLED)
                self.setPanelStatus(panel, COG_DEFEATED)
                self.setPanelStatus(panel, COG_COMPLETE2)
            

    
    def updateCogRadarButtons(self, radars):
        for index in range(0, len(radars)):
            if radars[index] == 1:
                self.radarButtons[index]['state'] = NORMAL
            
        

    
    def updateCogRadar(self, deptNum, panels, timeout = 0):
        taskMgr.remove('suitListResponseTimeout-later')
        if not timeout and hasattr(base.cr, 'currSuitPlanner') and base.cr.currSuitPlanner != None:
            cogList = base.cr.currSuitPlanner.suitList
        else:
            cogList = []
        for panel in panels:
            panel.count = 0
        
        for cog in cogList:
            self.panels[cog].count += 1
        
        for panel in panels:
            panel.cogRadarLabel['text'] = TTLocalizer.SuitPageCogRadar % panel.count
            if self.radarOn[deptNum]:
                panel.quotaLabel.hide()
                
                def showLabel(label):
                    label.show()

                taskMgr.doMethodLater(RADAR_DELAY * panels.index(panel), showLabel, 'showCogRadarLater', extraArgs = (panel.cogRadarLabel,))
                
                def activateButton(s = self, index = deptNum):
                    self.radarButtons[index]['state'] = NORMAL
                    return Task.done

                if not (self.radarButtons[deptNum].building):
                    taskMgr.doMethodLater(RADAR_DELAY * len(panels), activateButton, 'activateButtonLater')
                
            else:
                panel.cogRadarLabel.hide()
                panel.quotaLabel.show()
        

    
    def updateBuildingRadarButtons(self, radars):
        for index in range(0, len(radars)):
            if radars[index] == 1:
                self.radarButtons[index].building = 1
            
        

    
    def updateBuildingRadar(self, deptNum, timeout = 0):
        taskMgr.remove('buildingListResponseTimeout-later')
        if not timeout and hasattr(base.cr, 'currSuitPlanner') and base.cr.currSuitPlanner != None:
            buildingList = base.cr.currSuitPlanner.buildingList
        else:
            buildingList = [
                0,
                0,
                0,
                0]
        button = self.radarButtons[deptNum]
        if button.building:
            if not (button.buildingRadarLabel):
                self.addBuildingRadarLabel(button)
            
            if self.radarOn[deptNum]:
                num = buildingList[deptNum]
                if num == 1:
                    button.buildingRadarLabel['text'] = TTLocalizer.SuitPageBuildingRadarS % num
                else:
                    button.buildingRadarLabel['text'] = TTLocalizer.SuitPageBuildingRadarP % num
                
                def showLabel(button):
                    button.buildingRadarLabel.show()
                    button['state'] = NORMAL

                taskMgr.doMethodLater(RADAR_DELAY * SuitDNA.suitsPerDept, showLabel, 'showBuildingRadarLater', extraArgs = (button,))
            else:
                button.buildingRadarLabel.hide()
        


