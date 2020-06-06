# File: O (Python 2.2)

from pandac.PandaModules import *
import OTPLocalizer
QuietZone = 1
UberZone = 2
WallBitmask = BitMask32(1)
FloorBitmask = BitMask32(2)
CameraBitmask = BitMask32(4)
PieBitmask = BitMask32(256)
SafetyNetBitmask = BitMask32(512)
SafetyGateBitmask = BitMask32(1024)
GhostBitmask = BitMask32(2048)
OriginalCameraFov = 52.0
DefaultCameraFov = 52.0
DefaultCameraFar = 400.0
DefaultCameraNear = 1.0
AICollisionPriority = 10
AICollMovePriority = 8
MaxFriends = 50
MaxBackCatalog = 48
FriendChat = 1
CommonChat = 1
SuperChat = 2
MaxCustomMessages = 15
SPHidden = 0
SPRender = 1
SPDynamic = 4
CENormal = 0
CEBigHead = 1
CESmallHead = 2
CEBigLegs = 3
CESmallLegs = 4
CEBigToon = 5
CESmallToon = 6
CEFlatPortrait = 7
CEFlatProfile = 8
CETransparent = 9
CENoColor = 10
CEInvisible = 11
CEGhost = 'g'
BigToonScale = 1.5
SmallToonScale = 0.5
DisconnectUnknown = 0
DisconnectBookExit = 1
DisconnectCloseWindow = 2
DisconnectPythonError = 3
DisconnectSwitchShards = 4
DisconnectGraphicsError = 5
DatabaseDialogTimeout = 20.0
DatabaseGiveupTimeout = 45.0
PeriodTimerWarningTime = (600, 300, 60)
WalkCutOff = 0.5
RunCutOff = 8.0
FloorOffset = 0.025000000000000001
AvatarDefaultRadius = 1
InterfaceFont = None
InterfaceFontPath = None
SignFont = None
SignFontPath = None
DialogClass = None
GlobalDialogClass = None

def getInterfaceFont():
    global InterfaceFont
    if InterfaceFont == None:
        if InterfaceFontPath == None:
            InterfaceFont = TextNode.getDefaultFont()
        else:
            InterfaceFont = loader.loadFont(InterfaceFontPath, lineHeight = 1.0)
    
    return InterfaceFont


def setInterfaceFont(path):
    global InterfaceFontPath, InterfaceFont
    InterfaceFontPath = path
    InterfaceFont = None


def getSignFont():
    global SignFont
    if SignFont == None:
        if SignFontPath == None:
            SignFont = TextNode.getDefaultFont()
        else:
            SignFont = loader.loadFont(SignFontPath, lineHeight = 1.0)
    
    return SignFont


def setSignFont(path):
    global SignFontPath
    SignFontPath = path


def getDialogClass():
    global DialogClass
    if DialogClass == None:
        OTPDialog = OTPDialog
        import otp.otpgui.OTPDialog
        DialogClass = OTPDialog
    
    return DialogClass


def getGlobalDialogClass():
    global GlobalDialogClass
    if DialogClass == None:
        GlobalDialog = GlobalDialog
        import otp.otpgui.OTPDialog
        GlobalDialogClass = GlobalDialog
    
    return GlobalDialogClass


def setDialogClasses(dialogClass, globalDialogClass):
    global DialogClass, GlobalDialogClass
    DialogClass = dialogClass
    GlobalDialogClass = globalDialogClass

