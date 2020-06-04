# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\cygwin\home\toonpub\player\wintools\sdk\python\Python-2.4.1\Lib\urlparse.py
__all__ = [
 'urlparse', 'urlunparse', 'urljoin', 'urldefrag', 'urlsplit', 'urlunsplit']
uses_relative = [
 'ftp', 'http', 'gopher', 'nntp', 'imap', 'wais', 'file', 'https', 'shttp', 'mms', 'prospero', 'rtsp', 'rtspu', '']
uses_netloc = [
 'ftp', 'http', 'gopher', 'nntp', 'telnet', 'imap', 'wais', 'file', 'mms', 'https', 'shttp', 'snews', 'prospero', 'rtsp', 'rtspu', 'rsync', '']
non_hierarchical = [
 'gopher', 'hdl', 'mailto', 'news', 'telnet', 'wais', 'imap', 'snews', 'sip']
uses_params = [
 'ftp', 'hdl', 'prospero', 'http', 'imap', 'https', 'shttp', 'rtsp', 'rtspu', 'sip', 'mms', '']
uses_query = [
 'http', 'wais', 'imap', 'https', 'shttp', 'mms', 'gopher', 'rtsp', 'rtspu', 'sip', '']
uses_fragment = [
 'ftp', 'hdl', 'http', 'gopher', 'news', 'nntp', 'wais', 'https', 'shttp', 'snews', 'file', 'prospero', '']
scheme_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-.'
MAX_CACHE_SIZE = 20
_parse_cache = {}

def clear_cache():
    global _parse_cache
    _parse_cache = {}


def urlparse(url, scheme='', allow_fragments=1):
    tuple = urlsplit(url, scheme, allow_fragments)
    (scheme, netloc, url, query, fragment) = tuple
    if scheme in uses_params and ';' in url:
        (url, params) = _splitparams(url)
    else:
        params = ''
    return (
     scheme, netloc, url, params, query, fragment)


def _splitparams(url):
    if '/' in url:
        i = url.find(';', url.rfind('/'))
        if i < 0:
            return (
             url, '')
    else:
        i = url.find(';')
    return (
     url[:i], url[i + 1:])


def _splitnetloc(url, start=0):
    for c in '/?#':
        delim = url.find(c, start)
        if delim >= 0:
            break
    else:
        delim = len(url)

    return (
     url[start:delim], url[delim:])


def urlsplit(url, scheme='', allow_fragments=1):
    key = (
     url, scheme, allow_fragments)
    cached = _parse_cache.get(key, None)
    if cached:
        return cached
    if len(_parse_cache) >= MAX_CACHE_SIZE:
        clear_cache()
    netloc = query = fragment = ''
    i = url.find(':')
    if i > 0:
        if url[:i] == 'http':
            scheme = url[:i].lower()
            url = url[i + 1:]
            if url[:2] == '//':
                (netloc, url) = _splitnetloc(url, 2)
            if allow_fragments and '#' in url:
                (url, fragment) = url.split('#', 1)
            if '?' in url:
                (url, query) = url.split('?', 1)
            tuple = (
             scheme, netloc, url, query, fragment)
            _parse_cache[key] = tuple
            return tuple
        for c in url[:i]:
            if c not in scheme_chars:
                break
        else:
            scheme, url = url[:i].lower(), url[i + 1:]
    if scheme in uses_netloc and url[:2] == '//':
        (netloc, url) = _splitnetloc(url, 2)
    if allow_fragments and scheme in uses_fragment and '#' in url:
        (url, fragment) = url.split('#', 1)
    if scheme in uses_query and '?' in url:
        (url, query) = url.split('?', 1)
    tuple = (
     scheme, netloc, url, query, fragment)
    _parse_cache[key] = tuple
    return tuple


def urlunparse((scheme, netloc, url, params, query, fragment)):
    if params:
        url = '%s;%s' % (url, params)
    return urlunsplit((scheme, netloc, url, query, fragment))


def urlunsplit((scheme, netloc, url, query, fragment)):
    if netloc or scheme and scheme in uses_netloc and url[:2] != '//':
        if url and url[:1] != '/':
            url = '/' + url
        url = '//' + (netloc or '') + url
    if scheme:
        url = scheme + ':' + url
    if query:
        url = url + '?' + query
    if fragment:
        url = url + '#' + fragment
    return url


