def DNAsubsstring(s, t):
    repeats = ""
    for a in range(len(s)):
        if s.find(t, a) == a:
            repeats += str(a + 1) + " "
    return repeats[:-1]


print(DNAsubsstring("GATATATGCATATACTT", "ATAT"))