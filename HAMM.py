def hammingdist(s, t):
    hamdist = []
    for i in range(len(s)):
        if s[i] != t[i]:
            hamdist.append(str(i))
    return len(hamdist)

print(hammingdist("GAGGATGATGAACGATTCTCGCGCGGAATCGCTTAAAGTGAGAGATAAAGAGGGACTAATACAAGCTCGTTAACAGGCCAAGTTTCCCTACGTCAATGTACCGGGTCTCTCGACCATGGTTACGATTCGGTAATTCCACAACGAAGATATGTGATGAAGAATGGATTCAGCCAAATATTTGTTTAAGGCCGGATCCCTCATAGTTCAGACAGGTTAAAATTCGTAATAGTAATGGTTAAGAGCAAGTATACCGACAGACTGCTTATGATGAATGAAGAGTCACCCCGTAGGCATCGTACACTTTTAACCGCCATTCGATGAAAGCGGCCAAAATAATTTATTGACGTATACGTGATAGGGCCTCAGCCCAGGACCAAGTCATCTACTGACCGTAAGATATCTACGCTTTCCGAGGTCCACTCCTCGATGTACAACGTGGAATCTAACGCGCCCTACCAGACACGTCTAGCGGGTCGAAGTCACCGTGGTTTTACCTCGAAGGGTCCACCGATCCAGTCTCTCTCTTTCTCTTAATACTTGCCATCCTCAGACTGACACGTGCCCCATAGGCTAATCCGCAGGGGGGCTGCTATCGGATTTAGTTCACCACCTAACCGCGACTTAGCTTAGAATGGGCCCCTTCTGGTCTGCTTGCAGACATTTACACTTCTCGTAGTTCTAGCCTGACATTCAAGAGACATCGCAGTCCCGGTTGTTATGGTGCTGGGCCGGCGGCTGCAGGCCTTTCAACAATAGGGTTGAGACGGAACTAACAAACTTCTGCGCGTTTTTGCCGTCATGATTGGCGGAAGTTCATCTTGAACACACTAAGTCTGAATGTGAAGTTTTTTTTGTCTAATCTTCAGTGGGCGAGTCGCTCGAATAATACGCTACGGGAGCGGGCCTGCCGCGGGGCACACCCGGGCGGAAACAAATGCAATCGGTTACTGTCAT", "GCTGCTTTTGGACAATGGTCGCGGGCAATGGCTTAGACACCCCGATACGGAGAGAAAAATTCAACTAGGGAAACTGGCCATGTCTTCCTATGTCGAAGTACCGTTTTGGCCAACTAGCGTGAAGTTCCGACGCTTACTCTTTCGCTATTGGTTTTGCGAAGTTGAATCCGCAAAATAGTAGTCGTTGGCGGGAACGCTCCTCGTTCCGACATAGCTGAATTGGTATTTCAGGGAGGAAACAGACAGTATATGGTTGGACCTTTTAGGGAGAACGCTTATTCACACCGACCGTCTGAGGTCGTAGGAACGGGTATTCGTTTAATCTACTCAATGTATCTGAGCGACGTAATCGAGACAAGGCCTTAGGCAGGTGCGAATTGAAGTTGTATCAGTGTGTTATGCCTCATCTCACCGGAGGACTGGCCGATGTAGCAATGCGAAACTACCGCTCTAAATGAATAGCGTATTCCCTCACTGCTGGACCCGAATTTTTTCCTGACGAGTCCACGGTTCCTATAGTCCTAGTTCTCTTTGTCAACGCGAGGAACGGTATGACCCCCGCCCCAGAGTCTGTACTGTTGCTACGCATTTGTCCGCACTAGGTAAGAAGCCGTGCCACACTTAGGCTAGAGGGTTACCCATCGGGTCTCTTATGGGTCCTATTCACTCCCCTTGGTTACGGTATTACAATCGAGAAACAGGAAATTTAAGTTTTTTATGATGCGACACCGGAGGTTCCCGGCACTTCTGCGATAGGGATATTATGAAAGTACCAAAATTCTACGCCGGCAAGGTGTGGAGTCTCGCGCAAATTCAACAATACGACACTAACGCTGGAACGAACGTTTTAATTCGGAAGTCTCCGGTGCCCGAATGGCGTCGTTTATTTGCTAAGTCCGACTGCCTGTCGGGGGGCACCCCCGGGCACGGGCAATAGCAATAGGCTTCGGAGTT"))