translations = dict()
while True:
	s = input()
	if s == "":
		break
	else:
		tokens = s.split(" ")
		entry = tokens[1]
		translation = tokens[0]
		translations[entry] = translation
while True:
	try:
		word = input().rstrip("\n")
		if word in translations:
			translation = translations[word]
			print(translation)
		else:
			print("eh")
	except EOFError:
		break
