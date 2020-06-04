# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\cygwin\home\toonpub\player\wintools\sdk\python\Python-2.4.1\Lib\dummy_thread.py
__author__ = 'Brett Cannon'
__email__ = 'brett@python.org'
__all__ = [
 'error', 'start_new_thread', 'exit', 'get_ident', 'allocate_lock', 'interrupt_main', 'LockType']
import traceback as _traceback

class error(Exception):
    __module__ = __name__

    def __init__(self, *args):
        self.args = args


def start_new_thread(function, args, kwargs={}):
    global _interrupt
    global _main
    if type(args) != type(tuple()):
        raise TypeError('2nd arg must be a tuple')
    if type(kwargs) != type(dict()):
        raise TypeError('3rd arg must be a dict')
    _main = False
    try:
        function(*args, **kwargs)
    except SystemExit:
        pass
    except:
        _traceback.print_exc()

    _main = True
    if _interrupt:
        _interrupt = False
        raise KeyboardInterrupt


def exit():
    raise SystemExit


def get_ident():
    return -1


def allocate_lock():
    return LockType()


class LockType(object):
    __module__ = __name__

    def __init__(self):
        self.locked_status = False

    def acquire(self, waitflag=None):
        if waitflag is None:
            self.locked_status = True
            return
        elif not waitflag:
            if not self.locked_status:
                self.locked_status = True
                return True
            else:
                return False
        else:
            self.locked_status = True
            return True
        return

    def release(self):
        if not self.locked_status:
            raise error
        self.locked_status = False
        return True

    def locked(self):
        return self.locked_status


_interrupt = False
_main = True

def interrupt_main():
    global _interrupt
    if _main:
        raise KeyboardInterrupt
    else:
        _interrupt = True