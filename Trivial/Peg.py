def count_moves(a, x, y):
	character = a[x][y]
	if character == ".":
		count = 0
		rows = len(a)
		columns = len(a[x])
		# Top Check
		if ((x - 2) >= 0) and (a[x - 1][y] == "o") and (a[x - 2][y] == "o"):
			count += 1
		# Bottom Check
		if ((x + 2) < rows) and (a[x + 1][y] == "o") and (a[x + 2][y] == "o"):
			count += 1
		# Left Check
		if ((y - 2) >= 0) and (a[x][y - 1] == "o") and (a[x][y - 2] == "o"):
			count += 1
		# Right Check
		if ((y + 2) < columns) and (a[x][y + 1] == "o") and (a[x][y + 2] == "o"):
			count += 1
		return count
	else:
		return 0


moves = 0
size = 7
board = [input() for _ in range(size)]
for cx in range(size):
	for cy in range(size):
		moves += count_moves(board, cx, cy)
print(moves)
