identifiers = [x.strip() for x in open('input.txt').readlines()]

for identifier in identifiers:
    for search in identifiers:
        mismatches = 0
        position = 0
        for x in range(len(identifier)):
            if identifier[x] != search[x]:
                mismatches += 1
                position = x
        if mismatches == 1:
            answer = identifier[0:position] + identifier[position + 1:]
            print(answer)
            exit()
