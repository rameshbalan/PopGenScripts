#!/usr/bin/python
import pandas as pd
import collections as c
nucleotide = []
names = []
i = 0
with open ("rosalind_cons-4.txt","r") as in_file:
	with open ("rosa.fasta",'w') as out:
		for line in in_file:
			line.strip()
			if line[0] == ">":
				out.write('\n')
				out.write(line.rstrip())
				out.write('\n')
			else:
				out.write(line.rstrip('\n'))

with open("rosa.fasta","r") as infile:
	next(infile)
	for line in infile:
		if line.startswith(">"):
			names.append(line.rstrip())
		if not line.startswith(">"):
			length = len(line)
			nucleotide_list = tuple(line.rstrip())
			nucleotide.append((nucleotide_list))
	seq_df = pd.DataFrame(nucleotide,index=names)
	con_seq_df = pd.DataFrame(index=["A","C","G","T"])
	for i in range(0,length):
		a = c.Counter(seq_df.iloc[:,i])
		con_seq_df.loc["A",i] = int(a['A'])
		con_seq_df.loc["T",i] = int(a['T'])
		con_seq_df.loc["G",i] = int(a['G'])
		con_seq_df.loc["C",i] = int(a['C'])
	i = 0
	v = []
	consenus_sequence = []
	for i in range(0,length):
		v.append(con_seq_df.index[con_seq_df.iloc[:,i] == con_seq_df.iloc[:,i].max()].tolist())
	for value in v:
		consenus_sequence.append(value[0])
	#print(seq_df)
	print("".join(consenus_sequence))
	pd.options.display.float_format = '{:,.0f}'.format
	with pd.option_context('display.max_rows', 5, 'display.max_columns', 10000):
		print(con_seq_df.to_string())