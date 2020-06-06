# File: P (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.gui.DirectGui import *

class PatternPad(DirectFrame):
    ButtonNames = ('upButton', 'rightButton', 'downButton', 'leftButton')
    buttonNormalScale = 1.0
    buttonPressScale = 1.1000000000000001
    buttonNormalColor = Point4(1, 1, 1, 1)
    buttonDisabledColor = Point4(0.69999999999999996, 0.69999999999999996, 0.69999999999999996, 1)
    
    def __init__(self, parent = aspect2d, **kw):
        self._PatternPad__pressHandlers = (lambda db, self = self: self._PatternPad__pressButton(0), lambda db, self = self: self._PatternPad__pressButton(1), lambda db, self = self: self._PatternPad__pressButton(2), lambda db, self = self: self._PatternPad__pressButton(3))
        self._PatternPad__releaseHandlers = (lambda db, self = self: self._PatternPad__releaseButton(0), lambda db, self = self: self._PatternPad__releaseButton(1), lambda db, self = self: self._PatternPad__releaseButton(2), lambda db, self = self: self._PatternPad__releaseButton(3))
        self._PatternPad__enterHandlers = (lambda db, self = self: self._PatternPad__enterButton(0), lambda db, self = self: self._PatternPad__enterButton(1), lambda db, self = self: self._PatternPad__enterButton(2), lambda db, self = self: self._PatternPad__enterButton(3))
        self._PatternPad__exitHandlers = (lambda db, self = self: self._PatternPad__exitButton(0), lambda db, self = self: self._PatternPad__exitButton(1), lambda db, self = self: self._PatternPad__exitButton(2), lambda db, self = self: self._PatternPad__exitButton(3))
        optiondefs = (('callbacks', None, self.setCallbacks), ('pressHandlers', self._PatternPad__pressHandlers, self.setPressHandlers), ('releaseHandlers', self._PatternPad__releaseHandlers, self.setReleaseHandlers), ('enterHandlers', self._PatternPad__enterHandlers, self.setEnterHandlers), ('exitHandlers', self._PatternPad__exitHandlers, self.setExitHandlers), ('frameColor', (0, 0, 0, 0), None), ('buttons_clickSound', None, None), ('buttons_rolloverSound', None, None))
        self.defineoptions(kw, optiondefs, dynamicGroups = ('buttons',))
        DirectFrame.__init__(self, parent)
        gui = loader.loadModel('phase_3.5/models/gui/matching_game_gui')
        self['geom'] = gui.find('**/pink_circle')
        bnames = ('trumpet', 'guitar', 'drums', 'piano')
        bpos = ((-0.0050000000000000001, 0, 0.30499999999999999), (0.44800000000000001, 0, 0.089999999999999997), (0.029000000000000001, 0, -0.34799999999999998), (-0.41899999999999998, 0, 0.042999999999999997))
        for i in range(0, len(bnames)):
            buttonGeom = gui.find('**/' + bnames[i])
            buttonGeomRollover = gui.find('**/' + bnames[i] + '_rollover')
            buttonGeomPressed = buttonGeomRollover
            buttonGeomDisabled = buttonGeom
            self.createcomponent(self.ButtonNames[i], (), 'buttons', DirectButton, (), parent = self, pos = bpos[i], frameColor = (0, 0, 0, 0), pressEffect = 0, image = (buttonGeom, buttonGeomPressed, buttonGeomRollover, buttonGeomDisabled), image3_color = self.buttonDisabledColor)
        
        buttonGeomDisabled.removeNode()
        gui.removeNode()
        self.initialiseoptions(PatternPad)
        self.setPressCallback(None)
        self.setReleaseCallback(None)
        self.setEnterCallback(None)
        self.setExitCallback(None)

    
    def destroy(self):
        del self._PatternPad__pressHandlers
        del self._PatternPad__releaseHandlers
        del self._PatternPad__enterHandlers
        del self._PatternPad__exitHandlers
        self.setPressCallback(None)
        self.setReleaseCallback(None)
        self.setEnterCallback(None)
        self.setExitCallback(None)
        for name in self.ButtonNames:
            self.destroycomponent(name)
        
        DirectFrame.destroy(self)

    
    def _PatternPad__getButtons(self):
        buttons = []
        for name in self.ButtonNames:
            buttons.append(self.component(name))
        
        return buttons

    
    def disable(self):
        buttons = self._PatternPad__getButtons()
        for button in buttons:
            button['state'] = DISABLED
        

    
    def enable(self):
        buttons = self._PatternPad__getButtons()
        for button in buttons:
            button['state'] = NORMAL
        

    
    def setPressCallback(self, callback):
        self._PatternPad__clientPressCallback = callback

    
    def setReleaseCallback(self, callback):
        self._PatternPad__clientReleaseCallback = callback

    
    def setEnterCallback(self, callback):
        self._PatternPad__clientEnterCallback = callback

    
    def setExitCallback(self, callback):
        self._PatternPad__clientExitCallback = callback

    
    def setCallbacks(self):
        buttons = self._PatternPad__getButtons()
        if self['callbacks'] == None:
            for button in buttons:
                button['command'] = None
            
        else:
            for i in range(0, len(buttons)):
                buttons[i]['command'] = self['callbacks'][i]
            

    
    def _PatternPad__bindButtonHandlers(self, event, handlerTypeName):
        buttons = self._PatternPad__getButtons()
        if self[handlerTypeName] == None:
            for button in buttons:
                button.unbind(event)
            
        else:
            for i in range(0, len(buttons)):
                buttons[i].bind(event, self[handlerTypeName][i])
            

    
    def setPressHandlers(self):
        self._PatternPad__bindButtonHandlers(B1PRESS, 'pressHandlers')

    
    def setReleaseHandlers(self):
        self._PatternPad__bindButtonHandlers(B1RELEASE, 'releaseHandlers')

    
    def setEnterHandlers(self):
        self._PatternPad__bindButtonHandlers(ENTER, 'enterHandlers')

    
    def setExitHandlers(self):
        self._PatternPad__bindButtonHandlers(EXIT, 'exitHandlers')

    
    def _PatternPad__pressButton(self, index):
        button = self._PatternPad__getButtons()[index]
        button.setScale(self.buttonPressScale)
        if self._PatternPad__clientPressCallback != None:
            self._PatternPad__clientPressCallback(index)
        

    
    def _PatternPad__releaseButton(self, index):
        button = self._PatternPad__getButtons()[index]
        button.setScale(self.buttonNormalScale)
        if self._PatternPad__clientReleaseCallback != None:
            self._PatternPad__clientReleaseCallback(index)
        

    
    def _PatternPad__enterButton(self, index):
        if self._PatternPad__clientEnterCallback != None:
            self._PatternPad__clientEnterCallback(index)
        

    
    def _PatternPad__exitButton(self, index):
        if self._PatternPad__clientExitCallback != None:
            self._PatternPad__clientExitCallback(index)
        

    
    def simButtonPress(self, index):
        button = self._PatternPad__getButtons()[index]
        button.setScale(self.buttonPressScale)
        button.component('image3').setColor(self.buttonNormalColor)

    
    def simButtonRelease(self, index):
        button = self._PatternPad__getButtons()[index]
        button.setScale(self.buttonNormalScale)
        button.component('image3').setColor(self.buttonDisabledColor)


