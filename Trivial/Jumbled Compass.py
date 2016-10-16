def find_shortest_angle(a, b):
	positive = (n2 - n1) % 360
	negative = (n1 - n2) % 360
	if positive < negative:
		return positive
	elif positive > negative:
		return -negative
	else:
		return positive


n1 = int(input())
n2 = int(input())
shortest = find_shortest_angle(n1, n2)
print(shortest)
