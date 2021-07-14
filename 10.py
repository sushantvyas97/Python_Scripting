def reachTrgt(trgt):
    trgt = abs(trgt)

    sum = 0
    step = 0
    while (sum < trgt or (sum - trgt) %
           2 != 0):
        step = step + 1
        sum = sum + step
    return step

trgt = 1000000000
print(reachTrgt(trgt))
