# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\directtools\DirectGlobals.py
from pandac.PandaModules import Vec3, Point3, BitMask32
UNPICKABLE = ['x-disc-visible', 'y-disc-visible', 'z-disc-visible', 'GridBack', 'unpickable']
X_AXIS = Vec3(1, 0, 0)
Y_AXIS = Vec3(0, 1, 0)
Z_AXIS = Vec3(0, 0, 1)
NEG_X_AXIS = Vec3(-1, 0, 0)
NEG_Y_AXIS = Vec3(0, -1, 0)
NEG_Z_AXIS = Vec3(0, 0, -1)
ZERO_VEC = ORIGIN = Vec3(0)
UNIT_VEC = Vec3(1)
ZERO_POINT = Point3(0)
DIRECT_FLASH_DURATION = 1.5
MANIPULATION_MOVE_DELAY = 0.65
Q_EPSILON = 1e-10
DIRECT_NO_MOD = 0
DIRECT_SHIFT_MOD = 1
DIRECT_CONTROL_MOD = 2
DIRECT_ALT_MOD = 4
SKIP_NONE = 0
SKIP_HIDDEN = 1
SKIP_BACKFACE = 2
SKIP_CAMERA = 4
SKIP_UNPICKABLE = 8
SKIP_WIDGET = 16
SKIP_ALL = SKIP_HIDDEN | SKIP_BACKFACE | SKIP_CAMERA | SKIP_UNPICKABLE | SKIP_WIDGET
EDIT_TYPE_UNMOVABLE = 1
EDIT_TYPE_UNSCALABLE = 2
EDIT_TYPE_UNROTATABLE = 4
EDIT_TYPE_UNEDITABLE = EDIT_TYPE_UNMOVABLE | EDIT_TYPE_UNSCALABLE | EDIT_TYPE_UNROTATABLE
LE_TOP_CAM_MASK = BitMask32.bit(0)
LE_FRONT_CAM_MASK = BitMask32.bit(1)
LE_LEFT_CAM_MASK = BitMask32.bit(2)
LE_PERSP_CAM_MASK = BitMask32.bit(3)
LE_CAM_MASKS = {'persp': LE_PERSP_CAM_MASK, 'left': LE_LEFT_CAM_MASK, 'front': LE_FRONT_CAM_MASK, 'top': LE_TOP_CAM_MASK}

def LE_showInAllCam(nodePath):
    for camName in LE_CAM_MASKS.keys():
        nodePath.show(LE_CAM_MASKS[camName])


def LE_showInOneCam(nodePath, thisCamName):
    LE_showInAllCam(nodePath)
    for camName in LE_CAM_MASKS.keys():
        if camName != thisCamName:
            nodePath.hide(LE_CAM_MASKS[camName])