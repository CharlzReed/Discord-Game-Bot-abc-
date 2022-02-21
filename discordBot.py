# Discord Game Engine
# Charles Reed
# 2/15/2022
#========================

# Imports
from collections import OrderedDict
from random import randint
import discord

	
##############################################################################################################
class Deck:
	deck = {
		#   numbered  odd   even    suit       num    faceCard      name           key  used
		1 :  [False, True,  False, "spades",   "ace",   False, "Ace of Spades",     1,  True],
		2 :  [False, True,  False, "hearts",   "ace",   False, "Ace of Hearts",     2,  True],
		3 :  [False, True,  False, "diamonds", "ace",   False, "Ace of Diamonds",   3,  True],
		4 :  [False, True,  False, "clubs",    "ace",   False, "Ace of Clubs",      4,  True],
		5 :  [True,  False, True,  "spades",   "2",     False, "2 of Spades",       5,  True],
		6 :  [True,  False, True,  "hearts",   "2",     False, "2 of Hearts",       6,  True],
		7 :  [True,  False, True,  "diamonds", "2",     False, "2 of Diamonds",     7,  True],
		8 :  [True,  False, True,  "clubs",    "2",     False, "2 of Clubs",        8,  True],
		9 :  [True,  True,  False, "spades",   "3",     False, "3 of Spades",       9,  True],
		10 : [True,  True,  False, "hearts",   "3",     False, "3 of Hearts",       10, True],
		11 : [True,  True,  False, "diamonds", "3",     False, "3 of Diamonds",     11, True],
		12 : [True,  True,  False, "clubs",    "3",     False, "3 of Clubs",        12, True],
		13 : [True,  False, True,  "spades",   "4",     False, "4 of Spades",       13, True],
		14 : [True,  False, True,  "hearts",   "4",     False, "4 of Hearts",       14, True],
		15 : [True,  False, True,  "diamonds", "4",     False, "4 of Diamonds",     15, True],
		16 : [True,  False, True,  "clubs",    "4",     False, "4 of Clubs",        16, True],
		17 : [True,  True,  False, "spades",   "5",     False, "5 of Spades",       17, True],
		18 : [True,  True,  False, "hearts",   "5",     False, "5 of Hearts",       18, True],
		19 : [True,  True,  False, "diamonds", "5",     False, "5 of Diamonds",     19, True],
		20 : [True,  True,  False, "clubs",    "5",     False, "5 of Clubs",        20, True],
		21 : [True,  False, True,  "spades",   "6",     False, "6 of Spades",       21, True],
		22 : [True,  False, True,  "hearts",   "6",     False, "6 of Hearts",       22, True],
		23 : [True,  False, True,  "diamonds", "6",     False, "6 of Diamonds",     23, True],
		24 : [True,  False, True,  "clubs",    "6",     False, "6 of Clubs",        24, True],
		25 : [True,  True,  False, "spades",   "7",     False, "7 of Spades",       25, True],
		26 : [True,  True,  False, "hearts",   "7",     False, "7 of Hearts",       26, True],
		27 : [True,  True,  False, "diamonds", "7",     False, "7 of Diamonds",     27, True],
		28 : [True,  True,  False, "clubs",    "7",     False, "7 of Clubs",        28, True],
		29 : [True,  False, True,  "spades",   "8",     False, "8 of Spades",       29, True],
		30 : [True,  False, True,  "hearts",   "8",     False, "8 of Hearts",       30, True],
		31 : [True,  False, True,  "diamonds", "8",     False, "8 of Diamonds",     31, True],
		32 : [True,  False, True,  "clubs",    "8",     False, "8 of Clubs",        32, True],
		33 : [True,  True,  False, "spades",   "9",     False, "9 of Spades",       33, True],
		34 : [True,  True,  False, "hearts",   "9",     False, "9 of Hearts",       34, True],
		35 : [True,  True,  False, "diamonds", "9",     False, "9 of Diamonds",     35, True],
		36 : [True,  True,  False, "clubs",    "9",     False, "9 of Clubs",        36, True],
		37 : [True,  False, True,  "spades",   "10",    False, "10 of Spades",      37, True],
		38 : [True,  False, True,  "hearts",   "10",    False, "10 of Hearts",      38, True],
		39 : [True,  False, True,  "diamonds", "10",    False, "10 of Diamonds",    39, True],
		40 : [True,  False, True,  "clubs",    "10",    False, "10 of Clubs",       40, True],
		41 : [False, True,  False, "spades",   "jack",  True,  "Jack of Spades",    41, True],
		42 : [False, True,  False, "hearts",   "jack",  True,  "Jack of Hearts",    42, True],
		43 : [False, True,  False, "diamonds", "jack",  True,  "Jack of Diamonds",  43, True],
		44 : [False, True,  False, "clubs",    "jack",  True,  "Jack of Clubs",     44, True],
		45 : [False, False, True,  "spades",   "queen", True,  "Queen of Spades",   45, True],
		46 : [False, False, True,  "hearts",   "queen", True,  "Queen of Hearts",   46, True],
		47 : [False, False, True,  "diamonds", "queen", True,  "Queen of Diamonds", 47, True],
		48 : [False, False, True,  "clubs",    "queen", True,  "Queen of Clubs",    48, True],
		49 : [False, True,  False, "spades",   "king",  True,  "King of Spades",    49, True],
		50 : [False, True,  False, "hearts",   "king",  True,  "King of Hearts",    50, True],
		51 : [False, True,  False, "diamonds", "king",  True,  "King of Diamonds",  51, True],
		52 : [False, True,  False, "clubs",    "king",  True,  "King of Clubs",     52, True],
	}
	