def urljoin(base, url, allow_fragments=1):
    if not base:
        return url
    if not url:
        return base
    (bscheme, bnetloc, bpath, bparams, bquery, bfragment) = urlparse(base, '', allow_fragments)
    (scheme, netloc, path, params, query, fragment) = urlparse(url, bscheme, allow_fragments)
    if scheme != bscheme or scheme not in uses_relative:
        return url
    if scheme in uses_netloc:
        if netloc:
            return urlunparse((scheme, netloc, path, params, query, fragment))
        netloc = bnetloc
    if path[:1] == '/':
        return urlunparse((scheme, netloc, path, params, query, fragment))
    if not (path or params or query):
        return urlunparse((scheme, netloc, bpath, bparams, bquery, fragment))
    segments = bpath.split('/')[:-1] + path.split('/')
    if segments[(-1)] == '.':
        segments[-1] = ''
    while '.' in segments:
        segments.remove('.')

    while 1:
        i = 1
        n = len(segments) - 1
        while i < n:
            if segments[i] == '..' and segments[(i - 1)] not in ('', '..'):
                del segments[i - 1:i + 1]
                break
            i = i + 1
        else:
            break

    if segments == ['', '..']:
        segments[-1] = ''
    elif len(segments) >= 2 and segments[(-1)] == '..':
        segments[(-2):] = [
         '']
    return urlunparse((scheme, netloc, ('/').join(segments), params, query, fragment))


def urldefrag(url):
    if '#' in url:
        (s, n, p, a, q, frag) = urlparse(url)
        defrag = urlunparse((s, n, p, a, q, ''))
        return (defrag, frag)
    else:
        return (
         url, '')


test_input = '\n      http://a/b/c/d\n\n      g:h        = <URL:g:h>\n      http:g     = <URL:http://a/b/c/g>\n      http:      = <URL:http://a/b/c/d>\n      g          = <URL:http://a/b/c/g>\n      ./g        = <URL:http://a/b/c/g>\n      g/         = <URL:http://a/b/c/g/>\n      /g         = <URL:http://a/g>\n      //g        = <URL:http://g>\n      ?y         = <URL:http://a/b/c/d?y>\n      g?y        = <URL:http://a/b/c/g?y>\n      g?y/./x    = <URL:http://a/b/c/g?y/./x>\n      .          = <URL:http://a/b/c/>\n      ./         = <URL:http://a/b/c/>\n      ..         = <URL:http://a/b/>\n      ../        = <URL:http://a/b/>\n      ../g       = <URL:http://a/b/g>\n      ../..      = <URL:http://a/>\n      ../../g    = <URL:http://a/g>\n      ../../../g = <URL:http://a/../g>\n      ./../g     = <URL:http://a/b/g>\n      ./g/.      = <URL:http://a/b/c/g/>\n      /./g       = <URL:http://a/./g>\n      g/./h      = <URL:http://a/b/c/g/h>\n      g/../h     = <URL:http://a/b/c/h>\n      http:g     = <URL:http://a/b/c/g>\n      http:      = <URL:http://a/b/c/d>\n      http:?y         = <URL:http://a/b/c/d?y>\n      http:g?y        = <URL:http://a/b/c/g?y>\n      http:g?y/./x    = <URL:http://a/b/c/g?y/./x>\n'

def test():
    import sys
    base = ''
    if sys.argv[1:]:
        fn = sys.argv[1]
        if fn == '-':
            fp = sys.stdin
        else:
            fp = open(fn)
    else:
        import StringIO
        fp = StringIO.StringIO(test_input)
    while 1:
        line = fp.readline()
        if not line:
            break
        words = line.split()
        if not words:
            continue
        url = words[0]
        parts = urlparse(url)
        print '%-10s : %s' % (url, parts)
        abs = urljoin(base, url)
        if not base:
            base = abs
        wrapped = '<URL:%s>' % abs
        print '%-10s = %s' % (url, wrapped)
        if len(words) == 3 and words[1] == '=':
            if wrapped != words[2]:
                print 'EXPECTED', words[2], '!!!!!!!!!!'


if __name__ == '__main__':
    test()