frequencies = {0}

counter = 0
current = 0
lines = open('input.txt').readlines()
while True:
	current += int(lines[counter % len(lines)])
	if current in frequencies:
		print(current)
		exit()
	frequencies.add(current)
	counter += 1
