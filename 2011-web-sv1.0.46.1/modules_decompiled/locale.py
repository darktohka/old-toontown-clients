# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\cygwin\home\toonpub\player\wintools\sdk\python\Python-2.4.1\Lib\locale.py
import sys
__all__ = [
 'setlocale', 'Error', 'localeconv', 'strcoll', 'strxfrm', 'format', 'str', 'atof', 'atoi', 'LC_CTYPE', 'LC_COLLATE', 'LC_TIME', 'LC_MONETARY', 'LC_NUMERIC', 'LC_ALL', 'CHAR_MAX']
try:
    from _locale import *
except ImportError:
    CHAR_MAX = 127
    LC_ALL = 6
    LC_COLLATE = 3
    LC_CTYPE = 0
    LC_MESSAGES = 5
    LC_MONETARY = 4
    LC_NUMERIC = 1
    LC_TIME = 2
    Error = ValueError

    def localeconv():
        return {'grouping': [127], 'currency_symbol': '', 'n_sign_posn': 127, 'p_cs_precedes': 127, 'n_cs_precedes': 127, 'mon_grouping': [], 'n_sep_by_space': 127, 'decimal_point': '.', 'negative_sign': '', 'positive_sign': '', 'p_sep_by_space': 127, 'int_curr_symbol': '', 'p_sign_posn': 127, 'thousands_sep': '', 'mon_thousands_sep': '', 'frac_digits': 127, 'mon_decimal_point': '', 'int_frac_digits': 127}


    def setlocale(category, value=None):
        if value not in (None, '', 'C'):
            raise Error, '_locale emulation only supports "C" locale'
        return 'C'


    def strcoll(a, b):
        return cmp(a, b)


    def strxfrm(s):
        return s


def _group(s):
    conv = localeconv()
    grouping = conv['grouping']
    if not grouping:
        return (s, 0)
    result = ''
    seps = 0
    spaces = ''
    if s[(-1)] == ' ':
        sp = s.find(' ')
        spaces = s[sp:]
        s = s[:sp]
    while s and grouping:
        if grouping[0] == CHAR_MAX:
            break
        elif grouping[0] != 0:
            group = grouping[0]
            grouping = grouping[1:]
        if result:
            result = s[-group:] + conv['thousands_sep'] + result
            seps += 1
        else:
            result = s[-group:]
        s = s[:-group]
        if s and s[(-1)] not in '0123456789':
            return (s + result + spaces, seps)

    if not result:
        return (
         s + spaces, seps)
    if s:
        result = s + conv['thousands_sep'] + result
        seps += 1
    return (
     result + spaces, seps)


def format(f, val, grouping=0):
    result = f % val
    fields = result.split('.')
    seps = 0
    if grouping:
        (fields[0], seps) = _group(fields[0])
    if len(fields) == 2:
        result = fields[0] + localeconv()['decimal_point'] + fields[1]
    elif len(fields) == 1:
        result = fields[0]
    else:
        raise Error, 'Too many decimal points in result string'
    while seps:
        sp = result.find(' ')
        if sp == -1:
            break
        result = result[:sp] + result[sp + 1:]
        seps -= 1

    return result


def str(val):
    return format('%.12g', val)


def atof(string, func=float):
    ts = localeconv()['thousands_sep']
    if ts:
        string = string.replace(ts, '')
    dd = localeconv()['decimal_point']
    if dd:
        string = string.replace(dd, '.')
    return func(string)


def atoi(str):
    return atof(str, int)


def _test():
    setlocale(LC_ALL, '')
    s1 = format('%d', 123456789, 1)
    print s1, 'is', atoi(s1)
    s1 = str(3.14)
    print s1, 'is', atof(s1)


_setlocale = setlocale

def normalize(localename):
    fullname = localename.lower()
    if ':' in fullname:
        fullname = fullname.replace(':', '.')
    if '.' in fullname:
        (langname, encoding) = fullname.split('.')[:2]
        fullname = langname + '.' + encoding
    else:
        langname = fullname
        encoding = ''
    code = locale_alias.get(fullname, None)
    if code is not None:
        return code
    code = locale_alias.get(langname, None)
    if code is not None:
        if '.' in code:
            (langname, defenc) = code.split('.')
        else:
            langname = code
            defenc = ''
        if encoding:
            encoding = encoding_alias.get(encoding, encoding)
        else:
            encoding = defenc
        if encoding:
            return langname + '.' + encoding
        else:
            return langname
    else:
        return localename
    return


