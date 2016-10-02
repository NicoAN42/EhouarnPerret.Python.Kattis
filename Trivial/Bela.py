table = dict()
table["A"] = [11, 11]
table["K"] = [4, 4]
table["Q"] = [3, 3]
table["J"] = [20, 2]
table["T"] = [10, 10]
table["9"] = [14, 0]
table["8"] = [0, 0]
table["7"] = [0, 0]

n, b = input().split()
n = int(n)
result = 0
for _ in range(n * 4):
	s = input()
	card, suit = s[0], s[1]
	index = 0 if suit == b else 1
	result += table[card][index]
print (result)
