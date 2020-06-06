# File: s (Python 2.2)

import string
import sys
from sre_constants import *
SPECIAL_CHARS = '.\\[{()*+?^$|'
REPEAT_CHARS = '*+?{'
DIGITS = tuple('0123456789')
OCTDIGITS = tuple('01234567')
HEXDIGITS = tuple('0123456789abcdefABCDEF')
WHITESPACE = tuple(' \t\n\r\xb\xc')
ESCAPES = {
    '\\a': (LITERAL, ord('\x7')),
    '\\b': (LITERAL, ord('\x8')),
    '\\f': (LITERAL, ord('\xc')),
    '\\n': (LITERAL, ord('\n')),
    '\\r': (LITERAL, ord('\r')),
    '\\t': (LITERAL, ord('\t')),
    '\\v': (LITERAL, ord('\xb')),
    '\\\\': (LITERAL, ord('\\')) }
CATEGORIES = {
    '\\A': (AT, AT_BEGINNING_STRING),
    '\\b': (AT, AT_BOUNDARY),
    '\\B': (AT, AT_NON_BOUNDARY),
    '\\d': (IN, [
        (CATEGORY, CATEGORY_DIGIT)]),
    '\\D': (IN, [
        (CATEGORY, CATEGORY_NOT_DIGIT)]),
    '\\s': (IN, [
        (CATEGORY, CATEGORY_SPACE)]),
    '\\S': (IN, [
        (CATEGORY, CATEGORY_NOT_SPACE)]),
    '\\w': (IN, [
        (CATEGORY, CATEGORY_WORD)]),
    '\\W': (IN, [
        (CATEGORY, CATEGORY_NOT_WORD)]),
    '\\Z': (AT, AT_END_STRING) }
FLAGS = {
    'i': SRE_FLAG_IGNORECASE,
    'L': SRE_FLAG_LOCALE,
    'm': SRE_FLAG_MULTILINE,
    's': SRE_FLAG_DOTALL,
    'x': SRE_FLAG_VERBOSE,
    't': SRE_FLAG_TEMPLATE,
    'u': SRE_FLAG_UNICODE }

try:
    int('10', 8)
    atoi = int
except TypeError:
    atoi = string.atoi


class Pattern:
    
    def __init__(self):
        self.flags = 0
        self.open = []
        self.groups = 1
        self.groupdict = { }

    
    def opengroup(self, name = None):
        gid = self.groups
        self.groups = gid + 1
        if name:
            ogid = self.groupdict.get(name, None)
            if ogid is not None:
                raise error, 'redefinition of group name %s as group %d; was group %d' % (repr(name), gid, ogid)
            
            self.groupdict[name] = gid
        
        self.open.append(gid)
        return gid

    
    def closegroup(self, gid):
        self.open.remove(gid)

    
    def checkgroup(self, gid):
        if gid < self.groups:
            pass
        return gid not in self.open



