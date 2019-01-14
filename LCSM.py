def openingreadframes():
    rosalind = open("rosalind_lcsm.txt","r")
    fragment = rosalind.readlines()
    strs=[]
    for line in fragment:
        if line.startswith(">"):
            strs.append("kiko")
        else:
            strs.append(line.rstrip("\n"))
    rosalind.close()
    strs = strs[1:]
    joint = "".join(strs)
    joint_s = joint.split("kiko")

    theOne = joint_s[0]
    rest = joint_s[1:]

    start=0
    end=2
    matches=[]

    while end < len(theOne):
        while all(theOne[start:end] in seq for seq in rest):
            end += 1
        else:
            matches.append(theOne[start:end-1])
            end += 1
        start = start+1
    print(max(matches, key=len))

openingreadframes()
