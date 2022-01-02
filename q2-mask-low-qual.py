from Bio import SeqIO

# "ecoli.fastq"
c = SeqIO.parse(input("Name of fastq file: "), "fastq")
c = [i for i in c]

cutoff = int(input("Quality cut-off: "))

for k in range(len(c)):
    seq = list(c[k].seq)
    phred = c[k].letter_annotations['phred_quality']
    for j in range(len(seq)):
        if phred[j] < cutoff:
            seq[j] = 'N'
    print("Sequence at Index %d: "%(k), ''.join(seq))