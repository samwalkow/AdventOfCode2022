## Intructions:

# The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

# For example, suppose you were given the following strategy guide:

# A Y
# B X
# C Z

# This strategy guide predicts and recommends the following:

#     In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
#     In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
#     The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.

# In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

# What would your total score be if everything goes exactly according to your strategy guide?

file = open("./Day2Input.txt", "r")

# test file
#file = open("./TestDay2Input.txt", "r")
#file = open("./Test2Day2Input.txt")


total_score = 0

for line in file:
    # score from type of move
    # score from a win or loss
    round_score = 0
    if line[2] == "X":
        round_score += 1
        print("Rock was played")
        if line[0] == "A":
            round_score += 3
            print("Rock and rock was played for draw")
        if line[0] == "B":
            round_score += 0
            print("Rock losses to Paper ):")
        if line[0] == "C":
            round_score += 6
            print("Rock wins over Scissors!")
    if line[2] == "Y":
        round_score += 2
        print("Paper was played")
        if line[0] == "A":
            round_score += 6
            print("Paper wins over Rock!")
        if line[0] == "B":
            round_score += 3
            print("Paper and paper was played for draw")
        if line[0] == "C":
            round_score += 0
            print("Paper losses to Scissors ):")
    if line[2] == "Z":
        round_score += 3
        print("Scissors was played")
        if line[0] == "A":
            round_score += 0
            print("Scissors losses to Rock ):")
        if line[0] == "B":
            round_score += 6
            print("Scissors wins over Paper!")
        if line[0] == "C":
            round_score += 3
            print("Scissors and sciossors was played for draw")
    print("Round Score:", round_score)
    total_score += round_score
    
print("Total score:", total_score)
print()   
    
## Part 2 solution

## Instructions:

# The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

# The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

#     In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
#     In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
#     In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.

# Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

# Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?


total_score = 0

for line in file:
    # score from type of move
    # score from a win or loss
    round_score = 0
    if line[2] == "X":
        # I need to lose
        if line[0] == "A":
            # need to lose to rock, play scissors
            round_score += 3
            print("Scissors was played and loses to Rock")
        if line[0] == "B":
            # need to lose to paper, play rock
            round_score += 1
            print("Rock was played and losses to Paper")
        if line[0] == "C":
            # need to lose to scissors, play paper
            round_score += 2
            print("Paper is played and losses to Scissors")
    if line[2] == "Y":
        # I need to draw
        if line[0] == "A":
            # I need to draw with rock, play rock
            round_score += 4
            print("Rock and rock create a draw")
        if line[0] == "B":
            # I need to draw with paper, play paper
            round_score += 5
            print("Paper and paper was played for draw")
        if line[0] == "C":
            # I need to draw with scissors
            round_score += 6
            print("Scissors and scissors create a draw")
    if line[2] == "Z":
        # I need to win
        if line[0] == "A":
            # I need to win against rock, play paper
            round_score += 8
            print("Paper wins over Rock!")
        if line[0] == "B":
            # I need to win against paper, play scissors
            round_score += 9
            print("Scissors wins over Paper!")
        if line[0] == "C":
            # I need to win against scissors, play rock
            round_score += 7
            print("Rock wins over Scissors!")
    print("Round Score:", round_score)
    total_score += round_score
    
print("Total score:", total_score)
print() 


