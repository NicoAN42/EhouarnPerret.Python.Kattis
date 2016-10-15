import math

while True:
	s = input()
	if s != "0":
		x1, y1, x2, y2, p = map(float, s.split())
		r = (abs(x1 - x2) ** p + abs(y1 - y2) ** p) ** (1 / p)
		print(r)
	else:
		break
