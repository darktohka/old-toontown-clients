# File: T (Python 2.2)

import string
import time
InterfaceFont = 'phase_3/models/fonts/ImpressBT.ttf'
ToonFont = 'phase_3/models/fonts/ImpressBT.ttf'
SuitFont = 'phase_3/models/fonts/vtRemingtonPortable.ttf'
SignFont = 'phase_3/models/fonts/MickeyFont'
MinnieFont = 'phase_3/models/fonts/MinnieFont'
BuildingNametagFont = 'phase_3/models/fonts/MickeyFont'
BuildingNametagShadow = None
Mickey = 'Mickey'
Minnie = 'Minnie'
Donald = 'Donald'
Daisy = 'Daisy'
Goofy = 'Goofy'
Pluto = 'Pluto'
Flippy = 'Flippy'
lTheBrrrgh = 'The Brrrgh'
lDaisyGardens = 'Daisy Gardens'
lDonaldsDock = "Donald's Dock"
lDonaldsDreamland = "Donald's Dreamland"
lMinniesMelodyland = "Minnie's Melodyland"
lToontownCentral = 'Toontown Central'
lCancel = 'Cancel'
lClose = 'Close'
lOK = 'OK'
lNext = 'Next'
lNo = 'No'
lQuit = 'Quit'
lYes = 'Yes'
lHQOfficerF = 'HQ Officer'
lHQOfficerM = 'HQ Officer'
MickeyMouse = 'Mickey Mouse'
AIStartDefaultDistrict = 'Sillyville'
Cog = 'Cog'
Cogs = 'Cogs'
ACog = 'a Cog'
TheCogs = 'The Cogs'
Skeleton = 'Skelecog'
SkeletonP = 'Skelecogs'
ASkeleton = 'a Skelecog'
Foreman = 'Factory Foreman'
ForemanP = 'Factory Foremen'
AForeman = 'a Factory Foreman'
CogVP = Cog + ' VP'
CogVPs = "Cog VP's"
ACogVP = ACog + ' VP'
Supervisor = 'Mint Supervisor'
SupervisorP = 'Mint Supervisors'
ASupervisor = 'a Mint Supervisor'
CogCFO = Cog + ' CFO'
CogCFOs = "Cog CFO's"
ACogCFO = ACog + ' CFO'
TheFish = 'the Fish'
AFish = 'a fish'
Level = 'Level'
QuestsCompleteString = 'Complete'
QuestsNotChosenString = 'Not chosen'
Period = '.'
Laff = 'Laff'
QuestInLocationString = ' %(inPhrase)s %(location)s'
QuestsDefaultGreeting = ('Hello, _avName_!', 'Hi, _avName_!', 'Hey there, _avName_!', 'Say there, _avName_!', 'Welcome, _avName_!', 'Howdy, _avName_!', 'How are you, _avName_?', 'Greetings _avName_!')
QuestsDefaultIncomplete = ("How's that task coming, _avName_?", 'Looks like you still have more work to do on that task!', 'Keep up the good work, _avName_!', 'Keep trying to finish that task.  I know you can do it!', 'Keep trying to complete that task, we are counting on you!', 'Keep working on that ToonTask!')
QuestsDefaultIncompleteProgress = ('You came to the right place, but you need to finish your ToonTask first.', 'When you are finished with that ToonTask, come back here.', 'Come back when you are finished with your ToonTask.')
QuestsDefaultIncompleteWrongNPC = ('Nice work on that ToonTask. You should go visit _toNpcName_._where_', 'Looks like you are ready to finish your ToonTask. Go see _toNpcName_._where_.', 'Go see _toNpcName_ to finish your ToonTask._where_')
QuestsDefaultComplete = ('Nice work! Here is your reward...', 'Great job, _avName_! Take this reward...', 'Wonderful job, _avName_! Here is your reward...')
QuestsDefaultLeaving = ('Bye!', 'Goodbye!', 'So long, _avName_.', 'See ya, _avName_!', 'Good luck!', 'Have fun in Toontown!', 'See you later!')
QuestsDefaultReject = ('Hello.', 'Can I help you?', 'How are you?', 'Hello there.', "I'm a little busy now, _avName_.", 'Yes?', 'Howdy, _avName_!', 'Welcome, _avName_!', "Hey, _avName_! How's it going?", 'Did you know you can open your Shticker Book by hitting F8?', 'You can use your map to teleport back to the playground!', 'You can make friends with other players by clicking on them.', 'You can discover more about a ' + Cog + ' by clicking on him.', 'Gather treasures in the playgrounds to fill your Laff Meter.', Cog + ' buildings are dangerous places! Do not go in alone!', 'When you lose a battle, the ' + Cogs + ' take all your Gags.', 'To get more gags, play Trolley games!', 'You can get more Laff Points by completing ToonTasks.', 'Every ToonTask gives you a reward.', 'Some rewards let you carry more Gags.', 'If you win a battle, you get ToonTask credit for every ' + Cog + ' defeated.', 'If you recapture a ' + Cog + ' building, go back inside to see a special thank-you from its owner!', 'If you press the Page Up key, you can look up!', 'If you press the Tab key, you can see different views of your surroundings!', "To show secret friends what you're thinking, enter a '.' before your thought.", 'If a ' + Cog + ' is stunned, it is more difficult for them to avoid falling objects.', 'Each kind of ' + Cog + ' building has a distinct look.', 'Defeating ' + Cogs + ' on the higher floors of a building will give you greater skill rewards.')
QuestsDefaultTierNotDone = ('Hello, _avName_! You must finish your current ToonTasks before getting a new one.', 'Hi there! You need to finish the ToonTasks you are working on in order to get a new one.', 'Hi, _avName_! Before I can give you a new ToonTask, you need to finish the ones you have.')
QuestsDefaultQuest = None
QuestsDefaultVisitQuestDialog = ('I heard _toNpcName_ is looking for you._where_', 'Stop by and see _toNpcName_ when you get a chance._where_', 'Pay a visit to _toNpcName_ next time you are over that way._where_', 'If you get a chance, stop in and say hi to _toNpcName_._where_', '_toNpcName_ will give you your next ToonTask._where_')
QuestsLocationArticle = ''

def getLocalNum(num):
    return str(num)

QuestsItemNameAndNum = '%(num)s %(name)s'
QuestsCogQuestProgress = '%(progress)s of %(numCogs)s defeated'
QuestsCogQuestHeadline = 'WANTED'
QuestsCogQuestSCStringS = 'I need to defeat %(cogName)s%(cogLoc)s.'
QuestsCogQuestSCStringP = 'I need to defeat some %(cogName)s%(cogLoc)s.'
QuestsCogQuestDefeat = 'Defeat %s'
QuestsCogQuestDefeatDesc = '%(numCogs)s %(cogName)s'
QuestsCogNewNewbieQuestObjective = 'Help a new Toon defeat %s'
QuestsCogNewNewbieQuestCaption = 'Help a new Toon %d Laff or less'
QuestsCogOldNewbieQuestObjective = 'Help a Toon with %(laffPoints)d Laff or less defeat %(objective)s'
QuestsCogOldNewbieQuestCaption = 'Help a Toon %d Laff or less'
QuestsCogNewbieQuestAux = 'Defeat:'
QuestsNewbieQuestHeadline = 'APPRENTICE'
QuestsCogTrackQuestProgress = '%(progress)s of %(numCogs)s defeated'
QuestsCogTrackQuestHeadline = 'WANTED'
QuestsCogTrackQuestSCStringS = 'I need to defeat %(cogText)s%(cogLoc)s.'
QuestsCogTrackQuestSCStringP = 'I need to defeat some %(cogText)s%(cogLoc)s.'
QuestsCogTrackQuestDefeat = 'Defeat %s'
QuestsCogTrackDefeatDesc = '%(numCogs)s %(trackName)s'
QuestsCogLevelQuestProgress = '%(progress)s of %(numCogs)s defeated'
QuestsCogLevelQuestHeadline = 'WANTED'
QuestsCogLevelQuestDefeat = 'Defeat %s'
QuestsCogLevelQuestDesc = 'a Level %(level)s+ %(name)s'
QuestsCogLevelQuestDescC = '%(count)s Level %(level)s+ %(name)s'
QuestsCogLevelQuestDescI = 'some Level %(level)s+ %(name)s'
QuestsCogLevelQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsBuildingQuestFloorNumbers = ('', 'two+', 'three+', 'four+', 'five+')
QuestsBuildingQuestBuilding = 'Building'
QuestsBuildingQuestBuildings = 'Buildings'
QuestsBuildingQuestHeadline = 'DEFEAT'
QuestsBuildingQuestProgressString = '%(progress)s of %(num)s defeated'
QuestsBuildingQuestString = 'Defeat %s'
QuestsBuildingQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsBuildingQuestDesc = 'a %(type)s Building'
QuestsBuildingQuestDescF = 'a %(floors)s story %(type)s Building'
QuestsBuildingQuestDescC = '%(count)s %(type)s Buildings'
QuestsBuildingQuestDescCF = '%(count)s %(floors)s story %(type)s Buildings'
QuestsBuildingQuestDescI = 'some %(type)s Buildings'
QuestsBuildingQuestDescIF = 'some %(floors)s story %(type)s Buildings'
QuestFactoryQuestFactory = 'Factory'
QuestsFactoryQuestFactories = 'Factories'
QuestsFactoryQuestHeadline = 'DEFEAT'
QuestsFactoryQuestProgressString = '%(progress)s of %(num)s defeated'
QuestsFactoryQuestString = 'Defeat %s'
QuestsFactoryQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsFactoryQuestDesc = 'a %(type)s Factory'
QuestsFactoryQuestDescC = '%(count)s %(type)s Factories'
QuestsFactoryQuestDescI = 'some %(type)s Factories'
QuestMintQuestMint = 'Mint'
QuestsMintQuestMints = 'Mints'
QuestsMintQuestHeadline = 'DEFEAT'
QuestsMintQuestProgressString = '%(progress)s of %(num)s defeated'
QuestsMintQuestString = 'Defeat %s'
QuestsMintQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsMintQuestDesc = 'a Cog Mint'
QuestsMintQuestDescC = '%(count)s Cog Mints'
QuestsMintQuestDescI = 'some Cog Mints'
QuestsRescueQuestProgress = '%(progress)s of %(numToons)s rescued'
QuestsRescueQuestHeadline = 'RESCUE'
QuestsRescueQuestSCStringS = 'I need to rescue a Toon%(toonLoc)s.'
QuestsRescueQuestSCStringP = 'I need to rescue some Toons%(toonLoc)s.'
QuestsRescueQuestRescue = 'Rescue %s'
QuestsRescueQuestRescueDesc = '%(numToons)s Toons'
QuestsRescueQuestToonS = 'a Toon'
QuestsRescueQuestToonP = 'Toons'
QuestsRescueQuestAux = 'Rescue:'
QuestsRescueNewNewbieQuestObjective = 'Help a new Toon rescue %s'
QuestsRescueOldNewbieQuestObjective = 'Help a Toon with %(laffPoints)d Laff or less rescue %(objective)s'
QuestCogPartQuestCogPart = 'Cog Suit Part'
QuestsCogPartQuestFactories = 'Factories'
QuestsCogPartQuestHeadline = 'RETRIEVE'
QuestsCogPartQuestProgressString = '%(progress)s of %(num)s retrieved'
QuestsCogPartQuestString = 'Retrieve %s'
QuestsCogPartQuestSCString = 'I need to retrieve %(objective)s%(location)s.'
QuestsCogPartQuestAux = 'Retrieve:'
QuestsCogPartQuestDesc = 'a Cog Suit Part'
QuestsCogPartQuestDescC = '%(count)s Cog Suit Parts'
QuestsCogPartQuestDescI = 'some Cog Suit Parts'
QuestsCogPartNewNewbieQuestObjective = 'Help a new Toon retrieve %s'
QuestsCogPartOldNewbieQuestObjective = 'Help a Toon with %(laffPoints)d Laff or less retrieve %(objective)s'
QuestsDeliverGagQuestProgress = '%(progress)s of %(numGags)s delivered'
QuestsDeliverGagQuestHeadline = 'DELIVER'
QuestsDeliverGagQuestToSCStringS = 'I need to deliver %(gagName)s.'
QuestsDeliverGagQuestToSCStringP = 'I need to deliver some %(gagName)s.'
QuestsDeliverGagQuestSCString = 'I need make a delivery.'
QuestsDeliverGagQuestString = 'Deliver %s'
QuestsDeliverGagQuestStringLong = 'Deliver %s to _toNpcName_.'
QuestsDeliverGagQuestInstructions = 'You can buy this gag in the Gag Shop once you earn access to it.'
QuestsDeliverItemQuestProgress = ''
QuestsDeliverItemQuestHeadline = 'DELIVER'
QuestsDeliverItemQuestSCString = 'I need to deliver %(article)s%(itemName)s.'
QuestsDeliverItemQuestString = 'Deliver %s'
QuestsDeliverItemQuestStringLong = 'Deliver %s to _toNpcName_.'
QuestsVisitQuestProgress = ''
QuestsVisitQuestHeadline = 'VISIT'
QuestsVisitQuestStringShort = 'Visit'
QuestsVisitQuestStringLong = 'Visit _toNpcName_'
QuestsVisitQuestSeeSCString = 'I need to see %s.'
QuestsRecoverItemQuestProgress = '%(progress)s of %(numItems)s recovered'
QuestsRecoverItemQuestHeadline = 'RECOVER'
QuestsRecoverItemQuestSeeHQSCString = 'I need to see an ' + lHQOfficerM + '.'
QuestsRecoverItemQuestReturnToHQSCString = 'I need to return %s to an ' + lHQOfficerM + '.'
QuestsRecoverItemQuestReturnToSCString = 'I need to return %(item)s to %(npcName)s.'
QuestsRecoverItemQuestGoToHQSCString = 'I need to go to a Toon HQ.'
QuestsRecoverItemQuestGoToPlaygroundSCString = 'I need to go to %s Playground.'
QuestsRecoverItemQuestGoToStreetSCString = 'I need to go %(to)s %(street)s in %(hood)s.'
QuestsRecoverItemQuestVisitBuildingSCString = 'I need to visit %s%s.'
QuestsRecoverItemQuestWhereIsBuildingSCString = 'Where is %s%s?'
QuestsRecoverItemQuestRecoverFromSCString = 'I need to recover %(item)s from %(holder)s%(loc)s.'
QuestsRecoverItemQuestString = 'Recover %(item)s from %(holder)s'
QuestsRecoverItemQuestHolderString = '%(level)s %(holder)d+ %(cogs)s'
QuestsTrackChoiceQuestHeadline = 'CHOOSE'
QuestsTrackChoiceQuestSCString = 'I need to choose between %(trackA)s and %(trackB)s.'
QuestsTrackChoiceQuestMaybeSCString = 'Maybe I should choose %s.'
QuestsTrackChoiceQuestString = 'Choose between %(trackA)s and %(trackB)s'
QuestsFriendQuestHeadline = 'FRIEND'
QuestsFriendQuestSCString = 'I need to make a friend.'
QuestsFriendQuestString = 'Make a friend'
QuestsMailboxQuestHeadline = 'MAIL'
QuestsMailboxQuestSCString = 'I need to check my mail.'
QuestsMailboxQuestString = 'Check your mail'
QuestsPhoneQuestHeadline = 'CLARABELLE'
QuestsPhoneQuestSCString = 'I need to call Clarabelle.'
QuestsPhoneQuestString = 'Call Clarabelle'
QuestsFriendNewbieQuestString = 'Make %d friends %d laff or less'
QuestsFriendNewbieQuestProgress = '%(progress)s of %(numFriends)s made'
QuestsFriendNewbieQuestObjective = 'Make friends with %d new Toons'
QuestsTrolleyQuestHeadline = 'TROLLEY'
QuestsTrolleyQuestSCString = 'I need to ride the trolley.'
QuestsTrolleyQuestString = 'Ride on the trolley'
QuestsTrolleyQuestStringShort = 'Ride the trolley'
QuestsMinigameNewbieQuestString = '%d Minigames'
QuestsMinigameNewbieQuestProgress = '%(progress)s of %(numMinigames)s Played'
QuestsMinigameNewbieQuestObjective = 'Play %d minigames with new Toons'
QuestsMinigameNewbieQuestSCString = 'I need to play minigames with new Toons.'
QuestsMinigameNewbieQuestCaption = 'Help a new Toon %d laff or less'
QuestsMinigameNewbieQuestAux = 'Play:'
QuestsMaxHpReward = 'Your Laff Limit has been increased by %s.'
QuestsMaxHpRewardPoster = 'Reward: %s point LaffBoost'
QuestsMoneyRewardSingular = 'You get 1 jellybean.'
QuestsMoneyRewardPlural = 'You get %s jellybeans.'
QuestsMoneyRewardPosterSingular = 'Reward: 1 jellybean'
QuestsMoneyRewardPosterPlural = 'Reward: %s jellybeans'
QuestsMaxMoneyRewardSingular = 'You can now carry 1 jellybean.'
QuestsMaxMoneyRewardPlural = 'You can now carry %s jellybeans.'
QuestsMaxMoneyRewardPosterSingular = 'Reward: Carry 1 jellybean'
QuestsMaxMoneyRewardPosterPlural = 'Reward: Carry %s jellybeans'
QuestsMaxGagCarryReward = 'You get a %(name)s. You can now carry %(num)s gags.'
QuestsMaxGagCarryRewardPoster = 'Reward: %(name)s (%(num)s)'
QuestsMaxQuestCarryReward = 'You can now have %s ToonTasks.'
QuestsMaxQuestCarryRewardPoster = 'Reward: Carry %s ToonTasks'
QuestsTeleportReward = 'You now have teleport access to %s.'
QuestsTeleportRewardPoster = 'Reward: Teleport access to %s'
QuestsTrackTrainingReward = 'You can now train for "%s" gags.'
QuestsTrackTrainingRewardPoster = 'Reward: Gag training'
QuestsTrackProgressReward = 'You now have frame %(frameNum)s of the %(trackName)s track animation.'
QuestsTrackProgressRewardPoster = 'Reward: "%(trackName)s" track animation frame %(frameNum)s'
QuestsTrackCompleteReward = 'You may now carry and use "%s" gags.'
QuestsTrackCompleteRewardPoster = 'Reward: Final %s track training'
QuestsClothingTicketReward = 'You can change your clothes'
QuestsClothingTicketRewardPoster = 'Reward: Clothing Ticket'
QuestsCheesyEffectRewardPoster = 'Reward: %s'
QuestsCogSuitPartReward = 'You now have a %(cogTrack)s %(part)s Cog Suit Part.'
QuestsCogSuitPartRewardPoster = 'Reward: %(cogTrack)s %(part)s Part'
QuestsStreetLocationThisPlayground = 'in this playground'
QuestsStreetLocationThisStreet = 'on this street'
QuestsStreetLocationNamedPlayground = 'in the %s playground'
QuestsStreetLocationNamedStreet = 'on %s in %s'
QuestsLocationString = '%(string)s%(location)s'
QuestsLocationBuilding = "%s's building is called"
QuestsLocationBuildingVerb = 'which is'
QuestsLocationParagraph = '\x7%(building)s "%(buildingName)s"...\x7...%(buildingVerb)s %(street)s.'
QuestsGenericFinishSCString = 'I need to finish a ToonTask.'
QuestsMediumPouch = 'Medium Pouch'
QuestsLargePouch = 'Large Pouch'
QuestsSmallBag = 'Small Bag'
QuestsMediumBag = 'Medium Bag'
QuestsLargeBag = 'Large Bag'
QuestsSmallBackpack = 'Small Backpack'
QuestsMediumBackpack = 'Medium Backpack'
QuestsLargeBackpack = 'Large Backpack'
QuestsItemDict = {
    1: [
        'Pair of Glasses',
        'Pairs of Glasses',
        'a '],
    2: [
        'Key',
        'Keys',
        'a '],
    3: [
        'Blackboard',
        'Blackboards',
        'a '],
    4: [
        'Book',
        'Books',
        'a '],
    5: [
        'Candy Bar',
        'Candy Bars',
        'a '],
    6: [
        'Piece of Chalk',
        'Pieces of Chalk',
        'a '],
    7: [
        'Recipe',
        'Recipes',
        'a '],
    8: [
        'Note',
        'Notes',
        'a '],
    9: [
        'Adding machine',
        'Adding machines',
        'an '],
    10: [
        'Clown car tire',
        'Clown car tires',
        'a '],
    11: [
        'Air pump',
        'Air pumps',
        'an '],
    12: [
        'Octopus ink',
        'Octopus inks',
        'some '],
    13: [
        'Package',
        'Package',
        'a '],
    14: [
        'Goldfish receipt',
        'Goldfish receipts',
        'a '],
    15: [
        'Goldfish',
        'Goldfish',
        'a '],
    16: [
        'Oil',
        'Oils',
        'some '],
    17: [
        'Grease',
        'Greases',
        'some '],
    18: [
        'Water',
        'Waters',
        'some '],
    19: [
        'Gear report',
        'Gear reports',
        'a '],
    20: [
        'Blackboard Eraser',
        'Blackboard Erasers',
        'a '],
    1000: [
        'Clothing Ticket',
        'Clothing Tickets',
        'a '],
    2001: [
        'Inner Tube',
        'Inner Tubes',
        'an '],
    2002: [
        'Monocle Prescription',
        'Monocle Prescriptions',
        'a '],
    2003: [
        'Eyeglass Frames',
        'Eyeglass Frames',
        'some '],
    2004: [
        'Monocle',
        'Monocles',
        'a '],
    2005: [
        'Big White Wig',
        'Big White Wigs',
        'a '],
    2006: [
        'Bushel of Ballast',
        'Bushels of Ballast',
        'a '],
    2007: [
        'Cog Gear',
        'Cog Gears',
        'a '],
    2008: [
        'Sea Chart',
        'Sea Charts',
        'a '],
    2009: [
        'Cruddy Clovis',
        'Cruddy Clovi',
        'a '],
    2010: [
        'Clean Clovis',
        'Clean Clovi',
        'a '],
    2011: [
        'Clock Spring',
        'Clock Springs',
        'a '],
    2012: [
        'Counter Weight',
        'Counter Weights',
        'a '],
    4001: [
        "Tina's Inventory",
        "Tina's Inventories",
        ''],
    4002: [
        "Yuki's Inventory",
        "Yuki's Inventories",
        ''],
    4003: [
        'Inventory Form',
        'Inventory Forms',
        'an '],
    4004: [
        "Fifi's Inventory",
        "Fifi's Inventories",
        ''],
    4005: [
        "Lumber Jack's Ticket",
        "Lumber Jack's Tickets",
        ''],
    4006: [
        "Tabitha's Ticket",
        "Tabitha's Tickets",
        ''],
    4007: [
        "Barry's Ticket",
        "Barry's Tickets",
        ''],
    4008: [
        'Cloudy Castanet',
        'Cloudy Castanets',
        ''],
    4009: [
        'Blue Squid Ink',
        'Blue Squid Ink',
        'some '],
    4010: [
        'Clear Castanet',
        'Clear Castanets',
        'a '],
    4011: [
        "Leo's Lyrics",
        "Leo's Lyrics",
        ''],
    5001: [
        'Silk necktie',
        'Silk neckties',
        'a '],
    5002: [
        'Pinstripe Suit',
        'Pinstripe Suits',
        'a '],
    5003: [
        'Pair of Scissors',
        'Pairs of Scissors',
        'a '],
    5004: [
        'Postcard',
        'Postcards',
        'a '],
    5005: [
        'Pen',
        'Pens',
        'a '],
    5006: [
        'Inkwell',
        'Inkwells',
        'an '],
    5007: [
        'Notepad',
        'Notepads',
        'a '],
    5008: [
        'Office Lockbox',
        'Office Lockboxes',
        'an '],
    5009: [
        'Bag of Bird Seed',
        'Bags of Bird Seed',
        'a '],
    5010: [
        'Sprocket',
        'Sprockets',
        'a '],
    5011: [
        'Salad',
        'Salads',
        'a '],
    5012: [
        'Key to ' + lDaisyGardens,
        'Keys to ' + lDaisyGardens,
        'a '],
    5013: [
        'Sellbot HQ Blueprints',
        'Sellbot HQ Blueprints',
        'some '],
    5014: [
        'Sellbot HQ Memo',
        'Sellbot HQ Memos',
        'a '],
    5015: [
        'Sellbot HQ Memo',
        'Sellbot HQ Memos',
        'a '],
    5016: [
        'Sellbot HQ Memo',
        'Sellbot HQ Memos',
        'a '],
    5017: [
        'Sellbot HQ Memo',
        'Sellbot HQ Memos',
        'a '],
    3001: [
        'Soccer ball',
        'Soccer balls',
        'a '],
    3002: [
        'Toboggan',
        'Toboggans',
        'a '],
    3003: [
        'Ice cube',
        'Ice cubes',
        'an '],
    3004: [
        'Love letter',
        'Love letters',
        'a '],
    3005: [
        'Wiener dog',
        'Wiener dogs',
        'a '],
    3006: [
        'Engagement ring',
        'Engagement rings',
        'an '],
    3007: [
        'Sardine whiskers',
        'Sardine whiskers',
        'some '],
    3008: [
        'Calming potion',
        'Calming potion',
        'a '],
    3009: [
        'Broken tooth',
        'Broken teeth',
        'a '],
    3010: [
        'Gold tooth',
        'Gold teeth',
        'a '],
    3011: [
        'Pine cone bread',
        'Pine cone breads',
        'a '],
    3012: [
        'Lumpy cheese',
        'Lumpy cheeses',
        'some '],
    3013: [
        'Simple spoon',
        'Simple spoons',
        'a '],
    3014: [
        'Talking toad',
        'Talking toad',
        'a '],
    3015: [
        'Ice cream cone',
        'Ice cream cones',
        'an '],
    3016: [
        'Wig powder',
        'Wig powders',
        'some '],
    3017: [
        'Rubber ducky',
        'Rubber duckies',
        'a '],
    3018: [
        'Fuzzy dice',
        'Fuzzy dice',
        'some '],
    3019: [
        'Microphone',
        'Microphones',
        'a '],
    3020: [
        'Electric keyboard',
        'Electric keyboards',
        'an '],
    3021: [
        'Platform shoes',
        'Platform shoes',
        'some '],
    3022: [
        'Caviar',
        'Caviar',
        'some '],
    3023: [
        'Make-up powder',
        'Make-up powders',
        'some '],
    6001: [
        'Cashbot HQ Plans',
        'Cashbot HQ Plans',
        'some '],
    6002: [
        'Rod',
        'Rods',
        'a '],
    6003: [
        'Drive Belt',
        'Drive Belts',
        'a '],
    6004: [
        'Pair of Pincers',
        'Pairs of Pincers',
        'a '],
    6005: [
        'Reading Lamp',
        'Reading Lamps',
        'a '],
    6006: [
        'Zither',
        'Zithers',
        'a '],
    6007: [
        'Zamboni',
        'Zambonis',
        'a '],
    6008: [
        'Zebra Zabuton',
        'Zebra Zabutons',
        'a '],
    6009: [
        'Zinnias',
        'Zinnias',
        'some '],
    6010: [
        'Zydeco Records',
        'Zydeco Records',
        'some '],
    6011: [
        'Zucchini',
        'Zucchinis',
        'a '],
    6012: [
        'Zoot Suit',
        'Zoot Suits',
        'a '],
    7001: [
        'Plain Bed',
        'Plain Beds',
        'a '],
    7002: [
        'Fancy Bed',
        'Fancy Beds',
        'a '],
    7003: [
        'Blue Bedspread',
        'Blue Bedspreads',
        'a '],
    7004: [
        'Paisley Bedspread',
        'Paisley Bedspreads',
        'a '],
    7005: [
        'Pillows',
        'Pillows',
        'some '],
    7006: [
        'Hard Pillows',
        'Hard Pillows',
        'some '],
    7007: [
        'Pajamas',
        'Pajamas',
        'a pair of '],
    7008: [
        'Footie Pajamas',
        'Footie Pajamas',
        'a pair of '],
    7009: [
        'Puce Footie Pajamas',
        'Puce Footie Pajamas',
        'a pair of '],
    7010: [
        'Fuchsia Footie Pajamas',
        'Fuchsia Footie Pajamas',
        'a pair of '],
    7011: [
        'Cauliflower Coral',
        'Cauliflower Coral',
        'some '],
    7012: [
        'Slimy Kelp',
        'Slimy Kelp',
        'some '],
    7013: [
        'Pestle',
        'Pestles',
        'a '],
    7014: [
        'Jar of Wrinkle Cream',
        'Jars of Wrinkle Cream',
        'a '] }
QuestsHQOfficerFillin = lHQOfficerM
QuestsHQWhereFillin = ''
QuestsHQBuildingNameFillin = 'Toon HQ'
QuestsHQLocationNameFillin = 'in any neighborhood'
QuestsTailorFillin = 'Tailor'
QuestsTailorWhereFillin = ''
QuestsTailorBuildingNameFillin = 'Clothing Store'
QuestsTailorLocationNameFillin = 'in any neighborhood'
QuestsTailorQuestSCString = 'I need to see a Tailor.'
QuestMovieQuestChoiceCancel = 'Come back later if you need a ToonTask! Bye!'
QuestMovieTrackChoiceCancel = 'Come back when you are ready to decide! Bye!'
QuestMovieQuestChoice = 'Choose a ToonTask.'
QuestMovieTrackChoice = 'Ready to decide? Choose a track, or come back later.'
GREETING = 0
QUEST = 1
INCOMPLETE = 2
INCOMPLETE_PROGRESS = 3
INCOMPLETE_WRONG_NPC = 4
COMPLETE = 5
LEAVING = 6
TheBrrrghTrackQuestDict = {
    GREETING: '',
    QUEST: 'Now you are ready.\x7Go out and walk the earth until you know which track you would like to choose.\x7Choose wisely, because this is your final track.\x7When you are certain, return to me.',
    INCOMPLETE_PROGRESS: 'Choose wisely.',
    INCOMPLETE_WRONG_NPC: 'Choose wisely.',
    COMPLETE: 'Very wise choice!',
    LEAVING: 'Good luck.  Return to me when you have mastered your new skill.' }
QuestDialog_3225 = {
    QUEST: "Oh, thanks for coming, _avName_!\x7The Cogs in the neighborhood frightened away my delivery person.\x7I don't have anyone to deliver this salad to _toNpcName_!\x7Can you do it for me? Thanks so much!_where_" }
QuestDialog_2910 = {
    QUEST: 'Back so soon?\x7Great job on the spring.\x7The final item is a counter weight.\x7Stop by and see _toNpcName_ and bring back whatever you can get._where_' }
QuestDialogDict = {
    160: {
        GREETING: '',
        QUEST: "Ok, now I think you are ready for something more rewarding.\x7If you can defeat 3 Bossbots I'll give you a little bonus.",
        INCOMPLETE_PROGRESS: TheCogs + ' are out in the streets, through the tunnels.',
        INCOMPLETE_WRONG_NPC: 'Good job defeating those Cogs. Now go to the Toon Headquarters for your next step!',
        COMPLETE: QuestsDefaultComplete,
        LEAVING: QuestsDefaultLeaving },
    161: {
        GREETING: '',
        QUEST: "Ok, now I think you are ready for something more rewarding.\x7Come back after you defeat 3 Lawbots and I'll have a little something for you.",
        INCOMPLETE_PROGRESS: TheCogs + ' are out in the streets, through the tunnels.',
        INCOMPLETE_WRONG_NPC: 'Good job defeating those Cogs. Now go to the Toon Headquarters for your next step!',
        COMPLETE: QuestsDefaultComplete,
        LEAVING: QuestsDefaultLeaving },
    162: {
        GREETING: '',
        QUEST: 'Ok, now I think you are ready for something more rewarding.\x7Defeat 3 Cashbots and come back here to claim the bounty.',
        INCOMPLETE_PROGRESS: TheCogs + ' are out in the streets, through the tunnels.',
        INCOMPLETE_WRONG_NPC: 'Good job defeating those Cogs. Now go to the Toon Headquarters for your next step!',
        COMPLETE: QuestsDefaultComplete,
        LEAVING: QuestsDefaultLeaving },
    163: {
        GREETING: '',
        QUEST: "Ok, now I think you are ready for something more rewarding.\x7Come see us after you defeat 3 Sellbots and we'll hook you up.",
        INCOMPLETE_PROGRESS: TheCogs + ' are out in the streets, through the tunnels.',
        INCOMPLETE_WRONG_NPC: 'Good job defeating those Cogs. Now go to the Toon Headquarters for your next step!',
        COMPLETE: QuestsDefaultComplete,
        LEAVING: QuestsDefaultLeaving },
    164: {
        QUEST: 'You look like you could use some new gags.\x7Go see %s, maybe he can help you out._where_' % Flippy },
    165: {
        QUEST: 'Hi there.\x7Looks like you need to practice training your gags.\x7Every time you hit a Cog with one of your gags, your experience increases.\x7When you get enough experience, you will be able to use an even better gag.\x7Go practice your gags by defeating 4 Cogs.' },
    166: {
        QUEST: 'Nice work defeating those Cogs.\x7You know, the Cogs come in four different types.\x7They are Lawbots, Cashbots, Sellbots, and Bossbots.\x7You can tell them apart by their coloring and their name labels.\x7For practice go defeat 4 Bossbots.' },
    167: {
        QUEST: 'Nice work defeating those Cogs.\x7You know, the Cogs come in four different types.\x7They are Lawbots, Cashbots, Sellbots, and Bossbots.\x7You can tell them apart by their coloring and their name labels.\x7For practice go defeat 4 Lawbots.' },
    168: {
        QUEST: 'Nice work defeating those Cogs.\x7You know, the Cogs come in four different types.\x7They are Lawbots, Cashbots, Sellbots, and Bossbots.\x7You can tell them apart by their coloring and their name labels.\x7For practice go defeat 4 Sellbots.' },
    169: {
        QUEST: 'Nice work defeating those Cogs.\x7You know, the Cogs come in four different types.\x7They are Lawbots, Cashbots, Sellbots, and Bossbots.\x7You can tell them apart by their coloring and their name labels.\x7For practice go defeat 4 Cashbots.' },
    170: {
        QUEST: 'Nice work, now you know the difference between the 4 types of Cogs.\x7I think you are ready to start training for your third gag track.\x7Go talk to _toNpcName_ to choose your next gag track - he can give you some expert advice._where_' },
    171: {
        QUEST: 'Nice work, now you know the difference between the 4 types of Cogs.\x7I think you are ready to start training for your third gag track.\x7Go talk to _toNpcName_ to choose your next gag track - he can give you some expert advice._where_' },
    172: {
        QUEST: 'Nice work, now you know the difference between the 4 types of Cogs.\x7I think you are ready to start training for your third gag track.\x7Go talk to _toNpcName_ to choose your next gag track - she can give you some expert advice._where_' },
    175: {
        GREETING: '',
        QUEST: "Did you know you have your very own Toon house?\x7Clarabelle Cow runs a phone catalog where you can order furniture to decorate your house.\x7You can also buy SpeedChat phrases, clothing, and other fun things!\x7I'll tell Clarabelle to send you your first catalog now.\x7You get a catalog with new items every week!\x7Go to your home and use your phone to call Clarabelle.",
        INCOMPLETE_PROGRESS: 'Go home and use your phone to call Clarabelle.',
        COMPLETE: 'Hope you have fun ordering things from Clarabelle!\x7I just finished redecorating my house. It looks Toontastic!\x7Keep doing ToonTasks to get more rewards!',
        LEAVING: QuestsDefaultLeaving },
    400: {
        GREETING: '',
        QUEST: 'Throw and Squirt are great, but you will need more gags to fight higher level Cogs.\x7When you team up with other Toons against the Cogs, you can combine attacks for even more damage.\x7Try different combinations of Gags to see what works best.\x7For your next track, choose between Sound and Toonup.\x7Sound is special because when it hits, it damages all Cogs.\x7Toonup lets you heal other Toons in battle.\x7When you are ready to decide, come back here and choose.',
        INCOMPLETE_PROGRESS: 'Back so soon?  Okay, are you ready to choose?',
        INCOMPLETE_WRONG_NPC: 'Think about your decision before choosing.',
        COMPLETE: 'Good decision.  Now before you can use those gags, you must train for them.\x7You must complete a series of ToonTasks for training.\x7Each task will give you a single frame of your gag attack animation.\x7When you collect all 15, you can get the Final Gag Training task that will allow you to use your new gags.\x7You can check your progress in the Shticker Book.',
        LEAVING: QuestsDefaultLeaving },
    1039: {
        QUEST: 'Visit _toNpcName_ if you want to get around town more easily._where_' },
    1040: {
        QUEST: 'Visit _toNpcName_ if you want to get around town more easily._where_' },
    1041: {
        QUEST: 'Hi!  What brings you here?\x7Everybody uses their portable hole to travel around Toontown.\x7Why, you can teleport to your friends using the Friends List, or to any neighborhood using the map in the Shticker Book.\x7Of course, you have to earn that!\x7Say, I can turn on your teleport access to ' + lToontownCentral + ' if you help out a friend of mine.\x7Seems the Cogs are causing trouble over on Loopy Lane.  Go visit _toNpcName_._where_' },
    1042: {
        QUEST: 'Hi!  What brings you here?\x7Everybody uses their portable hole to travel around Toontown.\x7Why, you can teleport to your friends using the Friends List, or to any neighborhood using the map in the Shticker Book.\x7Of course, you have to earn that!\x7Say, I can turn on your teleport access to ' + lToontownCentral + ' if you help out a friend of mine.\x7Seems the Cogs are causing trouble over on Loopy Lane.  Go visit _toNpcName_._where_' },
    1043: {
        QUEST: 'Hi!  What brings you here?\x7Everybody uses their portable hole to travel around Toontown.\x7Why, you can teleport to your friends using the Friends List, or to any neighborhood using the map in the Shticker Book.\x7Of course, you have to earn that!\x7Say, I can turn on your teleport access to ' + lToontownCentral + ' if you help out a friend of mine.\x7Seems the Cogs are causing trouble over on Loopy Lane.  Go visit _toNpcName_._where_' },
    1044: {
        QUEST: 'Oh, thanks for stopping by.  I really need some help.\x7As you can see, I have no customers.\x7My secret recipe book is lost and nobody comes to my restaurant anymore.\x7I last saw it just before those Cogs took over my building.\x7Can you help me by recovering four of my famous recipes?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Any luck finding my recipes?' },
    1045: {
        QUEST: 'Thank you so much!\x7Before long I will have the entire collection and can reopen my restaurant.\x7Oh, I have a note here for you - something about teleport access?\x7It says thanks for helping my friend and to deliver this to Toon Headquarters.\x7Well, thanks indeed - bye!',
        LEAVING: '',
        COMPLETE: 'Ah, yes, says here you have been a great help to some of the fine folks out on Loopy Lane.\x7Says you need teleport access to ' + lToontownCentral + '.\x7Well, consider it done.\x7Now you can teleport back to the playground from almost anywhere in Toontown.\x7Just open your map and click on ' + lToontownCentral + '.' },
    1046: {
        QUEST: 'The Cashbots have really been bothering the Funny Money Savings and Loan.\x7Stop by there and see if there is anything you can do._where_' },
    1047: {
        QUEST: 'Cashbots have been sneaking into the bank and stealing our machines.\x7Please recover 5 adding machines from Cashbots.\x7To save you from running back and forth, just bring them all back at once.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Still looking for adding machines?' },
    1048: {
        QUEST: 'Wow!  Thanks for finding our adding machines.\x7Hm... They look a little damaged.\x7Say, could you take them over to _toNpcName_ over at her shop, "Tickle Machines" on this street?\x7See if she can fix them.',
        LEAVING: '' },
    1049: {
        QUEST: "What's that?  Broken adding machines?\x7Cashbots you say?\x7Well, let's have a look see...\x7Yep, gears are stripped, but I'm out of that part...\x7You know what might work - some Cog gears, large ones, from larger Cogs...\x7Level 3 Cog gears should do the trick.  I'll need 2 for each machine, so 10 total.\x7Bring them back all at once and I'll fix em up!",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Remember, I need 10 gears to fix the machines.' },
    1053: {
        QUEST: "Ah yes, that should do the trick indeedy.\x7All fixed now, free of charge.\x7Take these back to Funny Money, and tell 'im I said howdy.",
        LEAVING: '',
        COMPLETE: "Adding machines all fixed up?\x7Nice work.  I'm sure I've got something around here to reward you with..." },
    1054: {
        QUEST: '_toNpcName_ needs some help with his clown cars._where_' },
    1055: {
        QUEST: "Yowza!  I can't find the tires to this here clown car anywhere!\x7Do ya think you could help me out?\x7I think Loopy Bob may have tossed them in the pond in the " + lToontownCentral + ' playground.\x7If you stand on one of the docks there you can try and fish out the tires for me.',
        GREETING: 'Woohoo!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Are you having trouble fishing out all 4 tires?' },
    1056: {
        QUEST: 'Fan-flying-tastic!  Now I can get this old clown car on the road again!\x7Hey, I thought I had an air pump around here to inflate these tires...\x7Maybe _toNpcName_ borrowed it?\x7Could you go ask for it back for me?_where_',
        LEAVING: '' },
    1057: {
        QUEST: "Hi there.\x7A tire pump you say?\x7I'll tell you what - you help clean up the streets of some of those high level Cogs for me...\x7And I'll let you have the tire pump.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Is that the best you can do?' },
    1058: {
        QUEST: "Good job - I knew you could do it.\x7Here's the pump.  I'm sure _toNpcName_ will be glad to get it back.",
        LEAVING: '',
        GREETING: '',
        COMPLETE: "Yeehaw!  Now I'm good to go!\x7By the way, thanks for helping me out.\x7Here, take this." },
    1059: {
        QUEST: '_toNpcName_ is running low on supplies.  Maybe you can give him a hand?_where_' },
    1060: {
        QUEST: "Thanks for stopping by!\x7Those Cogs have been stealing my ink, so I'm running very low.\x7Could you fish some octopus ink out of the pond for me?\x7Just stand on a dock near the pond to fish.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Are you having trouble fishing?' },
    1061: {
        QUEST: "Great - thanks for the ink!\x7You know what, maybe if you cleared away some of those Pencil Pushers...\x7I wouldn't run out of ink again so quickly.\x7Defeat 6 Pencil Pushers in " + lToontownCentral + ' for your reward.',
        LEAVING: '',
        COMPLETE: 'Thanks!  Let me reward you for your help.',
        INCOMPLETE_PROGRESS: 'I just saw some more Pencil Pushers.' },
    1062: {
        QUEST: "Great - thanks for the ink!\x7You know what, maybe if you cleared away some of those Blood Suckers...\x7I wouldn't run out of ink again so quickly.\x7Defeat 6 Blood Sucker in " + lToontownCentral + ' for your reward.',
        LEAVING: '',
        COMPLETE: 'Thanks!  Let me reward you for your help.',
        INCOMPLETE_PROGRESS: 'I just saw some more Blood Suckers.' },
    900: {
        QUEST: 'I hear _toNpcName_ needs help with a package._where_' },
    1063: {
        QUEST: 'Hi - thanks for coming in.\x7A Cog stole a very important package from right under my nose.\x7Please see if you can get it back.  I think he was a level 3...\x7So, defeat level 3 Cogs until you find my package.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No luck finding the package, huh?' },
    1067: {
        QUEST: "That's it, all right!\x7Hey, the address is smudged...\x7All I can read is that it's for a Dr. - the rest is all blurry.\x7Maybe it's for _toNpcName_?  Could you take it to him?_where_",
        LEAVING: '' },
    1068: {
        QUEST: "I wasn't expecting a package.  Maybe it's for Dr. I.M. Euphoric?\x7My assistant was going over there today anyway, so I'll have him check for you.\x7In the meantime, would you mind getting rid of some of the Cogs on my street?\x7Defeat 10 Cogs in " + lToontownCentral + '.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "My assistant isn't back yet." },
    1069: {
        QUEST: "Dr. Euphoric says he wasn't expecting a package either.\x7Unfortunately, a Cashbot stole it from my assistant on the way back.\x7Could you try and get it back?",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No luck finding the package, huh?' },
    1070: {
        QUEST: "Dr. Euphoric says he wasn't expecting a package either.\x7Unfortunately, a Sellbot stole the package from my assistant on the way back.\x7I'm sorry, but you'll have to find that Sellbot and get it back.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No luck finding the package, huh?' },
    1071: {
        QUEST: "Dr. Euphoric says he wasn't expecting a package either.\x7Unfortunately, a Bossbot stole it from my assistant on the way back.\x7Could you try and get it back?",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No luck finding the package, huh?' },
    1072: {
        QUEST: 'Great - you got it back!\x7Maybe you should try _toNpcName_, it could be for him._where_',
        LEAVING: '' },
    1073: {
        QUEST: 'Oh, thanks for bringing me my packages.\x7Wait a second, I was expecting two.  Could you check with _toNpcName_ and see if he has the other one?',
        INCOMPLETE: 'Were you able to find my other package?',
        LEAVING: '' },
    1074: {
        QUEST: 'He said there was another package?  Maybe the Cogs stole it too.\x7Defeat Cogs until you find the second package.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No luck finding the other package, huh?' },
    1075: {
        QUEST: 'I guess there was a second package after all!\x7Hurry and take it over to _toNpcName_ with my apologies.',
        COMPLETE: 'Hey, my package is here!\x7Since you seem to be such a helpful Toon, this should come in handy.',
        LEAVING: '' },
    1076: {
        QUEST: "There's been some trouble over at 14 Karat Goldfish.\x7_toNpcName_ could probably use a hand._where_" },
    1077: {
        QUEST: "Thanks for coming - the Cogs stole all my goldfish.\x7I think the Cogs want to sell them to make a quick buck.\x7Those 5 fish have been my only companions in this tiny store for so many years...\x7If you could get them back for me I'd really appreciate it.\x7I'm sure one of the Cogs has my fish.\x7Defeat Cogs until you find my goldfish.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Please return my goldfish to me.' },
    1078: {
        QUEST: "Oh, you have my fish!\x7Huh?  What's this - a receipt?\x7Sigh, I guess they are Cogs, after all.\x7I can't make heads or tails out of this receipt.  Could you take it to _toNpcName_ and see if he can read it?_where_",
        INCOMPLETE: 'What did _toNpcName_ have to say about the receipt?',
        LEAVING: '' },
    1079: {
        QUEST: "Mmm, let me see that receipt.\x7...Ah Yes, it says that 1 goldfish was sold to a Flunky.\x7It doesn't seem to mention what happened to the other 4 fish.\x7Maybe you should try and find that Flunky.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I don't think there's anything else I can help you with.\x7Why don't you try and find that goldfish?" },
    1092: {
        QUEST: "Mmm, let me see that receipt.\x7...Ah Yes, it says that 1 goldfish was sold to a Short Change.\x7It doesn't seem to mention what happened to the other 4 fish.\x7Maybe you should try and find that Short Change.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I don't think there's anything else I can help you with.\x7Why don't you try and find that goldfish?" },
    1080: {
        QUEST: "Oh thank heavens!  You found Oscar - he's my favorite.\x7What's that, Oscar?  Uh huh... they did? ... they are?\x7Oscar says the other 4 escaped into the pond in the playground.\x7Could you go round them up for me?\x7Just fish them out of the pond.",
        LEAVING: '',
        COMPLETE: 'Ahh, I am sooo happy!  To be reunited with my little buddies!\x7You deserve a handsome reward for this!',
        INCOMPLETE_PROGRESS: 'Are you having trouble finding those fish?' },
    1081: {
        QUEST: '_toNpcName_ appears to be in a sticky situation.  She sure could use a hand._where_' },
    1082: {
        QUEST: "I spilled quick dry glue and I'm stuck - stuck cold!\x7If there were a way out, I sure would be sold.\x7That gives me an idea, if you are feeling loyal.\x7Defeat some Sellbots and bring back some oil.",
        LEAVING: '',
        GREETING: '',
        INCOMPLETE_PROGRESS: 'Can you help me get un-stuck?' },
    1083: {
        QUEST: "Well, oil helped a little, but I still cannot budge,\x7What else would help?  It's hard to judge.\x7That gives me an idea; it's worth a try at least.\x7Defeat some Lawbots and bring back some grease.",
        LEAVING: '',
        GREETING: '',
        INCOMPLETE_PROGRESS: 'Can you help me get un-stuck?' },
    1084: {
        QUEST: "Nope, that didn't help.  This is really not funny.\x7I put the grease right there on the money,\x7That gives me an idea, before I forget it.\x7Defeat some Cashbots; bring back water to wet it.",
        LEAVING: '',
        GREETING: '',
        COMPLETE: "Hooray, I'm free of this quick drying glue,\x7As a reward I give this gift to you,\x7You can laugh a little longer while battling and then...\x7Oh, no!  I'm already stuck here again!",
        INCOMPLETE_PROGRESS: 'Can you help me get un-stuck?' },
    1085: {
        QUEST: '_toNpcName_ is conducting some research on the Cogs.\x7Go talk to him if you want to help out._where_' },
    1086: {
        QUEST: "That's right, I'm conducting a study of the Cogs.\x7I want to know what makes them tick.\x7It sure would help me if you could gather some gears from Cogs.\x7Make sure they're from at least level 2 Cogs so they're big enough to examine.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Can't find enough gears?" },
    1089: {
        QUEST: "Okay, let's take a look.  These are excellent specimens!\x7Mmmm...\x7Okay, here's my report.  Take this back to Toon Headquarters right away.",
        INCOMPLETE: 'Have you delivered my report to Headquarters?',
        COMPLETE: "Good work _avName_, we'll take this one from here.",
        LEAVING: '' },
    1090: {
        QUEST: '_toNpcName_ has some useful information for you._where_' },
    1091: {
        QUEST: 'I hear that Toon Headquarters is working on a sort of Cog Radar.\x7It will let you see where the Cogs are so that it will be easier to find them.\x7That Cog Page in your Shticker Book is the key.\x7By defeating enough Cogs, you can tune in to their signals and actually track where they are.\x7Keep defeating Cogs, so you will be ready.',
        COMPLETE: 'Good work!  You could probably use this...',
        LEAVING: '' },
    401: {
        GREETING: '',
        QUEST: 'Now you get to choose the next gag track you want to learn.\x7Take your time deciding, and come back here where you are ready to choose.',
        INCOMPLETE_PROGRESS: 'Think about your decision before choosing.',
        INCOMPLETE_WRONG_NPC: 'Think about your decision before choosing.',
        COMPLETE: 'A wise decision...',
        LEAVING: QuestsDefaultLeaving },
    2201: {
        QUEST: 'Those sneaky Cogs are at it again.\x7_toNpcName_ has reported another missing item. Stop by and see if you can straighten it out._where_' },
    2202: {
        QUEST: "Hi, _avName_. Thank goodness you're here. A mean looking Penny Pincher was just in here and he made off with an inner tube.\x7I fear they may use it for their vile purposes.\x7Please see if you can find him and bring it back.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Any luck finding my inner tube?',
        COMPLETE: 'You found my inner tube! You ARE good. Here, take your reward...' },
    2203: {
        QUEST: TheCogs + ' are wreaking havoc over at the bank.\x7Go see Captain Carl and see what you can do._where_' },
    2204: {
        QUEST: "Welcome aboard, matey.\x7Argh! Those rapscallion Cogs smashed my monocle and I can't sort me change without it.\x7Be a good landlubber and take this prescription to Dr. Queequeg and fetch me a new one._where_",
        GREETING: '',
        LEAVING: '' },
    2205: {
        QUEST: "What's this?\x7Oh, I'd love to fill this prescription but the Cogs have been pilfering my supplies.\x7If you can get me the eyeglass frames off a flunky I can probably help you out.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Sorry. No flunky frames, no monocle.' },
    2206: {
        QUEST: 'Excellent!\x7Just a second...\x7Your prescription is filled. Please take this monocle straight to Captain Carl._where_',
        GREETING: '',
        LEAVING: '',
        COMPLETE: "Avast Ye!\x7You're gonna earn your sea legs after all.\x7Here ye be." },
    2207: {
        QUEST: "Barnacle Barbara has a Cog in her shop!\x7You'd better get over there pronto._where_" },
    2208: {
        QUEST: "Gosh! You just missed him, sweetie.\x7There was a Back Stabber in here. He took my big white wig.\x7He said it was for his boss and something about 'legal precedent.'\x7If you can get it back I'd be forever grateful.",
        LEAVING: '',
        GREETING: '',
        INCOMPLETE_PROGRESS: "Still haven't found him?\x7He's tall and has a pointy head",
        COMPLETE: "You found it!?!?\x7Aren't you a darling!\x7You've more than earned this..." },
    2209: {
        QUEST: 'Melville is preparing for an important voyage.\x7Pop in and see what you can do to help sort him out._where_' },
    2210: {
        QUEST: "I can use your help.\x7I've been asked by Toon HQ to take a voyage and see if I can find where the Cogs are coming from.\x7I'll need a few things for my ship but I don't have many jellybeans.\x7Stop by and pick up some ballast from Alice. You'll have to do a favor for her to get it._where_",
        GREETING: 'Howdy, _avName_',
        LEAVING: '' },
    2211: {
        QUEST: "So Melville wants ballast, does he?\x7He still owes me for the last bushel.\x7I'll give it to you if you can clear five Micromanagers off my street.",
        INCOMPLETE_PROGRESS: 'No, silly! I said FIVE micromanagers...',
        GREETING: 'What can I do for you?',
        LEAVING: '' },
    2212: {
        QUEST: "A deal's a deal.\x7Here's your ballast for that cheapskate Melville._where_",
        GREETING: 'Well, look what the cat dragged in...',
        LEAVING: '' },
    2213: {
        QUEST: "Excellent work. I knew she'd be reasonable.\x7Next I'll need a sailing chart from Art.\x7I don't think my credit is good there either so you'll have to work something out with him._where_",
        GREETING: '',
        LEAVING: '' },
    2214: {
        QUEST: "Yes, I have the sea chart Melville wants.\x7And if you're willing to work for it I'll let you have it.\x7I'm trying to build an astrolabe to navigate by the stars.\x7I could use three Cog gears to build it.\x7Come back when you've found them.",
        INCOMPLETE_PROGRESS: "How's it coming with those Cog gears?",
        GREETING: 'Welcome!',
        LEAVING: 'Good luck!' },
    2215: {
        QUEST: "Ooh! These gears will do rather nicely.\x7Here's the chart. Give it to Melville with my compliments._where_",
        GREETING: '',
        LEAVING: '',
        COMPLETE: "Well, that just about does it. I'm ready to sail!\x7I'd take you with me if you weren't so green. Take this instead." },
    901: {
        QUEST: "If you're up for it Ahab could use some assistance over at his place..._where_" },
    2902: {
        QUEST: "Are you the new recruit?\x7Good, good. Maybe you can help me.\x7I'm building a giant prefab crab to confuse the Cogs.\x7I could use a clovis though. Go see Claggart and bring one back, please._where_" },
    2903: {
        QUEST: "Hi there!\x7Yes, I heard about the giant crab Ahab's working on.\x7The best clovis I have is a little on the dirty side though.\x7Be a sport and run it by the cleaners for me before you drop it off._where_",
        LEAVING: 'Thanks!' },
    2904: {
        QUEST: 'You must be the one that Claggart sent over.\x7I think I can clean that up in short order.\x7Just a minute...\x7There you are. Good as new!\x7Tell Ahab I said hello._where_' },
    2905: {
        QUEST: "Ah, now this is exactly what I was looking for.\x7While you're here, I'm also going to need a very large clock spring.\x7Take a walk over to Hook's place and see if he has one._where_" },
    2906: {
        QUEST: "A large spring, eh?\x7I'm sorry but the largest spring I have is still quite small.\x7Perhaps I could assemble one out of squirt gun trigger springs.\x7Bring me three of these gags and I'll see what I can do." },
    2907: {
        QUEST: "Let's have a look then...\x7Smashing. Simply Smashing.\x7Sometimes I even surprise myself.\x7Here you go: one large spring for Ahab!_where_",
        LEAVING: 'Bon Voyage!' },
    2911: {
        QUEST: "I'd be happy to help the cause, _avName_.\x7But I'm afraid the streets are no longer safe.\x7Why don't you go take out some Cashbot Cogs and we'll talk.",
        INCOMPLETE_PROGRESS: 'I still think you need to make the streets safer.' },
    2916: {
        QUEST: 'Yes, I have a weight that Ahab can have.\x7I think it would be safer if you defeated a couple sellbots first though.',
        INCOMPLETE_PROGRESS: 'Not yet. Defeat some more sellbots.' },
    2921: {
        QUEST: "Hmmm, I supposed I could give up a weight.\x7I'd feel a lot better about it if there weren't so many Bossbot Cogs creeping around.\x7Defeat six and then come see me.",
        INCOMPLETE_PROGRESS: "I don't think its safe yet..." },
    2925: {
        QUEST: "All done?\x7Well, I guess it's safe enough now.\x7Here's the counter weight for Ahab._where_" },
    2926: {
        QUEST: "Well, that's everything.\x7Let's see if it works.\x7Hmmm, one small problem.\x7I'm not getting any power because that Cog building is blocking my solar panel.\x7Could you retake it for me?",
        INCOMPLETE_PROGRESS: 'Still no power. How about that building?',
        COMPLETE: 'Super! You are one heck of a Cog crusher! Here, take this as your reward...' },
    3200: {
        QUEST: "I just got a call in from _toNpcName_.\x7He's having a hard day. Maybe you can help him out!\x7Drop by and see what he needs._where_" },
    3201: {
        QUEST: 'Oh, thanks for coming!\x7I need someone to take this new silk tie to _toNpcName_.\x7Would you be able to do that for me?_where_' },
    3203: {
        QUEST: 'Oh, this must be the tie I ordered! Thanks!\x7It matches a pinstripe suit I just finished, right over here.\x7Hey, what happened to that suit?\x7Oh no! The Cogs must have stolen my new suit!\x7Defeat Cogs until you find my suit, and bring it back to me.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Have you found my suit yet? I'm sure the Cogs took it!",
        COMPLETE: 'Hooray! You found my new suit!\x7See, I told you the Cogs had it! Here is your reward...' },
    3204: {
        QUEST: "_toNpcName_ just called to report a theft.\x7Why don't you stop by and see if you can sort things out?_where_" },
    3205: {
        QUEST: "Hello, _avName_! Have you come to help me?\x7I just chased a Bloodsucker out of my shop. Whew! That was scary.\x7But now I can't find my scissors anywhere! I'm sure that Bloodsucker took them.\x7Find that Bloodsucker, and recover my scissors for me.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Are you still looking for my scissors?',
        COMPLETE: 'My scissors! Thank you so much! Here is your reward...' },
    3206: {
        QUEST: 'It sounds like _toNpcName_ is having problems with some Cogs.\x7Go see if you can help him out._where_' },
    3207: {
        QUEST: 'Hi, _avName_! Thanks for coming by!\x7A bunch of Double Talkers just broke in and stole a stack of postcards from my counter.\x7Please go out and defeat all those Double Talkers to get my postcards back!',
        INCOMPLETE_PROGRESS: "That's not enough postcards! Keep looking!",
        COMPLETE: 'Oh, thank you! Now I can deliver the mail on time! Here is your reward...' },
    3208: {
        QUEST: "We've been getting complaints from the residents lately about all of the Cold Callers.\x7See if you can defeat 10 Cold Callers to help out your fellow Toons in " + lDaisyGardens + '.' },
    3209: {
        QUEST: 'Thanks for taking care of those Cold Callers!\x7But now the Telemarketers have gotten out of hand.\x7Defeat 10 Telemarketers in ' + lDaisyGardens + ' and come back here for your reward.' },
    3247: {
        QUEST: "We've been getting complaints from the residents lately about all of the Blood Suckers.\x7See if you can defeat 20 Blood Suckers to help out your fellow Toons in " + lDaisyGardens + '.' },
    3210: {
        QUEST: 'Oh no, The Squirting Flower on Maple Street just ran out of flowers!\x7Take them ten of your own squirting flowers to help out.\x7Make sure you have 10 squirting flowers in your inventory first.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I need to have 10 squirting flowers. You don't have enough!" },
    3211: {
        QUEST: "Oh, thank you so much! Those squirting flowers will save the day.\x7But I'm scared of the Cogs outside.\x7Can you help me out and defeat some of those Cogs?\x7Come back to me after you have defeated 20 Cogs on this street.",
        INCOMPLETE_PROGRESS: 'There are still Cogs out there to defeat!  Keep it up!',
        COMPLETE: 'Oh, thank you! That helps a lot. Your reward is...' },
    3212: {
        QUEST: '_toNpcName_ needs some help looking for something she lost.\x7Go visit her and see what you can do._where_' },
    3213: {
        QUEST: 'Hi, _avName_. Can you help me?\x7I seem to have misplaced my pen. I think maybe some Cogs took it.\x7Defeat Cogs to find my stolen pen.',
        INCOMPLETE_PROGRESS: 'Have you found my pen yet?' },
    3214: {
        QUEST: "Yes, that's my pen! Thanks so much!\x7But while you were gone I realized my inkwell was missing too.\x7Defeat Cogs to find my inkwell.",
        INCOMPLETE_PROGRESS: "I'm still looking for my inkwell!" },
    3215: {
        QUEST: "Great! Now I have my pen and my inkwell back!\x7But wouldn't you know it?\x7My notepad is gone! They must have stolen it too!\x7Defeat Cogs to find my stolen notepad, and then bring it back for your reward.",
        INCOMPLETE_PROGRESS: 'Any word on that notepad yet?' },
    3216: {
        QUEST: "That's my notepad! Hooray! Your reward is...\x7Hey! Where did it go?\x7I had your reward right here in my office lockbox. But the whole lockbox is gone!\x7Can you believe it? Those Cogs stole your reward!\x7Defeat Cogs to recover my lockbox.\x7When you bring it back to me I'll give you your reward.",
        INCOMPLETE_PROGRESS: 'Keep looking for that lockbox!  It has your reward inside it!',
        COMPLETE: 'Finally! I had your new gag bag in that lockbox. Here it is...' },
    3217: {
        QUEST: "We've been performing some studies on Sellbot mechanics.\x7We still need to study some pieces more closely.\x7Bring us a sprocket from a Name Dropper.\x7You can catch one when the Cog is exploding." },
    3218: {
        QUEST: 'Good job! Now we need a sprocket from a Glad Hander for comparison.\x7These sprockets are harder to catch, so keep trying.' },
    3219: {
        QUEST: 'Great! Now we need just one more sprocket.\x7This time, we need a sprocket from a Mover & Shaker.\x7You might need to look inside some Sellbot buildings to find these Cogs.\x7When you catch one, bring it back for your reward.' },
    3244: {
        QUEST: "We've been performing some studies on Lawbot mechanics.\x7We still need to study some pieces more closely.\x7Bring us a sprocket from an Ambulance Chaser.\x7You can catch one when the Cog is exploding." },
    3245: {
        QUEST: 'Good job! Now we need a sprocket from a Back Stabber for comparison.\x7These sprockets are harder to catch, so keep trying.' },
    3246: {
        QUEST: 'Great! Now we need just one more sprocket.\x7This time, we need a sprocket from a Spin Doctor.\x7When you catch one, bring it back for your reward.' },
    3220: {
        QUEST: "I just heard that _toNpcName_ was asking around for you.\x7Why don't you drop by and see what she wants?_where_" },
    3221: {
        QUEST: 'Hi, _avName_! There you are!\x7I heard you were quite an expert in squirt attacks.\x7I need someone to set a good example for all the Toons in ' + lDaisyGardens + '.\x7Use your squirt attacks to defeat a bunch of Cogs.\x7Encourage your friends to use squirt too.\x7When you have defeated 20 Cogs, come back here for a reward!' },
    3222: {
        QUEST: "It's time to demonstrate your Toonmanship.\x7If you successfully reclaim a number of Cog buildings, you'll earn the right to carry three quests.\x7First, defeat any two Cog buildings.\x7Feel free to call on your friends to help you out." },
    3223: {
        QUEST: 'Great job on those buildings!\x7Now, defeat two more buildings.\x7These buildings must be at least two stories high, or higher.' },
    3224: {
        QUEST: 'Fantastic!\x7Now just defeat two more buildings.\x7These buildings must be at least three stories high.\x7When you finish, come back for your reward!',
        COMPLETE: 'You did it, _avName_!\x7You demonstrated your superior Toonmanship.',
        GREETING: '' },
    3225: {
        QUEST: "_toNpcName_ says she needs some help.\x7Why don't you go see what you can do to help out?_where_" },
    3235: {
        QUEST: "Oh, this is the salad I ordered!\x7Thank you for bringing it to me.\x7All those Cogs must have frightened away _toNpcName_'s regular delivery person again.\x7Why don't you do us a favor and defeat some of the Cogs out there?\x7Defeat 10 Cogs in " + lDaisyGardens + ' and then report back to _toNpcName_.',
        INCOMPLETE_PROGRESS: "You're working on defeating Cogs for me?\x7That's wonderful! Keep up the good work!",
        COMPLETE: 'Oh, thank you so much for defeating those Cogs!\x7Now maybe I can keep my regular delivery schedule.\x7Your reward is...',
        INCOMPLETE_WRONG_NPC: "Go tell _toNpcName_ about the Cogs you've defeated._where_" },
    3236: {
        QUEST: 'There are far too many Lawbots out there.\x7You can do your part to help!\x7Defeat 3 Lawbot buildings.' },
    3237: {
        QUEST: 'Great job on those Lawbot buildings!\x7But now there are too many Sellbots!\x7Defeat 3 Sellbot buildings, then come back for your reward.' },
    3238: {
        QUEST: 'Oh no! A "Mingler" Cog has stolen the Key to ' + lDaisyGardens + '!\x7See if you can recover it.\x7Remember, The Mingler can be found only inside Sellbot buildings.' },
    3239: {
        QUEST: "You found a key all right, but it isn't the right one!\x7We need the Key to " + lDaisyGardens + '.\x7Keep looking! A "Mingler" Cog still has it!' },
    3242: {
        QUEST: 'Oh no! A Legal Eagle Cog has stolen the Key to ' + lDaisyGardens + '!\x7See if you can recover it.\x7Remember, Legal Eagles can be found only inside Lawbot buildings.' },
    3243: {
        QUEST: "You found a key all right, but it isn't the right one!\x7We need the Key to " + lDaisyGardens + '.\x7Keep looking! A Legal Eagle Cog still has it!' },
    3240: {
        QUEST: "I've just heard from _toNpcName_ that a Legal Eagle stole a bag of his bird seed.\x7Defeat Legal Eagles until you recover Bud's bird seed, and take it to him.\x7Legal Eagles are only found inside Lawbot buildings._where_",
        COMPLETE: 'Oh, thank you so much for finding my bird seed!\x7Your reward is...',
        INCOMPLETE_WRONG_NPC: 'Good job getting that bird seed back!\x7Now take it to _toNpcName_._where_' },
    3241: {
        QUEST: 'Some of the Cog buildings out there are getting too tall for our comfort.\x7See if you can bring down some of the tallest buildings.\x7Rescue 5 3-story buildings or taller and come back for your reward.' },
    3250: {
        QUEST: 'Detective Lima over on Oak Street has heard some reports of a Sellbot Headquarters.\x7Head over there and help her investigate.' },
    3251: {
        QUEST: "There is something strange going on around here.\x7There are so many Sellbots!\x7I've heard they have organized their own headquarters at the end of this street.\x7Head down the street and see if you can get to the bottom of this.\x7Find Sellbot Cogs in their headquarters, defeat 5 of them, and report back." },
    3252: {
        QUEST: "Ok, spill the beans.\x7What's that you say?\x7Sellbot Headquarters?? Oh no!!! Something must be done.\x7We must notify Judge McIntosh - she'll know what to do.\x7Go at once and tell her what you have found out. She's just down the street." },
    3253: {
        QUEST: "Yes, can I help you? I'm very busy.\x7Eh? Cog Headquarters?\x7Eh? Nonsense. That could never happen.\x7You must be mistaken. Preposterous.\x7Eh? Don't argue with me.\x7Ok then, bring back some proof.\x7If Sellbots really are building this Cog HQ, any Cog there will be carrying blueprints.\x7Cogs love paperwork, you know?\x7Defeat Sellbots in there until you find blueprints.\x7Bring them back here and maybe I'll believe you." },
    3254: {
        QUEST: "You again, eh? Blueprints? You have them?\x7Let me see those! Hmmm... A factory?\x7That must be where they are building the Sellbots... And what's this?\x7Yes, just what I suspected. I knew it all along.\x7They are building a Sellbot Cog Headquarters.\x7This is not good. Must make some phone calls. Very busy. Goodbye!\x7Eh? Oh yes, take these blueprints back to Detective Lima.\x7She can make more sense of them.",
        COMPLETE: "What did Judge McIntosh say?\x7We were right? Oh no. Let's see those blueprints.\x7Hmmm... Looks like Sellbots constructed a factory with machinery for building Cogs.\x7Sounds very dangerous. Stay out until you have more Laff Points.\x7When you have more Laff Points, we have much more to learn about Sellbot HQ.\x7For now, nice work, here is your reward." },
    3255: {
        QUEST: '_toNpcName_ is investigating Sellbot Headquarters.\x7Go see if you can help._where_' },
    3256: {
        QUEST: '_toNpcName_ is investigating Sellbot Headquarters.\x7Go see if you can help._where_' },
    3257: {
        QUEST: '_toNpcName_ is investigating Sellbot Headquarters.\x7Go see if you can help._where_' },
    3258: {
        QUEST: 'There is much confusion about what the Cogs are up to in their new headquarters.\x7I need you to bring back some information directly from them.\x7If we can get four internal memos from Sellbots inside their HQ, that will clear things up.\x7Bring back your first memo to me so we can learn more.' },
    3259: {
        QUEST: 'Great! This let\'s see what the memo says....\x7"Attn Sellbots:"\x7"I\'ll be in my office at the top of Sellbot Towers promoting Cogs to higher levels."\x7"When you earn enough merits enter the elevator in the lobby to see me."\x7"Break time\'s over - back to work!"\x7"Signed, Sellbot VP"\x7Aha.... Flippy will want to see this. I\'ll send it to him right now.\x7Please go get your second memo and bring it back.' },
    3260: {
        QUEST: 'Oh good, you\'re back. Let\'s see what you found....\x7"Attn Sellbots:"\x7"Sellbot Towers has installed a new security system to keep all Toons out."\x7"Toons caught in Sellbot Towers will be detained for questioning."\x7"Please meet in the lobby for appetizers to discuss."\x7"Signed, Mingler"\x7Very interesting... I\'ll pass on this information immediately.\x7Please bring a third memo back.' },
    3261: {
        QUEST: 'Excellent job _avName_! What does the memo say?\x7"Attn Sellbots:"\x7"Toons have somehow found a way to infiltrate Sellbot Towers."\x7"I\'ll call you tonight during dinner to give you the details."\x7"Signed, Telemarketer"\x7Hmmm... I wonder how Toons are breaking in....\x7Please bring back one more memo and I think we\'ll have enough info for now.',
        COMPLETE: 'I knew you could do it! Ok, the memo says....\x7"Attn Sellbots:"\x7"I was having lunch with Mr. Hollywood yesterday."\x7"He reports that the VP is very busy these days."\x7"He will only be taking appointments from Cogs that deserve a promotion."\x7"Forgot to mention, Gladhander is golfing with me on Sunday."\x7"Signed, Name Dropper"\x7Well... _avName_, this has been very helpful.\x7Here is your reward.' },
    3262: {
        QUEST: "_toNpcName_ has some new information about the Sellbot HQ Factory.\x7Go see what he's got._where_" },
    3263: {
        GREETING: 'Hi buddy!',
        QUEST: 'I\'m Coach Zucchini, but you can just call me Coach Z.\x7I put the "squash" in squash and stretch, if you know what I mean.\x7Listen, Sellbots have finished an enormous factory to pump out Sellbots 24 hours a day.\x7Get a group of Toon buddies together and squash the factory!\x7Inside Sellbot HQ, look for the tunnel to the Factory then board the Factory elevator.\x7Make sure you have full gags, full Laff Points, and some strong Toons as guides.\x7Defeat the Foreman inside the factory to slow the Sellbot progress.\x7Sounds like a real workout, if you know what I mean.',
        LEAVING: 'See ya buddy!',
        COMPLETE: 'Hey buddy, nice work on that Factory!\x7Looks like you found part of a Cog suit.\x7It must be left over from their Cog manufacturing process.\x7That may come in handy. Keep collecting these when you have spare time.\x7Maybe when you collect an entire Cog suit it could be useful for something....' },
    4001: {
        GREETING: '',
        QUEST: 'Now you get to choose the next gag track you want to learn.\x7Take your time deciding, and come back here where you are ready to choose.',
        INCOMPLETE_PROGRESS: 'Think about your decision before choosing.',
        INCOMPLETE_WRONG_NPC: 'Think about your decision before choosing.',
        COMPLETE: 'A wise decision...',
        LEAVING: QuestsDefaultLeaving },
    4002: {
        GREETING: '',
        QUEST: 'Now you get to choose the next gag track you want to learn.\x7Take your time deciding, and come back here where you are ready to choose.',
        INCOMPLETE_PROGRESS: 'Think about your decision before choosing.',
        INCOMPLETE_WRONG_NPC: 'Think about your decision before choosing.',
        COMPLETE: 'A wise decision...',
        LEAVING: QuestsDefaultLeaving },
    4200: {
        QUEST: "I bet Tom could use some help with some research he's doing._where_" },
    4201: {
        GREETING: 'Howdy!',
        QUEST: "I'm very concerned about a rash of musical instrument theft.\x7I'm conducting a survey among my fellow merchants.\x7Perhaps I can find a pattern to help me crack this case.\x7Stop by and ask Tina for a concertina inventory._where_" },
    4202: {
        QUEST: 'Yes, I talked to Tom this morning.\x7I have the inventory right here.\x7Bring it right back to him, ok?_where_' },
    4203: {
        QUEST: "Great! One down...\x7Now swing by and get Yuki's._where_" },
    4204: {
        QUEST: 'Oh! The inventory!\x7I forgot all about it.\x7I bet I can have it done by the time you defeat 10 Cogs.\x7Stop in after that and I promise it will be ready.',
        INCOMPLETE_PROGRESS: '31, 32... DOH!\x7You made me lose count!',
        GREETING: '' },
    4205: {
        QUEST: 'Ah, there you are.\x7Thanks for giving me some time.\x7Take this to Tom and tell him I said Hello._where_' },
    4206: {
        QUEST: "Hmmm, very interesting.\x7Now we are getting somewhere.\x7Ok, the last inventory is Fifi's._where_" },
    4207: {
        QUEST: "Inventory?\x7How can I do an inventory if I don't have the form?\x7Go see Cleff and see if he has one for me._where_",
        INCOMPLETE_PROGRESS: 'Any sign of that form yet?' },
    4208: {
        QUEST: "Sure I got an inventory form, mon!\x7But dey ain't free, you know.\x7I'll tell you woht. I trade you for a whole cream pie.",
        GREETING: 'Hey, mon!',
        LEAVING: 'Cool runnings...',
        INCOMPLETE_PROGRESS: "A slice won't do.\x7I be hungry, mon. I need de WHOLE pie." },
    4209: {
        GREETING: '',
        QUEST: 'Mmmm...\x7Dem mighty nice!\x7Here be your form for Fifi._where_' },
    4210: {
        GREETING: '',
        QUEST: "Thank you. That's a big help.\x7Let's see...Fiddles: 2\x7All done! Here you go!",
        COMPLETE: "Great work, _avName_.\x7I'm sure I'll get to the bottom of these thefts now.\x7Why don't you get to the bottom of this!" },
    4211: {
        QUEST: 'Say, Dr. Fret keeps calling every five minutes. Can you go see what his problem is?_where_' },
    4212: {
        QUEST: "Whew! I'm glad Toon HQ finally sent somebody.\x7I haven't had a customer in days.\x7It's these darned Number Crunchers every where.\x7I think they are teaching our residents bad oral hygiene.\x7Defeat ten of them and let's see if business picks up.",
        INCOMPLETE_PROGRESS: 'Still no customers. But keep it up!' },
    4213: {
        QUEST: "You know maybe it wasn't the Number Crunchers after all.\x7Maybe it's just the Cashbots in general.\x7Take out twenty of them and hopefully someone will come in for at least a checkup.",
        INCOMPLETE_PROGRESS: "I know twenty is a lot. But I'm sure it's going to pay off in spades." },
    4214: {
        GREETING: '',
        LEAVING: '',
        QUEST: "I just don't understand it!\x7Still not a SINGLE customer.\x7Maybe we need to go to the source.\x7Try reclaiming a Cashbot Cog building.\x7That Should do the trick...",
        INCOMPLETE_PROGRESS: 'Oh, please! Just one little building...',
        COMPLETE: "Still not a soul in here.\x7But you know, come to think of it.\x7I didn't have any customers before the Cogs invaded either!\x7I really appreciate all your help though.\x7This should help you get around." },
    4215: {
        QUEST: "Anna desperately needs someone to help her.\x7Why don't you drop in and see what you can do._where_" },
    4216: {
        QUEST: "Thanks for coming so quickly!\x7Seems like the Cogs have made off with several of my customers' cruise tickets.\x7Yuki said she saw a Glad Hander leaving here with his glad hands full of them.\x7See if you can get Lumber Jack's ticket to Alaska back.",
        INCOMPLETE_PROGRESS: 'Those Glad Handers could be anywhere now...' },
    4217: {
        QUEST: "Oh, great. You found it!\x7Now be a trooper and run in by Jack's for me, would you?_where_" },
    4218: {
        QUEST: "Great Googely Moogely!\x7Alaska here I come!\x7I can't take these infernal Cogs anymore.\x7Say, I think Anna needs you again._where_" },
    4219: {
        QUEST: "Yup, you guessed it.\x7I need you to shake down those pesky Glad Handers for Tabitha's ticket to Jazzfest.\x7You know the procedure...",
        INCOMPLETE_PROGRESS: "There's more out there somewhere..." },
    4220: {
        QUEST: 'Sweet!\x7Could you swing this one by his place for me too?_where_' },
    4221: {
        GREETING: '',
        LEAVING: 'Be cool...',
        QUEST: "Cool, daddio!\x7Now I'm in fat city, _avName_.\x7Before you split, you better go check out Anna Banana again..._where_" },
    4222: {
        QUEST: "This is the last one, I promise!\x7Now you are looking for Barry's ticket to the big singing contest.",
        INCOMPLETE_PROGRESS: "C'mon, _avName_.\x7Barry is counting on you." },
    4223: {
        QUEST: "This should put a smile on Barry's face._where_" },
    4224: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Hello, Hello, HELLO!\x7Terrific!\x7I just know me and the boys are going to clean up this year.\x7Anna says to swing back by and get your reward._where_\x7Goodbye, Goodbye, GOODBYE!',
        COMPLETE: 'Thanks for all your help, _avName_.\x7You really are an asset here in Toontown.\x7Speaking of assets...' },
    902: {
        QUEST: 'Go see Leo.\x7He needs someone to deliver a message for him._where_' },
    4903: {
        QUEST: 'Dude!\x7My castanets are all cloudy and I have a big show tonight.\x7Take them to Carlos and see if he can polish them up._where_' },
    4904: {
        QUEST: 'Jes, I tink I can polish dees.\x7But I need soma de blue ink from de squid.',
        GREETING: 'Hola!',
        LEAVING: 'Adios!',
        INCOMPLETE_PROGRESS: "Juo can find de squid wherever dere's a fishing pier" },
    4905: {
        QUEST: "Jes! Dat's it!\x7Now I need a leetle time to polish dees.\x7Why don juo go takeover a one story beelding while I work?",
        GREETING: 'Hola!',
        LEAVING: 'Adios!',
        INCOMPLETE_PROGRESS: 'Jest anodder minute...' },
    4906: {
        QUEST: 'Bery good!\x7Here are de castanets for Leo._where_' },
    4907: {
        GREETING: '',
        QUEST: "Cool, dude!\x7They look awesome!\x7Now I need you to get a copy of the lyrics to 'A Beat Christmas' from Hedy._where_" },
    4908: {
        QUEST: "Hello there!\x7Hmmm, I don't have a copy of that song handy.\x7If you give me a little while I could transcribe it from memory.\x7Why don't you run along and reclaim a two story building while I write?" },
    4909: {
        QUEST: "I'm sorry.\x7My memory is getting a little fuzzy.\x7If you go reclaim a three story building I'm sure I'll be done when you get back..." },
    4910: {
        QUEST: 'All done!\x7Sorry it took so long.\x7Take this back to Leo._where_',
        GREETING: '',
        COMPLETE: 'Awesome, dude!\x7My concert is gonna rock!\x7Speaking of rock, you can rock some Cogs with this...' },
    5247: {
        QUEST: 'This neighborhood is pretty tough...\x7You might want to learn some new tricks.\x7_toNpcName_ taught me everything I know, so maybe he can help you too._where_' },
    5248: {
        GREETING: 'Ahh, yes.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'You appear to be struggling with my assignment.',
        QUEST: 'Ahh, so welcome, new apprentice.\x7I know all there is to know about the pie game.\x7But before we can begin your training, a small demonstration is necessary.\x7Go out and defeat ten of the largest Cogs.' },
    5249: {
        GREETING: 'Mmmmm.',
        QUEST: 'Excellent!\x7Now demonstrate your skill as a fisherman.\x7I dropped three fuzzy dice in the pond yesterday.\x7Fish them out and bring them to me.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'It seems you may not be so clever with the rod and reel.' },
    5250: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Aha!  These dice will look great hanging from the rearview mirror of my ox cart!\x7Now, show me that you can tell your enemies from one another.\x7Return when you have restored two of the tallest Lawbot buildings.',
        INCOMPLETE_PROGRESS: 'Do the buildings give you trouble?' },
    5258: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Aha!  These dice will look great hanging from the rearview mirror of my ox cart!\x7Now, show me that you can tell your enemies from one another.\x7Return when you have restored two of the tallest Bossbot buildings.',
        INCOMPLETE_PROGRESS: 'Do the buildings give you trouble?' },
    5259: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Aha!  These dice will look great hanging from the rearview mirror of my ox cart!\x7Now, show me that you can tell your enemies from one another.\x7Return when you have restored two of the tallest Cashbot buildings.',
        INCOMPLETE_PROGRESS: 'Do the buildings give you trouble?' },
    5260: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Aha!  These dice will look great hanging from the rearview mirror of my ox cart!\x7Now, show me that you can tell your enemies from one another.\x7Return when you have restored two of the tallest Sellbot buildings.',
        INCOMPLETE_PROGRESS: 'Do the buildings give you trouble?' },
    5200: {
        QUEST: 'Those sneaky Cogs are at it again.\x7_toNpcName_ has reported another missing item. Stop by and see if you can straighten it out._where_' },
    5201: {
        GREETING: '',
        QUEST: 'Hi, _avName_.  I reckon I should thank you for coming.\x7A group of those Head Hunters came in and stole my soccer ball.\x7The leader told me that I had to make some cutbacks and just grabbed it away from me!\x7Can you get my ball back?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Any luck finding my soccer ball?',
        COMPLETE: 'Yeehaw!  You found it!. Here, take your reward...' },
    5261: {
        GREETING: '',
        QUEST: 'Hi, _avName_.  I reckon I should thank you for coming.\x7A group of those Two-Faces came in and stole my soccer ball.\x7The leader told me that I had to make some cutbacks and just grabbed it away from me!\x7Can you get my ball back?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Any luck finding my soccer ball?',
        COMPLETE: 'Yeehaw!  You found it!. Here, take your reward...' },
    5262: {
        GREETING: '',
        QUEST: 'Hi, _avName_.  I reckon I should thank you for coming.\x7A group of those Money Bags came in and stole my soccer ball.\x7The leader told me that I had to make some cutbacks and just grabbed it away from me!\x7Can you get my ball back?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Any luck finding my soccer ball?',
        COMPLETE: 'Yeehaw!  You found it!. Here, take your reward...' },
    5263: {
        GREETING: '',
        QUEST: 'Hi, _avName_.  I reckon I should thank you for coming.\x7A group of those Spin Doctors came in and stole my soccer ball.\x7The leader told me that I had to make some cutbacks and just grabbed it away from me!\x7Can you get my ball back?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Any luck finding my soccer ball?',
        COMPLETE: 'Yeehaw!  You found it!. Here, take your reward...' },
    5202: {
        QUEST: lTheBrrrgh + " has been overrun with some of the toughest Cogs we've seen yet.\x7You will probably want to carry more gags around here.\x7I hear _toNpcName_ may have a large bag you can use to carry more gags._where_" },
    5203: {
        GREETING: 'Huh?  Are you on my sledding team?',
        QUEST: "What's that?  You want a bag?\x7I had one somewhere around here... maybe it's in my toboggan?\x7Only... I haven't seen my toboggan since the big race!\x7Maybe one of those Cogs took it?",
        LEAVING: 'Have you seen my toboggan?',
        INCOMPLETE_PROGRESS: "Who are you again?  Sorry, I'm a little woozy from the crash." },
    5204: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Is that my toboggan?  I don't see any bag here.\x7I think Bumpy Noggin was on the team... maybe he has it?_where_" },
    5205: {
        GREETING: 'Ohhh, my head!',
        LEAVING: '',
        QUEST: "Huh?  Ted who?  A bag?\x7Oh, maybe he was on our toboggan team?\x7My head hurts so much I can't think straight.\x7Could you fish me out some ice cubes from the frozen pond for my head?",
        INCOMPLETE_PROGRESS: "Oww, my head's killing me!  Got any ice?" },
    5206: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Ahhh, that feels much better!\x7So you're looking for Ted's bag, huh?\x7I think it ended up on Sam Simian's head after the crash._where_" },
    5207: {
        GREETING: 'Eeeep!',
        LEAVING: '',
        QUEST: 'What is bag?  Who is Bompy?\x7Me scared of buildings!  You beat buildings, I give you bag!',
        INCOMPLETE_PROGRESS: 'More buildings!  Me still scared!',
        COMPLETE: 'Ooooh!  Me like you!' },
    5208: {
        GREETING: '',
        LEAVING: 'Eeeek!',
        QUEST: 'Ooooh!  Me like you!\x7Go to Ski Clinic. Bag there.' },
    5209: {
        GREETING: 'Dude!',
        LEAVING: 'Later!',
        QUEST: "Man, that Simian Sam is crazy!\x7If you're wild like Sam, I'll give you your bag, man.\x7Go bag some Cogs for your bag, man! Hey now!",
        INCOMPLETE_PROGRESS: "Are you sure you're extreme enough?  Go bag some more Cogs.",
        COMPLETE: "Hey, you are pretty wild!  That was a heap of Cogs you bagged!\x7Here's your bag!" },
    5210: {
        QUEST: '_toNpcName_ is secretly in love with someone in the neighborhood.\x7If you help her, she may reward you handsomely._where_' },
    5211: {
        GREETING: 'Boo hoo.',
        QUEST: 'I spent all last night writing a letter to the dog I love.\x7But before I could deliver it, one of those nasty Cogs with a beak came in and took it.\x7Can you get it back for me?',
        LEAVING: 'Boo hoo.',
        INCOMPLETE_PROGRESS: 'Please find my letter.' },
    5264: {
        GREETING: 'Boo hoo.',
        QUEST: 'I spent all last night writing a letter to the dog I love.\x7But before I could deliver it, one of those nasty Cogs with a fin came in and took it.\x7Can you get it back for me?',
        LEAVING: 'Boo hoo.',
        INCOMPLETE_PROGRESS: 'Please find my letter.' },
    5265: {
        GREETING: 'Boo hoo.',
        QUEST: 'I spent all last night writing a letter to the dog I love.\x7But before I could deliver it, one of those nasty Mingler Cogs came in and took it.\x7Can you get it back for me?',
        LEAVING: 'Boo hoo.',
        INCOMPLETE_PROGRESS: 'Please find my letter.' },
    5266: {
        GREETING: 'Boo hoo.',
        QUEST: 'I spent all last night writing a letter to the dog I love.\x7But before I could deliver it, one of those nasty Corporate Raiders came in and took it.\x7Can you get it back for me?',
        LEAVING: 'Boo hoo.',
        INCOMPLETE_PROGRESS: 'Please find my letter.' },
    5212: {
        QUEST: 'Oh, thank you for finding my letter!\x7Please, please, please could you deliver it to the most handsome dog in the neighborhood?',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "You didn't deliver my letter, did you?" },
    5213: {
        GREETING: "Charmed, I'm sure.",
        QUEST: "I can't be bothered with your letter, you see.\x7All my doggies have been taken from me!\x7If you bring them back, maybe we can talk then.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'My poor little doggies!' },
    5214: {
        GREETING: '',
        LEAVING: 'Toodleloo!',
        QUEST: "Thank you for bringing back my little beauties.\x7Let's take a look at your letter now...\nMmmm, it seems I have yet another secret admirer.\x7This calls for a trip to my dear friend Carl.\x7I'm sure you'll like him immensely._where_" },
    5215: {
        GREETING: 'Heh, heh...',
        LEAVING: 'Come back, yes, yes.',
        INCOMPLETE_PROGRESS: "There are still some big ones around.  Comes back to us when they're gone.",
        QUEST: "Who sent you to us?  We don't like Snootsies much, we don't...\x7But we likes Cogs even less...\x7Run the big ones off and we'll helps you we will." },
    5216: {
        QUEST: 'We told you we would helps you.\x7So take this ring to the girl.',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'You still haves the ring???',
        COMPLETE: 'Oh darrrling!!! Thank you!!!\x7Oh, and I have something special for you as well.' },
    5217: {
        QUEST: 'It sounds like _toNpcName_ could use some help._where_' },
    5218: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I'm sure there are more Minglers around somewhere.",
        QUEST: "Help!!! Help!!! I can't take it anymore!\x7Those Minglers are driving me batty!!!" },
    5219: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "That can't be all of them.  I just saw one!!!",
        QUEST: "Oh, thanks, but now it's the Corporate Raiders!!!\x7You've got to help me!!!" },
    5220: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No, no, no there was one just here!',
        QUEST: "I realize now that it's those Loan Sharks!!!\x7I thought you were going to save me!!!" },
    5221: {
        GREETING: '',
        LEAVING: '',
        QUEST: "You know what, maybe it isn't the Cogs at all!\x7Could you ask Fanny to make me a soothing potion?  Maybe that would help...._where_" },
    5222: {
        LEAVING: '',
        QUEST: "Oh, that Harry, he sure is a card!\x7I'll whip up something that will fix him right up!\x7Oh, I appear to be out of sardine whiskers...\x7Be a dear and run down to the pond and catch some for me.",
        INCOMPLETE_PROGRESS: 'Got those whiskers for me yet?' },
    5223: {
        QUEST: 'Okay.  Thanks, hon.\x7Here, now take this to Harry.  It should calm him right down.',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Go on now, take the potion to Harry.' },
    5224: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Go get those Legal Eagles for me, will you?',
        QUEST: "Oh thank goodness you're back!\x7Give me the potion, quick!!!\x7Glug, glug, glug...\x7That tasted awful!\x7You know, what, though?  I feel much calmer.  Now that I can think clearly, I realize that...\x7It was the Legal Eagles that were driving me crazy all this time!!!",
        COMPLETE: "Oh boy!  Now I can relax!\x7I'm sure there's something here I can give you.  Oh, take this!" },
    5225: {
        QUEST: 'Ever since the incident with the turnip bread, Grumpy Phil has been mad at _toNpcName_.\x7Maybe you could help Gus fix things between them?_where_' },
    5226: {
        QUEST: 'Yeah, you probably heard Grumpy Phil is mad at me...\x7I was just trying to be nice with that turnip bread.\x7Maybe you can help cheer him up.\x7Phil really hates those Cashbot Cogs, especially their buildings.\x7If you reclaim some Cashbot buildings, it might help.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Maybe a few more buildings?' },
    5227: {
        QUEST: "That's terrific!  Go tell Phil what you've done._where_" },
    5228: {
        QUEST: 'Oh he did, did he?\x7That Gus thinks he can get off so easy, does he?\x7Only broke my tooth, he did, with that turnip bread of his!\x7Maybe if you took my tooth to Dr. Mumbleface for me he could fix it.',
        GREETING: 'Mmmmrrphh.',
        LEAVING: 'Grumble, grumble.',
        INCOMPLETE_PROGRESS: 'You again?  I thought you were going to get my tooth fixed for me.' },
    5229: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I'm still working on the tooth.  It will be a bit longer.",
        QUEST: "Yes, that tooth looks pretty bad, alrighty.\x7Maybe I can do something, but it will be a little while.\x7Maybe you could clear some of those Cashbot Cogs off the streets while you're waiting?\x7They're scaring off my customers." },
    5267: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I'm still working on the tooth.  It will be a bit longer.",
        QUEST: "Yes, that tooth looks pretty bad, alrighty.\x7Maybe I can do something, but it will be a little while.\x7Maybe you could clear some of those Sellbot Cogs off the streets while you're waiting?\x7They're scaring off my customers." },
    5268: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I'm still working on the tooth.  It will be a bit longer.",
        QUEST: "Yes, that tooth looks pretty bad, alrighty.\x7Maybe I can do something, but it will be a little while.\x7Maybe you could clear some of those Lawbot Cogs off the streets while you're waiting?\x7They're scaring off my customers." },
    5269: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I'm still working on the tooth.  It will be a bit longer.",
        QUEST: "Yes, that tooth looks pretty bad, alrighty.\x7Maybe I can do something, but it will be a little while.\x7Maybe you could clear some of those Bossbot Cogs off the streets while you're waiting?\x7They're scaring off my customers." },
    5230: {
        GREETING: '',
        QUEST: "I'm glad you're back!\x7I gave up trying to fix that old tooth, and made a new gold tooth for Phil instead.\x7Unfortunately a Robber Baron came in and took it from me.\x7Maybe you can catch him if you hurry.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Did you find that tooth yet?' },
    5270: {
        GREETING: '',
        QUEST: "I'm glad you're back!\x7I gave up trying to fix that old tooth, and made a new gold tooth for Phil instead.\x7Unfortunately a Big Cheese came in and took it from me.\x7Maybe you can catch him if you hurry.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Did you find that tooth yet?' },
    5271: {
        GREETING: '',
        QUEST: "I'm glad you're back!\x7I gave up trying to fix that old tooth, and made a new gold tooth for Phil instead.\x7Unfortunately Mr. Hollywood came in and took it from me.\x7Maybe you can catch him if you hurry.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Did you find that tooth yet?' },
    5272: {
        GREETING: '',
        QUEST: "I'm glad you're back!\x7I gave up trying to fix that old tooth, and made a new gold tooth for Phil instead.\x7Unfortunately a Big Wig came in and took it from me.\x7Maybe you can catch him if you hurry.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Did you find that tooth yet?' },
    5231: {
        QUEST: "Great, that's the tooth alrighty!\x7Why don't you just run it over to Phil for me?",
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'I bet Phil would like to see his new tooth.' },
    5232: {
        QUEST: "Oh, thanks.\x7Mmmrrrphhhh\x7How's that look, huh?\x7Okay, you can tell Gus that I forgive him.",
        LEAVING: '',
        GREETING: '' },
    5233: {
        QUEST: "Oh, that's great to hear.\x7I figured old Phil couldn't stay mad at me.\x7As a gesture of goodwill, I baked him this Pine cone bread.\x7Could you run it over to him for me?",
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Better hurry.  Pine cone bread is better when it's hot.",
        COMPLETE: "Oh, what's this?  For me?\x7Munch, munch...\x7Owwww!  My tooth!  That Gus Gooseburger!\x7Oh well, it wasn't your fault.  Here, you can have this for your trouble." },
    903: {
        QUEST: 'You may be ready to see _toNpcName_ the Blizzard Wizard for your final test._where_' },
    5234: {
        GREETING: '',
        QUEST: 'Aha, you are back.\x7Before we begin, we must eat.\x7Bring us some lumpy cheese for our broth.\x7Lumpy cheese can only be gathered from Big Cheese Cogs.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'We still need lumpy cheese' },
    5278: {
        GREETING: '',
        QUEST: 'Aha, you are back.\x7Before we begin, we must eat.\x7Bring us some caviar for our broth.\x7Caviar can only be gathered from Mr. Hollywood Cogs.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'We still need caviar' },
    5235: {
        GREETING: '',
        QUEST: 'A simple man eats with a simple spoon.\x7A Cog took my simple spoon, so I simply can not eat.\x7Return my spoon to me.  I think a Robber Baron took it.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'I simply must have my spoon.' },
    5279: {
        GREETING: '',
        QUEST: 'A simple man eats with a simple spoon.\x7A Cog took my simple spoon, so I can not eat.\x7Return my spoon to me.  I think a Big Wig took it.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'I simply must have my spoon.' },
    5236: {
        GREETING: '',
        QUEST: 'Many thanks.\x7Slurp, slurp...\x7Ahhh, now you must catch a talking toad.  Try fishing in the pond.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Where is that talking toad?' },
    5237: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'You have not yet obtained dessert.',
        QUEST: "Oh, that is certainly a talking toad.  Give him to me.\x7What's that you say, toad?\x7Uh huh.\x7Uh huh...\x7The toad has spoken.  We need dessert.\x7Bring us some ice cream cones from _toNpcName_.\x7The toad likes red bean flavored ice cream for some reason._where_" },
    5238: {
        GREETING: '',
        QUEST: "So the wizard sent you.  I'm sad to say we're fresh out of red bean ice cream cones.\x7You see, a bunch of Cogs came in and just took them.\x7They said they were for Mr. Hollywood, or some such nonsense.\x7I'd sure appreciate if you could round them back up for me.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Have you found all my ice cream cones yet?' },
    5280: {
        GREETING: '',
        QUEST: "So the wizard sent you.  I'm sad to say we're fresh out of red bean ice cream cones.\x7You see, a bunch of Cogs came in and just took them.\x7They said they were for The Big Cheese, or some such nonsense.\x7I'd sure appreciate if you could round them back up for me.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Have you found all my ice cream cones yet?' },
    5239: {
        QUEST: "Thanks for bringing back my ice cream cones!\x7Here's one for Lil Oldman.",
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'You better bring that ice cream to Lil Oldman before it melts.' },
    5240: {
        GREETING: '',
        QUEST: 'Very good.  Here you go toad...\x7Slurp, slurp...\x7Okay, now we are almost ready.\x7If you can just bring me some powder to dry my hands.\x7I think those Big Wig Cogs sometimes have powder from their wigs.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Did you find any powder?' },
    5281: {
        GREETING: '',
        QUEST: 'Very good.  Here you go toad...\x7Slurp, slurp...\x7Okay, now we are almost ready.\x7If you can just bring me some powder to dry my hands.\x7I think those Mr. Hollywood Cogs sometimes keep powder for their noses.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Did you find any powder?' },
    5241: {
        QUEST: 'Okay.\x7As I once said, to truly throw a pie, you must throw not with the hand...\x7...but with the soul.\x7I know not what that means, so I will sit and contemplate while you restore buildings.\x7Return when you have completed your task.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Your task is not yet complete.' },
    5242: {
        GREETING: '',
        QUEST: 'Although I still know not what I am talking about, you truly are worthy.\x7I give you a final task...\x7The talking toad would like a girlfriend.\x7Find another talking toad.  The toad has spoken.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Where is that other talking toad?',
        COMPLETE: 'Whew!  I am tired from all this effort.  I must rest now.\x7Here, take your reward and be off.' },
    5243: {
        QUEST: 'Sweaty Pete is starting to stink up the street.\x7Can you talk him into taking a shower or something?_where_' },
    5244: {
        GREETING: '',
        QUEST: "Yeah, I guess I do work up quite a sweat in here.\x7Mmmm, maybe if I could fix that leaky pipe in my shower...\x7I figure a gear from one of those tiny Cogs would do the trick.\x7Go find a gear from a Micromanager and we'll try it.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Where's that gear you were going to get?" },
    5245: {
        GREETING: '',
        QUEST: 'Yup, that seemed to do the trick.\x7But I get lonely when I shower...\x7Could you go fish me up a rubber ducky to keep me company?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Any luck with that duck?' },
    5246: {
        QUEST: "The ducky's great, but...\x7All those buildings around here make me nervous.\x7I'd feel a lot more relaxed if there were fewer buildings around.",
        LEAVING: '',
        COMPLETE: "Okay, I'll shower up now.  And here's something for you too.",
        INCOMPLETE_PROGRESS: "I'm still worried about buildings." },
    5251: {
        QUEST: 'Lounge Lassard is supposed to be playing a gig tonight.\x7I hear he might be having some trouble with his equipment._where_' },
    5252: {
        GREETING: '',
        QUEST: 'Oh yeah!  I could sure use some help.\x7Those Cogs came in and swiped all my gear while I was unloading the van.\x7Can you give me a hand and get back my microphone?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Hey man, I can't sing without my microphone." },
    5253: {
        GREETING: '',
        QUEST: "Yeah, that's my microphone all right.\x7Thanks for getting it for me, but...\x7I really need my keyboard so I can tickle the ivories.\x7I think one of those Corporate Raiders got my keyboard.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No luck finding my keboard?' },
    5273: {
        GREETING: '',
        QUEST: "Yeah, that's my microphone all right.\x7Thanks for getting it for me, but...\x7I really need my keyboard so I can tickle the ivories.\x7I think one of those Minglers got my keyboard.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No luck finding my keboard?' },
    5274: {
        GREETING: '',
        QUEST: "Yeah, that's my microphone all right.\x7Thanks for getting it for me, but...\x7I really need my keyboard so I can tickle the ivories.\x7I think one of those Loan Sharks got my keyboard.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No luck finding my keboard?' },
    5275: {
        GREETING: '',
        QUEST: "Yeah, that's my microphone all right.\x7Thanks for getting it for me, but...\x7I really need my keyboard so I can tickle the ivories.\x7I think one of those Legal Eagles got my keyboard.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No luck finding my keboard?' },
    5254: {
        GREETING: '',
        QUEST: "All right!  Now I'm in business.\x7If only they hadn't taken my platform shoes...\x7Those shoes probably ended up with a Mr. Hollywood, if I had to guess.",
        LEAVING: '',
        COMPLETE: "Allright!!  I'm ready now.\x7Hello Brrrgh!!!\x7Huh?  Where is everyone?\x7Okay, take this and round me up some fans, huh?",
        INCOMPLETE_PROGRESS: "I can't perform barefoot, can I?" },
    5282: {
        GREETING: '',
        QUEST: "All right!  Now I'm in business.\x7If only they hadn't taken my platform shoes...\x7Those shoes probably ended up with a Big Cheese, if I had to guess.",
        LEAVING: '',
        COMPLETE: "Allright!!  I'm ready now.\x7Hello Brrrgh!!!\x7Huh?  Where is everyone?\x7Okay, take this and round me up some fans, huh?",
        INCOMPLETE_PROGRESS: "I can't perform barefoot, can I?" },
    5283: {
        GREETING: '',
        QUEST: "All right!  Now I'm in business.\x7If only they hadn't taken my platform shoes...\x7Those shoes probably ended up with a Robber Baron, if I had to guess.",
        LEAVING: '',
        COMPLETE: "Allright!!  I'm ready now.\x7Hello Brrrgh!!!\x7Huh?  Where is everyone?\x7Okay, take this and round me up some fans, huh?",
        INCOMPLETE_PROGRESS: "I can't perform barefoot, can I?" },
    5284: {
        GREETING: '',
        QUEST: "All right!  Now I'm in business.\x7If only they hadn't taken my platform shoes...\x7Those shoes probably ended up with a Big Wig, if I had to guess.",
        LEAVING: '',
        COMPLETE: "Allright!!  I'm ready now.\x7Hello Brrrgh!!!\x7Huh?  Where is everyone?\x7Okay, take this and round me up some fans, huh?",
        INCOMPLETE_PROGRESS: "I can't perform barefoot, can I?" },
    5255: {
        QUEST: 'You look like you could use more laugh points.\x7Maybe _toNpcName_ will cut you a deal.\x7Make sure you get it in writing..._where_' },
    5256: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "A deal's a deal.",
        QUEST: "So you're looking for laff points, huh?\x7Have I got a deal for you!\x7Simply take care of a few Bossbot Cogs for me...\x7And I'll make it worth your while." },
    5276: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "A deal's a deal.",
        QUEST: "So you're looking for laff points, huh?\x7Have I got a deal for you!\x7Simply take care of a few Lawbot Cogs for me...\x7And I'll make it worth your while." },
    5257: {
        GREETING: '',
        LEAVING: '',
        COMPLETE: "Okay, but I'm certain I told you to round up some Lawbot Cogs.\x7Well, if you say so, but you owe me one.",
        INCOMPLETE_PROGRESS: "I don't think you're done yet.",
        QUEST: "You say you're done?  Defeated all the Cogs?\x7You must have misunderstood, our deal was for Sellbot Cogs.\x7I'm sure I told you to defeat some Sellbot Cogs for me." },
    5277: {
        GREETING: '',
        LEAVING: '',
        COMPLETE: "Okay, but I'm certain I told you to round up some Lawbot Cogs.\x7Well, if you say so, but you owe me one.",
        INCOMPLETE_PROGRESS: "I don't think you're done yet.",
        QUEST: "You say you're done?  Defeated all the Cogs?\x7You must have misunderstood, our deal was for Cashbot Cogs.\x7I'm sure I told you to defeat some Cashbot Cogs for me." },
    6201: {
        QUEST: 'Powers Erge needs some help. Could you drop by and lend her a hand?_where_' },
    6202: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Oh, a customer! Great! What can I do for you?\x7What do you mean, what can you do for me? OH! You're not a customer.\x7I remember now. You're here to help with those dreadful Cogs.\x7Well I could certainly use the help even if you're not a customer.\x7If you clean up the streets a bit, I'll have a little something for you.",
        INCOMPLETE_PROGRESS: "If you don't want electricity, I can't help you until you defeat those Cogs.",
        COMPLETE: "Good job on those Cogs, _avName_.\x7Now, are you sure I can't interest you in some electricity? Might come in handy....\x7No? OK, suit yourself.\x7Hunh? Oh yeah, I remember. Here ya go. This is sure to help with those nasty Cogs.\x7Keep up the good work!" },
    6206: {
        QUEST: "Well, _avName_, I don't have anything for you right now.\x7Wait! I think Susan Siesta was looking for help. Why don't you go see her?_where_" },
    6207: {
        GREETING: '',
        LEAVING: '',
        QUEST: "I'll never get rich with those darn Cogs driving away all my business!\x7You've got to help me, _avName_.\x7Clear out a few Cog buildings for the sake of the neighborhood and I'll add to your riches.",
        INCOMPLETE_PROGRESS: "Poor me! Can't you get rid of those buildings?",
        COMPLETE: "Now I'll be in the money! I can see it now!\x7I'll spend all my time fishing. Now, let me enrich your life a little.\x7There you go!" },
    6211: {
        QUEST: 'Hey _avName_! I heard Lawful Linda was looking for you.\x7You should stop by and pay her a visit._where_' },
    6212: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Hi there! Wow, am I glad to see you!\x7I've been working on this answering machine in my spare time but I'm short a couple of parts.\x7I need three more rods and the ones from Bean Counters seem to work pretty well.\x7Could you see if you could find some rods for me?",
        INCOMPLETE_PROGRESS: 'Still trying to find those rods?' },
    6213: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Oh, those will do nicely.\x7That's funny. I was sure I had a spare drive belt around here but I can't find it.\x7Could you please get one from a Money Bags for me? Thanks!",
        INCOMPLETE: "Well, I can't help you until I get that drive belt." },
    6214: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Ah, that's it. Now it should run like a charm.\x7Where'd my pliers go? I can't tighten this up without the pliers.\x7Maybe pincers from a Penny Pincher would do the job?\x7If you'd go find one, I could give you a little something to help you with those Cogs.",
        INCOMPLETE_PROGRESS: 'No pincers yet, hunh? Keep looking.',
        COMPLETE: "Great! Now I'll just tighten this up.\x7It seems to be working now. Back in business!\x7Well, except that we don't have a phone. But I'm glad for the help, anyway.\x7I think this'll help you out with those Cogs. Good luck!" },
    6221: {
        QUEST: 'I heard Rocco was looking for help. See what you can do for him._where_' },
    6222: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Yo! Youse came to da right place. I ain't too happy.\x7Yeah, I was lookin for some help wid dose Cogs. Dey always come and boss me around.\x7If you can retire some of dem Bossbots, I'll make it worth your while.",
        INCOMPLETE_PROGRESS: "Hey, _avName_, what's up wid youse?\x7You gotta keep after dem Bossbots. We got a deal, remember?\x7Rocco always keeps his word.",
        COMPLETE: "Yo, _avName_! Youse ok in my book.\x7Dem Bossbots ain't so bossy now, is they?\x7Here ya go! A nice big boost. Now, you stay outta trouble, ya hear!" },
    6231: {
        QUEST: 'Nat over on Pajama Place heard rumors about a Cashbot Headquarters.\x7Head over there and see if you can help him out._where_' },
    6232: {
        GREETING: '',
        LEAVING: '',
        QUEST: "I got a nibble about some strange goings on.\x7Well, maybe it's the fleas but something is going on anyway.\x7All these Cashbots!\x7I think they've opened another headquarters right off Pajama Place.\x7P.J. knows his way around.\x7Go see _toNpcName_ _where_ Ask him if he's heard anything.",
        INCOMPLETE_PROGRESS: "You haven't seen P.J. yet? What's keeping you?\x7Oh, these darn fleas!" },
    6233: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Hey there _avName_, where are you headed?\x7Cashbot Headquarters?? I haven't seen anything.\x7Could you go to the end of Pajama Place and see if it's true?\x7Find some Cashbot Cogs in their headquarters, defeat a few of them, and come tell me about it.",
        INCOMPLETE_PROGRESS: "Found the HQ yet? You'll need to defeat some Cashbots there to scope it out." },
    6234: {
        GREETING: '',
        LEAVING: '',
        QUEST: "What?! There really IS a Cashbot HQ?\x7You better go tell Nat right away!\x7Who would have guessed there'd be a Cog HQ right down the street from him?",
        INCOMPLETE_PROGRESS: "What did Nat have to say? You haven't seen him yet?" },
    6235: {
        GREETING: '',
        LEAVING: '',
        QUEST: "So, I'm itching to hear what P.J. had to say.\x7Hmm...we need more information about this Cog business but I've got to get rid of these fleas!\x7I know! YOU can go find out more!\x7Go defeat Cashbots at the HQ until you find some plans then come right back!",
        INCOMPLETE_PROGRESS: "No plans yet? Keep searching those Cogs!\x7They're bound to have some plans!",
        COMPLETE: "You got the plans?\x7Great! Let's see what they say.\x7I see... the Cashbots built a Mint to make Cogbucks.\x7It must be FULL of Cashbots. We should find out more about this.\x7Maybe if you had a disguise. Hmmm...wait! I think I've got part of a Cog suit here somewhere....\x7Here it is! Why don't you take this for your trouble? Thanks again for your help!" },
    6241: {
        QUEST: "The Countess has been looking everywhere for you! Please pay her a visit so she'll stop calling._where_" },
    6242: {
        GREETING: '',
        LEAVING: '',
        QUEST: "_avName_, I'm counting on you to help me!\x7You see, these Cogs are making so much noise that I simply can't concentrate.\x7I keep losing count of my sheep!\x7If you'll cut down on the noise, I'll help you out too! You can count on it!\x7Now, where was I? Right, one hundred thirty-six, one hundred thirty-seven....",
        INCOMPLETE_PROGRESS: "Four hundred forty-two...four hundred forty-three...\x7What? You're back already? But it's still so noisy!\x7Oh no, I've lost count again.\x7 One...two...three....",
        COMPLETE: "Five hundred ninety-three...five hundred ninety-four...\x7Hello? Oh, I knew I could count on you! It's much quieter now.\x7Here you go, for all those Number Crunchers.\x7Number? Now I need to start counting all over again! One...two...." },
    6251: {
        QUEST: "Poor Zari broke her zipper and now she can't make deliveries to her customers. She could sure use your help._where_" },
    6252: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Oh, hi _avName_. You're here to help with my deliveries?\x7That's terrific! This broken zipper makes it tough to zip around.\x7Let me see...ok, this should be easy. Cowboy George ordered a zither last week.\x7Could you please bring it over to him? _where_",
        INCOMPLETE_PROGRESS: 'Oh, hi! Did you forget something? Cowboy George is waiting for that zither.' },
    6253: {
        GREETING: '',
        LEAVING: '',
        QUEST: "My zither! At last! Gosh, I can't wait to play it.\x7Go tell Zari that I said thanks, would you?",
        INCOMPLETE_PROGRESS: "Thanks again for the zither. Doesn't Zari have more deliveries for you to do?" },
    6254: {
        GREETING: '',
        LEAVING: '',
        QUEST: "That was fast. What's next on my list?\x7Right. Master Mike ordered a Zamboni. That zany guy.\x7Could you bring this to him, please?_where_",
        INCOMPLETE_PROGRESS: 'That Zamboni needs to go to Master Mike._where_' },
    6255: {
        GREETING: '',
        LEAVING: '',
        QUEST: "All-right! The Zamboni I ordered!\x7Now, if only there weren't so many Cogs around, I might have some time to use it.\x7Be a sport and take care of a few of those Cashbots for me, would you?",
        INCOMPLETE_PROGRESS: 'Those Cashbots are tough, hunh? They make it hard to test my Zamboni.' },
    6256: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Excellent! Now I can go try out my Zamboni.\x7Tell Zari that I'll be in next week to place my next order, please.",
        INCOMPLETE_PROGRESS: "That's all I need for now. Isn't Zari waiting for you?" },
    6257: {
        GREETING: '',
        LEAVING: '',
        QUEST: "So, Master Mike was happy with his Zamboni? Great.\x7Who's next? Oh, Zen Glen ordered a zebra-striped zabuton.\x7Here it is! Could you zoom over to his place, please?_where_",
        INCOMPLETE_PROGRESS: 'I think Zen Glen needs that zabuton to meditate.' },
    6258: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Ah, my zabuton at last. Now I can meditate.\x7Who could focus with that racket going on? All those Cogs!\x7Since you're already here, maybe you could take care of some of these Cogs?\x7Then I could use my zabuton in peace.",
        INCOMPLETE_PROGRESS: 'Still so noisy with those Cogs! Who could focus?' },
    6259: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Peace and quiet at last. Thanks, _avName_.\x7Please tell Zari how happy I am. OM....',
        INCOMPLETE_PROGRESS: 'Zari called looking for you. You should go see what she needs.' },
    6260: {
        GREETING: '',
        LEAVING: '',
        QUEST: "I'm glad to hear that Zen Glen is happy with his zebra zabuton.\x7Oh, these zinnias just came in for Rose Petals.\x7Since you seem to have some zeal for deliveries, perhaps you could take them over to her?_where_",
        INCOMPLETE_PROGRESS: "Those zinnias will wilt if you don't deliver them soon." },
    6261: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'What lovely zinnias! Zari sure does deliver.\x7Oh, well, I guess YOU deliver, _avName_. Please thank Zari for me!',
        INCOMPLETE_PROGRESS: "Don't forget to thank Zari for the zinnias!" },
    6262: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Welcome back, _avName_. You're pretty zippy.\x7Let's see...what's next on my list to deliver? Zydeco records for Wyda Wake._where_",
        INCOMPLETE_PROGRESS: "I'm sure Wyda Wake is waiting for those Zydeco records." },
    6263: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Zydeco records? I don't remember asking for Zydeco records.\x7Oh, I bet Lullaby Lou ordered them._where_",
        INCOMPLETE_PROGRESS: 'No, those Zydeco records are for Lullaby Lou._where_' },
    6264: {
        GREETING: '',
        LEAVING: '',
        QUEST: "At last, my Zydeco records! I thought Zari had forgotten.\x7Could you please bring this zucchini to her? She'll find someone who wants one. Thanks!",
        INCOMPLETE_PROGRESS: "Oh, I've got plenty of zucchini already. Take that one to Zari." },
    6265: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Zucchini? Hmm. Well, someone will want it, I'm sure.\x7Ok, we're nearly done with my list. One more delivery to make.\x7Babyface MacDougal ordered a zoot suit._where_",
        INCOMPLETE_PROGRESS: "If you don't deliver that zoot suit to Babyface MacDougal,\x7 it'll get all wrinkled." },
    6266: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Once upon a time...oh! You're not here for a story, are you?\x7You're delivering my zoot suit? Great! Wow, that's something.\x7Hey, could you give Zari a message for me? I'll be needing zircon cufflinks to go with the suit. Thanks!",
        INCOMPLETE_PROGRESS: 'Did you give Zari my message?',
        COMPLETE: "Zircon cufflinks, hunh? Well, I'll see what I can do for him.\x7Anyway, you've been the very zenith of helpfulness and I can't let you leave with zilch.\x7Here's a BIG boost to help you zap those Cogs!" },
    6271: {
        QUEST: "Drowsy Dave is having some trouble that you might be able to help with. Why don't you stop by his shop?_where_" },
    6272: {
        GREETING: '',
        LEAVING: '',
        QUEST: "What? Huh? Oh, I must've fallen asleep.\x7You know, those Cogs buildings are full of machinery that makes me really sleepy.\x7I listen to them humming all day and...\x7Huh? Oh, yeah, right. If you could get rid of some of those Cog buildings, I could stay awake.",
        INCOMPLETE_PROGRESS: "Zzzzz...huh? Oh, it's you, _avName_.\x7Back already? I was just taking a little nap.\x7Come back when you're done with those buildings.",
        COMPLETE: "What? I dropped off to sleep for a minute there.\x7Now that those Cog buildings are gone I can finally relax.\x7Thanks for your help, _avName_.\x7See you later! I think maybe I'll take a little nap." },
    6281: {
        QUEST: "Head over and call on Teddy Blair. He's got a job for you._where_" },
    6282: {
        GREETING: '',
        LEAVING: '',
        QUEST: "What did you say? No, I don't have a fob for you.\x7Oh, a job! Why didn't you say so? You'll need to speak up.\x7Those Cogs make it hard to hibernate. If you'll help make Dreamland quieter,\x7I'll give you a little something.",
        INCOMPLETE_PROGRESS: "You beat the bogs? What bogs?\x7Oh, the Cogs! Why didn't you say so?\x7Hmm, it's still pretty loud. How 'bout you defeat a few more?",
        COMPLETE: "You had fun? Huh? Oh!\x7You're done! Great. Really nice of you to help out this way.\x7I found this in the back room but I don't have any use for it.\x7Maybe you'll find something to do with it. So long, _avName_!" },
    6291: {
        QUEST: 'Cogs broke into the First Security Blanket Bank! Go see William Teller and see if you can help.' },
    6292: {
        QUEST: 'Oh those darn Cashbot Cogs! They stole my reading lamps!\x7I need them back right away. Can you go look for them?\x7If you can get my reading lamps, I might be able to help you get into see the CFO.\x7Hurry!',
        INCOMPLETE_PROGRESS: 'I need those lamps back. Keep looking for them!',
        COMPLETE: "You're back! And you got my lamps!\x7I can't thank you enough but I can give you this." },
    7201: {
        QUEST: 'Nina Nightlight was looking for you, _avName_. She needs some help._where_' },
    7202: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Oh! I'm so glad to see you, _avName_. I could use some help!\x7Those darn Cogs have kept the delivery folks away and I have no beds in stock.\x7Could you go see Hardy O'Toole and bring me back a bed?_where_ ",
        INCOMPLETE_PROGRESS: "Did Hardy have any beds? I was sure he'd have one.",
        COMPLETE: '' },
    7203: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'A bed? Sure, here\'s one all ready to go.\x7Just bring it over to her for me, would you? Get it?\x7"WOOD" you? Hee-hee!\x7Pretty funny. No? Well, take it over there anyway, please?',
        INCOMPLETE_PROGRESS: 'Did Nina like the bed?',
        COMPLETE: '' },
    7204: {
        GREETING: '',
        LEAVING: '',
        QUEST: "This bed isn't right. It's much too plain.\x7Go see if he has anything fancier, would you?\x7I'm sure it won't take but a minute.",
        INCOMPLETE_PROGRESS: "I'm certain that Hardy has a fancier bed.",
        COMPLETE: '' },
    7205: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Didn't hit the nail on the head with that bed, huh? I've got one here that will do the job.\x7One small problem though - it needs to be assembled first.\x7While I hammer out this problem, could you get rid of some of those Cogs that are outside?\x7Those awful Cogs throw a wrench in the works.\x7Come back when you're done and the bed will be ready.",
        INCOMPLETE_PROGRESS: "Not quite done with assembling the bed.\x7When you're done with the Cogs, it'll be ready.",
        COMPLETE: '' },
    7206: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Hey there _avName_!\x7You did a bang-up job on those Cogs.\x7The bed is all ready. Could you please deliver it for me?\x7Now that those Cogs are gone, business will be brisk!',
        INCOMPLETE_PROGRESS: "I think Nina's waiting for that bed delivery.",
        COMPLETE: 'What a lovely bed!\x7Now my customers will be happy. Thanks, _avName_.\x7Say, you might be able to use this. Someone left it here.' },
    7209: {
        QUEST: 'Go see Honey Moon. She needs some help._where_' },
    7210: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Oh! I'm so glad to see you, _avName_. I really need some help!\x7I haven't been able to get my beauty sleep for ages. You see, those Cogs stole my bedspread.\x7Say, could you please run over and see if Ed's got anything in blue?_where_",
        INCOMPLETE_PROGRESS: 'What did Ed have to say about a blue bedspread?',
        COMPLETE: '' },
    7211: {
        GREETING: '',
        LEAVING: '',
        QUEST: "So, Honey wants a bedspread, huh?\x7What color? BLUE?!\x7Well, I'd have to make that for her special. Everything I've got is red.\x7Tell ya what...if you'll go deal with some of those Cogs out there, I'll make a special blue bedspread just for her.\x7Blue bedspreads...what'll it be next?",
        INCOMPLETE_PROGRESS: 'Still working on this blue bedspread, _avName_. Keep at those Cogs!',
        COMPLETE: '' },
    7212: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Nice to see you again. I've got something for you!\x7Here's the bedspread and it's blue. She'll love it.",
        INCOMPLETE_PROGRESS: 'Did Honey like the bedspread?',
        COMPLETE: '' },
    7213: {
        GREETING: '',
        LEAVING: '',
        QUEST: "My bedspread? No, that's not right.\x7It's PLAID! How can anyone sleep with such a LOUD pattern?\x7You'll just have to take it back and get a different one.\x7I'm sure he'll have others.",
        INCOMPLETE_PROGRESS: 'I simply will not accept a plaid bedspread. See what Ed can do about it.',
        COMPLETE: '' },
    7214: {
        GREETING: '',
        LEAVING: '',
        QUEST: "What? She doesn't like PLAID?\x7Hmm...let me see what we've got here.\x7This will take a while. Why don't you go take care of a few Cogs while I try to find something else?\x7I'll have something by the time you get back here.",
        INCOMPLETE_PROGRESS: "I'm still looking for another bedspread. How's it going with the Cogs?",
        COMPLETE: '' },
    7215: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Hey, good job on those Cogs!\x7Here you go, it's blue and it's not plaid.\x7Sure hope she likes paisley.\x7Bring the bedspread back to Honey.",
        INCOMPLETE_PROGRESS: "That's all I've got for you right now.\x7Please bring that bedspread to Honey.",
        COMPLETE: "Oh! That's lovely! Paisley suits me quite well.\x7Time for my beauty sleep, then! So long, _avName_.\x7What? You're still here? Can't you see I'm trying to sleep?\x7Here, take this and let me rest. I must look a fright!" },
    7218: {
        QUEST: 'Dreamy Daphne could use a hand._where_' },
    7219: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Oh, _avName_, I'm glad to see you! Those Cogs took my pillows.\x7Could you go see if Tex has some pillows?_where_\x7I'm sure he can help.",
        INCOMPLETE_PROGRESS: 'Does Tex have any pillows for me? ',
        COMPLETE: '' },
    7220: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Howdy! Daphne needs some pillows, huh? Well, you came to the right place, pardner!\x7More pillows in here than there's spines on a cactus.\x7Here you go, _avName_. Take these back over to Daphne with my compliments.\x7Always glad to help a gal out.",
        INCOMPLETE_PROGRESS: 'Were those pillows soft enough for the little lady?',
        COMPLETE: '' },
    7221: {
        GREETING: '',
        LEAVING: '',
        QUEST: "You got the pillows! Great!\x7Hey, wait a second! These pillows are awfully soft.\x7Much too soft for me. I need harder pillows.\x7Take these back to Tex and see what else he's got. Thanks.",
        INCOMPLETE_PROGRESS: 'Nope! Too soft. Ask Tex for different pillows.',
        COMPLETE: '' },
    7222: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Too soft, huh? Well, let me see what I've got....\x7Hmm...seems I had me a whole passel of hard pillows. Where'd they get to?\x7Oh! I remember. I was fixing to send them back so they're in storage.\x7How 'bout you clean up some of those Cog buildings out there while I get 'em out of storage, pardner?",
        INCOMPLETE_PROGRESS: "Cog buildings are hard. But these pillows aren't.\x7I'll keep looking.",
        COMPLETE: '' },
    7223: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Back already? Well, that's jess fine. See, I found those pillows Daphne wanted.\x7Now, you jess take these over to her. They're hard enough to break a tooth on!",
        INCOMPLETE_PROGRESS: "Yeah, those pillows are mighty hard. I hope Daphne fancies 'em.",
        COMPLETE: 'I knew Tex would have some harder pillows.\x7Oh yes, those are perfect. Nice and hard.\x7Would you have a use for this piece of a Cog suit? Might as well take it with you.' },
    7226: {
        QUEST: "Drop by to see Sandy Sandman. She's lost her pajamas._where_" },
    7227: {
        GREETING: '',
        LEAVING: '',
        QUEST: "I have no pajamas! They're missing!\x7What will I do? Oh! I know!\x7Go see Big Mama. She'll have pajamas for me._where_",
        INCOMPLETE_PROGRESS: 'Does Big Mama have pajamas for me?',
        COMPLETE: '' },
    7228: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Hey there, little toon! Big Mama's got the best pajamas from the Bahamas.\x7Oh, something for Sandy Sandman, huh? Well, let me see what I've got.\x7Here's a little something. Now she can sleep in style!\x7Would you run these back over to her for me? I can't leave the shop just now.\x7Thanks, _avName_. See you around!",
        INCOMPLETE_PROGRESS: 'You need to take those pajamas to Sandy._where_',
        COMPLETE: '' },
    7229: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Big Mama sent these for me? Oh...\x7Doesn't she have any pajamas with feet on them?\x7I always wear pajamas with feet. Doesn't everybody?\x7Take these back and ask her to find some with feet.",
        INCOMPLETE_PROGRESS: 'My pajamas must have feet. See what Big Mama can do.',
        COMPLETE: '' },
    7230: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Feet? Let me think....\x7Wait! I've got just the thing!\x7Ta-dah! Pajamas with feet. Nice blue pajamas with feet. Best ones on any island.\x7Please take them back to her, would you? Thanks!",
        INCOMPLETE_PROGRESS: 'Did Sandy like the blue footie pajamas?',
        COMPLETE: '' },
    7231: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Well, these DO have feet, but I can't wear blue pajamas!\x7Ask Big Mama if she has a different color.",
        INCOMPLETE_PROGRESS: "I'm sure Big Mama has footie pajamas in a different color.",
        COMPLETE: '' },
    7232: {
        GREETING: '',
        LEAVING: '',
        QUEST: "That's too bad. These are the only pajamas with feet I have.\x7Oh, I've got an idea. Go ask Cat. She may have some pajamas with feet._where_",
        INCOMPLETE_PROGRESS: "Nope, those are all the pajamas I've got. Go see what Cat has._where_",
        COMPLETE: '' },
    7233: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Pajamas with feet? Sure thing.\x7What do you mean, these are blue? She doesn't want blue?\x7Oh, that's a little trickier. Here, try these.\x7They're not blue and they DO have feet.",
        INCOMPLETE_PROGRESS: "I just love puce, don't you?\x7I hope Sandy likes them....",
        COMPLETE: '' },
    7234: {
        GREETING: '',
        LEAVING: '',
        QUEST: "No, these aren't blue but no one with my complexion could possibly wear puce.\x7Absolutely not. Back they go and you with them! See what else Cat has.",
        INCOMPLETE_PROGRESS: 'Cat must have more pajamas. No puce for me!',
        COMPLETE: '' },
    7235: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Not puce either. Hmm....\x7By my whiskers, I know I have some other ones.\x7They'll take a little while to find. Let's make a deal.\x7I'll find the other pajamas if you'll get rid of some of these Cog buildings. They're very unsettling.\x7I'll have the pajamas ready when you get back, _avName_.",
        INCOMPLETE_PROGRESS: 'You need to clear out a few more Cog buildings while I look for other pajamas.',
        COMPLETE: '' },
    7236: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'You did a great job on those Cogs! Thanks!\x7I found those pajamas for Sandy; hope she likes them.\x7Bring them over to her. Thank you.',
        INCOMPLETE_PROGRESS: "Sandy's waiting for those pajamas, _avName_.",
        COMPLETE: "Fuchsia pajamas with feet! Purr-fect!\x7Ah, now I'm all set. Let's see....\x7Oh, I suppose I should give you something for helping me out.\x7Maybe you can use this. Someone left it here." },
    7239: {
        QUEST: "Go see Smudgy Mascara. She's been looking for some help._where_" },
    7240: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Those darn Cogs took my wrinkle cream!\x7My customers simply MUST have wrinkle cream while I work on them.\x7Go see Rip and see if he has my special formula in stock._where_',
        INCOMPLETE_PROGRESS: 'I refuse to work on anyone without wrinkle cream.\x7See what Rip has for me.' },
    7241: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Oh, that Smudgy's a picky character. She won't settle for my usual formula.\x7That means I'll need some cauliflower coral, my super-secret special ingredient. But I haven't any in stock.\x7Could you go fish some out of the pond for me? As soon as you get the coral, I'll whip up a batch for Smudgy.",
        INCOMPLETE_PROGRESS: "I'll need that cauliflower coral to make a batch of wrinkle cream." },
    7242: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Wow, that's a nice cauliflower coral!\x7Ok, let's see...a little of this and a splash of that...now, just a dollop of kelp.\x7Huh, where's the kelp? Looks like I'm out of kelp, too.\x7Could you pop down to the pond and fish me out some nice, slimy kelp?",
        INCOMPLETE_PROGRESS: "Not a strip of slimy kelp in the shop.\x7Can't make the cream without it." },
    7243: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Oooh! Very slimy kelp you've got there, _avName_.\x7Now, I just crush some pearls with the mortar and pestle.\x7Um, where's my pestle? What good is a mortar without a pestle?\x7I bet that darn Loan Shark took it when he came in here!\x7You need to help me find it! He was headed for Cashbot HQ!",
        INCOMPLETE_PROGRESS: 'I simply cannot crush the pearls without a pestle.\x7Darn those Loan Sharks!' },
    7244: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Alright! You got my pestle!\x7Now we're in business. Crush that...stir this up and...\x7There ya go! Tell Smudgy's it's good and fresh.",
        INCOMPLETE_PROGRESS: "You should bring this over to Smudgy while it's fresh.\x7She's very picky.",
        COMPLETE: "Didn't Rip have a bigger jar of wrinkle cream than this? No?\x7Well, I guess I'll just order more when I run out.\x7So long, _avName_.\x7What? You're still here? Can't you see I'm trying to work?\x7Here, take this." } }
ChatGarblerDog = [
    'woof',
    'arf',
    'rruff']
ChatGarblerCat = [
    'meow',
    'mew']
ChatGarblerMouse = [
    'squeak',
    'squeaky',
    'squeakity']
ChatGarblerHorse = [
    'neigh',
    'brrr']
ChatGarblerRabbit = [
    'eek',
    'eepr',
    'eepy',
    'eeky']
ChatGarblerDuck = [
    'quack',
    'quackity',
    'quacky']
ChatGarblerMonkey = [
    'ooh',
    'ooo',
    'ahh']
ChatGarblerDefault = [
    'blah']
Bossbot = 'Bossbot'
Lawbot = 'Lawbot'
Cashbot = 'Cashbot'
Sellbot = 'Sellbot'
BossbotS = 'a Bossbot'
LawbotS = 'a Lawbot'
CashbotS = 'a Cashbot'
SellbotS = 'a Sellbot'
BossbotP = 'Bossbots'
LawbotP = 'Lawbots'
CashbotP = 'Cashbots'
SellbotP = 'Sellbots'
BossbotSkelS = 'a Bossbot Skelecog'
LawbotSkelS = 'a Lawbot Skelecog'
CashbotSkelS = 'a Cashbot Skelecog'
SellbotSkelS = 'a Sellbot Skelecog'
BossbotSkelP = 'Bossbot Skelecogs'
LawbotSkelP = 'Lawbot Skelecogs'
CashbotSkelP = 'Cashbot Skelecogs'
SellbotSkelP = 'Sellbot Skelecogs'
AvatarDetailPanelOK = lOK
AvatarDetailPanelCancel = lCancel
AvatarDetailPanelClose = lClose
AvatarDetailPanelLookup = 'Looking up details for %s.'
AvatarDetailPanelFailedLookup = 'Unable to get details for %s.'
AvatarDetailPanelOnline = 'District: %(district)s\nLocation: %(location)s'
AvatarDetailPanelOffline = 'District: offline\nLocation: offline'
AvatarPanelFriends = 'Friends'
AvatarPanelWhisper = 'Whisper'
AvatarPanelSecrets = 'Secrets'
AvatarPanelGoTo = 'Go To'
AvatarPanelPet = 'Show Doodle'
AvatarPanelIgnore = 'Ignore'
AvatarPanelCogLevel = 'Level: %s'
AvatarPanelCogDetailClose = lClose
AvatarPanelDetail = 'Toon Details'
PetPanelFeed = 'Feed'
PetPanelCall = 'Call'
PetPanelGoTo = 'Go To'
PetPanelOwner = 'Show Owner'
PetPanelDetail = 'Pet Details'
PetPanelScratch = 'Scratch'
PetDetailPanelTitle = 'Trick Training'
PetTrickStrings = {
    0: 'Jump',
    1: 'Beg',
    2: 'Play dead',
    3: 'Rollover',
    4: 'Backflip',
    5: 'Dance',
    6: 'Speak' }
PetMoodAdjectives = {
    'neutral': 'neutral',
    'hunger': 'hungry',
    'boredom': 'bored',
    'excitement': 'excited',
    'sadness': 'sad',
    'restlessness': 'restless',
    'playfulness': 'playful',
    'loneliness': 'lonely',
    'fatigue': 'tired',
    'confusion': 'confused',
    'anger': 'angry',
    'surprise': 'surprised',
    'affection': 'affectionate' }
FriendsListLabel = 'Friends'
TeleportPanelOK = lOK
TeleportPanelCancel = lCancel
TeleportPanelYes = lYes
TeleportPanelNo = lNo
TeleportPanelCheckAvailability = 'Trying to go to %s.'
TeleportPanelNotAvailable = '%s is busy right now; try again later.'
TeleportPanelIgnored = '%s is ignoring you.'
TeleportPanelNotOnline = "%s isn't online right now."
TeleportPanelWentAway = '%s went away.'
TeleportPanelUnknownHood = "You don't know how to get to %s!"
TeleportPanelUnavailableHood = '%s is not available right now; try again later.'
TeleportPanelDenySelf = "You can't go to yourself!"
TeleportPanelOtherShard = "%(avName)s is in district %(shardName)s, and you're in district %(myShardName)s.  Do you want to switch to %(shardName)s?"
BattleBldgBossTaunt = "I'm the boss."
FactoryBossTaunt = "I'm the Foreman."
FactoryBossBattleTaunt = 'Let me introduce you to the Foreman.'
MintBossTaunt = "I'm the Supervisor."
MintBossBattleTaunt = 'You need to talk to the Supervisor.'
ToonHealJokes = [
    [
        'What goes TICK-TICK-TICK-WOOF?',
        'A watchdog! '],
    [
        'Why do male deer need braces?',
        "Because they have 'buck teeth'!"],
    [
        'Why is it hard for a ghost to tell a lie?',
        'Because you can see right through him.'],
    [
        'What did the ballerina do when she hurt her foot?',
        'She called the toe truck!'],
    [
        'What has one horn and gives milk?',
        'A milk truck!'],
    [
        "Why don't witches ride their brooms when they're angry?",
        "They don't want to fly off the handle!"],
    [
        'Why did the dolphin cross the ocean?',
        'To get to the other tide.'],
    [
        'What kind of mistakes do spooks make?',
        'Boo boos.'],
    [
        'Why did the chicken cross the playground?',
        'To get to the other slide!'],
    [
        'Where does a peacock go when he loses his tail?',
        'A retail store.'],
    [
        "Why didn't the skeleton cross the road?",
        "He didn't have the guts."],
    [
        "Why wouldn't they let the butterfly into the dance?",
        'Because it was a moth ball.'],
    [
        "What's gray and squirts jam at you?",
        'A mouse eating a doughnut.'],
    [
        'What happened when 500 hares got loose on the main street?',
        'The police had to comb the area.'],
    [
        "What's the difference between a fish and a piano?",
        "You can tune a piano, but you can't tuna fish!"],
    [
        'What do people do in clock factories?',
        'They make faces all day.'],
    [
        'What do you call a blind dinosaur?',
        "An I-don't-think-he-saurus."],
    [
        'If you drop a white hat into the Red Sea, what does it become?',
        'Wet.'],
    [
        'Why was Cinderella thrown off the basketball team?',
        'She ran away from the ball.'],
    [
        'Why was Cinderella such a bad player?',
        'She had a pumpkin for a coach.'],
    [
        "What two things can't you have for breakfast?",
        'Lunch and dinner.'],
    [
        'What do you give an elephant with big feet?',
        'Big shoes.'],
    [
        'Where do baby ghosts go during the day?',
        'Day-scare centers.'],
    [
        'What did Snow White say to the photographer?',
        'Some day my prints will come.'],
    [
        "What's Tarzan's favorite song?",
        'Jungle bells.'],
    [
        "What's green and loud?",
        'A froghorn.'],
    [
        "What's worse than raining cats and dogs?",
        'Hailing taxis.'],
    [
        'When is the vet busiest?',
        "When it's raining cats and dogs."],
    [
        'What do you call a gorilla wearing ear-muffs?',
        "Anything you want, he can't hear you."],
    [
        'Where would you weigh a whale?',
        'At a whale-weigh station.'],
    [
        'What travels around the world but stays in the corner?',
        'A stamp.'],
    [
        'What do you give a pig with a sore throat?',
        'Oinkment.'],
    [
        'What did the hat say to the scarf?',
        'You hang around while I go on a head.'],
    [
        "What's the best parting gift?",
        'A comb.'],
    [
        'What kind of cats like to go bowling?',
        'Alley cats.'],
    [
        "What's wrong if you keep seeing talking animals?",
        "You're having Disney spells."],
    [
        'What did one eye say to the other?',
        'Between you and me, something smells.'],
    [
        "What's round, white and giggles?",
        'A tickled onion.'],
    [
        'What do you get when you cross Bambi with a ghost?',
        'Bamboo.'],
    [
        'Why do golfers take an extra pair of socks?',
        'In case they get a hole in one.'],
    [
        'What do you call a fly with no wings?',
        'A walk.'],
    [
        'Who did Frankenstein take to the prom?',
        'His ghoul friend.'],
    [
        'What lies on its back, one hundred feet in the air?',
        'A sleeping centipede.'],
    [
        'How do you keep a bull from charging?',
        'Take away his credit card.'],
    [
        'What do you call a chicken at the North Pole?',
        'Lost.'],
    [
        'What do you get if you cross a cat with a dog?',
        'An animal that chases itself.'],
    [
        'What did the digital watch say to the grandfather clock?',
        'Look dad, no hands.'],
    [
        'Where does Ariel the mermaid go to see movies?',
        'The dive-in.'],
    [
        'What do you call a mosquito with a tin suit?',
        'A bite in shining armor.'],
    [
        'What do giraffes have that no other animal has?',
        'Baby giraffes.'],
    [
        'Why did the man hit the clock?',
        'Because the clock struck first.'],
    [
        'Why did the apple go out with a fig?',
        "Because it couldn't find a date."],
    [
        'What do you get when you cross a parrot with a monster?',
        'A creature that gets a cracker whenever it asks for one.'],
    [
        "Why didn't the monster make the football team?",
        'Because he threw like a ghoul!'],
    [
        'What do you get if you cross a Cocker Spaniel with a Poodle and a rooster?',
        'A cockapoodledoo!'],
    [
        'What goes dot-dot-dash-dash-squeak?',
        'Mouse code.'],
    [
        "Why aren't elephants allowed on beaches?",
        "They can't keep their trunks up."],
    [
        'What is at the end of everything?',
        'The letter G.'],
    [
        'How do trains hear?',
        'Through the engineers.'],
    [
        'What does the winner of a marathon lose?',
        'His breath.'],
    [
        'Why did the pelican refuse to pay for his meal?',
        'His bill was too big.'],
    [
        'What has six eyes but cannot see?',
        'Three blind mice.'],
    [
        "What works only when it's fired?",
        'A rocket.'],
    [
        "Why wasn't there any food left after the monster party?",
        'Because everyone was a goblin!'],
    [
        'What bird can be heard at mealtimes?',
        'A swallow.'],
    [
        'What goes Oh, Oh, Oh?',
        'Santa walking backwards.'],
    [
        'What has green hair and runs through the forest?',
        'Moldy locks.'],
    [
        'Where do ghosts pick up their mail?',
        'At the ghost office.'],
    [
        'Why do dinosaurs have long necks?',
        'Because their feet smell.'],
    [
        'What do mermaids have on toast?',
        'Mermarlade.'],
    [
        'Why do elephants never forget?',
        'Because nobody ever tells them anything.'],
    [
        "What's in the middle of a jellyfish?",
        'A jellybutton.'],
    [
        'What do you call a very popular perfume?',
        'A best-smeller.'],
    [
        "Why can't you play jokes on snakes?",
        'Because you can never pull their legs.'],
    [
        'Why did the baker stop making donuts?',
        'He got sick of the hole business.'],
    [
        'Why do mummies make excellent spies?',
        "They're good at keeping things under wraps."],
    [
        'How do you stop an elephant from going through the eye of a needle?',
        'Tie a knot in its tail.'],
    [
        "What goes 'Ha Ha Ha Thud'?",
        'Someone laughing his head off.'],
    [
        "My friend thinks he's a rubber band.",
        'I told him to snap out of it.'],
    [
        "My sister thinks she's a pair of curtains.",
        'I told her to pull herself together!'],
    [
        'Did you hear about the dentist that married the manicurist?',
        'Within a month they were fighting tooth and nail.'],
    [
        'Why do hummingbirds hum?',
        "Because they don't know the words."],
    [
        'Why did the baby turkey bolt down his food?',
        'Because he was a little gobbler.'],
    [
        'Where did the whale go when it was bankrupt?',
        'To the loan shark.'],
    [
        'How does a sick sheep feel?',
        'Baah-aahd.'],
    [
        "What's gray, weighs 10 pounds and squeaks?",
        'A mouse that needs to go on a diet.'],
    [
        'Why did the dog chase his tail?',
        'To make ends meet.'],
    [
        'Why do elephants wear running shoes?',
        'For jogging of course.'],
    [
        'Why are elephants big and gray?',
        "Because if they were small and yellow they'd be canaries."],
    [
        'If athletes get tennis elbow what do astronauts get?',
        'Missile toe.'],
    [
        'Did you hear about the man who hated Santa?',
        'He suffered from Claustrophobia.'],
    [
        'Why did ' + Donald + ' sprinkle sugar on his pillow?',
        'Because he wanted to have sweet dreams.'],
    [
        'Why did ' + Goofy + ' take his comb to the dentist?',
        'Because it had lost all its teeth.'],
    [
        'Why did ' + Goofy + ' wear his shirt in the bath?',
        'Because the label said wash and wear.'],
    [
        'Why did the dirty chicken cross the road?',
        'For some fowl purpose.'],
    [
        "Why didn't the skeleton go to the party?",
        'He had no body to go with.'],
    [
        'Why did the burglar take a shower?',
        'To make a clean getaway.'],
    [
        'Why does a sheep have a woolly coat?',
        "Because he'd look silly in a plastic one."],
    [
        'Why do potatoes argue all the time?',
        "They can't see eye to eye."],
    [
        'Why did ' + Pluto + ' sleep with a banana peel?',
        'So he could slip out of bed in the morning.'],
    [
        'Why did the mouse wear brown sneakers?',
        'His white ones were in the wash.'],
    [
        'Why are false teeth like stars?',
        'They come out at night.'],
    [
        'Why are Saturday and Sunday so strong?',
        'Because the others are weekdays.'],
    [
        'Why did the archaeologist go bankrupt?',
        'Because his career was in ruins.'],
    [
        'What do you get if you cross the Atlantic on the Titanic?',
        'Very wet.'],
    [
        'What do you get if you cross a chicken with cement?',
        'A brick-layer.'],
    [
        'What do you get if you cross a dog with a phone?',
        'A golden receiver.'],
    [
        'What do you get if you cross an elephant with a shark?',
        'Swimming trunks with sharp teeth.'],
    [
        'What did the tablecloth say to the table?',
        "Don't move, I've got you covered."],
    [
        'Did you hear about the time ' + Goofy + ' ate a candle?',
        'He wanted a light snack.'],
    [
        'What did the balloon say to the pin?',
        'Hi Buster.'],
    [
        'What did the big chimney say to the little chimney?',
        "You're too young to smoke."],
    [
        'What did the carpet say to the floor?',
        'I got you covered.'],
    [
        'What did the necklace say to the hat?',
        "You go ahead, I'll hang around."],
    [
        'What goes zzub-zzub?',
        'A bee flying backwards.'],
    [
        'How do you communicate with a fish?',
        'Drop him a line.'],
    [
        "What do you call a dinosaur that's never late?",
        'A prontosaurus.'],
    [
        'What do you get if you cross a bear and a skunk?',
        'Winnie-the-phew.'],
    [
        'How do you clean a tuba?',
        'With a tuba toothpaste.'],
    [
        'What do frogs like to sit on?',
        'Toadstools.'],
    [
        'Why was the math book unhappy?',
        'It had too many problems.'],
    [
        'Why was the school clock punished?',
        'It tocked too much.'],
    [
        "What's a polygon?",
        'A dead parrot.'],
    [
        'What needs a bath and keeps crossing the street?',
        'A dirty double crosser.'],
    [
        'What do you get if you cross a camera with a crocodile?',
        'A snap shot.'],
    [
        'What do you get if you cross an elephant with a canary?',
        'A very messy cage.'],
    [
        'What do you get if you cross a jeweler with a plumber?',
        'A ring around the bathtub.'],
    [
        'What do you get if you cross an elephant with a crow?',
        'Lots of broken telephone poles.'],
    [
        'What do you get if you cross a plum with a tiger?',
        'A purple people eater.'],
    [
        "What's the best way to save water?",
        'Dilute it.'],
    [
        "What's a lazy shoe called?",
        'A loafer.'],
    [
        "What's green, noisy and dangerous?",
        'A thundering herd of cucumbers.'],
    [
        'What color is a shout?',
        'Yellow!'],
    [
        'What do you call a sick duck?',
        'A mallardy.'],
    [
        "What's worse then a giraffe with a sore throat?",
        "A centipede with athlete's foot."],
    [
        'What goes ABC...slurp...DEF...slurp?',
        'Someone eating alphabet soup.'],
    [
        "What's green and jumps up and down?",
        'Lettuce at a dance.'],
    [
        "What's a cow after she gives birth?",
        'De-calf-inated.'],
    [
        'What do you get if you cross a cow and a camel?',
        'Lumpy milk shakes.'],
    [
        "What's white with black and red spots?",
        'A Dalmatian with measles.'],
    [
        "What's brown has four legs and a trunk?",
        'A mouse coming back from vacation.'],
    [
        "What does a skunk do when it's angry?",
        'It raises a stink.'],
    [
        "What's gray, weighs 200 pounds and says, Here Kitty, kitty?",
        'A 200 pound mouse.'],
    [
        "What's the best way to catch a squirrel?",
        'Climb a tree and act like a nut.'],
    [
        "What's the best way to catch a rabbit?",
        'Hide in a bush and make a noise like lettuce.'],
    [
        'What do you call a spider that just got married?',
        'A newly web.'],
    [
        'What do you call a duck that robs banks?',
        'A safe quacker.'],
    [
        "What's furry, meows and chases mice underwater?",
        'A catfish.'],
    [
        "What's a funny egg called?",
        'A practical yolker.'],
    [
        "What's green on the outside and yellow inside?",
        'A banana disguised as a cucumber.'],
    [
        'What did the elephant say to the lemon?',
        "Let's play squash."],
    [
        'What weighs 4 tons, has a trunk and is bright red?',
        'An embarrassed elephant.'],
    [
        "What's gray, weighs 4 tons, and wears glass slippers?",
        'Cinderelephant.'],
    [
        "What's an elephant in a fridge called?",
        'A very tight squeeze.'],
    [
        'What did the elephant say to her naughty child?',
        'Tusk!  Tusk!'],
    [
        'What did the peanut say to the elephant?',
        "Nothing -- Peanuts can't talk."],
    [
        'What do elephants say when they bump into each other?',
        "Small world, isn't it?"],
    [
        'What did the cashier say to the register?',
        "I'm counting on you."],
    [
        'What did the flea say to the other flea?',
        'Shall we walk or take the cat?'],
    [
        'What did the big hand say to the little hand?',
        'Got a minute.'],
    [
        'What does the sea say to the sand?',
        'Not much.  It usually waves.'],
    [
        'What did the stocking say to the shoe?',
        'See you later, I gotta run.'],
    [
        'What did one tonsil say to the other tonsil?',
        'It must be spring, here comes a swallow.'],
    [
        'What did the soil say to the rain?',
        'Stop, or my name is mud.'],
    [
        'What did the puddle say to the rain?',
        'Drop in sometime.'],
    [
        'What did the bee say to the rose?',
        'Hi, bud.'],
    [
        'What did the appendix say to the kidney?',
        "The doctor's taking me out tonight."],
    [
        'What did the window say to the venetian blinds?',
        "If it wasn't for you it'd be curtains for me."],
    [
        'What did the doctor say to the sick orange?',
        'Are you peeling well?'],
    [
        'What do you get if you cross a chicken with a banjo?',
        'A self-plucking chicken.'],
    [
        'What do you get if you cross a hyena with a bouillon cube?',
        'An animal that makes a laughing stock of itself.'],
    [
        'What do you get if you cross a rabbit with a spider?',
        'A hare net.'],
    [
        'What do you get if you cross a germ with a comedian?',
        'Sick jokes.'],
    [
        'What do you get if you cross a hyena with a mynah bird?',
        'An animal that laughs at its own jokes.'],
    [
        'What do you get if you cross a railway engine with a stick of gum?',
        'A chew-chew train.'],
    [
        'What would you get if you crossed an elephant with a computer?',
        'A big know-it-all.'],
    [
        'What would you get if you crossed an elephant with a skunk?',
        'A big stinker.'],
    [
        'Why did ' + MickeyMouse + ' take a trip to outer space?',
        'He wanted to find ' + Pluto + '.']]
MovieHealLaughterMisses = ('hmm', 'heh', 'ha', 'harr harr')
MovieHealLaughterHits1 = ('Ha Ha Ha', 'Hee Hee', 'Tee Hee', 'Ha Ha')
MovieHealLaughterHits2 = ('BWAH HAH HAH!', 'HO HO HO!', 'HA HA HA!')
MovieSOSCallHelp = '%s HELP!'
MovieSOSWhisperHelp = '%s needs help in battle!'
MovieSOSObserverHelp = 'HELP!'
MovieNPCSOSGreeting = 'Hi %s! Glad to help!'
MovieNPCSOSGoodbye = 'See you later!'
MovieNPCSOSToonsHit = 'Toons Always Hit!'
MovieNPCSOSCogsMiss = 'Cogs Always Miss!'
MovieNPCSOSRestockGags = 'Restocking %s Gags!'
MovieNPCSOSHeal = 'Heal'
MovieNPCSOSTrap = 'Trap'
MovieNPCSOSLure = 'Lure'
MovieNPCSOSSound = 'Sound'
MovieNPCSOSThrow = 'Throw'
MovieNPCSOSSquirt = 'Squirt'
MovieNPCSOSDrop = 'Drop'
MovieNPCSOSAll = 'All'
MoviePetSOSTrickFail = 'Sigh'
MoviePetSOSTrickSucceedBoy = 'Good boy!'
MoviePetSOSTrickSucceedGirl = 'Good girl!'
MovieSuitCancelled = 'CANCELLED\nCANCELLED\nCANCELLED'
RewardPanelToonTasks = 'ToonTasks'
RewardPanelItems = 'Items Recovered'
RewardPanelMissedItems = 'Items Not Recovered'
RewardPanelQuestLabel = 'Quest %s'
RewardPanelCongratsStrings = [
    'Yeah!',
    'Congratulations!',
    'Wow!',
    'Cool!',
    'Awesome!',
    'Toon-tastic!']
RewardPanelNewGag = 'New %(gagName)s gag for %(avName)s!'
RewardPanelMeritsMaxed = 'Maxed'
RewardPanelMeritBarLabels = [
    'Pink Slips',
    'Subpoenas',
    'Cogbucks',
    'Merits']
RewardPanelMeritAlert = 'Ready for promotion!'
RewardPanelCogPart = 'You gained a Cog disguise part!'
CheesyEffectDescriptions = [
    ('Normal Toon', 'you will be normal'),
    ('Big head', 'you will have a big head'),
    ('Small head', 'you will have a small head'),
    ('Big legs', 'you will have big legs'),
    ('Small legs', 'you will have small legs'),
    ('Big toon', 'you will be a little bigger'),
    ('Small toon', 'you will be a little smaller'),
    ('Flat portrait', 'you will be two-dimensional'),
    ('Flat profile', 'you will be two-dimensional'),
    ('Transparent', 'you will be transparent'),
    ('No color', 'you will be colorless'),
    ('Invisible toon', 'you will be invisible')]
CheesyEffectIndefinite = 'Until you choose another effect, %(effectName)s%(whileIn)s.'
CheesyEffectMinutes = 'For the next %(time)s minutes, %(effectName)s%(whileIn)s.'
CheesyEffectHours = 'For the next %(time)s hours, %(effectName)s%(whileIn)s.'
CheesyEffectDays = 'For the next %(time)s days, %(effectName)s%(whileIn)s.'
CheesyEffectWhileYouAreIn = ' while you are in %s'
CheesyEffectExceptIn = ', except in %s'
SuitFlunky = 'Flunky'
SuitPencilPusher = 'Pencil Pusher'
SuitYesman = 'Yesman'
SuitMicromanager = 'Micro\x3manager'
SuitDownsizer = 'Downsizer'
SuitHeadHunter = 'Head Hunter'
SuitCorporateRaider = 'Corporate Raider'
SuitTheBigCheese = 'The Big Cheese'
SuitColdCaller = 'Cold Caller'
SuitTelemarketer = 'Tele\x3marketer'
SuitNameDropper = 'Name Dropper'
SuitGladHander = 'Glad Hander'
SuitMoverShaker = 'Mover & Shaker'
SuitTwoFace = 'Two-Face'
SuitTheMingler = 'The Mingler'
SuitMrHollywood = 'Mr. Hollywood'
SuitShortChange = 'Short Change'
SuitPennyPincher = 'Penny Pincher'
SuitTightwad = 'Tightwad'
SuitBeanCounter = 'Bean Counter'
SuitNumberCruncher = 'Number Cruncher'
SuitMoneyBags = 'Money Bags'
SuitLoanShark = 'Loan Shark'
SuitRobberBaron = 'Robber Baron'
SuitBottomFeeder = 'Bottom Feeder'
SuitBloodsucker = 'Blood\x3sucker'
SuitDoubleTalker = 'Double Talker'
SuitAmbulanceChaser = 'Ambulance Chaser'
SuitBackStabber = 'Back Stabber'
SuitSpinDoctor = 'Spin Doctor'
SuitLegalEagle = 'Legal Eagle'
SuitBigWig = 'Big Wig'
SuitFlunkyS = 'a Flunky'
SuitPencilPusherS = 'a Pencil Pusher'
SuitYesmanS = 'a Yesman'
SuitMicromanagerS = 'a Micromanager'
SuitDownsizerS = 'a Downsizer'
SuitHeadHunterS = 'a Head Hunter'
SuitCorporateRaiderS = 'a Corporate Raider'
SuitTheBigCheeseS = 'a The Big Cheese'
SuitColdCallerS = 'a Cold Caller'
SuitTelemarketerS = 'a Telemarketer'
SuitNameDropperS = 'a Name Dropper'
SuitGladHanderS = 'a Glad Hander'
SuitMoverShakerS = 'a Mover & Shaker'
SuitTwoFaceS = 'a Two-Face'
SuitTheMinglerS = 'a The Mingler'
SuitMrHollywoodS = 'a Mr. Hollywood'
SuitShortChangeS = 'a Short Change'
SuitPennyPincherS = 'a Penny Pincher'
SuitTightwadS = 'a Tightwad'
SuitBeanCounterS = 'a Bean Counter'
SuitNumberCruncherS = 'a Number Cruncher'
SuitMoneyBagsS = 'a Money Bags'
SuitLoanSharkS = 'a Loan Shark'
SuitRobberBaronS = 'a Robber Baron'
SuitBottomFeederS = 'a Bottom Feeder'
SuitBloodsuckerS = 'a Bloodsucker'
SuitDoubleTalkerS = 'a Double Talker'
SuitAmbulanceChaserS = 'an Ambulance Chaser'
SuitBackStabberS = 'a Back Stabber'
SuitSpinDoctorS = 'a Spin Doctor'
SuitLegalEagleS = 'a Legal Eagle'
SuitBigWigS = 'a Big Wig'
SuitFlunkyP = 'Flunkies'
SuitPencilPusherP = 'Pencil Pushers'
SuitYesmanP = 'Yesmen'
SuitMicromanagerP = 'Micromanagers'
SuitDownsizerP = 'Downsizers'
SuitHeadHunterP = 'Head Hunters'
SuitCorporateRaiderP = 'Corporate Raiders'
SuitTheBigCheeseP = 'The Big Cheeses'
SuitColdCallerP = 'Cold Callers'
SuitTelemarketerP = 'Telemarketers'
SuitNameDropperP = 'Name Droppers'
SuitGladHanderP = 'Glad Handers'
SuitMoverShakerP = 'Movers & Shakers'
SuitTwoFaceP = 'Two-Faces'
SuitTheMinglerP = 'The Minglers'
SuitMrHollywoodP = 'Mr. Hollywoods'
SuitShortChangeP = 'Short Changes'
SuitPennyPincherP = 'Penny Pinchers'
SuitTightwadP = 'Tightwads'
SuitBeanCounterP = 'Bean Counters'
SuitNumberCruncherP = 'Number Crunchers'
SuitMoneyBagsP = 'Money Bags'
SuitLoanSharkP = 'Loan Sharks'
SuitRobberBaronP = 'Robber Barons'
SuitBottomFeederP = 'Bottom Feeders'
SuitBloodsuckerP = 'Bloodsuckers'
SuitDoubleTalkerP = 'Double Talkers'
SuitAmbulanceChaserP = 'Ambulance Chasers'
SuitBackStabberP = 'Back Stabbers'
SuitSpinDoctorP = 'Spin Doctors'
SuitLegalEagleP = 'Legal Eagles'
SuitBigWigP = 'Big Wigs'
SuitFaceOffDefaultTaunts = [
    'Boo!']
SuitAttackDefaultTaunts = [
    'Take that!',
    'Take a memo on this!']
SuitAttackNames = {
    'Audit': 'Audit!',
    'Bite': 'Bite!',
    'BounceCheck': 'Bounce Check!',
    'BrainStorm': 'Brain Storm!',
    'BuzzWord': 'Buzz Word!',
    'Calculate': 'Calculate!',
    'Canned': 'Canned!',
    'Chomp': 'Chomp!',
    'CigarSmoke': 'Cigar Smoke!',
    'ClipOnTie': 'Clip On Tie!',
    'Crunch': 'Crunch!',
    'Demotion': 'Demotion!',
    'Downsize': 'Downsize!',
    'DoubleTalk': 'Double Talk!',
    'EvictionNotice': 'Eviction Notice!',
    'EvilEye': 'Evil Eye!',
    'Filibuster': 'Filibuster!',
    'FillWithLead': 'Fill With Lead!',
    'FiveOClockShadow': "Five O'Clock Shadow!",
    'FingerWag': 'Finger Wag!',
    'Fired': 'Fired!',
    'FloodTheMarket': 'Flood The Market!',
    'FountainPen': 'Fountain Pen!',
    'FreezeAssets': 'Freeze Assets!',
    'Gavel': 'Gavel!',
    'GlowerPower': 'Glower Power!',
    'GuiltTrip': 'Guilt Trip!',
    'HalfWindsor': 'Half Windsor!',
    'HangUp': 'Hang Up!',
    'HeadShrink': 'Head Shrink!',
    'HotAir': 'Hot Air!',
    'Jargon': 'Jargon!',
    'Legalese': 'Legalese!',
    'Liquidate': 'Liquidate!',
    'MarketCrash': 'Market Crash!',
    'MumboJumbo': 'Mumbo Jumbo!',
    'ParadigmShift': 'Paradigm Shift!',
    'PeckingOrder': 'Pecking Order!',
    'PickPocket': 'Pick Pocket!',
    'PinkSlip': 'Pink Slip!',
    'PlayHardball': 'Play Hardball!',
    'PoundKey': 'Pound Key!',
    'PowerTie': 'Power Tie!',
    'PowerTrip': 'Power Trip!',
    'Quake': 'Quake!',
    'RazzleDazzle': 'Razzle Dazzle!',
    'RedTape': 'Red Tape!',
    'ReOrg': 'Re-Org!',
    'RestrainingOrder': 'Restraining Order!',
    'Rolodex': 'Rolodex!',
    'RubberStamp': 'Rubber Stamp!',
    'RubOut': 'Rub Out!',
    'Sacked': 'Sacked!',
    'SandTrap': 'Sand Trap!',
    'Schmooze': 'Schmooze!',
    'Shake': 'Shake!',
    'Shred': 'Shred!',
    'SongAndDance': 'Song And Dance!',
    'Spin': 'Spin!',
    'Synergy': 'Synergy!',
    'Tabulate': 'Tabulate!',
    'TeeOff': 'Tee Off!',
    'ThrowBook': 'Throw Book!',
    'Tremor': 'Tremor!',
    'Watercooler': 'Watercooler!',
    'Withdrawal': 'Withdrawal!',
    'WriteOff': 'Write Off!' }
SuitAttackTaunts = {
    'Audit': [
        "I believe your books don't balance.",
        "Looks like you're in the red.",
        'Let me help you with your books.',
        'Your debit column is much too high.',
        "Let's check your assets.",
        'This will put you in debt.',
        "Let's take a close look at what you owe.",
        'This should drain your account.',
        'Time for you to account for your expenses.',
        "I've found an error in your books."],
    'Bite': [
        'Would you like a bite?',
        'Try a bite of this!',
        "You're biting off more than you can chew.",
        'My bite is bigger than my bark.',
        'Bite down on this!',
        'Watch out, I may bite.',
        "I don't just bite when I'm cornered.",
        "I'm just gonna grab a quick bite.",
        "I haven't had a bite all day.",
        'I just want a bite.  Is that too much to ask?'],
    'BounceCheck': [
        "Ah, too bad, you're funless.",
        'You have a payment due.',
        'I believe this check is yours.',
        'You owed me for this.',
        "I'm collecting on this debt.",
        "This check isn't going to be tender.",
        "You're going to be charged for this.",
        'Check this out.',
        'This is going to cost you.',
        "I'd like to cash this in.",
        "I'm just going to kick this back to you.",
        'This is one sour note.',
        "I'm deducting a service charge."],
    'BrainStorm': [
        'I forecast rain.',
        'Hope you packed your umbrella.',
        'I want to enlighten you.',
        'How about a few rain DROPS?',
        'Not so sunny now, are you Toon?',
        'Ready for a down pour?',
        "I'm going to take you by storm.",
        'I call this a lightning attack.',
        'I love to be a wet blanket.'],
    'BuzzWord': [
        'Pardon me if I drone on.',
        'Have you heard the latest?',
        'Can you catch on to this?',
        'See if you can hum this Toon.',
        'Let me put in a good word for you.',
        'I\'ll "B" perfectly clear.',
        'You should "B" more careful.',
        'See if you can dodge this swarm.',
        "Careful, you're about to get stung.",
        'Looks like you have a bad case of hives.'],
    'Calculate': [
        'These numbers do add up!',
        'Did you count on this?',
        "Add it up, you're going down.",
        'Let me help you add this up.',
        'Did you register all your expenses?',
        "According to my calculations, you won't be around much longer.",
        "Here's the grand total.",
        'Wow, your bill is adding up.',
        'Try fiddling with these numbers!',
        Cogs + ': 1 Toons: 0'],
    'Canned': [
        'Do you like it out of the can?',
        '"Can" you handle this?',
        "This one's fresh out of the can!",
        'Ever been attacked by canned goods before?',
        "I'd like to donate this canned good to you!",
        'Get ready to "Kick the can"!',
        'You think you "can", you think you "can".',
        "I'll throw you in the can!",
        "I'm making me a can o' toon-a!",
        "You don't taste so good out of the can."],
    'Chomp': [
        'Take a look at these chompers!',
        'Chomp, chomp, chomp!',
        "Here's something to chomp on.",
        'Looking for something to chomp on?',
        "Why don't you chomp on this?",
        "I'm going to have you for dinner.",
        'I love to feed on Toons!'],
    'ClipOnTie': [
        'Better dress for our meeting.',
        "You can't go OUT without your tie.",
        'The best dressed ' + Cogs + ' wear them.',
        'Try this on for size.',
        'You should dress for success.',
        'No tie, no service.',
        'Do you need help putting this on?',
        'Nothing says powerful like a good tie.',
        "Let's see if this fits.",
        'This is going to choke you up.',
        "You'll want to dress up before you go OUT.",
        "I think I'll tie you up."],
    'Crunch': [
        "Looks like you're in a crunch.",
        "It's crunch time!",
        "I'll give you something to crunch on!",
        'Crunch on this!',
        'I pack quite a crunch.',
        'Which do you prefer, smooth or crunchy?',
        "I hope you're ready for crunch time.",
        "It sounds like you're getting crunched!",
        "I'll crunch you like a can."],
    'Demotion': [
        "You're moving down the corporate ladder.",
        "I'm sending you back to the Mail Room.",
        'Time to turn in your nameplate.',
        "You're going down, clown.",
        "Looks like you're stuck.",
        "You're going nowhere fast.",
        "You're in a dead end position.",
        "You won't be moving anytime soon.",
        "You're not going anywhere.",
        'This will go on your permanent record.'],
    'Downsize': [
        'Come on down!',
        'Do you know how to get down?',
        "Let's get down to business.",
        "What's wrong? You look down.",
        'Going down?',
        "What's goin' down? You!",
        'Why pick on people my own size?',
        "Why don't I size you up, or should I say, down?",
        'Would you like a smaller size for just a quarter more?',
        'Try this on for size!',
        'You can get this in a smaller size.',
        'This attack is one size fits all!'],
    'EvictionNotice': [
        "It's moving time.",
        'Pack your bags, Toon.',
        'Time to make some new living arrangements.',
        'Consider yourself served.',
        "You're behind on your lease.",
        'This will be extremely unsettling.',
        "You're about to be uprooted.",
        "I'm going to send you packing.",
        "You're out of place.",
        'Prepare to be relocated.',
        "You're in a hostel position."],
    'EvilEye': [
        "I'm giving you the evil eye.",
        'Could you eye-ball this for me?',
        "Wait.  I've got something in my eye.",
        "I've got my eye on you!",
        'Could you keep an eye on this for me?',
        "I've got a real eye for evil.",
        "I'll poke you in the eye!",
        '"Eye" am as evil as they come!',
        "I'll put you in the eye of the storm!",
        "I'm rolling my eye at you."],
    'Filibuster': [
        "Shall I fill 'er up?",
        'This is going to take awhile.',
        'I could do this all day.',
        "I don't even need to take a breath.",
        'I keep going and going and going.',
        'I never get tired of this one.',
        'I can talk a blue streak.',
        'Mind if I bend your ear?',
        "I think I'll shoot the breeze.",
        'I can always get a word in edgewise.'],
    'FingerWag': [
        'I have told you a thousand times.',
        'Now see here Toon.',
        "Don't make me laugh.",
        "Don't make me come over there.",
        "I'm tired of repeating myself.",
        "I believe we've been over this.",
        'You have no respect for us ' + Cogs + '.',
        "I think it's time you pay attention.",
        'Blah, Blah, Blah, Blah, Blah.',
        "Don't make me stop this meeting.",
        'Am I going to have to separate you?',
        "We've been through this before."],
    'Fired': [
        'I hope you brought some marshmallows.',
        "It's going to get rather warm around here.",
        'This should take the chill out of the air.',
        "I hope you're cold blooded.",
        'Hot, hot and hotter.',
        'You better stop, drop, and roll!',
        "You're outta here.",
        'How does "well-done" sound?',
        'Can you say ouch?',
        'Hope you wore sunscreen.',
        'Do you feel a little toasty?',
        "You're going down in flames.",
        "You'll go out in a blaze.",
        "You're a flash in the pan.",
        'I think I have a bit of a flare about me.',
        "I just sparkle, don't I?",
        'Oh look, a crispy critter.',
        "You shouldn't run around half baked."],
    'FountainPen': [
        'This is going to leave a stain.',
        "Let's ink this deal.",
        'Be prepared for some permanent damage.',
        "You're going to need a good dry cleaner.",
        'You should change.',
        'This fountain pen has such a nice font.',
        "Here, I'll use my pen.",
        'Can you read my writing?',
        'I call this the plume of doom.',
        "There's a blot on your performance.",
        "Don't you hate when this happens?"],
    'FreezeAssets': [
        'Your assets are mine.',
        'Do you feel a draft?',
        "Hope you don't have plans.",
        'This should keep you on ice.',
        "There's a chill in the air.",
        'Winter is coming early this year.',
        'Are you feeling a little blue?',
        'Let me crystallize my plan.',
        "You're going to take this hard.",
        'This should cause freezer burn.',
        'I hope you like cold cuts.',
        "I'm very cold blooded."],
    'GlowerPower': [
        'You looking at me?',
        "I'm told I have very piercing eyes.",
        'I like to stay on the cutting edge.',
        "Jeepers, Creepers, don't you love my peepers?",
        "Here's looking at you kid.",
        "How's this for expressive eyes?",
        'My eyes are my strongest feature.',
        'The eyes have it.',
        'Peeka-boo, I see you.',
        'Look into my eyes...',
        'Shall we take a peek at your future?'],
    'GuiltTrip': [
        "I'll lay a real guilt trip on you!",
        'Feeling guilty?',
        "It's all your fault!",
        'I always blame everything on you.',
        'Wallow in your own guilt!',
        "I'm never speaking to you again!",
        "You had better say you're sorry.",
        "I'm would forgive you in a million years!",
        'Are you ready for your trip?',
        'Call me when you get back from your trip.',
        'When do you get back from your trip?'],
    'HalfWindsor': [
        "This is the fanciest tie you'll ever see!",
        'Try not to get too winded.',
        "This isn't even half the trouble you're in.",
        "You're lucky I don't have a whole windsor.",
        "You can't afford this tie.",
        "I bet you've never even SEEN a half windsor!",
        'This tie is out of your league.',
        "I shouldn't even waste this tie on you.",
        "You're not even worth half of this tie!"],
    'HangUp': [
        "You've been disconnected.",
        'Good bye!',
        "It's time I end our connection.",
        "...and don't call back!",
        'Click!',
        'This conversation is over.',
        "I'm severing this link.",
        'I think you have a few hang ups.',
        "It appears you've got a weak link.",
        'Your time is up.',
        'I hope you receive this loud and clear.',
        'You got the wrong number.'],
    'HeadShrink': [
        "Looks like you're seeing a shrink.",
        'Honey, I shrunk the toon.',
        "Hope this doesn't shrink your pride.",
        'Do you shrink in the wash?',
        'I shrink therefore I am.',
        "It's nothing to lose your head over.",
        'Are you going out of your head?',
        'Heads up! Or should I say, down.',
        'Objects may be larger than they appear.',
        'Good Toons come in small packages.'],
    'HotAir': [
        "We're having a heated discussion.",
        "You're experiencing a heat wave.",
        "I've reached my boiling point.",
        'This should cause some wind burn.',
        'I hate to grill you, but...',
        "Always remember, where there's smoke, there's fire.",
        "You're looking a little burned out.",
        'Another meeting up in smoke.',
        "Guess it's time to add fuel to the fire.",
        'Let me kindle a working relationship.',
        'I have some glowing remarks for you.',
        'Air Raid!!!'],
    'Jargon': [
        'What nonsense.',
        'See if you can make sense of this.',
        'I hope you get this loud and clear.',
        "Looks like I'm going to have to raise my voice.",
        'I insist on having my say.',
        "I'm very outspoken.",
        'I must pontificate on this subject.',
        'See, words can hurt you.',
        'Did you catch my meaning?',
        'Words, words, words, words, words.'],
    'Legalese': [
        'You must cease and desist.',
        'You will be defeated, legally speaking.',
        'Are you aware of the legal ramifications?',
        "You aren't above the law!",
        'There should be a law against you.',
        "There's no ex post facto with me!",
        "The opinions expressed in this attack are not those of Disney's Toontown Online.",
        'We cannot be held responsible for damages suffered in this attack.',
        'Your results for this attack may vary.',
        'This attack is void where prohibited.',
        "You don't fit into my legal system!",
        "You can't handle the legal matters."],
    'Liquidate': [
        'I like to keep things fluid.',
        'Are you having some cash flow problems?',
        "I'll have to purge your assets.",
        'Time for you to go with the flow.',
        "Remember it's slippery when wet.",
        'Your numbers are running.',
        'You seem to be slipping.',
        "It's all crashing down on you.",
        "I think you're diluted.",
        "You're all washed up."],
    'MarketCrash': [
        "I'm going to crash your party.",
        "You won't survive the crash.",
        "I'm more than the market can bear.",
        "I've got a real crash course for you!",
        "Now I'll come crashing down.",
        "I'm a real bull in the market.",
        'Looks like the market is going down.',
        'You had better get out quick!',
        'Sell! Sell! Sell!',
        'Shall I lead the recession?',
        "Everybody's getting out, shouldn't you?"],
    'MumboJumbo': [
        'Let me make this perfectly clear.',
        "It's as simple as this.",
        "This is how we're going to do this.",
        'Let me supersize this for you.',
        'You might call this technobabble.',
        'Here are my five-dollar words.',
        'Boy, this is a mouth full.',
        'Some call me bombastic.',
        'Let me just interject this.',
        'I believe these are the right words.'],
    'ParadigmShift': [
        "Watch out! I'm rather shifty.",
        'Prepare to have your paradigm shifted!',
        "Isn't this an interesting paradigm.",
        "You'll get shifted out of place.",
        "I guess it's your shift now.",
        'Your shift is up!',
        "You've never shifted this much in your life.",
        "I'm giving you the bad shift!",
        'Look into my shifty eyes!'],
    'PeckingOrder': [
        "This one's for the birds.",
        'Get ready for a bird bath.',
        "Looks like you're going to hit a birdie.",
        'Some think this attack is fowl.',
        "You're on the bottom of the pecking order.",
        'I bird in my hand is worth ten on your head!',
        'Your order is up; the pecking order!',
        "Why don't I peck on someone my own size? Nah.",
        'Birds of a feather strike together.'],
    'PickPocket': [
        'Let me check your valuables.',
        "Hey, what's that over there?",
        'Like taking candy from a baby.',
        'What a steal.',
        "I'll hold this for you.",
        'Watch my hands at all times.',
        'The hand is quicker than the eye.',
        "There's nothing up my sleeve.",
        'The management is not responsible for lost items.',
        "Finder's keepers.",
        "You'll never see it coming.",
        'One for me, none for you.',
        "Don't mind if I do.",
        "You won't be needing this..."],
    'PinkSlip': [
        'Try not to slip up.',
        "Are you frightened? You've turned pink!",
        'This one will surely slip you up.',
        'Oops, I guess you slipped there, huh?',
        "Watch yourself, wouldn't want to slip!",
        "This one's slippery when wet.",
        "I'll just slip this one in.",
        "Don't mind if you slip by, do you?",
        "Pink isn't really your color.",
        "Here's your pink slip, you're outta here!"],
    'PlayHardball': [
        'So you wanna play hardball?',
        "You don't wanna play hardball with me.",
        'Batter up!',
        'Hey batter, batter!',
        "And here's the pitch...",
        "You're going to need a relief pitcher.",
        "I'm going to knock you out of the park.",
        "Once you get hit, you'll run home.",
        'This is your final inning!',
        "You can't play with me!",
        "I'll strike you out.",
        "I'm throwing you a real curve ball!"],
    'PoundKey': [
        'Time to return some calls.',
        "I'd like to make a collect call.",
        "Ring-a-ling - it's for you!",
        "I've been wanting to drop a pound or two.",
        'I have a lot of clout.',
        'This may cause a slight pounding sensation.',
        "I'll just punch in this number.",
        'Let me call up a little surprise.',
        "I'll ring you up.",
        "O.K. Toon, it's the pound for you."],
    'PowerTie': [
        "I'll call later, you looked tied up.",
        'Are you ready to tie die?',
        "Ladies and gentlemen, it's a tie!",
        'You had better learn how to tie.',
        "I'll have you tongue-tied!",
        "This is the worst tie you'll ever get!",
        'Can you feel the power?',
        'My powers are far too great for you!',
        "I've got the power!",
        "By the powers vested in me, I'll tie you up."],
    'PowerTrip': [
        "Pack your bags, we're taking a little trip.",
        'Did you have a nice trip?',
        "Nice trip, I guess I'll see you next fall.",
        'How was your trip?',
        'Sorry to trip you up there!',
        'You look a little tripped up.',
        "Now you see who's in power!",
        'I am much more powerful than you.',
        "Who's got the power now?",
        "You can't fight the power.",
        'Power corrupts, especially in my hands!'],
    'Quake': [
        "Let's quake, rattle, and roll.",
        "I've got a whole lot of quakin' goin' on!",
        "I see you quakin' in your shoes.",
        "Here it comes, it's the big one!",
        "This one's off the Richter scale.",
        'Now the earth will quake!',
        "Hey, what's shakin'? You!",
        'Ever been in an earthquake?',
        "You're on shaky ground now!"],
    'RazzleDazzle': [
        'Read my lips.',
        'How about these choppers?',
        "Aren't I charming?",
        "I'm going to wow you.",
        'My dentist does excellent work.',
        "Blinding aren't they?",
        "Hard to believe these aren't real.",
        "Shocking, aren't they?",
        "I'm going to cap this off.",
        'I floss after every meal.',
        'Say Cheese!'],
    'RedTape': [
        'This should wrap things up.',
        "I'm going to tie you up for awhile.",
        "You're on a roll.",
        'See if you can cut through this.',
        'This will get sticky.',
        "Hope you're claustrophobic.",
        "I'll make sure you stick around.",
        'Let me keep you busy.',
        'Just try to unravel this.',
        'I want this meeting to stick with you.'],
    'ReOrg': [
        "You don't like the way I reorganized things!",
        'Perhaps a little reorganization is in order.',
        "You're not that bad, you just need to be reorganized.",
        'Do you like my organizational skills.',
        "I just thought I'd give things a new look.",
        'You need to get organized!',
        "You're looking a little disorganized.",
        'Hold on while I reorganize your thoughts.',
        "I'll just wait for you to get a little organized.",
        "You don't mind if I just reorganize a bit?"],
    'RestrainingOrder': [
        'You should show a little restraint.',
        "I'm slapping you with a restraining order!",
        "You can't come within five feet of me.",
        'Perhaps you better keep your distance.',
        'You should be restrained.',
        Cogs + '!  Restrain that Toon!',
        'Try and restrain yourself.',
        "I hope I'm being too much of a restraint on you.",
        'See if you can lift these restraints!',
        "I'm ordering you to restrain!",
        "Why don't we start with basic restraining?"],
    'Rolodex': [
        "Your card's in here somewhere.",
        "Here's the number for a pest exterminator.",
        'I want to give you my card.',
        "I've got your number right here.",
        "I've got you covered from a-z.",
        "You'll flip over this.",
        'Take this for a spin.',
        'Watch out for paper cuts.',
        "I'll let my fingers do the knocking.",
        'Is this how I can contact you?',
        'I want to make sure we stay in touch.'],
    'RubberStamp': [
        'I always make a good impression.',
        "It's important to apply firm and even pressure.",
        'A perfect imprint every time.',
        'I want to stamp you out.',
        'You must be RETURNED TO SENDER.',
        "You've been CANCELLED.",
        'You have a PRIORITY delivery.',
        "I'll make sure you RECEIVED my message.",
        "You're not going anywhere - you have POSTAGE DUE.",
        "I'll need a response ASAP."],
    'RubOut': [
        'And now for my disappearing act.',
        "I sense I've lost you somewhere.",
        'I decided to leave you out.',
        'I always rub out all obstacles.',
        "I'll just erase this error.",
        'I can make any nuisance disappear.',
        'I like things neat and tidy.',
        'Please try and stay animated.',
        "Now I see you...  now I don't.",
        'This will cause some fading.',
        "I'm going to eliminate the problem.",
        'Let me take care of your problem areas.'],
    'Sacked': [
        "Looks like you're getting sacked.",
        "This one's in the bag.",
        "You've been bagged.",
        'Paper or plastic?',
        'My enemies shall be sacked!',
        'I hold the Toontown record in sacks per game.',
        "You're no longer wanted around here.",
        "Your time is up around here, you're being sacked!",
        'Let me bag that for you.',
        'No defense can match my sack attack!'],
    'Schmooze': [
        "You'll never see this coming.",
        'This will look good on you.',
        "You've earned this.",
        "I don't mean to gush.",
        'Flattery will get me everywhere.',
        "I'm going to pile it on now.",
        'Time to lay it on thick.',
        "I'm going to get on your good side.",
        'That deserves a good slap on the back.',
        "I'm going to ring your praises.",
        'I hate to knock you off your pedestal, but...'],
    'Shake': [
        "You're right on the epicenter.",
        "You're standing on a fault line.",
        "It's going to be a bumpy ride.",
        'I think of this as a natural disaster.',
        "It's a disaster of seismic proportions.",
        "This one's off the Richter scale.",
        'Time to duck and cover.',
        'You seem disturbed.',
        'Ready for a jolt?',
        "I'll have you shaken, not stirred.",
        'This will shake you up.',
        'I suggest a good escape plan.'],
    'Shred': [
        'I need to get rid of some hazardous waste.',
        "I'm increasing my throughput.",
        "I think I'll dispose of you right now.",
        'This will get rid of the evidence.',
        "There's no way to prove it now.",
        'See if you can put this back together.',
        'This should cut you down to size.',
        "I'm going to rip that idea to shreds.",
        "We don't want this to fall into the wrong hands.",
        'Easy come, easy go.',
        "Isn't this your last shred of hope?"],
    'Spin': [
        'What do you say we go for a little spin?',
        'Do you use the spin cycle?',
        "This'll really make your head spin!",
        "Here's my spin on things.",
        "I'll take you for a spin.",
        'How do you like to "spin" your time?',
        "Watch it.  Wouldn't want to spin out of control!",
        "Oh what a spin you're in!",
        'My attacks will make your head spin!'],
    'Synergy': [
        "I'm taking this to committee.",
        "Your project's been cancelled.",
        "Your budget's been cut.",
        "We're restructuring your division.",
        'I put it to a vote, and you lose.',
        'I just received the final approval.',
        'A good team can get rid of any problem.',
        "I'll get back to you on this.",
        "Let's get right to business.",
        'Consider this a Synergy crisis.'],
    'Tabulate': [
        "This doesn't add up.",
        'By my count, you lose.',
        "You're racking up quite a tab.",
        "I'll have you totaled in a moment.",
        'Are you ready for these numbers?',
        'Your bill is now due and payable.',
        'Time for the reckoning.',
        'I like to put things in order.',
        'And the tally is...',
        'These numbers should prove to be quite powerful.'],
    'TeeOff': [
        "You're not up to par.",
        'Fore!',
        "I'm getting teed off.",
        "Caddie, I'll need my driver!",
        'Just try and avoid this hazard.',
        'Swing!',
        'This is a sure hole in one.',
        "You're in my fairway.",
        'Notice my grip.',
        'Watch the birdie!',
        'Keep your eye on the ball!',
        'Mind if I play through?'],
    'Tremor': [
        'Did you feel that?',
        'Not afraid of a little tremor are you?',
        'A tremor is only the beginning.',
        'You look jittery.',
        "I'll shake things up a bit!",
        'Are you ready to rumble?',
        "What's wrong? You look shaken.",
        'Tremor with fear!',
        'Why are you tremoring with fear?'],
    'Watercooler': [
        'This ought to cool you off.',
        "Isn't this refreshing?",
        'I deliver.',
        'Straight from the tap - into your lap.',
        "What's the matter, it's just spring water.",
        "Don't worry, it's purified.",
        'Ah, another satisfied customer.',
        "It's time for your daily delivery.",
        "Hope your colors don't run.",
        'Care for a drink?',
        'It all comes out in the wash.',
        "The drink's on you."],
    'Withdrawal': [
        "I believe you're overdrawn.",
        'I hope your balance is high enough for this.',
        'Take that, with interest.',
        'Your balance is dropping.',
        "You're going to need to make a deposit soon.",
        "You've suffered an economic collapse.",
        "I think you're in a slump.",
        'Your finances have taken a decline.',
        'I foresee a definite downturn.',
        "It's a reversal of fortune."],
    'WriteOff': [
        'Let me increase your losses.',
        "Let's make the best of a bad deal.",
        'Time to balance the books.',
        "This won't look good on your books.",
        "I'm looking for some dividends.",
        'You must account for your losses.',
        'You can forget about a bonus.',
        "I'll shuffle your accounts around.",
        "You're about to suffer some losses.",
        'This is going to hurt your bottom line.'] }
BuildingWaitingForVictors = ('Waiting for other players...',)
ElevatorHopOff = 'Hop off'
CogsIncExt = ', Inc.'
CogsIncModifier = '%s' + CogsIncExt
CogsInc = string.upper(Cogs) + CogsIncExt
DoorKnockKnock = 'Knock, knock.'
DoorWhosThere = "Who's there?"
DoorWhoAppendix = ' who?'
DoorNametag = 'Door'
FADoorCodes_UNLOCKED = None
FADoorCodes_TALK_TO_TOM = 'You need gags! Go talk to Tutorial Tom!'
FADoorCodes_DEFEAT_FLUNKY_HQ = 'Come back here when you have defeated the Flunky!'
FADoorCodes_TALK_TO_HQ = 'Go get your reward from HQ Harry!'
FADoorCodes_WRONG_DOOR_HQ = 'Wrong door! Take the other door to the playground!'
FADoorCodes_GO_TO_PLAYGROUND = 'Wrong way! You need to go to the playground!'
FADoorCodes_DEFEAT_FLUNKY_TOM = 'Walk up to that Flunky to battle him!'
FADoorCodes_TALK_TO_HQ_TOM = 'Go get your reward from Toon Headquarters!'
FADoorCodes_SUIT_APPROACHING = None
FADoorCodes_BUILDING_TAKEOVER = "Watch out! There's a Cog in there!"
FADoorCodes_SB_DISGUISE_INCOMPLETE = "You'll get caught going in there as a Toon! You need to complete your Sellbot Disguise first!\n\nBuild your Sellbot Disguise out of parts from the Factory."
FADoorCodes_CB_DISGUISE_INCOMPLETE = "You'll get caught going in there as a Toon! You need to complete your Cashbot Disguise first!\n\nBuild your Cashbot Disguise by doing ToonTasks in Dreamland."
KnockKnockContestJokes = {
    2100: [
        'Wally',
        "Wally's not looking, hit him with a pie!"],
    2200: [
        'Biscuit',
        'Biscuit out of here the Cogs are coming!'],
    2300: [
        'Justin',
        'Justin other couple of Cog parts and off we go!'] }
KnockKnockJokes = [
    [
        'Who',
        "Bad echo in here, isn't there?"],
    [
        'Dozen',
        'Dozen anybody want to let me in?'],
    [
        'Freddie',
        'Freddie or not, here I come.'],
    [
        'Dishes',
        'Dishes your friend, let me in.'],
    [
        'Wooden shoe',
        'Wooden shoe like to know.'],
    [
        'Betty',
        "Betty doesn't know who I am."],
    [
        'Kent',
        'Kent you tell?'],
    [
        'Noah',
        "Noah don't know who either."],
    [
        "I don't know",
        'Neither do I, I keep telling you that.'],
    [
        'Howard',
        'Howard I know?'],
    [
        'Emma',
        'Emma so glad you asked me that.'],
    [
        'Auto',
        "Auto know, but I've forgotten."],
    [
        'Jess',
        'Jess me and my shadow.'],
    [
        'One',
        'One-der why you keep asking that?'],
    [
        'Alma',
        'Alma not going to tell you!'],
    [
        'Zoom',
        'Zoom do you expect?'],
    [
        'Amy',
        "Amy fraid I've forgotten."],
    [
        'Arfur',
        'Arfur got.'],
    [
        'Ewan',
        'No, just me'],
    [
        'Cozy',
        "Cozy who's knocking will you?"],
    [
        'Sam',
        'Sam person who knocked on the door last time.'],
    [
        'Fozzie',
        'Fozzie hundredth time, my name is ' + Flippy + '.'],
    [
        'Deduct',
        Donald + ' Deduct.'],
    [
        'Max',
        'Max no difference, just open the door.'],
    [
        'N.E.',
        'N.E. body you like, let me in.'],
    [
        'Amos',
        'Amos-quito bit me.'],
    [
        'Alma',
        "Alma candy's gone."],
    [
        'Bruce',
        "I Bruce very easily, don't hit me."],
    [
        'Colleen',
        "Colleen up your room, it's filthy."],
    [
        'Elsie',
        'Elsie you later.'],
    [
        'Hugh',
        'Hugh is going to let me in?'],
    [
        'Hugo',
        "Hugo first - I'm scared."],
    [
        'Ida',
        'Ida know.  Sorry!'],
    [
        'Isabel',
        'Isabel on a bike really necessary?'],
    [
        'Joan',
        "Joan call us, we'll call you."],
    [
        'Kay',
        'Kay, L, M, N, O, P.'],
    [
        'Justin',
        'Justin time for dinner.'],
    [
        'Liza',
        'Liza wrong to tell.'],
    [
        'Luke',
        'Luke and see who it is.'],
    [
        'Mandy',
        "Mandy the lifeboats, we're sinking."],
    [
        'Max',
        'Max no difference - just open the door!'],
    [
        'Nettie',
        'Nettie as a fruitcake.'],
    [
        'Olivia',
        'Olivia me alone!'],
    [
        'Oscar',
        'Oscar stupid question, you get a stupid answer.'],
    [
        'Patsy',
        'Patsy dog on the head, he likes it.'],
    [
        'Paul',
        "Paul hard, the door's stuck again."],
    [
        'Thea',
        'Thea later, alligator.'],
    [
        'Tyrone',
        "Tyrone shoelaces, you're old enough."],
    [
        'Stella',
        'Stella no answer at the door.'],
    [
        'Uriah',
        'Keep Uriah on the ball.'],
    [
        'Dwayne',
        "Dwayne the bathtub.  I'm drowning."],
    [
        'Dismay',
        "Dismay be a joke, but it didn't make me laugh."],
    [
        'Ocelot',
        "Ocelot of questions, don't you?"],
    [
        'Thermos',
        'Thermos be a better knock knock joke than this.'],
    [
        'Sultan',
        'Sultan Pepper.'],
    [
        'Vaughan',
        'Vaughan day my prince will come.'],
    [
        'Donald',
        'Donald come baby, cradle and all.'],
    [
        'Lettuce',
        "Lettuce in, won't you?"],
    [
        'Ivor',
        'Ivor sore hand from knocking on your door!'],
    [
        'Isabel',
        'Isabel broken, because I had to knock.'],
    [
        'Heywood, Hugh, Harry',
        'Heywood Hugh Harry up and open this door.'],
    [
        'Juan',
        "Juan of this days you'll find out."],
    [
        'Earl',
        'Earl be glad to tell you if you open this door.'],
    [
        'Abbot',
        'Abbot time you opened this door!'],
    [
        'Ferdie',
        'Ferdie last time, open the door!'],
    [
        'Don',
        'Don mess around, just open the door.'],
    [
        'Sis',
        'Sis any way to treat a friend?'],
    [
        'Isadore',
        'Isadore open or locked?'],
    [
        'Harry',
        'Harry up and let me in!'],
    [
        'Theodore',
        "Theodore wasn't open so I knocked-knocked."],
    [
        'Ken',
        'Ken I come in?'],
    [
        'Boo',
        "There's no need to cry about it."],
    [
        'You',
        'You who!  Is there anybody there?'],
    [
        'Ice cream',
        "Ice cream if you don't let me in."],
    [
        'Sarah',
        "Sarah 'nother way into this building?"],
    [
        'Mikey',
        'Mikey dropped down the drain.'],
    [
        'Doris',
        'Doris jammed again.'],
    [
        'Yelp',
        'Yelp me, the door is stuck.'],
    [
        'Scold',
        'Scold outside.'],
    [
        'Diana',
        'Diana third, can I have a drink please?'],
    [
        'Doris',
        'Doris slammed on my finger, open it quick!'],
    [
        'Lettuce',
        'Lettuce tell you some knock knock jokes.'],
    [
        'Izzy',
        'Izzy come, izzy go.'],
    [
        'Omar',
        'Omar goodness gracious - wrong door!'],
    [
        'Says',
        "Says me, that's who!"],
    [
        'Duck',
        "Just duck, they're throwing things at us."],
    [
        'Tank',
        "You're welcome."],
    [
        'Eyes',
        'Eyes got loads more knock knock jokes for you.'],
    [
        'Pizza',
        'Pizza cake would be great right now.'],
    [
        'Closure',
        'Closure mouth when you eat.'],
    [
        'Harriet',
        "Harriet all my lunch, I'm starving."],
    [
        'Wooden',
        'Wooden you like to know?'],
    [
        'Punch',
        'Not me, please.'],
    [
        'Gorilla',
        'Gorilla me a hamburger.'],
    [
        'Jupiter',
        "Jupiter hurry, or you'll miss the trolley."],
    [
        'Bertha',
        'Happy Bertha to you!'],
    [
        'Cows',
        'Cows go "moo" not "who."'],
    [
        'Tuna fish',
        "You can tune a piano, but you can't tuna fish."],
    [
        'Consumption',
        'Consumption be done about all these knock knock jokes?'],
    [
        'Banana',
        'Banana spilt so ice creamed.'],
    [
        'X',
        'X-tremely pleased to meet you.'],
    [
        'Haydn',
        'Haydn seek is fun to play.'],
    [
        'Rhoda',
        'Rhoda boat as fast as you can.'],
    [
        'Quacker',
        "Quacker 'nother bad joke and I'm off!"],
    [
        'Nana',
        'Nana your business.'],
    [
        'Ether',
        'Ether bunny.'],
    [
        'Little old lady',
        "My, you're good at yodelling!"],
    [
        'Beets',
        'Beets me, I forgot the joke.'],
    [
        'Hal',
        'Halloo to you too!'],
    [
        'Sarah',
        'Sarah doctor in the house?'],
    [
        'Aileen',
        'Aileen Dover and fell down.'],
    [
        'Atomic',
        'Atomic ache'],
    [
        'Agatha',
        'Agatha headache.  Got an aspirin?'],
    [
        'Stan',
        "Stan back, I'm going to sneeze."],
    [
        'Hatch',
        'Bless you.'],
    [
        'Ida',
        "It's not Ida who, it's Idaho."],
    [
        'Zippy',
        'Mrs. Zippy.'],
    [
        'Yukon',
        'Yukon go away and come back another time.']]
SharedChatterGreetings = [
    'Hi, %!',
    'Yoo-hoo %, nice to see you.',
    "I'm glad you're here today!",
    'Well, hello there, %.']
SharedChatterComments = [
    "That's a great name, %.",
    'I like your name.',
    'Watch out for the ' + Cogs + '.',
    'Looks like the trolley is coming!',
    'I need to play a trolley game to get some pies!',
    'Sometimes I play trolley games just to eat the fruit pie!',
    'Whew, I just stopped a bunch of ' + Cogs + '. I need a rest!',
    'Yikes, some of those ' + Cogs + ' are big guys!',
    "You look like you're having fun.",
    "Oh boy, I'm having a good day.",
    "I like what you're wearing.",
    "I think I'll go fishing this afternoon.",
    'Have fun in my neighborhood.',
    'I hope you are enjoying your stay in Toontown!',
    "I heard it's snowing at the Brrrgh.",
    'Have you ridden the trolley today?',
    'I like to meet new people.',
    'Wow, there are lots of ' + Cogs + ' in the Brrrgh.',
    'I love to play tag. Do you?',
    'Trolley games are fun to play.',
    'I like to make people laugh.',
    "It's fun helping my friends.",
    "A-hem, are you lost?  Don't forget your map is in your shticker book.",
    'Try not to get tied up in the ' + Cogs + "' Red Tape.",
    'I hear ' + Daisy + ' has planted some new flowers in her garden.',
    'If you press the Page Up key, you can look up!',
    'If you help take over Cog buildings, you can earn a bronze star!',
    'If you press the Tab key, you can see different views of your surroundings!',
    'If you press the Ctrl key, you can jump!']
SharedChatterGoodbyes = [
    'I have to go now, bye!',
    "I think I'll go play a trolley game.",
    "Well, so long. I'll be seeing you, %!",
    "I'd better hurry and get to work stopping those " + Cogs + '.',
    "It's time for me to get going.",
    'Sorry, but I have to go.',
    'Good-bye.',
    'See you later, %!',
    "I think I'm going to go practice tossing cupcakes.",
    "I'm going to join a group and stop some " + Cogs + '.',
    'It was nice to see you today, %.',
    "I have a lot to do today. I'd better get busy."]
MickeyChatter = ([
    'Welcome to ' + lToontownCentral + '.',
    'Hi, my name is ' + Mickey + ". What's yours?"], [
    'Hey, have you seen ' + Donald + '?',
    "I'm going to go watch the fog roll in at " + lDonaldsDock + '.',
    'If you see my pal ' + Goofy + ', say hi to him for me.',
    'I hear ' + Daisy + ' has planted some new flowers in her garden.'], [
    "I'm going to MelodyLand to see " + Minnie + '!',
    "Gosh, I'm late for my date with " + Minnie + '!',
    "Looks like it's time for " + Pluto + "'s dinner.",
    "I think I'll go swimming at " + lDonaldsDock + '.',
    "It's time for a nap. I'm going to Dreamland."])
MinnieChatter = ([
    'Welcome to Melodyland.',
    'Hi, my name is ' + Minnie + ". What's yours?"], [
    'The hills are alive with the sound of music!',
    'You have a cool outfit, %.',
    'Hey, have you seen ' + Mickey + '?',
    'If you see my friend ' + Goofy + ', say hi to him for me.',
    'Wow, there are lots of ' + Cogs + ' near ' + Donald + "'s Dreamland.",
    "I heard it's foggy at the " + lDonaldsDock + '.',
    'Be sure and try the maze in ' + lDaisyGardens + '.',
    "I think I'll go catch some tunes.",
    'Hey %, look at that over there.',
    'I love the sound of music.',
    "I bet you didn't know Melodyland is also called TuneTown!  Hee Hee!",
    'I love to play the Matching Game. Do you?',
    'I like to make people giggle.',
    'Boy, trotting around in heels all day is hard on your feet!',
    'Nice shirt, %.',
    'Is that a jellybean on the ground?'], [
    "Gosh, I'm late for my date with %s!" % Mickey,
    "Looks like it's time for %s's dinner." % Pluto,
    "It's time for a nap. I'm going to Dreamland."])
GoofyChatter = ([
    'Welcome to ' + lDaisyGardens + '.',
    'Hi, my name is ' + Goofy + ". What's yours?",
    "Gawrsh, it's nice to see you %!"], [
    'Boy it sure is easy to get lost in the garden maze!',
    'Be sure and try the maze here.',
    "I haven't seen " + Daisy + ' all day.',
    'I wonder where ' + Daisy + ' is.',
    'Hey, have you seen ' + Donald + '?',
    'If you see my friend ' + Mickey + ', say hi to him for me.',
    "D'oh! I forgot to fix " + Mickey + "'s breakfast!",
    'Gawrsh there sure are a lot of ' + Cogs + ' near ' + lDonaldsDock + '.',
    'It looks like ' + Daisy + ' has planted some new flowers in her garden.',
    'At the Brrrgh branch of my Gag Shop, Hypno-Goggles are on sale for only 1 jellybean!',
    "Goofy's Gag Shops offer the best jokes, tricks, and funnybone-ticklers in all of Toontown!",
    "At Goofy's Gag Shops, every pie in the face is guaranteed to make a laugh or you get your jellybeans back!"], [
    "I'm going to Melody Land to see %s!" % Mickey,
    "Gosh, I'm late for my game with %s!" % Donald,
    "I think I'll go swimming at " + lDonaldsDock + '.',
    "It's time for a nap. I'm going to Dreamland."])
DonaldChatter = ([
    'Welcome to Dreamland.',
    "Hi, my name is %s. What's yours?" % Donald], [
    'Sometimes this place gives me the creeps.',
    'Be sure and try the maze in ' + Daisy + ' Gardens.',
    "Oh boy, I'm having a good day.",
    'Hey, have you seen ' + Mickey + '?',
    'If you see my buddy ' + Goofy + ', say hi to him for me.',
    "I think I'll go fishing this afternoon.",
    'Wow, there are lots of ' + Cogs + ' at ' + lDonaldsDock + '.',
    "Hey, didn't I take you on a boat ride at " + lDonaldsDock + '?',
    "I haven't seen " + Daisy + ' all day.',
    'I hear ' + Daisy + ' has planted some new flowers in her garden.',
    'Quack.'], [
    "I'm going to Melody Land to see %s!" % Minnie,
    "Gosh, I'm late for my date with %s!" % Daisy,
    "I think I'll go swimming at my dock.",
    "I think I'll take my boat for a spin at my dock."])
for chatter in [
    MickeyChatter,
    DonaldChatter,
    MinnieChatter,
    GoofyChatter]:
    chatter[0].extend(SharedChatterGreetings)
    chatter[1].extend(SharedChatterComments)
    chatter[2].extend(SharedChatterGoodbyes)

FriendsListPanelNewFriend = 'New Friend'
FriendsListPanelSecrets = 'Secrets'
FriendsListPanelOnlineFriends = 'ONLINE\nFRIENDS'
FriendsListPanelAllFriends = 'ALL\nFRIENDS'
FriendsListPanelIgnoredFriends = 'IGNORED\nTOONS'
FriendsListPanelPets = 'NEARBY\nPETS'
DownloadForceAcknowledgeMsg = "Sorry, you can't advance because %(phase)s download is only %(percent)s%% complete.\n\nPlease try again later."
TeaserTop = "  Sorry, but you can't do that in the free trial.\n\nSubscribe now and enjoy these great features:"
TeaserOtherHoods = 'Visit all 6 unique neighborhoods!'
TeaserTypeAName = 'Type in your favorite name for your toon!'
TeaserSixToons = 'Create up to 6 Toons on one account!'
TeaserOtherGags = 'Collect 6 skill levels in 6 different gag tracks!'
TeaserClothing = 'Buy unique clothing items to individualize your toon!'
TeaserFurniture = 'Purchase and arrange furniture in your own house!'
TeaserCogHQ = 'Infiltrate dangerous advanced Cog areas!'
TeaserSecretChat = 'Trade secrets with friends so you can chat with them online!'
TeaserCardsAndPosters = 'Receive a welcome pack and monthly newsletters\nwith posters and other cool stuff!'
TeaserHolidays = 'Participate in exciting special events and holiday celebrations!'
TeaserQuests = 'Complete hundreds of ToonTasks to help save Toontown!'
TeaserEmotions = 'Purchase emotions to make your Toon more expressive!'
TeaserMinigames = 'Play all 8 minigame varieties!'
TeaserSubscribe = 'Subscribe Now'
TeaserContinue = 'Continue Trial'
DownloadWatcherUpdate = 'Downloading %s'
DownloadWatcherInitializing = 'Download Initializing...'
LauncherPhaseNames = {
    0: 'Initialization',
    3: 'Make-A-Toon',
    3.5: 'Toontorial',
    4: 'Playground',
    5: 'Streets',
    5.5: 'Estates',
    6: 'Neighborhoods I',
    7: Cog + ' Buildings',
    8: 'Neighborhoods II',
    9: Sellbot + ' HQ',
    10: Cashbot + ' HQ' }
LauncherProgress = '%(name)s (%(current)s of %(total)s)'
LauncherStartingMessage = "Starting Disney's Toontown Online... "
LauncherDownloadFile = 'Downloading update for ' + LauncherProgress + '...'
LauncherDownloadFileBytes = 'Downloading update for ' + LauncherProgress + ': %(bytes)s'
LauncherDownloadFilePercent = 'Downloading update for ' + LauncherProgress + ': %(percent)s%%'
LauncherDecompressingFile = 'Decompressing update for ' + LauncherProgress + '...'
LauncherDecompressingPercent = 'Decompressing update for ' + LauncherProgress + ': %(percent)s%%'
LauncherExtractingFile = 'Extracting update for ' + LauncherProgress + '...'
LauncherExtractingPercent = 'Extracting update for ' + LauncherProgress + ': %(percent)s%%'
LauncherPatchingFile = 'Applying update for ' + LauncherProgress + '...'
LauncherPatchingPercent = 'Applying update for ' + LauncherProgress + ': %(percent)s%%'
LauncherConnectProxyAttempt = 'Connecting to Toontown: %s (proxy: %s) attempt: %s'
LauncherConnectAttempt = 'Connecting to Toontown: %s attempt %s'
LauncherDownloadServerFileList = 'Updating Toontown...'
LauncherCreatingDownloadDb = 'Updating Toontown...'
LauncherDownloadClientFileList = 'Updating Toontown...'
LauncherFinishedDownloadDb = 'Updating Toontown... '
LauncherStartingToontown = 'Starting Toontown...'
LauncherRecoverFiles = 'Updating Toontown. Recovering files...'
LauncherCheckUpdates = 'Checking for updates for ' + LauncherProgress
LauncherVerifyPhase = 'Updating Toontown...'
AvatarChoiceMakeAToon = 'Make A\nToon'
AvatarChoicePlayThisToon = 'Play\nThis Toon'
AvatarChoiceSubscribersOnly = 'Subscribe\n\n\n\nNow!'
AvatarChoiceDelete = 'Delete'
AvatarChoiceDeleteConfirm = 'This will delete %s forever.'
AvatarChoiceNameRejected = 'Name\nRejected'
AvatarChoiceNameApproved = 'Name\nApproved!'
AvatarChoiceNameReview = 'Under\nReview'
AvatarChoiceNameYourToon = 'Name\nYour Toon!'
AvatarChoiceDeletePasswordText = 'Careful! This will delete %s forever.  To delete this Toon, enter your password.'
AvatarChoiceDeleteConfirmText = 'Careful! This will delete %(name)s forever.  If you are sure you want to do this, type "%(confirm)s" and click OK.'
AvatarChoiceDeleteConfirmUserTypes = 'delete'
AvatarChoiceDeletePasswordTitle = 'Delete Toon?'
AvatarChoicePassword = 'Password'
AvatarChoiceDeletePasswordOK = lOK
AvatarChoiceDeletePasswordCancel = lCancel
AvatarChoiceDeleteWrongPassword = 'That password does not seem to match.  To delete this Toon, enter your password.'
AvatarChoiceDeleteWrongConfirm = 'You did not type the right thing.  To delete %(name)s, type "%(confirm)s" and click OK.  Do not type the quotation marks.  Click Cancel if you have changed your mind.'
AvatarChooserPickAToon = 'Pick  A  Toon  To  Play'
AvatarChooserQuit = lQuit
TTAccountCallCustomerService = 'Please call Customer Service at %s.'
TTAccountCustomerServiceHelp = '\nIf you need help, please call Customer Service at %s.'
TTAccountIntractibleError = 'An error occurred.'
DateOfBirthEntryMonths = [
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    'Oct',
    'Nov',
    'Dec']
DateOfBirthEntryDefaultLabel = 'Date of Birth'
AchievePageTitle = 'Achievements\n(Coming Soon)'
PhotoPageTitle = 'Photo\n(Coming Soon)'
BuildingPageTitle = 'Buildings\n(Coming Soon)'
InventoryPageTitle = 'Gags'
InventoryPageDeleteTitle = 'DELETE GAGS'
InventoryPageTrackFull = 'You have all the gags in the %s track.'
InventoryPagePluralPoints = 'You will get a new\n%(trackName)s gag when you\nget %(numPoints)s more %(trackName)s points.'
InventoryPageSinglePoint = 'You will get a new\n%(trackName)s gag when you\nget %(numPoints)s more %(trackName)s point.'
InventoryPageNoAccess = 'You do not have access to the %s track yet.'
NPCFriendPageTitle = 'SOS Toons'
MapPageTitle = 'Map'
MapPageBackToPlayground = 'Back to Playground'
MapPageBackToCogHQ = 'Back to Cog Headquarters'
MapPageGoHome = 'Go Home'
MapPageYouAreHere = 'You are in: %s\n%s'
MapPageYouAreAtHome = 'You are at\nyour estate'
MapPageYouAreAtSomeonesHome = 'You are at %s estate'
MapPageGoTo = 'Go To\n%s'
OptionsPageTitle = 'Options'
OptionsPagePurchase = 'Subscribe Now!'
OptionsPageLogout = 'Logout'
OptionsPageExitToontown = 'Exit Toontown'
OptionsPageMusicOnLabel = 'Music is on.'
OptionsPageMusicOffLabel = 'Music is off.'
OptionsPageSFXOnLabel = 'Sound Effects are on.'
OptionsPageSFXOffLabel = 'Sound Effects are off.'
OptionsPageFriendsEnabledLabel = 'Accepting new friend requests.'
OptionsPageFriendsDisabledLabel = 'Not accepting friend requests.'
OptionsPageSpeedChatStyleLabel = 'SpeedChat Color'
OptionsPageDisplayWindowed = 'windowed'
OptionsPageSelect = 'Select'
OptionsPageToggleOn = 'Turn On'
OptionsPageToggleOff = 'Turn Off'
OptionsPageChange = 'Change'
OptionsPageDisplaySettings = 'Display: %(screensize)s, %(api)s'
OptionsPageDisplaySettingsNoApi = 'Display: %(screensize)s'
OptionsPageExitConfirm = 'Exit Toontown?'
DisplaySettingsTitle = 'Display Settings'
DisplaySettingsIntro = 'The following settings are used to configure the way Toontown is displayed on your computer.  It is probably not necessary to adjust these unless you are experiencing a problem.'
DisplaySettingsIntroSimple = 'You may adjust the screen resolution to a higher value to improve the clarity of text and graphics in Toontown, but depending on your graphics card, some higher values may make the game run less smoothly or may not work at all.'
DisplaySettingsApi = 'Graphics API:'
DisplaySettingsResolution = 'Resolution:'
DisplaySettingsWindowed = 'In a window'
DisplaySettingsFullscreen = 'Full screen'
DisplaySettingsApply = 'Apply'
DisplaySettingsCancel = lCancel
DisplaySettingsApplyWarning = 'When you press OK, the display settings will change.  If the new configuration does not display properly on your computer, the display will automatically return to its original configuration after %s seconds.'
DisplaySettingsAccept = 'Press OK to keep the new settings, or Cancel to revert.  If you do not press anything, the settings will automatically revert back in %s seconds.'
DisplaySettingsRevertUser = 'Your previous display settings have been restored.'
DisplaySettingsRevertFailed = 'The selected display settings do not work on your computer.  Your previous display settings have been restored.'
TrackPageTitle = 'Gag Track Training'
TrackPageShortTitle = 'Gag Training'
TrackPageSubtitle = 'Complete ToonTasks to learn how to use new Gags!'
TrackPageTraining = 'You are training to use %s Gags.\nWhen you complete all 16 tasks you\nwill be able to use %s Gags in battle.'
TrackPageClear = 'You are not training any Gag Tracks now.'
TrackPageFilmTitle = '%s\nTraining\nFilm'
TrackPageDone = 'FIN'
QuestPageToonTasks = 'ToonTasks'
QuestPageChoose = 'Choose'
QuestPageDestination = '%s\n%s\n%s'
QuestPageNameAndDestination = '%s\n%s\n%s\n%s'
QuestPosterHQOfficer = lHQOfficerM
QuestPosterHQBuildingName = 'Toon HQ'
QuestPosterHQStreetName = 'Any Street'
QuestPosterHQLocationName = 'Any Neighborhood'
QuestPosterTailor = 'Tailor'
QuestPosterTailorBuildingName = 'Clothing Store'
QuestPosterTailorStreetName = 'Any Playground'
QuestPosterTailorLocationName = 'Any Neighborhood'
QuestPosterPlayground = 'In the playground'
QuestPosterAtHome = 'At your home'
QuestPosterInHome = 'In your home'
QuestPosterOnPhone = 'On your phone'
QuestPosterEstate = 'At your estate'
QuestPosterAnywhere = 'Anywhere'
QuestPosterAuxTo = 'to:'
QuestPosterAuxFrom = 'from:'
QuestPosterAuxFor = 'for:'
QuestPosterAuxOr = 'or:'
QuestPosterAuxReturnTo = 'Return to:'
QuestPosterLocationIn = ' in '
QuestPosterLocationOn = ' in '
QuestPosterFun = 'Just for fun!'
QuestPosterFishing = 'GO FISHING'
QuestPosterComplete = 'COMPLETE'
ShardPageTitle = 'Districts'
ShardPageHelpIntro = 'Each District is a copy of the Toontown world.'
ShardPageHelpWhere = '  You are currently in the "%s" District.'
ShardPageHelpWelcomeValley = '  You are currently in the "Welcome Valley" District, within "%s".'
ShardPageHelpMove = '  To move to a new District, click on its name.'
ShardPagePopulationTotal = 'Total Toontown Population:\n%d'
ShardPageScrollTitle = 'Name            Population'
SuitPageTitle = 'Cog Gallery'
SuitPageMystery = '???'
SuitPageQuota = '%s of %s'
SuitPageCogRadar = '%s present'
SuitPageBuildingRadarS = '%s building'
SuitPageBuildingRadarP = '%s buildings'
DisguisePageTitle = Cog + ' Disguise'
DisguisePageMeritAlert = 'Ready for\npromotion!'
DisguisePageCogLevel = 'Level %s'
DisguisePageMeritFull = 'Full'
FishPageTitle = 'Fishing'
FishPageTitleTank = 'Fish Bucket'
FishPageTitleCollection = 'Fish Album'
FishPageTitleTrophy = 'Fishing Trophies'
FishPageWeightStr = 'Weight: '
FishPageWeightLargeS = '%d lb. '
FishPageWeightLargeP = '%d lbs. '
FishPageWeightSmallS = '%d oz.'
FishPageWeightSmallP = '%d oz.'
FishPageWeightConversion = 16
FishPageValueS = 'Value: %d jellybean'
FishPageValueP = 'Value: %d jellybeans'
FishPageCollectedTotal = 'Fish Species Collected: %d of %d'
FishPageRodInfo = '%s Rod\n%d - %d Pounds'
FishPageTankTab = 'Bucket'
FishPageCollectionTab = 'Album'
FishPageTrophyTab = 'Trophies'
FishPickerTotalValue = 'Bucket: %s / %s\nValue: %d Jellybeans'
UnknownFish = '???'
FishingRod = '%s Rod'
FishingRodNameDict = {
    0: 'Twig',
    1: 'Bamboo',
    2: 'Hardwood',
    3: 'Steel',
    4: 'Gold' }
FishTrophyNameDict = {
    0: 'Guppy',
    1: 'Minnow',
    2: 'Fish',
    3: 'Flying Fish',
    4: 'Shark',
    5: 'Swordfish',
    6: 'Killer Whale' }
QuestChoiceGuiCancel = lCancel
TrackChoiceGuiChoose = 'Choose'
TrackChoiceGuiCancel = lCancel
TrackChoiceGuiHEAL = 'Toonup lets you heal other Toons in battle.'
TrackChoiceGuiTRAP = 'Traps are powerful gags that must be used with Lure.'
TrackChoiceGuiLURE = 'Use Lure to stun Cogs or draw them into traps.'
TrackChoiceGuiSOUND = 'Sound gags affect all Cogs, but are not very powerful.'
TrackChoiceGuiDROP = 'Drop gags do lots of damage, but are not very accurate.'
EmotePageTitle = 'Expressions / Emotions'
EmotePageDance = 'You have built the following dance sequence:'
EmoteJump = 'Jump'
EmoteDance = 'Dance'
EmoteHappy = 'Happy'
EmoteSad = 'Sad'
EmoteAnnoyed = 'Annoyed'
EmoteSleep = 'Sleepy'
SuitBaseNameWithLevel = '%(name)s\n%(dept)s\nLevel %(level)s'
HealthForceAcknowledgeMessage = 'You cannot leave the playground until your Laffmeter is smiling!'
InventoryTotalGags = 'Total Gags\n%d / %d'
InventoryDelete = 'DELETE'
InventoryDone = 'DONE'
InventoryDeleteHelp = 'Click on a gag to DELETE it.'
InventorySkillCredit = 'Skill credit: %s'
InventorySkillCreditNone = 'Skill credit: None'
InventoryDetailAmount = '%(numItems)s / %(maxItems)s'
InventoryDetailData = 'Accuracy: %(accuracy)s\n%(damageString)s: %(damage)d\n%(singleOrGroup)s'
InventoryTrackExp = '%(curExp)s / %(nextExp)s'
InventoryAffectsOneCog = 'Affects: One ' + Cog
InventoryAffectsOneToon = 'Affects: One Toon'
InventoryAffectsAllToons = 'Affects: All Toons'
InventoryAffectsAllCogs = 'Affects: All ' + Cogs
InventoryHealString = 'Toon-up'
InventoryDamageString = 'Damage'
InventoryBattleMenu = 'BATTLE MENU'
InventoryRun = 'RUN'
InventorySOS = 'SOS'
InventoryPass = 'PASS'
InventoryClickToAttack = 'Click a\ngag to\nattack'
NPCForceAcknowledgeMessage = "You must ride the trolley before leaving.\n\n\n\n\n\n\n\n\nYou can find the trolley next to Goofy's Gag Shop."
NPCForceAcknowledgeMessage2 = 'You must return to Toon Headquarters before leaving.\n\n\n\n\n\n\n\n\n\nToon Headquarters is located near the center of the playground.'
NPCForceAcknowledgeMessage3 = "Remember to ride the trolley.\n\n\n\n\n\n\n\nYou can find the trolley next to Goofy's Gag Shop."
NPCForceAcknowledgeMessage4 = 'Congratulations!  You found and rode the trolley!\n\n\n\n\n\n\n\n\n\nNow report back to Toon Headquarters.'
NPCForceAcknowledgeMessage5 = "Don't forget your ToonTask!\n\n\n\n\n\n\n\n\n\n\nYou can find Cogs to defeat on the other side of tunnels like this."
NPCForceAcknowledgeMessage6 = 'Great job defeating those Cogs!\n\n\n\n\n\n\n\n\nHead back to Toon Headquarters as soon as possible.'
NPCForceAcknowledgeMessage7 = "Don't forget to make a friend!\n\n\n\n\n\n\nClick on another player and use the New Friend button."
NPCForceAcknowledgeMessage8 = 'Great! You made a new friend!\n\n\n\n\n\n\n\n\nYou should go back at Toon Headquarters now.'
NPCForceAcknowledgeMessage9 = 'Good job using the phone!\n\n\n\n\n\n\n\n\nReturn to Toon Headquarters to claim your reward.'
ToonSleepString = '. . . ZZZ . . .'
MovieTutorialReward1 = 'You received 1 Throw point! When you get 10, you will get a new gag!'
MovieTutorialReward2 = 'You received 1 Squirt point! When you get 10, you will get a new gag!'
MovieTutorialReward3 = 'Good job! You completed your first ToonTask!'
MovieTutorialReward4 = 'Go to Toon Headquarters for your reward!'
MovieTutorialReward5 = 'Have fun!'
BattleGlobalTracks = [
    'toon-up',
    'trap',
    'lure',
    'sound',
    'throw',
    'squirt',
    'drop']
BattleGlobalNPCTracks = [
    'restock',
    'toons hit',
    'cogs miss']
BattleGlobalAvPropStrings = (('Feather', 'Megaphone', 'Lipstick', 'Bamboo Cane', 'Pixie Dust', 'Juggling Balls'), ('Banana Peel', 'Rake', 'Marbles', 'Quicksand', 'Trapdoor', 'TNT'), ('$1 bill', 'Small Magnet', '$5 bill', 'Big Magnet', '$10 bill', 'Hypno-goggles'), ('Bike Horn', 'Whistle', 'Bugle', 'Aoogah', 'Elephant Trunk', 'Foghorn'), ('Cupcake', 'Fruit Pie Slice', 'Cream Pie Slice', 'Whole Fruit Pie', 'Whole Cream Pie', 'Birthday Cake'), ('Squirting Flower', 'Glass of Water', 'Squirt Gun', 'Seltzer Bottle', 'Fire Hose', 'Storm Cloud'), ('Flower Pot', 'Sandbag', 'Anvil', 'Big Weight', 'Safe', 'Grand Piano'))
BattleGlobalAvPropStringsSingular = (('a Feather', 'a Megaphone', 'a Lipstick', 'a Bamboo Cane', 'a Pixie Dust', 'a set of Juggling Balls'), ('a Banana Peel', 'a Rake', 'a set of Marbles', 'a patch of Quicksand', 'a Trapdoor', 'a TNT'), ('a $1 bill', 'a Small Magnet', 'a $5 bill', 'a Big Magnet', 'a $10 bill', 'a pair of Hypno-goggles'), ('a Bike Horn', 'a Whistle', 'a Bugle', 'an Aoogah', 'an Elephant Trunk', 'a Foghorn'), ('a Cupcake', 'a Fruit Pie Slice', 'a Cream Pie Slice', 'a Whole Fruit Pie', 'a Whole Cream Pie', 'a Birthday Cake'), ('a Squirting Flower', 'a Glass of Water', 'a Squirt Gun', 'a Seltzer Bottle', 'a Fire Hose', 'a Storm Cloud'), ('a Flower Pot', 'a Sandbag', 'an Anvil', 'a Big Weight', 'a Safe', 'a Grand Piano'))
BattleGlobalAvPropStringsPlural = (('Feathers', 'Megaphones', 'Lipsticks', 'Bamboo Canes', 'Pixie Dusts', 'sets of Juggling Balls'), ('Banana Peels', 'Rakes', 'sets of Marbles', 'patches of Quicksand', 'Trapdoors', 'TNTs'), ('$1 bills', 'Small Magnets', '$5 bills', 'Big Magnets', '$10 bills', 'pairs of Hypno-goggles'), ('Bike Horns', 'Whistles', 'Bugles', 'Aoogahs', 'Elephant Trunks', 'Foghorns'), ('Cupcakes', 'Fruit Pie Slices', 'Cream Pie Slices', 'Whole Fruit Pies', 'Whole Cream Pies', 'Birthday Cakes'), ('Squirting Flowers', 'Glasses of Water', 'Squirt Guns', 'Seltzer Bottles', 'Fire Hoses', 'Storm Clouds'), ('Flower Pots', 'Sandbags', 'Anvils', 'Big Weights', 'Safes', 'Grand Pianos'))
BattleGlobalAvTrackAccStrings = ('Medium', 'Perfect', 'Low', 'High', 'Medium', 'High', 'Low')
AttackMissed = 'MISSED'
NPCCallButtonLabel = 'CALL'
GlobalStreetNames = {
    20000: ('to', 'on', 'Tutorial Terrace'),
    1000: ('to the', 'in the', 'Playground'),
    1100: ('to', 'on', 'Barnacle Boulevard'),
    1200: ('to', 'on', 'Seaweed Street'),
    1300: ('to', 'on', 'Lighthouse Lane'),
    2000: ('to the', 'in the', 'Playground'),
    2100: ('to', 'on', 'Silly Street'),
    2200: ('to', 'on', 'Loopy Lane'),
    2300: ('to', 'on', 'Punchline Place'),
    3000: ('to the', 'in the', 'Playground'),
    3100: ('to', 'on', 'Walrus Way'),
    3200: ('to', 'on', 'Sleet Street'),
    4000: ('to the', 'in the', 'Playground'),
    4100: ('to', 'on', 'Alto Avenue'),
    4200: ('to', 'on', 'Baritone Boulevard'),
    4300: ('to', 'on', 'Tenor Terrace'),
    5000: ('to the', 'in the', 'Playground'),
    5100: ('to', 'on', 'Elm Street'),
    5200: ('to', 'on', 'Maple Street'),
    5300: ('to', 'on', 'Oak Street'),
    9000: ('to the', 'in the', 'Playground'),
    9100: ('to', 'on', 'Lullaby Lane'),
    9200: ('to', 'on', 'Pajama Place'),
    10000: ('to', 'in', 'Bossbot HQ'),
    10100: ('to the', 'in the', 'Bossbot HQ Lobby'),
    11000: ('to the', 'in the', 'Sellbot HQ Courtyard'),
    11100: ('to the', 'in the', 'Sellbot HQ Lobby'),
    11200: ('to the', 'in the', 'Sellbot Factory'),
    11500: ('to the', 'in the', 'Sellbot Factory'),
    12000: ('to', 'in', 'Cashbot Train Yard'),
    12100: ('to the', 'in the', 'Cashbot HQ Lobby'),
    12500: ('to the', 'in the', 'Cashbot Coin Mint'),
    12600: ('to the', 'in the', 'Cashbot Dollar Mint'),
    12700: ('to the', 'in the', 'Cashbot Bullion Mint'),
    13000: ('to', 'in', 'Lawbot HQ'),
    13100: ('to the', 'in the', 'Lawbot HQ Lobby') }
DonaldsDock = ('to', 'in', lDonaldsDock)
ToontownCentral = ('to', 'in', lToontownCentral)
TheBrrrgh = ('to', 'in', lTheBrrrgh)
MinniesMelodyland = ('to', 'in', lMinniesMelodyland)
DaisyGardens = ('to', 'in', lDaisyGardens)
ConstructionZone = ('to the', 'in the', 'Construction Zone')
FunnyFarm = ('to the', 'in the', 'Funny Farm')
GoofyStadium = ('to', 'in', 'Goofy Stadium')
DonaldsDreamland = ('to', 'in', lDonaldsDreamland)
BossbotHQ = ('to', 'in', 'Bossbot HQ')
SellbotHQ = ('to', 'in', 'Sellbot HQ')
CashbotHQ = ('to', 'in', 'Cashbot HQ')
LawbotHQ = ('to', 'in', 'Lawbot HQ')
Tutorial = ('to the', 'in the', 'Toon-torial')
MyEstate = ('to', 'in', 'your house')
WelcomeValley = ('to', 'in', 'Welcome Valley')
Factory = 'Factory'
Headquarters = 'Headquarters'
SellbotFrontEntrance = 'Front Entrance'
SellbotSideEntrance = 'Side Entrance'
FactoryNames = {
    0: 'Factory Mockup',
    11500: 'Sellbot Cog Factory' }
FactoryTypeLeg = 'Leg'
FactoryTypeArm = 'Arm'
FactoryTypeTorso = 'Torso'
MintFloorTitle = 'Floor %s'
LoaderLabel = 'Loading...'
HeadingToHood = 'Heading %s %s...'
HeadingToYourEstate = 'Heading to your estate...'
HeadingToEstate = "Heading to %s's estate..."
HeadingToFriend = "Heading to %s's friend's estate..."
HeadingToPlayground = 'Heading to the Playground...'
HeadingToStreet = 'Heading %s %s...'
TownBattleRun = 'Run all the way back to the playground?'
TownBattleChooseAvatarToonTitle = 'WHICH TOON?'
TownBattleChooseAvatarCogTitle = 'WHICH ' + string.upper(Cog) + '?'
TownBattleChooseAvatarBack = 'BACK'
TownBattleSOSNoFriends = 'No friends to call!'
TownBattleSOSWhichFriend = 'Call which friend?'
TownBattleSOSNPCFriends = 'Rescued Toons'
TownBattleSOSBack = 'BACK'
TownBattleToonSOS = 'SOS'
TownBattleUndecided = '?'
TownBattleHealthText = '%(hitPoints)s/%(maxHit)s'
TownBattleWaitTitle = 'Waiting for\nother players...'
TownSoloBattleWaitTitle = 'Please wait...'
TownBattleWaitBack = 'BACK'
TownBattleSOSPetSearchTitle = 'Searching for doodle\n%s...'
TownBattleSOSPetInfoTitle = '%s is %s'
TownBattleSOSPetInfoOK = lOK
TrolleyHFAMessage = 'You may not board the trolley until your laffmeter is smiling.'
TrolleyTFAMessage = 'You may not board the trolley until ' + Mickey + ' says so.'
TrolleyHopOff = 'Hop off'
FishingExit = 'Exit'
FishingCast = 'Cast'
FishingAutoReel = 'Auto Reel'
FishingItemFound = 'You caught:'
FishingCrankTooSlow = 'Too\nslow'
FishingCrankTooFast = 'Too\nfast'
FishingFailure = "You didn't catch anything!"
FishingFailureTooSoon = "Don't start to reel in the line until you see a nibble.  Wait for your float to bob up and down rapidly!"
FishingFailureTooLate = 'Be sure to reel in the line while the fish is still nibbling!'
FishingFailureAutoReel = "The auto-reel didn't work this time.  Turn the crank by hand, at just the right speed, for your best chance to catch something!"
FishingFailureTooSlow = 'You turned the crank too slowly.  Some fish are faster than others.  Try to keep the speed bar centered!'
FishingFailureTooFast = 'You turned the crank too quickly.  Some fish are slower than others.  Try to keep the speed bar centered!'
FishingOverTankLimit = 'Your fish bucket is full. Go sell your fish to the Pet Shop Clerk and come back.'
FishingBroke = 'You do not have any more jellybeans for bait! Ride the trolley or sell fish to the Pet Shop Clerks to earn more jellybeans.'
FishingHowToFirstTime = 'Click and drag down from the Cast button. The farther down you drag, the stronger your cast will be. Adjust your angle to hit the fish targets.\n\nTry it now!'
FishingHowToFailed = 'Click and drag down from the Cast button. The farther down you drag, the stronger your cast will be. Adjust your angle to hit the fish targets.\n\nTry it again now!'
FishingBootItem = 'An old boot'
FishingJellybeanItem = '%s Jellybeans'
FishingNewEntry = 'New Species!'
FishingNewRecord = 'New Record!'
FishPokerCashIn = 'Cash In\n%s\n%s'
FishPokerLock = 'Lock'
FishPokerUnlock = 'Unlock'
FishPoker5OfKind = '5 of a Kind'
FishPoker4OfKind = '4 of a Kind'
FishPokerFullHouse = 'Full House'
FishPoker3OfKind = '3 of a Kind'
FishPoker2Pair = '2 Pair'
FishPokerPair = 'Pair'
TutorialGreeting1 = 'Hi %s!'
TutorialGreeting2 = 'Hi %s!\nCome over here!'
TutorialGreeting3 = 'Hi %s!\nCome over here!\nUse the arrow keys!'
TutorialMickeyWelcome = 'Welcome to Toontown!'
TutorialFlippyIntro = 'Let me introduce you to my friend %s...' % Flippy
TutorialFlippyHi = 'Hi, %s!'
TutorialQT1 = 'You can talk by using this.'
TutorialQT2 = 'You can talk by using this.\nClick it, then choose "Hi".'
TutorialChat1 = 'You can talk using either of these buttons.'
TutorialChat2 = 'The blue button lets you chat with the keyboard.'
TutorialChat3 = "Be careful!  Most other players won't understand what you say you when you use the keyboard."
TutorialChat4 = 'The green button opens the %s.'
TutorialChat5 = 'Everyone can understand you if you use the %s.'
TutorialChat6 = 'Try saying "Hi".'
TutorialBodyClick1 = 'Very good!'
TutorialBodyClick2 = 'Pleased to meet you! Want to be friends?'
TutorialBodyClick3 = 'To make friends with %s, click on him...' % Flippy
TutorialHandleBodyClickSuccess = 'Good Job!'
TutorialHandleBodyClickFail = 'Not quite. Try clicking right on %s...' % Flippy
TutorialFriendsButton = "Now click the 'Friends' button under %s's picture in the right hand corner." % Flippy
TutorialHandleFriendsButton = "And then click on the 'Yes' button.."
TutorialOK = lOK
TutorialYes = lYes
TutorialNo = lNo
TutorialFriendsPrompt = 'Would you like to make friends with %s?' % Flippy
TutorialFriendsPanelMickeyChat = "%s has agreed to be your friend. Click 'Ok' to finish up." % Flippy
TutorialFriendsPanelYes = '%s said yes!' % Flippy
TutorialFriendsPanelNo = "That's not very friendly!"
TutorialFriendsPanelCongrats = 'Congratulations! You made your first friend.'
TutorialFlippyChat1 = 'Come see me when you are ready for your first ToonTask!'
TutorialFlippyChat2 = "I'll be in ToonHall!"
TutorialAllFriendsButton = 'You can view all your friends by clicking the friends button. Try it out...'
TutorialEmptyFriendsList = "Right now your list is empty because %s isn't a real player." % Flippy
TutorialCloseFriendsList = "Click the 'Close'\nbutton to make the\nlist go away"
TutorialShtickerButton = 'The button in the lower, right corner opens your shticker book. Try it...'
TutorialBook1 = 'The book contains lots of useful information like this map of Toontown.'
TutorialBook2 = 'You can also check the progress of your ToonTasks.'
TutorialBook3 = 'When you are done click the book button again to make it close'
TutorialLaffMeter1 = 'You will also need this...'
TutorialLaffMeter2 = "You will also need this...\nIt's your Laffmeter."
TutorialLaffMeter3 = 'When ' + Cogs + ' attack you, it gets lower.'
TutorialLaffMeter4 = 'When you are in playgrounds like this one, it goes back up.'
TutorialLaffMeter5 = 'When you complete ToonTasks, you will get rewards, like increasing your LaffLimit.'
TutorialLaffMeter6 = 'Be careful! If the ' + Cogs + ' defeat you, you will lose all your gags.'
TutorialLaffMeter7 = 'To get more gags, play trolley games.'
TutorialTrolley1 = 'Follow me to the trolley!'
TutorialTrolley2 = 'Hop on board!'
TutorialBye1 = 'Play some games!'
TutorialBye2 = 'Play some games!\nBuy some gags!'
TutorialBye3 = 'Go see %s when you are done!' % Flippy
TutorialForceAcknowledgeMessage = 'You are going the wrong way! Go find %s!' % Mickey
PetTutorialTitle1 = 'The Doodle Panel'
PetTutorialTitle2 = 'Doodle SpeedChat'
PetTutorialTitle3 = 'Doodle Cattlelog'
PetTutorialNext = 'Next Page'
PetTutorialPrev = 'Previous Page'
PetTutorialDone = 'Done'
PetTutorialPage1 = 'Click on a Doodle to display the Doodle panel.  From here you can feed, scratch, and call the Doodle.'
PetTutorialPage2 = "Use the new 'Pets' area in the SpeedChat menu to get a Doodle to do a trick.  If he does it, reward him and he'll get better!"
PetTutorialPage3 = "Purchase new Doodle tricks from Clarabelle's Cattlelog.  Better tricks give better Toon-Ups!"
PlaygroundDeathAckMessage = TheCogs + ' took all your gags!\n\nYou are sad. You may not leave the playground until you are happy.'
ForcedLeaveFactoryAckMsg = 'The ' + Foreman + ' was defeated before you could reach him. You did not recover any Cog parts.'
ForcedLeaveMintAckMsg = 'The Mint Floor Supervisor was defeated before you could reach him. You did not recover any Cogbucks.'
HeadingToFactoryTitle = 'Heading to %s...'
ForemanConfrontedMsg = '%s is battling the ' + Foreman + '!'
MintBossConfrontedMsg = '%s is battling the Supervisor!'
MinigameWaitingForOtherPlayers = 'Waiting for other players to join...'
MinigamePleaseWait = 'Please wait...'
DefaultMinigameTitle = 'Minigame Title'
DefaultMinigameInstructions = 'Minigame Instructions'
HeadingToMinigameTitle = 'Heading to %s...'
MinigamePowerMeterLabel = 'Power Meter'
MinigamePowerMeterTooSlow = 'Too\nslow'
MinigamePowerMeterTooFast = 'Too\nfast'
MinigameTemplateTitle = 'Minigame Template'
MinigameTemplateInstructions = 'This is a template minigame. Use it to create new minigames.'
CannonGameTitle = 'Cannon Game'
CannonGameInstructions = 'Shoot your toon into the water tower as quickly as you can. Use the mouse or the arrow keys to aim the cannon. Be quick and win a big reward for everyone!'
CannonGameReward = 'REWARD'
TugOfWarGameTitle = 'Tug-O-War'
TugOfWarInstructions = "Alternately tap the left and right arrow keys just fast enough to line up the green bar with the red line. Don't tap them too slow or too fast, or you'll end up in the water!"
TugOfWarGameGo = 'GO!'
TugOfWarGameReady = 'Ready...'
TugOfWarGameEnd = 'Good game!'
TugOfWarGameTie = 'You tied!'
TugOfWarPowerMeter = 'Power meter'
PatternGameTitle = 'Match %s' % Minnie
PatternGameInstructions = Minnie + ' will show you a dance sequence. ' + 'Try to repeat ' + Minnie + "'s dance just the way you see it using the arrow keys!"
PatternGameWatch = 'Watch these dance steps...'
PatternGameGo = 'GO!'
PatternGameRight = 'Good, %s!'
PatternGameWrong = 'Oops!'
PatternGamePerfect = 'That was perfect, %s!'
PatternGameBye = 'Thanks for playing!'
PatternGameWaitingOtherPlayers = 'Waiting for other players...'
PatternGamePleaseWait = 'Please wait...'
PatternGameFaster = 'You were\nfaster!'
PatternGameFastest = 'You were\nthe fastest!'
PatternGameYouCanDoIt = 'Come on!\nYou can do it!'
PatternGameOtherFaster = '\nwas faster!'
PatternGameOtherFastest = '\nwas the fastest!'
PatternGameGreatJob = 'Great Job!'
PatternGameRound = 'Round %s!'
RaceGameTitle = 'Race Game'
RaceGameInstructions = 'Click a number. Choose wisely! You only advance if no one else picked the same number.'
RaceGameWaitingChoices = 'Waiting for other players to choose...'
RaceGameCardText = '%(name)s draws: %(reward)s'
RaceGameCardTextBeans = '%(name)s receives: %(reward)s'
RaceGameCardTextHi1 = '%(name)s is one Fabulous Toon!'
RaceGameForwardOneSpace = ' forward 1 space'
RaceGameForwardTwoSpaces = ' forward 2 spaces'
RaceGameForwardThreeSpaces = ' forward 3 spaces'
RaceGameBackOneSpace = ' back 1 space'
RaceGameBackTwoSpaces = ' back 2 spaces'
RaceGameBackThreeSpaces = ' back 3 spaces'
RaceGameOthersForwardThree = ' all others forward \n3 spaces'
RaceGameOthersBackThree = 'all others back \n3 spaces'
RaceGameInstantWinner = 'Instant Winner!'
RaceGameJellybeans2 = '2 Jellybeans'
RaceGameJellybeans4 = '4 Jellybeans'
RaceGameJellybeans10 = '10 Jellybeans!'
RingGameTitle = 'Ring Game'
RingGameInstructionsSinglePlayer = 'Try to swim through as many of the %s rings as you can.  Use the arrow keys to swim.'
RingGameInstructionsMultiPlayer = 'Try to swim through the %s rings.  Other players will try for the other colored rings.  Use the arrow keys to swim.'
RingGameMissed = 'MISSED'
RingGameGroupPerfect = 'GROUP\nPERFECT!!'
RingGamePerfect = 'PERFECT!'
RingGameGroupBonus = 'GROUP BONUS'
ColorRed = 'red'
ColorGreen = 'green'
ColorOrange = 'orange'
ColorPurple = 'purple'
ColorWhite = 'white'
ColorBlack = 'black'
ColorYellow = 'yellow'
TagGameTitle = 'Tag Game'
TagGameInstructions = 'Collect the treasures. You cannot collect treasure when you are IT!'
TagGameYouAreIt = 'You Are IT!'
TagGameSomeoneElseIsIt = '%s is IT!'
MazeGameTitle = 'Maze Game'
MazeGameInstructions = 'Collect the treasures. Try to get them all, but look out for the ' + Cogs + '!'
CatchGameTitle = 'Catching Game'
CatchGameInstructions = 'Catch as many %(fruit)s as you can. Watch out for the ' + Cogs + ", and try not to 'catch' any %(badThing)s!"
CatchGamePerfect = 'PERFECT!'
CatchGameApples = 'apples'
CatchGameOranges = 'oranges'
CatchGamePears = 'pears'
CatchGameCoconuts = 'coconuts'
CatchGameWatermelons = 'watermelons'
CatchGamePineapples = 'pineapples'
CatchGameAnvils = 'anvils'
PieTossGameTitle = 'Pie Toss Game'
PieTossGameInstructions = 'Toss pies at the targets.'
MinigameRulesPanelPlay = 'PLAY'
GagShopName = "Goofy's Gag Shop"
GagShopPlayAgain = 'PLAY\nAGAIN'
GagShopBackToPlayground = 'EXIT BACK TO\nPLAYGROUND'
GagShopYouHave = 'You have %s Jellybeans to spend'
GagShopYouHaveOne = 'You have 1 Jellybean to spend'
GagShopTooManyProps = 'Sorry, you have too many props'
GagShopDoneShopping = 'DONE\nSHOPPING'
GagShopTooManyOfThatGag = 'Sorry, you have enough %s already'
GagShopInsufficientSkill = 'You do not have enough skill for that yet'
GagShopYouPurchased = 'You purchased %s'
GagShopOutOfJellybeans = 'Sorry, you are all out of Jellybeans!'
GagShopWaitingOtherPlayers = 'Waiting for other players...'
GagShopPlayerDisconnected = '%s has disconnected'
GagShopPlayerExited = '%s has exited'
GagShopPlayerPlayAgain = 'Play Again'
GagShopPlayerBuying = 'Buying'
GenderShopQuestionMickey = 'To make a boy toon, click on me!'
GenderShopQuestionMinnie = 'To make a girl toon, click on me!'
GenderShopFollow = 'Follow me!'
GenderShopSeeYou = 'See you later!'
GenderShopBoyButtonText = 'Boy'
GenderShopGirlButtonText = 'Girl'
BodyShopHead = 'Head'
BodyShopBody = 'Body'
BodyShopLegs = 'Legs'
ColorShopHead = 'Head'
ColorShopBody = 'Body'
ColorShopLegs = 'Legs'
ColorShopToon = 'Toon'
ColorShopParts = 'Parts'
ColorShopAll = 'All'
ClothesShopShorts = 'Shorts'
ClothesShopShirt = 'Shirt'
ClothesShopBottoms = 'Bottoms'
MakeAToonDone = 'Done'
MakeAToonCancel = lCancel
MakeAToonNext = lNext
MakeAToonLast = 'Back'
CreateYourToon = 'Click the arrows to create your toon.'
CreateYourToonTitle = 'Create Your Toon'
CreateYourToonHead = "Click the 'head' arrows to pick different animals."
MakeAToonClickForNextScreen = 'Click the arrow below to go to the next screen.'
PickClothes = 'Click the arrows to pick clothes!'
PickClothesTitle = 'Choose Your Clothes'
PaintYourToon = 'Click the arrows to paint your toon!'
PaintYourToonTitle = 'Paint Your Toon'
MakeAToonYouCanGoBack = 'You can go back to change your body too!'
MakeAFunnyName = 'Choose a funny name for your toon with my Pick-A-Name game!'
MustHaveAFirstOrLast1 = "Your toon should have a first or last name, don't you think?"
MustHaveAFirstOrLast2 = "Don't you want your toon to have a first or last name?"
ApprovalForName1 = "That's it, your toon deserves a great name!"
ApprovalForName2 = 'Toon names are the best kind of names!'
MakeAToonLastStep = 'Last step before going to Toontown!'
PickANameYouLike = 'Pick a name you like!'
NameToonTitle = 'Name Your Toon'
TitleCheckBox = 'Title'
FirstCheckBox = 'First'
LastCheckBox = 'Last'
RandomButton = 'Random'
NameShopSubmitButton = 'Submit'
TypeANameButton = 'Type-A-Name'
TypeAName = "Don't like these names?\nClick here -->"
PickAName = 'Try the PickAName game!\nClick here -->'
PickANameButton = 'Pick-A-Name'
RejectNameText = 'That name is not allowed. Please try again.'
WaitingForNameSubmission = 'Submitting your name...'
PetNameMaster = 'PetNameMasterEnglish.txt'
PetshopUnknownName = 'Name: ???'
PetshopDescGender = 'Gender:\t%s'
PetshopDescCost = 'Cost:\t%s jellybeans'
PetshopDescTrait = 'Traits:\t%s'
PetshopDescStandard = 'Standard'
PetshopCancel = lCancel
PetshopSell = 'Sell Fish'
PetshopAdoptAPet = 'Adopt a Doodle'
PetshopReturnPet = 'Return your Doodle'
PetshopAdoptConfirm = 'Adopt %s for %d jellybeans?'
PetshopGoBack = 'Go Back'
PetshopAdopt = 'Adopt'
PetshopReturnConfirm = 'Return %s?'
PetshopReturn = 'Return'
PetshopChooserTitle = "TODAY'S DOODLES"
PetshopGoHomeText = 'Would you like to go to your estate to play with your new Doodle?'
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
NumToColor = [
    'White',
    'Peach',
    'Bright Red',
    'Red',
    'Maroon',
    'Sienna',
    'Brown',
    'Tan',
    'Coral',
    'Orange',
    'Yellow',
    'Cream',
    'Citrine',
    'Lime',
    'Sea Green',
    'Green',
    'Light Blue',
    'Aqua',
    'Blue',
    'Periwinkle',
    'Royal Blue',
    'Slate Blue',
    'Purple',
    'Lavender',
    'Pink',
    'Plum',
    'Black']
AnimalToSpecies = {
    'dog': 'Dog',
    'cat': 'Cat',
    'mouse': 'Mouse',
    'horse': 'Horse',
    'rabbit': 'Rabbit',
    'duck': 'Duck',
    'monkey': 'Monkey' }
NameTooLong = 'That name is too long. Please try again.'
ToonAlreadyExists = 'You already have a toon named %s!'
NameAlreadyInUse = 'That name is already used!'
EmptyNameError = 'You must enter a name first.'
NameError = 'Sorry.  That name will not work.'
NCTooShort = 'That name is too short.'
NCNoDigits = 'Your name cannot contain numbers.'
NCNeedLetters = 'Each word in your name must contain some letters.'
NCNeedVowels = 'Each word in your name must contain some vowels.'
NCAllCaps = 'Your name cannot be all capital letters.'
NCMixedCase = 'That name has too many capital letters.'
NCBadCharacter = "Your name cannot contain the character '%s'"
NCGeneric = 'Sorry, that name will not work.'
NCTooManyWords = 'Your name cannot be more than four words long.'
NCDashUsage = "Dashes may only be used to connect two words together (like in 'Boo-Boo')."
NCCommaEdge = 'Your name may not begin or end with a comma.'
NCCommaAfterWord = 'You may not begin a word with a comma.'
NCCommaUsage = 'That name does not use commas properly. Commas must join two words together, like in the name "Dr. Quack, MD". Commas must also be followed by a space.'
NCPeriodUsage = 'That name does not use periods properly. Periods are only allowed in words like "Mr.", "Mrs.", "J.T.", etc.'
NCApostrophes = 'That name has too many apostrophes.'
RemoveTrophy = 'Toon HQ: ' + TheCogs + ' took over one of the buildings you rescued!'
STOREOWNER_TOOKTOOLONG = 'Need more time to think?'
STOREOWNER_GOODBYE = 'See you later!'
STOREOWNER_NEEDJELLYBEANS = 'You need to ride the Trolley to get some Jellybeans.'
STOREOWNER_GREETING = 'Choose what you want to buy.'
STOREOWNER_BROWSING = 'You can browse, but you need a clothing ticket to buy.'
STOREOWNER_NOCLOTHINGTICKET = 'You need a clothing ticket to shop for clothes.'
STOREOWNER_NOFISH = 'Come back here to sell fish to the Pet Shop for jellybeans.'
STOREOWNER_THANKSFISH = 'Thanks! The Pet Shop will love these. Bye!'
STOREOWNER_THANKSFISH_PETSHOP = 'These are some fine specimens! Thanks.'
STOREOWNER_PETRETURNED = "Don't worry.  We'll find a good home for your Doodle."
STOREOWNER_PETADOPTED = 'Congratulations on your new Doodle!  You can play with him at your estate.'
STOREOWNER_PETCANCELED = 'Remember, if you see a Doodle you like, make sure to adopt him before someone else does!'
STOREOWNER_NOROOM = 'Hmm...you might want to make room in your closet before you buy new clothes.\n'
STOREOWNER_CONFIRM_LOSS = 'Your closet is full.  You will lose the clothes you were wearing.'
STOREOWNER_OK = lOK
STOREOWNER_CANCEL = lCancel
STOREOWNER_TROPHY = 'Wow! You collected %s of %s fish. That deserves a trophy and a LaffBoost!'
SuitInvasionBegin1 = 'Toon HQ: A Cog Invasion has begun!!!'
SuitInvasionBegin2 = 'Toon HQ: %s have taken over Toontown!!!'
SuitInvasionEnd1 = 'Toon HQ: The %s Invasion has ended!!!'
SuitInvasionEnd2 = 'Toon HQ: The Toons have saved the day once again!!!'
SuitInvasionUpdate1 = 'Toon HQ: The Cog Invasion is now at %s Cogs!!!'
SuitInvasionUpdate2 = 'Toon HQ: We must defeat those %s!!!'
SuitInvasionBulletin1 = 'Toon HQ: There is a Cog Invasion in progress!!!'
SuitInvasionBulletin2 = 'Toon HQ: %s have taken over Toontown!!!'
LeaderboardTitle = 'Toon Platoon'
QuestScriptTutorialMickey_1 = 'Toontown has a new citizen! Do you have some extra gags?'
QuestScriptTutorialMickey_2 = 'Sure, %s!'
QuestScriptTutorialMickey_3 = 'Tutorial Tom will tell you all about the Cogs.\x7Gotta go!'
QuestScriptTutorialMickey_4 = 'Come here! Use the arrow keys to move.'
QuestScriptTutorialMinnie_1 = 'Toontown has a new citizen! Do you have some extra gags?'
QuestScriptTutorialMinnie_2 = 'Sure, %s!'
QuestScriptTutorialMinnie_3 = 'Tutorial Tom will tell you all about the Cogs.\x7Gotta go!'
QuestScript101_1 = 'These are Cogs. They are robots that are trying to take over Toontown.'
QuestScript101_2 = 'There are many different kinds of Cogs and...'
QuestScript101_3 = '...they turn happy Toon buildings...'
QuestScript101_4 = '...into ugly Cog buildings!'
QuestScript101_5 = "But Cogs can't take a joke!"
QuestScript101_6 = 'A good gag will stop them.'
QuestScript101_7 = 'There are lots of gags, but take these to start.'
QuestScript101_8 = 'Oh! You also need a Laff Meter!'
QuestScript101_9 = "If your Laff Meter gets too low, you'll be sad!"
QuestScript101_10 = 'A happy Toon is a healthy Toon!'
QuestScript101_11 = "OH NO! There's a Cog outside my shop!"
QuestScript101_12 = 'HELP ME, PLEASE! Defeat that Cog!'
QuestScript101_13 = 'Here is your first ToonTask!'
QuestScript101_14 = 'Hurry up! Go defeat that Flunky!'
QuestScript110_1 = 'Good work defeating that Flunky. Let me give you a Shticker Book...'
QuestScript110_2 = 'The book is full of good stuff.'
QuestScript110_3 = "Open it, and I'll show you."
QuestScript110_4 = "The map shows where you've been."
QuestScript110_5 = 'Turn the page to see your gags...'
QuestScript110_6 = 'Uh oh! You have no gags! I will assign you a task.'
QuestScript110_7 = 'Turn the page to see your tasks.'
QuestScript110_8 = 'Take a ride on the trolley, and earn jelly beans to buy gags!'
QuestScript110_9 = 'To get to the trolley, go out the door behind me and head for the playground.'
QuestScript110_10 = 'Now, close the book and find the trolley!'
QuestScript110_11 = 'Return to Toon HQ when you are done. Bye!'
QuestScriptTutorialBlocker_1 = 'Why, hello there!'
QuestScriptTutorialBlocker_2 = 'Hello?'
QuestScriptTutorialBlocker_3 = "Oh! You don't know how to use SpeedChat!"
QuestScriptTutorialBlocker_4 = 'Click on the button to say something.'
QuestScriptTutorialBlocker_5 = 'Very good!\x7Where you are going there are many Toons to talk to.'
QuestScriptTutorialBlocker_6 = "If you want to chat with your friends using the keyboard, there's another button you can use."
QuestScriptTutorialBlocker_7 = 'It\'s called the "Chat" button. You need to be an official citizen of Toontown to use it.'
QuestScriptTutorialBlocker_8 = 'Good luck! See you later!'
QuestScriptGagShop_1 = 'Welcome to the Gag Shop!'
QuestScriptGagShop_1a = 'This is where Toons come to buy gags to use against the Cogs.'
QuestScriptGagShop_3 = 'To buy gags, click on the gag buttons. Try getting some now!'
QuestScriptGagShop_4 = 'Good! You can use these gags in battle against the Cogs.'
QuestScriptGagShop_5 = "Here's a peek at the advanced throw and squirt gags..."
QuestScriptGagShop_6 = "When you're done buying gags, click this button to return to the Playground."
QuestScriptGagShop_7 = 'Normally you can use this button to play another Trolley Game...'
QuestScriptGagShop_8 = "...but there's no time for another game right now. You're needed in Toon HQ!"
QuestScript120_1 = "Good job finding the trolley!\x7By the way, have you met Banker Bob?\x7He has quite a sweet tooth.\x7Why don't you introduce yourself by taking him this candy bar as a gift."
QuestScript120_2 = 'Banker Bob is over in the Toontown Bank.'
QuestScript121_1 = "Yum, thank you for the Candy Bar.\x7Say, if you can help me, I'll give you a reward.\x7Those Cogs stole the keys to my safe. Defeat Cogs to find a stolen key.\x7When you find a key, bring it back to me."
QuestScript130_1 = 'Good job finding the trolley!\x7By the way, I received a package for Professor Pete today.\x7It must be his new chalk he ordered.\x7Can you please take it to him?\x7He is over in the school house.'
QuestScript131_1 = 'Oh, thanks for the chalk.\x7What?!?\x7Those Cogs stole my blackboard. Defeat Cogs to find my stolen blackboard.\x7When you find it, bring it back to me.'
QuestScript140_1 = 'Good job finding the trolley!\x7By the way, I have this friend, Librarian Larry, who is quite a book worm.\x7I picked this book up for him last time I was over in ' + lDonaldsDock + '.\x7Could you take it over to him, he is usually in the Library.'
QuestScript141_1 = 'Oh, yes, this book almost completes my collection.\x7Let me see...\x7Uh oh...\x7Now where did I put my glasses?\x7I had them just before those Cogs took over my building.\x7Defeat Cogs to find my stolen glasses.\x7When you find them, bring them back to me for a reward.'
QuestScript145_1 = 'I see you had no problem with the trolley!\x7Listen, the Cogs have stolen our blackboard eraser.\x7Go into the streets and fight Cogs until you recover the eraser.\x7To reach the streets go through one of the tunnels like this:'
QuestScript145_2 = "When you find our eraser, bring it back here.\x7Don't forget, if you need gags, ride the trolley.\x7Also, if you need to recover Laff Points, collect ice cream cones in the Playground."
QuestScript150_1 = 'Great work!\x7Toontown is more fun when you have friends!'
QuestScript150_2 = 'To make friends, find another player, and use the New Friend button.'
QuestScript150_3 = 'Once you have made a friend, come back here.'
QuestScript150_4 = 'Some tasks are too difficult to do alone!'
MissingKeySanityCheck = 'Ignore me'
SellbotBossName = 'Senior V. P.'
CashbotBossName = 'C. F. O.'
BossCogNameWithDept = '%(name)s\n%(dept)s'
BossCogPromoteDoobers = 'You are hereby promoted to full-fledged %s.  Congratulations!'
BossCogDoobersAway = {
    's': 'Go!  And make that sale!' }
BossCogWelcomeToons = 'Welcome, new Cogs!'
BossCogPromoteToons = 'You are hereby promoted to full-fledged %s.  Congratu--'
CagedToonInterruptBoss = 'Hey! Hiya! Hey over there!'
CagedToonRescueQuery = 'So, did you Toons come to rescue me?'
BossCogDiscoverToons = 'Huh?  Toons!  In disguise!'
BossCogAttackToons = 'Attack!!'
CagedToonDrop = [
    "Great job!  You're wearing him down!",
    "Keep after him!  He's on the run!",
    'You guys are doing great!',
    "Fantastic!  You've almost got him now!"]
CagedToonPrepareBattleTwo = "Look out, he's trying to get away!\x7Help me, everyone--get up here and stop him!"
CagedToonPrepareBattleThree = "Hooray, I'm almost free!\x7Now you need to attack the VP Cog directly.\x7I've got a whole bunch of pies you can use!\x7Jump up and touch the bottom of my cage and I'll give you some pies.\x7Press the Ins key to throw pies once you've got them!"
BossBattleNeedMorePies = 'You need to get more pies!'
BossBattleHowToGetPies = 'Jump up to touch the cage to get pies.'
BossBattleHowToThrowPies = 'Press the Ins key to throw pies!'
CagedToonYippee = 'Yippee!'
CagedToonThankYou = "It's great to be free!\x7Thanks for all your help!\x7I am in your debt.\x7If you ever need help in battle, just give me a call!\x7Just click on the SOS button to call me."
CagedToonPromotion = "\x7Say--that VP Cog left behind your promotion papers.\x7I'll file them for you on the way out, so you'll get your promotion!"
CagedToonLastPromotion = "\x7Wow, you've reached level %s on your Cog suit!\x7Cogs don't get promoted higher than that.\x7You can't upgrade your Cog suit anymore, but you can certainly keep rescuing Toons!"
CagedToonHPBoost = "\x7You've rescued a lot of Toons from this HQ.\x7The Toon Council has decided to give you another Laff Point. Congratulations!"
CagedToonMaxed = '\x7I see that you have a level %s Cog suit. Very impressive!\x7On behalf of the Toon Council, thank you for coming back to rescue more Toons!'
CagedToonGoodbye = 'See ya!'
CagedToonBattleThree = {
    10: 'Nice jump, %(toon)s.  Here are some pies!',
    11: 'Hi, %(toon)s!  Have some pies!',
    12: "Hey there, %(toon)s!  You've got some pies now!",
    20: 'Hey, %(toon)s!  Jump up to my cage and get some pies to throw!',
    21: 'Hi, %(toon)s!  Use the Ctrl key to jump up and touch my cage!',
    100: 'Press the Insert key to throw a pie.',
    101: 'The blue power meter shows how high your pie will go.',
    102: 'First try to lob a pie inside his undercarriage to gum up his works.',
    103: 'Wait for the door to open, and throw a pie straight inside.',
    104: "When he's dizzy, hit him in the face or chest to knock him back!",
    105: "You'll know you've got a good hit when you see the splat in color.",
    106: 'If you hit a Toon with a pie, it gives that Toon a Laff point!' }
CagedToonBattleThreeMaxGivePies = 12
CagedToonBattleThreeMaxTouchCage = 21
CagedToonBattleThreeMaxAdvice = 106
CashbotBossHadEnough = "That's it.  I've had enough of these pesky Toons!"
CashbotBossOuttaHere = "I've got a train to catch!"
ResistanceToonName = 'Mata Hairy'
ResistanceToonCongratulations = "You did it!  Congratulations!\x7You're an asset to the Resistance!\x7Here's a special phrase you can use in a tight spot:\x7%s\x7When you say it, %s.\x7But you can only use it once, so choose that time well!"
ResistanceToonToonupInstructions = 'all the Toons near you will gain %s laff points'
ResistanceToonToonupAllInstructions = 'all the Toons near you will gain full laff points'
ResistanceToonMoneyInstructions = 'all the Toons near you will gain %s jellybeans'
ResistanceToonMoneyAllInstructions = 'all the Toons near you will fill their jellybean jars'
ResistanceToonRestockInstructions = 'all the Toons near you will restock their "%s" gags'
ResistanceToonRestockAllInstructions = 'all the Toons near you will restock all their gags'
ResistanceToonLastPromotion = "\x7Wow, you've reached level %s on your Cog suit!\x7Cogs don't get promoted higher than that.\x7You can't upgrade your Cog suit anymore, but you can certainly keep working for the Resistance!"
ResistanceToonHPBoost = "\x7You've done a lot of work for the Resistance.\x7The Toon Council has decided to give you another Laff Point. Congratulations!"
ResistanceToonMaxed = '\x7I see that you have a level %s Cog suit. Very impressive!\x7On behalf of the Toon Council, thank you for coming back to rescue more Toons!'
CashbotBossCogAttack = 'Get them!!!'
ResistanceToonWelcome = 'Hey, you made it!  Follow me to the main vault before the CFO finds us!'
ResistanceToonTooLate = "Blast it!  We're too late!"
CashbotBossDiscoverToons1 = 'Ah-HAH!'
CashbotBossDiscoverToons2 = 'I thought I smelled something a little toony in here!  Imposters!'
ResistanceToonKeepHimBusy = "Keep him busy!  I'm going to set a trap!"
ResistanceToonWatchThis = 'Watch this!'
CashbotBossGetAwayFromThat = 'Hey!  Get away from that!'
ResistanceToonCraneInstructions1 = 'Control a magnet by stepping up to a podium.'
ResistanceToonCraneInstructions2 = 'Use the arrow keys to move the crane, and press the Ctrl key to grab an object.'
ResistanceToonCraneInstructions3 = "Grab a safe with a magnet and knock the CFO's safe-ty helmet off."
ResistanceToonCraneInstructions4 = 'Once his helmet is gone, grab a disabled goon and hit him in the head!'
ResistanceToonGetaway = 'Eek!  Gotta run!'
MintElevatorRejectMessage = 'You cannot enter the Mints until you have completed your %s Cog Suit.'
BossElevatorRejectMessage = 'You cannot board this elevator until you have earned a promotion.'
FurnitureTypeName = 'Furniture'
PaintingTypeName = 'Painting'
ClothingTypeName = 'Clothing'
ChatTypeName = 'SpeedChat Phrase'
EmoteTypeName = 'Acting Lessons'
PoleTypeName = 'Fishing Pole'
WindowViewTypeName = 'Window View'
PetTrickTypeName = 'Doodle Training'
FurnitureYourOldCloset = 'your old wardrobe'
FurnitureYourOldBank = 'your old bank'
ChatItemQuotes = '"%s"'
FurnitureNames = {
    100: 'Armchair',
    105: 'Armchair',
    110: 'Chair',
    120: 'Desk Chair',
    130: 'Log Chair',
    140: 'Lobster Chair',
    145: 'Lifejacket Chair',
    150: 'Saddle Stool',
    160: 'Native Chair',
    170: 'Cupcake Chair',
    200: 'Bed',
    205: 'Bed',
    210: 'Bed',
    220: 'Bathtub Bed',
    230: 'Leaf Bed',
    240: 'Boat Bed',
    250: 'Cactus Hammock',
    260: 'Ice Cream Bed',
    300: 'Player Piano',
    310: 'Pipe Organ',
    400: 'Fireplace',
    410: 'Fireplace',
    420: 'Round Fireplace',
    430: 'Fireplace',
    440: 'Apple Fireplace',
    500: 'Wardrobe',
    502: '15 item Wardrobe',
    510: 'Wardrobe',
    512: '15 item Wardrobe',
    600: 'Short Lamp',
    610: 'Tall Lamp',
    620: 'Table Lamp',
    625: 'Table Lamp',
    630: 'Daisy Lamp',
    640: 'Daisy Lamp',
    650: 'Jellyfish Lamp',
    660: 'Jellyfish Lamp',
    670: 'Cowboy Lamp',
    700: 'Cushioned Chair',
    705: 'Cushioned Chair',
    710: 'Couch',
    715: 'Couch',
    720: 'Hay Couch',
    730: 'Shortcake Couch',
    800: 'Desk',
    810: 'Log Desk',
    900: 'Umbrella Stand',
    910: 'Coat Rack',
    920: 'Trash Can',
    930: 'Red Mushroom',
    940: 'Yellow Mushroom',
    950: 'Coat Rack',
    960: 'Barrel Stand',
    970: 'Cactus Plant',
    980: 'Teepee',
    1000: 'Large Rug',
    1010: 'Round Rug',
    1015: 'Round Rug',
    1020: 'Small Rug',
    1030: 'Leaf Mat',
    1100: 'Display Cabinet',
    1110: 'Display Cabinet',
    1120: 'Tall Bookcase',
    1130: 'Low Bookcase',
    1140: 'Sundae Chest',
    1200: 'End Table',
    1210: 'Small Table',
    1215: 'Small Table',
    1220: 'Coffee Table',
    1230: 'Coffee Table',
    1240: "Snorkeler's Table",
    1250: 'Cookie Table',
    1260: 'Bedroom Table',
    1300: '1000 Bean Bank',
    1310: '2500 Bean Bank',
    1320: '5000 Bean Bank',
    1330: '7500 Bean Bank',
    1340: '10000 Bean Bank',
    1399: 'Telephone',
    1400: 'Cezanne Toon',
    1410: 'Flowers',
    1420: 'Modern Mickey',
    1430: 'Rembrandt Toon',
    1440: 'Toonscape',
    1441: "Whistler's Horse",
    1442: 'Toon Star',
    1443: 'Not a Pie',
    1500: 'Radio',
    1510: 'Radio',
    1520: 'Radio',
    1530: 'Television',
    1600: 'Short Vase',
    1610: 'Tall Vase',
    1620: 'Short Vase',
    1630: 'Tall Vase',
    1640: 'Short Vase',
    1650: 'Short Vase',
    1660: 'Coral Vase',
    1661: 'Shell Vase',
    1700: 'Popcorn Cart',
    1710: 'Ladybug',
    1720: 'Fountain',
    1725: 'Washing Machine',
    1800: 'Fish Bowl',
    1810: 'Fish Bowl',
    1900: 'Swordfish',
    1910: 'Hammerhead',
    1920: 'Hanging Horns',
    1930: 'Simple Sombrero',
    1940: 'Fancy Sombrero',
    1950: 'Dream Catcher',
    1960: 'Horseshoe',
    1970: 'Bison Portrait',
    2000: 'Candy Swing Set',
    2010: 'Cake Slide',
    3000: 'Banana Split Tub',
    10000: 'Short Pumpkin',
    10010: 'Tall Pumpkin' }
ClothingArticleNames = ('Shirt', 'Shirt', 'Shirt', 'Shorts', 'Shorts', 'Skirt', 'Shorts')
ClothingTypeNames = {
    1400: "Matthew's Shirt",
    1401: "Jessica's Shirt",
    1402: "Marissa's Shirt" }
SurfaceNames = ('Wallpaper', 'Moulding', 'Flooring', 'Wainscoting', 'Border')
WallpaperNames = {
    1000: 'Parchment',
    1100: 'Milan',
    1200: 'Dover',
    1300: 'Victoria',
    1400: 'Newport',
    1500: 'Pastoral',
    1600: 'Harlequin',
    1700: 'Moon',
    1800: 'Stars',
    1900: 'Flowers',
    2000: 'Spring Garden',
    2100: 'Formal Garden',
    2200: 'Race Day',
    2300: 'Touchdown!',
    2400: 'Cloud 9',
    2500: 'Climbing Vine',
    2600: 'Springtime',
    2700: 'Kokeshi',
    2800: 'Posies',
    2900: 'Angel Fish',
    3000: 'Bubbles',
    3100: 'Bubbles',
    3200: 'Go Fish',
    3300: 'Stop Fish',
    3400: 'Sea Horse',
    3500: 'Sea Shells',
    3600: 'Underwater',
    3700: 'Boots',
    3800: 'Cactus',
    3900: 'Cowboy Hat',
    10100: 'Cats',
    10200: 'Bats',
    11000: 'Snowflakes',
    11100: 'Hollyleaf',
    11200: 'Snowman',
    13000: 'Shamrock',
    13100: 'Shamrock',
    13200: 'Rainbow',
    13300: 'Shamrock' }
FlooringNames = {
    1000: 'Hardwood Floor',
    1010: 'Carpet',
    1020: 'Diamond Tile',
    1030: 'Diamond Tile',
    1040: 'Grass',
    1050: 'Beige Bricks',
    1060: 'Red Bricks',
    1070: 'Square Tile',
    1080: 'Stone',
    1090: 'Boardwalk',
    1100: 'Dirt',
    1110: 'Wood Tile',
    1120: 'Tile',
    1130: 'Honeycomb',
    1140: 'Water',
    1150: 'Beach Tile',
    1160: 'Beach Tile',
    1170: 'Beach Tile',
    1180: 'Beach Tile',
    1190: 'Sand',
    10000: 'Ice Cube',
    10010: 'Igloo',
    11000: 'Shamrock',
    11010: 'Shamrock' }
MouldingNames = {
    1000: 'Knotty',
    1010: 'Painted',
    1020: 'Dental',
    1030: 'Flowers',
    1040: 'Flowers',
    1050: 'Ladybug' }
WainscotingNames = {
    1000: 'Painted',
    1010: 'Wood Panel',
    1020: 'Wood' }
WindowViewNames = {
    10: 'Large Garden',
    20: 'Wild Garden',
    30: 'Greek Garden',
    40: 'Cityscape',
    50: 'Wild West',
    60: 'Under the Sea',
    70: 'Tropical Island',
    80: 'Starry Night',
    90: 'Tiki Pool',
    100: 'Frozen Frontier',
    110: 'Farm Country',
    120: 'Native Camp',
    130: 'Main Street' }
NewCatalogNotify = 'There are new items available to order at your phone!'
NewDeliveryNotify = 'A new delivery has arrived at your mailbox!'
CatalogNotifyFirstCatalog = 'Your first cattlelog has arrived!  You may use this to order new items for yourself or for your house.'
CatalogNotifyNewCatalog = 'Your cattlelog #%s has arrived!  You can go to your phone to order items from this cattlelog.'
CatalogNotifyNewCatalogNewDelivery = 'A new delivery has arrived at your mailbox!  Also, your cattlelog #%s has arrived!'
CatalogNotifyNewDelivery = 'A new delivery has arrived at your mailbox!'
CatalogNotifyNewCatalogOldDelivery = 'Your cattlelog #%s has arrived, and there are still items waiting in your mailbox!'
CatalogNotifyOldDelivery = 'There are still items waiting in your mailbox for you to pick up!'
CatalogNotifyInstructions = 'Click the "Go home" button on the map page in your Shticker Book, then walk up to the phone inside your house.'
CatalogNewDeliveryButton = 'New\nDelivery!'
CatalogNewCatalogButton = 'New\nCattlelog'
CatalogSaleItem = 'Sale!  '
DistributedMailboxEmpty = 'Your mailbox is empty right now.  Come back here to look for deliveries after you place an order from your phone!'
DistributedMailboxWaiting = 'Your mailbox is empty right now, but the package you ordered is on its way.  Check back later!'
DistributedMailboxReady = 'Your order has arrived!'
DistributedMailboxNotOwner = 'Sorry, this is not your mailbox.'
DistributedPhoneEmpty = "You can use any phone to order special items for you and your house.  New items will become available to order over time.\n\nYou don't have any items available to order right now, but check back later!"
Clarabelle = 'Clarabelle'
MailboxExitButton = 'Close Mailbox'
MailboxAcceptButton = 'Take this item'
MailboxOneItem = 'Your mailbox contains 1 item.'
MailboxNumberOfItems = 'Your mailbox contains %s items.'
MailboxGettingItem = 'Taking %s from mailbox.'
MailboxItemNext = 'Next\nItem'
MailboxItemPrev = 'Previous\nItem'
CatalogCurrency = 'beans'
CatalogHangUp = 'Hang Up'
CatalogNew = 'NEW'
CatalogBackorder = 'BACKORDER'
CatalogPagePrefix = 'Page'
CatalogGreeting = "Hello! Thanks for calling Clarabelle's Cattlelog. Can I help you?"
CatalogGoodbyeList = [
    'Bye now!',
    'Call back soon!',
    'Thanks for calling!',
    'Ok, bye now!',
    'Bye!']
CatalogHelpText1 = 'Turn the page to see items for sale.'
CatalogSeriesLabel = 'Series %s'
CatalogPurchaseItemAvailable = 'Congratulations on your new purchase!  You can start using it right away.'
CatalogPurchaseItemOnOrder = 'Congratulations! Your purchase will be delivered to your mailbox soon.'
CatalogAnythingElse = 'Anything else I can get you today?'
CatalogPurchaseClosetFull = 'Your closet is full.  You may purchase this item anyway, but if you do you will need to delete something from your closet to make room for it when it arrives.\n\nDo you still want to purchase this item?'
CatalogAcceptClosetFull = 'Your closet is full.  You must go inside and delete something from your closet to make room for this item before you can take it out of your mailbox.'
CatalogAcceptShirt = 'You are now wearing your new shirt.  What you were wearing before has been moved to your closet.'
CatalogAcceptShorts = 'You are now wearing your new shorts.  What you were wearing before has been moved to your closet.'
CatalogAcceptSkirt = 'You are now wearing your new skirt.  What you were wearing before has been moved to your closet.'
CatalogAcceptPole = "You're now ready to go catch some bigger fish with your new pole!"
CatalogAcceptPoleUnneeded = 'You already have a better pole than this one!'
CatalogPurchaseHouseFull = 'Your house is full.  You may purchase this item anyway, but if you do you will need to delete something from your house to make room for it when it arrives.\n\nDo you still want to purchase this item?'
CatalogAcceptHouseFull = 'Your house is full.  You must go inside and delete something from your house to make room for this item before you can take it out of your mailbox.'
CatalogAcceptInAttic = 'Your new item is now in your attic.  You can put it in your house by going inside and clicking on the "Move Furniture" button.'
CatalogAcceptInAtticP = 'Your new items are now in your attic.  You can put them in your house by going inside and clicking on the "Move Furniture" button.'
CatalogPurchaseMailboxFull = "Your mailbox is full!  You can't purchase this item until you take some items out of your mailbox to make room."
CatalogPurchaseOnOrderListFull = "You have too many items currently on order.  You can't order any more items until some of the ones you have already ordered arrive."
CatalogPurchaseGeneralError = 'The item could not be purchased because of some internal game error: error code %s.'
CatalogAcceptGeneralError = 'The item could not be removed from your mailbox because of some internal game error: error code %s.'
HDMoveFurnitureButton = 'Move\nFurniture'
HDStopMoveFurnitureButton = 'Done\nMoving'
HDAtticPickerLabel = 'In the attic'
HDInRoomPickerLabel = 'In the room'
HDInTrashPickerLabel = 'In the trash'
HDDeletePickerLabel = 'Delete?'
HDInAtticLabel = 'Attic'
HDInRoomLabel = 'Room'
HDInTrashLabel = 'Trash'
HDToAtticLabel = 'Send\nto attic'
HDMoveLabel = 'Move'
HDRotateCWLabel = 'Rotate Right'
HDRotateCCWLabel = 'Rotate Left'
HDReturnVerify = 'Return this item to the attic?'
HDReturnFromTrashVerify = 'Return this item to the attic from the trash?'
HDDeleteItem = 'Click OK to send this item to the trash, or Cancel to keep it.'
HDNonDeletableItem = "You can't delete items of this type!"
HDNonDeletableBank = "You can't delete your bank!"
HDNonDeletableCloset = "You can't delete your wardrobe!"
HDNonDeletablePhone = "You can't delete your phone!"
HDNonDeletableNotOwner = "You can't delete %s's things!"
HDHouseFull = 'Your house is full.  You have to delete something else from your house or attic before you can return this item from the trash.'
HDHelpDict = {
    'DoneMoving': 'Finish room decorating.',
    'Attic': 'Show list of items in attic. The attic stores items that are not in your room.',
    'Room': 'Show list of items in room. Useful for finding lost items.',
    'Trash': 'Show items in trash. Oldest items are deleted after a while or when trash overflows.',
    'ZoomIn': 'Get a closer view of room.',
    'ZoomOut': 'Get a farther view of room.',
    'SendToAttic': 'Send the current furniture item to attic for storage.',
    'RotateLeft': 'Turn left.',
    'RotateRight': 'Turn right.',
    'DeleteEnter': 'Change to delete mode.',
    'DeleteExit': 'Exit delete mode.',
    'FurnitureItemPanelDelete': 'Send %s to trash.',
    'FurnitureItemPanelAttic': 'Place %s in room.',
    'FurnitureItemPanelRoom': 'Return %s to attic.',
    'FurnitureItemPanelTrash': 'Return %s to attic.' }
MessagePickerTitle = 'You have too many phrases. In order to purchase\n"%s"\n you must choose one to remove:'
MessagePickerCancel = lCancel
MessageConfirmDelete = 'Are you sure you want to remove "%s" from your SpeedChat menu?'
CatalogBuyText = 'Buy'
CatalogOnOrderText = 'On Order'
CatalogPurchasedText = 'Already\nPurchased'
CatalogPurchasedMaxText = 'Already\nPurchased Max'
CatalogVerifyPurchase = 'Purchase %(item)s for %(price)s jellybeans?'
CatalogOnlyOnePurchase = 'You may only have one of these items at a time.  If you purchase this one, it will replace %(old)s.\n\nAre you sure you want to purchase %(item)s for %(price)s jellybeans?'
CatalogExitButtonText = 'Hang Up'
CatalogCurrentButtonText = 'To Current Items'
CatalogPastButtonText = 'To Past Items'
TutorialHQOfficerName = 'HQ Harry'
NPCToonNames = {
    20000: 'Tutorial Tom',
    999: 'Toon Tailor',
    1000: 'Toon HQ',
    20001: Flippy,
    2001: Flippy,
    2002: 'Banker Bob',
    2003: 'Professor Pete',
    2004: 'Tammy the Tailor',
    2005: 'Librarian Larry',
    2006: 'Clerk Clark',
    2011: 'Clerk Clara',
    2007: lHQOfficerM,
    2008: lHQOfficerM,
    2009: lHQOfficerF,
    2010: lHQOfficerF,
    2012: 'Fisherman Freddy',
    2013: 'Clerk Poppy',
    2014: 'Clerk Peppy',
    2015: 'Clerk Pappy',
    2101: 'Dentist Daniel',
    2102: 'Sheriff Sherry',
    2103: 'Sneezy Kitty',
    2104: lHQOfficerM,
    2105: lHQOfficerM,
    2106: lHQOfficerF,
    2107: lHQOfficerF,
    2108: 'Canary Coalmine',
    2109: 'Babbles Blowhard',
    2110: 'Bill Board',
    2111: 'Dancing Diego',
    2112: 'Dr. Tom',
    2113: 'Rollo The Amazing',
    2114: 'Roz Berry',
    2115: 'Patty Papercut',
    2116: 'Bruiser McDougal',
    2117: 'Ma Putrid',
    2118: 'Jesse Jester',
    2119: 'Honey Haha',
    2120: 'Professor Binky',
    2121: 'Madam Chuckle',
    2122: 'Harry Ape',
    2123: 'Spamonia Biggles',
    2124: 'T.P. Rolle',
    2125: 'Lazy Hal',
    2126: 'Professor Guffaw',
    2127: 'Woody Nickel',
    2128: 'Loony Louis',
    2129: 'Frank Furter',
    2130: 'Joy Buzzer',
    2131: 'Feather Duster',
    2132: 'Daffy Don',
    2133: 'Dr. Euphoric',
    2134: 'Silent Simone',
    2135: 'Mary',
    2136: 'Sal Snicker',
    2137: 'Happy Heikyung',
    2138: 'Muldoon',
    2139: 'Dan Dribbles',
    2140: 'Fisherman Billy',
    2201: 'Postmaster Pete',
    2202: 'Shirley U. Jest',
    2203: lHQOfficerM,
    2204: lHQOfficerM,
    2205: lHQOfficerF,
    2206: lHQOfficerF,
    2207: 'Will Wiseacre',
    2208: 'Sticky Lou',
    2209: 'Charlie Chortle',
    2210: 'Tee Hee',
    2211: 'Sally Spittake',
    2212: 'Weird Warren',
    2213: 'Lucy Tires',
    2214: 'Sam Stain',
    2215: 'Sid Seltzer',
    2216: 'Nona Seeya',
    2217: 'Sharky Jones',
    2218: 'Fanny Pages',
    2219: 'Chef Knucklehead',
    2220: 'Rick Rockhead',
    2221: 'Clovinia Cling',
    2222: 'Shorty Fuse',
    2223: 'Sasha Sidesplitter',
    2224: 'Smokey Joe',
    2225: 'Fisherman Droopy',
    2301: 'Dr. Pulyurleg',
    2302: 'Professor Wiggle',
    2303: 'Nurse Nancy',
    2304: lHQOfficerM,
    2305: lHQOfficerM,
    2306: lHQOfficerF,
    2307: lHQOfficerF,
    2308: 'Nancy Gas',
    2309: 'Big Bruce',
    2311: 'Franz Neckvein',
    2312: 'Dr. Sensitive',
    2313: 'Lucy Shirtspot',
    2314: 'Ned Slinger',
    2315: 'Chewy Morsel',
    2316: 'Cindy Sprinkles',
    2318: 'Tony Maroni',
    2319: 'Zippy',
    2320: 'Crunchy Alfredo',
    2321: 'Fisherman Punchy',
    1001: 'Clerk Will',
    1002: 'Clerk Bill',
    1003: lHQOfficerM,
    1004: lHQOfficerF,
    1005: lHQOfficerM,
    1006: lHQOfficerF,
    1007: 'Longjohn Leroy',
    1008: 'Fisherman Furball',
    1009: 'Clerk Barky',
    1010: 'Clerk Purr',
    1011: 'Clerk Bloop',
    1101: 'Billy Budd',
    1102: 'Captain Carl',
    1103: 'Fishy Frank',
    1104: 'Doctor Squall',
    1105: 'Admiral Hook',
    1106: 'Mrs. Starch',
    1107: 'Cal Estenicks',
    1108: lHQOfficerM,
    1109: lHQOfficerF,
    1110: lHQOfficerM,
    1111: lHQOfficerF,
    1112: 'Gary Glubglub',
    1113: 'Lisa Luff',
    1114: 'Charlie Chum',
    1115: 'Sheila Squid, Atty',
    1116: 'Barnacle Bessie',
    1117: 'Captain Yucks',
    1118: 'Choppy McDougal',
    1121: 'Linda Landlubber',
    1122: 'Salty Stan',
    1123: 'Electra Eel',
    1124: 'Flappy Docksplinter',
    1125: 'Eileen Overboard',
    1126: 'Fisherman Barney',
    1201: 'Barnacle Barbara',
    1202: 'Art',
    1203: 'Ahab',
    1204: 'Rocky Shores',
    1205: lHQOfficerM,
    1206: lHQOfficerF,
    1207: lHQOfficerM,
    1208: lHQOfficerF,
    1209: 'Professor Plank',
    1210: 'Gang Wei',
    1211: 'Wynn Bag',
    1212: 'Toby Tonguestinger',
    1213: 'Dante Dolphin',
    1214: 'Gusty Kate',
    1215: 'Dinah Down',
    1216: 'Rod Reel',
    1217: 'CC Weed',
    1218: 'Pacific Tim',
    1219: 'Brian Beachead',
    1220: 'Carla Canal',
    1221: 'Blisters McKee',
    1222: 'Shep Ahoy',
    1223: 'Sid Squid',
    1224: 'Emily Eel',
    1225: 'Bonzo Bilgepump',
    1226: 'Heave Ho',
    1227: 'Coral Reef',
    1228: 'Fisherman Reed',
    1301: 'Alice',
    1302: 'Melville',
    1303: 'Claggart',
    1304: 'Svetlana',
    1305: lHQOfficerM,
    1306: lHQOfficerF,
    1307: lHQOfficerM,
    1308: lHQOfficerF,
    1309: 'Seafoam',
    1310: 'Ted Tackle',
    1311: 'Topsy Turvey',
    1312: 'Ethan Keel',
    1313: 'William Wake',
    1314: 'Rusty Ralph',
    1315: 'Doctor Drift',
    1316: 'Wilma Wobble',
    1317: 'Paula Pylon',
    1318: 'Dinghy Dan',
    1319: 'Davey Drydock',
    1320: 'Ted Calm',
    1321: 'Dinah Docker',
    1322: 'Whoopie Cushion',
    1323: 'Stinky Ned',
    1324: 'Pearl Diver',
    1325: 'Ned Setter',
    1326: 'Felicia Chips',
    1327: 'Cindy Splat',
    1328: 'Fred Flounder',
    1329: 'Shelly Seaweed',
    1330: 'Porter Hole',
    1331: 'Rudy Rudder',
    1332: 'Fisherman Shane',
    3001: 'Betty Freezes',
    3002: lHQOfficerM,
    3003: lHQOfficerF,
    3004: lHQOfficerM,
    3005: lHQOfficerM,
    3006: 'Clerk Lenny',
    3007: 'Clerk Penny',
    3008: 'Warren Bundles',
    3009: 'Fisherman Frizzy',
    3010: 'Clerk Skip',
    3011: 'Clerk Dip',
    3012: 'Clerk Kipp',
    3101: 'Mr. Cow',
    3102: 'Auntie Freeze',
    3103: 'Fred',
    3104: 'Bonnie',
    3105: 'Frosty Freddy',
    3106: 'Gus Gooseburger',
    3107: 'Patty Passport',
    3108: 'Toboggan Ted',
    3109: 'Kate',
    3110: 'Chicken Boy',
    3111: 'Snooty Sinjin',
    3112: 'Lil Oldman',
    3113: 'Hysterical Harry',
    3114: 'Henry the Hazard',
    3115: lHQOfficerM,
    3116: lHQOfficerF,
    3117: lHQOfficerM,
    3118: lHQOfficerM,
    3119: 'Creepy Carl',
    3120: 'Mike Mittens',
    3121: 'Joe Shockit',
    3122: 'Lucy Luge',
    3123: 'Frank Lloyd Ice',
    3124: 'Lance Iceberg',
    3125: 'Colonel Crunchmouth',
    3126: 'Colestra Awl',
    3127: 'Ifalla Yufalla',
    3128: 'Sticky George',
    3129: 'Baker Bridget',
    3130: 'Sandy',
    3131: 'Lazy Lorenzo',
    3132: 'Ashy',
    3133: 'Dr. Friezeframe',
    3134: 'Lounge Lassard',
    3135: 'Soggy Nell',
    3136: 'Happy Sue',
    3137: 'Mr. Freeze',
    3138: 'Chef Bumblesoup',
    3139: 'Granny Icestockings',
    3140: 'Fisherman Lucille',
    3201: 'Aunt Arctic',
    3202: 'Shakey',
    3203: 'Walt',
    3204: 'Dr. Ivanna Cee',
    3205: 'Bumpy Noggin',
    3206: 'Vidalia VaVoom',
    3207: 'Dr. Mumbleface',
    3208: 'Grumpy Phil',
    3209: 'Giggles McGhee',
    3210: 'Simian Sam',
    3211: 'Fanny Freezes',
    3212: 'Frosty Fred',
    3213: lHQOfficerM,
    3214: lHQOfficerF,
    3215: lHQOfficerM,
    3216: lHQOfficerM,
    3217: 'Sweaty Pete',
    3218: 'Blue Lou',
    3219: 'Tom Tandemfrost',
    3220: 'Mr. Sneeze',
    3221: 'Nelly Snow',
    3222: 'Mindy Windburn',
    3223: 'Chappy',
    3224: 'Freida Frostbite',
    3225: 'Blake Ice',
    3226: 'Santa Paws',
    3227: 'Solar Ray',
    3228: 'Wynne Chill',
    3229: 'Hernia Belt',
    3230: 'Balding Benjy',
    3231: 'Choppy',
    3232: 'Fisherman Albert',
    4001: 'Molly Molloy',
    4002: lHQOfficerM,
    4003: lHQOfficerF,
    4004: lHQOfficerF,
    4005: lHQOfficerF,
    4006: 'Clerk Doe',
    4007: 'Clerk Ray',
    4008: 'Tailor Harmony',
    4009: 'Fisherman Fanny',
    4010: 'Clerk Chris',
    4011: 'Clerk Neil',
    4012: 'Clerk Westin Girl',
    4101: 'Tom',
    4102: 'Fifi',
    4103: 'Dr. Fret',
    4104: lHQOfficerM,
    4105: lHQOfficerF,
    4106: lHQOfficerF,
    4107: lHQOfficerF,
    4108: 'Cleff',
    4109: 'Carlos',
    4110: 'Metra Gnome',
    4111: 'Tom Hum',
    4112: 'Fa',
    4113: 'Madam Manners',
    4114: 'Offkey Eric',
    4115: 'Barbara Seville',
    4116: 'Piccolo',
    4117: 'Mandy Lynn',
    4118: 'Attendant Abe',
    4119: 'Moe Zart',
    4120: 'Viola Padding',
    4121: 'Gee Minor',
    4122: 'Minty Bass',
    4123: 'Lightning Ted',
    4124: 'Riff Raff',
    4125: 'Melody Wavers',
    4126: 'Mel Canto',
    4127: 'Happy Feet',
    4128: 'Luciano Scoop',
    4129: 'Tootie Twostep',
    4130: 'Metal Mike',
    4131: 'Abraham Armoire',
    4132: 'Lowdown Sally',
    4133: 'Scott Poplin',
    4134: 'Disco Dave',
    4135: 'Sluggo Songbird',
    4136: 'Patty Pause',
    4137: 'Tony Deff',
    4138: 'Cliff Cleff',
    4139: 'Harmony Swell',
    4140: 'Clumsy Ned',
    4141: 'Fisherman Jed',
    4201: 'Tina',
    4202: 'Barry',
    4203: 'Lumber Jack',
    4204: lHQOfficerM,
    4205: lHQOfficerF,
    4206: lHQOfficerF,
    4207: lHQOfficerF,
    4208: 'Hedy',
    4209: 'Corny Canter',
    4211: 'Carl Concerto',
    4212: 'Detective Dirge',
    4213: 'Fran Foley',
    4214: 'Tina Toehooks',
    4215: 'Tim Tailgater',
    4216: 'Gummy Whistle',
    4217: 'Handsome Anton',
    4218: 'Wilma Wind',
    4219: 'Sid Sonata',
    4220: 'Curtis Finger',
    4221: 'Moe Madrigal',
    4222: 'John Doe',
    4223: 'Penny Prompter',
    4224: 'Jungle Jim',
    4225: 'Holly Hiss',
    4226: 'Thelma Throatreacher',
    4227: 'Quiet Francesca',
    4228: 'August Winds',
    4229: 'June Loon',
    4230: 'Julius Wheezer',
    4231: 'Steffi Squeezebox',
    4232: 'Hedly Hymn',
    4233: 'Charlie Carp',
    4234: 'Leed Guitar',
    4235: 'Fisherman Larry',
    4301: 'Yuki',
    4302: 'Anna',
    4303: 'Leo',
    4304: lHQOfficerM,
    4305: lHQOfficerF,
    4306: lHQOfficerF,
    4307: lHQOfficerF,
    4308: 'Tabitha',
    4309: 'Marshall',
    4310: 'Martha Mopp',
    4311: 'Sea Shanty',
    4312: 'Moe Saj',
    4313: 'Dumb Dolph',
    4314: 'Dana Dander',
    4315: 'Karen Clockwork',
    4316: 'Tim Tango',
    4317: 'Stubby Toe',
    4318: 'Bob Marlin',
    4319: 'Rinky Dink',
    4320: 'Cammy Coda',
    4321: 'Luke Lute',
    4322: 'Randy Rythm',
    4323: 'Hanna Hogg',
    4324: 'Ellie',
    4325: 'Banker Bran',
    4326: 'Fran Fret',
    4327: 'Flim Flam',
    4328: 'Wagner',
    4329: 'Telly Prompter',
    4330: 'Quentin',
    4331: 'Mellow Costello',
    4332: 'Ziggy',
    4333: 'Harry',
    4334: 'Fast Freddie',
    4335: 'Fisherman Walden',
    5001: lHQOfficerM,
    5002: lHQOfficerM,
    5003: lHQOfficerF,
    5004: lHQOfficerF,
    5005: 'Clerk Peaches',
    5006: 'Clerk Herb',
    5007: 'Bonnie Blossom',
    5008: 'Fisherman Flora',
    5009: 'Clerk Bo Tanny',
    5010: 'Clerk Tom A. Dough',
    5011: 'Clerk Doug Wood',
    5101: 'Artie',
    5102: 'Susan',
    5103: 'Bud',
    5104: 'Flutterby',
    5105: 'Jack',
    5106: 'Barber Bjorn',
    5107: 'Postman Felipe',
    5108: 'Innkeeper Janet',
    5109: lHQOfficerM,
    5110: lHQOfficerM,
    5111: lHQOfficerF,
    5112: lHQOfficerF,
    5113: 'Dr. Spud',
    5114: 'Wilt',
    5115: 'Honey Dew',
    5116: 'Vegetable Vern',
    5117: 'Petal',
    5118: 'Pop Corn',
    5119: 'Barry Medly',
    5120: 'Gopher',
    5121: 'Paula Peapod',
    5122: 'Leif Pyle',
    5123: 'Diane Vine',
    5124: 'Soggy Bottom',
    5125: 'Sanjay Splash',
    5126: 'Madam Mum',
    5127: 'Polly Pollen',
    5128: 'Shoshanna Sap',
    5129: 'Fisherman Sally',
    5201: 'Jake',
    5202: 'Cynthia',
    5203: 'Lisa',
    5204: 'Bert',
    5205: 'Dan D. Lion',
    5206: 'Vine Green',
    5207: 'Sofie Squirt',
    5208: 'Samantha Spade',
    5209: lHQOfficerM,
    5210: lHQOfficerM,
    5211: lHQOfficerF,
    5212: lHQOfficerF,
    5213: 'Big Galoot',
    5214: 'Itchie Bumps',
    5215: 'Tammy Tuber',
    5216: 'Stinky Jim',
    5217: 'Greg Greenethumb',
    5218: 'Rocky Raspberry',
    5219: 'Lars Bicep',
    5220: 'Lacy Underalls',
    5221: 'Pink Flamingo',
    5222: 'Whiny Wilma',
    5223: 'Wet Will',
    5224: 'Uncle Bumpkin',
    5225: 'Pamela Puddle',
    5226: 'Pete Moss',
    5227: 'Begonia Biddlesmore',
    5228: 'Digger Mudhands',
    5229: 'Fisherman Lily',
    5301: lHQOfficerM,
    5302: lHQOfficerM,
    5303: lHQOfficerM,
    5304: lHQOfficerM,
    5305: 'Crystal',
    5306: 'S. Cargo',
    5307: 'Fun Gus',
    5308: 'Naggy Nell',
    5309: 'Ro Maine',
    5310: 'Timothy',
    5311: 'Judge McIntosh',
    5312: 'Eugene',
    5313: 'Coach Zucchini',
    5314: 'Aunt Hill',
    5315: 'Uncle Mud',
    5316: 'Uncle Spud',
    5317: 'Detective Lima',
    5318: 'Caesar',
    5319: 'Rose',
    5320: 'April',
    5321: 'Professor Ivy',
    5322: 'Fisherman Rose',
    9001: "Snoozin' Susan",
    9002: 'Sleeping Tom',
    9003: 'Drowsy Dennis',
    9004: lHQOfficerF,
    9005: lHQOfficerF,
    9006: lHQOfficerM,
    9007: lHQOfficerM,
    9008: 'Clerk Jill',
    9009: 'Clerk Phil',
    9010: 'Worn Out Waylon',
    9011: 'Fisherman Freud',
    9012: 'Clerk Sarah Snuze',
    9013: 'Clerk Kat Knap',
    9014: 'Clerk R. V. Winkle',
    9101: 'Ed',
    9102: 'Big Mama',
    9103: 'P.J.',
    9104: 'Sweet Slumber',
    9105: 'Professor Yawn',
    9106: 'Max',
    9107: 'Snuggles',
    9108: 'Winky Wilbur',
    9109: 'Dreamy Daphne',
    9110: 'Kathy Nip',
    9111: 'Powers Erge',
    9112: 'Lullaby Lou',
    9113: 'Jacques Clock',
    9114: 'Smudgy Mascara',
    9115: 'Babyface MacDougal',
    9116: 'Dances with Sheep',
    9117: 'Afta Hours',
    9118: 'Starry Knight',
    9119: 'Rocco',
    9120: 'Sarah Slumber',
    9121: 'Serena Shortsheeter',
    9122: 'Puffy Ayes',
    9123: 'Teddy Blair',
    9124: 'Nina Nitelight',
    9125: 'Dr. Bleary',
    9126: 'Wyda Wake',
    9127: 'Tabby Tucker',
    9128: "Hardy O'Toole",
    9129: 'Bertha Bedhog',
    9130: 'Charlie Chamberpot',
    9131: 'Susan Siesta',
    9132: lHQOfficerF,
    9133: lHQOfficerF,
    9134: lHQOfficerF,
    9135: lHQOfficerF,
    9136: 'Fisherman Taylor',
    9201: 'Bernie',
    9202: 'Orville',
    9203: 'Nat',
    9204: 'Claire de Loon',
    9205: 'Zen Glen',
    9206: 'Skinny Ginny',
    9207: 'Jane Drain',
    9208: 'Drowsy Dave',
    9209: 'Dr. Floss',
    9210: 'Master Mike',
    9211: 'Dawn',
    9212: 'Moonbeam',
    9213: 'Rooster Rick',
    9214: 'Dr. Blinky',
    9215: 'Rip',
    9216: 'Cat',
    9217: 'Lawful Linda',
    9218: 'Waltzing Matilda',
    9219: 'The Countess',
    9220: 'Grumpy Gordon',
    9221: 'Zari',
    9222: 'Cowboy George',
    9223: 'Mark the Lark',
    9224: 'Sandy Sandman',
    9225: 'Fidgety Bridget',
    9226: 'William Teller',
    9227: 'Bed Head Ted',
    9228: 'Whispering Willow',
    9229: 'Rose Petals',
    9230: 'Tex',
    9231: 'Harry Hammock',
    9232: 'Honey Moon',
    9233: lHQOfficerM,
    9234: lHQOfficerM,
    9235: lHQOfficerM,
    9236: lHQOfficerM,
    9237: 'Fisherman Jung' }
zone2TitleDict = {
    2513: ('Toon Hall', ''),
    2514: ('Toontown Bank', ''),
    2516: ('Toontown School House', ''),
    2518: ('Toontown Library', ''),
    2519: ('Gag Shop', ''),
    2520: ('Toon HQ', ''),
    2521: ('Clothing Shop', ''),
    2522: ('Pet Shop', ''),
    2601: ('All Smiles Tooth Repair', ''),
    2602: ('', ''),
    2603: ('One-Liner Miners', ''),
    2604: ('Hogwash & Dry', ''),
    2605: ('Toontown Sign Factory', ''),
    2606: ('', ''),
    2607: ('Jumping Beans', ''),
    2610: ('Dr. Tom Foolery', ''),
    2611: ('', ''),
    2616: ("Weird Beard's Disguise Shop", ''),
    2617: ('Silly Stunts', ''),
    2618: ('All That Razz', ''),
    2621: ('Paper Airplanes', ''),
    2624: ('Happy Hooligans', ''),
    2625: ('House of Bad Pies', ''),
    2626: ("Jesse's Joke Repair", ''),
    2629: ("The Laughin' Place", ''),
    2632: ('Clown Class', ''),
    2633: ('Tee-Hee Tea Shop', ''),
    2638: ('Toontown Playhouse', ''),
    2639: ('Monkey Tricks', ''),
    2643: ('Canned Bottles', ''),
    2644: ('Impractical Jokes', ''),
    2649: ('All Fun and Games Shop', ''),
    2652: ('', ''),
    2653: ('', ''),
    2654: ('Laughing Lessons', ''),
    2655: ('Funny Money Savings & Loan', ''),
    2656: ('Used Clown Cars', ''),
    2657: ("Frank's Pranks", ''),
    2659: ('Joy Buzzers to the World', ''),
    2660: ('Tickle Machines', ''),
    2661: ('Daffy Taffy', ''),
    2662: ('Dr. I.M. Euphoric', ''),
    2663: ('Toontown Cinerama', ''),
    2664: ('The Merry Mimes', ''),
    2665: ("Mary's Go Around Travel Company", ''),
    2666: ('Laughing Gas Station', ''),
    2667: ('Happy Times', ''),
    2669: ("Muldoon's Maroon Balloons", ''),
    2670: ('Soup Forks', ''),
    2671: ('', ''),
    2701: ('', ''),
    2704: ('Movie Multiplex', ''),
    2705: ("Wiseacre's Noisemakers", ''),
    2708: ('Blue Glue', ''),
    2711: ('Toontown Post Office', ''),
    2712: ('Chortle Cafe', ''),
    2713: ('Laughter Hours Cafe', ''),
    2714: ('Kooky CinePlex', ''),
    2716: ('Soup and Crack Ups', ''),
    2717: ('Bottled Cans', ''),
    2720: ('Crack Up Auto Repair', ''),
    2725: ('', ''),
    2727: ('Seltzer Bottles and Cans', ''),
    2728: ('Vanishing Cream', ''),
    2729: ('14 Karat Goldfish', ''),
    2730: ('News for the Amused', ''),
    2731: ('', ''),
    2732: ('Spaghetti and Goofballs', ''),
    2733: ('Cast Iron Kites', ''),
    2734: ('Suction Cups and Saucers', ''),
    2735: ('The Kaboomery', ''),
    2739: ("Sidesplitter's Mending", ''),
    2740: ('Used Firecrackers', ''),
    2741: ('', ''),
    2742: ('', ''),
    2743: ('Ragtime Dry Cleaners', ''),
    2744: ('', ''),
    2747: ('Visible Ink', ''),
    2748: ('Jest for Laughs', ''),
    2801: ('Sofa Whoopee Cushions', ''),
    2802: ('Inflatable Wrecking Balls', ''),
    2803: ('The Karnival Kid', ''),
    2804: ('Dr. Pulyurleg, Chiropractor', ''),
    2805: ('', ''),
    2809: ('The Punch Line Gym', ''),
    2814: ('Toontown Theatre', ''),
    2818: ('The Flying Pie', ''),
    2821: ('', ''),
    2822: ('Rubber Chicken Sandwiches', ''),
    2823: ('Sundae Funnies Ice Cream', ''),
    2824: ('Punchline Movie Palace', ''),
    2829: ('Phony Baloney', ''),
    2830: ("Zippy's Zingers", ''),
    2831: ("Professor Wiggle's House of Giggles", ''),
    2832: ('', ''),
    2833: ('', ''),
    2834: ('Funny Bone Emergency Room', ''),
    2836: ('', ''),
    2837: ('Hardy Harr Seminars', ''),
    2839: ('Barely Palatable Pasta', ''),
    2841: ('', ''),
    1506: ('Gag Shop', ''),
    1507: ('Toon Headquarters', ''),
    1508: ('Clothing Shop', ''),
    1510: ('', ''),
    1602: ('Used Life Preservers', ''),
    1604: ('Wet Suit Dry Cleaners', ''),
    1606: ("Hook's Clock Repair", ''),
    1608: ("Luff 'N Stuff", ''),
    1609: ('Every Little Bait', ''),
    1612: ('Dime & Quarterdeck Bank', ''),
    1613: ('Squid Pro Quo, Attorneys at Law', ''),
    1614: ('Trim the Nail Boutique', ''),
    1615: ("Yacht's All, Folks!", ''),
    1616: ("Blackbeard's Beauty Parlor", ''),
    1617: ('Out to See Optics', ''),
    1619: ('Disembark! Tree Surgeons', ''),
    1620: ('From Fore to Aft', ''),
    1621: ('Poop Deck Gym', ''),
    1622: ('Bait and Switches Electrical Shop', ''),
    1624: ('Soles Repaired While U Wait', ''),
    1626: ('Salmon Chanted Evening Formal Wear', ''),
    1627: ("Billy Budd's Big Bargain Binnacle Barn", ''),
    1628: ('Piano Tuna', ''),
    1629: ('', ''),
    1701: ('Buoys and Gulls Nursery School', ''),
    1703: ('Wok the Plank Chinese Food', ''),
    1705: ('Sails for Sale', ''),
    1706: ('Peanut Butter and Jellyfish', ''),
    1707: ('Gifts With a Porpoise', ''),
    1709: ('Windjammers and Jellies', ''),
    1710: ('Barnacle Bargains', ''),
    1711: ('Deep Sea Diner', ''),
    1712: ('Able-Bodied Gym', ''),
    1713: ("Art's Smart Chart Mart", ''),
    1714: ("Reel 'Em Inn", ''),
    1716: ('Mermaid Swimwear', ''),
    1717: ('Be More Pacific Ocean Notions', ''),
    1718: ('Run Aground Taxi Service', ''),
    1719: ("Duck's Back Water Company", ''),
    1720: ('The Reel Deal', ''),
    1721: ('All For Nautical', ''),
    1723: ("Squid's Seaweed", ''),
    1724: ("That's  a Moray!", ''),
    1725: ("Ahab's Prefab Sea Crab Center", ''),
    1726: ('Root Beer Afloats', ''),
    1727: ('This Oar That', ''),
    1728: ('Good Luck Horseshoe Crabs', ''),
    1729: ('', ''),
    1802: ('Nautical But Nice', ''),
    1804: ('Mussel Beach Gymnasium', ''),
    1805: ('Tackle Box Lunches', ''),
    1806: ('Cap Size Hat Store', ''),
    1807: ('Keel Deals', ''),
    1808: ('Knots So Fast', ''),
    1809: ('Rusty Buckets', ''),
    1810: ('Anchor Management', ''),
    1811: ("What's Canoe With You?", ''),
    1813: ('Pier Pressure Plumbing', ''),
    1814: ('The Yo Ho Stop and Go', ''),
    1815: ("What's Up, Dock?", ''),
    1818: ('Seven Seas Cafe', ''),
    1819: ("Docker's Diner", ''),
    1820: ('Hook, Line, and Sinker Prank Shop', ''),
    1821: ("King Neptoon's Cannery", ''),
    1823: ('The Clam Bake Diner', ''),
    1824: ('Dog Paddles', ''),
    1825: ('Wholly Mackerel! Fish Market', ''),
    1826: ("Claggart's Clever Clovis Closet", ''),
    1828: ("Alice's Ballast Palace", ''),
    1829: ('Seagull Statue Store', ''),
    1830: ('Lost and Flounder', ''),
    1831: ('Kelp Around the House', ''),
    1832: ("Melville's Massive Mizzenmast Mart", ''),
    1833: ('This Transom Man Custom Tailored Suits', ''),
    1834: ('Rudderly Ridiculous!', ''),
    1835: ('', ''),
    4503: ('Gag Shop', ''),
    4504: ('Toon Headquarters', ''),
    4506: ('Clothing Shop', ''),
    4508: ('', ''),
    4603: ("Tom-Tom's Drums", ''),
    4604: ('In Four-Four Time', ''),
    4605: ("Fifi's Fiddles", ''),
    4606: ('Casa De Castanets', ''),
    4607: ('Catchy Toon Apparel', ''),
    4609: ('Do, Rae, Me Piano Keys', ''),
    4610: ('Please Refrain', ''),
    4611: ('Tuning Forks and Spoons', ''),
    4612: ("Dr. Fret's Dentistry", ''),
    4614: ('Shave and a Haircut for a Song', ''),
    4615: ("Piccolo's Pizza", ''),
    4617: ('Happy Mandolins', ''),
    4618: ('Rests Rooms', ''),
    4619: ('More Scores', ''),
    4622: ('Chin Rest Pillows', ''),
    4623: ('Flats Sharpened', ''),
    4625: ('Tuba Toothpaste', ''),
    4626: ('Notations', ''),
    4628: ('Accidental Insurance', ''),
    4629: ("Riff's Paper Plates", ''),
    4630: ('Music Is Our Forte', ''),
    4631: ('Canto Help You', ''),
    4632: ('Dance Around the Clock Shop', ''),
    4635: ('Tenor Times', ''),
    4637: ('For Good Measure', ''),
    4638: ('Hard Rock Shop', ''),
    4639: ('Four Score Antiques', ''),
    4641: ('Blues News', ''),
    4642: ('Ragtime Dry Cleaners', ''),
    4645: ('Club 88', ''),
    4646: ('', ''),
    4648: ('Carry a Toon Movers', ''),
    4649: ('', ''),
    4652: ('Full Stop Shop', ''),
    4653: ('', ''),
    4654: ('Pitch Perfect Roofing', ''),
    4655: ("The Treble Chef's Cooking School", ''),
    4656: ('', ''),
    4657: ('Barbershop Quartet', ''),
    4658: ('Plummeting Pianos', ''),
    4659: ('', ''),
    4701: ('The Schmaltzy Waltz School of Dance', ''),
    4702: ('Timbre! Equipment for the Singing Lumberjack', ''),
    4703: ('I Can Handel It!', ''),
    4704: ("Tina's Concertina Concerts", ''),
    4705: ('Zither Here Nor There', ''),
    4707: ("Doppler's Sound Effects Studio", ''),
    4709: ('On Ballet! Climbing Supplies', ''),
    4710: ('Hurry Up, Slow Polka! School of Driving', ''),
    4712: ('C-Flat Tire Repair', ''),
    4713: ('B-Sharp Fine Menswear', ''),
    4716: ('Four-Part Harmonicas', ''),
    4717: ('Sonata Your Fault! Discount Auto Insurance', ''),
    4718: ('Chopin Blocks and Other Kitchen Supplies', ''),
    4719: ('Madrigal Motor Homes', ''),
    4720: ('Name That Toon', ''),
    4722: ('Overture Understudies', ''),
    4723: ('Haydn Go Seek Playground Supplies', ''),
    4724: ('White Noise for Girls and Boys', ''),
    4725: ('The Baritone Barber', ''),
    4727: ('Vocal Chords Braided', ''),
    4728: ("Sing Solo We Can't Hear You", ''),
    4729: ('Double Reed Bookstore', ''),
    4730: ('Lousy Lyrics', ''),
    4731: ('Toon Tunes', ''),
    4732: ('Etude Brute? Theatre Company', ''),
    4733: ('', ''),
    4734: ('', ''),
    4735: ('Accordions, If You Want In, Just Bellow!', ''),
    4736: ('Her and Hymn Wedding Planners', ''),
    4737: ('Harp Tarps', ''),
    4738: ('Canticle Your Fancy Gift Shop', ''),
    4739: ('', ''),
    4801: ("Marshall's Stacks", ''),
    4803: ('What a Mezzo! Maid Service', ''),
    4804: ('The Mixolydian School of Bartending', ''),
    4807: ('Relax the Bach', ''),
    4809: ("I Can't Understanza!", ''),
    4812: ('', ''),
    4817: ('The Ternary Pet Shop', ''),
    4819: ("Yuki's Ukeleles", ''),
    4820: ('', ''),
    4821: ("Anna's Cruises", ''),
    4827: ('Common Time Watches', ''),
    4828: ("Schumann's Shoes for Men", ''),
    4829: ("Pachelbel's Canonballs", ''),
    4835: ('Ursatz for Kool Katz', ''),
    4836: ('Reggae Regalia', ''),
    4838: ('Kazoology School of Music', ''),
    4840: ('Coda Pop Musical Beverages', ''),
    4841: ('Lyre, Lyre, Pants on Fire!', ''),
    4842: ('The Syncopation Corporation', ''),
    4843: ('', ''),
    4844: ('Con Moto Cycles', ''),
    4845: ("Ellie's Elegant Elegies", ''),
    4848: ('Lotsa Lute Savings & Loan', ''),
    4849: ('', ''),
    4850: ('The Borrowed Chord Pawn Shop', ''),
    4852: ('Flowery Flute Fleeces', ''),
    4853: ("Leo's Fenders", ''),
    4854: ("Wagner's Vocational Violin Videos", ''),
    4855: ('The Teli-Caster Network', ''),
    4856: ('', ''),
    4862: ("Quentin's Quintessen\x3tial Quadrilles", ''),
    4867: ("Mr. Costello's Yellow Cellos", ''),
    4868: ('', ''),
    4870: ("Ziggy's Zoo of Zigeuner\x3musik", ''),
    4871: ("Harry's House of Harmonious Humbuckers", ''),
    4872: ("Fast Freddie's Fretless Fingerboards", ''),
    4873: ('', ''),
    5501: ('Gag Shop', ''),
    5502: ('Toon HQ', ''),
    5503: ('Clothing Shop', ''),
    5505: ('', ''),
    5601: ('Eye of the Potato Optometry', ''),
    5602: ("Artie Choke's Neckties", ''),
    5603: ('Lettuce Alone', ''),
    5604: ('Cantaloupe Bridal Shop', ''),
    5605: ('Vege-tables and Chairs', ''),
    5606: ('Petals', ''),
    5607: ('Compost Office', ''),
    5608: ('Mom and Pop Corn', ''),
    5609: ('Berried Treasure', ''),
    5610: ("Black-eyed Susan's Boxing Lessons", ''),
    5611: ("Gopher's Gags", ''),
    5613: ('Crop Top Barbers', ''),
    5615: ("Bud's Bird Seed", ''),
    5616: ('Dew Drop Inn', ''),
    5617: ("Flutterby's Butterflies", ''),
    5618: ("Peas and Q's", ''),
    5619: ("Jack's Beanstalks", ''),
    5620: ('Rake It Inn', ''),
    5621: ('Grape Expectations', ''),
    5622: ('Petal Pusher Bicycles', ''),
    5623: ('Bubble Bird Baths', ''),
    5624: ("Mum's the Word", ''),
    5625: ('Leaf It Bees', ''),
    5626: ('Pine Needle Crafts', ''),
    5627: ('', ''),
    5701: ('From Start to Spinach', ''),
    5702: ("Jake's Rakes", ''),
    5703: ("Photo Cynthia's Camera Shop", ''),
    5704: ('Lisa Lemon Used Cars', ''),
    5705: ('Poison Oak Furniture', ''),
    5706: ('14 Carrot Jewelers', ''),
    5707: ('Musical Fruit', ''),
    5708: ("We'd Be Gone Travel Agency", ''),
    5709: ('Astroturf Mowers', ''),
    5710: ('Tuft Guy Gym', ''),
    5711: ('Garden Hosiery', ''),
    5712: ('Silly Statues', ''),
    5713: ('Trowels and Tribulations', ''),
    5714: ('Spring Rain Seltzer Bottles', ''),
    5715: ('Hayseed News', ''),
    5716: ('Take It or Leaf It Pawn Shop', ''),
    5717: ('The Squirting Flower', ''),
    5718: ('The Dandy Lion Exotic Pets', ''),
    5719: ('Trellis the Truth! Private Investi\x3gators', ''),
    5720: ('Vine and Dandy Menswear', ''),
    5721: ('Root 66 Diner', ''),
    5725: ('Barley, Hops, and Malt Shop', ''),
    5726: ("Bert's Dirt", ''),
    5727: ('Gopher Broke Savings & Loan', ''),
    5728: ('', ''),
    5802: ('Toon HQ', ''),
    5804: ('Just Vase It', ''),
    5805: ('Snail Mail', ''),
    5809: ('Fungi Clown School', ''),
    5810: ('Honeydew This', ''),
    5811: ('Lettuce Inn', ''),
    5815: ('Grass Roots', ''),
    5817: ('Apples and Oranges', ''),
    5819: ('Green Bean Jeans', ''),
    5821: ('Squash and Stretch Gym', ''),
    5826: ('Ant Farming Supplies', ''),
    5827: ('Dirt. Cheap.', ''),
    5828: ('Couch Potato Furniture', ''),
    5830: ('Spill the Beans', ''),
    5833: ('The Salad Bar', ''),
    5835: ('Flower Bed and Breakfast', ''),
    5836: ("April's Showers and Tubs", ''),
    5837: ('School of Vine Arts', ''),
    9501: ('Lullaby Library', ''),
    9503: ('The Snooze Bar', ''),
    9504: ('Gag Shop', ''),
    9505: ('Toon HQ', ''),
    9506: ('Clothing Shop', ''),
    9508: ('', ''),
    9601: ('Snuggle Inn', ''),
    9602: ('Forty Winks for the Price of Twenty', ''),
    9604: ("Ed's Red Bed Spreads", ''),
    9605: ('Cloud Nine Design', ''),
    9607: ("Big Mama's Bahama Pajamas", ''),
    9608: ('Cat Nip for Cat Naps', ''),
    9609: ('Deep Sleep for Cheap', ''),
    9613: ('Clock Cleaners', ''),
    9616: ('Lights Out Electric Co.', ''),
    9617: ('Crib Notes - Music to Sleep By', ''),
    9619: ('Relax to the Max', ''),
    9620: ("PJ's Taxi Service", ''),
    9622: ('Sleepy Time Pieces', ''),
    9625: ('Curl Up Beauty Parlor', ''),
    9626: ('Bed Time Stories', ''),
    9627: ('The Sleepy Teepee', ''),
    9628: ('Call It a Day Calendars', ''),
    9629: ('Silver Lining Jewelers', ''),
    9630: ('Rock to Sleep Quarry', ''),
    9631: ('Down Time Watch Repair', ''),
    9633: ('The Dreamland Screening Room', ''),
    9634: ('Mind Over Mattress', ''),
    9636: ('Insomniac Insurance', ''),
    9639: ('House of Hibernation', ''),
    9640: ('One Nightstand Furniture Company', ''),
    9642: ('Sawing Wood Slumber Lumber', ''),
    9643: ('Shut-Eye Optometry', ''),
    9644: ('Pillow Fights Nightly', ''),
    9645: ('The All Tucked Inn', ''),
    9647: ('Make Your Bed! Hardware Store', ''),
    9649: ('Snore or Less', ''),
    9650: ('Crack of Dawn Repairs', ''),
    9651: ('For Richer or Snorer', ''),
    9652: ('', ''),
    9703: ('Fly By Night Travel Agency', ''),
    9704: ('Night Owl Pet Shop', ''),
    9705: ('Asleep At The Wheel Car Repair', ''),
    9706: ('Tooth Fairy Dentistry', ''),
    9707: ("Dawn's Yawn & Garden Center", ''),
    9708: ('Bed Of Roses Florist', ''),
    9709: ('Pipe Dream Plumbers', ''),
    9710: ('REM Optometry', ''),
    9711: ('Wake-Up Call Phone Company', ''),
    9712: ("Counting Sheep - So You Don't Have To!", ''),
    9713: ('Wynken, Blynken & Nod, Attorneys at Law', ''),
    9714: ('Dreamboat Marine Supply', ''),
    9715: ('First Security Blanket Bank', ''),
    9716: ('Wet Blanket Party Planners', ''),
    9717: ("Baker's Dozin' Doughnuts", ''),
    9718: ("Sandman's Sandwiches", ''),
    9719: ('Armadillo Pillow Company', ''),
    9720: ('Talking In Your Sleep Voice Training', ''),
    9721: ('Snug As A Bug Rug Dealer', ''),
    9722: ('Dream On Talent Agency', ''),
    9725: ("Cat's Pajamas", ''),
    9727: ('You Snooze, You Lose', ''),
    9736: ('Dream Jobs Employment Agency', ''),
    9737: ("Waltzing Matilda's Dance School", ''),
    9738: ('House of Zzzzzs', ''),
    9740: ('Hit The Sack Fencing School', ''),
    9741: ("Don't Let The Bed Bugs Bite Exterminators", ''),
    9744: ("Rip Van Winkle's Wrinkle Cream", ''),
    9752: ('Midnight Oil & Gas Company', ''),
    9753: ("Moonbeam's Ice Creams", ''),
    9754: ('Sleepless in the Saddle All Night Pony Rides', ''),
    9755: ('Bedknobs & Broomsticks Movie House', ''),
    9756: ('', ''),
    9759: ('Sleeping Beauty Parlor', ''),
    3507: ('Gag Shop', ''),
    3508: ('Toon HQ', ''),
    3509: ('Clothing Shop', ''),
    3511: ('', ''),
    3601: ('Northern Lights Electric Company', ''),
    3602: ("Nor'easter Bonnets", ''),
    3605: ('', ''),
    3607: ('The Blizzard Wizard', ''),
    3608: ('Nothing to Luge', ''),
    3610: ("Mike's Massive Mukluk Mart", ''),
    3611: ("Mr. Cow's Snow Plows", ''),
    3612: ('Igloo Design', ''),
    3613: ('Ice Cycle Bikes', ''),
    3614: ('Snowflakes Cereal Company', ''),
    3615: ('Fried Baked Alaskas', ''),
    3617: ('Cold Air Balloon Rides', ''),
    3618: ('Snow Big Deal! Crisis Management', ''),
    3620: ('Skiing Clinic', ''),
    3621: ('The Melting Ice Cream Bar', ''),
    3622: ('', ''),
    3623: ('The Mostly Toasty Bread Company', ''),
    3624: ('Subzero Sandwich Shop', ''),
    3625: ("Auntie Freeze's Radiator Supply", ''),
    3627: ('St. Bernard Kennel Club', ''),
    3629: ('Pea Soup Cafe', ''),
    3630: ('Icy London, Icy France Travel Agency', ''),
    3634: ('Easy Chair Lifts', ''),
    3635: ('Used Firewood', ''),
    3636: ('Affordable Goosebumps', ''),
    3637: ("Kate's Skates", ''),
    3638: ('Toboggan or Not Toboggan', ''),
    3641: ("Fred's Red Sled Beds", ''),
    3642: ('Eye of the Storm Optics', ''),
    3643: ('Snowball Hall', ''),
    3644: ('Melted Ice Cubes', ''),
    3647: ('The Sanguine Penguin Tuxedo Shop', ''),
    3648: ('Instant Ice', ''),
    3649: ('Hambrrrgers', ''),
    3650: ('Antarctic Antiques', ''),
    3651: ("Frosty Freddy's Frozen Frankfurters", ''),
    3653: ('Ice House Jewelry', ''),
    3654: ('', ''),
    3702: ('Winter Storage', ''),
    3703: ('', ''),
    3705: ('Icicles Built for Two', ''),
    3706: ("Shiverin' Shakes Malt Shop", ''),
    3707: ('Snowplace Like Home', ''),
    3708: ("Pluto's Place", ''),
    3710: ('Dropping Degrees Diner', ''),
    3711: ('', ''),
    3712: ('Go With the Floe', ''),
    3713: ('Chattering Teeth, Subzero Dentist', ''),
    3715: ("Aunt Arctic's Soup Shop", ''),
    3716: ('Road Salt and Pepper', ''),
    3717: ('Juneau What I Mean?', ''),
    3718: ('Designer Inner Tubes', ''),
    3719: ('Ice Cube on a Stick', ''),
    3721: ("Noggin's Toboggan Bargains", ''),
    3722: ('Snow Bunny Ski Shop', ''),
    3723: ("Shakey's Snow Globes", ''),
    3724: ('The Chattering Chronicle', ''),
    3725: ('You Sleigh Me', ''),
    3726: ('Solar Powered Blankets', ''),
    3728: ('Lowbrow Snowplows', ''),
    3729: ('', ''),
    3730: ('Snowmen Bought & Sold', ''),
    3731: ('Portable Fireplaces', ''),
    3732: ('The Frozen Nose', ''),
    3734: ('Icy Fine, Do You? Optometry', ''),
    3735: ('Polar Ice Caps', ''),
    3736: ('Diced Ice at a Nice Price', ''),
    3737: ('Downhill Diner', ''),
    3738: ("Heat-Get It While It's Hot", ''),
    3739: ('', '') }
ClosetTimeoutMessage = 'Sorry, you ran out\n of time.'
ClosetNotOwnerMessage = "This isn't your closet, but you may try on the clothes."
ClosetPopupOK = lOK
ClosetPopupCancel = lCancel
ClosetDiscardButton = 'Remove'
ClosetAreYouSureMessage = 'You have deleted some clothes.  Do you really want to delete them?'
ClosetYes = lYes
ClosetNo = lNo
ClosetVerifyDelete = 'Really delete %s?'
ClosetShirt = 'this shirt'
ClosetShorts = 'these shorts'
ClosetSkirt = 'this skirt'
ClosetDeleteShirt = 'Delete\nshirt'
ClosetDeleteShorts = 'Delete\nshorts'
ClosetDeleteSkirt = 'Delete\nskirt'
EstateOwnerLeftMessage = "Sorry, the owner of this estate left.  You'll be sent to the playground in %s seconds"
EstatePopupOK = lOK
EstateTeleportFailed = "Couldn't go home. Try again!"
EstateTeleportFailedNotFriends = "Sorry, %s is in a toon's estate that you are not friends with."
AvatarsHouse = '%s\n House'
BankGuiCancel = lCancel
BankGuiOk = 'Ok'
DistributedBankNoOwner = 'Sorry, this is not your bank.'
DistributedBankNotOwner = 'Sorry, this is not your bank.'
FishGuiCancel = lCancel
FishGuiOk = 'Sell All'
FishTankValue = 'Hi, %(name)s! You have %(num)s fish in your bucket worth a total of %(value)s jellybeans. Do you want to sell them all?'

def GetPossesive(name):
    if name[-1:] == 's':
        possesive = name + "'"
    else:
        possesive = name + "'s"
    return possesive

PetTrait2descriptions = {
    'hungerThreshold': ('Always Hungry', 'Often Hungry', 'Sometimes Hungry', 'Rarely Hungry'),
    'boredomThreshold': ('Always Bored', 'Often Bored', 'Sometimes Bored', 'Rarely Bored'),
    'angerThreshold': ('Always Grumpy', 'Often Grumpy', 'Sometimes Grumpy', 'Rarely Grumpy'),
    'forgetfulness': ('Always Forgets', 'Often Forgets', 'Sometimes Forgets', 'Rarely Forgets'),
    'excitementThreshold': ('Very Calm', 'Pretty Calm', 'Pretty Excitable', 'Very Excitable'),
    'sadnessThreshold': ('Always Sad', 'Often Sad', 'Sometimes Sad', 'Rarely Sad'),
    'restlessnessThreshold': ('Always Restless', 'Often Restless', 'Sometimes Restless', 'Rarely Restless'),
    'playfulnessThreshold': ('Rarely Playful', 'Sometimes Playful', 'Often Playful', 'Always Playful'),
    'lonelinessThreshold': ('Always Lonely', 'Often Lonely', 'Sometimes Lonely', 'Rarely Lonely'),
    'fatigueThreshold': ('Always Tired', 'Often Tired', 'Sometimes Tired', 'Rarely Tired'),
    'confusionThreshold': ('Always Confused', 'Often Confused', 'Sometimes Confused', 'Rarely Confused'),
    'surpriseThreshold': ('Always Surprised', 'Often Surprised', 'Sometimes Surprised', 'Rarely Surprised'),
    'affectionThreshold': ('Rarely Affectionate', 'Sometimes Affectionate', 'Often Affectionate', 'Always Affectionate') }
FireworksInstructions = 'Toon HQ: Hit the "Page Up" key to see better.'
FireworksJuly4Beginning = 'Toon HQ: Welcome to summer fireworks! Enjoy the show!'
FireworksJuly4Ending = 'Toon HQ: Hope you enjoyed the show! Have a great summer!'
FireworksNewYearsEveBeginning = 'Toon HQ: Happy New Year! Enjoy the fireworks show!'
FireworksNewYearsEveEnding = 'Toon HQ: Hope you enjoyed the show! Happy %s!' % (time.localtime()[0] + 1)
TIP_NONE = 0
TIP_GENERAL = 1
TIP_STREET = 2
TIP_MINIGAME = 3
TIP_COGHQ = 4
TIP_ESTATE = 5
TipTitle = 'TOON TIP:'
TipDict = {
    TIP_NONE: ('',),
    TIP_GENERAL: ('Quickly check your ToonTask progress by holding down the "End" key.', 'Quickly check your Gag page by holding down the "Home" key.', 'Open your Friends List by pressing the "F7" key.', 'Open or close your Shticker Book by pressing the "F8" key.', 'You can look up by pressing the "Page Up" key and look down by pressing the "Page Down" key.', 'Press the "Control" key to jump.', 'Press the "F9" key to take a screenshot, which will be saved in your Toontown folder on your computer.', 'You can change your screen resolution, adjust audio, and control other options on the Options Page in the Shticker Book.', "Try on your friend's clothing at the closet in their house.", 'You can go to your house using the "Go Home" button on your map.', 'Every time you turn in a completed ToonTask your Laff Points are automatically refilled.', 'You can browse the selection at Clothing Stores even without a clothing ticket.', 'Rewards for some ToonTasks allow you to carry more Gags and Jellybeans.', 'You can have up to 50 friends on your Friends List.', 'Some ToonTask rewards let you teleport to playgrounds in Toontown by using the Map Page in the Shticker Book.', 'Increase your Laff Points in the Playgrounds by collecting treasures like stars and ice cream cones.', 'To heal quickly after a battle, go to your estate and play with your Doodle.', 'Change to different views of your Toon by pressing the Tab Key.', 'Sometimes you can find several different ToonTasks offered for the same reward. Shop around!', 'Finding friends with similar ToonTasks is a fun way to progress through the game.', 'You never need to save your Toontown progress. The Toontown servers continually save all the necessary information.', 'You can whisper to other Toons either by clicking on them or by selecting them from your Friends List.', 'Some SpeedChat phrases play emotion animations on your Toon.', 'If the area you are in is crowded, try changing Districts. Go to the District Page in the Shticker Book and select a different one.', 'If you actively rescue buildings you will get a bronze, silver, or gold star above your Toon.', 'If you rescue enough buildings to get a star above your head you may find your name on the blackboard in a Toon HQ.', 'Rescued buildings are sometimes recaptured by the Cogs. The only way to keep your star is to go out and rescue more buildings!', 'The names of your Secret Friends will appear in Blue.', 'See if you can collect all the fish in Toontown!', 'Different ponds hold different fish. Try them all!', 'When your fishing bucket is full sell your fish to the Fishermen in the Playgrounds.', 'You can sell your fish to the Fishermen or inside Pet Shops.', 'Stronger fishing rods catch heavier fish but cost more jellybeans to use.', 'You can purchase stronger fishing rods in the Cattlelog.', 'Heavier fish are worth more Jellybeans to the Pet Shop.', 'Rare fish are worth more Jellybeans to the Pet Shop.', 'You can sometimes find bags of Jellybeans while fishing.', 'Some ToonTasks require fishing items out of the ponds.', 'Fishing ponds in the Playgrounds have different fish than ponds on the streets.', 'Some fish are really rare. Keep fishing until you collect them all!', 'The pond at your estate has fish that can only be found there.', 'For every 10 species you catch, you will get a fishing trophy!', 'You can see what fish you have collected in your Shticker Book.', 'Some fishing trophies reward you with a Laff Boost.', 'Fishing is a good way to earn more Jellybeans.', 'Adopt a Doodle at the Pet Shop!', 'Pet Shops get new Doodles to sell every day.', 'Visit the Pet Shops every day to see what new Doodles they have.', 'Different neighborhoods have different Doodles offered for adoption.'),
    TIP_STREET: ('There are four types of Cogs: Lawbots, Cashbots, Sellbots, and Bossbots.', 'Each Gag Track has different amounts of accuracy and damage.', 'Sound Gags will affect all Cogs but will wake up any lured Cogs.', 'Defeating Cogs in strategic order can greatly increase your chances of winning battles.', 'The Toon-Up Gag Track lets you heal other Toons in battle.', 'Gag experience points are doubled during a Cog Invasion!', 'Multiple Toons can team up and use the same Gag Track in battle to get bonus Cog damage.', 'In battle, Gags are used in order from top to bottom as displayed on the Gag Menu.', 'The row of circular lights over Cog Building elevators show how many floors will be inside.', 'Click on a Cog to see more details.', 'Using high level gags against low level Cogs will not earn any experience points.', 'A gag that will earn experience has a blue background on the Gag Menu in battle.', 'Gag experience is multiplied when used inside Cog Buildings. Higher floors have higher multipliers.', 'When a Cog is defeated, each Toon in that round will get credit for the Cog when the battle is over.', 'Each street in Toontown has different Cog levels and types.', 'Sidewalks are safe from Cogs.', 'On the streets, side doors tell knock-knock jokes when approached.', 'Some ToonTasks train you for new Gag Tracks. You only get to choose six of the seven Gag Tracks, so choose carefully!', 'Traps are only useful if you or your friends coordinate using Lure in battle.', 'Higher level Lures are less likely to miss.', 'Lower level gags have a lower accuracy against high level Cogs.', 'Cogs cannot attack once they have been lured in battle.', 'When you and your friends defeat a Cog Building you are rewarded with portraits inside the rescued Toon Building.', 'Using a Toon-Up gag on a Toon with a full Laffmeter will not earn Toon-Up experience.', 'Cogs will be briefly stunned when hit by any gag. This increases the chance that other Gags in the same round will hit.', 'Drop Gags have low chance of hitting, but accuracy is increased when Cogs are first hit by another gag in the same round.', 'When you\'ve defeated enough Cogs, use the "Cog Radar" by clicking the Cog icons on the Cog Gallery page in your Shticker book.', 'During a battle, you can tell which Cog your teammates are attacking by looking at the dashes (-) and Xs.', 'During a battle, Cogs have a light on them that displays their health; green is healthy, red is nearly destroyed.', 'A maximum of four Toons can battle at once.', 'On the street, Cogs are more likely to join a fight against multiple Toons than just one Toon.', 'The two most difficult Cogs of each type are only found in buildings.', 'Drop gags never work against lured Cogs.', 'Cogs tend to attack the Toon that has done them the most damage.', 'Sound gags do not get bonus damage against lured Cogs.', 'If you wait too long to attack a lured Cog, it will wake up. Higher level lures last longer.', 'There are fishing ponds on every street in Toontown. Some streets have unique fish.'),
    TIP_MINIGAME: ('After you fill up your Jellybean jar, any Jellybeans you get from Trolley Games automatically spill over into your bank.', 'You can use the arrow keys instead of the mouse in the "Match Minnie" Trolley Game.', 'In the Cannon Game you can use the arrow keys to move your cannon and press the "Control" key to fire.', 'In the Ring Game, bonus points are awarded when the entire group successfully swims through its rings.', 'A perfect game of Match Minnie will double your points.', 'In the Tug-O-War you are awarded more Jellybeans if you play against a tougher Cog.', 'Trolley Game difficulty varies by neighborhood; ' + lToontownCentral + ' has the easiest and ' + lDonaldsDreamland + ' has the hardest.', 'Certain Trolley Games can only be played in a group.'),
    TIP_COGHQ: ('You must complete your Cog Disguise before entering the Boss Building.', 'You can jump on Cog Goons to temporarily disable them.', 'Collect Cog Merits by defeating Cogs in battle.', 'You get more Merits from higher level Cogs.', 'When you collect enough Cog Merits to earn a promotion, go see the Sellbot VP!', 'You can talk like a Cog when you are wearing your Cog Disguise.', 'Up to eight Toons can join together to fight the Sellbot VP.', 'The Sellbot VP is at the top of Cog HQ.', 'Inside Cog Factories, follow stairs leading up to find your way to the Foreman.', 'Each time you battle through the factory you will gain one part of your Cog Disguise.', 'You can check the progress of your Cog Disguise in your Shticker Book.', 'You can check your merit progress on your Disguise Page in your Shticker Book.', 'Make sure you have full gags and a full Laff Meter before going to see the VP.', 'As you get promoted your Cog disguise updates.', 'You must defeat the ' + Foreman + ' to recover a Cog Disguise part.'),
    TIP_ESTATE: ('Doodles can understand some SpeedChat phrases. Try them!', 'Use the "Pet" SpeedChat menu to ask your Doodle to do tricks.', "You can teach Doodles tricks with training lessons from Clarabelle's Cattlelog.", 'Reward your Doodle for doing tricks.', "If you visit a friend's estate, your Doodle will come too.", 'Feed your Doodle a jellybean when it is hungry.', 'Click on a Doodle to get a menu where you can Feed, Scratch, and Call him.', 'Doodles love company. Invite your friends over to play!', 'All Doodles have unique personalities.', 'You can return your Doodle and adopt a new one at the Pet Shops.', 'When a Doodle performs a trick, the Toons around it heal.', 'Doodles become better at tricks with practice. Keep at it!', 'More advanced Doodle tricks heal Toons faster.', 'Experienced Doodles can perform more tricks before getting tired.', 'You can see a list of nearby Doodles in your Friends List.', "Purchase furniture from Clarabelle's Cattlelog to decorate your house.", 'The bank inside your house holds extra jellybeans.', 'The closet inside your house holds extra clothes.', "Go to your friend's house and try on his clothes.", "Purchase better fishing rods from Clarabelle's Cattlelog.", "Purchase larger banks from Clarabelle's Cattlelog.", 'Call Clarabelle using the phone inside your house.', 'Clarabelle sells a larger closet that holds more clothing.', 'Make room in your closet before using a Clothing Ticket.', 'Clarabelle sells everything you need to decorate your house.', 'Check your mailbox for deliveries after ordering from Clarabelle.', "Clothing from Clarabelle's Cattlelog takes one hour to be delivered.", "Wallpaper and flooring from Clarabelle's Cattlelog take one hour to be delivered.", "Furniture from Clarabelle's Cattlelog takes a full day to be delivered.", 'Store extra furniture in your attic.', 'You will get a notice from Clarabelle when a new Cattlelog is ready.', 'You will get a notice from Clarabelle when a Cattlelog delivery arrives.', 'New Cattlelogs are delivered each week.', 'Look for limited-edition holiday items in the Cattlelog.', 'Move unwanted furniture to the trash can.', 'Some fish, like the Holey Mackerel, are more commonly found in Toon Estates.', 'You can invite your friends to your Estate using SpeedChat.', 'Did you know the color of your house matches the color of your Pick-A-Toon panel?') }
FishGenusNames = {
    0: 'Balloon Fish',
    2: 'Cat Fish',
    4: 'Clown Fish',
    6: 'Frozen Fish',
    8: 'Star Fish',
    10: 'Holey Mackerel',
    12: 'Dog Fish',
    14: 'Amore Eel',
    16: 'Nurse Shark',
    18: 'King Crab',
    20: 'Moon Fish',
    22: 'Sea Horse',
    24: 'Pool Shark',
    26: 'Bear Acuda',
    28: 'Cutthroat Trout',
    30: 'Piano Tuna',
    32: 'Peanut Butter & Jellyfish',
    34: 'Devil Ray' }
FishSpeciesNames = {
    0: ('Balloon Fish', 'Hot Air Balloon Fish', 'Weather Balloon Fish', 'Water Balloon Fish', 'Red Balloon Fish'),
    2: ('Cat Fish', 'Siamese Cat Fish', 'Alley Cat Fish', 'Tabby Cat Fish', 'Tom Cat Fish'),
    4: ('Clown Fish', 'Sad Clown Fish', 'Party Clown Fish', 'Circus Clown Fish'),
    6: ('Frozen Fish',),
    8: ('Star Fish', 'Five Star Fish', 'Rock Star Fish', 'Shining Star Fish', 'All Star Fish'),
    10: ('Holey Mackerel',),
    12: ('Dog Fish', 'Bull Dog Fish', 'Hot Dog Fish', 'Dalmatian Dog Fish', 'Puppy Dog Fish'),
    14: ('Amore Eel', 'Electric Amore Eel'),
    16: ('Nurse Shark', 'Clara Nurse Shark', 'Florence Nurse Shark'),
    18: ('King Crab', 'Alaskan King Crab', 'Old King Crab'),
    20: ('Moon Fish', 'Full Moon Fish', 'Half Moon Fish', 'New Moon Fish', 'Crescent Moon Fish', 'Harvest Moon Fish'),
    22: ('Sea Horse', 'Rocking Sea Horse', 'Clydesdale Sea Horse', 'Arabian Sea Horse'),
    24: ('Pool Shark', 'Kiddie Pool Shark', 'Swimming Pool Shark', 'Olympic Pool Shark'),
    26: ('Brown Bear Acuda', 'Black Bear Acuda', 'Koala Bear Acuda', 'Honey Bear Acuda', 'Polar Bear Acuda', 'Panda Bear Acuda', 'Kodiac Bear Acuda', 'Grizzly Bear Acuda'),
    28: ('Cutthroat Trout', 'Captain Cutthroat Trout', 'Scurvy Cutthroat Trout'),
    30: ('Piano Tuna', 'Grand Piano Tuna', 'Baby Grand Piano Tuna', 'Upright Piano Tuna', 'Player Piano Tuna'),
    32: ('Peanut Butter & Jellyfish', 'Grape PB&J Fish', 'Crunchy PB&J Fish', 'Strawberry PB&J Fish', 'Concord Grape PB&J Fish'),
    34: ('Devil Ray',) }
FishFirstNames = ('', 'Angel', 'Artic', 'Baby', 'Bermuda', 'Big', 'Brooke', 'Bubbles', 'Buster', 'Candy', 'Captain', 'Chip', 'Chub', 'Coral', 'Doctor', 'Dusty', 'Emperor', 'Fangs', 'Fat', 'Fishy', 'Flipper', 'Flounder', 'Freckles', 'Honey', 'Jack', 'King', 'Little', 'Marlin', 'Miss', 'Mister', 'Peaches', 'Pinky', 'Prince', 'Princess', 'Professor', 'Puffy', 'Queen', 'Rainbow', 'Ray', 'Rosy', 'Rusty', 'Salty', 'Sam', 'Sandy', 'Scales', 'Sharky', 'Sir', 'Skippy', 'Slipper', 'Snapper', 'Speck', 'Spike', 'Spotty', 'Star', 'Sugar', 'Super', 'Tiger', 'Tiny', 'Whiskers')
FishLastPrefixNames = ('', 'Beach', 'Black', 'Blue', 'Boar', 'Bull', 'Cat', 'Deep', 'Double', 'East', 'Fancy', 'Flaky', 'Flat', 'Fresh', 'Giant', 'Gold', 'Golden', 'Gray', 'Green', 'Hog', 'Jabber', 'Jelly', 'Lady', 'Leather', 'Lemon', 'Long', 'Northern', 'Ocean', 'Octo', 'Oil', 'Pearl', 'Puff', 'Red', 'Ribbon', 'River', 'Rock', 'Ruby', 'Rudder', 'Salt', 'Sea', 'Silver', 'Snorkel', 'Sole', 'Southern', 'Spikey', 'Surf', 'Sword', 'Tiger', 'Triple', 'Tropical', 'Tuna', 'Wave', 'Weak', 'West', 'White', 'Yellow')
FishLastSuffixNames = ('', 'ball', 'bass', 'belly', 'bug', 'burglar', 'butter', 'claw', 'cobbler', 'crab', 'croaker', 'drum', 'fin', 'fish', 'flapper', 'flipper', 'ghost', 'grunt', 'head', 'jacket', 'jumper', 'mackerel', 'moon', 'mouth', 'mullet', 'neck', 'nose', 'perch', 'roughy', 'runner', 'sail', 'shark', 'shell', 'silk', 'slime', 'snapper', 'stink', 'tail', 'toad', 'trout', 'water')
CogPartNames = ('Upper Left Leg', 'Lower Left Leg', 'Left Foot', 'Upper Right Leg', 'Lower Right Leg', 'Right Foot', 'Left Shoulder', 'Right Shoulder', 'Chest', 'Health Meter', 'Pelvis', 'Upper Left Arm', 'Lower Left Arm', 'Left Hand', 'Upper Right Arm', 'Lower Right Arm', 'Right Hand')
CogPartNamesSimple = ('Upper Torso',)
FishBingoBingo = 'BINGO!'
FishBingoVictory = 'VICTORY!!'
FishBingoJackpot = 'JACKPOT!'
FishBingoGameOver = 'GAME OVER'
FishBingoIntermission = 'Intermission\nEnds In:'
FishBingoNextGame = 'Next Game\nStarts In:'
FishBingoTypeNormal = 'Classic'
FishBingoTypeCorners = 'Four Corners'
FishBingoTypeDiagonal = 'Diagonals'
FishBingoTypeThreeway = 'Three Way'
FishBingoTypeBlockout = 'BLOCKOUT!'
FishBingoStart = "It's time for Fish Bingo!  Go to any available pier to play!"
FishBingoEnd = 'Hope you had fun playing Fish Bingo.'
FishBingoHelpMain = 'Welcome to Toontown Fish Bingo!  Everyone at the pond works together to fill the card before time runs out.'
FishBingoHelpFlash = 'When you catch a fish, click on one of the flashing squares to mark the card.'
FishBingoHelpNormal = 'This is a Classic Bingo card.  Mark any row down, across or diagonally to win.'
FishBingoHelpDiagonals = 'Mark both of the diagonals to win.'
FishBingoHelpCorners = 'An easy Corners card.  Mark all four corners to win.'
FishBingoHelpThreeway = "Three-way.  Mark both diagonals and the middle row to win.  This one isn't easy!"
FishBingoHelpBlockout = 'Blockout!.  Mark the entire card to win.  You are competing against all the other ponds for a huge jackpot!'
FishBingoOfferToSellFish = 'Your fish bucket is full. Would you like to sell your fish?'
ResistanceToonupMenu = 'Toon-up'
ResistanceToonupItem = '%s Toon-up'
ResistanceToonupItemMax = 'Max'
ResistanceToonupChat = 'Toons of the World, Toon-up!'
ResistanceRestockMenu = 'Gag-up'
ResistanceRestockItem = 'Gag-up %s'
ResistanceRestockItemAll = 'All'
ResistanceRestockChat = 'Toons of the World, Gag-up!'
ResistanceMoneyMenu = 'Jellybeans'
ResistanceMoneyItem = '%s Jellybeans'
ResistanceMoneyChat = 'Toons of the World, Spend Wisely!'
