identifiers = open('input.txt').readlines()

threes = 0
twos = 0

for identifier in identifiers:
    chars = {}
    for char in identifier:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    if any(chars[char] == 3 for char in chars): threes += 1
    if any(chars[char] == 2 for char in chars): twos += 1

print(threes * twos)
