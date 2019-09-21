f= open("rosalind_iev.txt","r")

values = {}
count=1

for val in f.read().split():
    values.update({count:int(val)})
    count+= 1


E1,E2,E3 = 2,2,2
E4=2*.75
E5=2*.5

dominant_phenotype = values[1]*E1+values[2]*E2+values[3]*E3+values[4]*E4+values[5]*E5

print dominant_phenotype