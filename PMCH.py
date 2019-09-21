import Bio.SeqIO
from math import factorial

seqList=[]
inFile = open('rosalind_pmch.txt', 'r')
for record in Bio.SeqIO.parse(inFile, 'fasta'):
    seqList.append(str(record.seq))
sequence = seqList[0]
#print sequence

As = sequence.count("A")
Gs = sequence.count("G")

perfect_matchings = factorial(As) * factorial(Gs)
print perfect_matchings
#AU = 0
#GC = 0
#for nt in sequence:
#    if nt == 'A':
#        AU += 1
#    elif nt == 'G':
#        GC += 1

#matchings = factorial(AU) * factorial(GC)
#print(matchings)