# File: L (Python 2.2)

import string
Mickey = 'Mickey'
Minnie = 'Minnie'
Donald = 'Donald'
Daisy = 'Daisy'
Goofy = 'Goofy'
Pluto = 'Pluto'
Flippy = 'Flippy'
MickeyMouse = 'Mickey Mouse'
AIStartDefaultDistrict = 'Sillyville'
Cog = 'Cog'
Cogs = 'Cogs'
ACog = 'a Cog'
TheCogs = 'the Cogs'
TheFish = 'the Fish'
AFish = 'a fish'
Level = 'level'
QuestsCompleteString = 'Complete'
QuestsNotChosenString = 'Not chosen'
QuestsDefaultGreeting = ('Hello, _avName_!', 'Hi, _avName_!', 'Hey there, _avName_!', 'Say there, _avName_!', 'Welcome, _avName_!', 'Howdy, _avName_!', 'How are you, _avName_?', 'Greetings _avName_!')
QuestsDefaultIncomplete = ("How's that task coming, _avName_?", 'Looks like you still have more work to do on that task!', 'Keep up the good work, _avName_!', 'Keep trying to finish that task.  I know you can do it!', 'Keep trying to complete that task, we are counting on you!', 'Keep working on that ToonTask!')
QuestsDefaultIncompleteProgress = ('You came to the right place, but you need to finish your ToonTask first.', 'When you are finished with that ToonTask, come back here.', 'Come back when you are finished with your ToonTask.')
QuestsDefaultIncompleteWrongNPC = ('Nice work on that ToonTask. You should go visit _toNpcName_._where_', 'Looks like you are ready to finish your ToonTask. Go see _toNpcName_._where_.', 'Go see _toNpcName_ to finish your ToonTask._where_')
QuestsDefaultComplete = ('Nice work! Here is your reward...', 'Great job, _avName_! Take this reward...', 'Wonderful job, _avName_! Here is your reward...')
QuestsDefaultLeaving = ('Bye!', 'Goodbye!', 'So long, _avName_.', 'See ya, _avName_!', 'Good luck!', 'Have fun in Toontown!', 'See you later!')
QuestsDefaultReject = ('Hello.', 'Can I help you?', 'How are you?', 'Hello there.', "I'm a little busy now, _avName_.", 'Yes?', 'Howdy, _avName_!', 'Welcome, _avName_!', "Hey, _avName_! How's it going?", 'Did you know you can open your Shticker Book by hitting F8?', 'You can use your map to teleport back to the playground!', 'You can make friends with other players by clicking on them.', 'You can discover more about a ' + Cog + ' by clicking on him.', 'Gather treasures in the playgrounds to fill your Laff Meter.', Cog + ' buildings are dangerous places! Do not go in alone!', 'When you lose a battle, the ' + Cogs + ' take all your Gags.', 'To get more gags, play Trolley games!', 'You can get more Laff Points by completing ToonTasks.', 'Every ToonTask gives you a reward.', 'Some rewards let you carry more Gags.', 'If you win a battle, you get ToonTask credit for every ' + Cog + ' defeated.', 'If you recapture a ' + Cog + ' building, go back inside to see a special thank-you from its owner!', 'If you hold down the Page Up key, you can look up!', 'If you press the Tab key, you can see different views of your surroundings!', "To show secret friends what you're thinking, enter a '.' before your thought.", 'If a ' + Cog + ' is stunned, it is more difficult for them to avoid falling objects.', 'Each kind of ' + Cog + ' building has a distinct look.', 'Defeating ' + Cogs + ' on the higher floors of a building will give you greater skill rewards.')
QuestsDefaultTierNotDone = ('Hello, _avName_! You must finish your current ToonTasks before getting a new one.', 'Hi there! You need to finish the ToonTasks you are working on in order to get a new one.', 'Hi, _avName_! Before I can give you a new ToonTask, you need to finish the ones you have.')
QuestsDefaultQuest = None
QuestsDefaultVisitQuestDialog = ('I heard _toNpcName_ is looking for you._where_', 'Stop by and see _toNpcName_ when you get a chance._where_', 'Pay a visit to _toNpcName_ next time you are over that way._where_', 'If you get a chance, stop in and say hi to _toNpcName_._where_', '_toNpcName_ will give you your next ToonTask._where_')
QuestsCogQuestProgress = '%(progress)s of %(numCogs)s defeated'
QuestsCogQuestHeadline = 'WANTED'
QuestsCogQuestQTStringS = 'I need to defeat %(cogName)s%(cogLoc)s.'
QuestsCogQuestQTStringP = 'I need to defeat some %(cogName)s%(cogLoc)s.'
QuestsCogQuestDefeat = 'Defeat %s'
QuestsCogNewbieQuestObjective = 'Help Toons with %d laff points or less defeat %s'
QuestsCogNewbieQuestCaption = 'Help a new Toon %d laff or less'
QuestsCogNewbieQuestAux = 'Defeat:'
QuestsNewbieQuestHeadline = 'APPRENTICE'
QuestsCogTrackQuestProgress = '%(progress)s of %(numCogs)s defeated'
QuestsCogTrackQuestHeadline = 'WANTED'
QuestsCogTrackQuestQTString = 'I need to defeat %(cogText)s%(cogLoc)s.'
QuestsCogTrackQuestDefeat = 'Defeat %s'
QuestsCogLevelQuestProgress = '%(progress)s of %(numCogs)s defeated'
QuestsCogLevelQuestHeadline = 'WANTED'
QuestsCogLevelQuestQTString = 'I need to defeat %(cogText)s%(cogLoc)s.'
QuestsCogLevelQuestDefeat = 'Defeat %s'
QuestsCogLevelQuestDesc = 'a Level %(level)s+ Cog'
QuestsCogLevelQuestDescC = '%(count)s Level %(level)s+ Cogs'
QuestsCogLevelQuestDescI = 'some Level %(level)s+ Cogs'
QuestsCogLevelQuestQTString = 'I need to defeat %(objective)s%(location)s.'
QuestsBuildingQuestFloorNumbers = ('', 'two+', 'three+', 'four+', 'five+')
QuestsBuildingQuestBuilding = 'Building'
QuestsBuildingQuestBuildings = 'Buildings'
QuestsBuildingQuestHeadline = 'DEFEAT'
QuestsBuildingQuestProgressString = '%(progress)s of %(num)s defeated'
QuestsBuildingQuestString = 'Defeat %s'
QuestsBuildingQuestQTString = 'I need to defeat %(objective)s%(location)s.'
QuestsBuildingQuestDesc = 'a %(type)s Building'
QuestsBuildingQuestDescF = 'a %(floors)s story %(type)s Building'
QuestsBuildingQuestDescC = '%(count)s %(type)s Buildings'
QuestsBuildingQuestDescCF = '%(count)s %(floors)s story %(type)s Buildings'
QuestsBuildingQuestDescI = 'some %(type)s Buildings'
QuestsBuildingQuestDescIF = 'some %(floors)s story %(type)s Buildings'
QuestsDeliverGagQuestProgress = '%(progress)s of %(numGags)s delivered'
QuestsDeliverGagQuestHeadline = 'DELIVER'
QuestsDeliverGagQuestToQTStringS = 'I need to deliver %(gagName)s.'
QuestsDeliverGagQuestToQTStringP = 'I need to deliver some %(gagName)s.'
QuestsDeliverGagQuestQTString = 'I need make a delivery.'
QuestsDeliverGagQuestString = 'Deliver %s'
QuestsDeliverGagQuestStringLong = 'Deliver %s to _toNpcName_.'
QuestsDeliverItemQuestProgress = ''
QuestsDeliverItemQuestHeadline = 'DELIVER'
QuestsDeliverItemQuestQTString = 'I need to deliver %(article)s%(itemName)s.'
QuestsDeliverItemQuestString = 'Deliver %s'
QuestsDeliverItemQuestStringLong = 'Deliver %s to _toNpcName_.'
QuestsVisitQuestProgress = ''
QuestsVisitQuestHeadline = 'VISIT'
QuestsVisitQuestStringShort = 'Visit'
QuestsVisitQuestStringLong = 'Visit _toNpcName_'
QuestsRecoverItemQuestProgress = '%(progress)s of %(numItems)s recovered'
QuestsRecoverItemQuestHeadline = 'RECOVER'
QuestsRecoverItemQuestReturnToHQQTString = 'I need to return %s to an HQ Officer.'
QuestsRecoverItemQuestReturnToQTString = 'I need to return %(item)s to %(npcName)s.'
QuestsRecoverItemQuestGoToHQQTString = 'I need to go to a Toon HQ.'
QuestsRecoverItemQuestGoToPlaygroundQTString = 'I need to go to %s Playground.'
QuestsRecoverItemQuestGoToStreetQTString = 'I need to go to %(street)s in %(hood)s.'
QuestsRecoverItemQuestVisitBuildingQTString = 'I need to visit %s.'
QuestsRecoverItemQuestWhereIsBuildingQTString = 'Where is %s?'
QuestsRecoverItemQuestRecoverFromQTString = 'I need to recover %(item)s from %(holder)s%(loc)s.'
QuestsRecoverItemQuestString = 'Recover %(item)s from %(holder)s'
QuestsTrackChoiceQuestHeadline = 'CHOOSE'
QuestsTrackChoiceQuestQTString = 'I need to choose between %(trackA)s and %(trackB)s.'
QuestsTrackChoiceQuestMaybeQTString = 'Maybe I should choose %s.'
QuestsTrackChoiceQuestString = 'Choose between %(trackA)s and %(trackB)s'
QuestsFriendQuestHeadline = 'FRIEND'
QuestsFriendQuestQTString = 'I need to make a friend.'
QuestsFriendQuestString = 'Make a friend'
QuestsFriendNewbieQuestString = 'Make %d friends %d laff or less'
QuestsFriendNewbieQuestProgress = '%(progress)s of %(numFriends)s made'
QuestsFriendNewbieQuestObjective = 'Make friends with %d Toons with %d laff points or less'
QuestsTrolleyQuestHeadline = 'TROLLEY'
QuestsTrolleyQuestQTString = 'I need to ride the trolley.'
QuestsTrolleyQuestString = 'Ride on the trolley'
QuestsTrolleyQuestStringShort = 'Ride the trolley'
QuestsMinigameNewbieQuestString = '%d Minigames'
QuestsMinigameNewbieQuestProgress = '%(progress)s of %(numMinigames)s Played'
QuestsMinigameNewbieQuestObjective = 'Play %d minigames with Toons with %d laff points or less'
QuestsMinigameNewbieQuestQTString = 'I need to play minigames with new Toons.'
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
QuestsStreetLocationThisPlayground = 'in this playground'
QuestsStreetLocationThisStreet = 'on this street'
QuestsStreetLocationNamedPlayground = 'in the %s playground'
QuestsStreetLocationNamedStreet = 'on %s in %s'
QuestsLocationBuilding = "%s's building is called"
QuestsLocationBuildingVerb = 'which is'
QuestsLocationParagraph = '\x7%(building)s "%(buildingName)s"...\x7...%(buildingVerb)s %(street)s.'
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
        'Key to Daisy Gardens',
        'Keys to Daisy Gardens',
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
        'some '] }
