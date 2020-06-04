# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\DistributedDoorEntity.py
from pandac.PandaModules import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.distributed.ClockDelta import *
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
import DistributedDoorEntityBase
from direct.fsm import FourState
from direct.fsm import ClassicFSM
from otp.level import DistributedEntity
from toontown.toonbase import TTLocalizer
from otp.level import BasicEntities
from direct.fsm import State
from otp.level import VisibilityBlocker

class DistributedDoorEntityLock(DistributedDoorEntityBase.LockBase, FourState.FourState):
    __module__ = __name__
    slideLeft = Vec3(-7.5, 0.0, 0.0)
    slideRight = Vec3(7.5, 0.0, 0.0)

    def __init__(self, door, lockIndex, lockedNodePath, leftNodePath, rightNodePath, stateIndex):
        self.door = door
        self.lockIndex = lockIndex
        self.lockedNodePath = lockedNodePath
        self.leftNodePath = leftNodePath
        self.rightNodePath = rightNodePath
        self.initialStateIndex = stateIndex
        FourState.FourState.__init__(self, self.stateNames, self.stateDurations)

    def delete(self):
        self.takedown()
        del self.door

    def setup(self):
        self.setLockState(self.initialStateIndex)
        del self.initialStateIndex

    def takedown(self):
        if self.track is not None:
            self.track.pause()
            self.track = None
        for i in self.states.keys():
            del self.states[i]

        self.states = []
        self.fsm = None
        return

    def setLockState(self, stateIndex):
        if self.stateIndex != stateIndex:
            state = self.states.get(stateIndex)
            if state is not None:
                self.fsm.request(state)
        return

    def isUnlocked(self):
        return self.isOn()

    def enterState1(self):
        FourState.FourState.enterState1(self)
        beat = self.duration * 0.05
        slideSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_arms_retracting.mp3')
        self.setTrack(Sequence(Wait(beat * 2.0), Parallel(SoundInterval(slideSfx, node=self.door.node, volume=0.8), Sequence(ShowInterval(self.leftNodePath), ShowInterval(self.rightNodePath), Parallel(LerpPosInterval(nodePath=self.leftNodePath, other=self.lockedNodePath, duration=beat * 16.0, pos=Vec3(0.0), blendType='easeIn'), LerpPosInterval(nodePath=self.rightNodePath, other=self.lockedNodePath, duration=beat * 16.0, pos=Vec3(0.0), blendType='easeIn')), HideInterval(self.leftNodePath), HideInterval(self.rightNodePath), ShowInterval(self.lockedNodePath)))))

    def enterState2(self):
        FourState.FourState.enterState2(self)
        self.setTrack(None)
        self.leftNodePath.setPos(self.lockedNodePath, Vec3(0.0))
        self.rightNodePath.setPos(self.lockedNodePath, Vec3(0.0))
        self.leftNodePath.hide()
        self.rightNodePath.hide()
        self.lockedNodePath.show()
        return

    def enterState3(self):
        FourState.FourState.enterState3(self)
        unlockSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_door_unlock.mp3')
        slideSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_arms_retracting.mp3')
        beat = self.duration * 0.05
        self.setTrack(Sequence(Wait(beat * 2), Parallel(SoundInterval(unlockSfx, node=self.door.node, volume=0.8), SoundInterval(slideSfx, node=self.door.node, volume=0.8), Sequence(HideInterval(self.lockedNodePath), ShowInterval(self.leftNodePath), ShowInterval(self.rightNodePath), Parallel(LerpPosInterval(nodePath=self.leftNodePath, other=self.lockedNodePath, duration=beat * 16, pos=self.slideLeft, blendType='easeOut'), LerpPosInterval(nodePath=self.rightNodePath, other=self.lockedNodePath, duration=beat * 16, pos=self.slideRight, blendType='easeOut')), HideInterval(self.leftNodePath), HideInterval(self.rightNodePath)))))

    def enterState4(self):
        FourState.FourState.enterState4(self)
        self.setTrack(None)
        self.leftNodePath.setPos(self.lockedNodePath, self.slideLeft)
        self.rightNodePath.setPos(self.lockedNodePath, self.slideRight)
        self.leftNodePath.hide()
        self.rightNodePath.hide()
        self.lockedNodePath.hide()
        return


