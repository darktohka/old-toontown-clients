# File: T (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.gui.DirectGui import *
from direct.directnotify import DirectNotifyGlobal
import TTDialog
from toontown.toonbase import TTLocalizer
from direct.showbase import PythonUtil
from otp.login import LeaveToPayDialog
Pages = {
    'otherHoods': (TTLocalizer.TeaserOtherHoods, 'features-hoods', 0, 1),
    'typeAName': (TTLocalizer.TeaserTypeAName, 'features-typeAName', 0, 1),
    'sixToons': (TTLocalizer.TeaserSixToons, 'features-sixToons', 0, 1),
    'otherGags': (TTLocalizer.TeaserOtherGags, 'features-gags', 0, 1),
    'clothing': (TTLocalizer.TeaserClothing, 'features-clothes', 0, 0),
    'furniture': (TTLocalizer.TeaserFurniture, 'features-furniture', 0, 0),
    'cogHQ': (TTLocalizer.TeaserCogHQ, 'features-cogHq', 0, 1),
    'secretChat': (TTLocalizer.TeaserSecretChat, 'features-chat', 0, 1),
    'mailers': (TTLocalizer.TeaserCardsAndPosters, 'features-mailers', 1, 1),
    'holidays': (TTLocalizer.TeaserHolidays, 'features-holidays', 0, 0),
    'quests': (TTLocalizer.TeaserQuests, 'features-quests', 0, 0),
    'emotions': (TTLocalizer.TeaserEmotions, 'features-catalog', 2, 0),
    'minigames': (TTLocalizer.TeaserMinigames, 'features-minigames', 0, 0) }
PageOrder = [
    'sixToons',
    'typeAName',
    'otherHoods',
    'otherGags',
    'clothing',
    'furniture',
    'cogHQ',
    'secretChat',
    'mailers',
    'holidays',
    'quests',
    'emotions',
    'minigames']

