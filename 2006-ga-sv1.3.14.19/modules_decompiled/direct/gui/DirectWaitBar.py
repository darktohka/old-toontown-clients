# File: D (Python 2.2)

from DirectFrame import *

class DirectWaitBar(DirectFrame):
    
    def __init__(self, parent = None, **kw):
        optiondefs = (('pgFunc', PGWaitBar, None), ('frameSize', (-1, 1, -0.080000000000000002, 0.080000000000000002), None), ('borderWidth', (0, 0), None), ('range', 100, self.setRange), ('value', 0, self.setValue), ('barBorderWidth', (0, 0), self.setBarBorderWidth), ('barColor', (1, 0, 0, 1), self.setBarColor), ('barRelief', FLAT, self.setBarRelief), ('sortOrder', NO_FADE_SORT_INDEX, None))
        if kw.has_key('text'):
            textoptiondefs = (('text_pos', (0, -0.025000000000000001), None), ('text_scale', 0.10000000000000001, None))
        else:
            textoptiondefs = ()
        self.defineoptions(kw, optiondefs + textoptiondefs)
        DirectFrame.__init__(self, parent)
        self.barStyle = PGFrameStyle()
        self.initialiseoptions(DirectWaitBar)
        self.updateBarStyle()

    
    def destroy(self):
        del self.barStyle
        DirectFrame.destroy(self)

    
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

    
    def update(self, value):
        self['value'] = value
        base.graphicsEngine.renderFrame()

    
    def finish(self):
        N = 10
        remaining = self['range'] - self['value']
        if remaining:
            step = max(1, int(remaining / N))
            count = self['value']
            while count != self['range']:
                count += step
                if count > self['range']:
                    count = self['range']
                
                self.update(count)
        


