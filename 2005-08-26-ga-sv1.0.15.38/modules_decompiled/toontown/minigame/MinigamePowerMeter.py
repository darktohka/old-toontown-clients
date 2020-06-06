# File: M (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToontownGlobals import *
from direct.gui.DirectGui import *
from toontown.toonbase import TTLocalizer

class MinigamePowerMeter(DirectFrame):
    
    def __init__(self, size, label = None):
        DirectFrame.__init__(self, relief = None, state = NORMAL, image_color = GlobalDialogColor, image_scale = (0.47999999999999998, 1.0, 0.69999999999999996), image_pos = (0.0, 0.10000000000000001, 0.0), sortOrder = BACKGROUND_SORT_INDEX)
        self['image'] = getDefaultDialogGeom()
        self.resetFrameSize()
        if label == None:
            label = TTLocalizer.MinigamePowerMeterLabel
        
        self.powerText = DirectLabel(self, relief = None, text = label, text_scale = 0.070000000000000007, pos = (0.01, 0.0, 0.28999999999999998))
        self.tooSlow = DirectLabel(parent = self, relief = None, text = TTLocalizer.MinigamePowerMeterTooSlow, scale = 0.070000000000000007, pos = (-0.14999999999999999, 0, 0.050000000000000003), color = (0.10000000000000001, 0.29999999999999999, 0.59999999999999998))
        self.tooFast = DirectLabel(parent = self, relief = None, text = TTLocalizer.MinigamePowerMeterTooFast, scale = 0.070000000000000007, pos = (0.14999999999999999, 0, 0.050000000000000003), color = (0.10000000000000001, 0.29999999999999999, 0.59999999999999998))
        self.tooSlow.hide()
        self.tooFast.hide()
        self.largeGauge = []
        self.gaugeSize = size
        self._MinigamePowerMeter__createSpeedGauge()
        self.show()

    
    def cleanup(self):
        del self.powerText
        for gauge in self.largeGauge:
            if gauge:
                del gauge
            
        
        del self.largeGauge
        self.destroy()

    
    def _MinigamePowerMeter__createSpeedGauge(self):
        gaugeA = DirectWaitBar(parent = self, relief = RAISED, range = self.gaugeSize, frameSize = (-0.59999999999999998, 0.59999999999999998, -0.20000000000000001, 0.20000000000000001), borderWidth = (0.02, 0.02), scale = 0.34999999999999998, pos = (0, 0, 0), frameColor = (0.0, 0.0, 0.0, 0.0), barColor = (0, 1, 0, 0.59999999999999998), sortOrder = FOREGROUND_SORT_INDEX)
        gaugeA.setR(-90)
        gaugeA['value'] = 0
        self.largeGauge.append(gaugeA)
        gaugeTargetTop = DirectWaitBar(parent = self, relief = RAISED, range = self.gaugeSize, frameSize = (-0.59999999999999998, 0.59999999999999998, -0.20000000000000001, 0.20000000000000001), borderWidth = (0.02, 0.02), scale = 0.34999999999999998, pos = (0, 0, 0), frameColor = (1, 1, 1, 1), barColor = (1, 0, 0, 1), sortOrder = BACKGROUND_SORT_INDEX + 1)
        gaugeTargetTop.setR(-90)
        gaugeTargetTop['value'] = 1
        self.largeGauge.append(gaugeTargetTop)
        gaugeTargetBot = DirectWaitBar(parent = self, relief = RAISED, range = self.gaugeSize, frameSize = (-0.59999999999999998, 0.59999999999999998, -0.20000000000000001, 0.20000000000000001), borderWidth = (0.02, 0.02), scale = 0.34999999999999998, pos = (0, 0, 0), frameColor = (1, 1, 1, 0), barColor = (1, 1, 1, 1), sortOrder = BACKGROUND_SORT_INDEX + 2)
        gaugeTargetBot['value'] = 0
        gaugeTargetBot.setR(-90)
        self.largeGauge.append(gaugeTargetBot)
        for gauge in self.largeGauge:
            gauge.show()
        

    
    def setPower(self, power):
        self.largeGauge[0]['value'] = power

    
    def setTarget(self, target):
        self.largeGauge[2]['value'] = target
        self.largeGauge[1]['value'] = target + 1

    
    def updateTooSlowTooFast(self):
        curSpeed = self.largeGauge[0]['value']
        target = self.largeGauge[2]['value']
        self.tooSlow.hide()
        self.tooFast.hide()
        if curSpeed < target - 2:
            self.tooSlow.show()
        elif curSpeed > target + 2:
            self.tooFast.show()
        

    
    def setBarColor(self, color):
        self.largeGauge[0]['barColor'] = color


