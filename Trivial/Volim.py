l = 3 * 60 + 30
k = int(input()) - 1
n = int(input())
c = 0
for i in range(n):
	s = input().split()
	t = int(s[0])
	z = s[1]
	c += t
	if c > l:
		break
	if z == "T":
		k = (k + 1) % 8
print(k + 1)
