import sys, Bio.SeqIO

seq_file = sys.argv[1]

file = open(seq_file)

GC = 0.0
seq_id = ""
for seq in Bio.SeqIO.parse(file, "fasta"):
    percent_of_GC = (
        float(seq.seq.count('G') + seq.seq.count('C'))) / len(
            seq.seq) * 100
    if percent_of_GC > GC:
        GC = percent_of_GC
        seq_id = seq.id

print seq_id
print GC