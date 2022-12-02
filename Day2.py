
score = 0

rockscore = 1
paperscore = 2
scissorsscore = 3
lostscore = 0
drawscore = 3
winscore = 6

score = 0

# Read puzzle input
f = open("day2a.txt")
for x in f:
    # process this round
    x[0]   # opponent play
    x[2]   # our play

    # calculate the 'shape' score
    if x[2] == "X":
        # rock
        score += rockscore
    if x[2] == "Y":
        # paper
        score += paperscore
    if x[2] == "Z":
        # scissors
        score += scissorsscore

    #
    # calculate if we won
    # 
    if x[2] == "X":   # lose
        if x[0] == "A": # rock - draw
            score += drawscore
        if x[0] == "B": # paper - lose
            score += lostscore
        if x[0] == "C": # scissors - win
            score += winscore

    if x[2] == "Y":   # win
        if x[0] == "A": # rock - win
            score += winscore
        if x[0] == "B": # paper - draw
            score += drawscore
        if x[0] == "C": # scissors - lose 
            score += lostscore

    if x[2] == "Z":   # draw
        if x[0] == "A": # rock - lose
            score += lostscore
        if x[0] == "B": # paper - win
            score += winscore
        if x[0] == "C": # scissors - draw
            score += drawscore

print(score)