class SubPattern:
    
    def __init__(self, pattern, data = None):
        self.pattern = pattern
        if not data:
            data = []
        
        self.data = data
        self.width = None

    
    def dump(self, level = 0):
        nl = 1
        for (op, av) in self.data:
            print level * '  ' + opnl = 0if op == 'in':
                print 
                nl = 1
                for (op, a) in av:
                    print (level + 1) * '  ' + op, a
                
            elif op == 'branch':
                print 
                nl = 1
                i = 0
                for a in av[1]:
                    if i > 0:
                        print level * '  ' + 'or'
                    
                    a.dump(level + 1)
                    nl = 1
                    i = i + 1
                
            elif type(av) in (type(()), type([])):
                for a in av:
                    if isinstance(a, SubPattern):
                        if not nl:
                            print 
                        
                        a.dump(level + 1)
                        nl = 1
                    else:
                        print anl = 0,
                
            else:
                print avnl = 0,
            if not nl:
                print 
            
        

    
    def __repr__(self):
        return repr(self.data)

    
    def __len__(self):
        return len(self.data)

    
    def __delitem__(self, index):
        del self.data[index]

    
    def __getitem__(self, index):
        return self.data[index]

    
    def __setitem__(self, index, code):
        self.data[index] = code

    
    def __getslice__(self, start, stop):
        return SubPattern(self.pattern, self.data[start:stop])

    
    def insert(self, index, code):
        self.data.insert(index, code)

    
    def append(self, code):
        self.data.append(code)

    
    def getwidth(self):
        if self.width:
            return self.width
        
        lo = 0x0L
        hi = 0x0L
        for (op, av) in self.data:
            if op is BRANCH:
                i = sys.maxint
                j = 0
                for av in av[1]:
                    (l, h) = av.getwidth()
                    i = min(i, l)
                    j = max(j, h)
                
                lo = lo + i
                hi = hi + j
            elif op is CALL:
                (i, j) = av.getwidth()
                lo = lo + i
                hi = hi + j
            elif op is SUBPATTERN:
                (i, j) = av[1].getwidth()
                lo = lo + i
                hi = hi + j
            elif op in (MIN_REPEAT, MAX_REPEAT):
                (i, j) = av[2].getwidth()
                lo = lo + long(i) * av[0]
                hi = hi + long(j) * av[1]
            elif op in (ANY, RANGE, IN, LITERAL, NOT_LITERAL, CATEGORY):
                lo = lo + 1
                hi = hi + 1
            elif op == SUCCESS:
                break
            
        
        self.width = (int(min(lo, sys.maxint)), int(min(hi, sys.maxint)))
        return self.width



class Tokenizer:
    
    def __init__(self, string):
        self.string = string
        self.index = 0
        self._Tokenizer__next()

    
    def _Tokenizer__next(self):
        if self.index >= len(self.string):
            self.next = None
            return None
        
        char = self.string[self.index]
        if char[0] == '\\':
            
            try:
                c = self.string[self.index + 1]
            except IndexError:
                raise error, 'bogus escape (end of line)'

            char = char + c
        
        self.index = self.index + len(char)
        self.next = char

    
    def match(self, char, skip = 1):
        if char == self.next:
            if skip:
                self._Tokenizer__next()
            
            return 1
        
        return 0

    
    def get(self):
        this = self.next
        self._Tokenizer__next()
        return this

    
    def tell(self):
        return (self.index, self.next)

    
    def seek(self, index):
        (self.index, self.next) = index



def isident(char):
    if 'a' <= char:
        pass
    char <= 'z'
    if not 1:
        if 'A' <= char:
            pass
        char <= 'Z'
        if not 1:
            pass
    return char == '_'


def isdigit(char):
    if '0' <= char:
        pass
    char <= '9'
    return 1


def isname(name):
    if not isident(name[0]):
        return 0
    
    for char in name:
        if not isident(char) and not isdigit(char):
            return 0
        
    
    return 1


def _group(escape, groups):
    
    try:
        gid = atoi(escape[1:])
        if gid and gid < groups:
            return gid
    except ValueError:
        pass

    return None


def _class_escape(source, escape):
    code = ESCAPES.get(escape)
    if code:
        return code
    
    code = CATEGORIES.get(escape)
    if code:
        return code
    
    
    try:
        if escape[1:2] == 'x':
            while source.next in HEXDIGITS and len(escape) < 4:
                escape = escape + source.get()
            escape = escape[2:]
            if len(escape) != 2:
                raise error, 'bogus escape: %s' % repr('\\' + escape)
            
            return (LITERAL, atoi(escape, 16) & 255)
        elif str(escape[1:2]) in OCTDIGITS:
            while source.next in OCTDIGITS and len(escape) < 5:
                escape = escape + source.get()
            escape = escape[1:]
            return (LITERAL, atoi(escape, 8) & 255)
        
        if len(escape) == 2:
            return (LITERAL, ord(escape[1]))
    except ValueError:
        pass

    raise error, 'bogus escape: %s' % repr(escape)


