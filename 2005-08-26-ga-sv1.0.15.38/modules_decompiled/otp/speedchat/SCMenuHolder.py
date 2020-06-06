# File: S (Python 2.2)

from pandac.PandaModules import *
from direct.gui.DirectGui import *
from SCObject import SCObject
from SCElement import SCElement
from SCMenu import SCMenu
import types

class SCMenuHolder(SCElement):
    N = 0.90000000000000002
    DefaultFrameColor = (0, 0, 0, 1.0 - N)
    del N
    MenuColorScaleDown = 0.94999999999999996
    
    def __init__(self, title, menu = None):
        SCElement.__init__(self)
        self.title = title
        scGui = loader.loadModelOnce(SCMenu.GuiModelName)
        self.scArrow = scGui.find('**/chatArrow')
        self.menu = None
        self.setMenu(menu)

    
    def destroy(self):
        if self.menu is not None:
            self.menu.destroy()
            self.menu = None
        
        SCElement.destroy(self)

    
    def setTitle(self, title):
        self.title = title
        self.invalidate()

    
    def getTitle(self):
        return self.title

    
    def setMenu(self, menu):
        if self.menu is not None:
            self.menu.destroy()
        
        self.menu = menu
        if self.menu is not None:
            self.privAdoptSCObject(self.menu)
            self.menu.setHolder(self)
            self.menu.reparentTo(self, 1)
            self.menu.hide()
        
        self.updateViewability()

    
    def getMenu(self):
        return self.menu

    
    def showMenu(self):
        if self.menu is not None:
            cS = SCMenuHolder.MenuColorScaleDown
            self.menu.setColorScale(cS, cS, cS, 1)
            self.menu.enterVisible()
            self.menu.show()
        

    
    def hideMenu(self):
        if self.menu is not None:
            self.menu.hide()
            self.menu.exitVisible()
        

    
    def getMenuOverlap(self):
        if self.parentMenu.isTopLevel():
            return self.getTopLevelOverlap()
        else:
            return self.getSubmenuOverlap()

    
    def getMenuOffset(self):
        xOffset = self.width * (1.0 - self.getMenuOverlap())
        return Point3(xOffset, 0, 0)

    
    def onMouseClick(self, event):
        SCElement.enterActive(self)
        self.parentMenu.memberSelected(self)

    
    def enterActive(self):
        SCElement.enterActive(self)
        self.showMenu()
        (r, g, b) = self.getColorScheme().getMenuHolderActiveColor()
        a = self.getColorScheme().getAlpha()
        self.button.frameStyle[BUTTON_READY_STATE].setColor(r, g, b, a)
        self.button.updateFrameStyle()

    
    def exitActive(self):
        SCElement.exitActive(self)
        self.hideMenu()
        self.button.frameStyle[BUTTON_READY_STATE].setColor(*SCMenuHolder.DefaultFrameColor)
        self.button.updateFrameStyle()

    
    def getDisplayText(self):
        return self.title

    
    def updateViewability(self):
        if self.menu is None:
            self.setViewable(0)
            return None
        
        isViewable = False
        for child in self.menu:
            if child.isViewable():
                isViewable = True
                break
            
        
        self.setViewable(isViewable)

    
    def getMinSubmenuWidth(self):
        parentMenu = self.getParentMenu()
        if parentMenu is None:
            (myWidth, myWeight) = self.getMinDimensions()
        else:
            myWidth = parentMenu.getWidth()
        return 0.14999999999999999 + myWidth * self.getMenuOverlap()

    
    def getMinDimensions(self):
        (width, height) = SCElement.getMinDimensions(self)
        width += 1.0
        return (width, height)

    
    def invalidate(self):
        SCElement.invalidate(self)
        if self.menu is not None:
            self.menu.invalidate()
        

    
    def finalize(self, dbArgs = { }):
        if not self.isDirty():
            return None
        
        (r, g, b) = self.getColorScheme().getArrowColor()
        a = self.getColorScheme().getAlpha()
        self.scArrow.setColorScale(r, g, b, a)
        if self.menu is not None:
            self.menu.setPos(self.getMenuOffset())
        
        if self.isActive():
            (r, g, b) = self.getColorScheme().getMenuHolderActiveColor()
            a = self.getColorScheme().getAlpha()
            frameColor = (r, g, b, a)
        else:
            frameColor = SCMenuHolder.DefaultFrameColor
        args = {
            'image': self.scArrow,
            'image_pos': (self.width - 0.5, 0, -(self.height) * 0.5),
            'frameColor': frameColor }
        args.update(dbArgs)
        SCElement.finalize(self, dbArgs = args)

    
    def hasStickyFocus(self):
        return 1

    
    def privSetSettingsRef(self, settingsRef):
        SCObject.privSetSettingsRef(self, settingsRef)
        if self.menu is not None:
            self.menu.privSetSettingsRef(settingsRef)
        

    
    def invalidateAll(self):
        SCObject.invalidateAll(self)
        if self.menu is not None:
            self.menu.invalidateAll()
        

    
    def finalizeAll(self):
        SCObject.finalizeAll(self)
        if self.menu is not None:
            self.menu.finalizeAll()
        


