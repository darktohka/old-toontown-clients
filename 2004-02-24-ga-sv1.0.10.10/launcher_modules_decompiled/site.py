# File: s (Python 2.2)

import sys
import os

def makepath(*paths):
    dir = os.path.abspath(os.path.join(*paths))
    return (dir, os.path.normcase(dir))

for m in sys.modules.values():
    if hasattr(m, '__file__') and m.__file__:
        m.__file__ = os.path.abspath(m.__file__)
    

del m
L = []
_dirs_in_sys_path = { }
for dir in sys.path:
    if sys.platform != 'mac':
        if dir and not os.path.isdir(dir):
            continue
        
    elif dir and not os.path.exists(dir):
        continue
    
    (dir, dircase) = makepath(dir)
    if not _dirs_in_sys_path.has_key(dircase):
        L.append(dir)
        _dirs_in_sys_path[dircase] = 1
    

sys.path[:] = L
del dir
del L
if os.name == 'posix' and sys.path and os.path.basename(sys.path[-1]) == 'Modules':
    from distutils.util import get_platform
    s = 'build/lib.%s-%.3s' % (get_platform(), sys.version)
    s = os.path.join(os.path.dirname(sys.path[-1]), s)
    sys.path.append(s)
    del get_platform
    del s


def _init_pathinfo():
    global _dirs_in_sys_path
    _dirs_in_sys_path = { }
    d = { }
    for dir in sys.path:
        if dir and not os.path.isdir(dir):
            continue
        
        (dir, dircase) = makepath(dir)
        d[dircase] = 1
    


def addsitedir(sitedir):
    global _dirs_in_sys_path
    if _dirs_in_sys_path is None:
        _init_pathinfo()
        reset = 1
    else:
        reset = 0
    (sitedir, sitedircase) = makepath(sitedir)
    if not _dirs_in_sys_path.has_key(sitedircase):
        sys.path.append(sitedir)
    
    
    try:
        names = os.listdir(sitedir)
    except os.error:
        return None

    names.sort()
    for name in names:
        if name[-4:] == os.extsep + 'pth':
            addpackage(sitedir, name)
        
    
    if reset:
        _dirs_in_sys_path = None
    


def addpackage(sitedir, name):
    global _dirs_in_sys_path
    if _dirs_in_sys_path is None:
        _init_pathinfo()
        reset = 1
    else:
        reset = 0
    fullname = os.path.join(sitedir, name)
    
    try:
        f = open(fullname)
    except IOError:
        return None

    while 1:
        dir = f.readline()
        if not dir:
            break
        
        if dir[0] == '#':
            continue
        
        if dir.startswith('import'):
            exec dir
            continue
        
        if dir[-1] == '\n':
            dir = dir[:-1]
        
        (dir, dircase) = makepath(sitedir, dir)
        if not _dirs_in_sys_path.has_key(dircase) and os.path.exists(dir):
            sys.path.append(dir)
            _dirs_in_sys_path[dircase] = 1
        
    if reset:
        _dirs_in_sys_path = None
    

prefixes = [
    sys.prefix]
if sys.exec_prefix != sys.prefix:
    prefixes.append(sys.exec_prefix)

for prefix in prefixes:
    if prefix:
        if os.sep == '/':
            sitedirs = [
                os.path.join(prefix, 'lib', 'python' + sys.version[:3], 'site-packages'),
                os.path.join(prefix, 'lib', 'site-python')]
        else:
            sitedirs = [
                prefix,
                os.path.join(prefix, 'lib', 'site-packages')]
        for sitedir in sitedirs:
            if os.path.isdir(sitedir):
                addsitedir(sitedir)
            
        
    

_dirs_in_sys_path = None
if os.sep == ':':
    exit = 'Use Cmd-Q to quit.'
elif os.sep == '\\':
    exit = 'Use Ctrl-Z plus Return to exit.'
else:
    exit = 'Use Ctrl-D (i.e. EOF) to exit.'
import __builtin__
__builtin__.quit = exit
__builtin__.exit = exit
del exit

class _Printer:
    MAXLINES = 23
    
    def __init__(self, name, data, files = (), dirs = ()):
        self._Printer__name = name
        self._Printer__data = data
        self._Printer__files = files
        self._Printer__dirs = dirs
        self._Printer__lines = None

    
    def _Printer__setup(self):
        if self._Printer__lines:
            return None
        
        data = None
        for dir in self._Printer__dirs:
            for file in self._Printer__files:
                file = os.path.join(dir, file)
                
                try:
                    fp = open(file)
                    data = fp.read()
                    fp.close()
                except IOError:
                    pass

            
            if data:
                break
            
        
        if not data:
            data = self._Printer__data
        
        self._Printer__lines = data.split('\n')
        self._Printer__linecnt = len(self._Printer__lines)

    
    def __repr__(self):
        self._Printer__setup()
        if len(self._Printer__lines) <= self.MAXLINES:
            return '\n'.join(self._Printer__lines)
        else:
            return 'Type %s() to see the full %s text' % (self._Printer__name,) * 2

    
    def __call__(self):
        self._Printer__setup()
        prompt = 'Hit Return for more, or q (and Return) to quit: '
        lineno = 0
        while 1:
            
            try:
                for i in range(lineno, lineno + self.MAXLINES):
                    print self._Printer__lines[i]
            except IndexError:
                break

            lineno += self.MAXLINES
            key = None
            while key is None:
                key = raw_input(prompt)
                if key not in ('', 'q'):
                    key = None
                
            if key == 'q':
                break
            


__builtin__.copyright = _Printer('copyright', sys.copyright)
if sys.platform[:4] == 'java':
    __builtin__.credits = _Printer('credits', 'Jython is maintained by the Jython developers (www.jython.org).')
else:
    __builtin__.credits = _Printer('credits', 'Thanks to CWI, CNRI, BeOpen.com, Digital Creations and a cast of thousands\nfor supporting Python development.  See www.python.org for more information.')
here = os.path.dirname(os.__file__)
__builtin__.license = _Printer('license', 'See http://www.python.org/%.3s/license.html' % sys.version, [
    'LICENSE.txt',
    'LICENSE'], [
    os.path.join(here, os.pardir),
    here,
    os.curdir])

class _Helper:
    
    def __repr__(self):
        return 'Type help() for interactive help, or help(object) for help about object.'

    
    def __call__(self, *args, **kwds):
        import pydoc
        return pydoc.help(*args, **args)


__builtin__.help = _Helper()
encoding = 'ascii'
if encoding != 'ascii':
    sys.setdefaultencoding(encoding)


try:
    import sitecustomize
except ImportError:
    pass

if hasattr(sys, 'setdefaultencoding'):
    del sys.setdefaultencoding


def _test():
    print 'sys.path = ['
    for dir in sys.path:
        print '    %s,' % `dir`
    
    print ']'

if __name__ == '__main__':
    _test()

