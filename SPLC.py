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
    # Create a codon dictionary
    bases = ['t', 'c', 'a', 'g']
    codontable = [a + b + c for a in bases for b in bases for c in bases]
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    codondict = dict(zip(codontable, amino_acids))

    # Create list of codons in RNA
    rna = rna.lower()
    codonfrags = [rna[i:i + 3] for i in range(0, len(rna)-1, 3)]

    # Translate RNA to protein
    protein = ""
    for codon in codonfrags:
        if codondict[codon] != '*':
                protein += codondict[codon]
        else:
            pass
    return protein


def main(filename):
    dnastrings = parse_fasta(filename)
    # Set original DNA to the full list at the start
    fulldna = dnastrings[0]

    # Remove the full DNA from original list
    dnastrings = dnastrings[1::]

    # Remove introns from dnastring to leave exons
    for intron in dnastrings:
        fulldna = fulldna.replace(intron, "")

    # Return protein encoded output
    return(encoding(fulldna))

print(main("rosa.txt"))