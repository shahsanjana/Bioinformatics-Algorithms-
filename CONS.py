import sys
from Bio import SeqIO

f = open('rosalind_cons.txt')


for record in SeqIO.parse('rosalind_cons.txt', "fasta"):
    seqlength = len(record.seq)

A = [0]*seqlength
T = [0]*seqlength
C = [0]*seqlength
G = [0]*seqlength

file = open('rosalind_cons.txt')
for seq_record in SeqIO.parse(file, "fasta"):
    for i, nuc in enumerate(seq_record.seq):
        if nuc == "A":
            A[i] += 1
        elif nuc == "C":
            C[i] += 1
        elif nuc == "G":
            G[i] += 1
        else:
            T[i] += 1
file.close()



consensus_seq = ""

for i in range(seqlength):
    consensus = ("A", A[i])
    if C[i] > consensus[1]:
        consensus= ("C", C[i])
    if G[i] > consensus[1]:
        consensus= ("G", G[i])
    if T[i] > consensus[1]:
        consensus=("T", T[i])
    consensus_seq += consensus[0]

results=open("results","w")
consensus_seq
A= ' '.join(map(str,A))
C= ' '.join(map(str,C))
G= ' '.join(map(str,G))
T= ' '.join(map(str,T))
results.write(consensus_seq), results.write("\n")
results.write("A: "), results.write(A), results.write("\n")
results.write("C: "), results.write(C), results.write("\n")
results.write("G: "), results.write(G), results.write("\n")
results.write("T: "), results.write(T), results.write("\n")

results.close()