QuestsHQOfficerFillin = 'HQ Officer'
QuestsHQWhereFillin = ''
QuestsHQBuildingNameFillin = 'Toon HQ'
QuestsHQLocationNameFillin = 'in any neighborhood'
QuestsTailorFillin = 'Tailor'
QuestsTailorWhereFillin = ''
QuestsTailorBuildingNameFillin = 'Clothing Store'
QuestsTailorLocationNameFillin = 'in any neighborhood'
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
        QUEST: 'Ok, now I think you are ready for something more challenging.\x7Defeat 3 Bossbots.',
        INCOMPLETE_PROGRESS: 'The ' + Cogs + ' are out in the streets, through the tunnels.',
        INCOMPLETE_WRONG_NPC: 'Good job defeating those Bossbots. Now go to the Toon Headquarters for your reward!',
        COMPLETE: QuestsDefaultComplete,
        LEAVING: QuestsDefaultLeaving },
    161: {
        GREETING: '',
        QUEST: 'Ok, now I think you are ready for something more challenging.\x7Defeat 3 Lawbots.',
        INCOMPLETE_PROGRESS: 'The ' + Cogs + ' are out in the streets, through the tunnels.',
        INCOMPLETE_WRONG_NPC: 'Good job defeating those Lawbots. Now go to the Toon Headquarters for your reward!',
        COMPLETE: QuestsDefaultComplete,
        LEAVING: QuestsDefaultLeaving },
    162: {
        GREETING: '',
        QUEST: 'Ok, now I think you are ready for something more challenging.\x7Defeat 3 Cashbots.',
        INCOMPLETE_PROGRESS: 'The ' + Cogs + ' are out in the streets, through the tunnels.',
        INCOMPLETE_WRONG_NPC: 'Good job defeating those Cashbots. Now go to the Toon Headquarters for your reward!',
        COMPLETE: QuestsDefaultComplete,
        LEAVING: QuestsDefaultLeaving },
    163: {
        GREETING: '',
        QUEST: 'Ok, now I think you are ready for something more challenging.\x7Defeat 3 Sellbots.',
        INCOMPLETE_PROGRESS: 'The ' + Cogs + ' are out in the streets, through the tunnels.',
        INCOMPLETE_WRONG_NPC: 'Good job defeating those Sellbots. Now go to the Toon Headquarters for your reward!',
        COMPLETE: QuestsDefaultComplete,
        LEAVING: QuestsDefaultLeaving },
    164: {
        QUEST: 'You look like you could use some new gags.\x7Go see Flippy, maybe he can help you out._where_' },
    165: {
        QUEST: 'Hi there.\x7Looks like you need practice training your gags.\x7Every time you hit a Cog with one of your gags, your experience increases.\x7When you get enough experience, you will be able to use an even better gag.\x7Go practice your gags by defeating 4 Cogs.' },
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
        QUEST: 'Hi!  What brings you here?\x7Everbody uses their portable hole to travel around Toontown.\x7Why, you can teleport to your friends using the Friends List, or to any neighborhood using the map in the Shticker Book.\x7Of course, you have to earn that!\x7Say, I can turn on your teleport access to Toontown Central if you help out a friend of mine.\x7Seems the Cogs are causing trouble over on Loopy Lane.  Go visit _toNpcName_._where_' },
    1042: {
        QUEST: 'Hi!  What brings you here?\x7Everbody uses their portable hole to travel around Toontown.\x7Why, you can teleport to your friends using the Friends List, or to any neighborhood using the map in the Shticker Book.\x7Of course, you have to earn that!\x7Say, I can turn on your teleport access to Toontown Central if you help out a friend of mine.\x7Seems the Cogs are causing trouble over on Loopy Lane.  Go visit _toNpcName_._where_' },
    1043: {
        QUEST: 'Hi!  What brings you here?\x7Everbody uses their portable hole to travel around Toontown.\x7Why, you can teleport to your friends using the Friends List, or to any neighborhood using the map in the Shticker Book.\x7Of course, you have to earn that!\x7Say, I can turn on your teleport access to Toontown Central if you help out a friend of mine.\x7Seems the Cogs are causing trouble over on Loopy Lane.  Go visit _toNpcName_._where_' },
    1044: {
        QUEST: 'Oh, thanks for stopping by.  I really need some help.\x7As you can see, I have no customers.\x7My secret recipe book is lost and  nobody comes to my restaurant anymore.\x7I last saw it just before those Cogs took over my building.\x7Can you help me by recovering four of my famous recipes?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Any luck finding my recipes?' },
    1045: {
        QUEST: 'Thank you so much!\x7Before long I will have the entire collection and can reopen my restaurant.\x7Oh, I have a note here for you - something about teleport access?\x7It says thanks for helping my friend and to deliver this to Toon Headquarters.\x7Well, thanks indeed - bye!',
        LEAVING: '',
        COMPLETE: 'Ah, yes, says here you have been a great help to some of the fine folks out on Loopy Lane.\x7Says you need teleport access to Toontown Central.\x7Well, consider it done.\x7Now you can teleport back to the playground from almost anywhere in Toontown.\x7Just open your map and click on Toontown Central.' },
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
        QUEST: "Yowza!  I can't find the tires to this here clown car anywhere!\x7Do ya think you could help me out?\x7I think Loopy Bob may have tossed them in the pond in the Toontown Central playground.\x7If you stand on one of the docks there you can try and fish out the tires for me.",
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
        QUEST: "Great - thanks for the ink!\x7You know what, maybe if you cleared away some of those Pencil Pushers...\x7I wouldn't run out of ink again so quickly.\x7Defeat 6 Pencil Pushers in Toontown Central for your reward.",
        LEAVING: '',
        COMPLETE: 'Thanks!  Let me reward you for your help.',
        INCOMPLETE_PROGRESS: 'I just saw some more Pencil Pushers.' },
    1062: {
        QUEST: "Great - thanks for the ink!\x7You know what, maybe if you cleared away some of those Blood Suckers...\x7I wouldn't run out of ink again so quickly.\x7Defeat 6 Blood Sucker in Toontown Central for your reward.",
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
        QUEST: "I wasn't expecting a package.  Maybe it's for Dr. I.M. Euphoric?\x7My assistant was going over there today anyway, so I'll have him check for you.\x7In the meantime, would you mind getting rid of some of the Cogs on my street?\x7Defeat 10 Cogs in Toontown Central.",
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
        QUEST: 'Those sneaky cogs are at it again.\x7_toNpcName_ has reported another missing item. Stop by and see if you can straighten it out._where_' },
    2202: {
        QUEST: "Hi, _avName_. Thank goodness you're here. A mean looking Penny Pincher was just in here and he made off with an inner tube.\x7I fear they may use it for their vile purposes.\x7Please see if you can find him and bring it back.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Any luck finding my inner tube?',
        COMPLETE: 'You found my inner tube! You ARE good. Here, take your reward...' },
    2203: {
        QUEST: 'The cogs are wreaking havoc over at the bank.\x7Go see Captain Carl and see what you can do._where_' },
    2204: {
        QUEST: "Welcome aboard, matey.\x7Argh! Those rapscallion cogs smashed my monocle and I can't sort me change without it.\x7Be a good landlubber and take this prescription to Dr. Queequeg and fetch me a new one._where_",
        GREETING: '',
        LEAVING: '' },
    2205: {
        QUEST: "What's this?\x7Oh, I'd love to fill this prescription but the cogs have been pilfering my supplies.\x7If you can get me the eyeglass frames off a flunky I can probably help you out.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Sorry. No flunky frames, no monocle.' },
    2206: {
        QUEST: 'Excellent!\x7Just a second...\x7Your prescription is filled. Please take this monocle straight to Captain Carl._where_',
        GREETING: '',
        LEAVING: '',
        COMPLETE: "Avast Ye!\x7You're gonna earn your sea legs after all.\x7Here ye be." },
    2207: {
        QUEST: "Barnacle Barbara has a cog in her shop!\x7You'd better get over there pronto._where_" },
    2208: {
        QUEST: "Gosh! You just missed him, sweetie.\x7There was a Back Stabber in here. He took my big white wig.\x7He said it was for his boss and something about 'legal precedent.'\x7If you can get it back I'd be forever grateful.",
        LEAVING: '',
        GREETING: '',
        INCOMPLETE_PROGRESS: "Still haven't found him?\x7He's tall and has a pointy head",
        COMPLETE: "You found it!?!?\x7Aren't you a darling!\x7You've more than earned this..." },
    2209: {
        QUEST: 'Melville is preparing for an important voyage.\x7Pop in and see what you can do to help sort him out._where_' },
    2210: {
        QUEST: "I can use your help.\x7I've been asked by ToonHQ to take a voyage and see if I can find where the cogs are coming from.\x7I'll need a few things for my ship but I don't have many jellybeans.\x7Stop by and pick up some ballast from Alice. You'll have to do a favor for her to get it._where_",
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
        QUEST: "Yes, I have the sea chart Melville wants.\x7And if you're willing to work for it I'll let you have it.\x7I'm trying to build an astrolabe to navigate by the stars.\x7I could use three cog gears to build it.\x7Come back when you've found them.",
        INCOMPLETE_PROGRESS: "How's it coming with those cog gears?",
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
        QUEST: "Are you the new recruit?\x7Good, good. Maybe you can help me.\x7I'm building a giant prefab crab to confuse the cogs.\x7I could use a clovis though. Go see Claggart and bring one back, please._where_" },
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
        QUEST: "I'd be happy to help the cause, _avName_.\x7But I'm afraid the streets are no longer safe.\x7Why don't you go take out some Cashbot cogs and we'll talk.",
        INCOMPLETE_PROGRESS: 'I still think you need to make the streets safer.' },
    2911: {
        QUEST: "I'd be happy to help the cause, _avName_.\x7But I'm afraid the streets are no longer safe.\x7Why don't you go take out some Cashbot cogs and we'll talk.",
        INCOMPLETE_PROGRESS: 'I still think you need to make the streets safer.' },
    2916: {
        QUEST: 'Yes, I have a weight that Ahab can have.\x7I think it would be safer if you defeated a couple sellbots first though.',
        INCOMPLETE_PROGRESS: 'Not yet. Defeat some more sellbots.' },
    2921: {
        QUEST: "Hmmm, I supposed I could give up a weight.\x7I'd feel a lot better about it if there weren't so many bossbot cogs creeping around.\x7Defeat six and then come see me.",
        INCOMPLETE_PROGRESS: "I don't think its safe yet..." },
    2925: {
        QUEST: "All done?\x7Well, I guess it's safe enough now.\x7Here's the counter weight for Ahab._where_" },
    2926: {
        QUEST: "Well, that's everything.\x7Let's see if it works.\x7Hmmm, one small problem.\x7I'm not getting any power because that cog building is blocking my solar panel.\x7Could you retake it for me?",
        INCOMPLETE_PROGRESS: 'Still no power. How about that building?',
        COMPLETE: 'Super! You are one heck of a cog crusher! Here, take this as your reward...' },
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
        QUEST: "We've been getting complaints from the residents lately about all of the Cold Callers.\x7See if you can defeat 10 Cold Callers to help out your fellow Toons in Daisy Gardens." },
    3209: {
        QUEST: 'Thanks for taking care of those Cold Callers!\x7But now the Telemarketers have gotten out of hand.\x7Defeat 10 Telemarketers in Daisy Gardens and come back here for your reward.' },
    3247: {
        QUEST: "We've been getting complaints from the residents lately about all of the Blood Suckers.\x7See if you can defeat 20 Blood Suckers to help out your fellow Toons in Daisy Gardens." },
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
        INCOMPLETE_PROGRESS: "I'm still look for my inkwell!" },
    3215: {
        QUEST: "Great! Now I have my pen and my inkwell back!\x7But wouldn't you know it?\x7My notepad is gone! They must have stolen it too!\x7Defeat Cogs to find my stolen notepad, and then bring it back for your reward.",
        INCOMPLETE_PROGRESS: 'Any word on that notepad yet?' },
    3216: {
        QUEST: "That's my notepad! Hooray! Your reward is...\x7Hey! Where did it go?\x7I had your reward right here in my office lockbox. But the whole lockbox is gone!\x7Can you believe it? Those cogs stole your reward!\x7Defeat Cogs to recover my lockbox.\x7When you bring it back to me I'll give you your reward.",
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
        QUEST: 'Hi, _avName_! There you are!\x7I heard you were quite an expert in squirt attacks.\x7I need someone to set a good example for all the Toons in Daisy Gardens.\x7Use your squirt attacks to defeat a bunch of Cogs.\x7Encourage your friends to use squirt too.\x7When you have defeated 20 Cogs, come back here for a reward!' },
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
        QUEST: "Oh, this is the salad I ordered!\x7Thank you for bringing it to me.\x7All those Cogs must have frightened away _toNpcName_'s regular delivery person again.\x7Why don't you do us a favor and defeat some of the Cogs out there?\x7Defeat 10 Cogs in Daisy Gardens and then report back to _toNpcName_.",
        INCOMPLETE_PROGRESS: "You're working on defeating Cogs for me?\x7That's wonderful! Keep up the good work!",
        COMPLETE: 'Oh, thank you so much for defeating those Cogs!\x7Now maybe I can keep my regular delivery schedule.\x7Your reward is...',
        INCOMPLETE_WRONG_NPC: "Go tell _toNpcName_ about the Cogs you've defeated._where_" },
    3236: {
        QUEST: 'There are far too many Lawbots out there.\x7You can do your part to help!\x7Defeat 3 Lawbot buildings.' },
    3237: {
        QUEST: 'Great job on those Lawbot buildings!\x7But now there are too many Sellbots!\x7Defeat 3 Sellbot buildings, then come back for your reward.' },
    3238: {
        QUEST: 'Oh no! A "Mingler" Cog has stolen the Key to Daisy Gardens!\x7See if you can recover it.\x7Remember, The Mingler can be found only inside Sellbot buildings.' },
    3239: {
        QUEST: 'You found a key all right, but it isn\'t the right one!\x7We need the Key to Daisy Gardens.\x7Keep looking! A "Mingler" Cog still has it!' },
    3242: {
        QUEST: 'Oh no! A Legal Eagle Cog has stolen the Key to Daisy Gardens!\x7See if you can recover it.\x7Remember, Legal Eagles can be found only inside Lawbot buildings.' },
    3243: {
        QUEST: "You found a key all right, but it isn't the right one!\x7We need the Key to Daisy Gardens.\x7Keep looking! A Legal Eagle Cog still has it!" },
    3240: {
        QUEST: "I've just heard from _toNpcName_ that a Legal Eagle stole a bag of his bird seed.\x7Defeat Legal Eagles until you recover Bud's bird seed, and take it to him.\x7Legal Eagles are only found inside Lawbot buildings._where_",
        COMPLETE: 'Oh, thank you so much for finding my bird seed!\x7Your reward is...',
        INCOMPLETE_WRONG_NPC: 'Good job getting that bird seed back!\x7Now take it to _toNpcName_._where_' },
    3241: {
        QUEST: 'Some of the Cog buildings out there are getting too tall for our comfort.\x7See if you can bring down some of the tallest buildings.\x7Rescue 5 3-story buildings or taller and come back for your reward.' },
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
        QUEST: 'Oh! The inventory!\x7I forgot all about it.\x7I bet I can have it done by the time you defeat 10 cogs.\x7Stop in after that and I promise it will be ready.',
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
        QUEST: "Whew! I'm glad ToonHQ finally sent somebody.\x7I haven't had a customer in days.\x7It's these darned Number Crunchers every where.\x7I think they are teaching our residents bad oral hygiene.\x7Defeat ten of them and let's see if business picks up.",
        INCOMPLETE_PROGRESS: 'Still no customers. But keep it up!' },
    4213: {
        QUEST: "You know maybe it wasn't the Number Crunchers after all.\x7Maybe it's just the Cashbots in general.\x7Take out twenty of them and hopefully someone will come in for at least a checkup.",
        INCOMPLETE_PROGRESS: "I know twenty is a lot. But I'm sure it's going to pay off in spades." },
    4214: {
        GREETING: '',
        LEAVING: '',
        QUEST: "I just don't understand it!\x7Still not a SINGLE customer.\x7Maybe we need to go to the source.\x7Try reclaiming a Cashbot cog building.\x7That Should do the trick...",
        INCOMPLETE_PROGRESS: 'Oh, please! Just one little building...',
        COMPLETE: "Still not a soul in here.\x7But you know, come to think of it.\x7I didn't have any customers before the cogs invaded either!\x7I really appreciate all your help though.\x7This should help you get around." },
    4215: {
        QUEST: "Anna desperately needs someone to help her.\x7Why don't you drop in and see what you can do._where_" },
    4216: {
        QUEST: "Thanks for coming so quickly!\x7Seems like the cogs have made off with several of my customers' cruise tickets.\x7Yuki said she saw a Glad Hander leaving here with his glad hands full of them.\x7See if you can get Lumber Jack's ticket to Alaska back.",
        INCOMPLETE_PROGRESS: 'Those Glad Handers could be anywhere now...' },
    4217: {
        QUEST: "Oh, great. You found it!\x7Now be a trooper and run in by Jack's for me, would you?_where_" },
    4218: {
        QUEST: "Great Googely Moogely!\x7Alaska here I come!\x7I can't take these infernal cogs anymore.\x7Say, I think Anna needs you again._where_" },
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
        COMPLETE: 'Awesome, dude!\x7My concert is gonna rock!\x7Speaking of rock, you can rock some cogs with this...' },
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
        QUEST: 'Those sneaky cogs are at it again.\x7_toNpcName_ has reported another missing item. Stop by and see if you can straighten it out._where_' },
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
        QUEST: "The Brrrgh has been overrun with some of the toughest Cogs we've seen yet.\x7You will probably want to carry more gags around here.\x7I hear _toNpcName_ may have a large bag you can use to carry more gags._where_" },
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
        QUEST: "You say you're done?  Defeated all the Cogs?\x7You must have misunderstood, our deal was for Cashbot Cogs.\x7I'm sure I told you to defeat some Cashbot Cogs for me." } }
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
ChatGarblerFowl = [
    'quack',
    'quackity',
    'quacky']
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
AvatarDetailPanelOK = 'OK'
AvatarDetailPanelCancel = 'Cancel'
AvatarDetailPanelClose = 'Close'
AvatarDetailPanelLookup = 'Looking up details for %s.'
AvatarDetailPanelFailedLookup = 'Unable to get details for %s.'
AvatarDetailPanelOnline = 'District: %(district)s\nLocation: %(location)s'
AvatarDetailPanelOffline = 'District: offline\nLocation: offline'
AvatarPanelFriends = 'Friends'
AvatarPanelWhisper = 'Whisper'
AvatarPanelSecrets = 'Secrets'
AvatarPanelGoTo = 'Go To'
AvatarPanelIgnore = 'Ignore'
AvatarPanelCogLevel = 'Level: %s'
AvatarPanelCogDetailClose = 'Close'
WhisperNoLongerFriend = '%s left your friends list.'
WhisperNowSpecialFriend = '%s is now your secret friend!'
WhisperComingToVisit = '%s is coming to visit you.'
WhisperFailedVisit = '%s tried to visit you.'
WhisperTargetLeftVisit = '%s has gone somewhere else. Try again!'
WhisperGiveupVisit = "%s couldn't find you because you're moving around!"
WhisperIgnored = '%s is ignoring you!'
TeleportGreeting = 'Hi, %s.'
DialogSpecial = 'ooo'
DialogExclamation = '!'
DialogQuestion = '?'
DialogLength1 = 6
DialogLength2 = 12
DialogLength3 = 20
FriendsListLabel = 'Friends'
WhisperFriendComingOnline = '%s is coming online!'
WhisperFriendLoggedOut = '%s has logged out.'
TeleportPanelOK = 'OK'
TeleportPanelCancel = 'Cancel'
TeleportPanelYes = 'Yes'
TeleportPanelNo = 'No'
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
SuitFaceoffTaunts = {
    'b': [
        'Do you have a donation for me?',
        "I'm going to make you a sore loser.",
        "I'm going to leave you high and dry.",
        'I\'m "A Positive" I\'m going to win.',
        '"O" don\'t be so "Negative".',
        "I'm surprised you found me, I'm very mobile.",
        "I'm going to need to do a quick count on you.",
        "You're soon going to need a cookie and some juice.",
        "When I'm through you'll need to lie down.",
        'This will only hurt for a second.',
        "I'm going to make you dizzy.",
        "Good timing, I'm a pint low."],
    'm': [
        "You don't know who you're mingling with.",
        'Ever mingle with the likes of me?',
        'Good, it takes two to mingle.',
        "Let's mingle.",
        'This looks like a good place to mingle.',
        "Well,isn't this cozy?",
        "You're mingling with defeat.",
        "I'm going to mingle in your business.",
        "Are you sure you're ready to mingle?"],
    'ms': [
        'Get ready for a shake down.',
        'You had better move out of the way.',
        'Move it or lose it.',
        "I believe it's my move.",
        'This should shake you up.',
        'Prepare to be moved.',
        "I'm ready to make my move.",
        "Watch out toon, you're on shaky ground.",
        'This should be a moving moment.',
        'I feel moved to defeat you.',
        'Are you shaking yet?'],
    'hh': [
        "I'm way ahead of you.",
        "You're headed for big trouble.",
        "You'll wish this was all in your head.",
        "Oh good, I've been hunting for you.",
        "I'll have your head for this.",
        "Head's up!",
        "Looks like you've got a head for trouble.",
        'Headed my way?',
        'A perfect trophy for my collection.',
        'You are going to have such a headache.',
        "Don't lose your head over me."],
    'tbc': [
        "Watch out, I'm gouda getcha.",
        'You can call me Jack.',
        'Are you sure?  I can be such a Muenster at times.',
        'Well finally, I was afraid you were stringing me along.',
        "I'm going to cream you.",
        "Don't you think I've aged well?",
        "I'm going to make mozzarella outta ya.",
        "I've been told I'm very strong.",
        'Careful, I know your expiration date.',
        "Watch out, I'm a whiz at this game.",
        'Beating you will be a brieeze.'],
    'cr': [
        'RAID!',
        "You don't fit in my corporation.",
        'Prepare to be raided.',
        'Looks like your primed for a take-over.',
        'That is not proper corporate attire.',
        "You're looking rather vulnerable.",
        'Time to sign over your assets.',
        "I'm on a toon removal crusade.",
        'You are defenseless against my ideas.',
        "Relax, you'll find this is for the best."],
    'mh': [
        'Are you ready for my take?',
        'Lights, camera, action!',
        "Let's start rolling.",
        'Today the role of defeated toon, will be played by - YOU!',
        'This scene will go on the cutting room floor.',
        'I already know my motivation for this scene.',
        'Are you ready for your final scene?',
        "I'm ready to roll your end credits.",
        'I told you not to call me.',
        "Let's get on with the show.",
        "There's no business like it!.",
        "I hope you don't forget your lines."],
    'nc': [
        'Looks like your number is up.',
        'I hope you prefer extra crunchy.',
        "Now you're really in a crunch.",
        'Is it time for crunch already?',
        "Let's do crunch.",
        'Where would you like to have your crunch today?',
        "You've given me something to crunch on.",
        'This will not be smooth.',
        'Go ahead, try and take a number.',
        'I could do with a nice crunch about now.'],
    'ls': [
        "It's time to collect on your loan.",
        "You've been on borrowed time.",
        'Your loan is now due.',
        'Time to pay up.',
        'Well you asked for an advance and you got it.',
        "You're going to pay for this.",
        "It's pay back time.",
        'Can you lend me an ear?',
        "Good thing you're here,  I'm in a frenzy.",
        'Shall we have a quick bite?',
        'Let me take a bite at it.'],
    'mb': [
        'Time to bring in the big bags.',
        'I can bag this.',
        'Paper or plastic?',
        'Do you have your baggage claim?',
        "Remember, money won't make you happy.",
        'Careful, I have some serious baggage.',
        "You're about to have money trouble.",
        'Money will make your world go around.',
        "I'm too rich for your blood.",
        'You can never have too much money!'],
    'rb': [
        "You've been robbed.",
        "I'll rob you of this victory.",
        "I'm a royal pain!",
        'Hope you can grin and baron.',
        "You'll need to report this robbery.",
        "Stick 'em up.",
        "I'm a noble adversary.",
        "I'm going to take everything you have.",
        'You could call this neighborhood robbery.',
        'You should know not to talk to strangers.'],
    'bs': [
        'Never turn your back on me.',
        "You won't be coming back.",
        'Take that back or else!',
        "I'm good at cutting costs.",
        'I have lots of back up.',
        "There's no backing down now.",
        "I'm the best and I can back that up.",
        'Whoa, back up there toon.',
        'Let me get your back.',
        "You're going to have a stabbing headache soon.",
        'I have perfect puncture.'],
    'bw': [
        "Don't brush me aside.",
        'You make my hair curl.',
        'I can make this permanent if you want.',
        "It looks like you've going to have some split ends.",
        "You can't handle the truth.",
        "I think it's your turn to be dyed.",
        "I'm so glad you're on time for your cut.",
        "You're in big trouble.",
        "I'm going to wig out on you.",
        "I'm a big deal little toon."],
    'le': [
        "Careful, my legal isn't very tender.",
        'I soar, then I score.',
        "I'm bringing down the law on you.",
        'You should know, I have some killer instincts.',
        "I'm going to give you legal nightmares.",
        "You won't win this battle.",
        'This is so much fun it should be illegal.',
        "Legally, you're too small to fight me.",
        'There is no limit to my talons.',
        'I call this a citizen arrest.'],
    'sd': [
        "You'll never know when I'll stop.",
        'Let me take you for a spin.',
        'The doctor will see you now.',
        "I'm going to put you into a spin.",
        'You look like you need a doctor.',
        'The doctor is in, the Toon is out.',
        "You won't like my spin on this.",
        'You are going to spin out of control.',
        'Care to take a few turns with me?',
        'I have my own special spin on the subject.'],
    'f': [
        "I'm gonna tell the boss about you!",
        "I may be just a flunky - But I'm real spunky.",
        "I'm using you to step up the corporate ladder.",
        "You're not going to like the way I work.",
        'The boss is counting on me to stop you.',
        "You're going to look good on my resume.",
        "You'll have to go through me first.",
        "Let's see how you rate my job performance.",
        'I excel at Toon disposal.',
        "You're never going to meet my boss.",
        "I'm sending you back to the Playground."],
    'p': [
        "I'm gonna rub you out!",
        "Hey, you can't push me around.",
        "I'm No.2!",
        "I'm going to scratch you out.",
        "I'll have to make my point more clear.",
        'Let me get right to the point.',
        "Let's hurry, I bore easily.",
        'I hate it when things get dull.',
        'So you want to push your luck?',
        'Did you pencil me in?',
        'Careful, I may leave a mark.'],
    'ym': [
        "I'm positive you're not going to like this.",
        "I don't know the meaning of no.",
        'Want to meet?  I say yes, anytime.',
        'You need some positive enforcement.',
        "I'm going to make a positive impression.",
        "I haven't been wrong yet.",
        "Yes, I'm ready for you.",
        'Are you positive you want to do this?',
        "I'll be sure to end this on a positive note.",
        "I'm confirming our meeting time.",
        "I won't take no for an answer."],
    'mm': [
        "I'm going to get into your business!",
        'Sometimes big hurts come in small packages.',
        'No job is too small for me.',
        "I want the job done right, so I'll do it myself.",
        'You need someone to manage your assets.',
        'Oh good, a project.',
        "Well, you've managed to find me.",
        'I think you need some managing.',
        "I'll take care of you in no time.",
        "I'm watching every move you make.",
        'Are you sure you want to do this?',
        "We're going to do this my way.",
        "I'm going to be breathing down your neck.",
        'I can be very intimidating.'],
    'ds': [
        "You're going down!",
        'Your options are shrinking.',
        'Expect diminishing returns.',
        "You've just become expendable.",
        "Don't ask me to lay off.",
        'I might have to make a few cutbacks.',
        'Things are looking down for you.',
        'Why do you look so down?'],
    'cc': [
        'Surprised to hear from me?',
        'You rang?',
        'Are you ready to accept my charges?',
        'This caller always collects.',
        "I'm one smooth operator.",
        "Hold the phone -- I'm here.",
        'Have you been waiting for my call?',
        "I was hoping you'd answer my call.",
        "I'm going to cause a ringing sensation.",
        'I always make my calls direct.',
        'Boy, did you get your wires crossed.',
        'This call is going to cost you.',
        "You've got big trouble on the line."],
    'tm': [
        'I plan on making this inconvenient for you.',
        'Can I interest you in an insurance plan?',
        'You should have missed my call.',
        "You won't be able to get rid of me now.",
        'This a bad time?  Good.',
        'I was planning on running into you.',
        'I will be reversing the charges for this call.',
        'I have some costly items for you today.',
        'Too bad for you - I make house calls.',
        "I'm prepared to close this deal quickly.",
        "I'm going to use up a lot of your resources."],
    'nd': [
        'In my opinion, your name is mud.',
        "I hope you don't mind if I drop your name.",
        "Haven't we met before?",
        "Let's hurry, I'm having lunch with 'Mr. Hollywood.'",
        "Have I mentioned I know 'The Mingler?'",
        "You'll never forget me.",
        'I know all the right people to bring you down.',
        "I think I'll just drop in.",
        "I'm in the mood to drop some Toons.",
        "You name it, I've dropped it."],
    'gh': [
        'Put it there, Toon.',
        "Let's shake on it.",
        "I'm going to enjoy this.",
        "You'll notice I have a very firm grip.",
        "Let's seal the deal.",
        "Let's get right to the business at hand.",
        "Off handedly I'd say, you're in trouble.",
        "You'll find I'm a handful.",
        'I can be quite handy.',
        "I'm a very hands-on kinda guy.",
        'Would you like some hand-me-downs?',
        'Let me show you some of my handiwork.',
        'I think the handwriting is on the wall.'],
    'sc': [
        'I will make short work of you.',
        "You're about to have money trouble.",
        "You're about to be overcharged.",
        'This will be a short-term assignment.',
        "I'll be done with you in short order.",
        "You'll soon experience a shortfall.",
        "Let's make this a short stop.",
        "I think you've come up short.",
        'I have a short temper for Toons.',
        "I'll be with you shortly.",
        "You're about to be shorted."],
    'pp': [
        'This is going to sting a little.',
        "I'm going to give you a pinch for luck.",
        "You don't want to press your luck with me.",
        "I'm going to put a crimp in your smile.",
        'Perfect, I have an opening for you.',
        'Let me add my two cents.',
        "I've been asked to pinch-hit.",
        "I'll prove you're not dreaming.",
        'Heads you lose, tails I win.',
        'A Penny for your gags.'],
    'tw': [
        'Things are about to get very tight.',
        "That's Mr. Tightwad to you.",
        "I'm going to cut off your funding.",
        'Is this the best deal you can offer?',
        "Let's get going - time is money.",
        "You'll find I'm very tightfisted.",
        "You're in a tight spot.",
        'Prepare to walk a tight rope.',
        'I hope you can afford this.',
        "I'm going to make this a tight squeeze.",
        "I'm going to make a big dent in your budget."],
    'bc': [
        'I enjoy subtracting Toons.',
        'You can count on me to make you pay.',
        'Bean there, done that.',
        'I can hurt you where it counts.',
        'I make every bean count.',
        'Your expense report is overdue.',
        'Time for an audit.',
        "Let's step into my office.",
        'Where have you bean?',
        "I've bean waiting for you.",
        "I'm going to bean you."],
    'bf': [
        "Looks like you've hit rock bottom.",
        "I'm ready to feast.",
        "I'm a sucker for Toons.",
        'Oh goody, lunch time.',
        'Perfect timing, I need a quick bite.',
        "I'd like some feedback on my performance.",
        "Let's talk about the bottom line.",
        "You'll find my talents are bottomless.",
        'Good, I need a little pick-me-up.',
        "I'd love to have you for lunch."],
    'tf': [
        "It's time to face-off!",
        'You had better face up to defeat.',
        'Prepare to face your worst nightmare!',
        "Face it, I'm better than you.",
        'Two heads are better than one.',
        'It takes two to tango, you wanna tango?',
        "You're in for two times the trouble.",
        'Which face would you like to defeat you?',
        "I'm 'two' much for you.",
        "You don't know who you're facing.",
        'Are you ready to face your doom?'],
    'dt': [
        "I'm gonna give you double the trouble.",
        'See if you can stop my double cross.',
        'I serve a mean double-DECKER.',
        "It's time to do some double-dealing.",
        'I plan to do some double DIPPING.',
        "You're not going to like my double play.",
        'You may want to double think this.',
        'Get ready for a double TAKE.',
        'You may want to double up against me.',
        'Doubles anyone??'],
    'ac': [
        "I'm going to chase you out of town!",
        'Do you hear a siren?',
        "I'm going to enjoy this.",
        'I love the thrill of the chase.',
        'Let me give you the run down.',
        'Do you have insurance?',
        'I hope you brought a stretcher with you.',
        'I doubt you can keep up with me.',
        "It's all uphill from here.",
        "You're going to need some urgent care soon.",
        'This is no laughing matter.',
        "I'm going to give you the business."] }
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
    'DoubleTalk': 'Double Talk!!',
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
        "Always remember, where's there's smoke, there's fire.",
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
DoorKnockKnock = 'Knock, knock.'
DoorWhosThere = "Who's there?"
DoorWhoAppendix = ' who?'
FADoorCodes_UNLOCKED = None
FADoorCodes_TALK_TO_TOM = 'You need gags! Go talk to Tutorial Tom!'
FADoorCodes_DEFEAT_FLUNKY_HQ = 'Come back here when you have defeated the Flunky!'
FADoorCodes_TALK_TO_HQ = 'Go get your reward from HQ Harry!'
FADoorCodes_WRONG_DOOR_HQ = 'Wrong door! Take the other door to the playground!'
FADoorCodes_GO_TO_PLAYGROUND = 'Wrong way! You need to go to the playground!'
FADoorCodes_DEFEAT_FLUNKY_TOM = 'Walk up to that Flunky to battle him!'
FADoorCodes_TALK_TO_HQ_TOM = 'Go get your reward from Toon Headquarters!'
FADoorCodes_SUIT_APPROACHING = None
FADoorCodes_BUILDING_TAKEOVER = "Watch out! There's a COG in there!"
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
        'Justin in time for dinner.'],
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
ChatInputNormalSayIt = 'Say It'
ChatInputNormalCancel = 'Cancel'
ChatInputNormalWhisper = 'Whisper'
ChatInputWhisperLabel = 'To %s'
SCEmoteNoAccessMsg = 'You do not have access\nto this emotion yet.'
SCEmoteNoAccessOK = 'OK'
ChatManagerChat = 'Chat'
ChatManagerWhisperTo = 'Whisper to:'
ChatManagerWhisperToName = 'Whisper To:\n%s'
ChatManagerCancel = 'Cancel'
ChatManagerWhisperOffline = '%s is offline.'
OpenChatWarning = 'You don\'t have any "Secret Friends" yet!  You cannot chat with other Toons unless they are your Secret Friends.\n\nTo become Secret Friends with somebody, click on them, and select "Secrets" from the detail panel.  Of course, you can always talk to anybody with SpeedChat.'
OpenChatWarningOK = 'OK'
UnpaidChatWarning = 'Once you have subscribed, you can use this button to chat with your friends using the keyboard.  Until then, you should chat with other Toons using SpeedChat.'
UnpaidChatWarningPay = 'Subscribe Now!'
UnpaidChatWarningContinue = 'Continue Free Trial'
NoSecretChatAtAllTitle = 'Secret Friends Chat'
NoSecretChatAtAll = 'To chat with a friend, the Secret Friends feature must first be enabled.  Secret Friends allows one member to chat with another member only by means of a secret code that must be communicated outside of the game.\n\nTo activate this feature or to learn more about it, exit Toontown and then click on "Account Options" on the Toontown web page.'
NoSecretChatAtAllOK = 'OK'
NoSecretChatWarningTitle = 'Parental Controls'
NoSecretChatWarning = 'To chat with a friend, the Secret Friends feature must first be enabled.  Kids, have your parent log in with their Parent Password to learn about the Secret Friends feature and access parental controls.'
NoSecretChatWarningOK = 'OK'
NoSecretChatWarningCancel = 'Cancel'
NoSecretChatWarningWrongPassword = "That's not the correct password.  Please enter the Parent Password created when purchasing this account.  This is not the same password used to play the game."
ActivateChat = 'Secret Friends allows one member to chat with another member only by means of a secret code that must be communicated outside of the game.  For a complete description, click here:\n\n\n\nSecret Friends is not moderated or supervised.  If parents allow their children to use their account with the Secret Friends feature enabled, we encourage parents to supervise their children while they play.  Once enabled, the Secret Friends feature is available until it is disabled.\n\nBy enabling the Secret Friends feature, you acknowledge that there are some risks inherent in the Secret Friends feature and that you have been informed of, and agree to accept, any such risks.'
ActivateChatYes = 'Enable'
ActivateChatNo = 'Cancel'
ActivateChatMoreInfo = 'More Info'
ActivateChatPrivacyPolicy = 'Privacy Policy'
LeaveToPay = 'In order to purchase, the game will exit to Toontown.com.'
LeaveToPayYes = 'Purchase'
LeaveToPayNo = 'Cancel'
ChatMoreInfoOK = 'OK'
SecretChatActivated = 'The "Secret Friends" system has been enabled!\n\nIf you change your mind and decide to disable this feature later, click on "Account Options" on the Toontown web page.'
SecretChatActivatedOK = 'OK'
ProblemActivatingChat = 'Oops!  We were unable to activate the "Secret Friends" chat feature.\n\n%s\n\nPlease try again later.'
ProblemActivatingChatOK = 'OK'
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
    "Wow, there're a lot of " + Cogs + ' in the Brrrgh.',
    'I love to play tag. Do you?',
    'Trolley games are fun to play.',
    'I like to make people laugh.',
    "It's fun helping my friends.",
    "A-hem, are you lost?  Don't forget your map is in your shticker book.",
    'Try not to get tied up in the ' + Cogs + "' Red Tape.",
    'I hear ' + Daisy + ' has planted some new flowers in her garden.',
    'If you hold down the Page Up key, you can look up!',
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
    'Welcome to Toontown Central.',
    'Hi, my name is ' + Mickey + ". What's yours?"], [
    'Hey, have you seen ' + Donald + '?',
    "I'm going to go watch the fog roll in at " + Donald + "'s Dock.",
    'If you see my pal ' + Goofy + ', say hi to him for me.',
    'I hear ' + Daisy + ' has planted some new flowers in her garden.'], [
    "I'm going to MelodyLand to see " + Minnie + '!',
    "Gosh, I'm late for my date with " + Minnie + '!',
    "Looks like it's time for " + Pluto + "'s dinner.",
    "I think I'll go swimming at " + Donald + "'s Dock.",
    "It's time for a nap. I'm going to Dreamland."])
