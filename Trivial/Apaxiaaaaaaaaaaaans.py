name = input()
new_name = ""
previous_character = ""
for character in name:
	character = str(character)
	if character != previous_character:
		new_name += previous_character
		previous_character = character
new_name += previous_character
print(new_name)
