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

for claim in claims:
    claim_split = claim.split()
    point_split = claim_split[2].split(',')
    x_point = int(point_split[0])
    y_point = int(point_split[1][:-1])
    width = int(claim_split[3].split('x')[0])
    height = int(claim_split[3].split('x')[1])

    intact_claim = True
    for x in range(width):
        for y in range(height):
            if fabric[x_point+x][y_point+y] != 1:
                intact_claim = False

    if intact_claim:
        print(claim.split()[0][1:])