MinnieChatter = ([
    'Welcome to Melodyland.',
    'Hi, my name is ' + Minnie + ". What's yours?"], [
    'The hills are alive with the sound of music!',
    'Make sure you try riding the big turntable Merry-Go-Round!',
    'You have a cool outfit, %.',
    'Hey, have you seen ' + Mickey + '?',
    'If you see my friend ' + Goofy + ', say hi to him for me.',
    "Wow, there're a lot of " + Cogs + ' near ' + Donald + "'s Dreamland.",
    "I heard it's foggy at the " + Donald + "'s Dock.",
    'Be sure and try the maze in ' + Daisy + ' Gardens.',
    "I think I'll go catch some tunes.",
    'Hey %, look at that over there.',
    'I love the sound of music.',
    "I bet you didn't know Melodyland is also called TuneTown!  Hee Hee!",
    'I love to play the Matching Game. Do you?',
    'I like to make people giggle.',
    'Boy, trotting around in heels all day is hard on your feet!',
    'Nice shirt, %.',
    'Is that a jellybean on the ground?'], [
    "Gosh, I'm late for my date with " + Mickey + '!',
    "Looks like it's time for " + Pluto + "'s dinner.",
    "It's time for a nap. I'm going to Dreamland."])
GoofyChatter = ([
    'Welcome to ' + Daisy + ' Gardens.',
    'Hi, my name is ' + Goofy + ". What's yours?",
    "Gawrsh, it's nice to see you %!"], [
    'Boy it sure is easy to get lost in the garden maze!',
    'Be sure and try the maze here.',
    "I haven't seen " + Daisy + ' all day.',
    'I wonder where ' + Daisy + ' is.',
    'Hey, have you seen ' + Donald + '?',
    'If you see my friend ' + Mickey + ', say hi to him for me.',
    "D'oh! I forgot to fix " + Mickey + "'s breakfast!",
    'Gawrsh there sure are a lot of ' + Cogs + ' near ' + Donald + "'s Dock.",
    'It looks like ' + Daisy + ' has planted some new flowers in her garden.',
    'At the Brrgh branch of my Gag Shop, Hypno-Goggles are on sale for only 1 jellybean!',
    "Goofy's Gag Shops offer the best jokes, tricks, and funnybone-ticklers in all of Toontown!",
    "At Goofy's Gag Shops, every pie in the face is guaranteed to make a laugh or you get your jellybeans back!"], [
    "I'm going to Melody Land to see " + Minnie + '!',
    "Gosh, I'm late for my game with " + Donald + '!',
    "I think I'll go swimming at " + Donald + "'s Dock.",
    "It's time for a nap. I'm going to Dreamland."])
