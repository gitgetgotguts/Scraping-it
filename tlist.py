# test how to joiun a list of lists

import itertools

p=list(itertools.chain.from_iterable(L))
L=[['s','a'],['i'],['d','g','it']]

print(p)
