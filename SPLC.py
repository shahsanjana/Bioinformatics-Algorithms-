import sys
import Bio.SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna


inFile = open("rosalind_splc.txt","r")

seqList = []

for record in Bio.SeqIO.parse(inFile,'fasta'):
    seqList.append(str(record.seq))


sequence = seqList[0]
introns = seqList[1:]


exon = []

for i in introns:
    sequence = sequence.replace(i,"")
    #print sequence
    

exons = Seq(sequence,generic_dna)

print exons.translate(to_stop=True)