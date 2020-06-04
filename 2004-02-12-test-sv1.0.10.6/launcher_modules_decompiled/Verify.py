# File: V (Python 2.2)

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

