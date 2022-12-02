# Part 1

```py
print(sum([(lambda playerChoice: 1 if playerChoice == "X" else (2 if playerChoice == "Y" else 3))(game.split(" ")[1])+(lambda choices: 0 if ((choices[0] == "A" and choices[1] == "Z") or (choices[0] == "B" and choices[1] == "X") or (choices[0] == "C" and choices[1] == "Y")) else (3 if ord(choices[1]) == ord(choices[0]) + 23 else 6))(game.split(" ")) for game in open("input.txt").read().split("\n")]))
```

Like yesterday, we'll begin by examining what we know about the task.
- Each line in the input file represents a single round.
- A, B and C represent rock, paper and scissors respectively, as do X, Y and Z.
- The first letter in each line represents the opponent's choice.
- The second letter in each line represents the player's choice.
- The letters are separated by a space.
- For each round, we need to find the sum of the player's score which is based on the player's choice and the outcome of the round.
- Finally, we need to get the total score of the player by summing the scores of each round.

```py
print(
    sum(
        [
            # Get the choice score.
            (
                # This lambda function returns the amount of points the player should get based on their choice.
                # Rock = 1 point, Paper = 2 points, Scissors = 3 points
                # Doing this with a dictionary instead would probably be more clear. Part 2 will use dictionaries
                # for similar purposes.
                lambda playerChoice: 1 if playerChoice == "X" else (2 if playerChoice == "Y" else 3)
            )(game.split(" ")[1])   # Call the lambda function with the player's choice
            + # Add the outcome score.
            (
                # This is a lambda function that takes the opponent and player choices as a list and returns
                # the score based on whether the round ended in a draw, or if the player won or lost.
                lambda choices: 0 if (
                    # Begin by testing the three possible losing combinations
                    (choices[0] == "A" and choices[1] == "Z") or    # Rock beats scissors
                    (choices[0] == "B" and choices[1] == "X") or    # Paper beats rock
                    (choices[0] == "C" and choices[1] == "Y")       # Scissors beats paper
                ) else (
                    # Here we do some math to check if the player chose the same option as the opponent.
                    # If the round is a tie, return 3, otherwise the player must have won, so return 6.
                    # I will explain the math a bit more further down.
                    3 if ord(choices[1]) == ord(choices[0]) + 23 else 6
                )
            )(game.split(" "))  # Call the above lambda function with the opponent and player choices
            for game
            in open("input.txt")    # Open the input file
                .read()             # Read the file
                .split("\n")        # Split the file into a list of rounds
        ]
    )
)
```

## So about the math

We determine whether a round is a tie by checking if the following expression is true:
```py
ord(choices[1]) == ord(choices[0]) + 23
```

Let's break this down a bit.
- `ord()` is a built-in Python function that returns the Unicode code point for a single character string.
- We know that the opponent's choice is always A, B or C and the player's choice is always X, Y or Z. If we convert these to their Unicode code points, we get the following:
    | Character | Corresponding choice | Unicode code point |
    | --- | --- | --- |
    | A | Rock | 65 |
    | B | Paper | 66 |  
    | C | Scissors | 67 |
    | X | Rock | 88 |
    | Y | Paper | 89 |
    | Z | Scissors | 90 |

- We can see that the difference between the player's choice and the opponent's choice is always 23.
- So, if the code point for the player's choice is 23 more than the opponent's choice, they both have chosen the same option, and the round is a tie.
- From this we get an equation that's true if and only if the round is a tie: $\text{player's choice} = \text{opponent's choice} + 23$

<br>

# Part 2

```py
print(sum([(lambda choices: {"A": 3, "B": 1, "C": 2}[choices[0]] if choices[1] == "X" else (ord(choices[0]) - 64 if choices[1] == "Y" else {"A": 2, "B": 3, "C": 1}[choices[0]]))(game.split(" "))+{"X": 0,"Y": 3,"Z": 6}[game.split(" ")[1]] for game in open("input.txt").read().split("\n")]))
```

The rules for part 2 are mostly the same as part 1, but there is a small difference: now X means the player should play whatever choice will result in their loss, Y means the player should tie with the opponent and Z means the player should win.


```py
print(
    # Get the total score by summing the scores of each round.
    sum(
        # Use list comprehension to create a list of scores for each round.
        [
            # Get the amount of points rewarded based on what option the player chose.
            (
                lambda choices:
                # If the player should lose, we know that the player's choice must be
                # scissors when the opponent chose rock, paper when the opponent chose scissors,
                # or rock when the opponent chose paper. Therefore, we can use the opponent's choice
                # to determine how many points the player should get for their own choice.
                # We can use a dictionary to map the opponent's choice to the amount of points the player should get.
                {
                    "A": 3,
                    "B": 1,
                    "C": 2
                }[choices[0]] if choices[1] == "X"  # Index the dictionary only if the player loses.
                else (
                    # Y means a tie, so calculate the choice score based on the opponent's choice.
                    # The math is similar to the math used in part 1, but instead of adding 23, we subtract 64 from
                    # the opponent's choice, which we know is equivalent to the player's choice in a tie.
                    # This will give us 1 for rock (A), 2 for paper (B) and 3 for scissors (C).
                    ord(choices[0]) - 64 if choices[1] == "Y"

                    # Player didn't lose or tie, so they must have won.
                    # Similarly to the loss case, we can use a dictionary to map the opponent's choice
                    # to the amount of points the player should get.
                    else {
                        "A": 2,
                        "B": 3,
                        "C": 1
                    }[choices[0]]
                )
            )(game.split(" "))  # Call the lambda function with the opponent and player choices
            +   # Add the outcome score.
            # We know that X means the player loses, Y is a tie and Z is a win.
            # We also know that a loss is worth 0 points, a tie is worth 3 points and a win is worth 6 points.
            # We can use a dictionary to map the outcome of the round to the amount of points.
            {
                "X": 0, # Loss
                "Y": 3, # Tie
                "Z": 6  # Win
            }[game.split(" ")[1]]    # Get the outcome score from the dictionary.
            for game
            in open("input.txt")
                .read()
                .split("\n")
        ]
    )
)