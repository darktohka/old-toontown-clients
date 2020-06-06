# File: B (Python 2.2)

from direct.directnotify import DirectNotifyGlobal

class BulletinBoard:
    notify = DirectNotifyGlobal.directNotify.newCategory('BulletinBoard')
    
    def __init__(self):
        self._dict = { }

    
    def get(self, postName, default = None):
        return self._dict.get(postName, default)

    
    def has(self, postName):
        return postName in self._dict

    
    def getEventName(self, postName):
        return 'bboard-%s' % postName

    
    def post(self, postName, value = None):
        if postName in self._dict:
            BulletinBoard.notify.warning('changing %s from %s to %s' % (postName, self._dict[postName], value))
        
        self.update(postName, value)

    
    def update(self, postName, value):
        if postName in self._dict:
            BulletinBoard.notify.info('update: posting %s' % postName)
        
        self._dict[postName] = value
        messenger.send(self.getEventName(postName))

    
    def remove(self, postName):
        if postName in self._dict:
            del self._dict[postName]
        

    
    def removeIfEqual(self, postName, value):
        if self.has(postName):
            if self.get(postName) == value:
                self.remove(postName)
            
        

    
    def __repr__(self):
        str = 'Bulletin Board Contents\n'
        str += '======================='
        keys = self._dict.keys()
        keys.sort()
        for postName in keys:
            str += '\n%s: %s' % (postName, self._dict[postName])
        
        return str


