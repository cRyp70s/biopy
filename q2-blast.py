import Bio.SearchIO

query=next(Bio.SearchIO.parse("blast_output.xml", 'blast-xml'))

for i in range(len(query)):
    for j in range(len(query[i])):
        print("For hit: %d. hsp: %d. \t length: "%(i, j), len(query[i][j].query.seq))

