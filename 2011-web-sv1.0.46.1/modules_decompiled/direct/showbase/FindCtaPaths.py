# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\showbase\FindCtaPaths.py
__all__ = [
 'deCygwinify', 'getPaths']
import os, sys

def deCygwinify(path):
    if os.name in ['nt'] and path[0] == '/':
        dirs = path.split('/')
        if len(dirs) > 2 and len(dirs[1]) == 1:
            path = '%s:\\%s' % (dirs[1], ('\\').join(dirs[2:]))
        else:
            pandaRoot = os.getenv('PANDA_ROOT')
            if pandaRoot:
                path = os.path.normpath(pandaRoot + path)
    return path


def getPaths():
    ctprojs = os.getenv('CTPROJS')
    if ctprojs:
        print 'Appending to sys.path based on $CTPROJS:'
        packages = []
        for proj in ctprojs.split():
            projName = proj.split(':')[0]
            packages.append(projName)

        packages.reverse()
        parents = []
        for package in packages:
            tree = os.getenv(package)
            if not tree:
                print '  CTPROJS contains %s, but $%s is not defined.' % (package, package)
                sys.exit(1)
            tree = deCygwinify(tree)
            (parent, base) = os.path.split(tree)
            if base != package.lower():
                print '  Warning: $%s refers to a directory named %s (instead of %s)' % (package, base, package.lower())
            if parent not in parents:
                parents.append(parent)
            libdir = os.path.join(tree, 'built', 'lib')
            if os.path.isdir(libdir):
                if libdir not in sys.path:
                    sys.path.append(libdir)

        for parent in parents:
            print '  %s' % parent
            if parent not in sys.path:
                sys.path.append(parent)


getPaths()