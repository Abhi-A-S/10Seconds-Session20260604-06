## Excel Pattern
## 1 -> A
## 2 -> B
## 26 -> Z
## 27 -> AA
## 28 -> AB
## 52 -> AZ
## 53 -> BA

n = 28

resultStr = ''

while n > 0:
    rem = (n - 1) % 26
    asciiValue = ord('A') + rem
    resultStr = chr(asciiValue) + resultStr
    n = (n - 1) - 26

print(resultStr)