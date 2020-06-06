# File: S (Python 2.2)

from SCColorScheme import SCColorScheme
from direct.tkwidgets.Valuator import *
colors = { }
panels = { }

def scRgbPanel(callback, title, initColor):
    
    def getScaledColor(color, s):
        return tuple(map(lambda x: x * s, color))

    sInitColor = getScaledColor(initColor, 255.0)
    vgp = ValuatorGroupPanel(title = title, dim = 3, labels = [
        'R',
        'G',
        'B'], value = [
        int(sInitColor[0]),
        int(sInitColor[1]),
        int(sInitColor[2])], type = 'slider', valuator_style = 'mini', valuator_min = 0, valuator_max = 255, valuator_resolution = 1, fDestroy = 1)
    pButton = Button(vgp.interior(), text = '', bg = getTkColorString(sInitColor))
    pButton.pack(expand = 1, fill = BOTH)
    
    def acceptColor(color):
        pButton['bg'] = getTkColorString(color)
        callback(getScaledColor(color, 1 / 255.0))

    
    def getDefaultFrameColor():
        base.speedChat.setColorScheme(SCColorScheme(arrowColor = colors['arrowColor'], rolloverColor = colors['rolloverColor']))
        colors['frameColor'] = base.speedChat.getColorScheme().getFrameColor()
        p = panels['frameColor'].component('valuatorGroup')
        c = colors['frameColor']
        p.component('valuator0').set(math.floor(c[0] * 255))
        p.component('valuator1').set(math.floor(c[1] * 255))
        p.component('valuator2').set(math.floor(c[2] * 255))

    
    def updateAllPanels():
        cs = base.speedChat.getColorScheme()
        colors['arrowColor'] = cs.getArrowColor()
        colors['rolloverColor'] = cs.getRolloverColor()
        colors['frameColor'] = cs.getFrameColor()
        for panelName in colors.keys():
            p = panels[panelName].component('valuatorGroup')
            c = colors[panelName]
            p.component('valuator0').set(math.floor(c[0] * 255))
            p.component('valuator1').set(math.floor(c[1] * 255))
            p.component('valuator2').set(math.floor(c[2] * 255))
        

    menu = vgp.component('menubar').component('Valuator Group-menu')
    menu.insert_command(index = 0, label = 'Get Default FrameColor', command = getDefaultFrameColor)
    menu.insert_command(index = 1, label = 'Update All Panels', command = updateAllPanels)
    vgp['command'] = acceptColor
    return vgp


def adjustSCColors():
    global colors
    base.startTk()
    cs = base.speedChat.getColorScheme()
    colors = {
        'arrowColor': cs.getArrowColor(),
        'rolloverColor': cs.getRolloverColor(),
        'frameColor': cs.getFrameColor() }
    for colorName in colors.keys():
        
        def handleCallback(color, colorName = colorName):
            colors[colorName] = tuple(color)
            base.speedChat.setColorScheme(SCColorScheme(**None))

        panels[colorName] = scRgbPanel(handleCallback, colorName, colors[colorName])
    