def _parse_localename(localename):
    code = normalize(localename)
    if '@' in localename:
        (code, modifier) = code.split('@')
        if modifier == 'euro' and '.' not in code:
            return (
             code, 'iso-8859-15')
    if '.' in code:
        return tuple(code.split('.')[:2])
    elif code == 'C':
        return (None, None)
    raise ValueError, 'unknown locale: %s' % localename
    return


def _build_localename(localetuple):
    (language, encoding) = localetuple
    if language is None:
        language = 'C'
    if encoding is None:
        return language
    else:
        return language + '.' + encoding
    return


def getdefaultlocale(envvars=(
 'LANGUAGE', 'LC_ALL', 'LC_CTYPE', 'LANG')):
    try:
        import _locale
        (code, encoding) = _locale._getdefaultlocale()
    except (ImportError, AttributeError):
        pass
    else:
        if sys.platform == 'win32' and code and code[:2] == '0x':
            code = windows_locale.get(int(code, 0))
        return (
         code, encoding)

    import os
    lookup = os.environ.get
    for variable in envvars:
        localename = lookup(variable, None)
        if localename:
            break
    else:
        localename = 'C'

    return _parse_localename(localename)


def getlocale(category=LC_CTYPE):
    localename = _setlocale(category)
    if category == LC_ALL and ';' in localename:
        raise TypeError, 'category LC_ALL is not supported'
    return _parse_localename(localename)


def setlocale(category, locale=None):
    if locale and type(locale) is not type(''):
        locale = normalize(_build_localename(locale))
    return _setlocale(category, locale)


def resetlocale(category=LC_ALL):
    _setlocale(category, _build_localename(getdefaultlocale()))


if sys.platform in ('win32', 'darwin', 'mac'):

    def getpreferredencoding(do_setlocale=True):
        import _locale
        return _locale._getdefaultlocale()[1]


try:
    CODESET
except NameError:

    def getpreferredencoding(do_setlocale=True):
        return getdefaultlocale()[1]


else:

    def getpreferredencoding(do_setlocale=True):
        if do_setlocale:
            oldloc = setlocale(LC_CTYPE)
            setlocale(LC_CTYPE, '')
            result = nl_langinfo(CODESET)
            setlocale(LC_CTYPE, oldloc)
            return result
        else:
            return nl_langinfo(CODESET)


