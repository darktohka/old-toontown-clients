# File: P (Python 2.2)

from ShowBaseGlobal import *
from ToontownGlobals import *
import DirectNotifyGlobal

class ParentMgr:
    notify = DirectNotifyGlobal.directNotify.newCategory('ParentMgr')
    
    def __init__(self):
        self.token2nodepath = { }
        self.pendingChildren = { }

    
    def destroy(self):
        del self.token2nodepath
        del self.pendingChildren

    
    def requestReparent(self, child, parentToken):
        if parentToken in self.token2nodepath.keys():
            self.notify.debug("performing wrtReparent of %s to '%s'" % (repr(child), parentToken))
            child.wrtReparentTo(self.token2nodepath[parentToken])
        else:
            self.notify.warning("child %s requested reparent to '%s', not in list" % (repr(child), parentToken))
            if not self.pendingChildren.has_key(parentToken):
                self.pendingChildren[parentToken] = []
            
            self.pendingChildren[parentToken].append(child)

    
    def registerParent(self, token, parent):
        if token in self.token2nodepath.keys():
            self.notify.error("token '%s' already in the table, referencing %s" % (token, repr(self.token2nodepath[token])))
        
        self.notify.debug("registering %s as '%s'" % (repr(parent), token))
        self.token2nodepath[token] = parent
        if token in self.pendingChildren.keys():
            children = self.pendingChildren[token]
            for child in children:
                self.notify.debug("performing reparent of %s to '%s'" % (repr(child), token))
                child.reparentTo(self.token2nodepath[token])
            
            del self.pendingChildren[token]
        

    
    def unregisterParent(self, token):
        if token not in self.token2nodepath.keys():
            self.notify.warning("unknown token '%s'" % token)
            return None
        
        self.notify.debug("unregistering parent '%s'" % token)
        del self.token2nodepath[token]


