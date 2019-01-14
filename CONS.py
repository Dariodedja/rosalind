def consfunction_inp(a):
    f = open(a, 'r')
    rawdna = ""
    for line in f:
        rawdna += line
    fragments = rawdna.split('\n')
    rosaid = []
    dnafrag = []
    for i in range(1,len(fragments)):
        if fragments[i][0] == '>':
            rosaid = ''.join(rosaid)
            dnafrag.append(rosaid)
            rosaid = []
        else:
            rosaid.append(fragments[i])
    return dnafrag
def consfunction(a):
    m = consfunction_inp(a)
    r = []
    for j in range(len(m[0])):
        A, C, G, T = 0, 0, 0, 0
        for i in range(len(m)):
            if m[i][j] =='A':
                A+=1
            elif m[i][j] =='C':
                C+=1
            elif m[i][j] =='G':
                G+=1
            elif m[i][j] =='T':
                T+=1
        r.append([A,C,G,T])
    cons=""
    for i in r:
        if i[0]==max(i):
            cons+='A'
        elif i[1]==max(i):
            cons+='C'
        elif i[2]==max(i):
            cons+='G'
        elif i[3]==max(i):
            cons+='T'
    print(cons)
    name = {0:'A:',1:'C:',2:'G:',3:'T:'}
    for i in range(4):
        line = name[i]
        for j in range(len(r)):
            line += (' '+str(r[j][i]))
        print(line)

consfunction("rosalind_cons.txt")