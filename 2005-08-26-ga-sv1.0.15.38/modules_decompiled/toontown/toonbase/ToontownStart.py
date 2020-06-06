# File: T (Python 2.2)


class game:
    name = 'toontown'
    process = 'client'

__builtins__['game'] = game()
import time
import os
import sys
import random
import __builtin__

try:
    pass
except:
    launcher = None
    __builtin__.launcher = launcher

if launcher:
    launcher.setRegistry('EXIT_PAGE', 'normal')

pollingDelay = 0.5
if launcher:
    print 'ToontownStart: Polling for game2 to finish...'
    while not launcher.getGame2Done():
        time.sleep(pollingDelay)
    print 'ToontownStart: Game2 is finished.'

print 'ToontownStart: Starting the game.'
from pandac.PandaModules import *
if launcher == None:
    http = HTTPClient()

tempLoader = PandaLoader()
backgroundNode = tempLoader.loadSync(Filename('phase_3/models/gui/loading-background'))
from direct.gui import DirectGuiGlobals
print 'ToontownStart: setting default font'
import ToontownGlobals
DirectGuiGlobals.setDefaultFontFunc(ToontownGlobals.getInterfaceFont)
if launcher:
    launcher.setPandaErrorCode(7)

import ToonBase
ToonBase.ToonBase()
from direct.showbase.ShowBaseGlobal import *
if base.win == None:
    print 'Unable to open window; aborting.'
    sys.exit()

if launcher:
    launcher.setPandaErrorCode(0)
    launcher.setPandaWindowOpen()

backgroundNodePath = aspect2d.attachNewNode(backgroundNode, 0)
backgroundNodePath.setPos(0.0, 0.0, 0.0)
backgroundNodePath.setScale(render2d, VBase3(1))
backgroundNodePath.find('**/fg').setBin('fixed', 20)
backgroundNodePath.find('**/bg').setBin('fixed', 10)
base.graphicsEngine.renderFrame()
DirectGuiGlobals.setDefaultRolloverSound(base.loadSfx('phase_3/audio/sfx/GUI_rollover.mp3'))
DirectGuiGlobals.setDefaultClickSound(base.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.mp3'))
DirectGuiGlobals.setDefaultDialogGeom(loader.loadModelOnce('phase_3/models/gui/dialog_box_gui'))
if base.musicManagerIsValid:
    music = base.musicManager.getSound('phase_3/audio/bgm/tt_theme.mid')
    if music:
        music.setLoop(1)
        music.setVolume(0.90000000000000002)
        music.play()
    
    print 'ToontownStart: Loading default gui sounds'
    DirectGuiGlobals.setDefaultRolloverSound(base.loadSfx('phase_3/audio/sfx/GUI_rollover.mp3'))
    DirectGuiGlobals.setDefaultClickSound(base.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.mp3'))
else:
    music = None
import ToontownLoader
from direct.gui.DirectGui import *
serverVersion = base.config.GetString('server-version', 'no_version_set')
print 'ToontownStart: serverVersion: ', serverVersion
version = OnscreenText(serverVersion, pos = (-1.3, -0.97499999999999998), scale = 0.059999999999999998, fg = Vec4(0, 0, 1, 0.59999999999999998), align = TextNode.ALeft)
import TTLocalizer
loader.beginBulkLoad('init', TTLocalizer.LoaderLabel, 138, 0, TTLocalizer.TIP_NONE)
from ToonBaseGlobal import *
from direct.showbase.MessengerGlobal import *
from toontown.distributed import ToontownClientRepository
searchPath = DSearchPath()
if launcher and not launcher.isDummy():
    searchPath.appendDirectory(Filename('phase_3/etc'))
else:
    searchPath.appendDirectory(Filename.fromOsSpecific(os.path.expandvars('$TOONTOWN/src/configfiles')))
    searchPath.appendDirectory(Filename.fromOsSpecific(os.path.expandvars('$OTP/src/configfiles')))
cr = ToontownClientRepository.ToontownClientRepository(serverVersion, launcher)
cr.music = music
del music
base.initNametagGlobals()
base.cr = cr
loader.endBulkLoad('init')
from otp.friends import FriendManager
from otp.distributed.OtpDoGlobals import *
cr.generateGlobalObject(OTP_DO_ID_FRIEND_MANAGER, 'FriendManager')
if launcher:
    base.startShow(cr, launcher.getGameServer())
else:
    base.startShow(cr)
backgroundNodePath.reparentTo(hidden)
backgroundNodePath.removeNode()
del backgroundNodePath
del backgroundNode
del tempLoader
version.cleanup()
del version
base.loader = base.loader
__builtin__.loader = base.loader
autoRun = ConfigVariableBool('toontown-auto-run', 1)
if autoRun and not launcher:
    
    try:
        run()
    except SystemExit:
        raise 
    except:
        from direct.showbase import PythonUtil
        print PythonUtil.describeException()
        raise 


