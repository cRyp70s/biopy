import statistics

from Bio import SeqIO
from Bio.SeqUtils import GC
# "flax_seq.fasta"
query = list(SeqIO.parse(input("Name of fasta file: "), "fasta"))
b=[len(x) for x in query]

print("Average Read Length: ", statistics.mean(b))
print("Median Read Length: ", statistics.median(b))

b = [GC(i.seq) for i in query]
print("Average GC Content: ", statistics.mean(b))

n_count = 0
for i in query:
	n_count += i.seq.count('N')

print("Number of ambiguous bases ('N'): ", n_count)
