# 1 1 1 -----------> 3
# 8 9 6 8
#   6 5 6 (+)
# 9 6 2 4


n1 = 8968
n2 = 656

carryCount = 0
carryFlag = 0

while n1 != 0 or n2 != 0:
    last1 = n1 % 10
    last2 = n2 % 10
    
    sumLast = last1 + last2 + carryFlag
    
    if sumLast > 9:
        carryCount += 1
        carryFlag = 1
    else:
        carryFlag
        
    n1 = n1 // 10
    n2 = n2 // 10
    
print(f"Carry Count : {carryCount}")