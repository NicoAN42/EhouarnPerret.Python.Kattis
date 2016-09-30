xs = []
ys = []
for _ in range(3):
	x, y = map(int, input().split())
	xs.append(x)
	ys.append(y)
xs.sort()
ys.sort()
x4 = xs[2] if (xs[0] == xs[1]) else xs[0]
y4 = ys[2] if (ys[0] == ys[1]) else ys[0]
print(x4, y4)
