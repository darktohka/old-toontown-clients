# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\effects\DistributedFireworkShow.py
from direct.distributed import DistributedObject
from toontown.effects.FireworkShowMixin import FireworkShowMixin

class DistributedFireworkShow(DistributedObject.DistributedObject, FireworkShowMixin):
    __module__ = __name__
    notify = directNotify.newCategory('DistributedFireworkShow')

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        FireworkShowMixin.__init__(self)

    def generate(self):
        DistributedObject.DistributedObject.generate(self)

    def disable(self):
        DistributedObject.DistributedObject.disable(self)
        FireworkShowMixin.disable(self)

    def delete(self):
        DistributedObject.DistributedObject.delete(self)

    def d_requestFirework(self, x, y, z, style, color1, color2):
        self.sendUpdate('requestFirework', (x, y, z, style, color1, color2))