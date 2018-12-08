claims = open('input.txt').readlines()

fabric = [[0 for x in range(1000)] for x in range(1000)]

for claim in claims:
	claim_split = claim.split()
	point_split = claim_split[2].split(',')
	x_point = int(point_split[0])
	y_point = int(point_split[1][:-1])
	width = int(claim_split[3].split('x')[0])
	height = int(claim_split[3].split('x')[1])

	for x in range(width):
		for y in range(height):
			fabric[x_point+x][y_point+y] += 1

count = 0
for x in range(len(fabric)):
	for y in range(len(fabric[x])):
		if fabric[x][y] > 1:
			count += 1

print(count)