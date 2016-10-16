k = int(input())
a_count = 1
b_count = 0
for i in range(k):
	tmp = a_count + b_count
	a_count = b_count
	b_count = tmp
print(a_count, b_count)
