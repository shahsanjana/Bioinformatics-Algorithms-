from Bio import SeqIO                      
seqList = []                             
handle = open('rosalind_sseq.txt', 'r')     
for record in SeqIO.parse(handle, 'fasta'):
    seqList.append(str(record.seq))      
handle.close()

sequence = seqList[0]                           
subseq = seqList[1]
print sequence, subseq                           


pos = 0                                    
indices  = []                             
for i in subseq:                    
    for j in range(pos, len(sequence)):
        if sequence[j] == i:
            indices.append(j+1)
            pos = j+1
            break 
for i in indices:
    print i,