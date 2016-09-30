n = int(input())
x = 0
for _ in range(n):
	p = input()
	power = int(p[-1])
	number = int(p[:-1])
	x += number ** power
print(x)
