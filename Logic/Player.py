import json
from Files.CsvLogic.Characters import Characters
from Files.CsvLogic.Emotes import Emotes
from Files.CsvLogic.Skins import Skins
from Files.CsvLogic.Cards import Cards
class Players:
	config = open('config.json', 'r')
	content = config.read()

	settings = json.loads(content)

	# Player data
	BPTOKEN = 0
	BPXP = 0
	quests = []
	freepass = 0
	buypass = 0
	# Brawler data
	skins_id = Skins().get_skins_id()
	brawlers_id = Characters().get_brawlers_id()
	card_skills_id = Cards().get_spg_id()
	card_unlock_id = Cards().get_brawler_unlock()
	emotes_id  = Emotes().get_emotes_id()
	high_id = 0
	low_id = 0
	token = "None"
	IsFacebookLinked = 0
	FacebookID = "None"
	FacebookToken = "None"
	box_id = 0
	map_id = 7
	slot_index = 0
	room_id = 0
	brawler_id = 0
	skin_id = 0
	dudu = 0
	bulletX = 1
	bulletY = 1
	hasbollX = 3150
	hasbollY = 4950
	angle = 0
	hasboll = False
	hasgoal = 1
	bulletCount = 0
	charge = 3000
	checker = 0
	inmm = False
	index = 0
	ccc = ""
	trioWINS = 0
	sdWINS = 0
	theme = 15
	#newprl
	highest_trophies = 0
	trophies = 0
	brawlers_trophies = {}
	for id in brawlers_id:
		brawlers_trophies.update({f'{id}': brawlers_trophies})
	
	brawlers_trophies = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0, "18": 0, "19": 0, "20": 0, "21": 0, "22": 0, "23": 0, "24": 0, "25": 0, "26": 0, "27": 0, "28": 0, "29": 0, "30": 0, "31": 0, "32": 0, "34": 0, "35": 0, "36": 0, "37": 0, "38": 0, "39": 0}
	bet = 0
	#lobby box
	box = 0
	bigbox = 0
	#lobby box end
	online = 2
	state = 0
	UnlockedBrawlers = {"0": 1, "1": 1, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0, "18": 0, "19": 0, "20": 0, "21": 0, "22": 0, "23": 0, "24": 0, "25": 0, "26": 0, "27": 0, "28": 0, "29": 0, "30": 0, "31": 0, "32": 0,"34": 0, "35": 0, "36": 0, "37": 0, "38": 0, "39": 0}
	brawlerPowerLevel = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0, "18": 0, "19": 0, "20": 0, "21": 0, "22": 0, "23": 0, "24": 0, "25": 0, "26": 0, "27": 0, "28": 0, "29": 0, "30": 0, "31": 0, "32": 0, "34": 0, "35": 0, "36": 0, "37": 0, "38": 0, "39": 0}
	brawlerPoints = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0, "18": 0, "19": 0, "20": 0, "21": 0, "22": 0, "23": 0, "24": 0, "25": 0, "26": 0, "27": 0, "28": 0, "29": 0, "30": 0, "31": 0, "32": 0, "34": 0, "35": 0, "36": 0, "37": 0, "38": 0, "39": 0}
	UnlockedSkins = {"0": 0,"1": 0,"2": 0,"3": 0,"4": 0,"5": 0,"6": 0,"7": 0,"8": 0,"9": 0,"10": 0,"11": 0,"12": 0,"13": 0,"14": 0,"15": 0,"16": 0,"17": 0,"18": 0,"19": 0,"20": 0,"21": 0,"22": 0,"23": 0,"24": 0,"25": 0,"26": 0,"27": 0,"28": 0,"29": 0,"30": 0,"31": 0,"32": 0,"33": 0,"34": 0,"35": 0,"36": 0,"37": 0,"38": 0,"39": 0,"40": 0,"41": 0,"42": 0,"43": 0,"44": 0,"45": 0,"46": 0,"47": 0,"48": 0,"49": 0,"50": 0,"51": 0,"52": 0,"53": 0,"54": 0,"55": 0,"56": 0,"57": 0,"58": 0,"59": 0,"60": 0,"61": 0,"62": 0,"63": 0,"64": 0,"65": 0,"66": 0,"67": 0,"68": 0,"69": 0,"70": 0,"71": 0,"72": 0,"73": 0,"74": 0,"75": 0,"76": 0,"77": 0,"78": 0,"79": 0,"80": 0,"81": 0,"82": 0,"83": 0,"84": 0,"85": 0,"86": 0,"87": 0,"88": 0,"89": 0,"90": 0,"91": 0,"92": 0,"93": 0,"94": 0,"95": 0,"96": 0,"97": 0,"98": 0,"99": 0,"100": 0,"101": 0,"102": 0,"103": 0,"104": 0,"105": 0,"106": 0,"107": 0,"108": 0,"109": 0,"110": 0,"111": 0,"112": 0,"113": 0,"114": 0,"115": 0,"116": 0,"117": 0,"118": 0,"119": 0,"120": 0,"121": 0,"122": 0,"123": 0,"124": 0,"125": 0,"126": 0,"127": 0,"128": 0,"129": 0,"130": 0,"131": 0,"132": 0,"133": 0,"134": 0,"135": 0,"136": 0,"137": 0,"138": 0,"139": 0,"140": 0,"141": 0,"142": 0,"143": 0,"144": 0,"145": 0,"146": 0,"147": 0,"148": 0,"149": 0,"150": 0,"151": 0,"152": 0,"153": 0,"154": 0,"155": 0,"156": 0,"157": 0,"158": 0,"159": 0,"160": 0,"161": 0,"162": 0,"163": 0,"164": 0,"165": 0,"166": 0,"167": 0,"168": 0,"169": 0,"170": 0,"171": 0,"172": 0,"173": 0,"174": 0,"175": 0,"176": 0,"177": 0,"178": 0,"179": 0,"180": 0,"181": 0,"182": 0,"183": 0,"184": 0,"185": 0,"186": 0,"187": 0,"188": 0,"189": 0,"190": 0,"191": 0,"192": 0,"193": 0,"194": 0,"195": 0,"196": 0,"197": 0,"198": 0,"199": 0,"200": 0,"201": 0,"202": 0,"203": 0,"204": 0,"205": 0,"206": 0,"207": 0,"208": 0,"209": 0,"210": 0,"211": 0,"212": 0,"213": 0,"214": 0,"215": 0,"216": 0,"217": 0,"218": 0,"219": 0,"220": 0,"221": 0,"222": 0,"223": 0,"224": 0,"225": 0,"226": 0,"227": 0,"228": 0,"229": 0,"230": 0,"231": 0,"232": 0,"233": 0,"234": 0,"235": 0,"236": 0,"237": 0,"238": 0,"239": 0,"240": 0,"241": 0,"242": 0,"243": 0,"244": 0,"245": 0,"246": 0,"247": 0,"248": 0,"249": 0,"250": 0,"251": 0,"252": 0,"253": 0,"254": 0,"255": 0,"256": 0,"257": 0,"258": 0,"259": 0,"260": 0,"261": 0,"262": 0,"263": 0,"264": 0,"265": 0,"266": 0,"267": 0,"268": 0,"269": 0,"270": 0,"271": 0,"272": 0,"273": 0,"274": 0,"275": 0,"276": 0,"277": 0,"278": 0,"279": 0}
	skinremove = 0
	brawlerem = 1
	starpoints = 0
	tickets = 0
	gems = 0
	gold = 100
	Troproad = 1
	profile_icon = 0
	name_color = 0
	player_experience = 0
	vip = 0
	# Socket
	ClientDict = {}


	# General player (Brawler, Currency, etc..)
	
	BrawlersUnlockedState = {}
	brawlers_spg_unlock = {} # For starpower and gadget
	gadget = 255
	starpower = 76

	name = "VBC26"
	player_experience = 0
	do_not_distrub = 0

	solo_wins = 0
	duo_wins = 0
	ThreeVSThree_wins = 0
	tokensdoubler = 0
	player_tokens = 0
	tokens = 0

	# Alliances
	club_high_id = 0
	club_low_id = 0
	club_role = 0

	# Message stuff...
	update_url = ''
	patch_url = ''
	patch_sha = ''
	maintenance_time = 0

	err_code = 7
	maintenance = False
	patch = False

	if settings['Patch']:
		error_code = 7
		patch = True

	if settings['Maintenance']:
		err_code = 10
		maintenance = True
		maintenance_time = settings['MaintenanceTime']

	# Chat data
	message_tick = 0
	bot_message_tick = 0

    # Friendly game (Teams, info, result)
	battle_result = 0
	game_type = 0
	use_gadget = 1
	ctick = 0
	gadget = 0
	starpower = 0
	isReady = 0
	message = 0
	rank = 0
	team = 0
	isReady = 0

	bot1 = 0
	bot1_n = None
	bot2 = 0
	bot2_n = None
	bot3 = 0
	bot3_n = None
	bot4 = 0
	bot4_n = None
	bot5 = 0
	bot5_n = None

	def CreateNewBrawlersList():
		Players.BrawlersUnlockedState = {}
		for id in Players.brawlers_id:
			if id == 0:
				Players.BrawlersUnlockedState[str(id)] = 1
			else:
				Players.BrawlersUnlockedState[str(id)] = 0
		return Players.BrawlersUnlockedState

	def __init__(self, device):
		self.device = device
