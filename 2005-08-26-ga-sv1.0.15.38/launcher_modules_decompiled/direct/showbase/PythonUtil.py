# File: P (Python 2.2)

import types
import string
import re
import math
import operator
import inspect
import os
import sys
import random
from direct.directutil import Verify
ScalarTypes = (types.FloatType, types.IntType, types.LongType)

def enumerate(L):
    return zip(xrange(len(L)), L)

import __builtin__
if hasattr(__builtin__, 'enumerate'):
    print 'enumerate is already present in __builtin__'
else:
    __builtin__.enumerate = enumerate

def unique(L1, L2):
    continue
    L2 = []([ (k, None) for k in L2 ])
    continue
    return []


def indent(stream, numIndents, str):
    stream.write('    ' * numIndents + str)


def writeFsmTree(instance, indent = 0):
    if hasattr(instance, 'parentFSM'):
        writeFsmTree(instance.parentFSM, indent - 2)
    elif hasattr(instance, 'fsm'):
        name = ''
        if hasattr(instance.fsm, 'state'):
            name = instance.fsm.state.name
        
        print '%s: %s' % (instance.fsm.name, name)
    


def traceFunctionCall(frame):
    f = frame
    co = f.f_code
    dict = f.f_locals
    n = co.co_argcount
    if co.co_flags & 4:
        n = n + 1
    
    if co.co_flags & 8:
        n = n + 1
    
    r = f.f_code.co_name + '('
    comma = 0
    for i in range(n):
        name = co.co_varnames[i]
        if name == 'self':
            continue
        
        if comma:
            r += ', '
        else:
            comma = 1
        r += name
        r += '='
        if dict.has_key(name):
            v = str(dict[name])
            if len(v) > 200:
                r += '<too big for debug>'
            else:
                r += str(dict[name])
        else:
            r += '*** undefined ***'
    
    return r + ')'


def traceParentCall():
    return traceFunctionCall(sys._getframe(2))


def printThisCall():
    print traceFunctionCall(sys._getframe(1))
    return 1


def tron():
    sys.settrace(trace)


def trace(frame, event, arg):
    if event == 'line':
        pass
    1
    if event == 'call':
        print traceFunctionCall(sys._getframe(1))
    elif event == 'return':
        print 'returning'
    elif event == 'exception':
        print 'exception'
    
    return trace


def troff():
    sys.settrace(None)


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
    Valuator = Valuator
    import direct.tkwidgets
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
    
    d = []
    for i in a:
        if i in b and i not in d:
            d.append(i)
        
    
    for i in b:
        if i in a and i not in d:
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


def list2dict(L, value = None):
    continue
    return []([ (k, value) for k in L ])


def invertDict(D):
    n = { }
    for (key, value) in D.items():
        n[value] = key
    
    return n


def invertDictLossless(D):
    n = { }
    for (key, value) in D.items():
        n.setdefault(value, [])
        n[value].append(key)
    
    return n


def uniqueElements(L):
    return len(L) == len(list2dict(L))


def disjoint(L1, L2):
    continue
    used = []([ (k, None) for k in L1 ])
    for k in L2:
        if k in used:
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

def startProfile(filename = PyUtilProfileDefaultFilename, lines = PyUtilProfileDefaultLines, sorts = PyUtilProfileDefaultSorts, silent = 0, callInfo = 1, cmd = 'run()'):
    import profile
    profile.run(cmd, filename)
    if not silent:
        printProfile(filename, lines, sorts, callInfo)
    


def printProfile(filename = PyUtilProfileDefaultFilename, lines = PyUtilProfileDefaultLines, sorts = PyUtilProfileDefaultSorts, callInfo = 1):
    import pstats
    s = pstats.Stats(filename)
    s.strip_dirs()
    for sort in sorts:
        s.sort_stats(sort)
        s.print_stats(lines)
        if callInfo:
            s.print_callees(lines)
            s.print_callers(lines)
        
    


class Functor:
    
    def __init__(self, function, *args, **kargs):
        self._function = function
        self._args = args
        self._kargs = kargs
        self.__name__ = 'Functor: %s' % self._function.__name__
        self.__doc__ = self._function.__doc__

    
    def __call__(self, *args, **kargs):
        _args = list(self._args)
        _args.extend(args)
        _kargs = self._kargs.copy()
        _kargs.update(kargs)
        return apply(self._function, _args, _kargs)



def bound(value, bound1, bound2):
    if bound1 > bound2:
        return min(max(value, bound2), bound1)
    else:
        return min(max(value, bound1), bound2)


def lerp(v0, v1, t):
    return v0 + t * (v1 - v0)


def average(*args):
    val = 0.0
    for arg in args:
        val += arg
    
    return val / len(args)


def addListsByValue(a, b):
    c = []
    for (x, y) in zip(a, b):
        c.append(x + y)
    
    return c


def boolEqual(a, b):
    if not a and b:
        if not a:
            pass
    return not b


def lineupPos(i, num, spacing):
    pos = float(i) * spacing
    return pos - float(spacing) * (num - 1) / 2.0


def formatElapsedSeconds(seconds):
    sign = ''
    if seconds < 0:
        seconds = -seconds
        sign = '-'
    
    seconds = math.floor(seconds)
    hours = math.floor(seconds / 60 * 60)
    if hours > 36:
        days = math.floor((hours + 12) / 24)
        return '%s%d days' % (sign, days)
    
    seconds -= hours * 60 * 60
    minutes = int(seconds / 60)
    seconds -= minutes * 60
    if hours != 0:
        return '%s%d:%02d:%02d' % (sign, hours, minutes, seconds)
    else:
        return '%s%d:%02d' % (sign, minutes, seconds)