encoding_alias = {'437': 'C', 'c': 'C', 'iso8859': 'ISO8859-1', '8859': 'ISO8859-1', '88591': 'ISO8859-1', 'ascii': 'ISO8859-1', 'en': 'ISO8859-1', 'iso88591': 'ISO8859-1', 'iso_8859-1': 'ISO8859-1', '885915': 'ISO8859-15', 'iso885915': 'ISO8859-15', 'iso_8859-15': 'ISO8859-15', 'iso8859-2': 'ISO8859-2', 'iso88592': 'ISO8859-2', 'iso_8859-2': 'ISO8859-2', 'iso88595': 'ISO8859-5', 'iso88596': 'ISO8859-6', 'iso88597': 'ISO8859-7', 'iso88598': 'ISO8859-8', 'iso88599': 'ISO8859-9', 'iso-2022-jp': 'JIS7', 'jis': 'JIS7', 'jis7': 'JIS7', 'sjis': 'SJIS', 'tis620': 'TACTIS', 'ajec': 'eucJP', 'eucjp': 'eucJP', 'ujis': 'eucJP', 'utf-8': 'utf', 'utf8': 'utf', 'utf8@ucs4': 'utf'}
locale_alias = {'american': 'en_US.ISO8859-1', 'ar': 'ar_AA.ISO8859-6', 'ar_aa': 'ar_AA.ISO8859-6', 'ar_sa': 'ar_SA.ISO8859-6', 'arabic': 'ar_AA.ISO8859-6', 'bg': 'bg_BG.ISO8859-5', 'bg_bg': 'bg_BG.ISO8859-5', 'bulgarian': 'bg_BG.ISO8859-5', 'c-french': 'fr_CA.ISO8859-1', 'c': 'C', 'c_c': 'C', 'cextend': 'en_US.ISO8859-1', 'chinese-s': 'zh_CN.eucCN', 'chinese-t': 'zh_TW.eucTW', 'croatian': 'hr_HR.ISO8859-2', 'cs': 'cs_CZ.ISO8859-2', 'cs_cs': 'cs_CZ.ISO8859-2', 'cs_cz': 'cs_CZ.ISO8859-2', 'cz': 'cz_CZ.ISO8859-2', 'cz_cz': 'cz_CZ.ISO8859-2', 'czech': 'cs_CS.ISO8859-2', 'da': 'da_DK.ISO8859-1', 'da_dk': 'da_DK.ISO8859-1', 'danish': 'da_DK.ISO8859-1', 'de': 'de_DE.ISO8859-1', 'de_at': 'de_AT.ISO8859-1', 'de_ch': 'de_CH.ISO8859-1', 'de_de': 'de_DE.ISO8859-1', 'dutch': 'nl_BE.ISO8859-1', 'ee': 'ee_EE.ISO8859-4', 'el': 'el_GR.ISO8859-7', 'el_gr': 'el_GR.ISO8859-7', 'en': 'en_US.ISO8859-1', 'en_au': 'en_AU.ISO8859-1', 'en_ca': 'en_CA.ISO8859-1', 'en_gb': 'en_GB.ISO8859-1', 'en_ie': 'en_IE.ISO8859-1', 'en_nz': 'en_NZ.ISO8859-1', 'en_uk': 'en_GB.ISO8859-1', 'en_us': 'en_US.ISO8859-1', 'eng_gb': 'en_GB.ISO8859-1', 'english': 'en_EN.ISO8859-1', 'english_uk': 'en_GB.ISO8859-1', 'english_united-states': 'en_US.ISO8859-1', 'english_us': 'en_US.ISO8859-1', 'es': 'es_ES.ISO8859-1', 'es_ar': 'es_AR.ISO8859-1', 'es_bo': 'es_BO.ISO8859-1', 'es_cl': 'es_CL.ISO8859-1', 'es_co': 'es_CO.ISO8859-1', 'es_cr': 'es_CR.ISO8859-1', 'es_ec': 'es_EC.ISO8859-1', 'es_es': 'es_ES.ISO8859-1', 'es_gt': 'es_GT.ISO8859-1', 'es_mx': 'es_MX.ISO8859-1', 'es_ni': 'es_NI.ISO8859-1', 'es_pa': 'es_PA.ISO8859-1', 'es_pe': 'es_PE.ISO8859-1', 'es_py': 'es_PY.ISO8859-1', 'es_sv': 'es_SV.ISO8859-1', 'es_uy': 'es_UY.ISO8859-1', 'es_ve': 'es_VE.ISO8859-1', 'et': 'et_EE.ISO8859-4', 'et_ee': 'et_EE.ISO8859-4', 'fi': 'fi_FI.ISO8859-1', 'fi_fi': 'fi_FI.ISO8859-1', 'finnish': 'fi_FI.ISO8859-1', 'fr': 'fr_FR.ISO8859-1', 'fr_be': 'fr_BE.ISO8859-1', 'fr_ca': 'fr_CA.ISO8859-1', 'fr_ch': 'fr_CH.ISO8859-1', 'fr_fr': 'fr_FR.ISO8859-1', 'fre_fr': 'fr_FR.ISO8859-1', 'french': 'fr_FR.ISO8859-1', 'french_france': 'fr_FR.ISO8859-1', 'ger_de': 'de_DE.ISO8859-1', 'german': 'de_DE.ISO8859-1', 'german_germany': 'de_DE.ISO8859-1', 'greek': 'el_GR.ISO8859-7', 'hebrew': 'iw_IL.ISO8859-8', 'hr': 'hr_HR.ISO8859-2', 'hr_hr': 'hr_HR.ISO8859-2', 'hu': 'hu_HU.ISO8859-2', 'hu_hu': 'hu_HU.ISO8859-2', 'hungarian': 'hu_HU.ISO8859-2', 'icelandic': 'is_IS.ISO8859-1', 'id': 'id_ID.ISO8859-1', 'id_id': 'id_ID.ISO8859-1', 'is': 'is_IS.ISO8859-1', 'is_is': 'is_IS.ISO8859-1', 'iso-8859-1': 'en_US.ISO8859-1', 'iso-8859-15': 'en_US.ISO8859-15', 'iso8859-1': 'en_US.ISO8859-1', 'iso8859-15': 'en_US.ISO8859-15', 'iso_8859_1': 'en_US.ISO8859-1', 'iso_8859_15': 'en_US.ISO8859-15', 'it': 'it_IT.ISO8859-1', 'it_ch': 'it_CH.ISO8859-1', 'it_it': 'it_IT.ISO8859-1', 'italian': 'it_IT.ISO8859-1', 'iw': 'iw_IL.ISO8859-8', 'iw_il': 'iw_IL.ISO8859-8', 'ja': 'ja_JP.eucJP', 'ja.jis': 'ja_JP.JIS7', 'ja.sjis': 'ja_JP.SJIS', 'ja_jp': 'ja_JP.eucJP', 'ja_jp.ajec': 'ja_JP.eucJP', 'ja_jp.euc': 'ja_JP.eucJP', 'ja_jp.eucjp': 'ja_JP.eucJP', 'ja_jp.iso-2022-jp': 'ja_JP.JIS7', 'ja_jp.jis': 'ja_JP.JIS7', 'ja_jp.jis7': 'ja_JP.JIS7', 'ja_jp.mscode': 'ja_JP.SJIS', 'ja_jp.sjis': 'ja_JP.SJIS', 'ja_jp.ujis': 'ja_JP.eucJP', 'japan': 'ja_JP.eucJP', 'japanese': 'ja_JP.SJIS', 'japanese-euc': 'ja_JP.eucJP', 'japanese.euc': 'ja_JP.eucJP', 'jp_jp': 'ja_JP.eucJP', 'ko': 'ko_KR.eucKR', 'ko_kr': 'ko_KR.eucKR', 'ko_kr.euc': 'ko_KR.eucKR', 'korean': 'ko_KR.eucKR', 'lt': 'lt_LT.ISO8859-4', 'lv': 'lv_LV.ISO8859-4', 'mk': 'mk_MK.ISO8859-5', 'mk_mk': 'mk_MK.ISO8859-5', 'nl': 'nl_NL.ISO8859-1', 'nl_be': 'nl_BE.ISO8859-1', 'nl_nl': 'nl_NL.ISO8859-1', 'no': 'no_NO.ISO8859-1', 'no_no': 'no_NO.ISO8859-1', 'norwegian': 'no_NO.ISO8859-1', 'pl': 'pl_PL.ISO8859-2', 'pl_pl': 'pl_PL.ISO8859-2', 'polish': 'pl_PL.ISO8859-2', 'portuguese': 'pt_PT.ISO8859-1', 'portuguese_brazil': 'pt_BR.ISO8859-1', 'posix': 'C', 'posix-utf2': 'C', 'pt': 'pt_PT.ISO8859-1', 'pt_br': 'pt_BR.ISO8859-1', 'pt_pt': 'pt_PT.ISO8859-1', 'ro': 'ro_RO.ISO8859-2', 'ro_ro': 'ro_RO.ISO8859-2', 'ru': 'ru_RU.ISO8859-5', 'ru_ru': 'ru_RU.ISO8859-5', 'rumanian': 'ro_RO.ISO8859-2', 'russian': 'ru_RU.ISO8859-5', 'serbocroatian': 'sh_YU.ISO8859-2', 'sh': 'sh_YU.ISO8859-2', 'sh_hr': 'sh_HR.ISO8859-2', 'sh_sp': 'sh_YU.ISO8859-2', 'sh_yu': 'sh_YU.ISO8859-2', 'sk': 'sk_SK.ISO8859-2', 'sk_sk': 'sk_SK.ISO8859-2', 'sl': 'sl_CS.ISO8859-2', 'sl_cs': 'sl_CS.ISO8859-2', 'sl_si': 'sl_SI.ISO8859-2', 'slovak': 'sk_SK.ISO8859-2', 'slovene': 'sl_CS.ISO8859-2', 'sp': 'sp_YU.ISO8859-5', 'sp_yu': 'sp_YU.ISO8859-5', 'spanish': 'es_ES.ISO8859-1', 'spanish_spain': 'es_ES.ISO8859-1', 'sr_sp': 'sr_SP.ISO8859-2', 'sv': 'sv_SE.ISO8859-1', 'sv_se': 'sv_SE.ISO8859-1', 'swedish': 'sv_SE.ISO8859-1', 'th_th': 'th_TH.TACTIS', 'tr': 'tr_TR.ISO8859-9', 'tr_tr': 'tr_TR.ISO8859-9', 'turkish': 'tr_TR.ISO8859-9', 'univ': 'en_US.utf', 'universal': 'en_US.utf', 'zh': 'zh_CN.eucCN', 'zh_cn': 'zh_CN.eucCN', 'zh_cn.big5': 'zh_TW.eucTW', 'zh_cn.euc': 'zh_CN.eucCN', 'zh_tw': 'zh_TW.eucTW', 'zh_tw.euc': 'zh_TW.eucTW'}
windows_locale = {1028: 'zh_TW', 2052: 'zh_CN', 1030: 'da_DK', 1043: 'nl_NL', 1033: 'en_US', 2057: 'en_UK', 3081: 'en_AU', 4105: 'en_CA', 5129: 'en_NZ', 6153: 'en_IE', 7177: 'en_ZA', 1035: 'fi_FI', 1036: 'fr_FR', 2060: 'fr_BE', 3084: 'fr_CA', 4108: 'fr_CH', 1031: 'de_DE', 1032: 'el_GR', 1037: 'iw_IL', 1039: 'is_IS', 1040: 'it_IT', 1041: 'ja_JA', 1044: 'no_NO', 2070: 'pt_PT', 3082: 'es_ES', 1089: 'sw_KE', 1053: 'sv_SE', 2077: 'sv_FI', 1055: 'tr_TR'}

