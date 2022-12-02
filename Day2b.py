
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
    x[2]   # required outcome

    if x[2] == "X":   # lose
        if x[0] == "A": # rock - scissors
            score += lostscore
            score += scissorsscore
        if x[0] == "B": # paper - rock
            score += lostscore
            score += rockscore
        if x[0] == "C": # scissors - paper
            score += lostscore
            score += paperscore

    if x[2] == "Z":   # win
        if x[0] == "A": # rock - paper
            score += winscore
            score += paperscore
        if x[0] == "B": # paper - scissors
            score += winscore
            score += scissorsscore
        if x[0] == "C": # scissors - rock
            score += winscore
            score += rockscore

    if x[2] == "Y":   # draw
        if x[0] == "A": # rock - rock
            score += drawscore
            score += rockscore
        if x[0] == "B": # paper - paper
            score += drawscore
            score += paperscore
        if x[0] == "C": # scissors - scissors
            score += drawscore
            score += scissorsscore

print(score)
