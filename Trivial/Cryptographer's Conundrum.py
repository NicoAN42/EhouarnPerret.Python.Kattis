def count_days(text):
	per = ["P", "E", "R"]
	n = len(text)
	count = 0
	for i in range(n):
		letter = text[i].upper()
		peri = i % 3
		if letter != per[peri]:
			count += 1
	return count


s = input()
days = count_days(s)
print(days)
