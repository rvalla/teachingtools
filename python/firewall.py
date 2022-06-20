import random as rd

class Firewall():
	"The class the bot use let users to play..."

	def __init__(self):
		self.last_firewall = [0,0,0] #The last firewall which was sent...
		self.firewall, self.availables = self.load_firewalls() #Loading firewall database and total availables...

#Deciding if a move in firewalls game is good...
	def check_firewall(self, algorithm, move, parameters=[]):
		if algorithm == 0:
			try:
				n = int(move)
				return self.check_firewall_range(n, parameters)
			except:
				return False
		elif algorithm == 1:
			try:
				n = int(move)
				return self.check_firewall_remainder(n, parameters)
			except:
				return False
		elif algorithm == 2:
			return self.check_firewall_letter_count(move, parameters[0])
		elif algorithm == 3:
			return self.check_firewall_positions(move, parameters)
		elif algorithm == 4:
			return self.check_firewall_split(move, parameters)
		elif algorithm == 5:
			return self.check_firewall_sum(move, parameters[0])
		elif algorithm == 6:
			return self.check_firewall_positions_sum(move, parameters)

	#Checking a move in firewall's game: number range type...
	def check_firewall_range(self, move, range):
		good_move = False
		if move > range[0] and move < range[1]:
			good_move = True
		return good_move

	#Checking a move in firewall's game: number remainder type...
	def check_firewall_remainder(self, move, values):
		good_move = False
		if move%values[0] == values[1]:
			good_move = True
		return good_move

	#Checking a move in firewall's game: letter count type...
	def check_firewall_letter_count(self, move, count):
		good_move = False
		if len(move) == count:
			good_move = True
		return good_move

	#Checking a move in firewall's game: symbol position type...
	def check_firewall_positions(self, move, parameters):
		good_move = False
		loop_size = len(parameters)//2
		move_size = len(move)
		count = 0
		for i in range(loop_size):
			if move[int(parameters[2*i])%move_size] == parameters[2*i+1]:
				count += 1
		if count == loop_size:
			good_move = True
		return good_move

	#Checking a move in firewall's game: symbol count type...
	def check_firewall_split(self, move, values):
		good_move = False
		if len(move.split(values[1])) == int(values[0]):
			good_move = True
		return good_move

	#Checking a movi in firewall's game: total digit sum...
	def check_firewall_sum(self, move, result):
		good_move = False
		s = 0
		for d in move:
			s += int(d)
		if s == result:
			good_move = True
		return good_move

	#Checking a movi in firewall's game: total digit positions sum...
	def check_firewall_positions_sum(self, move, parameters):
		good_move = False
		loop_size = len(parameters) - 1
		move_size = len(move)
		s = 0
		for i in range(loop_size):
			s += int(move[parameters[i]%move_size])
		if s == parameters[len(parameters)-1]:
			good_move = True
		return good_move

	#Building a firewall's challenge for words of n letters...
	def get_firewall_game(self, difficulty):
		self.next_firewall_to_send(difficulty)
		data = self.firewall[difficulty][self.last_firewall[difficulty]].split(";")
		round = {}
		round["command"] = data[0]
		round["type"] = data[1]
		round["algorithm"] = int(data[2])
		round["ex_pass"] = data[3]
		round["ex_notpass"] = data[4]
		round["in_type"] = data[5]
		round["parameters"] = self.firewall_parameters(data[6], data[7])
		return round

	#Building a firewalls challenge parameters list...
	def firewall_parameters(self, parameters_type, data):
		in_l = data.split(",")
		out_l = []
		if parameters_type == "numbers":
			for i in in_l:
				out_l.append(int(i))
		else:
			out_l = in_l
		return out_l

	#Selecting next firewall to send...
	def next_firewall_to_send(self, difficulty):
		self.last_firewall[difficulty] = (self.last_firewall[difficulty] + rd.randint(1,4)) % self.availables[difficulty]

	#Building firewall database...
	def load_firewalls(self):
		firewalls = []
		easy = []
		medium = []
		hard = []
		file = open("assets/data/firewall.csv").readlines()[1:]
		for l in file:
			data = l.split(";")
			if int(data[8]) == 0:
				easy.append(l)
			elif int(data[8]) == 1:
				medium.append(l)
			elif int(data[8]) == 2:
				hard.append(l)
		availables = [len(easy), len(medium), len(hard)]
		firewalls.append(easy)
		firewalls.append(medium)
		firewalls.append(hard)
		return firewalls, availables
