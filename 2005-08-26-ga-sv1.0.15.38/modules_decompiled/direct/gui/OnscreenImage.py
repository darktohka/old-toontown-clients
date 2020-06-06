# File: O (Python 2.2)

from direct.showbase.PandaObject import *
import types

class OnscreenImage(PandaObject, NodePath):
    
    def __init__(self, image = None, pos = None, hpr = None, scale = None, color = None, parent = None, sort = 0):
        NodePath.__init__(self)
        if parent == None:
            parent = aspect2d
        
        self.sort = sort
        if isinstance(image, NodePath):
            self.assign(image.copyTo(parent, sort))
        elif type(image) == type(''):
            tex = loader.loadTexture(image)
            cm = CardMaker('OnscreenImage')
            cm.setFrame(-1, 1, -1, 1)
            self.assign(parent.attachNewNode(cm.generate(), sort))
            self.setTexture(tex)
        elif type(image) == type(()):
            model = loader.loadModelOnce(image[0])
            if model:
                node = model.find(image[1])
                if node:
                    self.assign(node.copyTo(parent, sort))
                else:
                    print 'OnscreenImage: node %s not found' % image[1]
                    return None
                model.removeNode()
            else:
                print 'OnscreenImage: model %s not found' % image[0]
                return None
        
        if isinstance(pos, types.TupleType) or isinstance(pos, types.ListType):
            apply(self.setPos, pos)
        elif isinstance(pos, VBase3):
            self.setPos(pos)
        
        if isinstance(hpr, types.TupleType) or isinstance(hpr, types.ListType):
            apply(self.setHpr, hpr)
        elif isinstance(hpr, VBase3):
            self.setHpr(hpr)
        
        if isinstance(scale, types.TupleType) or isinstance(scale, types.ListType):
            apply(self.setScale, scale)
        elif isinstance(scale, VBase3):
            self.setScale(scale)
        elif isinstance(scale, types.FloatType) or isinstance(scale, types.IntType):
            self.setScale(scale)
        
        if color:
            self.setColor(color[0], color[1], color[2], color[3])
        

    
    def setImage(self, image):
        parent = self.getParent()
        self.removeNode()
        if isinstance(image, NodePath):
            self.assign(image.copyTo(parent))
        elif type(image) == type(''):
            tex = loader.loadTexture(image)
            cm = CardMaker('OnscreenImage')
            cm.setFrame(-1, 1, -1, 1)
            self.assign(parent.attachNewNode(cm.generate(), self.sort))
            self.setTexture(tex)
        elif type(image) == type(()):
            model = loader.loadModelOnce(image[0])
            self.assign(model.find(image[1]))
            self.reparentTo(parent)
            model.removeNode()
        

    
    def getImage(self):
        return self

    
    def configure(self, option = None, **kw):
        for (option, value) in kw.items():
            
            try:
                setter = eval('self.set' + string.upper(option[0]) + option[1:])
                if (setter == self.setPos and setter == self.setHpr or setter == self.setScale) and isinstance(value, types.TupleType) or isinstance(value, types.ListType):
                    apply(setter, value)
                else:
                    setter(value)
            except AttributeError:
                print 'OnscreenText.configure: invalid option:', option

        

    
    def __setitem__(self, key, value):
        apply(self.configure, (), {
            key: value })

    
    def cget(self, option):
        getter = eval('self.get' + string.upper(option[0]) + option[1:])
        return getter()

    __getitem__ = cget
    
    def destroy(self):
        self.removeNode()


