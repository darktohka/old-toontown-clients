# File: P (Python 2.2)

import types
import string
import re
import math
import operator

def ifAbsentPut(dict, key, newValue):
    if dict.has_key(key):
        return dict[key]
    else:
        dict[key] = newValue
        return newValue


def unique(L1, L2):
    continue
    L2 = []([ (k, None) for k in L2 ])
    continue
    return []


def indent(stream, numIndents, str):
    stream.write('    ' * numIndents + str)


def apropos(obj, *args):
    print 'Use pdir instead'


def getClassLineage(obj):
    if type(obj) == types.DictionaryType:
        return [
            obj]
    elif type(obj) == types.InstanceType:
        return [
            obj] + getClassLineage(obj.__class__)
    elif type(obj) == types.ClassType:
        lineage = [
            obj]
        for c in obj.__bases__:
            lineage = lineage + getClassLineage(c)
        
        return lineage
    else:
        return []


def pdir(obj, str = None, fOverloaded = 0, width = None, fTruncate = 1, lineWidth = 75, wantPrivate = 0):
    uniqueLineage = []
    for l in getClassLineage(obj):
        if type(l) == types.ClassType:
            if l in uniqueLineage:
                break
            
        
        uniqueLineage.append(l)
    
    uniqueLineage.reverse()
    for obj in uniqueLineage:
        _pdir(obj, str, fOverloaded, width, fTruncate, lineWidth, wantPrivate)
        print 
    


def _pdir(obj, str = None, fOverloaded = 0, width = None, fTruncate = 1, lineWidth = 75, wantPrivate = 0):
    
    def printHeader(name):
        name = ' ' + name + ' '
        length = len(name)
        if length < 70:
            padBefore = int((70 - length) / 2.0)
            padAfter = max(0, 70 - length - padBefore)
            header = '*' * padBefore + name + '*' * padAfter
        
        print header
        print 

    
    def printInstanceHeader(i, printHeader = printHeader):
        printHeader(i.__class__.__name__ + ' INSTANCE INFO')

    
    def printClassHeader(c, printHeader = printHeader):
        printHeader(c.__name__ + ' CLASS INFO')

    
    def printDictionaryHeader(d, printHeader = printHeader):
        printHeader('DICTIONARY INFO')

    if type(obj) == types.InstanceType:
        printInstanceHeader(obj)
    elif type(obj) == types.ClassType:
        printClassHeader(obj)
    elif type(obj) == types.DictionaryType:
        printDictionaryHeader(obj)
    
    if type(obj) == types.DictionaryType:
        dict = obj
    else:
        dict = obj.__dict__
    if width:
        maxWidth = width
    else:
        maxWidth = 10
    keyWidth = 0
    aproposKeys = []
    privateKeys = []
    remainingKeys = []
    for key in dict.keys():
        if not width:
            keyWidth = len(key)
        
        if str:
            if re.search(str, key, re.I):
                aproposKeys.append(key)
                if not width and keyWidth > maxWidth:
                    maxWidth = keyWidth
                
            
        elif key[:1] == '_':
            if wantPrivate:
                privateKeys.append(key)
                if not width and keyWidth > maxWidth:
                    maxWidth = keyWidth
                
            
        else:
            remainingKeys.append(key)
            if not width and keyWidth > maxWidth:
                maxWidth = keyWidth
            
    
    if str:
        aproposKeys.sort()
    else:
        privateKeys.sort()
        remainingKeys.sort()
    if wantPrivate:
        keys = aproposKeys + privateKeys + remainingKeys
    else:
        keys = aproposKeys + remainingKeys
    format = '%-' + `maxWidth` + 's'
    for key in keys:
        value = dict[key]
        if callable(value):
            strvalue = `Signature(value)`
        else:
            strvalue = `value`
        if fTruncate:
            strvalue = strvalue[:max(1, lineWidth - maxWidth)]
        
        print format % key[:maxWidth] + '\t' + strvalue
    

_POS_LIST = 4
_KEY_DICT = 8

def _is_variadic(function):
    return function.func_code.co_flags & _POS_LIST


def _has_keywordargs(function):
    return function.func_code.co_flags & _KEY_DICT


def _varnames(function):
    return function.func_code.co_varnames


def _getcode(f):
    
    def method_get(f):
        return (f.__name__, f.im_func)

    
    def function_get(f):
        return (f.__name__, f)

    
    def instance_get(f):
        if hasattr(f, '__call__'):
            method = f.__call__
            if type(method) == types.MethodType:
                func = method.im_func
            else:
                func = method
            return ('%s%s' % (f.__class__.__name__, '__call__'), func)
        else:
            s = 'Instance %s of class %s does not have a __call__ method' % (f, f.__class__.__name__)
            raise TypeError, s

    
    def class_get(f):
        if hasattr(f, '__init__'):
            return (f.__name__, f.__init__.im_func)
        else:
            return (f.__name__, lambda : None)

    codedict = {
        types.UnboundMethodType: method_get,
        types.MethodType: method_get,
        types.FunctionType: function_get,
        types.InstanceType: instance_get,
        types.ClassType: class_get }
    
    try:
        return codedict[type(f)](f)
    except KeyError:
        if callable(f):
            return (f.__name__, None)
        else:
            raise TypeError, 'object %s of type %s is not callable.' % (f, type(f))
    except:
        callable(f)



