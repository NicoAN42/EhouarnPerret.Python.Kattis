while True:
	n = int(input())
	if n == -1:
		break
	else:
		d = 0
		lt = 0
		for i in range(n):
			s, t = map(int, input().split())
			t -= lt
			lt += t
			d += s * t
		print(d, "miles")
