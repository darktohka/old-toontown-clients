# File: L (Python 2.2)

from libpandaexpressGlobals import *
import string

try:
    language = getConfigExpress().GetString('language', 'english')
except:
    language = simbase.config.GetString('language', 'english')

print 'Localizer: Running in language: %s' % language
_languageModule = 'Localizer' + string.capitalize(language)
exec 'from ' + _languageModule + ' import *'
