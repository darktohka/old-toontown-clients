# File: w (Python 2.2)

import UserDict
from _weakref import getweakrefcount, getweakrefs, ref, proxy, CallableProxyType, ProxyType, ReferenceType
from exceptions import ReferenceError
ProxyTypes = (ProxyType, CallableProxyType)
__all__ = [
    'ref',
    'proxy',
    'getweakrefcount',
    'getweakrefs',
    'WeakKeyDictionary',
    'ReferenceType',
    'ProxyType',
    'CallableProxyType',
    'ProxyTypes',
    'WeakValueDictionary']

class WeakValueDictionary(UserDict.UserDict):
    
    def __getitem__(self, key):
        o = self.data[key]()
        if o is None:
            raise KeyError, key
        else:
            return o

    
    def __repr__(self):
        return '<WeakValueDictionary at %s>' % id(self)

    
    def __setitem__(self, key, value):
        self.data[key] = ref(value, self._WeakValueDictionary__makeremove(key))

    
    def copy(self):
        new = WeakValueDictionary()
        for (key, wr) in self.data.items():
            o = wr()
            if o is not None:
                new[key] = o
            
        
        return new

    
    def get(self, key, default = None):
        
        try:
            wr = self.data[key]
        except KeyError:
            return default

        o = wr()
        if o is None:
            return default
        else:
            return o

    
    def items(self):
        L = []
        for (key, wr) in self.data.items():
            o = wr()
            if o is not None:
                L.append((key, o))
            
        
        return L

    
    def iteritems(self):
        return WeakValuedItemIterator(self)

    
    def iterkeys(self):
        return self.data.iterkeys()

    __iter__ = iterkeys
    
    def itervalues(self):
        return WeakValuedValueIterator(self)

    
    def popitem(self):
        while 1:
            (key, wr) = self.data.popitem()
            o = wr()
            if o is not None:
                return (key, o)
            

    
    def setdefault(self, key, default):
        
        try:
            wr = self.data[key]
        except KeyError:
            self.data[key] = ref(default, self._WeakValueDictionary__makeremove(key))
            return default

        return wr()

    
    def update(self, dict):
        d = self.data
        for (key, o) in dict.items():
            d[key] = ref(o, self._WeakValueDictionary__makeremove(key))
        

    
    def values(self):
        L = []
        for wr in self.data.values():
            o = wr()
            if o is not None:
                L.append(o)
            
        
        return L

    
    def _WeakValueDictionary__makeremove(self, key):
        
        def remove(o, selfref = ref(self), key = key):
            self = selfref()
            if self is not None:
                del self.data[key]
            

        return remove



class WeakKeyDictionary(UserDict.UserDict):
    
    def __init__(self, dict = None):
        self.data = { }
        
        def remove(k, selfref = ref(self)):
            self = selfref()
            if self is not None:
                del self.data[k]
            

        self._remove = remove
        if dict is not None:
            self.update(dict)
        

    
    def __delitem__(self, key):
        for ref in self.data.iterkeys():
            o = ref()
            if o == key:
                del self.data[ref]
                return None
            
        

    
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

    
    def get(self, key, default = None):
        return self.data.get(ref(key), default)

    
    def has_key(self, key):
        
        try:
            wr = ref(key)
        except TypeError:
            return 0

        return self.data.has_key(wr)

    
    def items(self):
        L = []
        for (key, value) in self.data.items():
            o = key()
            if o is not None:
                L.append((o, value))
            
        
        return L

    
    def iteritems(self):
        return WeakKeyedItemIterator(self)

    
    def iterkeys(self):
        return WeakKeyedKeyIterator(self)

    __iter__ = iterkeys
    
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
                return (o, value)
            

    
    def setdefault(self, key, default):
        return self.data.setdefault(ref(key, self._remove), default)

    
    def update(self, dict):
        d = self.data
        for (key, value) in dict.items():
            d[ref(key, self._remove)] = value
        



class BaseIter:
    
    def __iter__(self):
        return self



class WeakKeyedKeyIterator(BaseIter):
    
    def __init__(self, weakdict):
        self._next = weakdict.data.iterkeys().next

    
    def next(self):
        while 1:
            wr = self._next()
            obj = wr()
            if obj is not None:
                return obj
            



class WeakKeyedItemIterator(BaseIter):
    
    def __init__(self, weakdict):
        self._next = weakdict.data.iteritems().next

    
    def next(self):
        while 1:
            (wr, value) = self._next()
            key = wr()
            if key is not None:
                return (key, value)
            



class WeakValuedValueIterator(BaseIter):
    
    def __init__(self, weakdict):
        self._next = weakdict.data.itervalues().next

    
    def next(self):
        while 1:
            wr = self._next()
            obj = wr()
            if obj is not None:
                return obj
            



class WeakValuedItemIterator(BaseIter):
    
    def __init__(self, weakdict):
        self._next = weakdict.data.iteritems().next

    
    def next(self):
        while 1:
            (key, wr) = self._next()
            value = wr()
            if value is not None:
                return (key, value)
            


del UserDict