DonaldChatter = ([
    'Welcome to Dreamland.',
    'Hi, my name is ' + Donald + ". What's yours?"], [
    'Sometimes this place gives me the creeps.',
    'Be sure and try the maze in ' + Daisy + ' Gardens.',
    "Oh boy, I'm having a good day.",
    'Hey, have you seen ' + Mickey + '?',
    'If you see my buddy ' + Goofy + ', say hi to him for me.',
    "I think I'll go fishing this afternoon.",
    "Wow, there're a lot of " + Cogs + ' at ' + Donald + "'s Dock.",
    "Hey, didn't I take you on a boat ride at " + Donald + "'s Dock?",
    "I haven't seen " + Daisy + ' all day.',
    'I hear ' + Daisy + ' has planted some new flowers in her garden.',
    'Quack.'], [
    "I'm going to Melody Land to see " + Minnie + '!',
    "Gosh, I'm late for my date with " + Daisy + '!',
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

TCRConnecting = 'Connecting...'
TCRNoConnectTryAgain = 'Could not connect to %s:%s. Try again?'
TCRNoConnectProxyNoPort = 'Could not connect to %s:%s.\n\nYou are communicating to the internet via a proxy, but your proxy does not permit connections on port %s.\n\nYou must open up this port, or disable your proxy, in order to play Toontown.  If your proxy has been provided by your ISP, you must contact your ISP to request them to open up this port.'
TCRNoDistrictsTryAgain = 'No Toontown Districts are available. Try again?'
TCRLostConnection = 'Your internet connection to Toontown has been unexpectedly broken.'
TCRBootedReasons = {
    1: 'An unexpected problem has occurred.  Your connection has been lost, but you should be able to connect again and go right back into the game.',
    100: 'You have been disconnected because someone else just logged in using your account on another computer.',
    120: 'You have been disconnected because of a problem with your authorization to use keyboard chat.',
    122: 'There has been an unexpected problem logging you in to Toontown.  Please contact Toontown customer support.',
    151: 'You have been logged out by an administrator working on the Toontown servers.',
    153: 'The Toontown district you were playing on has been reset.  Everyone who was playing on that district has been disconnected.  However, you should be able to connect again and go right back into the game.',
    288: 'Sorry, you have used up all of your available minutes in Toontown this month.',
    349: 'Sorry, you have used up all of your available minutes in Toontown this month.' }
TCRBootedReasonUnknownCode = 'An unexpected problem has occurred (error code %s).  Your connection has been lost, but you should be able to connect again and go right back into the game.'
TCRTryConnectAgain = '\n\nTry to connect again?'
TCRTutorialAckQuestion = '%s is new to Toontown.\n\nWould you like ' + Mickey + ' to show you around?'
TCRTutorialAckOk = 'Yes'
TCRTutorialAckCancel = 'No'
TCRToontownUnavailable = 'Toontown appears to be temporarily unavailable, still trying...'
TCRToontownUnavailableCancel = 'Cancel'
TCRNameCongratulations = 'CONGRATULATIONS!!'
TCRNameAccepted = 'Your name has been\napproved by the Toon Council.\n\nFrom this day forth\nyou will be named\n"%s"'
TCRServerConstantsProxyNoPort = 'Unable to contact %s.\n\nYou are communicating to the internet via a proxy, but your proxy does not permit connections on port %s.\n\nYou must open up this port, or disable your proxy, in order to play Toontown.  If your proxy has been provided by your ISP, you must contact your ISP to request them to open up this port.'
TCRServerConstantsProxyNoCONNECT = 'Unable to contact %s.\n\nYou are communicating to the internet via a proxy, but your proxy does not support the CONNECT method.\n\nYou must enable this capability, or disable your proxy, in order to play Toontown.  If your proxy has been provided by your ISP, you must contact your ISP to request them to enable this capability.'
TCRServerConstantsTryAgain = 'Unable to contact %s.\n\nThe Toontown account server might be temporarily down, or there might be some problem with your internet connection.\n\nTry again?'
TCRServerDateTryAgain = 'Could not get server date from %s. Try again?'
AfkForceAcknowledgeMessage = 'Your toon got sleepy and went to bed.'
PeriodTimerWarning = 'Your time limit in Toontown this month is almost over!'
PeriodForceAcknowledgeMessage = 'You have used up all of your available minutes in Toontown this month.  Come back and play some more next month!'
TCREnteringToontown = 'Entering Toontown...'
FriendInviteeTooManyFriends = '%s would like to be your friend, but you already have too many friends on your list!'
FriendInviteeInvitation = '%s would like to be your friend.'
FriendInviteeOK = 'OK'
FriendInviteeNo = 'No'
FriendInviterOK = 'OK'
FriendInviterCancel = 'Cancel'
FriendInviterStopBeingFriends = 'Stop being friends'
FriendInviterYes = 'Yes'
FriendInviterNo = 'No'
FriendInviterClickToon = 'Click on the toon you would like to make friends with.'
FriendInviterTooMany = 'You have too many friends on your list to add another one now. You will have to remove some friends if you want to make friends with %s.'
FriendInviterNotYet = 'Would you like to make friends with %s?'
FriendInviterCheckAvailability = 'Seeing if %s is available.'
FriendInviterNotAvailable = '%s is busy right now; try again later.'
FriendInviterWentAway = '%s went away.'
FriendInviterAlready = '%s is already your friend.'
FriendInviterAskingCog = 'Asking %s to be your friend.'
FriendInviterEndFriendship = 'Are you sure you want to stop being friends with %s?'
FriendInviterFriendsNoMore = '%s is no longer your friend.'
FriendInviterSelf = "You are already 'friends' with yourself!"
FriendInviterIgnored = '%s is ignoring you.'
FriendInviterAsking = 'Asking %s to be your friend.'
FriendInviterFriendSaidYes = '%s said yes!'
FriendInviterFriendSaidNo = '%s said no, thank you.'
FriendInviterFriendSaidNoNewFriends = "%s isn't looking for new friends right now."
FriendInviterTooMany = '%s has too many friends already!'
FriendInviterMaybe = '%s was unable to answer.'
FriendInviterDown = 'Cannot make friends now.'
FriendSecretIntro = "If you are playing Disney's Toontown Online with someone you know in the real world, you can become Secret Friends.  You can chat using the keyboard with your Secret Friends.  Other toons won't understand what you're saying.\n\nYou do this by getting a secret.  Tell the secret to your friend, but not to anyone else.  When your friend types in your secret on his or her screen, you'll be Secret Friends in Toontown!"
FriendSecretGetSecret = 'Get a secret'
FriendSecretEnterSecret = "If you've got a secret from someone you know, type it here."
FriendSecretOK = 'OK'
FriendSecretCancel = 'Cancel'
FriendSecretGettingSecret = 'Getting secret. . .'
FriendSecretGotSecret = "Here is your new secret.  Be sure to write it down!\n\nYou may give this secret to one person only.  Once someone types in your secret, it will not work for anyone else.  If you want to give a secret to more than one person, get another secret.\n\nThe secret will only work for the next two days.  Your friend will have to type it in before it goes away, or it won't work.\n\nYour secret is:"
FriendSecretTooMany = "Sorry, you can't have any more secrets today.  You've already had more than your fair share!\n\nTry again tomorrow."
FriendSecretTryingSecret = 'Trying secret. . .'
FriendSecretEnteredSecretSuccess = 'You are now Secret Friends with %s!'
FriendSecretEnteredSecretUnknown = "That's not anyone's secret.  Are you sure you spelled it correctly?\n\nIf you did type it correctly, it may have expired.  Ask your friend to get a new secret for you (or get a new one yourself and give it to your friend)."
FriendSecretEnteredSecretFull = "You can't be friends with %s because one of you has too many friends on your friends list."
FriendSecretEnteredSecretFullNoName = "You can't be friends because one of you has too many friends on your friends list."
FriendSecretEnteredSecretSelf = 'You just typed in your own secret!  Now no one else can use that secret.'
FriendSecretNowFriends = 'You are now Secret Friends with %s!'
FriendSecretNowFriendsNoName = 'You are now Secret Friends!'
FriendsListPanelNewFriend = 'New Friend'
FriendsListPanelSecrets = 'Secrets'
FriendsListPanelOnlineFriends = 'ONLINE\nFRIENDS'
FriendsListPanelAllFriends = 'ALL\nFRIENDS'
FriendsListPanelIgnoredFriends = 'IGNORED\nTOONS'
DownloadForceAcknowledgeMsg = "Sorry, you can't advance because %(phase)s download is only %(percent)s%% complete.\n\nPlease try again later."
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
    8: 'Neighborhoods II' }
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
AvatarChoiceDeletePasswordOK = 'OK'
AvatarChoiceDeletePasswordCancel = 'Cancel'
AvatarChoiceDeleteWrongPassword = 'That password does not seem to match.  To delete this Toon, enter your password.'
AvatarChoiceDeleteWrongConfirm = 'You did not type the right thing.  To delete %(name)s, type "%(confirm)s" and click OK.  Do not type the quotation marks.  Click Cancel if you have changed your mind.'
AvatarChooserPickAToon = 'Pick  A  Toon  To  Play'
AvatarChooserQuit = 'Quit'
MultiPageTextFrameNext = 'Next'
MultiPageTextFramePrev = 'Previous'
MultiPageTextFramePage = 'Page %s/%s'
MemberAgreementScreenTitle = 'Member Agreement'
MemberAgreementScreenAgree = 'I Agree'
MemberAgreementScreenDisagree = 'I Disagree'
MemberAgreementScreenCancel = 'Cancel'
MemberAgreementScreenWelcome = 'Welcome!'
MemberAgreementScreenOnYourWay = "You're on your way to becoming an official member of"
MemberAgreementScreenToontown = "Disney's Toontown Online"
MemberAgreementScreenPricing = "Disney's Toontown Online is             for\nthe first month. Each additional month is            .\nAnd registration is easy: simply read and fill out the\ninformation below and you're on your way!"
MemberAgreementScreenCCUpFrontPricing = "Sign up now for your     -day FREE trial. You may cancel anytime\nduring your free trial period and you'll owe nothing. At the end of\nthe free trial period, you will be automatically billed            for\nthe first month, then            for each additional month."
MemberAgreementScreenGetParents = "You must be 18 or older to purchase Disney's Toontown Online. Please ask a parent or guardian for help."
MemberAgreementScreenGetParentsUnconditional = "You must be 18 or older to purchase Disney's Toontown Online. If you are under 18, please ask a parent or guardian for help."
MemberAgreementScreenMustBeOlder = "You must be 18 or older to purchase Disney's Toontown Online. Please ask a parent or guardian for help."
MemberAgreementScreenYouMustAgree = "To purchase Disney's Toontown Online, you must agree to the Member Agreement."
MemberAgreementScreenYouMustAgreeOk = 'Ok'
MemberAgreementScreenYouMustAgreeQuit = 'Quit'
MemberAgreementScreenAgreementTitle = 'Member Agreement'
MemberAgreementScreenClickNext = 'Click "Next" to advance to the next page.'
MemberAgreementScreenLegalText = [
    '\n\n\n\n\n\n\nDISNEY\'S TOONTOWN ONLINE MEMBER AGREEMENT\n\nWelcome to Disney\'s Toontown Online (the "Service"). PLEASE READ THIS MEMBER AGREEMENT (THE "AGREEMENT") CAREFULLY BEFORE USING THIS SERVICE. This Service is owned and operated by Disney Online (referred to as "Disney," "we," "us," or "our" herein).\n',
    '\nBy using this Service, you show that you agree to these terms, the Terms of Use and House Rules posted on our Web site.  If you do not agree, please do not use the Service. Please note that you will be referred to from time to time as "Member" in this Agreement. The person who initially registers for the Service may also be referred to as the "Parent Account" in this Agreement. "Account" means the account registered to any Member, pursuant to the registration procedures for the Service. The terms of this Agreement apply to all Members, whether or not they are the Parent Account. The Parent Account is responsible for making each of their family members (and anyone else they may allow to play using their Account) aware of the terms of this Agreement and for ensuring compliance. The Parent Account for an Account is entirely liable for all activities conducted through that Account.\n',
    '\nWe reserve the right, at our discretion, to change, modify, add, or remove portions of this Agreement at any time. Notification of changes to this Agreement will be posted on the Service, or sent via e-mail or postal mail.\n\nIf any future changes to this Agreement are unacceptable to you, or cause you to no longer be in compliance with this Agreement, you may terminate your Account. Your continued use of the Service following notice of changes to this Agreement (including the Terms of Use and House Rules) will mean you accept those changes.\n',
    '\nWe may change, modify, suspend, or discontinue any aspect of the Service at any time, including, without limitation, the availability of any Service feature, database or content, hours of availability, or equipment needed to access the Service. We may also impose limits on certain features or restrict your access to parts or all of the Service, for extended periods of time, without notice or liability.\n\nMember is solely responsible for and must provide all telephone and other equipment necessary to access the Service, including without limitation Internet access software and modems.\n',
    '\nRESTRICTIONS ON USE OF MATERIALS\n\nAll materials published by Disney (including, but not limited to, informational resources, photographs, images, illustrations, audio clips, and video clips (collectively, "Content") are protected by copyright, and owned or controlled by Disney, its parent or affiliated companies, or a third-party provider. You shall abide by all copyright notices, information, or restrictions contained in any Content accessed through the Service.\n',
    '\nThe Service is protected by copyright as a collective work and/or compilation, pursuant to U.S. copyright laws, international conventions, and other copyright laws. No material from the Service or any Web site owned, operated, licensed, or controlled by Disney may be copied, reproduced, republished, uploaded, posted, or transmitted, nor may derivative works be created from them or distributed in any way, except that you may download one copy of the materials on any single computer for your personal, noncommercial home use only, provided that you keep intact all copyright and other proprietary notices. Using our Content for any other purpose is a violation of our copyright and other proprietary rights. For purposes of this Agreement, using any of our Content on any other Web site or networked computer environment is prohibited.  You may not sell or auction any Disney characters, items, or copyrighted material.\n',
    '\nIf you download software from the Service, the software, including any files, images incorporated in or generated by the software, and data accompanying the software (collectively, the "Software"), are licensed to you by Disney.  We hereby grant to you a non-exclusive license to use the Software solely in connection with the Service via an authorized and fully-paid (or authorized free trial) Account.  The Parent Account represents, warrants, and covenants (a) that no materials of any kind submitted through your Account will (i) violate, plagiarize, or infringe upon the rights of any third party, including copyright, trademark, privacy, or other personal or proprietary rights; or (ii) contain libelous or otherwise unlawful material; (b) the credit card provided to us is valid, the Parent Account is authorized to use the credit card, and the Parent Account is at least 18 years old; (c) we may charge the credit card provided to us, as more fully described in the Section titled "Price and Payment" below; and (d) the Parent Account and all Members will fully comply with the terms of this Agreement.\n',
    '\nYou, the Parent Account, hereby indemnify, defend, and hold Disney, its parent and affiliated companies, and all officers, directors, owners, agents, information providers, affiliates, licensers, and licensees (collectively, the "Indemnified Parties") harmless from and against any and all liability and costs incurred by the Indemnified Parties in connection with any claim arising out of any breach by you or any Member on yoDisney does not represent or endorse the accuracy or reliability of any advice, opinion, statement, or other information displayed, uploaded, or distributed through the Service by any Member, information provider, or other person or entity. You acknowledge that any reliance upon any such opinion, advice, statement, memorandum, or information shall be at your sole risk. Disney reserves the right, in its sole discretion, to correct any errors or omissions in any portion of the Service.\n',
    '\nDISCLAIMER\n\nTHE MATERIALS IN THIS SERVICE ARE PROVIDED "AS IS" AND WITHOUT WARRANTIES OF ANY KIND EITHER EXPRESS OR IMPLIED. TO THE FULLEST EXTENT PERMISSIBLE PURSUANT TO APPLICABLE LAW, DISNEY DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. DISNEY DOES NOT WARRANT THAT THE FUNCTIONS CONTAINED IN THE SERVICE WILL BE UNINTERRUPTED OR ERROR-FREE, THAT DEFECTS WILL BE CORRECTED, OR THAT THIS SERVICE OR THE SERVER THAT MAKES IT AVAILABLE ARE FREE OF VIRUSES OR OTHER HARMFUL COMPONENTS. DISNEY DOES NOT WARRANT OR MAKE ANY REPRESENTATIONS REGARDING THE USE OR THE RESULTS OF THE USE OF THE MATERIALS IN THIS SERVICE IN TERMS OF THEIR CORRECTNESS, ACCURACY, RELIABILITY, OR OTHERWISE.\n',
    '\nYOU (AND NOT DISNEY) ASSUME THE ENTIRE COST OF ALL NECESSARY SERVICING, REPAIR, OR CORRECTION. APPLICABLE LAW MAY NOT ALLOW THE EXCLUSION OF IMPLIED WARRANTIES, SO THE ABOVE EXCLUSION MAY NOT APPLY TO YOU.\n\nWITHOUT LIMITATION OF THE FOREGOING, YOU ACKNOWLEDGE THAT, AS A SERVICE TO USERS OF THE DISNEY SERVICE, WE INCLUDE LINKS TO OTHER WEB SITES ON THE WORLD WIDE WEB PORTION OF THE INTERNET AND THAT DISNEY HAS NO CONTROL OVER, AND MAKES NO REPRESENTATIONS OF ANY KIND WHATSOEVER, REGARDING THE CONTENT OR APPROPRIATENESS OF CONTENT ON SUCH WEB SITES, AND YOU HEREBY IRREVOCABLY WAIVE ANY CLAIM AGAINST US WITH RESPECT TO SUCH WEB SITES.\n',
    "\nFurther, Disney explicitly disclaims any responsibility for the accuracy, content, or availability of information found on sites that link to or from Disney's Toontown Online from third parties not associated with Disney. Disney encourages discretion when browsing the Internet using our or anyone else's service. Because some sites employ automated search results or otherwise link you to sites containing information that may be deemed inappropriate or offensive, Disney cannot be held responsible for the accuracy, copyright compliance, legality, or decency of material contained in third-party sites, and you hereby irrevocably waive any claim against us with respect to such sites. Disney cannot ensure that you will be satisfied with any products or services that you purchase from a third-party site that links to or from Disney's Toontown Online since other shop channels are owned and operated by independent retailers.\n",
    '\nDisney does not endorse any of the merchandise, nor has Disney taken any steps to confirm the accuracy or reliability of any of the information contained in such third-party sites. Disney does not make any representations or warranties as to the security of any information including, without limitation, credit card and other personal information you might be requested to give any third party and you hereby irrevocably waive any claim against us with respect to such sites. We strongly encourage you to make whatever investigation you feel necessary or appropriate before proceeding with any online or offline transaction with any of these third parties.\n',
    "\nLIMITATION OF LIABILITY\n\nUNDER NO CIRCUMSTANCES, INCLUDING, BUT NOT LIMITED TO, NEGLIGENCE, SHALL DISNEY BE LIABLE FOR ANY SPECIAL OR CONSEQUENTIAL DAMAGES THAT RESULT FROM THE USE OF, OR THE INABILITY TO USE, THE MATERIALS IN THIS SERVICE OR ANY OTHER WEB SITE, EVEN IF DISNEY OR A DISNEY AUTHORIZED REPRESENTATIVE HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. APPLICABLE LAW MAY NOT ALLOW THE LIMITATION OR EXCLUSION OF LIABILITY OR INCIDENTAL OR CONSEQUENTIAL DAMAGES, SO THE ABOVE LIMITATION OR EXCLUSION MAY NOT APPLY TO YOU. IN NO EVENT SHALL DISNEY'S TOTAL LIABILITY TO YOU FOR ALL DAMAGES, LOSSES, AND CAUSES OF ACTION (WHETHER IN CONTRACT, TORT INCLUDING, BUT NOT LIMITED TO, NEGLIGENCE OR OTHERWISE) EXCEED THE AMOUNT PAID BY YOU, IF ANY, FOR ACCESSING THE SERVICE.\n",
    '\nSECURITY\n\nAs part of the registration process, Members will select a password, parent password and member name ("Member Name"). You shall provide Disney with accurate, complete, and updated Account information. Failure to do so shall constitute a breach of this Agreement, which may result in immediate termination of your Account. You may not (i) select or use a Member Name of another person with the intent to impersonate that person; (ii) use a name subject to the rights of any other person without authorization; or (iii) use a Member Name that Disney, in its sole discretion, deems inappropriate or offensive.\n',
    "\nYou shall notify Disney by e-mail at toontown@disneyonline.com of any known or suspected unauthorized use(s) of your Account, or any known or suspected breach of security, including loss, theft, or unauthorized disclosure of your password or parent password. You shall be responsible for maintaining the confidentiality of your password and parent password.\n\nEach Parent Account must be 18 years or older to establish an Account. If Disney becomes aware that a Parent Account is under the age of 18, Disney reserves the right to cancel the Account.\n\nAny fraudulent, abusive, or otherwise illegal activity may be grounds for termination of your Account, at Disney's sole discretion, and you may be reported to appropriate law-enforcement agencies.\n",
    "\nPRICE AND PAYMENT\n\nDisney reserves the right at any time to charge additional fees for access to the Service. Disney reserves the right to change the amount of, or basis for determining, any fees or charges for the Service, and to institute new fees or charges effective upon prior notice to Members.  Disney reserves the right to provide the Service at no charge for promotional reasons or otherwise (such as a free trial).\n\nEach Parent Account agrees to pay all charges to the Parent's Account, including applicable taxes, in accordance with billing terms in effect at the time the fee or charge becomes payable. Parent Accounts must provide Disney with valid credit card information as requested during the registration process.\n",
    "\nDisney shall charge the Parent Account's credit card on the date Parent Account subscribes to the Service. Thereafter, Disney will automatically renew and charge the Parent's Account as follows:\n\n-Each month for the following month's service for monthly subscriptions\n\n-Upon every three(3)-month anniversary of the first billing date for quarterly subscriptions\n\n-Upon every six(6)-month anniversary of the first billing date for semiannual subscriptions\n\n-Upon every one(1)-year anniversary of the first billing date for annual subscriptions\n",
    '\nThe renewal charge shall be equal to or less than the original subscription price, unless otherwise notified in advance by Disney. You may notify Disney that you wish to cancel your subscription at any time.  Disney agrees that it will terminate your Account upon receipt of notification from the Parent Account, as described below.\n\nFor monthly subscriptions: If notice of cancellation is received within the first 15 days following the first day of the initial billing, you will be eligible to receive a refund of all subscription fees for the Service, but will still be obligated to pay any other charges incurred. If you cancel the Service more than 15 days after the initial billing, your Account will be canceled as of the end of the current billing period and no refund for unused time will be given.\n',
    '\nFor quarterly subscriptions: If notice of cancellation is received within the first 30 days following the first day of the initial billing, you will be eligible to receive a refund of all subscription fees for the Service, but will still be obligated to pay any other charges incurred. If you cancel the Service more than 30 days after the initial billing, no refund for unused time will be given.\n\nFor semiannual subscriptions: If notice of cancellation is received within the first 30 days following the first day of initial billing, you will be eligible to receive a refund of all subscription fees for the Service but will still be obligated to pay any other charges incurred. If you cancel the Service more than 30 days after the initial billing, no refund for unused time will be given.\n',
    '\nFor annual subscriptions: If notice of cancellation is received within the first 30 days following the first day of initial billing, you will be eligible to receive a refund of all subscription fees for the Service but will still be obligated to pay any other charges incurred. If you cancel the Service more than 30 days after the initial billing, no refund for unused time will be given.\n\nYour right to use the Service is subject to any limits established by Disney or by your credit card issuer. If payment cannot be charged to your credit card or your charge is returned to Disney for any reason, including chargeback, Disney reserves the right to either suspend or terminate your access and Account, thereby terminating this Agreement and all obligations of Disney hereunder.\n',
    '\nIf you have a balance due on any Disney Account, you agree that Disney can charge these unpaid fees to your credit card. Disney reserves the right to establish a credit limit (the "Ceiling") for each Member. If a Member\'s Account reaches the Ceiling at any time, Disney may immediately bill the Member\'s credit card for all unpaid charges on account. Until further notice, the Ceiling for each Member is $100.\n\nIf you have reason to believe that your Account is no longer secure (for example, in the event of a loss, theft, or unauthorized disclosure or use of your Member Name, Password, or any credit, debit, or charge card number stored on the Service), you must promptly change your Password and notify Disney of the problem (by notice given as described in the Notice section below) to avoid possible liability for any unauthorized charges to your Account.\n',
    '\nPARENTAL CONSENT\n\nUnder the Children\'s Online Privacy Protection Act ("COPPA"), parental consent is required for the online collection, use and/or disclosure of personal information obtained from a child under the age of 13.  As part of the registration process for the Service, the Parent Account will be asked to provide a valid credit card.  Parents and legal guardians, you will be allowed to create up to six Toons (a Toon is a character you create and use to play the game in the Service), all will be under the Parent Account.  Kids will need to have a parent or legal guardian register as the Parent Account holder and then they can create their own Toon within the Parent Account.\n',
    '\nBy providing his or her credit card number, the Parent Account holder: (a) represents and warrants that he or she is the parent or legal guardian of any child under the age of 13 for whom he or she allows to use the Parent Account; and (b) agrees to our collection, use and disclosure of personal information in accordance with the Privacy Policy with respect to any child under the age of 13 for whom the Parent Account holder allows to use the Parent Account.\n\nThe Service includes an interactive feature we call Secret Friends.  The Parent Account will be given the opportunity to disable the Secret Friends feature once he or she is inside the Service. Secret Friends allows one member to chat with another member only by means of a secret code that must be communicated outside of the game.  Secret Friends is not moderated or supervised.\n',
    '\nIf the Parent Account allows a child to use his or her account with the Secret Friends feature enabled, we encourage parents to supervise their child or children while they play in the Service.  By enabling the Secret Friends feature, the Parent Account acknowledges that there are some risks inherent in the Secret Friends feature and that the Parent Account has been informed of, and agrees to accept, any such risks.  You will be given the opportunity to learn more about the Secret Friends feature, and the chance to enable it, once you are inside the Service.\n',
    '\nNOTICE\n\nThe Parent Account will submit and maintain a correct e-mail address and other Account information. We may give notice to the Parent Account by means of a general notice on the Service, electronic mail to your e-mail address on record in our Account information, or by written communication sent by first-class mail to your address on record in our Account information. You may give notice to Disney. Such notice shall be deemed given when received by Disney at any time by e-mail at toontown@disneyonline.com.\n',
    '\nNON-TRANSFERABILITY OF MEMBERSHIP\n\nDisney grants to you a personal, nonexclusive, nonassignable, and non-transferable license to use and display the Disney Software on any machine(s) of which you are the primary user. Unauthorized copying of the Software or duplication of the Software in any manner, including software that has been modified, merged, or included with the Software, or the written materials associated therewith, is expressly forbidden. You acknowledge that you may not sublicense, transfer, sell, or assign this license or the Software. Any attempt to sublicense, transfer, sell, or assign the license is void.\n',
    "\nJURISDICTIONAL ISSUES\n\nThis Service is controlled and operated by Disney from its offices within the State of California, United States of America. Disney makes no representation that materials in the Service are appropriate or available for use in other locations. Those who choose to access this Service from other locations do so on their own initiative and are responsible for compliance with local laws, if and to the extent local laws are applicable. Software from this Service is further subject to United States export controls. No Software from this Service may be downloaded or otherwise exported or reexported (i) into (or to a national or resident of) Cuba, Iraq, Libya, North Korea, Iran, Syria, or any other country to which the U.S. has embargoed goods; or (ii) to anyone on the U.S. Treasury Department's list of Specially Designated Nationals or the U.S. Commerce Department's Table of Deny Orders.\n",
    '\nBy downloading or using the Software, you represent and warrant that you are not located in, under the control of, or a national or resident of any such country or on any such list. Certain Software that Members download to use or install from a CD-ROM is "Restricted Computer Software." Use, duplication, or disclosure by the U.S. Government is subject to restrictions as set forth in this Agreement and as provided in DFARS 227.7202-1(a) and 227.7202-3(a) (1995), DFARS 252.227-7013 (October 1988), FAR 12.212(a) (1995), FAR 52.227-19, or FAR 52.227-14, as applicable.\n',
    "\nTERMINATION OF SERVICE\n\nThis Agreement is effective until terminated by either party. You may terminate this Agreement and your right to use the Service at any time by sending an e-mail to toontown@disneyonline.com. Disney may terminate your Account or access rights to this Service immediately without notice if in Disney's sole discretion you fail to comply with any term or provision of this Agreement (including the Terms of Use and House Rules). Upon termination, you must destroy all materials obtained from this Service and all copies thereof, whether made under the terms of this Agreement or otherwise.\n",
    '\nOTHER\n\nThis Agreement shall be governed by and construed in accordance with the laws of the State of California, without giving effect to any principles of conflicts of law. If any provision of this Agreement shall be unlawful, void, or for any reason unenforceable, then that provision shall be deemed severable from this Agreement and shall not affect the validity and enforceability of any remaining provisions. This is the entire Agreement between the parties relating to the subject matter herein and shall not be modified except in writing other than as provided below.\n',
    '\nENTIRE AGREEMENT\n\nThis Agreement constitutes the entire agreement between the parties with respect to the subject matter contained herein and supersedes all previous and contemporaneous agreements, proposals, and communications, written or oral, between Disney representatives and you. Disney may amend or modify this Agreement or impose new conditions at any time upon notice from Disney to you as described in the Section titled "Notice" above. Any use of the Service by you after such notice shall be deemed to constitute acceptance by Member of such amendments, modifications, or new conditions.\n\nLAST UPDATED:\n10/18/02\n']
BillingScreenCCTypeInitialText = 'Please Choose'
BillingScreenCreditCardTypes = [
    'Visa',
    'American Express',
    'MasterCard']
BillingScreenTitle = 'Please Enter Billing Information'
BillingScreenAccountName = 'Account Name'
BillingScreenEmail = 'Billing/Parent Email Address'
BillingScreenEmailConfirm = 'Confirm Email Address'
BillingScreenCreditCardType = 'Credit Card Type'
BillingScreenCreditCardNumber = 'Credit Card Number'
BillingScreenCreditCardExpires = 'Expiration Date'
BillingScreenCreditCardName = 'Name as it appears on credit card'
BillingScreenAgreementText = 'By clicking the "Purchase" button I agree that, in accordance with the Privacy Policy, my child/children may use the interactive features that are authorized through the Parent Password that I establish on the following screen.'
BillingScreenBillingAddress = 'Billing Address: Street 1'
BillingScreenBillingAddress2 = 'Street 2 (if applicable)'
BillingScreenCity = 'City'
BillingScreenCountry = 'Country'
BillingScreenState = 'State'
BillingScreenZipCode = 'Zip Code'
BillingScreenCAProvince = 'Province or Territory'
BillingScreenProvince = 'Province (if applicable)'
BillingScreenPostalCode = 'Postal Code'
BillingScreenPricing = '              for the first month, then              per month'
BillingScreenSubmit = 'Purchase'
BillingScreenCancel = 'Cancel'
BillingScreenConfirmCancel = 'Cancel Purchase?'
BillingScreenConfirmCancelYes = 'Yes'
BillingScreenConfirmCancelNo = 'No'
BillingScreenPleaseWait = 'Please wait...'
BillingScreenConnectionErrorSuffix = '.\nPlease try again later.'
BillingScreenEnterEmail = 'Please enter your email address.'
BillingScreenEnterEmailConfirm = 'Please type your email address a second time.'
BillingScreenEnterValidEmail = 'Please enter a valid email address.'
BillingScreenEmailMismatch = 'The email addresses that you entered did not match. Please try again.'
BillingScreenEnterAddress = 'Please enter your full billing address.'
BillingScreenEnterValidState = 'Please enter a two-letter state abbreviation.'
BillingScreenChooseCreditCardType = 'Please choose a credit card type.'
BillingScreenEnterCreditCardNumber = 'Please enter your credit card number.'
BillingScreenEnterValidCreditCardNumber = 'Please double-check your credit card number.'
BillingScreenEnterValidSpecificCreditCardNumber = 'Please enter a valid %s credit card number.'
BillingScreenEnterValidCreditCardExpDate = 'Please enter a valid credit card expiration date.'
BillingScreenEnterNameOnCard = 'Please enter the name that appears on your credit card.'
BillingScreenCreditCardProblem = 'There was an error processing your credit card.'
BillingScreenTryAnotherCC = 'Try Another Card?'
BillingScreenCustomerServiceHelp = '\n\nIf you need help, please call Customer Service at %s.'
BillingScreenCCProbQuit = 'Quit'
BillingScreenWhySafe = 'Credit Card Security'
BillingScreenWhySafeTitle = 'Credit Card Security'
BillingScreenWhySafeCreditCardGuarantee = 'CREDIT CARD GUARANTEE'
BillingScreenWhySafeJoin = 'JOIN'
BillingScreenWhySafeToontown = "DISNEY'S TOONTOWN ONLINE"
BillingScreenWhySafeToday = 'TODAY!'
BillingScreenWhySafeClose = 'Close'
BillingScreenWhySafeText = [
    "\n\n\n\n\nWe use the Secure Sockets Layer (SSL) technology, which encrypts your credit card information, keeping it private and protected. This technology makes it safe to enter and transmit your credit card information over the Internet.\nThis security technology protects your Internet communication with:\n\n     Server authentication (thwarting imposters)\n     Privacy using encryption (thwarting eavesdroppers)\n     Data integrity (thwarting vandals)\n\nTo give you an additional layer of security, all credit card numbers are stored on a computer that is not connected to the Internet. After you type it in, your complete credit card number is transferred to this secure machine across a proprietary interface. Your credit card number is not stored anywhere else.\n\n\n\nSo, not only is your credit card information safe with us at Disney's Toontown Online -- we guarantee it!\nWe back every subscription to Disney's Toontown Online with our Credit Card Guarantee. If, through no fault of your own, unauthorized charges appear on your statement as a direct result of providing your credit card information to Disney's Toontown Online, we will cover the amount for which your bank holds you liable, up to a maximum of $50.\n\nIf you suspect a problem, follow the normal reporting procedures defined by your credit card provider and also contact us immediately. Most credit card companies cover all charges resulting from unauthorized use, but they may legally hold you liable for as much as $50. We will cover the liability not covered by your credit card.\nWhat does all of this mean? It means you can be confident in the security and support behind your subscription to Disney's Toontown Online.\n\nSo, what are you waiting for?\n"]
BillingScreenPrivacyPolicy = 'Privacy Policy'
BillingScreenPrivacyPolicyClose = 'Close'
BillingScreenPrivacyPolicyText = [
    "\nPrivacy Policy\n\nQ1 What types of information are WDIG sites collecting, and how are the sites collecting it?\n\nThe majority of great products and services on our sites are offered without our collecting any personally identifiable information from you. You can surf WDIG's Web sites and view much of our terrific content anonymously. For instance, you can view news headlines at ABCNEWS.com without giving out any personally identifiable information.\n\nInformation You Provide\nThere are a few activities on our sites where the collection of personally identifiable information is necessary. Those activities include things like entering a contest or sweepstakes, making a purchase, or contacting us. When personally identifiable information is collected, you will know because you will have to fill out a form. For most activities, we collect only your name, e-mail address, birth date, gender, and zip code. When you make a purchase, we also collect your street and billing addresses, your phone number, and credit card information. Depending on what you purchase, we may also need to collect other personal information, like your clothing size.\n",
    "\nInformation Collected from You with Technology\nWDIG sites collect some information about you using technology, so it may not be readily apparent to you that it is being collected. For instance, when you come to our site your IP address is collected so that we know where to send information you are requesting. An IP address is often associated with the place from which you enter the Internet like your ISP (Internet service provider), your company, or your university. This information is not personally identifiable. WDIG sites use information collected through technology to make our sites more interesting and useful to you. This includes helping advertisers on our site design advertisements our Guests might like. We normally don't combine this type of information with personally identifiable information. However, we will combine this information with personally identifiable information to identify a visitor in order to enforce compliance with our house rules or terms of service or to protect our service, site, Guests, or others.\n\nWhat Are Cookies, and How Does WDIG Use Them?\nCookies are pieces of information that a Web site sends to your computer while you are viewing the Web site. These pieces of information allow the Web site to remember important information that will make your use of that site more useful. WDIG and other Internet companies use cookies for a variety of purposes. For instance, DisneyStore.com uses cookies to remember and process the items in your shopping cart, and all WDIG sites use cookies to make sure kids don't enter unmoderated chat rooms.\n\nYou can choose to have your computer warn you each time a cookie is being sent, or you can choose to turn off all cookies. You do this through your browser (like Netscape Navigator or Internet Explorer) settings. Each browser is a little different, so look at your browser Help menu to learn the correct way to modify your cookies. If you turn cookies off, you won't have access to many WDIG features that make your Web experience more efficient -- like the features mentioned above -- and some of our services will not function properly.\n",
    "\nQ2 How does WDIG use the personally identifiable information that has been collected?\n\nWDIG uses personally identifiable information in a limited number of ways. We use the information to complete transactions. For instance, if you purchase a fantasy team on ESPN.com, we use your information to process your order, or if you contact us for help we will use the information to contact you. We use information collected to notify you if you've won a game or contest. Information we collect is used to send you e-mail updates and newsletters about our sites. We also use the information you provide to send you WDIG e-mail promotions and special offers from our third-party sponsors.\n",
    '\nQ3 Does WDIG share information with companies or other organizations that are not part of the WDIG family of sites?\n\nOne of the most valuable assets of our business is you. We aren\'t in the business of selling information about our Guests. However, if there is a value for our Guests, we will share your information or send you messages on behalf of another company as described below. We will also share information for security reasons.\nCompanies That Are "Standing in the Shoes" of WDIG\nSometimes we hire companies to help us deliver products or services, like a shipping company that delivers a package. In those instances, we need to share your information with them. These companies are basically "standing in the shoes" of WDIG, and they are allowed to use the information only to deliver the product or service.\n',
    "\nCompanies Offering Promotions, Products, or Services\nOn occasion, we offer promotions -- like sweepstakes or free subscriptions -- in conjunction with a sponsor. We will share your information with the sponsors if they need it to send you a product, such as a magazine subscription. We may share your information with those sponsors so that they can send you other special promotions they offer, but only if you give us your permission to do so, and we will share it only with that specific sponsor. In addition, WDIG occasionally sends e-mail promotions out to our Guests on behalf of third-party sponsors. In this instance, we don't share your name with the third party -- we do the mailing for them. Again, we only send these promotions to you if you've given your permission.\n\nContent Partners\nOn some of our sites, we provide content that is created by a third-party partner Web site. For instance, ESPN.com provides shopping opportunities with third parties. In some instances the third-party sites will collect information in order to facilitate the transaction or to make the use of their content more productive and efficient. In these circumstances the information collected is shared between WDIG and our third-party sponsors.\n\nThird-Party Advertisers and Network Advertisers\nTo help increase privacy protections for our Guests, WDIG allows advertising on our sites from only those companies that have their own privacy policy. Once you've clicked on an advertisement and have left WDIG sites, our privacy policy no longer applies. You must read the privacy policy of the advertiser to see how your personal information will be handled on their site.\n",
    '\nIn addition, many business advertisements are managed and placed on our site by third-party companies. These companies are called "network advertisers." Network advertisers collect non-personally identifiable information when you click on or scan one of their banner advertisements. The information is collected using technology, so you may not realize it\'s being collected. The network advertisers collect this information so that they can show you ads that are more relevant and interesting to you. If you would like to read more about network advertisers or do not want network advertisers to collect this non-personally identifiable information about you, click here.\n\nPurchase or Sale of Businesses\nOnline business is still in a very early stage and is changing and evolving rapidly. As WDIG continually looks for ways to improve our business, we may buy or sell a company. If we buy or sell a business, the names collected will likely be transferred as a part of the sale. Information about registrants will be used in the aggregate. However, if we buy a business, we will honor the requests that customers made of that business regarding e-mail communications. In the event that we sell a business, we will do everything in our power to ensure that the e-mail communications requests you made of us are honored.\n\nOrganizations That Help Protect the Security and Safety of Our Guests and Our Sites\nWe will give out personal information as required by law, for example, to comply with a court order or subpoena; to enforce our Terms of Service, or site or game rules; or to protect the safety and security of Guests and our sites.\n',
    "\nQ4 What choices do I have about WDIG collecting, using, and sharing my information?\n\nIt is possible for you to use much of our site without giving us any personally identifiable information. When you do register with us or give us personally identifiable information, you will have an opportunity at the time we collect your information -- to limit e-mail communications from WDIG and from our third-party partners. You can request at any time that WDIG not send future e-mail to you either by unsubscribing from the communication or by contacting us at memberservices@help.go.com. Also, as mentioned above, there are ways to limit the information collected through technology -- though some of our features won't work if you decide to do this.\n",
    "\nQ5 What type of security does WDIG provide?\n\nThe importance of security for all personally identifiable information associated with our Guests is of utmost concern to us. WDIG takes technical, contractual, administrative, and physical security steps to protect all visitors' information. When you provide credit card information, we use secure socket layer (SSL) encryption to protect it. There are some things that you can do to help protect the security of your information as well. For instance, never give out your Password, since this is what is used to access all of your account information. Also remember to sign out of your account and close your browser window when you finish surfing the Web, so that other people using the same computer won't have access to your information.\n",
    '\nQ6 How can I access my account information?\n\nYou can access the personally identifiable information you gave us during registration at our Account Options center available from (http://play.toontown.com).  Log-in with your account name and parent password. There are instructions on the start page to help you recover your password if you\'ve forgotten it.\nYou can also contact us by clicking "Contact Us" in the footer on any WDIG page and selecting "Registration/Personalization" in the drop down box, or send an e-mail directly to memberservices@help.go.com. Please include information in the e-mail that will help us identify your account so we can assist you with your inquiry or request.\n',
    '\nQ7 Whom do I contact with questions or concerns about this privacy policy?\n\nIf you need further assistance, please send an e-mail with your questions or comments to memberservices@help.go.com\nwrite us at:\n\nMember Services\nWalt Disney Internet Group\n506 2nd Avenue\nSuite 2100\nSeattle, WA 98104\n\nWalt Disney Internet Group is a licensee of the TRUSTe Privacy Program. If you believe that WDIG has not responded to your inquiry or your inquiry has not been satisfactorily addressed, please contact TRUSTe http://www.truste.org/users/users_watchdog.html.\n*You must be 18 or have the permission of your parent or guardian to dial this number.\n',
    "\nKids' Privacy Policy:\nWe recognize the need to provide additional privacy protections for kids who visit our sites.\n\nQ1 What types of information are WDIG sites collecting about kids who are 12 and younger?\n\nChildren can surf Disney.com or other WDIG sites, view content, and play some games without any personally identifiable information being collected. In addition, we occasionally do host some moderated chat rooms where no personally identifiable information is collected or posted. However, in some areas it is necessary to collect personally identifiable information from kids to allow participation in an activity (like entering a contest) or to communicate with our community (via e-mail or message boards).\nWDIG believes it is good policy not to collect more personally identifiable information from kids 12 and younger than is necessary for them to participate in our online activities. In addition, be aware that all sites that are targeted to children 12 and younger are prohibited by law from collecting more information than they need.\n\nThe only personally identifiable information we collect from kids is first name, parent's e-mail address, and child's birth date. We collect birth date to validate a Guest's age. We may also collect personal information, like a pet's name, to help Guests remember their Log-in Name and Password if they forget them.\n\nWe also allow parents to request at any time that the information collected about their child be removed from our database. If you would like to deactivate your child's account, please send an e-mail message to ms_support@help.go.com with your child's Log-in Name and Password requesting that the account be cancelled.\n",
    "\nQ2 How does WDIG use and share the personally identifiable information that has been collected?\n\nNo information collected from Guests 12 and younger is used for any marketing or promotional purposes whatsoever, either inside or outside Walt Disney Internet Group's family of sites.\nThe information collected about kids 12 and younger is used only by WDIG Web sites to provide services (such as calendars) or to conduct some games or contests. Although Guests 12 and younger may be allowed to participate in some contests where information is collected, notification and prizes are sent to the parents' or guardians' e-mail address provided during the initial registration process. Publication of contest winners' full names, ages, or images for individuals 12 and younger require parental or guardian consent. Sometimes a nonidentifiable version of a child's name will be published. In those circumstances, parents may not be contacted again for permission.\n\nWe do not allow kids 12 and younger to participate in unmoderated chat rooms.\n\nWe will give out personal information about kids if required by law, for example, to comply with a court order or subpoena; to enforce our Terms of Service, or site or game rules; or to protect the safety and security of Guests and our sites.\n",
    "\nQ3 Does WDIG notify parents about the collection of information on kids 12 and younger?\n\nAny time children 12 and younger register with us, we send an e-mail notification to their parent or guardian. In addition, we require parents to give express permission before we will allow their children to use e-mail, message boards, and other features where personally identifiable information can be made public to the Internet and shared with users of all ages.\nWe also give parents 48 hours to refuse any registrations kids make in order to play games and contests. If we don't hear back, we assume it's ok for a child to be registered with us. Once a child has registered, he or she will be allowed to enter any future registration-based games and contests, and parents aren't notified again. In this instance, we use the information collected only to notify parents when a child has won a game or contest. We don't use this information for any other purpose.\n",
    "\nQ4 How do parents access information about their kids?\n\nHere are three methods to review the information that has been collected about children who are 12 and younger.\n\nWhen parents give their children access to interactive features like message boards, they are required to establish a family account. Once a family account is established, the primary account holder can review the personally identifiable information of all family member accounts including a child's. You can access this information by logging in to your family account at the Your Account home page.\n\nIf you are not already a member of any of the WDIG sites, you can review your child's personally identifiable information by logging in to your child's account at the Account Options Home Page. You will need to have your child's account name and password. There are instructions on the Your Account home page to help you recover your child's password if they've forgotten it.\n\nYou can also contact Customer Service to view the information that has been collected from or about your child by sending an e-mail to ms_support@help.go.com. If you have not yet established a family account, you will need to have your child's user name and password. Please include information (child's account name, parent email address) in the email that will help us identify your child's account so we can assist you with your inquiry or request.\n",
    "\nQ5 What type of security does WDIG provide?\n\nThe importance of security for all personally identifiable information associated with our guests is of utmost concern to us. WDIG takes technical, contractual, administrative, and physical security steps to protect all visitors' information. When you provide credit card information, we use secure socket layer (SSL) encryption to protect it. There are some things that you can do to help protect the security of your information as well. For instance, never give out your Password, since this is what is used to access all of your account information. Also remember to sign out of your account and close your browser window when you finish surfing the Web so that other people using the same computer won't have access to your information.\n",
    '\nQ6 How will WDIG notify parents if this privacy policy changes?\n\nIf WDIG changes this privacy policy, we will notify parents via e-mail.\n\nQ7 Whom do I contact with questions or concerns about this privacy policy?\n\nIf you need further assistance, please send an e-mail with your questions or comments to ms_support@help.go.com\nwrite us at:\n\nMember Services\nWalt Disney Internet Group\n506 2nd Avenue\nSuite 2100\nSeattle, WA 98104\nor call us at (509) 742-4698\n\nWalt Disney Internet Group is a licensee of the TRUSTe Privacy Program. If you believe that WDIG has not responded to your inquiry or your inquiry has not been satisfactorily addressed, please contact TRUSTe http://www.truste.org/users/users_watchdog.html.\n*You must be 18 or have the permission of your parent or guardian to dial this number.\n']
BillingScreenCountryNames = {
    'US': 'United States',
    'CA': 'Canada',
    'AF': 'Afghanistan',
    'AL': 'Albania',
    'DZ': 'Algeria',
    'AS': 'American Samoa',
    'AD': 'Andorra',
    'AO': 'Angola',
    'AI': 'Anguilla',
    'AQ': 'Antarctica',
    'AG': 'Antigua and Barbuda',
    'AR': 'Argentina',
    'AM': 'Armenia',
    'AW': 'Aruba',
    'AU': 'Australia',
    'AT': 'Austria',
    'AZ': 'Azerbaijan',
    'BS': 'Bahamas',
    'BH': 'Bahrain',
    'BD': 'Bangladesh',
    'BB': 'Barbados',
    'BY': 'Belarus',
    'BE': 'Belgium',
    'BZ': 'Belize',
    'BJ': 'Benin',
    'BM': 'Bermuda',
    'BT': 'Bhutan',
    'BO': 'Bolivia',
    'BA': 'Bosnia and Herzegovina',
    'BW': 'Botswana',
    'BV': 'Bouv et Island',
    'BR': 'Brazil',
    'IO': 'British Indian Ocean Territory',
    'BN': 'Brunei Darussalam',
    'BG': 'Bulgaria',
    'BF': 'Burkina Faso',
    'BI': 'Burundi',
    'KH': 'Cambodia',
    'CM': 'Cameroon',
    'CV': 'Cape Verde',
    'KY': 'Cayman Islands',
    'CF': 'Central African Republic',
    'TD': 'Chad',
    'CL': 'Chile',
    'CN': 'China',
    'CX': 'Christmas Island',
    'CC': 'Cocos (Keeling) Islands',
    'CO': 'Colombia',
    'KM': 'Comoros',
    'CG': 'Congo',
    'CK': 'Cook Islands',
    'CR': 'Costa Rica',
    'CI': "Cote D'Ivoire (Ivory Coast)",
    'HR': 'Croatia (Hrvatska)',
    'CU': 'Cuba',
    'CY': 'Cyprus',
    'CZ': 'Czech Republic',
    'CS': 'Czechoslovakia (former)',
    'DK': 'Denmark',
    'DJ': 'Djibouti',
    'DM': 'Dominica',
    'DO': 'Dominican Republic',
    'TP': 'East Timor',
    'EC': 'Ecuador',
    'EG': 'Egypt',
    'SV': 'El Salvador',
    'GQ': 'Equatorial Guinea',
    'ER': 'Eritrea',
    'EE': 'Estonia',
    'ET': 'Ethiopia',
    'FK': 'Falkland Islands (Malvinas)',
    'FO': 'Faroe Islands',
    'FJ': 'Fiji',
    'FI': 'Finland',
    'FR': 'France',
    'FX': 'France - Metropolitan',
    'GF': 'French Guiana',
    'PF': 'French Polynesia',
    'TF': 'French Southern Territories',
    'GA': 'Gabon',
    'GM': 'Gambia',
    'GE': 'Georgia',
    'DE': 'Germany',
    'GH': 'Ghana',
    'GI': 'Gibraltar',
    'GB': 'Great Britain (UK)',
    'GR': 'Greece',
    'GL': 'Greenland',
    'GD': 'Grenada',
    'GP': 'Guadeloupe',
    'GU': 'Guam',
    'GT': 'Guatemala',
    'GN': 'Guinea',
    'GW': 'Guinea-Bissau',
    'GY': 'Guyana',
    'HT': 'Haiti',
    'HM': 'Heard and McDonald Islands',
    'HN': 'Honduras',
    'HK': 'Hong Kong',
    'HU': 'Hungary',
    'IS': 'Iceland',
    'IN': 'India',
    'ID': 'Indonesia',
    'IR': 'Iran',
    'IQ': 'Iraq',
    'IE': 'Ireland',
    'IL': 'Israel',
    'IT': 'Italy',
    'JM': 'Jamaica',
    'JP': 'Japan',
    'JO': 'Jordan',
    'KZ': 'Kazakhstan',
    'KE': 'Kenya',
    'KI': 'Kiribati',
    'KP': 'Korea (North)',
    'KR': 'Korea (South)',
    'KW': 'Kuwait',
    'KG': 'Kyrgyzstan',
    'LA': 'Laos',
    'LV': 'Latvia',
    'LB': 'Lebanon',
    'LS': 'Lesotho',
    'LR': 'Liberia',
    'LY': 'Libya',
    'LI': 'Liechtenstein',
    'LT': 'Lithuania',
    'LU': 'Luxembourg',
    'MO': 'Macau',
    'MK': 'Macedonia',
    'MG': 'Madagascar',
    'MW': 'Malawi',
    'MY': 'Malaysia',
    'MV': 'Maldives',
    'ML': 'Mali',
    'MT': 'Malta',
    'MH': 'Marshall Islands',
    'MQ': 'Martinique',
    'MR': 'Mauritania',
    'MU': 'Mauritius',
    'YT': 'Mayotte',
    'MX': 'Mexico',
    'FM': 'Micronesia',
    'MD': 'Moldova',
    'MC': 'Monaco',
    'MN': 'Mongolia',
    'MS': 'Montserrat',
    'MA': 'Morocco',
    'MZ': 'Mozambique',
    'MM': 'Myanmar',
    'NA': 'Namibia',
    'NR': 'Nauru',
    'NP': 'Nepal',
    'NL': 'Netherlands',
    'AN': 'Netherlands Antilles',
    'NT': 'Neutral Zone',
    'NC': 'New Caledonia',
    'NZ': 'New Zealand (Aotearoa)',
    'NI': 'Nicaragua',
    'NE': 'Niger',
    'NG': 'Nigeria',
    'NU': 'Niue',
    'NF': 'Norfolk Island',
    'MP': 'Northern Mariana Islands',
    'NO': 'Norway',
    'OM': 'Oman',
    'PK': 'Pakistan',
    'PW': 'Palau',
    'PA': 'Panama',
    'PG': 'Papua New Guinea',
    'PY': 'Paraguay',
    'PE': 'Peru',
    'PH': 'Philippines',
    'PN': 'Pitcairn',
    'PL': 'Poland',
    'PT': 'Portugal',
    'PR': 'Puerto Rico',
    'QA': 'Qatar',
    'RE': 'Reunion',
    'RO': 'Romania',
    'RU': 'Russian Federation',
    'RW': 'Rwanda',
    'GS': 'S. Georgia and S. Sandwich Isls.',
    'KN': 'Saint Kitts and Nevis',
    'LC': 'Saint Lucia',
    'VC': 'Saint Vincent and the Grenadines',
    'WS': 'Samoa',
    'SM': 'San Marino',
    'ST': 'Sao Tome and Principe',
    'SA': 'Saudi Arabia',
    'SN': 'Senegal',
    'SC': 'Seychelles',
    'SL': 'Sierra Leone',
    'SG': 'Singapore',
    'SK': 'Slovak Republic',
    'SI': 'Slovenia',
    'Sb': 'Solomon Islands',
    'SO': 'Somalia',
    'ZA': 'South Africa',
    'ES': 'Spain',
    'LK': 'Sri Lanka',
    'SH': 'St. Helena',
    'PM': 'St. Pierre and Miquelon',
    'SD': 'Sudan',
    'SR': 'Suriname',
    'SJ': 'Svalbard and Jan Mayen Islands',
    'SZ': 'Swaziland',
    'SE': 'Sweden',
    'CH': 'Switzerland',
    'SY': 'Syria',
    'TW': 'Taiwan',
    'TJ': 'Tajikistan',
    'TZ': 'Tanzania',
    'TH': 'Thailand',
    'TG': 'Togo',
    'TK': 'Tokelau',
    'TO': 'Tonga',
    'TT': 'Trinidad and Tobago',
    'TN': 'Tunisia',
    'TR': 'Turkey',
    'TM': 'Turkmenistan',
    'TC': 'Turks and Caicos Islands',
    'TV': 'Tuvalu',
    'UG': 'Uganda',
    'UA': 'Ukraine',
    'AE': 'United Arab Emirates',
    'UK': 'United Kingdom',
    'UY': 'Uruguay',
    'UM': 'US Minor Outlying Islands',
    'SU': 'USSR (former)',
    'UZ': 'Uzbekistan',
    'VU': 'Vanuatu',
    'VA': 'Vatican City State (Holy See)',
    'VE': 'Venezuela',
    'VN': 'Vietnam',
    'VG': 'Virgin Islands (British)',
    'VI': 'Virgin Islands (U.S.)',
    'WF': 'Wallis and Futuna Islands',
    'EH': 'Western Sahara',
    'YE': 'Yemen',
    'YU': 'Yugoslavia',
    'ZR': 'Zaire',
    'ZM': 'Zambia',
    'ZW': 'Zimbabwe' }
BillingScreenStateNames = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AR': 'Arkansas',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Lousiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming',
    'DC': 'District of Columbia',
    'AS': 'American Samoa',
    'GU': 'Guam',
    'MP': 'Northern Mariana Islands',
    'PR': 'Puerto Rico',
    'VI': 'Virgin Islands',
    'FPO': [
        'Midway Island',
        'Kingman Reef'],
    'APO': [
        'Wake Island',
        'Johnston Island'],
    'MH': 'Marshall Islands',
    'PW': 'Palau',
    'FM': 'Micronesia' }
