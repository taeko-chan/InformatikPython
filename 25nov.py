import time
import random

def ssp():
	a = ["Schere", "Stein", "Papier"]
	spiel = True
	while spiel:
		computer_choice = int(3*random.random())
		user_round = input("Schere, Stein oder Papier => ")
		computer_round = a[computer_choice]
		if not user_round in a:
			print("Keine gültige Antwort!")
		if user_round == computer_round:
			print("Unentschieden! Beide hatten", user_round)
		elif (user_round == "Schere" and computer_round == "Papier") \
			 or (user_round == "Stein" and computer_round == "Schere") \
			 or (user_round == "Papier" and computer_round == "Stein"):
			print("Du hast gewonnen! Der Computer wählte", computer_round)
		else:
			print("Du hast verloren! Der Computer wählte", computer_round)
		if input("Eine weitere Runde spielen? j = Ja, alles andere = Nein. => ") != "j":
			spiel = False


def lolrip():
	x = "2"
	y = 0
	z = False
	while z == False:
		y = "2" + x[0:len(x)-1]
		if int(y) == 2*int(x):
			print("Mit", x, "funktioniert es")
			z = True
		x = str(int(x) + 10)

def one():
	inp = input("Wort Eingeben: ")
	l = len(inp)
	i = 0
	while i < l:
		print(inp[i])
		if inp[i] == "s" or inp[i] == "S":
			i += 1

def two():
	i = 0
	while i < 5:
		x = input("Sind Sie sicher?")
		if x == "N":
			i = 6
			print("Sind Sie nicht.")
		i += 1

def three():
	i = 0
	while i < 10:
		note = float(input("Geben Sie eine Note ein: "))
		if note >= 5.75:
			print("Gratuliere!")
		elif note <= 3.75:
			print("Oje, besser lernen!")
		print(9-i, "übrig")
		i += 1


def dec_bin():
	bin = input("Bin: ")
	dec = 0
	i = 0
	while i <= len(bin)-1:
		dec += int(int(bin[i]) * 2**(len(bin)-i-1))
		i += 1
	print(dec)

def noten_rangliste_simpler(x):
	p1 = 0
	p1p = ""
	p2 = 0
	p2p = ""
	p3 = 0
	p3p = ""
	i = 0
	while i < x:
		person = input("Name einer Schüler/in: ")
		grade = float(input("Seine/ihre erzielte Note: "))
		#if grade < p1


def noten_rangliste(x):
	grades = []
	person = []
	i = 0
	while i < x:
		print(i+1, "von", x)
		person.append(input("Name einer Schüler/in: "))
		grades.append(float(input("Seine/ihre erzielte Note: ")))
		i += 1
	p1 = [0]
	p2 = [0]
	p3 = [0]
	i = 0
	while i < len(grades):
		if grades[i] > p3[0]:
			p3[0] = i
			if grades[i] > p2[0]:
				#p3.remove(len(p3)-1)
				p3.pop()
				if len(p3) == 0:
					p3 = [0]
				p2[0] = i
				if grades[i] > p1[0]:
					p2.pop()
					#p2.remove(len(p2)-1)
					if len(p2) == 0:
						p2 = [0]
					p1[0] = i
		if grades[i] == p3[0]:
			p3.append(i)
		elif grades[i] == p2[0]:
			p2.append(i)
		elif grades[i] == p1[0]:
			p1.append(i)
		i += 1

	i = 0
	print("1. Platz")
	while i < len(p1):
		print(person[p1[i]])
		print(grades[p1[i]])
		i += 1

	print("2. Platz")
	while i < len(p2):
		print(person[p2[i]])
		print(grades[p2[i]])
		i += 1


	print("3. Platz")
	while i < len(p3):
		print(person[p3[i]])
		print(grades[p3[i]])
		i += 1


def random_number_exact(factor):
	x = random.random()
	l = len(str(x))-2
	print((factor * 10**l * x)/10**l)

ssp()