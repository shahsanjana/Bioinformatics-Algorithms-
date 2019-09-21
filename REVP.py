from Bio import SeqIO

File = open("rosalind_revp.txt", "r")

for rec in SeqIO.parse(File, 'fasta'):
    forward = rec.seq

reverse = forward.complement()

for i in range(len(forward)):
    #range is exclusive
    for j in range(4, 13):
        if i + j <= len(forward) and forward[i:i + j] == reverse[i:i + j][::-1]:
                print i + 1, j