BillingScreenCanadianProvinces = {
    'AB': 'Alberta',
    'BC': 'British Columbia',
    'MB': 'Manitoba',
    'NB': 'New Brunswick',
    'NF': 'Newfoundland',
    'NT': 'Northwest Territories',
    'NS': 'Nova Scotia',
    'ON': 'Ontario',
    'PE': 'Prince Edward Island',
    'QC': 'Quebec',
    'SK': 'Saskatchewan',
    'YT': 'Yukon' }
ParentPassword = 'Parent Password'
WelcomeScreenHeading = 'Welcome!'
WelcomeScreenOk = "LET'S PLAY!"
WelcomeScreenSentence1 = 'You are now an official member of'
WelcomeScreenToontown = "Disney's Toontown Online"
WelcomeScreenSentence2 = "Remember to check your email later for exciting news about Disney's Toontown Online!"
TTAccountCallCustomerService = 'Please call Customer Service at %s.'
TTAccountCustomerServiceHelp = '\nIf you need help, please call Customer Service at %s.'
TTAccountIntractibleError = 'An error occurred.'
LoginScreenUserName = 'Account Name'
LoginScreenPassword = 'Password'
LoginScreenLogin = 'Login'
LoginScreenCreateAccount = 'Create Account'
LoginScreenForgotPassword = 'Forgot Your Password?'
LoginScreenQuit = 'Quit'
LoginScreenLoginPrompt = 'Please enter a user name and password.'
LoginScreenBadPassword = 'Bad password.\nPlease try again.'
LoginScreenInvalidUserName = 'Invalid user name.\nPlease try again.'
LoginScreenUserNameNotFound = 'User name not found.\nPlease try again or create a new account.'
LoginScreenPeriodTimeExpired = 'Sorry, you have already used up all of your available minutes in Toontown this month.  Please come back at the first of the next month.'
LoginScreenNoNewAccounts = 'Sorry, we are not accepting new accounts at this time.'
LoginScreenTryAgain = 'Try Again'
NewPlayerScreenNewAccount = 'Start Free Trial'
NewPlayerScreenLogin = 'Existing Member'
NewPlayerScreenQuit = 'Quit'
FreeTimeInformScreenDontForget = "Don't forget, your free trial\nwill expire in "
FreeTimeInformScreenNDaysLeft = FreeTimeInformScreenDontForget + 'only %s days!'
FreeTimeInformScreenOneDayLeft = FreeTimeInformScreenDontForget + '1 day!'
FreeTimeInformScreenNHoursLeft = FreeTimeInformScreenDontForget + 'only %s hours!'
FreeTimeInformScreenOneHourLeft = FreeTimeInformScreenDontForget + '1 hour!'
FreeTimeInformScreenLessThanOneHourLeft = FreeTimeInformScreenDontForget + 'less than 1 hour!'
FreeTimeInformScreenSecondSentence = "But there's still time to become an\nofficial member of Disney's Toontown Online!"
FreeTimeInformScreenOops = 'OOPS'
FreeTimeInformScreenExpired = "                 , your free trial is now over!\nWant to be an official member of Disney's Toontown Online?\nSign up now and jump right back into the fun!"
FreeTimeInformScreenExpiredQuitText = "Can't right now? Don't worry, we'll save\nyour Toon for you! But hurry back! We can\nonly save your Toon for up to 1 week after\nyour free trial is over."
FreeTimeInformScreenExpiredCCUF = "You have not yet purchased Disney's\nToontown Online. To use this account, you\nmust now register with a credit card.\nSign up now and jump into the fun!"
FreeTimeInformScreenExpiredQuitCCUFText = "Can't right now? Don't worry, we'll save\nyour account for you! But hurry back! We can\nonly save your account for up to 1 week."
FreeTimeInformScreenPurchase = 'Subscribe Now!'
FreeTimeInformScreenFreePlay = 'Continue Free Trial'
FreeTimeInformScreenQuit = 'Quit'
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
CreateAccountScreenUserName = 'Account Name'
CreateAccountScreenPassword = 'Password'
CreateAccountScreenConfirmPassword = 'Confirm Password'
CreateAccountScreenFree = 'FREE'
CreateAccountScreenFreeTrialLength = 'To start your              %s-day trial,\nyou need to create an account.'
CreateAccountScreenInstructionsUsername = 'Type the account name you would like to use:'
CreateAccountScreenInstructionsPassword = 'Type a password:'
CreateAccountScreenInstructionsConfirmPassword = 'Just to be sure, type your password again:'
CreateAccountScreenInstructionsDob = 'Enter your date of birth:'
CreateAccountScreenCancel = 'Cancel'
CreateAccountScreenSubmit = 'Next'
CreateAccountScreenConnectionErrorSuffix = '.\n\nPlease try again later.'
CreateAccountScreenNoAccountName = 'Please enter an account name.'
CreateAccountScreenAccountNameTooShort = 'Your account name must be at least %s characters long. Please try again.'
CreateAccountScreenPasswordTooShort = 'Your password must be at least %s characters long. Please try again.'
CreateAccountScreenPasswordMismatch = 'The passwords you typed did not match. Please try again.'
CreateAccountScreenInvalidDob = 'Please enter your date of birth.'
CreateAccountScreenUserNameTaken = 'That user name is already taken. Please try again.'
CreateAccountScreenInvalidUserName = 'Invalid user name.\nPlease try again.'
CreateAccountScreenUserNameNotFound = 'User name not found.\nPlease try again or create a new account.'
CreateAccountScreenEmailInstructions = "Please enter your E-Mail Address.\nWhy? For two reasons:\n1.If you forget your password, we can send it to you!\n2.We can send you the latest information on\nDisney's Toontown Online."
CreateAccountScreenEmailInstructionsUnder13 = 'You have indicated that you are under 13 years old.\nTo create an account, we need the E-Mail address of a parent or guardian.'
CreateAccountScreenEmailConfirm = 'Just to be sure, please type the E-Mail Address again:'
CreateAccountScreenEmailPanelSubmit = 'Next'
CreateAccountScreenEmailPanelCancel = 'Cancel'
CreateAccountScreenInvalidEmail = 'Please enter the full E-Mail Address.'
CreateAccountScreenEmailMismatch = 'The E-Mail addresses that you entered did not match. Please try again.'
SecretFriendsInfoPanelOk = 'Ok'
SecretFriendsInfoPanelText = [
    '\nThe Secret Friends Feature\n\nThe Secret Friends feature enables a member to chat directly with another member within Disney\'s Toontown Online (the "Service") once the members establish a Secret Friends connection.  When your child attempts to use the Secret Friends feature, we will require that you indicate your consent to your child\'s use of this feature by entering your Parent Password.  Here is a detailed description of the process of creating a Secret Friends connection between members whom we will call "Sally" and "Mike."\n1. Sally\'s parent and Mike\'s parent each enable the Secret Friends feature by entering their respective Parent Passwords either (a) in the Account Options areas within the Service, or (b) when prompted within the game by a Parental Controls pop-up.\n2. Sally requests a Secret (described below) from within the Service.\n',
    "\n3. Sally's Secret is communicated to Mike outside of the Service. (Sally's Secret may be communicated to Mike either directly by Sally, or indirectly through Sally's disclosure of the Secret to another person.)\n4. Mike submits Sally's Secret to the Service within 48 hours of the time that Sally requested the Secret from the Service.\n5. The Service then notifies Mike that Sally has become Mike's Secret Friend.  The Service similarly notifies Sally that Mike has become Sally's Secret Friend.\n6. Sally and Mike can now chat directly with each other until either one chooses to terminate the other as a Secret Friend, or until the Secret Friends feature is disabled for either Sally or Mike by their respective parent.  The Secret Friends connection can thus be disabled anytime by either: (a) a member removing the Secret Friend from his or her friends list (as described in the Service); or, (b) the parent of that member disabling the Secret Friends feature by going to the Account Options area within the Service and following the steps set forth there.\n",
    "\nA Secret is a computer-generated random code assigned to a particular member. The Secret must be used to activate a Secret Friend connection within 48 hours of the time that the member requests the Secret; otherwise, the Secret expires and cannot be used.  Moreover, a single Secret can only be used to establish one Secret Friend connection.  To make additional Secret Friend connections, a member must request an additional Secret for each additional Secret Friend.\n\nSecret Friendships do not transfer.  For example, if Sally becomes a Secret Friend of Mike, and Mike becomes a Secret Friend of Jessica, Sally does not automatically become Jessica's Secret Friend.  In order for Sally and Jessica to become Secret Friends, one of them must request a new Secret from the Service and communicate it to the other.\n",
    '\nSecret Friends communicate with one another in a free-form interactive chat.  The content of this chat is directly entered by the participating member and is processed through the Service, which is operated by the Walt Disney Internet Group ("WDIG"), 506 2nd Avenue, Suite 2100, Seattle, WA 98104 (telephone (509) 742-4698; email ms_support@help.go.com).  While we advise members not to exchange personal information such as first and last names, e-mail addresses, postal addresses, or phone numbers while using Secret Friends, we cannot guarantee that such exchanges of personal information will not happen. Although the Secret Friends chat is automatically filtered for most bad words, it is not moderated or supervised by us.  If parents allow their children to use their account with the Secret Friends feature enabled, we encourage parents to supervise their children while they play in the Service.\n',
    "\nWDIG does not use the content of Secret Friends chat for any purpose other than communicating that content to the member's secret friend, and does not disclose that content to any third party except: (1) if required by law, for example, to comply with a court order or subpoena; (2) to enforce the Terms of Use applicable to the Service (which may be accessed on the home page of the Service); or, (3) to protect the safety and security of Members of the Service and the Service itself.  Upon request to WDIG, a child's parent can review and have deleted any Secret Friends chat content supplied by that child, provided that such chat content has not already been deleted by WDIG from its files.  In accordance with the Children's Online Privacy Protection Act, we are prohibited from conditioning, and do not condition, a child's participation in any activity (including Secret Friends) on the child's disclosing more personal information than is reasonably necessary to participate in such activity.\n",
    '\nIn addition, as noted above, we recognize the right of a parent to refuse to permit us to continue to allow a child to use the Secret Friends feature. By enabling the Secret Friends feature, you acknowledge that there are some risks inherent in the ability of members to chat with one another through the Secret Friends feature, and that you have been informed of, and agree to accept, any such risks.\n']
