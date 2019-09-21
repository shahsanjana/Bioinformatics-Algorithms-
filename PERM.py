from itertools import permutations

n=5
num = list(permutations(range(1, n+1)))

permutation=[' '.join(map(str, i)) for i in num]

print len(num)
for item in permutation:
    print item