# File: T (Python 2.2)

import TTLocalizer
from otp.otpbase.OTPGlobals import *
from direct.showbase.PythonUtil import Enum, invertDict
CogHQCameraFov = 60.0
BossBattleCameraFov = 72.0
MakeAToonCameraFov = 35.0
PetBitmask = BitMask32(8)
CatchGameBitmask = BitMask32(16)
CashbotBossObjectBitmask = BitMask32(16)
FurnitureSideBitmask = BitMask32(32)
FurnitureTopBitmask = BitMask32(64)
FurnitureDragBitmask = BitMask32(128)
PetLookatPetBitmask = BitMask32(256)
PetLookatNonPetBitmask = BitMask32(512)
FullPies = 65535
CogHQCameraFar = 900.0
CogHQCameraNear = 1.0
CashbotHQCameraFar = 2000.0
CashbotHQCameraNear = 1.0
MaxMailboxContents = 20
MaxHouseItems = 30
ExtraDeletedItems = 5
DeletedItemLifetime = 7 * 24 * 60
CatalogNumWeeksPerSeries = 13
CatalogNumWeeks = 78
PetFloorCollPriority = 5
PetPanelProximityPriority = 6
P_OnOrderListFull = -11
P_MailboxFull = -10
P_NoPurchaseMethod = -9
P_ReachedPurchaseLimit = -8
P_NoRoomForItem = -7
P_NotShopping = -6
P_NotAtMailbox = -5
P_NotInCatalog = -4
P_NotEnoughMoney = -3
P_InvalidIndex = -2
P_UserCancelled = -1
P_ItemAvailable = 1
P_ItemOnOrder = 2
P_ItemUnneeded = 3
FM_InvalidItem = -7
FM_NondeletableItem = -6
FM_InvalidIndex = -5
FM_NotOwner = -4
FM_NotDirector = -3
FM_RoomFull = -2
FM_HouseFull = -1
FM_MovedItem = 1
FM_SwappedItem = 2
FM_DeletedItem = 3
FM_RecoveredItem = 4
SPDonaldsBoat = 2
SPMinniesPiano = 3
MaxHpLimit = 117
MaxCarryLimit = 80
MaxQuestCarryLimit = 4
MaxCogSuitLevel = 50 - 1
CogSuitHPLevels = (15 - 1, 20 - 1, 30 - 1, 40 - 1, 50 - 1)
setInterfaceFont(TTLocalizer.InterfaceFont)
setSignFont(TTLocalizer.SignFont)
from toontown.toontowngui import TTDialog
setDialogClasses(TTDialog.TTDialog, TTDialog.TTGlobalDialog)
ToonFont = None
BuildingNametagFont = None
MinnieFont = None
SuitFont = None

def getToonFont():
    global ToonFont
    if ToonFont == None:
        ToonFont = loader.loadFont(TTLocalizer.ToonFont, lineHeight = 1.0)
    
    return ToonFont


def getBuildingNametagFont():
    global BuildingNametagFont
    if BuildingNametagFont == None:
        BuildingNametagFont = loader.loadFont(TTLocalizer.BuildingNametagFont)
    
    return BuildingNametagFont


def getMinnieFont():
    global MinnieFont
    if MinnieFont == None:
        MinnieFont = loader.loadFont(TTLocalizer.MinnieFont)
    
    return MinnieFont


def getSuitFont():
    global SuitFont
    if SuitFont == None:
        SuitFont = loader.loadFont(TTLocalizer.SuitFont, pixelsPerUnit = 40, spaceAdvance = 0.25, lineHeight = 1.0)
    
    return SuitFont

