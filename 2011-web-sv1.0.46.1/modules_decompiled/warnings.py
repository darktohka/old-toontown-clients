# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\cygwin\home\toonpub\player\wintools\sdk\python\Python-2.4.1\Lib\warnings.py
import sys, types, linecache
__all__ = [
 'warn', 'showwarning', 'formatwarning', 'filterwarnings', 'resetwarnings']
filters = []
defaultaction = 'default'
onceregistry = {}

def warn(message, category=None, stacklevel=1):
    if isinstance(message, Warning):
        category = message.__class__
    if category is None:
        category = UserWarning
    try:
        caller = sys._getframe(stacklevel)
    except ValueError:
        globals = sys.__dict__
        lineno = 1
    else:
        globals = caller.f_globals
        lineno = caller.f_lineno

    if '__name__' in globals:
        module = globals['__name__']
    else:
        module = '<string>'
    filename = globals.get('__file__')
    if filename:
        fnl = filename.lower()
        if fnl.endswith('.pyc') or fnl.endswith('.pyo'):
            filename = filename[:-1]
    else:
        if module == '__main__':
            filename = sys.argv[0]
        if not filename:
            filename = module
    registry = globals.setdefault('__warningregistry__', {})
    warn_explicit(message, category, filename, lineno, module, registry)
    return


def warn_explicit(message, category, filename, lineno, module=None, registry=None):
    if module is None:
        module = filename
        if module[-3:].lower() == '.py':
            module = module[:-3]
    if registry is None:
        registry = {}
    if isinstance(message, Warning):
        text = str(message)
        category = message.__class__
    else:
        text = message
        message = category(message)
    key = (
     text, category, lineno)
    if registry.get(key):
        return
    for item in filters:
        (action, msg, cat, mod, ln) = item
        if (msg is None or msg.match(text)) and issubclass(category, cat) and (mod is None or mod.match(module)) and (ln == 0 or lineno == ln):
            break
    else:
        action = defaultaction

    if action == 'ignore':
        registry[key] = 1
        return
    if action == 'error':
        raise message
    if action == 'once':
        registry[key] = 1
        oncekey = (text, category)
        if onceregistry.get(oncekey):
            return
        onceregistry[oncekey] = 1
    elif action == 'always':
        pass
    elif action == 'module':
        registry[key] = 1
        altkey = (text, category, 0)
        if registry.get(altkey):
            return
        registry[altkey] = 1
    elif action == 'default':
        registry[key] = 1
    else:
        raise RuntimeError('Unrecognized action (%r) in warnings.filters:\n %s' % (action, item))
    showwarning(message, category, filename, lineno)
    return


def showwarning(message, category, filename, lineno, file=None):
    if file is None:
        file = sys.stderr
    try:
        file.write(formatwarning(message, category, filename, lineno))
    except IOError:
        pass

    return


def formatwarning(message, category, filename, lineno):
    s = '%s:%s: %s: %s\n' % (filename, lineno, category.__name__, message)
    line = linecache.getline(filename, lineno).strip()
    if line:
        s = s + '  ' + line + '\n'
    return s


def filterwarnings(action, message='', category=Warning, module='', lineno=0, append=0):
    import re
    item = (
     action, re.compile(message, re.I), category, re.compile(module), lineno)
    if append:
        filters.append(item)
    else:
        filters.insert(0, item)


def simplefilter(action, category=Warning, lineno=0, append=0):
    item = (
     action, None, category, None, lineno)
    if append:
        filters.append(item)
    else:
        filters.insert(0, item)
    return


def resetwarnings():
    filters[:] = []


class _OptionError(Exception):
    __module__ = __name__


def _processoptions(args):
    for arg in args:
        try:
            _setoption(arg)
        except _OptionError, msg:
            print >> sys.stderr, 'Invalid -W option ignored:', msg


def _setoption(arg):
    import re
    parts = arg.split(':')
    if len(parts) > 5:
        raise _OptionError('too many fields (max 5): %r' % (arg,))
    while len(parts) < 5:
        parts.append('')

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
            raise _OptionError('invalid lineno %r' % (lineno,))

    else:
        lineno = 0
    filterwarnings(action, message, category, module, lineno)


def _getaction(action):
    if not action:
        return 'default'
    if action == 'all':
        return 'always'
    for a in ['default', 'always', 'ignore', 'module', 'once', 'error']:
        if a.startswith(action):
            return a

    raise _OptionError('invalid action: %r' % (action,))


def _getcategory(category):
    import re
    if not category:
        return Warning
    if re.match('^[a-zA-Z0-9_]+$', category):
        try:
            cat = eval(category)
        except NameError:
            raise _OptionError('unknown warning category: %r' % (category,))

    else:
        i = category.rfind('.')
        module = category[:i]
        klass = category[i + 1:]
        try:
            m = __import__(module, None, None, [klass])
        except ImportError:
            raise _OptionError('invalid module name: %r' % (module,))

        try:
            cat = getattr(m, klass)
        except AttributeError:
            raise _OptionError('unknown warning category: %r' % (category,))

    if not isinstance(cat, types.ClassType) or not issubclass(cat, Warning):
        raise _OptionError('invalid warning category: %r' % (category,))
    return cat


_processoptions(sys.warnoptions)
simplefilter('ignore', category=OverflowWarning, append=1)
simplefilter('ignore', category=PendingDeprecationWarning, append=1)