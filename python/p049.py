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
# difference martix -- check 
# Get absolute values
abs_df = df.abs()
# Compute the difference matrix
perms = permutations_list2
diff_table = [[row_val - col_val for col_val in perms] for row_val in perms]

# Convert to DataFrame
df = pd.DataFrame(diff_table, index=perms, columns=perms)
# Loop through columns and show only actual repeated values
for col in abs_df.columns:
    col_vals = abs_df[col]
    duplicates = col_vals[col_vals.duplicated(keep=False)]
    
    if not duplicates.empty:
        print(f"\n🔁 Column {col} has repeated abs(diff) values:")
        print(duplicates.sort_values())
