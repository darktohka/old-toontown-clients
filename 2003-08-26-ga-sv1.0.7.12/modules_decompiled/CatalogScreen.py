# File: C (Python 2.2)

from DirectGui import *
from DirectScrolledList import *
import ToontownGlobals
import ToontownDialog
import CatalogItem
import Localizer
import CatalogItemPanel
import CatalogItemTypes
import Actor
import whrandom
NUM_CATALOG_ROWS = 3
NUM_CATALOG_COLS = 2
CatalogPanelCenters = [
    [
        Point3(-0.94999999999999996, 0, 0.91000000000000003),
        Point3(-0.27500000000000002, 0, 0.91000000000000003)],
    [
        Point3(-0.94999999999999996, 0, 0.27500000000000002),
        Point3(-0.27500000000000002, 0, 0.27500000000000002)],
    [
        Point3(-0.94999999999999996, 0, -0.40000000000000002),
        Point3(-0.27500000000000002, 0, -0.40000000000000002)]]
CatalogPanelColors = {
    CatalogItemTypes.FURNITURE_ITEM: Vec4(0.73299999999999998, 0.78000000000000003, 0.93300000000000005, 1.0),
    CatalogItemTypes.CHAT_ITEM: Vec4(0.92200000000000004, 0.92200000000000004, 0.753, 1.0),
    CatalogItemTypes.CLOTHING_ITEM: Vec4(0.91800000000000004, 0.68999999999999995, 0.68999999999999995, 1.0),
    CatalogItemTypes.EMOTE_ITEM: Vec4(0.92200000000000004, 0.92200000000000004, 0.753, 1.0),
    CatalogItemTypes.WALLPAPER_ITEM: Vec4(0.749, 0.98399999999999999, 0.60799999999999998, 1.0),
    CatalogItemTypes.WINDOW_ITEM: Vec4(0.82699999999999996, 0.91000000000000003, 0.65900000000000003, 1.0) }

