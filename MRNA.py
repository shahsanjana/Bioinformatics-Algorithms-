import sys


f= open('rosalind_mrna.txt', 'r')
seq = f.read().strip()


AAs    = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
Starts = '---M---------------M---------------M----------------------------'
Base1  = 'UUUUUUUUUUUUUUUUCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG'
Base2  = 'UUUUCCCCAAAAGGGGUUUUCCCCAAAAGGGGUUUUCCCCAAAAGGGGUUUUCCCCAAAAGGGG'
Base3  = 'UCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAG'

freq = {}
for i in AAs:
    if not freq.has_key(i):
        freq[i] = 0
    freq[i] += 1


variations = freq['*']


for prot in seq:
    variations *= freq[prot]

print >> sys.stdout, variations % 1000000