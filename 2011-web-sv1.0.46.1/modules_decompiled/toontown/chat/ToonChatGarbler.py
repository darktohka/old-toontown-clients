# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\chat\ToonChatGarbler.py
import string, random
from toontown.toonbase import TTLocalizer
from otp.otpbase import OTPLocalizer
from otp.chat import ChatGarbler

class ToonChatGarbler(ChatGarbler.ChatGarbler):
    __module__ = __name__
    animalSounds = {'dog': TTLocalizer.ChatGarblerDog, 'cat': TTLocalizer.ChatGarblerCat, 'mouse': TTLocalizer.ChatGarblerMouse, 'horse': TTLocalizer.ChatGarblerHorse, 'rabbit': TTLocalizer.ChatGarblerRabbit, 'duck': TTLocalizer.ChatGarblerDuck, 'monkey': TTLocalizer.ChatGarblerMonkey, 'bear': TTLocalizer.ChatGarblerBear, 'pig': TTLocalizer.ChatGarblerPig, 'default': OTPLocalizer.ChatGarblerDefault}

    def garble(self, toon, message):
        newMessage = ''
        animalType = toon.getStyle().getType()
        if ToonChatGarbler.animalSounds.has_key(animalType):
            wordlist = ToonChatGarbler.animalSounds[animalType]
        else:
            wordlist = ToonChatGarbler.animalSounds['default']
        numWords = random.randint(1, 7)
        for i in range(1, numWords + 1):
            wordIndex = random.randint(0, len(wordlist) - 1)
            newMessage = newMessage + wordlist[wordIndex]
            if i < numWords:
                newMessage = newMessage + ' '

        return newMessage

    def garbleSingle(self, toon, message):
        newMessage = ''
        animalType = toon.getStyle().getType()
        if ToonChatGarbler.animalSounds.has_key(animalType):
            wordlist = ToonChatGarbler.animalSounds[animalType]
        else:
            wordlist = ToonChatGarbler.animalSounds['default']
        numWords = 1
        for i in range(1, numWords + 1):
            wordIndex = random.randint(0, len(wordlist) - 1)
            newMessage = newMessage + wordlist[wordIndex]
            if i < numWords:
                newMessage = newMessage + ' '

        return newMessage