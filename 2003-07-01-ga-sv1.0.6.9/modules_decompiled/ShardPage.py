# File: S (Python 2.2)

from ShowBaseGlobal import *
import ShtikerPage
from DirectGui import *
import Localizer
import PotentialShard
import DirectNotifyGlobal

class ShardPage(ShtikerPage.ShtikerPage):
    notify = DirectNotifyGlobal.directNotify.newCategory('ShardPage')
    
    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.shardButtons = { }
        self.textRolloverColor = Vec4(1, 1, 0, 1)
        self.textDownColor = Vec4(0.5, 0.90000000000000002, 1, 1)
        self.textDisabledColor = Vec4(0.40000000000000002, 0.80000000000000004, 0.40000000000000002, 1)
        self.ShardInfoUpdateInterval = 5.0

    
    def load(self):
        main_text_scale = 0.059999999999999998
        title_text_scale = 0.12
        self.title = DirectLabel(parent = self, relief = None, text = Localizer.ShardPageTitle, text_scale = title_text_scale, textMayChange = 0, pos = (0, 0, 0.59999999999999998))
        helpText_ycoord = 0.40300000000000002
        self.helpText = DirectLabel(parent = self, relief = None, text = '', text_scale = main_text_scale, text_wordwrap = 12, text_align = TextNode.ALeft, textMayChange = 1, pos = (0.058000000000000003, 0, helpText_ycoord))
        shardPop_ycoord = helpText_ycoord - 0.52300000000000002
        self.shardPopulationText = DirectLabel(parent = self, relief = None, text = Localizer.ShardPagePopulationShard % ('', 1), text_scale = main_text_scale, text_wordwrap = 8, textMayChange = 1, text_align = TextNode.ACenter, pos = (0.38, 0, shardPop_ycoord))
        totalPop_ycoord = shardPop_ycoord - 0.26000000000000001
        self.totalPopulationText = DirectLabel(parent = self, relief = None, text = Localizer.ShardPagePopulationTotal % 1, text_scale = main_text_scale, text_wordwrap = 8, textMayChange = 1, text_align = TextNode.ACenter, pos = (0.38, 0, totalPop_ycoord))
        if config.GetBool('show-total-population', 0):
            self.totalPopulationText.show()
        else:
            self.totalPopulationText.hide()
        gui = loader.loadModelOnce('phase_3.5/models/gui/friendslist_gui')
        self.listXorigin = -0.02
        self.listFrameSizeX = 0.67000000000000004
        self.listZorigin = -0.95999999999999996
        self.listFrameSizeZ = 1.04
        self.arrowButtonScale = 1.3
        self.itemFrameXorigin = -0.23699999999999999
        self.itemFrameZorigin = 0.36499999999999999
        self.buttonXstart = self.itemFrameXorigin + 0.29299999999999998
        self.scrollList = DirectScrolledList(parent = self, relief = None, pos = (-0.5, 0, 0), incButton_image = (gui.find('**/FndsLst_ScrollUp'), gui.find('**/FndsLst_ScrollDN'), gui.find('**/FndsLst_ScrollUp_Rllvr'), gui.find('**/FndsLst_ScrollUp')), incButton_relief = None, incButton_scale = (self.arrowButtonScale, self.arrowButtonScale, -(self.arrowButtonScale)), incButton_pos = (self.buttonXstart, 0, self.itemFrameZorigin - 0.999), incButton_image3_color = Vec4(1, 1, 1, 0.20000000000000001), decButton_image = (gui.find('**/FndsLst_ScrollUp'), gui.find('**/FndsLst_ScrollDN'), gui.find('**/FndsLst_ScrollUp_Rllvr'), gui.find('**/FndsLst_ScrollUp')), decButton_relief = None, decButton_scale = (self.arrowButtonScale, self.arrowButtonScale, self.arrowButtonScale), decButton_pos = (self.buttonXstart, 0, self.itemFrameZorigin + 0.22700000000000001), decButton_image3_color = Vec4(1, 1, 1, 0.20000000000000001), itemFrame_pos = (self.itemFrameXorigin, 0, self.itemFrameZorigin), itemFrame_scale = 1.0, itemFrame_relief = SUNKEN, itemFrame_frameSize = (self.listXorigin, self.listXorigin + self.listFrameSizeX, self.listZorigin, self.listZorigin + self.listFrameSizeZ), itemFrame_frameColor = (0.84999999999999998, 0.94999999999999996, 1, 1), itemFrame_borderWidth = (0.01, 0.01), numItemsVisible = 15, forceHeight = 0.065000000000000002, items = [])
        scrollTitle = DirectFrame(parent = self.scrollList, text = Localizer.ShardPageScrollTitle, text_scale = main_text_scale, text_align = TextNode.ACenter, relief = None, pos = (self.buttonXstart, 0, self.itemFrameZorigin + 0.127))
        gui.removeNode()

    
    def unload(self):
        del self.title
        del self.scrollList
        del self.shardButtons
        taskMgr.remove('ShardPageUpdateTask-doLater')
        ShtikerPage.ShtikerPage.unload(self)

    
    def askForShardInfoUpdate(self, task = None):
        toonbase.tcr.sendGetShardListMsg()
        taskMgr.doMethodLater(self.ShardInfoUpdateInterval, self.askForShardInfoUpdate, 'ShardPageUpdateTask-doLater')
        return Task.done

    
    def getShardButtonText(self, shardName, shardPop):
        return shardName + '\nPop: ' + str(shardPop)

    
    def makeShardButton(self, shardTuple):
        (shardId, shardName, shardPop) = shardTuple
        shardButtonParent = DirectFrame()
        shardButtonL = DirectButton(parent = shardButtonParent, relief = None, text = shardName, text_scale = 0.059999999999999998, text_align = TextNode.ALeft, text1_bg = self.textDownColor, text2_bg = self.textRolloverColor, text3_fg = self.textDisabledColor, textMayChange = 1, command = self.choseShard, extraArgs = [
            shardId])
        shardButtonR = DirectButton(parent = shardButtonParent, relief = None, text = str(shardPop), text_scale = 0.059999999999999998, text_align = TextNode.ALeft, text1_bg = self.textDownColor, text2_bg = self.textRolloverColor, text3_fg = self.textDisabledColor, textMayChange = 1, pos = (0.5, 0, 0), command = self.choseShard, extraArgs = [
            shardId])
        return (shardButtonL, shardButtonR, shardButtonParent)

    
    def updateScrollList(self):
        curShardTuples = toonbase.tcr.listAvailableShards()
        curShardIds = []
        for shardTuple in curShardTuples:
            curShardIds.append(shardTuple[0])
            shardId = shardTuple[0]
            if shardId not in self.shardButtons.keys():
                shardButtons = self.makeShardButton(shardTuple)
                shardButtons[2].itemID = self.scrollList.addItem(shardButtons[2])
                self.shardButtons[shardId] = shardButtons
            
        
        for shardId in self.shardButtons.keys():
            if shardId not in curShardIds:
                shardButton = self.shardButtons[shardId][2]
                self.scrollList.removeItem(shardButton)
                shardButton.destroy()
                del self.shardButtons[shardId]
            
        
        currentShardId = toonbase.localToon.defaultShard
        totalPop = 0
        for (shardId, shardButtons) in self.shardButtons.items():
            shardPop = 0
            shardName = 'X'
            for shardTuple in curShardTuples:
                if shardId == shardTuple[0]:
                    shardName = shardTuple[1]
                    shardPop = shardTuple[2]
                
            
            if shardName == 'X':
                print "ShardPage warning: couldn't find shardId in current list of avail shards!"
            
            self.shardButtons[shardId][0]['text'] = shardName
            self.shardButtons[shardId][1]['text'] = str(shardPop)
            if currentShardId == shardId:
                shardButtons[0]['state'] = DISABLED
                shardButtons[1]['state'] = DISABLED
                if self.book.safeMode:
                    helpTextStr = Localizer.ShardPageHelpDisabled
                else:
                    helpTextStr = Localizer.ShardPageHelp
                self.helpText['text'] = helpTextStr % shardName
                self.shardPopulationText['text'] = Localizer.ShardPagePopulationShard % (shardName, shardPop)
                self.currentButtonID = shardButtons[2].itemID
            elif self.book.safeMode:
                shardButtons[0]['state'] = DISABLED
                shardButtons[1]['state'] = DISABLED
            else:
                shardButtons[0]['state'] = NORMAL
                shardButtons[1]['state'] = NORMAL
            totalPop += shardPop
        
        self.totalPopulationText['text'] = Localizer.ShardPagePopulationTotal % totalPop
        del curShardIds
        del curShardTuples

    
    def enter(self):
        self.askForShardInfoUpdate()
        self.updateScrollList()
        self.scrollList.scrollToItemID(self.currentButtonID, centered = 1)
        ShtikerPage.ShtikerPage.enter(self)
        self.accept('shardInfoUpdated', self.updateScrollList)
        return None

    
    def exit(self):
        self.ignore('shardInfoUpdated')
        taskMgr.remove('ShardPageUpdateTask-doLater')
        ShtikerPage.ShtikerPage.exit(self)
        return None

    
    def choseShard(self, shardId):
        if shardId == toonbase.localToon.defaultShard:
            return None
        else:
            
            try:
                place = toonbase.tcr.playGame.getPlace()
            except:
                
                try:
                    place = toonbase.tcr.playGame.hood.loader.place
                except:
                    place = toonbase.tcr.playGame.hood.place


            place.requestTeleport(toonbase.localToon.defaultZone, toonbase.localToon.defaultZone, shardId, -1)
        return None