NetworkLatency = 1.0
maxLoginWidth = 9.0999999999999996
STAND_INDEX = 0
WALK_INDEX = 1
RUN_INDEX = 2
REVERSE_INDEX = 3
STRAFE_LEFT_INDEX = 4
STRAFE_RIGHT_INDEX = 5
ToonStandableGround = 0.70699999999999996
ToonForwardSpeed = 16.0
ToonJumpForce = 24.0
ToonReverseSpeed = 8.0
ToonRotateSpeed = 80.0
ToonForwardSlowSpeed = 6.0
ToonJumpSlowForce = 4.0
ToonReverseSlowSpeed = 2.5
ToonRotateSlowSpeed = 33.0
MickeySpeed = 5.0
MinnieSpeed = 3.2000000000000002
DonaldSpeed = 3.6800000000000002
GoofySpeed = 5.2000000000000002
PlutoSpeed = 5.5
ThinkPosHotkey = 'f1-up'
PlaceMarkerHotkey = 'f2-up'
FriendsListHotkey = 'f7-up'
StickerBookHotkey = 'f8-up'
OptionsPageHotkey = 'escape-up'
ScreenshotHotkey = 'f9-up'
SynchronizeHotkey = 'f6-up'
QuestsHotkeyOn = 'end'
QuestsHotkeyOff = 'end-up'
InventoryHotkeyOn = 'home'
InventoryHotkeyOff = 'home-up'
PrintCamPosHotkey = 'f12-up'
GlobalDialogColor = (1, 1, 0.75, 1)
DefaultBackgroundColor = (0.29999999999999999, 0.29999999999999999, 0.29999999999999999, 1)
toonBodyScales = {
    'mouse': 0.59999999999999998,
    'cat': 0.72999999999999998,
    'duck': 0.66000000000000003,
    'rabbit': 0.73999999999999999,
    'horse': 0.84999999999999998,
    'dog': 0.84999999999999998,
    'monkey': 0.68000000000000005 }
toonHeadScales = {
    'mouse': Point3(1.0),
    'cat': Point3(1.0),
    'duck': Point3(1.0),
    'rabbit': Point3(1.0),
    'horse': Point3(1.0),
    'dog': Point3(1.0),
    'monkey': Point3(1.0) }
legHeightDict = {
    's': 1.5,
    'm': 2.0,
    'l': 2.75 }
torsoHeightDict = {
    's': 1.5,
    'm': 1.75,
    'l': 2.25,
    'ss': 1.5,
    'ms': 1.75,
    'ls': 2.25,
    'sd': 1.5,
    'md': 1.75,
    'ld': 2.25 }
headHeightDict = {
    'dls': 0.75,
    'dss': 0.5,
    'dsl': 0.5,
    'dll': 0.75,
    'cls': 0.75,
    'css': 0.5,
    'csl': 0.5,
    'cll': 0.75,
    'hls': 0.75,
    'hss': 0.5,
    'hsl': 0.5,
    'hll': 0.75,
    'mls': 0.75,
    'mss': 0.5,
    'rls': 0.75,
    'rss': 0.5,
    'rsl': 0.5,
    'rll': 0.75,
    'fls': 0.75,
    'fss': 0.5,
    'fsl': 0.5,
    'fll': 0.75,
    'pls': 0.75,
    'pss': 0.5,
    'psl': 0.5,
    'pll': 0.75 }
RandomButton = 'Randomize'
TypeANameButton = 'Type Name'
PickANameButton = 'Pick-A-Name'
NameShopSubmitButton = 'Submit'
RejectNameText = 'That name is not allowed. Please try again.'
WaitingForNameSubmission = 'Submitting your name...'
NameShopNameMaster = 'NameMasterEnglish.txt'
NameShopPay = 'Subscribe Now!'
NameShopPlay = 'Free Trial'
NameShopOnlyPaid = 'Only paid users\nmay name their Toons.\nUntil you subscribe\nyour name will be\n'
NameShopContinueSubmission = 'Continue Submission'
NameShopChooseAnother = 'Choose Another Name'
NameShopToonCouncil = 'The Toon Council\nwill review your\nname.  ' + 'Review may\ntake a few days.\nWhile you wait\nyour name will be\n '
PleaseTypeName = 'Please type your name:'
AllNewNames = 'All new names\nmust be approved\nby the Toon Council.'
NameShopNameRejected = 'The name you\nsubmitted has\nbeen rejected.'
NameShopNameAccepted = 'Congratulations!\nThe name you\nsubmitted has\nbeen accepted!'
NoPunctuation = "You can't use punctuation marks in your name!"
PeriodOnlyAfterLetter = 'You can use a period in your name, but only after a letter.'
ApostropheOnlyAfterLetter = 'You can use an apostrophe in your name, but only after a letter.'
NoNumbersInTheMiddle = 'Numeric digits may not appear in the middle of a word.'
ThreeWordsOrLess = 'Your name must be three words or fewer.'
CopyrightedNames = ('mickey', 'mickey mouse', 'mickeymouse', 'minnie', 'minnie mouse', 'minniemouse', 'donald', 'donald duck', 'donaldduck', 'pluto', 'goofy')
