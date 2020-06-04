# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\stdpy\thread.py
__all__ = [
 'error', 'LockType', 'start_new_thread', 'interrupt_main', 'exit', 'allocate_lock', 'get_ident', 'stack_size', 'forceYield', 'considerYield']
from pandac import PandaModules as pm
forceYield = pm.Thread.forceYield
considerYield = pm.Thread.considerYield

class error(StandardError):
    __module__ = __name__


class LockType:
    __module__ = __name__

    def __init__(self):
        self.__lock = pm.Mutex('PythonLock')
        self.__cvar = pm.ConditionVar(self.__lock)
        self.__locked = False

    def acquire(self, waitflag=1):
        self.__lock.acquire()
        try:
            if self.__locked and not waitflag:
                return False
            while self.__locked:
                self.__cvar.wait()

            self.__locked = True
            return True
        finally:
            self.__lock.release()

    def release(self):
        self.__lock.acquire()
        try:
            if not self.__locked:
                raise error, 'Releasing unheld lock.'
            self.__locked = False
            self.__cvar.notify()
        finally:
            self.__lock.release()

    def locked(self):
        return self.__locked

    __enter__ = acquire

    def __exit__(self, t, v, tb):
        self.release()


_threads = {}
_nextThreadId = 0
_threadsLock = pm.Mutex('thread._threadsLock')

def start_new_thread(function, args, kwargs={}, name=None):
    global _nextThreadId

    def threadFunc(threadId, function=function, args=args, kwargs=kwargs):
        try:
            try:
                function(*args, **kwargs)
            except SystemExit:
                pass

        finally:
            _remove_thread_id(threadId)

    _threadsLock.acquire()
    try:
        threadId = _nextThreadId
        _nextThreadId += 1
        if name is None:
            name = 'PythonThread-%s' % threadId
        thread = pm.PythonThread(threadFunc, [threadId], name, name)
        thread.setPythonData(threadId)
        _threads[threadId] = (thread, {}, None)
        thread.start(pm.TPNormal, False)
        return threadId
    finally:
        _threadsLock.release()
    return


def _add_thread(thread, wrapper):
    global _nextThreadId
    _threadsLock.acquire()
    try:
        threadId = _nextThreadId
        _nextThreadId += 1
        thread.setPythonData(threadId)
        _threads[threadId] = (thread, {}, wrapper)
        return threadId
    finally:
        _threadsLock.release()


def _get_thread_wrapper(thread, wrapperClass):
    global _nextThreadId
    threadId = thread.getPythonData()
    if threadId is None:
        _threadsLock.acquire()
        try:
            threadId = _nextThreadId
            _nextThreadId += 1
            thread.setPythonData(threadId)
            wrapper = wrapperClass(thread, threadId)
            _threads[threadId] = (thread, {}, wrapper)
            return wrapper
        finally:
            _threadsLock.release()
    else:
        _threadsLock.acquire()
        try:
            (t, locals, wrapper) = _threads[threadId]
            if wrapper is None:
                wrapper = wrapperClass(thread, threadId)
                _threads[threadId] = (thread, locals, wrapper)
            return wrapper
        finally:
            _threadsLock.release()
    return


def _get_thread_locals(thread, i):
    global _nextThreadId
    threadId = thread.getPythonData()
    if threadId is None:
        _threadsLock.acquire()
        try:
            threadId = _nextThreadId
            _nextThreadId += 1
            thread.setPythonData(threadId)
            locals = {}
            _threads[threadId] = (thread, locals, None)
            return locals.setdefault(i, {})
        finally:
            _threadsLock.release()
    else:
        _threadsLock.acquire()
        try:
            (t, locals, wrapper) = _threads[threadId]
            return locals.setdefault(i, {})
        finally:
            _threadsLock.release()
    return


def _remove_thread_id(threadId):
    _threadsLock.acquire()
    try:
        (thread, locals, wrapper) = _threads[threadId]
        del _threads[threadId]
        thread.setPythonData(None)
    finally:
        _threadsLock.release()
    return


def interrupt_main():
    pass


def exit():
    raise SystemExit


def allocate_lock():
    return LockType()


def get_ident():
    return pm.Thread.getCurrentThread().this


def stack_size(size=0):
    raise error


class _local(object):
    __module__ = __name__

    def __del__(self):
        i = id(self)
        _threadsLock.acquire()
        try:
            for (thread, locals, wrapper) in _threads.values():
                try:
                    del locals[i]
                except KeyError:
                    pass

        finally:
            _threadsLock.release()

    def __setattr__(self, key, value):
        d = _get_thread_locals(pm.Thread.getCurrentThread(), id(self))
        d[key] = value

    def __getattribute__(self, key):
        d = _get_thread_locals(pm.Thread.getCurrentThread(), id(self))
        if key == '__dict__':
            return d
        try:
            return d[key]
        except KeyError:
            return object.__getattribute__(self, key)