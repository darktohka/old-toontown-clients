# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\launcher\StartToontownWebLauncher.py
from toontown.launcher.ToontownWebLauncher import ToontownWebLauncher
from otp.launcher.ExploreDirectory import exploreDirectory
launcher = None

def main(appRunner=None):
    global launcher
    if not appRunner:
        print 'Not running in a web environment; using dummyAppRunner.'
        from direct.p3d.AppRunner import dummyAppRunner
        from pandac.PandaModules import PandaSystem
        appRunner = dummyAppRunner()
        hostUrl = PandaSystem.getPackageHostUrl()
        appRunner.addPackageInfo('tt_3', None, None, hostUrl)
    if int(appRunner.tokenDict.get('download', '0')):
        print 'Download token set; not running launcher.'
        import sys
        sys.exit(0)
    exploreDirectory(appRunner)
    launcher = ToontownWebLauncher(appRunner)
    print 'Reached end of StartToontownWebLauncher.py.'
    return