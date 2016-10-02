def move_ball(current, left, right):
	if current == left:
		return right
	elif current == right:
		return left
	else:
		return current


def find_last_position(moves):
	position = 1
	for move in moves:
		if move == "A":
			position = move_ball(position, 1, 2)
		elif move == "B":
			position = move_ball(position, 2, 3)
		elif move == "C":
			position = move_ball(position, 1, 3)
	return position


s = input()
cup = find_last_position(s)
print(cup)
