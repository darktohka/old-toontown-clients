# File: O (Python 2.2)

from pandac.PandaModules import *
import types
from direct.gui import OnscreenText
from direct.directtools import DirectUtil

class OnScreenDebug:
    
    def __init__(self):
        self.enabled = config.GetBool('on-screen-debug-enabled', 0)
        self.onScreenText = None
        self.frame = 0
        self.text = ''
        self.data = { }

    
    def load(self):
        if self.onScreenText:
            return None
        
        fontPath = config.GetString('on-screen-debug-font', 'cmtt12')
        fontScale = config.GetFloat('on-screen-debug-font-scale', 0.050000000000000003)
        color = {
            'black': Vec4(0, 0, 0, 1),
            'white': Vec4(1, 1, 1, 1) }
        fgColor = color[config.GetString('on-screen-debug-fg-color', 'white')]
        bgColor = color[config.GetString('on-screen-debug-bg-color', 'black')]
        fgColor.setW(config.GetFloat('on-screen-debug-fg-alpha', 0.84999999999999998))
        bgColor.setW(config.GetFloat('on-screen-debug-bg-alpha', 0.84999999999999998))
        font = loader.loadFont(fontPath)
        if not font.isValid():
            print 'failed to load OnScreenDebug font', fontPath
            font = TextNode.getDefaultFont()
        
        self.onScreenText = OnscreenText.OnscreenText(pos = (-1.0, 0.90000000000000002), fg = fgColor, bg = bgColor, scale = (fontScale, fontScale, 0.0), align = TextNode.ALeft, mayChange = 1, font = font)
        DirectUtil.useDirectRenderStyle(self.onScreenText)

    
    def render(self):
        if not (self.enabled):
            return None
        
        if not (self.onScreenText):
            self.load()
        
        self.onScreenText.clearText()
        entries = self.data.items()
        entries.sort()
        for (k, v) in entries:
            if v[0] == self.frame:
                isNew = '='
            else:
                isNew = '~'
            value = v[1]
            if type(value) == types.FloatType:
                value = '% 10.4f' % (value,)
            
            self.onScreenText.appendText('%20s %s %-44s\n' % (k, isNew, value))
        
        self.onScreenText.appendText(self.text)
        self.frame += 1

    
    def clear(self):
        self.text = ''
        if self.onScreenText:
            self.onScreenText.clearText()
        

    
    def add(self, key, value):
        self.data[key] = (self.frame, value)
        return 1

    
    def remove(self, key):
        del self.data[key]

    
    def removeAllWithPrefix(self, prefix):
        toRemove = []
        for key in self.data.keys():
            if len(key) >= len(prefix):
                if key[:len(prefix)] == prefix:
                    toRemove.append(key)
                
            
        
        for key in toRemove:
            self.remove(key)
        

    
    def append(self, text):
        self.text += text


