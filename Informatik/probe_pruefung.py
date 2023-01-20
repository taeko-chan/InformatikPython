import random
#from progress.bar import Bar

def aufgabe1(word):
	i = 0
	new_word = ""
	while i <= len(word) - 1:
		new_word = new_word + word[i]
		if i != len(word) - 1:
			new_word = new_word + "-"
		i += 1
	print(new_word)

def aufgabe2():
	print("output 32")

def aufgabe3(numbers):
	sorted_numbers = []
	i = 0
	while i < len(numbers):
		if numbers[i] % 2 == 0:
			sorted_numbers.append(numbers.pop(i))
		i += 1
	sorted_numbers = sorted_numbers + numbers
	print(sorted_numbers)

def aufgabe4(list1, list2):
	i = 0
	common_fruits = []
	while i < len(list1):
		j = 0
		while j < len(list2):
			if list1[i] == list2[j]:
				duplicate = False
				for x in common_fruits:
					if x == list1[i]:
						duplicate = True
				if not duplicate:
					common_fruits.append(list1[i])
			j += 1
		i += 1
	print(common_fruits)

def aufgabe5(tries, target_sum, dice):
	random.seed()
	i = 0
	successful_rolls = 0
	while i < tries:
		j = 0
		current_rolls = []
		while j < dice:
			current_rolls.append(int(random.random() * 6) + 1)
			j += 1
		current_sum = 0
		for x in current_rolls:
			current_sum += x
		if current_sum == target_sum:
			successful_rolls += 1
		i += 1
	print(successful_rolls/tries)*100

#-------------------------------------------------------------------------------------

def most_probable(chances, target, range):
	min = int(target/6) + 1
	print("################### START ###################")
	print("For the target", target, "the minimum possible dice amount is", min, ", will start there...")
	i = min
	highest_probablity = 0
	highest_probablity_dice = 0
	bar = Bar('Processing', max=range)
	while i < min + range:
		result = aufgabe5(chances, target, i)
		if result > highest_probablity:
			highest_probablity = result
			highest_probablity_dice = i
		i += 1
		bar.next()
	bar.finish()
	print("Result:")
	print(highest_probablity_dice, "dice had the most likely outcome with around", int(highest_probablity), "%")
	print("################### END ###################")



aufgabe1("bonjour monsieur")