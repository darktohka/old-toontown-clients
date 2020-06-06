# File: P (Python 2.2)

from direct.directnotify import DirectNotifyGlobal

class ParentMgr:
    notify = DirectNotifyGlobal.directNotify.newCategory('ParentMgr')
    
    def __init__(self):
        self.token2nodepath = { }
        self.pendingParentToken2children = { }
        self.pendingChild2parentToken = { }

    
    def destroy(self):
        del self.token2nodepath
        del self.pendingParentToken2children
        del self.pendingChild2parentToken

    
    def privRemoveReparentRequest(self, child):
        if child in self.pendingChild2parentToken:
            self.notify.debug("cancelling pending reparent of %s to '%s'" % (repr(child), self.pendingChild2parentToken[child]))
            parentToken = self.pendingChild2parentToken[child]
            del self.pendingChild2parentToken[child]
            self.pendingParentToken2children[parentToken].remove(child)
        

    
    def requestReparent(self, child, parentToken):
        if self.token2nodepath.has_key(parentToken):
            self.privRemoveReparentRequest(child)
            self.notify.debug("performing wrtReparent of %s to '%s'" % (repr(child), parentToken))
            child.wrtReparentTo(self.token2nodepath[parentToken])
        else:
            self.notify.warning("child %s requested reparent to parent '%s' that is not (yet) registered" % (repr(child), parentToken))
            self.privRemoveReparentRequest(child)
            self.pendingChild2parentToken[child] = parentToken
            self.pendingParentToken2children.setdefault(parentToken, [])
            self.pendingParentToken2children[parentToken].append(child)
            child.reparentTo(hidden)

    
    def registerParent(self, token, parent):
        if self.token2nodepath.has_key(token):
            self.notify.error("registerParent: token '%s' already registered, referencing %s" % (token, repr(self.token2nodepath[token])))
        
        self.notify.debug("registering %s as '%s'" % (repr(parent), token))
        self.token2nodepath[token] = parent
        if token in self.pendingParentToken2children:
            children = self.pendingParentToken2children[token]
            del self.pendingParentToken2children[token]
            for child in children:
                self.notify.debug("performing reparent of %s to '%s'" % (repr(child), token))
                child.reparentTo(self.token2nodepath[token])
                del self.pendingChild2parentToken[child]
            
        

    
    def unregisterParent(self, token):
        if not self.token2nodepath.has_key(token):
            self.notify.warning("unregisterParent: unknown parent token '%s'" % token)
            return None
        
        self.notify.debug("unregistering parent '%s'" % token)
        del self.token2nodepath[token]


