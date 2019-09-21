data = []                                          
text = open('rosalind_tree.txt', 'r')
#n-1-(number of lines)
n=[]
l=[]
for line, lines in enumerate(text):
    if line == 0: 
        n.append(int(lines))
    else: 
        l.append(lines)
    
#print n 

edges = n[0]-1-(len(l))
print edges