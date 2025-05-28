# Generating Permutations 
# option 1:
int_str = "1487"
permutations_list = [a+b+c+d for a in int_str for b in int_str if b!=a for c in int_str if c not in(a,b) for d in int_str if d not in (a,b,c)]
print(permutations_list[:4], len(permutations_list))
# option 2:
permutations4digits = lambda s: [a+b+c+d for a in s for b in s if b!=a for c in s if c not in(a,b) for d in s if d not in (a,b,c)]
permutations_list1 = permutations4digits("1487")
print(permutations_list1[:4], len(permutations_list1))
print(set(permutations_list1) == set(permutations_list1))
# option 3:
from itertools import permutations
permut_func = lambda digits, length: ["".join(d) for d in permutations(digits,length) if len(set(d)) == length]
permutations_list2 = permut_func("1487", 4)
print(permutations_list2[:4], len(permutations_list2))
print(set(permutations_list1) == set(permutations_list2))
