def reverse_rot(n, text):
	symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
	symbols_length = len(symbols)
	d = dict()
	for i in range(symbols_length):
		letter = symbols[i]
		d[letter] = i
	text = text[::-1]
	result = ""
	for letter in text:
		i = d[letter]
		ri = (i + n) % symbols_length
		result += symbols[ri]
	return result


while True:
	s = input().split()
	n = int(s[0])
	if n == 0:
		break
	else:
		t = s[1]
		r = reverse_rot(n, t)
		print(r)
