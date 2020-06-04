# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\cogdominium\CogdoBarrelRoomConsts.py
from pandac.PandaModules import *
CollectionTime = 30
BarrelRoomIntroTimeout = 15.0
RewardUiTime = 5.0
EndWithAllBarrelsCollected = False
ShowRewardUI = False
AllBarrelsCollectedTime = 5.0
ToonUp = (
 2, 4)
BarrelProps = [{'pos': (-10, -66, 0), 'heading': 9}, {'pos': (-7.8, -54.5, 0), 'heading': 12}, {'pos': (-10.5, -44, 0), 'heading': 166}, {'pos': (-8.9, -33.5, 0), 'heading': 142}, {'pos': (-9.6, -19.8, 0), 'heading': 94}, {'pos': (7.8, -63.9, 0), 'heading': 169}, {'pos': (10, -44.5, 0), 'heading': 120}, {'pos': (7.4, -36.6, 0), 'heading': 127}, {'pos': (10.6, -27.5, 0), 'heading': 141}, {'pos': (10, -14.4, 0), 'heading': 2}]
StomperProps = [{'path': '**/stomper_GRP_01/stomper_cylinder_01', 'motion': 'up'}, {'path': '**/stomper_GRP_02/stomper_cylinder_034', 'motion': 'down'}, {'path': '**/stomper_GRP_03/stomper_cylinder_034', 'motion': 'up'}, {'path': '**/stomper_GRP_04/stomper_cylinder_034', 'motion': 'up'}, {'path': '**/stomper_GRP_05/stomper_cylinder_034', 'motion': 'down'}, {'path': '**/stomper_GRP_06/stomper_cylinder_034', 'motion': 'up'}, {'path': '**/stomper_GRP_07/stomper_cylinder_034', 'motion': 'down'}, {'path': '**/stomper_GRP_08/stomper_cylinder_034', 'motion': 'up'}, {'path': '**/stomper_GRP_09/stomper_cylinder_034', 'motion': 'up'}, {'path': '**/stomper_GRP_10/stomper_cylinder_034', 'motion': 'down'}, {'path': '**/stomper_GRP_11/stomper_cylinder_034', 'motion': 'up'}, {'path': '**/stomper_GRP_12/stomper_cylinder_034', 'motion': 'up'}]
StomperHaltTime = 7.3
StomperSound = 'phase_9/audio/sfx/CHQ_FACT_stomper_raise.mp3'
MaxToons = 4
BarrelRoomModel = 'phase_5/models/cogdominium/tt_m_ara_cbr_barrelRoom'
BarrelRoomModelPos = (
 0, 0, 0)
BarrelRoomElevatorOutPath = '**/elevatorOut_locator'
BarrelRoomPlayerSpawnPoints = [
 (
  -4, 0, 0, 0, 0, 0), (-2, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0), (2, 0, 0, 0, 0, 0)]
BarrelRoomCameraFar = 525.0
BarrelRoomFogColor = Vec4(0.65, 0.21, 0, 1.0)
BarrelRoomFogLinearRange = (0.0, 800.0)
BarrelModel = 'phase_5/models/cogdominium/tt_m_ara_cbr_laughBarrel'
BarrelModelScale = 1.0
BarrelCollParams = (
 0, 0, 2, 2.0)
BarrelBumpSound = 'phase_4/audio/sfx/Golf_Hit_Barrier_2.mp3'
BarrelGrabSound = 'phase_4/audio/sfx/SZ_DD_treasure.mp3'
(StateHidden, StateAvailable, StateUsed, StateCrushed) = range(4)

def numBarrels():
    return len(BarrelProps)