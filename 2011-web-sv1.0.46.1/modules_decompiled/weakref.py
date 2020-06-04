# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\cygwin\home\toonpub\player\wintools\sdk\python\Python-2.4.1\Lib\weakref.py
import UserDict
from _weakref import getweakrefcount, getweakrefs, ref, proxy, CallableProxyType, ProxyType, ReferenceType
from exceptions import ReferenceError
ProxyTypes = (
 ProxyType, CallableProxyType)
__all__ = [
 'ref', 'proxy', 'getweakrefcount', 'getweakrefs', 'WeakKeyDictionary', 'ReferenceType', 'ProxyType', 'CallableProxyType', 'ProxyTypes', 'WeakValueDictionary']

class WeakValueDictionary(UserDict.UserDict):
    __module__ = __name__

    def __init__(self, *args, **kw):
        UserDict.UserDict.__init__(self, *args, **kw)

        def remove(wr, selfref=ref(self)):
            self = selfref()
            if self is not None:
                del self.data[wr.key]
            return

        self._remove = remove

    def __getitem__(self, key):
        o = self.data[key]()
        if o is None:
            raise KeyError, key
        else:
            return o
        return

    def __contains__(self, key):
        try:
            o = self.data[key]()
        except KeyError:
            return False

        return o is not None

    def has_key(self, key):
        try:
            o = self.data[key]()
        except KeyError:
            return False

        return o is not None

    def __repr__(self):
        return '<WeakValueDictionary at %s>' % id(self)

    def __setitem__(self, key, value):
        self.data[key] = KeyedRef(value, self._remove, key)

    def copy(self):
        new = WeakValueDictionary()
        for (key, wr) in self.data.items():
            o = wr()
            if o is not None:
                new[key] = o

        return new

    def get(self, key, default=None):
        try:
            wr = self.data[key]
        except KeyError:
            return default
        else:
            o = wr()
            if o is None:
                return default
            else:
                return o

        return

    def items(self):
        L = []
        for (key, wr) in self.data.items():
            o = wr()
            if o is not None:
                L.append((key, o))

        return L

    def iteritems(self):
        for wr in self.data.itervalues():
            value = wr()
            if value is not None:
                yield (
                 wr.key, value)

        return

    def iterkeys(self):
        return self.data.iterkeys()

    def __iter__(self):
        return self.data.iterkeys()

    def itervalues(self):
        for wr in self.data.itervalues():
            obj = wr()
            if obj is not None:
                yield obj

        return

    def popitem(self):
        while 1:
            (key, wr) = self.data.popitem()
            o = wr()
            if o is not None:
                return (
                 key, o)

        return

    def pop(self, key, *args):
        try:
            o = self.data.pop(key)()
        except KeyError:
            if args:
                return args[0]
            raise

        if o is None:
            raise KeyError, key
        else:
            return o
        return

    def setdefault(self, key, default=None):
        try:
            wr = self.data[key]
        except KeyError:
            self.data[key] = KeyedRef(default, self._remove, key)
            return default
        else:
            return wr()

    def update(self, dict=None, **kwargs):
        d = self.data
        if dict is not None:
            if not hasattr(dict, 'items'):
                dict = type({})(dict)
            for (key, o) in dict.items():
                d[key] = KeyedRef(o, self._remove, key)

        if len(kwargs):
            self.update(kwargs)
        return

    def values(self):
        L = []
        for wr in self.data.values():
            o = wr()
            if o is not None:
                L.append(o)

        return L


class KeyedRef(ref):
    __module__ = __name__
    __slots__ = ('key', )

    def __new__(type, ob, callback, key):
        self = ref.__new__(type, ob, callback)
        self.key = key
        return self

    def __init__(self, ob, callback, key):
        super(KeyedRef, self).__init__(ob, callback)


class WeakKeyDictionary(UserDict.UserDict):
    __module__ = __name__

    def __init__(self, dict=None):
        self.data = {}

        def remove(k, selfref=ref(self)):
            self = selfref()
            if self is not None:
                del self.data[k]
            return

        self._remove = remove
        if dict is not None:
            self.update(dict)
        return

    def __delitem__(self, key):
        del self.data[ref(key)]

    def __getitem__(self, key):
        return self.data[ref(key)]

    def __repr__(self):
        return '<WeakKeyDictionary at %s>' % id(self)

    def __setitem__(self, key, value):
        self.data[ref(key, self._remove)] = value

    def copy(self):
        new = WeakKeyDictionary()
        for (key, value) in self.data.items():
            o = key()
            if o is not None:
                new[o] = value

        return new

    def get(self, key, default=None):
        return self.data.get(ref(key), default)

    def has_key(self, key):
        try:
            wr = ref(key)
        except TypeError:
            return 0

        return wr in self.data

    def __contains__(self, key):
        try:
            wr = ref(key)
        except TypeError:
            return 0

        return wr in self.data

    def items(self):
        L = []
        for (key, value) in self.data.items():
            o = key()
            if o is not None:
                L.append((o, value))

        return L

    def iteritems(self):
        for (wr, value) in self.data.iteritems():
            key = wr()
            if key is not None:
                yield (
                 key, value)

        return

    def iterkeys(self):
        for wr in self.data.iterkeys():
            obj = wr()
            if obj is not None:
                yield obj

        return

    def __iter__(self):
        return self.iterkeys()

    def itervalues(self):
        return self.data.itervalues()

    def keys(self):
        L = []
        for wr in self.data.keys():
            o = wr()
            if o is not None:
                L.append(o)

        return L

    def popitem(self):
        while 1:
            (key, value) = self.data.popitem()
            o = key()
            if o is not None:
                return (
                 o, value)

        return

    def pop(self, key, *args):
        return self.data.pop(ref(key), *args)

    def setdefault(self, key, default=None):
        return self.data.setdefault(ref(key, self._remove), default)

    def update(self, dict=None, **kwargs):
        d = self.data
        if dict is not None:
            if not hasattr(dict, 'items'):
                dict = type({})(dict)
            for (key, value) in dict.items():
                d[ref(key, self._remove)] = value

        if len(kwargs):
            self.update(kwargs)
        return