def _escape(source, escape, state):
    code = CATEGORIES.get(escape)
    if code:
        return code
    
    code = ESCAPES.get(escape)
    if code:
        return code
    
    
    try:
        if escape[1:2] == 'x':
            while source.next in HEXDIGITS and len(escape) < 4:
                escape = escape + source.get()
            if len(escape) != 4:
                raise ValueError
            
            return (LITERAL, atoi(escape[2:], 16) & 255)
        elif escape[1:2] == '0':
            while source.next in OCTDIGITS and len(escape) < 4:
                escape = escape + source.get()
            return (LITERAL, atoi(escape[1:], 8) & 255)
        elif escape[1:2] in DIGITS:
            here = source.tell()
            if source.next in DIGITS:
                escape = escape + source.get()
                if escape[1] in OCTDIGITS and escape[2] in OCTDIGITS and source.next in OCTDIGITS:
                    escape = escape + source.get()
                    return (LITERAL, atoi(escape[1:], 8) & 255)
                
            
            group = _group(escape, state.groups)
            if group:
                if not state.checkgroup(group):
                    raise error, 'cannot refer to open group'
                
                return (GROUPREF, group)
            
            raise ValueError
        
        if len(escape) == 2:
            return (LITERAL, ord(escape[1]))
    except ValueError:
        pass

    raise error, 'bogus escape: %s' % repr(escape)


def _parse_sub(source, state, nested = 1):
    items = []
    while 1:
        items.append(_parse(source, state))
        if source.match('|'):
            continue
        
        if not nested:
            break
        
        if not (source.next) or source.match(')', 0):
            break
        else:
            raise error, 'pattern not properly closed'
    if len(items) == 1:
        return items[0]
    
    subpattern = SubPattern(state)
    while 1:
        prefix = None
        for item in items:
            if not item:
                break
            
            if prefix is None:
                prefix = item[0]
            elif item[0] != prefix:
                break
            
        else:
            for item in items:
                del item[0]
            
        break
    for item in items:
        if len(item) != 1 or item[0][0] != LITERAL:
            break
        
    else:
        set = []
        for item in items:
            set.append(item[0])
        
        return subpattern
    subpattern.append((BRANCH, (None, items)))
    return subpattern


