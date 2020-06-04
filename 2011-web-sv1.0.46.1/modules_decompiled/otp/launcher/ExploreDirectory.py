# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\launcher\ExploreDirectory.py
import os, sys, webbrowser, string, direct
from pandac.PandaModules import Filename

def __do_explore(dirname):
    if not os.path.isdir(dirname):
        print 'Not a directory: %s' % dirname
        return False
    if sys.platform == 'win32':
        url = dirname.replace('\\', '/')
        if len(url) > 1 and url[0] in string.letters and url[1] == ':':
            url = '/' + url
    else:
        url = dirname
    url = 'file://' + url
    print 'exploring %s' % url
    webbrowser.open(url, autoraise=True)
    sys.exit(0)


def exploreDirectory(appRunner):
    explore = appRunner.tokenDict.get('explore', '')
    if explore:
        print 'Explore token set to "%s"; not running launcher.' % explore
        if explore == 'start':
            __do_explore(os.getcwd())
        elif explore == 'log':
            __do_explore(Filename(appRunner.logDirectory).toOsSpecific())
        else:
            print 'Undefined explore token.'
            sys.exit(1)