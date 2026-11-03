
import random

def roll():
    return random.randint(1, 6)


def pigTurn(target=20, score=0):
    turnTotal = 0
    rolledOne = False

    while turnTotal < target and turnTotal + score < 100 and not rolledOne:
        dice = roll()
        # print("Roll:", dice)

        if dice == 1:
            turnTotal = 0
            rolledOne = True
        else:
            turnTotal += dice

    # print("Turn Total:", turnTotal)
    # print("New score:", score + turnTotal)

    return turnTotal


def holdAtXSims(trials, target=20):
    results = {0: 0}

    for i in range(target, target + 6):
        results[i] = 0

    for _ in range(trials):
        turnTotal = pigTurn(target)
        results[turnTotal] += 1

    print("Turn total\tEstimated Prob")

    for turnTotal in results:
        print(turnTotal, results[turnTotal] / trials, sep="\t\t")


def par4Test(score):
    for _ in range(3):
        score = score + pigTurn(20, score)
        print("Score:", score)
        print()


def solitaireGame(target=20):
    score = 0
    turns = 0

    while score < 100:
        score = score + pigTurn(target, score)
        turns += 1

    return turns


def avgTurns(trials, target=20):
    totalTurns = 0

    for _ in range(trials):
        totalTurns += solitaireGame(target)

    print(target, "Average turns:", totalTurns / trials, sep="\t")



for target in range(5, 50):
    avgTurns(10000, target)
