def fibd(n, k=1):
    ages = [1] + [0] * (k - 1)
    for i in xrange(n - 1):
        ages = [sum(ages[1:])] + ages[:-1]
    return sum(ages)

print fibd(85,17)