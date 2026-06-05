# Greedy Technique
# value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
# symbols = [M, CM, D, CD, C, XC, L, XL, X, IX, V, IV, I]

# 45 -> XLV
# 13 -> XIII
# 3000 -> MMM

values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

valueLen = len(values)
inputValue = 45

finalString = ""
for i in range(valueLen):
    while inputValue >= values[i]:
        finalString += symbols[i]
        inputValue -= values[i]
        
print(finalString)