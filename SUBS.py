#a="GATATATGCATATACTT"
#b="ATAT"
f = open('rosalind_subs.txt', 'r').read().split()
a=f[0]
b=f[1]


index = 0
while index < len(a):
    index = a.find(b, index)
    if index == -1:
        break
    index += 1
    print(index),