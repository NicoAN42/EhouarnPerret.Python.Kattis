def print_differences(a, b):
	abn = len(a)
	result = ""
	for i in range(abn):
		if a[i] == b[i]:
			result += "."
		else:
			result += "*"
	print(a)
	print(b)
	print(result)
	print()


n = int(input())
for _ in range(n):
	s1 = input()
	s2 = input()
	print_differences(s1, s2)
