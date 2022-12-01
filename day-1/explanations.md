# Part 1

```py
print(max([sum([int(line) for line in group.split('\n')]) for group in open('input.txt').read().split('\n\n')]))
```

First, let's examine what we know and what we actually need to do.

 - We have an input file with groups of numbers.
    - Each group has one number per line. In other words, each number ends with a newline character.
    - In this file, each group is separated by an empty line.
       - Because we know that each number ends with a newline, and each group is separated by an empty line, we can split the input file by `\n\n` to get a list of groups.
 - We need to find the sum of each group and then output the largest sum.

<br>

Let's make the code slightly easier to read by splitting it up into multiple lines and add some comments to see what's going on.


```py
print(
    # Get the largest value in the list of sums
    max(
        # Use list comprehension to find the sum of each group
        [
            # For each group, split it by newlines and sum the numbers.
            sum(
                [
                    int(line)               # Convert each line to an integer in order to sum them.
                    for line                # For each line in the group...
                    in group.split('\n')    # Split the group by newlines to get a list of individual numbers.
                ]
            )
            for group               # For each group in the list of groups we get below
            in open('input.txt')    # Open the input file
                .read()             # Read the contents of the file, which returns a string
                .split('\n\n')      # Split the string by '\n\n' to get a list of groups
        ]
    )
)
```

<br>

# Part 2

```py
print(sum(sorted([sum([int(line) for line in group.split('\n')]) for group in open('input.txt').read().split('\n\n')])[-3:]))
```

Just like in part 1, we know that the numbers in the input file are separated by newlines, and that each group is separated by an empty line. We also know that we need to find the sum of each group. However, this time instead of just returning the largest sum, we need to return the sum of the three largest sums. The easiest way to do this is to sort the list of sums and then extract the last three elements and sum them.

```py
print(
    # Sum the last three elements in the list of sums
    sum(
        # Create a sorted list of the sums in ascending order
        sorted(
            # Find the sum of each group in the file
            [
                sum(
                    [int(line) for line in group.split('\n')]   # Same as part 1
                )
                for group
                in open('input.txt')    # Just like in part 1, we get a list of groups
                    .read()
                    .split('\n\n')
            ]
        )[-3:]  # Extract the last three elements to get a list of the three largest values
    )
)
```