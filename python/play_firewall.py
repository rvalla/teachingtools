import random as rd
from firewall import Firewall

pl = Firewall()
victory_threshold = 5
hits = set()
ok_msg = ["¡Muy bien! Pasa...",
			"¡Excelente! Pasó.",
			"Un lujo. Pasó.",
			"El mensaje atrevesó el portal.",
			"¡Qué bien che! Pasa...",
			"Pasó el mensaje. ¡Impresionante!",
			"No lo puedo creer. Pasa.",
			"Se escucha un aplauso. Pasó."]
wrong_msg = ["No che... No pasa.",
			"El mensaje se chocó contra el portal.",
			"El mensaje no cumple la regla.",
			"No pasa.",
			"Vale la intención, pero no pasa.",
			"El mensaje se quedó trabado.",
			"No, este no pasa.",
			"Vas a tener que seguir probando. No pasa."]
cheat_msg = ["He detectado la trampa.",
			"¡Trampa! Ese mensaje ya había pasado.",
			"No vale usar dos veces el mismo mensaje.",
			"¡Ese mensaje ya había pasado!"]

#We can start with a message...
print("Hola, voy a desafiarte...", end="\n")

#Let's prepare a firewall game...
def start():
	print("--------------------------", end="\n")
	print("Hay un portal. Tenés que descubrir la regla para atravesarlo.", end="\n")
	print("Elegí dificultad: 1, 2 o 3", end="\n")
	d = input()
	try:
		round = pl.get_firewall_game(int(d)-1)
		print(round["ex_pass"].capitalize() + " pasa...", end="\n")
		print(round["ex_notpass"].capitalize() + " no pasa...", end="\n")
		hits.add(round["ex_pass"])
		check_game(round["algorithm"], round["in_type"], round["parameters"], 0)
	except:
		print("No puedo procesar eso. Termino el desafío.", end="\n")
		hits.clear()
		start()

#Interacting with user's messages...
def check_game(a, in_type, args, hits_count):
	if hits_count < victory_threshold:
		move = input().lower()
		if move == "terminar":
			print("OK. Terminamos...", end="\n")
		else:
			if in_type == "number":
				try:
					m = int(move)
				except:
					print(rd.choice(wrong_msg), end="\n")
					check_game(a, in_type, args, hits_count)
			else:
				m = move
			if not m in hits:
				if pl.check_firewall(a, m, args):
					print(rd.choice(ok_msg), end="\n")
					hits.add(m)
					hits_count += 1
				else:
					print(rd.choice(wrong_msg), end="\n")
			else:
				print(rd.choice(cheat_msg), end="\n")
			check_game(a, in_type, args, hits_count)
	else:
		print("¡Bravo! Lograste pasar " + str(victory_threshold) + " mensajes... ¡Ganaste!", end="\n")
		hits.clear()
		start()

start()
