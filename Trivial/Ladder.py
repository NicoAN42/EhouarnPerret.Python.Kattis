import math

h, v = map(int, input().split())
v = math.radians(v)
l = math.ceil(h / math.sin(v))
print(l)
