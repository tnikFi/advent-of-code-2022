# Part 1
print(len([x for x in [[sections[0].split("-"), sections[1].split("-")] for sections in [pair.split(",") for pair in open("input.txt").read().splitlines()]] if (int(x[0][0]) >= int(x[1][0]) and int(x[0][1]) <= int(x[1][1])) or ((int(x[0][0]) <= int(x[1][0]) and int(x[0][1]) >= int(x[1][1])))]))

# Part 2
print(len([x for x in [[sections[0].split("-"), sections[1].split("-")] for sections in [pair.split(",") for pair in open("input.txt").read().splitlines()]] if int(x[0][0]) <= int(x[1][1]) and int(x[0][1]) >= int(x[1][0])]))