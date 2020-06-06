# File: D (Python 2.2)

from DirectButton import *
from DirectFrame import *

class DirectSliderButton(DirectButton):
    
    def __init__(self, parent = None, **kw):
        optiondefs = (('pgFunc', PGSliderButton, None),)
        self.defineoptions(kw, optiondefs)
        DirectButton.__init__(self, parent)
        self.initialiseoptions(DirectSliderButton)



class DirectSliderBar(DirectFrame):
    
    def __init__(self, parent = None, **kw):
        optiondefs = (('pgFunc', PGSliderBar, None), ('width', 10, None), ('height', 1, None), ('button', None, None), ('sliderOnly', 0, self.setSliderOnly), ('negativeMapping', 0, self.setNegativeMapping), ('range', 100, self.setRange), ('value', 0, self.setValue), ('barBorderWidth', (0, 0), self.setBarBorderWidth), ('barColor', (1, 0, 0, 1), self.setBarColor), ('barRelief', FLAT, self.setBarRelief), ('active', 0, self.setActive), ('sortOrder', NO_FADE_SORT_INDEX, None), ('command', None, None), ('extraArgs', [], None))
        if kw.has_key('text'):
            textoptiondefs = (('text_pos', (0, -0.025000000000000001), None), ('text_scale', 0.10000000000000001, None))
        else:
            textoptiondefs = ()
        self.defineoptions(kw, optiondefs + textoptiondefs)
        DirectFrame.__init__(self, parent)
        self.barStyle = PGFrameStyle()
        self.initialiseoptions(DirectSliderBar)
        if self['button'] != None:
            self.guiItem.setSliderButton(self['button'], self['button'].guiItem)
        
        if self['image'] != None:
            self.guiItem.setScale(self['image_scale'][0])
            self.guiItem.setup(self.getWidth(), self.getHeight(), self['range'])
        else:
            self.guiItem.setFrame(-3.0, 3.0, -0.25, 0.25)
            self.barStyle.setWidth(0.050000000000000003, 0.050000000000000003)
            self.barStyle.setColor(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 1)
            self.barStyle.setType(PGFrameStyle.TBevelIn)
            self.guiItem.setFrameStyle(0, self.barStyle)
            self.guiItem.setScale(2)
            self.guiItem.setup(6, 0.5, self['range'])
            self.guiItem.setValue(self['value'])
            if self['scale'] != None:
                self.setScale(self['scale'])
            else:
                self.setScale(0.10000000000000001)
        self.guiItem.setActive(1)
        self.barStyle.setColor(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1)
        self.barStyle.setType(PGFrameStyle.TBevelOut)
        self.updateBarStyle()
        if self['command'] != None:
            self.bind('updated-slider-', self.commandFunc)
        

    
    def destroy(self):
        del self.barStyle
        DirectFrame.destroy(self)

    
    def setSliderOnly(self):
        self.guiItem.setSliderOnly(self['sliderOnly'])

    
    def setNegativeMapping(self):
        self.guiItem.setNegativeMapping(self['negativeMapping'])

    
    def setRange(self):
        self.guiItem.setRange(self['range'])

    
    def setValue(self):
        self.guiItem.setValue(self['value'])

    
    def getPercent(self):
        return self.guiItem.getPercent()

    
    def updateBarStyle(self):
        if not (self.fInit):
            self.guiItem.setBarStyle(self.barStyle)
        

    
    def setBarRelief(self):
        self.barStyle.setType(self['barRelief'])
        self.updateBarStyle()

    
    def setBarBorderWidth(self):
        self.barStyle.setWidth(*self['barBorderWidth'])
        self.updateBarStyle()

    
    def setBarColor(self):
        color = self['barColor']
        self.barStyle.setColor(color[0], color[1], color[2], color[3])
        self.updateBarStyle()

    
    def setActive(self):
        self.guiItem.setActive(self['active'])

    
    def commandFunc(self):
        if self['command']:
            apply(self['command'], self['extraArgs'])
        


