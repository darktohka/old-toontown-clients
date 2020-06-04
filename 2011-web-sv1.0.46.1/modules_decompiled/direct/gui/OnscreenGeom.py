# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\gui\OnscreenGeom.py
__all__ = [
 'OnscreenGeom']
from pandac.PandaModules import *
import DirectGuiGlobals as DGG
from direct.showbase.DirectObject import DirectObject
import string, types

class OnscreenGeom(DirectObject, NodePath):
    __module__ = __name__

    def __init__(self, geom=None, pos=None, hpr=None, scale=None, color=None, parent=None, sort=0):
        NodePath.__init__(self)
        if parent == None:
            parent = aspect2d
        self.setGeom(geom, parent=parent, sort=sort, color=color)
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
        return

    def setGeom(self, geom, parent=NodePath(), transform=None, sort=0, color=None):
        if not self.isEmpty():
            parent = self.getParent()
            if transform == None:
                transform = self.getTransform()
            sort = self.getSort()
            if color == None and self.hasColor():
                color = self.getColor()
        self.removeNode()
        if isinstance(geom, NodePath):
            self.assign(geom.copyTo(parent, sort))
        elif isinstance(geom, types.StringTypes):
            self.assign(loader.loadModel(geom))
            self.reparentTo(parent, sort)
        if not self.isEmpty():
            if transform:
                self.setTransform(transform.compose(self.getTransform()))
            if color:
                self.setColor(color[0], color[1], color[2], color[3])
        return

    def getGeom(self):
        return self

    def configure(self, option=None, **kw):
        for (option, value) in kw.items():
            try:
                setter = eval('self.set' + string.upper(option[0]) + option[1:])
                if (setter == self.setPos or setter == self.setHpr or setter == self.setScale) and (isinstance(value, types.TupleType) or isinstance(value, types.ListType)):
                    apply(setter, value)
                else:
                    setter(value)
            except AttributeError:
                print 'OnscreenText.configure: invalid option:', option

    def __setitem__(self, key, value):
        apply(self.configure, (), {key: value})

    def cget(self, option):
        getter = eval('self.get' + string.upper(option[0]) + option[1:])
        return getter()

    __getitem__ = cget

    def destroy(self):
        self.removeNode()