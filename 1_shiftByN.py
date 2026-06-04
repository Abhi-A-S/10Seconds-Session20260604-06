###
# [10, 20, 30, 40, 50]
# [50, 10, 20, 30, 40] | n = 1
# [40, 50, 10, 20, 30] | n = 2
# [50, 10, 20, 30, 40] | n = 156
#

data = [10, 20, 30, 40, 50]
datalen = len(data)

n = 143
n = n % datalen

# 1 shift
for x in range(n):
    last = data[-1]
    
    for i in range(datalen - 1, -1, -1):
        data[i] = data[i - 1]
        
    data[0] = last