def _print_locale():
    categories = {}

    def _init_categories(categories=categories):
        for (k, v) in globals().items():
            if k[:3] == 'LC_':
                categories[k] = v

    _init_categories()
    del categories['LC_ALL']
    print 'Locale defaults as determined by getdefaultlocale():'
    print '-' * 72
    (lang, enc) = getdefaultlocale()
    print 'Language: ', lang or '(undefined)'
    print 'Encoding: ', enc or '(undefined)'
    print
    print 'Locale settings on startup:'
    print '-' * 72
    for (name, category) in categories.items():
        print name, '...'
        (lang, enc) = getlocale(category)
        print '   Language: ', lang or '(undefined)'
        print '   Encoding: ', enc or '(undefined)'
        print

    print
    print 'Locale settings after calling resetlocale():'
    print '-' * 72
    resetlocale()
    for (name, category) in categories.items():
        print name, '...'
        (lang, enc) = getlocale(category)
        print '   Language: ', lang or '(undefined)'
        print '   Encoding: ', enc or '(undefined)'
        print

    try:
        setlocale(LC_ALL, '')
    except:
        print 'NOTE:'
        print 'setlocale(LC_ALL, "") does not support the default locale'
        print 'given in the OS environment variables.'
    else:
        print
        print 'Locale settings after calling setlocale(LC_ALL, ""):'
        print '-' * 72
        for (name, category) in categories.items():
            print name, '...'
            (lang, enc) = getlocale(category)
            print '   Language: ', lang or '(undefined)'
            print '   Encoding: ', enc or '(undefined)'
            print


try:
    LC_MESSAGES
except NameError:
    pass
else:
    __all__.append('LC_MESSAGES')

if __name__ == '__main__':
    print 'Locale aliasing:'
    print
    _print_locale()
    print
    print 'Number formatting:'
    print
    _test()