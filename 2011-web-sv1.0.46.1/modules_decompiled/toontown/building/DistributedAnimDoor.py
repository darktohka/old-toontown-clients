# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\building\DistributedAnimDoor.py
from pandac.PandaModules import NodePath, VBase3
from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import Parallel, Sequence, Wait, HprInterval, LerpHprInterval, SoundInterval
from toontown.building import DistributedDoor
from toontown.building import DoorTypes
if __debug__:
    import pdb

class DistributedAnimDoor(DistributedDoor.DistributedDoor):
    __module__ = __name__

    def __init__(self, cr):
        DistributedDoor.DistributedDoor.__init__(self, cr)
        base.animDoor = self

    def getBuilding(self):
        if not self.__dict__.has_key('building'):
            if self.doorType == DoorTypes.EXT_ANIM_STANDARD:
                searchStr = '**/??' + str(self.block) + ':animated_building_*_DNARoot;+s'
                self.notify.debug('searchStr=%s' % searchStr)
                self.building = self.cr.playGame.hood.loader.geom.find(searchStr)
            else:
                self.notify.error('DistributedAnimDoor.getBuiding with doorType=%s' % self.doorType)
        return self.building

    def getDoorNodePath(self):
        if self.doorType == DoorTypes.EXT_ANIM_STANDARD:
            if hasattr(self, 'tempDoorNodePath'):
                return self.tempDoorNodePath
            else:
                building = self.getBuilding()
                doorNP = building.find('**/door_origin')
                self.notify.debug('creating doorOrigin at %s %s' % (str(doorNP.getPos()), str(doorNP.getHpr())))
                otherNP = NodePath('doorOrigin')
                otherNP.setPos(doorNP.getPos())
                otherNP.setHpr(doorNP.getHpr())
                otherNP.reparentTo(doorNP.getParent())
                self.tempDoorNodePath = otherNP
        else:
            self.notify.error('DistributedAnimDoor.getDoorNodePath with doorType=%s' % self.doorType)
        return otherNP

    def setTriggerName(self):
        if self.doorType == DoorTypes.EXT_ANIM_STANDARD:
            building = self.getBuilding()
            if not building.isEmpty():
                doorTrigger = building.find('**/door_0_door_trigger')
                if not doorTrigger.isEmpty():
                    doorTrigger.node().setName(self.getTriggerName())
            else:
                self.notify.warning('setTriggerName failed no building')
        else:
            self.notify.error('setTriggerName doorTYpe=%s' % self.doorType)

    def getAnimBuilding--- This code section failed: ---

 L.  89         0  LOAD_FAST             0  'self'
                3  LOAD_ATTR             1  '__dict__'
                6  LOAD_ATTR             2  'has_key'
                9  LOAD_CONST               'animBuilding'
               12  CALL_FUNCTION_1       1  None
               15  JUMP_IF_TRUE        209  'to 227'
             18_0  THEN                     228
               18  POP_TOP          

 L.  90        19  LOAD_FAST             0  'self'
               22  LOAD_ATTR             3  'doorType'
               25  LOAD_GLOBAL           4  'DoorTypes'
               28  LOAD_ATTR             5  'EXT_ANIM_STANDARD'
               31  COMPARE_OP            2  ==
               34  JUMP_IF_FALSE       157  'to 194'
             37_0  THEN                     224
               37  POP_TOP          

 L.  93        38  LOAD_FAST             0  'self'
               41  LOAD_ATTR             6  'getBuilding'
               44  CALL_FUNCTION_0       0  None
               47  STORE_FAST            2  'bldg'

 L.  94        50  LOAD_FAST             2  'bldg'
               53  LOAD_ATTR             8  'getParent'
               56  CALL_FUNCTION_0       0  None
               59  LOAD_ATTR             8  'getParent'
               62  CALL_FUNCTION_0       0  None
               65  STORE_FAST            4  'key'

 L.  95        68  LOAD_FAST             0  'self'
               71  LOAD_ATTR            10  'cr'
               74  LOAD_ATTR            11  'playGame'
               77  LOAD_ATTR            12  'hood'
               80  LOAD_ATTR            13  'loader'
               83  LOAD_ATTR            14  'animPropDict'
               86  LOAD_ATTR            15  'get'
               89  LOAD_FAST             4  'key'
               92  CALL_FUNCTION_1       1  None
               95  STORE_FAST            1  'animPropList'

 L.  97        98  LOAD_FAST             1  'animPropList'
              101  JUMP_IF_FALSE        60  'to 164'
              104  POP_TOP          

 L.  98       105  SETUP_LOOP           83  'to 191'
              108  LOAD_FAST             1  'animPropList'
              111  GET_ITER         
              112  FOR_ITER             45  'to 160'
              115  STORE_FAST            3  'prop'

 L. 100       118  LOAD_FAST             2  'bldg'
              121  LOAD_FAST             3  'prop'
              124  LOAD_ATTR            18  'getActor'
              127  CALL_FUNCTION_0       0  None
              130  LOAD_ATTR             8  'getParent'
              133  CALL_FUNCTION_0       0  None
              136  COMPARE_OP            2  ==
              139  JUMP_IF_FALSE        14  'to 156'
              142  POP_TOP          

 L. 101       143  LOAD_FAST             3  'prop'
              146  LOAD_FAST             0  'self'
              149  STORE_ATTR           19  'animBuilding'

 L. 102       152  BREAK_LOOP       
              153  JUMP_BACK           112  'to 112'
            156_0  COME_FROM           139  '139'
              156  POP_TOP          
              157  JUMP_BACK           112  'to 112'
              160  POP_BLOCK        
              161  JUMP_ABSOLUTE       224  'to 224'
            164_0  COME_FROM           101  '101'
              164  POP_TOP          

 L. 104       165  LOAD_FAST             0  'self'
              168  LOAD_ATTR            20  'notify'
              171  LOAD_ATTR            21  'error'
              174  LOAD_CONST               'could not find'
              177  LOAD_GLOBAL          22  'str'
              180  LOAD_FAST             4  'key'
              183  CALL_FUNCTION_1       1  None
              186  BINARY_ADD       
              187  CALL_FUNCTION_1       1  None
              190  POP_TOP          
            191_0  COME_FROM           105  '105'
              191  JUMP_ABSOLUTE       228  'to 228'
            194_0  COME_FROM            34  '34'
              194  POP_TOP          

 L. 106       195  LOAD_FAST             0  'self'
              198  LOAD_ATTR            20  'notify'
              201  LOAD_ATTR            21  'error'
              204  LOAD_CONST               'No such door type as '
              207  LOAD_GLOBAL          22  'str'
              210  LOAD_FAST             0  'self'
              213  LOAD_ATTR             3  'doorType'
              216  CALL_FUNCTION_1       1  None
              219  BINARY_ADD       
              220  CALL_FUNCTION_1       1  None
              223  POP_TOP          
              224  JUMP_FORWARD          1  'to 228'
            227_0  COME_FROM            15  '15'
              227  POP_TOP          
            228_0  COME_FROM           224  '224'

 L. 109       228  LOAD_FAST             0  'self'
              231  LOAD_ATTR            19  'animBuilding'
              234  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `JUMP_ABSOLUTE' instruction at offset 191

    def getBuildingActor(self):
        result = self.getAnimBuilding().getActor()
        return result

    def enterOpening(self, ts):
        bldgActor = self.getBuildingActor()
        rightDoor = bldgActor.controlJoint(None, 'modelRoot', 'def_right_door')
        if rightDoor.isEmpty():
            self.notify.warning('enterOpening(): did not find rightDoor')
            return
        otherNP = self.getDoorNodePath()
        trackName = 'doorOpen-%d' % self.doId
        if self.rightSwing:
            h = 100
        else:
            h = -100
        self.finishDoorTrack()
        self.doorTrack = Parallel(SoundInterval(self.openSfx, node=rightDoor), Sequence(HprInterval(rightDoor, VBase3(0, 0, 0)), Wait(0.4), LerpHprInterval(nodePath=rightDoor, duration=0.6, hpr=VBase3(h, 0, 0), startHpr=VBase3(0, 0, 0), blendType='easeInOut')), name=trackName)
        self.doorTrack.start(ts)
        return

    def enterClosing(self, ts):
        bldgActor = self.getBuildingActor()
        rightDoor = bldgActor.controlJoint(None, 'modelRoot', 'def_right_door')
        if rightDoor.isEmpty():
            self.notify.warning('enterClosing(): did not find rightDoor')
            return
        otherNP = self.getDoorNodePath()
        trackName = 'doorClose-%d' % self.doId
        if self.rightSwing:
            h = 100
        else:
            h = -100
        self.finishDoorTrack()
        self.doorTrack = Sequence(LerpHprInterval(nodePath=rightDoor, duration=1.0, hpr=VBase3(0, 0, 0), startHpr=VBase3(h, 0, 0), blendType='easeInOut'), SoundInterval(self.closeSfx, node=rightDoor), name=trackName)
        self.doorTrack.start(ts)
        if hasattr(self, 'done'):
            request = self.getRequestStatus()
            messenger.send('doorDoneEvent', [request])
        return

    def exitDoorEnterOpening(self, ts):
        bldgActor = self.getBuildingActor()
        leftDoor = bldgActor.controlJoint(None, 'modelRoot', 'def_left_door')
        if self.leftSwing:
            h = -100
        else:
            h = 100
        if not leftDoor.isEmpty():
            otherNP = self.getDoorNodePath()
            trackName = 'doorDoorExitTrack-%d' % self.doId
            self.finishDoorExitTrack()
            self.doorExitTrack = Parallel(SoundInterval(self.openSfx, node=leftDoor), Sequence(LerpHprInterval(nodePath=leftDoor, duration=0.6, hpr=VBase3(h, 0, 0), startHpr=VBase3(0, 0, 0), blendType='easeInOut')), name=trackName)
            self.doorExitTrack.start(ts)
        else:
            self.notify.warning('exitDoorEnterOpening(): did not find leftDoor')
        return

    def exitDoorEnterClosing(self, ts):
        bldgActor = self.getBuildingActor()
        leftDoor = bldgActor.controlJoint(None, 'modelRoot', 'def_left_door')
        if self.leftSwing:
            h = -100
        else:
            h = 100
        if not leftDoor.isEmpty():
            otherNP = self.getDoorNodePath()
            trackName = 'doorExitTrack-%d' % self.doId
            self.finishDoorExitTrack()
            self.doorExitTrack = Sequence(LerpHprInterval(nodePath=leftDoor, duration=1.0, hpr=VBase3(0, 0, 0), startHpr=VBase3(h, 0, 0), blendType='easeInOut'), SoundInterval(self.closeSfx, node=leftDoor), name=trackName)
            self.doorExitTrack.start(ts)
        return