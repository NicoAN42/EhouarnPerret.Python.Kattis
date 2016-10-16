a, b, c = map(int, input().split())
if a == (b + c):
	print(a, "=", b, "+", c, sep="")
elif a == (b - c):
	print(a, "=", b, "-", c, sep="")
elif a == (b * c):
	print(a, "=", b, "*", c, sep="")
elif (c != 0) and (a == (b / c)):
	print(a, "=", b, "/", c, sep="")
elif (a + b) == c:
	print(a, "+", b, "=", c, sep="")
elif (a - b) == c:
	print(a, "-", b, "=", c, sep="")
elif (a * b) == c:
	print(a, "*", b, "=", c, sep="")
else:
	print(a, "/", b, "=", c, sep="")
