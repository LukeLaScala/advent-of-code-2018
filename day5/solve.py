import sys

sys.setrecursionlimit(10000)
polymer = open('input.txt').read()

def reduce(polymer):
	polymer = list(polymer)
	for x in range(len(polymer) - 1):
		if polymer[x] != polymer[x + 1] and polymer[x].lower() == polymer[x + 1].lower():
			polymer[x] = '_'
			polymer[x + 1] = '_'
	if '_' in polymer:
		return reduce(''.join(polymer).replace('_', ''))
	else:
		return polymer

print(len(''.join(reduce(polymer))))