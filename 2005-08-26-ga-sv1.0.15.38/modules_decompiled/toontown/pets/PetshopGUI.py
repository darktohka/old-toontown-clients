# File: P (Python 2.2)

from direct.gui.DirectGui import *
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownTimer
from direct.task import Task
from otp.namepanel import NameTumbler
from otp.otpbase import OTPGlobals
from otp.otpbase import OTPLocalizer
from toontown.fishing import FishSellGUI
from toontown.pets import Pet, PetConstants
from toontown.pets import PetDNA
from toontown.pets import PetUtil
from toontown.pets import PetDetail
from toontown.pets import PetTraits
from toontown.pets import PetNameGenerator
from toontown.hood import ZoneUtil
import string
Dialog_MainMenu = 0
Dialog_AdoptPet = 1
Dialog_ChoosePet = 2
Dialog_ReturnPet = 3
Dialog_SellFish = 4
Dialog_NamePicker = 5
Dialog_GoHome = 6
disabledImageColor = Vec4(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 1)
text0Color = Vec4(0.65000000000000002, 0, 0.87, 1)
text1Color = Vec4(0.65000000000000002, 0, 0.87, 1)
text2Color = Vec4(1, 1, 0.5, 1)
text3Color = Vec4(0.40000000000000002, 0.40000000000000002, 0.40000000000000002, 1)