def solveQuadratic(a, b, c):
    if a == 0.0:
        return None
    
    D = b * b - 4.0 * a * c
    if D < 0:
        return None
    elif D == 0:
        return -b / 2.0 * a
    else:
        sqrtD = math.sqrt(D)
        twoA = 2.0 * a
        root1 = (-b - sqrtD) / twoA
        root2 = (-b + sqrtD) / twoA
        return [
            root1,
            root2]


def stackEntryInfo(depth = 0, baseFileName = 1):
    
    try:
        stack = None
        frame = None
        
        try:
            stack = inspect.stack()
            frame = stack[depth + 1]
            filename = frame[1]
            if baseFileName:
                filename = os.path.basename(filename)
            
            lineNum = frame[2]
            funcName = frame[3]
            result = (filename, lineNum, funcName)
        finally:
            del stack
            del frame

    except:
        result = (None, None, None)

    return result


def lineInfo(baseFileName = 1):
    return stackEntryInfo(1)


def callerInfo(baseFileName = 1):
    return stackEntryInfo(2)


def lineTag(baseFileName = 1, verbose = 0, separator = ':'):
    (fileName, lineNum, funcName) = callerInfo()
    if fileName is None:
        return ''
    
    if verbose:
        return 'File "%s", line %s, in %s' % (fileName, lineNum, funcName)
    else:
        return '%s%s%s%s%s' % (fileName, separator, lineNum, separator, funcName)


def findPythonModule(module):
    filename = module + '.py'
    for dir in sys.path:
        pathname = os.path.join(dir, filename)
        if os.path.exists(pathname):
            return pathname
        
    
    return None


def describeException(backTrace = 4):
    
    def byteOffsetToLineno(code, byte):
        import array
        lnotab = array.array('B', code.co_lnotab)
        line = code.co_firstlineno
        for i in range(0, len(lnotab), 2):
            byte -= lnotab[i]
            if byte <= 0:
                return line
            
            line += lnotab[i + 1]
        
        return line

    infoArr = sys.exc_info()
    exception = infoArr[0]
    exceptionName = getattr(exception, '__name__', None)
    extraInfo = infoArr[1]
    trace = infoArr[2]
    stack = []
    while trace.tb_next:
        frame = trace.tb_frame
        module = frame.f_globals.get('__name__', None)
        lineno = byteOffsetToLineno(frame.f_code, frame.f_lasti)
        stack.append('%s:%s, ' % (module, lineno))
        trace = trace.tb_next
    frame = trace.tb_frame
    module = frame.f_globals.get('__name__', None)
    lineno = byteOffsetToLineno(frame.f_code, frame.f_lasti)
    stack.append('%s:%s, ' % (module, lineno))
    description = ''
    for i in range(len(stack) - 1, max(len(stack) - backTrace, 0) - 1, -1):
        description += stack[i]
    
    description += '%s: %s' % (exceptionName, extraInfo)
    return description


def mostDerivedLast(classList):
    
    def compare(a, b):
        if issubclass(a, b):
            result = 1
        elif issubclass(b, a):
            result = -1
        else:
            result = 0
        return result

    classList.sort(compare)


def clampScalar(value, a, b):
    if a < b:
        if value < a:
            return a
        elif value > b:
            return b
        else:
            return value
    elif value < b:
        return b
    elif value > a:
        return a
    else:
        return value


def weightedChoice(choiceList, rng = random.random, sum = None):
    if sum is None:
        sum = 0.0
        for (weight, item) in choiceList:
            sum += weight
        
    
    rand = rng()
    accum = rand * sum
    for (weight, item) in choiceList:
        accum -= weight
        if accum <= 0.0:
            return item
        
    
    return item


def randFloat(a, b = 0.0, rng = random.random):
    return lerp(a, b, rng())


def normalDistrib(a, b, gauss = random.gauss):
    return max(a, min(b, gauss((a + b) * 0.5, (b - a) / 6.0)))


def weightedRand(valDict, rng = random.random):
    selections = valDict.keys()
    weights = valDict.values()
    totalWeight = 0
    for weight in weights:
        totalWeight += weight
    
    randomWeight = rng() * totalWeight
    for i in range(len(weights)):
        totalWeight -= weights[i]
        if totalWeight <= randomWeight:
            return selections[i]
        
    
    return selections[-1]


def randUint31(rng = random.random):
    return int(rng() * 2147483647)


def randInt32(rng = random.random):
    i = int(rng() * 2147483647)
    if rng() < 0.5:
        i += -2147483648
    
    return i


class Enum:
    
    def __init__(self, items, start = 0):
        if type(items) == types.StringType:
            items = items.split(',')
        
        self._stringTable = { }
        i = start
        for item in items:
            item = string.strip(item)
            if len(item) == 0:
                continue
            
            self.__dict__[item] = i
            self._stringTable[i] = item
            i += 1
        

    
    def getString(self, value):
        return self._stringTable[value]

    
    def __contains__(self, value):
        return value in self._stringTable

    
    def __len__(self):
        return len(self._stringTable)



class Singleton(type):
    
    def __init__(cls, name, bases, dic):
        super(Singleton, cls).__init__(name, bases, dic)
        cls.instance = None

    
    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **args)
        
        return cls.instance



class SingletonError(ValueError):
    pass

