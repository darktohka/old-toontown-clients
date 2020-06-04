# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\showbase\ContainerReport.py
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.showbase.PythonUtil import Queue, fastRepr, invertDictLossless
from direct.showbase.PythonUtil import itype, safeRepr
from direct.showbase.Job import Job
import types

class ContainerReport(Job):
    __module__ = __name__
    notify = directNotify.newCategory('ContainerReport')
    PrivateIds = set()

    def __init__(self, name, log=False, limit=None, threaded=False):
        Job.__init__(self, name)
        self._log = log
        self._limit = limit
        self._visitedIds = set()
        self._id2pathStr = {}
        self._id2container = {}
        self._type2id2len = {}
        self._instanceDictIds = set()
        self._queue = Queue()
        jobMgr.add(self)
        if threaded == False:
            jobMgr.finish(self)

    def destroy(self):
        del self._queue
        del self._instanceDictIds
        del self._type2id2len
        del self._id2container
        del self._id2pathStr
        del self._visitedIds
        del self._limit
        del self._log

    def finished(self):
        if self._log:
            self.destroy()

    def run(self):
        ContainerReport.PrivateIds.update(set([id(ContainerReport.PrivateIds), id(self._visitedIds), id(self._id2pathStr), id(self._id2container), id(self._type2id2len), id(self._queue), id(self._instanceDictIds)]))
        try:
            base
        except:
            pass
        else:
            self._enqueueContainer(base.__dict__, 'base')

        try:
            simbase
        except:
            pass
        else:
            self._enqueueContainer(simbase.__dict__, 'simbase')

        self._queue.push(__builtins__)
        self._id2pathStr[id(__builtins__)] = ''
        while len(self._queue) > 0:
            yield None
            parentObj = self._queue.pop()
            isInstanceDict = False
            if id(parentObj) in self._instanceDictIds:
                isInstanceDict = True
            try:
                if parentObj.__class__.__name__ == 'method-wrapper':
                    continue
            except:
                pass

            if type(parentObj) in (types.StringType, types.UnicodeType):
                continue
            if type(parentObj) in (types.ModuleType, types.InstanceType):
                child = parentObj.__dict__
                if self._examine(child):
                    self._instanceDictIds.add(id(child))
                    self._id2pathStr[id(child)] = str(self._id2pathStr[id(parentObj)])
                continue
            if type(parentObj) is types.DictType:
                key = None
                attr = None
                keys = parentObj.keys()
                try:
                    keys.sort()
                except TypeError, e:
                    self.notify.warning('non-sortable dict keys: %s: %s' % (self._id2pathStr[id(parentObj)], repr(e)))
                else:
                    for key in keys:
                        try:
                            attr = parentObj[key]
                        except KeyError, e:
                            self.notify.warning('could not index into %s with key %s' % (self._id2pathStr[id(parentObj)], key))

                        if id(attr) not in self._visitedIds:
                            self._visitedIds.add(id(attr))
                            if self._examine(attr):
                                if parentObj is __builtins__:
                                    self._id2pathStr[id(attr)] = key
                                elif isInstanceDict:
                                    self._id2pathStr[id(attr)] = self._id2pathStr[id(parentObj)] + '.%s' % key
                                else:
                                    self._id2pathStr[id(attr)] = self._id2pathStr[id(parentObj)] + '[%s]' % safeRepr(key)

                    del key
                    del attr
                    continue
            if type(parentObj) is not types.FileType:
                try:
                    itr = iter(parentObj)
                except:
                    pass
                else:
                    try:
                        index = 0
                        while 1:
                            try:
                                attr = itr.next()
                            except:
                                attr = None
                                break

                            if id(attr) not in self._visitedIds:
                                self._visitedIds.add(id(attr))
                                if self._examine(attr):
                                    self._id2pathStr[id(attr)] = self._id2pathStr[id(parentObj)] + '[%s]' % index
                            index += 1

                        del attr
                    except StopIteration, e:
                        pass
                    else:
                        del itr
                        continue
            try:
                childNames = dir(parentObj)
            except:
                pass
            else:
                childName = None
                child = None
                for childName in childNames:
                    child = getattr(parentObj, childName)
                    if id(child) not in self._visitedIds:
                        self._visitedIds.add(id(child))
                        if self._examine(child):
                            self._id2pathStr[id(child)] = self._id2pathStr[id(parentObj)] + '.%s' % childName

                del childName
                del child
                continue

        if self._log:
            self.printingBegin()
            for i in self._output(limit=self._limit):
                yield None

            self.printingEnd()
        yield Job.Done
        return

    def _enqueueContainer(self, obj, pathStr=None):
        self._queue.push(obj)
        objId = id(obj)
        if pathStr is not None:
            self._id2pathStr[objId] = pathStr
        try:
            length = len(obj)
        except:
            length = None

        if length is not None and length > 0:
            self._id2container[objId] = obj
            self._type2id2len.setdefault(type(obj), {})
            self._type2id2len[type(obj)][objId] = length
        return

    def _examine(self, obj):
        if type(obj) in (types.BooleanType, types.BuiltinFunctionType, types.BuiltinMethodType, types.ComplexType, types.FloatType, types.IntType, types.LongType, types.NoneType, types.NotImplementedType, types.TypeType, types.CodeType, types.FunctionType):
            return False
        if id(obj) in ContainerReport.PrivateIds:
            return False
        self._enqueueContainer(obj)
        return True

    def _outputType(self, type, limit=None):
        if type not in self._type2id2len:
            return
        len2ids = invertDictLossless(self._type2id2len[type])
        lengths = len2ids.keys()
        lengths.sort()
        lengths.reverse()
        print '====='
        print '===== %s' % type
        count = 0
        stop = False
        for l in lengths:
            pathStrList = list()
            for id in len2ids[l]:
                obj = self._id2container[id]
                pathStrList.append(self._id2pathStr[id])
                count += 1
                if count & 127 == 0:
                    yield None

            pathStrList.sort()
            for pathstr in pathStrList:
                print '%s: %s' % (l, pathstr)

            if limit is not None and count >= limit:
                return

        return

    def _output(self, **kArgs):
        print "===== ContainerReport: '%s' =====" % (self._name,)
        initialTypes = (types.DictType, types.ListType, types.TupleType)
        for type in initialTypes:
            for i in self._outputType(type, **kArgs):
                yield None

        otherTypes = list(set(self._type2id2len.keys()).difference(set(initialTypes)))
        otherTypes.sort()
        for type in otherTypes:
            for i in self._outputType(type, **kArgs):
                yield None

        return

    def log(self, **kArgs):
        self._output(**kArgs)