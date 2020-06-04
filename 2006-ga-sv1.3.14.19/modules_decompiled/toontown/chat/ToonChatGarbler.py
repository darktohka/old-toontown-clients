# File: T (Python 2.2)

import string
import whrandom
from toontown.toonbase import TTLocalizer
from otp.otpbase import OTPLocalizer
from otp.chat import ChatGarbler

class ToonChatGarbler(ChatGarbler.ChatGarbler):
    animalSounds = {
        'dog': TTLocalizer.ChatGarblerDog,
        'cat': TTLocalizer.ChatGarblerCat,
        'mouse': TTLocalizer.ChatGarblerMouse,
        'horse': TTLocalizer.ChatGarblerHorse,
        'rabbit': TTLocalizer.ChatGarblerRabbit,
        'duck': TTLocalizer.ChatGarblerDuck,
        'default': OTPLocalizer.ChatGarblerDefault }
    
    def garble(self, toon, message):
        newMessage = ''
        animalType = toon.getStyle().getType()
        if ToonChatGarbler.animalSounds.has_key(animalType):
            wordlist = ToonChatGarbler.animalSounds[animalType]
        else:
            wordlist = ToonChatGarbler.animalSounds['default']
        numWords = whrandom.randint(1, 7)
        for i in range(1, numWords + 1):
            wordIndex = whrandom.randint(0, len(wordlist) - 1)
            newMessage = newMessage + wordlist[wordIndex]
            if i < numWords:
                newMessage = newMessage + ' '
            
        
        return newMessage