DonaldsDock = 1000
ToontownCentral = 2000
TheBrrrgh = 3000
MinniesMelodyland = 4000
DaisyGardens = 5000
ConstructionZone = 6000
FunnyFarm = 7000
GoofyStadium = 8000
DonaldsDreamland = 9000
BarnacleBoulevard = 1100
SeaweedStreet = 1200
LighthouseLane = 1300
SillyStreet = 2100
LoopyLane = 2200
PunchlinePlace = 2300
WalrusWay = 3100
SleetStreet = 3200
AltoAvenue = 4100
BaritoneBoulevard = 4200
TenorTerrace = 4300
ElmStreet = 5100
MapleStreet = 5200
OakStreet = 5300
LullabyLane = 9100
PajamaPlace = 9200
HoodHierarchy = {
    ToontownCentral: (SillyStreet, LoopyLane, PunchlinePlace),
    DonaldsDock: (BarnacleBoulevard, SeaweedStreet, LighthouseLane),
    TheBrrrgh: (WalrusWay, SleetStreet),
    MinniesMelodyland: (AltoAvenue, BaritoneBoulevard, TenorTerrace),
    DaisyGardens: (ElmStreet, MapleStreet, OakStreet),
    DonaldsDreamland: (LullabyLane, PajamaPlace) }
WelcomeValleyToken = 0
BossbotHQ = 10000
BossbotLobby = 10100
SellbotHQ = 11000
SellbotLobby = 11100
SellbotFactoryExt = 11200
SellbotFactoryInt = 11500
CashbotHQ = 12000
CashbotLobby = 12100
CashbotMintIntA = 12500
CashbotMintIntB = 12600
CashbotMintIntC = 12700
LawbotHQ = 13000
LawbotLobby = 13100
Tutorial = 15000
MyEstate = 16000
WelcomeValleyBegin = 20000
WelcomeValleyEnd = 61000
DynamicZonesBegin = 61000
DynamicZonesEnd = 1 << 20
cogDept2index = {
    'c': 0,
    'l': 1,
    'm': 2,
    's': 3 }
cogIndex2dept = invertDict(cogDept2index)
HQToSafezone = {
    SellbotHQ: DaisyGardens,
    CashbotHQ: DonaldsDreamland,
    LawbotHQ: DonaldsDock,
    BossbotHQ: TheBrrrgh }
CogDeptNames = [
    TTLocalizer.Bossbot,
    TTLocalizer.Lawbot,
    TTLocalizer.Cashbot,
    TTLocalizer.Sellbot]

def cogHQZoneId2deptIndex(zone):
    if zone >= 13000 and zone <= 13999:
        return 1
    elif zone >= 12000:
        return 2
    elif zone >= 11000:
        return 3
    else:
        return 0


def cogHQZoneId2dept(zone):
    return cogIndex2dept[cogHQZoneId2deptIndex(zone)]


def dept2cogHQ(dept):
    dept2hq = {
        'c': BossbotHQ,
        'l': LawbotHQ,
        'm': CashbotHQ,
        's': SellbotHQ }
    return dept2hq[dept]

MockupFactoryId = 0
MintNumFloors = {
    CashbotMintIntA: 20,
    CashbotMintIntB: 20,
    CashbotMintIntC: 20 }
CashbotMintCogLevel = 10
CashbotMintSkelecogLevel = 11
CashbotMintBossLevel = 12
MintNumBattles = {
    CashbotMintIntA: 4,
    CashbotMintIntB: 6,
    CashbotMintIntC: 8 }
MintCogBuckRewards = {
    CashbotMintIntA: 8,
    CashbotMintIntB: 14,
    CashbotMintIntC: 20 }
MintNumRooms = {
    CashbotMintIntA: 2 * (6,) + 5 * (7,) + 5 * (8,) + 5 * (9,) + 3 * (10,),
    CashbotMintIntB: 3 * (8,) + 6 * (9,) + 6 * (10,) + 5 * (11,),
    CashbotMintIntC: 4 * (10,) + 10 * (11,) + 6 * (12,) }
FT_FullSuit = 'fullSuit'
FT_Leg = 'leg'
FT_Arm = 'arm'
FT_Torso = 'torso'
factoryId2factoryType = {
    MockupFactoryId: FT_FullSuit,
    SellbotFactoryInt: FT_FullSuit }
