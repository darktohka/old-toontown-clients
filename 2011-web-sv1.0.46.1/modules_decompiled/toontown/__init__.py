# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\cygwin\home\toonpub\player_1_0_46_qa\toontown\__init__.py
package = 'TOONTOWN'
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


if os.getenv('CTPROJS'):
    tree = os.getenv(package)
    if not tree:
        raise StandardError, 'CTPROJS is defined, but you are not attached to %s!' % package
    tree = deCygwinify(tree)
    __path__[0] = os.path.join(tree, 'src')
    if package != 'DIRECT':
        tree = os.getenv('DIRECT')
        if not tree:
            raise StandardError, 'CTPROJS is defined, but you are not attached to DIRECT!'
        tree = deCygwinify(tree)
        (parent, base) = os.path.split(tree)
        if parent not in sys.path:
            sys.path.append(parent)
    import direct.showbase.FindCtaPaths
else:
    srcDir = os.path.join(__path__[0], 'src')
    if os.path.isdir(srcDir):
        __path__[0] = srcDir