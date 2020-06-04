# File: C (Python 2.2)

import string
import whrandom
from otp.otpbase import OTPLocalizer

class ChatGarbler:
    
    def garble(self, avatar, message):
        newMessage = ''
        numWords = whrandom.randint(1, 7)
        wordlist = OTPLocalizer.ChatGarblerDefault
        for i in range(1, numWords + 1):
            wordIndex = whrandom.randint(0, len(wordlist) - 1)
            newMessage = newMessage + wordlist[wordIndex]
            if i < numWords:
                newMessage = newMessage + ' '
            
        
        return newMessage


