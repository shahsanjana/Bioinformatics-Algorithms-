import itertools 

Input = "A B C D E F G H I J"
n = 2

split_input = list(Input.split(" "))


results= itertools.product(split_input,repeat=n)


for item in results:
    print "".join(item)