def _parse(source, state):
    subpattern = SubPattern(state)
    while 1:
        if source.next in ('|', ')'):
            break
        
        this = source.get()
        if this is None:
            break
        
        if state.flags & SRE_FLAG_VERBOSE:
            if this in WHITESPACE:
                continue
            
            if this == '#':
                while 1:
                    this = source.get()
                    if this in (None, '\n'):
                        break
                    
                continue
            
        
        if this and this[0] not in SPECIAL_CHARS:
            subpattern.append((LITERAL, ord(this)))
        elif this == '[':
            set = []
            if source.match('^'):
                set.append((NEGATE, None))
            
            start = set[:]
            while 1:
                this = source.get()
                if this == ']' and set != start:
                    break
                elif this and this[0] == '\\':
                    code1 = _class_escape(source, this)
                elif this:
                    code1 = (LITERAL, ord(this))
                else:
                    raise error, 'unexpected end of regular expression'
                if source.match('-'):
                    this = source.get()
                    if this == ']':
                        if code1[0] is IN:
                            code1 = code1[1][0]
                        
                        set.append(code1)
                        set.append((LITERAL, ord('-')))
                        break
                    elif this[0] == '\\':
                        code2 = _class_escape(source, this)
                    else:
                        code2 = (LITERAL, ord(this))
                    if code1[0] != LITERAL or code2[0] != LITERAL:
                        raise error, 'bad character range'
                    
                    lo = code1[1]
                    hi = code2[1]
                    if hi < lo:
                        raise error, 'bad character range'
                    
                    set.append((RANGE, (lo, hi)))
                elif code1[0] is IN:
                    code1 = code1[1][0]
                
                set.append(code1)
            if len(set) == 1 and set[0][0] is LITERAL:
                subpattern.append(set[0])
            elif len(set) == 2 and set[0][0] is NEGATE and set[1][0] is LITERAL:
                subpattern.append((NOT_LITERAL, set[1][1]))
            else:
                subpattern.append((IN, set))
        elif this and this[0] in REPEAT_CHARS:
            if this == '?':
                (min, max) = (0, 1)
            elif this == '*':
                (min, max) = (0, MAXREPEAT)
            elif this == '+':
                (min, max) = (1, MAXREPEAT)
            elif this == '{':
                here = source.tell()
                (min, max) = (0, MAXREPEAT)
                lo = ''
                hi = ''
                while source.next in DIGITS:
                    lo = lo + source.get()
                if source.match(','):
                    while source.next in DIGITS:
                        hi = hi + source.get()
                else:
                    hi = lo
                if not source.match('}'):
                    subpattern.append((LITERAL, ord(this)))
                    source.seek(here)
                    continue
                
                if lo:
                    min = atoi(lo)
                
                if hi:
                    max = atoi(hi)
                
                if max < min:
                    raise error, 'bad repeat interval'
                
            else:
                raise error, 'not supported'
            if subpattern:
                item = subpattern[-1:]
            else:
                item = None
            if not item and len(item) == 1 and item[0][0] == AT:
                raise error, 'nothing to repeat'
            
            if item[0][0] in (MIN_REPEAT, MAX_REPEAT):
                raise error, 'multiple repeat'
            
            if source.match('?'):
                subpattern[-1] = (MIN_REPEAT, (min, max, item))
            else:
                subpattern[-1] = (MAX_REPEAT, (min, max, item))
        elif this == '.':
            subpattern.append((ANY, None))
        elif this == '(':
            group = 1
            name = None
            if source.match('?'):
                group = 0
                if source.match('P'):
                    if source.match('<'):
                        name = ''
                        while 1:
                            char = source.get()
                            if char is None:
                                raise error, 'unterminated name'
                            
                            if char == '>':
                                break
                            
                            name = name + char
                        group = 1
                        if not isname(name):
                            raise error, 'bad character in group name'
                        
                    elif source.match('='):
                        name = ''
                        while 1:
                            char = source.get()
                            if char is None:
                                raise error, 'unterminated name'
                            
                            if char == ')':
                                break
                            
                            name = name + char
                        if not isname(name):
                            raise error, 'bad character in group name'
                        
                        gid = state.groupdict.get(name)
                        if gid is None:
                            raise error, 'unknown group name'
                        
                        subpattern.append((GROUPREF, gid))
                        continue
                    else:
                        char = source.get()
                        if char is None:
                            raise error, 'unexpected end of pattern'
                        
                        raise error, 'unknown specifier: ?P%s' % char
                elif source.match(':'):
                    group = 2
                elif source.match('#'):
                    while 1:
                        if source.next is None or source.next == ')':
                            break
                        
                        source.get()
                    if not source.match(')'):
                        raise error, 'unbalanced parenthesis'
                    
                    continue
                elif source.next in ('=', '!', '<'):
                    char = source.get()
                    dir = 1
                    if char == '<':
                        if source.next not in ('=', '!'):
                            raise error, 'syntax error'
                        
                        dir = -1
                        char = source.get()
                    
                    p = _parse_sub(source, state)
                    if not source.match(')'):
                        raise error, 'unbalanced parenthesis'
                    
                    if char == '=':
                        subpattern.append((ASSERT, (dir, p)))
                    else:
                        subpattern.append((ASSERT_NOT, (dir, p)))
                    continue
                elif not FLAGS.has_key(source.next):
                    raise error, 'unexpected end of pattern'
                
                while FLAGS.has_key(source.next):
                    state.flags = state.flags | FLAGS[source.get()]
            
            if group:
                if group == 2:
                    group = None
                else:
                    group = state.opengroup(name)
                p = _parse_sub(source, state)
                if not source.match(')'):
                    raise error, 'unbalanced parenthesis'
                
                if group is not None:
                    state.closegroup(group)
                
                subpattern.append((SUBPATTERN, (group, p)))
            else:
                while 1:
                    char = source.get()
                    if char is None:
                        raise error, 'unexpected end of pattern'
                    
                    if char == ')':
                        break
                    
                    raise error, 'unknown extension'
        elif this == '^':
            subpattern.append((AT, AT_BEGINNING))
        elif this == '$':
            subpattern.append((AT, AT_END))
        elif this and this[0] == '\\':
            code = _escape(source, this, state)
            subpattern.append(code)
        else:
            raise error, 'parser error'
    return subpattern


