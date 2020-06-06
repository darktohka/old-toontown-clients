# File: C (Python 2.2)

import CatalogItem
from pandac.PandaModules import *
import types
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator

class CatalogItemList:
    
    def __init__(self, source = None, store = 0):
        self.store = store
        self._CatalogItemList__blob = None
        self._CatalogItemList__list = None
        if isinstance(source, types.StringType):
            self._CatalogItemList__blob = source
        elif isinstance(source, types.ListType):
            self._CatalogItemList__list = source[:]
        elif isinstance(source, CatalogItemList):
            if source.store == store:
                if source._CatalogItemList__list != None:
                    self._CatalogItemList__list = source._CatalogItemList__list[:]
                
                self._CatalogItemList__blob = source._CatalogItemList__blob
            else:
                self._CatalogItemList__list = source[:]
        

    
    def markDirty(self):
        if self._CatalogItemList__list:
            self._CatalogItemList__blob = None
        

    
    def getBlob(self, store = None):
        if store == None or store == self.store:
            if self._CatalogItemList__blob == None:
                self._CatalogItemList__encodeList()
            
            return self._CatalogItemList__blob
        
        return self._CatalogItemList__makeBlob(store)

    
    def getNextDeliveryDate(self):
        nextDeliveryDate = None
        for item in self:
            if nextDeliveryDate == None or item.deliveryDate < nextDeliveryDate:
                nextDeliveryDate = item.deliveryDate
            
        
        return nextDeliveryDate

    
    def extractDeliveryItems(self, cutoffTime):
        beforeTime = []
        afterTime = []
        for item in self:
            if item.deliveryDate <= cutoffTime:
                beforeTime.append(item)
            else:
                afterTime.append(item)
        
        return (CatalogItemList(beforeTime, store = self.store), CatalogItemList(afterTime, store = self.store))

    
    def extractOldestItems(self, count):
        return (self[0:count], self[count:])

    
    def _CatalogItemList__encodeList(self):
        self._CatalogItemList__blob = self._CatalogItemList__makeBlob(self.store)

    
    def _CatalogItemList__makeBlob(self, store):
        dg = PyDatagram()
        if self._CatalogItemList__list:
            dg.addUint8(CatalogItem.CatalogItemVersion)
            for item in self._CatalogItemList__list:
                CatalogItem.encodeCatalogItem(dg, item, store)
            
        
        return dg.getMessage()

    
    def _CatalogItemList__decodeList(self):
        self._CatalogItemList__list = self._CatalogItemList__makeList(self.store)

    
    def _CatalogItemList__makeList(self, store):
        list = []
        if self._CatalogItemList__blob:
            dg = PyDatagram(self._CatalogItemList__blob)
            di = PyDatagramIterator(dg)
            versionNumber = di.getUint8()
            while di.getRemainingSize() > 0:
                item = CatalogItem.decodeCatalogItem(di, versionNumber, store)
                list.append(item)
        
        return list

    
    def append(self, item):
        if self._CatalogItemList__list == None:
            self._CatalogItemList__decodeList()
        
        self._CatalogItemList__list.append(item)
        self._CatalogItemList__blob = None

    
    def extend(self, items):
        self += items

    
    def count(self, item):
        if self._CatalogItemList__list == None:
            self._CatalogItemList__decodeList()
        
        return self._CatalogItemList__list.count(item)

    
    def index(self, item):
        if self._CatalogItemList__list == None:
            self._CatalogItemList__decodeList()
        
        return self._CatalogItemList__list.index(item)

    
    def insert(self, index, item):
        if self._CatalogItemList__list == None:
            self._CatalogItemList__decodeList()
        
        self._CatalogItemList__list.insert(index, item)
        self._CatalogItemList__blob = None

    
    def pop(self, index = None):
        if self._CatalogItemList__list == None:
            self._CatalogItemList__decodeList()
        
        self._CatalogItemList__blob = None
        if index == None:
            return self._CatalogItemList__list.pop()
        else:
            return self._CatalogItemList__list.pop(index)

    
    def remove(self, item):
        if self._CatalogItemList__list == None:
            self._CatalogItemList__decodeList()
        
        self._CatalogItemList__list.remove(item)
        self._CatalogItemList__blob = None

    
    def reverse(self):
        if self._CatalogItemList__list == None:
            self._CatalogItemList__decodeList()
        
        self._CatalogItemList__list.reverse()
        self._CatalogItemList__blob = None

    
    def sort(self, cmpfunc = None):
        if self._CatalogItemList__list == None:
            self._CatalogItemList__decodeList()
        
        if cmpfunc == None:
            self._CatalogItemList__list.sort()
        else:
            self._CatalogItemList__list.sort(cmpfunc)
        self._CatalogItemList__blob = None

    
    def __len__(self):
        if self._CatalogItemList__list == None:
            self._CatalogItemList__decodeList()
        
        return len(self._CatalogItemList__list)

    
    def __getitem__(self, index):
        if self._CatalogItemList__list == None:
            self._CatalogItemList__decodeList()
        
        return self._CatalogItemList__list[index]

    
    def __setitem__(self, index, item):
        if self._CatalogItemList__list == None:
            self._CatalogItemList__decodeList()
        
        self._CatalogItemList__list[index] = item
        self._CatalogItemList__blob = None

    
    def __delitem__(self, index):
        if self._CatalogItemList__list == None:
            self._CatalogItemList__decodeList()
        
        del self._CatalogItemList__list[index]
        self._CatalogItemList__blob = None

    
    def __getslice__(self, i, j):
        if self._CatalogItemList__list == None:
            self._CatalogItemList__decodeList()
        
        return CatalogItemList(self._CatalogItemList__list[i:j], store = self.store)

    
    def __setslice__(self, i, j, s):
        if self._CatalogItemList__list == None:
            self._CatalogItemList__decodeList()
        
        if isinstance(s, CatalogItemList):
            self._CatalogItemList__list[i:j] = s._CatalogItemList__list
        else:
            self._CatalogItemList__list[i:j] = s
        self._CatalogItemList__blob = None

    
    def __delslice__(self, i, j):
        if self._CatalogItemList__list == None:
            self._CatalogItemList__decodeList()
        
        del self._CatalogItemList__list[i:j]
        self._CatalogItemList__blob = None

    
    def __iadd__(self, other):
        if self._CatalogItemList__list == None:
            self._CatalogItemList__decodeList()
        
        self._CatalogItemList__list += list(other)
        self._CatalogItemList__blob = None
        return self

    
    def __add__(self, other):
        copy = CatalogItemList(self, store = self.store)
        copy += other
        return copy

    
    def __repr__(self):
        return self.output()

    
    def __str__(self):
        return self.output()

    
    def output(self, store = -1):
        if self._CatalogItemList__list == None:
            self._CatalogItemList__decodeList()
        
        inner = ''
        for item in self._CatalogItemList__list:
            inner += ', %s' % item.output(store)
        
        return 'CatalogItemList([%s])' % inner[2:]


