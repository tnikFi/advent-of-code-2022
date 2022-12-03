# Part 1
print(sum([ord(item[0]) - ord('a') + 1 if item[0].islower() else ord(item[0]) - ord('A') + 27 for item in [list(set(rucksack[:len(rucksack)//2]).intersection(rucksack[len(rucksack)//2:])) for rucksack in open("input.txt").read().splitlines()]if len(item) > 0]))

# Part 2
with open("input.txt") as file: lines=file.read().splitlines(); print(sum([ord(item[0]) - ord('a') + 1 if item[0].islower() else ord(item[0]) - ord('A') + 27 for item in [list(set(lines[i]).intersection(lines[i+1]).intersection(lines[i+2])) for i in range(0, len(lines), 3)]]))