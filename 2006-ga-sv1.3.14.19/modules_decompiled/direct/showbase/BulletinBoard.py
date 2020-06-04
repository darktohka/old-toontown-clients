# File: B (Python 2.2)

from direct.directnotify import DirectNotifyGlobal

class BulletinBoard:
    notify = DirectNotifyGlobal.directNotify.newCategory('BulletinBoard')
    
    def __init__(self):
        self._dict = { }

    
    def get(self, name):
        return self._dict.get(name)

    
    def has(self, name):
        return name in self._dict

    
    def post(self, name, value = None):
        if name in self._dict:
            BulletinBoard.notify.warning('changing %s from %s to %s' % (name, self._dict[name], value))
        
        self.update(name, value)

    
    def update(self, name, value):
        if name in self._dict:
            BulletinBoard.notify.info('update: posting %s' % name)
        
        self._dict[name] = value

    
    def remove(self, name):
        if name in self._dict:
            del self._dict[name]
        

    
    def __repr__(self):
        return str(self._dict)


