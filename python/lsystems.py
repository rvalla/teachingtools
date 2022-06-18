# Let's play with Lindenmayer systems...

alphabet = ["A", "B", "C"] #Our alphabet

the_rules = {"A": "AB", "B": "AA", "C": "AC"} #Our rules

iterations = 10 #Limit for steps
steps = 0 #Current step

print("Vamos a simular sistemas de Lindenmayer", end="\n")
print("Nuestro alfabeto es: " + str(alphabet), end="\n")

def get_next_level(past_level, rules):
	level = ""
	for c in past_level:
		level += rules[c]
	return level

def is_trigger_valid(trigger):
	valid = True
	for c in trigger:
		if not c in alphabet:
			valid = False
	return valid

while 1 > 0:
	msg = input()
	if msg == "q":
		print("Se acabó lo que se daba...", end="\n")
		break
	elif not is_trigger_valid(msg):
		print("El estado inicial del sistema no puede tener símbolos que no estén en el alfabeto.", end="\n")
	else:
		level = msg
		print("Vamos a calcular " + str(iterations) + " para el sistema L...", end="\n")
		print(level)
		while steps < iterations - 1:
			print("-----", end="\n")
			level = get_next_level(level, the_rules)
			print(level)
			steps += 1
