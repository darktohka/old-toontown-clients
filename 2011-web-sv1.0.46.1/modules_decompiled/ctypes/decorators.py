# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\cygwin\home\toonpub\player_1_0_46_qa\wintools\sdk\python\Python-2.4.1\lib\site-packages\ctypes\decorators.py
import sys, ctypes
LOGGING = False

def stdcall(restype, dll, argtypes, logging=False):

    def decorate(func):
        if isinstance(dll, basestring):
            this_dll = ctypes.CDLL(dll)
        else:
            this_dll = dll
        api = ctypes.WINFUNCTYPE(restype, *argtypes)(func.func_name, this_dll)
        func._api_ = api
        if logging or LOGGING:

            def f(*args):
                result = func(*args)
                print >> sys.stderr, '# function call: %s%s -> %s' % (func.func_name, args, result)
                return result

            return f
        else:
            return func

    return decorate


def cdecl(restype, dll, argtypes, logging=False):

    def decorate(func):
        if isinstance(dll, basestring):
            this_dll = ctypes.CDLL(dll)
        else:
            this_dll = dll
        api = ctypes.CFUNCTYPE(restype, *argtypes)(func.func_name, this_dll)
        func._api_ = api
        if logging or LOGGING:

            def f(*args):
                result = func(*args)
                print >> sys.stderr, func.func_name, args, '->', result
                return result

            return f
        else:
            return func

    return decorate