# File: D (Python 2.2)

from PandaModules import *
INITOPT = [
    'initopt']
LMB = 0
MMB = 1
RMB = 2
NORMAL = 'normal'
DISABLED = 'disabled'
FLAT = PGFrameStyle.TFlat
RAISED = PGFrameStyle.TBevelOut
SUNKEN = PGFrameStyle.TBevelIn
GROOVE = PGFrameStyle.TGroove
RIDGE = PGFrameStyle.TRidge
FrameStyleDict = {
    'flat': FLAT,
    'raised': RAISED,
    'sunken': SUNKEN,
    'groove': GROOVE,
    'ridge': RIDGE }
DIALOG_NO = 0
DIALOG_OK = 1
DIALOG_YES = 1
DIALOG_RETRY = 1
DIALOG_CANCEL = -1
DESTROY = 'destroy-'
PRINT = 'print-'
ENTER = PGButton.getEnterPrefix()
EXIT = PGButton.getExitPrefix()
WITHIN = PGButton.getWithinPrefix()
WITHOUT = PGButton.getWithoutPrefix()
B1CLICK = PGButton.getClickPrefix() + MouseButton.one().getName() + '-'
B2CLICK = PGButton.getClickPrefix() + MouseButton.two().getName() + '-'
B3CLICK = PGButton.getClickPrefix() + MouseButton.three().getName() + '-'
B1PRESS = PGButton.getPressPrefix() + MouseButton.one().getName() + '-'
B2PRESS = PGButton.getPressPrefix() + MouseButton.two().getName() + '-'
B3PRESS = PGButton.getPressPrefix() + MouseButton.three().getName() + '-'
B1RELEASE = PGButton.getReleasePrefix() + MouseButton.one().getName() + '-'
B2RELEASE = PGButton.getReleasePrefix() + MouseButton.two().getName() + '-'
B3RELEASE = PGButton.getReleasePrefix() + MouseButton.three().getName() + '-'
OVERFLOW = PGEntry.getOverflowPrefix()
ACCEPT = PGEntry.getAcceptPrefix() + KeyboardButton.enter().getName() + '-'
TYPE = PGEntry.getTypePrefix()
ERASE = PGEntry.getErasePrefix()
IMAGE_SORT_INDEX = 10
GEOM_SORT_INDEX = 20
TEXT_SORT_INDEX = 30
BACKGROUND_SORT_INDEX = -100
MIDGROUND_SORT_INDEX = 0
FOREGROUND_SORT_INDEX = 100
defaultFont = None
defaultFontFunc = TextNode.getDefaultFont
defaultClickSound = None
defaultRolloverSound = None
defaultDialogGeom = None
drawOrder = 100
panel = None

def getDefaultRolloverSound():
    global defaultRolloverSound
    if defaultRolloverSound == None:
        defaultRolloverSound = base.loadSfx('audio/sfx/GUI_rollover.mp3')
    
    return defaultRolloverSound


def setDefaultRolloverSound(newSound):
    global defaultRolloverSound
    defaultRolloverSound = newSound


def getDefaultClickSound():
    global defaultClickSound
    if defaultClickSound == None:
        defaultClickSound = base.loadSfx('audio/sfx/GUI_click.mp3')
    
    return defaultClickSound


def setDefaultClickSound(newSound):
    global defaultClickSound
    defaultClickSound = newSound


def getDefaultFont():
    global defaultFont
    if defaultFont == None:
        defaultFont = defaultFontFunc()
    
    return defaultFont


def setDefaultFont(newFont):
    global defaultFont
    defaultFont = newFont


def setDefaultFontFunc(newFontFunc):
    global defaultFontFunc
    defaultFontFunc = newFontFunc


def getDefaultDialogGeom():
    global defaultDialogGeom
    if defaultDialogGeom == None:
        defaultDialogGeom = loader.loadModelOnce('models/gui/dialog_box_gui')
    
    return defaultDialogGeom


def setDefaultDialogGeom(newDialogGeom):
    global defaultDialogGeom
    defaultDialogGeom = newDialogGeom


def getDefaultDrawOrder():
    return drawOrder


def setDefaultDrawOrder(newDrawOrder):
    global drawOrder
    drawOrder = newDrawOrder


def getDefaultPanel():
    return panel


def setDefaultPanel(newPanel):
    global panel
    panel = newPanel

