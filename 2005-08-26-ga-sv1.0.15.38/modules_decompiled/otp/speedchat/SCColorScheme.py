# File: S (Python 2.2)

from ColorSpace import *

class SCColorScheme:
    
    def __init__(self, arrowColor = (0.5, 0.5, 1), rolloverColor = (0.53000000000000003, 0.90000000000000002, 0.53000000000000003), frameColor = None, pressedColor = None, menuHolderActiveColor = None, emoteIconColor = None, textColor = (0, 0, 0), emoteIconDisabledColor = (0.5, 0.5, 0.5), textDisabledColor = (0.40000000000000002, 0.40000000000000002, 0.40000000000000002), alpha = 0.94999999999999996):
        
        def scaleColor(color, s):
            (y, u, v) = rgb2yuv(*color)
            return yuv2rgb(y * s, u, v)

        
        def scaleIfNone(color, srcColor, s):
            if color is not None:
                return color
            else:
                return scaleColor(srcColor, s)

        self._SCColorScheme__arrowColor = arrowColor
        self._SCColorScheme__rolloverColor = rolloverColor
        self._SCColorScheme__frameColor = frameColor
        if self._SCColorScheme__frameColor is None:
            (h, s, v) = rgb2hsv(*arrowColor)
            self._SCColorScheme__frameColor = hsv2rgb(h, 0.20000000000000001 * s, v)
        
        self._SCColorScheme__pressedColor = scaleIfNone(pressedColor, self._SCColorScheme__rolloverColor, 0.92000000000000004)
        self._SCColorScheme__menuHolderActiveColor = scaleIfNone(menuHolderActiveColor, self._SCColorScheme__rolloverColor, 0.83999999999999997)
        self._SCColorScheme__emoteIconColor = emoteIconColor
        if self._SCColorScheme__emoteIconColor is None:
            (h, s, v) = rgb2hsv(*self._SCColorScheme__rolloverColor)
            self._SCColorScheme__emoteIconColor = hsv2rgb(h, 1.0, 0.80000000000000004 * v)
        
        self._SCColorScheme__emoteIconDisabledColor = emoteIconDisabledColor
        self._SCColorScheme__textColor = textColor
        self._SCColorScheme__textDisabledColor = textDisabledColor
        self._SCColorScheme__alpha = alpha

    
    def getArrowColor(self):
        return self._SCColorScheme__arrowColor

    
    def getRolloverColor(self):
        return self._SCColorScheme__rolloverColor

    
    def getFrameColor(self):
        return self._SCColorScheme__frameColor

    
    def getPressedColor(self):
        return self._SCColorScheme__pressedColor

    
    def getMenuHolderActiveColor(self):
        return self._SCColorScheme__menuHolderActiveColor

    
    def getEmoteIconColor(self):
        return self._SCColorScheme__emoteIconColor

    
    def getTextColor(self):
        return self._SCColorScheme__textColor

    
    def getEmoteIconDisabledColor(self):
        return self._SCColorScheme__emoteIconDisabledColor

    
    def getTextDisabledColor(self):
        return self._SCColorScheme__textDisabledColor

    
    def getAlpha(self):
        return self._SCColorScheme__alpha

    
    def __str__(self):
        members = ('arrowColor', 'rolloverColor', 'frameColor', 'pressedColor', 'menuHolderActiveColor', 'emoteIconColor', 'textColor', 'emoteIconDisabledColor', 'textDisabledColor', 'alpha')
        result = ''
        for member in members:
            result += '%s = %s' % (member, self.__dict__['_%s__%s' % (self.__class__.__name__, member)])
            if member is not members[-1]:
                result += '\n'
            
        
        return result

    
    def __repr__(self):
        return str(self)