class PetshopGUI(DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('PetshopGui')
    
    class GoHomeDlg(DirectFrame):
        notify = DirectNotifyGlobal.directNotify.newCategory('GoHomeDlg')
        
        def __init__(self, doneEvent):
            DirectFrame.__init__(self, pos = (0.0, 0.0, 0.0), image_color = ToontownGlobals.GlobalDialogColor, image_scale = (1.0, 1.0, 0.59999999999999998), text = '', text_wordwrap = 13.5, text_scale = 0.059999999999999998, text_pos = (0.0, 0.13))
            self['image'] = getDefaultDialogGeom()
            self['text'] = TTLocalizer.PetshopGoHomeText
            buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
            gui = loader.loadModelOnce('phase_3.5/models/gui/avatar_panel_gui')
            self.bYes = DirectButton(self, image = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr')), relief = None, text = TTLocalizer.TutorialYes, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), pos = (-0.14999999999999999, 0.0, -0.10000000000000001), command = lambda : messenger.send(doneEvent, [
1]))
            self.bNo = DirectButton(self, image = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr')), relief = None, text = TTLocalizer.TutorialNo, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), pos = (0.14999999999999999, 0.0, -0.10000000000000001), command = lambda : messenger.send(doneEvent, [
0]))
            buttons.removeNode()
            gui.removeNode()


    
    class NamePicker(DirectFrame):
        notify = DirectNotifyGlobal.directNotify.newCategory('PetshopGUI.NamePicker')
        
        def __init__(self, doneEvent, petSeed, gender):
            zoneId = ZoneUtil.getCanonicalSafeZoneId(base.localAvatar.getZoneId())
            (name, dna, traitSeed) = PetUtil.getPetInfoFromSeed(petSeed, zoneId)
            self.gui = loader.loadModelOnce('phase_4/models/gui/PetNamePanel')
            self.guiScale = 0.089999999999999997
            DirectFrame.__init__(self, relief = None, geom = self.gui, geom_scale = self.guiScale, state = 'normal', frameSize = (-1, 1, -1, 1))
            self.initialiseoptions(PetshopGUI.NamePicker)
            self.petView = self.attachNewNode('petView')
            self.petView.setPos(-0.20999999999999999, 0, -0.040000000000000001)
            self.petModel = Pet.Pet(forGui = 1)
            self.petModel.setDNA(dna)
            self.petModel.fitAndCenterHead(0.435, forGui = 1)
            self.petModel.reparentTo(self.petView)
            self.petModel.setH(225)
            self.petModel.enterNeutralHappy()
            self.ng = PetNameGenerator.PetNameGenerator()
            if gender == 1:
                self.allNames = self.ng.boyFirsts
            else:
                self.allNames = self.ng.girlFirsts
            self.allNames += self.ng.neutralFirsts
            self.allNames.sort()
            self.checkNames()
            self.letters = []
            for name in self.allNames:
                if not (name[0] in self.letters):
                    self.letters += name[0]
                
            
            self.curLetter = self.letters[0]
            self.curNames = []
            self.curName = ''
            self.alphabetList = self.makeScrollList(self.gui, (-0.012, 0, -0.074999999999999997), (1, 0.80000000000000004, 0.80000000000000004, 1), self.letters, self.makeLabel, [
                TextNode.ACenter,
                'alphabet'], 6)
            self.nameList = None
            self.rebuildNameList()
            self.randomButton = DirectButton(parent = self, relief = None, image = (self.gui.find('**/RandomUpButton'), self.gui.find('**/RandomDownButton'), self.gui.find('**/RandomRolloverButton')), scale = self.guiScale, text = TTLocalizer.RandomButton, text_pos = (-0.80000000000000004, -5.7000000000000002), text_scale = 0.80000000000000004, text_fg = text2Color, pressEffect = False, command = self.randomName)
            self.nameResult = DirectLabel(parent = self, relief = None, scale = self.guiScale, text = '', text_align = TextNode.ACenter, text_pos = (-1.8500000000000001, 2.6000000000000001), text_fg = text0Color, text_scale = 0.59999999999999998, text_wordwrap = 8)
            self.submitButton = DirectButton(parent = self, relief = None, image = (self.gui.find('**/SubmitUpButton'), self.gui.find('**/SubmitDownButton'), self.gui.find('**/SubmitRolloverButton')), scale = self.guiScale, text = TTLocalizer.PetshopAdopt, text_pos = (3.2999999999999998, -5.7000000000000002), text_scale = 0.80000000000000004, text_fg = text0Color, pressEffect = False, command = lambda : messenger.send(doneEvent, [
self.ng.returnUniqueID(self.curName)]))
            model = loader.loadModelOnce('phase_4/models/gui/PetShopInterface')
            modelScale = 0.10000000000000001
            cancelImageList = (model.find('**/CancelButtonUp'), model.find('**/CancelButtonDown'), model.find('**/CancelButtonRollover'))
            cancelIcon = model.find('**/CancelIcon')
            self.cancelButton = DirectButton(parent = self, relief = None, pos = (-0.040000000000000001, 0, -0.46999999999999997), image = cancelImageList, geom = cancelIcon, scale = modelScale, pressEffect = False, command = lambda : messenger.send(doneEvent, [
-1]))
            self.randomName()

        
        def checkNames(self):
            if __dev__:
                for name in self.allNames:
                    if not name.replace(' ', '').isalpha():
                        self.notify.warning('Bad name:%s' % name)
                    
                
            

        
        def destroy(self):
            self.petModel.delete()
            DirectFrame.destroy(self)

        
        def rebuildNameList(self):
            self.curNames = []
            for name in self.allNames:
                if name[0] == self.curLetter:
                    self.curNames += [
                        name]
                
            
            if self.nameList:
                self.nameList.destroy()
            
            self.nameList = self.makeScrollList(self.gui, (0.27700000000000002, 0, -0.074999999999999997), (1, 0.80000000000000004, 0.80000000000000004, 1), self.curNames, self.makeLabel, [
                TextNode.ACenter,
                'name'], 5)

        
        def updateNameText(self):
            self.nameResult['text'] = self.curName

        
        def nameClickedOn(self, listType, index):
            if listType == 'alphabet':
                self.curLetter = self.letters[index]
                self.rebuildNameList()
            elif listType == 'name':
                self.curName = self.curNames[index]
                self.updateNameText()
            

        
        def makeLabel(self, te, index, others):
            alig = others[0]
            listName = others[1]
            if alig == TextNode.ARight:
                newpos = (0.44, 0, 0)
            elif alig == TextNode.ALeft:
                newpos = (0, 0, 0)
            else:
                newpos = (0.20000000000000001, 0, 0)
            df = DirectButton(parent = self, state = 'normal', relief = None, text = te, text_scale = 0.10000000000000001, text_pos = (0.20000000000000001, 0, 0), text_align = alig, textMayChange = 0, command = lambda : self.nameClickedOn(listName, index))
            return df

        
        def makeScrollList(self, gui, ipos, mcolor, nitems, nitemMakeFunction, nitemMakeExtraArgs, nVisibleItems):
            decScale = self.guiScale / 0.44
            incScale = (decScale, decScale, -decScale)
            it = nitems[:]
            listType = nitemMakeExtraArgs[1]
            if listType == 'alphabet':
                arrowList = (gui.find('**/ArrowSmUpButton'), gui.find('**/ArrowSmUpRollover'), gui.find('**/ArrowSmUpRollover'), gui.find('**/ArrowSmUpButton'))
                fHeight = 0.089999999999999997
            elif listType == 'name':
                arrowList = (gui.find('**/ArrowUpBigButton'), gui.find('**/ArrowUpBigRollover'), gui.find('**/ArrowUpBigRollover'), gui.find('**/ArrowUpBigButton'))
                fHeight = 0.11899999999999999
            
            ds = DirectScrolledList(parent = self, items = it, itemMakeFunction = nitemMakeFunction, itemMakeExtraArgs = nitemMakeExtraArgs, relief = None, command = None, pos = ipos, scale = 0.44, incButton_image = arrowList, incButton_image_pos = (1.0149999999999999, 0, 3.3199999999999998), incButton_relief = None, incButton_scale = incScale, incButton_image3_color = Vec4(0.40000000000000002, 0.40000000000000002, 0.40000000000000002, 1), decButton_image = arrowList, decButton_image_pos = (1.0149999999999999, 0, 1.1100000000000001), decButton_relief = None, decButton_scale = decScale, decButton_image3_color = Vec4(0.40000000000000002, 0.40000000000000002, 0.40000000000000002, 1), numItemsVisible = nVisibleItems, forceHeight = fHeight)
            return ds

        
        def randomName(self):
            numNames = len(self.allNames)
            self.curName = self.allNames[random.randrange(numNames)]
            self.curLetter = self.curName[0]
            self.rebuildNameList()
            self.updateNameText()
            self.alphabetList.scrollTo(self.letters.index(self.curLetter))
            self.nameList.scrollTo(self.curNames.index(self.curName))


    
    class MainMenuDlg(DirectFrame):
        notify = DirectNotifyGlobal.directNotify.newCategory('PetshopGUI.MainMenuDlg')
        
        def __init__(self, doneEvent):
            model = loader.loadModelCopy('phase_4/models/gui/AdoptReturnSell')
            modelPos = (0, 0, -0.29999999999999999)
            modelScale = 0.055
            DirectFrame.__init__(self, relief = None, state = 'normal', geom = model, geom_scale = (modelScale, modelScale, modelScale), pos = modelPos, frameSize = (-1, 1, -1, 1))
            self.initialiseoptions(PetshopGUI.MainMenuDlg)
            textScale = 1
            sellFishImageList = (model.find('**/SellButtonUp'), model.find('**/SellButtonDown'), model.find('**/SellButtonRollover'), model.find('**/SellButtonDown'))
            fishLogoImageList = model.find('**/Fish')
            cancelImageList = (model.find('**/CancelButtonUp'), model.find('**/cancelButtonDown'), model.find('**/CancelButtonRollover'))
            XImageList = model.find('**/CancelIcon')
            adoptImageList = (model.find('**/AdoptButtonUp'), model.find('**/AdoptButtonDown'), model.find('**/AdoptButtonRollover'))
            pawLogoAdoptImageList = model.find('**/PawPink')
            returnImageList = (model.find('**/ReturnButtonUp'), model.find('**/ReturnButtonDown'), model.find('**/ReturnButtonRollover'), model.find('**/ReturnButtonDown'))
            pawLogoReturnImageList = model.find('**/PawYellow')
            self.cancelButton = DirectButton(parent = self, relief = None, scale = (modelScale, modelScale, modelScale), geom = XImageList, image = cancelImageList, text = ('', TTLocalizer.PetshopCancel), text_pos = (-3.2999999999999998, 2.9500000000000002), text_scale = 0.80000000000000004, pressEffect = False, command = lambda : messenger.send(doneEvent, [
0]))
            self.sellFishButton = DirectButton(parent = self, relief = None, image = sellFishImageList, image3_color = disabledImageColor, geom = fishLogoImageList, scale = (modelScale, modelScale, modelScale), text = TTLocalizer.PetshopSell, text_scale = textScale, text_pos = (0, 6), text0_fg = text2Color, text1_fg = text2Color, text2_fg = text0Color, text3_fg = text3Color, pressEffect = False, command = lambda : messenger.send(doneEvent, [
1]))
            fishValue = base.localAvatar.fishTank.getTotalValue()
            if fishValue == 0:
                self.sellFishButton['state'] = DISABLED
            
            self.adoptPetButton = DirectButton(parent = self, relief = None, image = adoptImageList, geom = pawLogoAdoptImageList, scale = (modelScale, modelScale, modelScale), text = TTLocalizer.PetshopAdoptAPet, text_scale = textScale, text_pos = (0, 12.5), text0_fg = text0Color, text1_fg = text1Color, text2_fg = text2Color, text3_fg = text3Color, pressEffect = False, command = lambda : messenger.send(doneEvent, [
2]))
            self.returnPetButton = DirectButton(parent = self, relief = None, image = returnImageList, geom = pawLogoReturnImageList, image3_color = disabledImageColor, scale = (modelScale, modelScale, modelScale), text = TTLocalizer.PetshopReturnPet, text_scale = textScale, text_pos = (-0.59999999999999998, 9.1999999999999993), text0_fg = text2Color, text1_fg = text2Color, text2_fg = text0Color, text3_fg = text3Color, pressEffect = False, command = lambda : messenger.send(doneEvent, [
3]))
            if not base.localAvatar.hasPet():
                self.returnPetButton['state'] = DISABLED
            
            model.removeNode()


    
    class AdoptPetDlg(DirectFrame):
        notify = DirectNotifyGlobal.directNotify.newCategory('PetshopGUI.AdoptPetDlg')
        
        def __init__(self, doneEvent, petSeed, petNameIndex):
            zoneId = ZoneUtil.getCanonicalSafeZoneId(base.localAvatar.getZoneId())
            (name, dna, traitSeed) = PetUtil.getPetInfoFromSeed(petSeed, zoneId)
            name = PetNameGenerator.PetNameGenerator().getName(petNameIndex)
            cost = PetUtil.getPetCostFromSeed(petSeed, zoneId)
            model = loader.loadModelOnce('phase_4/models/gui/AdoptPet')
            modelPos = (0, 0, -0.29999999999999999)
            modelScale = 0.055
            DirectFrame.__init__(self, relief = None, state = 'normal', geom = model, geom_color = ToontownGlobals.GlobalDialogColor, geom_scale = modelScale, frameSize = (-1, 1, -1, 1), pos = modelPos, text = TTLocalizer.PetshopAdoptConfirm % (name, cost), text_wordwrap = 12, text_scale = 0.050000000000000003, text_pos = (0, 0.55000000000000004), text_fg = text0Color)
            self.initialiseoptions(PetshopGUI.AdoptPetDlg)
            self.petView = self.attachNewNode('petView')
            self.petView.setPos(-0.13, 0, 0.80000000000000004)
            self.petModel = Pet.Pet(forGui = 1)
            self.petModel.setDNA(dna)
            self.petModel.fitAndCenterHead(0.39500000000000002, forGui = 1)
            self.petModel.reparentTo(self.petView)
            self.petModel.setH(130)
            self.petModel.enterNeutralHappy()
            self.moneyDisplay = DirectLabel(parent = self, relief = None, text = str(base.localAvatar.getTotalMoney()), text_scale = 0.074999999999999997, text_fg = (0.94999999999999996, 0.94999999999999996, 0, 1), text_shadow = (0, 0, 0, 1), text_pos = (0.22500000000000001, 0.33000000000000002), text_font = ToontownGlobals.getSignFont())
            self.accept(localAvatar.uniqueName('moneyChange'), self._AdoptPetDlg__moneyChange)
            self.accept(localAvatar.uniqueName('bankMoneyChange'), self._AdoptPetDlg__moneyChange)
            okImageList = (model.find('**/CheckButtonUp'), model.find('**/CheckButtonDown'), model.find('**/CheckButtonRollover'))
            cancelImageList = (model.find('**/CancelButtonUp'), model.find('**/CancelButtonDown'), model.find('**/CancelRollover'))
            cancelIcon = model.find('**/CancelIcon')
            checkIcon = model.find('**/CheckIcon')
            self.cancelButton = DirectButton(parent = self, relief = None, image = cancelImageList, geom = cancelIcon, scale = modelScale, text = ('', TTLocalizer.PetshopGoBack), text_pos = (-5.7999999999999998, 4.4000000000000004), text_scale = 0.69999999999999996, pressEffect = False, command = lambda : messenger.send(doneEvent, [
0]))
            self.okButton = DirectButton(parent = self, relief = None, image = okImageList, geom = checkIcon, scale = modelScale, text = ('', TTLocalizer.PetshopAdopt), text_pos = (5.7999999999999998, 4.4000000000000004), text_scale = 0.69999999999999996, pressEffect = False, command = lambda : messenger.send(doneEvent, [
1]))
            model.removeNode()

        
        def destroy(self):
            self.ignore(localAvatar.uniqueName('moneyChange'))
            self.ignore(localAvatar.uniqueName('bankMoneyChange'))
            self.petModel.delete()
            DirectFrame.destroy(self)

        
        def _AdoptPetDlg__moneyChange(self, money):
            self.moneyDisplay['text'] = str(base.localAvatar.getTotalMoney())


    
    class ReturnPetDlg(DirectFrame):
        notify = DirectNotifyGlobal.directNotify.newCategory('PetshopGUI.ReturnPetDlg')
        
        def __init__(self, doneEvent):
            
            def showDialog(avatar):
                model = loader.loadModelOnce('phase_4/models/gui/ReturnPet')
                modelPos = (0, 0, -0.29999999999999999)
                modelScale = (0.055, 0.055, 0.055)
                base.r = self
                DirectFrame.__init__(self, relief = None, state = 'normal', geom = model, geom_scale = modelScale, frameSize = (-1, 1, -1, 1), pos = modelPos, text = TTLocalizer.PetshopReturnConfirm % avatar.getName(), text_wordwrap = 12, text_scale = 0.070000000000000007, text_pos = (0, 0.45000000000000001), text_fg = text2Color)
                self.initialiseoptions(PetshopGUI.ReturnPetDlg)
                okImageList = (model.find('**/CheckButtonUp'), model.find('**/CheckButtonDown'), model.find('**/CheckRollover'))
                cancelImageList = (model.find('**/CancelButtonUp'), model.find('**/CancelButtonDown'), model.find('**/CancelRollover'))
                cancelIcon = model.find('**/CancelIcon')
                checkIcon = model.find('**/CheckIcon')
                self.cancelButton = DirectButton(parent = self, relief = None, image = cancelImageList, geom = cancelIcon, scale = modelScale, text = ('', TTLocalizer.PetshopGoBack), text_pos = (-5.7999999999999998, 4.4000000000000004), text_scale = 0.69999999999999996, pressEffect = False, command = lambda : messenger.send(doneEvent, [
0]))
                self.okButton = DirectButton(parent = self, relief = None, image = okImageList, geom = checkIcon, scale = modelScale, text = ('', TTLocalizer.PetshopReturn), text_pos = (5.7999999999999998, 4.4000000000000004), text_scale = 0.69999999999999996, pressEffect = False, command = lambda : messenger.send(doneEvent, [
1]))
                self.petView = self.attachNewNode('petView')
                self.petView.setPos(-0.14999999999999999, 0, 0.80000000000000004)
                self.petModel = Pet.Pet(forGui = 1)
                self.petModel.setDNA(avatar.getDNA())
                self.petModel.fitAndCenterHead(0.39500000000000002, forGui = 1)
                self.petModel.reparentTo(self.petView)
                self.petModel.setH(130)
                self.petModel.enterNeutralSad()
                model.removeNode()
                self.initialized = True

            self.initialized = False
            PetDetail.PetDetail(base.localAvatar.getPetId(), showDialog)

        
        def destroy(self):
            if self.initialized:
                self.petModel.delete()
                DirectFrame.destroy(self)
            


    
    class ChoosePetDlg(DirectFrame):
        notify = DirectNotifyGlobal.directNotify.newCategory('PetshopGUI.ChoosePetDlg')
        
        def __init__(self, doneEvent, petSeeds):
            model = loader.loadModelOnce('phase_4/models/gui/PetShopInterface')
            modelPos = (0, 0, -0.90000000000000002)
            modelScale = (0.185, 0.185, 0.185)
            DirectFrame.__init__(self, relief = None, state = 'normal', geom = model, geom_scale = modelScale, frameSize = (-1, 1, -1, 1), pos = modelPos, text = TTLocalizer.PetshopChooserTitle, text_wordwrap = 26, text_scale = 0.10000000000000001, text_fg = Vec4(0.35999999999999999, 0.93999999999999995, 0.93000000000000005, 1), text_pos = (0, 1.5800000000000001))
            self.initialiseoptions(PetshopGUI.ChoosePetDlg)
            adoptImageList = (model.find('**/AdoptButtonUp'), model.find('**/AdoptButtonDown'), model.find('**/AdoptButtonRollover'), model.find('**/AdoptButtonRollover'))
            cancelImageList = (model.find('**/CancelButtonUp'), model.find('**/CancelButtonDown'), model.find('**/CancelButtonRollover'))
            cancelIcon = model.find('**/CancelIcon')
            pawLImageList = (model.find('**/Paw1Up'), model.find('**/Paw1Down'), model.find('**/Paw1Rollover'))
            pawLArrowImageList = model.find('**/Arrow1')
            pawRImageList = (model.find('**/Paw2Up'), model.find('**/Paw2Down'), model.find('**/Paw2Rollover'))
            pawRArrowImageList = model.find('**/Arrow2')
            self.cancelButton = DirectButton(parent = self, relief = None, image = cancelImageList, geom = cancelIcon, scale = modelScale, pressEffect = False, command = lambda : messenger.send(doneEvent, [
-1]))
            self.pawLButton = DirectButton(parent = self, relief = None, image = pawLImageList, geom = pawLArrowImageList, scale = modelScale, pressEffect = False, command = lambda : self._ChoosePetDlg__handlePetChange(-1))
            self.pawRButton = DirectButton(parent = self, relief = None, image = pawRImageList, geom = pawRArrowImageList, scale = modelScale, pressEffect = False, command = lambda : self._ChoosePetDlg__handlePetChange(1))
            self.okButton = DirectButton(parent = self, relief = None, image = adoptImageList, image3_color = disabledImageColor, scale = modelScale, text = TTLocalizer.PetshopAdopt, text_scale = 0.59999999999999998, text_pos = (-0.20999999999999999, 1.05), text0_fg = text0Color, text1_fg = text1Color, text2_fg = text2Color, text3_fg = text3Color, pressEffect = False, command = lambda : messenger.send(doneEvent, [
self.curPet]))
            self.moneyDisplay = DirectLabel(parent = self, relief = None, text = str(base.localAvatar.getTotalMoney()), text_scale = 0.10000000000000001, text_fg = (0.94999999999999996, 0.94999999999999996, 0, 1), text_shadow = (0, 0, 0, 1), text_pos = (0.34000000000000002, 0.12), text_font = ToontownGlobals.getSignFont())
            self.accept(localAvatar.uniqueName('moneyChange'), self._ChoosePetDlg__moneyChange)
            self.accept(localAvatar.uniqueName('bankMoneyChange'), self._ChoosePetDlg__moneyChange)
            self.petView = self.attachNewNode('petView')
            self.petView.setPos(-0.050000000000000003, 0, 1.1499999999999999)
            model.removeNode()
            self.petSeeds = petSeeds
            self.makePetList()
            self.showPet()

        
        def makePetList(self):
            self.numPets = len(self.petSeeds)
            self.curPet = 0
            self.petDNA = []
            self.petName = []
            self.petDesc = []
            self.petCost = []
            for i in range(self.numPets):
                random.seed(self.petSeeds[i])
                zoneId = ZoneUtil.getCanonicalSafeZoneId(base.localAvatar.getZoneId())
                (name, dna, traitSeed) = PetUtil.getPetInfoFromSeed(self.petSeeds[i], zoneId)
                cost = PetUtil.getPetCostFromSeed(self.petSeeds[i], zoneId)
                traits = PetTraits.PetTraits(traitSeed, zoneId)
                traitList = traits.getExtremeTraitDescriptions()
                numGenders = len(PetDNA.PetGenders)
                gender = i % numGenders
                PetDNA.setGender(dna, gender)
                self.petDNA.append(dna)
                self.petName.append(TTLocalizer.PetshopUnknownName)
                descList = []
                descList.append(TTLocalizer.PetshopDescGender % PetDNA.getGenderString(gender = gender))
                if traitList:
                    descList.append(TTLocalizer.PetshopDescTrait % traitList[0])
                else:
                    descList.append(TTLocalizer.PetshopDescTrait % TTLocalizer.PetshopDescStandard)
                traitList.extend([
                    '',
                    '',
                    '',
                    ''])
                for trait in traitList[1:4]:
                    descList.append('\t%s' % trait)
                
                descList.append(TTLocalizer.PetshopDescCost % cost)
                self.petDesc.append(string.join(descList, '\n'))
                self.petCost.append(cost)
            

        
        def destroy(self):
            self.ignore(localAvatar.uniqueName('moneyChange'))
            self.ignore(localAvatar.uniqueName('bankMoneyChange'))
            self.petModel.delete()
            DirectFrame.destroy(self)

        
        def _ChoosePetDlg__handlePetChange(self, nDir):
            self.curPet = (self.curPet + nDir) % self.numPets
            self.nameLabel.destroy()
            self.petModel.delete()
            self.descLabel.destroy()
            self.showPet()
            return None

        
        def showPet(self):
            self.nameLabel = DirectLabel(parent = self, pos = (0, 0, 1.3500000000000001), relief = None, text = self.petName[self.curPet], text_fg = Vec4(0.45000000000000001, 0, 0.60999999999999999, 1), text_pos = (0, 0), text_scale = 0.080000000000000002, text_shadow = (1, 1, 1, 1))
            self.petModel = Pet.Pet(forGui = 1)
            self.petModel.setDNA(self.petDNA[self.curPet])
            self.petModel.fitAndCenterHead(0.56999999999999995, forGui = 1)
            self.petModel.reparentTo(self.petView)
            self.petModel.setH(130)
            self.petModel.enterNeutralHappy()
            self.descLabel = DirectLabel(parent = self, pos = (-0.40000000000000002, 0, 0.71999999999999997), relief = None, scale = 0.050000000000000003, text = self.petDesc[self.curPet], text_align = TextNode.ALeft, text_wordwrap = 14, text_scale = 0.90000000000000002)
            if self.petCost[self.curPet] > base.localAvatar.getTotalMoney():
                self.okButton['state'] = DISABLED
            else:
                self.okButton['state'] = NORMAL

        
        def _ChoosePetDlg__moneyChange(self, money):
            self.moneyDisplay['text'] = str(base.localAvatar.getTotalMoney())


    
    def __init__(self, eventDict, petSeeds):
        self.eventDict = eventDict
        self.mainMenuDoneEvent = 'MainMenuGuiDone'
        self.adoptPetDoneEvent = 'AdoptPetGuiDone'
        self.returnPetDoneEvent = 'ReturnPetGuiDone'
        self.petChooserDoneEvent = 'PetChooserGuiDone'
        self.fishGuiDoneEvent = 'MyFishGuiDone'
        self.namePickerDoneEvent = 'NamePickerGuiDone'
        self.goHomeDlgDoneEvent = 'GoHomeDlgDone'
        self.dialog = None
        self.dialogStack = []
        self.petSeeds = petSeeds
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.reparentTo(aspect2d)
        self.timer.posInTopRightCorner()
        self.timer.countdown(PetConstants.PETCLERK_TIMER, self._PetshopGUI__timerExpired)
        self.doDialog(Dialog_MainMenu)

    
    def _PetshopGUI__timerExpired(self):
        messenger.send(self.eventDict['guiDone'], [
            True])

    
    def destroy(self):
        self.destroyDialog()
        self.timer.destroy()
        del self.timer
        self.ignore(self.mainMenuDoneEvent)
        self.ignore(self.adoptPetDoneEvent)
        self.ignore(self.returnPetDoneEvent)
        self.ignore(self.petChooserDoneEvent)
        self.ignore(self.fishGuiDoneEvent)
        self.ignore(self.namePickerDoneEvent)
        self.ignore(self.goHomeDlgDoneEvent)

    
    def destroyDialog(self):
        if self.dialog != None:
            self.dialog.destroy()
            self.dialog = None
        

    
    def popDialog(self):
        self.dialogStack.pop()
        self.doDialog(self.dialogStack.pop())

    
    def doDialog(self, nDialog):
        self.destroyDialog()
        self.dialogStack.append(nDialog)
        if nDialog == Dialog_MainMenu:
            self.acceptOnce(self.mainMenuDoneEvent, self._PetshopGUI__handleMainMenuDlg)
            self.dialog = self.MainMenuDlg(self.mainMenuDoneEvent)
        elif nDialog == Dialog_AdoptPet:
            self.acceptOnce(self.adoptPetDoneEvent, self._PetshopGUI__handleAdoptPetDlg)
            self.dialog = self.AdoptPetDlg(self.adoptPetDoneEvent, self.petSeeds[self.adoptPetNum], self.adoptPetNameIndex)
        elif nDialog == Dialog_ChoosePet:
            self.acceptOnce(self.petChooserDoneEvent, self._PetshopGUI__handleChoosePetDlg)
            self.dialog = self.ChoosePetDlg(self.petChooserDoneEvent, self.petSeeds)
        elif nDialog == Dialog_ReturnPet:
            self.acceptOnce(self.returnPetDoneEvent, self._PetshopGUI__handleReturnPetDlg)
            self.dialog = self.ReturnPetDlg(self.returnPetDoneEvent)
        elif nDialog == Dialog_SellFish:
            self.acceptOnce(self.fishGuiDoneEvent, self._PetshopGUI__handleFishSellDlg)
            self.dialog = FishSellGUI.FishSellGUI(self.fishGuiDoneEvent)
        elif nDialog == Dialog_NamePicker:
            self.acceptOnce(self.namePickerDoneEvent, self._PetshopGUI__handleNamePickerDlg)
            self.dialog = self.NamePicker(self.namePickerDoneEvent, self.petSeeds[self.adoptPetNum], gender = self.adoptPetNum % 2)
        elif nDialog == Dialog_GoHome:
            self.acceptOnce(self.goHomeDlgDoneEvent, self._PetshopGUI__handleGoHomeDlg)
            self.dialog = self.GoHomeDlg(self.goHomeDlgDoneEvent)
        

    
    def _PetshopGUI__handleMainMenuDlg(self, exitVal):
        print 'Exiting Main Menu'
        if exitVal == 0:
            messenger.send(self.eventDict['guiDone'])
        elif exitVal == 1:
            self.doDialog(Dialog_SellFish)
        elif exitVal == 2:
            self.doDialog(Dialog_ChoosePet)
        elif exitVal == 3:
            self.doDialog(Dialog_ReturnPet)
        

    
    def _PetshopGUI__handleFishSellDlg(self, exitVal):
        if exitVal == 0:
            self.popDialog()
        elif exitVal == 1:
            self.destroyDialog()
            messenger.send(self.eventDict['fishSold'])
        

    
    def _PetshopGUI__handleChoosePetDlg(self, exitVal):
        if exitVal == -1:
            self.popDialog()
        else:
            self.adoptPetNum = exitVal
            self.doDialog(Dialog_NamePicker)

    
    def _PetshopGUI__handleNamePickerDlg(self, exitVal):
        if exitVal == -1:
            self.popDialog()
        else:
            self.adoptPetNameIndex = exitVal
            if base.localAvatar.hasPet():
                self.doDialog(Dialog_ReturnPet)
            else:
                self.doDialog(Dialog_AdoptPet)

    
    def _PetshopGUI__handleAdoptPetDlg(self, exitVal):
        if exitVal == 0:
            self.popDialog()
        elif exitVal == 1:
            self.destroyDialog()
            messenger.send(self.eventDict['petAdopted'], [
                self.adoptPetNum,
                self.adoptPetNameIndex])
            messenger.send(self.eventDict['guiDone'])
        

    
    def _PetshopGUI__handleGoHomeDlg(self, exitVal):
        if exitVal == 0:
            messenger.send(self.eventDict['guiDone'])
        elif exitVal == 1:
            messenger.send(self.eventDict['guiDone'])
            place = base.cr.playGame.getPlace()
            if place == None:
                self.notify.warning('Tried to go home, but place is None.')
                return None
            
            place.goHomeNow(base.localAvatar.lastHood)
        

    
    def _PetshopGUI__handleReturnPetDlg(self, exitVal):
        print 'Exiting Return Pet'
        if exitVal == 0:
            self.popDialog()
        elif exitVal == 1:
            if self.dialogStack[len(self.dialogStack) - 2] == Dialog_NamePicker:
                self.doDialog(Dialog_AdoptPet)
            else:
                self.destroyDialog()
                messenger.send(self.eventDict['petReturned'])
                messenger.send(self.eventDict['guiDone'])
        


