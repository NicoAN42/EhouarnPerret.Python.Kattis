import math


r, c = map(int, input().split())
pizza = math.pi * r ** 2
cheese = math.pi * (r - c) ** 2
percent = (cheese / pizza) * 100
print(percent)
