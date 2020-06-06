# File: S (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
import ShtikerPage
from direct.gui.DirectGui import *
from toontown.toonbase import TTLocalizer
from direct.directnotify import DirectNotifyGlobal
from toontown.hood import ZoneUtil
from toontown.toonbase import ToontownGlobals
LOW_POP = 0
MID_POP = 150
HIGH_POP = 300
POP_COLORS = (Vec4(0.0, 1.0, 0.0, 1.0), Vec4(1.0, 1.0, 0.0, 1.0), Vec4(1.0, 0.64000000000000001, 0.0, 1.0))

class ShardPage(ShtikerPage.ShtikerPage):
    notify = DirectNotifyGlobal.directNotify.newCategory('ShardPage')
    
    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.shardButtonMap = { }
        self.shardButtons = []
        self.scrollList = None
        self.textRolloverColor = Vec4(1, 1, 0, 1)
        self.textDownColor = Vec4(0.5, 0.90000000000000002, 1, 1)
        self.textDisabledColor = Vec4(0.40000000000000002, 0.80000000000000004, 0.40000000000000002, 1)
        self.ShardInfoUpdateInterval = 5.0
        self.lowPop = config.GetInt('shard-low-pop', LOW_POP)
        self.midPop = config.GetInt('shard-mid-pop', MID_POP)
        self.highPop = config.GetInt('shard-high-pop', HIGH_POP)

    
    def load(self):
        main_text_scale = 0.059999999999999998
        title_text_scale = 0.12
        self.title = DirectLabel(parent = self, relief = None, text = TTLocalizer.ShardPageTitle, text_scale = title_text_scale, textMayChange = 0, pos = (0, 0, 0.59999999999999998))
        helpText_ycoord = 0.40300000000000002
        self.helpText = DirectLabel(parent = self, relief = None, text = '', text_scale = main_text_scale, text_wordwrap = 12, text_align = TextNode.ALeft, textMayChange = 1, pos = (0.058000000000000003, 0, helpText_ycoord))
        shardPop_ycoord = helpText_ycoord - 0.52300000000000002
        totalPop_ycoord = shardPop_ycoord - 0.26000000000000001
        self.totalPopulationText = DirectLabel(parent = self, relief = None, text = TTLocalizer.ShardPagePopulationTotal % 1, text_scale = main_text_scale, text_wordwrap = 8, textMayChange = 1, text_align = TextNode.ACenter, pos = (0.38, 0, totalPop_ycoord))
        if config.GetBool('show-total-population', 0):
            self.totalPopulationText.show()
        else:
            self.totalPopulationText.hide()
        self.gui = loader.loadModelOnce('phase_3.5/models/gui/friendslist_gui')
        self.listXorigin = -0.02
        self.listFrameSizeX = 0.67000000000000004
        self.listZorigin = -0.95999999999999996
        self.listFrameSizeZ = 1.04
        self.arrowButtonScale = 1.3
        self.itemFrameXorigin = -0.23699999999999999
        self.itemFrameZorigin = 0.36499999999999999
        self.buttonXstart = self.itemFrameXorigin + 0.29299999999999998
        self.regenerateScrollList()
        scrollTitle = DirectFrame(parent = self.scrollList, text = TTLocalizer.ShardPageScrollTitle, text_scale = main_text_scale, text_align = TextNode.ACenter, relief = None, pos = (self.buttonXstart, 0, self.itemFrameZorigin + 0.127))

    
    def unload(self):
        self.gui.removeNode()
        del self.title
        del self.scrollList
        del self.shardButtons
        taskMgr.remove('ShardPageUpdateTask-doLater')
        ShtikerPage.ShtikerPage.unload(self)

    
    def regenerateScrollList(self):
        selectedIndex = 0
        if self.scrollList:
            selectedIndex = self.scrollList.getSelectedIndex()
            for button in self.shardButtons:
                button.detachNode()
            
            self.scrollList.destroy()
            self.scrollList = None
        
        self.scrollList = DirectScrolledList(parent = self, relief = None, pos = (-0.5, 0, 0), incButton_image = (self.gui.find('**/FndsLst_ScrollUp'), self.gui.find('**/FndsLst_ScrollDN'), self.gui.find('**/FndsLst_ScrollUp_Rllvr'), self.gui.find('**/FndsLst_ScrollUp')), incButton_relief = None, incButton_scale = (self.arrowButtonScale, self.arrowButtonScale, -(self.arrowButtonScale)), incButton_pos = (self.buttonXstart, 0, self.itemFrameZorigin - 0.999), incButton_image3_color = Vec4(1, 1, 1, 0.20000000000000001), decButton_image = (self.gui.find('**/FndsLst_ScrollUp'), self.gui.find('**/FndsLst_ScrollDN'), self.gui.find('**/FndsLst_ScrollUp_Rllvr'), self.gui.find('**/FndsLst_ScrollUp')), decButton_relief = None, decButton_scale = (self.arrowButtonScale, self.arrowButtonScale, self.arrowButtonScale), decButton_pos = (self.buttonXstart, 0, self.itemFrameZorigin + 0.22700000000000001), decButton_image3_color = Vec4(1, 1, 1, 0.20000000000000001), itemFrame_pos = (self.itemFrameXorigin, 0, self.itemFrameZorigin), itemFrame_scale = 1.0, itemFrame_relief = SUNKEN, itemFrame_frameSize = (self.listXorigin, self.listXorigin + self.listFrameSizeX, self.listZorigin, self.listZorigin + self.listFrameSizeZ), itemFrame_frameColor = (0.84999999999999998, 0.94999999999999996, 1, 1), itemFrame_borderWidth = (0.01, 0.01), numItemsVisible = 15, forceHeight = 0.065000000000000002, items = self.shardButtons)
        self.scrollList.scrollTo(selectedIndex)

    if not wantOtpServer:
        
        def askForShardInfoUpdate(self, task = None):
            base.cr.sendGetShardListMsg()
            taskMgr.doMethodLater(self.ShardInfoUpdateInterval, self.askForShardInfoUpdate, 'ShardPageUpdateTask-doLater')
            return Task.done

    
    
    def makeShardButton(self, shardId, shardName, shardPop):
        shardButtonParent = DirectFrame()
        shardButtonL = DirectButton(parent = shardButtonParent, relief = None, text = shardName, text_scale = 0.059999999999999998, text_align = TextNode.ALeft, text1_bg = self.textDownColor, text2_bg = self.textRolloverColor, text3_fg = self.textDisabledColor, textMayChange = 0, command = self.choseShard, extraArgs = [
            shardId])
        if base.cr.productName == 'NTT-DMC':
            model = loader.loadModelCopy('phase_3.5/models/gui/matching_game_gui')
            button = model.find('**/minnieCircle')
            shardButtonR = DirectButton(parent = shardButtonParent, relief = None, image = button, image_scale = (0.29999999999999999, 1, 0.29999999999999999), image2_scale = (0.34999999999999998, 1, 0.34999999999999998), image_color = self.getPopColor(shardPop), pos = (0.59999999999999998, 0, 0.012500000000000001), command = self.choseShard, extraArgs = [
                shardId])
            del model
            del button
        else:
            popText = str(shardPop)
            if shardPop == None:
                popText = ''
            
            shardButtonR = DirectButton(parent = shardButtonParent, relief = None, text = popText, text_scale = 0.059999999999999998, text_align = TextNode.ALeft, text1_bg = self.textDownColor, text2_bg = self.textRolloverColor, text3_fg = self.textDisabledColor, textMayChange = 1, pos = (0.5, 0, 0), command = self.choseShard, extraArgs = [
                shardId])
        return (shardButtonParent, shardButtonR, shardButtonL)

    
    def getPopColor(self, pop):
        if pop < self.midPop:
            color1 = POP_COLORS[0]
            color2 = POP_COLORS[1]
            popRange = self.midPop - self.lowPop
            pop = pop - self.lowPop
        else:
            color1 = POP_COLORS[1]
            color2 = POP_COLORS[2]
            popRange = self.highPop - self.midPop
            pop = pop - self.midPop
        popPercent = pop / float(popRange)
        if popPercent > 1:
            popPercent = 1
        
        return color2 * popPercent + color1 * (1 - popPercent)

    
    def getCurrentZoneId(self):
        
        try:
            zoneId = base.cr.playGame.getPlace().getZoneId()
        except:
            zoneId = None

        return zoneId

    
    def getCurrentShardId(self):
        zoneId = self.getCurrentZoneId()
        if zoneId != None and ZoneUtil.isWelcomeValley(zoneId):
            return ToontownGlobals.WelcomeValleyToken
        else:
            return base.localAvatar.defaultShard

    
    def updateScrollList(self):
        curShardTuples = base.cr.listActiveShards()
        
        def compareShardTuples(a, b):
            if a[1] < b[1]:
                return -1
            elif b[1] < a[1]:
                return 1
            else:
                return 0

        curShardTuples.sort(compareShardTuples)
        if base.cr.welcomeValleyManager:
            curShardTuples.append((ToontownGlobals.WelcomeValleyToken, TTLocalizer.WelcomeValley[-1], 0, 0))
        
        currentShardId = self.getCurrentShardId()
        actualShardId = base.localAvatar.defaultShard
        actualShardName = None
        anyChanges = 0
        totalPop = 0
        totalWVPop = 0
        currentMap = { }
        self.shardButtons = []
        for i in range(len(curShardTuples)):
            (shardId, name, pop, WVPop) = curShardTuples[i]
            if shardId == actualShardId:
                actualShardName = name
            
            totalPop += pop
            totalWVPop += WVPop
            pop -= WVPop
            currentMap[shardId] = 1
            buttonTuple = self.shardButtonMap.get(shardId)
            if buttonTuple == None:
                buttonTuple = self.makeShardButton(shardId, name, pop)
                self.shardButtonMap[shardId] = buttonTuple
                anyChanges = 1
            elif base.cr.productName == 'NTT-DMC':
                buttonTuple[1]['image_color'] = self.getPopColor(pop)
            else:
                buttonTuple[1]['text'] = str(pop)
            self.shardButtons.append(buttonTuple[0])
            if shardId == currentShardId or self.book.safeMode:
                buttonTuple[1]['state'] = DISABLED
                buttonTuple[2]['state'] = DISABLED
            else:
                buttonTuple[1]['state'] = NORMAL
                buttonTuple[2]['state'] = NORMAL
        
        for (shardId, buttonTuple) in self.shardButtonMap.items():
            if shardId not in currentMap:
                buttonTuple[0].destroy()
                del self.shardButtonMap[shardId]
                anyChanges = 1
            
        
        buttonTuple = self.shardButtonMap.get(ToontownGlobals.WelcomeValleyToken)
        if buttonTuple:
            if base.cr.productName == 'NTT-DMC':
                buttonTuple[1]['image_color'] = self.getPopColor(totalWVPop)
            else:
                buttonTuple[1]['text'] = str(totalWVPop)
        
        if anyChanges:
            self.regenerateScrollList()
        
        self.totalPopulationText['text'] = TTLocalizer.ShardPagePopulationTotal % totalPop
        helpText = TTLocalizer.ShardPageHelpIntro
        if actualShardName:
            if currentShardId == ToontownGlobals.WelcomeValleyToken:
                helpText += TTLocalizer.ShardPageHelpWelcomeValley % actualShardName
            else:
                helpText += TTLocalizer.ShardPageHelpWhere % actualShardName
        
        if not (self.book.safeMode):
            helpText += TTLocalizer.ShardPageHelpMove
        
        self.helpText['text'] = helpText

    
    def enter(self):
        if not wantOtpServer:
            self.askForShardInfoUpdate()
        
        self.updateScrollList()
        currentShardId = self.getCurrentShardId()
        buttonTuple = self.shardButtonMap.get(currentShardId)
        if buttonTuple:
            i = self.shardButtons.index(buttonTuple[0])
            self.scrollList.scrollTo(i, centered = 1)
        
        ShtikerPage.ShtikerPage.enter(self)
        self.accept('shardInfoUpdated', self.updateScrollList)

    
    def exit(self):
        self.ignore('shardInfoUpdated')
        taskMgr.remove('ShardPageUpdateTask-doLater')
        ShtikerPage.ShtikerPage.exit(self)

    
    def choseShard(self, shardId):
        zoneId = self.getCurrentZoneId()
        canonicalHoodId = ZoneUtil.getCanonicalHoodId(base.localAvatar.lastHood)
        currentShardId = self.getCurrentShardId()
        if shardId == currentShardId:
            return None
        elif shardId == ToontownGlobals.WelcomeValleyToken:
            self.doneStatus = {
                'mode': 'teleport',
                'hood': ToontownGlobals.WelcomeValleyToken }
            messenger.send(self.doneEvent)
        elif shardId == base.localAvatar.defaultShard:
            self.doneStatus = {
                'mode': 'teleport',
                'hood': canonicalHoodId }
            messenger.send(self.doneEvent)
        else:
            
            try:
                place = base.cr.playGame.getPlace()
            except:
                
                try:
                    place = base.cr.playGame.hood.loader.place
                except:
                    place = base.cr.playGame.hood.place


            place.requestTeleport(canonicalHoodId, canonicalHoodId, shardId, -1)
        return None


