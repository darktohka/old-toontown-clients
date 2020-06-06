# File: T (Python 2.2)

from direct.gui.DirectGui import *
from toontown.toonbase import ToontownTimer
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import ToontownBattleGlobals
from toontown.toonbase import TTLocalizer

class TrackPoster(DirectFrame):
    normalTextColor = (0.29999999999999999, 0.25, 0.20000000000000001, 1)
    
    def __init__(self, trackId, callback):
        DirectFrame.__init__(self, relief = None)
        self.initialiseoptions(TrackPoster)
        bookModel = loader.loadModelOnce('phase_3.5/models/gui/stickerbook_gui')
        trackName = ToontownBattleGlobals.Tracks[trackId].capitalize()
        self.poster = DirectFrame(parent = self, relief = None, image = bookModel.find('**/questCard'), image_scale = (0.80000000000000004, 0.57999999999999996, 0.57999999999999996))
        invModel = loader.loadModelOnce('phase_3.5/models/gui/inventory_icons')
        iconGeom = invModel.find('**/' + ToontownBattleGlobals.AvPropsNew[trackId][1])
        invModel.removeNode()
        self.pictureFrame = DirectFrame(parent = self.poster, relief = None, image = bookModel.find('**/questPictureFrame'), image_scale = 0.25, image_color = (0.45000000000000001, 0.80000000000000004, 0.45000000000000001, 1), text = trackName, text_font = ToontownGlobals.getInterfaceFont(), text_pos = (0, -0.16), text_fg = self.normalTextColor, text_scale = 0.050000000000000003, text_align = TextNode.ACenter, text_wordwrap = 8.0, textMayChange = 0, geom = iconGeom, pos = (-0.20000000000000001, 0, 0.059999999999999998))
        bookModel.removeNode()
        if trackId == ToontownBattleGlobals.HEAL_TRACK:
            help = TTLocalizer.TrackChoiceGuiHEAL
        elif trackId == ToontownBattleGlobals.TRAP_TRACK:
            help = TTLocalizer.TrackChoiceGuiTRAP
        elif trackId == ToontownBattleGlobals.LURE_TRACK:
            help = TTLocalizer.TrackChoiceGuiLURE
        elif trackId == ToontownBattleGlobals.SOUND_TRACK:
            help = TTLocalizer.TrackChoiceGuiSOUND
        elif trackId == ToontownBattleGlobals.DROP_TRACK:
            help = TTLocalizer.TrackChoiceGuiDROP
        else:
            help = ''
        self.helpText = DirectFrame(parent = self.poster, relief = None, text = help, text_font = ToontownGlobals.getInterfaceFont(), text_fg = self.normalTextColor, text_scale = 0.050000000000000003, text_align = TextNode.ALeft, text_wordwrap = 8.0, textMayChange = 0, pos = (-0.050000000000000003, 0, 0.14000000000000001))
        guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
        self.chooseButton = DirectButton(parent = self.poster, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (0.69999999999999996, 1, 1), text = TTLocalizer.TrackChoiceGuiChoose, text_scale = 0.059999999999999998, text_pos = (0, -0.02), command = callback, extraArgs = [
            trackId], pos = (0, 0, -0.16), scale = 0.80000000000000004)
        guiButton.removeNode()



class TrackChoiceGui(DirectFrame):
    
    def __init__(self, tracks, timeout):
        DirectFrame.__init__(self, relief = None, geom = getDefaultDialogGeom(), geom_color = Vec4(0.80000000000000004, 0.59999999999999998, 0.40000000000000002, 1), geom_scale = (1.5, 1, 0.90000000000000002), geom_hpr = (0, 0, -90), pos = (-0.84999999999999998, 0, 0))
        self.initialiseoptions(TrackChoiceGui)
        guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
        self.cancelButton = DirectButton(parent = self, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (0.69999999999999996, 1, 1), text = TTLocalizer.TrackChoiceGuiCancel, pos = (0.14999999999999999, 0, -0.625), text_scale = 0.059999999999999998, text_pos = (0, -0.02), command = self.chooseTrack, extraArgs = [
            -1])
        guiButton.removeNode()
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.reparentTo(self)
        self.timer.setScale(0.34999999999999998)
        self.timer.setPos(-0.20000000000000001, 0, -0.59999999999999998)
        self.timer.countdown(timeout, self.timeout)
        self.trackChoicePosters = []
        for trackId in tracks:
            tp = TrackPoster(trackId, self.chooseTrack)
            tp.reparentTo(self)
            self.trackChoicePosters.append(tp)
        
        self.trackChoicePosters[0].setPos(0, 0, -0.20000000000000001)
        self.trackChoicePosters[1].setPos(0, 0, 0.40000000000000002)

    
    def chooseTrack(self, trackId):
        self.timer.stop()
        messenger.send('chooseTrack', [
            trackId])

    
    def timeout(self):
        messenger.send('chooseTrack', [
            -1])


