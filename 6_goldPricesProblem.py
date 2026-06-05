# two pointers
# {5, 1, 4, 3, 2, 7}
# gold prices problem
# {15, 2, 3, 1, 7, 11, 8}   ->  B:1, S: 11, P: 10
# {9, 4, 9, 3, 1, 3, 2}     ->  B:4, S: 9, P: 5

arr = [15, 2, 3, 1, 7, 11, 8]
arrlen = len(arr)

maxProfit = 0
minValue = arr[0]
for i in range(arrlen):
    if arr[i] < minValue:
        minValue = arr[i]
        
    profit = arr[i] - minValue
    if profit > maxProfit:
        maxProfit = profit
        
print(f"Max profit = {maxProfit}")