class Signature:
    
    def __init__(self, func):
        self.type = type(func)
        (self.name, self.func) = _getcode(func)

    
    def ordinary_args(self):
        n = self.func.func_code.co_argcount
        return _varnames(self.func)[0:n]

    
    def special_args(self):
        n = self.func.func_code.co_argcount
        x = { }
        if _is_variadic(self.func):
            x['positional'] = _varnames(self.func)[n]
            if _has_keywordargs(self.func):
                x['keyword'] = _varnames(self.func)[n + 1]
            
        elif _has_keywordargs(self.func):
            x['keyword'] = _varnames(self.func)[n]
        
        return x

    
    def full_arglist(self):
        base = list(self.ordinary_args())
        x = self.special_args()
        if x.has_key('positional'):
            base.append(x['positional'])
        
        if x.has_key('keyword'):
            base.append(x['keyword'])
        
        return base

    
    def defaults(self):
        defargs = self.func.func_defaults
        args = self.ordinary_args()
        mapping = { }
        if defargs is not None:
            for i in range(-1, -(len(defargs) + 1), -1):
                mapping[args[i]] = defargs[i]
            
        
        return mapping

    
    def __repr__(self):
        if self.func:
            defaults = self.defaults()
            specials = self.special_args()
            l = []
            for arg in self.ordinary_args():
                if defaults.has_key(arg):
                    l.append(arg + '=' + str(defaults[arg]))
                else:
                    l.append(arg)
            
            if specials.has_key('positional'):
                l.append('*' + specials['positional'])
            
            if specials.has_key('keyword'):
                l.append('**' + specials['keyword'])
            
            return '%s(%s)' % (self.name, string.join(l, ', '))
        else:
            return '%s(?)' % self.name



def aproposAll(obj):
    apropos(obj, fOverloaded = 1, fTruncate = 0)


def doc(obj):
    if isinstance(obj, types.MethodType) or isinstance(obj, types.FunctionType):
        print obj.__doc__
    


def adjust(command = None, dim = 1, parent = None, **kw):
    import Valuator
    if command:
        
        kw['command'] = lambda x: apply(command, x)
        if parent is None:
            kw['title'] = command.__name__
        
    
    kw['dim'] = dim
    if not parent:
        vg = apply(Valuator.ValuatorGroupPanel, (parent,), kw)
    else:
        vg = apply(Valuator.ValuatorGroup, (parent,), kw)
        vg.pack(expand = 1, fill = 'x')
    return vg


def intersection(a, b):
    if not a:
        return []
    
    if not b:
        return []
    
    c = a + b
    d = []
    for i in c:
        if i in a and i in b:
            if i not in d:
                d.append(i)
            
        
    
    return d


def union(a, b):
    c = a[:]
    for i in b:
        if i not in c:
            c.append(i)
        
    
    return c


def sameElements(a, b):
    if len(a) != len(b):
        return 0
    
    for elem in a:
        if elem not in b:
            return 0
        
    
    for elem in b:
        if elem not in a:
            return 0
        
    
    return 1


def contains(whole, sub):
    if whole == sub:
        return 1
    
    for elem in sub:
        if elem not in whole:
            return 0
        
    
    return 1


def replace(list, old, new, all = 0):
    if old not in list:
        return 0
    
    if not all:
        i = list.index(old)
        list[i] = new
        return 1
    else:
        numReplaced = 0
        for i in xrange(len(list)):
            if list[i] == old:
                numReplaced += 1
                list[i] = new
            
        
        return numReplaced


def reduceAngle(deg):
    return (deg + 180.0) % 360.0 - 180.0


def fitSrcAngle2Dest(src, dest):
    return dest + reduceAngle(src - dest)


def fitDestAngle2Src(src, dest):
    return src + reduceAngle(dest - src)


def closestDestAngle2(src, dest):
    diff = src - dest
    if diff > 180:
        return dest - 360
    elif diff < -180:
        return dest + 360
    else:
        return dest


def closestDestAngle(src, dest):
    diff = src - dest
    if diff > 180:
        return src - diff - 360
    elif diff < -180:
        return src - 360 + diff
    else:
        return dest


def binaryRepr(number, max_length = 32):
    shifts = map(operator.rshift, max_length * [
        number], range(max_length - 1, -1, -1))
    digits = map(operator.mod, shifts, max_length * [
        2])
    if not digits.count(1):
        return 0
    
    digits = digits[digits.index(1):]
    return string.join(map(repr, digits), '')

PyUtilProfileDefaultFilename = 'profiledata'
PyUtilProfileDefaultLines = 80
PyUtilProfileDefaultSorts = [
    'cumulative',
    'time',
    'calls']

def startProfile(filename = PyUtilProfileDefaultFilename, lines = PyUtilProfileDefaultLines, sorts = PyUtilProfileDefaultSorts, silent = 0):
    import profile
    profile.run('run()', filename)
    if not silent:
        printProfile(filename, lines, sorts)
    


def printProfile(filename = PyUtilProfileDefaultFilename, lines = PyUtilProfileDefaultLines, sorts = PyUtilProfileDefaultSorts):
    import pstats
    s = pstats.Stats(filename)
    s.strip_dirs()
    for sort in sorts:
        s.sort_stats(sort)
        s.print_stats(lines)
    


class Functor:
    
    def __init__(self, function, *args, **kargs):
        self._function = function
        self._args = args
        self._kargs = kargs

    
    def __call__(self, *args, **kargs):
        _args = list(self._args)
        _args.extend(args)
        _kargs = self._kargs.copy()
        _kargs.update(kargs)
        return apply(self._function, _args, _kargs)


