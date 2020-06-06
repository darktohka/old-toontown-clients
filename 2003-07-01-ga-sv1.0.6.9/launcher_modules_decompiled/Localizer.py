# File: L (Python 2.2)

from libpandaexpressGlobals import *
import string
import types

try:
    language = getConfigExpress().GetString('language', 'english')
    checkLanguage = getConfigExpress().GetBool('check-language', 1)
except:
    language = simbase.config.GetString('language', 'english')
    checkLanguage = simbase.config.GetBool('check-language', 1)


def getLanguage():
    return language

print 'Localizer: Running in language: %s' % language
_languageModule = 'Localizer' + string.capitalize(language)
exec 'from ' + _languageModule + ' import *'
if checkLanguage:
    l = { }
    g = { }
    englishModule = __import__('LocalizerEnglish', g, l)
    foreignModule = __import__(_languageModule, g, l)
    for (key, val) in englishModule.__dict__.items():
        if not foreignModule.__dict__.has_key(key):
            print 'WARNING: Foreign module: %s missing key: %s' % (_languageModule, key)
            locals()[key] = val
        elif isinstance(val, types.DictType):
            fval = foreignModule.__dict__.get(key)
            for (dkey, dval) in val.items():
                if not fval.has_key(dkey):
                    print 'WARNING: Foreign module: %s missing key: %s.%s' % (_languageModule, key, dkey)
                    fval[dkey] = dval
                
            
            for dkey in fval.keys():
                if not val.has_key(dkey):
                    print 'WARNING: Foreign module: %s extra key: %s.%s' % (_languageModule, key, dkey)
                
            
        
    
    for key in foreignModule.__dict__.keys():
        if not englishModule.__dict__.has_key(key):
            print 'WARNING: Foreign module: %s extra key: %s' % (_languageModule, key)
        
    

