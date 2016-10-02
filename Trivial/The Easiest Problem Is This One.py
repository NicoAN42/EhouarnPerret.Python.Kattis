def sum_digits(number):
	digits = [int(str_digit) for str_digit in str(number)]
	result = sum(digits)
	return result


while True:
	n = int(input())
	if n == 0:
		break
	else:
		sum_n = sum_digits(n)
		for p in range(11, 100000):
			m = n * p
			if sum_digits(m) == sum_n:
				print(p)
				break
