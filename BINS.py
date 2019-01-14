def bsearch(number ,Array):
    max = len(Array) - 1
    min = 0
    m = int((max + min) / 2)

    while True:
        if Array[m] == number:
            return m+1

        if Array[m] < number:
            min = m + 1
        elif Array[m] > number:
            max = m

        m = int((max + min) / 2)

        if max <= min:
            return -1

f = open('rosalind_bins.txt','r')
f = f.read()
f = f.splitlines()
f.pop(0)
f.pop(0)
array = []
keys = []
items = []

for i in f[0].split(' '):
    array.append(int(i))
for i in f[1].split(' '):
    keys.append(int(i))

for i in keys:
    items.append(bsearch(i, array))
for i in range(len(items)):
    items[i] = str(items[i])

print(' '.join(items))
