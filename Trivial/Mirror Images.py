t = int(input())
for ti in range(t):
	r, c = map(int, input().split())
	result = [""] * r
	for i in range(r):
		row = input()
		result[r - 1 - i] = row[::-1]
	print("Test", ti + 1)
	print(*result, sep="\n")