def parse(str, flags = 0, pattern = None):
    source = Tokenizer(str)
    if pattern is None:
        pattern = Pattern()
    
    pattern.flags = flags
    pattern.str = str
    p = _parse_sub(source, pattern, 0)
    tail = source.get()
    if tail == ')':
        raise error, 'unbalanced parenthesis'
    elif tail:
        raise error, 'bogus characters at end of regular expression'
    
    if flags & SRE_FLAG_DEBUG:
        p.dump()
    
    if not (flags & SRE_FLAG_VERBOSE) and p.pattern.flags & SRE_FLAG_VERBOSE:
        return parse(str, p.pattern.flags)
    
    return p


def parse_template(source, pattern):
    s = Tokenizer(source)
    p = []
    a = p.append
    
    def literal(literal, p = p):
        if p and p[-1][0] is LITERAL:
            p[-1] = (LITERAL, p[-1][1] + literal)
        else:
            p.append((LITERAL, literal))

    sep = source[:0]
    if type(sep) is type(''):
        makechar = chr
    else:
        makechar = unichr
    while 1:
        this = s.get()
        if this is None:
            break
        
        if this and this[0] == '\\':
            if this == '\\g':
                name = ''
                if s.match('<'):
                    while 1:
                        char = s.get()
                        if char is None:
                            raise error, 'unterminated group name'
                        
                        if char == '>':
                            break
                        
                        name = name + char
                
                if not name:
                    raise error, 'bad group name'
                
                
                try:
                    index = atoi(name)
                except ValueError:
                    if not isname(name):
                        raise error, 'bad character in group name'
                    
                    
                    try:
                        index = pattern.groupindex[name]
                    except KeyError:
                        raise IndexError, 'unknown group name'


                a((MARK, index))
            elif len(this) > 1 and this[1] in DIGITS:
                code = None
                while 1:
                    group = _group(this, pattern.groups + 1)
                    if group:
                        if s.next not in DIGITS or not _group(this + s.next, pattern.groups + 1):
                            code = (MARK, group)
                            break
                        
                    elif s.next in OCTDIGITS:
                        this = this + s.get()
                    else:
                        break
                if not code:
                    this = this[1:]
                    code = (LITERAL, makechar(atoi(this[-6:], 8) & 255))
                
                if code[0] is LITERAL:
                    literal(code[1])
                else:
                    a(code)
            else:
                
                try:
                    this = makechar(ESCAPES[this][1])
                except KeyError:
                    pass

                literal(this)
        else:
            literal(this)
    i = 0
    groups = []
    literals = []
    for (c, s) in p:
        if c is MARK:
            groups.append((i, s))
            literals.append(None)
        else:
            literals.append(s)
        i = i + 1
    
    return (groups, literals)


def expand_template(template, match):
    g = match.group
    sep = match.string[:0]
    (groups, literals) = template
    literals = literals[:]
    
    try:
        for (index, group) in groups:
            literals[index] = g(group)
            s = g(group)
            if s is None:
                raise IndexError
            
    except IndexError:
        raise error, 'empty group'

    return string.join(literals, sep)

