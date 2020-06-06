# File: T (Python 2.2)

import TTStreet
import NametagGlobals

class TutorialStreet(TTStreet.TTStreet):
    
    def enter(self, requestStatus):
        TTStreet.TTStreet.enter(self, requestStatus, visibilityFlag = 0, arrowsOn = 0)

    
    def exit(self):
        TTStreet.TTStreet.exit(self, visibilityFlag = 0)

    
    def enterTeleportIn(self, requestStatus):
        TTStreet.TTStreet.enterTeleportIn(self, requestStatus)
        return None

    
    def enterTownBattle(self, event):
        self.loader.townBattle.enter(event, self.fsm.getStateNamed('battle'), tutorialFlag = 1)

    
    def handleEnterTunnel(self, requestStatus, collEntry):
        messenger.send('stopTutorial')
        TTStreet.TTStreet.handleEnterTunnel(self, requestStatus, collEntry)
        return None

    
    def exitDoorIn(self):
        toonbase.localToon.obscureMoveFurnitureButton(-1)


