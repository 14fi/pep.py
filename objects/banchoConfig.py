# TODO: Rewrite this shit
from common import generalUtils
from constants import serverPackets
from objects import glob
from common.log import logUtils as log


class banchoConfig:
	"""
	Class that loads settings from bancho_settings db table
	"""

	config = {"banchoMaintenance": False, "freeDirect": True, "menuIcon": "", "loginNotification": ""}

	def __init__(self, loadFromDB = True):
		"""
		Initialize a banchoConfig object (and load bancho_settings from db)

		loadFromDB -- if True, load values from db. If False, don't load values. Optional.
		"""
		if loadFromDB:
			try:
				self.loadSettings()
			except:
				raise


	def loadSettings(self):
		"""
		(re)load bancho_settings from DB and set values in config array
		"""
		self.config["banchoMaintenance"] = generalUtils.stringToBool(glob.db.fetch("SELECT value_int FROM bancho_settings WHERE name = 'bancho_maintenance'")["value_int"])
		self.config["freeDirect"] = generalUtils.stringToBool(glob.db.fetch("SELECT value_int FROM bancho_settings WHERE name = 'free_direct'")["value_int"])
		mainMenuIcon = glob.db.fetch("SELECT file_id, url FROM main_menu_icons WHERE is_current = 1 LIMIT 1")
		if mainMenuIcon is None:
			self.config["menuIcon"] = ""
		else:
			imageURL = "https://i.ppy.sh/{}.png".format(mainMenuIcon["file_id"])
			self.config["menuIcon"] = "{}|{}".format(imageURL, mainMenuIcon["url"])
		#self.config["loginNotification"] = glob.db.fetch("SELECT value_string FROM bancho_settings WHERE name = 'login_notification'")["value_string"]
		self.config["Quotes"] = [
			"Welcome to osuHOW!",
			"sakuru is a loli",
			"t r i a n g l e s",
			"gamer'd",
			"peppy did a bad job on my taxes",
			"osu!2013 GAMING",
			"c.osuhow.cf",
			"peppycode",
			"ripplecode",
			"bad python code",
			"HOWosu",
			"bad server",
			"peppy GET OUT",
			"If you don't play osu!, well, I don't even know how you got here!",
			"osu bad game",
			"disco prince",
			"habbas is funny",
			"buy the c o i n s",
			"no cbcc allowed, seriously, i unranked it!",
			"realistikdash why did you cheat on my old server",
			"neko cucucumber",
			"help my pc is on fire",
			"bad game",
			"i installed osu on my toaster",
			"peppy open up",
			"Activate Windows",
			"hha funi nubmer guysz psl liek an subscrbe",
			"peppy (osu osx)",
			"Go to Settings to activate Windows.",
			"i hate u ripple",
			"Second biggest exporter of triangles!",
			'"yuuor amd" -hubz',
			"You received a glizzy from 'BanchoBot'. Click to eat it!",
			"sakuru's credit card number is 5",
			"they found irregularities in the pension fund scoob",
			"help i accidentally built a shelf",
			"asbestos style",
			"!",
			"miiiiine diiamonndsss",
			"nokaia ringtime arabic",
			"pizza timing",
			"this post has been provel false by real federal agents",
			"cool, awesome!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
			"add more egg",
			"Sakuru has rankedrankedrankedrankedrankedrankedrankedrankedrankedranked beatmapset 259",
			'"i swear my server gets worse every day" -Sakuru"',
			'[2022-06-04 18:27:32] WARNING - no',
			"bruh",
			"i am no breakthelawer",
			"i no use lovesmack",
			"OYOYOYOYOYOYOYOYOYOYOYOYOYOYOY",
			"i installed gentoo on my toaster",
			"the only osu! server with nutella between the cpu and heatsink",
			"obama do you like my plane",
			"!important !important !important !important !important !important !important !important !important",
			"rock n roll mcdonalds",
			"mcdonalds and you",
			"my iq is a negative number!",
			"i made pancakes at 3 am",
			"h a c k y o u",
			"obama used to have cat ears but he lost them in the war",
			"whitecat lost his #1 because he didnt have crystal button",
			"https://shine.osuhow.cf/api/v1/users/favourites?id=1000",
			"free tech tip: insert butter into usb port, speed!",
			"my cat proves the earth is flat",
			"tux racer best game",
			"CRAZY HAMBORGER IS TERRIBLE",
			"i am sorry for my stupid inside jokes",
			"d-d-d-d-d-d-d-d-d-dmca",
			"chris pratt mario",
			"yubi o nomimasu",
			"asbestos my beloved",
			"if you send me boobs pic i kill you",
			"oh no my smoke alarm got hacked and now its playing rick astley",
			"hey did u guys know theres an among us manga",
			"how long until we remove these splashes?",
			"there's this youtube channel full of videos of a guy in a spiderman costume digging a hole in the ground and pouring soda into it",
			"DO NOT LEAVE THE DOTTED osu! COOKIE TEMPLATE VISABLE IN YOUR SUBMISSION",
			"i tried to ask out my crush in my Boeing 777-300ER but i accidentally re-established the soviet union",
			"i am the computer toucher",
			"pipo pipo",
			"i love 1997 ford taurus",
			"chizu paranetsu",
			"blog it",
			"don't click the up arrow button while in full screen or you will crash winamp",
			"snusk juice",
			"there is a rat man in the basement",
			"obama 4 presidante 2088~~~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1B",
			"happy new year 2012!!!!!!!!!!!!!",
			"KEWR is literally the worst airport on the planet",
			"H e x o p o w o",
			"NO CURVED ROOOOOOOOOOOOAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDDDDDDDDDDDDDDDSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS",
			"el bear",
			"fun fact: pepto bismol is radioactive",
			"you are now smarter than you used to be and there is nothing you can do about it :^)",
			"i got caught eating batteries again :(",
			"suslink",
			"lodestone",
			"saw your arms off in the new pokemon game",
			"lttstore.com",
			"i've been writing splashes for almost an hour at this point",
			"HELIKOPTER HELIKOPTER",
			"hanbaagaa",
			"chernobyl cookies",
			"nvidia cpu",
			"obama signed my diploma",
			"i take that back actually, lying on the internet is illegal",
			"I AM BECOME SUS FOR CRIME I NOT COMMITTTTT",
			"we're gonna be in the hudson",
			"hhhhhhhHHHHHHH help me hello",
			"ababababababa",
			"if only the cyperpunk devs didnt forget to install cs: source",
			"i want to buy electrical fire scented candles",
			"the penguin should have the same feature",
			"spraypaint the flower pink",
			"DRINK FIRE EXTINGUISHER FOAM CHALLENGE",
			"roblox sued by squid game",
			"classic j",
			"yo guys you ever punched a bathtub?",
			"bread blanket",
			"failed my instrument checkride, i dont understand why though, i played the saxophone so well",
			"Welcome to Ainu! wait this isn't ainu",
			"le shill lion",
			"night sky",
			"RAHABAG akio BING",
			"Fly jeff air, only 60% mortality",
			"kiedy miaem 10 lat, zem do kibla wpadl!",
			"chiCkeN nOodLe SoUp 7*",
			"help why cant i run omnidazzle",
			"dont play among us at 3 am",
			"this is a test beatmap to test functionality in osekai medals and more",
			"doro no bunzai de watashi dake no taisetsu o ubaouda nante",
			"how fish is made?",
			"The Fish Is Blocked ! It Is Time To Inject The Serum !",
			"whimt camt v ersojng 32.8945332",
			"NZXT CPU",
			"asbestos mask",
			"play it mr toot",
			"obama body pillow",
			"i am win nobel prize in linguistics",
			"hey guys did u know fortnite ninja plays osu!!!!!!????????????????????????????",
			"gaeming chernobyl is my favourite youtube channel",
			"steal all nft get rich",
			"Free and open source!",
			# can you guess what i was thinking about when i wrote these?
			"You have caused a meltdown. Please try again.",
			"add uranium-235 to taste",
			"chernobyl people",
			"if steve minecraft can make an rbmk reactor he can do anything",
			"whats up youtube today im going to be showing you how to build a rbmk-1000 in your backyard",
			"cant wait for the dr stone episode where they build an rbmk-1000 nuclear reactor",
			"the more you donate the hotter the nuclear reactor gets",
			"i plugged my kindle fire into my nuclear reactor and it caused a radiation leak",
			"i played football and i accidentally started a nuclear war",
			"can i beat halo before the radiation from the melting nuclear fuel destroys my tv???",
			"oh no my helicopter has radiation poisioning",
			"why does this funny pencil say \"drop and run\"",
			"eating swedish fish as i scram my reactor",
			"Install Gentoo! It's only *almost* as complicated as starting up a nuclear power plant!",
			"i bet your pc dosen't have a synchroscope!",
			"The new Apple M1 Chip is now up to 40% more radioactive!",
			"The new iPod Shuffle, Now with built-in Geiger counter!",
			"uranium ingot"
		]


	def setMaintenance(self, maintenance):
		"""
		Turn on/off bancho maintenance mode. Write new value to db too

		maintenance -- if True, turn on maintenance mode. If false, turn it off
		"""
		self.config["banchoMaintenance"] = maintenance
		glob.db.execute("UPDATE bancho_settings SET value_int = %s WHERE name = 'bancho_maintenance'", [int(maintenance)])

	def reload(self):
		# Reload settings from bancho_settings
		glob.banchoConf.loadSettings()

		# Reload channels too
		glob.channels.loadChannels()

		# And chat filters
		glob.chatFilters.loadFilters()

		# Send new channels and new bottom icon to everyone
		glob.streams.broadcast("main", serverPackets.mainMenuIcon(glob.banchoConf.config["menuIcon"]))
		glob.streams.broadcast("main", serverPackets.channelInfoEnd())
		for key, value in glob.channels.channels.items():
			if value.publicRead and not value.hidden:
				glob.streams.broadcast("main", serverPackets.channelInfo(key))
