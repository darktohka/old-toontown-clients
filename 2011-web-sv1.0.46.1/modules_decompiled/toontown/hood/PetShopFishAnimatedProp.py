# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\hood\PetShopFishAnimatedProp.py
import AnimatedProp
from direct.actor import Actor
from direct.interval.IntervalGlobal import *

class PetShopFishAnimatedProp(AnimatedProp.AnimatedProp):
    __module__ = __name__

    def __init__(self, node):
        AnimatedProp.AnimatedProp.__init__(self, node)
        parent = node.getParent()
        self.fish = Actor.Actor(node, copy=0)
        self.fish.reparentTo(parent)
        self.fish.loadAnims({'swim': 'phase_4/models/props/exteriorfish-swim'})
        self.fish.pose('swim', 0)
        self.node = self.fish

    def delete(self):
        AnimatedProp.AnimatedProp.delete(self)
        self.fish.cleanup()
        del self.fish
        del self.node

    def enter(self):
        AnimatedProp.AnimatedProp.enter(self)
        self.fish.loop('swim')

    def exit(self):
        AnimatedProp.AnimatedProp.exit(self)
        self.fish.stop()