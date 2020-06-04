# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\cygwin\home\toonpub\player\wintools\sdk\python\Python-2.4.1\Lib\whichdb.py
import os, struct, sys
try:
    import dbm
    _dbmerror = dbm.error
except ImportError:
    dbm = None
    _dbmerror = IOError

def whichdb(filename):
    try:
        f = open(filename + os.extsep + 'pag', 'rb')
        f.close()
        if not (dbm.library == 'GNU gdbm' and sys.platform == 'os2emx'):
            f = open(filename + os.extsep + 'dir', 'rb')
            f.close()
        return 'dbm'
    except IOError:
        try:
            f = open(filename + os.extsep + 'db', 'rb')
            f.close()
            if dbm is not None:
                d = dbm.open(filename)
                d.close()
                return 'dbm'
        except (IOError, _dbmerror):
            pass

    try:
        os.stat(filename + os.extsep + 'dat')
        size = os.stat(filename + os.extsep + 'dir').st_size
        if size == 0:
            return 'dumbdbm'
        f = open(filename + os.extsep + 'dir', 'rb')
        try:
            if f.read(1) in ["'", '"']:
                return 'dumbdbm'
        finally:
            f.close()
    except (OSError, IOError):
        pass

    try:
        f = open(filename, 'rb')
    except IOError:
        return

    s16 = f.read(16)
    f.close()
    s = s16[0:4]
    if len(s) != 4:
        return ''
    try:
        (magic,) = struct.unpack('=l', s)
    except struct.error:
        return ''

    if magic == 324508366:
        return 'gdbm'
    if magic in (398689, 1628767744):
        return 'bsddb185'
    try:
        (magic,) = struct.unpack('=l', s16[-4:])
    except struct.error:
        return ''

    if magic in (398689, 1628767744):
        return 'dbhash'
    return ''


if __name__ == '__main__':
    for filename in sys.argv[1:]:
        print whichdb(filename) or 'UNKNOWN', filename