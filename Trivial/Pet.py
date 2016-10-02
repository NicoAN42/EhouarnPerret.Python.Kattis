contestant_winner_score = 0
contestant_winner = 1
for contestant in range(1, 5 + 1):
	grades = [int(token) for token in input().split()]
	contestant_score = sum(grades)
	if contestant_score > contestant_winner_score:
		contestant_winner = contestant
		contestant_winner_score = contestant_score
print(contestant_winner, contestant_winner_score)
