from enum import Enum


class Card(Enum):
	Tablet = "T"
	Compass = "C"
	Gear = "G"


cards = {Card.Tablet: 0, Card.Compass: 0, Card.Gear: 0}
s = input()
for c in s:
	if c == Card.Tablet.value:
		cards[Card.Tablet] += 1
	elif c == Card.Compass.value:
		cards[Card.Compass] += 1
	else:
		cards[Card.Gear] += 1
score = 0
for key in cards:
	value = cards[key]
	score += value ** 2
sets = min(cards.values())
set_bonus = sets * 7
score += set_bonus
print(score)