class CatalogScreen(DirectFrame):
    
    def __init__(self, parent = aspect2d, **kw):
        guiItems = loader.loadModel('phase_5.5/models/gui/catalog_gui')
        background = guiItems.find('**/catalog_background')
        optiondefs = (('scale', 0.66700000000000004, None), ('pos', (0, 1, 0.025000000000000001), None), ('phone', None, None), ('doneEvent', None, None), ('image', background, None), ('relief', None, None))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent)
        self.load(guiItems)
        self.initialiseoptions(CatalogScreen)
        self.enableBackorderCatalogButton()
        self.setMaxPageIndex(self.numNewPages)
        self.setPageIndex(-1)
        self.showPageItems()
        self.hide()
        self.clarabelleChatNP = None
        self.clarabelleChatBalloon = None

    
    def show(self):
        self.accept('CatalogItemPurchaseRequest', self._CatalogScreen__handlePurchaseRequest)
        render.hide()
        DirectFrame.show(self)
        
        def clarabelleGreeting(task):
            self.setClarabelleChat(Localizer.CatalogGreeting)

        
        def clarabelleHelpText1(task):
            self.setClarabelleChat(Localizer.CatalogHelpText1)

        taskMgr.doMethodLater(1.0, clarabelleGreeting, 'clarabelleGreeting')
        taskMgr.doMethodLater(12.0, clarabelleHelpText1, 'clarabelleHelpText1')

    
    def hide(self):
        self.ignore('CatalogItemPurchaseRequest')
        render.show()
        DirectFrame.hide(self)

    
    def setNumNewPages(self, numNewPages):
        self.numNewPages = numNewPages

    
    def setNumBackPages(self, numBackPages):
        self.numBackPages = numBackPages

    
    def setPageIndex(self, index):
        self.pageIndex = index

    
    def setMaxPageIndex(self, numPages):
        self.maxPageIndex = max(numPages - 1, -1)

    
    def enableBackorderCatalogButton(self):
        self.backCatalogButton['state'] = NORMAL
        self.newCatalogButton['state'] = DISABLED

    
    def enableNewCatalogButton(self):
        self.backCatalogButton['state'] = DISABLED
        self.newCatalogButton['state'] = NORMAL

    
    def showNewItems(self, index = None):
        taskMgr.remove('clarabelleHelpText1')
        self.viewing = 'New'
        self.enableBackorderCatalogButton()
        self.setMaxPageIndex(self.numNewPages)
        if self.numNewPages == 0:
            self.setPageIndex(-1)
        elif index is not None:
            self.setPageIndex(index)
        else:
            self.setPageIndex(0)
        self.showPageItems()

    
    def showBackorderItems(self):
        taskMgr.remove('clarabelleHelpText1')
        self.viewing = 'Backorder'
        self.enableNewCatalogButton()
        self.setMaxPageIndex(self.numBackPages)
        if self.numBackPages == 0:
            self.setPageIndex(-1)
        else:
            self.setPageIndex(0)
        self.showPageItems()

    
    def showNextPage(self):
        taskMgr.remove('clarabelleHelpText1')
        self.pageIndex = self.pageIndex + 1
        if self.viewing == 'New' and self.pageIndex > self.maxPageIndex and self.numBackPages > 0:
            self.showBackorderItems()
        else:
            self.pageIndex = min(self.pageIndex, self.maxPageIndex)
            self.showPageItems()

    
    def showBackPage(self):
        taskMgr.remove('clarabelleHelpText1')
        self.pageIndex = self.pageIndex - 1
        if self.viewing == 'Backorder' and self.pageIndex < 0 and self.numNewPages > 0:
            self.showNewItems(self.numNewPages - 1)
        else:
            self.pageIndex = max(self.pageIndex, -1)
            self.showPageItems()

    
    def showPageItems(self):
        self.hidePages()
        if self.pageIndex < 0:
            self.closeCover()
        elif self.pageIndex == 0:
            self.openCover()
        
        if self.viewing == 'New':
            page = self.pageList[self.pageIndex]
            newOrBack = 0
        else:
            page = self.backPageList[self.pageIndex]
            newOrBack = 1
        page.show()
        for panel in self.panelDict[page.id()]:
            panel.load()
            if panel.ival:
                panel.ival.loop()
            
            self.visiblePanels.append(panel)
        
        pIndex = 0
        import whrandom
        whrandom.seed(toonbase.localToon.catalogScheduleCurrentWeek * 10 % 256, self.pageIndex * 10 % 256, newOrBack * 255)
        for i in range(NUM_CATALOG_ROWS):
            for j in range(NUM_CATALOG_COLS):
                if pIndex < len(self.visiblePanels):
                    type = self.visiblePanels[pIndex]['item'].getTypeCode()
                    self.squares[i][j].setColor(CatalogPanelColors.values()[whrandom.randint(0, len(CatalogPanelColors) - 1)])
                    cs = 0.69999999999999996 + 0.29999999999999999 * whrandom.random()
                    self.squares[i][j].setColorScale(0.69999999999999996 + 0.29999999999999999 * whrandom.random(), 0.69999999999999996 + 0.29999999999999999 * whrandom.random(), 0.69999999999999996 + 0.29999999999999999 * whrandom.random(), 1)
                else:
                    self.squares[i][j].setColor(CatalogPanelColors[CatalogItemTypes.CHAT_ITEM])
                    self.squares[i][j].clearColorScale()
                pIndex += 1
            
        
        self.pageLabel['text'] = self.viewing + ' - %d' % (self.pageIndex + 1)
        if self.pageIndex < self.maxPageIndex:
            self.nextPageButton.show()
        elif self.viewing == 'Backorder' and self.viewing == 'New' and self.numBackPages == 0:
            self.nextPageButton.hide()
        

    
    def hidePages(self):
        for page in self.pageList:
            page.hide()
        
        for page in self.backPageList:
            page.hide()
        
        for panel in self.visiblePanels:
            if panel.ival:
                panel.ival.finish()
            
        
        self.visiblePanels = []

    
    def openCover(self):
        self.cover.hide()
        self.rings.show()
        self.hideDummyTabs()
        self.backPageButton.show()
        self.pageLabel.show()

    
    def closeCover(self):
        self.cover.show()
        self.rings.hide()
        self.showDummyTabs()
        self.nextPageButton.show()
        self.backPageButton.hide()
        self.pageLabel.hide()
        self.hidePages()

    
    def showDummyTabs(self):
        if self.numNewPages > 0:
            self.newCatalogButton2.show()
        
        if self.numBackPages > 0:
            self.backCatalogButton2.show()
        
        self.newCatalogButton.hide()
        self.backCatalogButton.hide()

    
    def hideDummyTabs(self):
        self.newCatalogButton2.hide()
        self.backCatalogButton2.hide()
        if self.numNewPages > 0:
            self.newCatalogButton.show()
        
        if self.numBackPages > 0:
            self.backCatalogButton.show()
        

    
    def packPages(self, panelList, pageList, prefix):
        i = 0
        j = 0
        numPages = 0
        pageName = prefix + '_page%d' % numPages
        for item in panelList:
            if i == 0 and j == 0:
                numPages += 1
                pageName = prefix + '_page%d' % numPages
                page = self.base.attachNewNode(pageName)
                pageList.append(page)
            
            item.reparentTo(page)
            item.setPos(CatalogPanelCenters[i][j])
            itemList = self.panelDict.get(page.id(), [])
            itemList.append(item)
            self.panelDict[page.id()] = itemList
            j += 1
            if j == NUM_CATALOG_COLS:
                j = 0
                i += 1
            
            if i == NUM_CATALOG_ROWS:
                i = 0
            
        
        return numPages

    
    def load(self, guiItems):
        self.pageIndex = -1
        self.maxPageIndex = 0
        self.numNewPages = 0
        self.numBackPages = 5
        self.viewing = 'New'
        self.panelList = []
        self.backPanelList = []
        self.pageList = []
        self.backPageList = []
        self.panelDict = { }
        self.visiblePanels = []
        self.responseDialog = None
        base = guiItems.find('**/catalog_base')
        self.base = DirectLabel(self, relief = None, image = base)
        newDown = guiItems.find('**/new1')
        newUp = guiItems.find('**/new2')
        backDown = guiItems.find('**/previous2')
        backUp = guiItems.find('**/previous1')
        self.backCatalogButton = DirectButton(self.base, relief = None, image = [
            backDown,
            backDown,
            backDown,
            backUp], pressEffect = 0, command = self.showBackorderItems, text = Localizer.CatalogBackorder, text_font = ToontownGlobals.getSignFont(), text_pos = (0.35499999999999998, 0.13200000000000001), text3_pos = (0.35499999999999998, 0.112), text_scale = 0.065000000000000002, text_fg = (0.39200000000000002, 0.54900000000000004, 0.627, 1.0), text2_fg = (0.39200000000000002, 0.34899999999999998, 0.42699999999999999, 1.0))
        self.backCatalogButton.hide()
        self.newCatalogButton = DirectButton(self.base, relief = None, image = [
            newDown,
            newDown,
            newDown,
            newUp], pressEffect = 0, command = self.showNewItems, text = Localizer.CatalogNew, text_font = ToontownGlobals.getSignFont(), text_pos = (-0.48999999999999999, 0.13), text3_pos = (-0.48999999999999999, 0.10000000000000001), text_scale = 0.080000000000000002, text_fg = (0.35299999999999998, 0.627, 0.627, 1.0), text2_fg = (0.35299999999999998, 0.42699999999999999, 0.42699999999999999, 1.0))
        self.newCatalogButton.hide()
        self.backCatalogButton2 = DirectButton(self.base, relief = None, image = backDown, pressEffect = 0, command = self.showBackorderItems, text = Localizer.CatalogBackorder, text_font = ToontownGlobals.getSignFont(), text_pos = (0.35499999999999998, 0.13200000000000001), text_scale = 0.065000000000000002, text_fg = (0.39200000000000002, 0.54900000000000004, 0.627, 1.0), text2_fg = (0.39200000000000002, 0.34899999999999998, 0.42699999999999999, 1.0))
        self.backCatalogButton2.hide()
        self.newCatalogButton2 = DirectButton(self.base, relief = None, image = newDown, pressEffect = 0, command = self.showNewItems, text = Localizer.CatalogNew, text_font = ToontownGlobals.getSignFont(), text_pos = (-0.48999999999999999, 0.13), text_scale = 0.080000000000000002, text_fg = (0.35299999999999998, 0.627, 0.627, 1.0), text2_fg = (0.35299999999999998, 0.42699999999999999, 0.42699999999999999, 1.0))
        self.newCatalogButton2.hide()
        for i in range(4):
            self.backCatalogButton.component('text%d' % i).setR(-90)
            self.newCatalogButton.component('text%d' % i).setR(-90)
            self.backCatalogButton2.component('text%d' % i).setR(-90)
            self.newCatalogButton2.component('text%d' % i).setR(-90)
        
        self.squares = [
            [],
            [],
            [],
            []]
        for i in range(NUM_CATALOG_ROWS):
            for j in range(NUM_CATALOG_COLS):
                square = guiItems.find('**/square%d%db' % (i + 1, j + 1))
                label = DirectLabel(self.base, image = square, relief = None, state = 'normal')
                self.squares[i].append(label)
            
        
        
        def priceSort(a, b, type):
            priceA = a.getPrice(type)
            priceB = b.getPrice(type)
            if priceA < priceB:
                return -1
            elif priceA > priceB:
                return 1
            else:
                return 0

        itemList = toonbase.localToon.monthlyCatalog + toonbase.localToon.weeklyCatalog
        itemList.sort(lambda a, b: priceSort(a, b, CatalogItem.CatalogTypeWeekly))
        itemList.reverse()
        for item in itemList:
            self.panelList.append(CatalogItemPanel.CatalogItemPanel(parent = hidden, item = item, type = CatalogItem.CatalogTypeWeekly))
        
        itemList = toonbase.localToon.backCatalog
        itemList.sort(lambda a, b: priceSort(a, b, CatalogItem.CatalogTypeBackorder))
        itemList.reverse()
        for item in itemList:
            self.backPanelList.append(CatalogItemPanel.CatalogItemPanel(parent = hidden, item = item, type = CatalogItem.CatalogTypeBackorder))
        
        numPages = self.packPages(self.panelList, self.pageList, 'new')
        self.setNumNewPages(numPages)
        numPages = self.packPages(self.backPanelList, self.backPageList, 'back')
        self.setNumBackPages(numPages)
        cover = guiItems.find('**/cover')
        cover.find('**/cover_picture1').reparentTo(cover)
        cover.find('**/cover_bottom').reparentTo(cover)
        guiItems.find('**/square12b2').reparentTo(cover)
        cover.find('**/clarabelle_text').reparentTo(cover)
        cover.find('**/blue_circle').reparentTo(cover)
        cover.find('**/clarabelle').reparentTo(cover)
        cover.find('**/circle_green').reparentTo(cover)
        self.cover = DirectLabel(self.base, relief = None, geom = cover)
        self.catalogNumber = DirectLabel(self.cover, relief = None, scale = 0.20000000000000001, pos = (-0.22, 0, -0.33000000000000002), text = '#%d' % toonbase.localToon.catalogScheduleCurrentWeek, text_fg = (0.94999999999999996, 0.94999999999999996, 0, 1), text_shadow = (0, 0, 0, 1), text_font = ToontownGlobals.getInterfaceFont())
        self.rings = DirectLabel(self.base, relief = None, geom = guiItems.find('**/rings'))
        self.rings.hide()
        self.clarabelleFrame = DirectLabel(self, relief = None, image = guiItems.find('**/clarabelle_frame'))
        hangupGui = guiItems.find('**/hangup')
        hangupRolloverGui = guiItems.find('**/hangup_rollover')
        self.hangup = DirectButton(self, relief = None, pos = (1.78, 0, -1.3), image = [
            hangupGui,
            hangupRolloverGui,
            hangupRolloverGui,
            hangupGui], text = [
            '',
            Localizer.CatalogHangUp,
            Localizer.CatalogHangUp], text_fg = Vec4(1), text_scale = 0.070000000000000007, text_pos = (0.0, 0.14000000000000001), command = self.hangUp)
        self.beanBank = DirectLabel(self, relief = None, image = guiItems.find('**/bean_bank'), text = str(toonbase.localToon.getMoney() + toonbase.localToon.getBankMoney()), text_align = TextNode.ARight, text_scale = 0.11, text_fg = (0.94999999999999996, 0.94999999999999996, 0, 1), text_shadow = (0, 0, 0, 1), text_pos = (0.75, -0.81000000000000005), text_font = ToontownGlobals.getSignFont())
        nextUp = guiItems.find('**/arrow_up')
        nextRollover = guiItems.find('**/arrow_Rollover')
        nextDown = guiItems.find('**/arrow_Down')
        prevUp = guiItems.find('**/arrowUp')
        prevDown = guiItems.find('**/arrowDown1')
        prevRollover = guiItems.find('**/arrowRollover')
        self.nextPageButton = DirectButton(self, relief = None, pos = (-0.10000000000000001, 0, -0.90000000000000002), image = [
            nextUp,
            nextDown,
            nextRollover,
            nextUp], image_color = (0.90000000000000002, 0.90000000000000002, 0.90000000000000002, 1), image2_color = (1, 1, 1, 1), command = self.showNextPage)
        self.backPageButton = DirectButton(self, relief = None, pos = (-0.10000000000000001, 0, -0.90000000000000002), image = [
            prevUp,
            prevDown,
            prevRollover,
            prevUp], image_color = (0.90000000000000002, 0.90000000000000002, 0.90000000000000002, 1), image2_color = (1, 1, 1, 1), command = self.showBackPage)
        self.backPageButton.hide()
        self.pageLabel = DirectLabel(self.base, relief = None, pos = (-1.3300000000000001, 0, -0.90000000000000002), scale = 0.059999999999999998, text = Localizer.CatalogPagePrefix, text_fg = (0.94999999999999996, 0.94999999999999996, 0, 1), text_shadow = (0, 0, 0, 1), text_font = ToontownGlobals.getSignFont(), text_align = TextNode.ALeft)
        self.loadClarabelle()

    
    def loadClarabelle(self):
        self.cRender = NodePath('cRender')
        self.cCamera = self.cRender.attachNewNode('cCamera')
        self.cCamNode = Camera('cCam')
        self.cLens = PerspectiveLens()
        self.cLens.setFov(40, 40)
        self.cLens.setNear(0.10000000000000001)
        self.cLens.setFar(100.0)
        self.cCamNode.setLens(self.cLens)
        self.cCamNode.setScene(self.cRender)
        self.cCam = self.cCamera.attachNewNode(self.cCamNode)
        chan = base.win.getChannel(0)
        self.cLayer = chan.makeLayer(1)
        self.layerIndex = 1
        self.cDr = self.cLayer.makeDisplayRegion(0.57999999999999996, 0.81999999999999995, 0.53000000000000003, 0.84999999999999998)
        self.cDr.setClearDepthActive(1)
        self.cDr.setClearColorActive(1)
        self.cDr.setClearColor(Vec4(0.29999999999999999, 0.29999999999999999, 0.29999999999999999, 1))
        self.cDr.setCamera(self.cCam)
        self.clarabelle = Actor.Actor('phase_5.5/models/char/Clarabelle-zero', {
            'listen': 'phase_5.5/models/char/Clarabelle-listens' })
        self.clarabelle.loop('listen')
        self.clarabelle.find('**/eyes').setBin('fixed', 0)
        self.clarabelle.find('**/pupilL').setBin('fixed', 1)
        self.clarabelle.find('**/pupilR').setBin('fixed', 1)
        self.clarabelle.find('**/glassL').setBin('fixed', 2)
        self.clarabelle.find('**/glassR').setBin('fixed', 2)
        switchboard = loader.loadModel('phase_5.5/models/estate/switchboard')
        switchboard.reparentTo(self.clarabelle)
        switchboard.setPos(0, -2, 0)
        self.clarabelle.reparentTo(self.cRender)
        self.clarabelle.setPosHprScale(-0.56000000000000005, 6.4299999999999997, -3.8100000000000001, 121.61, 0.0, 0.0, 1.0, 1.0, 1.0)
        self.clarabelleFrame.setPosHprScale(-0.040000000000000001, 0.0, 0.17000000000000001, 0.0, 0.0, 0.0, 1.05, 1.0, 0.83999999999999997)

    
    def unload(self):
        taskMgr.remove('clearClarabelleChat')
        taskMgr.remove('postGoodbyeHangUp')
        taskMgr.remove('clarabelleGreeting')
        taskMgr.remove('clarabelleHelpText1')
        taskMgr.remove('clarabelleAskAnythingElse')
        self.hide()
        self.destroy()
        del self.base
        del self.squares
        for panel in self.panelList + self.backPanelList:
            panel.destroy()
        
        del self.panelList
        del self.backPanelList
        del self.cover
        del self.catalogNumber
        del self.rings
        del self.clarabelleFrame
        del self.hangup
        del self.beanBank
        del self.nextPageButton
        del self.backPageButton
        del self.backCatalogButton
        del self.newCatalogButton
        del self.backCatalogButton2
        del self.newCatalogButton2
        del self.pageLabel
        self.unloadClarabelle()
        if self.responseDialog:
            self.responseDialog.cleanup()
            self.responseDialog = None
        

    
    def unloadClarabelle(self):
        chan = base.win.getChannel(0)
        chan.removeLayer(self.layerIndex)
        del self.cRender
        del self.cCamera
        del self.cCamNode
        del self.cLens
        del self.cCam
        del self.cLayer
        del self.cDr
        self.clarabelle.cleanup()
        del self.clarabelle

    
    def hangUp(self):
        self.setClarabelleChat(whrandom.choice(Localizer.CatalogGoodbyeList))
        self.setPageIndex(-1)
        self.showPageItems()
        self.nextPageButton.hide()
        self.backPageButton.hide()
        self.newCatalogButton.hide()
        self.newCatalogButton2.hide()
        self.backCatalogButton.hide()
        self.backCatalogButton2.hide()
        self.hangup.hide()
        taskMgr.remove('clarabelleGreeting')
        taskMgr.remove('clarabelleHelpText1')
        taskMgr.remove('clarabelleAskAnythingElse')
        
        def postGoodbyeHangUp(task):
            messenger.send(self['doneEvent'])
            self.unload()

        taskMgr.doMethodLater(1.5, postGoodbyeHangUp, 'postGoodbyeHangUp')

    
    def update(self):
        self.beanBank['text'] = str(toonbase.localToon.getMoney() + toonbase.localToon.getBankMoney())
        for item in self.panelList + self.backPanelList:
            if type(item) != type(''):
                item.updateBuyButton()
            
        

    
    def _CatalogScreen__handlePurchaseRequest(self, item):
        item.requestPurchase(self['phone'], self._CatalogScreen__handlePurchaseResponse)
        taskMgr.remove('clarabelleAskAnythingElse')

    
    def _CatalogScreen__handlePurchaseResponse(self, retCode, item):
        if retCode == ToontownGlobals.P_UserCancelled:
            return None
        
        self.setClarabelleChat(item.getRequestPurchaseErrorText(retCode))
        
        def askAnythingElse(task):
            self.setClarabelleChat(Localizer.CatalogAnythingElse)

        if retCode >= 0:
            self.update()
            taskMgr.doMethodLater(8, askAnythingElse, 'clarabelleAskAnythingElse')
        

    
    def _CatalogScreen__clearDialog(self, event):
        self.responseDialog.cleanup()
        self.responseDialog = None

    
    def setClarabelleChat(self, str, timeout = 6):
        self.clearClarabelleChat()
        if not (self.clarabelleChatBalloon):
            self.clarabelleChatBalloon = loader.loadModel('phase_3/models/props/chatbox.bam')
        
        self.clarabelleChat = ChatBalloon(self.clarabelleChatBalloon.node())
        chatNode = self.clarabelleChat.generate(str, ToontownGlobals.getInterfaceFont(), 10, Vec4(0, 0, 0, 1), Vec4(1, 1, 1, 1), 0, 0, 0, NodePath(), 0, 0, NodePath())
        self.clarabelleChatNP = self.attachNewNode(chatNode, 1000)
        self.clarabelleChatNP.setScale(0.080000000000000002)
        self.clarabelleChatNP.setPos(0.69999999999999996, 0, 0.59999999999999998)
        if timeout:
            taskMgr.doMethodLater(timeout, self.clearClarabelleChat, 'clearClarabelleChat')
        

    
    def clearClarabelleChat(self, task = None):
        taskMgr.remove('clearClarabelleChat')
        if self.clarabelleChatNP:
            self.clarabelleChatNP.removeNode()
            self.clarabelleChatNP = None
            del self.clarabelleChat
        


