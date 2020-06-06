# File: N (Python 2.2)

import string
from otp.otpbase import OTPLocalizer
from direct.directnotify import DirectNotifyGlobal
notify = DirectNotifyGlobal.directNotify.newCategory('NameCheck')

def filterString(str, filter):
    result = ''
    for char in str:
        if char in filter:
            result = result + char
        
    
    return result


def wordList(str):
    words = str.split()
    result = []
    for word in words:
        subWords = word.split('-')
        for sw in subWords:
            if sw:
                result.append(sw)
            
        
    
    return result


def checkName(name):
    
    def longEnough(name):
        if len(name) < 2:
            notify.info('name is too short')
            return OTPLocalizer.NCTooShort
        

    
    def emptyName(name):
        if name.strip() == '':
            notify.info('name is empty')
            return OTPLocalizer.NCTooShort
        

    
    def printableChars(name):
        for char in name:
            if ord(char) < 128 and char not in string.printable:
                notify.info('name contains non-printable char #%s' % ord(char))
                return OTPLocalizer.NCGeneric
            
        

    
    def badCharacters(name):
        okChars = ".,'-" + string.letters + string.whitespace
        allowUtf8Name = base.config.GetBool('allow-utf8-name', 1)
        for char in name:
            if ord(char) >= 128:
                if not allowUtf8Name:
                    notify.info('name contains utf-8 character.')
                    i = name.index(char)
                    if ord(char) >= 224:
                        char = char + name[i + 1] + name[i + 2]
                    else:
                        char = char + name[i + 1]
                    return OTPLocalizer.NCBadCharacter % char
                
            elif char not in okChars:
                if char in string.digits:
                    notify.info('name contains digits')
                    return OTPLocalizer.NCNoDigits
                else:
                    notify.info('name contains bad char: %s' % char)
                    return OTPLocalizer.NCBadCharacter % char
            
        

    
    def hasLetters(name):
        words = wordList(name)
        for word in words:
            hasUtf8 = 0
            for char in word:
                if ord(char) >= 128:
                    hasUtf8 = 1
                
            
            letters = filterString(word, string.letters)
            if len(letters) == 0 and not hasUtf8:
                notify.info('word "%s" has no letters' % word)
                return OTPLocalizer.NCNeedLetters
            
        

    
    def hasVowels(name):
        
        def perWord(word):
            if '.' in word:
                return None
            
            for char in word:
                if ord(char) >= 128:
                    return None
                
            
            letters = filterString(word, string.letters)
            if len(letters) > 2:
                vowels = filterString(letters, 'aeiouyAEIOUY')
                if len(vowels) == 0:
                    notify.info('word "%s" has no vowels' % word)
                    return OTPLocalizer.NCNeedVowels
                
            

        for word in wordList(name):
            problem = perWord(word)
            if problem:
                return problem
            
        

    
    def monoLetter(name):
        
        def perWord(word):
            for char in word:
                if ord(char) >= 128:
                    return None
                
            
            letters = filterString(word, string.letters)
            if len(letters) > 2:
                filtered = filterString(letters, name[0])
                if filtered == letters:
                    notify.info('word "%s" uses only one letter' % word)
                    return OTPLocalizer.NCGeneric
                
            

        for word in wordList(name):
            problem = perWord(word)
            if problem:
                return problem
            
        

    
    def checkDashes(name):
        
        def validDash(index, name = name):
            if index == 0 or i == len(name) - 1:
                return 0
            
            if not (name[i - 1] in string.letters):
                return 0
            
            if not (name[i + 1] in string.letters):
                return 0
            
            return 1

        i = 0
        while 1:
            i = name.find('-', i, len(name))
            if i < 0:
                return None
            
            if not validDash(i):
                notify.info('name makes invalid use of dashes')
                return OTPLocalizer.NCDashUsage
            
            i += 1

    
    def checkCommas(name):
        
        def validComma(index, name = name):
            if index == 0 or i == len(name) - 1:
                return OTPLocalizer.NCCommaEdge
            
            if name[i - 1] in string.whitespace:
                return OTPLocalizer.NCCommaAfterWord
            
            if not (name[i + 1] in string.whitespace):
                return OTPLocalizer.NCCommaUsage
            
            return None

        i = 0
        while 1:
            i = name.find(',', i, len(name))
            if i < 0:
                return None
            
            problem = validComma(i)
            if problem:
                notify.info('name makes invalid use of commas')
                return problem
            
            i += 1

    
    def checkPeriods(name):
        words = wordList(name)
        for word in words:
            if word[-1] == ',':
                word = word[:-1]
            
            numPeriods = word.count('.')
            if not numPeriods:
                continue
            
            letters = filterString(word, string.letters)
            numLetters = len(letters)
            if word[-1] != '.':
                notify.info('word "%s" does not end in a period' % word)
                return OTPLocalizer.NCPeriodUsage
            
            if numPeriods > 2:
                notify.info('word "%s" has too many periods' % word)
                return OTPLocalizer.NCPeriodUsage
            
            if numPeriods == 2:
                if word[1] == '.':
                    pass
                if not (word[3] == '.'):
                    notify.info('word "%s" does not fit the J.T. pattern' % word)
                    return OTPLocalizer.NCPeriodUsage
                
            
        
        return None

    
    def checkApostrophes(name):
        words = wordList(name)
        for word in words:
            numApos = word.count("'")
            if numApos > 2:
                notify.info('word "%s" has too many apostrophes.' % word)
                return OTPLocalizer.NCApostrophes
            
        
        numApos = name.count("'")
        if numApos > 3:
            notify.info('name has too many apostrophes.')
            return OTPLocalizer.NCApostrophes
        

    
    def tooManyWords(name):
        if len(wordList(name)) > 4:
            notify.info('name has too many words')
            return OTPLocalizer.NCTooManyWords
        

    
    def allCaps(name):
        letters = filterString(name, string.letters)
        if len(letters) > 2:
            if string.upper(letters) == letters:
                notify.info('name is all caps')
                return OTPLocalizer.NCAllCaps
            
        

    
    def mixedCase(name):
        words = wordList(name)
        for word in words:
            if len(word) > 2:
                capitals = filterString(word, string.uppercase)
                if len(capitals) > 2:
                    notify.info('name has mixed case')
                    return OTPLocalizer.NCMixedCase
                
            
        

    
    def npcNames(name):
        
        def match(npcName, name = name):
            return string.upper(npcName) == string.upper(string.strip(name))


    checks = [
        longEnough,
        emptyName,
        printableChars,
        badCharacters,
        hasLetters,
        hasVowels,
        monoLetter,
        checkDashes,
        checkCommas,
        checkPeriods,
        checkApostrophes,
        tooManyWords,
        allCaps,
        mixedCase]
    symmetricChecks = [
        npcNames]
    notify.info('checking name "%s"...' % name)
    for check in checks:
        problem = check(name[:])
        if not problem and check in symmetricChecks:
            bName = name[:]
            bName = list(bName)
            bName.reverse()
            bName = string.join(bName, '')
            problem = check(bName)
        
        if problem:
            return problem
        
    
    return None

