# Part 1
print(sum([(lambda playerChoice: 1 if playerChoice == "X" else (2 if playerChoice == "Y" else 3))(game.split(" ")[1])+(lambda choices: 0 if ((choices[0] == "A" and choices[1] == "Z") or (choices[0] == "B" and choices[1] == "X") or (choices[0] == "C" and choices[1] == "Y")) else (3 if ord(choices[1]) == ord(choices[0]) + 23 else 6))(game.split(" "))for game in open("input.txt").read().split("\n")]))

# Part 2
print(sum([(lambda choices: (lambda opponentChoice: 1 if opponentChoice == "B" else (2 if opponentChoice == "C" else 3))(choices[0]) if choices[1] == "X" else (ord(choices[0]) - 64 if choices[1] == "Y" else (lambda opponentChoice: 1 if opponentChoice == "C" else (2 if opponentChoice == "A" else 3))(choices[0])))(game.split(" "))+{"X": 0, "Y": 3, "Z": 6}[game.split(" ")[1]] for game in open("input.txt").read().split("\n")]))