candidates = \
{
	"Adrian": ["ABC", 0],
	"Bruno": ["BABC", 0],
	"Goran": ["CCAABB", 0]
}
n = int(input())
answers = input()
for i in range(n):
	answer = answers[i]
	for key in candidates:
		value = candidates[key][0]
		index = i % len(value)
		candidate_answer = value[index]
		if candidate_answer == answer:
			candidates[key][1] += 1
candidates = list(candidates.items())
best_candidate_score = max(candidates, key=lambda item: item[1][1])[1][1]
candidates.sort(key=lambda item: item[0])
print(best_candidate_score)
for candidate in candidates:
	candidate_score = candidate[1][1]
	if candidate_score == best_candidate_score:
		candidate_name = candidate[0]
		print(candidate_name)
