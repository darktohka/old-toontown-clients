# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\directutil\Verify.py
wantVerifyPdb = 0

def verify(assertion):
    if not assertion:
        print '\n\nverify failed:'
        import sys
        print '    File "%s", line %d' % (sys._getframe(1).f_code.co_filename, sys._getframe(1).f_lineno)
        if wantVerifyPdb:
            import pdb
            pdb.set_trace()
        raise AssertionError


if not hasattr(__builtins__, 'verify'):
    __builtins__['verify'] = verify