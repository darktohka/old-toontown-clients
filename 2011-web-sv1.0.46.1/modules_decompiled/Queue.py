# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\cygwin\home\toonpub\player\wintools\sdk\python\Python-2.4.1\Lib\Queue.py
from time import time as _time
from collections import deque
__all__ = [
 'Empty', 'Full', 'Queue']

class Empty(Exception):
    __module__ = __name__


class Full(Exception):
    __module__ = __name__


class Queue:
    __module__ = __name__

    def __init__(self, maxsize=0):
        try:
            import threading
        except ImportError:
            import dummy_threading as threading

        self._init(maxsize)
        self.mutex = threading.Lock()
        self.not_empty = threading.Condition(self.mutex)
        self.not_full = threading.Condition(self.mutex)

    def qsize(self):
        self.mutex.acquire()
        n = self._qsize()
        self.mutex.release()
        return n

    def empty(self):
        self.mutex.acquire()
        n = self._empty()
        self.mutex.release()
        return n

    def full(self):
        self.mutex.acquire()
        n = self._full()
        self.mutex.release()
        return n

    def put(self, item, block=True, timeout=None):
        self.not_full.acquire()
        try:
            if not block:
                if self._full():
                    raise Full
            else:
                if timeout is None:
                    while self._full():
                        self.not_full.wait()

                elif timeout < 0:
                    raise ValueError("'timeout' must be a positive number")
                endtime = _time() + timeout
                while self._full():
                    remaining = endtime - _time()
                    if remaining <= 0.0:
                        raise Full
                    self.not_full.wait(remaining)

            self._put(item)
            self.not_empty.notify()
        finally:
            self.not_full.release()
        return

    def put_nowait(self, item):
        return self.put(item, False)

    def get(self, block=True, timeout=None):
        self.not_empty.acquire()
        try:
            if not block:
                if self._empty():
                    raise Empty
            else:
                if timeout is None:
                    while self._empty():
                        self.not_empty.wait()

                elif timeout < 0:
                    raise ValueError("'timeout' must be a positive number")
                endtime = _time() + timeout
                while self._empty():
                    remaining = endtime - _time()
                    if remaining <= 0.0:
                        raise Empty
                    self.not_empty.wait(remaining)

            item = self._get()
            self.not_full.notify()
            return item
        finally:
            self.not_empty.release()
        return

    def get_nowait(self):
        return self.get(False)

    def _init(self, maxsize):
        self.maxsize = maxsize
        self.queue = deque()

    def _qsize(self):
        return len(self.queue)

    def _empty(self):
        return not self.queue

    def _full(self):
        return self.maxsize > 0 and len(self.queue) == self.maxsize

    def _put(self, item):
        self.queue.append(item)

    def _get(self):
        return self.queue.popleft()