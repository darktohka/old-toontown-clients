# File: N (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.showbase import PandaObject
import whrandom
from direct.task import Task
from direct.gui.DirectGui import *
import string
from direct.gui import OnscreenText

class NameTumbler:
    
    def __init__(self, tPosition, nameList, category, priority, linkage, tColor):
        self.tPosition = tPosition
        self.nameList = nameList
        self.category = category
        self.priority = priority
        self.linkage = linkage
        self.tumblerColor = tColor
        self.displayList = [
            ' '] + [
            ' '] + self.nameList + [
            ' '] + [
            ' ']
        self.nameIndex = -1
        self.isActive = 1
        self.circle = 'src/maps/NameTumblerCheck.tif'
        self.background = 'src/maps/NameTumbler.tif'
        self.upArrow = 'src/maps/NameTumblerUpArrow.tif'
        self.downArrow = 'src/maps/NameTumblerDownArrow.tif'
        self.loadTumblerGUI()

    
    def loadTumblerGUI(self):
        self.tumbler = DirectFrame(parent = aspect2d, relief = 'flat', scale = (1, 1, 1), state = 'disabled', pos = self.tPosition, frameColor = (1, 1, 1, 0))
        self.hilight = self.makeHighlight((-0.71036699999999997, 0.0, 0.12296700000000001))
        self.hilight.reparentTo(self.tumbler, 1)
        self.tumblerscrollList = self.makeScrollList((-0.59999999999999998, 0, 0.20000000000000001), self.tumblerColor, self.displayList, self.makeLabel, [
            TextNode.ACenter,
            'title'])
        self.tumblerscrollList['command'] = self._NameTumbler__listsChanged
        self.tumblerscrollList.reparentTo(self.tumbler)
        if self.category != '':
            self.check = self.makeCheckBox((-0.61699999999999999, 0, 0.374), self.category, (0, 0.25, 0.5, 1), self.toggleTumbler)
            self.check.reparentTo(self.tumbler)
        
        self.getRandomResult()

    
    def unloadTumblerGUI(self):
        if self.category != '':
            self.check.destroy()
            del self.check
        
        self.tumblerscrollList.destroy()
        del self.tumblerscrollList
        self.hilight.destroy()
        del self.hilight
        self.tumbler.destroy()
        del self.tumbler

    
    def toggleTumbler(self, value):
        if self.isActive:
            if self.priority == 1:
                messenger.send('CheckTumblerPriority', [
                    self.category])
            else:
                self.deactivateTumbler()
        else:
            self.activateTumbler()
        if self.linkage > 0:
            messenger.send('CheckTumblerLinkage', [
                self.category])
        
        self._NameTumbler__listsChanged()
        if self.isActive:
            self.tumblerscrollList.refresh()
        
        self.updateCheckBoxes()

    
    def _NameTumbler__listsChanged(self):
        newname = ''
        self.nameIndex = self.tumblerscrollList.index + 2
        messenger.send('updateNameResult')

    
    def updateLists(self):
        self.tumblerscrollList.scrollTo(self.nameIndex - 2)
        messenger.send('updateNameResult')

    
    def updateCheckBoxes(self):
        if self.category != '':
            if self.isActive:
                self.check['indicatorValue'] = self.isActive
            else:
                self.check['indicatorValue'] = -1
            self.check.setIndicatorValue()
        

    
    def nameClickedOn(self, index):
        self.nameIndex = index
        self.updateLists()
        self._NameTumbler__listsChanged()

    
    def activateTumbler(self):
        self.hilight.show()
        self.isActive = 1
        self.tumblerscrollList.itemFrame['frameColor'] = self.tumblerColor

    
    def deactivateTumbler(self):
        self.hilight.hide()
        self.isActive = 0
        self.tumblerscrollList.itemFrame['frameColor'] = (0.69999999999999996, 0.69999999999999996, 0.69999999999999996, 1)

    
    def getName(self):
        if self.isActive:
            name = self.nameList[self.nameIndex - 2]
        else:
            name = ''
        return name

    
    def makeLabel(self, te, index, others):
        alig = others[0]
        if alig == TextNode.ARight:
            newpos = (0.44, 0, 0)
        elif alig == TextNode.ALeft:
            newpos = (0, 0, 0)
        else:
            newpos = (0.20000000000000001, 0, 0)
        df = DirectFrame(state = 'normal', relief = None, text = te, text_scale = 0.10000000000000001, text_pos = newpos, text_align = alig, textMayChange = 0)
        df.bind(B1PRESS, lambda x, df = df: self.nameClickedOn(index))
        return df

    
    def makeScrollList(self, ipos, mcolor, nitems, nitemMakeFunction, nitemMakeExtraArgs):
        it = nitems[:]
        ds = DirectScrolledList(items = it, itemMakeFunction = nitemMakeFunction, itemMakeExtraArgs = nitemMakeExtraArgs, parent = aspect2d, relief = None, command = None, pos = ipos, scale = 0.59999999999999998, incButton_image = (self.downArrow, self.upArrow, self.circle, self.downArrow), incButton_relief = None, incButton_scale = (0.20000000000000001, 0.050000000000000003, 0.050000000000000003), incButton_pos = (0, 0, -0.54500000000000004), decButton_image = (self.upArrow, self.downArrow, self.circle, self.upArrow), decButton_relief = None, decButton_scale = (0.20000000000000001, 0.050000000000000003, 0.050000000000000003), decButton_pos = (0, 0, 0.19500000000000001), itemFrame_pos = (-0.20000000000000001, 0, 0.028000000000000001), itemFrame_scale = 1.0, itemFrame_relief = RAISED, itemFrame_frameSize = (-0.050000000000000003, 0.47999999999999998, -0.5, 0.10000000000000001), itemFrame_frameColor = mcolor, itemFrame_borderWidth = (0.01, 0.01), numItemsVisible = 5)
        ds.setTransparency(1)
        return ds

    
    def makeCheckBox(self, npos, ntex, ntexcolor, comm):
        dcf = DirectCheckButton(parent = aspect2d, relief = None, scale = 0.10000000000000001, boxBorder = 0.080000000000000002, boxImage = self.circle, boxImageScale = (0.40000000000000002, 0.40000000000000002, 0.40000000000000002), boxRelief = None, pos = npos, text = ntex, text_fg = ntexcolor, text_scale = 0.80000000000000004, text_pos = (0.20000000000000001, 0), indicator_pos = (-0.56666700000000003, 0, -0.044999999999999998), indicator_image_pos = (-0.26000000000000001, 0, 0.074999999999999997), command = comm, text_align = TextNode.ALeft)
        dcf.setTransparency(1)
        return dcf

    
    def makeHighlight(self, npos):
        return DirectFrame(parent = aspect2d, relief = 'flat', scale = (0.55200000000000005, 0, 0.11), state = 'disabled', frameSize = (-0.050000000000000003, 0.47999999999999998, -0.5, 0.10000000000000001), borderWidth = (0.01, 0.01), pos = npos, frameColor = (1, 0, 1, 0.40000000000000002))

    
    def getRandomResult(self):
        randomName = whrandom.choice(self.nameList)
        self.nameIndex = self.displayList.index(randomName)
        self.updateCheckBoxes()
        self.updateLists()