##############################################################################################################
class ABC(Deck):

	def __init__(self, name, idd, emoji_indx):
		self.name = name
		self.id = idd

		self.pos = 0
		self.current_card = []
		self.current_roll = 0
		self.chat_log = []
		self.deck = Deck.deck	
		self.board = ""
		self.emoji = [":plunger:",":100:",":recycle:",":warning:",":biohazard:",":mute:",":jigsaw:",":8ball:",":snake:",":mushroom:",":space_invader:",":alien:"][emoji_indx]
		self.bet_win_lose = 0
		self.still_playing = True

		# counter = 0
		# for num in ['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']:
		# 	for suit in ['spades','hearts','diamonds','clubs']:
		# 		counter += 1
		# 		numbered = True if num not in ['ace','jack','queen','king'] else False
		# 		even = True if num in ['2','4','6','8','10','queen'] else False
		# 		odd = True if num in ['ace','3','5','7','9','jack','king'] else False
		# 		num = num
		# 		suit = suit
		# 		faceCard = True if num in ['jack','queen','king'] else False
		# 		formatted = f"{num.capitalize()} of {suit.capitalize()}"
		# 		print(f'{counter} : [{numbered}, {odd}, {even}, "{suit}", "{num}", {faceCard}, "{formatted}", {counter}, True], ')

	def get_attr(self, attr):
		return getattr(self, attr)


	def dice_roll(self):
		self.current_roll = randint(1,6)
		# print('current roll', self.current_roll)
		return self.current_roll
	

	def gameboard(self):
		if self.pos >= 30:
			self.still_playing = False
			# print('game status:', self.still_playing)
			self.board = f"``{self.name} have finished the game!``"
		else:
			self.board = ":arrow_right:" + ":blue_square:" * (self.pos) + self.emoji + ":red_square:" * (30 - (self.pos)) + ":white_check_mark:     ``" + self.name.capitalize() + f" ({self.pos}/30)``"
		return self.board


	def pick_card(self):
		while True:
			card = self.deck[randint(1, 52)]
			if card[8] == True:
				self.current_card = card
				break
	
	def card_name(self):
		# print(self.current_card)
		return self.current_card

	def remove_card(self):
		self.deck[self.current_card[7]][8] = False
	
	def stop_playing(self):
		self.still_playing = False
	

	def bet(self, *args):
		# print(f"NAME:({self.name}), POSITION:({self.pos})")


		total_sum = 0
		total_bool = True
		associates = {
			"numbered" : [0, 2],

			"odd"  : [1, 3],
			"even" : [2, 4],

			"face"  : [5, 8],

			"spades"   : [3, 9],
			"hearts"   : [3, 9],
			"diamonds" : [3, 9],
			"clubs"    : [3, 9],

			"ace"   : [4, 14],
			"2"     : [4, 14],
			"3"     : [4, 14],
			"4"     : [4, 14],
			"5"     : [4, 14],
			"6"     : [4, 14],
			"7"     : [4, 14],
			"8"     : [4, 14],
			"9"     : [4, 14],
			"10"    : [4, 14],
			"jack"  : [4, 14],
			"queen" : [4, 14],
			"king"  : [4, 14],
		}

		if str(args[0]) == "ans":
			self.pos += self.current_roll + 15
			self.bet_win_lose = "``Passed    +" + str(self.current_roll) + "``"
			# print(f"NAME:({self.user}), POSITION:({self.pos}), CURRENT ROLL:({self.current_roll})")
			return self.bet_win_lose

		if str(args[0]) == "pass":
			# print(self.pos, self.current_roll)
			self.pos += self.current_roll
			# print(self.pos)
			self.bet_win_lose = "``Passed    +" + str(self.current_roll) + "``"
			# print(f"NAME:({self.user}), POSITION:({self.pos}), CURRENT ROLL:({self.current_roll})")
			return self.bet_win_lose

		else:
			self.pick_card()
			for bets in args:
				if bets in associates:
					indx = associates[bets][0]
					gain = associates[bets][1]
					
					if self.current_card[indx] == True or self.current_card[indx] == bets:
						total_sum += gain

					else:
						total_sum += gain
						total_bool = False

				else:
					print("Invalid bet")
					

			if total_bool == True:
				# print("You bet correct!")
				self.bet_win_lose = "``You bet correct! (your card was: " + self.current_card[6] + ")    +" + str(self.current_roll + total_sum) + "``"
				self.pos += (self.current_roll + total_sum)

			else:
				# print("You bet wrong!")
				self.bet_win_lose = "``You bet wrong! (your card was: " + self.current_card[6] + ")    -" + str(self.current_roll + total_sum) + "``"
				self.pos -= (self.current_roll + total_sum)
			
			if self.pos < 0:
				self.pos = 0
			
			self.remove_card()
					
			# print(f"NAME:({self.user}), POSITION:({self.pos}), CURRENT ROLL:({self.current_roll})")
			print(f"NAME:({self.name}), POSITION:({self.pos})\n")
			return self.bet_win_lose
		

