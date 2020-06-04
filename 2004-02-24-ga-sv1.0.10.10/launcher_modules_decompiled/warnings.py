# File: w (Python 2.2)

import sys
import re
import types
__all__ = [
    'warn',
    'showwarning',
    'formatwarning',
    'filterwarnings',
    'resetwarnings']
defaultaction = 'default'
filters = []
onceregistry = { }

def warn(message, category = None, stacklevel = 1):
    if category is None:
        category = UserWarning
    
    
    try:
        caller = sys._getframe(stacklevel)
    except ValueError:
        globals = sys.__dict__
        lineno = 1

    globals = caller.f_globals
    lineno = caller.f_lineno
    if globals.has_key('__name__'):
        module = globals['__name__']
    else:
        module = '<string>'
    filename = globals.get('__file__')
    if filename:
        fnl = filename.lower()
        if fnl.endswith('.pyc') or fnl.endswith('.pyo'):
            filename = filename[:-1]
        
    elif module == '__main__':
        filename = sys.argv[0]
    
    if not filename:
        filename = module
    
    registry = globals.setdefault('__warningregistry__', { })
    warn_explicit(message, category, filename, lineno, module, registry)


def warn_explicit(message, category, filename, lineno, module = None, registry = None):
    if module is None:
        module = filename
        if module[-3:].lower() == '.py':
            module = module[:-3]
        
    
    if registry is None:
        registry = { }
    
    key = (message, category, lineno)
    if registry.get(key):
        return None
    
    for item in filters:
        (action, msg, cat, mod, ln) = item
        if msg.match(message) and issubclass(category, cat) and mod.match(module) and ln == 0 or lineno == ln:
            break
        
    else:
        action = defaultaction
    if action == 'ignore':
        registry[key] = 1
        return None
    
    if action == 'error':
        raise category(message)
    
    if action == 'once':
        registry[key] = 1
        oncekey = (message, category)
        if onceregistry.get(oncekey):
            return None
        
        onceregistry[oncekey] = 1
    elif action == 'always':
        pass
    elif action == 'module':
        registry[key] = 1
        altkey = (message, category, 0)
        if registry.get(altkey):
            return None
        
        registry[altkey] = 1
    elif action == 'default':
        registry[key] = 1
    else:
        raise RuntimeError('Unrecognized action (%s) in warnings.filters:\n %s' % (`action`, str(item)))
    showwarning(message, category, filename, lineno)


def showwarning(message, category, filename, lineno, file = None):
    if file is None:
        file = sys.stderr
    
    
    try:
        file.write(formatwarning(message, category, filename, lineno))
    except IOError:
        pass



def formatwarning(message, category, filename, lineno):
    import linecache
    s = '%s:%s: %s: %s\n' % (filename, lineno, category.__name__, message)
    line = linecache.getline(filename, lineno).strip()
    if line:
        s = s + '  ' + line + '\n'
    
    return s


def filterwarnings(action, message = '', category = Warning, module = '', lineno = 0, append = 0):
    item = (action, re.compile(message, re.I), category, re.compile(module), lineno)
    if append:
        filters.append(item)
    else:
        filters.insert(0, item)


def resetwarnings():
    filters[:] = []


class _OptionError(Exception):
    pass


def _processoptions(args):
    for arg in args:
        
        try:
            _setoption(arg)
        except _OptionError:
            msg = None
            print >>sys.stderr, 'Invalid -W option ignored:', msg

    


def _setoption(arg):
    parts = arg.split(':')
    if len(parts) > 5:
        raise _OptionError('too many fields (max 5): %s' % `arg`)
    
    while len(parts) < 5:
        parts.append('')
    continue
    (action, message, category, module, lineno) = [ s.strip() for s in parts ]
    action = _getaction(action)
    message = re.escape(message)
    category = _getcategory(category)
    module = re.escape(module)
    if module:
        module = module + '$'
    
    if lineno:
        
        try:
            lineno = int(lineno)
            if lineno < 0:
                raise ValueError
        except (ValueError, OverflowError):
            []
            raise _OptionError('invalid lineno %s' % `lineno`)
        except:
            []

    else:
        lineno = 0
    filterwarnings(action, message, category, module, lineno)


def _getaction(action):
    if not action:
        return 'default'
    
    if action == 'all':
        return 'always'
    
    for a in [
        'default',
        'always',
        'ignore',
        'module',
        'once',
        'error']:
        if a.startswith(action):
            return a
        
    
    raise _OptionError('invalid action: %s' % `action`)


def _getcategory(category):
    if not category:
        return Warning
    
    if re.match('^[a-zA-Z0-9_]+$', category):
        
        try:
            cat = eval(category)
        except NameError:
            raise _OptionError('unknown warning category: %s' % `category`)

    else:
        i = category.rfind('.')
        module = category[:i]
        klass = category[i + 1:]
        
        try:
            m = __import__(module, None, None, [
                klass])
        except ImportError:
            raise _OptionError('invalid module name: %s' % `module`)

        
        try:
            cat = getattr(m, klass)
        except AttributeError:
            raise _OptionError('unknown warning category: %s' % `category`)

    if not isinstance(cat, types.ClassType) or not issubclass(cat, Warning):
        raise _OptionError('invalid warning category: %s' % `category`)
    
    return cat


def _test():
    import getopt
    testoptions = []
    
    try:
        (opts, args) = getopt.getopt(sys.argv[1:], 'W:')
    except getopt.error:
        msg = None
        print >>sys.stderr, msg
        return None

    for (o, a) in opts:
        testoptions.append(a)
    
    
    try:
        _processoptions(testoptions)
    except _OptionError:
        msg = None
        print >>sys.stderr, msg
        return None

    for item in filters:
        print item
    
    hello = 'hello world'
    warn(hello)
    warn(hello)
    warn(hello)
    warn(hello)
    warn(hello, UserWarning)
    warn(hello, DeprecationWarning)
    for i in range(3):
        warn(hello)
    
    filterwarnings('error', '', Warning, '', 0)
    
    try:
        warn(hello)
    except Exception:
        msg = None
        print 'Caught', msg.__class__.__name__ + ':', msg

    print 'No exception'
    resetwarnings()
    
    try:
        filterwarnings('booh', '', Warning, '', 0)
    except Exception:
        msg = None
        print 'Caught', msg.__class__.__name__ + ':', msg

    print 'No exception'

if __name__ == '__main__':
    import __main__
    sys.modules['warnings'] = __main__
    _test()
else:
    _processoptions(sys.warnoptions)
    filterwarnings('ignore', category = OverflowWarning, append = 1)
