from itertools import permutations
from itertools import combinations
l=[1,2,3]
parm=permutations(l,3)
p=[]
for i in parm:
    p.append(i)
print(p)
comb=combinations(l,3)
c=[]
for i in comb:
    c.append(i)
print(c)
