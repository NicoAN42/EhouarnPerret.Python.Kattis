def cards_check(cards_string):
	i = 0
	cards = dict()
	suits = ["P", "K", "H", "T"]
	for suit in suits:
		cards[suit] = set()
	while i < len(cards_string):
		suit = cards_string[i]
		number = int(cards_string[i + 1] + cards_string[i + 2])
		if number in cards[suit]:
			return "GRESKA"
		else:
			cards[suit].add(number)
		i += 3
	result = ""
	for suit in suits:
		result += str(13 - len(cards[suit])) + " "
	return result


s = input()
r = cards_check(s)
print(r)
