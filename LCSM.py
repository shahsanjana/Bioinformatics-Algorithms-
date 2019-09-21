import Bio.SeqIO
seq = []
f = open("rosalind_lcsm.txt", "r")
for handle in (Bio.SeqIO.parse(f, "fasta")):
    seq.append(handle.seq)


seqs = sorted(seq, key=len)
shortest = seqs[0]
others = seqs[1:]
motif = ''
for i in range(len(shortest)):
    for j in range(i, len(shortest)):
        m = shortest[i:j + 1]
        found = False
        for s in others:
            if m in s:
                found = True
            else:
                found = False
                break
        if found and len(m) > len(motif):
            motif = m
print motif