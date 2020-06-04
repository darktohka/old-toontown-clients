# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\building\DistributedAnimBuilding.py
from pandac.PandaModules import DecalEffect, DepthWriteAttrib
from direct.directnotify import DirectNotifyGlobal
from toontown.building import DistributedBuilding

class DistributedAnimBuilding(DistributedBuilding.DistributedBuilding):
    __module__ = __name__

    def __init__(self, cr):
        DistributedBuilding.DistributedBuilding.__init__(self, cr)

    def enterToon(self, ts):
        DistributedBuilding.DistributedBuilding.enterToon(self, ts)
        self.fixEffects()

    def fixEffects(self):
        nodes = self.getNodePaths()
        for curNode in nodes:
            mf = curNode.find('**/*mesh_front*')
            sign_joint = curNode.find('**/sign_origin_joint')
            if not sign_joint.isEmpty():
                self.notify.debug('I found sign_origin_joint 1')
            if not mf.isEmpty():
                sign = mf.find('**/sign')
                mf.clearEffect(DecalEffect.getClassType())
                if not sign.isEmpty():
                    sign.setDepthWrite(1, 1)
                    sign.setEffect(DecalEffect.make())
                    sign_joint = curNode.find('**/sign_origin_joint')
                    allSignJoints = curNode.findAllMatches('**/sign_origin_joint')
                    num = allSignJoints.getNumPaths()
                    if num:
                        sign_joint = allSignJoints.getPath(num - 1)
                    if not sign_joint.isEmpty():
                        self.notify.debug('I found sign_origin_joint 2')
                        sign.wrtReparentTo(sign_joint)

    def setupNametag(self):
        if not self.wantsNametag():
            return
        DistributedBuilding.DistributedBuilding.setupNametag(self)

    def getSbSearchString(self):
        result = 'landmarkBlocks/sb' + str(self.block) + ':*animated_building_*_DNARoot'
        return result

    def adjustSbNodepathScale(self, nodePath):
        nodePath.setScale(0.543667, 1, 1)

    def animToToon(self, timeStamp):
        DistributedBuilding.DistributedBuilding.animToToon(self, timeStamp)
        self.fixEffects()