import itertools

def permutation(position):
	leads = ''
	for i in range(1,position+1):
		leads += str(i)
	permlist = ([x for x in itertools.permutations(leads)])
	print(len(permlist))
	for i in permlist:
		print(' '.join(map(str, i)))

permutation(6)