StreetNames = TTLocalizer.GlobalStreetNames
StreetBranchZones = StreetNames.keys()
Hoods = (DonaldsDock, ToontownCentral, TheBrrrgh, MinniesMelodyland, DaisyGardens, ConstructionZone, FunnyFarm, GoofyStadium, DonaldsDreamland, BossbotHQ, SellbotHQ, CashbotHQ, LawbotHQ)
NoPreviousGameId = 0
RaceGameId = 1
CannonGameId = 2
TagGameId = 3
PatternGameId = 4
RingGameId = 5
MazeGameId = 6
TugOfWarGameId = 7
CatchGameId = 8
MinigameNames = {
    'race': RaceGameId,
    'cannon': CannonGameId,
    'tag': TagGameId,
    'pattern': PatternGameId,
    'minnie': PatternGameId,
    'match': PatternGameId,
    'matching': PatternGameId,
    'ring': RingGameId,
    'maze': MazeGameId,
    'tug': TugOfWarGameId,
    'catch': CatchGameId }
MinigameTemplateId = -1
MinigameIDs = (RaceGameId, CannonGameId, TagGameId, PatternGameId, RingGameId, MazeGameId, TugOfWarGameId, CatchGameId)
MinigamePlayerMatrix = {
    1: (CannonGameId, RingGameId, MazeGameId, TugOfWarGameId, CatchGameId),
    2: (CannonGameId, PatternGameId, RingGameId, TagGameId, MazeGameId, TugOfWarGameId, CatchGameId),
    3: (CannonGameId, PatternGameId, RingGameId, TagGameId, RaceGameId, MazeGameId, TugOfWarGameId, CatchGameId),
    4: (CannonGameId, PatternGameId, RingGameId, TagGameId, RaceGameId, MazeGameId, TugOfWarGameId, CatchGameId) }
phaseMap = {
    Tutorial: 4,
    ToontownCentral: 4,
    MyEstate: 5.5,
    DonaldsDock: 6,
    MinniesMelodyland: 6,
    GoofyStadium: 6,
    TheBrrrgh: 8,
    DaisyGardens: 8,
    FunnyFarm: 8,
    DonaldsDreamland: 8,
    ConstructionZone: 8,
    BossbotHQ: 9,
    SellbotHQ: 9,
    CashbotHQ: 10,
    LawbotHQ: 9 }
streetPhaseMap = {
    ToontownCentral: 5,
    DonaldsDock: 6,
    MinniesMelodyland: 6,
    GoofyStadium: 6,
    TheBrrrgh: 8,
    DaisyGardens: 8,
    FunnyFarm: 8,
    DonaldsDreamland: 8,
    ConstructionZone: 8,
    BossbotHQ: 9,
    SellbotHQ: 9,
    CashbotHQ: 10,
    LawbotHQ: 9 }
dnaMap = {
    Tutorial: 'toontown_central',
    ToontownCentral: 'toontown_central',
    DonaldsDock: 'donalds_dock',
    MinniesMelodyland: 'minnies_melody_land',
    GoofyStadium: 'not done yet',
    TheBrrrgh: 'the_burrrgh',
    DaisyGardens: 'daisys_garden',
    FunnyFarm: 'not done yet',
    DonaldsDreamland: 'donalds_dreamland',
    ConstructionZone: 'not done yet',
    BossbotHQ: 'cog_hq_bossbot',
    SellbotHQ: 'cog_hq_sellbot',
    CashbotHQ: 'cog_hq_cashbot',
    LawbotHQ: 'cog_hq_lawbot' }
hoodNameMap = {
    DonaldsDock: TTLocalizer.DonaldsDock,
    ToontownCentral: TTLocalizer.ToontownCentral,
    TheBrrrgh: TTLocalizer.TheBrrrgh,
    MinniesMelodyland: TTLocalizer.MinniesMelodyland,
    DaisyGardens: TTLocalizer.DaisyGardens,
    ConstructionZone: TTLocalizer.ConstructionZone,
    FunnyFarm: TTLocalizer.FunnyFarm,
    GoofyStadium: TTLocalizer.GoofyStadium,
    DonaldsDreamland: TTLocalizer.DonaldsDreamland,
    BossbotHQ: TTLocalizer.BossbotHQ,
    SellbotHQ: TTLocalizer.SellbotHQ,
    CashbotHQ: TTLocalizer.CashbotHQ,
    LawbotHQ: TTLocalizer.LawbotHQ,
    Tutorial: TTLocalizer.Tutorial,
    MyEstate: TTLocalizer.MyEstate }
