set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1-set2)

set1 = frozenset(set1)
set2 = frozenset(set2)
print(set1-set2)