ParentPasswordScreenTitle = 'Parental Controls'
ParentPasswordScreenPassword = 'Create Parent Password'
ParentPasswordScreenConfirmPassword = 'Confirm Parent Password'
ParentPasswordScreenSubmit = 'Set Parent Password'
ParentPasswordScreenConnectionErrorSuffix = '.\nPlease try again later.'
ParentPasswordScreenPasswordTooShort = 'Your password must be at least %s characters long. Please try again.'
ParentPasswordScreenPasswordMismatch = 'The passwords you typed did not match. Please try again.'
ParentPasswordScreenConnectionProblemJustPaid = "There was a problem contacting the account server, but don't worry; your purchase did go through.\n\nYou will be asked to set your Parent Password again the next time you log in."
ParentPasswordScreenConnectionProblemJustLoggedIn = 'There was a problem contacting the account server. Please try again later.'
ParentPasswordScreenSecretFriendsMoreInfo = 'More Info'
ParentPasswordScreenInstructions = 'Please create a "Parent Password" for this account.  The Parent Password will later be required:\n\n  1.  When we ask you to consent to your child\'s/children\'s\n       use of certain interactive features of Toontown, such\n       as the "Secret Friends" feature.  For a complete\n       description of the Secret Friends feature, including\n       how it may enable your child/children to communicate\n       online with other members of Toontown, please click\n       the \'' + ParentPasswordScreenSecretFriendsMoreInfo + "' button below. Your consent is required\n       to enable this feature.\n\n\n  2. To update billing and account information from the\n       Toontown web page.\n"
ParentPasswordScreenAdvice = "Remember, keep this Parent Password confidential. Keeping this Parent Password confidential is your key to maintaining control over your child's/children's use of the interactive features of your account."
ParentPasswordScreenPrivacyPolicy = 'Privacy Policy'
ForgotPasswordScreenTitle = 'If you forgot your password, we can send it to you.'
ForgotPasswordScreenInstructions = 'Enter your account name OR the E-Mail address you gave us.'
ForgotPasswordScreenEmailEntryLabel = 'E-Mail Address'
ForgotPasswordScreenOr = 'OR'
ForgotPasswordScreenAcctNameEntryLabel = 'Account Name'
ForgotPasswordScreenSubmit = 'Submit'
ForgotPasswordScreenCancel = 'Cancel'
ForgotPasswordScreenEmailSuccess = "Your password has been sent to '%s'."
ForgotPasswordScreenEmailFailure = "E-Mail address not found: '%s'."
ForgotPasswordScreenAccountNameSuccess = 'Your password has been sent to the e-mail address that you provided when you created your account.'
ForgotPasswordScreenAccountNameFailure = 'Account not found: %s'
ForgotPasswordScreenNoEmailAddress = 'That account was created by someone under the age of 13, and does not have an email address. We cannot send your password to you.\n\nFeel free to create another account!'
ForgotPasswordScreenInvalidEmail = 'Please enter a valid email address.'
GuiScreenToontownUnavailable = 'Toontown appears to be temporarily unavailable, still trying...'
AchievePageTitle = 'Achievements\n(Coming Soon)'
BuildingPageTitle = 'Buildings\n(Coming Soon)'
InventoryPageTitle = 'Gags'
InventoryPageDeleteTitle = 'DELETE GAGS'
InventoryPageTrackFull = 'You have all the gags in the %s track.'
InventoryPagePluralPoints = 'You will get a new\n%(trackName)s gag when you\nget %(numPoints)s more %(trackName)s points.'
InventoryPageSinglePoint = 'You will get a new\n%(trackName)s gag when you\nget %(numPoints)s more %(trackName)s point.'
InventoryPageNoAccess = 'You do not have access to the %s track yet.'
MapPageBackToPlayground = 'Back to Playground'
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
OptionsPageSpeedChatStyleLabel = 'Speed Chat Color'
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
DisplaySettingsCancel = 'Cancel'
DisplaySettingsApplyWarning = 'When you press OK, the display settings will change.  If the new configuration does not display properly on your computer, the display will automatically return to its original configuration after %s seconds.'
DisplaySettingsAccept = 'Press OK to keep the new settings, or Cancel to revert.  If you do not press anything, the settings will automatically revert back in %s seconds.'
DisplaySettingsRevertUser = 'Your previous display settings have been restored.'
DisplaySettingsRevertFailed = 'The selected display settings do not work on your computer.  Your previous display settings have been restored.'
TrackPageTitle = 'Gag Track Training'
TrackPageSubtitle = 'Complete ToonTasks to learn how to use new Gags!'
TrackPageTraining = 'You are training to use %s Gags.\nWhen you complete all 16 tasks you\nwill be able to use %s Gags in battle.'
TrackPageClear = 'You are not training any Gag Tracks now.'
TrackPageFilmTitle = '%s\nTraining\nFilm'
QuestPageToonTasks = 'ToonTasks'
QuestPageChoose = 'Choose'
QuestPageDestination = '%s\n%s\n%s'
QuestPageNameAndDestination = '%s\n%s\n%s\n%s'
QuestPosterHQOfficer = 'HQ Officer'
QuestPosterHQBuildingName = 'Toon HQ'
QuestPosterHQStreetName = 'Any Street'
QuestPosterHQLocationName = 'Any Neighborhood'
QuestPosterTailor = 'Tailor'
QuestPosterTailorBuildingName = 'Clothing Store'
QuestPosterTailorStreetName = 'Any Playground'
QuestPosterTailorLocationName = 'Any Neighborhood'
QuestPosterPlayground = 'In the playground'
QuestPosterAnywhere = 'Anywhere'
QuestPosterAuxTo = 'to:'
QuestPosterAuxFrom = 'from:'
QuestPosterAuxFor = 'for:'
QuestPosterAuxOr = 'or:'
QuestPosterAuxReturnTo = 'Return to:'
QuestPosterLocationIn = ' in '
QuestPosterLocationOn = ' on '
QuestPosterFun = 'Just for fun!'
ShardPageTitle = 'Districts'
ShardPageHelp = 'Each District is a copy of the Toontown world. You are currently in the "%s" District.  To move to a new District, click on its name.'
ShardPageHelpDisabled = 'Each District is a copy of the Toontown world. You are currently in the "%s" District.'
ShardPagePopulationShard = '%s Population:\n%d'
ShardPagePopulationTotal = 'Total Toontown Population:\n%d'
ShardPageScrollTitle = 'Name            Population'
SuitPageTitle = Cog + ' Gallery'
SuitPageMystery = DialogQuestion + DialogQuestion + DialogQuestion
FishNames = (('Leopard Fish', 'Leopard Fishes'), ('Rainbow Trout', 'Rainbow Trouts'), ('Carr Tuna', 'Carr Tuna'), ('Whole Emackerel', 'Whole Emackerels'), ('One-Eyed Amberjack', 'One-Eyed Amberjacks'), ('Fred Snapper', 'Fred Snappers'), ('Rock Grouper', 'Rock Groupers'), ('Seasick Bass', 'Seasick Bass'), ('Front Perch', 'Front Perches'), ('Mullet Head', 'Mullet Heads'), ('Out-of-the Bluefish', 'Out-of-the Bluefishes'), ('Forsale Fish', 'Forsale Fishes'), ('Would-be Kingfish', 'Would-be Kingfishes'), ('Doggone Catfish', 'Doggone Catfishes'), ('TransAtlantic Cod', 'TransAtlantic Cod'), ('Old Shoe', 'Old Shoes'), ('Old Tire', 'Old Tires'))
FishPageTitle = 'Fish Tank'
FishPageOverflow = 'You have too many fish now!\n Pick one below to release:'
FishPageOldFish = 'You already have:'
FishPageVerify = 'Are you sure you want to release %s?'
QuestChoiceGuiCancel = 'Cancel'
TrackChoiceGuiChoose = 'Choose'
TrackChoiceGuiCancel = 'Cancel'
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
EmoteList = [
    'Wave',
    'Happy',
    'Sad',
    'Angry',
    'Sleepy',
    'Shrug',
    'Dance',
    'Wink',
    'Bored',
    'Applause',
    'Surprised',
    'Confused',
    'Taunt',
    'Bow',
    'Really sad',
    'Hello',
    'Goodbye',
    'Yes',
    'No',
    'OK']
EmoteWhispers = [
    '%s waves.',
    '%s is happy.',
    '%s is sad.',
    '%s is angry.',
    '%s is sleepy.',
    '%s shrugs.',
    '%s dances.',
    '%s winks.',
    '%s is bored.',
    '%s applauds.',
    '%s is surprised.',
    '%s is confused.',
    '%s taunts you.',
    '%s bows to you.',
    '%s is really sad.',
    "%s says 'Hello'.",
    "%s says 'Goodbye'.",
    "%s says 'Yes'.",
    "%s says 'No'.",
    "%s says 'OK'."]
EmoteFuncDict = {
    'wave': 0,
    'happy': 1,
    'sad': 2,
    'angry': 3,
    'sleepy': 4,
    'laugh': 5,
    'dance': 6,
    'wink': 7,
    'bored': 8,
    'applause': 9,
    'surprised': 10,
    'confused': 11,
    'taunt': 12,
    'bow': 13,
    'really sad': 14,
    'hello': 15,
    'goodbye': 16,
    'yes': 17,
    'no': 18,
    'ok': 19 }
SuitBaseNameWithLevel = '%(name)s\n%(dept)s\nLevel %(level)s'
SuitBrushOffs = {
    'f': [
        "I'm late for a meeting"],
    'p': [
        'Push off'],
    'ym': [
        'Yes Man says NO'],
    None: [
        "It's my day off",
        "I believe you're in the wrong office",
        'Have your people call my people',
        "You're in no position to meet with me",
        'Talk to my assistant'] }
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
NPCForceAcknowledgeMessage = "You must ride the trolley before leaving.\n\n\n\n\nYou can find the trolley next to Goofy's Gag Shop."
NPCForceAcknowledgeMessage2 = 'Good job completing your trolley quest!\nVisit Toon Headquarters to claim your reward.\n\n\n\n\n\nToon Headquarters is located near the center of the playground.'
NPCForceAcknowledgeMessage3 = "Remember to ride the trolley.\n\n\n\nYou can find the trolley next to Goofy's Gag Shop."
NPCForceAcknowledgeMessage4 = "Congratulations!  You've completed your first Toontask!\n\n\n\n\nVisit Toon Headquarters to claim your reward."
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
BattleGlobalAvPropStrings = (('Feather', 'Megaphone', 'Lipstick', 'Bamboo Cane', 'Pixie Dust', 'Juggling Balls'), ('Banana Peel', 'Rake', 'Marbles', 'Quicksand', 'Trapdoor', 'TNT'), ('$1 bill', 'Small Magnet', '$5 bill', 'Big Magnet', '$10 bill', 'Hypno-goggles'), ('Bike Horn', 'Whistle', 'Bugle', 'Aoogah', 'Elephant Trunk', 'Foghorn'), ('Cupcake', 'Fruit Pie Slice', 'Cream Pie Slice', 'Whole Fruit Pie', 'Whole Cream Pie', 'Birthday Cake'), ('Squirting Flower', 'Glass of Water', 'Squirt Gun', 'Seltzer Bottle', 'Fire Hose', 'Storm Cloud'), ('Flower Pot', 'Sandbag', 'Anvil', 'Big Weight', 'Safe', 'Grand Piano'))
BattleGlobalAvPropStringsSingular = (('a Feather', 'a Megaphone', 'a Lipstick', 'a Bamboo Cane', 'a Pixie Dust', 'a set of Juggling Balls'), ('a Banana Peel', 'a Rake', 'a set of Marbles', 'a patch of Quicksand', 'a Trapdoor', 'a TNT'), ('a $1 bill', 'a Small Magnet', 'a $5 bill', 'a Big Magnet', 'a $10 bill', 'a pair of Hypno-goggles'), ('a Bike Horn', 'a Whistle', 'a Bugle', 'an Aoogah', 'an Elephant Trunk', 'a Foghorn'), ('a Cupcake', 'a Fruit Pie Slice', 'a Cream Pie Slice', 'a Whole Fruit Pie', 'a Whole Cream Pie', 'a Birthday Cake'), ('a Squirting Flower', 'a Glass of Water', 'a Squirt Gun', 'a Seltzer Bottle', 'a Fire Hose', 'a Storm Cloud'), ('a Flower Pot', 'a Sandbag', 'an Anvil', 'a Big Weight', 'a Safe', 'a Grand Piano'))
BattleGlobalAvPropStringsPlural = (('Feathers', 'Megaphones', 'Lipsticks', 'Bamboo Canes', 'Pixie Dusts', 'sets of Juggling Balls'), ('Banana Peels', 'Rakes', 'sets of Marbles', 'patches of Quicksand', 'Trapdoors', 'TNTs'), ('$1 bills', 'Small Magnets', '$5 bills', 'Big Magnets', '$10 bills', 'pairs of Hypno-goggles'), ('Bike Horns', 'Whistles', 'Bugles', 'Aoogahs', 'Elephant Trunks', 'Foghorns'), ('Cupcakes', 'Fruit Pie Slices', 'Cream Pie Slices', 'Whole Fruit Pies', 'Whole Cream Pies', 'Birthday Cakes'), ('Squirting Flowers', 'Glasses of Water', 'Squirt Guns', 'Seltzer Bottles', 'Fire Hoses', 'Storm Clouds'), ('Flower Pots', 'Sandbags', 'Anvils', 'Big Weights', 'Safes', 'Grand Pianos'))
BattleGlobalAvTrackAccStrings = ('Medium', 'Perfect', 'Low', 'High', 'Medium', 'High', 'Low')
AttackMissed = 'MISSED'
GlobalStreetNames = {
    20000: ('to', 'Tutorial Terrace'),
    1000: ('to the', 'Playground'),
    1100: ('to', 'Barnacle Boulevard'),
    1200: ('to', 'Seaweed Street'),
    1300: ('to', 'Lighthouse Lane'),
    2000: ('to the', 'Playground'),
    2100: ('to', 'Silly Street'),
    2200: ('to', 'Loopy Lane'),
    2300: ('to', 'Punchline Place'),
    3000: ('to the', 'Playground'),
    3100: ('to', 'Walrus Way'),
    3200: ('to', 'Sleet Street'),
    4000: ('to the', 'Playground'),
    4100: ('to', 'Alto Avenue'),
    4200: ('to', 'Baritone Boulevard'),
    4300: ('to', 'Tenor Terrace'),
    5000: ('to the', 'Playground'),
    5100: ('to', 'Elm Street'),
    5200: ('to', 'Maple Street'),
    9000: ('to the', 'Playground'),
    9100: ('to', 'Lullaby Lane') }