safeZoneCountMap = {
    MyEstate: 8,
    Tutorial: 6,
    ToontownCentral: 6,
    DonaldsDock: 10,
    MinniesMelodyland: 5,
    GoofyStadium: 500,
    TheBrrrgh: 8,
    DaisyGardens: 9,
    FunnyFarm: 500,
    DonaldsDreamland: 5,
    ConstructionZone: 500 }
townCountMap = {
    MyEstate: 8,
    Tutorial: 40,
    ToontownCentral: 37,
    DonaldsDock: 40,
    MinniesMelodyland: 40,
    GoofyStadium: 40,
    TheBrrrgh: 40,
    DaisyGardens: 40,
    FunnyFarm: 40,
    DonaldsDreamland: 40,
    ConstructionZone: 40 }
hoodCountMap = {
    MyEstate: 2,
    Tutorial: 2,
    ToontownCentral: 2,
    DonaldsDock: 2,
    MinniesMelodyland: 2,
    GoofyStadium: 2,
    TheBrrrgh: 2,
    DaisyGardens: 2,
    FunnyFarm: 2,
    DonaldsDreamland: 2,
    ConstructionZone: 2,
    BossbotHQ: 2,
    SellbotHQ: 43,
    CashbotHQ: 2,
    LawbotHQ: 2 }
TrophyStarLevels = (10, 20, 30, 50, 75, 100)
TrophyStarColors = (Vec4(0.90000000000000002, 0.59999999999999998, 0.20000000000000001, 1), Vec4(0.90000000000000002, 0.59999999999999998, 0.20000000000000001, 1), Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1), Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1), Vec4(1, 1, 0, 1), Vec4(1, 1, 0, 1))
SuitWalkSpeed = 4.7999999999999998
PieCodeBossCog = 1
PieCodeNotBossCog = 2
PieCodeToon = 3
PieCodeBossInsides = 4
PieCodeColors = {
    PieCodeBossCog: None,
    PieCodeNotBossCog: (0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1),
    PieCodeToon: None }
BossCogRollSpeed = 7.5
BossCogTurnSpeed = 20
BossCogTreadSpeed = 3.5
BossCogDizzy = 0
BossCogElectricFence = 1
BossCogSwatLeft = 2
BossCogSwatRight = 3
BossCogAreaAttack = 4
BossCogFrontAttack = 5
BossCogRecoverDizzyAttack = 6
BossCogDirectedAttack = 7
BossCogStrafeAttack = 8
BossCogNoAttack = 9
BossCogGoonZap = 10
BossCogSlowDirectedAttack = 11
BossCogDizzyNow = 12
BossCogAttackTimes = {
    BossCogElectricFence: 0,
    BossCogSwatLeft: 5.5,
    BossCogSwatRight: 5.5,
    BossCogAreaAttack: 4.21,
    BossCogFrontAttack: 2.6499999999999999,
    BossCogRecoverDizzyAttack: 5.0999999999999996,
    BossCogDirectedAttack: 4.8399999999999999,
    BossCogNoAttack: 6,
    BossCogSlowDirectedAttack: 7.8399999999999999 }
BossCogDamageLevels = {
    BossCogElectricFence: 1,
    BossCogSwatLeft: 5,
    BossCogSwatRight: 5,
    BossCogAreaAttack: 10,
    BossCogFrontAttack: 3,
    BossCogRecoverDizzyAttack: 3,
    BossCogDirectedAttack: 3,
    BossCogStrafeAttack: 2,
    BossCogGoonZap: 5,
    BossCogSlowDirectedAttack: 10 }
