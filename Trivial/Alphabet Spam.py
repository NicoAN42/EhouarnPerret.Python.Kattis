s = input()
count = len(s)
whitespaces = 0
lowercases = 0
uppercases = 0
symbols = 0
for c in s:
	if c == "_":
		whitespaces += 1
	elif c.islower():
		lowercases += 1
	elif c.isupper():
		uppercases += 1
	else:
		symbols += 1
print(whitespaces / count)
print(lowercases / count)
print(uppercases / count)
print(symbols / count)
