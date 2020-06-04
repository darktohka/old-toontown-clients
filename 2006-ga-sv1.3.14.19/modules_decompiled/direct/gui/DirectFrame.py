# File: D (Python 2.2)

from DirectGuiBase import *

class DirectFrame(DirectGuiWidget):
    
    def __init__(self, parent = None, **kw):
        optiondefs = (('pgFunc', PGItem, None), ('numStates', 1, None), ('state', self.inactiveInitState, None), ('image', None, self.setImage), ('geom', None, self.setGeom), ('text', None, self.setText), ('textMayChange', 1, None))
        self.defineoptions(kw, optiondefs, dynamicGroups = ('text', 'geom', 'image'))
        DirectGuiWidget.__init__(self, parent)
        self.initialiseoptions(DirectFrame)

    
    def destroy(self):
        DirectGuiWidget.destroy(self)

    
    def setText(self):
        if self['text'] == None:
            textList = (None,) * self['numStates']
        elif type(self['text']) == types.StringType:
            textList = (self['text'],) * self['numStates']
        else:
            textList = self['text']
        for i in range(self['numStates']):
            component = 'text' + `i`
            
            try:
                text = textList[i]
            except IndexError:
                text = textList[-1]

            if self.hascomponent(component):
                if text == None:
                    self.destroycomponent(component)
                else:
                    self[component + '_text'] = text
            elif text == None:
                return None
            else:
                OnscreenText = OnscreenText
                import OnscreenText
                self.createcomponent(component, (), 'text', OnscreenText, (), parent = self.stateNodePath[i], text = text, scale = 1, mayChange = self['textMayChange'], sort = TEXT_SORT_INDEX)
        

    
    def setGeom(self):
        if self['geom'] == None:
            geomList = (None,) * self['numStates']
        elif isinstance(self['geom'], NodePath):
            geomList = (self['geom'],) * self['numStates']
        else:
            geomList = self['geom']
        for i in range(self['numStates']):
            component = 'geom' + `i`
            
            try:
                geom = geomList[i]
            except IndexError:
                geom = geomList[-1]

            if self.hascomponent(component):
                if geom == None:
                    self.destroycomponent(component)
                else:
                    self[component + '_geom'] = geom
            elif geom == None:
                return None
            else:
                self.createcomponent(component, (), 'geom', OnscreenGeom, (), parent = self.stateNodePath[i], geom = geom, scale = 1, sort = GEOM_SORT_INDEX)
        

    
    def setImage(self):
        arg = self['image']
        if arg == None:
            imageList = (None,) * self['numStates']
        elif isinstance(arg, NodePath):
            imageList = (arg,) * self['numStates']
        elif type(arg) == types.StringType:
            imageList = (arg,) * self['numStates']
        elif len(arg) == 2 and type(arg[0]) == types.StringType and type(arg[1]) == types.StringType:
            imageList = (arg,) * self['numStates']
        else:
            imageList = arg
        for i in range(self['numStates']):
            component = 'image' + `i`
            
            try:
                image = imageList[i]
            except IndexError:
                image = imageList[-1]

            if self.hascomponent(component):
                if image == None:
                    self.destroycomponent(component)
                else:
                    self[component + '_image'] = image
            elif image == None:
                return None
            else:
                self.createcomponent(component, (), 'image', OnscreenImage, (), parent = self.stateNodePath[i], image = image, scale = 1, sort = IMAGE_SORT_INDEX)
        


