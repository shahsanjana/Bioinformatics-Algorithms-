f = open('rosalind_iprb.txt', 'r').read().split()
i = map(int,f)
p = 0
for n in i:
    p = p+n

k = i[0]
m = i[1]
n = i[2]

dominant = (4 * (k * (k - 1) + 2 * k * m + 2 * k * n + m * n) + 3 * m *(m - 1)) / (float(4 * p * (p- 1)))
#print dominant
print '%.5f' % dominant