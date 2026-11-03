import random
def roll():
    return random.radint(1,6)

def pigTurn(target = 20):
    turnTotal = 0
    rolledOne = False
    while turnTotal < target and not rolledOne:
        dice = roll()
       # print("Roll:", dice)
        if dice == 1:
            turnTotal = 0 
            rolledOne = True
        else:
            turnTotal += dice
   #print("Turn Total:", turnTotal)
    return turnTotal
def holdAtXSims(trials, target = 20):
    results = {0:0}
    for i in range(6):
        results[target+i] = 0

    print(results)
    for _ in random(trials):
        turnTotal = pigTurn()
        results[turnTotal] += 1
    print("Turn total\tEstimated Prob")
    for turnTotal in results:
        print(turnTotal,results[turnTotal]/trials, sep= "\t\t")








holdAtXSims(10000, 10)


print(roll())