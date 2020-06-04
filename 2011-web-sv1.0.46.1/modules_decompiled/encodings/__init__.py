# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\cygwin\home\toonpub\player\wintools\sdk\python\Python-2.4.1\Lib\encodings\__init__.py
import codecs, exceptions, types, aliases
_cache = {}
_unknown = '--unknown--'
_import_tail = ['*']
_norm_encoding_map = '                                              . 0123456789       ABCDEFGHIJKLMNOPQRSTUVWXYZ      abcdefghijklmnopqrstuvwxyz                                                                                                                                     '
_aliases = aliases.aliases

class CodecRegistryError(exceptions.LookupError, exceptions.SystemError):
    __module__ = __name__


def normalize_encoding(encoding):
    if type(encoding) is types.UnicodeType:
        encoding = encoding.encode('latin-1')
    return ('_').join(encoding.translate(_norm_encoding_map).split())


def search_function(encoding):
    entry = _cache.get(encoding, _unknown)
    if entry is not _unknown:
        return entry
    norm_encoding = normalize_encoding(encoding)
    aliased_encoding = _aliases.get(norm_encoding) or _aliases.get(norm_encoding.replace('.', '_'))
    if aliased_encoding is not None:
        modnames = [
         aliased_encoding, norm_encoding]
    else:
        modnames = [
         norm_encoding]
    for modname in modnames:
        if not modname:
            continue
        try:
            mod = __import__(modname, globals(), locals(), _import_tail)
        except ImportError:
            pass
        else:
            break
    else:
        mod = None

    try:
        getregentry = mod.getregentry
    except AttributeError:
        mod = None

    if mod is None:
        _cache[encoding] = None
        return
    entry = tuple(getregentry())
    if len(entry) != 4:
        raise CodecRegistryError, 'module "%s" (%s) failed to register' % (mod.__name__, mod.__file__)
    for obj in entry:
        if not callable(obj):
            raise CodecRegistryError, 'incompatible codecs in module "%s" (%s)' % (mod.__name__, mod.__file__)

    _cache[encoding] = entry
    try:
        codecaliases = mod.getaliases()
    except AttributeError:
        pass
    else:
        for alias in codecaliases:
            if not _aliases.has_key(alias):
                _aliases[alias] = modname

    return entry


codecs.register(search_function)