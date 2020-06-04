# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\gui\DirectCheckButton.py
__all__ = [
 'DirectCheckButton']
from pandac.PandaModules import *
import DirectGuiGlobals as DGG
from DirectButton import *
from DirectLabel import *

class DirectCheckButton(DirectButton):
    __module__ = __name__

    def __init__(self, parent=None, **kw):
        self.colors = None
        optiondefs = (('indicatorValue', 0, self.setIndicatorValue), ('boxBorder', 0, None), ('boxPlacement', 'left', None), ('boxImage', None, None), ('boxImageScale', 1, None), ('boxImageColor', None, None), ('boxRelief', 'sunken', None))
        self.defineoptions(kw, optiondefs)
        DirectButton.__init__(self, parent)
        self.indicator = self.createcomponent('indicator', (), None, DirectLabel, (self,), numStates=2, image=self['boxImage'], image_scale=self['boxImageScale'], image_color=self['boxImageColor'], state='disabled', text=('X',
                                                                                                                                                                                                                              'X'), relief=self['boxRelief'])
        self.initialiseoptions(DirectCheckButton)
        if self['boxImage'] == None:
            self.indicator['text'] = (' ', '*')
            self.indicator['text_pos'] = (0, -0.2)
        else:
            self.indicator['text'] = (' ', ' ')
        if self['boxImageColor'] != None and self['boxImage'] != None:
            self.colors = [
             VBase4(0, 0, 0, 0), self['boxImageColor']]
            self.component('indicator')['image_color'] = VBase4(0, 0, 0, 0)
        return

    def resetFrameSize(self):
        self.setFrameSize(fClearFrame=1)

    def setFrameSize(self, fClearFrame=0):
        if self['frameSize']:
            self.bounds = self['frameSize']
            frameType = self.frameStyle[0].getType()
            ibw = self.indicator['borderWidth']
        else:
            frameType = self.frameStyle[0].getType()
            if fClearFrame and frameType != PGFrameStyle.TNone:
                self.frameStyle[0].setType(PGFrameStyle.TNone)
                self.guiItem.setFrameStyle(0, self.frameStyle[0])
                self.guiItem.getStateDef(0)
            self.getBounds()
            if frameType != PGFrameStyle.TNone:
                self.frameStyle[0].setType(frameType)
                self.guiItem.setFrameStyle(0, self.frameStyle[0])
            ibw = self.indicator['borderWidth']
            indicatorWidth = self.indicator.getWidth() + 2 * ibw[0]
            indicatorHeight = self.indicator.getHeight() + 2 * ibw[1]
            diff = indicatorHeight + 2 * self['boxBorder'] - (self.bounds[3] - self.bounds[2])
            if diff > 0:
                if self['boxPlacement'] == 'left':
                    self.bounds[0] += -(indicatorWidth + 2 * self['boxBorder'])
                    self.bounds[3] += diff / 2
                    self.bounds[2] -= diff / 2
                elif self['boxPlacement'] == 'below':
                    self.bounds[2] += -(indicatorHeight + 2 * self['boxBorder'])
                elif self['boxPlacement'] == 'right':
                    self.bounds[1] += indicatorWidth + 2 * self['boxBorder']
                    self.bounds[3] += diff / 2
                    self.bounds[2] -= diff / 2
                else:
                    self.bounds[3] += indicatorHeight + 2 * self['boxBorder']
            elif self['boxPlacement'] == 'left':
                self.bounds[0] += -(indicatorWidth + 2 * self['boxBorder'])
            elif self['boxPlacement'] == 'below':
                self.bounds[2] += -(indicatorHeight + 2 * self['boxBorder'])
            elif self['boxPlacement'] == 'right':
                self.bounds[1] += indicatorWidth + 2 * self['boxBorder']
            else:
                self.bounds[3] += indicatorHeight + 2 * self['boxBorder']
        if frameType != PGFrameStyle.TNone:
            if frameType != PGFrameStyle.TFlat:
                bw = self['borderWidth']
            else:
                bw = (0, 0)
            self.guiItem.setFrame(self.bounds[0] - bw[0], self.bounds[1] + bw[0], self.bounds[2] - bw[1], self.bounds[3] + bw[1])
            bbounds = self.indicator['pos'] or self.bounds
            lbounds = self.indicator.bounds
            newpos = [0, 0, 0]
            if self['boxPlacement'] == 'left':
                newpos[0] += bbounds[0] - lbounds[0] + self['boxBorder'] + ibw[0]
                dropValue = (bbounds[3] - bbounds[2] - lbounds[3] + lbounds[2]) / 2 + self['boxBorder']
                newpos[2] += bbounds[3] - lbounds[3] + self['boxBorder'] - dropValue
            elif self['boxPlacement'] == 'right':
                newpos[0] += bbounds[1] - lbounds[1] - self['boxBorder'] - ibw[0]
                dropValue = (bbounds[3] - bbounds[2] - lbounds[3] + lbounds[2]) / 2 + self['boxBorder']
                newpos[2] += bbounds[3] - lbounds[3] + self['boxBorder'] - dropValue
            elif self['boxPlacement'] == 'above':
                newpos[2] += bbounds[3] - lbounds[3] - self['boxBorder'] - ibw[1]
            else:
                newpos[2] += bbounds[2] - lbounds[2] + self['boxBorder'] + ibw[1]
            self.indicator.setPos(newpos[0], newpos[1], newpos[2])

    def commandFunc(self, event):
        self['indicatorValue'] = 1 - self['indicatorValue']
        if self.colors != None:
            self.component('indicator')['image_color'] = self.colors[self['indicatorValue']]
        if self['command']:
            apply(self['command'], [self['indicatorValue']] + self['extraArgs'])
        return

    def setIndicatorValue(self):
        self.component('indicator').guiItem.setState(self['indicatorValue'])
        if self.colors != None:
            self.component('indicator')['image_color'] = self.colors[self['indicatorValue']]
        return