DonaldsDock = ('to', "Donald's Dock")
ToontownCentral = ('to', 'Toontown Central')
TheBrrrgh = ('to', 'The Brrrgh')
MinniesMelodyland = ('to', "Minnie's Melodyland")
DaisyGardens = ('to', 'Daisy Gardens')
ConstructionZone = ('to the', 'Construction Zone')
FunnyFarm = ('to the', 'Funny Farm')
GoofyStadium = ('to', 'Goofy Stadium')
DonaldsDreamland = ('to', "Donald's Dreamland")
BossbotHQ = ('to the', 'Bossbot HQ')
SellbotHQ = ('to the', 'Sellbot HQ')
CashbotHQ = ('to the', 'Cashbot HQ')
LawbotHQ = ('to the', 'Lawbot HQ')
Tutorial = ('to the', 'Toon-torial')
MyEstate = ('to', 'your house')
LoaderLabel = 'Loading...'
HeadingToHood = 'Heading %s %s...'
HeadingToYourEstate = 'Heading to your estate...'
HeadingToEstate = "Heading to %s's estate..."
HeadingToFriend = "Heading to %s's friend's estate..."
HeadingToPlayground = 'Heading to the Playground...'
HeadingToStreet = 'Heading %s %s...'
ToontownDialogOK = 'OK'
ToontownDialogCancel = 'Cancel'
TownBattleRun = 'Run all the way back to the playground?'
TownBattleChooseAvatarToonTitle = 'WHICH TOON?'
TownBattleChooseAvatarCogTitle = 'WHICH ' + string.upper(Cog) + '?'
TownBattleChooseAvatarBack = 'BACK'
TownBattleSOSNoFriends = 'No friends to call!'
TownBattleSOSWhichFriend = 'Call which friend?'
TownBattleSOSBack = 'BACK'
TownBattleToonSOS = 'SOS'
TownBattleUndecided = '?'
TownBattleHealthText = '%(hitPoints)s/%(maxHit)s'
TownBattleWaitTitle = 'Waiting for\nother players...'
TownSoloBattleWaitTitle = 'Please wait...'
TownBattleWaitBack = 'BACK'
TrolleyHFAMessage = 'You may not board the trolley until your laffmeter is smiling.'
TrolleyTFAMessage = 'You may not board the trolley until ' + Mickey + ' says so.'
TrolleyHopOff = 'Hop off'
FishingExit = 'Done'
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
FishingBrokeHeader = "You're out of jellybeans!"
FishingBroke = "You don't have anything to put on your hook!  Go ride on the trolley and earn some more jellybeans."
TutorialGreeting1 = 'Hi %s!'
TutorialGreeting2 = 'Hi %s!\nCome over here!'
TutorialGreeting3 = 'Hi %s!\nCome over here!\nUse the arrow keys!'
TutorialMickeyWelcome = 'Welcome to Toontown!'
TutorialFlippyIntro = 'Let me introduce you to my friend ' + Flippy + '...'
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
TutorialBodyClick3 = 'To make friends with ' + Flippy + ', click on him...'
TutorialHandleBodyClickSuccess = 'Good Job!'
TutorialHandleBodyClickFail = 'Not quite. Try clicking right on ' + Flippy + '...'
TutorialFriendsButton = "Now click the 'Friends' button under " + Flippy + "'s picture in the right hand corner."
TutorialHandleFriendsButton = "And then click on the 'Yes' button.."
TutorialOK = 'OK'
TutorialYes = 'Yes'
TutorialNo = 'No'
TutorialFriendsPrompt = 'Would you like to make friends with ' + Flippy + '?'
TutorialFriendsPanelMickeyChat = Flippy + " has agreed to be your friend. Click 'Ok' to finish up."
TutorialFriendsPanelYes = Flippy + ' said yes!'
TutorialFriendsPanelNo = "That's not very friendly!"
TutorialFriendsPanelCongrats = 'Congratulations! You made your first friend.'
TutorialFlippyChat1 = 'Come see me when you are ready for your first ToonTask!'
TutorialFlippyChat2 = "I'll be in ToonHall!"
TutorialAllFriendsButton = 'You can view all your friends by clicking the friends button. Try it out...'
TutorialEmptyFriendsList = 'Right now your list is empty because ' + Flippy + " isn't a real player."
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
TutorialBye3 = 'Go see ' + Flippy + ' when you are done!'
TutorialForceAcknowledgeMessage = 'You are going the wrong way! Go find ' + Mickey + '!'
GlobalQuickTalkerName = 'SpeedChat'
QTLocalizationError = 'Error: the localized SpeedChat menu no longer matches the English SpeedChat menu:\n'
QTLocalizationErrorLength = QTLocalizationError + 'these lists have different lengths:\n%s\n%s'
QTLocalizationErrorType = QTLocalizationError + 'these entries are of different types:\n%s\n%s'
QTMenuEmotions = 'EMOTIONS'
QTMenuCustom = 'MY PHRASES'
QTMenuHello = 'HELLO'
QTMenuBye = 'GOODBYE'
QTMenuHappy = 'HAPPY'
QTMenuSad = 'SAD'
QTMenuFriendly = 'FRIENDLY'
QTMenuSorry = 'SORRY'
QTMenuStinky = 'STINKY'
QTMenuPlaces = 'PLACES'
QTMenuToontasks = 'TOONTASKS'
QTMenuBattle = 'BATTLE'
QTMenuGagShop = 'GAG SHOP'
QTFriendlyYou = 'You'
QTFriendlyILike = 'I like'
QTPlacesLetsGo = "Let's go"
QTToontasksMyTasks = 'MY TASKS'
QTToontasksYouShouldChoose = 'I think you should choose'
QTBattleLetsUse = "Let's use"
QTHelloEntries = [
    [
        'Hi!',
        0],
    [
        'Hello!',
        0],
    [
        'Hi there!',
        0],
    [
        'Hey!',
        0],
    [
        'Howdy!',
        0],
    [
        'Hi everybody!',
        0],
    'Welcome to Toontown!',
    "What's up?",
    'How are you doing?',
    'Hello?']
QTByeEntries = [
    [
        'Bye!',
        0],
    [
        'Later!',
        0],
    [
        'See ya!',
        0],
    'Have a nice day!',
    'Have fun!',
    'Good luck!',
    "I'll be right back.",
    'I need to go.']
QTHappyEntries = [
    [
        ':-)',
        1],
    [
        'Yay!',
        1],
    [
        'Hooray!',
        1],
    'Cool!',
    [
        'Woo hoo!',
        1],
    'Yeah!',
    'Ha ha!',
    'Hee hee!',
    'Wow!',
    'Great!',
    'Whee!',
    'Oh boy!',
    [
        'Whoopee!',
        1],
    [
        'Yippee!',
        1],
    [
        'Yee hah!',
        1],
    'Toontastic!']
QTSadEntries = [
    [
        ':-(',
        2],
    [
        'Oh no!',
        2],
    [
        'Uh oh!',
        2],
    'Rats!',
    'Drat!',
    'Ouch!',
    'Oof!',
    'No!!!',
    'Yikes!',
    'Huh?',
    'I need more Laff points.']
QTFriendlyYouEntries = [
    'You look nice.',
    'You are awesome!',
    'You rock!',
    'You are a genius!']
QTFriendlyILikeEntries = [
    'I like your name.',
    'I like your look.',
    'I like your shirt.',
    'I like your skirt.',
    'I like your shorts.',
    'I like this game!']
QTFriendlyEntries = [
    'Thanks!',
    'No problem.',
    "You're welcome!",
    'Any time!',
    'No thank you.',
    'Good teamwork!',
    'That was fun!',
    'Please be my friend!',
    "Let's work together!",
    'You guys are great!',
    'Are you new here?',
    'Did you win?',
    'I think this is too risky for you.',
    'Would you like some help?',
    'Can you help me?']
QTSorryEntries = [
    'Sorry!',
    'Oops!',
    "Sorry, I'm busy fighting Cogs!",
    "Sorry, I'm busy getting Jellybeans!",
    "Sorry, I'm busy completing a ToonTask!",
    'Sorry, I had to leave unexpectedly.',
    'Sorry, I was delayed.',
    "I couldn't wait any longer.",
    "I can't.",
    [
        "I can't understand you.",
        5],
    'Use the ' + GlobalQuickTalkerName + '.']
QTStinkyEntries = [
    [
        'Hey!',
        3],
    [
        'Please go away!',
        3],
    [
        'Stop that!',
        3],
    [
        "That wasn't nice!",
        3],
    "Don't be mean!",
    [
        'You stink!',
        3],
    "That's a bug.",
    'Send a bug report.',
    "I'm stuck because of a bug."]
QTPlacesLetsGoEntries = [
    "Let's go on the trolley!",
    "Let's go back to the playground!",
    "Let's go to my house!",
    "Let's go fight the " + Cogs + '!',
    "Let's go take over a " + Cog + ' building!',
    "Let's go in the elevator!",
    "Let's go to Toontown Central!",
    "Let's go to Donald's Dock!",
    "Let's go to Minnie's Melodyland!",
    "Let's go to Daisy Gardens!",
    "Let's go to The Brrrgh!",
    "Let's go to Donald's Dreamland!"]
QTPlacesEntries = [
    "Let's go!",
    'Can you teleport to me?',
    'Can you come to my house?',
    'Shall we go?',
    'Where should we go?',
    'Which way?',
    'This way.',
    'Follow me.',
    'Wait for me!',
    "Let's wait for my friend.",
    "Let's find other toons.",
    'Wait here.',
    'Wait a minute.',
    'Meet here.']
QTYouShouldChooseEntries = [
    'I think you should choose Toon-up.',
    'I think you should choose Sound.',
    'I think you should choose Drop.',
    'I think you should choose Trap.',
    'I think you should choose Lure.']
QTToontasksEntries = [
    'What ToonTask are you working on?',
    "Let's work on that.",
    "This isn't what I'm looking for.",
    "I'm going to look for that.",
    "It isn't on this street.",
    "I haven't found it yet."]
QTBattleLetsUseEntries = [
    "Let's use toon-up!",
    "Let's use trap!",
    "Let's use lure!",
    "Let's use sound!",
    "Let's use throw!",
    "Let's use squirt!",
    "Let's use drop!"]
QTBattleEntries = [
    'Hurry!',
    'Nice shot!',
    'Nice gag!',
    'Missed me!',
    'You did it!',
    'We did it!',
    'Bring it on!',
    'Piece of cake!',
    'That was easy!',
    'Run!',
    'Help!',
    'Phew!',
    'We are in trouble.',
    'I need more gags.',
    'I need a Toon-Up.']
QTGagShopEntries = [
    'I have enough gags.',
    'I need more jellybeans.',
    'Me too.',
    'Hurry up!',
    'One more?',
    'Play again?',
    "Let's play again."]
QTTopEntries = [
    [
        'Yes',
        17],
    [
        'No',
        18],
    'Ok']
QTYes = 'Yes'
QTNo = 'No'
QTOk = 'Ok'
QTPopupEmoteMessage = 'You do not have access\n to this emotion yet'
QTPopupEmoteMessageOK = 'OK'
QTQuestNodeNeedATask = 'I need to get a ToonTask.'
CustomQTStrings = {
    10: 'Oh, well.',
    20: 'Why not?',
    30: 'Naturally!',
    40: "That's the way to do it.",
    50: 'Right on!',
    60: 'What up?',
    70: 'But of course!',
    80: 'Bingo!' }
PlaygroundDeathAckMessage = 'The ' + Cogs + ' took all your gags!\n\nYou are sad. You may not leave the playground until you are happy.'
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
PatternGameTitle = 'Match ' + Minnie
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
MakeAToonCancel = 'Cancel'
MakeAToonNext = 'Next'
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
NameShopNameMaster = 'NameMasterEnglish.txt'
NameShopPay = 'Subscribe Now!'
NameShopPlay = 'Free Trial'
NameShopOnlyPaid = 'Only paid users\nmay name their toons.\nUntil you subscribe\nyour name will be\n'
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
    'Pink']
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
RemoveTrophy = 'Toon HQ: The ' + Cogs + ' took over one of the buildings you rescued!'
STOREOWNER_TOOKTOOLONG = 'Need more time to think?'
STOREOWNER_GOODBYE = 'See you later!'
STOREOWNER_NEEDJELLYBEANS = 'You need to ride the Trolley to get some Jellybeans.'
STOREOWNER_GREETING = 'Choose what you want to buy.'
STOREOWNER_BROWSING = 'You can browse, but you need a clothing ticket to buy.'
STOREOWNER_NOCLOTHINGTICKET = 'You need a clothing ticket to shop for clothes.'
STOREOWNER_NOROOM = 'Hmm...you might want to make room in your closet before you buy new clothes.\n'
STOREOWNER_CONFIRM_LOSS = 'Your closet is full.  You will lose the clothes you were wearing.'
STOREOWNER_OK = 'OK'
STOREOWNER_CANCEL = 'Cancel'
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
QuestScript101_1 = 'These are COGS. They are robots that are trying to take over Toontown.'
QuestScript101_2 = 'There are many different kinds of COGS and...'
QuestScript101_3 = '...they turn happy Toon buildings...'
QuestScript101_4 = '...into ugly Cog buildings!'
QuestScript101_5 = "But COGS can't take a joke!"
QuestScript101_6 = 'A good gag will stop them.'
QuestScript101_7 = 'There are lots of gags, but take these to start.'
QuestScript101_8 = 'Oh! You also need a Laff Meter!'
QuestScript101_9 = "If your Laff Meter gets too low, you'll be sad!"
QuestScript101_10 = 'A happy toon is a healthy toon!'
QuestScript101_11 = "OH NO! There's a COG outside my shop!"
QuestScript101_12 = 'HELP ME, PLEASE! Defeat that COG!'
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
QuestScript110_11 = 'Return to ToonHQ when you are done. Bye!'
QuestScriptTutorialBlocker_1 = 'Why, hello there!'
QuestScriptTutorialBlocker_2 = 'Hello?'
QuestScriptTutorialBlocker_3 = "Oh! You don't know how to use SpeedChat!"
QuestScriptTutorialBlocker_4 = 'Click on the button to say something.'
QuestScriptTutorialBlocker_5 = 'Very good!\x7Where you are going there are many toons to talk to.'
QuestScriptTutorialBlocker_6 = "If you want to chat with your friends using the keyboard, there's another button you can use."
QuestScriptTutorialBlocker_7 = 'It\'s called the "Chat" button. You need to be an official citizen of Toontown to use it.'
QuestScriptTutorialBlocker_8 = 'Good luck! See you later!'
QuestScript120_1 = "Good job finding the trolley!\x7By the way, have you met Banker Bob?\x7He has quite a sweet tooth.\x7Why don't you introduce yourself by taking him this candy bar as a gift."
QuestScript120_2 = 'Banker Bob is over in the Toontown Bank.'
QuestScript121_1 = "Yum, thank you for the Candy Bar.\x7Say, if you can help me, I'll give you a reward.\x7Those Cogs stole the keys to my safe. Defeat Cogs to find a stolen key.\x7When you find a key, bring it back to me."
QuestScript130_1 = 'Good job finding the trolley!\x7By the way, I received a package for Professor Pete today.\x7It must be his new chalk he ordered.\x7Can you please take it to him?\x7He is over in the school house.'
QuestScript131_1 = 'Oh, thanks for the chalk.\x7What?!?\x7Those Cogs stole my blackboard. Defeat Cogs to find my stolen blackboard.\x7When you find it, bring it back to me.'
QuestScript140_1 = "Good job finding the trolley!\x7By the way, I have this friend, Librarian Larry, who is quite a book worm.\x7I picked this book up for him last time I was over in Donald's Dock.\x7Could you take it over to him, he is usually in the Library."
QuestScript141_1 = 'Oh, yes, this book almost completes my collection.\x7Let me see...\x7Uh oh...\x7Now where did I put my glasses?\x7I had them just before those Cogs took over my building.\x7Defeat Cogs to find my stolen glasses.\x7When you find them, bring them back to me for a reward.'
QuestScript150_1 = 'Oh... this next task might be too hard for you to do alone!'
QuestScript150_2 = 'To make friends, find another player, and use the New Friend button.'
QuestScript150_3 = 'Once you have made a friend, come back here.'
QuestScript150_4 = 'Some tasks are too difficult to do alone!'
MissingKeySanityCheck = 'Ignore me'
FurnitureNames = {
    100: 'Chair',
    200: 'Bed',
    210: 'Bed',
    220: 'Bathtub Bed',
    300: 'Player Piano',
    310: 'Pipe Organ',
    400: 'Fireplace',
    410: 'Fireplace',
    420: 'Round Fireplace',
    500: 'Wardrobe',
    510: 'Wardrobe' }
TutorialHQOfficerName = 'HQ Harry'
NPCToonNames = {
    20000: 'Tutorial Tom',
    999: 'Toon Tailor',
    1000: 'Toon HQ',
    20001: 'Flippy',
    2001: 'Flippy',
    2002: 'Banker Bob',
    2003: 'Professor Pete',
    2004: 'Tammy the Tailor',
    2005: 'Librarian Larry',
    2006: 'Clerk Clark',
    2011: 'Clerk Clara',
    2007: 'HQ Officer',
    2008: 'HQ Officer',
    2009: 'HQ Officer',
    2010: 'HQ Officer',
    2101: 'Dentist Daniel',
    2102: 'Sheriff Sherry',
    2103: 'Sneezy Kitty',
    2104: 'HQ Officer',
    2105: 'HQ Officer',
    2106: 'HQ Officer',
    2107: 'HQ Officer',
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
    2201: 'Postmaster Pete',
    2202: 'Shirley U. Jest',
    2203: 'HQ Officer',
    2204: 'HQ Officer',
    2205: 'HQ Officer',
    2206: 'HQ Officer',
    2207: 'Willy Wiseacre',
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
    2301: 'Dr. Pulyurleg',
    2302: 'Professor Wiggle',
    2303: 'Nurse Nancy',
    2304: 'HQ Officer',
    2305: 'HQ Officer',
    2306: 'HQ Officer',
    2307: 'HQ Officer',
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
    1001: 'Clerk Willy',
    1002: 'Clerk Billy',
    1003: 'HQ Officer',
    1004: 'HQ Officer',
    1005: 'HQ Officer',
    1006: 'HQ Officer',
    1007: 'Longjohn Leroy',
    1101: 'Billy Budd',
    1102: 'Captain Carl',
    1103: 'Fishy Frank',
    1104: 'Doctor Squall',
    1105: 'Admiral Hook',
    1106: 'Mrs. Starch',
    1107: 'Cal Estenicks',
    1108: 'HQ Officer',
    1109: 'HQ Officer',
    1110: 'HQ Officer',
    1111: 'HQ Officer',
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
    1201: 'Barnacle Barbara',
    1202: 'Art',
    1203: 'Ahab',
    1204: 'Rocky Shores',
    1205: 'HQ Officer',
    1206: 'HQ Officer',
    1207: 'HQ Officer',
    1208: 'HQ Officer',
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
    1301: 'Alice',
    1302: 'Melville',
    1303: 'Claggart',
    1304: 'Svetlana',
    1305: 'HQ Officer',
    1306: 'HQ Officer',
    1307: 'HQ Officer',
    1308: 'HQ Officer',
    1309: 'Seafoam',
    1310: 'Ted Tackle',
    1311: 'Topsy Turvey',
    1312: 'Ethan Keel',
    1313: 'Willy Wake',
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
    3001: 'Betty Freezes',
    3002: 'HQ Officer',
    3003: 'HQ Officer',
    3004: 'HQ Officer',
    3005: 'HQ Officer',
    3006: 'Clerk Lenny',
    3007: 'Clerk Penny',
    3008: 'Warren Bundles',
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
    3115: 'HQ Officer',
    3116: 'HQ Officer',
    3117: 'HQ Officer',
    3118: 'HQ Officer',
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
    3213: 'HQ Officer',
    3214: 'HQ Officer',
    3215: 'HQ Officer',
    3216: 'HQ Officer',
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
    4001: 'Molly Molloy',
    4002: 'HQ Officer',
    4003: 'HQ Officer',
    4004: 'HQ Officer',
    4005: 'HQ Officer',
    4006: 'Clerk Doe',
    4007: 'Clerk Ray',
    4008: 'Tailor Harmony',
    4101: 'Tom',
    4102: 'Fifi',
    4103: 'Dr. Fret',
    4104: 'HQ Officer',
    4105: 'HQ Officer',
    4106: 'HQ Officer',
    4107: 'HQ Officer',
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
    4201: 'Tina',
    4202: 'Barry',
    4203: 'Lumber Jack',
    4204: 'HQ Officer',
    4205: 'HQ Officer',
    4206: 'HQ Officer',
    4207: 'HQ Officer',
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
    4301: 'Yuki',
    4302: 'Anna',
    4303: 'Leo',
    4304: 'HQ Officer',
    4305: 'HQ Officer',
    4306: 'HQ Officer',
    4307: 'HQ Officer',
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
    5001: 'HQ Officer',
    5002: 'HQ Officer',
    5003: 'HQ Officer',
    5004: 'HQ Officer',
    5005: 'Clerk Peaches',
    5006: 'Clerk Herb',
    5007: 'Bonnie Blossom',
    5101: 'Artie',
    5102: 'Susan',
    5103: 'Bud',
    5104: 'Flutterby',
    5105: 'Jack',
    5106: 'Barber Bjorn',
    5107: 'Postman Felipe',
    5108: 'Innkeeper Janet',
    5109: 'HQ Officer',
    5110: 'HQ Officer',
    5111: 'HQ Officer',
    5112: 'HQ Officer',
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
    5201: 'Jake',
    5202: 'Cynthia',
    5203: 'Lisa',
    5204: 'Bert',
    5205: 'Dan D. Lion',
    5206: 'Vine Green',
    5207: 'Sofie Squirt',
    5208: 'Samantha Spade',
    5209: 'HQ Officer',
    5210: 'HQ Officer',
    5211: 'HQ Officer',
    5212: 'HQ Officer',
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
    5223: 'Wet Willy',
    5224: 'Uncle Bumpkin',
    5225: 'Pamela Puddle',
    5226: 'Pete Moss',
    5227: 'Begonia Biddlesmore',
    5228: 'Digger Mudhands',
    9001: "Snoozin' Susan",
    9002: 'Sleeping Tom',
    9003: 'Drowsy Dennis',
    9004: 'HQ Officer',
    9005: 'HQ Officer',
    9006: 'HQ Officer',
    9007: 'HQ Officer',
    9008: 'Clerk Jill',
    9009: 'Clerk Phil',
    9010: 'Worn Out Waylon',
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
    9132: 'HQ Officer',
    9133: 'HQ Officer',
    9134: 'HQ Officer',
    9135: 'HQ Officer' }
