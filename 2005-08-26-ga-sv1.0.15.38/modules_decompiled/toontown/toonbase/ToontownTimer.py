# File: T (Python 2.2)

from otp.otpbase import OTPTimer
from direct.showbase.ShowBaseGlobal import *
from ToontownGlobals import *
from direct.task import Task

class ToontownTimer(OTPTimer.OTPTimer):
    
    def __init__(self):
        OTPTimer.OTPTimer.__init__(self)
        self.initialiseoptions(ToontownTimer)

    
    def getImage(self):
        if ToontownTimer.ClockImage == None:
            model = loader.loadModel('phase_3.5/models/gui/clock_gui')
            ToontownTimer.ClockImage = model.find('**/alarm_clock')
            model.removeNode()
        
        return ToontownTimer.ClockImage


