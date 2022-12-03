"""
# A Y
# B X
# C Z
# This strategy guide predicts and recommends the following:

# In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). 
# This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
# In the second round, your opponent will choose Paper (B), and you should choose Rock (X). 
# This ends in a loss for you with a score of 1 (1 + 0).
# The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
# In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

Win : 6
Draw: 3
Loss: 0
X : 1 (A)
Y : 2 (B)
Z : 3 (C)
"""
points = {'X':1,'Y':2,'Z':3}
drawRules = {'A':'X','B':'Y','C':'Z'}
winRules = {'A':'Y','B':'Z','C':'X'}
loseRules = {'A':'Z','B':'X','C':'Y'}
def part1(filename):
    score = 0
    input_file = open(filename, 'r')
    Lines = input_file.readlines()
    for line in Lines:
        score = score + points[line[2]] # Points based on what is selected
        if line[2] == drawRules[line[0]]:
            score = score + 3 # Points based on the same option selected
        if line[2] == winRules[line[0]]:
            score = score + 6 # Winning points
    return score

def part2(filename):
    score = 0
    input_file = open(filename, 'r')
    Lines = input_file.readlines()
    for line in Lines:
        if line[2] == 'X':
            score = score + points[loseRules[line[0]]]
        if line[2] == 'Y':
            score = score + points[drawRules[line[0]]] + 3
        if line[2] == 'Z':
            score = score + points[winRules[line[0]]] + 6
    return score

if __name__ == "__main__":
    file = "input.txt"
    print(f'Your total score for part 1 is {part1(file)}')
    print(f'Your total score for part 2 is {part2(file)}')