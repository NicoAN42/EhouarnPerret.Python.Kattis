h, m = map(int, input().split())
mm = 24 * 60
tm = h * 60 + m
tm -= 45
if tm < 0:
	tm += mm
h = tm // 60
m = tm - h * 60
print(h, m)
