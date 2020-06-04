# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\effects\PooledEffect.py
from pandac.PandaModules import *
from direct.showbase import Pool
from direct.showbase.DirectObject import DirectObject
import re

class PooledEffect(DirectObject, NodePath):
    __module__ = __name__
    pool = None
    poolLimit = 124

    @classmethod
    def getEffect(cls, context=''):
        if cls.pool is None:
            cls.pool = Pool.Pool()
        if cls.pool.hasFree():
            return cls.pool.checkout()
        else:
            (free, used) = cls.pool.getNumItems()
            if free + used < cls.poolLimit:
                cls.pool.add(cls())
                return cls.pool.checkout()
            else:
                return
        return

    @classmethod
    def cleanup(cls):
        if cls.pool:
            cls.pool.cleanup(cls.destroy)
            cls.pool = None
        return

    def __init__(self):
        NodePath.__init__(self, self.__class__.__name__)
        self.accept('clientLogout', self.__class__.cleanup)

    def destroy(self, item=None):
        if item:
            self.pool.remove(item)
        self.ignore('clientLogout')
        self.removeNode()