##############################################################################################################
class Logs:
	def __init__(self):
		self.prev_command = []
	
	def log_command(self, command):
		self.prev_command.append(command)
		return self.prev_command

	def set_command(self, command):
		self.prev_command = command
		return self.prev_command

	def get_prevs(self):
		return self.prev_command


##############################################################################################################
class Whos_Turn:
	def __init__(self):
		self.indx_turn = 0
		self.players = []
		self.limit = 0
		self.one_cycle = []
		self.one_cycle_sorted = []
	
	def set_player_num(self, num):
		self.limit = num-1
		for _ in range(150):
			for i in range(num):
				self.players.append(i)
		self.one_cycle = self.players[self.indx_turn : self.indx_turn + len(list(set(self.players)))]
		self.one_cycle_sorted = sorted(self.one_cycle)


	def current(self):
		# print(self.players, self.indx_turn, self.limit)
		return self.players[self.indx_turn]

	def next_player(self):
		self.indx_turn += 1
		self.one_cycle = self.players[self.indx_turn : self.indx_turn + len(list(set(self.players)))]
		self.one_cycle_sorted = sorted(self.one_cycle)
		# print(f"{self.indx_turn}/{self.limit}")
		return self.indx_turn
	
	def reset_turns(self):
		self.indx_turn = 0
		self.players = []
		self.limit = 0
		self.one_cycle = []
		self.one_cycle_sorted = []


##############################################################################################################
class Temp_names:
	def __init__(self):
		self.names = []
	
	def add_name(self, name):
		if name not in self.names:
			self.names.append(name)
	
	def get_names(self):
		return self.names

	def clear(self):
		self.names = []


##############################################################################################################
# Client for discord
client = discord.Client()

# Class instances
winners = Temp_names()
w = Whos_Turn()
log = Logs()

# Variables
counter2obj = {}
bets_and_opening_msg = '''```txt
-------------------------------------------------------WELCOME------------------------------------------------------------

The goal of this game is to get to the end of the board by rolling the dice and betting on whether or not the card is
even/odd/face card/etc. Winning the bet will result in bonus points added to the dice's initial number. Losing the bet
results in the dice's initial number + the potential bonus (had the bet gone well) being subtracted from your position.


Bets / Commands:
	"!!join @user1 user1's nickname @user2 user2's nickname ..."  :  Creates a new game with the pinged users (PLAYERS > 1)
	"!!quit"                                                      :  Quits and deletes the messages sent during the game

	"-bet numbered"  :  Bets on a numbered card         (ace,2,3,4,5,6,7,8,9,10)                  {77%}  ->  dice roll +2
	"-bet odd"       :  Bets on an odd numbered card    (ace,3,5,7,9,jack,queen,king)             {54%}  ->  dice roll +3
	"-bet even"      :  Bets on an even numbered card   (2,4,6,8,10,queen)                        {46%}  ->  dice roll +4
	"-bet spades"    :  Bets on the suit being spades   (same for hearts, diamonds, clubs)        {25%}  ->  dice roll +8
	"-bet face"      :  Bets on a face card             (jack,queen,king)                         {23%}  ->  dice roll +9
	"-bet 9"         :  Bets on the exact card number   (ace,2,3,4,5,6,7,8,9,10,jack,queen,king)  {7%}   ->  dice roll +14
	"-bet pass"      :  Skips your bet                                                            {100%} ->  dice roll +0

-------------------------------------------------------WELCOME------------------------------------------------------------
```'''


