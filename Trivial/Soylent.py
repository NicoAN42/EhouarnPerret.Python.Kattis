import math

b = 400
t = int(input())
for _ in range(t):
	n = int(input())
	c = math.ceil(n / b)
	print(c)
