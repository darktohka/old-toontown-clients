# File: C (Python 2.2)

import string
import whrandom
import Localizer

class ChatGarbler:
    animalSounds = {
        'dog': Localizer.ChatGarblerDog,
        'cat': Localizer.ChatGarblerCat,
        'mouse': Localizer.ChatGarblerMouse,
        'horse': Localizer.ChatGarblerHorse,
        'rabbit': Localizer.ChatGarblerRabbit,
        'fowl': Localizer.ChatGarblerFowl,
        'default': Localizer.ChatGarblerDefault }
    
    def garble(self, toon, message):
        newMessage = ''
        animalType = toon.getStyle().getType()
        if ChatGarbler.animalSounds.has_key(animalType):
            wordlist = ChatGarbler.animalSounds[animalType]
        else:
            wordlist = ChatGarbler.animalSounds['default']
        numWords = whrandom.randint(1, 7)
        for i in range(1, numWords + 1):
            wordIndex = whrandom.randint(0, len(wordlist) - 1)
            newMessage = newMessage + wordlist[wordIndex]
            if i < numWords:
                newMessage = newMessage + ' '
            
        
        return newMessage


