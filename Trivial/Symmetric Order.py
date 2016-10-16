set_index = 0
n = int(input())
while n > 0:
	set_index += 1
	print("SET", set_index)
	upper = []
	lower = []
	for i in range(n):
		name = input()
		if (i % 2) == 0:
			upper.append(name)
		else:
			lower.append(name)
	print(*upper, sep="\n")
	print(*lower[::-1], sep="\n")
	upper.clear()
	lower.clear()
	n = int(input())
