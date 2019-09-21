import Bio.SeqIO
file = open("rosalind_grph.txt", "rU")

records =  Bio.SeqIO.to_dict(Bio.SeqIO.parse(file, "fasta"))
#print records["Rosalind_1675"]
#print records.items()
overlaplist = []
for rec, attrib in records.items():
	
	overlaps = [(s.id, s.seq) for s in records.values() if attrib.seq[-3:] in s.seq[0:3]]
	
	for i in overlaps:
		if i[0] != rec: 
			overlaplist.append((rec, i[0]))

#print overlaplist
for o in overlaplist:
    print o[0], o[1]