class DistributedDoorEntity(DistributedDoorEntityBase.DistributedDoorEntityBase, DistributedEntity.DistributedEntity, BasicEntities.NodePathAttribsProxy, FourState.FourState, VisibilityBlocker.VisibilityBlocker):
    __module__ = __name__

    def __init__(self, cr):
        self.innerDoorsTrack = None
        self.isVisReady = 0
        self.isOuterDoorOpen = 0
        DistributedEntity.DistributedEntity.__init__(self, cr)
        FourState.FourState.__init__(self, self.stateNames, self.stateDurations)
        VisibilityBlocker.VisibilityBlocker.__init__(self)
        self.locks = []
        return

    def generate(self):
        DistributedEntity.DistributedEntity.generate(self)

    def announceGenerate(self):
        self.doorNode = hidden.attachNewNode('door-%s' % self.entId)
        DistributedEntity.DistributedEntity.announceGenerate(self)
        BasicEntities.NodePathAttribsProxy.initNodePathAttribs(self)
        self.setup()

    def disable(self):
        self.takedown()
        self.doorNode.removeNode()
        del self.doorNode
        DistributedEntity.DistributedEntity.disable(self)

    def delete(self):
        DistributedEntity.DistributedEntity.delete(self)

    def setup(self):
        self.setupDoor()
        for i in self.locks:
            i.setup()

        self.accept('exit%s' % (self.getName(),), self.exitTrigger)
        self.acceptAvatar()
        if __dev__:
            self.initWantDoors()

    def takedown(self):
        if __dev__:
            self.shutdownWantDoors()
        self.ignoreAll()
        if self.track is not None:
            self.track.finish()
        self.track = None
        if self.innerDoorsTrack is not None:
            self.innerDoorsTrack.finish()
        self.innerDoorsTrack = None
        for i in self.locks:
            i.takedown()

        self.locks = []
        self.fsm = None
        for i in self.states.keys():
            del self.states[i]

        self.states = []
        return

    setUnlock0Event = DistributedDoorEntityBase.stubFunction
    setUnlock1Event = DistributedDoorEntityBase.stubFunction
    setUnlock2Event = DistributedDoorEntityBase.stubFunction
    setUnlock3Event = DistributedDoorEntityBase.stubFunction
    setIsOpenEvent = DistributedDoorEntityBase.stubFunction
    setIsLock0Unlocked = DistributedDoorEntityBase.stubFunction
    setIsLock1Unlocked = DistributedDoorEntityBase.stubFunction
    setIsLock2Unlocked = DistributedDoorEntityBase.stubFunction
    setIsLock3Unlocked = DistributedDoorEntityBase.stubFunction
    setIsOpen = DistributedDoorEntityBase.stubFunction
    setSecondsOpen = DistributedDoorEntityBase.stubFunction

    def acceptAvatar(self):
        self.accept('enter%s' % (self.getName(),), self.enterTrigger)

    def rejectInteract(self):
        DistributedEntity.DistributedEntity.rejectInteract(self)
        self.acceptAvatar()

    def avatarExit(self, avatarId):
        DistributedEntity.DistributedEntity.avatarExit(self, avatarId)
        self.acceptAvatar()

    def enterTrigger(self, args=None):
        messenger.send('DistributedInteractiveEntity_enterTrigger')
        self.sendUpdate('requestOpen')

    def exitTrigger(self, args=None):
        messenger.send('DistributedInteractiveEntity_exitTrigger')

    def okToUnblockVis(self):
        VisibilityBlocker.VisibilityBlocker.okToUnblockVis(self)
        self.isVisReady = 1
        self.openInnerDoors()

    def changedOnState(self, isOn):
        messenger.send(self.getOutputEventName(), [not isOn])

    def setLocksState(self, stateBits):
        lock0 = stateBits & 15
        lock1 = (stateBits & 240) >> 4
        lock2 = (stateBits & 3840) >> 8
        if self.isGenerated():
            self.locks[0].setLockState(lock0)
            self.locks[1].setLockState(lock1)
            self.locks[2].setLockState(lock2)
        else:
            self.initialLock0StateIndex = lock0
            self.initialLock1StateIndex = lock1
            self.initialLock2StateIndex = lock2

    def setDoorState(self, stateIndex, timeStamp):
        self.stateTime = globalClockDelta.localElapsedTime(timeStamp)
        if self.isGenerated():
            if self.stateIndex != stateIndex:
                state = self.states.get(stateIndex)
                if state is not None:
                    self.fsm.request(state)
        else:
            self.initialState = stateIndex
            self.initialStateTimestamp = timeStamp
        return

    def getName(self):
        return 'switch-%s' % str(self.entId)

    def getNodePath(self):
        if hasattr(self, 'doorNode'):
            return self.doorNode
        return

    def setupDoor--- This code section failed: ---

 L. 415         0  LOAD_GLOBAL           0  'loader'
                3  LOAD_ATTR             1  'loadModel'
                6  LOAD_CONST               'phase_9/models/cogHQ/CogDoorHandShake'
                9  CALL_FUNCTION_1       1  None
               12  STORE_FAST            8  'model'

 L. 417        15  LOAD_FAST             8  'model'
               18  JUMP_IF_FALSE      1639  'to 1660'
               21  POP_TOP          

 L. 418        22  LOAD_FAST             8  'model'
               25  LOAD_ATTR             3  'find'
               28  LOAD_CONST               '**/Doorway1'
               31  CALL_FUNCTION_1       1  None
               34  STORE_FAST            4  'doorway'

 L. 421        37  LOAD_FAST             0  'self'
               40  LOAD_ATTR             6  'doorNode'
               43  LOAD_ATTR             7  'attachNewNode'
               46  LOAD_FAST             0  'self'
               49  LOAD_ATTR             8  'getName'
               52  CALL_FUNCTION_0       0  None
               55  LOAD_CONST               '-root'
               58  BINARY_ADD       
               59  CALL_FUNCTION_1       1  None
               62  STORE_FAST            6  'rootNode'

 L. 422        65  LOAD_FAST             6  'rootNode'
               68  LOAD_ATTR            10  'setPos'
               71  LOAD_FAST             0  'self'
               74  LOAD_ATTR            11  'pos'
               77  CALL_FUNCTION_1       1  None
               80  POP_TOP          

 L. 423        81  LOAD_FAST             6  'rootNode'
               84  LOAD_ATTR            12  'setHpr'
               87  LOAD_FAST             0  'self'
               90  LOAD_ATTR            13  'hpr'
               93  CALL_FUNCTION_1       1  None
               96  POP_TOP          

 L. 424        97  LOAD_FAST             6  'rootNode'
              100  LOAD_ATTR            14  'setScale'
              103  LOAD_FAST             0  'self'
              106  LOAD_ATTR            15  'scale'
              109  CALL_FUNCTION_1       1  None
              112  POP_TOP          

 L. 425       113  LOAD_FAST             6  'rootNode'
              116  LOAD_ATTR            16  'setColor'
              119  LOAD_FAST             0  'self'
              122  LOAD_ATTR            17  'color'
              125  CALL_FUNCTION_1       1  None
              128  POP_TOP          

 L. 427       129  LOAD_FAST             6  'rootNode'
              132  LOAD_ATTR             7  'attachNewNode'
              135  LOAD_CONST               'changePos'
              138  CALL_FUNCTION_1       1  None
              141  STORE_FAST            9  'change'

 L. 432       144  LOAD_FAST             4  'doorway'
              147  LOAD_ATTR            19  'reparentTo'
              150  LOAD_FAST             9  'change'
              153  CALL_FUNCTION_1       1  None
              156  POP_TOP          

 L. 434       157  LOAD_FAST             6  'rootNode'
              160  LOAD_FAST             0  'self'
              163  STORE_ATTR           20  'node'

 L. 435       166  LOAD_FAST             0  'self'
              169  LOAD_ATTR            20  'node'
              172  LOAD_ATTR            21  'show'
              175  CALL_FUNCTION_0       0  None
              178  POP_TOP          

 L. 437       179  LOAD_FAST             0  'self'
              182  LOAD_ATTR            22  'locks'
              185  LOAD_ATTR            23  'append'
              188  LOAD_GLOBAL          24  'DistributedDoorEntityLock'
              191  LOAD_FAST             0  'self'

 L. 439       194  LOAD_CONST               0

 L. 440       197  LOAD_FAST             4  'doorway'
              200  LOAD_ATTR             3  'find'
              203  LOAD_CONST               '**/Slide_One_Closed'
              206  CALL_FUNCTION_1       1  None

 L. 441       209  LOAD_FAST             4  'doorway'
              212  LOAD_ATTR             3  'find'
              215  LOAD_CONST               '**/Slide_One_Left_Open'
              218  CALL_FUNCTION_1       1  None

 L. 442       221  LOAD_FAST             4  'doorway'
              224  LOAD_ATTR             3  'find'
              227  LOAD_CONST               '**/Slide_One_Right_Open'
              230  CALL_FUNCTION_1       1  None

 L. 443       233  LOAD_FAST             0  'self'
              236  LOAD_ATTR            25  'initialLock0StateIndex'
              239  CALL_FUNCTION_6       6  None
              242  CALL_FUNCTION_1       1  None
              245  POP_TOP          

 L. 444       246  LOAD_FAST             0  'self'
              249  LOAD_ATTR            22  'locks'
              252  LOAD_ATTR            23  'append'
              255  LOAD_GLOBAL          24  'DistributedDoorEntityLock'
              258  LOAD_FAST             0  'self'

 L. 446       261  LOAD_CONST               1

 L. 447       264  LOAD_FAST             4  'doorway'
              267  LOAD_ATTR             3  'find'
              270  LOAD_CONST               '**/Slide_Two_Closed'
              273  CALL_FUNCTION_1       1  None

 L. 448       276  LOAD_FAST             4  'doorway'
              279  LOAD_ATTR             3  'find'
              282  LOAD_CONST               '**/Slide_Two_Left_Open'
              285  CALL_FUNCTION_1       1  None

 L. 449       288  LOAD_FAST             4  'doorway'
              291  LOAD_ATTR             3  'find'
              294  LOAD_CONST               '**/Slide_Two_Right_Open'
              297  CALL_FUNCTION_1       1  None

 L. 450       300  LOAD_FAST             0  'self'
              303  LOAD_ATTR            26  'initialLock1StateIndex'
              306  CALL_FUNCTION_6       6  None
              309  CALL_FUNCTION_1       1  None
              312  POP_TOP          

 L. 451       313  LOAD_FAST             0  'self'
              316  LOAD_ATTR            22  'locks'
              319  LOAD_ATTR            23  'append'
              322  LOAD_GLOBAL          24  'DistributedDoorEntityLock'
              325  LOAD_FAST             0  'self'

 L. 453       328  LOAD_CONST               2

 L. 454       331  LOAD_FAST             4  'doorway'
              334  LOAD_ATTR             3  'find'
              337  LOAD_CONST               '**/Slide_Three_Closed'
              340  CALL_FUNCTION_1       1  None

 L. 455       343  LOAD_FAST             4  'doorway'
              346  LOAD_ATTR             3  'find'
              349  LOAD_CONST               '**/Slide_Three_Left_Open'
              352  CALL_FUNCTION_1       1  None

 L. 456       355  LOAD_FAST             4  'doorway'
              358  LOAD_ATTR             3  'find'
              361  LOAD_CONST               '**/Slide_Three_Right_Open'
              364  CALL_FUNCTION_1       1  None

 L. 457       367  LOAD_FAST             0  'self'
              370  LOAD_ATTR            27  'initialLock2StateIndex'
              373  CALL_FUNCTION_6       6  None
              376  CALL_FUNCTION_1       1  None
              379  POP_TOP          

 L. 458       380  LOAD_FAST             0  'self'
              383  DELETE_ATTR          25  'initialLock0StateIndex'

 L. 459       386  LOAD_FAST             0  'self'
              389  DELETE_ATTR          26  'initialLock1StateIndex'

 L. 460       392  LOAD_FAST             0  'self'
              395  DELETE_ATTR          27  'initialLock2StateIndex'

 L. 464       398  LOAD_FAST             4  'doorway'
              401  LOAD_ATTR             3  'find'
              404  LOAD_CONST               'doortop'
              407  CALL_FUNCTION_1       1  None
              410  STORE_FAST            2  'door'

 L. 465       413  LOAD_FAST             2  'door'
              416  LOAD_ATTR            29  'isEmpty'
              419  CALL_FUNCTION_0       0  None
              422  JUMP_IF_FALSE        68  'to 493'
            425_0  THEN                     494
              425  POP_TOP          

 L. 466       426  LOAD_CONST               'doortop hack'
              429  PRINT_ITEM       
              430  PRINT_NEWLINE_CONT

 L. 467       431  LOAD_FAST             4  'doorway'
              434  LOAD_ATTR             7  'attachNewNode'
              437  LOAD_CONST               'doortop'
              440  CALL_FUNCTION_1       1  None
              443  STORE_FAST            2  'door'

 L. 468       446  LOAD_FAST             4  'doorway'
              449  LOAD_ATTR             3  'find'
              452  LOAD_CONST               'doortop1'
              455  CALL_FUNCTION_1       1  None
              458  LOAD_ATTR            19  'reparentTo'
              461  LOAD_FAST             2  'door'
              464  CALL_FUNCTION_1       1  None
              467  POP_TOP          

 L. 469       468  LOAD_FAST             4  'doorway'
              471  LOAD_ATTR             3  'find'
              474  LOAD_CONST               'doortop2'
              477  CALL_FUNCTION_1       1  None
              480  LOAD_ATTR            19  'reparentTo'
              483  LOAD_FAST             2  'door'
              486  CALL_FUNCTION_1       1  None
              489  POP_TOP          
              490  JUMP_FORWARD          1  'to 494'
            493_0  COME_FROM           422  '422'
              493  POP_TOP          
            494_0  COME_FROM           490  '490'

 L. 472       494  LOAD_FAST             0  'self'
              497  LOAD_ATTR             6  'doorNode'
              500  LOAD_ATTR             7  'attachNewNode'
              503  LOAD_FAST             0  'self'
              506  LOAD_ATTR             8  'getName'
              509  CALL_FUNCTION_0       0  None
              512  LOAD_CONST               '-topDoor'
              515  BINARY_ADD       
              516  CALL_FUNCTION_1       1  None
              519  STORE_FAST            6  'rootNode'

 L. 473       522  LOAD_FAST             6  'rootNode'
              525  LOAD_ATTR            10  'setPos'
              528  LOAD_FAST             0  'self'
              531  LOAD_ATTR            11  'pos'
              534  CALL_FUNCTION_1       1  None
              537  POP_TOP          

 L. 474       538  LOAD_FAST             6  'rootNode'
              541  LOAD_ATTR            12  'setHpr'
              544  LOAD_FAST             0  'self'
              547  LOAD_ATTR            13  'hpr'
              550  CALL_FUNCTION_1       1  None
              553  POP_TOP          

 L. 475       554  LOAD_FAST             6  'rootNode'
              557  LOAD_ATTR            14  'setScale'
              560  LOAD_FAST             0  'self'
              563  LOAD_ATTR            15  'scale'
              566  CALL_FUNCTION_1       1  None
              569  POP_TOP          

 L. 476       570  LOAD_FAST             6  'rootNode'
              573  LOAD_ATTR            16  'setColor'
              576  LOAD_FAST             0  'self'
              579  LOAD_ATTR            17  'color'
              582  CALL_FUNCTION_1       1  None
              585  POP_TOP          

 L. 478       586  LOAD_FAST             6  'rootNode'
              589  LOAD_ATTR             7  'attachNewNode'
              592  LOAD_CONST               'changePos'
              595  CALL_FUNCTION_1       1  None
              598  STORE_FAST            9  'change'

 L. 483       601  LOAD_FAST             2  'door'
              604  LOAD_ATTR            19  'reparentTo'
              607  LOAD_FAST             9  'change'
              610  CALL_FUNCTION_1       1  None
              613  POP_TOP          

 L. 485       614  LOAD_FAST             6  'rootNode'
              617  LOAD_FAST             0  'self'
              620  STORE_ATTR           30  'doorTop'

 L. 486       623  LOAD_FAST             0  'self'
              626  LOAD_ATTR            30  'doorTop'
              629  LOAD_ATTR            21  'show'
              632  CALL_FUNCTION_0       0  None
              635  POP_TOP          

 L. 489       636  LOAD_FAST             0  'self'
              639  LOAD_ATTR            30  'doorTop'
              642  LOAD_ATTR            31  'getParent'
              645  CALL_FUNCTION_0       0  None
              648  LOAD_ATTR             7  'attachNewNode'
              651  LOAD_FAST             0  'self'
              654  LOAD_ATTR             8  'getName'
              657  CALL_FUNCTION_0       0  None
              660  LOAD_CONST               '-leftDoor'
              663  BINARY_ADD       
              664  CALL_FUNCTION_1       1  None
              667  STORE_FAST            6  'rootNode'

 L. 490       670  LOAD_FAST             6  'rootNode'
              673  LOAD_ATTR             7  'attachNewNode'
              676  LOAD_CONST               'change'
              679  CALL_FUNCTION_1       1  None
              682  STORE_FAST            9  'change'

 L. 491       685  LOAD_FAST             4  'doorway'
              688  LOAD_ATTR             3  'find'
              691  LOAD_CONST               '**/doorLeft'
              694  CALL_FUNCTION_1       1  None
              697  STORE_FAST            2  'door'

 L. 493       700  LOAD_FAST             2  'door'
              703  LOAD_ATTR            19  'reparentTo'
              706  LOAD_FAST             9  'change'
              709  CALL_FUNCTION_1       1  None
              712  STORE_FAST            2  'door'

 L. 495       715  LOAD_FAST             6  'rootNode'
              718  LOAD_FAST             0  'self'
              721  STORE_ATTR           32  'doorLeft'

 L. 496       724  LOAD_FAST             0  'self'
              727  LOAD_ATTR            32  'doorLeft'
              730  LOAD_ATTR            21  'show'
              733  CALL_FUNCTION_0       0  None
              736  POP_TOP          

 L. 498       737  LOAD_FAST             9  'change'
              740  LOAD_ATTR            10  'setPos'
              743  LOAD_FAST             0  'self'
              746  LOAD_ATTR            11  'pos'
              749  CALL_FUNCTION_1       1  None
              752  POP_TOP          

 L. 499       753  LOAD_FAST             9  'change'
              756  LOAD_ATTR            12  'setHpr'
              759  LOAD_FAST             0  'self'
              762  LOAD_ATTR            13  'hpr'
              765  CALL_FUNCTION_1       1  None
              768  POP_TOP          

 L. 500       769  LOAD_FAST             9  'change'
              772  LOAD_ATTR            14  'setScale'
              775  LOAD_FAST             0  'self'
              778  LOAD_ATTR            15  'scale'
              781  CALL_FUNCTION_1       1  None
              784  POP_TOP          

 L. 501       785  LOAD_FAST             9  'change'
              788  LOAD_ATTR            16  'setColor'
              791  LOAD_FAST             0  'self'
              794  LOAD_ATTR            17  'color'
              797  CALL_FUNCTION_1       1  None
              800  POP_TOP          

 L. 504       801  LOAD_FAST             4  'doorway'
              804  LOAD_ATTR             3  'find'
              807  LOAD_CONST               'doorbottom'
              810  CALL_FUNCTION_1       1  None
              813  STORE_FAST            2  'door'

 L. 505       816  LOAD_FAST             2  'door'
              819  LOAD_ATTR            29  'isEmpty'
              822  CALL_FUNCTION_0       0  None
              825  JUMP_IF_FALSE        68  'to 896'
            828_0  THEN                     897
              828  POP_TOP          

 L. 506       829  LOAD_CONST               'doorbottom hack'
              832  PRINT_ITEM       
              833  PRINT_NEWLINE_CONT

 L. 507       834  LOAD_FAST             4  'doorway'
              837  LOAD_ATTR             7  'attachNewNode'
              840  LOAD_CONST               'doorbottom'
              843  CALL_FUNCTION_1       1  None
              846  STORE_FAST            2  'door'

 L. 508       849  LOAD_FAST             4  'doorway'
              852  LOAD_ATTR             3  'find'
              855  LOAD_CONST               'doorbottom1'
              858  CALL_FUNCTION_1       1  None
              861  LOAD_ATTR            19  'reparentTo'
              864  LOAD_FAST             2  'door'
              867  CALL_FUNCTION_1       1  None
              870  POP_TOP          

 L. 509       871  LOAD_FAST             4  'doorway'
              874  LOAD_ATTR             3  'find'
              877  LOAD_CONST               'doorbottom2'
              880  CALL_FUNCTION_1       1  None
              883  LOAD_ATTR            19  'reparentTo'
              886  LOAD_FAST             2  'door'
              889  CALL_FUNCTION_1       1  None
              892  POP_TOP          
              893  JUMP_FORWARD          1  'to 897'
            896_0  COME_FROM           825  '825'
              896  POP_TOP          
            897_0  COME_FROM           893  '893'

 L. 512       897  LOAD_GLOBAL          33  'render'
              900  LOAD_ATTR             7  'attachNewNode'
              903  LOAD_CONST               'changePos'
              906  CALL_FUNCTION_1       1  None
              909  STORE_FAST            9  'change'

 L. 518       912  LOAD_FAST             2  'door'
              915  LOAD_ATTR            19  'reparentTo'
              918  LOAD_FAST             9  'change'
              921  CALL_FUNCTION_1       1  None
              924  POP_TOP          

 L. 520       925  LOAD_FAST             0  'self'
              928  LOAD_ATTR             6  'doorNode'
              931  LOAD_ATTR             7  'attachNewNode'
              934  LOAD_FAST             0  'self'
              937  LOAD_ATTR             8  'getName'
              940  CALL_FUNCTION_0       0  None
              943  LOAD_CONST               '-bottomDoor'
              946  BINARY_ADD       
              947  CALL_FUNCTION_1       1  None
              950  STORE_FAST            6  'rootNode'

 L. 521       953  LOAD_FAST             6  'rootNode'
              956  LOAD_ATTR            10  'setPos'
              959  LOAD_FAST             0  'self'
              962  LOAD_ATTR            11  'pos'
              965  CALL_FUNCTION_1       1  None
              968  POP_TOP          

 L. 522       969  LOAD_FAST             6  'rootNode'
              972  LOAD_ATTR            12  'setHpr'
              975  LOAD_FAST             0  'self'
              978  LOAD_ATTR            13  'hpr'
              981  CALL_FUNCTION_1       1  None
              984  POP_TOP          

 L. 523       985  LOAD_FAST             6  'rootNode'
              988  LOAD_ATTR            14  'setScale'
              991  LOAD_FAST             0  'self'
              994  LOAD_ATTR            15  'scale'
              997  CALL_FUNCTION_1       1  None
             1000  POP_TOP          

 L. 524      1001  LOAD_FAST             6  'rootNode'
             1004  LOAD_ATTR            16  'setColor'
             1007  LOAD_FAST             0  'self'
             1010  LOAD_ATTR            17  'color'
             1013  CALL_FUNCTION_1       1  None
             1016  POP_TOP          

 L. 526      1017  LOAD_FAST             9  'change'
             1020  LOAD_ATTR            19  'reparentTo'
             1023  LOAD_FAST             6  'rootNode'
             1026  CALL_FUNCTION_1       1  None
             1029  POP_TOP          

 L. 528      1030  LOAD_FAST             6  'rootNode'
             1033  LOAD_FAST             0  'self'
             1036  STORE_ATTR           34  'doorBottom'

 L. 529      1039  LOAD_FAST             0  'self'
             1042  LOAD_ATTR            34  'doorBottom'
             1045  LOAD_ATTR            21  'show'
             1048  CALL_FUNCTION_0       0  None
             1051  POP_TOP          

 L. 532      1052  LOAD_FAST             0  'self'
             1055  LOAD_ATTR            30  'doorTop'
             1058  LOAD_ATTR            31  'getParent'
             1061  CALL_FUNCTION_0       0  None
             1064  LOAD_ATTR             7  'attachNewNode'
             1067  LOAD_FAST             0  'self'
             1070  LOAD_ATTR             8  'getName'
             1073  CALL_FUNCTION_0       0  None
             1076  LOAD_CONST               '-rightDoor'
             1079  BINARY_ADD       
             1080  CALL_FUNCTION_1       1  None
             1083  STORE_FAST            6  'rootNode'

 L. 533      1086  LOAD_FAST             6  'rootNode'
             1089  LOAD_ATTR             7  'attachNewNode'
             1092  LOAD_CONST               'change'
             1095  CALL_FUNCTION_1       1  None
             1098  STORE_FAST            9  'change'

 L. 534      1101  LOAD_FAST             4  'doorway'
             1104  LOAD_ATTR             3  'find'
             1107  LOAD_CONST               '**/doorRight'
             1110  CALL_FUNCTION_1       1  None
             1113  STORE_FAST            2  'door'

 L. 536      1116  LOAD_FAST             2  'door'
             1119  LOAD_ATTR            19  'reparentTo'
             1122  LOAD_FAST             9  'change'
             1125  CALL_FUNCTION_1       1  None
             1128  STORE_FAST            2  'door'

 L. 538      1131  LOAD_FAST             6  'rootNode'
             1134  LOAD_FAST             0  'self'
             1137  STORE_ATTR           35  'doorRight'

 L. 539      1140  LOAD_FAST             0  'self'
             1143  LOAD_ATTR            35  'doorRight'
             1146  LOAD_ATTR            21  'show'
             1149  CALL_FUNCTION_0       0  None
             1152  POP_TOP          

 L. 541      1153  LOAD_FAST             9  'change'
             1156  LOAD_ATTR            10  'setPos'
             1159  LOAD_FAST             0  'self'
             1162  LOAD_ATTR            11  'pos'
             1165  CALL_FUNCTION_1       1  None
             1168  POP_TOP          

 L. 542      1169  LOAD_FAST             9  'change'
             1172  LOAD_ATTR            12  'setHpr'
             1175  LOAD_FAST             0  'self'
             1178  LOAD_ATTR            13  'hpr'
             1181  CALL_FUNCTION_1       1  None
             1184  POP_TOP          

 L. 543      1185  LOAD_FAST             9  'change'
             1188  LOAD_ATTR            14  'setScale'
             1191  LOAD_FAST             0  'self'
             1194  LOAD_ATTR            15  'scale'
             1197  CALL_FUNCTION_1       1  None
             1200  POP_TOP          

 L. 544      1201  LOAD_FAST             9  'change'
             1204  LOAD_ATTR            16  'setColor'
             1207  LOAD_FAST             0  'self'
             1210  LOAD_ATTR            17  'color'
             1213  CALL_FUNCTION_1       1  None
             1216  POP_TOP          

 L. 548      1217  LOAD_FAST             0  'self'
             1220  LOAD_ATTR            32  'doorLeft'
             1223  LOAD_ATTR             3  'find'
             1226  LOAD_CONST               '**/doorLeft_collision1'
             1229  CALL_FUNCTION_1       1  None
             1232  STORE_FAST            3  'collision'

 L. 550      1235  LOAD_FAST             3  'collision'
             1238  LOAD_ATTR            37  'setName'
             1241  LOAD_FAST             0  'self'
             1244  LOAD_ATTR             8  'getName'
             1247  CALL_FUNCTION_0       0  None
             1250  CALL_FUNCTION_1       1  None
             1253  POP_TOP          

 L. 551      1254  LOAD_FAST             0  'self'
             1257  LOAD_ATTR            32  'doorLeft'
             1260  LOAD_ATTR             3  'find'
             1263  LOAD_CONST               '**/doorLeft_collision2'
             1266  CALL_FUNCTION_1       1  None
             1269  STORE_FAST            3  'collision'

 L. 553      1272  LOAD_FAST             3  'collision'
             1275  LOAD_ATTR            37  'setName'
             1278  LOAD_FAST             0  'self'
             1281  LOAD_ATTR             8  'getName'
             1284  CALL_FUNCTION_0       0  None
             1287  CALL_FUNCTION_1       1  None
             1290  POP_TOP          

 L. 554      1291  LOAD_FAST             0  'self'
             1294  LOAD_ATTR            35  'doorRight'
             1297  LOAD_ATTR             3  'find'
             1300  LOAD_CONST               '**/doorRight_collision1'
             1303  CALL_FUNCTION_1       1  None
             1306  STORE_FAST            3  'collision'

 L. 556      1309  LOAD_FAST             3  'collision'
             1312  LOAD_ATTR            37  'setName'
             1315  LOAD_FAST             0  'self'
             1318  LOAD_ATTR             8  'getName'
             1321  CALL_FUNCTION_0       0  None
             1324  CALL_FUNCTION_1       1  None
             1327  POP_TOP          

 L. 557      1328  LOAD_FAST             0  'self'
             1331  LOAD_ATTR            35  'doorRight'
             1334  LOAD_ATTR             3  'find'
             1337  LOAD_CONST               '**/doorRight_collision2'
             1340  CALL_FUNCTION_1       1  None
             1343  STORE_FAST            3  'collision'

 L. 559      1346  LOAD_FAST             3  'collision'
             1349  LOAD_ATTR            37  'setName'
             1352  LOAD_FAST             0  'self'
             1355  LOAD_ATTR             8  'getName'
             1358  CALL_FUNCTION_0       0  None
             1361  CALL_FUNCTION_1       1  None
             1364  POP_TOP          

 L. 561      1365  LOAD_FAST             0  'self'
             1368  LOAD_ATTR            32  'doorLeft'
             1371  LOAD_ATTR             3  'find'
             1374  LOAD_CONST               '**/doorLeft_innerCollision'
             1377  CALL_FUNCTION_1       1  None
             1380  STORE_FAST            3  'collision'

 L. 563      1383  LOAD_FAST             3  'collision'
             1386  LOAD_ATTR            37  'setName'
             1389  LOAD_FAST             0  'self'
             1392  LOAD_ATTR             8  'getName'
             1395  CALL_FUNCTION_0       0  None
             1398  CALL_FUNCTION_1       1  None
             1401  POP_TOP          

 L. 564      1402  LOAD_FAST             3  'collision'
             1405  LOAD_FAST             0  'self'
             1408  STORE_ATTR           38  'leftInnerCollision'

 L. 565      1411  LOAD_FAST             0  'self'
             1414  LOAD_ATTR            35  'doorRight'
             1417  LOAD_ATTR             3  'find'
             1420  LOAD_CONST               '**/doorRight_innerCollision'
             1423  CALL_FUNCTION_1       1  None
             1426  STORE_FAST            3  'collision'

 L. 567      1429  LOAD_FAST             3  'collision'
             1432  LOAD_ATTR            37  'setName'
             1435  LOAD_FAST             0  'self'
             1438  LOAD_ATTR             8  'getName'
             1441  CALL_FUNCTION_0       0  None
             1444  CALL_FUNCTION_1       1  None
             1447  POP_TOP          

 L. 568      1448  LOAD_FAST             3  'collision'
             1451  LOAD_FAST             0  'self'
             1454  STORE_ATTR           39  'rightInnerCollision'
             1457  JUMP_FORWARD        128  'to 1588'
             1460  POP_TOP          

 L. 586      1461  LOAD_CONST               8.0
             1464  STORE_FAST            7  'radius'

 L. 587      1467  LOAD_GLOBAL          41  'CollisionSphere'
             1470  LOAD_CONST               0.0
             1473  LOAD_CONST               0.0
             1476  LOAD_CONST               0.0
             1479  LOAD_FAST             7  'radius'
             1482  CALL_FUNCTION_4       4  None
             1485  STORE_FAST            1  'cSphere'

 L. 588      1488  LOAD_FAST             1  'cSphere'
             1491  LOAD_ATTR            43  'setTangible'
             1494  LOAD_CONST               0
             1497  CALL_FUNCTION_1       1  None
             1500  POP_TOP          

 L. 589      1501  LOAD_GLOBAL          44  'CollisionNode'
             1504  LOAD_FAST             0  'self'
             1507  LOAD_ATTR             8  'getName'
             1510  CALL_FUNCTION_0       0  None
             1513  CALL_FUNCTION_1       1  None
             1516  STORE_FAST            5  'cSphereNode'

 L. 590      1519  LOAD_FAST             5  'cSphereNode'
             1522  LOAD_ATTR            46  'addSolid'
             1525  LOAD_FAST             1  'cSphere'
             1528  CALL_FUNCTION_1       1  None
             1531  POP_TOP          

 L. 591      1532  LOAD_FAST             5  'cSphereNode'
             1535  LOAD_ATTR            47  'setFromCollideMask'
             1538  LOAD_GLOBAL          48  'BitMask32'
             1541  LOAD_ATTR            49  'allOff'
             1544  CALL_FUNCTION_0       0  None
             1547  CALL_FUNCTION_1       1  None
             1550  POP_TOP          

 L. 592      1551  LOAD_FAST             5  'cSphereNode'
             1554  LOAD_ATTR            50  'setIntoCollideMask'
             1557  LOAD_GLOBAL          51  'ToontownGlobals'
             1560  LOAD_ATTR            52  'WallBitmask'
             1563  CALL_FUNCTION_1       1  None
             1566  POP_TOP          

 L. 593      1567  LOAD_FAST             0  'self'
             1570  LOAD_ATTR            20  'node'
             1573  LOAD_ATTR             7  'attachNewNode'
             1576  LOAD_FAST             5  'cSphereNode'
             1579  CALL_FUNCTION_1       1  None
             1582  LOAD_FAST             0  'self'
             1585  STORE_ATTR           53  'cSphereNodePath'
           1588_0  COME_FROM          1457  '1457'

 L. 598      1588  LOAD_FAST             0  'self'
             1591  LOAD_ATTR            20  'node'
             1594  LOAD_ATTR            54  'flattenMedium'
             1597  CALL_FUNCTION_0       0  None
             1600  POP_TOP          

 L. 599      1601  LOAD_FAST             0  'self'
             1604  LOAD_ATTR            30  'doorTop'
             1607  LOAD_ATTR            54  'flattenMedium'
             1610  CALL_FUNCTION_0       0  None
             1613  POP_TOP          

 L. 600      1614  LOAD_FAST             0  'self'
             1617  LOAD_ATTR            34  'doorBottom'
             1620  LOAD_ATTR            54  'flattenMedium'
             1623  CALL_FUNCTION_0       0  None
             1626  POP_TOP          

 L. 601      1627  LOAD_FAST             0  'self'
             1630  LOAD_ATTR            32  'doorLeft'
             1633  LOAD_ATTR            54  'flattenMedium'
             1636  CALL_FUNCTION_0       0  None
             1639  POP_TOP          

 L. 602      1640  LOAD_FAST             0  'self'
             1643  LOAD_ATTR            35  'doorRight'
             1646  LOAD_ATTR            54  'flattenMedium'
             1649  CALL_FUNCTION_0       0  None
             1652  POP_TOP          
             1653  JUMP_ABSOLUTE      1661  'to 1661'
             1656  POP_TOP          
             1657  JUMP_FORWARD          1  'to 1661'
           1660_0  COME_FROM            18  '18'
             1660  POP_TOP          
           1661_0  COME_FROM          1657  '1657'

 L. 603      1661  LOAD_FAST             0  'self'
             1664  LOAD_ATTR            55  'setDoorState'
             1667  LOAD_FAST             0  'self'
             1670  LOAD_ATTR            56  'initialState'
             1673  LOAD_FAST             0  'self'
             1676  LOAD_ATTR            57  'initialStateTimestamp'
             1679  CALL_FUNCTION_2       2  None
             1682  POP_TOP          

 L. 604      1683  LOAD_FAST             0  'self'
             1686  DELETE_ATTR          56  'initialState'

 L. 605      1689  LOAD_FAST             0  'self'
             1692  DELETE_ATTR          57  'initialStateTimestamp'

