# File: I (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
import string

def isValidEmailAddr(addr):
    strict = config.GetBool('strict-email-check', 1)
    if not strict:
        return len(addr) > 0
    
    sections = addr.split('@')
    if len(sections) != 2:
        return 0
    
    (name, host) = sections
    if len(name) == 0:
        return 0
    
    sections = host.split('.')
    if len(sections) < 2:
        return 0
    
    if len(sections[-1]) == 0:
        return 0
    
    return 1


def emailAddrMatch(addr1, addr2):
    return addr1 == addr2


def stripWhitespace(str):
    return str.replace(' ', '')


def isBlank(text):
    return stripWhitespace(text) == ''


def stripCreditCardNumber(str):
    legalChars = (' ', '-')
    for char in legalChars:
        str = str.replace(char, '')
    
    return str


def isNumeric(str):
    return str.isdigit()


def isCorrectCreditCardLength(num, ccType = 'any'):
    if ccType == 'American Express':
        if len(num) != 15:
            return 0
        
    elif ccType == 'Visa':
        if len(num) != 16:
            return 0
        
    elif ccType == 'MasterCard':
        if len(num) != 16:
            return 0
        
    elif ccType == 'any':
        if len(num) not in (15, 16):
            return 0
        
    
    return 1


def creditCardNumberMatchesType(num, ccType = 'any'):
    if ccType == 'American Express':
        if num[0] != '3':
            return 0
        
    elif ccType == 'Visa':
        if num[0] != '4':
            return 0
        
    elif ccType == 'MasterCard':
        if num[0] != '5':
            return 0
        
    elif ccType == 'any':
        if num[0] not in ('3', '4', '5'):
            return 0
        
    
    return 1


def isValidCreditCardNum(num, ccType = 'any'):
    if not isNumeric(num):
        return 0
    
    if not isCorrectCreditCardLength(num, ccType):
        return 0
    
    if not creditCardNumberMatchesType(num, ccType):
        return 0
    
    return 1


def isValidCreditCardExpDate(month, year, curMonth = None, curYear = None):
    if curYear == None:
        curYear = base.cr.dateObject.getYear()
    
    if curMonth == None:
        curMonth = base.cr.dateObject.getMonth()
    
    year = int(year)
    month = int(month)
    if year < curYear:
        return 0
    
    if year > curYear:
        return 1
    
    if month < curMonth:
        return 0
    
    return 1