class TeaserPanel(DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('TeaserPanel')
    
    def __init__(self, pageName, doneFunc = None):
        self.doneFunc = doneFunc
        if not hasattr(self, 'browser'):
            self.browser = FeatureBrowser()
            self.browser.load()
            self.browser.setPos(0, 0, -0.65000000000000002)
            self.browser.reparentTo(hidden)
        
        self.leaveDialog = None
        self.showPage(pageName)

    
    def _TeaserPanel__handleDone(self, choice):
        self.cleanup()
        self.unload()
        if choice == 1:
            self._TeaserPanel__handlePay()
        else:
            self._TeaserPanel__handleContinue()
        if self.doneFunc:
            self.doneFunc()
        

    
    def _TeaserPanel__handleContinue(self):
        pass

    
    def _TeaserPanel__handlePay(self):
        if base.cr.isWebPlayToken():
            if self.leaveDialog == None:
                self.leaveDialog = LeaveToPayDialog.LeaveToPayDialog(0)
            
            self.leaveDialog.show()
        else:
            self.notify.error('You should not have a TeaserPanel without a PlayToken')

    
    def cleanup(self):
        if hasattr(self, 'browser'):
            self.browser.reparentTo(hidden)
            self.browser.ignoreAll()
        
        if hasattr(self, 'dialog'):
            base.transitions.noTransitions()
            self.dialog.cleanup()
            del self.dialog
        
        if self.leaveDialog:
            self.leaveDialog.destroy()
            self.leaveDialog = None
        
        self.ignoreAll()

    
    def unload(self):
        if hasattr(self, 'browser'):
            self.browser.destroy()
            del self.browser
        

    
    def showPage(self, pageName):
        if not (pageName in PageOrder):
            self.notify.error("unknown page '%s'" % pageName)
        
        self.browser.scrollTo(PageOrder.index(pageName))
        self.cleanup()
        self.dialog = TTDialog.TTDialog(text = TTLocalizer.TeaserTop, text_wordwrap = 20, topPad = -0.050000000000000003, midPad = 1.25, sidePad = 0.0, command = self._TeaserPanel__handleDone, fadeScreen = 0.5, style = TTDialog.TwoChoice, buttonTextList = [
            TTLocalizer.TeaserSubscribe,
            TTLocalizer.TeaserContinue], button_text_scale = 0.070000000000000007, buttonPadSF = 5.5, sortOrder = NO_FADE_SORT_INDEX)
        self.dialog.setPos(0, 0, 0.75)
        self.browser.reparentTo(self.dialog)
        base.transitions.fadeScreen(0.5)
        self.accept('arrow_right', self.showNextPage)
        self.accept('arrow_left', self.showPrevPage)

    
    def showNextPage(self):
        self.browser.scrollBy(1)

    
    def showPrevPage(self):
        self.browser.scrollBy(-1)

    
    def showPay(self):
        self.dialog.buttonList[0].show()

    
    def hidePay(self):
        self.dialog.buttonList[0].hide()



class FeatureBrowser(DirectScrolledList):
    
    def __init__(self, parent = aspect2dp, **kw):
        self.parent = parent
        gui = loader.loadModelOnce('phase_3/models/gui/scroll_arrows_gui')
        optiondefs = (('parent', self.parent, None), ('relief', None, None), ('incButton_image', (gui.find('**/FndsLst_ScrollUp'), gui.find('**/FndsLst_ScrollDN'), gui.find('**/FndsLst_ScrollUp_Rllvr'), gui.find('**/FndsLst_ScrollUp')), None), ('incButton_relief', None, None), ('incButton_scale', (2.0, 1.5, 2.5), None), ('incButton_pos', (0.65000000000000002, 0, 0.029999999999999999), None), ('incButton_hpr', (0, 0, 90), None), ('incButton_image3_color', Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 0.5), None), ('decButton_image', (gui.find('**/FndsLst_ScrollUp'), gui.find('**/FndsLst_ScrollDN'), gui.find('**/FndsLst_ScrollUp_Rllvr'), gui.find('**/FndsLst_ScrollUp')), None), ('decButton_relief', None, None), ('decButton_scale', (2.0, 1.5, 2.5), None), ('decButton_pos', (-0.65000000000000002, 0, 0.029999999999999999), None), ('decButton_hpr', (0, 0, -90), None), ('decButton_image3_color', Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 0.5), None), ('numItemsVisible', 1, None), ('items', [], None), ('scrollSpeed', 4, None))
        gui.removeNode()
        self.defineoptions(kw, optiondefs)
        DirectScrolledList.__init__(self, parent)
        self.initialiseoptions(FeatureBrowser)

    
    def destroy(self):
        DirectScrolledList.destroy(self)

    
    def load(self):
        guiModel = loader.loadModelOnce('phase_3/models/gui/feature_gui')
        logoModel = loader.loadModelOnce('phase_3/models/gui/members_only_gui')
        for page in PageOrder:
            (textInfo, imageName, aspect, members) = Pages.get(page)
            if base.cr.productName == 'DisneyOnline-UK':
                if imageName == 'features-mailers':
                    imageName = 'features-mailers-UK'
                
            
            imageModel = guiModel.find('**/' + imageName)
            if aspect == 0:
                scale = (1.1000000000000001, 0, 0.84999999999999998)
                logoPos = (0.44, 0, -0.31)
            elif aspect == 1:
                scale = (0.69999999999999996, 0, 0.90000000000000002)
                logoPos = (0.27500000000000002, 0, -0.33500000000000002)
            else:
                scale = (0.80000000000000004, 0, 0.80000000000000004)
                logoPos = (0.45000000000000001, 0, -0.28000000000000003)
            panel = DirectFrame(parent = self, relief = None, image = imageModel, image_scale = scale, image_pos = (0, 0, 0.050000000000000003), text = textInfo, text_scale = 0.050000000000000003, text_pos = (0, -0.55000000000000004))
            self.addItem(panel)
            if members:
                logo = DirectFrame(parent = panel, relief = None, image = logoModel.find('**/MembersOnly'), image_scale = (0.28749999999999998, 0, 0.25), image_pos = logoPos)
            
        
        guiModel.removeNode()
        logoModel.removeNode()