Parse error at or near `POP_TOP' instruction at offset 1656

    def setInnerDoorsTrack(self, track):
        if self.innerDoorsTrack is not None:
            self.innerDoorsTrack.pause()
            self.innerDoorsTrack = None
        if track is not None:
            track.start(0.0)
            self.innerDoorsTrack = track
        return

    def openInnerDoors(self):
        print 'openInnerDoors'
        if not self.level.complexVis() or self.isOuterDoorOpen and (not self.isVisBlocker or self.isVisReady):
            print 'openInnerDoors stage Two'
            duration = self.duration
            slideSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_door_open_sliding.mp3')
            finalSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_door_open_final.mp3')
            moveDistance = 8.0
            self.setInnerDoorsTrack(Sequence(Func(self.leftInnerCollision.unstash), Func(self.rightInnerCollision.unstash), Parallel(SoundInterval(slideSfx, node=self.node, duration=duration * 0.4, volume=0.8), LerpPosInterval(nodePath=self.doorLeft, duration=duration * 0.4, pos=Vec3(-moveDistance, 0.0, 0.0), blendType='easeOut'), LerpPosInterval(nodePath=self.doorRight, duration=duration * 0.4, pos=Vec3(moveDistance, 0.0, 0.0), blendType='easeOut'), Sequence(Wait(duration * 0.375), SoundInterval(finalSfx, node=self.node, duration=1.0, volume=0.8))), Func(self.doorLeft.stash), Func(self.doorRight.stash)))

    def closeInnerDoors(self):
        duration = self.duration
        slideSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_door_open_sliding.mp3')
        finalSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_door_open_final.mp3')
        moveDistance = 8.0
        self.setInnerDoorsTrack(Sequence(Func(self.doorLeft.unstash), Func(self.doorRight.unstash), Parallel(SoundInterval(slideSfx, node=self.node, duration=duration * 0.4, volume=0.8), LerpPosInterval(nodePath=self.doorLeft, duration=duration * 0.4, pos=Vec3(0.0), blendType='easeIn'), LerpPosInterval(nodePath=self.doorRight, duration=duration * 0.4, pos=Vec3(0.0), blendType='easeIn'), Sequence(Wait(duration * 0.375), SoundInterval(finalSfx, node=self.node, duration=1.0, volume=0.8))), Func(self.leftInnerCollision.stash), Func(self.rightInnerCollision.stash)))

    def setisOuterDoorOpen(self, isOpen):
        self.isOuterDoorOpen = isOpen

    def enterState1(self):
        print 'doors enter state 1'
        FourState.FourState.enterState1(self)
        self.isOuterDoorOpen = 0
        if self.isVisBlocker:
            if not self.isVisReady:
                self.requestUnblockVis()
        else:
            self.okToUnblockVis()
        duration = self.duration
        slideSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_door_open_sliding.mp3')
        finalSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_door_open_final.mp3')
        moveDistance = 8.0
        self.setTrack(Sequence(Wait(duration * 0.1), Parallel(SoundInterval(slideSfx, node=self.node, duration=duration * 0.4, volume=0.8), LerpPosInterval(nodePath=self.doorTop, duration=duration * 0.4, pos=Vec3(0.0, 0.0, moveDistance), blendType='easeOut'), LerpPosInterval(nodePath=self.doorBottom, duration=duration * 0.4, pos=Vec3(0.0, 0.0, -moveDistance), blendType='easeOut'), Sequence(Wait(duration * 0.375), SoundInterval(finalSfx, node=self.node, duration=1.0, volume=0.8))), Func(self.doorTop.stash), Func(self.doorBottom.stash), Func(self.setisOuterDoorOpen, 1), Func(self.openInnerDoors)))

    def enterState2(self):
        FourState.FourState.enterState2(self)
        self.isOuterDoorOpen = 1
        self.setTrack(None)
        moveDistance = 7.5
        (self.doorTop.setPos(Vec3(0.0, 0.0, moveDistance)),)
        (self.doorBottom.setPos(Vec3(0.0, 0.0, -moveDistance)),)
        self.doorTop.stash()
        self.doorBottom.stash()
        if not self.isVisBlocker or not self.isWaitingForUnblockVis():
            self.setInnerDoorsTrack(None)
            self.doorLeft.setPos(Vec3(-moveDistance, 0.0, 0.0))
            self.doorRight.setPos(Vec3(moveDistance, 0.0, 0.0))
            self.doorLeft.stash()
            self.doorRight.stash()
        return

    def exitState2(self):
        FourState.FourState.exitState2(self)
        self.cancelUnblockVis()

    def enterState3(self):
        FourState.FourState.enterState3(self)
        duration = self.duration
        slideSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_door_open_sliding.mp3')
        finalSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_door_open_final.mp3')
        self.setTrack(Sequence(Wait(duration * 0.1), Func(self.closeInnerDoors), Wait(duration * 0.4), Func(self.doorTop.unstash), Func(self.doorBottom.unstash), Parallel(SoundInterval(slideSfx, node=self.node, duration=duration * 0.4, volume=0.8), LerpPosInterval(nodePath=self.doorTop, duration=duration * 0.4, pos=Vec3(0.0), blendType='easeIn'), LerpPosInterval(nodePath=self.doorBottom, duration=duration * 0.4, pos=Vec3(0.0), blendType='easeIn'), Sequence(Wait(duration * 0.375), SoundInterval(finalSfx, node=self.node, duration=duration * 0.4, volume=0.8))), Func(self.setisOuterDoorOpen, 0)))

    def enterState4(self):
        FourState.FourState.enterState4(self)
        self.setisOuterDoorOpen(0)
        self.isVisReady = 0
        self.setTrack(None)
        self.doorTop.unstash()
        self.doorBottom.unstash()
        self.doorTop.setPos(Vec3(0.0))
        self.doorBottom.setPos(Vec3(0.0))
        self.setInnerDoorsTrack(None)
        self.leftInnerCollision.stash()
        self.rightInnerCollision.stash()
        self.doorLeft.unstash()
        self.doorRight.unstash()
        self.doorLeft.setPos(Vec3(0.0))
        self.doorRight.setPos(Vec3(0.0))
        return

    if __dev__:

        def initWantDoors(self):
            self.accept('wantDoorsChanged', self.onWantDoorsChanged)
            self.onWantDoorsChanged()

        def shutdownWantDoors(self):
            self.ignore('wantDoorsChanged')

        def onWantDoorsChanged(self):
            if self.level.levelMgrEntity.wantDoors:
                self.getNodePath().unstash()
            else:
                self.getNodePath().stash()

        def attribChanged(self, attrib, value):
            self.takedown()
            self.setup()