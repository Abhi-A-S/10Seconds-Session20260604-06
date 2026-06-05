# Remove Duplicates from Sorted Array
# O(n)
# {1, 2, 2, 3}

# sp = 0 | fp = 1
# compare value of Fp and Sp
# if Fp != Sp
# increment slow pointer by 1
# update Slow pointer Value with Fast pointer Value

# sp = 1 | fp = 1
# {1, 2, 2, 3}

# sp = 1 | fp = 2

# sp = 1 | fp = 3
# sp = 2 | fp = 3
# {1, 2, 3, 3}

arr = [1, 2, 2, 3]
arrlen = len(arr)

sp = 0
for fp in range(arrlen):
    if arr[fp] != arr[sp]:
        sp += 1
        arr[sp] = arr [fp]
        
print([arr[x] for x in range(sp + 1)])