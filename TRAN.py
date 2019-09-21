from Bio import SeqIO                        
seqList = []                               
file = open('rosalind_tran.txt', 'r')       
for record in SeqIO.parse(file, 'fasta'):  
    seqList.append(str(record.seq))        
file.close()     

s1 = seqList[0]                            
s2 = seqList[1]  

comp_seq = zip(s1,s2)


trans ={"A":"G","G":"A","C":"T","T":"C"}

transition = 0 
transversion = 0 

for x,y in comp_seq:
    if x!=y:
        if trans[x]==y:
            transition+=1
        else: 
            transversion+=1

prob = transition/float(transversion)

print prob