# File: M (Python 2.2)

from DirectGui import *
from DirectNotifyGlobal import *
import ToontownGlobals
import DirectObject
import CatalogItem
import Localizer
import ToontownDialog
import PythonUtil

class MailboxScreen(DirectObject.DirectObject):
    notify = directNotify.newCategory('MailboxScreen')
    
    def __init__(self, mailbox, avatar, doneEvent = None):
        self.mailbox = mailbox
        self.avatar = avatar
        self.items = self.avatar.mailboxContents
        self.doneEvent = doneEvent
        self.itemIndex = 0
        self.itemPanel = None
        self.ival = None
        self.itemText = None
        self.acceptingIndex = None
        self.acceptErrorDialog = None
        self.frame = DirectFrame(image = getDefaultDialogGeom(), image_scale = 1.5, image_pos = (0, 0, 0), image_color = (0.25, 0.75, 0.125, 1.0), relief = None)
        self.load()
        self.hide()

    
    def show(self):
        self.frame.show()
        self._MailboxScreen__showCurrentItem()

    
    def hide(self):
        self.frame.hide()

    
    def load(self):
        gui = loader.loadModelOnce('phase_3/models/gui/create_a_toon_gui')
        auxGui = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
        self.itemCountLabel = DirectLabel(parent = self.frame, relief = None, text = self._MailboxScreen__getNumberOfItemsText(), text_wordwrap = 16, pos = (0.0, 0.0, 0.58999999999999997), scale = 0.089999999999999997)
        self.exitButton = DirectButton(parent = self.frame, relief = None, image = (auxGui.find('**/CloseBtn_UP'), auxGui.find('**/CloseBtn_DN'), auxGui.find('**/CloseBtn_Rllvr')), pos = (0.0, 0.0, -0.59999999999999998), scale = 1.2, text = ('', Localizer.MailboxExitButton, Localizer.MailboxExitButton), text_scale = 0.040000000000000001, text_pos = (0, -0.080000000000000002), textMayChange = 0, command = self._MailboxScreen__handleExit)
        self.gettingText = DirectLabel(parent = self.frame, relief = None, text = '', text_wordwrap = 16, pos = (0.0, 0.0, 0.17000000000000001), scale = 0.089999999999999997)
        self.gettingText.hide()
        self.itemText = DirectLabel(parent = self.frame, relief = None, text = '', text_wordwrap = 16, pos = (0.0, 0.0, -0.25), scale = 0.089999999999999997)
        self.itemText.hide()
        self.acceptButton = DirectButton(parent = self.frame, relief = None, image = (auxGui.find('**/ChtBx_OKBtn_UP'), auxGui.find('**/ChtBx_OKBtn_DN'), auxGui.find('**/ChtBx_OKBtn_Rllvr')), pos = (0.0, 0.0, -0.34999999999999998), scale = 1.2, text = ('', Localizer.MailboxAcceptButton, Localizer.MailboxAcceptButton), text_scale = 0.059999999999999998, text_pos = (0, -0.089999999999999997), textMayChange = 0, command = self._MailboxScreen__handleAccept)
        self.acceptButton.hide()
        self.nextButton = DirectButton(parent = self.frame, relief = None, image = (gui.find('**/CrtAtoon_Btn3_UP'), gui.find('**/CrtAtoon_Btn3_DN'), gui.find('**/CrtAtoon_Btn3_RLVR')), pos = (0.59999999999999998, 0, -0.59999999999999998), scale = 0.75, text = ('', Localizer.MailboxItemNext, Localizer.MailboxItemNext), text_scale = 0.080000000000000002, text_pos = (0, 0), text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), textMayChange = 0, command = self._MailboxScreen__nextItem)
        self.nextButton.hide()
        self.prevButton = DirectButton(parent = self.frame, relief = None, image = (gui.find('**/CrtAtoon_Btn3_UP'), gui.find('**/CrtAtoon_Btn3_DN'), gui.find('**/CrtAtoon_Btn3_RLVR')), image_scale = (-1.0, 1, 1), pos = (-0.59999999999999998, 0, -0.59999999999999998), scale = 0.75, text = ('', Localizer.MailboxItemPrev, Localizer.MailboxItemPrev), text_scale = 0.080000000000000002, text_pos = (0, 0), text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), textMayChange = 0, command = self._MailboxScreen__prevItem)
        self.prevButton.hide()

    
    def unload(self):
        self._MailboxScreen__clearCurrentItem()
        self.frame.destroy()
        del self.frame
        del self.mailbox
        if self.acceptErrorDialog:
            self.acceptErrorDialog.cleanup()
            self.acceptErrorDialog = None
        
        for item in self.items:
            item.acceptItemCleanup()
        
        self.ignoreAll()

    
    def _MailboxScreen__handleExit(self):
        self.hide()
        self.unload()
        messenger.send(self.doneEvent)

    
    def _MailboxScreen__handleAccept(self):
        if self.acceptingIndex != None:
            return None
        
        self.acceptingIndex = self.itemIndex
        self.acceptButton.hide()
        self._MailboxScreen__showCurrentItem()
        item = self.items[self.itemIndex]
        item.acceptItem(self.mailbox, self.acceptingIndex, self._MailboxScreen__acceptItemCallback)

    
    def _MailboxScreen__acceptItemCallback(self, retcode, item, index):
        if not hasattr(self, 'frame'):
            return None
        
        if self.acceptingIndex != index:
            self.notify.warning('Got unexpected callback for index %s, expected %s.' % index)
            return None
        
        self.acceptingIndex = None
        if retcode < 0:
            self.notify.info('Could not take item %s: retcode %s' % (item, retcode))
            self.acceptErrorDialog = ToontownDialog.ToontownDialog(style = ToontownDialog.CancelOnly, text = item.getAcceptItemErrorText(retcode), text_wordwrap = 15, command = self._MailboxScreen__acceptError)
            self.acceptErrorDialog.show()
        else:
            callback = PythonUtil.Functor(self._MailboxScreen__acceptOk, index)
            self.acceptErrorDialog = ToontownDialog.ToontownDialog(style = ToontownDialog.Acknowledge, text = item.getAcceptItemErrorText(retcode), text_wordwrap = 15, command = callback)
            self.acceptErrorDialog.show()

    
    def _MailboxScreen__acceptError(self, buttonValue):
        self.acceptErrorDialog.cleanup()
        self.acceptErrorDialog = None
        self._MailboxScreen__showCurrentItem()

    
    def _MailboxScreen__acceptOk(self, index, buttonValue):
        self.acceptErrorDialog.cleanup()
        self.acceptErrorDialog = None
        self.items = self.avatar.mailboxContents
        if self.itemIndex > index or self.itemIndex >= len(self.items):
            self.itemIndex -= 1
        
        if len(self.items) == 0:
            self._MailboxScreen__handleExit()
            return None
        
        self.itemCountLabel['text'] = (self._MailboxScreen__getNumberOfItemsText(),)
        self._MailboxScreen__showCurrentItem()

    
    def _MailboxScreen__getNumberOfItemsText(self):
        if len(self.items) == 1:
            return Localizer.MailboxOneItem
        else:
            return Localizer.MailboxNumberOfItems % len(self.items)

    
    def _MailboxScreen__clearCurrentItem(self):
        if self.itemPanel:
            self.itemPanel.destroy()
            self.itemPanel = None
        
        if self.ival:
            self.ival.finish()
            self.ival = None
        
        self.gettingText.hide()
        self.itemText.hide()
        self.acceptButton.hide()

    
    def _MailboxScreen__showCurrentItem(self):
        self._MailboxScreen__clearCurrentItem()
        item = self.items[self.itemIndex]
        if self.itemIndex == self.acceptingIndex:
            self.gettingText['text'] = Localizer.MailboxGettingItem % item.getName()
            self.gettingText.show()
            return None
        
        self.itemText['text'] = item.getName()
        self.itemText.show()
        (self.itemPanel, self.ival) = item.getPicture(toonbase.localToon)
        if self.itemPanel:
            self.itemPanel.reparentTo(self.frame, -1)
            self.itemPanel.setPos(0, 0, 0.20000000000000001)
            self.itemPanel.setScale(0.34999999999999998)
            self.itemText.setPos(0.0, 0.0, -0.25)
        else:
            self.itemText.setPos(0, 0, 0.17000000000000001)
        if self.ival:
            self.ival.loop()
        
        if self.acceptingIndex == None:
            self.acceptButton.show()
        
        if self.itemIndex > 0:
            self.prevButton.show()
        else:
            self.prevButton.hide()
        if self.itemIndex + 1 < len(self.items):
            self.nextButton.show()
        else:
            self.nextButton.hide()

    
    def _MailboxScreen__nextItem(self):
        if self.itemIndex + 1 < len(self.items):
            self.itemIndex += 1
            self._MailboxScreen__showCurrentItem()
        

    
    def _MailboxScreen__prevItem(self):
        if self.itemIndex > 0:
            self.itemIndex -= 1
            self._MailboxScreen__showCurrentItem()
        


