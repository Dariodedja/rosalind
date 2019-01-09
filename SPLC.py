def parse_fasta(filename):
    f = open(filename)
    sequences = []
    oneline = ''
    for line in f:
        if not line.startswith('>'):
            oneline += line.rstrip('\n')
        else:
            sequences.append(oneline)
            oneline = ''
    sequences.append(oneline)
    sequences.pop(0)
    return sequences

def encoding(rna):
    bases = ['t', 'c', 'a', 'g']
    codontable = [a + b + c for a in bases for b in bases for c in bases]
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    codondict = dict(zip(codontable, amino_acids))
    rna = rna.lower()
    codonfrags = [rna[i:i + 3] for i in range(0, len(rna)-1, 3)]
    protein = ""
    for codon in codonfrags:
        if codondict[codon] != '*':
                protein += codondict[codon]
        else:
            pass
    return protein

def main(filename):
    dnastrings = parse_fasta(filename)
    fulldna = dnastrings[0]
    dnastrings = dnastrings[1::]
    for intron in dnastrings:
        fulldna = fulldna.replace(intron, "")
    return(encoding(fulldna))

print(main("rosa.txt"))
