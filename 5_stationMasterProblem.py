# n = 6
# arr: {900, 940, 950, 1100, 1500, 1800}
# dep: {910, 1200, 1120, 1130, 1900, 2000}
# min platform required ?

n = 6

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

i = 0
j = 0

platform = 0
minPlatform = 0

while i < n and j < n:
    if arr[i] < dep[j]:
        platform += 1
        i += 1
        
        if platform > minPlatform:
            minPlatform = platform
    else:
        platform -= 1
        j += 1
        
print(f"Min platforms: {minPlatform}")