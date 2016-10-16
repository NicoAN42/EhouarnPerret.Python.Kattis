def find_single(l):
	r = 0
	for li in l:
		r ^= li
	return r


n = int(input())
for i in range(n):
	g = int(input())
	c = map(int, input().split())
	s = find_single(c)
	print("Case #", i + 1, ": ", s, sep="")
