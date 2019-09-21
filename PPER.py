import itertools

n,k = 97,9
counter = 1
#can't be set at 0The statistic P(n,k) counts the total number of partial permutations of 
# k objects that can be formed from a collection of n objects. Note that P(n,n) is just the number of permutations 

for i in range(k):
    #*= multuplies previous value
    counter *= (n - i)
    #print counter
print(counter % 1000000)