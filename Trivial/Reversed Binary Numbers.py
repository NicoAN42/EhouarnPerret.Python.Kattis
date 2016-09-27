n = int(input())
n = bin(n)[:1:-1]
n = int(n, base=2)
print(n)
