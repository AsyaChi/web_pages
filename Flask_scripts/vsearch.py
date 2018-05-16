def search4letters(phrase,letters="aeiuo"):
	return set(phrase).intersection(set(letters))

print(search4letters('The world around is so big and wonderfull'))