# Callin a cleint event when bot goes online and printing message
@client.event
async def on_ready():
	chat = client.get_channel("chat ID")
	await chat.send(':green_square:   *Status: Online. (**!!help** for commands)*')

@client.event
async def on_message(message):
	chat = client.get_channel("chat ID")

	if "place is" not in message.content and "`<~|========================|~>`" not in message.content:
		log.log_command(message)
	
	author = message.author
	text = message.content.lower()

	if message.content.startswith('!!'):

		if text == '!!help':
			await chat.send(bets_and_opening_msg)

		if text[2:6] == "join" and "@" in text[5:]:
			players = text[5:].replace(" ", "").replace("<","").replace(">","").replace("!","").replace("&","").split("@")
			players = [x for x in players if x != "" and x != " " and len(x) > 1]
			players_id = [x[:18] for x in players]
			players_name = [x[18:] for x in players]
		
			five = []
			for _ in range(10):
				num = randint(0,11)
				if num not in five:
					five.append(num)

			counter = 0
			for idd,name in zip(players_id, players_name):
				if idd not in counter2obj:
					await chat.send(f'{name} *has joined the game!*')
					# time.sleep(0.25)
					counter2obj[counter] = ABC(name, idd, five[counter])
					counter += 1
			w.set_player_num(len(counter2obj))
			await chat.send(f'Enter **-start** to start the game!')


		if text[2:6] == "quit":
			for cmds in log.get_prevs()[::-1]:
				try:
					await cmds.delete()
				except:
					pass
			log.set_command([])
			winners.clear()
			w.reset_turns()
			await chat.send(f'*Ready to play again*')


			# await chat.send(':black_large_square:   *Status: Offline*')
			# await client.close()
			# exit()
	


#---------------------------------------------------------------------------------------------------------------------------------
	if message.content[0] == '-' and len(message.content) > 1 and len(counter2obj) > 0:
		playing = True


		if text[1:4] == "bet":# and names_dict_counter2name[whos_turn.current_turn()] == author.name:
			await chat.send(counter2obj[w.current()].bet(text[5:]))
			w.next_player()
		
		temp = True
		for values in w.one_cycle_sorted:
			if counter2obj[values].get_attr('pos') > 30:
				temp = False
				break
		if temp:
			await chat.send("`|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|`")
			await chat.send(f"``It is {counter2obj[w.current()].get_attr('name').capitalize()}'s turn to bet``:black_joker:")

		for values in w.one_cycle_sorted:
			if counter2obj[values].get_attr('pos') <= 30:
				await chat.send(counter2obj[values].gameboard())

			else:
				await chat.send("`<~|========================|~>`")
				ordered_winners = {}
				for values in range(len(counter2obj)):
					ordered_winners[counter2obj[values].get_attr('pos')] = counter2obj[values].get_attr('name')
				ordered_winners = OrderedDict(sorted(ordered_winners.items(), key=lambda x: x[0], reverse=True))
				formatted = ""
				for counter, place in enumerate(ordered_winners.values()):
					if counter == 0:
						place_num = ':first_place: 1st '
					elif counter == 1:
						place_num = ':second_place: 2nd'
					elif counter == 2:
						place_num = ':third_place: 3rd'
					elif counter == 3:
						place_num = ':medal: 4th'
					elif counter == 4:
						place_num = ':medal: 5th'
					elif counter == 5:
						place_num = ':medal: 6th'
					elif counter == 6:
						place_num = ':medal: 7th'
					elif counter == 7:
						place_num = ':medal: 8th'
					elif counter == 8:
						place_num = ':medal: 9th'
					elif counter == 9:
						place_num = ':medal: 10th'
					
					formatted += f"\n{place_num} ``place is {place.capitalize()}!``"

				await chat.send(f"{formatted}")

				await chat.send("`<~|========================|~>`")
				
				for cmds in log.get_prevs()[::-1]:
					try:
						await cmds.delete()
					except:
						pass
				log.set_command([])
				winners.clear()
				w.reset_turns()
				playing = False
				await chat.send(f'*Ready to play again*')
				break


				# await chat.send(':black_large_square:   *Status: Offline*')
				# await client.close()
				# exit()
				
		temp = True
		for values in w.one_cycle_sorted:
			if counter2obj[values].get_attr('pos') > 30:
				temp = False
				break
		if temp and playing:
			await chat.send(f"``You rolled a {counter2obj[w.current()].dice_roll()}!``:game_die:")

		


# Client ID for the bot
client.run('Bot ID')