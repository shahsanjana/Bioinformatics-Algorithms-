#s = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC" 
import sys

s = sys.stdin.readline()

print s.count("A"), s.count("C"), s.count("G"), s.count("T")