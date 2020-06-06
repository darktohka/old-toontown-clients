# File: T (Python 2.2)

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
from PandaModules import *
tempLoader = PandaLoader()
backgroundNode = tempLoader.loadSync(Filename('phase_3/models/gui/loading-background'))
import DirectGuiGlobals
print 'ToontownStart: setting default font'
import ToontownGlobals
DirectGuiGlobals.setDefaultFontFunc(ToontownGlobals.getInterfaceFont)
if launcher:
    launcher.setPandaErrorCode(7)

from ShowBaseGlobal import *
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
tempLoaderOther = ToontownLoader.ToontownLoader(base)
base.loader = tempLoaderOther
__builtin__.loader = tempLoaderOther
from DirectGui import *
serverVersion = base.config.GetString('server-version', 'no_version_set')
print 'ToontownStart: serverVersion: ', serverVersion
version = OnscreenText(serverVersion, pos = (-1.3, -0.97499999999999998), scale = 0.059999999999999998, fg = Vec4(0, 0, 1, 0.59999999999999998), align = TextNode.ALeft)
import Localizer
loader.beginBulkLoad('init', Localizer.LoaderLabel, 138, gui = 0)
from ToonBaseGlobal import *
from MessengerGlobal import *
import ToontownClientRepository
searchPath = DSearchPath()
searchPath.appendDirectory(Filename('phase_3/etc'))
searchPath.appendDirectory(Filename.fromOsSpecific(os.path.expandvars('$TOONTOWN/src/configfiles')))
dcfile = Filename('toon.dc')
if vfs:
    found = vfs.resolveFilename(dcfile, searchPath)
else:
    found = dcfile.resolveFilename(searchPath)
if not found:
    print 'ToontownStart: Could not find toon.dc file'
    sys.exit()

tcr = ToontownClientRepository.ToontownClientRepository(dcfile, serverVersion, launcher)
tcr.music = music
del music
toonbase.initNametagGlobals()
toonbase.tcr = tcr
loader.endBulkLoad('init')
if launcher:
    toonbase.startShow(tcr, launcher.getGameServer())
else:
    toonbase.startShow(tcr)
backgroundNodePath.reparentTo(hidden)
backgroundNodePath.removeNode()
del backgroundNodePath
del backgroundNode
del tempLoader
del tempLoaderOther
version.cleanup()
del version
base.loader = toonbase.loader
__builtin__.loader = toonbase.loader
if not launcher:
    run()

