# File: C (Python 2.2)

from direct.gui.DirectGui import *
from direct.showbase import DirectObject
import CatalogItem
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from otp.otpbase import OTPLocalizer
from toontown.toontowngui import TTDialog
NUM_ITEMS_SHOWN = 15

class CatalogChatItemPicker(DirectObject.DirectObject):
    
    def __init__(self, callback, newMsg):
        self.confirmDelete = None
        self.doneCallback = callback
        self.panel = DirectFrame(relief = None, geom = getDefaultDialogGeom(), geom_color = ToontownGlobals.GlobalDialogColor, geom_scale = (1.3999999999999999, 1, 1.6000000000000001), text = TTLocalizer.MessagePickerTitle % OTPLocalizer.CustomSCStrings[newMsg], text_pos = (0, 0.68000000000000005), text_scale = 0.050000000000000003, text_wordwrap = 24, pos = (0, 0, 0))
        msgStrings = []
        for msg in base.localAvatar.customMessages:
            msgStrings.append(OTPLocalizer.CustomSCStrings[msg])
        
        gui = loader.loadModelOnce('phase_3.5/models/gui/friendslist_gui')
        self.picker = DirectScrolledList(parent = self.panel, relief = None, pos = (0, 0, 0), incButton_image = (gui.find('**/FndsLst_ScrollUp'), gui.find('**/FndsLst_ScrollDN'), gui.find('**/FndsLst_ScrollUp_Rllvr'), gui.find('**/FndsLst_ScrollUp')), incButton_relief = None, incButton_scale = (1.3, 1.3, -1.3), incButton_pos = (0, 0, -0.5), incButton_image3_color = Vec4(1, 1, 1, 0.20000000000000001), decButton_image = (gui.find('**/FndsLst_ScrollUp'), gui.find('**/FndsLst_ScrollDN'), gui.find('**/FndsLst_ScrollUp_Rllvr'), gui.find('**/FndsLst_ScrollUp')), decButton_relief = None, decButton_scale = (1.3, 1.3, 1.3), decButton_pos = (0, 0, 0.5), decButton_image3_color = Vec4(1, 1, 1, 0.20000000000000001), itemFrame_pos = (0, 0, 0.39000000000000001), itemFrame_scale = 1.0, itemFrame_relief = SUNKEN, itemFrame_frameSize = (-0.55000000000000004, 0.55000000000000004, -0.84999999999999998, 0.059999999999999998), itemFrame_frameColor = (0.84999999999999998, 0.94999999999999996, 1, 1), itemFrame_borderWidth = (0.01, 0.01), itemMakeFunction = self.makeMessageButton, itemMakeExtraArgs = [
            base.localAvatar.customMessages], numItemsVisible = NUM_ITEMS_SHOWN, items = msgStrings)
        clipper = PlaneNode('clipper')
        clipper.setPlane(Plane(Vec3(-1, 0, 0), Point3(0.55000000000000004, 0, 0)))
        self.picker.attachNewNode(clipper)
        cpa = ClipPlaneAttrib.make(ClipPlaneAttrib.OSet, clipper)
        self.picker.node().setAttrib(cpa)
        gui.removeNode()
        buttonModels = loader.loadModelOnce('phase_3.5/models/gui/inventory_gui')
        upButton = buttonModels.find('**/InventoryButtonUp')
        downButton = buttonModels.find('**/InventoryButtonDown')
        rolloverButton = buttonModels.find('**/InventoryButtonRollover')
        exitButton = DirectButton(parent = self.panel, relief = None, pos = (0, 0, -0.69999999999999996), text = TTLocalizer.MessagePickerCancel, text_scale = 0.059999999999999998, text_pos = (-0.0050000000000000001, -0.01), text_fg = Vec4(1, 1, 1, 1), textMayChange = 0, image = (upButton, downButton, rolloverButton), image_scale = 1.1000000000000001, image_color = (0, 0.59999999999999998, 1, 1), command = self._CatalogChatItemPicker__handleCancel)
        buttonModels.removeNode()

    
    def hide(self):
        self.panel.hide()

    
    def show(self):
        self.panel.show()

    
    def destroy(self):
        self.panel.destroy()
        del self.panel
        del self.picker
        del self.doneCallback
        if self.confirmDelete:
            self.confirmDelete.cleanup()
            del self.confirmDelete
            self.confirmDelete = None
        

    
    def makeMessageButton(self, name, number, *extraArgs):
        msg = extraArgs[0][0][number]
        return DirectButton(relief = None, text = OTPLocalizer.CustomSCStrings[msg], text_pos = (-0.5, 0, 0), text_scale = 0.050000000000000003, text_align = TextNode.ALeft, text1_bg = Vec4(1, 1, 0, 1), text2_bg = Vec4(0.5, 0.90000000000000002, 1, 1), text3_fg = Vec4(0.40000000000000002, 0.80000000000000004, 0.40000000000000002, 1), command = self._CatalogChatItemPicker__handleDelete, extraArgs = [
            msg])

    
    def _CatalogChatItemPicker__handleDelete(self, msg):
        self.confirmDelete = TTDialog.TTGlobalDialog(doneEvent = 'confirmDelete', message = TTLocalizer.MessageConfirmDelete % OTPLocalizer.CustomSCStrings[msg], style = TTDialog.TwoChoice)
        self.confirmDelete.msg = msg
        self.confirmDelete.show()
        self.accept('confirmDelete', self._CatalogChatItemPicker__handleDeleteConfirm)

    
    def _CatalogChatItemPicker__handleCancel(self):
        self.doneCallback('cancel')

    
    def _CatalogChatItemPicker__handleDeleteConfirm(self):
        status = self.confirmDelete.doneStatus
        msg = self.confirmDelete.msg
        self.ignore('confirmDelete')
        self.confirmDelete.cleanup()
        del self.confirmDelete
        self.confirmDelete = None
        if status == 'ok':
            self.doneCallback('pick', base.localAvatar.customMessages.index(msg))
        