BossCogBattleAPosHpr = (0, -25, 0, 0, 0, 0)
BossCogBattleBPosHpr = (0, 25, 0, 180, 0, 0)
SellbotBossMaxDamage = 100
SellbotBossBattleOnePosHpr = (0, -35, 0, -90, 0, 0)
SellbotBossBattleTwoPosHpr = (0, 60, 18, -90, 0, 0)
SellbotBossBattleThreeHpr = (180, 0, 0)
SellbotBossBottomPos = (0, -110, -6.5)
SellbotBossDeathPos = (0, -175, -6.5)
SellbotBossDooberTurnPosA = (-20, -50, 0)
SellbotBossDooberTurnPosB = (20, -50, 0)
SellbotBossDooberTurnPosDown = (0, -50, 0)
SellbotBossDooberFlyPos = (0, -135, -6.5)
SellbotBossTopRampPosA = (-80, -35, 18)
SellbotBossTopRampTurnPosA = (-80, 10, 18)
SellbotBossP3PosA = (-50, 40, 18)
SellbotBossTopRampPosB = (80, -35, 18)
SellbotBossTopRampTurnPosB = (80, 10, 18)
SellbotBossP3PosB = (50, 60, 18)
CashbotBossMaxDamage = 500
CashbotBossOffstagePosHpr = (120, -195, 0, 0, 0, 0)
CashbotBossBattleOnePosHpr = (120, -230, 0, 90, 0, 0)
CashbotRTBattleOneStartPosHpr = (94, -220, 0, 110, 0, 0)
CashbotBossBattleThreePosHpr = (120, -315, 0, 180, 0, 0)
CashbotToonsBattleThreeStartPosHpr = [
    (105, -285, 0, 208, 0, 0),
    (136, -342, 0, 398, 0, 0),
    (105, -342, 0, 333, 0, 0),
    (135, -292, 0, 146, 0, 0),
    (93, -303, 0, 242, 0, 0),
    (144, -327, 0, 64, 0, 0),
    (145, -302, 0, 117, 0, 0),
    (93, -327, 0, -65, 0, 0)]
CashbotBossSafePosHprs = [
    (120, -315, 30, 0, 0, 0),
    (77.200000000000003, -329.30000000000001, 0, -90, 0, 0),
    (77.099999999999994, -302.69999999999999, 0, -90, 0, 0),
    (165.69999999999999, -326.39999999999998, 0, 90, 0, 0),
    (165.5, -302.39999999999998, 0, 90, 0, 0),
    (107.8, -359.10000000000002, 0, 0, 0, 0),
    (133.90000000000001, -359.10000000000002, 0, 0, 0, 0),
    (107.0, -274.69999999999999, 0, 180, 0, 0),
    (134.19999999999999, -274.69999999999999, 0, 180, 0, 0)]
CashbotBossCranePosHprs = [
    (97.400000000000006, -337.60000000000002, 0, -45, 0, 0),
    (97.400000000000006, -292.39999999999998, 0, -135, 0, 0),
    (142.59999999999999, -292.39999999999998, 0, 135, 0, 0),
    (142.59999999999999, -337.60000000000002, 0, 45, 0, 0)]
CashbotBossToMagnetTime = 0.20000000000000001
CashbotBossFromMagnetTime = 1
CashbotBossSafeKnockImpact = 0.5
CashbotBossSafeNewImpact = 0.0
CashbotBossGoonImpact = 0.10000000000000001
CashbotBossKnockoutDamage = 15
TTWakeWaterHeight = -4.79
DDWakeWaterHeight = 1.669
EstateWakeWaterHeight = -0.29999999999999999
WakeRunDelta = 0.10000000000000001
WakeWalkDelta = 0.20000000000000001
NoItems = 0
NewItems = 1
OldItems = 2
SuitInvasionBegin = 0
SuitInvasionUpdate = 1
SuitInvasionEnd = 2
SuitInvasionBulletin = 3
NO_HOLIDAY = 0
JULY4_FIREWORKS = 1
NEWYEARS_FIREWORKS = 2
HALLOWEEN = 3
WINTER_DECORATIONS = 4
SKELECOG_INVASION = 5
MR_HOLLYWOOD_INVASION = 6
FISH_BINGO_NIGHT = 7
ELECTION_PROMOTION = 8
BLACK_CAT_DAY = 9
RESISTANCE_EVENT = 10
