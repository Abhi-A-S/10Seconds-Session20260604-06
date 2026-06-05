# Sliding Window Technique

# {7, 5, 3 ,9, 4, 6}
# Sub Array Size = 3
# Max Sub Array Sum in Main Array

# 7 5 3 -> 15
# 5 3 9 -> Incoming: 9  Out Going Value: 7 | 15 + 9 - 7 = 17
# 3 9 4 -> Incoming: 4  Out Going Value: 3 | 17 + 4 - 5 = 16
# 9 4 6 -> Incoming: 6  Out Going Value: 3 | 16 + 6 - 3 = 19
# Max : 19
#

arr = [7, 5, 3, 9, 4, 6]
arrlen = len(arr)
k = 3

# Initial window sum
windowSum = 0
for i in range(k):
    windowSum += arr[i]
maxSum = windowSum

for j in range(k, arrlen):
    windowSum += arr[j] - arr[j - k]
    if windowSum > maxSum:
        maxSum = windowSum

print(f" Max Sum of Sub array: {maxSum}")