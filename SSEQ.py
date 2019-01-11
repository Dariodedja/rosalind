def openfile(filename):
    f = open(filename)
    sequences = []
    for line in f:
        if not line.startswith('>'):
            sequences.append(line.rstrip('\n'))
    return sequences

def main(filename):
    dnastrings = openfile(filename)
    s = dnastrings[0]
    t = dnastrings[1]

    currentbase = -1
    subseqindex = []

    for base in t:
        currentbase += s.index(base) + 2
        subseqindex.append(currentbase)

        s = s[s.index(base) + 2::]

    print(' '.join(map(str, subseqindex)))

main("rosalind_sseq.txt")