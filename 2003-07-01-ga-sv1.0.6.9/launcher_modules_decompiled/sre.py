# File: s (Python 2.2)

import sys
import sre_compile
import sre_parse
__all__ = [
    'match',
    'search',
    'sub',
    'subn',
    'split',
    'findall',
    'compile',
    'purge',
    'template',
    'escape',
    'I',
    'L',
    'M',
    'S',
    'X',
    'U',
    'IGNORECASE',
    'LOCALE',
    'MULTILINE',
    'DOTALL',
    'VERBOSE',
    'UNICODE',
    'error']
__version__ = '2.2.1'
import string
I = sre_compile.SRE_FLAG_IGNORECASE
IGNORECASE = sre_compile.SRE_FLAG_IGNORECASE
L = sre_compile.SRE_FLAG_LOCALE
LOCALE = sre_compile.SRE_FLAG_LOCALE
U = sre_compile.SRE_FLAG_UNICODE
UNICODE = sre_compile.SRE_FLAG_UNICODE
M = sre_compile.SRE_FLAG_MULTILINE
MULTILINE = sre_compile.SRE_FLAG_MULTILINE
S = sre_compile.SRE_FLAG_DOTALL
DOTALL = sre_compile.SRE_FLAG_DOTALL
X = sre_compile.SRE_FLAG_VERBOSE
VERBOSE = sre_compile.SRE_FLAG_VERBOSE
T = sre_compile.SRE_FLAG_TEMPLATE
TEMPLATE = sre_compile.SRE_FLAG_TEMPLATE
DEBUG = sre_compile.SRE_FLAG_DEBUG
error = sre_compile.error

def match(pattern, string, flags = 0):
    return _compile(pattern, flags).match(string)


def search(pattern, string, flags = 0):
    return _compile(pattern, flags).search(string)


def sub(pattern, repl, string, count = 0):
    return _compile(pattern, 0).sub(repl, string, count)


def subn(pattern, repl, string, count = 0):
    return _compile(pattern, 0).subn(repl, string, count)


def split(pattern, string, maxsplit = 0):
    return _compile(pattern, 0).split(string, maxsplit)


def findall(pattern, string):
    return _compile(pattern, 0).findall(string)

if sys.hexversion >= 33685504:
    __all__.append('finditer')
    
    def finditer(pattern, string):
        return _compile(pattern, 0).finditer(string)



def compile(pattern, flags = 0):
    return _compile(pattern, flags)


def purge():
    _cache.clear()
    _cache_repl.clear()


def template(pattern, flags = 0):
    return _compile(pattern, flags | T)


def escape(pattern):
    s = list(pattern)
    for i in range(len(pattern)):
        c = pattern[i]
        if 'a' <= c:
            pass
        c <= 'z'
        if not 1:
            if 'A' <= c:
                pass
            c <= 'Z'
            if not 1:
                if '0' <= c:
                    pass
                c <= '9'
        if not 1:
            if c == '\x0':
                s[i] = '\\000'
            else:
                s[i] = '\\' + c
        
    
    return _join(s, pattern)

_cache = { }
_cache_repl = { }
_pattern_type = type(sre_compile.compile('', 0))
_MAXCACHE = 100

def _join(seq, sep):
    return string.join(seq, sep[:0])


def _compile(*key):
    p = _cache.get(key)
    if p is not None:
        return p
    
    (pattern, flags) = key
    if type(pattern) is _pattern_type:
        return pattern
    
    if type(pattern) not in sre_compile.STRING_TYPES:
        raise TypeError, 'first argument must be string or compiled pattern'
    
    
    try:
        p = sre_compile.compile(pattern, flags)
    except error:
        v = None
        raise error, v

    if len(_cache) >= _MAXCACHE:
        _cache.clear()
    
    _cache[key] = p
    return p


def _compile_repl(*key):
    p = _cache_repl.get(key)
    if p is not None:
        return p
    
    (repl, pattern) = key
    
    try:
        p = sre_parse.parse_template(repl, pattern)
    except error:
        v = None
        raise error, v

    if len(_cache_repl) >= _MAXCACHE:
        _cache_repl.clear()
    
    _cache_repl[key] = p
    return p


def _expand(pattern, match, template):
    template = sre_parse.parse_template(template, pattern)
    return sre_parse.expand_template(template, match)


def _subx(pattern, template):
    template = _compile_repl(template, pattern)
    if not template[0] and len(template[1]) == 1:
        return template[1][0]
    
    
    def filter(match, template = template):
        return sre_parse.expand_template(template, match)

    return filter

import copy_reg

def _pickle(p):
    return (_compile, (p.pattern, p.flags))

copy_reg.pickle(_pattern_type, _pickle, _compile)

class Scanner:
    
    def __init__(self, lexicon, flags = 0):
        BRANCH = BRANCH
        SUBPATTERN = SUBPATTERN
        import sre_constants
        self.lexicon = lexicon
        p = []
        s = sre_parse.Pattern()
        s.flags = flags
        for (phrase, action) in lexicon:
            p.append(sre_parse.SubPattern(s, [
                (SUBPATTERN, (len(p) + 1, sre_parse.parse(phrase, flags)))]))
        
        p = sre_parse.SubPattern(s, [
            (BRANCH, (None, p))])
        s.groups = len(p)
        self.scanner = sre_compile.compile(p)

    
    def scan(self, string):
        result = []
        append = result.append
        match = self.scanner.scanner(string).match
        i = 0
        while 1:
            m = match()
            if not m:
                break
            
            j = m.end()
            if i == j:
                break
            
            action = self.lexicon[m.lastindex - 1][1]
            if callable(action):
                self.match = m
                action = action(self, m.group())
            
            if action is not None:
                append(action)
            
            i = j
        return (result, string[i:])


