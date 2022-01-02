from Bio import SeqIO
# "dna.fasta"
query = SeqIO.parse(input("Name of fasta file: "), "fasta")

for i in query:
	print("Name: ", i.name)
	print("Description: ", i.description)
	print("Length: ", len(i))
	print("Reverse Compliment: ", i.reverse_complement())
	print("Reverse Compliment Sequence: ", i.reverse_complement().seq)
	print("\n\n\n\n")