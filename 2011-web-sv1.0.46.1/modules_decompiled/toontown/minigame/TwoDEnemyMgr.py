# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\TwoDEnemyMgr.py
from pandac.PandaModules import *
from direct.directnotify import DirectNotifyGlobal
from direct.showbase.DirectObject import DirectObject
from toontown.minigame import ToonBlitzGlobals
from toontown.minigame import TwoDEnemy

class TwoDEnemyMgr(DirectObject):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('TwoDEnemyMgr')

    def __init__(self, section, enemyList):
        self.section = section
        self.enemyList = enemyList
        self.load()

    def destroy(self):
        self.section = None
        while len(self.enemies):
            enemy = self.enemies[0]
            enemy.destroy()
            self.enemies.remove(enemy)

        self.enemies = None
        return

    def load(self):
        if len(self.enemyList):
            self.enemiesNP = NodePath('Enemies')
            self.enemiesNP.reparentTo(self.section.sectionNP)
        self.enemies = []
        for index in xrange(len(self.enemyList)):
            enemyId = self.section.getSectionizedId(index)
            suitAttribs = self.enemyList[index]
            newEnemy = TwoDEnemy.TwoDEnemy(self, enemyId, suitAttribs)
            newEnemy.suit.reparentTo(self.enemiesNP)
            self.enemies.append(newEnemy)

    def enterPlay(self, elapsedTime):
        for enemy in self.enemies:
            enemy.start(elapsedTime)

    def exitPlay(self):
        pass

    def enterPause(self):
        for enemy in self.enemies:
            enemy.enterPause()

    def exitPause(self):
        for enemy in self.enemies:
            enemy.exitPause()