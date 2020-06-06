# File: L (Python 2.2)

import string
ExtraKeySanityCheck = 'Ignore me'
InterfaceFont = 'phase_3/models/fonts/ImpressBT.ttf'
Mickey = 'Mickey'
Minnie = 'Minnie'
Donald = 'Donald'
Daisy = 'Daisy'
Goofy = 'Goofy'
Pluto = 'Pluto'
Flippy = 'Flipi'
MickeyMouse = 'Mickey Mouse'
AIStartDefaultDistrict = 'Villaboba'
Cog = 'Bot'
Cogs = 'Bots'
ACog = 'un Bot'
TheCogs = 'Los Bots'
TheFish = 'los peces'
AFish = 'un pez'
Level = 'nivel'
QuestsCompleteString = 'Completada'
QuestsNotChosenString = 'No est\xc3\xa1 elegida'
QuestsDefaultGreeting = ('\xc2\xa1Hola, _avName_!', '\xc2\xa1Buenas, _avName_!', '\xc2\xbfQu\xc3\xa9 tal, _avName_?', '\xc2\xbfQu\xc3\xa9 tal todo, _avName_?', '\xc2\xbfC\xc3\xb3mo te va, _avName_?', '\xc2\xbfQu\xc3\xa9 hay, _avName_?', '\xc2\xbfC\xc3\xb3mo est\xc3\xa1s, _avName_?')
QuestsDefaultIncomplete = ('\xc2\xbfQu\xc3\xa9 tal va la tarea, _avName_?', '\xc2\xa1Parece que todav\xc3\xada te queda trabajo por hacer con esa tarea!', '\xc2\xa1Sigue trabajando as\xc3\xad, _avName_!', 'Intenta terminar la tarea.  \xc2\xa1S\xc3\xa9 que puedes hacerlo!', '\xc2\xa1Sigue intentando terminar la tarea, contamos contigo!', '\xc2\xa1Sigue trabajando en tu dibutarea!')
QuestsDefaultIncompleteProgress = ('Has venido al lugar adecuado, pero antes tienes que terminar la dibutarea.', 'Cuando hayas terminado con la dibutarea, vuelve por aqu\xc3\xad.', 'Vuelve cuando hayas terminado la dibutarea.')
QuestsDefaultIncompleteWrongNPC = ('Buen trabajo con esa dibutarea. Deber\xc3\xadas ir a ver a _toNpcName_._where_', 'Parece que est\xc3\xa1s a punto de acabar tu dibutarea. Ve a ver a _toNpcName_._where_.', 'Ve a ver a _toNpcName_ para terminar la dibutarea._where_')
QuestsDefaultComplete = ('\xc2\xa1Buen trabajo! Aqu\xc3\xad est\xc3\xa1 tu recompensa...', '\xc2\xa1Buen trabajo, _avName_! Toma, tu recompensa...', '\xc2\xa1Muy bien, _avName_!  Aqu\xc3\xad est\xc3\xa1 tu recompensa...')
QuestsDefaultLeaving = ('\xc2\xa1Chao!', '\xc2\xa1Adi\xc3\xb3s!', 'Nos vemos, _avName_.', '\xc2\xa1Hasta la vista, _avName_!', '\xc2\xa1Buena suerte!', '\xc2\xa1Divi\xc3\xa9rtete en Toontown!', '\xc2\xa1Hasta luego!')
QuestsDefaultReject = ('Hola.', '\xc2\xbfEn qu\xc3\xa9 puedo ayudarte?', '\xc2\xbfC\xc3\xb3mo est\xc3\xa1s?', 'Muy buenas.', 'Ahora estoy un poco ocupado, _avName_.', '\xc2\xbfS\xc3\xad?', '\xc2\xbfQu\xc3\xa9 hay, _avName_?', '\xc2\xbfC\xc3\xb3mo te va, _avName_?', '\xc2\xa1Eh, _avName_! \xc2\xbfC\xc3\xb3mo va todo?', '\xc2\xbfSab\xc3\xadas que puedes abrir el dibucuaderno pulsando la tecla F8?', '\xc2\xa1Puedes usar el mapa para teletransportarte de vuelta al dibuparque!', 'Para hacerte amigo de otros jugadores, haz clic en ellos.', 'Para averiguar m\xc3\xa1s sobre un ' + Cog + ' haz clic en \xc3\xa9l.', 'Re\xc3\xbane tesoros en el dibuparque para rellenar el ris\xc3\xb3metro.', 'Edificios' + Cog + ' son lugares peligrosos! \xc2\xa1No entres en ellos solo!', 'Cuando pierdas un combate, los ' + Cogs + ' se llevar\xc3\xa1n todas tus bromas.', 'Para conseguir m\xc3\xa1s bromas, juega a los juegos del tranv\xc3\xada!', 'Para conseguir m\xc3\xa1s puntos de risa, completa las dibutareas.', 'Todas las dibutareas proporcionan recompensas.', 'Algunas recompensas sirven para poder llevar m\xc3\xa1s bromas.', 'Si ganas un combate, consigues cr\xc3\xa9ditos de dibutareas por cada ' + Cog + ' derrotado.', 'Si recuperas un edificio ' + Cog + ' vuelve a entrar para ver el agradecimiento especial de su propietario.', 'Para mirar hacia arriba, mant\xc3\xa9n pulsada la tecla Re P\xc3\xa1g.', 'Si pulsas la tecla Tab, podr\xc3\xa1s contemplar diferentes vistas de los alrededores.', "Para mostrar lo que piensas a tus amigos secretos, escribe un '.' antes del pensamiento.", 'Cuando dejes aturdido a un ' + Cog + ' le ser\xc3\xa1 m\xc3\xa1s dif\xc3\xadcil esquivar los objetos que caen.', 'Cada tipo de edificio ' + Cog + ' tiene un aspecto distinto.', 'Cuando derrotes a los ' + Cogs + ' de los pisos altos de un edificio, obtendr\xc3\xa1s habilidades superiores.')
QuestsDefaultTierNotDone = ('\xc2\xa1Hola, _avName_! Antes de acceder a una nueva dibutarea debes terminar la actual.', '\xc2\xa1Muy buenas! Tienes que terminar las dibutareas actuales para acceder a una nueva.', '\xc2\xa1Buenas, _avName_! Para poderte asignar una nueva dibutarea, tienes que terminar las dibutareas actuales.')
QuestsDefaultQuest = None
QuestsDefaultVisitQuestDialog = ('He o\xc3\xaddo que _toNpcName_ te anda buscando._where_', 'D\xc3\xa9jate caer por donde _toNpcName_ cuando tengas la ocasi\xc3\xb3n._where_', 'Ve a ver a _toNpcName_ cuando pases por all\xc3\xad._where_', 'Si tienes la ocasi\xc3\xb3n, p\xc3\xa1sate a saludar a _toNpcName_._where_', '_toNpcName_ te asignar\xc3\xa1 tu pr\xc3\xb3xima dibutarea._where_')
QuestsCogQuestProgress = '%(progress)s de %(numCogs)s derrotados'
QuestsCogQuestHeadline = 'SE BUSCA'
QuestsCogQuestSCStringS = 'Tengo que derrotar %(cogName)s%(cogLoc)s.'
QuestsCogQuestSCStringP = 'Tengo que derrotar algunos %(cogName)s%(cogLoc)s.'
QuestsCogQuestDefeat = 'Derrotar a %s'
QuestsCogNewbieQuestObjective = 'Ayuda a los dibus con %d puntos de risas o derrota a algunos %s'
QuestsCogNewbieQuestCaption = 'Ayuda a un nuevo dibu con %d puntos de risas o menos'
QuestsCogNewbieQuestAux = 'Derrotar:'
QuestsNewbieQuestHeadline = 'Aprend\xc3\xads'
QuestsCogTrackQuestProgress = '%(progress)s de %(numCogs)s derrotados'
QuestsCogTrackQuestHeadline = 'SE BUSCA'
QuestsCogTrackQuestSCString = 'Tengo que derrotar a %(cogText)s%(cogLoc)s.'
QuestsCogTrackQuestDefeat = 'Derrotar a %s'
QuestsCogLevelQuestProgress = '%(progress)s de %(numCogs)s derrotados'
QuestsCogLevelQuestHeadline = 'SE BUSCA'
QuestsCogLevelQuestSCString = 'Tengo que derrotar a %(cogText)s%(cogLoc)s.'
QuestsCogLevelQuestDefeat = 'Derrotar a %s'
QuestsCogLevelQuestDesc = 'de nivel %(level)s+ ' + Cog
QuestsCogLevelQuestDescC = '%(count)s nivel %(level)s+ ' + Cogs
QuestsCogLevelQuestDescI = 'algunos de nivel %(level)s+ ' + Cogs
QuestsCogLevelQuestSCString = 'Tengo que derrotar a %(objective)s%(location)s.'
QuestsBuildingQuestFloorNumbers = ('', 'dos+', 'tres+', 'cuatro+', 'cinco+')
QuestsBuildingQuestBuilding = 'Edificio'
QuestsBuildingQuestBuildings = 'Edificios'
QuestsBuildingQuestHeadline = 'DERROTAR'
QuestsBuildingQuestProgressString = '%(progress)s de %(num)s derrotados'
QuestsBuildingQuestString = 'Derrotar a %s'
QuestsBuildingQuestSCString = 'Tengo que derrotar a %(objective)s%(location)s.'
QuestsBuildingQuestDesc = 'un edificio %(type)s'
QuestsBuildingQuestDescF = 'un edificio %(type)s de %(floors)s pisos'
QuestsBuildingQuestDescC = '%(count)s edificios %(type)s'
QuestsBuildingQuestDescCF = '%(count)s edificios %(type)s de %(floors)s pisos'
QuestsBuildingQuestDescI = 'algunos edificios %(type)s'
QuestsBuildingQuestDescIF = 'algunos edificios %(type)s de %(floors)s pisos'
QuestsDeliverGagQuestProgress = '%(progress)s de %(numGags)s entregados'
QuestsDeliverGagQuestHeadline = 'ENTREGAR'
QuestsDeliverGagQuestToSCStringS = 'Tengo que entregar %(gagName)s.'
QuestsDeliverGagQuestToSCStringP = 'Tengo que entregar %(gagName)s.'
QuestsDeliverGagQuestSCString = 'Tengo que hacer una entrega.'
QuestsDeliverGagQuestString = 'Entregar %s'
QuestsDeliverGagQuestStringLong = 'Entregar %s a _toNpcName_.'
QuestsDeliverItemQuestProgress = ''
QuestsDeliverItemQuestHeadline = 'ENTREGAR'
QuestsDeliverItemQuestSCString = 'Tengo que entregar %(article)s%(itemName)s.'
QuestsDeliverItemQuestString = 'Entregar %s'
QuestsDeliverItemQuestStringLong = 'Entregar %s a _toNpcName_.'
QuestsVisitQuestProgress = ''
QuestsVisitQuestHeadline = 'VISITAR'
QuestsVisitQuestStringShort = 'Visitar'
QuestsVisitQuestStringLong = 'Ir a ver a _toNpcName_'
QuestsVisitQuestSeeSCString = 'Tengo que ver a %s.'
QuestsRecoverItemQuestProgress = '%(progress)s de %(numItems)s recuperados'
QuestsRecoverItemQuestHeadline = 'RECUPERAR'
QuestsRecoverItemQuestSeeHQSCString = 'Tengo que ver a un funcionario del cuartel general.'
QuestsRecoverItemQuestReturnToHQSCString = 'Tengo que devolver %s a un funcionario del cuartel general.'
QuestsRecoverItemQuestReturnToSCString = 'Tengo que devolver %(item)s a %(npcName)s.'
QuestsRecoverItemQuestGoToHQSCString = 'Tengo que ir al Cuartel General Dibu.'
QuestsRecoverItemQuestGoToPlaygroundSCString = 'Tengo que ir al dibuparque %s.'
QuestsRecoverItemQuestGoToStreetSCString = 'Tengo que ir %(to)s %(street)s en %(hood)s.'
QuestsRecoverItemQuestVisitBuildingSCString = 'Tengo que ir a %s %s.'
QuestsRecoverItemQuestWhereIsBuildingSCString = '\xc2\xbfD\xc3\xb3nde est\xc3\xa1 %s %s?'
QuestsRecoverItemQuestRecoverFromSCString = 'Tengo que recuperar: %(item)s de %(holder)s%(loc)s.'
QuestsRecoverItemQuestString = 'Recuperar %(item)s de %(holder)s'
QuestsTrackChoiceQuestHeadline = 'ELIGE'
QuestsTrackChoiceQuestSCString = 'Tengo que escoger entre %(trackA)s y %(trackB)s.'
QuestsTrackChoiceQuestMaybeSCString = 'Quiz\xc3\xa1 deba escoger %s.'
QuestsTrackChoiceQuestString = 'Elige entre %(trackA)s y %(trackB)s'
QuestsFriendQuestHeadline = 'AMIGO'
QuestsFriendQuestSCString = 'Necesito hacer amigos.'
QuestsFriendQuestString = 'Hacer un amigo'
QuestsFriendNewbieQuestString = 'Has %d amigos con %d puntos de risa o menos'
QuestsFriendNewbieQuestProgress = '%(progress)s de %(numFriends)s echos'
QuestsFriendNewbieQuestObjective = 'Haste amigo con %d dibus que tengan %d puntos de risa o menos'
QuestsTrolleyQuestHeadline = 'TRANV\xc3\x8dA'
QuestsTrolleyQuestSCString = 'Tengo que subir al tranv\xc3\xada.'
QuestsTrolleyQuestString = 'Subir al tranv\xc3\xada.'
QuestsTrolleyQuestStringShort = '\xc2\xbfQuieres subir al tranv\xc3\xada?'
QuestsMinigameNewbieQuestString = '%d Minijuegos'
QuestsMinigameNewbieQuestProgress = '%(progress)s of %(numMinigames)s Played'
QuestsMinigameNewbieQuestObjective = 'Juega %d minijuegos con Dibus que tienen %d puntos un el risometro o menos.'
QuestsMinigameNewbieQuestSCString = 'Necesito jugar en los minijuegos con Dibus nuevos.'
QuestsMinigameNewbieQuestCaption = 'Ayuda a un Dibu Nuevo con %d puntos en el risometro o menos.'
QuestsMinigameNewbieQuestAux = 'Juega:'
QuestsMaxHpReward = 'Tu ris\xc3\xb3metro ha aumentado en %s.'
QuestsMaxHpRewardPoster = 'Recompensa: %s punto(s) de aumento en el ris\xc3\xb3metro'
QuestsMoneyRewardSingular = 'Has conseguido 1 gominola.'
QuestsMoneyRewardPlural = 'Has conseguido %s gominolas.'
QuestsMoneyRewardPosterSingular = 'Recompensa: 1 gominola'
QuestsMoneyRewardPosterPlural = 'Recompensa: %s gominolas'
QuestsMaxMoneyRewardSingular = 'Ahora puedes llevar 1 gominola.'
QuestsMaxMoneyRewardPlural = 'Ahora puedes llevar %s gominolas.'
QuestsMaxMoneyRewardPosterSingular = 'Recompensa: Llevar 1 gominola'
QuestsMaxMoneyRewardPosterPlural = 'Recompensa: Llevar %s gominolas'
QuestsMaxGagCarryReward = 'Consigues un %(name)s. Ahora puedes llevar %(num)s bromas.'
QuestsMaxGagCarryRewardPoster = 'Recompensa: %(name)s (%(num)s)'
QuestsMaxQuestCarryReward = 'Ahora puedes tener %s dibutareas.'
QuestsMaxQuestCarryRewardPoster = 'Recompensa: Tener %s dibutareas'
QuestsTeleportReward = 'Ahora puedes teletransportarte a %s.'
QuestsTeleportRewardPoster = 'Recompensa: Acceso por teletransporte a %s'
QuestsTrackTrainingReward = 'Ahora puedes entrenar las bromas de "%s".'
QuestsTrackTrainingRewardPoster = 'Recompensa: Entrenamiento de bromas'
QuestsTrackProgressReward = 'Ahora tienes el fotograma %(frameNum)s de la animaci\xc3\xb3n del circuito %(trackName)s.'
QuestsTrackProgressRewardPoster = 'Recompensa: Fotograma %(frameNum)s de la animaci\xc3\xb3n de circuito "%(trackName)s"'
QuestsTrackCompleteReward = 'Ahora puedes llevar y usar las bromas de "%s".'
QuestsTrackCompleteRewardPoster = 'Recompensa: Entrenamiento de circuito %s final'
QuestsClothingTicketReward = 'Puedes cambiarte de ropa'
QuestsClothingTicketRewardPoster = 'Recompensa: Ticket de ropa'
QuestsCheesyEffectRewardPoster = 'Recompensa: %s'
QuestsStreetLocationThisPlayground = 'en este parque'
QuestsStreetLocationThisStreet = 'en esta calle'
QuestsStreetLocationNamedPlayground = 'en el parque de %s'
QuestsStreetLocationNamedStreet = 'en la %s de %s'
QuestsLocationBuilding = 'El edificio de %s se llama'
QuestsLocationBuildingVerb = 'el cual est\xc3\xa1 '
QuestsLocationParagraph = '\x7%(building)s   "%(buildingName)s"...\x7...%(buildingVerb)s %(street)s.'
QuestsGenericFinishSCString = 'Necesito terminar la Dibutarea.'
QuestsMediumPouch = 'Bolsita mediana'
QuestsLargePouch = 'Bolsita grande'
QuestsSmallBag = 'Bolsa peque\xc3\xb1a'
QuestsMediumBag = 'Bolsa mediana'
QuestsLargeBag = 'Bolsa grande'
QuestsSmallBackpack = 'Mochila peque\xc3\xb1a'
QuestsMediumBackpack = 'Mochila mediana'
QuestsLargeBackpack = 'Mochila grande'
QuestsItemDict = {
    1: [
        'Gafas',
        'Gafas',
        'unas '],
    2: [
        'Llave',
        'Llaves',
        'una '],
    3: [
        'Pizarra',
        'Pizarras',
        'una '],
    4: [
        'Libro',
        'Libros',
        'un '],
    5: [
        'Chocolatina',
        'Chocolatinas',
        'una '],
    6: [
        'Tiza',
        'Tizas',
        'una '],
    7: [
        'Receta',
        'Recetas',
        'una '],
    8: [
        'Nota',
        'Notas',
        'una '],
    9: [
        'Calculadora',
        'Calculadoras',
        'una '],
    10: [
        'Neum\xc3\xa1tico de coche de payasos',
        'Neum\xc3\xa1ticos de coche de payasos',
        'un '],
    11: [
        'Bomba de aire',
        'Bombas de aire',
        'una '],
    12: [
        'Tinta de pulpo',
        'Tintas de pulpo',
        'un poco de '],
    13: [
        'Paquete',
        'Paquetes',
        'un '],
    14: [
        'Recibo de pez de acuario',
        'Recibos de pez de acuario',
        'un '],
    15: [
        'Pez de acuario',
        'Peces de acuario',
        'un '],
    16: [
        'Aceite',
        'Aceites',
        'un poco de '],
    17: [
        'Grasa',
        'Grasas',
        'un poco de '],
    18: [
        'Agua',
        'Aguas',
        'un poco de '],
    19: [
        'Informe de equipo',
        'Informes de equipo',
        'un '],
    1000: [
        'Ticket de ropa',
        'Tickets de ropa',
        'un '],
    2001: [
        'Tubo interno',
        'Tubos internos',
        'un '],
    2002: [
        'Prescripci\xc3\xb3n de mon\xc3\xb3culo',
        'Prescripciones de mon\xc3\xb3culo',
        'una '],
    2003: [
        'Montura de mon\xc3\xb3culo',
        'Monturas de mon\xc3\xb3culo',
        'una '],
    2004: [
        'Mon\xc3\xb3culo',
        'Mon\xc3\xb3culos',
        'un '],
    2005: [
        'Peluca blanca grande',
        'Pelucas blancas grandes',
        'una '],
    2006: [
        'Granel de lastre',
        'Graneles de lastre',
        'una '],
    2007: [
        'Engranaje de bot',
        'Engranajes de bot',
        'un '],
    2008: [
        'Carta n\xc3\xa1utica',
        'Cartas n\xc3\xa1uticas',
        'una '],
    2009: [
        'Coraza repugnante',
        'Corazas repugnantes',
        'un '],
    2010: [
        'Coraza limpia',
        'Corazas limpias',
        'un '],
    2011: [
        'Resorte de reloj',
        'Resortes de reloj',
        'un '],
    2012: [
        'Contrapeso',
        'Contrapesos',
        'un '],
    4001: [
        'Inventario de Tina',
        'Inventarios de Tina',
        ''],
    4002: [
        'Inventario de Uki',
        'Inventarios de Uki',
        ''],
    4003: [
        'Formulario de inventario',
        'Formularios de inventario',
        'un '],
    4004: [
        'Inventario de Bibi',
        'Inventarios de Bibi',
        ''],
    4005: [
        'Billete de Chopo Chop\xc3\xadn',
        'Billetes de Chopo Chop\xc3\xadn',
        ''],
    4006: [
        'Billete de Felisa Felina',
        'Billetes de Felisa Felina',
        ''],
    4007: [
        'Billete de Barbo',
        'Billetes de Barbo',
        ''],
    4008: [
        'Casta\xc3\xb1uela sucia',
        'Casta\xc3\xb1uelas sucias',
        ''],
    4009: [
        'Tinta azul de pulpo',
        'Tintas azules de pulpo',
        'un poco de '],
    4010: [
        'Casta\xc3\xb1uela transparente',
        'Casta\xc3\xb1uelas transparentes',
        'una '],
    4011: [
        'Letra de Leo',
        'Letras de Leo',
        ''],
    5001: [
        'Corbata de seda',
        'Corbatas de seda',
        'una '],
    5002: [
        'Traje mil rayas',
        'Trajes mil rayas',
        'un '],
    5003: [
        'Tijera',
        'Tijeras',
        'unas '],
    5004: [
        'Postal',
        'Postales',
        'una '],
    5005: [
        'Pluma',
        'Plumas',
        'una '],
    5006: [
        'Tintero',
        'Tinteros',
        'un '],
    5007: [
        'Libreta',
        'Libretas',
        'una '],
    5008: [
        'Caja de seguridad',
        'Cajas de seguridad',
        'una '],
    5009: [
        'Bolsa de alpiste',
        'Bolsas de alpiste',
        'una '],
    5010: [
        'Rueda dentada',
        'Ruedas dentadas',
        'una '],
    5011: [
        'Ensalada',
        'Ensaladas',
        'una '],
    5012: [
        'Llave de los Jardines de Daisy',
        'Llaves de los Jardines de Daisy',
        'una '],
    3001: [
        'Bal\xc3\xb3n de f\xc3\xbatbol',
        'Balones de f\xc3\xbatbol',
        'un '],
    3002: [
        'Tobog\xc3\xa1n',
        'Toboganes',
        'un '],
    3003: [
        'Cubito de hielo',
        'Cubitos de hielo',
        'un '],
    3004: [
        'Carta de amor',
        'Cartas de amor',
        'una '],
    3005: [
        'Perrito caliente',
        'Perritos calientes',
        'un '],
    3006: [
        'Anillo de compromiso',
        'Anillos de compromiso',
        'un '],
    3007: [
        'Aleta de sardina',
        'Aletas de sardina',
        'una '],
    3008: [
        'Poci\xc3\xb3n calmante',
        'Pociones calmantes',
        'una '],
    3009: [
        'Diente roto',
        'Dientes rotos',
        'un '],
    3010: [
        'Diente de oro',
        'Dientes de oro',
        'un '],
    3011: [
        'Pan de pi\xc3\xb1ones',
        'Panes de pi\xc3\xb1ones',
        'un '],
    3012: [
        'Queso abultado',
        'Quesos abultados',
        'unos '],
    3013: [
        'Cuchara sencilla',
        'Cucharas sencillas',
        'una '],
    3014: [
        'Sapo parlanch\xc3\xadn',
        'Sapos parlanchines',
        'un '],
    3015: [
        'Helado de cucurucho',
        'Helados de cucurucho ',
        'un '],
    3016: [
        'Talco para peluca',
        'Talco para pelucas',
        'un poco de '],
    3017: [
        'Patito de goma',
        'Patitos de goma',
        'un '],
    3018: [
        'Dados de goma',
        'Dados de goma',
        'unos '],
    3019: [
        'Micr\xc3\xb3fono',
        'Micr\xc3\xb3fonos',
        'un '],
    3020: [
        'Teclado electr\xc3\xb3nico',
        'Teclados electr\xc3\xb3nicos',
        'un '],
    3021: [
        'Zapatos con plataforma',
        'Zapatos con plataforma',
        'unos '],
    3022: [
        'Caviar',
        'Caviar',
        'un poco de '],
    3023: [
        'Maquillaje',
        'Maquillaje',
        'un poco de '] }
QuestsHQOfficerFillin = 'Funcionario del cuartel general'
QuestsHQWhereFillin = ''
QuestsHQBuildingNameFillin = 'Cuartel General Dibu'
QuestsHQLocationNameFillin = 'en cualquier barrio'
QuestsTailorFillin = 'Sastre'
QuestsTailorWhereFillin = ''
QuestsTailorBuildingNameFillin = 'Tienda de Ropa'
QuestsTailorLocationNameFillin = 'en cualquier barrio'
QuestsTailorQuestSCString = 'Tengo que ir al sastre.'
QuestMovieQuestChoiceCancel = '\xc2\xa1Vuelve m\xc3\xa1s tarde, si necesitas una Dibutarea! \xc2\xa1Chao!'
QuestMovieTrackChoiceCancel = 'Vuelve m\xc3\xa1s tarde, cuando te hayas decidido! \xc2\xa1Chao!'
QuestMovieQuestChoice = 'Elige una Dibutarea.'
QuestMovieTrackChoice = '\xc2\xbfTe has decidido? Elige un circuito, o vuelve m\xc3\xa1s tarde.'
GREETING = 0
QUEST = 1
INCOMPLETE = 2
INCOMPLETE_PROGRESS = 3
INCOMPLETE_WRONG_NPC = 4
COMPLETE = 5
LEAVING = 6
TheBrrrghTrackQuestDict = {
    GREETING: '',
    QUEST: 'Ya est\xc3\xa1s listo.\x7Sal y ponte a caminar hasta que decidas qu\xc3\xa9 circuito elegir.\x7Pi\xc3\xa9nsalo bien, porque \xc3\xa9ste ser\xc3\xa1 tu circuito final.\x7Cuando est\xc3\xa9s seguro, vuelve conmigo.',
    INCOMPLETE_PROGRESS: 'Pi\xc3\xa9nsalo bien.',
    INCOMPLETE_WRONG_NPC: 'Pi\xc3\xa9nsalo bien.',
    COMPLETE: '\xc2\xa1Muy buena elecci\xc3\xb3n!',
    LEAVING: 'Buena suerte.  Vuelve conmigo cuando tengas dominada tu nueva habilidad.' }
QuestDialog_3225 = {
    QUEST: 'Gracias por venir, _avName_!\x7Los bots del vecindario han asustado a mi repartidor.\x7No tengo a nadie que entregue esta ensalada a _toNpcName_!\x7\xc2\xbfPuedes encargarte t\xc3\xba? \xc2\xa1Muchas gracias!_where_' }
QuestDialog_2910 = {
    QUEST: '\xc2\xbfYa has vuelto?\x7Buen trabajo con el resorte.\x7El objeto final es un contrapeso.\x7P\xc3\xa1sate a ver a _toNpcName_ y tr\xc3\xa1ete lo que encuentres._where_' }
QuestDialogDict = {
    160: {
        GREETING: '',
        QUEST: 'Bueno, creo que ya est\xc3\xa1s listo para algo m\xc3\xa1s complicado.\x7Derrota a 3 jefebots.',
        INCOMPLETE_PROGRESS: 'Los ' + Cogs + ' est\xc3\xa1n en las calles, atravesando los t\xc3\xbaneles.',
        INCOMPLETE_WRONG_NPC: 'Muy bien, has derrotado a los jefebots. \xc2\xa1Ve al cuartel general dibu para recibir una recompensa!',
        COMPLETE: QuestsDefaultComplete,
        LEAVING: QuestsDefaultLeaving },
    161: {
        GREETING: '',
        QUEST: 'Bueno, creo que ya est\xc3\xa1s listo para algo m\xc3\xa1s complicado.\x7Derrota a 3 abogabots.',
        INCOMPLETE_PROGRESS: 'Los ' + Cogs + ' est\xc3\xa1n en las calles, atravesando los t\xc3\xbaneles.',
        INCOMPLETE_WRONG_NPC: 'Muy bien, has derrotado a los abogabots. \xc2\xa1Ve al cuartel general dibu para recibir una recompensa!',
        COMPLETE: QuestsDefaultComplete,
        LEAVING: QuestsDefaultLeaving },
    162: {
        GREETING: '',
        QUEST: 'Bueno, creo que ya est\xc3\xa1s listo para algo m\xc3\xa1s complicado.\x7Derrota a 3 chequebots.',
        INCOMPLETE_PROGRESS: 'Los ' + Cogs + ' est\xc3\xa1n en las calles, atravesando los t\xc3\xbaneles.',
        INCOMPLETE_WRONG_NPC: 'Muy bien, has derrotado a los chequebots. \xc2\xa1Ve al cuartel general dibu para recibir una recompensa!',
        COMPLETE: QuestsDefaultComplete,
        LEAVING: QuestsDefaultLeaving },
    163: {
        GREETING: '',
        QUEST: 'Bueno, creo que ya est\xc3\xa1s listo para algo m\xc3\xa1s complicado.\x7Derrota a 3 vendebots.',
        INCOMPLETE_PROGRESS: 'Los ' + Cogs + ' est\xc3\xa1n en las calles, atravesando los t\xc3\xbaneles.',
        INCOMPLETE_WRONG_NPC: 'Muy bien, has derrotado a los vendebots. \xc2\xa1Ve al cuartel general dibu para recibir una recompensa!',
        COMPLETE: QuestsDefaultComplete,
        LEAVING: QuestsDefaultLeaving },
    164: {
        QUEST: 'Creo que te vendr\xc3\xa1n bien unas cuantas bromas nuevas.\x7Ve a ver a Flipi, quiz\xc3\xa1 te pueda ayudar._where_' },
    165: {
        QUEST: 'Muy buenas.\x7Creo que tienes que practicar con las bromas.\x7Cada vez que alcances a un bot con una de las bromas, aumentar\xc3\xa1 tu experiencia.\x7Cuando tengas la suficiente experiencia, podr\xc3\xa1s usar bromas mejores.\x7Practica ahora con tus bromas derrotando a 4 bots.' },
    166: {
        QUEST: 'Te felicito, has derrotado a esos bots.\x7\xc2\xbfSab\xc3\xadas que hay cuatro tipos diferentes de bots?\x7Hay abogabots, chequebots, vendebots y jefebots.\x7Se diferencian en el color y en las etiquetas con su nombre.\x7Entr\xc3\xa9nate derrotando a 4 jefebots.' },
    167: {
        QUEST: 'Te felicito, has derrotado a esos bots.\x7\xc2\xbfSab\xc3\xadas que hay cuatro tipos diferentes de bots?\x7Hay abogabots, chequebots, vendebots y jefebots.\x7Se diferencian en el color y en las etiquetas con su nombre.\x7Entr\xc3\xa9nate derrotando a 4 abogabots.' },
    168: {
        QUEST: 'Te felicito, has derrotado a esos bots.\x7\xc2\xbfSab\xc3\xadas que hay cuatro tipos diferentes de bots?\x7Hay abogabots, chequebots, vendebots y jefebots.\x7Se diferencian en el color y en las etiquetas con su nombre.\x7Entr\xc3\xa9nate derrotando a 4 vendebots.' },
    169: {
        QUEST: 'Te felicito, has derrotado a esos bots.\x7\xc2\xbfSab\xc3\xadas que hay cuatro tipos diferentes de bots?\x7Hay abogabots, chequebots, vendebots y jefebots.\x7Se diferencian en el color y en las etiquetas con su nombre.\x7Entr\xc3\xa9nate derrotando a 4 chequebots.' },
    170: {
        QUEST: 'Muy bien, ya sabes en qu\xc3\xa9 se diferencian los cuatro tipos distintos de bots.\x7Creo que ya est\xc3\xa1s listo para empezar a entrenarte en el tercer circuito de trucos.\x7Ve a ver a _toNpcName_ para elegir el pr\xc3\xb3ximo circuito de trucos; \xc3\xa9l te aconsejar\xc3\xa1 bien._where_' },
    171: {
        QUEST: 'Muy bien, ya sabes en qu\xc3\xa9 se diferencian los cuatro tipos distintos de bots.\x7Creo que ya est\xc3\xa1s listo para empezar a entrenarte en el tercer circuito de trucos.\x7Ve a ver a _toNpcName_ para elegir el pr\xc3\xb3ximo circuito de trucos; \xc3\xa9l te aconsejar\xc3\xa1 bien._where_' },
    172: {
        QUEST: 'Muy bien, ya sabes en qu\xc3\xa9 se diferencian los cuatro tipos distintos de bots.\x7Creo que ya est\xc3\xa1s listo para empezar a entrenarte en el tercer circuito de trucos.\x7Ve a ver a _toNpcName_ para elegir el pr\xc3\xb3ximo circuito de trucos; ella te aconsejar\xc3\xa1 bien._where_' },
    400: {
        GREETING: '',
        QUEST: 'Las bromas de lanzamiento y chorro son estupendas, pero te har\xc3\xa1n falta otras para enfrentarte a los bots de niveles superiores.\x7Cuando te juntes con otros dibus para luchar contra los bots, podr\xc3\xa1s combinar ataques para infligirles m\xc3\xa1s da\xc3\xb1os. \x7Prueba con distintas combinaciones de trucos para ver cu\xc3\xa1les funcionan mejor.\x7En el siguiente circuito, escoge entre Sonido y Curadibu.\x7Sonido es una broma especial que causa da\xc3\xb1os a todos los bots al hacer impacto.\x7Curadibu te permite sanar a otros dibus durante el combate.\x7Cuando te hayas decidido, vuelve para elegir la broma que desees.',
        INCOMPLETE_PROGRESS: '\xc2\xbfYa has vuelto?  Vale, \xc2\xbfte has decidido ya?',
        INCOMPLETE_WRONG_NPC: 'Antes de elegir, medita tu decisi\xc3\xb3n.',
        COMPLETE: 'Buena decisi\xc3\xb3n.  Antes de usar esas bromas, deber\xc3\xa1s entrenarte con ellas.\x7En el entrenamiento tienes que completar una serie de dibutareas.\x7Cada tarea te proporcionar\xc3\xa1 un fotograma de la animaci\xc3\xb3n del ataque con la broma.\x7Cuando re\xc3\xbanas los 15, conseguir\xc3\xa1s la tarea final de entrenamiento, que te permitir\xc3\xa1 usar la nueva broma.\x7Comprueba c\xc3\xb3mo vas en el dibucuaderno.',
        LEAVING: QuestsDefaultLeaving },
    1039: {
        QUEST: 'Si quieres recorrer la ciudad m\xc3\xa1s f\xc3\xa1cilmente, ve a ver a _toNpcName_._where_' },
    1040: {
        QUEST: 'Si quieres recorrer la ciudad m\xc3\xa1s f\xc3\xa1cilmente, ve a ver a _toNpcName_._where_' },
    1041: {
        QUEST: '\xc2\xa1Hola!  \xc2\xbfQu\xc3\xa9 te trae por aqu\xc3\xad?\x7Todo el mundo usa los agujeros port\xc3\xa1tiles para viajar en Toontown.\x7Puedes teletransportarte al lugar donde est\xc3\xa1n tus amigos mediante la Lista de amigos, o a cualquier barrio con el mapa del dibucuaderno.\x7\xc2\xa1Desde luego, tendr\xc3\xa1s que gan\xc3\xa1rtelo!\x7Activar\xc3\xa9 tu acceso por teletransporte al centro de Toontown si ayudas a un amiguete m\xc3\xado.\x7Parece que los bots est\xc3\xa1n dando guerra en la calle Locuela.  Ve a ver a _toNpcName_._where_' },
    1042: {
        QUEST: '\xc2\xa1Hola!  \xc2\xbfQu\xc3\xa9 te trae por aqu\xc3\xad?\x7Todo el mundo usa los agujeros port\xc3\xa1tiles para viajar en Toontown.\x7Puedes teletransportarte al lugar donde est\xc3\xa1n tus amigos mediante la Lista de amigos, o a cualquier barrio con el mapa del dibucuaderno.\x7\xc2\xa1Desde luego, tendr\xc3\xa1s que gan\xc3\xa1rtelo!\x7Activar\xc3\xa9 tu acceso por teletransporte al centro de Toontown si ayudas a un amiguete m\xc3\xado.\x7Parece que los bots est\xc3\xa1n dando guerra en la calle Locuela.  Ve a ver a _toNpcName_._where_' },
    1043: {
        QUEST: '\xc2\xa1Hola!  \xc2\xbfQu\xc3\xa9 te trae por aqu\xc3\xad?\x7Todo el mundo usa los agujeros port\xc3\xa1tiles para viajar en Toontown.\x7Puedes teletransportarte al lugar donde est\xc3\xa1n tus amigos mediante la Lista de amigos, o a cualquier barrio con el mapa del dibucuaderno.\x7\xc2\xa1Desde luego, tendr\xc3\xa1s que gan\xc3\xa1rtelo!\x7Activar\xc3\xa9 tu acceso por teletransporte al centro de Toontown si ayudas a un amiguete m\xc3\xado.\x7Parece que los bots est\xc3\xa1n dando guerra en la calle Locuela.  Ve a ver a _toNpcName_._where_' },
    1044: {
        QUEST: 'Vaya, gracias por pasarte por aqu\xc3\xad.  La verdad es que necesito ayuda.\x7Como ves, no tengo clientes.\x7He perdido mi libro secreto de recetas y ya nadie viene a mi restaurante.\x7Lo vi por \xc3\xbaltima vez justo antes de que los bots ocupasen mi edificio.\x7\xc2\xbfPuedes ayudarme a recuperar cuatro famosas recetas m\xc3\xadas?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfHas conseguido encontrar mis recetas?' },
    1045: {
        QUEST: '\xc2\xa1Muchas gracias!\x7En poco tiempo tendr\xc3\xa9 todo el recetario y podr\xc3\xa9 volver a abrir mi restaurante.\x7Ah, tengo una nota para ti: algo sobre el teletransporte.\x7Dice Gracias por ayudar a mi amigo. Entrega esto en el Cuartel General Dibu.\x7De verdad, muchas gracias.\x7\xc2\xa1Adi\xc3\xb3s!',
        LEAVING: '',
        COMPLETE: 'Ah, s\xc3\xad, aqu\xc3\xad dice que has sido de gran ayuda para algunos de los amigos de la calle Locuela.\x7Dice que necesitas teletransportarte al centro de Toontown.\x7Pues bien, eso est\xc3\xa1 hecho.\x7Ahora puedes teletransportarte para volver al dibuparque desde casi cualquier lugar de Toontown.\x7Abre tu mapa y haz clic en Centro de Toontown.' },
    1046: {
        QUEST: 'Los chequebots han estado dando la lata en la Caja de Ahorros Pastagansa.\x7P\xc3\xa1sate por all\xc3\xad para ver si puedes hacer algo._where_' },
    1047: {
        QUEST: 'Los chequebots se han estado colando en el banco para robar nuestras calculadoras.\x7Recupera cinco calculadoras que han robado los chequebots.\x7Para no tener que estar yendo y viniendo, tr\xc3\xa1elas todas de una vez.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfSigues buscando las calculadoras?' },
    1048: {
        QUEST: '\xc2\xa1Vaya!  Gracias por recuperar nuestras calculadoras.\x7Mmm... Est\xc3\xa1n un poco estropeadas.\x7\xc2\xbfPuedes llev\xc3\xa1rselas a _toNpcName_ a su tienda, "Cosquilladores autom\xc3\xa1ticos" en esta calle?\x7Tal vez ella pueda arreglarlas.',
        LEAVING: '' },
    1049: {
        QUEST: '\xc2\xbfQu\xc3\xa9 es eso?  \xc2\xbfCalculadoras rotas?\x7\xc2\xbfChequebots, dices?\x7Um, veamos...\x7S\xc3\xad, han quitado los engranajes, pero no me quedan repuestos...\x7\xc2\xbfSabes que podr\xc3\xada servirnos? Unos engranajes de bots, grandes, de bots grandotes.\x7Los engranajes de bots de nivel 3 valdr\xc3\xa1n.  Necesito dos para cada m\xc3\xa1quina, as\xc3\xad que son diez en total.\x7\xc2\xa1Tr\xc3\xa1elos enseguida y los arreglar\xc3\xa9!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Recuerda que necesito diez engranajes para arreglar las calculadoras.' },
    1053: {
        QUEST: 'Muy bien, con esto seguro que vale.\x7Todas arregladas, es gratis.\x7Devu\xc3\xa9lveselas a Pastagansa y sal\xc3\xbadales de mi parte.',
        LEAVING: '',
        COMPLETE: '\xc2\xbfEst\xc3\xa1n arregladas todas las calculadoras?\x7Buen trabajo.  Seguro que tengo algo por aqu\xc3\xad con lo que recompensarte...' },
    1054: {
        QUEST: '_toNpcName_ necesita ayuda con sus coches de payasos._where_' },
    1055: {
        QUEST: '\xc2\xa1Hola!  \xc2\xa1No puedo encontrar por ning\xc3\xban sitio los neum\xc3\xa1ticos de este coche de payasos!\x7\xc2\xbfCrees que podr\xc3\xa1s echarme una mano?\x7Me parece que Perico Pirado los ha tirado al estanque del dibuparque del centro de Toontown. \x7Si te colocas encima de uno de los amarraderos del estanque podr\xc3\xa1s intentar pescar los neum\xc3\xa1ticos para tra\xc3\xa9rmelos.',
        GREETING: '\xc2\xa1Jujuj\xc3\xba!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfAlg\xc3\xban problemilla pescando los cuatro neum\xc3\xa1ticos?' },
    1056: {
        QUEST: '\xc2\xa1Estupend\xc3\xadsimo!  \xc2\xa1Ahora puedo volver a conducir este viejo coche de payasos!\x7Eh, cre\xc3\xada que ten\xc3\xada una vieja bomba de aire por aqu\xc3\xad para inflar estos neum\xc3\xa1ticos...\x7\xc2\xbfSe la habr\xc3\xa1 llevado prestada _toNpcName_?\x7\xc2\xbfPodr\xc3\xadas hacerme el favor de pedirle que me la devuelva?_where_',
        LEAVING: '' },
    1057: {
        QUEST: '\xc2\xbfQu\xc3\xa9 tal?\x7\xc2\xbfUna bomba de aire, dices?\x7\xc2\xbfSabes lo que te digo? Si me ayudas a limpiar las calles de algunos de esos bots de nivel alto...\x7Te dar\xc3\xa9 la bomba de aire.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfEso es todo lo que sabes hacer?' },
    1058: {
        QUEST: 'Buen trabajo, sab\xc3\xada que lo conseguir\xc3\xadas.\x7Aqu\xc3\xad est\xc3\xa1 la bomba.  Seguro que _toNpcName_ se alegra de recuperarla.',
        LEAVING: '',
        GREETING: '',
        COMPLETE: '\xc2\xa1Yujuuu!  \xc2\xa1Ya puedo conducir!\x7Por cierto, gracias por ayudarme.\x7Toma esto.' },
    1059: {
        QUEST: '_toNpcName_ se est\xc3\xa1 quedando sin suministros.  \xc2\xbfPuedes echarle una mano?_where_' },
    1060: {
        QUEST: '\xc2\xa1Gracias por venir!\x7Esos bots han estado rob\xc3\xa1ndome la tinta, y casi no me queda nada.\x7\xc2\xbfPodr\xc3\xadas pescar un poco de tinta de pulpo en el estanque?\x7Para pescar, basta con que te sit\xc3\xbaes en el amarradero de la orilla.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfHas tenido problemas para pescar?' },
    1061: {
        QUEST: '\xc2\xa1Estupendo, gracias por la tinta!\x7\xc2\xbfSabes qu\xc3\xa9? Si quitases de en medio a unos cuantos de esos chupatintas...\x7No me quedar\xc3\xada sin tinta tan r\xc3\xa1pidamente.\x7Derrota a seis chupatintas en el centro de Toontown para llevarte una recompensa.',
        LEAVING: '',
        COMPLETE: '\xc2\xa1Gracias!  Te recompensar\xc3\xa9 por tu ayuda.',
        INCOMPLETE_PROGRESS: 'He visto unos cuantos chupatintas m\xc3\xa1s.' },
    1062: {
        QUEST: '\xc2\xa1Estupendo, gracias por la tinta!\x7\xc2\xbfSabes qu\xc3\xa9? Si quitases de en medio a unos cuantos de esos chupasangres...\x7No me quedar\xc3\xada sin tinta tan r\xc3\xa1pidamente.\x7Derrota a seis chupasangres en el centro de Toontown para llevarte una recompensa.',
        LEAVING: '',
        COMPLETE: '\xc2\xa1Gracias!  Te recompensar\xc3\xa9 por tu ayuda.',
        INCOMPLETE_PROGRESS: 'He visto unos cuantos chupasangres m\xc3\xa1s.' },
    900: {
        QUEST: 'He o\xc3\xaddo que _toNpcName_ necesita ayuda con un paquete._where_' },
    1063: {
        QUEST: '\xc2\xa1Hola, gracias por venir!\x7Un bot me ha robado un paquete muy importante delante de mis narices.\x7Por favor, intenta recuperarlo.  Creo que era de nivel 3...\x7As\xc3\xad que tendr\xc3\xa1s que derrotar a bots de nivel 3 hasta que encuentres mi paquete.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No ha habido suerte con el paquete, \xc2\xbfeh?' },
    1067: {
        QUEST: '\xc2\xa1\xc3\x89se es, muy bien!\x7Eh, la direcci\xc3\xb3n est\xc3\xa1 borrosa...\x7S\xc3\xb3lo se lee que es para un doctor, el resto est\xc3\xa1 emborronado.\x7\xc2\xbfSer\xc3\xa1 para _toNpcName_?  \xc2\xbfPuedes llev\xc3\xa1rselo?_where_',
        LEAVING: '' },
    1068: {
        QUEST: 'No esperaba ning\xc3\xban paquete.  Quiz\xc3\xa1 sea para el doctor Eufo Rico.\x7Mi ayudante iba a ir all\xc3\xad hoy de todas formas, as\xc3\xad que le dir\xc3\xa9 que se lo pregunte.\x7Mientras tanto, \xc2\xbfte importa deshacerte de unos cuantos bots en mi calle?\x7Derrota a diez bots en el centro de Toontown.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Mi ayudante no ha vuelto todav\xc3\xada.' },
    1069: {
        QUEST: 'El doctor Eufo Rico no esperaba un paquete, tampoco.\x7Por desgracia, un chequebot se lo ha robado a mi ayudante cuando volv\xc3\xada.\x7\xc2\xbfPodr\xc3\xadas intentar recuperarlo?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No ha habido suerte con el paquete, \xc2\xbfeh?' },
    1070: {
        QUEST: 'El doctor Eufo Rico no esperaba un paquete, tampoco.\x7Por desgracia, un vendebot se lo ha robado a mi ayudante cuando volv\xc3\xada.\x7Lo siento, pero tendr\xc3\xa1s que encontrar a ese vendebot para recuperarlo.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No ha habido suerte con el paquete, \xc2\xbfeh?' },
    1071: {
        QUEST: 'El doctor Eufo Rico no esperaba un paquete, tampoco.\x7Por desgracia, un jefebot se lo ha robado a mi ayudante cuando volv\xc3\xada.\x7\xc2\xbfPodr\xc3\xadas intentar recuperarlo?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No ha habido suerte con el paquete, \xc2\xbfeh?' },
    1072: {
        QUEST: '\xc2\xa1Estupendo, lo has recuperado!\x7Deber\xc3\xadas probar con _toNpcName_, puede que sea para \xc3\xa9l._where_',
        LEAVING: '' },
    1073: {
        QUEST: 'Oh, gracias por traerme mis paquetes.\x7Espera un momento, estaba esperando dos.  \xc2\xbfPodr\xc3\xadas ir a ver a _toNpcName_ para preguntarle si tiene el otro?',
        INCOMPLETE: '\xc2\xbfHas conseguido encontrar mi otro paquete?',
        LEAVING: '' },
    1074: {
        QUEST: '\xc2\xbfHa dicho que hab\xc3\xada otro paquete?  A lo mejor lo han robado tambi\xc3\xa9n los bots.\x7Derrota a bots hasta que encuentres el segundo paquete.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No ha habido suerte con el otro paquete, \xc2\xbfeh?' },
    1075: {
        QUEST: '\xc2\xa1Al final resulta que s\xc3\xad que hab\xc3\xada un segundo paquete!\x7Deprisa, ll\xc3\xa9vaselo a _toNpcName_ y p\xc3\xaddele disculpas de mi parte.',
        COMPLETE: '\xc2\xa1Eh, ha llegado mi paquete!\x7Como pareces ser un dibu muy servicial, esto te vendr\xc3\xa1 bien.',
        LEAVING: '' },
    1076: {
        QUEST: 'Ha habido problemas en Peces dorados de 14 kilates.\x7A _toNpcName_ le vendr\xc3\xa1 bien una ayudita._where_' },
    1077: {
        QUEST: 'Gracias por venir. Los bots han robado todos mis peces dorados.\x7Creo que quieren venderlos para sacar un dinero r\xc3\xa1pido.\x7Esos cinco peces han sido mi \xc3\xbanica compa\xc3\xb1\xc3\xada en esta tiendecita durante tantos a\xc3\xb1os...\x7Si pudieses hacerme el favor de recuperarlos, te lo agradecer\xc3\xada eternamente.\x7Seguro que uno de los bots tiene mis peces.\x7Derrota a bots hasta que encuentres mis peces.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Por favor, recupera mis peces dorados.' },
    1078: {
        QUEST: '\xc2\xa1Oh, tienes mis peces!\x7\xc2\xbfEh?  \xc2\xbfQu\xc3\xa9 es eso? \xc2\xbfUn recibo?\x7Ah, s\xc3\xad son los bots, a fin de cuentas.\x7No consigo averiguar qu\xc3\xa9 diantre es este recibo.  \xc2\xbfPodr\xc3\xadas llev\xc3\xa1rselo a _toNpcName_ para ver si \xc3\xa9l lo entiende?_where_',
        INCOMPLETE: '\xc2\xbfQu\xc3\xa9 ha dicho _toNpcName_ del recibo?',
        LEAVING: '' },
    1079: {
        QUEST: 'Mmm, d\xc3\xa9jame ver ese recibo.\x7... Ah, s\xc3\xad, dice que un pez dorado fue vendido a un secuaz.\x7No menciona para nada qu\xc3\xa9 ha sido de los otros cuatro peces.\x7Quiz\xc3\xa1 debas ponerte a buscar a ese secuaz.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No creo que te pueda ayudar m\xc3\xa1s.\x7\xc2\xbfPor qu\xc3\xa9 no te pones a buscar ese pez dorado?' },
    1092: {
        QUEST: 'Mmm, d\xc3\xa9jame ver ese recibo.\x7... Ah, s\xc3\xad, dice que un pez dorado fue vendido a un calderilla.\x7No menciona para nada qu\xc3\xa9 ha sido de los otros cuatro peces.\x7Quiz\xc3\xa1 debas ponerte a buscar a ese calderilla.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No creo que te pueda ayudar m\xc3\xa1s.\x7\xc2\xbfPor qu\xc3\xa9 no te pones a buscar ese pez dorado?' },
    1080: {
        QUEST: '\xc2\xa1Oh, gracias a Dios!  Has encontrado a \xc3\x93scar. Es mi favorito.\x7\xc2\xbfQu\xc3\xa9 pasa, \xc3\x93scar?  Oh, vaya... \xc2\xbfde verdad? ... \xc2\xbfEst\xc3\xa1n all\xc3\xad?\x7\xc3\x93scar dice que los otros cuatro escaparon y se metieron en el estanque del dibuparque.\x7\xc2\xbfMe haces el favor de ir a recogerlos? \x7Basta con que los pesques en el estanque.',
        LEAVING: '',
        COMPLETE: '\xc2\xa1Oooh, qu\xc3\xa9 contento estoy!  \xc2\xa1Por fin vuelvo a estar junto a mis amiguitos!\x7\xc2\xa1Te mereces una estupenda recompensa!',
        INCOMPLETE_PROGRESS: '\xc2\xbfTe est\xc3\xa1 costando encontrar a los peces?' },
    1081: {
        QUEST: 'Parece ser que _toNpcName_ se encuentra en una situaci\xc3\xb3n pegajosa.  Seguro que le vendr\xc3\xa1 bien una ayudita._where_' },
    1082: {
        QUEST: '\xc2\xa1Se me ha derramado el pegamento r\xc3\xa1pido y me he quedado pegado!\x7Si pudiera hacer algo para liberarme...\x7Se me ocurre una idea, si te sientes valiente.\x7Derrota a unos vendebots y tr\xc3\xa1eme un poco de aceite.',
        LEAVING: '',
        GREETING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfPuedes ayudarme a despegarme?' },
    1083: {
        QUEST: 'El aceite ha ayudado, pero sigo sin despegarme del todo.\x7\xc2\xbfQu\xc3\xa9 puedo probar?  Nada procede.\x7Se me ocurre una idea, por probarla no pasa nada.\x7Derrota a unos abogabots y tr\xc3\xa1eme un poco de grasa.',
        LEAVING: '',
        GREETING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfPuedes ayudarme a despegarme?' },
    1084: {
        QUEST: 'No, no ha servido de nada.  Esto no me divierte.\x7He puesto la grasa y no ha habido suerte.\x7Se me ocurre una idea para sacarme de aqu\xc3\xad.\x7Derrota a unos chequebots y trae agua para mojarme.',
        LEAVING: '',
        GREETING: '',
        COMPLETE: '\xc2\xa1Hurra! Estoy libre de este pegamento rapido.\x7Como recompensa, toma este obsequio.\x7Podr\xc3\xa1s disfrutar de una combativa velada...\x7\xc2\xa1Oh, no!  \xc2\xa1He vuelto a quedarme pegado!',
        INCOMPLETE_PROGRESS: '\xc2\xbfPuedes ayudarme a despegarme?' },
    1085: {
        QUEST: '_toNpcName_ est\xc3\xa1 llevando a cabo ciertas investigaciones sobre los bots.\x7Vete a hablar con \xc3\xa9l si quieres ayudarle._where_' },
    1086: {
        QUEST: 'Efectivamente, estoy realizando un estudio sobre los bots.\x7Quiero saber c\xc3\xb3mo funcionan.\x7Me ser\xc3\xada de gran ayuda que consiguieses algunos engranajes de bot.\x7Aseg\xc3\xbarate de que pertenezcan a bots de nivel 2 al menos, para que tengan el tama\xc3\xb1o suficiente para examinarlos.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfNo puedes conseguir suficientes engranajes?' },
    1089: {
        QUEST: 'Muy bien, veamos.  \xc2\xa1Excelentes espec\xc3\xadmenes!\x7Mmm...\x7De acuerdo, aqu\xc3\xad est\xc3\xa1 mi informe.  Lleva esto enseguida al cuartel general dibu.',
        INCOMPLETE: '\xc2\xbfHas llevado mi informe al cuartel general?',
        COMPLETE: 'Buen trabajo, _avName_, a partir de ahora nos ocuparemos nosotros.',
        LEAVING: '' },
    1090: {
        QUEST: '_toNpcName_ tiene informaci\xc3\xb3n \xc3\xbatil para ti._where_' },
    1091: {
        QUEST: 'He o\xc3\xaddo que en el cuartel general dibu est\xc3\xa1n trabajando en una especie de radar de bots.\x7Te permitir\xc3\xa1 ver d\xc3\xb3nde est\xc3\xa1n los bots y as\xc3\xad poder encontrarlos m\xc3\xa1s f\xc3\xa1cilmente.\x7La p\xc3\xa1gina Bot del dibucuaderno es la clave.\x7Si derrotas suficientes bots, podr\xc3\xa1s sintonizar sus se\xc3\xb1ales y detectar su paradero.\x7Sigue derrotando a los bots para estar listo.',
        COMPLETE: '\xc2\xa1Buen trabajo!  Seguro que esto te viene bien...',
        LEAVING: '' },
    401: {
        GREETING: '',
        QUEST: 'Ahora tienes que elegir el nuevo circuito de trucos que quieres aprender.\x7Pi\xc3\xa9nsatelo todo lo que quieras y vuelve cuando hayas tomado una decisi\xc3\xb3n.',
        INCOMPLETE_PROGRESS: 'Antes de elegir, medita tu decisi\xc3\xb3n.',
        INCOMPLETE_WRONG_NPC: 'Antes de elegir, medita tu decisi\xc3\xb3n.',
        COMPLETE: 'Muy buena decisi\xc3\xb3n...',
        LEAVING: QuestsDefaultLeaving },
    2201: {
        QUEST: 'Esos bots tan pesados est\xc3\xa1n dando problemas otra vez.\x7_toNpcName_ ha informado de que falta otro objeto. P\xc3\xa1sate por all\xc3\xad, a ver si puedes arreglar la situaci\xc3\xb3n._where_' },
    2202: {
        QUEST: 'Hola, _avName_. Gracias a Dios que has venido. Un cacomatraco acaba de pasar por aqu\xc3\xad y se ha largado corriendo con un tubo interno.\x7Temo que lo usen para sus malvados prop\xc3\xb3sitos.\x7Por favor, busca al bot y recupera el tubo.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfHas conseguido encontrar mi tubo interno?',
        COMPLETE: '\xc2\xa1Has encontrado mi tubo interno! Eres SENSACIONAL. Aqu\xc3\xad tienes tu recompensa...' },
    2203: {
        QUEST: 'Los bots est\xc3\xa1n sembrando el caos en el banco.\x7Ve a ver al capit\xc3\xa1n Dobl\xc3\xb3n, a ver qu\xc3\xa9 puedes hacer._where_' },
    2204: {
        QUEST: 'Bienvenido a bordo, grumete.\x7\xc2\xa1Arg! Esa escoria de bots han aplastado mi mon\xc3\xb3culo y no me puedo apa\xc3\xb1ar sin \xc3\xa9l.\x7S\xc3\xa9 un buen marinero y lleva esta prescripci\xc3\xb3n al doctor Rompecubiertas para que me haga uno nuevo._where_.',
        GREETING: '',
        LEAVING: '' },
    2205: {
        QUEST: '\xc2\xbfQu\xc3\xa9 es esto?\x7Me encantar\xc3\xada hacer este mon\xc3\xb3culo, pero los bots han estado saqueando mis existencias.\x7Si consigues arrebatarle las monturas de mon\xc3\xb3culo a un secuaz, me ser\xc3\xa1s de gran ayuda.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Lo siento. Si no tengo las monturas del secuaz, no hay mon\xc3\xb3culo.' },
    2206: {
        QUEST: '\xc2\xa1Excelente!\x7Un momento...\x7Aqu\xc3\xad tienes el mon\xc3\xb3culo de la prescripci\xc3\xb3n. Ll\xc3\xa9vaselo al capit\xc3\xa1n Dobl\xc3\xb3n._where_',
        GREETING: '',
        LEAVING: '',
        COMPLETE: '\xc2\xa1Avante a toda!\x7No, si al final te vas a ganar los galones y todo.\x7Aqu\xc3\xad tienes.' },
    2207: {
        QUEST: '\xc2\xa1Perci Percebe tiene un bot en la tienda!\x7M\xc3\xa1s vale que vayas para all\xc3\xa1 enseguida._where_' },
    2208: {
        QUEST: '\xc2\xa1Vaya! Se te acaba de escapar, cari\xc3\xb1o.\x7Aqu\xc3\xad hab\xc3\xada un apu\xc3\xb1alaespaldas.  Se ha llevado mi peluca blanca grande.\x7Ha dicho que era para su jefe, y no s\xc3\xa9 qu\xc3\xa9 sobre un "precedente legal".\x7Si pudieses recuperarla, te estar\xc3\xada eternamente agradecida.',
        LEAVING: '',
        GREETING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfTodav\xc3\xada no lo has encontrado?\x7Es alto y tiene la cabeza puntiaguda.',
        COMPLETE: '\xc2\xa1La has encontrado!\x7\xc2\xa1Eres todo un encanto!\x7Te has ganado esto, sin duda...' },
    2209: {
        QUEST: 'Isidoro se est\xc3\xa1 preparando para un viaje importante.\x7Ac\xc3\xa9rcate a ver en qu\xc3\xa9 puedes ayudarle._where_' },
    2210: {
        QUEST: 'Puedo utilizar tu ayuda.\x7En el cuartel general dibu me han pedido que haga un viaje para averiguar de d\xc3\xb3nde proceden los bots.\x7Necesito unas cuantas cosas para mi barco, pero ando escaso de gominolas.\x7P\xc3\xa1sate a ver a Pepa Sastre para que te d\xc3\xa9 algo de lastre. Para conseguirlo, tendr\xc3\xa1s que hacerle un favor._where_',
        GREETING: '\xc2\xbfQu\xc3\xa9 hay, _avName_?',
        LEAVING: '' },
    2211: {
        QUEST: 'As\xc3\xad que Isidoro quiere lastre, \xc2\xbfeh?\x7Todav\xc3\xada me debe la \xc3\xbaltima fanega.\x7Te la dar\xc3\xa9 si consigues limpiar mi calle de cinco microgerentes.',
        INCOMPLETE_PROGRESS: '\xc2\xa1No, tonto! \xc2\xa1He dicho CINCO microgerentes!...',
        GREETING: '\xc2\xbfQu\xc3\xa9 puedo hacer por ti?',
        LEAVING: '' },
    2212: {
        QUEST: 'Un trato es un trato.\x7Aqu\xc3\xad tienes el lastre para ese taca\xc3\xb1o de Isidoro._where_',
        GREETING: 'Vaya, mira lo que aparece por aqu\xc3\xad...',
        LEAVING: '' },
    2213: {
        QUEST: 'Gran trabajo. Sab\xc3\xada que se atendr\xc3\xada a razones. \x7Ahora necesito una carta n\xc3\xa1utica de Pasma Rote.\x7No creo que me f\xc3\xaden all\xc3\xad tampoco, as\xc3\xad que tendr\xc3\xa1s que llegar a un acuerdo con \xc3\xa9l._where_.',
        GREETING: '',
        LEAVING: '' },
    2214: {
        QUEST: 'S\xc3\xad, tengo la carta de navegaci\xc3\xb3n que necesita Isidoro.\x7Y te la dar\xc3\xa9 si est\xc3\xa1s dispuesto a trabajar para conseguirla.\x7Estoy intentando construir un astrolabio para orientarme con las estrellas.\x7Para hacerlo necesito tres engranajes de bot.\x7Vuelve cuando los hayas conseguido.',
        INCOMPLETE_PROGRESS: '\xc2\xbfQu\xc3\xa9 tal te va con los engranajes de bot?',
        GREETING: '\xc2\xa1Bienvenido!',
        LEAVING: '\xc2\xa1Buena suerte!' },
    2215: {
        QUEST: '\xc2\xa1Oooh! Estos engranajes me vendr\xc3\xa1n muy bien.\x7Aqu\xc3\xad tienes la carta. D\xc3\xa1sela a Isidoro, y dale recuerdos._where_',
        GREETING: '',
        LEAVING: '',
        COMPLETE: 'Bueno, esto es todo. \xc2\xa1Estoy listo para zarpar!\x7Te dejar\xc3\xada acompa\xc3\xb1arme si no estuvieses tan verde. A cambio, toma esto.' },
    901: {
        QUEST: 'Si est\xc3\xa1s disponible, a Ajab le vendr\xc3\xada bien una ayuda._where_' },
    2902: {
        QUEST: '\xc2\xbfT\xc3\xba eres el nuevo recluta?\x7Bien, bien. Tal vez puedas ayudarme.\x7Estoy construyendo un gigantesco cangrejo prefabricado para confundir a los bots.\x7Aunque tambi\xc3\xa9n me servir\xc3\xada una coraza. Ve a ver a Clodovico Croma\xc3\xb1\xc3\xb3n y p\xc3\xaddele una, por favor._where_' },
    2903: {
        QUEST: '\xc2\xa1Muy buenas!\x7S\xc3\xad, he o\xc3\xaddo hablar del cangrejo gigante en el que trabaja Ajab.\x7Sin embargo, la mejor coraza que tengo est\xc3\xa1 un poco sucia.\x7P\xc3\xb3rtate bien y ll\xc3\xa9vala a la tintorer\xc3\xada antes de entregarla._where_',
        LEAVING: '\xc2\xa1Gracias!' },
    2904: {
        QUEST: 'Debes de ser el que viene de parte de Clodovico.\x7Creo que puedo limpiar eso en un santiam\xc3\xa9n.\x7Dame un minuto...\x7Aqu\xc3\xad tienes. \xc2\xa1Como nuevo!\x7Saluda a Ajab de mi parte._where_' },
    2905: {
        QUEST: 'Vaya, esto es exactamente lo que andaba buscando.\x7Ya que est\xc3\xa1s aqu\xc3\xad, tambi\xc3\xa9n voy a necesitar un resorte de reloj muy grande.\x7P\xc3\xa1sate por la tienda de Garfio para ver si tiene uno._where_' },
    2906: {
        QUEST: 'Un resorte grande, \xc2\xbfeh?\x7Lo siento, pero el m\xc3\xa1s grande que tengo es bastante peque\xc3\xb1o, en realidad.\x7Quiz\xc3\xa1s pueda hacer uno con los resortes de los gatillos de pistola de agua.\x7Tr\xc3\xa1eme tres de esos chismes y ver\xc3\xa9 que puedo hacer.' },
    2907: {
        QUEST: 'Veamos...\x7Impresionante. Simplemente impresionante.\x7A veces me sorprendo a m\xc3\xad mismo.\x7Aqu\xc3\xad tienes: un resorte grande para Ajab._where_',
        LEAVING: '\xc2\xa1Buen viaje!' },
    2911: {
        QUEST: 'Me encantar\xc3\xada ayudar a la causa, _avName_.\x7Pero me temo que las calles ya no son seguras.\x7\xc2\xbfPor qu\xc3\xa9 no acabas con unos cuantos chequebots? Despu\xc3\xa9s hablaremos.',
        INCOMPLETE_PROGRESS: 'Creo que las calles no son todav\xc3\xada muy seguras que digamos.' },
    2911: {
        QUEST: 'Me encantar\xc3\xada ayudar a la causa, _avName_.\x7Pero me temo que las calles ya no son seguras.\x7\xc2\xbfPor qu\xc3\xa9 no acabas con unos cuantos chequebots? Despu\xc3\xa9s hablaremos.',
        INCOMPLETE_PROGRESS: 'Creo que las calles no son todav\xc3\xada muy seguras que digamos.' },
    2916: {
        QUEST: 'S\xc3\xad, tengo un contrapeso que le vendr\xc3\xada bien a Ajab.\x7Sin embargo, creo que ser\xc3\xada mejor que antes derrotases a un par de vendebots.',
        INCOMPLETE_PROGRESS: 'Todav\xc3\xada no. Derrota a unos cuantos vendebots m\xc3\xa1s.' },
    2921: {
        QUEST: 'Mmm, se supone que tengo que darte un contrapeso.\x7Pero me sentir\xc3\xada mucho m\xc3\xa1s seguro si no hubiese tantos jefebots rondando por aqu\xc3\xad.\x7Derrota a seis y ven a verme.',
        INCOMPLETE_PROGRESS: 'Creo que esta zona todav\xc3\xada no es segura...' },
    2925: {
        QUEST: '\xc2\xbfHas acabado?\x7Bien, supongo que la zona ya es bastante segura.\x7Aqu\xc3\xad tienes el contrapeso para Ajab._where_' },
    2926: {
        QUEST: 'Bueno, eso es todo.\x7Veamos si funciona.\x7Mmm, hay un peque\xc3\xb1o problema.\x7No puedo encenderlo porque ese edificio bot est\xc3\xa1 tapando mi panel solar.\x7\xc2\xbfPuedes hacerme el favor de reconquistarlo?',
        INCOMPLETE_PROGRESS: 'Sigo sin tener electricidad. \xc2\xbfQu\xc3\xa9 hay de ese edificio?',
        COMPLETE: '\xc2\xa1Estupendo! \xc2\xa1Se te da de miedo zurrar a los bots! Toma, aqu\xc3\xad tienes tu recompensa...' },
    3200: {
        QUEST: 'Acabo de recibir una llamada de _toNpcName_.\x7Est\xc3\xa1 teniendo un d\xc3\xada de perros. Tal vez puedas ayudarle.\x7P\xc3\xa1sate por all\xc3\xad para ver qu\xc3\xa9 necesita._where_' },
    3201: {
        QUEST: '\xc2\xa1Vaya, gracias por venir!\x7Necesito que alguien lleve esta corbata de seda nueva a _toNpcName_.\x7\xc2\xbfMe har\xc3\xadas t\xc3\xba ese favor?_where_' },
    3203: {
        QUEST: '\xc2\xa1Ah, \xc3\xa9sta debe de ser la corbata que he encargado! \xc2\xa1Gracias!\x7Va a juego con el traje mil rayas que acabo de terminar, justo ah\xc3\xad.\x7Eh, \xc2\xbfqu\xc3\xa9 ha pasado con el traje?\x7\xc2\xa1Oh, no! \xc2\xa1Los bots deben de haberme robado el traje nuevo!\x7Lucha con los bots hasta que encuentres el traje y tr\xc3\xa1emelo.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfHas encontrado ya mi traje? \xc2\xa1Seguro que se lo han llevado los bots!',
        COMPLETE: '\xc2\xa1Hurra! \xc2\xa1Has encontrado mi traje nuevo!\x7\xc2\xbfVes? Te dije que los bots lo ten\xc3\xadan. Toma tu recompensa...' },
    3204: {
        QUEST: '_toNpcName_ acaba de llamar para informar de un robo.\x7\xc2\xbfPor qu\xc3\xa9 no te pasas por all\xc3\xad para ver si puedes arreglar la situaci\xc3\xb3n?_where_' },
    3205: {
        QUEST: '\xc2\xa1Hola, _avName_! \xc2\xbfHas venido a ayudarme?\x7Acabo de ahuyentar a un chupasangres de mi tienda. \xc2\xa1Guau! Daba mucho miedo.\x7\xc2\xa1Pero ahora no puedo encontrar las tijeras! Seguro que se las ha llevado el chupasangres.\x7Por favor, busca al chupasangres y recupera las tijeras.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfSigues buscando las tijeras?',
        COMPLETE: '\xc2\xa1Mis tijeras! \xc2\xa1Muchas gracias! Toma tu recompensa...' },
    3206: {
        QUEST: 'Parece ser que _toNpcName_ est\xc3\xa1 teniendo alg\xc3\xban que otro problema con los bots.\x7Ve a ver si puedes ayudarle._where_' },
    3207: {
        QUEST: '\xc2\xa1Buenas, _avName_! \xc2\xa1Gracias por venir!\x7Unos cuantos embaucadores han entrado y se han llevado un taco de postales del mostrador.\x7\xc2\xa1Por favor, derrota a esos embaucadores y recupera mis postales!',
        INCOMPLETE_PROGRESS: '\xc2\xa1No hay postales suficientes! \xc2\xa1Sigue buscando!',
        COMPLETE: '\xc2\xa1Oh, gracias! \xc2\xa1Ahora puedo entregar el correo a tiempo! Toma tu recompensa...' },
    3208: {
        QUEST: 'Hemos estado recibiendo quejas de los vecinos sobre todos esos gorrones.\x7Por favor, intenta derrotar a diez gorrones para ayudar a tus amigos, los dibus de los Jardines de Daisy. ' },
    3209: {
        QUEST: '\xc2\xa1Gracias por ocuparte de los gorrones!\x7\xc2\xa1Pero ahora los televendedores se han desmadrado!\x7Derrota a diez televendedores en los Jardines de Daisy y vuelve para llevarte una recompensa.' },
    3247: {
        QUEST: 'Hemos estado recibiendo quejas de los vecinos sobre todos esos chupasangres.\x7Por favor, intenta derrotar a veinte chupasangres para ayudar a tus amigos, los dibus de los Jardines de Daisy. ' },
    3210: {
        QUEST: '\xc2\xa1Oh, no, La flor chorreante, de la calle Arce, se ha quedado sin flores!\x7Ll\xc3\xa9vales diez flores chorreantes de las tuyas para ayudarles. \x7Primero comprueba que tienes diez flores chorreantes en el inventario.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Necesito diez flores chorreantes. \xc2\xa1No tienes suficientes!' },
    3211: {
        QUEST: '\xc2\xa1Oh, muchas gracias! Esas flores arreglar\xc3\xa1n la situaci\xc3\xb3n.\x7Pero los bots que hay fuera me dan miedo.\x7\xc2\xbfPuedes ayudarme derrotando a unos cuantos?\x7Vuelve cuando hayas derrotado a veinte bots en esta calle.',
        INCOMPLETE_PROGRESS: '\xc2\xa1Todav\xc3\xada quedan bots ah\xc3\xad fuera!  \xc2\xa1Sigue luchando!',
        COMPLETE: '\xc2\xa1Oh, gracias! Me has ayudado un mont\xc3\xb3n. Tu recompensa es...' },
    3212: {
        QUEST: '_toNpcName_ necesita ayuda para encontrar una cosa que ha perdido.\x7Ve a verla, tal vez puedas ayudarla._where_' },
    3213: {
        QUEST: 'Hola, _avName_. \xc2\xbfPuedes ayudarme?\x7Parece que he perdido mi pluma estilogr\xc3\xa1fica. Creo que se la han llevado unos bots.\x7Derr\xc3\xb3talos y recupera la pluma, por favor.',
        INCOMPLETE_PROGRESS: '\xc2\xbfHas encontrado ya mi pluma?' },
    3214: {
        QUEST: '\xc2\xa1S\xc3\xad, \xc3\xa9sa es! \xc2\xa1Muchas gracias!\x7Pero en cuanto te has marchado me he dado cuenta de que tambi\xc3\xa9n me faltaba el tintero.\x7Vence a los bots y recupera el tintero, por favor.',
        INCOMPLETE_PROGRESS: '\xc2\xa1Sigo buscando el tintero!' },
    3215: {
        QUEST: '\xc2\xa1Fant\xc3\xa1stico! Ahora he recuperado la pluma y el tintero.\x7Pero \xc2\xbfa que no te lo imaginas?\x7\xc2\xa1No encuentro la libreta! \xc2\xa1La deben haber robado tambi\xc3\xa9n!\x7Derrota a los bots hasta que encuentres la libreta y tr\xc3\xa1emela para que te d\xc3\xa9 una recompensa.',
        INCOMPLETE_PROGRESS: '\xc2\xbfAlguna novedad sobre la libreta?' },
    3216: {
        QUEST: '\xc2\xa1\xc3\x89sa es mi libreta! \xc2\xa1Hurra! Tu recompensa es...\x7\xc2\xa1Eh! \xc2\xbfD\xc3\xb3nde est\xc3\xa1?\x7Ten\xc3\xada tu recompensa justo aqu\xc3\xad, en la caja de seguridad. \xc2\xa1Pero se la han llevado!\x7\xc2\xbfPuedes creerlo? \xc2\xa1Los bots han robado tu recompensa!\x7Vence a los bots para recuperar la caja de seguridad.\x7Cuando me la traigas, te dar\xc3\xa9 tu recompensa.',
        INCOMPLETE_PROGRESS: '\xc2\xa1Sigue buscando la caja de seguridad!  \xc2\xa1Tu recompensa est\xc3\xa1 dentro!',
        COMPLETE: '\xc2\xa1Por fin! Ten\xc3\xada tu nueva bolsa de bromas en la caja. Aqu\xc3\xad est\xc3\xa1...' },
    3217: {
        QUEST: 'Hemos estado estudiando la mec\xc3\xa1nica de los vendebots.\x7Queremos estudiar m\xc3\xa1s de cerca algunas piezas.\x7Tr\xc3\xa1enos la rueda dentada de un fardoncete.\x7Puedes atraparlas cuando los bots estallan.' },
    3218: {
        QUEST: '\xc2\xa1Buen trabajo! Ahora tenemos que compararla con la rueda dentada de un efusivo.\x7Esas ruedas dentadas son m\xc3\xa1s dif\xc3\xadciles de atrapar, as\xc3\xad que sigue intent\xc3\xa1ndolo.' },
    3219: {
        QUEST: '\xc2\xa1Fant\xc3\xa1stico! Ahora s\xc3\xb3lo necesitamos una rueda dentada m\xc3\xa1s.\x7Esta vez necesitamos la rueda de un mandam\xc3\xa1s.\x7Para encontrar a estos bots, tal vez tengas que buscar en el interior de algunos edificios de vendebots.\x7Cuando la tengas, tr\xc3\xa1ela, y a cambio obtendr\xc3\xa1s tu recompensa.' },
    3244: {
        QUEST: 'Hemos estado estudiando la mec\xc3\xa1nica de los abogabots.\x7Queremos estudiar m\xc3\xa1s de cerca algunas piezas.\x7Tr\xc3\xa1enos la rueda dentada de un persigueambulancias.\x7Puedes atraparlas cuando los bots estallan.' },
    3245: {
        QUEST: '\xc2\xa1Buen trabajo! Ahora tenemos que compararla con la rueda dentada de un apu\xc3\xb1alaespaldas.\x7Esas ruedas dentadas son m\xc3\xa1s dif\xc3\xadciles de atrapar, as\xc3\xad que sigue intent\xc3\xa1ndolo.' },
    3246: {
        QUEST: '\xc2\xa1Fant\xc3\xa1stico! Ahora s\xc3\xb3lo necesitamos una rueda dentada m\xc3\xa1s.\x7Esta vez necesitamos la rueda de un portavoz.\x7Cuando la tengas, tr\xc3\xa1ela para obtener a cambio tu recompensa.' },
    3220: {
        QUEST: 'Acabo de o\xc3\xadr que _toNpcName_ estaba preguntando por ti.\x7\xc2\xbfPor qu\xc3\xa9 no pasas a verla para ver qu\xc3\xa9 quiere?_where_' },
    3221: {
        QUEST: '\xc2\xa1Buenas, _avName_! \xc2\xa1Aqu\xc3\xad est\xc3\xa1s!\x7He o\xc3\xaddo que eres todo un experto en ataques chorreantes.\x7Necesito a alguien que d\xc3\xa9 un buen ejemplo a todos los dibus de Jardines de Daisy.\x7Usa tus ataques chorreantes para derrotar a un mont\xc3\xb3n de bots.\x7Anima a tus amigos a usar este tipo de ataques.\x7Cuando hayas derrotado a veinte bots, vuelve para llevarte una recompensa.' },
    3222: {
        QUEST: 'Ha llegado el momento de demostrar tu dibupunter\xc3\xada.\x7Si consigues recuperar cierto n\xc3\xbamero de edificios bot, tendr\xc3\xa1s el privilegio de asumir tres tareas a la vez.\x7Primero reconquista dos edificios bot cualesquiera.\x7Llama a los amigos que quieras para que te ayuden.' },
    3223: {
        QUEST: '\xc2\xa1Un gran trabajo con los edificios! \x7Ahora reconquista dos edificios m\xc3\xa1s.\x7Los edificios deben de tener al menos dos pisos de altura.' },
    3224: {
        QUEST: '\xc2\xa1Fant\xc3\xa1stico!\x7Ahora basta con que recuperes dos edificios m\xc3\xa1s.\x7Los edificios deben tener al menos tres pisos de altura.\x7Cuando termines, vuelve para obtener tu recompensa.',
        COMPLETE: '\xc2\xa1Lo has conseguido, _avName_!\x7\xc2\xa1Has demostrado una dibupunter\xc3\xada incre\xc3\xadble!',
        GREETING: '' },
    3225: {
        QUEST: '_toNpcName_ dice que necesita ayuda.\x7\xc2\xbfPor qu\xc3\xa9 no vas a verla para ver en qu\xc3\xa9 la puedes ayudar?_where_' },
    3235: {
        QUEST: '\xc2\xa1Ah, \xc3\xa9sta debe de ser la ensalada que encargu\xc3\xa9!\x7Gracias por tra\xc3\xa9rmela.\x7Todos esos bots deben de haber asustado al repartidor habitual de _toNpcName_.\x7\xc2\xbfPor qu\xc3\xa9 no nos haces un favor y derrotas a unos cuantos bots de ah\xc3\xad fuera?\x7Derrota a diez bots en los Jardines de Daisy y vuelve con _toNpcName_.',
        INCOMPLETE_PROGRESS: '\xc2\xbfNo estabas venciendo a los bots por m\xc3\xad?\x7\xc2\xa1Maravilloso! \xc2\xa1Sigue as\xc3\xad!',
        COMPLETE: '\xc2\xa1Oh, muchas gracias por derrotar a esos bots!\x7Ahora quiz\xc3\xa1s pueda seguir con mis repartos normales.\x7Tu recompensa es...',
        INCOMPLETE_WRONG_NPC: 'Informa a _toNpcName_ sobre los bots a los que has derrotado._where_' },
    3236: {
        QUEST: 'Hay demasiados abogabots all\xc3\xad.\x7\xc2\xa1Ayuda en lo que puedas!\x7Recupera tres edificios de abogabots.' },
    3237: {
        QUEST: '\xc2\xa1Un gran trabajo con los edificios de abogabots! \x7\xc2\xa1Pero ahora hay demasiados vendebots!\x7Recupera tres edificios de vendebots y vuelve a por tu recompensa.' },
    3238: {
        QUEST: '\xc2\xa1Oh, no! \xc2\xa1Un bot "confraternizador" ha robado la llave de los Jardines de Daisy!\x7Intenta recuperarla.\x7Recuerda, s\xc3\xb3lo encontrar\xc3\xa1s al confraternizador en el interior de edificios de vendebots. ' },
    3239: {
        QUEST: 'S\xc3\xad, has encontrado una llave, pero no es la correcta.\x7Necesitamos la llave de los Jardines de Daisy.\x7\xc2\xa1Sigue buscando! \xc2\xa1La tiene un bot "confraternizador"!' },
    3242: {
        QUEST: '\xc2\xa1Oh, no! \xc2\xa1Un bot picapleitos ha robado la llave de Jardines de Daisy!\x7Intenta recuperarla.\x7Recuerda, s\xc3\xb3lo encontrar\xc3\xa1s al picapleitos en el interior de edificios de abogabots. ' },
    3243: {
        QUEST: 'S\xc3\xad, has encontrado una llave, pero no es la correcta.\x7Necesitamos la llave de los Jardines de Daisy.\x7\xc2\xa1Sigue buscando! \xc2\xa1La tiene un bot picapleitos!' },
    3240: {
        QUEST: '_toNpcName_ me acaba de decir que un picapleitos le ha robado una bolsa de alpiste.\x7Derrota a los picapleitos hasta que encuentres el alpiste de Federico Tilla y ll\xc3\xa9vaselo.\x7S\xc3\xb3lo encontrar\xc3\xa1s a los picapleitos en el interior de los edificios de abogabots._where_',
        COMPLETE: '\xc2\xa1Oh, muchas gracias por encontrar el alpiste!\x7Tu recompensa es...',
        INCOMPLETE_WRONG_NPC: '\xc2\xa1Muy bien, has conseguido recuperar el alpiste!\x7Ahora ll\xc3\xa9vaselo a _toNpcName_._where_' },
    3241: {
        QUEST: 'Algunos edificios bot est\xc3\xa1n creciendo demasiado para nuestro gusto.\x7Intenta recuperar algunos de los edificios m\xc3\xa1s altos.\x7Reconquista cinco edificios de tres plantas o m\xc3\xa1s y vuelve para llevarte una recompensa.' },
    4001: {
        GREETING: '',
        QUEST: 'Ahora tienes que elegir el nuevo circuito de trucos que quieres aprender.\x7Pi\xc3\xa9nsatelo todo lo que quieras y vuelve cuando hayas tomado una decisi\xc3\xb3n.',
        INCOMPLETE_PROGRESS: 'Antes de elegir, medita tu decisi\xc3\xb3n.',
        INCOMPLETE_WRONG_NPC: 'Antes de elegir, medita tu decisi\xc3\xb3n.',
        COMPLETE: 'Muy buena decisi\xc3\xb3n...',
        LEAVING: QuestsDefaultLeaving },
    4002: {
        GREETING: '',
        QUEST: 'Ahora tienes que elegir el nuevo circuito de trucos que quieres aprender.\x7Pi\xc3\xa9nsatelo todo lo que quieras y vuelve cuando hayas tomado una decisi\xc3\xb3n.',
        INCOMPLETE_PROGRESS: 'Antes de elegir, medita tu decisi\xc3\xb3n.',
        INCOMPLETE_WRONG_NPC: 'Antes de elegir, medita tu decisi\xc3\xb3n.',
        COMPLETE: 'Muy buena decisi\xc3\xb3n...',
        LEAVING: QuestsDefaultLeaving },
    4200: {
        QUEST: 'Seguro que a Ropo Pomp\xc3\xb3n le viene bien un poco de ayuda en su investigaci\xc3\xb3n._where_' },
    4201: {
        GREETING: '\xc2\xa1Hola!',
        QUEST: 'Estoy muy preocupado con una racha de robos de instrumentos musicales.\x7Estoy llevando a cabo un estudio entre mis compa\xc3\xb1eros comerciantes.\x7Tal vez pueda encontrar una pauta que me ayude a resolver el caso.\x7P\xc3\xa1sate por Sonatas y sonatinas para que Tina te d\xc3\xa9 su inventario de concertinas. _where_' },
    4202: {
        QUEST: 'S\xc3\xad, he hablado con Ropo esta ma\xc3\xb1ana.\x7Tengo el inventario aqu\xc3\xad mismo.\x7Ll\xc3\xa9vaselo, \xc2\xbfvale?_where_' },
    4203: {
        QUEST: '\xc2\xa1Fant\xc3\xa1stico! Uno menos...\x7Ahora ve a por el de Uki._where_' },
    4204: {
        QUEST: '\xc2\xa1Oh! \xc2\xa1El inventario!\x7Me hab\xc3\xada olvidado de \xc3\xa9l.\x7Seguro que lo tengo terminado para cuando hayas derrotado a diez bots.\x7P\xc3\xa1sate por aqu\xc3\xad despu\xc3\xa9s y te prometo que estar\xc3\xa1 listo.',
        INCOMPLETE_PROGRESS: '31, 32... \xc2\xa1Vaya!\x7\xc2\xa1Me has hecho perder la cuenta!',
        GREETING: '' },
    4205: {
        QUEST: 'Ah, ah\xc3\xad est\xc3\xa1s.\x7Gracias por darme algo de tiempo.\x7Ll\xc3\xa9vale esto a Ropo y sal\xc3\xbadale de mi parte._where_' },
    4206: {
        QUEST: 'Mmm, muy interesante.\x7Ahora s\xc3\xad que estoy dando con ello.\x7Muy bien, el \xc3\xbaltimo inventario es el de Bibi._where_' },
    4207: {
        QUEST: '\xc2\xbfInventario?\x7\xc2\xbfC\xc3\xb3mo voy a hacerlo si no tengo el formulario?\x7Ve a ver si Sordino Quena puede darme uno._where_',
        INCOMPLETE_PROGRESS: '\xc2\xbfAlguna novedad sobre el formulario?' },
    4208: {
        QUEST: '\xc2\xa1Pues claro que tengo un formulario de inventario!\x7Pero no es gratis, \xc2\xbfsabes?\x7\xc2\xbfSabes qu\xc3\xa9? Te lo dar\xc3\xa9 a cambio de una tarta de nata entera.',
        GREETING: '\xc2\xa1Muy buenas!',
        LEAVING: 'Hasta luego...',
        INCOMPLETE_PROGRESS: 'No me vale con un trozo.\x7Me quedar\xc3\xa9 con hambre. Quiero TODA la tarta.' },
    4209: {
        GREETING: '',
        QUEST: 'Mmm...\x7\xc2\xa1Qu\xc3\xa9 rica!\x7Aqu\xc3\xad tienes el formulario para Bibi._where_' },
    4210: {
        GREETING: '',
        QUEST: 'Gracias. Has sido de gran ayuda.\x7Veamos... Violines Bibi: 2\x7\xc2\xa1Ya est\xc3\xa1! \xc2\xa1Aqu\xc3\xad tienes!',
        COMPLETE: 'Buen trabajo, _avName_.\x7Seguro que ahora llego al fondo de la cuesti\xc3\xb3n de los robos.\x7\xc2\xbfPor qu\xc3\xa9 no llegas t\xc3\xba al fondo de esto?' },
    4211: {
        QUEST: 'Mira, el doctor Pavo Rotti est\xc3\xa1 llamando cada cinco minutos. \xc2\xbfPuedes ir a ver qu\xc3\xa9 problema tiene?_where_' },
    4212: {
        QUEST: '\xc2\xa1Guau! Me alegro de que el cuartel general haya mandado por fin a alguien.\x7No he tenido un solo cliente durante d\xc3\xadas.\x7Son estos malditos contables que hay por todas partes.\x7Creo que est\xc3\xa1n propagando una mala higiene bucal entre los vecinos.\x7Derrota a diez de ellos y veamos si el negocio mejora.',
        INCOMPLETE_PROGRESS: 'Sigo sin tener clientes. \xc2\xa1Pero sigue luchando!' },
    4213: {
        QUEST: '\xc2\xbfSabes? A lo mejor resulta que los culpables no eran los contables.\x7Igual son los chequebots en general.\x7Acaba con veinte de ellos y tal vez venga alguien por fin a mi cl\xc3\xadnica.',
        INCOMPLETE_PROGRESS: 'S\xc3\xa9 que veinte son muchos. Pero seguro que merece la pena.' },
    4214: {
        GREETING: '',
        LEAVING: '',
        QUEST: '\xc2\xa1No lo entiendo!\x7Sigo sin tener ni un solo cliente.\x7A lo mejor hay que atacar al origen del problema.\x7Intenta reconquistar un edificio de chequebots.\x7Eso deber\xc3\xada bastar.',
        INCOMPLETE_PROGRESS: '\xc2\xa1Por favor! \xc2\xa1S\xc3\xb3lo un peque\xc3\xb1o edificio de nada!...',
        COMPLETE: 'Sigue sin venir un alma por aqu\xc3\xad.\x7Pero la verdad es que, pens\xc3\xa1ndolo bien...\x7\xc2\xa1Tampoco ven\xc3\xadan clientes antes de que los bots nos invadiesen!\x7Sin embargo, aprecio de veras tu ayuda.\x7Seguro que esto te viene bien.' },
    4215: {
        QUEST: 'Olga necesita desesperadamente a alguien que la ayude.\x7\xc2\xbfPor qu\xc3\xa9 no te pasas a verla para ver qu\xc3\xa9 puedes hacer?_where_' },
    4216: {
        QUEST: '\xc2\xa1Gracias por venir tan pronto!\x7Parece que los bots se han hecho con muchos de los billetes de crucero de mis clientes.\x7Uki dice que ha visto a un efusivo irse de aqu\xc3\xad con un mont\xc3\xb3n.\x7Mira a ver si puedes recuperar el billete a Alaska de Chopo Chop\xc3\xadn.',
        INCOMPLETE_PROGRESS: 'Los efusivos pueden estar ya en cualquier sitio...' },
    4217: {
        QUEST: '\xc2\xa1Estupendo! \xc2\xa1Lo has encontrado!\x7\xc2\xbfMe har\xc3\xadas ahora el favor de llev\xc3\xa1rselo a Chopo Chop\xc3\xadn?_where_' },
    4218: {
        QUEST: '\xc2\xa1Estupendo, estupend\xc3\xadsimo!\x7\xc2\xa1Alaska, voy para all\xc3\xa1!\x7Ya no soporto a estos malditos bots.\x7Oye, creo que Olga te vuelve a necesitar._where_' },
    4219: {
        QUEST: 'S\xc3\xad, lo has adivinado.\x7Necesito que sacudas a los pesados de los efusivos para recuperar el billete de Felisa Felina al festival de Jazz.  \x7Ya sabes c\xc3\xb3mo funciona...',
        INCOMPLETE_PROGRESS: 'Hay m\xc3\xa1s en alguna parte...' },
    4220: {
        QUEST: '\xc2\xa1Estupendo!\x7\xc2\xbfPodr\xc3\xadas llevarle tambi\xc3\xa9n el billete?_where_' },
    4221: {
        GREETING: '',
        LEAVING: 'Hasta luego...',
        QUEST: '\xc2\xa1Hola!\x7Me voy de viaje, _avName_.\x7Antes de irte, m\xc3\xa1s vale que te pases de nuevo a ver a Olga..._where_' },
    4222: {
        QUEST: '\xc2\xa1\xc3\x89ste es el \xc3\xbaltimo, lo prometo!\x7Ahora hay que buscar el billete de Barbo para el gran concurso de canto.',
        INCOMPLETE_PROGRESS: 'Vamos, _avName_.\x7Barbo cuenta contigo.' },
    4223: {
        QUEST: 'Esto har\xc3\xa1 que Barbo se alegre mucho._where_' },
    4224: {
        GREETING: '',
        LEAVING: '',
        QUEST: '\xc2\xa1Vaya, vaya, VAYA!\x7\xc2\xa1Sensacional!\x7\xc2\xbfSabes? Este a\xc3\xb1o, los chicos y yo vamos a barrer en el concurso.\x7Olga dice que vuelvas por all\xc3\xad para recoger tu recompensa._where_\x7\xc2\xa1Adi\xc3\xb3s, adi\xc3\xb3s, ADI\xc3\x93S!',
        COMPLETE: 'Gracias por todo, _avName_.\x7Eres muy valioso aqu\xc3\xad en Toontown.\x7Hablando de cosas valiosas...' },
    902: {
        QUEST: 'Ve a ver a Leo.\x7Necesita que alguien entregue un mensaje._where_' },
    4903: {
        QUEST: '\xc2\xa1Colega!\x7Mis casta\xc3\xb1uelas est\xc3\xa1n empa\xc3\xb1adas y tengo una gran actuaci\xc3\xb3n esta noche.\x7Ll\xc3\xa9vaselas a Carlos para ver si las puede limpiar._where_' },
    4904: {
        QUEST: 'S\xc3\xad, creo que puedo limpiarlas.\x7Pero necesito un poco de tinta azul de un pulpo.',
        GREETING: '\xc2\xa1Hola!',
        LEAVING: '\xc2\xa1Adi\xc3\xb3s!',
        INCOMPLETE_PROGRESS: 'Los pulpos est\xc3\xa1n cerca de los amarraderos.' },
    4905: {
        QUEST: '\xc2\xa1S\xc3\xad! \xc2\xa1Eso es!\x7Ahora necesito un poco de tiempo para limpiarlas.\x7\xc2\xbfPor qu\xc3\xa9 no vas a recuperar un edificio de un piso mientras trabajo?',
        GREETING: '\xc2\xa1Hola!',
        LEAVING: '\xc2\xa1Adi\xc3\xb3s!',
        INCOMPLETE_PROGRESS: 'S\xc3\xb3lo un poco m\xc3\xa1s...' },
    4906: {
        QUEST: '\xc2\xa1Muy bien!\x7Aqu\xc3\xad tienes las casta\xc3\xb1uelas para Leo._where_' },
    4907: {
        GREETING: '',
        QUEST: '\xc2\xa1Muy bien, colega!\x7Tienen una pinta estupenda.\x7Ahora necesito que consigas una copia de la letra de "Navidades felices" de L\xc3\xadrica T\xc3\xa1strofe._where_' },
    4908: {
        QUEST: '\xc2\xa1Muy buenas!\x7Mmm, no tengo un ejemplar de esa letra a mano.\x7Si me dieses algo de tiempo, la podr\xc3\xada escribir de memoria.\x7\xc2\xbfPor qu\xc3\xa9 no te vas a recuperar un edificio de dos plantas mientras la escribo?' },
    4909: {
        QUEST: 'Lo siento.\x7Mi memoria ya no es lo que era.\x7Si vas a recuperar un edificio de tres plantas, seguro que tendr\xc3\xa9 la letra lista para cuando vuelvas.' },
    4910: {
        QUEST: '\xc2\xa1Ya est\xc3\xa1!\x7Siento haber tardado tanto.\x7Ll\xc3\xa9vale esto a Leo._where_',
        GREETING: '',
        COMPLETE: '\xc2\xa1Genial, colega!\x7\xc2\xa1Mi concierto va a ser la bomba!\x7Ah, que no se me olvide. Toma, esto te servir\xc3\xa1 para los bots.' },
    5247: {
        QUEST: 'Este barrio es bastante duro...\x7Te vendr\xc3\xada bien aprender unos cuantos trucos nuevos.\x7_toNpcName_ me ense\xc3\xb1\xc3\xb3 todo lo que s\xc3\xa9, as\xc3\xad que a lo mejor te puede ense\xc3\xb1ar a ti tambi\xc3\xa9n._where_' },
    5248: {
        GREETING: 'Aah, s\xc3\xad.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Parece que mi tarea te est\xc3\xa1 causando problemas.',
        QUEST: 'Aaah, un nuevo aprendiz, bienvenido.\x7Yo s\xc3\xa9 todo lo que hay que saber sobre las tartas.\x7Pero antes de empezar con tu entrenamiento, tienes que hacerme una peque\xc3\xb1a demostraci\xc3\xb3n.\x7Sal fuera y derrota a diez de los bots m\xc3\xa1s grandes.' },
    5249: {
        GREETING: 'Mmmmm.',
        QUEST: '\xc2\xa1Excelente!\x7Ahora, demu\xc3\xa9strame tu habilidad como pescador.\x7Ayer tir\xc3\xa9 tres dados de goma al estanque.\x7P\xc3\xa9scalos y tr\xc3\xa1emelos.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Parece que la ca\xc3\xb1a y el sedal no se te dan tan bien.' },
    5250: {
        GREETING: '',
        LEAVING: '',
        QUEST: '\xc2\xa1Aj\xc3\xa1!  Estos dados quedar\xc3\xa1n de miedo colgados del retrovisor de mi carreta de bueyes.\x7Ahora demu\xc3\xa9strame que sabes distinguir a los enemigos.\x7Vuelve cuando hayas reconquistado dos de los edificios de abogabots m\xc3\xa1s grandes.',
        INCOMPLETE_PROGRESS: '\xc2\xbfEst\xc3\xa1s teniendo problemas con los edificios?' },
    5258: {
        GREETING: '',
        LEAVING: '',
        QUEST: '\xc2\xa1Aj\xc3\xa1!  Estos dados quedar\xc3\xa1n de miedo colgados del retrovisor de mi carreta de bueyes.\x7Ahora demu\xc3\xa9strame que sabes distinguir a los enemigos.\x7Vuelve cuando hayas reconquistado dos de los edificios de jefebots m\xc3\xa1s grandes.',
        INCOMPLETE_PROGRESS: '\xc2\xbfEst\xc3\xa1s teniendo problemas con los edificios?' },
    5259: {
        GREETING: '',
        LEAVING: '',
        QUEST: '\xc2\xa1Aj\xc3\xa1!  Estos dados quedar\xc3\xa1n de miedo colgados del retrovisor de mi carreta de bueyes.\x7Ahora demu\xc3\xa9strame que sabes distinguir a los enemigos.\x7Vuelve cuando hayas reconquistado dos de los edificios de chequebots m\xc3\xa1s grandes.',
        INCOMPLETE_PROGRESS: '\xc2\xbfEst\xc3\xa1s teniendo problemas con los edificios?' },
    5260: {
        GREETING: '',
        LEAVING: '',
        QUEST: '\xc2\xa1Aj\xc3\xa1!  Estos dados quedar\xc3\xa1n de miedo colgados del retrovisor de mi carreta de bueyes.\x7Ahora demu\xc3\xa9strame que sabes distinguir a los enemigos.\x7Vuelve cuando hayas reconquistado dos de los edificios de vendebots m\xc3\xa1s grandes.',
        INCOMPLETE_PROGRESS: '\xc2\xbfEst\xc3\xa1s teniendo problemas con los edificios?' },
    5200: {
        QUEST: 'Esos bots tan pesados est\xc3\xa1n otra vez dando problemas.\x7_toNpcName_ ha informado de que falta otro objeto. P\xc3\xa1sate por all\xc3\xad, a ver si puedes arreglar la situaci\xc3\xb3n._where__where_' },
    5201: {
        GREETING: '',
        QUEST: 'Hola, _avName_.  Creo que debo darte las gracias por venir.\x7Un grupo de cazacabezas ha estado aqu\xc3\xad y se ha llevado mi bal\xc3\xb3n de f\xc3\xbatbol.\x7\xc2\xa1Su jefe me ha dicho que ten\xc3\xada que hacer un recorte de plantilla y me lo ha quitado!\x7\xc2\xbfPuedes recuperar el bal\xc3\xb3n?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfHas conseguido encontrar mi bal\xc3\xb3n?',
        COMPLETE: '\xc2\xa1Yujuuu!  \xc2\xa1Lo has encontrado! Aqu\xc3\xad tienes tu recompensa...' },
    5261: {
        GREETING: '',
        QUEST: 'Hola, _avName_.  Creo que debo darte las gracias por venir.\x7Un grupo de doscaras ha estado aqu\xc3\xad y se ha llevado mi bal\xc3\xb3n de f\xc3\xbatbol.\x7\xc2\xa1Su jefe me ha dicho que ten\xc3\xada que hacer un recorte de plantilla y me lo ha quitado!\x7\xc2\xbfPuedes recuperar el bal\xc3\xb3n?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfHas conseguido encontrar mi bal\xc3\xb3n?',
        COMPLETE: '\xc2\xa1Yujuuu!  \xc2\xa1Lo has encontrado! Aqu\xc3\xad tienes tu recompensa...' },
    5262: {
        GREETING: '',
        QUEST: 'Hola, _avName_.  Creo que debo darte las gracias por venir.\x7Un grupo de monederos ha estado aqu\xc3\xad y se ha llevado mi bal\xc3\xb3n de f\xc3\xbatbol.\x7\xc2\xa1Su jefe me ha dicho que ten\xc3\xada que hacer un recorte de plantilla y me lo ha quitado!\x7\xc2\xbfPuedes recuperar el bal\xc3\xb3n?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfHas conseguido encontrar mi bal\xc3\xb3n?',
        COMPLETE: '\xc2\xa1Yujuuu!  \xc2\xa1Lo has encontrado! Aqu\xc3\xad tienes tu recompensa...' },
    5263: {
        GREETING: '',
        QUEST: 'Hola, _avName_.  Creo que debo darte las gracias por venir.\x7Un grupo de portavoces ha estado aqu\xc3\xad y se ha llevado mi bal\xc3\xb3n de f\xc3\xbatbol.\x7\xc2\xa1Su jefe me ha dicho que ten\xc3\xada que hacer un recorte de plantilla y me lo ha quitado!\x7\xc2\xbfPuedes recuperar el bal\xc3\xb3n?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfHas conseguido encontrar mi bal\xc3\xb3n?',
        COMPLETE: '\xc2\xa1Yujuuu!  \xc2\xa1Lo has encontrado! Aqu\xc3\xad tienes tu recompensa...' },
    5202: {
        QUEST: 'Frescolandia ha sido invadida por los bots m\xc3\xa1s duros de pelar que he visto en mi vida.\x7M\xc3\xa1s vale que cargues m\xc3\xa1s bromas.\x7Me han dicho que es posible que _toNpcName_ tenga una bolsa m\xc3\xa1s grande en la que te cabr\xc3\xa1n m\xc3\xa1s bromas._where_' },
    5203: {
        GREETING: '\xc2\xbfEh?  \xc2\xbfEst\xc3\xa1s en mi equipo de trineo?',
        QUEST: '\xc2\xbfQu\xc3\xa9?  \xc2\xbfQuieres una bolsa?\x7El caso es que ten\xc3\xada una por aqu\xc3\xad... \xc2\xbfEstar\xc3\xa1 en mi trineo?\x7Vaya... \xc2\xa1No he visto mi trineo desde la gran carrera!\x7\xc2\xbfSe lo habr\xc3\xa1 llevado uno de esos bots?',
        LEAVING: '\xc2\xbfHas visto mi trineo?',
        INCOMPLETE_PROGRESS: '\xc2\xbfQui\xc3\xa9n dec\xc3\xadas que eras?  Lo siento, estoy un poco mareado por el choque.' },
    5204: {
        GREETING: '',
        LEAVING: '',
        QUEST: '\xc2\xbfEs \xc3\xa9se mi trineo?  No veo ninguna bolsa por aqu\xc3\xad.\x7Creo que Perico Arenque estaba en el equipo... \xc2\xbfLa tendr\xc3\xa1 \xc3\xa9l?_where_' },
    5205: {
        GREETING: '\xc2\xa1Oooh, la cabeza!',
        LEAVING: '',
        QUEST: '\xc2\xbfEh?  \xc2\xbfDoroteo qu\xc3\xa9?   \xc2\xbfUna bolsa?\x7Ah, \xc2\xbfno era miembro de nuestro equipo de trineo?\x7Me duele tanto la cabeza que no puedo pensar bien.\x7\xc2\xbfPuedes pescar unos cuantos cubitos de hielo en el estanque para que me los ponga en la cabeza?',
        INCOMPLETE_PROGRESS: '\xc2\xa1Ayyy, la cabeza me va a estallar!  \xc2\xbfTienes un poco de hielo?' },
    5206: {
        GREETING: '',
        LEAVING: '',
        QUEST: '\xc2\xa1Aaah, as\xc3\xad est\xc3\xa1 mucho mejor!\x7As\xc3\xad que buscas la bolsa de Doroteo, \xc2\xbfeh?\x7Creo que acab\xc3\xb3 en la cabeza de Nutrio Cenutrio despu\xc3\xa9s del choque._where_' },
    5207: {
        GREETING: '\xc2\xa1Eeeh!',
        LEAVING: '',
        QUEST: '\xc2\xbfBolsa?  \xc2\xbfQui\xc3\xa9n ser Perico?\x7\xc2\xa1Yo tener miedo de edificios!  \xc2\xa1T\xc3\xba derrotar edificios, yo darte bolsa!',
        INCOMPLETE_PROGRESS: '\xc2\xa1M\xc3\xa1s edificios!  \xc2\xa1Yo todav\xc3\xada tener miedo!',
        COMPLETE: '\xc2\xa1Oooh!  \xc2\xa1T\xc3\xba gustarme!' },
    5208: {
        GREETING: '',
        LEAVING: '\xc2\xa1Eeeh!',
        QUEST: '\xc2\xa1Oooh!  \xc2\xa1T\xc3\xba gustarme!\x7T\xc3\xba ir a cl\xc3\xadnica de esqu\xc3\xad. Bolsa all\xc3\xad.' },
    5209: {
        GREETING: '\xc2\xa1Colega!',
        LEAVING: '\xc2\xa1Nos vemos!',
        QUEST: '\xc2\xa1T\xc3\xado, ese tal Nutrio Cenutrio est\xc3\xa1 loco!\x7Colega, si est\xc3\xa1s loco como Nutrio, la bolsa ser\xc3\xa1 tuya.\x7\xc2\xa1Emb\xc3\xb3lsate a unos cuantos bots y la bolsa ser\xc3\xa1 tuya, colega! \xc2\xa1Vamos!',
        INCOMPLETE_PROGRESS: '\xc2\xbfEst\xc3\xa1s seguro de que eres bastante bestiajo?  Anda, vete a zurrar a los bots.',
        COMPLETE: '\xc2\xa1Eh, eres todo un campe\xc3\xb3n!  \xc2\xa1Has zurrado de lo lindo a un mont\xc3\xb3n de bots!\x7\xc2\xa1Aqu\xc3\xad tienes la bolsa!' },
    5210: {
        QUEST: '_toNpcName_ est\xc3\xa1 enamorada en secreto de alguien del barrio.\x7Si la ayudas, te recompensar\xc3\xa1 de lo lindo._where_' },
    5211: {
        GREETING: '\xc2\xa1Buaaaa!',
        QUEST: 'Me he pasado toda la noche escribiendo al perro que amo.\x7Pero antes de que pudiera entregar la carta, uno de esos apestosos bots con pico ha entrado y se la ha llevado.\x7\xc2\xbfMe haces el favor de recuperarla?',
        LEAVING: '\xc2\xa1Buaaaa!',
        INCOMPLETE_PROGRESS: 'Por favor, encuentra mi carta.' },
    5264: {
        GREETING: '\xc2\xa1Buaaaa!',
        QUEST: 'Me he pasado toda la noche escribiendo al perro que amo.\x7Pero antes de que pudiera entregar la carta, uno de esos apestosos bots con aleta ha entrado y se la ha llevado.\x7\xc2\xbfMe haces el favor de recuperarla?',
        LEAVING: '\xc2\xa1Buaaaa!',
        INCOMPLETE_PROGRESS: 'Por favor, encuentra mi carta.' },
    5265: {
        GREETING: '\xc2\xa1Buaaaa!',
        QUEST: 'Me he pasado toda la noche escribiendo al perro que amo.\x7Pero antes de que pudiera entregar la carta, uno de esos apestosos bots confraternizadores ha entrado y se la ha llevado.\x7\xc2\xbfMe haces el favor de recuperarla?',
        LEAVING: '\xc2\xa1Buaaaa!',
        INCOMPLETE_PROGRESS: 'Por favor, encuentra mi carta.' },
    5266: {
        GREETING: '\xc2\xa1Buaaaa!',
        QUEST: 'Me he pasado toda la noche escribiendo al perro que amo.\x7Pero antes de que pudiera entregar la carta, uno de esos apestosos bots corporativistas ha entrado y se la ha llevado.\x7\xc2\xbfMe haces el favor de recuperarla?',
        LEAVING: '\xc2\xa1Buaaaa!',
        INCOMPLETE_PROGRESS: 'Por favor, encuentra mi carta.' },
    5212: {
        QUEST: '\xc2\xa1Oh, gracias por encontrar la carta!\x7Por favor, \xc2\xbfpodr\xc3\xadas entreg\xc3\xa1rsela al perro m\xc3\xa1s guapo de todo el barrio?',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No has entregado la carta, \xc2\xbfverdad?' },
    5213: {
        GREETING: 'Encantado de verte.',
        QUEST: 'Lo siento, pero no puedo molestarme con tu carta.\x7\xc2\xa1Me han quitado a todos mis perritos!\x7Tr\xc3\xa1emelos y hablaremos.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xa1Mis pobres perritos!' },
    5214: {
        GREETING: '',
        LEAVING: '\xc2\xa1Hasta luego!',
        QUEST: 'Gracias por devolverme a mis preciosidades.\x7Echemos un vistazo a tu carta...\nMmmm, parece que tengo otra admiradora secreta.\x7Esto pide a gritos una visita a mi querido amigo Carlos Congelado.\x7\xc2\xa1Seguro que te cae muy bien!_where_' },
    5215: {
        GREETING: 'Je, je...',
        LEAVING: 'Vuelve, s\xc3\xad, s\xc3\xad.',
        INCOMPLETE_PROGRESS: 'Todav\xc3\xada quedan unos cuantos grandullones.  Vuelve cuando ya no est\xc3\xa9n.',
        QUEST: '\xc2\xbfQui\xc3\xa9n te ha enviado?  No me gustan los forasteros, no...\x7Pero todav\xc3\xada me gustan menos los bots...\x7Acaba con los grandotes y ya veremos si te ayudo.' },
    5216: {
        QUEST: 'Te he dicho que te vamos a ayudar.\x7As\xc3\xad que ll\xc3\xa9vale este anillo a la chica.',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xa1\xc2\xbfSigues teniendo el anillo?!',
        COMPLETE: '\xc2\xa1Oh, queriiiido! \xc2\xa1\xc2\xa1\xc2\xa1Gracias!!!\x7Ah, tambi\xc3\xa9n tengo algo especial para ti.' },
    5217: {
        QUEST: 'Parece que a _toNpcName_ le vendr\xc3\xada bien algo de ayuda._where_' },
    5218: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Seguro que hay confraternizadores por alg\xc3\xban sitio.',
        QUEST: '\xc2\xa1\xc2\xa1\xc2\xa1Socorro!!! \xc2\xa1\xc2\xa1\xc2\xa1Socorro!!! \xc2\xa1Ya no lo aguanto m\xc3\xa1s!\x7\xc2\xa1Esos confraternizadores me est\xc3\xa1n volviendo tarumba!' },
    5219: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No pueden ser todos.  \xc2\xa1S\xc3\xb3lo he visto a uno!',
        QUEST: '\xc2\xa1Vaya, gracias, pero ahora se trata de los corporativistas!\x7\xc2\xa1Tienes que ayudarme!' },
    5220: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xa1No, no, no, hab\xc3\xada uno justo aqu\xc3\xad!',
        QUEST: '\xc2\xa1Ahora me doy cuenta de que son esos prestamistas despiadados!\x7\xc2\xa1Cre\xc3\xada que ibas a salvarme!' },
    5221: {
        GREETING: '',
        LEAVING: '',
        QUEST: '\xc2\xbfSabes qu\xc3\xa9? \xc2\xa1A lo mejor la culpa no es de los bots!\x7\xc2\xbfPuedes pedirle a Pega Moide que me prepare una poci\xc3\xb3n calmante?  A lo mejor eso ayuda..._where_' },
    5222: {
        LEAVING: '',
        QUEST: '\xc2\xa1El tal Cris T\xc3\xa9rico es todo un personaje!\x7\xc2\xa1Voy a prepararle algo que le pondr\xc3\xa1 a tono!\x7Vaya, parece que me he quedado sin aletas de sardina...\x7P\xc3\xb3rtate bien y ve al estanque a pescarme unas cuantas.',
        INCOMPLETE_PROGRESS: '\xc2\xbfYa has conseguido las aletas?' },
    5223: {
        QUEST: 'Vale.  Gracias, cari\xc3\xb1o.\x7Toma, ahora ll\xc3\xa9vale esto a Cris.  Seguro que se calma enseguida.',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Vamos, ll\xc3\xa9vale la poci\xc3\xb3n a Cris.' },
    5224: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Hazme el favor de acabar con los picapleitos \xc2\xbfvale?',
        QUEST: '\xc2\xa1Oh, gracias a Dios que has vuelto!\x7\xc2\xa1\xc2\xa1\xc2\xa1Dame la poci\xc3\xb3n, r\xc3\xa1pido!!!\x7Glu, glu, glu...\x7\xc2\xa1Puaj, qu\xc3\xa9 mal sab\xc3\xada!\x7Pero \xc2\xbfsabes qu\xc3\xa9?  Me siento mucho m\xc3\xa1s tranquilo.  Ahora que puedo pensar con claridad, me doy cuenta de que...\x7\xc2\xa1\xc2\xa1\xc2\xa1Eran los picapleitos los que me volv\xc3\xadan loco todo el rato!!!',
        COMPLETE: '\xc2\xa1Es estupendo!  \xc2\xa1Ahora puedo relajarme!\x7Seguro que por aqu\xc3\xad hay algo que pueda darte.  \xc2\xa1Toma!' },
    5225: {
        QUEST: 'Desde el incidente del bocadillo de nabos, Felipe el gru\xc3\xb1\xc3\xb3n ha estado enfadado con _toNpcName_. \x7A lo mejor puedes ayudar a Frigo a arreglar las cosas entre ellos._where_' },
    5226: {
        QUEST: 'S\xc3\xad, seguro que te han contado que Felipe el gru\xc3\xb1\xc3\xb3n est\xc3\xa1 enfadado conmigo...\x7S\xc3\xb3lo intentaba ser amable regal\xc3\xa1ndole un bocadillo de nabos.\x7A lo mejor puedes animarle.\x7Felipe odia a los chequebots, sobre todo sus edificios. \x7Si reconquistas unos cuantos edificios de chequebots, tal vez sirva de algo.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfY si lo intentas con unos cuantos edificios m\xc3\xa1s?' },
    5227: {
        QUEST: '\xc2\xa1Es fant\xc3\xa1stico!  Ve a contar a Felipe lo que has hecho._where_' },
    5228: {
        QUEST: 'Vaya, eso ha hecho, \xc2\xbfeh?\x7Ese Frigo cree que puede arreglarlo todo as\xc3\xad de f\xc3\xa1cil, \xc2\xbfeh?\x7\xc2\xa1Me romp\xc3\xad una muela con ese bocadillo de nabos que me dio!\x7Quiz\xc3\xa1 si le llevas la muela al doctor Bocamaraca, \xc3\xa9l pueda arreglarla.',
        GREETING: 'Brrrrr.',
        LEAVING: 'Grr\xc3\xb1\xc3\xb1\xc3\xb1, gr\xc3\xb1\xc3\xb1\xc3\xb1\xc3\xb1.',
        INCOMPLETE_PROGRESS: '\xc2\xbfT\xc3\xba otra vez?  \xc2\xa1Cre\xc3\xada que ibas a arreglarme la muela!' },
    5229: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Sigo trabajando en la muela.  Tardar\xc3\xa9 un poquito m\xc3\xa1s.',
        QUEST: 'S\xc3\xad, la muela tiene bastante mala pinta, la verdad.\x7A lo mejor puedo hacer algo, pero tardar\xc3\xa9 un poco.\x7Mientras tanto, \xc2\xbfpodr\xc3\xadas limpiar la zona de esos chequebots?\x7Est\xc3\xa1n asustando a mis pacientes.' },
    5267: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Sigo trabajando en la muela.  Tardar\xc3\xa9 un poquito m\xc3\xa1s.',
        QUEST: 'S\xc3\xad, la muela tiene bastante mala pinta, la verdad.\x7A lo mejor puedo hacer algo, pero tardar\xc3\xa9 un poco.\x7Mientras tanto, \xc2\xbfpodr\xc3\xadas limpiar la zona de esos vendebots?\x7Est\xc3\xa1n asustando a mis pacientes.' },
    5268: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Sigo trabajando en la muela.  Tardar\xc3\xa9 un poquito m\xc3\xa1s.',
        QUEST: 'S\xc3\xad, la muela tiene bastante mala pinta, la verdad.\x7A lo mejor puedo hacer algo, pero tardar\xc3\xa9 un poco.\x7Mientras tanto, \xc2\xbfpodr\xc3\xadas limpiar la zona de esos abogabots?\x7Est\xc3\xa1n asustando a mis pacientes.' },
    5269: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Sigo trabajando en la muela.  Tardar\xc3\xa9 un poquito m\xc3\xa1s.',
        QUEST: 'S\xc3\xad, la muela tiene bastante mala pinta, la verdad.\x7A lo mejor puedo hacer algo, pero tardar\xc3\xa9 un poco.\x7Mientras tanto, \xc2\xbfpodr\xc3\xadas limpiar la zona de esos jefebots?\x7Est\xc3\xa1n asustando a mis pacientes.' },
    5230: {
        GREETING: '',
        QUEST: '\xc2\xa1Me alegro de que hayas vuelto!\x7He desistido de intentar arreglar la muela, y en su lugar, le he fabricado a Felipe una nueva, de oro.\x7Por desgracia, un bar\xc3\xb3n ladr\xc3\xb3n me la ha birlado.\x7Si te das prisa, a lo mejor consigues atraparle.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfHas encontrado ya la muela?' },
    5270: {
        GREETING: '',
        QUEST: '\xc2\xa1Me alegro de que hayas vuelto!\x7He desistido de intentar arreglar la muela, y en su lugar, le he fabricado a Felipe una nueva, de oro.\x7Por desgracia, un pez gordo me la ha birlado.\x7Si te das prisa, a lo mejor consigues atraparle.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfHas encontrado ya la muela?' },
    5271: {
        GREETING: '',
        QUEST: '\xc2\xa1Me alegro de que hayas vuelto!\x7He desistido de intentar arreglar la muela, y en su lugar, le he fabricado a Felipe una nueva, de oro.\x7Por desgracia, un Sr. Hollywood me la ha birlado.\x7Si te das prisa, a lo mejor consigues atraparle.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfHas encontrado ya la muela?' },
    5272: {
        GREETING: '',
        QUEST: '\xc2\xa1Me alegro de que hayas vuelto!\x7He desistido de intentar arreglar la muela, y en su lugar, le he fabricado a Felipe una nueva, de oro.\x7Por desgracia, un peluc\xc3\xb3n me la ha birlado.\x7Si te das prisa, a lo mejor consigues atraparle.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfHas encontrado ya la muela?' },
    5231: {
        QUEST: '\xc2\xa1Estupendo, \xc3\xa9sa es la muela!\x7\xc2\xbfPor qu\xc3\xa9 no me haces el favor de llev\xc3\xa1rsela a Felipe?',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Seguro que Felipe est\xc3\xa1 impaciente por ver su nueva muela.' },
    5232: {
        QUEST: 'Oh, gracias.\x7Ummmmf\x7\xc2\xbfQu\xc3\xa9 tal estoy, eh?\x7Bueno, puedes decirle a Frigo que le perdono.',
        LEAVING: '',
        GREETING: '' },
    5233: {
        QUEST: 'Oh, me alegro much\xc3\xadsimo de o\xc3\xadr eso.\x7Me imaginaba que el cascarrabias de Felipe no podr\xc3\xada seguir enfadado conmigo.\x7Como gesto de amistad, le he preparado este bocadillo de pi\xc3\xb1ones.\x7\xc2\xbfMe haces el favor de llev\xc3\xa1rselo? ',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Date prisa, por favor.  El bocadillo de pi\xc3\xb1ones est\xc3\xa1 m\xc3\xa1s rico cuando est\xc3\xa1 calentito.',
        COMPLETE: 'Vaya, \xc2\xbfqu\xc3\xa9 es esto?  \xc2\xbfEs para m\xc3\xad?\x7\xc3\x91am, \xc3\xb1am....\x7\xc2\xa1Aaay!  \xc2\xa1Mi muela!  \xc2\xa1Ese Frigo Saba\xc3\xb1\xc3\xb3n!\x7Bueno, vale, no ha sido culpa tuya.  Toma, ll\xc3\xa9vate esto como recompensa por tu esfuerzo.' },
    903: {
        QUEST: 'Creo que est\xc3\xa1s listo para ir a ver a _toNpcName_, en Ventisca a la vista, para tu prueba final._where_' },
    5234: {
        GREETING: '',
        QUEST: 'Ah, has vuelto.\x7Antes de empezar, tenemos que comer algo.\x7Tr\xc3\xa1enos un poco de queso abultado para el caldo.\x7El queso abultado s\xc3\xb3lo se puede conseguir de los bots peces gordos.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Seguimos necesitando queso abultado.' },
    5278: {
        GREETING: '',
        QUEST: 'Ah, has vuelto.\x7Antes de empezar, tenemos que comer algo.\x7Tr\xc3\xa1enos un poco de caviar para el caldo.\x7El caviar s\xc3\xb3lo se puede conseguir de los bots Sr. Hollywood.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Seguimos necesitando caviar.' },
    5235: {
        GREETING: '',
        QUEST: 'Los hombres sencillos comen con cucharas sencillas.\x7Un bot se ha llevado mi cuchara sencilla, as\xc3\xad que sencillamente, no puedo comer.\x7Tr\xc3\xa1eme mi cuchara. Creo que un bar\xc3\xb3n ladr\xc3\xb3n se la ha llevado.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Es sencillo: debo recuperar la cuchara.' },
    5279: {
        GREETING: '',
        QUEST: 'Los hombres sencillos comen con cucharas sencillas.\x7Un bot se ha llevado mi cuchara sencilla, as\xc3\xad que no puedo comer.\x7Tr\xc3\xa1eme mi cuchara. Creo que un peluc\xc3\xb3n se la ha llevado.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Es sencillo: debo recuperar la cuchara.' },
    5236: {
        GREETING: '',
        QUEST: 'Oh, gracias.\x7Slurp, slurp...\x7Aaah, ahora tienes que atrapar a un sapo parlanch\xc3\xadn.  Ponte a pescar en el estanque.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfD\xc3\xb3nde est\xc3\xa1 el sapo parlanch\xc3\xadn?' },
    5237: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Todav\xc3\xada no has conseguido el postre.',
        QUEST: 'Vaya, no cabe duda de que es un sapo parlanch\xc3\xadn.  D\xc3\xa1melo.\x7\xc2\xbfQu\xc3\xa9 dices, sapo?\x7Vaya vaya.\x7Vaya vaya...\x7El sapo ha hablado.  Necesitamos un postre.\x7Tr\xc3\xa1enos unos cuantos cucuruchos de helado de _toNpcName_.\x7Por alg\xc3\xban motivo, al sapo le gusta el helado de jud\xc3\xadas pintas._where_' },
    5238: {
        GREETING: '',
        QUEST: 'As\xc3\xad que te ha enviado Fredo Dedo.   Siento decirte que nos hemos quedado sin cucuruchos de helado de jud\xc3\xadas pintas.\x7Ver\xc3\xa1s, un mont\xc3\xb3n de bots ha entrado y se los ha llevado.\x7Han dicho que eran para un se\xc3\xb1or de Hollywood o algo as\xc3\xad.\x7Te agradecer\xc3\xada mucho que los recuperases.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfHas encontrado ya los cucuruchos de helado?' },
    5280: {
        GREETING: '',
        QUEST: 'As\xc3\xad que te ha enviado Fredo Dedo.   Siento decirte que nos hemos quedado sin cucuruchos de helado de jud\xc3\xadas pintas.\x7Ver\xc3\xa1s, un mont\xc3\xb3n de bots ha entrado y se los ha llevado.\x7Han dicho que eran para el pez gordo o algo as\xc3\xad.\x7Te agradecer\xc3\xada mucho que los recuperases.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfHas encontrado ya los cucuruchos de helado?' },
    5239: {
        QUEST: '\xc2\xa1Gracias por recuperar los cucuruchos de helado!\x7Aqu\xc3\xad tienes uno para Fredo Dedo.',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'M\xc3\xa1s vale que le lleves el helado a Fredo Dedo antes de que se derrita.' },
    5240: {
        GREETING: '',
        QUEST: 'Muy bien.  Aqu\xc3\xad tienes, sapo...\x7Slurp, slurp...\x7Muy bien, estamos casi listos.\x7Si pudieses traerme un poco de talco para secarme las manos...\x7Creo que los bots pelucones llevan a veces polvos de talco en la peluca.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfHas encontrado talco?' },
    5281: {
        GREETING: '',
        QUEST: 'Muy bien.  Aqu\xc3\xad tienes, sapo...\x7Slurp, slurp...\x7Muy bien, estamos casi listos.\x7Si pudieses traerme un poco de talco para secarme las manos...\x7Creo que los bots Sr. Hollywood llevan a veces polvos de talco para empolvarse la nariz.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfHas encontrado talco?' },
    5241: {
        QUEST: 'Vale.\x7Como dije en su d\xc3\xada, para lanzar bien una tarta, no se debe usar la mano...\x7... sino con el alma.\x7No s\xc3\xa9 qu\xc3\xa9 significa eso, as\xc3\xad que me sentar\xc3\xa9 a contemplar c\xc3\xb3mo reconquistas edificios.\x7Vuelve cuando hayas terminado tu tarea.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Tu tarea todav\xc3\xada no ha terminado.' },
    5242: {
        GREETING: '',
        QUEST: 'Aunque sigo sin saber de qu\xc3\xa9 hablo, no cabe duda de que eres de gran valor.\x7Te asigno una tarea final...\x7Al sapo parlanch\xc3\xadn le gustar\xc3\xada tener una novia.\x7Busca otro sapo parlanch\xc3\xadn.  El sapo ha hablado.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfD\xc3\xb3nde est\xc3\xa1 el otro sapo parlanch\xc3\xadn?',
        COMPLETE: '\xc2\xa1Guau!  Estoy cansado de todo este esfuerzo.  Voy a descansar.\x7Toma, ten tu recompensa y m\xc3\xa1rchate.' },
    5243: {
        QUEST: 'Pedro Glaciares est\xc3\xa1 empezando a apestar la calle.\x7\xc2\xbfPuedes convencerle de que se d\xc3\xa9 una ducha?_where_' },
    5244: {
        GREETING: '',
        QUEST: 'S\xc3\xad, supongo que suelo sudar bastante aqu\xc3\xad.\x7Mmm, a lo mejor si pudiese arreglar la tuber\xc3\xada que gotea en mi ducha...\x7Supongo que un engranaje de esos bots diminutos me servir\xc3\xa1.\x7Ve a por un engranaje de un microgerente y lo intentaremos.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfD\xc3\xb3nde est\xc3\xa1 el engranaje ese que me ibas a traer?' },
    5245: {
        GREETING: '',
        QUEST: 'S\xc3\xad, parece que eso ha funcionado.\x7Pero cuando me ducho me siento solo...\x7\xc2\xbfPodr\xc3\xadas ir a pescarme un patito de goma para que me haga compa\xc3\xb1\xc3\xada?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfHas conseguido encontrar el patito?' },
    5246: {
        QUEST: 'El patito es estupendo, pero...\x7Todos esos edificios alrededor me ponen nervioso.\x7Me sentir\xc3\xada mucho m\xc3\xa1s relajado si hubiese menos edificios cerca.',
        LEAVING: '',
        COMPLETE: 'Vale, me voy a dar una ducha.  Toma, esto es para ti.',
        INCOMPLETE_PROGRESS: 'Siguen preocup\xc3\xa1ndome los edificios.' },
    5251: {
        QUEST: 'Creo que Pago Gelado va a dar un recital esta noche.\x7Me han dicho que el material del concierto le est\xc3\xa1 dando problemas._where_' },
    5252: {
        GREETING: '',
        QUEST: '\xc2\xa1Ah, s\xc3\xad!  Pues claro que me viene bien algo de ayuda.\x7Los bots han venido y me han robado todo el equipo mientras descargaba la furgoneta.\x7\xc2\xbfPuedes echarme una mano recuperando el micr\xc3\xb3fono?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Oye, t\xc3\xado, no puedo cantar sin un micr\xc3\xb3fono.' },
    5253: {
        GREETING: '',
        QUEST: '\xc2\xa1S\xc3\xad, \xc3\xa9se es mi micr\xc3\xb3fono, muy bien!\x7Gracias por recuperarlo, pero...\x7Lo que necesito de verdad es el teclado para poder tocar unas cuantas notas.\x7Creo que se lo ha llevado uno de esos corporativistas.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfHas conseguido encontrar el teclado?' },
    5273: {
        GREETING: '',
        QUEST: '\xc2\xa1S\xc3\xad, \xc3\xa9se es mi micr\xc3\xb3fono, muy bien!\x7Gracias por recuperarlo, pero...\x7Lo que necesito de verdad es el teclado para poder tocar unas cuantas notas.\x7Creo que se lo ha llevado uno de esos confraternizadores.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfHas conseguido encontrar el teclado?' },
    5274: {
        GREETING: '',
        QUEST: '\xc2\xa1S\xc3\xad, \xc3\xa9se es mi micr\xc3\xb3fono, muy bien!\x7Gracias por recuperarlo, pero...\x7Lo que necesito de verdad es el teclado para poder tocar unas cuantas notas.\x7Creo que se lo ha llevado uno de esos prestamistas despiadados.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfHas conseguido encontrar el teclado?' },
    5275: {
        GREETING: '',
        QUEST: '\xc2\xa1S\xc3\xad, \xc3\xa9se es mi micr\xc3\xb3fono, muy bien!\x7Gracias por recuperarlo, pero...\x7Lo que necesito de verdad es el teclado para poder tocar unas cuantas notas.\x7Creo que se lo ha llevado uno de esos picapleitos.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc2\xbfHas conseguido encontrar el teclado?' },
    5254: {
        GREETING: '',
        QUEST: '\xc2\xa1Muy bien!  Ahora podr\xc3\xa9 actuar.\x7Si no se hubiesen llevado mis zapatos de plataforma...\x7Seguro que han terminado en manos de un Sr. Hollywood.',
        LEAVING: '',
        COMPLETE: '\xc2\xa1\xc2\xa1Fant\xc3\xa1stico!!  Ahora s\xc3\xad que estoy listo.\x7\xc2\xa1Hola, Frescolandia!\x7\xc2\xbfEh?  \xc2\xbfD\xc3\xb3nde est\xc3\xa1 la gente?\x7Vale, toma esto y tr\xc3\xa1eme unos cuantos fans, \xc2\xbfde acuerdo?',
        INCOMPLETE_PROGRESS: 'No querr\xc3\xa1s que act\xc3\xbae descalzo, \xc2\xbfno? ' },
    5282: {
        GREETING: '',
        QUEST: '\xc2\xa1Muy bien!  Ahora podr\xc3\xa9 actuar.\x7Si no se hubiesen llevado mis zapatos de plataforma...\x7Seguro que han terminado en manos de un pez gordo.',
        LEAVING: '',
        COMPLETE: '\xc2\xa1\xc2\xa1Fant\xc3\xa1stico!!  Ahora s\xc3\xad que estoy listo.\x7\xc2\xa1Hola, Frescolandia!\x7\xc2\xbfEh?  \xc2\xbfD\xc3\xb3nde est\xc3\xa1 la gente?\x7Vale, toma esto y tr\xc3\xa1eme unos cuantos fans, \xc2\xbfde acuerdo?',
        INCOMPLETE_PROGRESS: 'No querr\xc3\xa1s que act\xc3\xbae descalzo, \xc2\xbfno? ' },
    5283: {
        GREETING: '',
        QUEST: '\xc2\xa1Muy bien!  Ahora podr\xc3\xa9 actuar.\x7Si no se hubiesen llevado mis zapatos de plataforma...\x7Seguro que han terminado en manos de un bar\xc3\xb3n ladr\xc3\xb3n.',
        LEAVING: '',
        COMPLETE: '\xc2\xa1\xc2\xa1Fant\xc3\xa1stico!!  Ahora s\xc3\xad que estoy listo.\x7\xc2\xa1Hola, Frescolandia!\x7\xc2\xbfEh?  \xc2\xbfD\xc3\xb3nde est\xc3\xa1 la gente?\x7Vale, toma esto y tr\xc3\xa1eme unos cuantos fans, \xc2\xbfde acuerdo?',
        INCOMPLETE_PROGRESS: 'No querr\xc3\xa1s que act\xc3\xbae descalzo, \xc2\xbfno? ' },
    5284: {
        GREETING: '',
        QUEST: '\xc2\xa1Muy bien!  Ahora podr\xc3\xa9 actuar.\x7Si no se hubiesen llevado mis zapatos de plataforma...\x7Seguro que han terminado en manos de un peluc\xc3\xb3n.',
        LEAVING: '',
        COMPLETE: '\xc2\xa1\xc2\xa1Fant\xc3\xa1stico!!  Ahora s\xc3\xad que estoy listo.\x7\xc2\xa1Hola, Frescolandia!\x7\xc2\xbfEh?  \xc2\xbfD\xc3\xb3nde est\xc3\xa1 la gente?\x7Vale, toma esto y tr\xc3\xa1eme unos cuantos fans, \xc2\xbfde acuerdo?',
        INCOMPLETE_PROGRESS: 'No querr\xc3\xa1s que act\xc3\xbae descalzo, \xc2\xbfno? ' },
    5255: {
        QUEST: 'Creo que te vendr\xc3\xadan bien m\xc3\xa1s puntos de risa.\x7Quiz\xc3\xa1 puedas hacer un trato con _toNpcName_.\x7No te olvides de ponerlo por escrito..._where_' },
    5256: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Un trato es un trato.',
        QUEST: 'As\xc3\xad que quieres puntos de risa, \xc2\xbfeh?\x7\xc2\xa1Te propongo un trato!\x7Si te ocupas de unos cuantos jefebots...\x7Yo te recompensar\xc3\xa9 por ello.' },
    5276: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Un trato es un trato.',
        QUEST: 'As\xc3\xad que quieres puntos de risa, \xc2\xbfeh?\x7\xc2\xa1Te propongo un trato!\x7Si te ocupas de unos cuantos abogabots...\x7Yo te recompensar\xc3\xa9 por ello.' },
    5257: {
        GREETING: '',
        LEAVING: '',
        COMPLETE: 'Vale, pero estoy seguro de que te dije que te ocupases de unos cuantos abogabots.\x7Bueno, si t\xc3\xba lo dices... Pero me debes una.',
        INCOMPLETE_PROGRESS: 'Creo que todav\xc3\xada no has terminado.',
        QUEST: '\xc2\xbfDices que has terminado?  \xc2\xbfHas derrotado a todos los bots?\x7Me debes de haber entendido mal; nuestro trato se refer\xc3\xada a los vendebots.\x7Estoy segur\xc3\xadsimo de que te dije que te ocupases de unos cuantos vendebots.' },
    5277: {
        GREETING: '',
        LEAVING: '',
        COMPLETE: 'Vale, pero estoy seguro de que te dije que te ocupases de unos cuantos abogabots.\x7Bueno, si t\xc3\xba lo dices... Pero me debes una.',
        INCOMPLETE_PROGRESS: 'Creo que todav\xc3\xada no has terminado.',
        QUEST: '\xc2\xbfDices que has terminado?  \xc2\xbfHas derrotado a todos los bots?\x7Me debes de haber entendido mal, nuestro trato se refer\xc3\xada a los chequebots.\x7Estoy segur\xc3\xadsimo de que te dije que te ocupases de unos cuantos chequebots.' } }
ChatGarblerDog = [
    'guau',
    'arf',
    'grrrr']
ChatGarblerCat = [
    'miau',
    'miao']
ChatGarblerMouse = [
    '\xc3\xb1ic',
    '\xc3\xb1iiiic',
    '\xc3\xb1ic \xc3\xb1ic']
ChatGarblerHorse = [
    'relincho',
    'brrr']
ChatGarblerRabbit = [
    'iiik',
    'ipr',
    'iiipi',
    'iiiki']
ChatGarblerFowl = [
    'cuac',
    'cuaaac ',
    'cuac cuac']
ChatGarblerDefault = [
    'bla']
Bossbot = 'Jefebot'
Lawbot = 'Abogabot'
Cashbot = 'Chequebot'
Sellbot = 'Vendebot'
BossbotS = 'un Jefebot'
LawbotS = 'un Abogabot'
CashbotS = 'un Chequebot'
SellbotS = 'un Vendebot'
BossbotP = 'Jefebots'
LawbotP = 'Abogabots'
CashbotP = 'Chequebots'
SellbotP = 'Vendebots'
AvatarDetailPanelOK = 'Aceptar'
AvatarDetailPanelCancel = 'Cancelar'
AvatarDetailPanelClose = 'Cerrar'
AvatarDetailPanelLookup = 'Buscando detalles de %s.'
AvatarDetailPanelFailedLookup = 'Imposible obtener detalles de %s.'
AvatarDetailPanelOnline = 'Distrito: %(district)s\nLocalidad: %(location)s'
AvatarDetailPanelOffline = 'Distrito: sin conexi\xc3\xb3n\nLocalidad: sin conexi\xc3\xb3n'
AvatarPanelFriends = 'Amigos'
AvatarPanelWhisper = 'Susurrar'
AvatarPanelSecrets = 'Secretos'
AvatarPanelGoTo = 'Ir a'
AvatarPanelIgnore = 'No hacer caso'
AvatarPanelCogLevel = 'Nivel: %s'
AvatarPanelCogDetailClose = 'Cerrar'
WhisperNoLongerFriend = '%s ha abandonado tu lista de amigos.'
WhisperNowSpecialFriend = '\xc2\xa1%s es ahora tu amigo secreto!'
WhisperComingToVisit = '%s viene a verte.'
WhisperFailedVisit = '%s ha intentado venir a verte.'
WhisperTargetLeftVisit = '%s se ha ido a otro sitio. \xc2\xa1Prueba de nuevo!'
WhisperGiveupVisit = '%s no ha podido encontrarte porque te est\xc3\xa1s moviendo.'
WhisperIgnored = '\xc2\xa1%s no te est\xc3\xa1 haciendo caso!'
TeleportGreeting = 'Hola, %s.'
DialogSpecial = 'ooo'
DialogExclamation = '!'
DialogQuestion = '?'
DialogLength1 = 6
DialogLength2 = 12
DialogLength3 = 20
FriendsListLabel = 'Amigos'
WhisperFriendComingOnline = '\xc2\xa1%s se est\xc3\xa1 conectando!'
WhisperFriendLoggedOut = '%s ha cerrado la sesi\xc3\xb3n.'
TeleportPanelOK = 'Aceptar'
TeleportPanelCancel = 'Cancelar'
TeleportPanelYes = 'S\xc3\xad'
TeleportPanelNo = 'No'
TeleportPanelCheckAvailability = 'Intentando ir a %s.'
TeleportPanelNotAvailable = '%s est\xc3\xa1 ocupado ahora mismo. Int\xc3\xa9ntalo m\xc3\xa1s tarde.'
TeleportPanelIgnored = '%s no te est\xc3\xa1 haciendo caso.'
TeleportPanelNotOnline = '%s no est\xc3\xa1 conectado ahora mismo.'
TeleportPanelWentAway = '%s se ha marchado.'
TeleportPanelUnknownHood = '\xc2\xa1No sabes c\xc3\xb3mo llegar a %s!'
TeleportPanelUnavailableHood = '%s no est\xc3\xa1 disponible ahora mismo. Int\xc3\xa9ntalo m\xc3\xa1s tarde.'
TeleportPanelDenySelf = '\xc2\xa1No puedes ir t\xc3\xba solo!'
TeleportPanelOtherShard = '%(avName)s est\xc3\xa1 en el distrito %(shardName)s, y t\xc3\xba est\xc3\xa1s en el distrito %(myShardName)s. \xc2\xbfQuieres cambiarte a %(shardName)s?'
BattleBldgBossTaunt = 'Soy el jefe.'
ToonHealJokes = [
    [
        '\xc2\xbfQu\xc3\xa9 le dice un dos a un cero?',
        '\xc2\xa1Vente conmigo! '],
    [
        '\xc2\xbfQu\xc3\xa9 es una br\xc3\xbajula?',
        'Una vi\xc3\xa9jula montada en una esc\xc3\xb3bula.'],
    [
        'Qu\xc3\xa9 es un l\xc3\xb3bulo?',
        'Un perro gr\xc3\xa1ndulo que se come a las ov\xc3\xa9julas.'],
    [
        '\xc2\xbfQu\xc3\xa9 es una orilla?',
        'Sesenta minutillos.'],
    [
        '\xc2\xbfQu\xc3\xa9 es una oreja?',
        'Sesenta minutejos.'],
    [
        '\xc2\xbfQu\xc3\xa9 es un c\xc3\xb3digo?',
        'Por donde se dobla el br\xc3\xa1cigo.'],
    [
        '\xc2\xbfQu\xc3\xa9 le dice un cero a otro cero?',
        'No valemos nada.'],
    [
        '\xc2\xbfQu\xc3\xa9 le dice un jaguar a otro?',
        '\xc2\xbfJaguar you?'],
    [
        '\xc2\xbfCu\xc3\xa1ntos astr\xc3\xb3nomos hacen falta para cambiar una bombilla?',
        'Ninguno, los astr\xc3\xb3nomos prefieren la oscuridad.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el hombre que piensa m\xc3\xa1s profundo?',
        'El minero.'],
    [
        '\xc2\xbfC\xc3\xb3mo se dice suspense en chino?',
        '\xc2\xa1Cha cha cha chaaaaan!'],
    [
        '\xc2\xbfQu\xc3\xa9 le dice el ping\xc3\xbcino a la ping\xc3\xbcina?',
        'Te quiero como a ning\xc3\xbcina.'],
    [
        '\xc2\xbfQu\xc3\xa9 le dice la pelota a la raqueta? ',
        'Lo nuestro es imposible, siempre me est\xc3\xa1s pegando...'],
    [
        '\xc2\xbfQu\xc3\xa9 le dice un poste a otro poste?',
        'P\xc3\xb3state bien.'],
    [
        '\xc2\xbfQu\xc3\xa9 le dice un caim\xc3\xa1n mexicano a otro?',
        '\xc2\xa1Cai-manito!'],
    [
        '\xc2\xbfCu\xc3\xa1l es la sal que peor huele?',
        'La sal-pargatas.'],
    [
        '\xc2\xbfQu\xc3\xa9 es un punto verde en una esquina?',
        'Un guisante castigado.'],
    [
        '\xc2\xbfC\xc3\xb3mo se dice 99 en chino?',
        'Cachi-chien.'],
    [
        '\xc2\xbfPor qu\xc3\xa9 en Lepe ponen ajos en la carretera nacional?',
        'Porque son buenos para la circulaci\xc3\xb3n.'],
    [
        '\xc2\xbfQu\xc3\xa9 es m\xc3\xa1s asqueroso que encontrarse un gusano en una manzana?',
        'Encontrar s\xc3\xb3lo medio gusano.'],
    [
        '\xc2\xbfQui\xc3\xa9n invento las fracciones?',
        'Enrique Octavo.'],
    [
        '\xc2\xbfQui\xc3\xa9n mat\xc3\xb3 al libro de lengua?',
        'El sujeto.'],
    [
        '\xc2\xbfQu\xc3\xa9 hora es cuando un elefante se sienta en una valla?',
        'La hora de ponerla nueva.'],
    [
        '\xc2\xbfPor qu\xc3\xa9 los elefantes no pueden montar en bicicleta?',
        'Porque no tienen dedo gordo para tocar el timbre.'],
    [
        '\xc2\xbfC\xc3\xb3mo se meten cuatro elefantes en un Mini?',
        'Pues dos delante y dos detr\xc3\xa1s.'],
    [
        '\xc2\xbfCu\xc3\xa1ntos psicoanalistas hacen falta para cambiar una bombilla?',
        'Uno, pero la bombilla tiene que querer ser cambiada.'],
    [
        '\xc2\xbfPor qu\xc3\xa9 los flamencos se sostienen sobre una sola pata?',
        'Porque si no se caen.'],
    [
        '\xc2\xbfCu\xc3\xa1l es la patrona de los inform\xc3\xa1ticos? ',
        'Santa Tecla.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el patr\xc3\xb3n de los n\xc3\xa1ufragos?',
        'San Est\xc3\xa1n Aislados de la Costa.'],
    [
        '\xc2\xbfQui\xc3\xa9n es el patr\xc3\xb3n de los profesores de educaci\xc3\xb3n f\xc3\xadsica?',
        'San Gimnasio de Loyola.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el grupo musical m\xc3\xa1s oscuro? ',
        'Estatos Q\xc3\xbao.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el vaquero m\xc3\xa1s sucio del Oeste?',
        'Johny Melabo.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el queso favorito de Sherlock Holmes?',
        'El emmental, querido Watson.'],
    [
        '\xc2\xbfEn qu\xc3\xa9 se parece un elefante a una cama?',
        'En que el elefante es paquidermo y la cama paquiduermas.'],
    [
        '\xc2\xbfEn qu\xc3\xa9 se parece una camisa vieja a un hotel barato? ',
        'En que ninguno tiene botones.'],
    [
        '\xc2\xbfEn qu\xc3\xa9 se parece un boxeador a un telescopio?',
        'En que los dos hacen ver las estrellas.'],
    [
        '\xc2\xbfEn que se parece una diligencia a una silla?',
        'La diligencia va para Kansas City y la silla es para "siti" cansas.'],
    [
        '\xc2\xbfEn qu\xc3\xa9 se parecen una escopeta y una gata?',
        'En que las dos tienen gatillos.'],
    [
        '\xc2\xbfEn qu\xc3\xa9 se parecen un panadero y un pol\xc3\xadtico?',
        'En que los dos mueven masas.'],
    [
        '\xc2\xbfEn qu\xc3\xa9 se parece una bruja a un fin de semana?',
        'En que los dos pasan volando.'],
    [
        '\xc2\xbfEn que se parecen los limones a los terratenientes?',
        'En que los dos tienen muchas propiedades.'],
    [
        '\xc2\xbfEn qu\xc3\xa9 se parece una casa incendi\xc3\xa1ndose a una casa vac\xc3\xada?',
        'En que de la casa incendi\xc3\xa1ndose "salen llamas" y en la casa vac\xc3\xada "llamas y nadie sale".'],
    [
        '\xc2\xbfEn qu\xc3\xa9 se parece una pistola a un panadero?',
        'En que los dos hacen pan.'],
    [
        '\xc2\xbfEn qu\xc3\xa9 se parece un ladr\xc3\xb3n a una pulga?',
        'En que la pulga salta y el ladr\xc3\xb3n asalta.'],
    [
        '\xc2\xbfEn qu\xc3\xa9 se parece una estufa a un avi\xc3\xb3n?',
        'En que los dos tienen piloto.'],
    [
        '\xc2\xbfQu\xc3\xa9 le dice un chinche a una chinche?',
        'Te amo chincheramente.'],
    [
        '\xc2\xbfQu\xc3\xa9 le dice un sem\xc3\xa1foro a otro?',
        'No me mires que me estoy cambiando.'],
    [
        '\xc2\xbfQu\xc3\xa9 le dice el n\xc3\xbamero 3 al n\xc3\xbamero 30?',
        'Para ser como yo, tienes que ser sincero.'],
    [
        '\xc2\xbfQu\xc3\xa9 le dice un sem\xc3\xa1foro a otro?',
        'No me mires que me pongo rojo.'],
    [
        '\xc2\xbfQu\xc3\xa9 le dice el timbre al dedo?',
        'Si me tocas, grito.'],
    [
        '\xc2\xbfQu\xc3\xa9 le dice un zapato al otro?',
        '\xc2\xa1Qu\xc3\xa9 vida m\xc3\xa1s arrastrada llevamos!'],
    [
        '\xc2\xbfQu\xc3\xa9 le dice un diente a otro?',
        'Si te picas, pierdes.'],
    [
        '\xc2\xbfQu\xc3\xa9 le dice un ojo a otro?',
        'Estamos separados por narices.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el \xc3\xbaltimo animal acu\xc3\xa1tico?',
        'El delf\xc3\xadn.'],
    [
        '\xc2\xbfPor qu\xc3\xa9 es la cebra el animal m\xc3\xa1s antiguo de la selva?',
        'Porque est\xc3\xa1 en blanco y negro.'],
    [
        '\xc2\xbfPor qu\xc3\xa9 las pel\xc3\xadculas de Chaplin eran mudas?',
        'Porque el director siempre dec\xc3\xada: \xc2\xa1No charles, Chaplin! '],
    [
        '\xc2\xbfPor qu\xc3\xa9 los perros persiguen a los coches?',
        'Porque llevan un gato en el maletero.'],
    [
        '\xc2\xbfPor qu\xc3\xa9 los franceses comen caracoles? ',
        'Porque no les gusta la comida r\xc3\xa1pida.'],
    [
        '\xc2\xbfPor qu\xc3\xa9 se esconden los animales de la selva? ',
        'Porque los elefantes est\xc3\xa1n haciendo paracaidismo.'],
    [
        'Ring, ring - Muy buenas, \xc2\xbfes el uno-uno-uno-uno-uno-uno? ',
        '- No, \xc3\xa9ste es el once-once-once.'],
    [
        'Ring, ring - Oiga, \xc2\xbfes la Real Academia de la Lengua? ',
        '- No, pero como si lo seriese.'],
    [
        'Ring, ring - \xc2\xbfEs Otto? ',
        '- No, soy el de siempre.'],
    [
        'Ring, ring - Hola, \xc2\xbfest\xc3\xa1 Agust\xc3\xadn?',
        '- Pues s\xc3\xad, estoy aqu\xc3\xad calentito.'],
    [
        'Ring, ring - Hola, \xc2\xbfest\xc3\xa1 Cholo?',
        'No, estoy acompa\xc3\xb1ado.'],
    [
        'Ring, ring - Hola, \xc2\xbfest\xc3\xa1 Alberto?',
        '- \xc2\xa1No, est\xc3\xa1 celado!'],
    [
        'Ring, ring - Hola, \xc2\xbfest\xc3\xa1 Conchita?',
        '- No, estoy con Tarz\xc3\xa1n.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de la l\xc3\xadrica?',
        'Haber tenido un pl\xc3\xa1cido domingo.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un carnicero?',
        'Tener un hijo chuleta.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un forzudo?',
        'Doblar una esquina.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un sastre?',
        'Tener un hijo botones que se case con una americana.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un carpintero?',
        'Tener una hija c\xc3\xb3moda y otra coqueta.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un arquitecto?',
        'Construir castillos en el aire.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un peluquero?',
        'Perder el tren por los pelos.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un caballo?',
        'Tener silla y no poder sentarse.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un alba\xc3\xb1il?',
        'Tener una hija paleta.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un fot\xc3\xb3grafo?',
        'Que se le rebelen los hijos.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de la pereza?',
        'Levantarse dos horas antes para estar m\xc3\xa1s tiempo sin hacer nada.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un jardinero?',
        'Que su novia se llame Rosa y lo deje plantado.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de los colmos?',
        'Sentarse en un pajar y pincharse con la aguja.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un electricista?',
        'Que su mujer se llame Luz y sus hijos le sigan la corriente.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un libro?',
        'Que en oto\xc3\xb1o se le caigan las hojas.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de una ballena?',
        'Ir vac\xc3\xada.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un polic\xc3\xada?',
        'Denunciar a un hurac\xc3\xa1n por exceso de velocidad. '],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un robot?',
        'Tener nervios de acero.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de una jirafa?',
        'Tener dolor de garganta.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un pez?',
        'Quejarse porque no llueve.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de Aladino?',
        'Tener mal genio.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un astronauta?',
        'Quejarse de no tener espacio.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un dinamitero?',
        'Que lo exploten en su trabajo.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de los colmos?',
        'Que dos palomas de la paz se peleen por la ramita de olivo.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de Santa Claus?',
        'No poder bajar por la chimenea debido a la claustrofobia.'],
    [
        '\xc2\xbfPor qu\xc3\xa9 echa Donald az\xc3\xbacar en la almohada?',
        'Porque quiere tener dulces sue\xc3\xb1os.'],
    [
        '\xc2\xbfPor qu\xc3\xa9 ha llevado Goofy el peine al dentista?',
        'Porque ha perdido todos los dientes.'],
    [
        '\xc2\xbfPor qu\xc3\xa9 se sienta Goofy en la \xc3\xbaltima fila de los cines?',
        'Porque el que r\xc3\xade el \xc3\xbaltimo, r\xc3\xade mejor.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un escritor?',
        'Que su esposa le d\xc3\xa9 sopa de letras.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un calvo?',
        'Tener ideas descabelladas.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de una maleta?',
        'Pedir vacaciones porque est\xc3\xa1 cansada de tanto viajar.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un gallo?',
        'Que se le ponga la piel de gallina.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un charcutero?',
        'Tener un perro salchicha.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de una silla? ',
        'Tener patas y no poder caminar.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un gato?',
        'Vivir una vida de perros.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo m\xc3\xa1s peque\xc3\xb1o?',
        'El colmillo.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un paracaidista?',
        'Tener la moral por los suelos.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de la taca\xc3\xb1er\xc3\xada?',
        'Contarse los dedos cada vez que se le da la mano a alguien.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un d\xc3\xa1lmata?',
        'Que le saquen una foto y salga en blanco y negro.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un pastor?',
        'Quedarse dormido contando ovejas.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un vidriero?',
        'Que quiebre su negocio.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un cerrajero? ',
        'Dejarse las llaves dentro de casa.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de la paciencia?',
        'Tirar una moneda al agua y esperar a que la cara pida socorro.'],
    [
        '\xc2\xbfCu\xc3\xa1l es colmo de una costurera?',
        'Perder el hilo de la conversaci\xc3\xb3n.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un escritor?',
        'Querer poner siempre punto final a todas las reuniones.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un le\xc3\xb1ador?',
        'Dormir como un tronco.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un m\xc3\xbasico?',
        'Que su hijo d\xc3\xa9 la nota.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de Saturno?',
        'Tener anillos y no tener dedos.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un comediante?',
        'Que le digan que es un artista serio.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un vanidoso?',
        'Que su juego favorito sea el yo-yo.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un plumero?',
        'Ser al\xc3\xa9rgico al polvo.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de una cocinera?',
        'Llamar a la polic\xc3\xada porque los fideos se est\xc3\xa1n pegando.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un dinamitero?',
        'Que lo exploten en su trabajo.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un dentista?',
        'Quitarle los dientes a un serrucho.'],
    [
        '\xc2\xbfPor qu\xc3\xa9 era el matem\xc3\xa1tico un infeliz?',
        'Porque ten\xc3\xada muchos problemas.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un pez?',
        'Morir ahogado.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un cazador?',
        'Querer cazar la Osa Mayor.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un bombero?',
        'Llevarse trabajo a casa.'],
    [
        '\xc2\xbfCual es el colmo de la paciencia?',
        'Meter una zapatilla en una jaula y esperar a que cante.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un desdentado? ',
        'Estar armado hasta los dientes.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de una enfermera?',
        'Llamarse Dolores de Cabeza.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un cobarde? ',
        'Salirse de la cocina cuando se pegan los fideos.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de Pinocho?',
        'No tener madera de estudiante.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de una enfermera?',
        'Ponerle una tirita a la leche cortada.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un camello?',
        'Vivir toda la vida jorobado.'],
    [
        '\xc2\xbfCu\xc3\xa1l es colmo de un cementerio?',
        'Estar cerrado por defunci\xc3\xb3n.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de una sardina?',
        'Que le d\xc3\xa9 lata.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un c\xc3\xb3ctel?',
        'Sentirse agitado.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el colmo de un granjero?',
        'Dejar abierta la puerta del corral para que se ventile.'],
    [
        '\xc2\xbfCu\xc3\xa1l es la palabra m\xc3\xa1s larga del mundo?',
        'Arroz, porque empieza con A y termina con Z.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el animal que ve menos?',
        'La venada.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el animal m\xc3\xa1s fiero? ',
        'El lopintan, porque no es tan fiero el le\xc3\xb3n como lopintan.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el perro m\xc3\xa1s explosivo?',
        'El vol-can.'],
    [
        '\xc2\xbfCu\xc3\xa1l es el animal que juega al ajedrez?',
        'El caballo.'],
    [
        '\xc2\xbfQu\xc3\xa9 es un codo? ',
        'Un gdupo de ni\xc3\xb1ods cantodes.'],
    [
        '\xc2\xbfEn que se parece una cueva a un frigor\xc3\xadfico? ',
        'La cueva tiene estalactitas y estalagmitas y el frigor\xc3\xadfico esta latita de at\xc3\xban, esta latita de anchoas...'],
    [
        '- Doctor, me siento mal.',
        '- Pues si\xc3\xa9ntese bien.'],
    [
        '- Hoy tose usted mejor que ayer.',
        '- S\xc3\xad, doctor... He estado ensayando toda la noche.'],
    [
        '- Doctor, doctor... \xc2\xbfc\xc3\xb3mo s\xc3\xa9 si estoy perdiendo la memoria? ',
        '- Eso ya se lo dije ayer.'],
    [
        '- Doctor, \xc2\xbfqu\xc3\xa9 me aconseja para evitar resfriarme de nuevo? ',
        'Conservar el resfriado que tiene ahora.'],
    [
        '- Doctor, doctor, sigo pensando que soy invisible.',
        '- \xc2\xbfQui\xc3\xa9n ha dicho eso?'],
    [
        '- Doctor, doctor, el pelo se me est\xc3\xa1 cayendo. \xc2\xbfC\xc3\xb3mo puedo conservarlo?',
        '- Tome una caja de zapatos.'],
    [
        '- Doctor, doctor, hace dos semanas que no como ni duermo. \xc2\xbfQu\xc3\xa9 tengo? ',
        '- Seguramente sue\xc3\xb1o y hambre.'],
    [
        '- Doctor, doctor, vengo a que me reconozca.',
        '- Pues ahora mismo no caigo.'],
    [
        '- Doctor, doctor, es que tengo un hueso fuera...',
        '- Pues d\xc3\xadgale que pase.'],
    [
        '- Doctor, doctor que se me juntan las letras.',
        '- Pues p\xc3\xa1guelas, p\xc3\xa1guelas...'],
    [
        '- Doctor, doctor, cuando tomo caf\xc3\xa9 se me ponen los ojos morados.',
        '- \xc2\xbfHa probado a apartar la cucharilla?'],
    [
        '- \xc2\xa1\xc2\xa1Doctor, doctor, vengo a que me osculte!!',
        '- \xc2\xa1R\xc3\xa1pido, detr\xc3\xa1s del sill\xc3\xb3n!'],
    [
        '- Doctor, tengo los dientes muy amarillos, \xc2\xbfqu\xc3\xa9 me recomienda?',
        '- Una corbata marr\xc3\xb3n.'],
    [
        '- Mam\xc3\xa1, mam\xc3\xa1, en el cole me llaman despistado.',
        '- Anda, ni\xc3\xb1o, vete a tu casa.'],
    [
        '- Mam\xc3\xa1, mam\xc3\xa1, en el colegio me llaman despistado.',
        '- SU TABACO, GRACIAS.'],
    [
        '- Mam\xc3\xa1, mam\xc3\xa1, \xc2\xbfcu\xc3\xa1ndo vamos a comer pan de hoy?',
        '- Ma\xc3\xb1ana, hijo, ma\xc3\xb1ana.'],
    [
        '- \xc2\xa1Mam\xc3\xa1, mam\xc3\xa1, est\xc3\xa1n golpeando la puerta!',
        '- D\xc3\xa9jala que se defienda sola.'],
    [
        '- Mam\xc3\xa1, mam\xc3\xa1... \xc2\xbfpor qu\xc3\xa9 me llaman pies grandes en el cole?',
        'No lo s\xc3\xa9, pero \xc2\xbfhas guardado los zapatos en el garaje?'],
    [
        '- Mam\xc3\xa1, \xc2\xbfqu\xc3\xa9 es la amnesia?',
        '- \xc2\xbfQu\xc3\xa9? \xc2\xbfQui\xc3\xa9n eres?'],
    [
        '- Camarero, camarero, \xc2\xbfqu\xc3\xa9 hace esta mosca en mi sopa? ',
        '- Yo dir\xc3\xada que braza australiana, se\xc3\xb1or.'],
    [
        '- Camarero, camarero, \xc2\xbfme ali\xc3\xb1a la ensalada? ',
        '- Con el uno pepino, con el dos tomate, con el tres cebolla...'],
    [
        '- \xc2\xbfC\xc3\xb3mo ha encontrado el se\xc3\xb1or el solomillo?',
        '- De milagro, oiga, de milagro.'],
    [
        '- Camarero, camarero, est\xc3\xa1 usted metiendo la corbata en mi sopa.',
        '- No se preocupe, se\xc3\xb1or, no encoge.'],
    [
        '- Camarero, \xc2\xa1ya le he pedido cien veces un vaso de agua! ',
        '- \xc2\xa1Cien vasos de agua para el se\xc3\xb1or!'],
    [
        '- Camarero, camarero, hay una mosca muerta en mi sopa.',
        '- \xc2\xbfY qu\xc3\xa9 esperaba por este precio? \xc2\xbfUna viva?'],
    [
        '- Camarero, \xc2\xbfel pescado viene solo?',
        '- No, se lo traigo yo.'],
    [
        '- Camarero, un caf\xc3\xa9 solo, por favor.',
        '- \xc2\xa1Todo el mundo fuera!'],
    [
        '- \xc2\xa1Capit\xc3\xa1n, capit\xc3\xa1n, que vamos a pique! ',
        '-\xc2\xa1He dicho yo que vamos a C\xc3\xa1diz y vamos a C\xc3\xa1diz!'],
    [
        '- Capit\xc3\xa1n, capit\xc3\xa1n, \xc2\xa1nos hundimos!',
        '- \xc2\xa1Pero bobo, si estamos en un submarino!'],
    [
        '- \xc2\xa1Capit\xc3\xa1n, capit\xc3\xa1n, hemos perdido la guerra! ',
        '- Pues buscadla enseguida.'],
    [
        '- \xc2\xa1Soldado, ice la bandera!',
        '- Le felicito mi general, le qued\xc3\xb3 muy bonita.'],
    [
        '- \xc2\xa1Soldados, presenten armas!',
        '- Aqu\xc3\xad mi general, aqu\xc3\xad mi fusil.'],
    [
        '- Mi capit\xc3\xa1n, los soldados no aguantan m\xc3\xa1s, estamos a 42\xc2\xba a la sombra.',
        '- Est\xc3\xa1 bien sargento, pueden descansar diez minutos al sol.'],
    [
        '- Por favor, \xc2\xbfla calle Sagasta?',
        '- Hombre, si pisa fuerte...'],
    [
        '- Oiga, que este reloj no anda.',
        '- Claro, todav\xc3\xada no tiene un a\xc3\xb1o.'],
    [
        '- Camarero, p\xc3\xb3ngame un caf\xc3\xa9 corto.',
        '- Se me ha roto la m\xc3\xa1quina, cambio.']]
MovieHealLaughterMisses = ('ji', 'je', 'ja', 'jua, jua')
MovieHealLaughterHits1 = ('Ja, ja, ja', 'ji, ji', 'Je, je, je', 'Ja, ja')
MovieHealLaughterHits2 = ('\xc2\xa1JUA, JUA, JUA!', '\xc2\xa1JUO, JUO, JUO!', '\xc2\xa1JA, JA, JA!')
MovieSOSCallHelp = '\xc2\xa1SOCORRO %s!'
MovieSOSWhisperHelp = '\xc2\xa1%s necesita que le ayuden en el combate!'
MovieSOSObserverHelp = '\xc2\xa1SOCORRO!'
MovieSuitCancelled = 'CANCELADO\nCANCELADO\nCANCELADO'
RewardPanelToonTasks = 'Dibutareas'
RewardPanelItems = 'Objetos recuperados'
RewardPanelMissedItems = 'Objetos no recuperados'
RewardPanelQuestLabel = 'Tarea %s'
RewardPanelCongratsStrings = [
    '\xc2\xa1As\xc3\xad se hace!',
    '\xc2\xa1Enhorabuena!',
    '\xc2\xa1Guau!',
    '\xc2\xa1Chupi!',
    '\xc2\xa1Impresionante!',
    '\xc2\xa1Dibufant\xc3\xa1stico!']
RewardPanelNewGag = '\xc2\xa1Nueva broma %(gagName)s para %(avName)s!'
CheesyEffectDescriptions = [
    ('Dibu normal', 'ser\xc3\xa1s normal'),
    ('Cabezota grande', 'tendr\xc3\xa1s la cabeza grande'),
    ('Cabecita peque\xc3\xb1a', 'tendr\xc3\xa1s la cabeza peque\xc3\xb1a'),
    ('Piernotas grandes', 'tendr\xc3\xa1s las piernas grandes'),
    ('Piernecitas peque\xc3\xb1as', 'tendr\xc3\xa1s las piernas peque\xc3\xb1as'),
    ('Dibu grandote', 'ser\xc3\xa1s un poco m\xc3\xa1s grande'),
    ('Dibu peque\xc3\xb1ito', 'ser\xc3\xa1s un poco m\xc3\xa1s peque\xc3\xb1o'),
    ('Imagen plana', 'tendr\xc3\xa1s s\xc3\xb3lo dos dimensiones'),
    ('Perfil plano', 'tendr\xc3\xa1s s\xc3\xb3lo dos dimensiones'),
    ('Transparente', 'ser\xc3\xa1s transparente'),
    ('Incoloro', 'no tendr\xc3\xa1s color'),
    ('Dibu invisible', 'ser\xc3\xa1s invisible')]
CheesyEffectIndefinite = 'hasta que elijas otro efecto, %(effectName)s%(whileIn)s.'
CheesyEffectMinutes = 'Durante los pr\xc3\xb3ximos %(time)s minutos, %(effectName)s%(whileIn)s.'
CheesyEffectHours = 'Durante los pr\xc3\xb3ximas %(time)s horas, %(effectName)s%(whileIn)s.'
CheesyEffectDays = 'Durante los pr\xc3\xb3ximos %(time)s d\xc3\xadas, %(effectName)s%(whileIn)s.'
CheesyEffectWhileYouAreIn = ' mientras est\xc3\xa1s en %s'
CheesyEffectExceptIn = ', excepto en %s'
SuitFlunky = 'Secuaz'
SuitPencilPusher = 'Chupatintas'
SuitYesman = 'Sonriente'
SuitMicromanager = 'Micro\x3gerente'
SuitDownsizer = 'Regulador de Empleo'
SuitHeadHunter = 'Cazacabezas'
SuitCorporateRaider = 'Corporati\x3vista'
SuitTheBigCheese = 'Pez Gordo'
SuitColdCaller = 'Gorr\xc3\xb3n'
SuitTelemarketer = 'Tele\x3vendedor'
SuitNameDropper = 'Fardoncete'
SuitGladHander = 'Efusivo'
SuitMoverShaker = 'Mandam\xc3\xa1s'
SuitTwoFace = 'Doscaras'
SuitTheMingler = 'Confrater\x3nizadora'
SuitMrHollywood = 'Sr. Hollywood'
SuitShortChange = 'Calderilla'
SuitPennyPincher = 'Cacomatraco'
SuitTightwad = 'Ro\xc3\xb1oso'
SuitBeanCounter = 'Cuenta cuentos'
SuitNumberCruncher = 'Contable'
SuitMoneyBags = 'Monedero'
SuitLoanShark = 'Prestamista Despiadado'
SuitRobberBaron = 'Bar\xc3\xb3n ladr\xc3\xb3n'
SuitBottomFeeder = 'Morrudo'
SuitBloodsucker = 'Chupa\x3sangres'
SuitDoubleTalker = 'Embaucador'
SuitAmbulanceChaser = 'Persigue Ambulancias'
SuitBackStabber = 'Apu\xc3\xb1a la Espaldas'
SuitSpinDoctor = 'Portavoz'
SuitLegalEagle = 'Picapleitos'
SuitBigWig = 'Peluc\xc3\xb3n'
SuitFlunkyS = 'un Secuaz'
SuitPencilPusherS = 'un Chupatintas'
SuitYesmanS = 'un Sonriente'
SuitMicromanagerS = 'una Micro\x3gerente'
SuitDownsizerS = 'un Regulador de Empleo'
SuitHeadHunterS = 'un Cazacabezas'
SuitCorporateRaiderS = 'un Corporati\x3vista'
SuitTheBigCheeseS = 'un Pez gordo'
SuitColdCallerS = 'un Gorr\xc3\xb3n'
SuitTelemarketerS = 'un Tele\x3vendedor'
SuitNameDropperS = 'un Fardoncete'
SuitGladHanderS = 'un Efusivo'
SuitMoverShakerS = 'un Mandam\xc3\xa1s'
SuitTwoFaceS = 'un Doscaras'
SuitTheMinglerS = 'una Confrater\x3nizadora'
SuitMrHollywoodS = 'un Sr. Hollywood'
SuitShortChangeS = 'un Calderilla'
SuitPennyPincherS = 'un Cacomatraco'
SuitTightwadS = 'un Ro\xc3\xb1oso'
SuitBeanCounterS = 'un Cuenta Cuentos'
SuitNumberCruncherS = 'una Contable'
SuitMoneyBagsS = 'un Monedero'
SuitLoanSharkS = 'un Prestamista Despiadado'
SuitRobberBaronS = 'un Bar\xc3\xb3n Ladr\xc3\xb3n'
SuitBottomFeederS = 'un Morrudo'
SuitBloodsuckerS = 'un Chupa\x3sangres'
SuitDoubleTalkerS = 'un Embaucador'
SuitAmbulanceChaserS = 'un Persigue Ambulancias'
SuitBackStabberS = 'un Apu\xc3\xb1a la Espaldas'
SuitSpinDoctorS = 'un Portavoz'
SuitLegalEagleS = 'un Picapleitos'
SuitBigWigS = 'un Peluc\xc3\xb3n'
SuitFlunkyP = 'Secuaces'
SuitPencilPusherP = 'Chupatintas'
SuitYesmanP = 'Sonrientes'
SuitMicromanagerP = 'Micro\x3gerentes'
SuitDownsizerP = 'Reguladores de Empleo'
SuitHeadHunterP = 'Cazacabezas'
SuitCorporateRaiderP = 'Corporati\x3vistas'
SuitTheBigCheeseP = 'Peces Gordos'
SuitColdCallerP = 'Gorrones'
SuitTelemarketerP = 'Tele\x3vendedores'
SuitNameDropperP = 'Fardoncetes'
SuitGladHanderP = 'Efusivos'
SuitMoverShakerP = 'Mandamases'
SuitTwoFaceP = 'Doscaras'
SuitTheMinglerP = 'Confrater\x3nizadoras'
SuitMrHollywoodP = 'Sres. Hollywood'
SuitShortChangeP = 'Calderillas'
SuitPennyPincherP = 'Cacomatracos'
SuitTightwadP = 'Ro\xc3\xb1osos'
SuitBeanCounterP = 'Cuenta Cuentos'
SuitNumberCruncherP = 'Contables'
SuitMoneyBagsP = 'Monederos'
SuitLoanSharkP = 'Prestamistas Despiadados'
SuitRobberBaronP = 'Barones Ladrones'
SuitBottomFeederP = 'Morrudos'
SuitBloodsuckerP = 'Chupa\x3sangres'
SuitDoubleTalkerP = 'Embaucadores'
SuitAmbulanceChaserP = 'Persigue Ambulancias'
SuitBackStabberP = 'Apu\xc3\xb1a la Espaldas'
SuitSpinDoctorP = 'Portavoces'
SuitLegalEagleP = 'Picapleitos'
SuitBigWigP = 'Pelucones'
SuitFaceOffDefaultTaunts = [
    '\xc2\xa1Buuu!']
SuitFaceoffTaunts = {
    'b': [
        '\xc2\xbfMe haces una donaci\xc3\xb3n?',
        'Te voy a dejar hecho unos zorros.',
        'Te voy a dejar m\xc3\xa1s seco que la mojama.',
        'Hay que ser "RH positivo" ante la vida.',
        'Oh, no seas tan "RH negativo".',
        'Me sorprende que me hayas encontrado, soy muy escurridizo.',
        'Voy a tener que hacerte una transfusi\xc3\xb3n r\xc3\xa1pida.',
        'Pronto vas a tener que tomarte un bocadillo y un zumito.',
        'Cuando acabe contigo no vas a poder ni levantarte.',
        'No mires, s\xc3\xb3lo te pinchar\xc3\xa1 un poquito.',
        'Vas a marearte un poquito.',
        'Justo a tiempo, estaba un poco sediento.'],
    'm': [
        'No sabes con qui\xc3\xa9n est\xc3\xa1s confraternizando.',
        '\xc2\xbfHas confraternizado alguna vez con gente como yo?',
        'Estupendo, confraternicemos pues.',
        '\xc2\xa1Me encanta confraternizar!',
        'Parece un buen sitio para confraternizar.',
        'Qu\xc3\xa9 situaci\xc3\xb3n m\xc3\xa1s tierna, \xc2\xbfno?',
        'Vas a confraternizar con la derrota.',
        'Voy a hacer que confraternices con el suelo.',
        '\xc2\xbfSeguro que quieres confraternizar conmigo?'],
    'ms': [
        'Prep\xc3\xa1rate; soy muy mand\xc3\xb3n.',
        'M\xc3\xa1s te valdr\xc3\xada quitarte de en medio.',
        'Te mando que te largues.',
        'Creo que me toca mandar.',
        'Vas a ver ad\xc3\xb3nde te mando.',
        'Cuando mando, los dem\xc3\xa1s tiemblan.',
        'Hoy me he levantado de lo m\xc3\xa1s mand\xc3\xb3n.',
        'Cuidado, dibu, te va a caer encima un mandoble.',
        'Te voy a mandar bien lejos.',
        'El coraz\xc3\xb3n me manda que te zurre.',
        '\xc2\xbfNecesitas que te manden un poco?'],
    'hh': [
        'Te saco una cabeza.',
        'Vas de cr\xc3\xa1neo, me parece.',
        'Creo que has perdido la cabeza.',
        'Estupendo. Ten\xc3\xada ganas de coleccionar tu cocorota.',
        'Te vas a quedar sin cabeza por esto.',
        '\xc2\xa1Cabeza al frente!',
        'Me parece que la cabeza te ha jugado una mala pasada.',
        'Qu\xc3\xa9 poca cabeza est\xc3\xa1s teniendo.',
        'Un trofeo perfecto para mi colecci\xc3\xb3n.',
        'Vas a tener un buen dolor de cabeza.',
        '\xc2\xa1Cuidado, no pierdas la cabeza!'],
    'tbc': [
        'Te voy a pescar con las manos.',
        'Puedes llamarme Cachalote.',
        'Ten cuidado.  A veces soy como un tibur\xc3\xb3n blanco.',
        'Por fin, ya pensaba que me estabas dando sedal.',
        'Voy a cocinarte a la sal.',
        '\xc2\xbfQu\xc3\xa9 tal me sienta el escabeche?',
        'Ven aqu\xc3\xad, voy a quitarte las escamas.',
        'Te va a pasar igual que a Jon\xc3\xa1s.',
        'Cuidadito, te he preparado un buen cebo.',
        '\xc2\xbfTe gusta que te preparen al pil-pil?',
        '\xc2\xa1Te voy a dar un buen pez-coz\xc3\xb3n!'],
    'cr': [
        '\xc2\xa1DESPEDIDO!',
        'No encajas en mi colectivo.',
        'Vas a ser expulsado de la hermandad.',
        'No pareces defender los intereses comunes.',
        'Ese atuendo no es propio de tu colectivo.',
        'Te gusta sacar los pies del tiesto, \xc2\xbfeh?',
        'Te voy a expulsar del colegio profesional.',
        'Un esquirol, \xc2\xbfeh? \xc2\xa1Vas a ver!',
        'No defiendes bien las ideas del colectivo.',
        'Rel\xc3\xa1jate; esto es por el bien del colectivo.'],
    'mh': [
        '\xc2\xbfEst\xc3\xa1s listo para mi escena?',
        '\xc2\xa1Luces, c\xc3\xa1maras, acci\xc3\xb3n!',
        '\xc2\xa1Estamos rodando!',
        '\xc2\xa1Hoy te toca desempe\xc3\xb1ar el papel del dibu derrotado!',
        'Por esta escena me van a dar el Oscar.',
        'Acabo de encontrar la inspiraci\xc3\xb3n para esta escena.',
        '\xc2\xbfEst\xc3\xa1s listo para tu escena final?',
        'No vas a aparecer ni en los cr\xc3\xa9ditos finales.',
        'No pienso firmarte ni un aut\xc3\xb3grafo.',
        'Voy a rodar contigo una escena de terror.',
        '\xc2\xa1Me encanta zurrar a los extras como t\xc3\xba!',
        'Espero que no olvides tu parte del gui\xc3\xb3n.'],
    'nc': [
        'Parece que tu balance no cuadra.',
        'Creo que tienes un d\xc3\xa9ficit enorme.',
        'D\xc3\xa9jame que equilibre tus cuentas.',
        '\xc2\xa1Est\xc3\xa1s en n\xc3\xbameros rojos!',
        '\xc2\xa1Vas a tener que contabilizar tu factura del hospital!',
        '\xc2\xbfEn qu\xc3\xa9 columna te pongo? \xc2\xbfDebe o haber?',
        'Eres un cero a la izquierda.',
        'Tu presupuesto est\xc3\xa1 muy desequilibrado.',
        'Cuando acabe contigo no vas a saber ni contar.',
        'Voy a contar las veces que te machaco.'],
    'ls': [
        'Es la hora de que pagues tu pr\xc3\xa9stamo.',
        'Te he prestado demasiado tiempo.',
        'Es el momento del vencimiento.',
        'Venga, vamos a saldar cuentas.',
        'Pediste un anticipo y te lo voy a dar.',
        'Vas a pagar por esto.',
        'Lleg\xc3\xb3 el d\xc3\xada del ajuste de cuentas.',
        '\xc2\xbfMe prestas una oreja?',
        'Me alegro de que est\xc3\xa9s aqu\xc3\xad; quiero lo que es m\xc3\xado.',
        'Voy a prestarte una paliza.',
        'Te voy a ofrecer un inter\xc3\xa9s especial.'],
    'mb': [
        'Es la hora de recoger la calderilla.',
        'Eres dinero suelto para m\xc3\xad.',
        '\xc2\xbfEn efectivo o con tarjeta?',
        '\xc2\xbfTienes el recibo?',
        'Recuerda que el dinero no da la felicidad.',
        'Me parece que andas escaso de fondos.',
        'Vas a tener un peque\xc3\xb1o problema de efectivo.',
        'Despu\xc3\xa9s de esto, te veo pidiendo calderilla.',
        'Soy demasiado rico para mancharme las manos contigo.',
        '\xc2\xa1No hay dinero suficiente para satisfacerme!'],
    'rb': [
        'Te han robado.',
        'Te voy a robar la victoria.',
        '\xc2\xa1Soy un bar\xc3\xb3n del incordio!',
        'Soy la nobleza avasalladora.',
        'Vas a tener que denunciar este robo.',
        'Tengo la sangre azul... Veamos la tuya.',
        'Soy un rival noble.',
        'Te voy a dejar pelado.',
        'Supongo que esto es un robo a mano desarmada.',
        '\xc2\xbfNo sab\xc3\xadas que no se debe hablar con desconocidos?'],
    'bs': [
        'Nunca me des la espalda.',
        'Te voy a dar un buen espaldarazo.',
        'Vas de espaldas por la vida.',
        'Se me da bien cortar el lomo.',
        '\xc2\xbfTe hago la acupuntura en la espalda?',
        '\xc2\xa1De espaldas contra la pared!',
        '\xc2\xbfQuieres que te haga cosquillas en la espalda?',
        'Me encanta jugar con las espalderas.',
        'Deja que te rasque la espalda.',
        '\xc2\xa1Date la vuelta, alguien viene!',
        '\xc2\xa1Mira, a tu espalda!'],
    'bw': [
        '\xc2\xbfQuieres que te pase el cepillo?',
        'S\xc3\xb3lo de verte se me riza el pelo.',
        'Si quieres hacemos esto permanente.',
        'Creo que vas a tener las puntas un poco abiertas.',
        'Creo que est\xc3\xa1s un poco biso\xc3\xb1o.',
        'Te voy a te\xc3\xb1ir todo el cuerpo de morado.',
        'Has venido justo a tiempo para que te d\xc3\xa9 un buen repaso.',
        'Se te va a caer el pelo.',
        'S\xc3\xb3lo de verte me salen entradas.',
        'Se te va a poner el pelo blanco.'],
    'le': [
        'Creo que no tienes defensa posible. ',
        'Estoy picado contigo.',
        'Va a caer todo el peso de la ley encima de ti.',
        'Deber\xc3\xadas saber que, cuando llevo la toga, soy implacable.',
        'Lo tuyo es un caso perdido de antemano.',
        'Creo que te va a caer cadena perpetua.',
        'Esto es tan divertido que deber\xc3\xada ser ilegal.',
        'Lo siento; te tendr\xc3\xa1s que defender a ti mismo.',
        'Mis honorarios son bastante altos. \xc2\xbfPodr\xc3\xa1s permit\xc3\xadrtelos?',
        'Te voy a hacer trizas en el estrado.'],
    'sd': [
        'Voy a anunciar tu fin.',
        'Deja que proclame tu derrota.',
        'El portavoz va anunciar tu desaparici\xc3\xb3n.',
        'El mundo entero va a saber lo acabado que est\xc3\xa1s.',
        'Te vendr\xc3\xada bien alguien que hablase por ti.',
        '\xc2\xa1Uy! \xc2\xa1Al verte se me corta la voz!',
        'Deja que me aclare la voz un momento.',
        'Cuando acabe contigo no vas a tener voz ni voto.',
        'Podr\xc3\xada anunciar mi victoria antes de tiempo.',
        'Damas y caballeros, este dibu es penoso.'],
    'f': [
        '\xc2\xa1Me voy a chivar al jefe de ti!',
        '\xc2\xa1Soy un secuaz, pero soy muy pertinaz!',
        'Gracias a ti voy a conseguir un ascenso.',
        'No creo que te guste mi forma de trabajar.',
        'El jefe cuenta conmigo para ponerte fin.',
        'Vas a hacer que gane puntos ante el jefe.',
        'Primero tendr\xc3\xa1s que v\xc3\xa9rtelas conmigo.',
        'Veamos qu\xc3\xa9 te parece mi trabajo.',
        'Se me da de miedo deshacerme de los dibus.',
        'Nunca llegar\xc3\xa1s a ver a mi jefe.',
        'Te voy a enviar de vuelta al dibuparque.'],
    'p': [
        '\xc2\xa1Voy a borrarte de un plumazo!',
        '\xc2\xa1Ch\xc3\xbapate \xc3\xa9sta, pelele!',
        '\xc2\xa1Voy a cargar las tintas!',
        'Esto est\xc3\xa1 adquiriendo tintes dram\xc3\xa1ticos...',
        'Deja que te aplique un poco de secante.',
        'Te voy a archivar para siempre.',
        'Deprisa, tengo que fichar pronto.',
        'Habr\xc3\xa9 acabado contigo antes de que la tinta se seque.',
        '\xc2\xa1Nuestro encuentro har\xc3\xa1 correr r\xc3\xados de tinta!',
        'Creo que tienes la tinta un poco seca, d\xc3\xa9jame que te vea.',
        '\xc2\xa1Cuidado, que mancho!'],
    'ym': [
        'L\xc3\xa1stima que esto no te vaya a gustar.',
        'Odio que la gente est\xc3\xa9 seria.',
        'Sonr\xc3\xade, la vida es bella... Aunque no para ti.  Una sonrisa vale por cien dibus.',
        'Necesitas algo de alegr\xc3\xada en tu vida.',
        'Despu\xc3\xa9s de esto se te va a quedar sonrisa de tonto.',
        'Mi sonrisa desarma a cualquiera.',
        'Al verte, he sonre\xc3\xaddo m\xc3\xa1s todav\xc3\xada.',
        '\xc2\xbfTe gusta mi sonrisa? \xc2\xa1Vas a recordarla mucho tiempo!',
        'Te veo y sonr\xc3\xado para mis adentros.',
        '\xc2\xbfUna sonrisita antes de que acabe contigo?',
        'No sonr\xc3\xades nada... No me extra\xc3\xb1a.'],
    'mm': [
        '\xc2\xa1Voy tomar el control de tus negocios!',
        'Las grandes palizas vienen a veces en frasco peque\xc3\xb1o.',
        'Ning\xc3\xban reto que queda grande.',
        'Cuando quiero que algo salga bien, lo hago yo mismo.',
        'Necesitas a alguien que te gestione bien.',
        '\xc2\xa1Qu\xc3\xa9 bien, un proyecto!',
        'Te voy a gestionar una buena lecci\xc3\xb3n.',
        'Hay que reorganizarte la agenda del d\xc3\xada.',
        'Voy a gestionar tu presencia aqu\xc3\xad.',
        'Estoy vigilando todos tus movimientos.',
        '\xc2\xbfSeguro que te atreves?',
        'Haremos esto a mi manera.',
        'No te pienso quitar el ojo de encima.',
        'Vas a ver lo que es acoso laboral.'],
    'ds': [
        '\xc2\xa1Vas a irte a la calle!',
        'Tu puesto de trabajo peligra.',
        'Creo que tu perfil no se ajusta a mis necesidades.',
        'Ya no nos eres de utilidad.',
        'Yo que t\xc3\xba empezaba a pedir entrevistas.',
        'Tendr\xc3\xa9 que hacer algunos ajustes de plantilla.',
        'Tienes poco futuro en mi empresa.',
        'Voy a tener que hacer algunos recortes.'],
    'cc': [
        'Hola, \xc2\xbfllevas algo suelto?',
        'Te devolver\xc3\xa9 lo que te debo ma\xc3\xb1ana sin falta.',
        '\xc2\xbfMe dejas que llame desde tu m\xc3\xb3vil?',
        '\xc2\xbfMe invitas a comer? Me dejado la cartera en casa.',
        '\xc2\xbfQu\xc3\xa9 tienes hoy de comida?',
        'Me gusta tu ropa; creo que me la voy a quedar.',
        'Hoy vas a prestarme dinerito, \xc2\xbfverdad?',
        'No te preocupes; siempre lo devuelvo todo.',
        'Creo que me voy a quedar una semanita en tu casa.',
        'Creo que voy a hacer unos recados en tu coche.',
        'Seguro que tus zapatos me quedan bien.',
        'Me encanta como cocinas; \xc2\xa1voy a aficionarme a tu casa!',
        'He puesto mi l\xc3\xadnea telef\xc3\xb3nica a tu nombre.'],
    'tm': [
        'Nunca he visto un producto peor que t\xc3\xba.',
        'Con mi superquitamanchas salen borrones como t\xc3\xba.',
        'Te voy a aplastar con mi megabdominator.',
        'Si acabo contigo, me regalo un cuchillo de cocina.',
        'Tu final est\xc3\xa1 disponible con una llamada.  \xc2\xa1Date prisa! \xc2\xa1Tu fin est\xc3\xa1 al caer!',
        'Acabe con los dibus molestos con "zurradibu".',
        '\xc2\xa1Te voy a poner los super\xc3\xa9xitos de los bots!',
        '\xc2\xbfCansado de tu figura? \xc2\xa1Yo tengo la soluci\xc3\xb3n!',
        '\xc2\xbfNo sabes qu\xc3\xa9 hacer con tu pelo? \xc2\xa1Ll\xc3\xa1mame!',
        'Acepto tarjetas de cr\xc3\xa9dito.',
        'Cuando acabe contigo, no habr\xc3\xa1s probado nada igual.'],
    'nd': [
        'Seguro que mi coche corre m\xc3\xa1s que el tuyo. ',
        'Supongo que sabr\xc3\xa1s que tengo mucho m\xc3\xa1s dinero que t\xc3\xba.',
        'Contigo no tengo ni para empezar.',
        'Venga, deprisa, que tengo que comer con el Sr. Hollywood.',
        '\xc2\xbfTe hab\xc3\xada dicho que conozco al pez gordo?',
        'Soy \xc3\xadntimo amigo del mandam\xc3\xa1s.',
        'Conozco a gente que sabr\xc3\xada encargarse de ti.',
        '\xc2\xbfSabes con qui\xc3\xa9n est\xc3\xa1s hablando?',
        'Acabar\xc3\xa9 r\xc3\xa1pidamente contigo; he quedado con gente importante.',
        'Lo siento; no me suelo codear con dibus como t\xc3\xba.'],
    'gh': [
        '\xc2\xa1Hombre, un dibu! \xc2\xa1Qu\xc3\xa9 alegr\xc3\xada machacarte!',
        '\xc2\xa1Qu\xc3\xa9 bien! \xc2\xa1Un dibu al que zurrar!',
        '\xc2\xa1Me lo voy a pasar de lo lindo contigo!',
        '\xc2\xa1Yupiii! \xc2\xa1Ten\xc3\xada ganas de v\xc3\xa9rmelas con un dibu!',
        '\xc2\xa1Vas a ver lo que es bueno!',
        '\xc2\xa1C\xc3\xb3mo me alegro de no volver a verte!',
        'Encantado de conocer... \xc2\xa1tu fin!',
        '\xc2\xa1Cu\xc3\xa1nto tiempo sin verte! \xc2\xa1Y cu\xc3\xa1nto m\xc3\xa1s va a pasar!',
        '\xc2\xa1He estado a\xc3\xb1os esperando este momento!',
        '\xc2\xa1Me siento feliz de poder zurrarte!',
        '\xc2\xa1Hurra! \xc2\xa1Un dibu tiernecito!',
        '\xc2\xa1Hoooola! \xc2\xbfC\xc3\xb3mo quieres que acabe contigo?',
        '\xc2\xa1Un dibu! \xc2\xa1D\xc3\xa9jame que te estreche bien la mano!'],
    'sc': [
        '\xc2\xa1Voy a hacerte calderilla!',
        'Vas a tener un peque\xc3\xb1o problema de efectivo.',
        'No acepto tus divisas.',
        'No tengo cambio para ti.',
        'Cuando acabe contigo, no vas a valer ni un c\xc3\xa9ntimo.',
        'Creo que la inflaci\xc3\xb3n te va a venir muy mal.',
        'Te voy a depreciar en breve.',
        'Mmm, creo que no llevo dibus sueltos.',
        'Cuando acabe contigo no te va a quedar ni un c\xc3\xa9ntimo.',
        '\xc2\xbfLlevas calderilla para tu vuelta al dibuparque?',
        'No acepto propinas de un dibu.'],
    'pp': [
        'Espera, te voy a aligerar de peso. ',
        '\xc2\xbfNo notas que te falta algo?',
        'Yo que t\xc3\xba guardar\xc3\xada bien la cartera.',
        '\xc2\xbfTe has acordado de cerrar con llave tu casa?',
        'Me encanta tu reloj; creo que me lo voy a quedar.',
        'Vas a volver al dibuparque pelado de gominolas.',
        'Lo siento; tengo que requisarte unas cosillas.',
        '\xc2\xbfMe dejas ver qu\xc3\xa9 llevas en los bolsillos?',
        '\xc2\xbfAlgo que declarar?',
        '\xc2\xa1Otro dibu al que desplumar!'],
    'tw': [
        'No esperes que d\xc3\xa9 ni los buenos d\xc3\xadas.',
        'Para ti soy el Sr. Ro\xc3\xb1oso.',
        'Voy a cortarte los fondos.',
        '\xc2\xbfEs \xc3\xa9sa la mejor oferta que tienes?',
        'Venga, deprisa. El tiempo es oro.',
        '\xc2\xa1Soy de la hermandad del pu\xc3\xb1o cerrado!',
        'Creo que tu oferta no me convence.',
        'Vas a tener que ofrecer mucho m\xc3\xa1s, me temo.',
        'A ver si puedes permitirte esto.',
        'No te pienso dar ni una oportunidad.',
        'Voy a pegarles un buen bocado a tus fondos.'],
    'bc': [
        'Me encanta contar cuentos a los dibus.',
        'Cuenta conmigo para pasarlo mal.',
        'Cuenta con que te voy a zurrar bien.',
        '\xc2\xbfTe cuento un cuento de miedo?',
        'Aqu\xc3\xad el que cuenta soy yo.',
        'Cuenta con volver al dibuparque.',
        'Despu\xc3\xa9s de esto, no lo vas a contar.',
        'Este cuento va a acabar mal para ti.',
        'No tengas cuento...',
        'Cuando acabe contigo, no te van a salir las cuentas.',
        'Ten\xc3\xada unas cuantas cuentas pendientes contigo...'],
    'bf': [
        'Todos me dicen que tengo mucho morro.',
        'Siempre le echo morro a la vida.',
        'Hay que tener morro para venir aqu\xc3\xad.',
        'Tienes bastante morro, \xc2\xbfno crees?',
        'Justo a tiempo, te voy a hinchar los morros.',
        'Tengo un morro que me lo piso.',
        'Para ganarme le vas a tener que echar mucho morro.',
        'Tu morro no est\xc3\xa1 a la altura de las circunstancias.',
        'Te voy a mandar al dibuparque de un morrazo.',
        'Vas a ver mis morros por \xc3\xbaltima vez.'],
    'tf': [
        '\xc2\xa1Por fin nos vemos las caras!',
        '\xc2\xa1Vas a tener que encarar la derrota!',
        '\xc2\xbfA que no sabes hacia d\xc3\xb3nde estoy mirando?',
        'Como tengo dos caras, es dif\xc3\xadcil que me las rompan.',
        'Dos caras son mejor que una.',
        '\xc2\xbfCu\xc3\xa1l de mis dos caras te gusta m\xc3\xa1s?',
        'Creo que te llaman en el dibuparque.',
        '\xc2\xbfQu\xc3\xa9 cara quieres que se encargue de ti?',
        'Tengo bastante m\xc3\xa1s cara que t\xc3\xba.',
        'No sabes la cara que tengo...',
        'Lo mire por donde lo mire, siempre te veo...'],
    'dt': [
        'Ha llegado el momento de embaucar a alguien.',
        'Oye, hay un elefante detr\xc3\xa1s de ti.',
        '\xc2\xbfQuieres que le eche un poco de cara al asunto?',
        '\xc2\xbfCu\xc3\xa1l de mis dos caras dice la verdad?',
        'Yo que t\xc3\xba encaraba la salida.',
        'No te va a gustar mi doble juego.',
        'Yo que t\xc3\xba me lo pensaba dos veces.',
        'Prep\xc3\xa1rate para una raci\xc3\xb3n DOBLE.',
        'Vas a ver mis caras en sue\xc3\xb1os.',
        'Para vencerme hacen falta dos como t\xc3\xba.'],
    'ac': [
        '\xc2\xa1Te voy a perseguir hasta el dibuparque!',
        '\xc2\xbfNo oyes una sirena?',
        'Ja, ja, c\xc3\xb3mo voy a disfrutar.',
        'Me encanta la emoci\xc3\xb3n de la persecuci\xc3\xb3n.',
        '\xc2\xa1Corre, corre, que te pillo!',
        '\xc2\xbfTe has hecho un seguro?',
        'Espero que te hayas tra\xc3\xaddo una camilla.',
        'Dudo que aguantes mi ritmo.',
        'A partir de aqu\xc3\xad se te va a hacer todo cuesta arriba.',
        'Pronto vas a necesitar atenci\xc3\xb3n m\xc3\xa9dica urgente.',
        'Esto no es para re\xc3\xadrse.',
        'Espero que te gusten los hospitales.'] }
SuitAttackDefaultTaunts = [
    '\xc2\xa1Toma ya!!',
    '\xc2\xa1F\xc3\xadjate bien en esto!']
SuitAttackNames = {
    'Audit': '\xc2\xa1Auditor\xc3\xada!',
    'Bite': '\xc2\xa1Mordisco!',
    'BounceCheck': 'Cheque sin fondos!',
    'BrainStorm': '\xc2\xa1Aguacero!',
    'BuzzWord': '\xc2\xa1Charlat\xc3\xa1n!',
    'Calculate': '\xc2\xa1Calculadora!',
    'Canned': '\xc2\xa1Enlatado!',
    'Chomp': '\xc2\xa1Zamp\xc3\xb3n!',
    'CigarSmoke': '\xc2\xa1Humo de Cigarro!',
    'ClipOnTie': '\xc2\xa1Corbat\xc3\xb3n!',
    'Crunch': '\xc2\xa1Crujido!',
    'Demotion': '\xc2\xa1Degradaci\xc3\xb3n!',
    'Downsize': '\xc2\xa1Recorte de plantilla!',
    'DoubleTalk': '\xc2\xa1Embaucar!',
    'EvictionNotice': '\xc2\xa1Deshaucio!',
    'EvilEye': '\xc2\xa1Mal de ojo!',
    'Filibuster': '\xc2\xa1Discurso plasta!',
    'FillWithLead': '\xc2\xa1Lleno de Plomo!',
    'FiveOClockShadow': '\xc2\xa1Barbudo!',
    'FingerWag': '\xc2\xa1Rega\xc3\xb1ado!',
    'Fired': '\xc2\xa1Despedido!',
    'FloodTheMarket': '\xc2\xa1Saturar el Mercado!',
    'FountainPen': '\xc2\xa1Manch\xc3\xb3n de tinta!',
    'FreezeAssets': '\xc2\xa1Activos congelados!',
    'Gavel': '\xc2\xa1Martillo!',
    'GlowerPower': '\xc2\xa1Mirada feroz!',
    'GuiltTrip': '\xc2\xa1Culpable!',
    'HalfWindsor': '\xc2\xa1Nudo imposible!',
    'HangUp': '\xc2\xa1Corte de l\xc3\xadnea!',
    'HeadShrink': '\xc2\xa1Reducci\xc3\xb3n de cabeza!',
    'HotAir': '\xc2\xa1Aire caliente!',
    'Jargon': '\xc2\xa1Jerga jur\xc3\xaddica!',
    'Legalese': '\xc2\xa1Parrafada legal!',
    'Liquidate': '\xc2\xa1Liquidaci\xc3\xb3n!',
    'MarketCrash': '\xc2\xa1Desplome de bolsa!',
    'MumboJumbo': '\xc2\xa1Rollo total!',
    'ParadigmShift': '\xc2\xa1Cambio de rumbo!',
    'PeckingOrder': '\xc2\xa1Pajarraco!',
    'PickPocket': '\xc2\xa1Caco!',
    'PinkSlip': '\xc2\xa1Carta de despido!',
    'PlayHardball': '\xc2\xa1\xc3\x9altima partida!',
    'PoundKey': '\xc2\xa1Factura de tel\xc3\xa9fono!',
    'PowerTie': '\xc2\xa1Corbata feroz!',
    'PowerTrip': '\xc2\xa1Viajecito!',
    'Quake': '\xc2\xa1Terremoto!',
    'RazzleDazzle': '\xc2\xa1Sonrisote!',
    'RedTape': '\xc2\xa1Cinta roja!',
    'ReOrg': '\xc2\xa1Reorganizaci\xc3\xb3n!',
    'RestrainingOrder': '\xc2\xa1Orden de alejamiento!',
    'Rolodex': '\xc2\xa1Agenda!',
    'RubberStamp': '\xc2\xa1Sellazo!',
    'RubOut': '\xc2\xa1Borrado!',
    'Sacked': '\xc2\xa1Al saco!',
    'SandTrap': '\xc2\xa1Arenas movedizas!',
    'Schmooze': '\xc2\xa1Adulaci\xc3\xb3n!',
    'Shake': '\xc2\xa1Sacudida!',
    'Shred': '\xc2\xa1Triturador!',
    'SongAndDance': '\xc2\xa1Canto y danza!',
    'Spin': '\xc2\xa1Giro loco!',
    'Synergy': 'Sinergia!',
    'Tabulate': '\xc2\xa1Contabilidad!',
    'TeeOff': '\xc2\xa1Bolazo!',
    'ThrowBook': '\xc2\xa1Tirar el libro!',
    'Tremor': '\xc2\xa1Trepidaci\xc3\xb3n!',
    'Watercooler': '\xc2\xa1Nevera!',
    'Withdrawal': '\xc2\xa1Retidada de fondos!',
    'WriteOff': '\xc2\xa1Agujero contable!' }
SuitAttackTaunts = {
    'Audit': [
        'Creo que no te cuadran las cuentas.',
        'Parece que est\xc3\xa1s en n\xc3\xbameros rojos.',
        'Deja que te ayude con la contabilidad.',
        'Tu columna de d\xc3\xa9bito est\xc3\xa1 por las nubes. ',
        'Voy a echar un vistazo a tus activos.',
        'Esto te va a desequilibrar las cuentas.',
        'Voy a examinar de cerca lo que debes.',
        'Con esto voy a dejar tu cuenta a cero.',
        'Es la hora de contabilizar tus gastos.',
        'He encontrado un error en tu libro de contabilidad.'],
    'Bite': [
        '\xc2\xbfTe apetece un mordisquito?',
        '\xc2\xa1Prueba un poco de esto!',
        'Perro ladrador, poco mordedor.',
        '\xc2\xa1Hoy estoy que muerdo!',
        '\xc2\xa1Vas a morder el polvo!',
        'Cuidado, que muerdo.',
        'Muerdo siempre que puedo.',
        'Voy a morderte un poquito.',
        'No me pienso morder la lengua contigo.',
        'S\xc3\xb3lo un mordisquito...  \xc2\xbfEs pedir demasiado?'],
    'BounceCheck': [
        'Qu\xc3\xa9 l\xc3\xa1stima, eres un rollo.',
        'Tienes pendiente un pago.',
        'Creo que este cheque es tuyo.',
        'Me debes este cheque.',
        'Estoy cobrando deudas atrasadas.',
        'Este cheque est\xc3\xa1 al rojo vivo.',
        'Te voy a pasar un buen recargo.',
        'Echa un vistazo a esto.',
        'Esto te va a costar una buena pasta.',
        'Me gustar\xc3\xada cobrar esto.',
        'Voy a devolverte este regalito.',
        '\xc3\x89ste ser\xc3\xa1 tu tal\xc3\xb3n de Aquiles.',
        'Voy a incluir una penalizaci\xc3\xb3n.'],
    'BrainStorm': [
        'Mi predicci\xc3\xb3n es que va a llover.',
        'Espero que lleves paraguas.',
        'Voy a remojarte un poco.',
        '\xc2\xbfQu\xc3\xa9 te parecen unas cuantas GOTITAS?',
        'Ya no hace un d\xc3\xada tan bueno, \xc2\xbfeh, dibu?',
        '\xc2\xbfEst\xc3\xa1s listo para un aguacero?',
        'Vas a ver lo que es una buena tormenta.',
        'A esto lo llamo ataque rel\xc3\xa1mpago.',
        'Me encanta ser un aguafiestas.'],
    'BuzzWord': [
        'Deja que te diga unas palabras.',
        '\xc2\xbfTe has enterado de lo \xc3\xbaltimo?',
        'A ver si pillas esto.',
        'Intenta pronunciar esto, dibu.',
        'Deja que te ponga los puntos sobre las \xc3\xades.',
        'Te doy mi palabra de que ser\xc3\xa9 claro.',
        'Deber\xc3\xadas medir mejor tus palabras.',
        'A ver c\xc3\xb3mo esquivas esto.',
        'Cuidado, esto no es un juego de palabras.',
        'D\xc3\xa9jate de palabrer\xc3\xada y prueba esto.'],
    'Calculate': [
        '\xc2\xa1Con esto te van a salir las cuentas!',
        '\xc2\xbfHab\xc3\xadas contado con esto?',
        'Suma y sigue; est\xc3\xa1s acabado.',
        'Espera; te voy a ayudar a sumar esto.',
        '\xc2\xbfHas sumado todos tus gastos?',
        'Seg\xc3\xban mis c\xc3\xa1lculos, no estar\xc3\xa1s aqu\xc3\xad mucho tiempo.',
        'Aqu\xc3\xad tienes el total.',
        'Vaya; tu factura no para de aumentar.',
        '\xc2\xa1Ponte a sumar esto!',
        'Bots: 1; Dibus: 0'],
    'Canned': [
        '\xc2\xbfTe gustan las conservas?',
        '"Conserva" esto como recuerdo.',
        '\xc2\xa1Esto est\xc3\xa1 reci\xc3\xa9n salido de la lata!',
        '\xc2\xbfTe han dado el latazo alguna vez?',
        '\xc2\xa1Voy a hacerte una donaci\xc3\xb3n de alimentos en conserva!',
        '\xc2\xa1Prep\xc3\xa1rate para una buena lata!',
        'Me gusta que "conserves" todos tus \xc3\xa1nimos.',
        '\xc2\xa1Te voy a poner en conserva!',
        '\xc2\xa1El men\xc3\xba de hoy va a ser dibu enlatado!',
        '"Conserva" esto para el recuerdo...'],
    'Chomp': [
        '\xc2\xbfQuieres hacer el favor de masticar bien?',
        '\xc2\xa1\xc3\x91am, \xc3\xb1am, \xc3\xb1am!',
        'No te olvides de cerrar la boca al comer.',
        '\xc2\xbfTienes ganas de masticar algo?',
        'Prueba a masticar esto.',
        '\xc2\xa1Vas a ser mi cena!',
        '\xc2\xa1Me encantan las dietas a base de dibus!'],
    'ClipOnTie': [
        '\xc2\xbfPor qu\xc3\xa9 no te arreglas un poco?',
        '\xc2\xa1Tienes que llevar corbata a las reuniones!',
        'Los bots elegantes siempre se ponen una de \xc3\xa9stas...',
        'Pru\xc3\xa9bate \xc3\xa9sta, a ver qu\xc3\xa9 tal te queda.',
        'La imagen es fundamental para tener \xc3\xa9xito en la vida.',
        'Aqu\xc3\xad no se admite a nadie sin corbata.',
        '\xc2\xbfQuieres que te ayude a ponerte esto?',
        'Una buena corbata dice mucho de ti.',
        'Veamos qu\xc3\xa9 tal te sienta esto.',
        'Esto a lo mejor te aprieta un poco.',
        'Es mejor que te arregles antes de MARCHARTE.',
        'Toma, con esto ser\xc3\xa1s el dibu m\xc3\xa1s guapo del dibuparque.'],
    'Crunch': [
        'Parece que est\xc3\xa1s un poco crujido.',
        '\xc2\xa1Es hora de crujirse un poco!',
        'Con esto te van a crujir las articulaciones.',
        '\xc2\xa1Mira qu\xc3\xa9 crujido m\xc3\xa1s delicioso!',
        '\xc2\xbfNo oyes un crujido?',
        '\xc2\xbfQu\xc3\xa9 prefieres, blandito o crujiente?',
        'Esto est\xc3\xa1 crujiente y apetitoso.',
        '\xc2\xa1Prep\xc3\xa1rate para que te crujan los huesos!',
        '\xc2\xa1Me encantan los postres crujientes!'],
    'Demotion': [
        'Vas a bajar puestos en la empresa. ',
        'Vas a volver a trabajar de botones.',
        'Me parece que te has quedado sin despacho.',
        '\xc2\xa1Majo, vas para abajo!',
        'Creo que tu puesto peligra.',
        'Tienes poco futuro en esta empresa.',
        'Laboralmente, est\xc3\xa1s en un callej\xc3\xb3n sin salida.',
        'Tu puesto en la empresa se est\xc3\xa1 tambaleando.',
        'Te veo preparando caf\xc3\xa9 bien pronto.',
        'Esto va a ir directo a tu expediente.'],
    'Downsize': [
        '\xc2\xbfQu\xc3\xa9 tal unos cuantos recortes?',
        'A veces hay que aplicar la tijera.',
        'Yo que t\xc3\xba ir\xc3\xada pidiendo entrevistas de trabajo.',
        '\xc2\xbfHas guardado el suplemento de empleo de tu peri\xc3\xb3dico?',
        '\xc2\xbfNunca te han dicho que eres prescindible?',
        'Tu perfil no se ajusta a nuestras necesidades actuales.',
        '\xc2\xbfHas o\xc3\xaddo hablar de las reestructuraciones?',
        'Me temo que ya no nos eres \xc3\xbatil.',
        '\xc2\xbfPor qu\xc3\xa9 no te buscas un trabajo en otro sitio?',
        'Este a\xc3\xb1o no te comes el turr\xc3\xb3n en esta empresa.',
        'Me temo que los cambios en la empresa te van a afectar.',
        'Me temo que nos sobra algo de personal.'],
    'EvictionNotice': [
        '\xc2\xa1Ha llegado la hora de la mudanza!',
        'Haz las maletas, dibu.',
        'Creo que vas a tener que cambiar de residencia.',
        'Creo que debajo del puente se est\xc3\xa1 muy bien.',
        'Me temo que no has pagado el alquiler.',
        '\xc2\xbfHab\xc3\xadas pensado en redecorar tu vivienda?',
        'A partir de ahora vas a disfrutar del aire libre.',
        '\xc2\xbfNo dec\xc3\xadas que te gustaban los espacios abiertos?',
        '\xc2\xa1Est\xc3\xa1s fuera de lugar!',
        'Prep\xc3\xa1rate para ser reubicado.',
        'Tranquilo; ahora vas a conocer a m\xc3\xa1s gente.'],
    'EvilEye': [
        'Te voy a echar el mal de ojo.',
        '\xc2\xbfPuedes echarle un ojo a esto?',
        'Espera.  Se me ha metido algo en el ojo.',
        '\xc2\xa1Te he puesto el ojo encima!',
        'En la vida hay que tener ojo para todo.',
        'Tengo mucho ojo para el mal.',
        '\xc2\xa1Te voy a meter el dedo en el ojo!',
        '\xc2\xa1Ten mucho ojo conmigo!',
        '\xc2\xa1Te voy a meter en el ojo del hurac\xc3\xa1n!',
        '\xc2\xa1No te pienso quitar ojo!'],
    'Filibuster': [
        '\xc2\xbfTe gustan los discursos?',
        'Esto va a durar un ratito.',
        'Podr\xc3\xada estar as\xc3\xad todo el d\xc3\xada.',
        'No me hace falta tomarme ni un respiro.',
        'Puedo seguir y seguir.',
        'Nunca me canso de hacer esto.',
        'Soy capaz de aburrir a las ovejas.',
        '\xc2\xbfTe importa si digo unas palabras?',
        'Creo que voy a soltar un discursito.',
        'Tengo preparadas unas frases para ti.'],
    'FingerWag': [
        'Te lo he dicho un mill\xc3\xb3n de veces.',
        'Dibu, te estoy hablando a ti.',
        'No me hagas re\xc3\xadr.',
        'No me hagas ir hasta ah\xc3\xad.',
        'Estoy harto de repet\xc3\xadrtelo.',
        'Creo que ya te hab\xc3\xada dicho esto.',
        'No nos guardas ning\xc3\xban respeto a los bots.',
        'Es hora de que empieces a prestar atenci\xc3\xb3n.',
        'Bla, bla, bla, bla, bla.',
        'Voy a tener que aplicarte un correctivo.',
        '\xc2\xbfCu\xc3\xa1ntas veces te lo tengo que decir?',
        'No es la primera vez que pasa esto.'],
    'Fired': [
        'Espero que te hayas tra\xc3\xaddo algo para la barbacoa.',
        'Esto va a ponerse calentito.',
        'Seguro que con esto entres en calor.',
        'Espero que seas un animal de sangre fr\xc3\xada.',
        '\xc2\xa1Caliente, caliente!',
        'Creo que te va a hacer falta un extintor.',
        '\xc2\xa1Vas a quedarte chamuscado!',
        '\xc2\xa1Vas a quedar muy doradito!',
        'Esto le da otro significado a la expresi\xc3\xb3n "bien hecho".',
        'Espero que te hayas puesto protecci\xc3\xb3n solar.',
        'Av\xc3\xadsame cuando est\xc3\xa9s crujiente.',
        'La cosa est\xc3\xa1 que arde.',
        'Vas a arder en deseos de volver al dibuparque.',
        'Creo que tienes un temperamento ardiente.',
        'A ver, d\xc3\xa9jame que te ponga el term\xc3\xb3metro...',
        '\xc2\xa1Tienes mucha chispa!',
        'El que juega con fuego...',
        '\xc2\xbfNunca te han dicho que te sale humo de las orejas?'],
    'FountainPen': [
        'Esta mancha no va a salir. ',
        'Vas a tener que ir a la tintorer\xc3\xada.',
        'Prep\xc3\xa1rate para comprar detergente.',
        'Esto no es precisamente tinta invisible.',
        'Vas a tener que cambiarte de ropa.',
        'La tinta de esta pluma no se acaba nunca.',
        'Toma, usa mi pluma.',
        '\xc2\xbfLees bien mi letra?',
        'Ya no hacen plumas como las de antes.',
        'Vaya, hay un borr\xc3\xb3n en tu expediente.',
        'Te dije que no cargaras las tintas.'],
    'FreezeAssets': [
        '\xc2\xbfTe sirvo un poco de hielo?',
        'Te voy a juzgar por tus acciones.',
        'Me parece que voy a pasar a la acci\xc3\xb3n.',
        'Voy a congelar la imagen.',
        'El ambiente est\xc3\xa1 muy fr\xc3\xado.',
        'Este a\xc3\xb1o se va a adelantar el invierno.',
        'Esto te enfriar\xc3\xa1 los \xc3\xa1nimos.',
        'Mi plan est\xc3\xa1 a punto de cristalizar.',
        'Te vas a quedar petrificado.',
        'Se te van a congelar las ideas.',
        '\xc2\xbfTe gustan las cenas fr\xc3\xadas?',
        'Voy a refrescarte la memoria.'],
    'GlowerPower': [
        '\xc2\xbfMe miras a m\xc3\xad?',
        'Me han dicho que tengo una mirada penetrante.',
        'M\xc3\xadrame fijamente a los ojos...',
        '\xc2\xbfTe gusta mi ca\xc3\xadda de ojos?',
        'Tengo una mirada arrebatadora.',
        '\xc2\xbfNo te parecen unos ojos muy expresivos?',
        'Siempre me han dicho que tengo unos ojos preciosos.',
        'El secreto est\xc3\xa1 en la mirada.',
        '\xc2\xa1Veo, veo! \xc2\xa1Veo un dibu en apuros!',
        'Deja que te mire bien...',
        '\xc2\xbfEchamos una mirada a tu futuro?'],
    'GuiltTrip': [
        '\xc2\xa1Vas a cargar con toda la culpa!',
        '\xc2\xbfTe sientes culpable?',
        '\xc2\xa1Todo es culpa tuya!',
        '\xc2\xa1Te pienso culpar por todo!',
        '\xc2\xa1Has sido declarado culpable!',
        '\xc2\xa1No pienso volver a hablarte!',
        '\xc2\xa1M\xc3\xa1s te valdr\xc3\xada pedir perd\xc3\xb3n!',
        '\xc2\xa1No te pienso perdonar en la vida!',
        '\xc2\xbfNo crees que te has portado mal?',
        '\xc2\xa1No intentes echarme la culpa!',
        '\xc2\xa1Eres un culpable con causa!'],
    'HalfWindsor': [
        '\xc2\xa1\xc3\x89sta es la corbata m\xc3\xa1s bonita que has visto en tu vida!',
        'Intenta no hacerte un nudo.',
        'Se te va a poner un nudo en el est\xc3\xb3mago.',
        'Tienes suerte de que sea un nudo f\xc3\xa1cil.',
        '\xc2\xbfNo se te hace un nudo en la garganta?',
        '\xc2\xa1Seguro que no sabes ni hacerte el nudo!',
        '\xc2\xa1Despu\xc3\xa9s de esto te voy a anudar la lengua!',
        'No deber\xc3\xada malgastar esta corbata contigo.',
        '\xc2\xa1No te mereces esta corbata tan bonita!'],
    'HangUp': [
        'Se ha cortado tu llamada.',
        '\xc2\xa1Adi\xc3\xb3s!',
        'Es el momento de terminar la conexi\xc3\xb3n.',
        '... \xc2\xa1Y no vuelvas a llamarme!',
        '\xc2\xa1Clic!',
        'Se acab\xc3\xb3 la conversaci\xc3\xb3n.',
        'Voy a cortar la l\xc3\xadnea.',
        'Creo que tienes la l\xc3\xadnea en mal estado.',
        'Me parece que no tienes l\xc3\xadnea.',
        'Ha finalizado tu llamada.',
        'Espero que me escuches alto y claro.',
        'Te has equivocado de n\xc3\xbamero.'],
    'HeadShrink': [
        '\xc2\xbfHas estado \xc3\xbaltimamente en el Amazonas?',
        'Cari\xc3\xb1o, he encogido a un dibu.',
        'Espero que tu orgullo no se quede encogido.',
        '\xc2\xbfHas encogido en la lavadora?',
        'Te he dicho que no te laves con agua caliente.',
        'No pierdas la cabeza por esto.',
        '\xc2\xbfEs que has perdido la cabeza?',
        '\xc2\xa1Pero qu\xc3\xa9 poca cabeza tienes!',
        '\xc2\xa1Eres un cabeza de chorlito!',
        'No sab\xc3\xada que hab\xc3\xadas pasado una temporada con los j\xc3\xadbaros.'],
    'HotAir': [
        'El ambiente se est\xc3\xa1 acalorando.',
        'Vas a sufrir una ola de calor.',
        'He llegado al punto de ebullici\xc3\xb3n.',
        'Me parece que te vas a achicharrar un poco.',
        'Vas a quedar un poco doradito...',
        'Recuerda: si ves humo, es que hay fuego.',
        'Te veo un poco quemado.',
        'Creo que hoy va a haber fumata blanca.',
        'Supongo que es la hora de avivar un poco el fuego.',
        'Perm\xc3\xadteme que encienda la llama del amor.',
        '\xc2\xa1Esto se va a poner al rojo vivo!',
        '\xc2\xbfTe seco un poco el pelo?'],
    'Jargon': [
        'Qu\xc3\xa9 cantidad de tonter\xc3\xadas se dicen...',
        'A ver si adivinas qu\xc3\xa9 significa esto.',
        'Espero que me recibas alto y claro.',
        'Me parece que voy a tener que hablar m\xc3\xa1s alto.',
        'Insisto; es mi turno para hablar.',
        'Te voy a ser muy sincero.',
        'He de pontificar sobre este asunto.',
        '\xc2\xbfVes? Las palabras pueden hacer da\xc3\xb1o.',
        '\xc2\xbfHas pillado lo que quiero decir?',
        'Palabras, palabras, palabras...'],
    'Legalese': [
        'Debes cejar en tu empe\xc3\xb1o.',
        'En t\xc3\xa9rminos legales, vas a perder el juicio.',
        '\xc2\xbfEst\xc3\xa1s al tanto de las connotaciones legales?',
        '\xc2\xa1No puedes situarte al margen de la ley!',
        'Deber\xc3\xadan hacer una ley expresamente contra ti.',
        'Me reservo el derecho de modificar tu contrato.',
        'Las opiniones expresadas en este ataque no coinciden con las de Toontown Online.',
        'No me hago responsable de los da\xc3\xb1os derivados de este ataque.',
        'Vas a asumir los costes directos e indirectos de este ataque.',
        'Me reservo el derecho de prolongar este ataque.',
        '\xc2\xa1Est\xc3\xa1s fuera de mi sistema legal!',
        'No vas a poder asumir los costes legales de este ataque.'],
    'Liquidate': [
        'Me encanta que nuestra relaci\xc3\xb3n sea fluida.',
        '\xc2\xbfEst\xc3\xa1s teniendo problemas de liquidez?',
        'Voy a tener que ponerte en remojo.',
        'Hay que dar fluidez a este proceso.',
        '\xc2\xa1Recuerda que el suelo est\xc3\xa1 resbaladizo!',
        'Tu dinero es papel mojado.',
        'En esta vida hay que mojarse un poco.',
        'Te voy a poner en venta al 50 %.',
        'Te vas a diluir un poco...',
        'Me apetece un dibu pasado por agua.'],
    'MarketCrash': [
        'Me parece que tus acciones han ca\xc3\xaddo.',
        'No vas a sobrevivir al cierre de sesi\xc3\xb3n.',
        'Tus valores caen en picado.',
        'Tu cartera de acciones va a quedarse temblando.',
        'Va a ser todo un lunes negro para ti.',
        'Hoy estoy de lo m\xc3\xa1s alcista.',
        'Creo que me voy a desprender de tus acciones.',
        '\xc2\xa1M\xc3\xa1s vale que vendas todo pronto!',
        '\xc2\xa1Vende, r\xc3\xa1pido!',
        'Vas a iniciar una tendencia bajista.',
        'El mercado se va a desplomar encima de ti.'],
    'MumboJumbo': [
        'Voy a ver si me expreso con claridad.',
        'Es as\xc3\xad de sencillo.',
        'Te voy a explicar c\xc3\xb3mo vamos a resolver esto.',
        'Perm\xc3\xadteme que te resuma esto.',
        'A lo mejor esto te suena a discurso.',
        'No quiero soltarte una parrafada, pero...',
        'Vaya; se me llena la boca.',
        'Odio alargarme en mis peroratas.',
        'Perm\xc3\xadteme unas palabrillas.',
        'Tengo preparado un discursito para ti.'],
    'ParadigmShift': [
        '\xc2\xa1Cuidado! Hoy estoy de lo m\xc3\xa1s cambiante.',
        '\xc2\xa1Prep\xc3\xa1rate para un buen golpe de tim\xc3\xb3n!',
        'Creo que hay que enderezar tu rumbo.',
        'Vas a tener un ligero cambio de perspectiva.',
        'Supongo que no vas a tener cambio para esto.',
        '\xc2\xa1Has perdido el norte!',
        'Seguro que nunca has cambiado tanto de orientaci\xc3\xb3n.',
        '\xc2\xa1Creo que no te va a gustar este cambio!',
        '\xc2\xa1No me hagas cambiar de parecer!'],
    'PeckingOrder': [
        'S\xc3\xad; soy todo un p\xc3\xa1jaro.',
        'M\xc3\xa1s vale p\xc3\xa1jaro en mano...',
        'Me ha dicho un pajarito que vas a volver de golpe al dibuparque.',
        '\xc2\xa1No huyas como un gallina!',
        'Creo que tienes la cabeza llena de p\xc3\xa1jaros.',
        '\xc2\xa1Cr\xc3\xada cuervos y tendr\xc3\xa1s muchos!',
        '\xc2\xa1Ya has volado bastante, pajarito!',
        'Me encanta salir de picoteo.',
        'Voy a hacer un buen caldo de gallina contigo.'],
    'PickPocket': [
        'Deja que me haga cargo de tus objetos personales.',
        '\xc2\xbfA ver qu\xc3\xa9 llevas ah\xc3\xad?',
        'Esto es como quitarle un caramelo a un ni\xc3\xb1o.',
        'Menudo robo...',
        'Espera, yo te sujeto eso.',
        'No pierdas de vista mis manos.',
        'La mano es m\xc3\xa1s r\xc3\xa1pida que el ojo...',
        'Nada por aqu\xc3\xad...',
        'La direcci\xc3\xb3n no se hace responsable de los objetos perdidos.',
        'Santa Rita, Rita...',
        'No te vas a dar ni cuenta.',
        'Te voy a dejar desplumado.',
        '\xc2\xbfTe importa si me quedo con esto?',
        'Te voy a aligerar de peso.'],
    'PinkSlip': [
        'Tengo algo de correspondencia para ti.',
        '\xc2\xbfEst\xc3\xa1s asustado? \xc2\xa1Te has puesto p\xc3\xa1lido!',
        'Esta carta te va a hacer mucha ilusi\xc3\xb3n.',
        'Vaya; creo que alguien va a tener que hacer las maletas.',
        '\xc2\xa1Eh, no te vayas sin despedirte!',
        '\xc2\xbfTe has despedido ya de todo el mundo?',
        '\xc2\xa1Mira, una carta de amor!',
        'Creo que este papel es para ti...',
        'La verdad es que \xc3\xa9ste color no te favorece.',
        '\xc2\xa1Aqu\xc3\xad tienes tu carta de despido. Largo de aqu\xc3\xad!'],
    'PlayHardball': [
        '\xc2\xbfAs\xc3\xad que quieres jugar al b\xc3\xa9isbol?',
        'No te recomiendo que juegues conmigo.',
        '\xc2\xa1Batea de una vez!',
        '\xc2\xa1Venga, batea esto!',
        '\xc2\xa1Y aqu\xc3\xad viene el lanzamiento...!',
        'Vas a tener que mandarla lejos.',
        'Te voy a sacar del estadio de un batazo.',
        'Te voy a mandar al dibuparque de un batazo.',
        '\xc2\xa1\xc3\x89sta es tu carrera final!',
        '\xc2\xa1No vas a poder jugar conmigo!',
        '\xc2\xa1Te voy a poner en \xc3\xb3rbita!',
        '\xc2\xa1Vas a ver qu\xc3\xa9 bola te lanzo!'],
    'PoundKey': [
        'Es hora de devolver algunas llamadas.',
        '\xc2\xbfQu\xc3\xa9 tal una llamada a cobro revertido?',
        '\xc2\xa1Ring, ring! \xc2\xa1Es para ti!',
        'Toma, para que me llames cuando quieras.',
        'Me sobra una almohadilla...',
        'Espero que tu tel\xc3\xa9fono sea de tonos.',
        'D\xc3\xa9jame que marque este n\xc3\xbamero.',
        'Voy a hacer una llamada por sorpresa.',
        'Espera, te voy a dar un toque.',
        'Dibu, vas a poder hacer s\xc3\xb3lo una llamada.'],
    'PowerTie': [
        'Te ver\xc3\xa9 m\xc3\xa1s tarde; parece que se te ha hecho un nudo en la garganta.',
        'Voy a atar unos cuantos cabos sueltos.',
        '\xc2\xa1Con esto vas a ir muy elegante!',
        'Para que vayas practicando los nudos...',
        'Ya es hora de que empieces a vestir bien.',
        '\xc2\xa1\xc3\x89sta es la corbata m\xc3\xa1s fea que has visto en tu vida!',
        '\xc2\xbfNo te sientes importante llevando esto?',
        '\xc2\xa1Vas a ver c\xc3\xb3mo cambia tu aspecto!',
        '\xc2\xa1Nada mejor que una corbata de regalo!',
        'No sab\xc3\xada qu\xc3\xa9 regalarte, as\xc3\xad que \xc2\xa1toma!'],
    'PowerTrip': [
        'Haz las maletas, que nos vamos de excursi\xc3\xb3n.',
        '\xc2\xbfHas tenido un buen viaje?',
        'Bonito viaje; te ver\xc3\xa9 el a\xc3\xb1o que viene.',
        '\xc2\xbfQu\xc3\xa9 tal tu viaje?',
        '\xc2\xa1Siento que hayas tenido que venir hasta aqu\xc3\xad!',
        '\xc2\xa1Me parece que vas a irte de viaje!',
        '\xc2\xa1Vas a ver lo que es viajar!',
        '\xc2\xbfTe gusta la astrolog\xc3\xada?',
        '\xc2\xbfQuieres tener una experiencia astral?',
        '\xc2\xa1Vas a ver las estrellas!',
        'Prepara las maletas, te vas de viaje... \xc2\xa1astral!'],
    'Quake': [
        '\xc2\xbfQu\xc3\xa9 tal una sacudidita de tierra?',
        'Me encantan los modelos a escala... Richter.',
        'Eres todo un terremoto, \xc2\xbfeh?',
        '\xc2\xbfA que no sabes d\xc3\xb3nde est\xc3\xa1 el epicentro?',
        '\xc3\x89ste se va a salir de la escala Richter.',
        '\xc2\xa1Con esto se van a sacudir los cimientos!',
        '\xc2\xa1Vas a ver qu\xc3\xa9 meneo!',
        '\xc2\xbfHas sufrido alguna vez un terremoto?',
        '\xc2\xa1Cuidado; la tierra se agita bajo tus pies!'],
    'RazzleDazzle': [
        'L\xc3\xa9eme los labios.',
        '\xc2\xbfTe gustan mis dientes?',
        '\xc2\xbfNo te parezco encantador?',
        'Disfruta de mi encantadora sonrisa...',
        'Mi dentista es un gran profesional.',
        'Una sonrisa cegadora, \xc2\xbfeh?',
        'Parece mentira que sean postizos, \xc2\xbfeh?',
        'Una sonrisa arrebatadora, \xc2\xbfeh?',
        'Suelo anunciar dent\xc3\xadfricos, \xc2\xbfsabes?',
        'Siempre uso seda dental despu\xc3\xa9s de comer.',
        '\xc2\xa1Di "patata"!'],
    'RedTape': [
        'Te voy a envolver para regalo.',
        'Voy a dejar todo atado y bien atado.',
        '\xc2\xa1C\xc3\xb3mo te enrollas!',
        'A ver si puedes cortar esta cinta roja.',
        'Vas a estar un poco estrecho ah\xc3\xad.',
        'Espero que no tengas claustrofobia.',
        'Me asegurar\xc3\xa9 de que no vayas a ninguna parte.',
        'Espera; te voy a aislar.',
        '\xc2\xa1Vamos a inaugurar un nuevo dibu!',
        'Quiero que sientas apego por m\xc3\xad.'],
    'ReOrg': [
        '\xc2\xa1No te va a gustar la forma en que he reorganizado todo!',
        'Creo que hace falta un poco de reorganizaci\xc3\xb3n.',
        'No est\xc3\xa1s tan mal, s\xc3\xb3lo hay que reorganizarte.',
        '\xc2\xbfTe gusta mi capacidad de reorganizaci\xc3\xb3n?',
        'He pensado que le ir\xc3\xada bien una nueva imagen a todo.',
        '\xc2\xa1Hay que reorganizarte!',
        'Pareces un poco desorganizado.',
        'Espera; voy a reorganizar tus pensamientos.',
        'Voy a esperar a que te reorganices un poco.',
        '\xc2\xbfTe importa si organizo un poco todo esto?'],
    'RestrainingOrder': [
        'Deber\xc3\xadas alejarte un poco.',
        '\xc2\xa1Me han encargado que te d\xc3\xa9 una orden de alejamiento!',
        'No te puedes acercar a menos de dos metros de m\xc3\xad.',
        'Creo que deber\xc3\xadas guardar las distancias.',
        'Deber\xc3\xada alejarte para siempre.',
        '\xc2\xa1Hay que alejar a este dibu!',
        'Intenta alejar tu mente de todo esto.',
        'Espero que todo esto no te aleje demasiado de la realidad.',
        '\xc2\xa1A ver si consigues acercarte ahora!',
        '\xc2\xa1Te ordeno que te alejes!',
        '\xc2\xbfPor qu\xc3\xa9 no empezamos por alejar posiciones?'],
    'Rolodex': [
        'Tengo tu direcci\xc3\xb3n en alg\xc3\xban sitio.',
        'Aqu\xc3\xad tengo el n\xc3\xbamero de la perrera. ',
        'Espera; te voy a dar mi tarjeta.',
        'Tengo tu n\xc3\xbamero aqu\xc3\xad mismo.',
        'Te tengo controlado de la A a la Z.',
        'Te tengo m\xc3\xa1s que fichado.',
        '\xc2\xa1Esquiva esto!',
        'Cuidado; no te cortes con los bordes.',
        'Voy a darte unas cuantas direcciones \xc3\xbatiles.',
        'Toma; ll\xc3\xa1mame a estos n\xc3\xbameros.',
        'Quiero asegurarme de que sigamos en contacto.'],
    'RubberStamp': [
        'Me gusta dejar siempre una buena impresi\xc3\xb3n.',
        'Es importante aplicar una presi\xc3\xb3n firme.',
        'Dejo siempre una buena huella.',
        'Te voy a dejar m\xc3\xa1s plano que un sello.',
        'Hay que DEVOLVERTE AL REMITENTE.',
        'Has sido CANCELADO.',
        'Voy a mandarte al dibuparque con sello URGENTE.',
        'Creo que te vas a sentir muy RECHAZADO.',
        'Para mandarte al dibuparque no har\xc3\xa1 falta FRANQUEO.',
        'Vas a ir al dibuparque POR AVI\xc3\x93N.'],
    'RubOut': [
        'Y ahora, la desaparici\xc3\xb3n final.',
        'Me parece que te he perdido.',
        'He decidido que te quedas fuera.',
        'Siempre elimino todos los obst\xc3\xa1culos.',
        'Vaya; voy a borrar este error.',
        'Me gusta que todo lo molesto desaparezca.',
        'Me gusta que todo est\xc3\xa9 limpio y ordenado.',
        'Por favor, intenta seguir animado.',
        'Ahora te veo... Ahora no te veo.',
        'Creo que vas a ponerte borroso.',
        'Voy a eliminar el problema.',
        'Me voy a ocupar de tus \xc3\xa1reas problem\xc3\xa1ticas.'],
    'Sacked': [
        'Cuidado; viene el hombre del saco.',
        '\xc2\xa1Te tengo en el saco!',
        '\xc2\xbfTe apetece echar una carrera de sacos?',
        '\xc2\xbfSacas t\xc3\xba o saco yo?',
        '\xc2\xa1Voy a ponerte a buen recaudo!',
        'Tengo el r\xc3\xa9cord de carreras de sacos.',
        'Te voy a sacar de aqu\xc3\xad...',
        '\xc2\xa1Se acab\xc3\xb3; te voy a meter en el saco!',
        '\xc2\xa1No nos metas a todos los bots en el mismo saco!',
        'Todos me dicen que tengo un buen saque.'],
    'Schmooze': [
        'Seguro que no te esperabas esto.',
        'Esto te va a quedar muy bien.',
        '\xc2\xa1Te lo has ganado!',
        'No quiero aburrirte con mi discurso.',
        'Adular a la gente me da buenos resultados.',
        'Voy a exagerar un poquito.',
        'Es hora de dorar la p\xc3\xadldora un poco.',
        'Ahora hablemos un poco de ti.',
        'Te mereces una palmadita en la espalda.',
        'Ha llegado el momento de alabar tu trayectoria.',
        'Siento tener que bajarte de tu pedestal, pero...'],
    'Shake': [
        'Est\xc3\xa1s justo en el epicentro.',
        'Est\xc3\xa1s pisando una falla.',
        'Esto va a estar movidito...',
        'Creo que va a ocurrir un desastre natural.',
        'Es un desastre de proporciones s\xc3\xadsmicas.',
        '\xc3\x89ste se va a salir de la escala Richter.',
        'Es hora de ponerse a cubierto.',
        'Pareces alterado.',
        '\xc2\xbfListo para bailar el mene\xc3\xadto?',
        'No te agites demasiado, por favor.',
        'Esto te va a poner patas arriba.',
        'Te recomiendo un buen plan de escape.'],
    'Shred': [
        'Tengo que deshacerme de bastante morralla.',
        'Voy a reciclar un poco de papel.',
        'Creo que me voy a deshacer de ti ahora mismo.',
        'Con esto me deshar\xc3\xa9 de las pruebas.',
        'Ya no hay manera de demostrar nada.',
        'A ver si consigues recomponer esto.',
        'Esto te va a hacer trizas.',
        'Voy a triturar esa idea.',
        'No quiero que esto caiga en malas manos.',
        'Adi\xc3\xb3s a las pruebas.',
        'Creo que \xc3\xa9sta era tu \xc3\xbaltima esperanza.'],
    'Spin': [
        '\xc2\xbfTe apetece ir a dar una vuelta?',
        '\xc2\xbfQu\xc3\xa9 tal si te centrifugo un poco?',
        '\xc2\xa1Tu cabeza va a dar vueltas con esto!',
        'Voy a dar otra vuelta de tuerca.',
        'Te voy a dar una vuelta.',
        'Yo siempre estoy de vuelta de todo.',
        'Cuidado.  La vida da muchas vueltas.',
        '\xc2\xa1Vamos a hacer un doble giro mortal!',
        'Un poco m\xc3\xa1s y de vuelta al dibuparque.'],
    'Synergy': [
        'Voy a presentar esto en el comit\xc3\xa9.',
        'Tu proyecto ha sido cancelado.',
        'Hemos cortado tus fondos.',
        'Estamos reestructurando tu divisi\xc3\xb3n.',
        'Lo he sometido a votaci\xc3\xb3n y has perdido.',
        'Acabo de recibir la aprobaci\xc3\xb3n final.',
        'Un buen equipo puede superar cualquier problema.',
        'Luego me ocupar\xc3\xa9 de esto contigo.',
        'Vamos a ir al grano.',
        'Considera esto una crisis sinerg\xc3\xa9tica.'],
    'Tabulate': [
        'Esto no me cuadra.',
        'No te salen las cuentas.',
        'Te va a salir una cuenta enorme.',
        'Voy a desglosarte en un momento.',
        '\xc2\xbfEst\xc3\xa1s listo para unas cifras de v\xc3\xa9rtigo?',
        'Es la hora de que pagues la dolorosa.',
        'Hora de saldar cuentas...',
        'Me encanta tener las cuentas claras.',
        'Las cuentas claras y el chocolate oscuro.',
        'Estos n\xc3\xbameros van a dejarte con la boca abierta.'],
    'TeeOff': [
        'Tienes un par nefasto.',
        '\xc2\xa1Bola!',
        'Vas a ver qu\xc3\xa9 bien le pego.',
        '\xc2\xa1Caddie, dame un hierro!',
        'A ver si mejoras este golpe.',
        '\xc2\xa1Mira qu\xc3\xa9 swing!',
        '\xc3\x89sta bola va a entrar de un solo golpe.',
        'Est\xc3\xa1s pisando mi green.',
        'F\xc3\xadjate qu\xc3\xa9 buen grip tengo.',
        '\xc2\xa1Mira qu\xc3\xa9 birdie!',
        '\xc2\xa1No pierdas de vista la bola!',
        '\xc2\xbfTe importa si juego un poco?'],
    'Tremor': [
        '\xc2\xbfHas notado eso?',
        'No te dan miedo los temblores, \xc2\xbfverdad?',
        'Los temblores suelen ser el principio.',
        'Pareces tembloroso. ',
        '\xc2\xa1Voy a agitar un poco las cosas!',
        '\xc2\xbfEst\xc3\xa1s listo para bailar la rumba?',
        '\xc2\xbfQu\xc3\xa9 te pasa? Pareces agitado.',
        '\xc2\xa1Tiembla de miedo!',
        '\xc2\xbfPor qu\xc3\xa9 tiemblas de miedo?'],
    'Watercooler': [
        'Esto te refrescar\xc3\xa1 un poco.',
        '\xc2\xbfNo es refrescante?',
        'Ven\xc3\xada a entregar un pedido.',
        '\xc2\xa1Pru\xc3\xa9bala; est\xc3\xa1 fresquita!',
        '\xc2\xbfQu\xc3\xa9 pasa? \xc2\xa1Es s\xc3\xb3lo agua!',
        'No te preocupes; es agua potable.',
        'Qu\xc3\xa9 bien; otro cliente satisfecho.',
        'Es la hora de entregar el pedido diario.',
        'Espero que no desti\xc3\xb1as.',
        '\xc2\xbfTe apetece un trago?',
        'Hay que dar de beber al sediento.',
        '\xc2\xbfNo ten\xc3\xadas sed? \xc2\xa1Pues toma!'],
    'Withdrawal': [
        'Creo que te has quedado sin fondos',
        'Espero que tengas suficientes fondos en tu cuenta.',
        '\xc2\xa1Toma ya, con intereses!',
        'Te est\xc3\xa1s quedando sin liquidez.',
        'Pronto vas a tener que hacer un ingreso.',
        'Est\xc3\xa1s al borde del colapso econ\xc3\xb3mico.',
        'Creo que est\xc3\xa1s en recesi\xc3\xb3n.',
        'Tus finanzas se van a ver afectadas.',
        'Preveo una crisis inminente.',
        '\xc2\xa1Vas a tener un agujero en tu cuenta!'],
    'WriteOff': [
        'Perm\xc3\xadteme que incremente tus deudas.',
        'Vamos a intentar sanear tu situaci\xc3\xb3n.',
        'Es hora de hacer el balance de tus cuentas.',
        'Esto no va a quedar nada bien en tu libro de contabilidad.',
        'Estoy buscando dividendos.',
        '\xc2\xbfPor qu\xc3\xa9 no haces balance de tus p\xc3\xa9rdidas?',
        'Olv\xc3\xaddate de la gratificaci\xc3\xb3n que te toca.',
        'Voy a poner patas arriba tus cuentas.',
        'Creo que tus p\xc3\xa9rdidas van a ser cuantiosas.',
        'Tu saldo se va a ver un poco afectado.'] }
BuildingWaitingForVictors = ('Esperando a otros jugadores...',)
ElevatorHopOff = 'Bajarse'
CogsIncModifier = '%s, Inc.'
CogsInc = 'BOTS, Inc.'
DoorKnockKnock = 'Toc, toc.'
DoorWhosThere = '\xc2\xbfQui\xc3\xa9n es?'
DoorWhoAppendix = ' qu\xc3\xa9?'
FADoorCodes_UNLOCKED = None
FADoorCodes_TALK_TO_TOM = '\xc2\xa1T\xc3\xb9 necesitas bromas! Anda a hablar con Tato Tutorial'
FADoorCodes_DEFEAT_FLUNKY_HQ = '\xc2\xa1Ven devuelta cuando hayas derrotado al Secuaz!'
FADoorCodes_TALK_TO_HQ = '\xc2\xa1Anda y obten tu recompense del funcionario Enrique!'
FADoorCodes_WRONG_DOOR_HQ = '\xc2\xa1Puerta incorrecta! \xc2\xa1Sal por la otra puerta al Dibuparque!'
FADoorCodes_GO_TO_PLAYGROUND = '\xc2\xa1Salida equivocada! \xc2\xa1T\xc3\xb9 necesitas salir al Dibuparque!'
FADoorCodes_DEFEAT_FLUNKY_TOM = '\xc2\xa1As\xc3\xa9rcate al Secuaz para combatir con \xc3\xa9l!'
FADoorCodes_TALK_TO_HQ_TOM = 'Ve y obt\xc3\xa9n tu recompense en el Cuartel General Dibu!'
FADoorCodes_SUIT_APPROACHING = None
FADoorCodes_BUILDING_TAKEOVER = '\xc2\xa1Cuidado! \xc2\xa1Adentro est\xc3\xa1 un Bot!'
KnockKnockJokes = [
    [
        'Aitor ',
        '\xc2\xa1Aitor Tilla de Patatas!'],
    [
        'Adela',
        '\xc2\xa1Carmelo Cotonenalm\xc3\xadbar!'],
    [
        'Abraham',
        '\xc2\xa1Abraham Lapuerta!'],
    [
        'Amira',
        '\xc2\xa1Amira Quienhavenido!'],
    [
        'Aquiles',
        '\xc2\xa1Aquiles Dejoporhoy!'],
    [
        'Archibaldo',
        '\xc2\xa1Archibaldo Enlascarpetas!'],
    [
        'Armando',
        '\xc2\xa1Armando Adistancia!'],
    [
        'Ariel',
        '\xc2\xa1Ariel Lavamasblanco!'],
    [
        'Augusto',
        '\xc2\xa1Augusto de Conocerle!'],
    [
        'Azucena',
        '\xc2\xa1Azucena Estaservida!'],
    [
        'Baldomero',
        '\xc2\xa1Baldomero Alaplancha!'],
    [
        'Baltasar',
        '\xc2\xa1Baltasar Ysecay\xc3\xb3!'],
    [
        'Belinda',
        '\xc2\xa1Belinda Flordeljard\xc3\xadn!'],
    [
        'Beltr\xc3\xa1n',
        '\xc2\xa1Beltr\xc3\xa1n Chetes de Quesito!'],
    [
        'Bernab\xc3\xa9',
        '\xc2\xa1Bernab\xc3\xa9 Abrirlapuerta!'],
    [
        'Blasa',
        '\xc2\xbfBlasa Briron\xc3\xb3?'],
    [
        'Carmen',
        '\xc2\xa1Carmen Tolada y Fresca!'],
    [
        'Calixto',
        '\xc2\xa1Calixto Queesuno!'],
    [
        'Camila',
        '\xc2\xa1Camila Groquehayavenido!'],
    [
        'Cintia',
        '\xc2\xa1Cintia Palpelo!'],
    [
        'Clemente',
        '\xc2\xa1Clemente Claraydespejada!'],
    [
        'Cleopatra',
        '\xc2\xa1Cleopatra Ficoenhorapunta!'],
    [
        'Clotilde',
        '\xc2\xa1Clotilde Alfinal!'],
    [
        'Consuelo',
        '\xc2\xa1Consuelo Recienfregado!'],
    [
        'Cris\xc3\xb3stomo',
        '\xc2\xa1Cris\xc3\xb3stomo Uncafeconleche!'],
    [
        'Demetrio',
        '\xc2\xa1Demetrio Doloquetenga!'],
    [
        'Bernab\xc3\xa9',
        '\xc2\xa1Bernab\xc3\xa9 Averquien\xc3\xa9s!'],
    [
        'Edmundo',
        '\xc2\xa1Edmundo Esunpa\xc3\xb1uelo!'],
    [
        'Engracia',
        '\xc2\xa1Engracia Porabrirlapuerta!'],
    [
        'Estela',
        '\xc2\xa1Estela Marinera!'],
    [
        'Eugenio',
        '\xc2\xa1Eugenio de la L\xc3\xa1mpara!'],
    [
        'Ezequiel',
        '\xc2\xbfEzequiel Es?'],
    [
        'Fabiola',
        '\xc2\xa1Fabiola Iadi\xc3\xb3s!'],
    [
        'Filomeno',
        'Filomeno Malquehellegado.'],
    [
        'Florinda',
        '\xc2\xa1Florinda Se y Bajelasmanos!'],
    [
        'Gaspar',
        '\xc2\xa1Gaspar Ecequevallover!'],
    [
        'Genoveva',
        '\xc2\xa1Genoveva Desabotella!'],
    [
        'Jairo',
        '\xc2\xa1Jairo Niasdelavida!'],
    [
        'Jazm\xc3\xadn',
        '\xc2\xa1Jazm\xc3\xadn Nero del Carb\xc3\xb3n!'],
    [
        'Jerem\xc3\xadas',
        '\xc2\xa1Jerem\xc3\xadas Sonpasiempre!'],
    [
        'Jessica',
        '\xc2\xa1Jessica N\xc3\xa1lisis Gratuito!'],
    [
        'Jes\xc3\xbas',
        '\xc2\xa1Jes\xc3\xbas Piros de Espa\xc3\xb1a!'],
    [
        'Joaqu\xc3\xadn',
        '\xc2\xbfJoaqu\xc3\xadn Havenidoestavez?'],
    [
        'Kevin',
        '\xc2\xbfKevin Olesirvo?'],
    [
        'Leonor',
        '\xc2\xa1Leonor Abuena Porelpremio!'],
    [
        'Mabel',
        '\xc2\xa1Mabel Siabresdunavez!'],
    [
        'Macarena',
        '\xc2\xa1Macarena Blanca de la Playa!'],
    [
        'Magdalena',
        '\xc2\xa1Magdalena Ycaf\xc3\xa9 Conleche!'],
    [
        'Maite',
        '\xc2\xa1Maite Digoquesoyy\xc3\xb3!'],
    [
        'Marcos',
        '\xc2\xa1Marcos Sacos del Don!'],
    [
        'Armando',
        '\xc2\xa1Armando de la Tropa!'],
    [
        'Olimpia',
        '\xc2\xa1Olimpia Fijaydaesplendor!'],
    [
        'Olivia',
        '\xc2\xa1Olivia Ductoromano!'],
    [
        'Omar',
        '\xc2\xa1Omar Ejadilla del Cant\xc3\xa1brico!'],
    [
        '\xc3\x93scar',
        '\xc2\xa1\xc3\x93scar Naval de Tenerife!'],
    [
        'P\xc3\xa1nfilo',
        '\xc2\xa1P\xc3\xa1nfilo de la Navaja!'],
    [
        'Pascual',
        '\xc2\xbfPascual Esudireci\xc3\xb3n?'],
    [
        'Pura',
        '\xc2\xa1Pura Suertehaberloencontrado!'],
    [
        'Ramiro',
        '\xc2\xa1Raimiro Ynoteveo!'],
    [
        'Ramona',
        '\xc2\xa1Ramona Vestida de Seda!'],
    [
        'Ra\xc3\xbal',
        '\xc2\xa1Ra\xc3\xbal Timo de la Fila!'],
    [
        'Renato',
        '\xc2\xa1Renato Sigadoportodos!'],
    [
        'Juan Ricardo',
        '\xc2\xa1Juan Ricardo Borriquero!'],
    [
        'Rub\xc3\xa9n',
        '\xc2\xa1Rub\xc3\xa9n Averloquemehecomprado!'],
    [
        'Sabina',
        '\xc2\xa1Sabina Questariasaqu\xc3\xad!'],
    [
        'Samanta',
        '\xc2\xa1Samanta de Lanaquehacefr\xc3\xado!'],
    [
        'Sandra',
        '\xc2\xa1Sandra Josa!'],
    [
        'Seraf\xc3\xadn',
        '\xc2\xa1Seraf\xc3\xadn de la Historia!'],
    [
        'Serena',
        '\xc2\xa1Serena y Tranquila!'],
    [
        'Servando',
        '\xc2\xa1Servando Lero de Sierra Morena!'],
    [
        'Silvestre',
        '\xc2\xa1Silvestre Senunburro!'],
    [
        'Silvio',
        '\xc2\xbfSilvio Ustedamiperro?'],
    [
        'Sixta',
        '\xc2\xa1Sixta Vezquevengoaqu\xc3\xad!'],
    [
        'Socorro',
        '\xc2\xa1Socorro Aux\xc3\xadlio!'],
    [
        'Sol',
        '\xc2\xa1Sol Oquieropasar!'],
    [
        'Soledad',
        '\xc2\xa1Soledad de Tenertentusbrazos!'],
    [
        'Tadeo',
        '\xc2\xa1Tadeo Graciasadi\xc3\xb3s!'],
    [
        'Tamara',
        '\xc2\xa1Tamara Casdemach\xc3\xadn!'],
    [
        'Teobaldo',
        '\xc2\xa1Teobaldo Sas de Cer\xc3\xa1mica!'],
    [
        'Ulrico',
        '\xc2\xa1Ulrico Helado, oiga!'],
    [
        'Virgilio',
        '\xc2\xa1Virgil\xc3\xado Mehasmetido!'],
    [
        'Vladimir',
        '\xc2\xa1Vladimir Aquienhavenido!'],
    [
        'Wenceslao',
        '\xc2\xa1Wenceslao de Vainilla!'],
    [
        'Wenceslao',
        '\xc2\xa1Wenceslao de Chocolate!'],
    [
        'Amira',
        '\xc2\xa1Amira Quiensoy!'],
    [
        'Sa\xc3\xbal',
        '\xc2\xa1Sa\xc3\xbal Timaoportunidadqueledoy!'],
    [
        'No\xc3\xa9',
        '\xc2\xa1No\xc3\xa9 Nadieconocido!'],
    [
        'No\xc3\xa9',
        '\xc2\xbfNo\xc3\xa9 Verdadquemesperabas?'],
    [
        'Nadia',
        '\xc2\xa1Nadia Importante, la verdad!'],
    [
        'Otto',
        '\xc2\xa1Otto Quenomeconoce!'],
    [
        'Abel',
        '\xc2\xa1Abel Quien\xc3\xa9s!'],
    [
        'Alcira',
        '\xc2\xa1Alcira Esapuertaquehacefr\xc3\xado!'],
    [
        'Apolo',
        '\xc2\xa1Apolo de Naranja y Lim\xc3\xb3n!'],
    [
        'Carmelo',
        '\xc2\xbfCarmelo Dicesomelocuentas?'],
    [
        'Padm\xc3\xa9',
        '\xc2\xbfPadm\xc3\xa9 Dicequehoraes?'],
    [
        'Eleazar',
        '\xc2\xa1Eleazar Aleat\xc3\xb3riez!'],
    [
        'Elijah',
        '\xc2\xa1Elijah Elquemasleguste!'],
    [
        'Elmer',
        '\xc2\xa1Elmer Cader de Venecia!'],
    [
        'Elpida',
        '\xc2\xa1Elpida Loqueleapetezca!'],
    [
        'Quique',
        '\xc2\xa1Quique Cosasdice, oiga!'],
    [
        'Euridice',
        '\xc2\xa1Euridice Quelellames!'],
    [
        'Calvino',
        '\xc2\xa1Calvino Tinto de Verano!'],
    [
        'Mercedes',
        '\xc2\xa1Mercedes Elpaso!'],
    [
        'Mercurio',
        '\xc2\xa1Mercurio Soquelopregunte!'],
    [
        'Merlin',
        '\xc2\xa1Merlin Dacasatieneusted!'],
    [
        'Minerva',
        '\xc2\xa1Minerva Minfada y Mixaspera!'],
    [
        'Miranda',
        '\xc2\xa1Miranda Yvetedeunavez!'],
    [
        'Morgana',
        '\xc2\xa1Morgana Tengodefastidiar!'],
    [
        'Morfeo',
        '\xc2\xa1Morfeo Quepegarleaunpadre!'],
    [
        'Pancho',
        '\xc2\xa1Pancho Colate Blanco!'],
    [
        'Parker',
        '\xc2\xa1Parker Levoyacontar!'],
    [
        'Pasha',
        '\xc2\xbfPasha Contigot\xc3\xado?'],
    [
        'Patty',
        'Patty Todo Noquieronada.'],
    [
        'Stan',
        '\xc2\xa1Stan Todosdetenidos!'],
    [
        'Pierre',
        '\xc2\xa1Pierre Queerre!'],
    [
        'Ida',
        '\xc2\xa1Ida Yvuelta!'],
    [
        'Savannah',
        '\xc2\xa1Savannah de Lino Blanco!'],
    [
        'Renata',
        '\xc2\xa1Renata Conchocolate!']]
ChatInputNormalSayIt = 'Dec\xc3\xadrselo'
ChatInputNormalCancel = 'Cancelar'
ChatInputNormalWhisper = 'Susurrar'
ChatInputWhisperLabel = 'A %s'
SCEmoteNoAccessMsg = ' Todav\xc3\xada no tienes acceso\n a este emoticono.'
SCEmoteNoAccessOK = 'Aceptar'
ChatManagerChat = 'Charla'
ChatManagerWhisperTo = 'Susurrar a:'
ChatManagerWhisperToName = 'Susurrar a:\n%s'
ChatManagerCancel = 'Cancelar'
ChatManagerWhisperOffline = '%s est\xc3\xa1 desconectado.'
OpenChatWarning = '\xc2\xa1Todav\xc3\xada no tienes "amigos secretos"!  No puedes conversar con otros dibus a menos que sean tus amigos secretos.\n\nPara convertirte en amigo secreto de alguien, haz clic en \xc3\xa9l y selecciona "Secretos" en el panel de detalles.  No hace falta decir que siempre puedes hablar con quien quieras por medio de la Charla r\xc3\xa1pida.'
OpenChatWarningOK = 'Aceptar'
UnpaidChatWarning = 'Cuando te hayas suscrito, podr\xc3\xa1s usar este bot\xc3\xb3n para charlar con tus amigos mediante el teclado.  Hasta entonces, deber\xc3\xadas usar la herramienta Charla r\xc3\xa1pida para conversar con los dem\xc3\xa1s dibus.'
UnpaidChatWarningPay = '\xc2\xa1Suscr\xc3\xadbete ya!'
UnpaidChatWarningContinue = 'Continuar prueba gratuita'
NoSecretChatAtAllTitle = 'Charla de Amigos secretos'
NoSecretChatAtAll = 'Para charlar con un amigo, la herramienta Amigos secretos debe estar activada.  La herramienta Amigos secretos permite a un miembro charlar con otro gracias al uso de un c\xc3\xb3digo secreto que se debe comunicar fuera del juego.\n\nPara activar esta herramienta sal de Toontown y act\xc3\xadvala a trav\xc3\xa9s de Los Controles Parentales en Conecta Disney'
NoSecretChatAtAllOK = 'Aceptar'
NoSecretChatWarningTitle = 'Controles parentales'
NoSecretChatWarning = 'Para que sea posible charlar con un amigo, la herramienta Amigos secretos debe estar activada.  Para saber m\xc3\xa1s cosas sobre la herramienta Amigos secretos y acceder a los controles parentales, diles a tus padres que abran la sesi\xc3\xb3n con su contrase\xc3\xb1a parental.'
NoSecretChatWarningOK = 'Aceptar'
NoSecretChatWarningCancel = 'Cancelar'
NoSecretChatWarningWrongPassword = 'Esa contrase\xc3\xb1a no es correcta.  Introduce la contrase\xc3\xb1a parental que se cre\xc3\xb3 al adquirir esta cuenta.  No se trata de la misma contrase\xc3\xb1a que se emplea para jugar al juego.'
ActivateChat = 'La herramienta Amigos secretos permite a los socios charlar entre s\xc3\xad gracias al uso de un c\xc3\xb3digo secreto que se debe comunicar fuera del juego.  Para obtener toda la informaci\xc3\xb3n, haz clic aqu\xc3\xad:\n\n\nLa herramienta Amigos secretos no est\xc3\xa1 moderada ni supervisada.  Si los padres permiten a sus hijos usar su cuenta con la opci\xc3\xb3n Amigos secretos activada, les aconsejamos que los supervisen mientras juegan.  Una vez activada, la herramienta Amigos secretos est\xc3\xa1 disponible hasta que se desactiva.\n\nAl activar la herramienta Amigos secretos, los padres reconocen que existen ciertos riesgos inherentes a la posibilidad de charla de la herramienta y reconocen que han sido informados sobre dichos riesgos y est\xc3\xa1n de acuerdo en aceptarlos.'
ActivateChatYes = 'Activar'
ActivateChatNo = 'Cancelar'
ActivateChatMoreInfo = 'M\xc3\xa1s informaci\xc3\xb3n'
ActivateChatPrivacyPolicy = 'Normas de confidencialidad'
LeaveToPay = 'Para adquirir Toontown, el producto ir\xc3\xa1 a Toontown.com.'
LeaveToPayYes = 'Adquirir'
LeaveToPayNo = 'Cancelar'
ChatMoreInfoOK = 'Aceptar'
SecretChatActivated = '\xc2\xa1La herramienta "Amigos secretos" ha sido activada!\n\nSi m\xc3\xa1s tarde cambias de opini\xc3\xb3n y decides desactivar esta herramienta, haz clic en "Opciones de cuenta" en la p\xc3\xa1gina web de Toontown.'
SecretChatActivatedOK = 'Aceptar'
ProblemActivatingChat = '\xc2\xa1Vaya!  No hemos podido activar la herramienta de charla "Amigos secretos".\n\n%s\n\nVuelve a intentarlo m\xc3\xa1s tarde.'
ProblemActivatingChatOK = 'Aceptar'
SharedChatterGreetings = [
    '\xc2\xa1Hola, %!',
    'Eh, %, me alegro de verte.',
    '\xc2\xa1Me alegro de que hayas venido hoy!',
    '\xc2\xbfC\xc3\xb3mo est\xc3\xa1s, %?']
SharedChatterComments = [
    'Es un nombre estupendo, %.',
    'Me gusta tu nombre.',
    'Cuidado con los bots.',
    '\xc2\xa1Parece que llega el tranv\xc3\xada!',
    '\xc2\xa1Tengo que subir al tranv\xc3\xada para jugar y conseguir tartas!',
    'A veces me subo al tranv\xc3\xada s\xc3\xb3lo para conseguir la tarta de frutas.',
    'Guau, acabo de deshacerme de un mont\xc3\xb3n de bots. \xc2\xa1Necesito descansar un poco!',
    '\xc2\xa1Vaya, hay algunos bots que son muy grandotes!',
    'Parece que te lo pasas pipa.',
    'Caramba, qu\xc3\xa9 buen d\xc3\xada estoy teniendo.',
    'Me gusta lo que llevas puesto.',
    'Creo que esta tarde me voy a ir de pesca.',
    'Divi\xc3\xa9rtete en mi barrio.',
    '\xc2\xa1Espero que te lo est\xc3\xa9s pasando en grande en Toontown!',
    'Me han dicho que en Frescolandia est\xc3\xa1 nevando.',
    '\xc2\xbfHas subido hoy al tranv\xc3\xada?',
    'Me gustar\xc3\xada conocer a m\xc3\xa1s gente.',
    'Caramba, en Frescolandia hay un mont\xc3\xb3n de bots.',
    'Me encanta jugar al "T\xc3\xba la llevas". \xc2\xbfY a ti?',
    'Los juegos del tranv\xc3\xada son divertid\xc3\xadsimos.',
    'Me encanta hacer que la gente se r\xc3\xada.',
    'Ayudar a los amigos es muy divertido.',
    'Ejem, \xc2\xbfte has perdido?  No olvides que tienes un mapa en el dibucuaderno.',
    '\xc2\xa1Que no te l\xc3\xaden los bots con su cinta roja!',
    'Me han dicho que Daisy ha plantado flores nuevas en su jard\xc3\xadn.',
    '\xc2\xa1Para mirar hacia arriba, mant\xc3\xa9n pulsada la tecla Re P\xc3\xa1g!',
    '\xc2\xa1Si ayudas a reconquistar los edificios bot, podr\xc3\xa1s ganar una estrella de bronce!',
    'Si pulsas la tecla Tab, podr\xc3\xa1s contemplar diferentes vistas de los alrededores.',
    '\xc2\xa1Si pulsas la tecla Ctrl, podr\xc3\xa1s saltar!']
SharedChatterGoodbyes = [
    'Me tengo que ir; adi\xc3\xb3s.',
    'Creo que voy a subir al tranv\xc3\xada para jugar.',
    'Bueno, hasta otra. Te veo luego, %.',
    'M\xc3\xa1s me vale darme prisa para acabar con los bots.',
    'Es la hora de ponerse en marcha.',
    'Lo siento, pero tengo que irme.',
    'Adi\xc3\xb3s.',
    '\xc2\xa1Hasta luego, %!',
    'Creo que voy a practicar el lanzamiento de magdalenas.',
    'Voy a unirme a un grupo para acabar con unos cuantos bots.',
    'Me alegro de haberte visto hoy, %.',
    'Hoy tengo mucho que hacer. Voy a ponerme en marcha.']
MickeyChatter = ([
    'Bienvenido al Centro de Toontown.',
    'Hola, me llamo Mickey. \xc2\xbfC\xc3\xb3mo te llamas?'], [
    'Eh, \xc2\xbfhas visto a Donald?',
    'Voy a ver c\xc3\xb3mo sube la marea en Puerto Donald.',
    'Si ves a mi amiguete Goofy, dale recuerdos de mi parte.',
    'Me han dicho que Daisy ha plantado flores nuevas en su jard\xc3\xadn.'], [
    '\xc2\xa1Me voy a Melodilandia a ver a Minnie!',
    '\xc2\xa1Dios m\xc3\xado, llego tarde a mi cita con Minnie!',
    'Parece que es la hora de la cena de Pluto.',
    'Creo que voy a Puerto Donald a nadar un poco.',
    'Es la hora de la siesta. Me voy a Sue\xc3\xb1olandia.'])
MinnieChatter = ([
    'Bienvenido a Melodilandia.',
    'Hola, me llamo Minnie. \xc2\xbfC\xc3\xb3mo te llamas?'], [
    '\xc2\xa1La m\xc3\xbasica se siente por todas partes!',
    'No te olvides de montarte en el gran tiovivo.',
    'Llevas un disfraz muy chulo, %.',
    'Eh, \xc2\xbfhas visto a Mickey?',
    'Si ves a mi amigo Goofy, dale recuerdos de mi parte.',
    'Caramba, en Sue\xc3\xb1olandia de Donald hay un mont\xc3\xb3n de bots.',
    'Me han dicho que en Puerto Donald hay niebla.',
    'No te olvides de probar el laberinto de los Jardines de Daisy.',
    'Creo que voy a escuchar m\xc3\xbasica.',
    'Eh, %, mira eso.',
    'Me encanta la m\xc3\xbasica.',
    '\xc2\xbfA que no sab\xc3\xadas que a Melodilandia tambi\xc3\xa9n la llaman Cancioncity?  \xc2\xa1Ji, ji!',
    'Me encanta jugar al juego de imitar movimientos. \xc2\xbfY a ti?',
    'Me encanta hacer re\xc3\xadr a la gente.',
    '\xc2\xa1Uf, andar todo el d\xc3\xada con tacones acaba haciendo da\xc3\xb1o a los pies!',
    'Qu\xc3\xa9 camisa m\xc3\xa1s bonita, %.',
    '\xc2\xbfNo te encanta el juego de imitar movimientos?',
    '\xc2\xbfEso del suelo es una gominola?'], [
    '\xc2\xa1Vaya, llego tarde a mi cita con Mickey!',
    'Parece que es la hora de la cena de Pluto.',
    'Es la hora de la siesta. Me voy a Sue\xc3\xb1olandia.'])
GoofyChatter = ([
    'Bienvenido a los Jardines de Daisy.',
    'Hola, me llamo Goofy. \xc2\xbfY t\xc3\xba?',
    '\xc2\xa1Hola, me alegro de verte, %!'], [
    '\xc2\xa1Vaya! \xc2\xa1Cualquiera se pierde en el laberinto del jard\xc3\xadn!',
    'No te olvides de ir al laberinto.',
    'No he visto a Daisy en todo el d\xc3\xada.',
    '\xc2\xbfD\xc3\xb3nde estar\xc3\xa1 Daisy?',
    'Eh, \xc2\xbfhas visto a Donald?',
    'Si ves a mi amigo Mickey, dale recuerdos de mi parte.',
    '\xc2\xa1Oh! \xc2\xa1Me he olvidado de prepararle el desayuno a Mickey!',
    'Guau, seguro que en Puerto Donald hay un mont\xc3\xb3n de bots.',
    'Parece ser que Daisy ha plantado flores nuevas en su jard\xc3\xadn.',
    '\xc2\xa1Las gafas hipn\xc3\xb3ticas est\xc3\xa1n rebajadas a una gominola en mi tienda de bromas de Frescolandia!',
    '\xc2\xa1Las tiendas de bromas de Goofy tienen las mejores bromas, trucos y gansadas de todo Toontown!',
    'En las tiendas de bromas de Goofy garantizamos que todas las tartas en la cara te har\xc3\xa1n re\xc3\xadr. \xc2\xa1Si no es as\xc3\xad, te devolvemos tus gominolas!'], [
    '\xc2\xa1Me voy a Melodilandia a ver a Minnie!',
    '\xc2\xa1Vaya, llego tarde a mi cita con Donald!',
    'Creo que voy a Puerto Donald a nadar un poco.',
    'Es la hora de la siesta. Me voy a Sue\xc3\xb1olandia.'])
DonaldChatter = ([
    'Bienvenido a Sue\xc3\xb1olandia.',
    'Hola, me llamo Donald. \xc2\xbfY t\xc3\xba?'], [
    'A veces, este sitio me da escalofr\xc3\xados.',
    'No te olvides de probar el laberinto de los Jardines de Daisy.',
    'Caramba, qu\xc3\xa9 buen d\xc3\xada estoy teniendo.',
    'Eh, \xc2\xbfhas visto a Mickey?',
    'Si ves a mi buen amigo Goofy, dale recuerdos de mi parte.',
    'Creo que esta tarde me voy a ir de pesca.',
    'Caramba, en Puerto Donald hay un mont\xc3\xb3n de bots.',
    'Eh, \xc2\xbfno te he llevado en barco en Puerto Donald?',
    'No he visto a Daisy en todo el d\xc3\xada.',
    'Me han dicho que Daisy ha plantado flores nuevas en su jard\xc3\xadn.',
    'Cuac.'], [
    '\xc2\xa1Me voy a Melodilandia a ver a Minnie!',
    '\xc2\xa1Vaya! \xc2\xa1Llego tarde a mi cita con Daisy!',
    'Creo que voy a mi puerto a nadar un poco.',
    'Creo que voy a darme una vuelta en mi barco en Puerto Donald.'])
for chatter in [
    MickeyChatter,
    DonaldChatter,
    MinnieChatter,
    GoofyChatter]:
    chatter[0].extend(SharedChatterGreetings)
    chatter[1].extend(SharedChatterComments)
    chatter[2].extend(SharedChatterGoodbyes)

TCRConnecting = 'Conectando...'
TCRNoConnectTryAgain = 'Imposible conectar con %s:%s. \xc2\xbfQuieres intentarlo de nuevo?'
TCRNoConnectProxyNoPort = 'Imposible conectar con %s:%s.\n\nTe est\xc3\xa1s conectando al Internet a trav\xc3\xa9s de un proxy que no permite las conexiones al puerto %s.\n\nPara jugar a Toontown es necesario abrir este puerto o desactivar el proxy.  Si el proxy ha sido suministrado por tu proveedor de Internet, debes ponerte en contacto con \xc3\xa9l para que abra este puerto.'
TCRNoDistrictsTryAgain = 'No hay distritos de Toontown disponibles. \xc2\xbfDeseas intentarlo de nuevo?'
TCRLostConnection = 'Tu conexi\xc3\xb3n de Internet a Toontown se ha interrumpido inesperadamente.'
TCRBootedReasons = {
    1: 'Se ha producido un problema inesperado.  Se ha perdido la conexi\xc3\xb3n, pero deber\xc3\xadas poder conectarte de nuevo y volver al juego.',
    100: 'Has sido desconectado porque otra persona que ha abierto una sesi\xc3\xb3n con tu cuenta en otro ordenador.',
    120: 'Has sido desconectado debido a un problema con tu autorizaci\xc3\xb3n para usar la charla mediante el teclado.',
    122: 'Se ha producido un problema inesperado en la conexi\xc3\xb3n con Toontown.  Ponte en contacto con el Servicio de atenci\xc3\xb3n al cliente de Toontown.',
    151: 'Tu sesi\xc3\xb3n ha sido cerrada por un administrador de los servidores de Toontown.',
    153: 'Se ha reiniciado el distrito de Toontown en el que te hallabas.  Todos los que estaban en ese distrito han sido desconectados.  Sin embargo, deber\xc3\xadas poder conectarte de nuevo para volver al juego.',
    288: 'Lo sentimos, pero has gastado todos los minutos de que dispon\xc3\xadas en Toontown este mes.',
    349: 'Lo sentimos, pero has gastado todos los minutos de que dispon\xc3\xadas en Toontown este mes.' }
TCRBootedReasonUnknownCode = 'Ha surgido un problema inesperado (c\xc3\xb3digo de error %s).  Se ha perdido la conexi\xc3\xb3n, pero deber\xc3\xadas poder conectarte de nuevo y volver al juego.'
TCRTryConnectAgain = '\n\n\xc2\xbfQuieres intentar conectarte de nuevo?'
TCRTutorialAckQuestion = '%s es nuevo en Toontown.\n\n\xc2\xbfQuieres que Mickey te lo ense\xc3\xb1e?'
TCRTutorialAckOk = 'S\xc3\xad'
TCRTutorialAckCancel = 'No'
TCRToontownUnavailable = 'Toontown no parece estar disponible por el momento; seguimos intent\xc3\xa1ndolo...'
TCRToontownUnavailableCancel = 'Cancelar'
TCRNameCongratulations = '\xc2\xa1\xc2\xa1ENHORABUENA!!'
TCRNameAccepted = 'Tu nombre ha sido\naprobado por el Consejo Dibu.\n\nA partir de ahora,\nte llamar\xc3\xa1s\n"%s"'
TCRServerConstantsProxyNoPort = 'Imposible ponerse en contacto con %s.\n\nTe est\xc3\xa1s conectando al Internet a trav\xc3\xa9s de un proxy que no permite conexiones al puerto %s.\n\nPara jugar a Toontown es necesario abrir este puerto o desactivar el proxy.  Si el proxy ha sido suministrado por tu proveedor de Internet, debes ponerte en contacto con \xc3\xa9l para que abra este puerto.'
TCRServerConstantsProxyNoCONNECT = 'Imposible ponerse en contacto con %s.\n\nTe est\xc3\xa1s conectando al Internet a trav\xc3\xa9s de un proxy que no es compatible con el m\xc3\xa9todo CONNECT.\n\nPara jugar a Toontown es necesario activar esta opci\xc3\xb3n o desactivar el proxy.  Si el proxy ha sido suministrado por tu proveedor de Internet, debes ponerte en contacto con \xc3\xa9l para activar esta opci\xc3\xb3n.'
TCRServerConstantsTryAgain = 'Imposible ponerse en contacto con %s.\n\nEl servidor de la cuenta de Toontown podr\xc3\xada estar inoperativo en este momento, o puede ser que haya surgido un problema con tu conexi\xc3\xb3n de Internet.\n\n\xc2\xbfDeseas intentarlo de nuevo?'
TCRServerDateTryAgain = 'Imposible obtener la fecha del servidor de %s. \xc2\xbfDeseas intentarlo de nuevo?'
AfkForceAcknowledgeMessage = 'A tu dibu le ha entrado sue\xc3\xb1o y se ha ido a la cama.'
PeriodTimerWarning = '\xc2\xa1Tu l\xc3\xadmite de tiempo en Toontown este mes casi ha terminado!'
PeriodForceAcknowledgeMessage = 'Has gastado todos los minutos de que dispon\xc3\xadas en Toontown este mes.  \xc2\xa1Ven otra vez a jugar el mes que viene!'
TCREnteringToontown = 'Entrando a Toontown...'
FriendInviteeTooManyFriends = '%s desea ser tu amigo, pero ya tienes demasiados amigos en tu lista.'
FriendInviteeInvitation = 'A %s le gustar\xc3\xada ser tu amigo.'
FriendInviteeOK = 'Aceptar'
FriendInviteeNo = 'No'
FriendInviterOK = 'Aceptar'
FriendInviterCancel = 'Cancelar'
FriendInviterStopBeingFriends = 'Dejar de ser amigo'
FriendInviterYes = 'S\xc3\xad'
FriendInviterNo = 'No'
FriendInviterClickToon = 'Haz clic en el dibu del que deseas ser amigo.'
FriendInviterTooMany = 'No puedes a\xc3\xb1adir m\xc3\xa1s amigos a tu lista porque ya tienes demasiados. Si quieres ser amigo de %s, tendr\xc3\xa1s que quitar algunos amigos de tu lista.'
FriendInviterNotYet = '\xc2\xbfQuieres ser amigo de %s?'
FriendInviterCheckAvailability = 'Comprobando si %s est\xc3\xa1 disponible.'
FriendInviterNotAvailable = '%s est\xc3\xa1 ocupado ahora mismo. Int\xc3\xa9ntalo m\xc3\xa1s tarde.'
FriendInviterWentAway = '%s se ha marchado.'
FriendInviterAlready = '%s ya es tu amigo.'
FriendInviterAskingCog = 'Preguntando a %s si quiere ser tu amigo.'
FriendInviterEndFriendship = '\xc2\xbfSeguro que quieres dejar de ser amigo de %s?'
FriendInviterFriendsNoMore = '%s ya no es tu amigo.'
FriendInviterSelf = '\xc2\xa1 Ya eres tu propio amigo!'
FriendInviterIgnored = '%s no te est\xc3\xa1 haciendo caso.'
FriendInviterAsking = 'Preguntando a %s si quiere ser tu amigo.'
FriendInviterFriendSaidYes = '\xc2\xa1%s ha dicho que s\xc3\xad!'
FriendInviterFriendSaidNo = '%s ha dicho que no, gracias.'
FriendInviterFriendSaidNoNewFriends = '%s no quiere tener amigos nuevos ahora mismo.'
FriendInviterTooMany = '\xc2\xa1%s ya tiene demasiados amigos!'
FriendInviterMaybe = '%s no ha podido responder.'
FriendInviterDown = 'Imposible hacer amigos ahora.'
FriendSecretIntro = "Si est\xc3\xa1s jugando a Disney's Toontown Online con alguien que conozcas en la vida real, los dos pueden convertirse en amigos secretos.  Puedes charlar con tus amigos secretos usando el teclado.  Los dem\xc3\xa1s dibus no entender\xc3\xa1n lo que est\xc3\xa1s diciendo.\n\nPara hacer esto, necesitas obtener un Secreto.  Transm\xc3\xadtele el Secreto a tu amigo y a nadie m\xc3\xa1s.  Cuando tu amigo escriba el Secreto en su pantalla, los dos seran amigos secretos en Toontown."
FriendSecretGetSecret = 'Obtener Secreto'
FriendSecretEnterSecret = 'Si tienes un Secreto de alguien que conozcas, escr\xc3\xadbelo aqu\xc3\xad.'
FriendSecretOK = 'Aceptar'
FriendSecretCancel = 'Cancelar'
FriendSecretGettingSecret = 'Obteniendo Secreto. . .'
FriendSecretGotSecret = 'Aqu\xc3\xad tienes tu nuevo Secreto.  \xc2\xa1No te olvides de anotarlo!\n\nPuedes dar este Secreto solamente a una persona.  Cuando alguien escriba tu Secreto, \xc3\xa9ste no valdr\xc3\xa1 ya para nadie m\xc3\xa1s.  Si deseas dar un Secreto a alguien m\xc3\xa1s, tienes que pedir otro.\n\nEl Secreto s\xc3\xb3lo valdr\xc3\xa1 durante los dos d\xc3\xadas siguientes.  Tu amigo tendr\xc3\xa1 que escribirlo antes de que desaparezca, o de lo contrario el proceso no funcionar\xc3\xa1.\n\nTu Secreto es:'
FriendSecretTooMany = 'Lo siento, no puedes tener m\xc3\xa1s Secretos hoy.  \xc2\xa1Ya has tenido m\xc3\xa1s que suficientes!\n\nPrueba de nuevo ma\xc3\xb1ana.'
FriendSecretTryingSecret = 'Probando Secreto. . .'
FriendSecretEnteredSecretSuccess = '\xc2\xa1Ya eres amigo secreto de %s!'
FriendSecretEnteredSecretUnknown = '\xc3\x89se no es el Secreto de nadie.  \xc2\xbfSeguro que lo has escrito bien?\n\nSi lo has escrito correctamente, tal vez haya caducado.  P\xc3\xaddele a tu amigo que te obtenga un Secreto nuevo (o consigue t\xc3\xba uno y d\xc3\xa1selo a tu amigo).'
FriendSecretEnteredSecretFull = 'No puedes ser amigo de %s porque uno de los dos tiene demasiados amigos en la lista.'
FriendSecretEnteredSecretFullNoName = 'No pueden ser amigos porque uno de los dos tiene demasiados amigos en la lista.'
FriendSecretEnteredSecretSelf = '\xc2\xa1Acabas de escribir tu propio Secreto!  Ahora, nadie m\xc3\xa1s puede usar ese Secreto.'
FriendSecretNowFriends = '\xc2\xa1Ya eres amigo secreto de %s!'
FriendSecretNowFriendsNoName = '\xc2\xa1Ya sois amigos secretos!'
FriendsListPanelNewFriend = 'Amigo nuevo'
FriendsListPanelSecrets = 'Secretos'
FriendsListPanelOnlineFriends = 'AMIGOS\nCONECTADOS'
FriendsListPanelAllFriends = 'TODOS LOS\nAMIGOS'
FriendsListPanelIgnoredFriends = 'DIBUS NO\nATENDIDOS'
DownloadForceAcknowledgeMsg = 'Lo siento; no puedes avanzar porque la descarga de %(phase)s s\xc3\xb3lo lleva completada un %(percent)s%%.\n\nVuelve a intentarlo m\xc3\xa1s tarde.'
DownloadWatcherUpdate = 'Descargando %s.'
DownloadWatcherInitializing = 'Iniciando descarga...'
LauncherPhaseNames = {
    0: 'Inicializando',
    3: 'Crear un dibu',
    3.5: 'Dibututorial',
    4: 'Dibuparque',
    5: 'Calles',
    5.5: 'Propiedades',
    6: 'Barrio I',
    7: 'Edificios' + Cog,
    8: 'Barrio II' }
LauncherProgress = '%(name)s (%(current)s de %(total)s)'
LauncherStartingMessage = "Iniciando Disney's Toontown Online... "
LauncherDownloadFile = 'Descargando actualizaci\xc3\xb3n para ' + LauncherProgress + '...'
LauncherDownloadFileBytes = 'Descargando actualizaci\xc3\xb3n para ' + LauncherProgress + ': %(bytes)s'
LauncherDownloadFilePercent = 'Descargando actualizaci\xc3\xb3n para ' + LauncherProgress + ': %(percent)s%%'
LauncherDecompressingFile = 'Descomprimiendo actualizaci\xc3\xb3n para ' + LauncherProgress + '...'
LauncherDecompressingPercent = 'Descomprimiendo actualizaci\xc3\xb3n para ' + LauncherProgress + ': %(percent)s%%'
LauncherExtractingFile = 'Extrayendo actualizaci\xc3\xb3n para ' + LauncherProgress + '...'
LauncherExtractingPercent = 'Extrayendo actualizaci\xc3\xb3n para ' + LauncherProgress + ': %(percent)s%%'
LauncherPatchingFile = 'Aplicando actualizaci\xc3\xb3n para ' + LauncherProgress + '...'
LauncherPatchingPercent = 'Aplicando actualizaci\xc3\xb3n para ' + LauncherProgress + ': %(percent)s%%'
LauncherConnectProxyAttempt = 'Conectando con Toontown: %s (proxy: %s) intento: %s'
LauncherConnectAttempt = 'Conectando con Toontown: %s intento %s'
LauncherDownloadServerFileList = 'Actualizando Toontown...'
LauncherCreatingDownloadDb = 'Actualizando Toontown...'
LauncherDownloadClientFileList = 'Actualizando Toontown...'
LauncherFinishedDownloadDb = 'Actualizando Toontown... '
LauncherStartingToontown = 'Iniciando Toontown...'
LauncherRecoverFiles = 'Actualizando Toontown. Recuperando archivos...'
LauncherCheckUpdates = 'Comprobando actualizaciones para ' + LauncherProgress
LauncherVerifyPhase = 'Actualizando Toontown...'
AvatarChoiceMakeAToon = 'Crea un\ndibu'
AvatarChoicePlayThisToon = 'Juega con\neste dibu'
AvatarChoiceDelete = 'Borrar'
AvatarChoiceDeleteConfirm = 'Con esto borrar\xc3\xa1s a %s para siempre.'
AvatarChoiceNameRejected = 'Nombre\nrechazado'
AvatarChoiceNameApproved = '\xc2\xa1Nombre\naprobado!'
AvatarChoiceNameReview = 'En proceso\nde revisi\xc3\xb3n'
AvatarChoiceNameYourToon = '\xc2\xa1Pon un nombre\na tu dibu!'
AvatarChoiceDeletePasswordText = '\xc2\xa1Cuidado! Con esto borrar\xc3\xa1s a %s para siempre. Para borrar este dibu, escribe tu contrase\xc3\xb1a.'
AvatarChoiceDeleteConfirmText = '\xc2\xa1Cuidado! Con esto borrar\xc3\xa1s a %(name)s para siempre.  Para confirmar escribe "%(confirm)s" y hace click en Aceptar.'
AvatarChoiceDeleteConfirmUserTypes = 'Borrar'
AvatarChoiceDeletePasswordTitle = '\xc2\xbfQuieres borrar este dibu?'
AvatarChoicePassword = 'Contrase\xc3\xb1a'
AvatarChoiceDeletePasswordOK = 'Aceptar'
AvatarChoiceDeletePasswordCancel = 'Cancelar'
AvatarChoiceDeleteWrongPassword = 'Esa contrase\xc3\xb1a no coincide. Para borrar este dibu, escribe tu contrase\xc3\xb1a.'
AvatarChoiceDeleteWrongConfirm = 'T\xc3\xba no has escrito la palabra correcta.  Para borrar a %(name)s, escribe "%(confirm)s" y hace click en Aceptar.  No escribas las ap\xc3\xb3strofes .  Hace click en Cancelar, si has cambiado de parecer.'
AvatarChooserPickAToon = 'Escoge el dibu con el que vas a jugar'
AvatarChooserQuit = 'Salir'
MultiPageTextFrameNext = 'Siguiente'
MultiPageTextFramePrev = 'Anterior'
MultiPageTextFramePage = 'P\xc3\xa1gina %s/%s'
MemberAgreementScreenTitle = 'Contrato de registro'
MemberAgreementScreenAgree = 'Acepto'
MemberAgreementScreenDisagree = 'No acepto'
MemberAgreementScreenCancel = 'Cancelar'
MemberAgreementScreenWelcome = '\xc2\xa1Bienvenido!'
MemberAgreementScreenOnYourWay = 'Se ha iniciado el proceso para que te conviertas en un socio oficial de'
MemberAgreementScreenToontown = "Avance preliminar de Disney's Toontown Online"
MemberAgreementScreenPricing = "El avance preliminar de Disney's Toontown Online cuesta             \nel primer mes. Cada mes adicional es              .\nY el registro es f\xc3\xa1cil: basta con leer y rellenar la \ninformaci\xc3\xb3n que aparece a continuaci\xc3\xb3n y ya est\xc3\xa1."
MemberAgreementScreenCCUpFrontPricing = 'Inscr\xc3\xadbete ya en la prueba GRATUITA de      d\xc3\xadas. Puedes cancelar tu suscripci\xc3\xb3n\nen cualquier momento del per\xc3\xadodo gratuito sin coste alguno. Al final del\nper\xc3\xadodo gratuito de prueba, se te facturar\xc3\xa1n autom\xc3\xa1ticamente            por\nel primer mes, y despu\xc3\xa9s,            por cada mes adicional.'
MemberAgreementScreenGetParents = "Debes tener al menos 18 a\xc3\xb1os para adquirir Disney's Toontown Online. Pide a tus padres o tutores que te ayuden."
MemberAgreementScreenGetParentsUnconditional = "Debes tener al menos 18 a\xc3\xb1os para adquirir Disney's Toontown Online. Si tienes menos de 18 a\xc3\xb1os, pide ayuda a tus padres o tutores."
MemberAgreementScreenMustBeOlder = "Debes tener al menos 18 a\xc3\xb1os para adquirir Disney's Toontown Online. Pide a tus padres o tutores que te ayuden."
MemberAgreementScreenYouMustAgree = "Para adquirir Disney's Toontown Online, debes aceptar el Contrato de registro."
MemberAgreementScreenYouMustAgreeOk = 'Aceptar'
MemberAgreementScreenYouMustAgreeQuit = 'Salir'
MemberAgreementScreenAgreementTitle = 'Contrato de registro'
MemberAgreementScreenClickNext = 'Pulsa "Siguiente" para pasar a la p\xc3\xa1gina siguiente.'
MemberAgreementScreenLegalText = [
    '\n\n\n\n\n\n\nCONTRATO DE REGISTRO DE TOONTOWN ONLINE DE DISNEY\n\nBienvenido/a a Toontown Online de Disney (en lo sucesivo, el "Servicio"). LE ROGAMOS QUE LEA ATENTAMENTE ESTE CONTRATO (EN LO SUCESIVO, EL "CONTRATO") ANTES DE UTILIZAR ESTE SERVICIO. Este Servicio es propiedad de Disney Online, el cual se encarga tambi\xc3\xa9n de su explotaci\xc3\xb3n (en la presente, referido como "Disney", "nosotros" o cualquier forma de la primera persona del plural).\n',
    '\nEl uso de este Servicio implica la aceptaci\xc3\xb3n de estas condiciones, las Cl\xc3\xa1usulas de utilizaci\xc3\xb3n y las Normas de la casa que aparecen en nuestro sitio Web. Si no est\xc3\xa1 de acuerdo con todas ellas, le rogamos que se abstenga de utilizar este Servicio. Tenga en cuenta que en este Contrato usted aparecer\xc3\xa1 como el "Socio". La persona que se registre por primera vez en el Servicio tambi\xc3\xa9n recibir\xc3\xa1 la denominaci\xc3\xb3n de "Cuenta matriz" en este documento. Por "Cuenta" se entiende la cuenta con la que se ha registrado cualquier socio, en virtud de los procedimientos de registro del Servicio. Las cl\xc3\xa1usulas de este Contrato ser\xc3\xa1n de aplicaci\xc3\xb3n para todos los Socios, conformen \xc3\xa9stos o no la Cuenta matriz. El titular de la Cuenta matriz ser\xc3\xa1 responsable de hacer que todos los socios de una misma familia (y cualquier otra persona a la que permita jugar mediante la Cuenta) conozcan las condiciones de este Contrato y de garantizar que las cumplan. El titular de la Cuenta matriz de una Cuenta cualquiera ser\xc3\xa1 totalmente responsable de todas las actividades que se lleven a cabo mediante dicha Cuenta.\n',
    '\nNos reservamos el derecho, cuando as\xc3\xad lo estimemos oportuno, de cambiar, modificar, agregar o eliminar cualquier parte de este Contrato en cualquier momento. Todas las modificaciones realizadas en \xc3\xa9l ser\xc3\xa1n notificadas por medio de su publicaci\xc3\xb3n en el Servicio o mediante correo electr\xc3\xb3nico u ordinario.\n\nSi alg\xc3\xban cambio futuro en este Contrato resultase inaceptable para usted, o debido a dicho cambio usted no cumpliese dicho Contrato, podr\xc3\xa1 cancelar su Cuenta. El uso continuado por su parte del Servicio tras haber sido informado de los cambios que se hayan dado en el Contrato (incluidas las Cl\xc3\xa1usulas de uso y las Normas de la casa) implicar\xc3\xa1 que ha aceptado dichos cambios.\n',
    '\nNos reservamos el derecho de cambiar, modificar, suspender o interrumpir cualquiera de los aspectos del Servicio en cualquier momento, lo que incluye, entre otros aspectos, la disponibilidad de cualquier Servicio, base de datos o contenido, las horas de disponibilidad y el equipo necesario para acceder al Servicio. Tambi\xc3\xa9n podremos establecer l\xc3\xadmites sobre algunas funciones concretas o restringir su acceso a parte o la totalidad del Servicio, durante amplios periodos, sin notificaci\xc3\xb3n previa y sin que incurramos en ninguna responsabilidad.\n\nEl Socio ser\xc3\xa1 el \xc3\xbanico responsable de obtener la conexi\xc3\xb3n telef\xc3\xb3nica y el equipo necesarios para acceder al Servicio, lo que incluye, entre otras partes del equipo, el software y los medios de a Internet.\n',
    '\nRESTRICCIONES EN EL USO DEL MATERIAL\n\nTodo el material publicado por Disney (incluidos, entre otros, los recursos de informaci\xc3\xb3n, las fotograf\xc3\xadas, las im\xc3\xa1genes, las ilustraciones y los clips de sonido y de v\xc3\xaddeo, denominados de manera colectiva el "Contenido") est\xc3\xa1n protegidos por derechos de copyright y son propiedad de Disney, sus empresas matrices o filiales o cualquier proveedor externo, y est\xc3\xa1n controlados por todos ellos. El socio deber\xc3\xa1 acatar todas las notificaciones informaciones y restricciones de copyright que aparezca en cualquier Contenido al que tenga acceso mediante el Servicio.\n',
    '\nEl Servicio est\xc3\xa1 protegido por derechos de copyright como trabajo colectivo y/o recopilaci\xc3\xb3n, en virtud de las leyes estadounidenses de copyright, los convenios internacionales y el resto de las leyes sobre copyright existentes. Queda prohibido copiar, reproducir, volver a publicar, subir a un sitio web, publicar y transmitir cualquier material procedente del Servicio o de cualquier sitio Web que sea propiedad de Disney, que est\xc3\xa9 explotado o controlado por Disney o sobre el cual Disney posea una licencia; asimismo est\xc3\xa1 prohibido crear y distribuir cualquier trabajo derivado de dicho material, excepto en el caso de la descarga de Internet de una copia del material en un \xc3\xbanico ordenador para su uso personal no comercial, siempre y cuando cumpla todas las notificaciones de copyright y de propiedad. La utilizaci\xc3\xb3n de nuestro Contenido para cualquier otro uso constituir\xc3\xa1 una violaci\xc3\xb3n de nuestros derechos de copyright y de propiedad. A efectos de este Contrato, el uso de cualquier parte de nuestro Contenido en cualquier otro sitio web o en cualquier ordenador que est\xc3\xa9 conectado a una red queda terminantemente prohibido. No est\xc3\xa1 autorizado a vender ni subastar ninguno de los personajes, art\xc3\xadculos y material protegidos por los derechos de copyright de Disney.\n',
    '\nSi descarga alg\xc3\xban tipo de software del Servicio, dicho software, incluidos todos los archivos, las im\xc3\xa1genes que se encuentren en \xc3\xa9l o que \xc3\xa9ste genere y todos los datos que acompa\xc3\xb1en a dicho software (denominados, de manera colectiva, el "Software"), contar\xc3\xa1 con la licencia que le ofrece Disney. Por la presente, le conferimos una licencia no exclusiva para utilizar el Software \xc3\xbanicamente en relaci\xc3\xb3n con el Servicio a trav\xc3\xa9s de una Cuenta autorizada y pagada (o una versi\xc3\xb3n de prueba autorizada). La Cuenta matriz pacta y acuerda que (a) ninguno de los materiales, sea del tipo que sea, que se env\xc3\xade a trav\xc3\xa9s de su Cuenta podr\xc3\xa1 (i) transgredir, plagiar o infringir en menoscabo de los derechos a terceros, incluidos los derechos de copyright, marca registrada, confidencialidad y cualquier otro tipo de derecho personal o de propiedad, ni (ii) contener material ilegal ni injurioso; (b) el n\xc3\xbamero de la tarjeta de cr\xc3\xa9dito que nos ha facilitado es v\xc3\xa1lido, el titular de la Cuenta matriz tiene la autorizaci\xc3\xb3n para utilizar dicha tarjeta de cr\xc3\xa9dito y tiene al menos 18 a\xc3\xb1os de edad; (c) podemos cargar pagos en la tarjeta de cr\xc3\xa9dito cuyo n\xc3\xbamero se nos ha proporcionado, tal y como se describe en detalle en la secci\xc3\xb3n llamada "Precios y pagos" que aparece a continuaci\xc3\xb3n y (d) el titular de la Cuenta matriz y todos los Socios cumplir\xc3\xa1n plenamente las cl\xc3\xa1usulas de este Contrato.\n',
    '\nEl titular de la Cuenta matriz, por la presente eximir\xc3\xa1 a Disney, sus empresas matrices y filiales, y a cualquier empleado, cargo directivo, propietario, agente, proveedor de informaci\xc3\xb3n, afiliado, licenciatario o concedente (denominados de manera colectiva las "Partes eximidas") de cualquier indemnizaci\xc3\xb3n por da\xc3\xb1os y perjuicios en los que hayan incurrido las Partes eximidas en conexi\xc3\xb3n con cualquier reclamaci\xc3\xb3n derivada del incumplimiento por parte suya o de cualquier otro Socio. Disney no acuerda ni acepta la exactitud ni la fiabilidad de ning\xc3\xban consejo, opini\xc3\xb3n, declaraci\xc3\xb3n o cualquier otro tipo de informaci\xc3\xb3n publicada, subida o distribuida mediante el Servicio por parte de cualquier Socio, proveedor de informaci\xc3\xb3n o cualquier otra persona f\xc3\xadsica o jur\xc3\xaddica. Por la presente, el Socio acepta bajo su propio riesgo la fiabilidad de dichas opiniones, consejos, declaraciones, memorandos o informaci\xc3\xb3n en general. Disney se reserva el derecho, cuando as\xc3\xad lo estime oportuno, de corregir cualquier error u omisi\xc3\xb3n en cualquier parte del Servicio.\n',
    '\nEXENCI\xc3\x93N DE RESPONSABILIDAD\n\nEL MATERIAL QUE APARECE EN ESTE SERVICIO SE OFRECE "TAL Y COMO EST\xc3\x81" Y SIN NING\xc3\x9aN TIPO DE GARANT\xc3\x8dA, IMPL\xc3\x8dCITA NI EXPL\xc3\x8dCITA. SIEMPRE QUE LA LEY VIGENTE LO PERMITA, DISNEY ESTAR\xc3\x81 EXENTO DE TODAS LAS GARANT\xc3\x8dAS, IMPL\xc3\x8dCITAS O EXPL\xc3\x8dCITAS, INCLUIDAS, ENTRE OTRAS, LAS GARANT\xc3\x8dAS IMPL\xc3\x8dCITAS DE COMERCIALIZACI\xc3\x93N Y ADECUACI\xc3\x93N A UN OBJETIVO CONCRETO. DISNEY NO GARANTIZA QUE LAS FUNCIONES QUE APARECEN EN ESTE SERVICIO EST\xc3\x89N EXENTAS DE INTERRUPCIONES O ERRORES, QUE SE CORRIJAN TODOS LOS DEFECTOS NI QUE ESTE SERVICIO NI EL SERVIDOR A TRAV\xc3\x89S DEL QUE FUNCIONA EST\xc3\x89N EXENTOS DE VIRUS U OTROS COMPONENTES DA\xc3\x91INOS. DISNEY NO GARANTIZA TAMPOCO NI ACUERDA NINGUNA CL\xc3\x81USULA RESPECTO AL USO O LAS CONSECUENCIAS DEL USO DEL MATERIAL DE ESTE SERVICIO EN CUANTO A SU EXACTITUD, FIABILIDAD, ETC.\n',
    '\nEL SOCIO (Y NO DISNEY) ASUME EL COSTO TOTAL POR CUALQUIER TAREA DE MANTENIMIENTO, REPARACI\xc3\x93N O CORRECCI\xc3\x93N. EN CASO DE QUE LA LEY VIGENTE PROH\xc3\x8dBA LA EXCLUSI\xc3\x93N DE LAS GARANT\xc3\x8dAS IMPL\xc3\x8dCITAS, LA EXCLUSI\xc3\x93N ANTERIOR PUEDE NO RESULTAR DE APLICACI\xc3\x93N EN SU CASO.\nSIN PERJUICIO DE LO ESTABLECIDO ANTERIORMENTE, EL SOCIO RECONOCE QUE, EN LA CALIDAD DE SERVICIO PARA LOS USUARIOS DEL SERVICIO DE DISNEY, PODEMOS INCLUIR ENLACES A OTROS SITIOS WEB DE INTERNET, Y DISNEY NO TIENE NING\xc3\x9aN CONTROL NI PACTA NING\xc3\x9aN TIPO DE GARANT\xc3\x8dA EN RELACI\xc3\x93N CON EL CONTENIDO O LA ADECUACI\xc3\x93N DEL CONTENIDO DE DICHOS SITIOS WEB. EL SOCIO, POR LA PRESENTE, NOS EXIME DE MANERA IRREVOCABLE DE CUALQUIER RECLAMACI\xc3\x93N REFERIDA A DICHOS SITIOS WEB.\n',
    '\nAdem\xc3\xa1s, Disney rechaza cualquier responsabilidad relativa a la exactitud, el contenido o la disponibilidad de la informaci\xc3\xb3n que aparece en los sitios web a los que se acceda a trav\xc3\xa9s de Toontown Online de Disney de terceros que no est\xc3\xa9n asociados con Disney. En Disney le aconsejamos que sea precavido cuando navegue por el Internet, ya se encuentre, utilizando nuestro servicio o el de cualquier otra persona o empresa. Dado que en ocasiones algunos sitios utilizan los resultados de b\xc3\xbasquedas automatizadas o bien conducen a sitios web que contienen informaci\xc3\xb3n que puede ser considerada ofensiva o inadecuada, Disney no se responsabilizar\xc3\xa1 por la exactitud ni por el cumplimiento de los derechos de copyright, legalidad o decencia del material en los sitios Web de terceros, y el socio, por la presente, nos exime de cualquier reclamaci\xc3\xb3n contra nosotros en relaci\xc3\xb3n con dichos sitios web. Disney no podr\xc3\xa1 garantizarle que estar\xc3\xa1 satisfecho con los productos o servicios que contrate en un sitio Web de terceros conectado a Toontown Online de Disney, ya que los canales de otros establecimientos son propiedad de otros minoristas que los explotan.\n',
    '\nDisney no garantiza ninguna de las mercanc\xc3\xadas, ni tampoco confirma la exactitud o la fiabilidad de la informaci\xc3\xb3n que aparezca en los sitios web de dichas terceras personas. Disney no pacta ni garantiza la seguridad de ning\xc3\xban tipo de informaci\xc3\xb3n, lo que incluye, entre otras cosas, los datos de su tarjeta de cr\xc3\xa9dito y cualquier otro tipo de informaci\xc3\xb3n personal que le pida cualquier empresa externa, y el Socio, por la presente, nos exime de cualquier reclamaci\xc3\xb3n contra nosotros en relaci\xc3\xb3n con dichos sitios web. Le rogamos encarecidamente que efect\xc3\xbae las investigaciones necesarias o que considere adecuadas antes de realizar cualquier transacci\xc3\xb3n a trav\xc3\xa9s del Internet o fuera de ella con dichas terceras partes.\n',
    '\nRESPONSABILIDAD LIMITADA\n\nBAJO NINGUNA CIRCUNSTANCIA, INCLUIDA, ENTRE OTRAS, LA NEGLIGENCIA, SER\xc3\x81 DISNEY RESPONSABLE DE NINGUNA INDEMNIZACI\xc3\x93N POR DA\xc3\x91OS Y PERJUICIOS, ESPECIALES O INDIRECTOS, QUE SE DERIVEN DEL USO DE LOS MATERIAL DE ESTE SERVICIO O DE CUALQUIER SITIO WEB, NI DE LA INCAPACIDAD PARA USARLO, NI SIQUIERA EN EL CASO DE QUE DISNEY O UN REPRESENTANTE AUTORIZADO POR DISNEY HAYA SIDO ADVERTIDO DE LA POSIBILIDAD DE DICHA RECLAMACI\xc3\x93N POR DA\xc3\x91OS Y PERJUICIOS. ES POSIBLE QUE LA LEGISLACI\xc3\x93N VIGENTE NO PERMITA LA EXCLUSI\xc3\x93N O LA LIMITACI\xc3\x93N DE RESPONSABILIDAD O DE DA\xc3\x91OS Y PERJUICIOS ACCESORIOS O INDIRECTOS, POR LO CUAL LA LIMITACI\xc3\x93N O EXCLUSI\xc3\x93N ANTERIOR PUEDE NO RESULTAR APLICABLE PARA USTED. EN TODO CASO, LA RESPONSABILIDAD TOTAL DE DISNEY FRENTE AL SOCIO POR CUALQUIER INDEMNIZACI\xc3\x93N POR DA\xc3\x91OS Y PERJUICIOS, P\xc3\x89RDIDAS Y ACCIONES LEGALES (YA SEAN CONTRACTUALES O POR IL\xc3\x8dCITO CIVIL INCLUIDA, ENTRE OTRAS, LA NEGLIGENCIA) NO SOBREPASAR\xc3\x81 LA CANTIDAD ABONADA, DE HABERLO HECHO, PARA ACCEDER AL SERVICIO.\n',
    '\nSEGURIDAD\nComo parte integrante del proceso de registro, los Socios deber\xc3\xa1n elegir una contrase\xc3\xb1a, una contrase\xc3\xb1a principal y un nombre de socio (en lo sucesivo, el "Nombre de socio"). Deber\xc3\xa1 proporcionar a Disney informaci\xc3\xb3n de la Cuenta actualizada, exacta y completa. En caso contrario, estar\xc3\xa1 incumpliendo este Contrato, lo que puede resultar en la cancelaci\xc3\xb3n inmediata de su Cuenta. En ning\xc3\xban caso podr\xc3\xa1 (i) seleccionar o utilizar el Nombre de socio de otra persona con la intenci\xc3\xb3n de hacerse pasar por esa persona; (ii) utilizar un nombre que est\xc3\xa9 sujeto a los derechos de otra persona sin autorizaci\xc3\xb3n o (iii) utilizar un Nombre de socio que, en opini\xc3\xb3n de Disney, sea inadecuado u ofensivo.\n',
    '\nEn caso de que le conste o sospeche que existe alg\xc3\xban usuario no autorizado de su Cuenta, o si conoce alg\xc3\xban incumplimiento de la seguridad (o lo sospecha), lo que incluye la p\xc3\xa9rdida, el robo y la divulgaci\xc3\xb3n no autorizada de su contrase\xc3\xb1a o de la contrase\xc3\xb1a principal, deber\xc3\xa1 notific\xc3\xa1rselo inmediatamente a Disney en la direcci\xc3\xb3n de correo electr\xc3\xb3nico toontown@disneyonline.com,. La responsabilidad de mantener la confidencialidad de su contrase\xc3\xb1a y contrase\xc3\xb1a principal ser\xc3\xa1 \xc3\xbanicamente suya.\n\nTodos los titulares de las Cuentas matrices deber\xc3\xa1n tener 18 a\xc3\xb1os de edad o m\xc3\xa1s para poder abrir una Cuenta. Si Disney descubriese que el titular de una Cuenta matriz es menor de 18 a\xc3\xb1os, se reserva el derecho de cancelar dicha Cuenta.\n\nCualquier actividad fraudulenta, abusiva o que no resulte conforme a derecho puede constituir la base de la cancelaci\xc3\xb3n de su Cuenta, y cuando Disney as\xc3\xad lo estime oportuno, se pondr\xc3\xa1 su caso en conocimiento de las instituciones legislativas pertinentes.\n',
    '\nPRECIOS Y PAGOS\n\nDisney se reserva el derecho de cobrar, cuando as\xc3\xad lo considere oportuno, cualquier tarifa adicional por el acceso al Servicio. Disney se reserva el derecho de cobrar cualquier cantidad o tarifa por el Servicio y de establecer nuevas tarifas o precios, que entrar\xc3\xa1n en vigor previa notificaci\xc3\xb3n a los Socios. Disney se reserva el derecho de ofrecer el Servicio de manera gratuita por motivos promocionales u otras razones (como, por ejemplo, una versi\xc3\xb3n de prueba).\n\nLos titulares de las Cuentas matrices se comprometen a abonar todos los pagos en que incurra la Cuenta matriz, incluidos los impuestos vigentes, de conformidad con las normas de facturaci\xc3\xb3n existentes en el momento en el que la tarifa o el gravamen resulte pagadero. Los titulares de las Cuentas matrices deber\xc3\xa1n proporcionar a Disney informaci\xc3\xb3n de la tarjeta de cr\xc3\xa9dito v\xc3\xa1lida, tal y como se solicita durante el proceso de registro.\n',
    '\nDisney pasar\xc3\xa1 el cobro a la tarjeta de cr\xc3\xa9dito del titular de la Cuenta matriz en la fecha en la que \xc3\xa9ste se suscriba al Servicio. A partir de esa fecha, Disney efectuar\xc3\xa1, de manera autom\xc3\xa1tica, las siguientes acciones y proceder\xc3\xa1 al cobro de la Cuenta matriz como se indica a continuaci\xc3\xb3n:\n\n- Cada mes, en concepto del Servicio del mes siguiente para suscripciones mensuales.\n\n- Cada tres (3) meses desde el primer cobro para las suscripciones trimestrales.\n\n- Cada seis (6) meses desde el primer cobro para las suscripciones semestrales.\n\n- Cada a\xc3\xb1o (1) desde el primer cobro para las suscripciones anuales.\n',
    '\nEl cargo por renovaci\xc3\xb3n ser\xc3\xa1 equivalente o inferior al precio de suscripci\xc3\xb3n, a menos que Disney indique previamente lo contrario. Podr\xc3\xa1 informar a Disney de que desea cancelar su suscripci\xc3\xb3n en cualquier momento. Disney se compromete a cancelar su Cuenta a la recepci\xc3\xb3n de dicha notificaci\xc3\xb3n de la Cuenta matriz, tal y como se describe m\xc3\xa1s adelante.\n\nEn el caso de las suscripciones mensuales: Si se recibe la notificaci\xc3\xb3n de la cancelaci\xc3\xb3n durante los 15 d\xc3\xadas siguientes al cobro inicial, tendr\xc3\xa1 derecho a que le devuelvan todas las tasas de suscripci\xc3\xb3n del Servicio, pero deber\xc3\xa1 pagar el resto de los gastos en los que haya incurrido. Si cancela el Servicio despu\xc3\xa9s de los 15 d\xc3\xadas siguientes al cobro inicial, su Cuenta ser\xc3\xa1 cancelada al final del per\xc3\xadodo de facturaci\xc3\xb3n en curso y no se le devolver\xc3\xa1 ning\xc3\xban importe por el tiempo en que no lo haya utilizado.\n',
    '\nEn el caso de las suscripciones trimestrales: Si se recibe la notificaci\xc3\xb3n de la cancelaci\xc3\xb3n durante los 30 d\xc3\xadas siguientes al cobro inicial, tendr\xc3\xa1 derecho a que le devuelvan todas las tasas de suscripci\xc3\xb3n del Servicio, pero deber\xc3\xa1 pagar el resto de los gastos en los que haya incurrido. Si cancela el Servicio despu\xc3\xa9s de transcurridos 30 d\xc3\xadas, no se le devolver\xc3\xa1 ning\xc3\xban importe por el tiempo en que no lo haya utilizado.\n\nEn el caso de las suscripciones semestrales: Si se recibe la notificaci\xc3\xb3n de la cancelaci\xc3\xb3n durante los 30 d\xc3\xadas siguientes al cobro inicial, tendr\xc3\xa1 derecho a que le devuelvan todas las tasas de suscripci\xc3\xb3n del Servicio, pero deber\xc3\xa1 pagar el resto de los gastos en los que haya incurrido. Si cancela el Servicio despu\xc3\xa9s de los 30, no se le devolver\xc3\xa1 ninguna cantidad por el tiempo en que no lo haya utilizado.\n',
    '\nEn el caso de las suscripciones anuales: Si se recibe la notificaci\xc3\xb3n de la cancelaci\xc3\xb3n durante los 30 d\xc3\xadas siguientes al cobro inicial, tendr\xc3\xa1 derecho a que le devuelvan todas las tasas de suscripci\xc3\xb3n del Servicio, pero deber\xc3\xa1 pagar el resto de los gastos en los que haya incurrido. Si cancela el Servicio despu\xc3\xa9s de transcurridos 30 d\xc3\xadas, no se le devolver\xc3\xa1 ning\xc3\xban importe por el tiempo en que no lo haya utilizado.\n\nSu derecho a utilizar el Servicio est\xc3\xa1 sujeto a los l\xc3\xadmites que establezca Disney o la entidad emisora de su tarjeta de cr\xc3\xa9dito. Si no se pueden cargar o nos son devueltos los pagos cargados en su tarjeta de cr\xc3\xa9dito, incluido el cargo al usuario, Disney se reserva el derecho de suspender o cancelar su acceso y Cuenta, con lo que quedan rescindidos este Contrato y todas las obligaciones de Disney.\n',
    '\nSi alguna de sus Cuentas de Disney presenta un saldo deudor, el Socio se compromete a que Disney puede cargar estas tarifas morosas en su tarjeta de cr\xc3\xa9dito. Disney se reserva el derecho a establecer un l\xc3\xadmite crediticio (en lo sucesivo, el "L\xc3\xadmite m\xc3\xa1ximo")para cada Socio. Si la Cuenta de un Socio alcanza el L\xc3\xadmite m\xc3\xa1ximo en alg\xc3\xban momento, Disney cargar\xc3\xa1 todos los pagos morosos de la cuenta en la tarjeta de cr\xc3\xa9dito del Socio. A menos que se especifique lo contrario, el L\xc3\xadmite m\xc3\xa1ximo para cada Socio es de 100 d\xc3\xb3lares estadounidenses.\n\nSi sospecha que su Cuenta no es segura (por ejemplo, en caso de p\xc3\xa9rdida, robo o divulgaci\xc3\xb3n no autorizada de su Nombre de socio, su Contrase\xc3\xb1a o el n\xc3\xbamero de la tarjeta de cr\xc3\xa9dito o de d\xc3\xa9bito que aparezca en el Servicio), deber\xc3\xa1 cambiar su Contrase\xc3\xb1a inmediatamente e informar a Disney del problema (mediante notificaci\xc3\xb3n de la forma que se indica en la secci\xc3\xb3n Notificaciones, a continuaci\xc3\xb3n) para evitar cualquier posible responsabilidad por cobros no autorizados que se carguen en su Cuenta.\n',
    '\nCONSENTIMIENTO DE LOS PROGENITORES\n\nDe acuerdo con la Ley estadounidense para la protecci\xc3\xb3n del menor en medios electr\xc3\xb3nicos (Children\'s Online Privacy Protection Act, en lo sucesivo "COPPA"), se necesita el consentimiento de los progenitores para la recopilaci\xc3\xb3n, el uso y la divulgaci\xc3\xb3n de informaci\xc3\xb3n personal correspondiente a un ni\xc3\xb1o de menos de 13 a\xc3\xb1os. Como parte del proceso de registro del Servicio, el titular de la Cuenta matriz deber\xc3\xa1 proporcionar una tarjeta de cr\xc3\xa9dito v\xc3\xa1lida. Los progenitores y representantes legales podr\xc3\xa1n crear un m\xc3\xa1ximo de seis Toons (un Toon es un personaje que el socio crea y utiliza para jugar en el Servicio), todos ellos dentro de la Cuenta matriz. Los ni\xc3\xb1os podr\xc3\xa1n crear su propio Toon dentro de la Cuenta matriz previo consentimiento del progenitor o el tutor inscrito como titular de la Cuenta matriz.\n',
    '\nAl proporcionar el n\xc3\xbamero de su tarjeta de cr\xc3\xa9dito, el titular de la Cuenta matriz (a) pacta y acuerda ser el progenitor o representante legal de cualquier ni\xc3\xb1o menor de 13 a\xc3\xb1os al que permita utilizar la Cuenta matriz y (b) consiente en que recopilemos, utilicemos y divulguemos la informaci\xc3\xb3n personal, en conformidad con las Normas de confidencialidad, respecto a cualquier ni\xc3\xb1o menor de 13 a\xc3\xb1os al que el titular de la Cuenta matriz permita utilizar dicha cuenta.\n\nEl Servicio incluye una funci\xc3\xb3n interactiva que denominados Amigos secretos. El titular de la Cuenta matriz podr\xc3\xa1 desactivar la funci\xc3\xb3n de Amigos secretos una vez que est\xc3\xa9 dentro del Servicio. La funci\xc3\xb3n de Amigos secretos permite a los socios charlar con otros socios mediante un c\xc3\xb3digo secreto que se debe comunicar fuera del juego. La funci\xc3\xb3n de Amigos secretos no tiene ning\xc3\xban moderador ni supervisor.\n',
    '\nSi el titular de una Cuenta matriz permite a un ni\xc3\xb1o usar su propia cuenta con la funci\xc3\xb3n de Amigos secretos activada, le rogamos que supervise a sus hijos mientras juegan con el Servicio. Al activar la funci\xc3\xb3n de Amigos secretos, el titular de la Cuenta matriz reconoce que existen riesgos inherentes a dicha funci\xc3\xb3n y que ha sido informado y acepta dichos riesgos. Podr\xc3\xa1 obtener m\xc3\xa1s informaci\xc3\xb3n de la funci\xc3\xb3n de Amigos secretos y la forma de activarla dentro del Servicio.\n',
    '\nNOTIFICACIONES\n\nEl titular de la Cuenta matriz enviar\xc3\xa1 y dispondr\xc3\xa1 de una direcci\xc3\xb3n de correo electr\xc3\xb3nico correcta, as\xc3\xad como otros datos sobre la Cuenta. Podremos realizar las notificaciones al titular de la Cuenta matriz a trav\xc3\xa9s de una notificaci\xc3\xb3n de tipo general en el Servicio, mediante correo electr\xc3\xb3nico a la direcci\xc3\xb3n que consta en nuestra informaci\xc3\xb3n de Cuenta, o mediante carta urgente enviada a la direcci\xc3\xb3n postal que consta en nuestro poder. Puede enviar cualquier notificaci\xc3\xb3n a Disney. Dicha notificaci\xc3\xb3n se considerar\xc3\xa1 entregada cuando Disney la reciba por correo electr\xc3\xb3nico en la direcci\xc3\xb3n toontown@disneyonline.com.\n',
    '\nNO TRANSFERIBILIDAD\n\nDisney le otorga una licencia personal, no exclusiva y de no cesi\xc3\xb3n para utilizar y poder ver el Software de Disney en cualquier dispositivo del cual usted sea el principal usuario. La copia no autorizada del Software o la reproducci\xc3\xb3n de cualquier forma del software del programa principal y el software que haya sido modificado, integrado o incluido con el Software, as\xc3\xad como la documentaci\xc3\xb3n relacionada con \xc3\xa9l, quedan totalmente prohibidas. Por la presente, el Socio acuerda que no puede ceder esta licencia ni el Software, ni transferirlos, venderlos o cederlos. Cualquier intento de emprender dichas acciones se considera ileg\xc3\xadtimo. \n',
    '\nCUESTIONES JUR\xc3\x8dDICAS \n\nEste Servicio est\xc3\xa1 controlado y explotado por Disney desde sus oficinas en el estado de California (Estados Unidos). Disney no garantiza que el material que aparece en el Servicio sea adecuado o est\xc3\xa9 disponible en otros lugares. Las personas que decidan acceder a este Servicio desde otros lugares lo har\xc3\xa1n por iniciativa propia y ser\xc3\xa1n responsables del cumplimiento de la legislaci\xc3\xb3n local aplicable. El Software disponible en este Servicio tambi\xc3\xa9n est\xc3\xa1 sujeto a los controles de exportaci\xc3\xb3n de los Estados Unidos. Est\xc3\xa1 prohibido descargar, exportar o hacer llegar el Software de este Servicio a (i) Cuba, Irak, Libia, Corea del Norte, Ir\xc3\xa1n, Siria (ni a un ciudadano o residente de estos pa\xc3\xadses), a ning\xc3\xban pa\xc3\xads con el que Estados Unidos mantenga un embargo o (ii) a alguien que aparezca en la lista Specially Designated Nationals (Ciudadanos especialmente mencionados) del Ministerio de Hacienda estadounidense o en la Table of Deny Orders (tabla de denegaci\xc3\xb3n de pedidos) del Ministerio de Comercio.\n',
    '\nAl descargar o utilizar el Software, el Socio pacta y conviene que no est\xc3\xa1 situado bajo el control de dichos pa\xc3\xadses, ni es ciudadano o residente de ellos, y asimismo, que no aparece en las listas mencionadas. Algunos tipos de Software que los Socios descargan para usarlo o instalan desde un CD-ROM es "Software restringido a ordenadores". El uso, la copia y la divulgaci\xc3\xb3n por parte del gobierno estadounidense est\xc3\xa1n sujetos a las restricciones que se establecen en este Contrato y en las leyes federales DFARS 227.7202-1(a) y 227.7202-3(a) (1995), DFARS 252.227-7013 (Octubre de 1988), FAR 12.212(a) (1995), FAR 52.227-19, o FAR 52.227-14, seg\xc3\xban sea el caso.\n',
    '\nEXPIRACI\xc3\x93N DEL SERVICIO\n\nEste Contrato estar\xc3\xa1 en vigencia hasta que sea cancelado por una de las dos partes. Puede cancelar este Contrato y su derecho a utilizar el Servicio cuando lo desee enviando un mensaje de correo electr\xc3\xb3nico a toontown@disneyonline.com. Disney podr\xc3\xa1 cancelar su Cuenta o sus derechos de acceso a este Servicio de manera inmediata sin notificaci\xc3\xb3n previa si, en opini\xc3\xb3n de Disney, incumple alguna de las cl\xc3\xa1usulas de este Contrato (incluidas las Cl\xc3\xa1usulas de uso y las Normas de la casa). Una vez cancelado el contrato, deber\xc3\xa1 destruir todo el material que haya obtenido gracias a este Servicio y cualquier copia existente, independientemente de que se hiciera de acuerdo con las cl\xc3\xa1usulas de este Contrato.\n',
    '\nVARIOS\n\nEste Contrato se regir\xc3\xa1 e interpretar\xc3\xa1 de conformidad con las leyes del estado de Carolina, sin consideraci\xc3\xb3n de ning\xc3\xban principio de conflicto de leyes. Si alguna cl\xc3\xa1usula del presente Contrato no fuese conforme a derecho, fuese nula o, por alguna raz\xc3\xb3n, no resultara aplicable, dicha cl\xc3\xa1usula podr\xc3\xa1 eliminarse de este Contrato y el resto de las cl\xc3\xa1usulas conservar\xc3\xa1n su vigencia. El presente Contrato constituye la totalidad del acuerdo entre las partes acerca del objeto que se trata en \xc3\xa9l y s\xc3\xb3lo podr\xc3\xa1 ser modificado por escrito, y siempre de la forma que se describe a continuaci\xc3\xb3n.\n',
    '\nCONTRATO COMPLETO\n\nEste Contrato constituye la totalidad del contrato entre las partes respecto al objeto que en \xc3\xa9l se trata y sustituye a cualquier contrato anterior o actual que exista o haya existido, as\xc3\xad como a cualquier propuesta o comunicado, ya sea escrito o verbal, entre los representantes de Disney y el Socio. Disney podr\xc3\xa1 modificarlo o alterarlo, as\xc3\xad como incluir nuevas cl\xc3\xa1usulas, siempre que lo estime oportuno, previa notificaci\xc3\xb3n al Socio, tal y como se describe en el apartado "Notificaciones" anterior. Cualquier uso del Servicio por su parte posterior a dicha notificaci\xc3\xb3n constituir\xc3\xa1 una aceptaci\xc3\xb3n impl\xc3\xadcita de dichas modificaciones, alteraciones o nuevas cl\xc3\xa1usulas.\xc3\x9aLTIMA ACTUALIZACI\xc3\x93N:\n\n18/10/02\n']
BillingScreenCCTypeInitialText = 'Elija una opci\xc3\xb3n'
BillingScreenCreditCardTypes = [
    'Visa',
    'American Express',
    'MasterCard']
BillingScreenTitle = 'Introduzca la informaci\xc3\xb3n de facturaci\xc3\xb3n'
BillingScreenAccountName = 'Nombre de la cuenta'
BillingScreenEmail = 'Direcci\xc3\xb3n de correo electr\xc3\xb3nico de los padres para la facturaci\xc3\xb3n'
BillingScreenEmailConfirm = 'Confirme la direcci\xc3\xb3n de correo electr\xc3\xb3nico'
BillingScreenCreditCardType = 'Tipo de tarjeta de cr\xc3\xa9dito'
BillingScreenCreditCardNumber = 'N\xc3\xbamero de la tarjeta de cr\xc3\xa9dito'
BillingScreenCreditCardExpires = 'Fecha de caducidad'
BillingScreenCreditCardName = 'Nombre que aparece en la tarjeta de cr\xc3\xa9dito'
BillingScreenAgreementText = 'Al hacer clic en el bot\xc3\xb3n "Comprar" acepto que, de acuerdo con las Normas de confidencialidad, mis hijos pueden usar las herramientas interactivas autorizadas mediante la contrase\xc3\xb1a parental que establecer\xc3\xa9 en la pantalla siguiente.'
BillingScreenBillingAddress = 'Direcci\xc3\xb3n de facturaci\xc3\xb3n: Calle 1'
BillingScreenBillingAddress2 = 'Calle 2 (si procede)'
BillingScreenCity = 'Ciudad'
BillingScreenCountry = 'Pa\xc3\xads'
BillingScreenState = 'Estado'
BillingScreenZipCode = 'C\xc3\xb3digo postal'
BillingScreenCAProvince = 'Provincia o territorio'
BillingScreenProvince = 'Provincia (si procede)'
BillingScreenPostalCode = 'C\xc3\xb3digo postal'
BillingScreenPricing = '              durante el primer mes, despu\xc3\xa9s              al mes'
BillingScreenSubmit = 'Comprar'
BillingScreenCancel = 'Cancelar'
BillingScreenConfirmCancel = '\xc2\xbfDesea cancelar la compra?'
BillingScreenConfirmCancelYes = 'S\xc3\xad'
BillingScreenConfirmCancelNo = 'No'
BillingScreenPleaseWait = 'Espere un momento...'
BillingScreenConnectionErrorSuffix = '.\nVuelva a intentarlo m\xc3\xa1s tarde.'
BillingScreenEnterEmail = 'Escriba su direcci\xc3\xb3n de correo electr\xc3\xb3nico.'
BillingScreenEnterEmailConfirm = 'Vuelva a escribir su direcci\xc3\xb3n de correo electr\xc3\xb3nico.'
BillingScreenEnterValidEmail = 'Introduzca una direcci\xc3\xb3n de correo electr\xc3\xb3nico v\xc3\xa1lida.'
BillingScreenEmailMismatch = 'Las direcciones de correo electr\xc3\xb3nico que ha introducido no coinciden. Int\xc3\xa9ntelo de nuevo.'
BillingScreenEnterAddress = 'Escriba su direcci\xc3\xb3n de facturaci\xc3\xb3n completa.'
BillingScreenEnterValidState = 'Escriba la abreviatura de dos letras correspondiente al estado.'
BillingScreenChooseCreditCardType = 'Elija un tipo de tarjeta de cr\xc3\xa9dito.'
BillingScreenEnterCreditCardNumber = 'Escriba el n\xc3\xbamero de la tarjeta de cr\xc3\xa9dito.'
BillingScreenEnterValidCreditCardNumber = 'Compruebe el n\xc3\xbamero de la tarjeta de cr\xc3\xa9dito.'
BillingScreenEnterValidSpecificCreditCardNumber = 'Escriba un n\xc3\xbamero v\xc3\xa1lido de la tarjeta de cr\xc3\xa9dito %s.'
BillingScreenEnterValidCreditCardExpDate = 'Escriba una fecha de caducidad v\xc3\xa1lida de la tarjeta de cr\xc3\xa9dito.'
BillingScreenEnterNameOnCard = 'Escriba el nombre que aparece en la tarjeta de cr\xc3\xa9dito.'
BillingScreenCreditCardProblem = 'Se ha producido un error al procesar la tarjeta de cr\xc3\xa9dito.'
BillingScreenTryAnotherCC = '\xc2\xbfDesea probar con otra tarjeta?'
BillingScreenCustomerServiceHelp = '\n\nSi necesita ayuda, p\xc3\xb3ngase en contacto con el Servicio de atenci\xc3\xb3n al cliente, en el tel\xc3\xa9fono %s.'
BillingScreenCCProbQuit = 'Salir'
BillingScreenWhySafe = 'Seguridad de la tarjeta de cr\xc3\xa9dito'
BillingScreenWhySafeTitle = 'Seguridad de la tarjeta de cr\xc3\xa9dito'
BillingScreenWhySafeCreditCardGuarantee = 'GARANT\xc3\x8dA DE LA TARJETA DE CR\xc3\x89DITO'
BillingScreenWhySafeJoin = '\xc2\xa1JUEGA EN'
BillingScreenWhySafeToontown = "DISNEY'S TOONTOWN ONLINE"
BillingScreenWhySafeToday = 'HOY MISMO!'
BillingScreenWhySafeClose = 'Cerrar'
BillingScreenWhySafeText = [
    "\n\n\n\n\nUsamos la tecnolog\xc3\xada Secure Sockets Layer (SSL) para cifrar la informaci\xc3\xb3n de la tarjeta de cr\xc3\xa9dito, protegi\xc3\xa9ndola y garantizando la confidencialidad. Esta tecnolog\xc3\xada permite introducir y transmitir la informaci\xc3\xb3n de la tarjeta de cr\xc3\xa9dito por Internet con total seguridad.\nEsta tecnolog\xc3\xada de seguridad protege sus comunicaciones en Internet con:\n\n     Verificaci\xc3\xb3n de servidores (impide las suplantaciones)\n     Confidencialidad mediante el cifrado (evita la monitorizaci\xc3\xb3n oculta)\n     Integridad de los datos (evita el vandalismo)\n\nPara aumentar m\xc3\xa1s a\xc3\xban la seguridad, todos los n\xc3\xbameros de tarjetas de cr\xc3\xa9dito se almacenan en un ordenador que no est\xc3\xa1 conectado a Internet. Una vez introducido el n\xc3\xbamero completo de la tarjeta de cr\xc3\xa9dito, \xc3\xa9ste se transfiere a dicho ordenador seguro a trav\xc3\xa9s de una conexi\xc3\xb3n no est\xc3\xa1ndar. Los n\xc3\xbameros de las tarjetas de cr\xc3\xa9dito no se almacenan en ning\xc3\xban otro sitio.\n\n\n\nPor tanto, la informaci\xc3\xb3n de su tarjeta de cr\xc3\xa9dito no s\xc3\xb3lo est\xc3\xa1 a salvo en Disney's Toontown Online, sino que adem\xc3\xa1s la garantizamos.\nTodas las suscripciones a Disney's Toontown Online est\xc3\xa1n respaldadas por nuestra garant\xc3\xada de tarjetas de cr\xc3\xa9dito. Si en su extracto de cuentas aparecen cargos no autorizados de los que usted no es responsable como resultado directo de haber enviado los datos de su tarjeta de cr\xc3\xa9dito a Disney's Toontown Online, haremos efectiva la cantidad que le reclama su banco hasta un m\xc3\xa1ximo de 50 USD.\n\nSi sospecha que hay un problema, d\xc3\xa9 parte siguiendo el procedimiento habitual del proveedor de su tarjeta de cr\xc3\xa9dito y p\xc3\xb3ngase en contacto de inmediato con nosotros.  La mayor\xc3\xada de las compa\xc3\xb1\xc3\xadas de tarjetas de cr\xc3\xa9dito se hacen cargo de todos los gastos derivados del uso no autorizado de dichas tarjetas, pero pueden reclamarle el pago de un m\xc3\xa1ximo de 50 USD. Nosotros nos hacemos cargo del pasivo que no est\xc3\xa9 cubierto por su tarjeta de cr\xc3\xa9dito.\n\xc2\xbfQu\xc3\xa9 significa todo esto? Significa que puede confiar en la seguridad y el servicio proporcionados por Disney's Toontown Online.\n\n\xc2\xbfA qu\xc3\xa9 espera, entonces?\n"]
BillingScreenPrivacyPolicy = 'Normas de confidencialidad'
BillingScreenPrivacyPolicyClose = 'Cerrar'
BillingScreenPrivacyPolicyText = [
    '\nNormas de confidencialidad\n\nP1 \xc2\xbfQu\xc3\xa9 tipo de informaci\xc3\xb3n recogen los sitios web de WDIG y c\xc3\xb3mo lo hacen?\n\nLa mayor\xc3\xada de los excelentes productos y servicios que se presentan en nuestros sitios web se ofrecen sin necesidad de recabar ning\xc3\xban tipo de informaci\xc3\xb3n personal de los visitantes. Puede navegar por los sitios web de WDIG y ver una gran parte de nuestro estupendo contenido de forma an\xc3\xb3nima. Por ejemplo, puede consultar los titulares de \xc3\xbaltima hora en ABCNEWS.com sin por ello tener que facilitar ning\xc3\xban tipo de informaci\xc3\xb3n de identificaci\xc3\xb3n personal.\n\nLa informaci\xc3\xb3n que usted nos proporciona\nEn nuestros sitios web existen algunas actividades para las cuales resulta necesario recabar informaci\xc3\xb3n de identificaci\xc3\xb3n personal. Entre ellas se incluyen, por ejemplo, la participaci\xc3\xb3n en concursos, las compras y los mensajes dirigidos a Disney. Cuando recabemos informaci\xc3\xb3n de identificaci\xc3\xb3n personal usted ser\xc3\xa1 consciente de ello, ya que tendr\xc3\xa1 que rellenar un impreso. Para la mayor\xc3\xada de las actividades s\xc3\xb3lo se solicitan el nombre, la direcci\xc3\xb3n de correo electr\xc3\xb3nico, la fecha de nacimiento, el sexo y el c\xc3\xb3digo postal. Cuando se efect\xc3\xbaa una compra, tambi\xc3\xa9n se solicitan las direcciones postales de env\xc3\xado y facturaci\xc3\xb3n, el n\xc3\xbamero de tel\xc3\xa9fono y los datos de la tarjeta de cr\xc3\xa9dito. Seg\xc3\xban lo que se compre, es posible que tambi\xc3\xa9n se solicite otro tipo de informaci\xc3\xb3n personal como, por ejemplo, la talla de ropa.\n',
    '\nInformaci\xc3\xb3n personal recopilada mediante dispositivos tecnol\xc3\xb3gicos\nLos sitios web de WDIG recaban algunos datos mediante dispositivos tecnol\xc3\xb3gicos, de tal forma que puede no darse cuenta de que estamos recogiendo dicha informaci\xc3\xb3n. Por ejemplo, cuando visita nuestro sitio web, se recoge su direcci\xc3\xb3n IP para que sepamos d\xc3\xb3nde tenemos que enviar la informaci\xc3\xb3n que est\xc3\xa1 solicitando. Normalmente, la direcci\xc3\xb3n IP est\xc3\xa1 asociada con el lugar desde el que se ha accedido a Internet, como por ejemplo, el proveedor de Internet, la empresa o la universidad. Esta informaci\xc3\xb3n no le identifica individualmente. Gracias a la informaci\xc3\xb3n recabada mediante los dispositivos tecnol\xc3\xb3gicos, los sitios web de WDIG resultan m\xc3\xa1s interesantes y \xc3\xbatiles para sus visitantes. Esto incluye ayudar a las empresas que se anuncian en nuestro sitio web a dise\xc3\xb1ar anuncios por los que nuestros visitantes puedan sentirse atra\xc3\xaddos. Normalmente no combinamos esta informaci\xc3\xb3n con los datos personales. No obstante, en caso necesario combinaremos la informaci\xc3\xb3n de este tipo con los datos personales con el fin de identificar a los visitante para hacer cumplir las normas de la casa o las cl\xc3\xa1usulas del servicio, as\xc3\xad como para proteger el servicio, el sitio web, a los otros visitantes, etc.\n\n\xc2\xbfQu\xc3\xa9 son las cookies y c\xc3\xb3mo las utiliza WDIG?\nLas cookies son peque\xc3\xb1os fragmentos de informaci\xc3\xb3n que los sitios web visitados env\xc3\xadan al ordenador del visitante. Esta informaci\xc3\xb3n permite al sitio web recordar datos importantes que har\xc3\xa1n que su uso del sitio sea m\xc3\xa1s \xc3\xbatil. WDIG y otras empresas de Internet utilizan cookies por diversos motivos. Por ejemplo, DisneyStore.com utiliza cookies para recordar y procesar los art\xc3\xadculos del carro de la compra, y todos los sitios web de WDIG utilizan cookies para asegurarse de que los ni\xc3\xb1os no entran en las salas de conversaci\xc3\xb3n que no est\xc3\xa9n moderadas.\n\n',
    '\n\nPuede elegir que el ordenador le avise siempre que se env\xc3\xade una cookie, o puede desactivar todas las cookies. Para ello, es necesario modificar la configuraci\xc3\xb3n navegador (como, por ejemplo, Netscape Navigator o Internet Explorer). Todos los navegadores son distintos; por tanto, si desea informaci\xc3\xb3n sobre la forma de modificar las cookies, consulte el men\xc3\xba Ayuda del programa que utiliza. Si desactiva todas las cookies, no podr\xc3\xa1 acceder a muchas funciones de WDIG que mejoran su visita a la web sea mejor (como por ejemplo, las funciones que hemos mencionado antes), y no todos nuestros servicios funcionar\xc3\xa1n correctamente.\n\nP2 \xc2\xbfC\xc3\xb3mo utiliza WDIG la informaci\xc3\xb3n de identificaci\xc3\xb3n personal recabada?\n\nWDIG utiliza la informaci\xc3\xb3n de identificaci\xc3\xb3n personal en situaciones muy concretas. Los datos se utilizan para llevar a cabo las transacciones. Por ejemplo, si adquiere un equipo de fantas\xc3\xada en ESPN.com, utilizamos su informaci\xc3\xb3n para procesar el pedido, o si se pone en contacto con nosotros para pedirnos ayuda, utilizamos esa informaci\xc3\xb3n para ponernos en contacto con usted. Asimismo, utilizaremos la informaci\xc3\xb3n recogida para comunicarle si ha ganado un juego o concurso. Los datos solicitados tambi\xc3\xa9n se utilizan para enviarle por correo electr\xc3\xb3nico actualizaciones y boletines sobre nuestros sitios web, as\xc3\xad como sobre las promociones de WDIG y las ofertas especiales de nuestros patrocinadores externos.\n',
    '\nP3 \xc2\xbfComparte WDIG en alg\xc3\xban caso la informaci\xc3\xb3n con empresas u otro tipo de organizaciones que no forman parte de su grupo de sitios web?\n\nNuestros clientes son los activos m\xc3\xa1s importantes de nuestro negocio. No nos dedicamos a vender la informaci\xc3\xb3n de nuestros visitantes. Sin embargo, cuando esto suponga una ventaja para nuestros visitantes, compartiremos la informaci\xc3\xb3n que tenemos sobre usted o le enviaremos mensajes de parte de otra empresa, como describimos m\xc3\xa1s adelante. Tambi\xc3\xa9n podemos compartir la informaci\xc3\xb3n por motivos de seguridad.\nLas empresas subyacentes al WDIG\nEn ocasiones contratamos a otras empresas para la entrega de productos o servicios, como por ejemplo una empresa de env\xc3\xados que entrega un paquete. En esas ocasiones, nos vemos obligados a compartir la informaci\xc3\xb3n con ellos. Estas empresas pr\xc3\xa1cticamente son representantes de WDIG, y s\xc3\xb3lo pueden utilizar la informaci\xc3\xb3n para entregar el producto o el servicio.\n',
    '\nEmpresas que ofrecen promociones, productos o servicios\nDe vez en cuando, lanzamos promociones, como concursos o suscripciones gratuitas, en colaboraci\xc3\xb3n con un patrocinador. Compartiremos la informaci\xc3\xb3n con los patrocinadores si la necesitan para enviarle un producto, como puede ser la suscripci\xc3\xb3n a una revista. Asimismo, podemos compartir la informaci\xc3\xb3n con dichos patrocinadores para que puedan ofrecerle sus promociones especiales, pero s\xc3\xb3lo si usted as\xc3\xad lo permite y, en ese caso, la compartiremos s\xc3\xb3lo con ese patrocinador en concreto.  Adem\xc3\xa1s, WDIG puede enviar por correo electr\xc3\xb3nico a los visitantes promociones de parte de otros patrocinadores. En estos casos, no compartimos su nombre con dichos patrocinadores; lo que hacemos es enviarle los mensajes en su nombre. \xc3\x9anicamente le enviaremos estas promociones si nos ha autorizado para ello.\n\nColaboradores de contenido\nEn algunos de nuestros sitios web ofrecemos contenido creado por un sitio web de un colaborador externo. Por ejemplo, ESPN.com ofrece oportunidades de compra en empresas de terceros. En algunos casos, los sitos web de terceros solicitan informaci\xc3\xb3n con el fin de realizar la transacci\xc3\xb3n o para que el uso de su contenido resulte m\xc3\xa1s productivo y eficaz. En estos casos, la informaci\xc3\xb3n que se recoge se comparte entre WDIG y los patrocinadores externos.\n\nAnunciadores externos y anunciadores de la red\nCon el fin de aumentar la protecci\xc3\xb3n de la intimidad de nuestros visitantes, WDIG s\xc3\xb3lo permite anunciarse en nuestros sitios web a empresas que tienen sus propias normas de confidencialidad. Cuando se hace clic en un anuncio y se abandonan los sitios web de WDIG, nuestras normas de confidencialidad dejan de ser aplicables. Debe leer las normas de confidencialidad de la empresa anunciada para saber c\xc3\xb3mo se tratar\xc3\xa1 su informaci\xc3\xb3n personal en su sitio web.\n',
    '\nAdem\xc3\xa1s, en nuestro sitio web existen muchos anuncios comerciales gestionados y publicados por empresas externas. Estas empresas reciben el nombre de "anunciadores de la red". Los anunciadores de la red recogen informaci\xc3\xb3n de car\xc3\xa1cter no personal cuando se hace clic en sus b\xc3\xa1ners, y en ocasiones, cuando se pasa por encima con el rat\xc3\xb3n. La informaci\xc3\xb3n se obtiene por medio de dispositivos tecnol\xc3\xb3gicos, por lo que es posible que no se d\xc3\xa9 cuenta de que est\xc3\xa1 siendo recogida. Los anunciadores de la red recogen esta informaci\xc3\xb3n para mostrarle despu\xc3\xa9s anuncios que pueden resultarle m\xc3\xa1s interesantes. Si desea obtener m\xc3\xa1s informaci\xc3\xb3n sobre los anunciadores de la red o no desea que recojan este tipo de informaci\xc3\xb3n de car\xc3\xa1cter no personal sobre usted, haga clic aqu\xc3\xad.\n\nCompra y venta de negocios\nLos negocios en l\xc3\xadnea se encuentran todav\xc3\xada en una etapa muy temprana, pero est\xc3\xa1n cambiando y evolucionando con mucha rapidez. Como WDIG busca continuamente formas de mejorar nuestro negocio, se puede dar el caso de que compremos o vendamos una empresa. Si compramos o vendemos un negocio, es probable que los nombres recogidos se transfieran como parte de la venta. La informaci\xc3\xb3n sobre las personas registradas se utilizar\xc3\xa1 en la sociedad constituida. Sin embargo, si compramos un negocio, satisfaremos los deseos de sus clientes en lo que se refiere a comunicaciones por correo electr\xc3\xb3nico. En caso de que vendamos un negocio, haremos todo lo que est\xc3\xa9 a nuestro alcance para garantizar que se cumplan las peticiones de comunicaciones por correo electr\xc3\xb3nico que nos confi\xc3\xb3.\n\nOrganizaciones que ayudan a proteger y salvaguardar la seguridad de nuestros visitantes y nuestros sitios web\nDivulgaremos la informaci\xc3\xb3n personal cuando la legislaci\xc3\xb3n as\xc3\xad lo requiera, por ejemplo, en cumplimiento de un requerimiento judicial o una c\xc3\xa9dula de citaci\xc3\xb3n; para hacer cumplir nuestras Cl\xc3\xa1usulas de servicio o las normas del sitio web o de los juegos; o para proteger y salvaguardar la seguridad de los visitantes y de nuestros sitios web.\n',
    '\nP4 \xc2\xbfQu\xc3\xa9 opciones tiene el cliente en lo relativo a la informaci\xc3\xb3n recogida, utilizada y compartida por WDIG?\n\nPuede utilizar gran parte de nuestro sitio web sin darnos ning\xc3\xban tipo de informaci\xc3\xb3n de identificaci\xc3\xb3n personal. Cuando se registre con nosotros o nos proporcione informaci\xc3\xb3n de identificaci\xc3\xb3n personal, tendr\xc3\xa1 la oportunidad de restringir las comunicaciones por correo electr\xc3\xb3nico de WDIG y de nuestros colaboradores externos. Puede solicitar en cualquier momento que WDIG deje de enviarle m\xc3\xa1s mensajes de correo electr\xc3\xb3nico, bien cancelando su suscripci\xc3\xb3n a dicha comunicaci\xc3\xb3n, bien poni\xc3\xa9ndose en contacto con nosotros en la direcci\xc3\xb3n memeberservices@help.go.com. Asimismo, como hemos mencionado anteriormente, existen formas de restringir la informaci\xc3\xb3n que se recoge a trav\xc3\xa9s de nuestros dispositivos tecnol\xc3\xb3gicos, aunque, en ese caso, algunas de nuestras funciones no se podr\xc3\xa1n utilizar.\n',
    '\nP5 \xc2\xbfQu\xc3\xa9 tipo de seguridad ofrece WDIG?\n\nLa importancia de la seguridad de toda la informaci\xc3\xb3n de identificaci\xc3\xb3n personal de nuestros visitantes supone nuestra mayor preocupaci\xc3\xb3n. WDIG adopta medidas t\xc3\xa9cnicas, contractuales, administrativas y f\xc3\xadsicas relacionadas con la seguridad, con el fin de proteger los datos de todos los visitantes. Cuando los visitantes proporcionan informaci\xc3\xb3n relativa a su tarjeta de cr\xc3\xa9dito, nos valemos del cifrado SSL para protegerla. Los visitantes tambi\xc3\xa9n pueden realizar varias acciones para ayudarnos a proteger la seguridad de su informaci\xc3\xb3n. Por ejemplo, no divulgue nunca su contrase\xc3\xb1a, ya que con ella se puede acceder a toda la informaci\xc3\xb3n de su cuenta. No se olvide tampoco de cerrar la sesi\xc3\xb3n de su cuenta y la ventana del navegador cuando acabe de navegar por la red, de manera que si otra persona utiliza el mismo ordenador no pueda acceder a su informaci\xc3\xb3n.\n',
    '\nP6 \xc2\xbfC\xc3\xb3mo puedo acceder a la informaci\xc3\xb3n de mi cuenta?\n\nPuede acceder a la informaci\xc3\xb3n de identificaci\xc3\xb3n personal que nos facilit\xc3\xb3 durante el proceso de registro en el Centro de opciones de cuentas, disponible en http://play.toontown.com.  Inicie una sesi\xc3\xb3n con su nombre de cuenta y la contrase\xc3\xb1a principal. En la p\xc3\xa1gina de inicio encontrar\xc3\xa1 instrucciones para poder recuperar su contrase\xc3\xb1a en caso de que la olvide.\nSi desea ponerse en contacto con nosotros, haga clic en el enlace "Contact Us" (Contacto) que aparece al pie de todas las p\xc3\xa1ginas de WDIG y seleccione "Registration/Personalization" (Registro/Personalizaci\xc3\xb3n) en el men\xc3\xba desplegable, o bien env\xc3\xadenos un mensaje de correo electr\xc3\xb3nico con informaci\xc3\xb3n que nos ayude a identificar su cuenta con el fin de que podamos ayudarle a resolver el problema.\n',
    '\nP7 \xc2\xbfCon qui\xc3\xa9n hay que ponerse contacto si surge alguna pregunta o duda sobre estas normas de confidencialidad?\n\nSi necesita m\xc3\xa1s ayuda, le rogamos que nos env\xc3\xade un mensaje de correo electr\xc3\xb3nico con sus preguntas y comentarios a memberservices@help.go.com.\nTambi\xc3\xa9n puede escribirnos por correo ordinario a:\n\nMember Services\nWalt Disney Internet Group\n506 2nd Avenue\nSuite 2100\nSeattle, WA 98104, Estados Unidos\n\nWalt Disney Internet Group es licenciatario del TRUSTe Privacy Program. Si considera que WDIG no ha contestado a su pregunta o no la ha enfocado de la forma deseada, le rogamos que se ponga en contacto con el programa TRUSTe en http://www.truste.org/users/users_watchdog.html.\n*Para llamar a este tel\xc3\xa9fono es necesario tener 18 a\xc3\xb1os de edad o contar con el permiso de los padres o el tutor.\n',
    '\nNormas de confidencialidad para ni\xc3\xb1os\nSomos conscientes de la necesidad de ofrecer servicios adicionales de protecci\xc3\xb3n de los datos personales de los ni\xc3\xb1os que visitan nuestros sitios web.\n\nP1 \xc2\xbfQu\xc3\xa9 tipo de informaci\xc3\xb3n recogen los sitios web de WDIG sobre los ni\xc3\xb1os que tienen 12 a\xc3\xb1os o menos?\n\nLos ni\xc3\xb1os pueden navegar por Disney.com u otros sitios web de WDIG, ver distintos contenidos y jugar a algunos juegos sin que se recoja ning\xc3\xban tipo de informaci\xc3\xb3n de identificaci\xc3\xb3n personal. Adem\xc3\xa1s, espor\xc3\xa1dicamente alojamos salas de conversaci\xc3\xb3n moderadas en las que no se solicita ni se hace p\xc3\xbablica informaci\xc3\xb3n de identificaci\xc3\xb3n personal de ning\xc3\xban tipo. No obstante, en algunas zonas es necesario recoger informaci\xc3\xb3n de identificaci\xc3\xb3n personal de los ni\xc3\xb1os para permitir la participaci\xc3\xb3n en ciertas actividades (como, por ejemplo, un concurso) o para comunicarse con nuestra comunidad (por correo electr\xc3\xb3nico o tablones de mensajes).\n\nEn WDIG no consideramos adecuado recoger m\xc3\xa1s informaci\xc3\xb3n de identificaci\xc3\xb3n personal de ni\xc3\xb1os de 12 a\xc3\xb1os o menores que la necesaria para que puedan participar en nuestras actividades en l\xc3\xadnea. Adem\xc3\xa1s, se debe tener en cuenta que los sitios web que est\xc3\xa1n dirigidos a ni\xc3\xb1os de 12 a\xc3\xb1os y menores no pueden, por ley, solicitar m\xc3\xa1s informaci\xc3\xb3n de la necesaria.\n\nLa \xc3\xbanica informaci\xc3\xb3n de identificaci\xc3\xb3n personal que recogemos de los ni\xc3\xb1os es el nombre, la fecha de nacimiento y la direcci\xc3\xb3n de correo electr\xc3\xb3nico de los padres. La fecha de nacimiento se recoge para comprobar la edad de los visitantes. Tambi\xc3\xa9n podemos solicitar informaci\xc3\xb3n personal, como por ejemplo el nombre de un animal dom\xc3\xa9stico, para recordar a los visitantes su nombre de inicio de sesi\xc3\xb3n y su ',
    '\ncontrase\xc3\xb1a en caso de que los olviden.\n\nTambi\xc3\xa9n permitimos a los padres solicitar, cuando lo estimen oportuno, la supresi\xc3\xb3n de nuestra base de datos de toda la informaci\xc3\xb3n que figura sobre sus hijos. Si desea desactivar la cuenta de su hijo, le rogamos que nos lo solicite por medio de un mensaje dirigido a ms_support@help.go.com en el que consten el nombre de inicio de sesi\xc3\xb3n y la contrase\xc3\xb1a del ni\xc3\xb1o.\n\nP2 \xc2\xbfC\xc3\xb3mo utiliza y comparte WDIG la informaci\xc3\xb3n de identificaci\xc3\xb3n personal que recabada?\n\nNing\xc3\xban dato sobre los visitantes de 12 a\xc3\xb1os o menores se utiliza con ning\xc3\xban fin de marketing ni promocional, ni dentro ni fuera de la familia de sitios web del Walt Disney Internet Group.\nLos sitios web de WDIG s\xc3\xb3lo utilizan los datos recogidos sobre los ni\xc3\xb1os de 12 a\xc3\xb1os o menores para ofrecer servicios (como por ejemplo calendarios) o para llevar a cabo algunos juegos o concursos. A pesar de que los visitantes de 12 a\xc3\xb1os y menores pueden participar en algunos concursos en los que se recoge informaci\xc3\xb3n, las notificaciones y los premios se env\xc3\xadan a la direcci\xc3\xb3n de correo electr\xc3\xb3nico de los padres o tutores que se proporcion\xc3\xb3 durante el proceso de registro inicial. No se publican el nombre completo, la edad ni las fotos de los ganadores de los concursos para ni\xc3\xb1os de 12 a\xc3\xb1os o menores sin el consentimiento de los padres o el tutor. En ocasiones se publica una forma inidentificable del nombre del ni\xc3\xb1o. En esos casos, es posible que no nos volvamos a poner en contacto con los padres para pedirles permiso.\n\nNo permitimos a los ni\xc3\xb1os de 12 a\xc3\xb1os y menores participar en salas de conversaci\xc3\xb3n sin moderador.\n\n',
    '\nFacilitaremos la informaci\xc3\xb3n personal sobre los ni\xc3\xb1os cuando la legislaci\xc3\xb3n as\xc3\xad lo requiera, por ejemplo, en cumplimiento de un requerimiento judicial o c\xc3\xa9dula de citaci\xc3\xb3n; para hacer cumplir nuestras Cl\xc3\xa1usulas de servicio, o las normas del sitio web o de los juegos; o para proteger y salvaguardar la seguridad de los visitantes y de nuestros sitios web.\n\nP3 \xc2\xbfSe ocupa WDIG de informar a los padres sobre la recogida de informaci\xc3\xb3n de ni\xc3\xb1os de 12 a\xc3\xb1os o menores?\n\nSiempre que un ni\xc3\xb1o de 12 a\xc3\xb1os o menor se registre en nuestro servicio, se lo notificaremos por correo electr\xc3\xb3nico a sus padres o a su tutor. Adem\xc3\xa1s, solicitamos a los padres que otorguen un permiso expl\xc3\xadcito para permitir a sus hijos utilizar el correo electr\xc3\xb3nico, los tableros de mensajes y otras funciones a trav\xc3\xa9s de las cuales se puede hacer p\xc3\xbablica la informaci\xc3\xb3n de identificaci\xc3\xb3n personal en Internet y compartirla con usuarios de todas las edades.\nTambi\xc3\xa9n damos a los padres un plazo de 48 horas para rechazar cualquier registro que sus hijos hayan efectuado para jugar a juegos y concursos. Si no recibimos ning\xc3\xban mensaje en contra, damos por supuesto que no hay ning\xc3\xban problema en que el ni\xc3\xb1o est\xc3\xa9 registrado en el servicio. Cuando el ni\xc3\xb1o se haya registrado, podr\xc3\xa1 acceder a cualquier juego y concurso que requiera inscripci\xc3\xb3n, pero no se lo volveremos a notificar a sus padres. En este caso, utilizamos la informaci\xc3\xb3n recogida \xc3\xbanicamente para comunicar a los padres si un ni\xc3\xb1o ha ganado un juego o concurso. No utilizamos esta informaci\xc3\xb3n con ning\xc3\xban otro fin.\n',
    '\nP4 \xc2\xbfC\xc3\xb3mo pueden acceder los padres a la informaci\xc3\xb3n de sus hijos?\n\nExisten tres formas de revisar la informaci\xc3\xb3n que se ha recogido sobre los ni\xc3\xb1os de 12 a\xc3\xb1os o menores.\n\nCuando los padres proporcionan a sus hijos el acceso a funciones interactivas, como los tableros de mensajes, se les solicita que configuren una cuenta familiar. Cuando la cuenta familiar se encuentre en funcionamiento, el titular de la cuenta principal podr\xc3\xa1 revisar la informaci\xc3\xb3n de identificaci\xc3\xb3n personal de todas las cuentas de los socios de la familia, incluidas las de los ni\xc3\xb1os. Para acceder a esta informaci\xc3\xb3n, inicie una sesi\xc3\xb3n en su cuenta familiar en la p\xc3\xa1gina de inicio Your Account (Su cuenta).\n\nSi todav\xc3\xada no es socio de un sitio web de WDIG, para revisar la informaci\xc3\xb3n de identificaci\xc3\xb3n personal de su hijo inicie una sesi\xc3\xb3n de su cuenta en la p\xc3\xa1gina de inicio Account Options (Opciones de cuenta). Deber\xc3\xa1 tener el nombre de cuenta y la contrase\xc3\xb1a de su hijo. En la p\xc3\xa1gina de inicio Your Account (Su cuenta) encontrar\xc3\xa1 instrucciones para poder recuperar la contrase\xc3\xb1a de su hijo en caso de que la olvide.\n\nTambi\xc3\xa9n puede ponerse en contacto con el Servicio de atenci\xc3\xb3n al cliente para ver la informaci\xc3\xb3n que se ha recogido de su hijo mediante un mensaje dirigido a ms_support@help.go.com. Si todav\xc3\xada no ha establecido una cuenta familiar, deber\xc3\xa1 tener el nombre de usuario y la contrase\xc3\xb1a de su hijo. Le rogamos que incluya en el mensaje de correo electr\xc3\xb3nico datos (nombre de cuenta del ni\xc3\xb1o, direcci\xc3\xb3n de correo electr\xc3\xb3nico de los padres) que nos permitan identificar la cuenta de su hijo, con el fin de que podamos ayudarle a resolver el problema.\n',
    '\nP5 \xc2\xbfQu\xc3\xa9 tipo de seguridad ofrece WDIG?\n\nLa importancia de la seguridad de toda la informaci\xc3\xb3n de identificaci\xc3\xb3n personal de nuestros visitantes supone nuestra mayor preocupaci\xc3\xb3n. WDIG adopta medidas t\xc3\xa9cnicas, contractuales, administrativas y f\xc3\xadsicas relacionadas con la seguridad, con el fin de proteger los datos de todos los visitantes. Cuando los visitantes proporcionan informaci\xc3\xb3n relativa a su tarjeta de cr\xc3\xa9dito, nos valemos del cifrado SSL para protegerla. Los visitantes tambi\xc3\xa9n pueden realizar varias acciones para ayudarnos a proteger la seguridad de su informaci\xc3\xb3n. Por ejemplo, no divulgue nunca su contrase\xc3\xb1a, ya que con ella se puede acceder a toda la informaci\xc3\xb3n de su cuenta. No se olvide tampoco de cerrar la sesi\xc3\xb3n de su cuenta y la ventana del navegador cuando acabe de navegar por la red, de manera que si otra persona utiliza el mismo ordenador no pueda acceder a su informaci\xc3\xb3n.\n',
    '\nP6 \xc2\xbfC\xc3\xb3mo se enteran los padres si WDIG modifica estas normas de confidencialidad?\n\nSi WDIG modifica estas normas de confidencialidad, se lo notificaremos a los padres por correo electr\xc3\xb3nico.\n\nP7 \xc2\xbf Con qui\xc3\xa9n hay que ponerse contacto si surge alguna pregunta o duda sobre estas normas de confidencialidad?\n\nSi necesita m\xc3\xa1s ayuda, le rogamos que env\xc3\xade un mensaje de correo electr\xc3\xb3nico con sus preguntas o comentarios a ms_support@help.go.com.\nTambi\xc3\xa9n puede escribirnos por correo ordinario a:\n\nMember Services\nWalt Disney Internet Group\n506 2nd Avenue\nSuite 2100\nSeattle, WA 98104, Estados Unidos\nO llamarnos por tel\xc3\xa9fono al n\xc3\xbamero 00 (1) (509) 742-4698.\n\nWalt Disney Internet Group es licenciatario del TRUSTe Privacy Program. Si considera que WDIG no ha contestado a su pregunta o no la ha enfocado de la forma deseada, le rogamos que se ponga en contacto con el programa TRUSTe en http://www.truste.org/users/users_watchdog.html.\n*Para llamar a este tel\xc3\xa9fono es necesario tener 18 a\xc3\xb1os de edad o contar con el permiso de los padres o el tutor.\n']
BillingScreenCountryNames = {
    'US': 'Estados Unidos de Am\xc3\xa9rica',
    'CA': 'Canad\xc3\xa1',
    'AF': 'Afganist\xc3\xa1n',
    'AL': 'Albania',
    'DZ': 'Argelia',
    'AS': 'Samoa estadounidense',
    'AD': 'Andorra',
    'AO': 'Angola',
    'AI': 'Anguilla',
    'AQ': 'Ant\xc3\xa1rtida',
    'AG': 'Antigua y Barbuda',
    'AR': 'Argentina',
    'AM': 'Armenia',
    'AW': 'Aruba',
    'AU': 'Australia',
    'AT': 'Austria',
    'AZ': 'Azerbaiy\xc3\xa1n',
    'BS': 'Bahamas',
    'BH': 'Bahr\xc3\xa9in',
    'BD': 'Bangladesh',
    'BB': 'Barbados',
    'BY': 'Bielorrusia',
    'BE': 'B\xc3\xa9lgica',
    'BZ': 'Belice',
    'BJ': 'Ben\xc3\xadn',
    'BM': 'Bermudas',
    'BT': 'But\xc3\xa1n',
    'BO': 'Bolivia',
    'BA': 'Bosnia y Herzegovina',
    'BW': 'Botsuana',
    'BV': 'Isla de Bouvet',
    'BR': 'Brasil',
    'IO': 'Territorio oce\xc3\xa1nico de las Indias Brit\xc3\xa1nicas',
    'BN': 'Brun\xc3\xa9i Darussalam',
    'BG': 'Bulgaria',
    'BF': 'Burkina Faso',
    'BI': 'Burundi',
    'KH': 'Camboya',
    'CM': 'Camer\xc3\xban',
    'CV': 'Cabo Verde',
    'KY': 'Islas Caim\xc3\xa1n',
    'CF': 'Rep\xc3\xbablica Centroafricana',
    'TD': 'Chad',
    'CL': 'Chile',
    'CN': 'China',
    'CX': 'Isla de Navidad',
    'CC': 'Islas Cocos',
    'CO': 'Colombia',
    'KM': 'Comoras',
    'CG': 'Congo',
    'CK': 'Islas Cook ',
    'CR': 'Costa Rica',
    'CI': 'Costa de Marfil',
    'HR': 'Croacia',
    'CU': 'Cuba',
    'CY': 'Chipre',
    'CZ': 'Rep\xc3\xbablica Checa',
    'CS': 'Checoslovaquia (anteriormente)',
    'DK': 'Dinamarca',
    'DJ': 'Yibuti',
    'DM': 'Dominica',
    'DO': 'Rep\xc3\xbablica Dominicana',
    'TP': 'Timor Oriental',
    'EC': 'Ecuador',
    'EG': 'Egipto',
    'SV': 'El Salvador',
    'GQ': 'Guinea Ecuatorial',
    'ER': 'Eritrea',
    'EE': 'Estonia',
    'ET': 'Etiop\xc3\xada',
    'FK': 'Islas Malvinas',
    'FO': 'Islas Feroe',
    'FJ': 'Fiyi',
    'FI': 'Finlandia',
    'FR': 'Francia',
    'FX': 'Francia (Europa)',
    'GF': 'Guyana Francesa',
    'PF': 'Polinesia Francesa',
    'TF': 'Territorios franceses de los Mares del Sur',
    'GA': 'Gab\xc3\xb3n',
    'GM': 'Gambia',
    'GE': 'Georgia',
    'DE': 'Alemania',
    'GH': 'Ghana',
    'GI': 'Gibraltar',
    'GB': 'Reino Unido',
    'GR': 'Grecia',
    'GL': 'Groenlandia',
    'GD': 'Isla de Granada',
    'GP': 'Guadalupe',
    'GU': 'Guam',
    'GT': 'Guatemala',
    'GN': 'Guinea',
    'GW': 'Guinea-Bissau',
    'GY': 'Guyana',
    'HT': 'Hait\xc3\xad',
    'HM': 'Islas Heard y McDonald',
    'HN': 'Honduras',
    'HK': 'Hong Kong',
    'HU': 'Hungr\xc3\xada',
    'IS': 'Islandia',
    'IN': 'India',
    'ID': 'Indonesia',
    'IR': 'Ir\xc3\xa1n',
    'IQ': 'Irak',
    'IE': 'Irlanda',
    'IL': 'Israel',
    'IT': 'Italia',
    'JM': 'Jamaica',
    'JP': 'Jap\xc3\xb3n',
    'JO': 'Jordania',
    'KZ': 'Kazajst\xc3\xa1n',
    'KE': 'Kenia',
    'KI': 'Kiribati',
    'KP': 'Corea del Norte',
    'KR': 'Corea del Sur',
    'KW': 'Kuwait',
    'KG': 'Kirguist\xc3\xa1n',
    'LA': 'Laos',
    'LV': 'Letonia',
    'LB': 'L\xc3\xadbano',
    'LS': 'Lesoto',
    'LR': 'Liberia',
    'LY': 'Libia',
    'LI': 'Liechtenstein',
    'LT': 'Lituania',
    'LU': 'Luxemburgo',
    'MO': 'Macao',
    'MK': 'Macedonia',
    'MG': 'Madagascar',
    'MW': 'Malawi',
    'MY': 'Malasia',
    'MV': 'Maldivas',
    'ML': 'Mal\xc3\xad',
    'MT': 'Malta',
    'MH': 'Islas Marshall',
    'MQ': 'Martinica',
    'MR': 'Mauritania',
    'MU': 'Mauricio',
    'YT': 'Mayotte',
    'MX': 'M\xc3\xa9xico',
    'FM': 'Micronesia',
    'MD': 'Moldavia',
    'MC': 'M\xc3\xb3naco',
    'MN': 'Mongolia',
    'MS': 'Montserrat',
    'MA': 'Marruecos',
    'MZ': 'Mozambique',
    'MM': 'Myanmar',
    'NA': 'Namibia',
    'NR': 'Nauru',
    'NP': 'Nepal',
    'NL': 'Pa\xc3\xadses Bajos',
    'AN': 'Antillas Holandesas',
    'NT': 'Zona neutral',
    'NC': 'Nueva Caledonia',
    'NZ': 'Nueva Zelanda',
    'NI': 'Nicaragua',
    'NE': 'N\xc3\xadger',
    'NG': 'Nigeria',
    'NU': 'Niue',
    'NF': 'Isla Norfolk',
    'MP': 'Islas Marianas Septentrionales',
    'NO': 'Noruega',
    'OM': 'Om\xc3\xa1n',
    'PK': 'Pakist\xc3\xa1n',
    'PW': 'Pal\xc3\xa1u',
    'PA': 'Panam\xc3\xa1',
    'PG': 'Papua Nueva Guinea',
    'PY': 'Paraguay',
    'PE': 'Per\xc3\xba',
    'PH': 'Filipinas',
    'PN': 'Pitcairn',
    'PL': 'Polonia',
    'PT': 'Portugal',
    'PR': 'Puerto Rico',
    'QA': 'Qatar',
    'RE': 'Reuni\xc3\xb3n',
    'RO': 'Ruman\xc3\xada',
    'RU': 'Federaci\xc3\xb3n Rusa',
    'RW': 'Ruanda',
    'GS': 'Islas Meridionales de Georgia y Sandwich',
    'KN': 'Saint Kitts y Nevis',
    'LC': 'Santa Luc\xc3\xada',
    'VC': 'San Vicente y las Granadinas',
    'WS': 'Samoa',
    'SM': 'San Marino',
    'ST': 'Santo Tom\xc3\xa9 y Pr\xc3\xadncipe',
    'SA': 'Arabia Saud\xc3\xad ',
    'SN': 'Senegal',
    'SC': 'Seychelles',
    'SL': 'Sierra Leona',
    'SG': 'Singapur',
    'SK': 'Rep\xc3\xbablica Eslovaca',
    'SI': 'Eslovenia',
    'Sb': 'Islas Salom\xc3\xb3n',
    'SO': 'Somalia',
    'ZA': 'Rep\xc3\xbablica Sudafricana',
    'ES': 'Espa\xc3\xb1a',
    'LK': 'Sri Lanka',
    'SH': 'Santa Elena',
    'PM': 'St. Pierre y Miquelon',
    'SD': 'Sud\xc3\xa1n',
    'SR': 'Surinam',
    'SJ': 'Islas Svalbard y Jan Mayen',
    'SZ': 'Suazilandia',
    'SE': 'Suecia',
    'CH': 'Suiza',
    'SY': 'Siria',
    'TW': 'Taiw\xc3\xa1n',
    'TJ': 'Tayikist\xc3\xa1n',
    'TZ': 'Tanzania',
    'TH': 'Tailandia',
    'TG': 'Togo',
    'TK': 'Tokelau',
    'TO': 'Tonga',
    'TT': 'Trinidad y Tobago',
    'TN': 'T\xc3\xbanez',
    'TR': 'Turqu\xc3\xada',
    'TM': 'Turkmenist\xc3\xa1n',
    'TC': 'Islas Turks y Caicos',
    'TV': 'Tuvalu',
    'UG': 'Uganda',
    'UA': 'Ucrania',
    'AE': 'Emiratos \xc3\x81rabes Unidos',
    'UK': 'Reino Unido',
    'UY': 'Uruguay',
    'UM': 'Islas adyacentes a los EE.UU.',
    'SU': 'URSS (anteriormente)',
    'UZ': 'Uzbekist\xc3\xa1n',
    'VU': 'Vanuatu',
    'VA': 'Ciudad del Vaticano',
    'VE': 'Venezuela',
    'VN': 'Vietnam',
    'VG': 'Islas V\xc3\xadrgenes Brit\xc3\xa1nicas',
    'VI': 'Islas V\xc3\xadrgenes Estadounidenses',
    'WF': 'Islas Wallis y Futuna',
    'EH': 'Sahara Occideental',
    'YE': 'Yemen',
    'YU': 'Yugoslavia',
    'ZR': 'Zaire',
    'ZM': 'Zambia',
    'ZW': 'Zimbabue' }
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
    'HI': 'Hawai',
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
    'MI': 'M\xc3\xadchigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MS': 'Misisipi',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NC': 'Carolina del Norte',
    'ND': 'Dakota del Norte ',
    'NH': 'Nuevo Hampshire',
    'NJ': 'Nueva Jersey',
    'NM': 'Nuevo M\xc3\xa9xico',
    'NV': 'Nevada',
    'NY': 'Nueva York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oreg\xc3\xb3n',
    'PA': 'Pensilvania',
    'RI': 'Rhode Island',
    'SC': 'Carolina del Sur ',
    'SD': 'Dakota del Sur ',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'Virginia Occidental',
    'WY': 'Wyoming',
    'DC': 'Distrito de Columbia',
    'AS': 'Samoa estadounidense',
    'GU': 'Guam',
    'MP': 'Islas Marianas Septentrionales',
    'PR': 'Puerto Rico',
    'VI': 'Islas V\xc3\xadrgenes Estadounidenses',
    'FPO': [
        'Isla de Midway',
        'Arrecife Kingman'],
    'APO': [
        'Isla Wake',
        'Isla Johnston'],
    'MH': 'Islas Marshall',
    'PW': 'Pal\xc3\xa1u',
    'FM': 'Micronesia' }
BillingScreenCanadianProvinces = {
    'AB': 'Alberta',
    'BC': 'Columbia Brit\xc3\xa1nica',
    'MB': 'Manitoba',
    'NB': 'Nueva Brunswick',
    'NF': 'Newfoundland',
    'NT': 'Territorios del Noroeste',
    'NS': 'Nueva Escocia',
    'ON': 'Ontario',
    'PE': 'Isla Prince Edward',
    'QC': 'Qu\xc3\xa9bec',
    'SK': 'Saskatchewan',
    'YT': 'Yukon' }
ParentPassword = 'Contrase\xc3\xb1a parental'
WelcomeScreenHeading = '\xc2\xa1Bienvenido!'
WelcomeScreenOk = '\xc2\xa1VAMOS A JUGAR!'
WelcomeScreenSentence1 = 'Ahora eres socio oficial de'
WelcomeScreenToontown = "Disney's Toontown Online"
WelcomeScreenSentence2 = "No te olvides de buscar m\xc3\xa1s adelante en el correo electr\xc3\xb3nico las sorprendentes noticias sobre Disney's Toontown Online."
TTAccountCallCustomerService = 'Para ponerte en contacto con el Servicio de atenci\xc3\xb3n al cliente, llama al %s.'
TTAccountCustomerServiceHelp = '\n\nSi necesitas ayuda, ponte en contacto con el Servicio de atenci\xc3\xb3n al cliente, en el n\xc3\xbamero %s.'
TTAccountIntractibleError = 'Se ha producido un error.'
LoginScreenUserName = 'Nombre de la cuenta'
LoginScreenPassword = 'Contrase\xc3\xb1a'
LoginScreenLogin = 'Inicio de sesi\xc3\xb3n'
LoginScreenCreateAccount = 'Crear cuenta'
LoginScreenForgotPassword = '\xc2\xbfHas olvidado la contrase\xc3\xb1a?'
LoginScreenQuit = 'Salir'
LoginScreenLoginPrompt = 'Introduce un nombre de usuario y una contrase\xc3\xb1a.'
LoginScreenBadPassword = 'Contrase\xc3\xb1a incorrecta.\nInt\xc3\xa9ntalo de nuevo.'
LoginScreenInvalidUserName = 'Nombre de usuario incorrecto.\nInt\xc3\xa9ntalo de nuevo.'
LoginScreenUserNameNotFound = 'No se ha encontrado el nombre de usuario.\nInt\xc3\xa9ntalo de nuevo o crea otra cuenta.'
LoginScreenPeriodTimeExpired = 'Lo sentimos, pero ya has gastado todos los minutos de que dispon\xc3\xadas en Toontown este mes.  Vuelve a principios del mes que viene.'
LoginScreenNoNewAccounts = 'Lo sentimos mucho, pero no aceptamos nuevas cuentas en este momento.'
LoginScreenTryAgain = 'Int\xc3\xa9ntalo de nuevo'
NewPlayerScreenNewAccount = 'Empezar prueba gratuita'
NewPlayerScreenLogin = 'Socio Activo'
NewPlayerScreenQuit = 'Salir'
FreeTimeInformScreenDontForget = 'No te olvides de que tu prueba gratuita\ncaducar\xc3\xa1 en '
FreeTimeInformScreenNDaysLeft = FreeTimeInformScreenDontForget + '\xc2\xa1s\xc3\xb3lo %s d\xc3\xadas!'
FreeTimeInformScreenOneDayLeft = FreeTimeInformScreenDontForget + '\xc2\xa1un d\xc3\xada!'
FreeTimeInformScreenNHoursLeft = FreeTimeInformScreenDontForget + '\xc2\xa1s\xc3\xb3lo %s horas!'
FreeTimeInformScreenOneHourLeft = FreeTimeInformScreenDontForget + '\xc2\xa1una hora!'
FreeTimeInformScreenLessThanOneHourLeft = FreeTimeInformScreenDontForget + '\xc2\xa1menos de una hora!'
FreeTimeInformScreenSecondSentence = "Pero todav\xc3\xada tienes tiempo para hacerte\nsocio oficial de Disney's Toontown Online."
FreeTimeInformScreenOops = '\xc2\xa1VAYA!'
FreeTimeInformScreenExpired = "                 , tu prueba gratuita ha caducado.\n\xc2\xbfDeseas convertirte en socio oficial de Disney's Toontown Online?\n\xc2\xa1Inscr\xc3\xadbete ahora y divi\xc3\xa9rtete como nunca!"
FreeTimeInformScreenExpiredQuitText = '\xc2\xbfNo puedes hacerlo ahora mismo? No te preocupes, te guardaremos\nel dibu. Pero \xc2\xa1date prisa! S\xc3\xb3lo podemos\nguardarte el dibu durante una semana despu\xc3\xa9s\nde que haya caducado tu prueba gratuita.'
FreeTimeInformScreenExpiredCCUF = "Todav\xc3\xada no has adquirido Disney's\nToontown Online. Para usar esta cuenta\ndebes registrarte ahora con una tarjeta de cr\xc3\xa9dito.\n\xc2\xa1Inscr\xc3\xadbete ahora y vuelve a divertirte como nunca!"
FreeTimeInformScreenExpiredQuitCCUFText = '\xc2\xbfNo puedes hacerlo ahora mismo? No te preocupes, te guardaremos\nla cuenta. Pero \xc2\xa1date prisa! S\xc3\xb3lo podemos\nguardarte la cuenta durante una semana.'
FreeTimeInformScreenPurchase = '\xc2\xa1Suscr\xc3\xadbete ya!'
FreeTimeInformScreenFreePlay = 'Continuar prueba gratuita'
FreeTimeInformScreenQuit = 'Salir'
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
DateOfBirthEntryDefaultLabel = 'Fecha de nacimiento'
CreateAccountScreenUserName = 'Nombre de la cuenta'
CreateAccountScreenPassword = 'Contrase\xc3\xb1a'
CreateAccountScreenConfirmPassword = 'Confirmar contrase\xc3\xb1a'
CreateAccountScreenFree = 'GRATIS'
CreateAccountScreenFreeTrialLength = 'Para empezar tu prueba de           %s d\xc3\xadas\ntienes que crear una cuenta.'
CreateAccountScreenInstructionsUsername = 'Escribe el nombre de la cuenta que deseas usar:'
CreateAccountScreenInstructionsPassword = 'Escribe una contrase\xc3\xb1a:'
CreateAccountScreenInstructionsConfirmPassword = 'Para asegurarte, escribe de nuevo la contrase\xc3\xb1a:'
CreateAccountScreenInstructionsDob = 'Escribe tu fecha de nacimiento:'
CreateAccountScreenCancel = 'Cancelar'
CreateAccountScreenSubmit = 'Siguiente'
CreateAccountScreenConnectionErrorSuffix = '.\n\nVuelve a intentarlo m\xc3\xa1s tarde.'
CreateAccountScreenNoAccountName = 'Escribe un nombre de cuenta.'
CreateAccountScreenAccountNameTooShort = 'El nombre de cuenta debe tener al menos %s caracteres. Int\xc3\xa9ntalo de nuevo.'
CreateAccountScreenPasswordTooShort = 'La contrase\xc3\xb1a debe tener al menos %s caracteres. Int\xc3\xa9ntalo de nuevo.'
CreateAccountScreenPasswordMismatch = 'Las contrase\xc3\xb1as que has escrito no coinciden. Int\xc3\xa9ntalo de nuevo.'
CreateAccountScreenInvalidDob = 'Escribe tu fecha de nacimiento.'
CreateAccountScreenUserNameTaken = 'Ese nombre de usuario ya existe. Int\xc3\xa9ntalo de nuevo.'
CreateAccountScreenInvalidUserName = 'Nombre de usuario no v\xc3\xa1lido.\nInt\xc3\xa9ntalo de nuevo.'
CreateAccountScreenUserNameNotFound = 'No se ha encontrado el nombre de usuario.\nInt\xc3\xa9ntalo de nuevo o crea otra cuenta.'
CreateAccountScreenEmailInstructions = "Escribe tu direcci\xc3\xb3n de correo electr\xc3\xb3nico.\n\xc2\xbfPor qu\xc3\xa9? Por dos razones:\n1. Si olvidas la contrase\xc3\xb1a, te la podremos enviar.\n2. Podemos enviarte la informaci\xc3\xb3n m\xc3\xa1s reciente\nsobre Disney's Toontown Online."
CreateAccountScreenEmailInstructionsUnder13 = 'Has indicado que tienes menos de 13 a\xc3\xb1os.\nPara crear una cuenta necesitamos la direcci\xc3\xb3n de correo electr\xc3\xb3nico de tus padres o tu tutor.'
CreateAccountScreenEmailConfirm = 'Para asegurarte, escribe de nuevo la direcci\xc3\xb3n de correo electr\xc3\xb3nico.'
CreateAccountScreenEmailPanelSubmit = 'Siguiente'
CreateAccountScreenEmailPanelCancel = 'Cancelar'
CreateAccountScreenInvalidEmail = 'Escribe la direcci\xc3\xb3n de correo electr\xc3\xb3nico completa.'
CreateAccountScreenEmailMismatch = 'Las direcciones de correo electr\xc3\xb3nico que has introducido no coinciden. Int\xc3\xa9ntalo de nuevo.'
SecretFriendsInfoPanelOk = 'Aceptar'
SecretFriendsInfoPanelText = [
    '\nLa herramienta Amigos secretos\n\nLa herramienta Amigos secretos permite a los socios conversar directamente entre s\xc3\xad mediante en Disney\'s Toontown Online (en lo sucesivo, el "Servicio"). Para ello, los socios deben establecer una conexi\xc3\xb3n de Amigos secretos.  Cuando su hijo intente usar la herramienta Amigos secretos, le pediremos que introduzca su contrase\xc3\xb1a parental para confirmar su consentimiento al uso de dicha herramienta.  A continuaci\xc3\xb3n se describe con detalle proceso de creaci\xc3\xb3n de una conexi\xc3\xb3n de Amigos secretos entre dos socios imaginarios a los que llamaremos "Susana" y "Miguel".\n1. Los padres de Susana y los de Miguel activan la herramienta Amigos secretos, introduciendo sus contrase\xc3\xb1as parentales (a) en las Opciones de cuenta del Servicio o (b) cuando el juego se lo requiera en una ventana emergente de Control parental.\n',
    '\n2. Susana solicita un Secreto (descrito m\xc3\xa1s adelante) desde dentro del Servicio.\n3. El Secreto de Susana se env\xc3\xada a Miguel fuera del Servicio. (Susana le puede comunicar su Secreto a Miguel directamente o indirectamente, a trav\xc3\xa9s de otra persona.)\n4. Miguel env\xc3\xada el Secreto de Susana al Servicio en un plazo de 48 horas a partir del momento en que Susana lo ha solicitado.\n5. El Servicio comunica a Miguel que Susana se ha convertido en su amiga secreta.  De igual modo, el Servicio notifica a Susana que Miguel se ha convertido en su amigo secreto.\n6. Ahora, Susana y Miguel pueden charlar entre s\xc3\xad hasta que uno de ellos decida que el otro deje de ser su amigo secreto o hasta que los padres de Susana o Miguel desactiven la herramienta Amigos secretos.  Por tanto, la conexi\xc3\xb3n Amigos secretos puede ser desactivada en cualquier momento por:\n',
    '\n(a) Un socio que borre a otro de su lista de amigos secretos (de la forma\ndescrita en el Servicio) o (b) los padres de un socio que desactiven la herramienta Amigos secretos por medio de las Opciones de cuenta del Servicio (siguiendo los pasos all\xc3\xad establecidos).\n\nUn Secreto es un c\xc3\xb3digo inform\xc3\xa1tico generado al azar y asignado a un socio en concreto. Es necesario usar el Secreto para activar la conexi\xc3\xb3n de Amigos secretos dentro de un plazo de 48 horas a partir del momento de su solicitud. De lo contrario, el Secreto caduca y no se puede utilizar.  Adem\xc3\xa1s, un secreto s\xc3\xb3lo se puede usar para establecer una sola conexi\xc3\xb3n de Amigos Secretos.  Para crear m\xc3\xa1s conexiones de Amigos secretos, el socio debe solicitar un Secreto adicional para cada uno de los nuevos amigos.\n\nLas amistades secretas no se transfieren.  Por ejemplo, si Susana es amiga\n',
    '\nsecreta de Miguel y Miguel es amigo secreto de Ana, Susana no se convierte autom\xc3\xa1ticamente en amiga secreta de Ana.  Para que Susana y Ana se hagan\namigas secretas, una de ellas deber\xc3\xa1 solicitar un nuevo Secreto al Servicio y\ncomunic\xc3\xa1rselo a la otra.\n\nLos amigos secretos se comunican entre s\xc3\xad mediante un servicio de conversaci\xc3\xb3n interactivo de formato libre.  El contenido de esta conversaci\xc3\xb3n es escrito directamente por el socio participante y procesado a trav\xc3\xa9s del Servicio, que est\xc3\xa1 gestionado por Walt Disney Internet Group ("WDIG"), 506 2nd Avenue, Suite 2100, Seattle, WA 98104, EE.UU. (tel\xc3\xa9fono +1 (509) 742-4698; correo electr\xc3\xb3nico: ms_support@help.go.com).  Aunque aconsejamos a los socios que no intercambien datos personales, como sus nombres y apellidos, direcciones de correo electr\xc3\xb3nico, direcciones postales o n\xc3\xbameros de tel\xc3\xa9fono mientras utilizan la herramienta Amigos secretos, no\n',
    '\npodemos garantizar que tales intercambios de informaci\xc3\xb3n personal no se produzcan. Aunque el servicio de conversaci\xc3\xb3n de Amigos secretos tiene un filtro autom\xc3\xa1tico de palabras malsonantes y obscenas, no est\xc3\xa1 moderado ni  supervisado por nosotros.  Si los padres permiten a sus hijos usar su cuenta con la opci\xc3\xb3n Amigos secretos activada, les aconsejamos que los supervisen mientras juegan en el Servicio..\n\nWDIG no hace uso del contenido de las conversaciones de Amigos secretos para ning\xc3\xban otro prop\xc3\xb3sito que no sea el de comunicar dicho contenido al amigo secreto del socio, y no divulga ese contenido a terceros excepto en los siguientes casos: (1) Si la ley lo requiere, por ejemplo, para acatar una orden o citaci\xc3\xb3n judicial; (2) para hacer cumplir las Condiciones de uso aplicables al Servicio (a las que se puede acceder en la p\xc3\xa1gina principal del Servicio); (3) para proteger la seguridad de los socios del Servicio y del Servicio mismo.  \n',
    "\nLos padres de un ni\xc3\xb1o pueden, previa petici\xc3\xb3n a WDIG, revisar y borrar el contenido de cualquier conversaci\xc3\xb3n mantenida por ese ni\xc3\xb1o, suponiendo que dicho contenido no haya sido ya borrado por WDIG de sus archivos.  Seg\xc3\xban lo estipulado en la Ley estadounidense para la protecci\xc3\xb3n del menor en medios electr\xc3\xb3nicos (Children's Online Privacy Protection Act), no estamos autorizados a condicionar la participaci\xc3\xb3n de un ni\xc3\xb1o en ninguna actividad (lo que incluye Amigos secretos) en base a la revelaci\xc3\xb3n por parte del ni\xc3\xb1o de m\xc3\xa1s informaci\xc3\xb3n personal de la razonablemente necesaria para participar en tal actividad.\n\nAdem\xc3\xa1s, tal y como se menciona anteriormente, reconocemos el derecho de los padres a negarse a permitir que el ni\xc3\xb1o siga utilizando la herramienta Amigos secretos. Al activar la herramienta Amigos secretos, los padres reconocen que existen ciertos riesgos inherentes a la posibilidad de charlar de los socios por medio de dicha herramienta, y reconocen que han sido informados sobre dichos riesgos y est\xc3\xa1n de acuerdo en aceptarlos.\n"]
ParentPasswordScreenTitle = 'Controles parentales'
ParentPasswordScreenPassword = 'Crear contrase\xc3\xb1a parental'
ParentPasswordScreenConfirmPassword = 'Confirmar contrase\xc3\xb1a parental'
ParentPasswordScreenSubmit = 'Establecer contrase\xc3\xb1a parental'
ParentPasswordScreenConnectionErrorSuffix = '.\nVuelva a intentarlo m\xc3\xa1s tarde.'
ParentPasswordScreenPasswordTooShort = 'La contrase\xc3\xb1a debe tener al menos %s caracteres. Int\xc3\xa9ntelo de nuevo.'
ParentPasswordScreenPasswordMismatch = 'Las contrase\xc3\xb1as que ha escrito no coinciden. Int\xc3\xa9ntelo de nuevo.'
ParentPasswordScreenConnectionProblemJustPaid = 'Ha surgido un problema con la conexi\xc3\xb3n con el servidor de la cuenta, pero la adquisici\xc3\xb3n se ha procesado.\n\nLa pr\xc3\xb3xima vez que inicie una sesi\xc3\xb3n se le solicitar\xc3\xa1 que establezca la contrase\xc3\xb1a parental.'
ParentPasswordScreenConnectionProblemJustLoggedIn = 'Ha surgido un problema en la conexi\xc3\xb3n con el servidor de la cuenta. Vuelva a intentarlo m\xc3\xa1s tarde.'
ParentPasswordScreenSecretFriendsMoreInfo = 'M\xc3\xa1s informaci\xc3\xb3n'
ParentPasswordScreenInstructions = 'Cree una contrase\xc3\xb1a parental para esta cuenta.  La contrase\xc3\xb1a parental se le solicitar\xc3\xa1 m\xc3\xa1s adelante:\n\n  1.  Cuando le pidamos consentimiento para que tu hijo\n       use ciertas herramientas interactivas de Toontown\n       tales como la herramienta "Amigos secretos".  Si desea\n       una descripci\xc3\xb3n completa de la herramienta Amigos\n       secretos, que permite que sus hijos se\n       comuniquen en l\xc3\xadnea con otros socios de Toontown,\n       pulse el bot\xc3\xb3n ' + ParentPasswordScreenSecretFriendsMoreInfo + "', situado debajo. Es necesario que d\xc3\xa9 su consentimiento\n       para activar esta herramienta.\n\n\n  2. Para actualizar la informaci\xc3\xb3n sobre la facturaci\xc3\xb3n\n       y la cuenta desde la p\xc3\xa1gina web de Toontown.\n"
ParentPasswordScreenAdvice = 'Recuerde que la contrase\xc3\xb1a parental debe ser confidencial. Mantenerla a salvo es fundamental para conservar el control sobre el uso de las herramientas interactivas de la cuenta por parte de su hijo. '
ParentPasswordScreenPrivacyPolicy = 'Normas de confidencialidad'
ForgotPasswordScreenTitle = 'Si ha olvidado la contrase\xc3\xb1a, se la podemos enviar.'
ForgotPasswordScreenInstructions = 'Introduzca el nombre de su cuenta o la direcci\xc3\xb3n de correo electr\xc3\xb3nico que nos facilit\xc3\xb3.'
ForgotPasswordScreenEmailEntryLabel = 'Direcci\xc3\xb3n de correo electr\xc3\xb3nico'
ForgotPasswordScreenOr = 'O bien'
ForgotPasswordScreenAcctNameEntryLabel = 'Nombre de la cuenta'
ForgotPasswordScreenSubmit = 'Enviar'
ForgotPasswordScreenCancel = 'Cancelar'
ForgotPasswordScreenEmailSuccess = "Su contrase\xc3\xb1a ha sido enviada a '%s'."
ForgotPasswordScreenEmailFailure = "Direcci\xc3\xb3n de correo electr\xc3\xb3nico no encontrada: '%s'."
ForgotPasswordScreenAccountNameSuccess = 'Su contrase\xc3\xb1a ha sido enviada a la direcci\xc3\xb3n de correo electr\xc3\xb3nico que nos facilit\xc3\xb3 al crear la cuenta.'
ForgotPasswordScreenAccountNameFailure = 'Cuenta no encontrada: %s'
ForgotPasswordScreenNoEmailAddress = 'Esa cuenta ha sido creada por un menor de 13 a\xc3\xb1os y no tiene una direcci\xc3\xb3n de correo electr\xc3\xb3nico. No podemos enviarle la contrase\xc3\xb1a.\n\n\xc2\xa1Cree otra cuenta si lo desea!'
ForgotPasswordScreenInvalidEmail = 'Introduzca una direcci\xc3\xb3n de correo electr\xc3\xb3nico v\xc3\xa1lida.'
GuiScreenToontownUnavailable = 'Toontown no parece estar disponible por el momento, seguimos intent\xc3\xa1ndolo...'
AchievePageTitle = 'Logros\n(pr\xc3\xb3ximamente)'
BuildingPageTitle = 'Edificios\n(pr\xc3\xb3ximamente)'
InventoryPageTitle = 'Bromas'
InventoryPageDeleteTitle = 'BORRAR BROMAS'
InventoryPageTrackFull = 'Tienes todas las bromas del circuito %s. '
InventoryPagePluralPoints = 'Conseguir\xc3\xa1s una nueva\nbroma de %(trackName)s cuando\nconsigas %(numPoints)s puntos m\xc3\xa1s de %(trackName)s.'
InventoryPageSinglePoint = 'Conseguir\xc3\xa1s una nueva\nbroma de %(trackName)s cuando\nconsigas %(numPoints)s punto m\xc3\xa1s de %(trackName)s.'
InventoryPageNoAccess = 'Todav\xc3\xada no tienes acceso al circuito %s.'
MapPageBackToPlayground = 'Volver al dibuparque'
MapPageGoHome = 'Ir a casa'
MapPageYouAreHere = 'Est\xc3\xa1s en: %s\n%s'
MapPageYouAreAtHome = 'Est\xc3\xa1s en\ntu propiedad'
MapPageYouAreAtSomeonesHome = 'Est\xc3\xa1s en\nla propiedad %s'
MapPageGoTo = 'Ir a\n%s'
OptionsPageTitle = 'Opciones'
OptionsPagePurchase = '\xc2\xa1Suscr\xc3\xadbete ya!'
OptionsPageLogout = 'Cerrar sesi\xc3\xb3n'
OptionsPageExitToontown = 'Salir de Toontown'
OptionsPageMusicOnLabel = 'La m\xc3\xbasica est\xc3\xa1 activada.'
OptionsPageMusicOffLabel = 'La m\xc3\xbasica est\xc3\xa1 desactivada.'
OptionsPageSFXOnLabel = 'Los efectos de sonido est\xc3\xa1n activados.'
OptionsPageSFXOffLabel = 'Los efectos de sonido est\xc3\xa1n desactivados.'
OptionsPageFriendsEnabledLabel = 'Se aceptan solicitudes de nuevos amigos.'
OptionsPageFriendsDisabledLabel = 'No se aceptan solicitudes de nuevos amigos.'
OptionsPageDisplayWindowed = 'en ventana'
OptionsPageSelect = 'Escoger'
OptionsPageToggleOn = 'Activar'
OptionsPageToggleOff = 'Desactivar'
OptionsPageChange = 'Cambiar'
OptionsPageDisplaySettings = 'Pantalla: %(screensize)s, %(api)s'
OptionsPageDisplaySettingsNoApi = 'Pantalla: %(screensize)s'
OptionsPageExitConfirm = '\xc2\xbfQuieres salir de Toontown?'
DisplaySettingsTitle = 'Configuraci\xc3\xb3n de la pantalla'
DisplaySettingsIntro = 'Los siguientes par\xc3\xa1metros sirven para configurar el aspecto de Toontown en tu ordenador.  Lo m\xc3\xa1s probable es que no haga falta modificarlos a no ser que surja alg\xc3\xban problema.'
DisplaySettingsIntroSimple = 'Usted puede ajustar la resolucion de su pantalla a un valor m\xc3\xa1s alto, para mejorar la claridad gr\xc3\xa1fica y de texto, pero todo depende de la tarjeta gr\xc3\xa1fica, un valor m\xc3\xa1s alto puede hacer el juego menos fluido o que no trabaje del todo'
DisplaySettingsApi = 'Interfaz gr\xc3\xa1fica:'
DisplaySettingsResolution = 'Resoluci\xc3\xb3n:'
DisplaySettingsWindowed = 'En ventana'
DisplaySettingsFullscreen = 'Pantalla completa'
DisplaySettingsApply = 'Aplicar'
DisplaySettingsCancel = 'Cancelar'
DisplaySettingsApplyWarning = 'Cuando pulses Aceptar cambiar\xc3\xa1 la configuraci\xc3\xb3n gr\xc3\xa1fica.  Si la nueva configuraci\xc3\xb3n no se representa correctamente en tu ordenador, la pantalla volver\xc3\xa1 autom\xc3\xa1ticamente a la configuraci\xc3\xb3n original transcurridos %s segundos.'
DisplaySettingsAccept = 'Pulsa Aceptar para conservar la nueva configuraci\xc3\xb3n, o Cancelar para volver a la anterior.  Si no pulsas nada, se volver\xc3\xa1 a la configuraci\xc3\xb3n anterior al cabo de %s segundos.'
DisplaySettingsRevertUser = 'Se ha restablecido la configuraci\xc3\xb3n anterior de la pantalla. '
DisplaySettingsRevertFailed = 'La configuraci\xc3\xb3n de pantalla seleccionada no funciona en tu ordenador.  Se ha restablecido la configuraci\xc3\xb3n anterior de la pantalla. '
TrackPageTitle = 'Circuito Entrenador de Bromas'
TrackPageSubtitle = '\xc2\xa1Completa las dibutareas para aprender a usar las bromas nuevas!'
TrackPageTraining = 'Est\xc3\xa1s entren\xc3\xa1ndote para usar las bromas de %s.\nCuando completes las 16 tareas,\npodr\xc3\xa1s usar las bromas de %s en los combates.'
TrackPageClear = 'Ahora mismo no te est\xc3\xa1s entrenando en ning\xc3\xban circuito de bromas.'
TrackPageFilmTitle = '%s\nPel\xc3\xadcula de\nentrenamiento'
QuestPageToonTasks = 'Dibutareas'
QuestPageChoose = 'Elige'
QuestPageDestination = '%s\n%s\n%s'
QuestPageNameAndDestination = '%s\n%s\n%s\n%s'
QuestPosterHQOfficer = 'Funcionario del cuartel general'
QuestPosterHQBuildingName = 'Cuartel General Dibu'
QuestPosterHQStreetName = 'Cualquier calle'
QuestPosterHQLocationName = 'Cualquier barrio'
QuestPosterTailor = 'Sastre'
QuestPosterTailorBuildingName = 'Tienda de Ropa'
QuestPosterTailorStreetName = 'Cualquier Dibuparque'
QuestPosterTailorLocationName = 'Cualquier barrio'
QuestPosterPlayground = 'En el Dibuparque'
QuestPosterAnywhere = 'Cualquier parte'
QuestPosterAuxTo = 'hacia:'
QuestPosterAuxFrom = 'de:'
QuestPosterAuxFor = 'para:'
QuestPosterAuxOr = 'o:'
QuestPosterAuxReturnTo = 'Devuelvete\nhacia:'
QuestPosterLocationIn = ' en '
QuestPosterLocationOn = ' en '
QuestPosterFun = '\xc2\xa1Para Divertirse!'
QuestPosterFishing = 'Anda a pescar'
QuestPosterComplete = 'COMPLETADA'
ShardPageTitle = 'Distritos'
ShardPageHelp = 'Cada distrito es una copia del mundo de Toontown. Ahora mismo est\xc3\xa1s en el distrito "%s".  Para desplazarte a otro distrito, haz clic en su nombre.'
ShardPageHelpDisabled = 'Cada distrito es una copia del mundo de Toontown. Ahora mismo est\xc3\xa1s en el distrito "%s".'
ShardPagePopulationShard = 'N.\xc2\xba de habitantes de %s:\n%d'
ShardPagePopulationTotal = 'N.\xc2\xba total de habitantes de Toontown:\n%d'
ShardPageScrollTitle = 'Nombre            Habitantes'
SuitPageTitle = 'Galer\xc3\xada de bots'
SuitPageMystery = DialogQuestion + DialogQuestion + DialogQuestion
FishNames = (('Pez leopardo', 'Peces leopardo'), ('Trucha arcoiris', 'Truchas arcoiris'), ('At\xc3\xban tunante', 'Atunes tunantes'), ('Caballa de Troya', 'Caballas de Troya'), ('Palometa delapaz', 'Palometas delapaz'), ('Pargo largo', 'Pargos largos'), ('Mero casualidado', 'Meros casualidados'), ('R\xc3\xb3balo ihuye', 'R\xc3\xb3balos ihuye'), ('Perca cuelgarropa', 'Percas cuelgarropa'), ('Salmonete decara', 'Salmonetes decara'), ('Pescadilla muerdecola', 'Pescadillas muerdecola'), ('Lenguado deslenguado', 'Lenguados deslenguados'), ('Emperador destronado', 'Emperadores destronados'), ('Besugo Boss', 'Besugos Boss'), ('Bacalao hastaloshuesos', 'Bacalaos hastaloshuesos'), ('Zapato viejo', 'Zapatos viejo'), ('Neum\xc3\xa1tico viejo', 'Neum\xc3\xa1ticos viejos'))
FishPageTitle = 'Pecera'
FishPageOverflow = '\xc2\xa1Tienes demasiados peces!\n Escoge el que desees liberar:'
FishPageOldFish = 'Ya tienes:'
FishPageVerify = '\xc2\xbfSeguro que quieres liberar a %s?'
QuestChoiceGuiCancel = 'Cancelar'
TrackChoiceGuiChoose = 'Elige'
TrackChoiceGuiCancel = 'Cancelar'
TrackChoiceGuiHEAL = 'Curadibu te permite sanar a otros dibus durante el combate.'
TrackChoiceGuiTRAP = 'Las trampas son potentes bromas que se deben usar con cebos.'
TrackChoiceGuiLURE = 'los cebos permiten aturdir a los bots y atraerlos a las trampas.'
TrackChoiceGuiSOUND = 'Las bromas de sonido afectan a todos los bots, pero no son muy potentes.'
TrackChoiceGuiDROP = 'Las bromas de ca\xc3\xadda causan un mont\xc3\xb3n de da\xc3\xb1os, pero no son muy precisas.'
EmotePageTitle = 'Expresiones / Emociones'
EmotePageDance = 'Has creado la siguiente secuencia de baile:'
EmoteJump = 'Saltar'
EmoteDance = 'Bailar'
EmoteHappy = 'Feliz'
EmoteSad = 'Triste'
EmoteAnnoyed = 'Fastidiado'
EmoteSleep = 'So\xc3\xb1oliento'
EmoteList = [
    'Saludar',
    'Contento',
    'Triste',
    'Enfadado',
    'So\xc3\xb1oliento',
    'Encoger hombros',
    'Bailar',
    'Gui\xc3\xb1ar ojo',
    'Aburrido',
    'Aplaudir',
    'Sorprendido',
    'Confundido',
    'Mofarse',
    'Inclinarse',
    'Muy triste',
    'Hola',
    'Adi\xc3\xb3s',
    'S\xc3\xad',
    'No',
    'Vale']
EmoteWhispers = [
    '%s Saluda.',
    '%s esta contento.',
    '%s esta triste.',
    '%s esta enfadado.',
    '%s esta so\xc3\xb1oliento.',
    '%s se encoge de hombros.',
    '%s baila.',
    '%s gui\xc3\xb1a un ojo.',
    '%s esta aburrido.',
    '%s aplaude.',
    '%s esta sorprendido.',
    '%s esta confundido.',
    '%s se mofa de t\xc3\xad.',
    '%s te hace una reverencia.',
    '%s esta muy triste.',
    "%s dice 'Hola'.",
    "%s dice 'Adi\xc3\xb3s'.",
    "%s dice 'S\xc3\xad'.",
    "%s dice 'No'.",
    "%s dice 'Vale'."]
EmoteFuncDict = {
    'saludar': 0,
    'contento': 1,
    'triste': 2,
    'enfadado': 3,
    'so\xc3\xb1oliento': 4,
    're\xc3\xadr': 5,
    'bailar': 6,
    'gui\xc3\xb1ar ojo': 7,
    'aburrido': 8,
    'aplaudir': 9,
    'sorprendido': 10,
    'confundido': 11,
    'mofarse': 12,
    'inclinarse': 13,
    'muy triste': 14,
    'hola': 15,
    'adi\xc3\xb3s': 16,
    's\xc3\xad': 17,
    'no': 18,
    'vale': 19 }
SuitBaseNameWithLevel = '%(name)s\n%(dept)s\nNivel %(level)s'
SuitBrushOffs = {
    'f': [
        'Llego tarde a una reuni\xc3\xb3n'],
    'p': [
        'L\xc3\xa1rgate'],
    'ym': [
        'Al sonriente no le hace gracia'],
    None: [
        'Es mi d\xc3\xada libre',
        'Creo que te has equivocado de despacho',
        'Que tu secretaria llame a la m\xc3\xada',
        'No tengo tiempo para reunirme contigo',
        'Habla con mi ayudante'] }
HealthForceAcknowledgeMessage = '\xc2\xa1No puedes irte del dibuparque hasta que tu ris\xc3\xb3metro est\xc3\xa9 sonriendo!'
InventoryTotalGags = 'Bromas totales\n%d / %d'
InventoryDelete = 'BORRAR'
InventoryDone = 'HECHO'
InventoryDeleteHelp = 'Haz clic en una broma para BORRARLA.'
InventorySkillCredit = 'Habilidad: %s'
InventorySkillCreditNone = 'Habilidad: Ninguna'
InventoryDetailAmount = '%(numItems)s / %(maxItems)s'
InventoryDetailData = 'Precisi\xc3\xb3n: %(accuracy)s\n%(damageString)s: %(damage)d\n%(singleOrGroup)s'
InventoryTrackExp = '%(curExp)s / %(nextExp)s'
InventoryAffectsOneCog = 'Afecta a: Un ' + Cog
InventoryAffectsOneToon = 'Afecta a: Un dibu'
InventoryAffectsAllToons = 'Afecta a: Todos los dibus'
InventoryAffectsAllCogs = 'Afecta a: Todos los ' + Cogs
InventoryHealString = 'Curadibu'
InventoryDamageString = 'Da\xc3\xb1os'
InventoryBattleMenu = 'MEN\xc3\x9a DE COMBATE'
InventoryRun = 'CORRER'
InventorySOS = 'S.O.S.'
InventoryPass = 'PASAR'
InventoryClickToAttack = 'Haz clic en \nuna broma \npara atacar'
NPCForceAcknowledgeMessage = 'Antes de marcharte debes subirte en el tranvia.\n\n\n\n\n\nEl tranvia esta al lado de la tienda de bromas de Goofy.'
NPCForceAcknowledgeMessage2 = '!Enhorabuena por completar tu tarea del tranvia!\nVe al cuartel general dibu para recibir tu recompensa.\n\n\n\n\n\n\nEl cuartel general dibu esta cerca del centro del dibuparque.'
NPCForceAcknowledgeMessage3 = 'Recuerda que tienes que subirte en el tranvia.\n\n\n\n\n\nEl tranvia esta al lado de la tienda de bromas de Goofy.'
NPCForceAcknowledgeMessage4 = '!Enhorabuena!  !Has completado la primera dibutarea!\n\n\n\n\n\nVe al cuartel general dibu para recibir tu recompensa.'
ToonSleepString = '. . . ZZZ . . .'
MovieTutorialReward1 = '\xc2\xa1Has recibido 1 punto de lanzamiento! \xc2\xa1Cuando hayas recibido 10, recibiras una broma nueva!'
MovieTutorialReward2 = '\xc2\xa1Has recibido 1 punto de chorro! Cuando hayas recibido 10, recibiras una broma nueva!'
MovieTutorialReward3 = '\xc2\xa1Buen trabajo! \xc2\xa1Has completado tu primera Dibutarea!'
MovieTutorialReward4 = '\xc2\xa1Anda al Cuartel General para recibir tu premio!'
MovieTutorialReward5 = '\xc2\xa1Que te entretengas!'
BattleGlobalTracks = [
    'curadibu',
    'trampa',
    'cebo',
    'sonido',
    'lanzamiento',
    'chorro',
    'ca\xc3\xadda']
BattleGlobalAvPropStrings = (('Pluma', 'Meg\xc3\xa1fono', 'Pintalabios', 'Ca\xc3\xb1a de bamb\xc3\xba', 'Polvo de hadas', 'Bolas de malabarista'), ('Cascara de Pl\xc3\xa1tano', 'Rastrillo', 'Canicas', 'Arena movediza', 'Trampilla', 'TNT'), ('Billete de 10 euros', 'Im\xc3\xa1n peque\xc3\xb1o', 'Billete de 20 euros', 'Im\xc3\xa1n grande', 'Billete de 50 euros', 'Gafas hipn\xc3\xb3ticas'), ('Bocina de bicicleta', 'Silbato', 'Corneta', 'Sirena', 'Trompa de elefante', 'Sirena de niebla'), ('Magdalena', 'Trozo de tarta de frutas', 'Trozo de tarta de nata', 'Tarta de frutas entera', 'Tarta de nata entera', 'Tarta de cumplea\xc3\xb1os'), ('Flor chorreante', 'Vaso de agua', 'Pistola de agua', 'Botella de soda', 'Manguera', 'Nube tormentosa'), ('Maceta', 'Saco de arena', 'Yunque', 'Pesa grande', 'Caja fuerte', 'Piano de cola'))
BattleGlobalAvPropStringsSingular = (('una Pluma', 'un Meg\xc3\xa1fono', 'un Pintalabios', 'una Ca\xc3\xb1a de bamb\xc3\xba', 'un Polvo de hadas', 'unas Bolas de malabarista'), ('una Cascara de Pl\xc3\xa1tano', 'un Rastrillo', 'unas Canicas', 'una Arena movediza', 'una Trampilla', 'un TNT'), ('un Billete de 10 euros', 'un Im\xc3\xa1n peque\xc3\xb1o', 'un Billete de 20 euros', 'un Im\xc3\xa1n grande', 'un Billete de 50 euros', 'unas Gafas hipn\xc3\xb3ticas'), ('una Bocina de bicicleta', 'un Silbato', 'una Corneta', 'una Sirena', 'una Trompa de elefante', 'una Sirena de niebla'), ('una Magdalena', 'un Trozo de tarta de frutas', 'un Trozo de tarta de nata', 'una Tarta de frutas entera', 'una Tarta de nata entera', 'una Tarta de cumplea\xc3\xb1os'), ('una Flor chorreante', 'un Vaso de agua', 'una Pistola de agua', 'una Botella de soda', 'una Manguera', 'una Nube tormentosa'), ('una Maceta', 'un Saco de arena', 'un Yunque', 'una Pesa grande', 'una Caja fuerte', 'un Piano de cola'))
BattleGlobalAvPropStringsPlural = (('Plumas', 'Meg\xc3\xa1fonos', 'Pintalabios', 'Ca\xc3\xb1as de bamb\xc3\xba', 'Polvos de hadas', 'Bolas de malabarista'), ('Cascaras de Pl\xc3\xa1tano', 'Rastrillos', 'Canicas', 'Arenas movedizas', 'Trampillas', 'TNT'), ('Billetes de 10 euros', 'Imanes peque\xc3\xb1os', 'Billetes de 20 euros', 'Imanes grandes', 'Billetes de 50 euros', 'Gafas hipn\xc3\xb3ticas'), ('Bocinas de bicicleta', 'Silbatos', 'Cornetas', 'Sirenas', 'Trompas de elefante', 'Sirenas de niebla'), ('Magdalenas', 'Trozos de tarta de frutas', 'Trozos de tarta de nata', 'Tartas de frutas enteras', 'Tartas de nata enteras', 'Tartas de cumplea\xc3\xb1os'), ('Flores chorreantes', 'Vasos de agua', 'Pistolas de agua', 'Botellas de soda', 'Mangueras', 'Nubes tormentosas'), ('Macetas', 'Sacos de arena', 'Yunques', 'Pesas grandes', 'Cajas fuertes', 'Pianos de cola'))
BattleGlobalAvTrackAccStrings = ('Medio', 'Perfecto', 'Bajo', 'Alto', 'Medio', 'Alto', 'Bajo')
AttackMissed = 'Erraste'
GlobalStreetNames = {
    20000: ('a la', 'Calle del Tutorial'),
    1000: ('al', 'Dibuparque'),
    1100: ('al', 'Paseo del Percebe'),
    1200: ('a la', 'Avenida de las Algas'),
    1300: ('a la', 'Calle del Faro'),
    2000: ('al', 'Dibuparque'),
    2100: ('a la', 'Calle Boba'),
    2200: ('a la', 'Calle Locuela'),
    2300: ('a la', 'Avenida del Chiste'),
    3000: ('al', 'Dibuparque'),
    3100: ('a la', 'Calle de la Morsa'),
    3200: ('a la', 'Traves\xc3\xada del Trineo'),
    4000: ('al', 'Dibuparque'),
    4100: ('a la', 'Traves\xc3\xada de la Melod\xc3\xada'),
    4200: ('al', 'Bulevar del Bar\xc3\xadtono'),
    4300: ('a la', 'Calle del Tenor'),
    5000: ('al', 'Dibuparque'),
    5100: ('a la', 'Calle del Chopo'),
    5200: ('a la', 'Calle Arce'),
    9000: ('al', 'Dibuparque'),
    9100: ('a la ', 'Avenida de la Nana') }
DonaldsDock = ('a', 'Puerto Donald')
ToontownCentral = ('al', 'Centro de Toontown')
TheBrrrgh = ('a', 'Frescolandia')
MinniesMelodyland = ('a', 'Melodilandia de Minnie')
DaisyGardens = ('a', 'los Jardines de Daisy')
ConstructionZone = ('a la', 'Zona de obras')
FunnyFarm = ('a la', 'Granja Jolgorio')
GoofyStadium = ('al', 'Estadio Goofy')
DonaldsDreamland = ('a', 'Sue\xc3\xb1olandia de Donald')
BossbotHQ = ('al', 'Cuartel general jefebot')
SellbotHQ = ('al', 'Cuartel general vendebot')
CashbotHQ = ('al', 'Cuartel general chequebot')
LawbotHQ = ('al', 'Cuartel general abogabot')
Tutorial = ('al', 'Dibututorial')
MyEstate = ('a', 'Tu casa')
LoaderLabel = 'Cargando...'
HeadingToHood = 'Entrando %s %s...'
HeadingToYourEstate = 'Entrando a t\xc3\xba propiedad...'
HeadingToEstate = 'Entrando a la propiedad %s...'
HeadingToFriend = 'Entrando a la propiedad del amigo %s...'
HeadingToPlayground = 'Entrando al Dibuparque...'
HeadingToStreet = 'Entrando %s %s...'
ToontownDialogOK = 'Aceptar'
ToontownDialogCancel = 'Cancelar'
TownBattleRun = '\xc2\xbfQuieres volver corriendo al dibuparque?'
TownBattleChooseAvatarToonTitle = '\xc2\xbfQU\xc3\x89 DIBU?'
TownBattleChooseAvatarCogTitle = '\xc2\xbfCU\xc3\x81L ' + string.upper(Cog) + '?'
TownBattleChooseAvatarBack = 'ATR\xc3\x81S'
TownBattleSOSNoFriends = '\xc2\xa1No tienes amigos a los que llamar!'
TownBattleSOSWhichFriend = '\xc2\xbfA qu\xc3\xa9 amigo quieres llamar?'
TownBattleSOSBack = 'ATR\xc3\x81S'
TownBattleToonSOS = 'S.O.S.'
TownBattleUndecided = '?'
TownBattleHealthText = '%(hitPoints)s/%(maxHit)s'
TownBattleWaitTitle = 'Esperando a\notros jugadores...'
TownSoloBattleWaitTitle = 'Espera...'
TownBattleWaitBack = 'ATR\xc3\x81S'
TrolleyHFAMessage = 'No puedes subirte al tranv\xc3\xada hasta que el ris\xc3\xb3metro est\xc3\xa9 sonriendo.'
TrolleyTFAMessage = 'No puedes subirte al tranv\xc3\xada hasta que lo diga Mickey.'
TrolleyHopOff = 'Bajarse'
FishingExit = 'Hecho'
FishingCast = 'Lanzar'
FishingAutoReel = 'Carrete autom\xc3\xa1tico'
FishingItemFound = 'Has pescado:'
FishingCrankTooSlow = 'Muy\nlento'
FishingCrankTooFast = 'Muy\nr\xc3\xa1pido'
FishingFailure = '\xc2\xa1No has pescado nada!'
FishingFailureTooSoon = 'No empieces a enrollar el carrete hasta que veas que pican.  \xc2\xa1Espera a que la boya se mueva hacia arriba y abajo r\xc3\xa1pidamente!'
FishingFailureTooLate = '\xc2\xa1Es importante que enrolles el sedal mientras el pez est\xc3\xa1 mordiendo el anzuelo!'
FishingFailureAutoReel = 'El carrete autom\xc3\xa1tico no ha funcionado esta vez.  Enrolla a mano el carrete a la velocidad correcta para poder pescar algo.'
FishingFailureTooSlow = 'Has enrollado el carrete demasiado despacio.  Algunos peces son m\xc3\xa1s r\xc3\xa1pidos que otros.  \xc2\xa1Intenta mantener centrada la barra de velocidad!'
FishingFailureTooFast = 'Has enrollado el carrete demasiado deprisa.  Algunos peces son m\xc3\xa1s lentos que otros.  \xc2\xa1Intenta mantener centrada la barra de velocidad!'
FishingBrokeHeader = '\xc2\xa1Te has quedado sin gominolas!'
FishingBroke = '\xc2\xa1No tienes nada que poner en el anzuelo!  S\xc3\xbabete al tranv\xc3\xada para conseguir m\xc3\xa1s gominolas.'
TutorialGreeting1 = '\xc2\xa1Hola, %s!'
TutorialGreeting2 = '\xc2\xa1Hola, %s!\n\xc2\xa1Ven aqu\xc3\xad!'
TutorialGreeting3 = '\xc2\xa1Hola, %s!\n\xc2\xa1Ven aqu\xc3\xad!\n\xc2\xa1Usa las flechas del teclado!'
TutorialMickeyWelcome = '\xc2\xa1Bienvenido a Toontown!'
TutorialFlippyIntro = 'Te voy a presentar a mi amigo Flipi.'
TutorialFlippyHi = '\xc2\xa1Hola, %s!'
TutorialQT1 = 'Puedes usar esto para hablar.'
TutorialQT2 = 'Puedes usar esto para hablar.\nHaz clic y elige "Hola".'
TutorialChat1 = 'Puedes hablar con cualquiera de estos botones.'
TutorialChat2 = 'El bot\xc3\xb3n azul te permite charlar en l\xc3\xadnea por medio del teclado.'
TutorialChat3 = '\xc2\xa1Ten cuidado!  Muchos de los jugadores no entender\xc3\xa1n lo que dices si usas el teclado.'
TutorialChat4 = 'El bot\xc3\xb3n verde abre el %s.'
TutorialChat5 = 'Todos entienden lo que dices cuando usas el %s.'
TutorialChat6 = 'Prueba a decir "Hola".'
TutorialBodyClick1 = '\xc2\xa1Muy bien!'
TutorialBodyClick2 = '\xc2\xa1Encantado de conocerte! \xc2\xbfQuieres ser mi amigo?'
TutorialBodyClick3 = 'Para ser amigo de Flipi, haz clic en \xc3\xa9l...'
TutorialHandleBodyClickSuccess = '\xc2\xa1Buen trabajo!'
TutorialHandleBodyClickFail = 'Todav\xc3\xada no. Prueba a hacer clic en Flipi...'
TutorialFriendsButton = 'Ahora pulsa el bot\xc3\xb3n "Amigos", situado debajo de la imagen de Flipi, en la esquina derecha.'
TutorialHandleFriendsButton = 'Despu\xc3\xa9s, pulsa el bot\xc3\xb3n "S\xc3\xad".'
TutorialOK = 'Aceptar'
TutorialYes = 'S\xc3\xad'
TutorialNo = 'No'
TutorialFriendsPrompt = '\xc2\xbfQuieres ser amigo de Flipi?'
TutorialFriendsPanelMickeyChat = 'Flipi ha accedido a ser tu amigo. Pulsa "Aceptar" para terminar.'
TutorialFriendsPanelYes = '\xc2\xa1Flipi ha dicho que s\xc3\xad!'
TutorialFriendsPanelNo = '\xc2\xa1No es que seas muy amable!'
TutorialFriendsPanelCongrats = '\xc2\xa1Enhorabuena! Acabas de hacer tu primer amigo.'
TutorialFlippyChat1 = 'Ven a verme cuando est\xc3\xa9s preparado para tu primera dibutarea.'
TutorialFlippyChat2 = 'Estar\xc3\xa9 en el Ayuntamiento.'
TutorialAllFriendsButton = 'Para ver a todos tus amigos, haz clic en el bot\xc3\xb3n Amigos. Pru\xc3\xa9balo...'
TutorialEmptyFriendsList = 'Ahora mismo la lista est\xc3\xa1 vac\xc3\xada porque Flipi no es un jugador de verdad.'
TutorialCloseFriendsList = 'Pulsa el bot\xc3\xb3n\nCerrar para que la\nlista se cierre.'
TutorialShtickerButton = 'El bot\xc3\xb3n de la esquina inferior derecha sirve para abrir el dibucuaderno.  Pr\xc3\xbaebalo...'
TutorialBook1 = 'El dibucuaderno contiene un mont\xc3\xb3n de informaci\xc3\xb3n \xc3\xbatil, como este mapa de Toontown.'
TutorialBook2 = 'Tambi\xc3\xa9n puedes ver c\xc3\xb3mo van tus dibutareas.'
TutorialBook3 = 'Cuando hayas terminado, vuelve a pulsar el bot\xc3\xb3n del libro para que se cierre.'
TutorialLaffMeter1 = 'Tambi\xc3\xa9n vas a necesitar esto...'
TutorialLaffMeter2 = 'Tambi\xc3\xa9n vas a necesitar esto...\nEs tu ris\xc3\xb3metro.'
TutorialLaffMeter3 = 'Cuando los bots te ataquen, ir\xc3\xa1 disminuyendo.'
TutorialLaffMeter4 = 'Cuando est\xc3\xa9s en dibuparques como \xc3\xa9ste, subir\xc3\xa1 de nuevo.'
TutorialLaffMeter5 = 'Cuando completes dibutareas obtendr\xc3\xa1s recompensas, como por ejemplo un aumento del l\xc3\xadmite del ris\xc3\xb3metro.'
TutorialLaffMeter6 = '\xc2\xa1Ten cuidado! Si los bots te vencen, perder\xc3\xa1s todas las bromas.'
TutorialLaffMeter7 = 'Para conseguir m\xc3\xa1s bromas, juega a los juegos del tranv\xc3\xada.'
TutorialTrolley1 = '\xc2\xa1S\xc3\xadgueme hasta el tranv\xc3\xada!'
TutorialTrolley2 = '\xc2\xa1S\xc3\xbabete!'
TutorialBye1 = '\xc2\xa1Juega a unos cuantos juegos!'
TutorialBye2 = '\xc2\xa1Juega a unos cuantos juegos!\n\xc2\xa1Compra unas cuantas bromas!'
TutorialBye3 = 'Cuando hayas terminado, ve a ver a Flipi.'
TutorialForceAcknowledgeMessage = '\xc2\xa1Vas en direcci\xc3\xb3n contraria! \xc2\xa1Ve a buscar a Mickey!'
GlobalSpeedChatName = 'Charla r\xc3\xa1pida'
SCMenuEmotions = 'EMOCIONES'
SCMenuCustom = 'MIS FRASES'
SCMenuHello = 'HOLA'
SCMenuBye = 'ADIOS'
SCMenuHappy = 'FELIZ'
SCMenuSad = 'TRISTE'
SCMenuFriendly = 'AMIGABLE'
SCMenuSorry = 'LO SIENTO'
SCMenuStinky = 'HEDIONDO'
SCMenuPlaces = 'LUGARES'
SCMenuToontasks = 'DIBUTAREAS'
SCMenuBattle = 'COMBATE'
SCMenuGagShop = 'BROMAS'
SCMenuFriendlyYou = 'Eres...'
SCMenuFriendlyILike = 'me gusta...'
SCMenuPlacesLetsGo = 'Vamos a...'
SCMenuToontasksMyTasks = 'Mis tareas'
SCMenuToontasksYouShouldChoose = 'Creo que deberias escoger...'
SCMenuBattleLetsUse = 'Vamos a usar...'
SpeedChatStaticText = {
    1: 'S\xc3\xad',
    2: 'No',
    3: 'Aceptar',
    100: '\xc2\xa1Buenas!',
    101: '\xc2\xa1Hola!',
    102: '\xc2\xa1Muy Buenas!',
    103: '\xc2\xa1Eh!',
    104: '\xc2\xbfQu\xc3\xa9 hay?',
    105: '\xc2\xa1Hola a todos!',
    106: '\xc2\xa1ienvenido a Toontown!',
    107: '\xc2\xbfQu\xc3\xa9 tal?',
    108: '\xc2\xbfC\xc3\xb3mo est\xc3\xa1s?',
    109: '\xc2\xbfHola?',
    200: '\xc2\xa1Chao!',
    201: '\xc2\xa1Nos vemos!',
    202: '\xc2\xa1Hasta la vista!',
    203: '\xc2\xa1Que pases un buen d\xc3\xada!',
    204: '\xc2\xa1Divi\xc3\xa9rtete!',
    205: '\xc2\xa1Buena suerte!',
    206: 'Vuelvo enseguida.',
    207: 'Tengo que irme.',
    300: ':-)',
    301: '\xc2\xa1Hey!',
    302: '\xc2\xa1Hurra!',
    303: '\xc2\xa1chupi!',
    304: '\xc2\xa1Yujuuu!',
    305: '\xc2\xa1S\xc3\xad!',
    306: '\xc2\xa1Ja, ja!',
    307: '\xc2\xa1Ji, ji!',
    308: '\xc2\xa1Guau!',
    309: '\xc2\xa1Fant\xc3\xa1stico!',
    310: '\xc2\xa1Yepaa!',
    311: '\xc2\xa1Estupendo!',
    312: '\xc2\xa1Yupii!',
    313: '\xc2\xa1Yipee!',
    314: '\xc2\xa1Yiii ja!',
    315: '\xc2\xa1Dibufant\xc3\xa1stico!',
    400: ':-(',
    401: '\xc2\xa1Oh no!',
    402: '\xc2\xa1Oh oh!',
    403: '\xc2\xa1Caramba!',
    404: '\xc2\xa1Vaya!',
    405: '\xc2\xa1Ay!',
    406: '\xc2\xa1Uf!',
    407: '\xc2\xa1\xc2\xa1\xc2\xa1No!!!',
    408: '\xc2\xa1Auuu!',
    409: '\xc2\xbfEh?',
    410: 'Necesito m\xc3\xa1s puntos de risa.',
    500: '\xc2\xa1Gracias!',
    501: 'No hay de qu\xc3\xa9.',
    502: '\xc2\xa1De nada!',
    503: '\xc2\xa1A tu disposici\xc3\xb3n!',
    504: 'No, gracias a ti.',
    505: '\xc2\xa1Buen trabajo en equipo!',
    506: '\xc2\xa1Qu\xc3\xa9 divertido!',
    507: '\xc2\xa1S\xc3\xa9 mi amigo!',
    508: '\xc2\xa1Trabajemos en equipo!',
    509: '\xc2\xa1Sois estupendo!',
    510: '\xc2\xbfEres nuevo aqu\xc3\xad?',
    511: '\xc2\xbfHas ganado?',
    512: 'Creo que esto es demasiado para ti.',
    513: '\xc2\xbfQuieres que te ayude?',
    514: '\xc2\xbfPuedes ayudarme?',
    600: 'Pareces simp\xc3\xa1tico.',
    601: '\xc2\xa1Eres genial!',
    602: '\xc2\xa1Eres la bomba!',
    603: '\xc2\xa1Eres sensacional!',
    700: 'Me gusta tu nombre.',
    701: 'Me gusta tu aspecto.',
    702: 'Me gusta tu camiseta.',
    703: 'Me gusta tu falda.',
    704: 'Me gustan tus shorts.',
    705: '\xc2\xa1Me gusta este juego!',
    800: '\xc2\xa1Lo siento!',
    801: '\xc2\xa1Vaya!',
    802: '\xc2\xa1Lo siento, estoy peleando con los bots!',
    803: '\xc2\xa1Lo siento, estoy obteniendo gominolas!',
    804: '\xc2\xa1Lo siento, estoy haciendo una dibutarea!',
    805: 'Lo siento, he tenido que marcharme repentinamente.',
    806: 'Disculpame, me retreas\xc3\xa9.',
    807: 'Lo siento, no puedo.',
    808: 'No he podido esperar m\xc3\xa1s.',
    809: 'No te entiendo.',
    810: 'Usa el %s.' % GlobalSpeedChatName,
    900: '\xc2\xa1Eh!',
    901: '\xc2\xa1Vete de aqu\xc3\xad!',
    902: '\xc2\xa1Deja de hacer eso!',
    903: '\xc2\xa1Eso es mala educaci\xc3\xb3n!',
    904: '\xc2\xa1No seas malo!',
    905: '\xc2\xa1Estas hediondo!',
    906: 'Env\xc3\xada un informe de error.',
    907: 'No me puedo mover, porque hay un error.',
    1000: '\xc2\xa1Vamos!',
    1001: '\xc2\xbfPuedes teletransportarte a donde estoy?',
    1002: '\xc2\xbfNos vamos?',
    1003: '\xc2\xbfAd\xc3\xb3nde deber\xc3\xadamos ir?',
    1004: '\xc2\xbfPor qu\xc3\xa9 camino?',
    1005: 'Por aqu\xc3\xad.',
    1006: 'Sigueme.',
    1007: '\xc2\xa1Esp\xc3\xa9rame!',
    1008: 'Vamos a esperar a mi amigo.',
    1009: 'Vamos a buscar a otros dibus.',
    1010: 'Espera aqu\xc3\xad.',
    1011: 'Espera un momento.',
    1012: 'Nos encontraremos aqu\xc3\xad.',
    1013: '\xc2\xbfPuedes venire a mi casa?',
    1100: '\xc2\xa1V\xc3\xa1monos en el tranv\xc3\xada!',
    1101: '\xc2\xa1Vamos a volver al dibuparque!',
    1102: '\xc2\xa1Vamos a luchar contra los %s!' % Cogs,
    1103: '\xc2\xa1Vamos a tomar un edificio %s!' % Cog,
    1104: '\xc2\xa1Vamos al ascensor!',
    1105: '\xc2\xa1Vamos al Centro de Toontown!',
    1106: '\xc2\xa1Vamos a Puerto Donald!',
    1107: '\xc2\xa1Vamos a Melodilandia de Minnie!',
    1108: '\xc2\xa1Vamos a los Jardines de Daisy!',
    1109: '\xc2\xa1Vamos a Frescolandia!',
    1110: '\xc2\xa1Vamos a Sue\xc3\xb1olandia de Donald!',
    1111: '\xc2\xa1Vamos a mi casa!',
    1200: '\xc2\xbfEn qu\xc3\xa9 dibutarea est\xc3\xa1s trabajando?',
    1201: 'Ocup\xc3\xa9monos de eso.',
    1202: 'Esto no es lo que busco.',
    1203: 'Voy a buscar eso.',
    1204: 'No est\xc3\xa1 en esta calle.',
    1205: 'Todav\xc3\xada no lo he encontrado.',
    1299: 'Necesito que me asignen una dibutarea.',
    1300: 'Creo que debes usarun curadibu.',
    1301: 'Creo que debes usar un sonido.',
    1302: 'Creo que debes usar una ca\xc3\xadda.',
    1303: 'Creo que debes usar un cebo.',
    1304: 'Creo que debes usar una trampa.',
    1400: '\xc2\xa1Deprisa!',
    1401: '\xc2\xa1Buen Disparo!',
    1402: '\xc2\xa1Buena Broma!',
    1403: '\xc2\xa1No me has dado!',
    1404: '\xc2\xa1Lo has conseguido!',
    1405: '\xc2\xa1Lo hemos echo!',
    1406: '\xc2\xa1Sigue as\xc3\xad!',
    1407: '\xc2\xa1Est\xc3\xa1 chupado!',
    1408: '\xc2\xa1Qu\xc3\xa9 facil!',
    1409: '\xc2\xa1Corre!',
    1410: '\xc2\xa1Socorro!',
    1411: '\xc2\xa1Uf!',
    1412: 'Tenemos problemas.',
    1413: 'Necesito m\xc3\xa1s bromas.',
    1414: 'Necesito un curadibu.',
    1415: 'Deber\xc3\xadas pasar.',
    1500: '\xc2\xa1Usemos un curadibu!',
    1501: '\xc2\xa1Usemos una trampa!',
    1502: '\xc2\xa1Usemos un cebo!',
    1503: '\xc2\xa1Usemos un sonido!',
    1504: '\xc2\xa1Usemos un lanzamiento!',
    1505: '\xc2\xa1Usemos un chorro!',
    1506: '\xc2\xa1Usemos una caida!',
    1600: 'Tengo suficientes bromas.',
    1601: 'Necesito m\xc3\xa1s gominolas.',
    1602: 'Yo tambi\xc3\xa9n.',
    1603: '\xc2\xa1Deprisa!',
    1604: '\xc2\xbfUna m\xc3\xa1s?',
    1605: '\xc2\xbfQuieres jugar otra vez?',
    1606: 'Jugemos de nuevo.' }
CustomSCStrings = {
    10: 'Est\xc3\xa1 bien.',
    20: '\xc2\xbfPorque no?',
    30: '\xc2\xa1Naturalmente!',
    40: 'Esa es la manera de hacerlo.',
    50: '\xc2\xa1Exacto!',
    60: '\xc2\xbfQue pasa?',
    70: '\xc2\xa1Por supuesto!',
    80: 'Bingo!' }
PlaygroundDeathAckMessage = '\xc2\xa1Los bots se han llevado todas tus bromas!\n\nEst\xc3\xa1s triste. No puedes irte del dibuparque hasta que est\xc3\xa9s feliz.'
MinigameWaitingForOtherPlayers = 'Esperando a que se unan otros jugadores...'
MinigamePleaseWait = 'Espera...'
DefaultMinigameTitle = 'T\xc3\xadtulo del minijuego'
DefaultMinigameInstructions = 'Instrucciones del minijuego'
HeadingToMinigameTitle = 'Entrando al %s...'
MinigamePowerMeterLabel = 'Indicador\nde fuerza'
MinigamePowerMeterTooSlow = 'Muy\nlento'
MinigamePowerMeterTooFast = 'Muy\nr\xc3\xa1pido'
MinigameTemplateTitle = 'Plantilla del minijuego'
MinigameTemplateInstructions = '\xc3\x89sta es una plantilla de minijuegos. \xc3\x9asala para crear nuevos minijuegos.'
CannonGameTitle = 'Juego El Ca\xc3\xb1\xc3\xb3n'
CannonGameInstructions = 'Dispara a tu dibu para meterlo en el dep\xc3\xb3sito de agua tan rapido como puedas. Usa el rat\xc3\xb3n o las teclas de flecha para apuntar el ca\xc3\xb1\xc3\xb3n. \xc2\xa1Date prisa y consigue una gran recompensa para todos!'
CannonGameReward = 'RECOMPENSA'
TugOfWarGameTitle = 'Juego La Cuerda'
TugOfWarInstructions = 'Pulsa alternativamente las teclas de flecha izquierda y derecha con la suficiente rapidez para alinear la barra verde con la l\xc3\xadnea roja. \xc2\xa1No pulses demasiado deprisa ni demasiado despacio, o acabar\xc3\xa1s en el agua!'
TugOfWarGameGo = '\xc2\xa1YA!'
TugOfWarGameReady = 'Listo...'
TugOfWarGameEnd = '\xc2\xa1Muy bien!'
TugOfWarGameTie = '\xc2\xa1Has empatado!'
TugOfWarPowerMeter = 'Indicador de fuerza'
PatternGameTitle = 'Imita a ' + Minnie
PatternGameInstructions = Minnie + ' te ense\xc3\xb1ar\xc3\xa1 una secuencia de baile ' + 'Intenta repetir con las teclas de flecha el baile de Minnie justo igual que lo hace ella.'
PatternGameWatch = 'Observa estos pasos de baile...'
PatternGameGo = '\xc2\xa1YA!'
PatternGameRight = '\xc2\xa1Bien, %s!'
PatternGameWrong = '\xc2\xa1Vaya!'
PatternGamePerfect = '\xc2\xa1Ha sido perfecto, %s!'
PatternGameBye = '\xc2\xa1Gracias por jugar!'
PatternGameWaitingOtherPlayers = 'Esperando a otros jugadores...'
PatternGamePleaseWait = 'Espera...'
PatternGameFaster = '\xc2\xa1Has sido\nmuy r\xc3\xa1pido!'
PatternGameFastest = '\xc2\xa1Has sido\nel m\xc3\xa1s r\xc3\xa1pido!'
PatternGameYouCanDoIt = '\xc2\xa1Vamos!\n\xc2\xa1Puedes hacerlo!'
PatternGameOtherFaster = '\nha sido m\xc3\xa1s r\xc3\xa1pido.'
PatternGameOtherFastest = '\nha sido el m\xc3\xa1s r\xc3\xa1pido.'
PatternGameGreatJob = '\xc2\xa1Buen trabajo!'
RaceGameTitle = 'Juego La Carrera'
RaceGameInstructions = 'Haz clic en un n\xc3\xbamero. \xc2\xa1Pi\xc3\xa9nsalo bien! S\xc3\xb3lo avanzar\xc3\xa1s si nadie m\xc3\xa1s ha escogido ese mismo n\xc3\xbamero.'
RaceGameWaitingChoices = 'Esperando a que elijan otros jugadores...'
RaceGameCardText = '%(name)s saca: %(reward)s'
RaceGameCardTextBeans = '%(name)s recibe: %(reward)s'
RaceGameCardTextHi1 = '\xc2\xa1%(name)s es un dibu fabuloso!'
RaceGameForwardOneSpace = ' adelante 1 espacio'
RaceGameForwardTwoSpaces = ' adelante 2 espacios'
RaceGameForwardThreeSpaces = ' adelante 3 espacios'
RaceGameBackOneSpace = ' atr\xc3\xa1s 1 espacio'
RaceGameBackTwoSpaces = ' atr\xc3\xa1s 2 espacios'
RaceGameBackThreeSpaces = ' atr\xc3\xa1s 3 espacios'
RaceGameOthersForwardThree = ' todos los dem\xc3\xa1s, adelante \n3 espacios'
RaceGameOthersBackThree = 'todos los dem\xc3\xa1s, atr\xc3\xa1s \n3 espacios'
RaceGameInstantWinner = '\xc2\xa1Ganador instant\xc3\xa1neo!'
RaceGameJellybeans2 = '2 gominolas'
RaceGameJellybeans4 = '4 gominolas'
RaceGameJellybeans10 = '\xc2\xa110 gominolas!'
RingGameTitle = 'Juego Los Anillos'
RingGameInstructionsSinglePlayer = 'Intenta atravesar nadando todos los anillos que puedas de color %s. Usa las teclas de flecha para nadar.'
RingGameInstructionsMultiPlayer = 'Intenta atravesar nadando los anillos de color %s.  Los dem\xc3\xa1s jugadores intentar\xc3\xa1n atravesar el resto de los anillos.  Usa las flechas del teclado para nadar.'
RingGameMissed = 'FALLO'
RingGameGroupPerfect = 'GRUPO\n\xc2\xa1\xc2\xa1PERFECTO!!'
RingGamePerfect = '\xc2\xa1PERFECTO!'
RingGameGroupBonus = 'BONIFICACI\xc3\x93N POR GRUPO'
ColorRed = 'rojo'
ColorGreen = 'verde'
ColorOrange = 'naranja'
ColorPurple = 'morado'
ColorWhite = 'blanco'
ColorBlack = 'negro'
ColorYellow = 'amarillo'
TagGameTitle = 'T\xc3\xba la llevas'
TagGameInstructions = 'Recoge los tesoros. \xc2\xa1No puedes recoger tesoros cuando LA LLEVES!'
TagGameYouAreIt = '\xc2\xa1T\xc3\xba la LLEVAS!'
TagGameSomeoneElseIsIt = '\xc2\xa1%s la LLEVA!'
MazeGameTitle = 'Juego El Laberinto'
MazeGameInstructions = 'Recoge los tesoros. \xc2\xa1Intenta recogerlos todos, pero ten cuidado con los bots!'
CatchGameTitle = 'Juego Atrapa las frutas'
CatchGameInstructions = 'Atrapa %(fruit)s que puedas. Cuidado con los ' + Cogs + ', y trata de no \xe2\x80\x98atrapar\xe2\x80\x99 ningun %(badThing)s!'
CatchGamePerfect = '\xc2\xa1PERFECTO!'
CatchGameApples = 'todas las manzanas'
CatchGameOranges = 'todas las naranjas'
CatchGamePears = 'todas las peras'
CatchGameCoconuts = 'todos los cocos'
CatchGameWatermelons = 'todas las sand\xc3\xacas'
CatchGamePineapples = 'todas las pi\xc3\xb1as'
CatchGameAnvils = 'yunque'
MinigameRulesPanelPlay = 'JUGAR'
GagShopName = 'Tienda de bromas de Goofy'
GagShopPlayAgain = 'JUGAR\nOTRA VEZ'
GagShopBackToPlayground = 'VOLVER AL\nDIBUPARQUE'
GagShopYouHave = 'Tienes %s gominolas para gastar'
GagShopYouHaveOne = 'Tienes 1 gominola para gastar'
GagShopTooManyProps = 'Lo siento, tienes demasiados accesorios'
GagShopDoneShopping = 'COMPRAS\nFINALIZADAS'
GagShopTooManyOfThatGag = 'Lo siento, ya tienes suficientes %s.'
GagShopInsufficientSkill = 'Todav\xc3\xada no tienes suficiente habilidad para eso'
GagShopYouPurchased = 'Has comprado %s'
GagShopOutOfJellybeans = '\xc2\xa1Lo siento, te has quedado sin gominolas!'
GagShopWaitingOtherPlayers = 'Esperando a otros jugadores...'
GagShopPlayerDisconnected = '%s se ha desconectado'
GagShopPlayerExited = '%s se ha marchado'
GagShopPlayerPlayAgain = 'Jugar de nuevo'
GagShopPlayerBuying = 'Comprando'
GenderShopQuestionMickey = '\xc2\xa1Para crear un dibuchico, haz clic en m\xc3\xad!'
GenderShopQuestionMinnie = '\xc2\xa1Para crear una dibuchica, haz clic en m\xc3\xad!'
GenderShopFollow = '\xc2\xa1S\xc3\xadgueme!'
GenderShopSeeYou = '\xc2\xa1Hasta luego!'
GenderShopBoyButtonText = 'Chico'
GenderShopGirlButtonText = 'Chica'
BodyShopHead = 'Cabeza'
BodyShopBody = 'Cuerpo'
BodyShopLegs = 'Piernas'
ClothesShopShorts = 'Shorts'
ClothesShopShirt = 'Camiseta'
ClothesShopBottoms = 'Falda'
ColorShopHead = 'Cabeza'
ColorShopBody = 'Cuerpo'
ColorShopLegs = 'Piernas'
ColorShopToon = 'Dibu'
ColorShopParts = 'Partes'
ColorShopAll = 'Todo'
MakeAToonDone = 'Hecho'
MakeAToonCancel = 'Cancelar'
MakeAToonNext = 'Siguiente'
MakeAToonLast = 'Atr\xc3\xa1s'
CreateYourToon = 'Haz clic en las flechas para crear a tu dibu.'
CreateYourToonTitle = 'Crea a tu dibu'
CreateYourToonHead = 'Haz clic en las flechas de la "cabeza" para escoger diferentes animales.'
MakeAToonClickForNextScreen = 'Haz clic en la flecha situada abajo para ir a la pantalla siguiente.'
PickClothes = '\xc2\xa1Haz clic en las flechas para escoger prendas!'
PickClothesTitle = 'Escoge tus prendas'
PaintYourToon = '\xc2\xa1Haz clic en las flechas para pintar a tu dibu!'
PaintYourToonTitle = 'Pinta a tu dibu'
MakeAToonYouCanGoBack = '\xc2\xa1Tambi\xc3\xa9n puedes volver para cambiar tu cuerpo!'
MakeAFunnyName = '\xc2\xa1Elige un nombre divertido para el dibu con el juego de los nombres!'
MustHaveAFirstOrLast1 = 'Tu dibu deber\xc3\xada tener un nombre o un apellido, \xc2\xbfno crees?'
MustHaveAFirstOrLast2 = '\xc2\xbfNo quieres que tu dibu tenga un nombre o un apellido?'
ApprovalForName1 = '\xc2\xa1Eso es, tu dibu se merece un gran nombre!'
ApprovalForName2 = '\xc2\xa1Los nombres de dibus son los mejores!'
MakeAToonLastStep = '\xc2\xa1\xc3\x9altimo paso antes de ir a Toontown!'
PickANameYouLike = '\xc2\xa1Escoge un nombre que te guste!'
NameToonTitle = 'Pon un nombre a tu dibu'
TitleCheckBox = 'T\xc3\xadtulo'
FirstCheckBox = 'Nombre'
LastCheckBox = 'Apellido'
RandomButton = 'Al azar'
NameShopSubmitButton = 'Enviar'
TypeANameButton = 'Escribe un nombre'
TypeAName = '\xc2\xbfNo te gustan estos nombres?\nHaz clic aqu\xc3\xad -->'
PickAName = '\xc2\xa1Prueba con el juego de los nombres!\nHaz clic aqu\xc3\xad -->'
PickANameButton = 'Juego de los nombres'
RejectNameText = 'Ese nombre no est\xc3\xa1 permitido. Int\xc3\xa9ntalo de nuevo.'
NameShopNameMaster = 'NameMasterCastillian.txt'
NameShopPay = '\xc2\xa1Suscr\xc3\xadbete ya!'
NameShopPlay = 'Prueba gratuita'
NameShopOnlyPaid = 'S\xc3\xb3lo los usuarios abonados\npueden poner nombre a sus dibus.\nHasta que te suscribas,\ntu nombre ser\xc3\xa1\n'
NameShopContinueSubmission = 'Continuar env\xc3\xado'
NameShopChooseAnother = 'Elegir otro nombre'
NameShopToonCouncil = 'El Consejo Dibu\nrevisar\xc3\xa1 tu\nnombre.  ' + 'La revisi\xc3\xb3n puede\ntardar unos d\xc3\xadas.\nMientras esperas,\ntu nombre ser\xc3\xa1\n '
PleaseTypeName = 'Escribe tu nombre:'
AllNewNames = 'Todos los nombres nuevos\ndeben ser aprobados\npor el Consejo Dibu.'
NameShopNameRejected = 'El nombre que has\nenviado ha sido\nrechazado.'
NameShopNameAccepted = '\xc2\xa1Enhorabuena!\nEl nombre que has\nenviado ha sido\naceptado.'
NoPunctuation = '\xc2\xa1No puedes usar signos de puntuaci\xc3\xb3n en tu nombre!'
PeriodOnlyAfterLetter = 'Tu nombre puede incluir un punto, pero s\xc3\xb3lo despu\xc3\xa9s de una letra.'
ApostropheOnlyAfterLetter = 'Tu nombre puede incluir un ap\xc3\xb3strofo, pero s\xc3\xb3lo despu\xc3\xa9s de una letra.'
NoNumbersInTheMiddle = 'Es posible que los n\xc3\xbameros no aparezcan si est\xc3\xa1n en medio de una palabra.'
ThreeWordsOrLess = 'Tu nombre debe tener un m\xc3\xa1ximo de tres palabras.'
CopyrightedNames = ('mickey', 'mickey mouse', 'mickeymouse', 'minnie', 'minnie mouse', 'minniemouse', 'donald', 'donald duck', 'donaldduck', 'pluto', 'goofy')
NumToColor = [
    'Blanco',
    'Melocot\xc3\xb3n',
    'Rojo brillante',
    'Rojo',
    'Casta\xc3\xb1o',
    'Siena',
    'Marr\xc3\xb3n',
    'Marr\xc3\xb3n claro',
    'Coral',
    'Naranja',
    'Amarillo',
    'Crema',
    'Topacio',
    'Lima',
    'Verde mar',
    'Verde',
    'Azul claro',
    'Aguamarina',
    'Azul',
    'Hierba',
    'Azul marino',
    'Azul pizarra',
    'Morado',
    'Lavanda',
    'Rosa']
NameTooLong = 'Ese nombre es demasiado largo. Int\xc3\xa9ntalo de nuevo.'
ToonAlreadyExists = '\xc2\xa1Ya tienes un dibu llamado %s!'
NameAlreadyInUse = '\xc2\xa1Ese nombre ya ha sido usado!'
EmptyNameError = 'Primero debes introducir un nombre.'
NameError = 'Lo siento. Ese nombre no sirve.'
NCTooShort = 'Ese nombre es demasiado corto.'
NCNoDigits = 'Tu nombre no puede contener n\xc3\xbameros.'
NCNeedLetters = 'Todas las palabras de tu nombre deben contener letras.'
NCNeedVowels = 'Todas las palabras de tu nombre deben contener vocales.'
NCAllCaps = 'Tu nombre no puede estar por completo en may\xc3\xbasculas.'
NCMixedCase = 'Ese nombre tiene demasiadas may\xc3\xbasculas.'
NCBadCharacter = "Tu nombre no puede contener el car\xc3\xa1cter '%s'"
NCGeneric = 'Lo siento, ese nombre no sirve.'
NCTooManyWords = 'Tu nombre no puede tener m\xc3\xa1s de cuatro palabras.'
NCDashUsage = 'S\xc3\xb3lo puedes usar los guiones para unir dos palabras (como en "Bu-bu").'
NCCommaEdge = 'Tu nombre no puede comenzar ni terminar con una coma.'
NCCommaAfterWord = 'No puedes comenzar una palabra con una coma.'
NCCommaUsage = 'Ese nombre no emplea las comas correctamente. Las comas deben unir dos palabras, como en el nombre "Dr. Pato, cirujano"". Adem\xc3\xa1s, las comas deben ir seguidas por un espacio.'
NCPeriodUsage = 'Ese nombre no emplea los puntos correctamente. S\xc3\xb3lo se permiten los puntos en palabras como "Sr.", "Sra.", "J.T.", etc.'
NCApostrophes = 'Ese nombre tiene demasiados ap\xc3\xb3strofos.'
RemoveTrophy = 'Cuartel general dibu: \xc2\xa1Los bots han tomado el control de uno de los edificios que has recuperado!'
STOREOWNER_TOOKTOOLONG = '\xc2\xbfNecesitas m\xc3\xa1s tiempo para pens\xc3\xa1rtelo?'
STOREOWNER_GOODBYE = '\xc2\xa1Hasta luego!'
STOREOWNER_NEEDJELLYBEANS = 'Tienes que subir al tranv\xc3\xada para conseguir gominolas.'
STOREOWNER_GREETING = 'Elige lo que quieras comprar.'
STOREOWNER_BROWSING = 'Puedes mirar, pero para comprar necesitas un t\xc3\xadcket de ropa.'
STOREOWNER_NOCLOTHINGTICKET = 'Para comprar prendas necesitas un t\xc3\xadcket de ropa.'
STOREOWNER_NOROOM = 'Mmm...tienes que tener mas sitio en tu cl\xc3\xb3set antes de comprar mas ropa.\n'
STOREOWNER_CONFIRM_LOSS = 'T\xc3\xba closet esta lleno. T\xc3\xba vas a perder la ropa que estabas usando.'
STOREOWNER_OK = 'Muy bien'
STOREOWNER_CANCEL = 'Cancelar'
TutorialHQOfficerName = 'Funcionario Enrique'
NPCToonNames = {
    20000: 'Tato Tutorial',
    1000: 'Cuartel General Dibu',
    20001: 'Flipi',
    2001: 'Flipi',
    2002: 'Pecunio el banquero',
    2003: 'Pedro el maestro',
    2004: 'Calixta la modista',
    2005: 'Leopoldo el bibliotecario',
    2006: 'Dependiente Vicente',
    2011: 'Dependienta Vicenta',
    2007: 'Funcionario del cuartel general',
    2008: 'Funcionario del cuartel general',
    2009: 'Funcionaria del cuartel general',
    2010: 'Funcionaria del cuartel general',
    2101: 'Bautista el dentista',
    2102: 'Luc\xc3\xada la polic\xc3\xada',
    2103: 'Camale\xc3\xb3n Atu\xc3\xa9ndez',
    2104: 'Funcionario del cuartel general',
    2105: 'Funcionario del cuartel general',
    2106: 'Funcionaria del cuartel general',
    2107: 'Funcionaria del cuartel general',
    2108: 'Fagucia Carasucia',
    2109: 'Burbujo Irujo',
    2110: '\xc3\x93scar Tel',
    2111: 'Agust\xc3\xadn el bailar\xc3\xadn',
    2112: 'Dr. Tom\xc3\xa1s',
    2113: 'El incre\xc3\xadble Esnafro',
    2114: 'Chiquito Lepero',
    2115: 'Flexia Pap\xc3\xadrez',
    2116: 'Pepe Pu\xc3\xb1os',
    2117: 'Facta Putre ',
    2118: 'Inocencio Santos',
    2119: 'Hilaria Jaj\xc3\xa1',
    2120: 'Profesor Nino',
    2121: 'Sra. Orni Mans',
    2122: 'Or\xc3\xa1n Guto',
    2123: 'Marivi Guasona',
    2124: 'Bromi Stilla',
    2125: 'Morgan Dul',
    2126: 'Profesor Carcajada',
    2127: 'Mauro Euro',
    2128: 'Luis el Chiflado',
    2129: 'Carmelo Cot\xc3\xb3n',
    2130: 'Calambrita Amp\xc3\xa9rez',
    2131: 'Cosquilla Plum\xc3\xb3n',
    2132: 'Chucho Ch\xc3\xbachez',
    2133: 'Dr. Rico',
    2134: 'M\xc3\xb3nica Llada',
    2135: 'Mar\xc3\xada Corremillas',
    2136: 'Dexter Nillo',
    2137: 'Mari Fe Liz',
    2138: 'Pepote Cobos',
    2139: 'Dani Dea',
    2201: 'Pepe el cartero',
    2202: 'Jocosa Risa',
    2203: 'Funcionario del cuartel general',
    2204: 'Funcionario del cuartel general',
    2205: 'Funcionaria del cuartel general',
    2206: 'Funcionaria del cuartel general',
    2207: 'Cholo Calandracas',
    2208: 'Luisillo Pegajosillo',
    2209: 'Chancho La Monda',
    2210: 'Pirul\xc3\xad',
    2211: 'Carca Ajada ',
    2212: 'Roque Raro',
    2213: 'Pepi Bielas',
    2214: 'Pancho Quemancho',
    2215: 'Benito Lat\xc3\xb3nez',
    2216: 'Noa Ynada',
    2217: 'Tiburcio Algas',
    2218: 'Mari Jo Cosa',
    2219: 'Chef P\xc3\xa1nfilo',
    2220: 'Tancredo Cabezarroca',
    2221: 'Clovinia Dherente',
    2222: 'Corto M\xc3\xa9chez',
    2223: 'Guasa Tomasa',
    2224: 'Sacha Muscado',
    2301: 'Dr. Tronchaespinazo',
    2302: 'Profesor Cosquillas',
    2303: 'Enfermera Mondi',
    2304: 'Funcionario del cuartel general',
    2305: 'Funcionario del cuartel general',
    2306: 'Funcionaria del cuartel general',
    2307: 'Funcionaria del cuartel general',
    2308: 'Mullida Mull\xc3\xaddez',
    2309: 'Desmo\xc3\xb1o Ruinez',
    2311: 'Paco Gotazo',
    2312: 'Dra. Sensible',
    2313: 'Lila Lampar\xc3\xb3n',
    2314: 'Disco Bolo',
    2315: 'Francisco Reoso',
    2316: 'Cindi Charachera',
    2318: 'Toni Chich\xc3\xb3n',
    2319: 'Zipi',
    2320: 'Alfredo Pastosi',
    1001: 'Dependiente Pipe',
    1002: 'Dependiente Pape',
    1003: 'Funcionario del cuartel general',
    1004: 'Funcionaria del cuartel general',
    1005: 'Funcionario del cuartel general',
    1006: 'Funcionaria del cuartel general',
    1007: 'Fifo Pretaporter',
    1101: 'Beto Buque',
    1102: 'Capit\xc3\xa1n Dobl\xc3\xb3n',
    1103: 'Raspo Esp\xc3\xadnez',
    1104: 'Dr. Rompecubiertas',
    1105: 'Almirante Garfio',
    1106: 'Sra. Almid\xc3\xb3nez',
    1107: 'Nemo Mancuerna',
    1108: 'Funcionario del cuartel general',
    1109: 'Funcionaria del cuartel general',
    1110: 'Funcionario del cuartel general',
    1111: 'Funcionaria del cuartel general',
    1112: 'Pepe Glubglub',
    1113: 'Chiqui Quillas',
    1114: 'Magdaleno Yapican',
    1115: 'Abogada Tent\xc3\xa1cula Calamar',
    1116: 'Pili Percebe',
    1117: 'Billy Yates',
    1118: 'Nelson Tintes',
    1121: 'Lisa M\xc3\xa1stiles',
    1122: 'Tit\xc3\xa1nico Iceberg',
    1123: 'Electra Angu\xc3\xadlez',
    1124: 'Astillo Mu\xc3\xa9llez',
    1125: 'Tunanta Estribor',
    1201: 'Perci Percebe',
    1202: 'Pasma Rote',
    1203: 'Ajab',
    1204: 'Claus Anclas',
    1205: 'Funcionario del cuartel general',
    1206: 'Funcionaria del cuartel general',
    1207: 'Funcionario del cuartel general',
    1208: 'Funcionaria del cuartel general',
    1209: 'Profesor Curasardinas',
    1210: 'Pong Peyeng',
    1211: 'Velo Dromo',
    1212: 'Pico Tazos',
    1213: 'R\xc3\xa9moro Tiburcio ',
    1214: 'Catalina Timoneles',
    1215: 'Mar\xc3\xada del Mar Salada',
    1216: 'Carrete Ca\xc3\xb1as',
    1217: 'Marina Naval',
    1218: 'Paco Pac\xc3\xadfico',
    1219: 'Alvar Cabeza de Playa',
    1220: 'Isabel Segunda',
    1221: 'Blasco B\xc3\xa1\xc3\xb1ez',
    1222: 'Alberto Abordaje',
    1223: 'Sepio Calam\xc3\xa1rez',
    1224: 'Emilia Anguila',
    1225: 'Gonzo Friegacubiertas',
    1226: 'Izo Velamen',
    1227: 'Coral Bistur\xc3\xad',
    1301: 'Pepa Sastre',
    1302: 'Isidoro Subem\xc3\xa1stiles',
    1303: 'Clodovico Croma\xc3\xb1\xc3\xb3n',
    1304: 'Santiagui\xc3\xb1a N\xc3\xa9corez',
    1305: 'Funcionario del cuartel general',
    1306: 'Funcionaria del cuartel general',
    1307: 'Funcionario del cuartel general',
    1308: 'Funcionaria del cuartel general',
    1309: 'Mar Oc\xc3\xa9ana',
    1310: 'Trucho Ca\xc3\xb1ete',
    1311: 'Goyo Gorrotocho',
    1312: 'Quillo Quilla',
    1313: 'Gordi Gordios',
    1314: 'Jorge Rumbre',
    1315: 'Catedr\xc3\xa1tico \xc3\x81ncora',
    1316: 'Canuta Canoas',
    1317: 'Juana Salvadora Gaviota',
    1318: 'Salva Vidas',
    1319: 'Quique Diqueseco',
    1320: 'Mario Almejo',
    1321: 'Dina Atraque',
    1322: 'Estibora P\xc3\xb3pez',
    1323: 'Pericles Cabezabuque',
    1324: 'Concha Coqu\xc3\xadnez ',
    1325: 'Vaporeto Misisipi',
    1326: 'Jurela Bes\xc3\xbaguez',
    1327: 'Gabi Ota',
    1328: 'Carlitos Lenguado',
    1329: 'Flora Mar\xc3\xadnez',
    1330: 'Fredo Barbarrala',
    1331: 'Tim\xc3\xb3n Bocanegra',
    3001: 'Adela Dita',
    3002: 'Funcionario del cuartel general',
    3003: 'Funcionaria del cuartel general',
    3004: 'Funcionario del cuartel general',
    3005: 'Funcionario del cuartel general',
    3006: 'Dependiente Poli',
    3007: 'Dependienta Pili',
    3008: 'Giorgio Armi\xc3\xb1o',
    3101: 'Juanjo Esc\xc3\xa1rchez',
    3102: 'T\xc3\xada Ritona',
    3103: 'Pepe Tundra',
    3104: 'Geli da Pinto',
    3105: 'Pipe Pelado',
    3106: 'Frigo Saba\xc3\xb1\xc3\xb3n',
    3107: 'Maite Aterida',
    3108: 'Doroteo Escarcha',
    3109: 'Pati',
    3110: 'Lucas Friolero',
    3111: 'Kevin Kelvin',
    3112: 'Fredo Dedo',
    3113: 'Cris T\xc3\xa9rico',
    3114: 'Beto Tomba',
    3115: 'Funcionario del cuartel general',
    3116: 'Funcionaria del cuartel general',
    3117: 'Funcionario del cuartel general',
    3118: 'Funcionario del cuartel general',
    3119: 'Carlos Congelado',
    3120: 'Mito Mit\xc3\xb3n',
    3121: 'Voltio Amp\xc3\xa9rez',
    3122: 'Beb\xc3\xa9 Bob',
    3123: 'Ricardo Bofrigo',
    3124: 'Manfredo Car\xc3\xa1mbanez',
    3125: 'Tiritono Quelog',
    3126: 'Pescanovo Mart\xc3\xadnez',
    3127: 'Popoco Mecaigo',
    3128: 'Pipo Polar',
    3129: 'Dina Frigomiga',
    3130: 'Roberta',
    3131: 'Lorenzo Rascafr\xc3\xada',
    3132: 'Cenicilla',
    3133: 'Dr. Congelaimagen',
    3134: 'Paco Gelado',
    3135: 'Empa Pada',
    3136: 'Felicia Simp\xc3\xa1tica',
    3137: 'Kevin Ator',
    3138: 'Chef Sopacar\xc3\xa1mbano ',
    3139: 'Abuelita Polosur',
    3201: 'T\xc3\xada \xc3\x81rtica',
    3202: 'Antonio Tiritonio',
    3203: 'Eugenio Criogenio',
    3204: 'Dra. Soplillos',
    3205: 'Perico Arenque',
    3206: 'Fernando Anchoa',
    3207: 'Dr. Bocamaraca',
    3208: 'Felipe el gru\xc3\xb1\xc3\xb3n',
    3209: 'Garmillo Panterquircho',
    3210: 'Nutrio Cenutrio',
    3211: 'Pega Moide',
    3212: 'Federico Gelado',
    3213: 'Funcionario del cuartel general',
    3214: 'Funcionaria del cuartel general',
    3215: 'Funcionario del cuartel general',
    3216: 'Funcionario del cuartel general',
    3217: 'Pedro Glaciares',
    3218: 'Pepe Napiazul',
    3219: 'Tom\xc3\xa1s Bufandilla',
    3220: 'Estornio Atch\xc3\xads',
    3221: 'In\xc3\xa9s Carcha',
    3222: 'Ventiscona Copogordo',
    3223: 'Macario Ajillo',
    3224: 'Madame Glac\xc3\xa9',
    3225: 'Gregorio Saba\xc3\xb1\xc3\xb3n ',
    3226: 'Pap\xc3\xa1 No\xc3\xa9s',
    3227: 'Solario R\xc3\xa1yez',
    3228: 'Escalo Fr\xc3\xado',
    3229: 'Hernia Tar\xc3\xbaguez',
    3230: 'Optimisto Pel\xc3\xa1ez ',
    3231: 'Pedro Picahielo',
    4001: 'Moli Mel\xc3\xb3dica',
    4002: 'Funcionario del cuartel general',
    4003: 'Funcionaria del cuartel general',
    4004: 'Funcionaria del cuartel general',
    4005: 'Funcionaria del cuartel general',
    4006: 'Dependienta Dina',
    4007: 'Dependiente Dino',
    4008: 'Modista Armon\xc3\xada',
    4101: 'Ropo Pompom',
    4102: 'Bibi',
    4103: 'Dr. Pavo Rotti',
    4104: 'Funcionario del cuartel general',
    4105: 'Funcionaria del cuartel general',
    4106: 'Funcionaria del cuartel general',
    4107: 'Funcionaria del cuartel general',
    4108: 'Sordino Quena',
    4109: 'Carlos',
    4110: 'Metr\xc3\xb3noma Diapas\xc3\xb3n',
    4111: 'Camilo S\xc3\xa9ptimo',
    4112: 'Fa',
    4113: 'Madame Modales',
    4114: 'Dum D\xc3\xbamez',
    4115: 'B\xc3\xa1rbara Sevilla',
    4116: 'Pizzicato',
    4117: 'Lina Mando',
    4118: 'Rapsodio Sonata',
    4119: 'Beto Ven',
    4120: 'Tara Reo',
    4121: 'Bemolio Sostenido',
    4122: 'Noa Ybemoles',
    4123: 'Cornet\xc3\xadn Gaita',
    4124: 'Rifi Rafe',
    4125: 'Clinia Eastwood',
    4126: 'Tortillo Tenorio',
    4127: 'Vivaracho Vivaldi',
    4128: 'Pl\xc3\xa1cido Lunes',
    4129: 'Fina Desafinada',
    4130: 'Ironio M\xc3\xa1idez',
    4131: 'Abraham Zambomba',
    4132: 'Teresa Benicanta',
    4133: 'Impo Luto',
    4134: 'DJ Diborio',
    4135: 'Teresito Sopranillo',
    4136: 'Fusa Patidifusa',
    4137: 'Roy Bate',
    4138: 'Octavo Seisillo',
    4139: 'Ada Gio',
    4140: 'Tr\xc3\xa9molo Torpe',
    4201: 'Tina Sonatina',
    4202: 'Barbo',
    4203: 'Chopo Chop\xc3\xadn',
    4204: 'Funcionario del cuartel general',
    4205: 'Funcionaria del cuartel general',
    4206: 'Funcionaria del cuartel general',
    4207: 'Funcionaria del cuartel general',
    4208: 'L\xc3\xadrica T\xc3\xa1strofe',
    4209: 'Sissy de Triana',
    4211: 'Jos\xc3\xa9 Carrerilla',
    4212: 'Filarmonio Opereto',
    4213: 'Ambulancio Raudo',
    4214: 'Arnesia Mifasol',
    4215: 'Corneto Claxon',
    4216: 'Amadeo Parche',
    4217: 'Juan Strauss',
    4218: 'Octava Pianola',
    4219: 'Tromb\xc3\xb3n Charango',
    4220: 'Sartenio Batuta',
    4221: 'Pipo Madrigal',
    4222: 'Fulano de Tal',
    4223: 'Felisa Obelisco',
    4224: 'Jon\xc3\xa1s Clarinete',
    4225: 'Cuchi Cheo',
    4226: 'Paca Canora',
    4227: 'Betina Trompetilla',
    4228: 'Nabuco Donosor',
    4229: 'Melodia Pas\xc3\xb3n',
    4230: 'Rigo Letto',
    4231: 'Acordia Deona',
    4232: 'F\xc3\xadgaro Casamentero',
    4233: 'Arpo Marx',
    4234: 'Coro Voc\xc3\xa1lez',
    4301: 'Uki',
    4302: 'Juanola',
    4303: 'Leo',
    4304: 'Funcionario del cuartel general',
    4305: 'Funcionaria del cuartel general',
    4306: 'Funcionaria del cuartel general',
    4307: 'Funcionaria del cuartel general',
    4308: 'Felisa Felina',
    4309: 'Isidoro T\xc3\xa1piez',
    4310: 'Marta Falla',
    4311: 'Corneta Camarera',
    4312: 'Horacio Pianola',
    4313: 'Renato Enquequedamos',
    4314: 'Vilma Mascota',
    4315: 'Rola Roles',
    4316: 'Pachi Zapatillo',
    4317: 'Piero Pereta',
    4318: 'Bob Marlene',
    4319: 'Urraca Gr\xc3\xa1jez',
    4320: 'Irene Fervescente',
    4321: 'Pepe Palmira',
    4322: 'Aitor Poloneso',
    4323: 'Ana Balada',
    4324: 'Elisa',
    4325: 'Banquero Ram\xc3\xb3n',
    4326: 'Morlana Chicharra',
    4327: 'Flautilla Hamel\xc3\xadn',
    4328: 'Wagner',
    4329: 'Maruja Televenta',
    4330: 'Maestro Soniquete',
    4331: 'Celo Costelo',
    4332: 'Tato Timbal',
    4333: 'Chiflo Chiflete',
    4334: 'Maraco Marchoso',
    5001: 'Funcionario del cuartel general',
    5002: 'Funcionario del cuartel general',
    5003: 'Funcionaria del cuartel general',
    5004: 'Funcionaria del cuartel general',
    5005: 'Dependienta Azucena',
    5006: 'Dependiente Jacinto',
    5007: 'Florinda Rosales',
    5101: 'Pepe Pino',
    5102: 'Alca Chofa',
    5103: 'Federico Tilla',
    5104: 'Polillo Marip\xc3\xb3sez',
    5105: 'Comino P\xc3\xa9rez Gil',
    5106: 'Patillo Siegacogotes',
    5107: 'Cartero Felipe',
    5108: 'Posadera Piti',
    5109: 'Funcionario del cuartel general',
    5110: 'Funcionario del cuartel general',
    5111: 'Funcionaria del cuartel general',
    5112: 'Funcionaria del cuartel general',
    5113: 'Dr. Zanahorio',
    5114: 'Marchito Mate',
    5115: 'Mimosa Nomeolvides',
    5116: 'Lucho Borrajo',
    5117: 'P\xc3\xa9talo',
    5118: 'Palomo Ma\xc3\xadz',
    5119: 'Seto Podal',
    5120: 'Cardamomo',
    5121: 'Grosella Falsa',
    5122: 'Trufo Champi\xc3\xb1\xc3\xb3n',
    5123: 'Tempranilla M\xc3\xb3stez',
    5124: 'Hinojo Hinault',
    5125: 'Burbujo Chof',
    5126: 'Madre Selva',
    5127: 'Pili Polen',
    5128: 'Barba Coa',
    5201: 'Pulgarcillo',
    5202: 'Edel Weiss',
    5203: 'Campanilla',
    5204: 'Pipe Barroso',
    5205: 'Le\xc3\xb3n Mondadientes',
    5206: 'Cardo Borriquero',
    5207: 'Flor Chorro',
    5208: 'Lisa Buesa',
    5209: 'Funcionario del cuartel general',
    5210: 'Funcionario del cuartel general',
    5211: 'Funcionaria del cuartel general',
    5212: 'Funcionaria del cuartel general',
    5213: 'Al Cornoque',
    5214: 'Hortensia Comopincha',
    5215: 'Josefa Repera',
    5216: 'Luisillo Membrillo',
    5217: 'An\xc3\xadbal Nomeolvides',
    5218: 'Rufo Segadora',
    5219: 'Sacha Cachas',
    5220: 'Lenti Juela',
    5221: 'Flamenca Rosa',
    5222: 'Belladona Jazm\xc3\xadn',
    5223: 'Frido Quememojo',
    5224: 'Guido Casta\xc3\xb1apilonga',
    5225: 'Pipa Giras\xc3\xb3lez',
    5226: 'Rumio Cuentauvas',
    5227: 'Petunia Barricarroble',
    5228: 'Prior Primo Prelado',
    9001: 'Belinda Traspuesta',
    9002: 'Bello Durmiente',
    9003: 'Plancho Rejas',
    9004: 'Funcionaria del cuartel general',
    9005: 'Funcionaria del cuartel general',
    9006: 'Funcionario del cuartel general',
    9007: 'Funcionario del cuartel general',
    9008: 'Dependienta Modorra',
    9009: 'Dependiente Modorro',
    9010: 'Almohado Edred\xc3\xb3n',
    9101: 'Vito',
    9102: 'Pl\xc3\xbambea Triz',
    9103: 'Cafe\xc3\xadno Paloseco ',
    9104: 'Copito de Nieve',
    9105: 'Profesor Bostezo',
    9106: 'Sopor\xc3\xadfero Indolente',
    9107: 'Acurruco Paloma',
    9108: 'So\xc3\xb1o Liento',
    9109: 'Dafne Marmota',
    9110: 'Adela Duermevela',
    9111: 'Apag\xc3\xb3n Pl\xc3\xb3mez',
    9112: 'Marqu\xc3\xa9s de la Nana',
    9113: 'Jaime Cuco',
    9114: 'M\xc3\xa1scara Pep\xc3\xadnez',
    9115: 'Hiberno Cuandoquiero',
    9116: 'Mariano Cuentaovejas',
    9117: 'Madrugona Grogui',
    9118: 'Estrella Vespertina',
    9119: 'Tronco S\xc3\xb3pez',
    9120: 'Lirona Frita',
    9121: 'Serena Vigilia',
    9122: 'Trasnocho Pocho',
    9123: 'Osito Pel\xc3\xbachez',
    9124: 'Vela Zascandil',
    9125: 'Dr. Vig\xc3\xadliez',
    9126: 'Pluma Oca',
    9127: 'Pili Piltra',
    9128: 'Juanjo Manitas',
    9129: 'Beltr\xc3\xa1n Puesto',
    9130: 'Siesto Buenasn\xc3\xb3chez',
    9131: 'Let\xc3\xa1rgica Catorcehoras',
    9132: 'Funcionaria del cuartel general',
    9133: 'Funcionaria del cuartel general',
    9134: 'Funcionaria del cuartel general',
    9135: 'Funcionaria del cuartel general' }
zone2TitleDict = {
    2513: ('Ayuntamiento', 'el'),
    2514: ('Banco de Toontown', 'el'),
    2516: ('Colegio de Toontown', 'el'),
    2518: ('Biblioteca de Toontown', 'la'),
    2519: ('Tienda de Bromas', 'la'),
    2520: ('Cuartel General Dibu', 'el'),
    2521: ('Tienda de Ropa de Toontown', 'la'),
    2601: ('Cl\xc3\xadnica Dental Pi\xc3\xb1atasana', 'la'),
    2602: ('', ''),
    2603: ('Mineros Carboneros', 'los'),
    2604: ('Limpiezas por Piezas', 'las'),
    2605: ('F\xc3\xa1brica de Carteles de Toontown', 'la'),
    2606: ('', ''),
    2607: ('Habas saltarinas', 'las'),
    2610: ('Dr. Tom\xc3\xa1s Todonte', 'el'),
    2611: ('', ''),
    2616: ('Tienda de Disfraces Barbarrara', 'la'),
    2617: ('Acrobacias a Granel', 'las'),
    2618: ('Chistes Lepetitivos', 'los'),
    2621: ('Aviones de Papel', 'los'),
    2624: ('Perros Gamberros', 'los'),
    2625: ('Pasteler\xc3\xada Moho Feliz', 'la'),
    2626: ('Reparaci\xc3\xb3n de Bromas', 'las'),
    2629: ('El Rinc\xc3\xb3n de la Risa', 'el'),
    2632: ('Academia de Payasos', 'la'),
    2633: ('Sal\xc3\xb3n de T\xc3\xa9 La Tetera', 'el'),
    2638: ('Willie, el Barco de Vapor', ''),
    2639: ('Travesuras Simiescas', 'las'),
    2643: ('Botellas Enlatadas', 'las'),
    2644: ('Bromas Ligeras', 'las'),
    2649: ('Tienda de Juegos', 'la'),
    2652: ('', ''),
    2653: ('', ''),
    2654: ('Clases de Re\xc3\xadr', 'las'),
    2655: ('Caja de Ahorros Pastagansa', 'la'),
    2656: ('Coches Usados de Payasos', 'los'),
    2657: ('Bromas a Tutipl\xc3\xa9n', 'las'),
    2659: ('Calambres Reunidos Amp\xc3\xa9rez', 'los'),
    2660: ('Cosquilladores Autom\xc3\xa1ticos', 'los'),
    2661: ('Chuches Chucho', ''),
    2662: ('Dr. Eufo Rico', 'el'),
    2663: ('Don Rat\xc3\xb3n Se Va De Vacaciones', ''),
    2664: ('Mimos Mimosos', 'los'),
    2665: ('Agencia de Viajes Corremillas', 'la'),
    2666: ('Gasolinera Desternillante', 'la'),
    2667: ('Tiempos Felices', 'los'),
    2669: ('Globos Cobos', 'los'),
    2670: ('Tenedores de Sopa', 'los'),
    2671: ('Cuartel General Dibu', 'el'),
    2701: ('', ''),
    2704: ('Un Marinerito Valiente', ''),
    2705: ('Matracas Calandracas', 'las'),
    2708: ('Cola Azul', 'la'),
    2711: ('Oficina de Correos de Toontown', 'la'),
    2712: ('Caf\xc3\xa9 La Monda', 'el'),
    2713: ('Caf\xc3\xa9 Chachi', 'el'),
    2714: ('Un Tranv\xc3\xada En Apuros', ''),
    2716: ('Calditos Carcajada', 'los'),
    2717: ('Latas Embotelladas', 'las'),
    2720: ('Taller Despilporre', 'el'),
    2725: ('', ''),
    2727: ('Botellas y Latas Lat\xc3\xb3nez', 'las'),
    2728: ('Nata Invisible', 'la'),
    2729: ('Peces Dorados de 14 Kilates', 'los'),
    2730: ('Noticias Jocosas', 'las'),
    2731: ('', ''),
    2732: ('Pasta P\xc3\xa1nfilo', 'la'),
    2733: ('Cometas de Plomo', 'los'),
    2734: ('Platillos y Ventosas', 'los'),
    2735: ('Detonaciones a Domicilio', 'las'),
    2739: ('Reparaci\xc3\xb3n de Chistes', 'las'),
    2740: ('Petardos Usados', 'los'),
    2741: ('', ''),
    2742: ('Cuartel General Dibu', 'el'),
    2743: ('Limpieza En Seco En Un Minueto', 'la'),
    2744: ('', ''),
    2747: ('Tinta Visible', 'la'),
    2748: ('Risa Deprisa', 'la'),
    2801: ('Cojines Mull\xc3\xaddez', 'los'),
    2802: ('Bolas de demolici\xc3\xb3n inflables', 'las'),
    2803: ('El Chico Del Carnaval', ''),
    2804: ('Cl\xc3\xadnica de Fisioterapia Tronchalomo', 'la'),
    2805: ('', ''),
    2809: ('Gimnasio Capirotazo', 'el'),
    2814: ('Un Dia De Atasco', ''),
    2818: ('Tartas volantes', 'las'),
    2821: ('', ''),
    2822: ('S\xc3\xa1ndwiches de pollo de goma', 'los'),
    2823: ('Helader\xc3\xada El cucurucho agudo', 'la'),
    2824: ('Las Locuras De Mickey', ''),
    2829: ('Salchichones y chichones', 'los'),
    2830: ('Melod\xc3\xadas de Zipi', 'las'),
    2831: ('Casa de las risillas del profesor Cosquillas', 'la'),
    2832: ('Cuartel General Dibu', 'el'),
    2833: ('', ''),
    2834: ('Sala de traumatolog\xc3\xada del hueso de la risa', 'la'),
    2836: ('', ''),
    2837: ('Seminarios sobre Risa persistente', 'los'),
    2839: ('Pasta pastosa', 'la'),
    2841: ('', ''),
    1506: ('Tienda de Bromas', 'la'),
    1507: ('Cuartel General Dibu', 'el'),
    1508: ('Tienda de Ropa', 'la'),
    1602: ('Flotadores Usados', 'los'),
    1604: ('Limpieza en Seco de Ropa Chorreantes', 'la'),
    1606: ('Relojer\xc3\xada Garfio', 'la'),
    1608: ('Quillas y Cosquillas', 'las'),
    1609: ('Echa el Cebo Magdaleno', ''),
    1612: ('Banco Gale\xc3\xb3n Hundido', 'el'),
    1613: ('Bufete Calamar, Pulpo & Sepia', 'el'),
    1614: ('Boutique U\xc3\xb1a Deslumbrante', 'la'),
    1615: ('Yates Todo a cien', 'el'),
    1616: ('Sal\xc3\xb3n de Belleza Barbanegra', 'el'),
    1617: ('\xc3\x93ptica El Vig\xc3\xada Miope', 'la'),
    1619: ('Cl\xc3\xadnica Quir\xc3\xbargica de Arboles', 'la'),
    1620: ('De Popa a Proa', ''),
    1621: ('Gimnasio Estibadores Fornidos', 'el'),
    1622: ('Accesorios El\xc3\xa9ctricos Rayas y Centollos', 'los'),
    1624: ('Reparaci\xc3\xb3n de Suelas de Buque', 'la'),
    1626: ('Ropa de etiqueta El Salm\xc3\xb3n Coqueto', 'la'),
    1627: ('Surtido de Bit\xc3\xa1coras de Beto Buque', 'el'),
    1628: ('At\xc3\xban de la Tuna', 'el'),
    1629: ('Cuartel General Dibu', 'el'),
    1701: ('Escuela de Enfermer\xc3\xada La Boya Pocha', 'la'),
    1703: ('Restaurante Chino Cocochas de Drag\xc3\xb3n', 'el'),
    1705: ('Velas y Bielas', 'las'),
    1706: ('Medusas para Ba\xc3\xb1eras', 'las'),
    1707: ('Regalos Tiburcio', 'los'),
    1709: ('Cata de Maranes', 'la'),
    1710: ('Surtido de Percebes', 'el'),
    1711: ('Restaurante Sal Gorda', 'el'),
    1712: ('Gimnasio Levad Anclas', 'el'),
    1713: ('Mapas Pasma', 'las'),
    1714: ('Posada Suelta el Carrete', 'la'),
    1716: ('Ba\xc3\xb1adores La Sirena con Piernas', 'las'),
    1717: ('Telas y Botones Oc\xc3\xa9ano Pac\xc3\xadfico', 'las'),
    1718: ('Servicio de Taxi Callo Encallado', 'el'),
    1719: ('Compa\xc3\xb1\xc3\xada de Aguas Lomo de Pato', 'la'),
    1720: ('Ca\xc3\xb1as y Barro', 'las'),
    1721: ('A Toda M\xc3\xa1quina', ''),
    1723: ('Algas Sepio', 'las'),
    1724: ('Anguilas Gustativas', 'las'),
    1725: ('Cangrejos y Aparejos Ajab', 'los'),
    1726: ('Con Cien Gaseosas por Banda', ''),
    1727: ('Los Remos del Volga', ''),
    1728: ('Centollos El Meollo', 'los'),
    1729: ('Cuartel General Dibu', 'el'),
    1802: ('N\xc3\xa1utico y As\xc3\xa9ptico', 'el'),
    1804: ('Gimnasio El Crust\xc3\xa1ceo Cachas', 'el'),
    1805: ('Comidas El Carrete Audaz', 'las'),
    1806: ('Sombrerer\xc3\xada Gorrotocho', 'la'),
    1807: ('Quillas al Pil Pil', 'las'),
    1808: ('Nudos Imposibles', 'los'),
    1809: ('Cubos Oxidados', 'los'),
    1810: ('M\xc3\xa1ster en Gesti\xc3\xb3n de Anclas', 'el'),
    1811: ('Canoas y Anchoas', 'las'),
    1813: ('Asesor\xc3\xada Vuela m\xc3\xa1s Alto', 'la'),
    1814: ('Apeadero Amarras Salvajes', 'el'),
    1815: ('Consulta del Dr. Diqueseco', 'la'),
    1818: ('Cafeter\xc3\xada Los Siete Mares', 'la'),
    1819: ('El Estibador Gourmet', ''),
    1820: ('Art\xc3\xadculos de Broma El Simp\xc3\xa1tico Maremoto', 'los'),
    1821: ('F\xc3\xa1brica de Conservas Dibuque', 'la'),
    1823: ('Restaurante El Molusco Feroz', 'el'),
    1824: ('Paletas y Maletas', 'las'),
    1825: ('Caballas Pura Sangre Pescader\xc3\xada', 'las'),
    1826: ('Sastrer\xc3\xada Croma\xc3\xb1\xc3\xb3n', 'la'),
    1828: ('Lastre Pepa Sastre', 'el'),
    1829: ('Estatuas de Gaviotas', 'las'),
    1830: ('Objetos N\xc3\xa1uticos Perdidos', 'los'),
    1831: ('Algas de Compa\xc3\xb1\xc3\xada', 'las'),
    1832: ('Surtido de M\xc3\xa1stiles', 'el'),
    1833: ('Trajes a Medida El Corsario Elegante', 'los'),
    1834: ('Timones de dise\xc3\xb1o', 'los'),
    1835: ('Cuartel General Dibu', 'el'),
    4503: ('Tienda de Bromas', 'la'),
    4504: ('Cuartel General Dibu', 'el'),
    4506: ('Tienda de Ropa de Toontown', 'la'),
    4603: ('Tambores Ropopompom', 'los'),
    4604: ('Comp\xc3\xa1s de Dos por Cuatro', 'el'),
    4605: ('Violines Bibi', 'los'),
    4606: ('Casa de las Casta\xc3\xb1uelas', 'la'),
    4607: ('Dibumoda Septiminod', 'la'),
    4609: ('Teclas de Piano Dorrem\xc3\xad', 'las'),
    4610: ('No Pierdan los Estribillos', ''),
    4611: ('A Bombo y Platillos Volantes', ''),
    4612: ('Cl\xc3\xadnica Dental Rotti', 'la'),
    4614: ('Peluquer\xc3\xada de Corcheas', 'la'),
    4615: ('Pizzer\xc3\xada Pizzicato', 'la'),
    4617: ('Mandolinas Mandonas', 'las'),
    4618: ('Cuartos para Cuartetos', 'los'),
    4619: ('Pentagramas a la Carta', 'los'),
    4622: ('Almohadas Acompasadas', 'las'),
    4623: ('Bemoles a Cien', 'los'),
    4625: ('Tuba de Pasta de Dientes', 'la'),
    4626: ('Solfeo a Granel', ''),
    4628: ('Seguros a Tercetos', 'los'),
    4629: ('Platillos de Papel', 'los'),
    4630: ('Tocata y Fuga de Alcatraz', 'la'),
    4631: ('Tocatas de Tortilla', 'las'),
    4632: ('Tienda Abierta los 24 Tiempos', 'la'),
    4635: ('Tenores de Alquiler', 'los'),
    4637: ('Afinado de Platillos', 'el'),
    4638: ('Cuartetos de Heavy Metal', 'los'),
    4639: ('Antig\xc3\xbcedades La Flauta de No\xc3\xa9', 'las'),
    4641: ('Noticiero La Voz de la Soprano', 'el'),
    4642: ('Limpieza en Seco en un Minueto', 'la'),
    4645: ('Dibudisco', 'el'),
    4646: ('', ''),
    4648: ('Mudanzas Berganza', 'las'),
    4649: ('', ''),
    4652: ('Regalos Clave de Luna', 'los'),
    4653: ('', ''),
    4654: ('Puertas Tannh\xc3\xa4user', 'las'),
    4655: ('Escuela de Cocina Sonata a la Sal', 'la'),
    4656: ('', ''),
    4657: ('Barber\xc3\xada El Cuarteto Afeitador', 'la'),
    4658: ('Pianos en Ca\xc3\xadda Libre', 'los'),
    4659: ('Cuartel General Dibu', 'el'),
    4701: ('Escuela de Baile El Pasodoble Zapateado', 'la'),
    4702: ('\xc2\xa1M\xc3\xa1s Madera! Le\xc3\xb1adores Mel\xc3\xb3dicos', ''),
    4703: ('Tenor al por Menor', 'el'),
    4704: ('Sonatas y Sonatinas', 'las'),
    4705: ('C\xc3\xadtaras al Peso', 'las'),
    4707: ('Estudio de Efectos Doppler', 'el'),
    4709: ('Escala Escalada Aparejos de Escalada', 'la'),
    4710: ('Escuela de Conducci\xc3\xb3n Marcha y Contrafuga', 'la'),
    4712: ('Reparaci\xc3\xb3n de Pinchazos de Oboes', 'la'),
    4713: ('Vaqueros Strauss', 'los'),
    4716: ('Arm\xc3\xb3nicas Polif\xc3\xb3nicas', 'las'),
    4717: ('Seguros de Coches Un Acorde\xc3\xb3n en la Guantera', 'los'),
    4718: ('Utensilios de Cocina Cascanueces', 'los'),
    4719: ('Caravanas Madrigal', 'las'),
    4720: ('Tararea esa Dibucanci\xc3\xb3n', 'la'),
    4722: ('Oberturas para Oboe', 'las'),
    4723: ('Jugueter\xc3\xada El Xil\xc3\xb3fono de Plastilina', 'la'),
    4724: ('Cacofon\xc3\xadas a Domicilio', 'las'),
    4725: ('El Barbero Bar\xc3\xadtono', ''),
    4727: ('Planchado de Cuerdas Vocales', 'el'),
    4728: ('Ablanda\x3miento de O\xc3\xaddos Duros', 'el'),
    4729: ('Librer\xc3\xada El Violoncelo Celoso', 'la'),
    4730: ('Letras Pat\xc3\xa9ticas', 'las'),
    4731: ('Melodibus', 'los'),
    4732: ('Compa\xc3\xb1\xc3\xada de Teatro El Flaut\xc3\xadn de Venecia', 'la'),
    4733: ('', ''),
    4734: ('', ''),
    4735: ('Acordeones para Amenizar Reuniones', 'las'),
    4736: ('Bodas F\xc3\xadgaro', 'las'),
    4737: ('Arpas de Esparto', 'las'),
    4738: ('Regalos La Balalaica Silvestre', 'los'),
    4739: ('Cuartel General Dibu', 'el'),
    4801: ('Organillos en Est\xc3\xa9reo', 'los'),
    4803: ('Florister\xc3\xada El Sombrero de Tres Ficus', 'la'),
    4804: ('Escuela de Hosteler\xc3\xada El Platillo Danzar\xc3\xadn', 'la'),
    4807: ('Tr\xc3\xa9molos Embotellados', 'los'),
    4809: ('Allegros Tristes', 'los'),
    4812: ('', ''),
    4817: ('Pajarer\xc3\xada Pedro y el Lobo', 'la'),
    4819: ('Ukeleles de Uki', 'los'),
    4820: ('', ''),
    4821: ('Gramolas Juanola', 'las'),
    4827: ('Relojer\xc3\xada La Danza de las Horas', 'la'),
    4828: ('Zapater\xc3\xada Masculina Claqu\xc3\xa9 para Ciempies', 'la'),
    4829: ('Ca\xc3\xb1ones Pachelbel', 'los'),
    4835: ('Cascabeles para Gatos', 'los'),
    4836: ('Regalos Reggae', 'los'),
    4838: ('Academia de Canto Gr\xc3\xa1jez', 'la'),
    4840: ('Bebidas Musicales Cocapiano Cola', 'las'),
    4841: ('Liras Palmira', 'las'),
    4842: ('S\xc3\xadncopas Hechas a Mano', 'las'),
    4843: ('', ''),
    4844: ('Motocicletas Harley Mendelson', 'las'),
    4845: ('Eleg\xc3\xadas Elegantes de Elisa', 'las'),
    4848: ('Caja de ahorros Guita Ram\xc3\xb3n', 'la'),
    4849: ('', ''),
    4850: ('Empe\xc3\xb1os La Cuerda Prestada', 'los'),
    4852: ('Fundas para Flautas', 'las'),
    4853: ('Guitarras a Vapor Leo', 'las'),
    4854: ('V\xc3\xaddeos de Valquirias y Violines', 'los'),
    4855: ('C\xc3\xadmbalos a Domicilio', 'los'),
    4856: ('', ''),
    4862: ('Pasodobles, Pasotriples y Pasocu\xc3\xa1druples', 'los'),
    4867: ('Liquidaci\xc3\xb3n de Violoncelos', 'la'),
    4868: ('', ''),
    4870: ('Timbales y Tambores de Titanio', 'los'),
    4871: ('Clarines, Clarinetes y Chifletes', 'los'),
    4872: ('Marimbas, Matracas y Maracas', 'las'),
    4873: ('Cuartel General Dibu', 'el'),
    5501: ('Tienda de Bromas', 'la'),
    5502: ('Cuartel General Dibu', 'el'),
    5503: ('Tienda de Ropa', 'la'),
    5601: ('\xc3\x93ptica Zanahoria a Tutipl\xc3\xa9n', 'la'),
    5602: ('Corbatas Pino', 'las'),
    5603: ('Lechuga a Granel', 'la'),
    5604: ('Listas de Bodas Nomeolvides', 'las'),
    5605: ('Compa\xc3\xb1\xc3\xada de Aguas de Borrajas', 'la'),
    5606: ('P\xc3\xa9talos', 'los'),
    5607: ('Correos Florestales', 'los'),
    5608: ('Palomitas y Palomitos de Ma\xc3\xadz', 'las'),
    5609: ('Enredaderas de Compa\xc3\xb1\xc3\xada', 'las'),
    5610: ('Betunes El Tulip\xc3\xa1n Negro', 'los'),
    5611: ('Bromas Cardamomo', 'las'),
    5613: ('Peluqueros Siegacogotes', 'los'),
    5615: ('Semillas para Cotillas', 'las'),
    5616: ('Posada Coli Flor de Pitimin\xc3\xad', 'la'),
    5617: ('Mariposas de Encargo', 'los'),
    5618: ('Guisantes Farsantes', 'los'),
    5619: ('Comino Importante', 'el'),
    5620: ('Hierbabuenas Tardes', 'las'),
    5621: ('Vi\xc3\xb1as Lejanas', 'las'),
    5622: ('Bicicletas Hinojo Hinault', 'las'),
    5623: ('Jacuzzis para Gorriones', 'los'),
    5624: ('Madreselva Tropical', 'la'),
    5625: ('Pa\xc3\xb1ales para Panales', 'los'),
    5626: ('Zarzaparrillas de Carb\xc3\xb3n', 'las'),
    5627: ('Cuartel General Dibu', 'el'),
    5701: ('Espinacas de Dise\xc3\xb1o', 'las'),
    5702: ('Rastrillos Miga de Pan', 'los'),
    5703: ('Fotograf\xc3\xada La Flor de un D\xc3\xada', 'la'),
    5704: ('Coches Usados Campanilla', 'los'),
    5705: ('Colchones Suavec\xc3\xa1ctus', 'los'),
    5706: ('Joyer\xc3\xada La Pulsera de Chopo', 'la'),
    5707: ('Fruta Musical', 'la'),
    5708: ('Agencia de Viajes Villadiego', 'la'),
    5709: ('Cortac\xc3\xa9sped Amor de Hortelano', 'el'),
    5710: ('Gimnasio Espantalobos', 'el'),
    5711: ('Calceter\xc3\xada Lentejuela Guisada', 'la'),
    5712: ('Estatuas Bobas', 'las'),
    5713: ('Jabones de Higo Chumbo', 'los'),
    5714: ('Agua de Lluvia Embotellada', 'el'),
    5715: ('Noticiario Telecasta\xc3\xb1a', 'el'),
    5716: ('Caja de Ahorros y Monte de Or\xc3\xa9gano', 'la'),
    5717: ('La Flor Chorreante', ''),
    5718: ('Animales Ex\xc3\xb3ticos Diente de Le\xc3\xb3n', 'los'),
    5719: ('Agencia de Detectives Azotalenguas', 'la'),
    5720: ('Ropa Masculina Borriquero', 'la'),
    5721: ('Comidas Alfalfa Romeo', 'las'),
    5725: ('Destiler\xc3\xada Malta Cibelina', 'la'),
    5726: ('Barro a Granel', 'el'),
    5727: ('Pr\xc3\xa9stamos y Empr\xc3\xa9stitos Praderas Primitivas', 'los'),
    5728: ('Cuartel General Dibu', 'el'),
    9501: ('Biblioteca Sobetotal', 'la'),
    9503: ('Bar La Cabezadita Tonta', 'el'),
    9504: ('Tienda de Bromas', 'la'),
    9505: ('Cuartel General Dibu', 'el'),
    9506: ('Tienda de Ropa de Toontown', 'la'),
    9601: ('Posada Pluma de Ganso', 'la'),
    9602: ('Siestas a Domicilio', 'las'),
    9604: ('Fundas N\xc3\xb3rdicas para Pinreles', 'las'),
    9605: ('Avenida de la Canci\xc3\xb3n de Cuna, 323', 'la'),
    9607: ('Pijamas de Plomo para Dormir de Pie', 'el'),
    9608: ('', ''),
    9609: ('Arrullos a Granel', 'los'),
    9613: ('Los Limpiadores Del Reloj', ''),
    9616: ('Compa\xc3\xb1\xc3\xada El\xc3\xa9ctrica Luces Fuera', 'la'),
    9617: ('Avenida de la Canci\xc3\xb3n de Cuna, 212', 'la'),
    9619: ('Sopas Sopor\xc3\xadferas', 'las'),
    9620: ('Servicio de Taxis Insomnes', 'el'),
    9622: ('Relojer\xc3\xada El Cuco Dormido', 'la'),
    9625: ('Sal\xc3\xb3n de Belleza El Ronquido Alegre', 'el'),
    9626: ('Avenida de la Canci\xc3\xb3n de Cuna, 818', 'la'),
    9627: ('Mecedoras Autom\xc3\xa1ticas', 'las'),
    9628: ('Calendarios Nocturnos', 'los'),
    9629: ('Avenida de la Canci\xc3\xb3n de Cuna, 310', 'la'),
    9630: ('Serrer\xc3\xada Como un Tronco', 'la'),
    9631: ('Arreglo de Relojes Estoysopa', 'el'),
    9633: ('La Siesta De Pluto', ''),
    9634: ('Colchones La Pluma Audaz', 'los'),
    9636: ('Seguro Contra Insomnios', 'el'),
    9639: ('Conservas Ultrahibernadas', 'las'),
    9640: ('Avenida de la Canci\xc3\xb3n de Cuna, 805', 'la'),
    9642: ('Ganader\xc3\xada Cuentaovejas', 'la'),
    9643: ('\xc3\x93ptica Nopegojo', 'la'),
    9644: ('Peleas de Almohadas Organizadas', 'las'),
    9645: ('Posada Todos al Sobre', 'la'),
    9647: ('\xc2\xa1Hazte la cama! Ferreter\xc3\xada', ''),
    9649: ('Ronquidos Lejanos', 'los'),
    9650: ('Avenida de la Canci\xc3\xb3n de Cuna, 714', 'la'),
    9651: ('Martillos para Despertadores', 'los'),
    9652: ('', ''),
    3507: ('Tienda de Bromas', 'la'),
    3508: ('Cuartel General Dibu', 'el'),
    3509: ('Tienda de Ropa', 'la'),
    3601: ('Compa\xc3\xb1\xc3\xada El\xc3\xa9ctrica Polo Norte', 'la'),
    3602: ('Gorros de Nieve Geli', 'los'),
    3605: ('', ''),
    3607: ('Ventisca a la Vista', 'la'),
    3608: ('Bobsled para Lactantes', ''),
    3610: ('Hipermercado Esquimal de Mito', 'el'),
    3611: ('Quitanieves Esc\xc3\xa1rchez', 'la'),
    3612: ('Dise\xc3\xb1o de Igl\xc3\xbas', 'el'),
    3613: ('Bicicletas Car\xc3\xa1mbanez', 'las'),
    3614: ('Cereales Copos de Nieve', 'los'),
    3615: ('Arenques en Alm\xc3\xadbar', 'los'),
    3617: ('Dirigibles de Aire Fr\xc3\xado', 'los'),
    3618: ('\xc2\xbfAvalancha? Sin Problemas Gesti\xc3\xb3n de Crisis', 'la'),
    3620: ('Cl\xc3\xadnica de Esqu\xc3\xad', 'la'),
    3621: ('Bar El Deshielo', 'el'),
    3622: ('', ''),
    3623: ('Panes Criogenizados Frigomiga', 'los'),
    3624: ('Bocadillos Bajocero', 'los'),
    3625: ('Radiadores de la T\xc3\xada Ritona', 'los'),
    3627: ('Adiestramiento de San Bernardos', 'el'),
    3629: ('Cafeter\xc3\xada El Braserillo que R\xc3\xade', 'la'),
    3630: ('Agencia de Viajes T\xc3\xa9mpano Tenaz', 'la'),
    3634: ('Remontes Rascafr\xc3\xada', 'los'),
    3635: ('Le\xc3\xb1a Usada', 'la'),
    3636: ('Surtido de Saba\xc3\xb1ones', 'el'),
    3637: ('Patines Pati', 'los'),
    3638: ('Trineos y Cuatrineos', 'los'),
    3641: ('Camas Heladas Pepe Tundra', 'las'),
    3642: ('\xc3\x93ptica El Yeti Tuerto', 'la'),
    3643: ('Sal\xc3\xb3n de la Bola de Nieve', 'el'),
    3644: ('Cubitos de Hielo Fundidos', 'los'),
    3647: ('Alquiler de Chaqu\xc3\xa9s El Ping\xc3\xbcino Beduino', 'el'),
    3648: ('Hielo Instant\xc3\xa1neo', 'el'),
    3649: ('Hambrrrrguesas', 'las'),
    3650: ('Antig\xc3\xbcedades Ant\xc3\xa1rticas', 'las'),
    3651: ('Perritos Helados Pipe', 'los'),
    3653: ('Joyer\xc3\xada Fr\xc3\xado como el Diamante', 'la'),
    3654: ('Cuartel General Dibu', 'el'),
    3702: ('Almac\xc3\xa9n de Invierno', 'el'),
    3703: ('', ''),
    3705: ('Car\xc3\xa1mbanos a Granel', 'los'),
    3706: ('Batidos El Tembleque', 'los'),
    3707: ('Hogar, G\xc3\xa9lido Hogar', ''),
    3708: ('Plut\xc3\xb3n en tu Casa', ''),
    3710: ('Comidas Alaska en Enero', 'las'),
    3711: ('', ''),
    3712: ('Tuber\xc3\xadas Muy Muy Fr\xc3\xadas', 'las'),
    3713: ('Dentista El Casta\xc3\xb1eteo Perpetuo', 'el'),
    3715: ('Surtido de Sopitas de la T\xc3\xada \xc3\x81rtica', 'el'),
    3716: ('Sal Gorda para Carreteras', 'la'),
    3717: ('Polos y Helados Variados', 'los'),
    3718: ('Calefacci\xc3\xb3n a Domicilio', 'la'),
    3719: ('Pat\xc3\xa9 de Cubitos', 'el'),
    3721: ('Trineos de Ocasi\xc3\xb3n', 'los'),
    3722: ('Tienda de Esqu\xc3\xad Anchoa', 'la'),
    3723: ('Guantes de Nieve Tiritonio', 'los'),
    3724: ('La Voz de la Tundra', 'la'),
    3725: ('Me Mareo en Trineo', ''),
    3726: ('Mantas El\xc3\xa9ctricas Solares', 'las'),
    3728: ('Quitanieves Cenutrio', 'el'),
    3729: ('', ''),
    3730: ('Desguace de Mu\xc3\xb1ecos de Nieve', 'el'),
    3731: ('Chimeneas Port\xc3\xa1tiles', 'las'),
    3732: ('La Nariz Helada', ''),
    3734: ('T\xc3\xadmpanos como T\xc3\xa9mpanos Otorrino', 'los'),
    3735: ('Forros Polares de Papel', 'los'),
    3736: ('Cucuruchos de Hielo Picado', 'los'),
    3737: ('Comidas Eslalon', 'las'),
    3738: ('Escondites Fr\xc3\xado Fr\xc3\xado', 'los'),
    3739: ('Cuartel General Dibu', 'el') }
SuitInvasionBegin1 = 'Cuartel general: \xc2\xa1\xc2\xa1Hay una invasi\xc3\xb3n de bots!!'
SuitInvasionBegin2 = 'Cuartel general: \xc2\xa1\xc2\xa1Los %s han tomado Toontown!!!'
SuitInvasionEnd1 = 'Cuartel general: \xc2\xa1\xc2\xa1\xc2\xa1La invasi\xc3\xb3n de %s ha terminado!!!'
SuitInvasionEnd2 = 'Cuartel general: \xc2\xa1\xc2\xa1\xc2\xa1Los dibus han vuelto a salvarnos!!!'
SuitInvasionUpdate1 = 'Cuartel general: \xc2\xa1\xc2\xa1\xc2\xa1La invasi\xc3\xb3n de bots consta ahora de %s bots!!!'
SuitInvasionUpdate2 = 'Cuartel general: \xc2\xa1\xc2\xa1\xc2\xa1Debemos derrotar a esos %s!!!'
SuitInvasionBulletin1 = 'Cuartel general: \xc2\xa1\xc2\xa1\xc2\xa1Se est\xc3\xa1 produciendo una invasi\xc3\xb3n de bots!!!'
SuitInvasionBulletin2 = 'Cuartel general: \xc2\xa1\xc2\xa1Los %s han tomado Toontown!!!'
LeaderboardTitle = 'Pelot\xc3\xb3n de dibus'
QuestScriptTutorialMickey_1 = '\xc2\xa1Toontown tiene un nuevo habitante! \xc2\xbfTienes alguna broma de sobra?'
QuestScriptTutorialMickey_2 = '\xc2\xa1Claro, %s!'
QuestScriptTutorialMickey_3 = 'Tato Tutorial te lo explicar\xc3\xa1 todo sobre los bots.\x7\xc2\xa1Tengo que irme!'
QuestScriptTutorialMickey_4 = '\xc2\xa1Ven aqu\xc3\xad! Usa las flechas del teclado para moverte.'
QuestScript101_1 = '\xc3\x89sos son los BOTS. Son robots que intentan tomar el control de Toontown.'
QuestScript101_2 = 'Hay muchos tipos distintos de BOTS, que...'
QuestScript101_3 = '...convierten los alegres edificios de los dibus...'
QuestScript101_4 = '...\xc2\xa1en horribles edificios bot!'
QuestScript101_5 = '\xc2\xa1Pero los BOTS no aguantan las bromas!'
QuestScript101_6 = 'Una buena broma acaba con ellos.'
QuestScript101_7 = 'Hay un mont\xc3\xb3n de bromas, pero puedes empezar con \xc3\xa9stas.'
QuestScript101_8 = '\xc2\xa1Oh! \xc2\xa1Tambi\xc3\xa9n necesitas un ris\xc3\xb3metro!'
QuestScript101_9 = 'Si tu ris\xc3\xb3metro disminuye demasiado, te pondr\xc3\xa1s triste.'
QuestScript101_10 = '\xc2\xa1Cuanto m\xc3\xa1s contento est\xc3\xa1 un dibu, m\xc3\xa1s sano est\xc3\xa1!'
QuestScript101_11 = '\xc2\xa1OH, NO! \xc2\xa1Hay un BOT fuera de la tienda!'
QuestScript101_12 = '\xc2\xa1AY\xc3\x9aDAME, POR FAVOR! \xc2\xa1Derrota a ese BOT!'
QuestScript101_13 = '\xc2\xa1Aqu\xc3\xad tienes tu primera dibutarea!'
QuestScript101_14 = '\xc2\xa1Deprisa! \xc2\xa1Derrota a ese secuaz!'
QuestScript110_1 = 'Gracias por derrotar a ese secuaz. Te voy a dar un dibucuaderno...'
QuestScript110_2 = 'Es un cuaderno lleno de cosas chulas.'
QuestScript110_3 = '\xc3\x81brelo y te ir\xc3\xa9 ense\xc3\xb1ando cosas.'
QuestScript110_4 = 'El mapa te muestra d\xc3\xb3nde has estado.'
QuestScript110_5 = 'Pasa la p\xc3\xa1gina para ver tus bromas...'
QuestScript110_6 = '\xc2\xa1Vaya! \xc2\xa1No tienes bromas! Te voy a asignar una tarea.'
QuestScript110_7 = 'Pasa la p\xc3\xa1gina para ver las tareas.'
QuestScript110_8 = 'Para comprar bromas tienes que subirte al tranv\xc3\xada y conseguir gominolas.'
QuestScript110_9 = 'Para subirte al tranv\xc3\xada, sal por la puerta que hay detr\xc3\xa1s de m\xc3\xad y dir\xc3\xadgete al dibuparque.'
QuestScript110_10 = 'Ahora, cierra el dibucuaderno y busca el tranv\xc3\xada.'
QuestScript110_11 = 'Vuelve al cuartel general cuando hayas terminado. \xc2\xa1Chao!'
QuestScriptTutorialBlocker_1 = '\xc2\xa1Eh, hola!'
QuestScriptTutorialBlocker_2 = '\xc2\xbfHola?'
QuestScriptTutorialBlocker_3 = '\xc2\xa1Oh! \xc2\xa1No sabes c\xc3\xb3mo se usa la Charla r\xc3\xa1pida!'
QuestScriptTutorialBlocker_4 = 'Haz clic en el bot\xc3\xb3n para decir algo.'
QuestScriptTutorialBlocker_5 = '\xc2\xa1Muy bien!\x7En el sitio al que vas hay muchos dibus con los que puedes hablar.'
QuestScriptTutorialBlocker_6 = 'Si quieres charlar con tus amigos mediante el teclado, tienes que usar otro bot\xc3\xb3n.'
QuestScriptTutorialBlocker_7 = 'Es el bot\xc3\xb3n "Charla". Para poder usarlo tienes que ser habitante oficial de Toontown.'
QuestScriptTutorialBlocker_8 = '\xc2\xa1Buena suerte! \xc2\xa1Hasta luego!'
QuestScript120_1 = '\xc2\xa1Que bueno, encontraste el tranv\xc3\xada!\x7Por cierto, \xc2\xbfconoces ya a Pecunio el banquero?\x7Es bastante goloso.\x7\xc2\xbfPor qu\xc3\xa9 no te presentas llev\xc3\xa1ndole esta chocolatina como regalo?'
QuestScript120_2 = 'Pecunio el banquero est\xc3\xa1 en el Banco de Toontown.'
QuestScript121_1 = 'Mmm, gracias por la chocolatina.\x7Oye, si me ayudas, te dar\xc3\xa9 una recompensa.\x7Los bots han robado las llaves de mi caja fuerte. Derrota a los bots hasta recuperar la llave robada.\x7Cuando encuentres la llave, tr\xc3\xa1emela.'
QuestScript130_1 = '\xc2\xa1Que bueno, encontraste el tranv\xc3\xada!\x7Por cierto, hoy he recibido un paquete para Pedro el maestro.\x7Deben de ser las nuevas tizas que ha encargado.\x7\xc2\xbfPuedes llev\xc3\xa1rselas?\x7Est\xc3\xa1 en el colegio.'
QuestScript131_1 = 'Oh, gracias por las tizas.\x7\xc2\xa1\xc2\xbfQu\xc3\xa9?!\x7Los bots me han robado la pizarra. Derr\xc3\xb3tales y recupera mi pizarra.\x7Cuando la encuentres, tr\xc3\xa1emela.'
QuestScript140_1 = '\xc2\xa1Que bueno, encontraste el tranv\xc3\xada!\x7Por cierto, mi amigo Leopoldo es todo un devorador de libros.\x7La \xc3\xbaltima vez que estuve en Puerto Donald le recog\xc3\xad este libro.\x7\xc2\xbfPodr\xc3\xadas llev\xc3\xa1rselo? Suele estar en la biblioteca.'
QuestScript141_1 = 'Oh, s\xc3\xad, con este libro casi completar\xc3\xa9 mi colecci\xc3\xb3n.\x7D\xc3\xa9jame ver...\x7Vaya...\x7\xc2\xbfD\xc3\xb3nde habr\xc3\xa9 puesto las gafas?\x7Las ten\xc3\xada justo antes de que los bots ocupasen mi edificio.\x7Derr\xc3\xb3tales y recupera mis gafas.\x7Cuando las encuentres, tr\xc3\xa1emelas y te dar\xc3\xa9 una recompensa.'
QuestScript150_1 = 'Oh... \xc2\xa1Es posible que la tarea siguiente sea demasiado dif\xc3\xadcil para que la hagas solo!'
QuestScript150_2 = 'Para hacerte amigo de alguien, busca a otro jugador y pulsa el bot\xc3\xb3n Amigo nuevo.'
QuestScript150_3 = 'Cuando tengas un amigo nuevo, vuelve aqu\xc3\xad.'
QuestScript150_4 = '\xc2\xa1Algunas tareas son demasiado dif\xc3\xadciles para hacerlas solo!'
ClosetTimeoutMessage = 'Lo siento, el tiempo se\n te ha acabado.'
ClosetNotOwnerMessage = 'Este no es tu cl\xc3\xb3set, pero te puedes probar la ropa.'
ClosetPopupOK = 'Muy bien'
ClosetPopupCancel = 'Cancelar'
ClosetDiscardButton = 'Remover'
ClosetAreYouSureMessage = 'T\xc3\xba has borrado algunas prendas. \xc2\xbfRealmente quieres borrarlas ?'
ClosetYes = 'S\xc3\xad'
ClosetNo = 'No'
ClosetVerifyDelete = 'Borrar %s?'
ClosetShirt = 'Esta polera'
ClosetShorts = 'Estos shorts'
ClosetSkirt = 'Esta falda'
ClosetDeleteShirt = 'Borrar\npolera'
ClosetDeleteShorts = 'Borrar\nshorts'
ClosetDeleteSkirt = 'Borrar\nfalda'
EstateOwnerLeftMessage = 'Lo siento, el due\xc3\xb1o de esta propiedad se ha ido.  T\xc3\xba vas a ser enviado al dibuparque en %s segundos'
EstatePopupOK = 'Muy bien'
EstateTeleportFailed = 'No pude irme a la casa. \xc2\xa1Trata de nuevo!'
EstateTeleportFailedNotFriends = 'Lo siento, %s esta en una propiedad en la cual t\xc3\xba no tienes amigos.'
AvatarsHouse = 'Casa %s\n'
BankGuiCancel = 'Cancelar'
BankGuiOk = 'Aceptar'
DistributedBankNoOwner = 'Lo siento, este no es t\xc3\xba banco.'
DistributedBankNotOwner = 'Lo siento, este no es t\xc3\xba banco.'

def GetPossesive(name):
    return 'de:\n' + name

