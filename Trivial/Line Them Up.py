from enum import Enum


class string_order(Enum):
	neither = "NEITHER"
	increasing = "INCREASING"
	decreasing = "DECREASING"


def get_order(a, b):
	if a < b:
		return string_order.increasing
	else:
		return string_order.decreasing


n = int(input())
order = None
previous = input()
for _ in range(n - 1):
	current = input()
	if not order:
		order = get_order(previous, current)
	else:
		current_order = get_order(previous, current)
		if current_order != string_order.neither:
			if current_order != order:
				order = string_order.neither
	previous = current
print(order.value)
