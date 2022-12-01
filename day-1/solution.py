# Part 1
print(max([sum([int(line) for line in group.split('\n')]) for group in open('input.txt').read().split('\n\n')]))

# Part 2
print(sum(sorted([sum([int(line) for line in group.split('\n')]) for group in open('input.txt').read().split('\n\n')])[-3:]))