import sys
from math import factorial


input1=sys.argv[1]
input2=sys.argv[2]

k=int(input1)
N=int(input2)
                                                                   
P = 2**k                                                                       
probability = 0                                                                
for i in range(N, P + 1):                                                      
    v = (factorial(P) /                                                
            (factorial(i) * factorial(P - i))) * (0.25**i) * (0.75**(
                P - i))                                                        
    probability += v                                                       
print probability