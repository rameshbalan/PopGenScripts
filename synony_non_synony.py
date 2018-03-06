#!/usr/bin/python

gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

seq1 = raw_input("Enter Sequence one\n")
seq2 = raw_input("Enter Sequence two\n")

i = 0
synonymous_substitutions = 0
non_synonymous_substitutions = 0

for codon in seq1:
    if i < len(seq1):
        if str(seq1[i:i+3]) != str(seq2[i:i+3]):
            if gencode[str(seq1[i:i+3])] == gencode[str(seq2[i:i+3])]:
                #print str(seq1[i:i+3]),str(seq2[i:i+3])
                #print gencode[str(seq1[i:i+3])],gencode[str(seq2[i:i+3])]
                synonymous_substitutions += 1
            else:
                #print str(seq1[i:i+3]),str(seq2[i:i+3])
                #print gencode[str(seq1[i:i+3])],gencode[str(seq2[i:i+3])]
                non_synonymous_substitutions +=1
            i += 3
print "Number of Synonymous Substitutions is %s" % synonymous_substitutions
print "Number of Non-Synonymous Substitutions is %s" % non_synonymous_substitutions
synonymous_sites = 0
non_synonymous_sites = 0
def find_synony_non_synony(seq):
    i = 0
    synonymous_sites = 0
    non_synonymous_sites = 0
    for codon in range(0,len(seq)+1,3):
        if i < len(seq):
        #if str(seq1[i:i+3]) != str(seq2[i:i+3]):
            if seq[i] == "A":
                new_seq = "T"+seq[i+1]+seq[i+2]
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
                new_seq = "G"+seq[i+1]+seq[i+2]
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
                new_seq = "C"+seq[i+1]+seq[i+2]
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
            if seq[i] == "T":
                new_seq = "A"+seq[i+1]+seq[i+2]
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
                new_seq = "G"+seq[i+1]+seq[i+2]
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
                new_seq = "C"+seq[i+1]+seq[i+2]
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
            if seq[i] == "G":
                new_seq = "T"+seq[i+1]+seq[i+2]
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
                new_seq = "A"+seq[i+1]+seq[i+2]
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
                new_seq = "C"+seq[i+1]+seq[i+2]
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
            if seq[i] == "C":
                new_seq = "T"+seq[i+1]+seq[i+2]
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
                new_seq = "G"+seq[i+1]+seq[i+2]
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
                new_seq = "A"+seq[i+1]+seq[i+2]
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
            if seq[i+1] == "A":
                new_seq = seq[i]+"T"+seq[i+2]
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
                new_seq = seq[i]+"G"+seq[i+2]
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
                new_seq = seq[i]+"C"+seq[i+2]
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
            if seq[i+1] == "T":
                new_seq = seq[i]+"A"+seq[i+2]
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
                new_seq = seq[i]+"G"+seq[i+2]
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
                new_seq = seq[i]+"C"+seq[i+2]
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
            if seq[i+1] == "G":
                new_seq = seq[i]+"A"+seq[i+2]
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
                new_seq = seq[i]+"C"+seq[i+2]
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
                new_seq = seq[i]+"T"+seq[i+2]
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
            if seq[i+1] == "C":
                new_seq = seq[i]+"G"+seq[i+2]
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
                new_seq = seq[i]+"T"+seq[i+2]
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
                new_seq = seq[i]+"A"+seq[i+2]
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
            if seq[i+2] == "A":
                new_seq = seq[i]+seq[i+1]+"T"
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
                new_seq = seq[i]+seq[i+1]+"G"
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
                new_seq = seq[i]+seq[i+1]+"C"
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
            if seq[i+2] == "T":
                new_seq = seq[i]+seq[i+1]+"A"
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
                new_seq = seq[i]+seq[i+1]+"G"
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
                new_seq = seq[i]+seq[i+1]+"C"
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
            if seq[i+2] == "G":
                new_seq = seq[i]+seq[i+1]+"A"
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
                new_seq = seq[i]+seq[i+1]+"T"
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
                new_seq = seq[i]+seq[i+1]+"C"
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
            if seq[i+2] == "C":
                new_seq = seq[i]+seq[i+1]+"A"
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
                new_seq = seq[i]+seq[i+1]+"G"
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
                new_seq = seq[i]+seq[i+1]+"T"
                if gencode[new_seq] == gencode[seq[i:i+3]]:
                    synonymous_sites += float(1)/3
                else:
                    non_synonymous_sites += float(1)/3
        i += 3
        #print (synonymous_sites,non_synonymous_sites)
    return (synonymous_sites,non_synonymous_sites)

syn_non_syn_seq1 = find_synony_non_synony(seq1)

syn_non_syn_seq2 = find_synony_non_synony(seq2)

syn = syn_non_syn_seq1[0] + syn_non_syn_seq2[0]
non_syn = syn_non_syn_seq1[1] + syn_non_syn_seq2[1]

i = 0
codons = [seq1[i:i+3] for i in range(0, len(seq1), 3)]
codons.extend([seq2[i:i+3] for i in range(0, len(seq2), 3)])


'''
if ('TGA' or 'TGT' or 'TGC' or 'TGG') in codons:
    print 'hi'
    non_syn = non_syn - 2.6666666667
    non_syn = non_syn + 1.5
    syn = syn - 0.33333333333
    syn = syn + 0.5

print "Number of Synonymous Sites is %s" % syn
print "Number of Non-Synonymous Sites is %s" % non_syn

if ('TAA' or 'TAC' or 'TAT' or 'TAG') in codons:
    print 'hi2'
    non_syn = non_syn - 0.6666666667
    #non_syn = non_syn + 2
    syn = syn - 0.33333333333
    #syn = syn + 1
'''
print '*******************************************'
print 'WARNING: TG* CODONS AND TA* CODONS ARE NOT ACCOUNTED FOR UNEQUAL CONTRIBUTION'
print '*******************************************'
print syn_non_syn_seq1
print syn_non_syn_seq2
print "Number of Synonymous Sites is %s" % syn
print "Number of Non-Synonymous Sites is %s" % non_syn

dn = float(non_synonymous_substitutions)/(non_syn/2)
ds = float(synonymous_substitutions)/(syn/2)

print dn
print ds

ratio = float(dn)/ds

print 'dn/ds ratio is %s' % ratio
