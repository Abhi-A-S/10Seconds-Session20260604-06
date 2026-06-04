### SBIVM
### Encryption Key = 1
### Decryption Key = -1
### RAHUL

name = "SBIVM"
key = -1

finalDecryptedString = ''
for ch in name:
    shifted = (ord(ch) - ord('A') + key) % 26
    resultchar = ord('A') + shifted
    finalDecryptedString += chr(resultchar)
    
print(finalDecryptedString)