zone2TitleDict = {
    2513: 'Toon Hall',
    2514: 'Toontown Bank',
    2516: 'Toontown School House',
    2518: 'Toontown Library',
    2519: 'Gag Shop',
    2520: 'Toon HQ',
    2521: 'Clothing Shop',
    2601: 'All Smiles Tooth Repair',
    2602: '',
    2603: 'One-Liner Miners',
    2604: 'Hogwash & Dry',
    2605: 'Toontown Sign Factory',
    2606: '',
    2607: 'Jumping Beans',
    2610: 'Dr. Tom Foolery',
    2611: '',
    2616: "Weird Beard's Disguise Shop",
    2617: 'Silly Stunts',
    2618: 'All That Razz',
    2621: 'Paper Airplanes',
    2624: 'Happy Hooligans',
    2625: 'House of Bad Pies',
    2626: "Jesse's Joke Repair",
    2629: "The Laughin' Place",
    2632: 'Clown Class',
    2633: 'Tee-Hee Tea Shop',
    2638: 'Toontown Playhouse',
    2639: 'Monkey Tricks',
    2643: 'Canned Bottles',
    2644: 'Impractical Jokes',
    2649: 'All Fun and Games Shop',
    2652: '',
    2653: '',
    2654: 'Laughing Lessons',
    2655: 'Funny Money Savings & Loan',
    2656: 'Used Clown Cars',
    2657: "Frank's Pranks",
    2659: 'Joy Buzzers to the World',
    2660: 'Tickle Machines',
    2661: 'Daffy Taffy',
    2662: 'Dr. I.M. Euphoric',
    2663: 'Toontown Cinerama',
    2664: 'The Merry Mimes',
    2665: "Mary's Go Round Travel Agency",
    2666: 'Laughing Gas Station',
    2667: 'Happy Times',
    2669: "Muldoon's Maroon Balloons",
    2670: 'Soup Forks',
    2671: '',
    2701: '',
    2704: 'Movie Multiplex',
    2705: "Wiseacre's Noisemakers",
    2708: 'Blue Glue',
    2711: 'Toontown Post Office',
    2712: 'Chortle Cafe',
    2713: 'Laughter Hours Cafe',
    2714: 'Kooky CinePlex',
    2716: 'Soup and Crack Ups',
    2717: 'Bottled Cans',
    2720: 'Crack Up Auto Repair',
    2725: '',
    2727: 'Seltzer Bottles and Cans',
    2728: 'Vanishing Cream',
    2729: '14 Karat Goldfish',
    2730: 'News for the Amused',
    2731: '',
    2732: 'Spaghetti and Goofballs',
    2733: 'Cast Iron Kites',
    2734: 'Suction Cups and Saucers',
    2735: 'The Kaboomery',
    2739: "Sidesplitter's Mending",
    2740: 'Used Firecrackers',
    2741: '',
    2742: '',
    2743: 'Ragtime Dry Cleaners',
    2744: '',
    2747: 'Visible Ink',
    2748: 'Jest for Laughs',
    2801: 'Sofa Whoopee Cushions',
    2802: 'Inflatable Wrecking Balls',
    2803: 'The Karnival Kid',
    2804: 'Dr. Pulyurleg, Chiropractor',
    2805: '',
    2809: 'The Punch Line Gym',
    2814: 'Toontown Theatre',
    2818: 'The Flying Pie',
    2821: '',
    2822: 'Rubber Chicken Sandwiches',
    2823: 'Sundae Funnies Ice Cream',
    2824: 'Punchline Movie Palace',
    2829: 'Phony Baloney',
    2830: "Zippy's Zingers",
    2831: "Professor Wiggle's House of Giggles",
    2832: '',
    2833: '',
    2834: 'Funny Bone Emergency Room',
    2836: '',
    2837: 'Hardy Harr Seminars',
    2839: 'Barely Palatable Pasta',
    2841: '',
    1506: 'Gag Shop',
    1507: 'Toon Headquarters',
    1508: 'Clothing Shop',
    1602: 'Used Life Preservers',
    1604: 'Wetsuit Dry Cleaners',
    1606: "Hook's Clock Repair",
    1608: "Luff 'N Stuff",
    1609: 'Every Little Bait',
    1612: 'Dime & Quarterdeck Bank',
    1613: 'Squid Pro Quo, Attorneys at Law',
    1614: 'Trim the Nail Boutique',
    1615: "Yacht's All, Folks!",
    1616: "Blackbeard's Beauty Parlor",
    1617: 'Out to See Optics',
    1619: 'Disembark! Tree Surgeons',
    1620: 'From Fore to Aft',
    1621: 'Poop Deck Gym',
    1622: 'Bait and Switches Electrical Shop',
    1624: 'Soles Repaired While U Wait',
    1626: 'Salmon Chanted Evening Formal Wear',
    1627: "Billy Budd's Bargain Binnacle Barn",
    1628: 'Piano Tuna',
    1629: '',
    1701: 'Buoys and Gulls Nursery School',
    1703: 'Wok the Plank Chinese Food',
    1705: 'Sails for Sale',
    1706: 'Peanut Butter and Jellyfish',
    1707: 'Gifts With a Porpoise',
    1709: 'Windjammers and Jellies',
    1710: 'Barnacle Bargains',
    1711: 'Deep Sea Diner',
    1712: 'Able-Bodied Gym',
    1713: "Art's Smart Chart Mart",
    1714: "Reel 'Em Inn",
    1716: 'Mermaid Swimwear',
    1717: 'Be More Pacific Ocean Notions',
    1718: 'Run Aground Taxi Service',
    1719: "Duck's Back Water Company",
    1720: 'The Reel Deal',
    1721: 'All For Nautical',
    1723: "Squid's Seaweed",
    1724: "That's  a Moray!",
    1725: "Ahab's Prefab Sea Crab Center",
    1726: 'Root Beer Afloats',
    1727: 'This Oar That',
    1728: 'Good Luck Horseshoe Crabs',
    1729: '',
    1802: 'Nautical But Nice',
    1804: 'Mussel Beach Gymnasium',
    1805: 'Tackle Box Lunches',
    1806: 'Cap Size Hat Store',
    1807: 'Keel Deals',
    1808: 'Knots So Fast',
    1809: 'Rusty Buckets',
    1810: 'Anchor Management',
    1811: "What's Canoe With You?",
    1813: 'Pier Pressure Plumbing',
    1814: 'The Yo Ho Stop and Go',
    1815: "What's Up, Dock?",
    1818: 'Seven Seas Cafe',
    1819: "Docker's Diner",
    1820: 'Hook, Line, and Sinker Prank Shop',
    1821: "King Neptoon's Cannery",
    1823: 'The Clam Bake Diner',
    1824: 'Dog Paddles',
    1825: 'Wholly Mackerel! Fish Market',
    1826: "Claggart's Clever Clovis Closet",
    1828: "Alice's Ballast Palace",
    1829: 'Seagull Statue Store',
    1830: 'Lost and Flounder',
    1831: 'Kelp Around the House',
    1832: "Melville's Massive Mizzenmast Mart",
    1833: 'This Transom Man Custom Tailored Suits',
    1834: 'Rudderly Ridiculous!',
    1835: '',
    4503: 'Gag Shop',
    4504: 'Toon Headquarters',
    4506: 'Clothing Shop',
    4603: "Tom-Tom's Drums",
    4604: 'In Four-Four Time',
    4605: "Fifi's Fiddles",
    4606: 'Casa De Castanets',
    4607: 'Catchy Toon Apparel',
    4609: 'Do, Rae, Me Piano Keys',
    4610: 'Please Refrain',
    4611: 'Tuning Forks and Spoons',
    4612: "Dr. Fret's Dentistry",
    4614: 'Shave and a Haircut for a Song',
    4615: "Piccolo's Pizza",
    4617: 'Happy Mandolins',
    4618: 'Rests Rooms',
    4619: 'More Scores',
    4622: 'Chin Rest Pillows',
    4623: 'Flats Sharpened',
    4625: 'Tuba Toothpaste',
    4626: 'Notations',
    4628: 'Accidental Insurance',
    4629: "Riff's Paper Plates",
    4630: 'Music Is Our Forte',
    4631: 'Canto Help You',
    4632: 'Dance Around the Clock Shop',
    4635: 'Tenor Times',
    4637: 'For Good Measure',
    4638: 'Hard Rock Shop',
    4639: 'Four Score Antiques',
    4641: 'Blues News',
    4642: 'Ragtime Dry Cleaners',
    4645: 'Club 88',
    4646: '',
    4648: 'Carry a Toon Movers',
    4649: '',
    4652: 'Full Stop Shop',
    4653: '',
    4654: 'Pitch Perfect Roofing',
    4655: "The Treble Chef's Cooking School",
    4656: '',
    4657: 'Barbershop Quartet',
    4658: 'Plummeting Pianos',
    4659: '',
    4701: 'The Schmaltzy Waltz School of Dance',
    4702: 'Timbre! Lumberjack Supplies',
    4703: 'I Can Handel It!',
    4704: "Tina's Concertina Concerts",
    4705: 'Zither Here Nor There',
    4707: "Doppler's Sound Effects Studio",
    4709: 'On Ballet! Climbing Supplies',
    4710: 'Hurry Up, Slow Polka! School of Driving',
    4712: 'C-Flat Tire Repair',
    4713: 'B-Sharp Fine Menswear',
    4716: 'Four-Part Harmonicas',
    4717: 'Sonata Your Fault! Discount Auto Insurance',
    4718: 'Chopin Blocks and Other Kitchen Supplies',
    4719: 'Madrigal Motor Homes',
    4720: 'Name That Toon',
    4722: 'Overture Understudies',
    4723: 'Haydn Go Seek Playground Supplies',
    4724: 'White Noise for Girls and Boys',
    4725: 'The Baritone Barber',
    4727: 'Vocal Chords Braided',
    4728: "Sing Solo We Can't Hear You",
    4729: 'Double Reed Bookstore',
    4730: 'Lousy Lyrics',
    4731: 'Toon Tunes',
    4732: 'Etude Brute? Theatre Company',
    4733: '',
    4734: '',
    4735: 'Accordions, If You Want In, Just Bellow!',
    4736: 'Her and Hymn Wedding Planners',
    4737: 'Harp Tarps',
    4738: 'Canticle Your Fancy Gift Shop',
    4739: '',
    4801: "Marshall's Stacks",
    4803: 'What a Mezzo! Maid Service',
    4804: 'The Mixolydian School of Bartending',
    4807: 'Relax the Bach',
    4809: "I Can't Understanza!",
    4812: '',
    4817: 'The Ternary Pet Shop',
    4819: "Yuki's Ukeleles",
    4820: '',
    4821: "Anna's Cruises",
    4827: 'Common Time Watches',
    4828: "Schumann's Shoes for Men",
    4829: "Pachelbel's Canonballs",
    4835: 'Ursatz for Kool Katz',
    4836: 'Reggae Regalia',
    4838: 'Kazoology School of Music',
    4840: 'Coda Pop Musical Beverages',
    4841: 'Lyre, Lyre, Pants on Fire!',
    4842: 'The Syncopation Corporation',
    4843: '',
    4844: 'Con Moto Cycles',
    4845: "Ellie's Elegant Elegies",
    4848: 'Lotsa Lute Savings & Loan',
    4849: '',
    4850: 'The Borrowed Chord Pawn Shop',
    4852: 'Flowery Flute Fleeces',
    4853: "Leo's Fenders",
    4854: "Wagner's Vocational Violin Videos",
    4855: 'The Teli-Caster Network',
    4856: '',
    4862: "Quentin's Quintessential Quadrilles",
    4867: "Mr. Costello's Yellow Cellos",
    4868: '',
    4870: "Ziggy's Zoo of Zigeunermusik",
    4871: "Harry's House of Harmonious Humbuckers",
    4872: "Fast Freddie's Fretless Fingerboards",
    4873: '',
    5501: 'Gag Shop',
    5502: 'Toon HQ',
    5503: 'Clothing Shop',
    5601: 'Eye of the Potato Optometry',
    5602: "Artie Choke's Neckties",
    5603: 'Lettuce Alone',
    5604: 'Cantaloupe Bridal Shop',
    5605: 'Vege-tables and Chairs',
    5606: 'Petals',
    5607: 'Compost Office',
    5608: 'Mom and Pop Corn',
    5609: 'Berried Treasure',
    5610: "Black-eyed Susan's Boxing Lessons",
    5611: "Gopher's Gags",
    5613: 'Crop Top Barbers',
    5615: "Bud's Bird Seed",
    5616: 'Dew Drop Inn',
    5617: "Flutterby's Butterflies",
    5618: "Peas and Q's",
    5619: "Jack's Beanstalks",
    5620: 'Rake It Inn',
    5621: 'Grape Expectations',
    5622: 'Petal Pusher Bicycles',
    5623: 'Bubble Bird Baths',
    5624: "Mum's the Word",
    5625: 'Leaf It Bees',
    5626: 'Pine Needle Crafts',
    5627: '',
    5701: 'From Start to Spinach',
    5702: "Jake's Rakes",
    5703: "Photo Cynthia's Camera Shop",
    5704: 'Lisa Lemon Used Cars',
    5705: 'Poison Oak Furniture',
    5706: '14 Carrot Jewelers',
    5707: 'Musical Fruit',
    5708: "We'd Be Gone Travel Agency",
    5709: 'Astroturf Mowers',
    5710: 'Tuft Guy Gym',
    5711: 'Garden Hosiery',
    5712: 'Silly Statues',
    5713: 'Trowels and Tribulations',
    5714: 'Spring Rain Seltzer Bottles',
    5715: 'Hayseed News',
    5716: 'Take It or Leaf It Pawn Shop',
    5717: 'The Squirting Flower',
    5718: 'The Dandy Lion Pet Shop',
    5719: 'Trellis the Truth! Private Investigators',
    5720: 'Vine and Dandy Menswear',
    5721: 'Root 66 Diner',
    5725: 'Barley, Hops, and Malt Shop',
    5726: "Bert's Dirt",
    5727: 'Gopher Broke Savings & Loan',
    5728: '',
    9501: 'Lullaby Library',
    9503: 'The Snooze Bar',
    9504: 'Gag Shop',
    9505: 'Toon HQ',
    9506: 'Clothing Shop',
    9601: 'Snuggle Inn',
    9602: 'Forty Winks for the Price of Twenty',
    9604: "Ed's Red Bed Spreads",
    9605: '323 Lullaby Lane',
    9607: "Big Mama's Bahama Pajamas",
    9608: 'Cat Nip for Cat Naps',
    9609: 'Deep Sleep for Cheap',
    9613: 'Clock Cleaners',
    9616: 'Lights Out Electric Co.',
    9617: '212 Lullaby Lane',
    9619: 'Relax to the Max',
    9620: "PJ's Taxi Service",
    9622: 'Sleepy Time Pieces',
    9625: 'Curl Up Beauty Parlor',
    9626: '818 Lullaby Lane',
    9627: 'The Sleepy Teepee',
    9628: 'Call It a Day Calendars',
    9629: '310 Lullaby Lane',
    9630: 'Rock to Sleep Quarry',
    9631: 'Down Time Watch Repair',
    9633: 'The Dreamland Screening Room',
    9634: 'Mind Over Mattress',
    9636: 'Insomniac Insurance',
    9639: 'House of Hibernation',
    9640: '805 Lullaby Lane',
    9642: 'Sawing Wood Slumber Lumber',
    9643: 'Shut-Eye Optometry',
    9644: 'Pillow Fights Nightly',
    9645: 'The All Tucked Inn',
    9647: 'Make Your Bed! Hardware Store',
    9649: 'Snore or Less',
    9650: '714 Lullaby Lane',
    9651: 'For Richer or Snorer',
    9652: '',
    3507: 'Gag Shop',
    3508: 'Toon HQ',
    3509: 'Clothing Shop',
    3601: 'Northern Lights Electric Company',
    3602: "Nor'easter Bonnets",
    3605: '',
    3607: 'The Blizzard Wizard',
    3608: 'Nothing to Luge',
    3610: "Mike's Massive Mukluk Mart",
    3611: "Mr. Cow's Snow Plows",
    3612: 'Igloo Design',
    3613: 'Ice Cycle Bikes',
    3614: 'Snowflakes Cereal Company',
    3615: 'Fried Baked Alaskas',
    3617: 'Cold Air Balloon Rides',
    3618: 'Snow Big Deal! Crisis Management',
    3620: 'Skiing Clinic',
    3621: 'The Melting Ice Cream Bar',
    3622: '',
    3623: 'The Mostly Toasty Bread Company',
    3624: 'Subzero Sandwich Shop',
    3625: "Auntie Freeze's Radiator Supply",
    3627: 'St. Bernard Kennel Club',
    3629: 'Pea Soup Cafe',
    3630: 'Icy London, Icy France Travel Agency',
    3634: 'Easy Chair Lifts',
    3635: 'Used Firewood',
    3636: 'Affordable Goosebumps',
    3637: "Kate's Skates",
    3638: 'Toboggan or Not Toboggan',
    3641: "Fred's Red Sled Beds",
    3642: 'Eye of the Storm Optics',
    3643: 'Snowball Hall',
    3644: 'Melted Ice Cubes',
    3647: 'The Sanguine Penguin Tuxedo Shop',
    3648: 'Instant Ice',
    3649: 'Hambrrrgers',
    3650: 'Antarctic Antiques',
    3651: "Frosty Freddy's Frozen Frankfurters",
    3653: 'Ice House Jewelry',
    3654: '',
    3702: 'Winter Storage',
    3703: '',
    3705: 'Icicles Built for Two',
    3706: "Shiverin' Shakes Malt Shop",
    3707: 'Snowplace Like Home',
    3708: "Pluto's Place",
    3710: 'Dropping Degrees Diner',
    3711: '',
    3712: 'Go With the Floe',
    3713: 'Chattering Teeth, Subzero Dentist',
    3715: "Aunt Arctic's Soup Shop",
    3716: 'Road Salt and Pepper',
    3717: 'Juneau What I Mean?',
    3718: 'Designer Inner Tubes',
    3719: 'Ice Cube on a Stick',
    3721: "Noggin's Toboggan Bargains",
    3722: 'Snow Bunny Ski Shop',
    3723: "Shakey's Snow Globes",
    3724: 'The Chattering Chronicle',
    3725: 'You Sleigh Me',
    3726: 'Solar Powered Blankets',
    3728: 'Lowbrow Snowplows',
    3729: '',
    3730: 'Snowmen Bought & Sold',
    3731: 'Portable Fireplaces',
    3732: 'The Frozen Nose',
    3734: 'Icy Fine, Do You? Optometry',
    3735: 'Polar Ice Caps',
    3736: 'Diced Ice at a Nice Price',
    3737: 'Downhill Diner',
    3738: "Heat-Get It While It's Hot",
    3739: '' }
ClosetTimeoutMessage = 'Sorry, you ran out\n of time.'
ClosetNotOwnerMessage = "This isn't your closet, but you may try on the clothes."
ClosetPopupOK = 'OK'
ClosetDiscardButton = 'Remove'
ClosetAreYouSureMessage = 'You have deleted some clothes.  Do you really want to delete them?'
ClosetYes = 'Yes'
ClosetNo = 'No'
EstateOwnerLeftMessage = "Sorry, the owner of this estate left.  You'll be sent to the playground in %s seconds"
EstatePopupOK = 'OK'
EstateTeleportFailed = "Couldn't go home. Try again!"
EstateTeleportFailedNotFriends = "Sorry, %s is in a toon's estate that you are not friends with."
AvatarsHouse = '%s\n House'
BankGuiCancel = 'Cancel'
BankGuiOk = 'Ok'
DistributedBankNoOwner = 'Sorry, this is not your bank.'
DistributedBankNotOwner = 'Sorry, this is not your bank.'

def GetPossesive(name):
    if name[-1:] == 's':
        possesive = name + "'"
    else:
        possesive = name + "'s"
    return possesive

FireworksBeginning = 'Toon HQ: Welcome to summer fireworks! Enjoy the show!'
FireworksInstructions = 'Toon HQ: Hit the "Page Up" key to see better.'
FireworksEnding = 'Toon HQ: Hope you enjoyed the show! Have a great summer!'
