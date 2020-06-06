# File: O (Python 2.2)

from direct.showbase.PandaObject import *
import types

class OnscreenGeom(PandaObject, NodePath):
    
    def __init__(self, geom = None, pos = None, hpr = None, scale = None, color = None, parent = None, sort = 0):
        NodePath.__init__(self)
        if parent == None:
            parent = aspect2d
        
        self.parent = parent
        self.sort = sort
        if isinstance(geom, NodePath):
            self.assign(geom.copyTo(parent, self.sort))
        elif type(geom) == type(''):
            self.assign(loader.loadModelCopy(geom))
            self.reparentTo(parent, self.sort)
        
        if isinstance(pos, types.TupleType) or isinstance(pos, types.ListType):
            apply(self.setPos, pos)
        elif isinstance(pos, VBase3):
            self.setPos(pos)
        
        if isinstance(hpr, types.TupleType) or isinstance(hpr, types.ListType):
            apply(self.setHpr, hpr)
        elif isinstance(hpr, VBase3):
            self.setPos(hpr)
        
        if isinstance(scale, types.TupleType) or isinstance(scale, types.ListType):
            apply(self.setScale, scale)
        elif isinstance(scale, VBase3):
            self.setPos(scale)
        elif isinstance(scale, types.FloatType) or isinstance(scale, types.IntType):
            self.setScale(scale)
        
        if color:
            self.setColor(color[0], color[1], color[2], color[3])
        

    
    def setGeom(self, geom):
        self.removeNode()
        if isinstance(geom, NodePath):
            self.assign(geom.copyTo(self.parent))
        elif type(geom) == type(''):
            self.assign(loader.loadModelCopy(geom))
            self.reparentTo(self.parent)
        

    
    def getGeom(self):
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


