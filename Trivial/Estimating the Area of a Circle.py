import math


while True:
	r, m, c = map(float, input().split())
	if (r == 0) and (m == 0) and (c == 0):
		break
	else:
		true_area = math.pi * r**2
		ratio = (c / m)
		estimated_area = ratio * (2 * r) ** 2
		print(true_area, estimated_area)
