while True:
	n, d = map(int, input().split())
	if (n == 0) and (d == 0):
		break
	else:
		w = n // d
		n = n - (w * d)
		print(w, n, "/", d)
